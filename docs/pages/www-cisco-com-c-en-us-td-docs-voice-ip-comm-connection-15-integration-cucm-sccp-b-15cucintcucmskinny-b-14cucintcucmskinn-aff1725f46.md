---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-integration-cucm-sccp-b-15cucintcucmskinny-b-14cucintcucmskinn-aff1725f46
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/integration/cucm_sccp/b_15cucintcucmskinny/b_14cucintcucmskinny_chapter_010.html
retrieved_at: 2026-08-16T18:28:59.704725+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Setting Up a Cisco Unified
	 Communications Manager SCCP Integration

## Chapter: Setting Up a Cisco Unified
	 Communications Manager SCCP Integration

# Setting Up a Cisco Unified
                     	 Communications Manager SCCP Integration

## Setting Up a Cisco Unified
                        	 Communications Manager SCCP Integration

### Introduction

This chapter provides instructions for setting up SCCP Integration between Cisco Unified Communications Manager and Cisco Unity
                              Connection.

If you are configuring MWI relay across trunks in a distributed phone system, you must see the Cisco Unified CM documentation
                                          for requirements and instructions. Configuring MWI relay across trunks does not involve Unity Connection settings.

### Pre-requisites

Before starting the
                              		SCCP integration between Cisco Unified CM and Unity Connection, you need to
                              		understand the tasks to be done and the components required for the
                              		integration. Below Table
                                 		  3-1 contains a list of pre-requisites that you must consider to ensure a
                              		successful integration.

For
                                                						  compatible version of Cisco Unified CM, see the Compatibility Matrix:
                                                   							 Cisco Unity Connection at Setting Up a Cisco Unified Communications Manager SCCP Integration .

- For details on compatible
                                             						versions of Unity Connection, see the Compatibility Matrix for Cisco Unity
                                             						Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html .

- For details on installation tasks, see the “Installing Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection , Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html

Only
                                                   						  IP phones for the Cisco Unified CM extensions.

Both
                                                   						  IP phones and SIP phones for the Cisco Unified CM extensions without a media
                                                   						  termination point (MTP) on the Cisco Unified CM server.

A LAN
                                                						  connection in each location is required where you plug the applicable phone
                                                						  into the network.

For
                                                						  multiple Cisco Unified CM clusters, the capability for users to dial an
                                                						  extension on another Cisco Unified CM cluster without dialing a trunk access
                                                						  code or prefix.

If Unity
                                          					 Connection uses IPv6 or dual-mode (IPv4 and IPv6) to communicate with Cisco
                                          					 Unified CM, do the following subtasks:

Enable
                                                						  IPv6 on the Unity Connection server.

In
                                                						  Cisco Unity Connection Administration, on the System Settings > General Configuration page, select an
                                                						  option for IP Addressing Mode to control where Unity Connection listens for
                                                						  incoming traffic. You can select IPv4, IPv6, or IPv4 and IPv6. The setting
                                                						  defaults to IPv4.

See the “Ethernet IPv6 Configuration Settings” section in the “Security” chapter of the Cisco Unified Communications Operating
                                          System Administration Guide for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

### Integration
                           	 Tasks

The following task list describes the process for creating and
                              		changing the integration.

Review the system and hardware requirements to confirm that all
                                    			 phone system and Unity Connection server requirements have been met. See
                                    			 the“ Pre-requisites ”
                                    			 section on page 3-1

Plan and configure how the voice messaging ports are used by
                                    			 Unity Connection. See Planning
                                       				the Voice Messaging Ports

All the forwarded calls are routed to opening greeting instead
                                                				of subscriber greeting when Voice mail port, Voice mail pilot, and CTI route
                                                				point used for routing calls to Unity Connection are same as that of Phone DN
                                                				on call manager.

Program Cisco Unified CM. See the Programming
                                       				the Cisco Unified CallManager Phone System .

Create the integration. See the “ Creating
                                       				a New Integration with Cisco Unified CM .

An additional Cisco Unified CM cluster can be added by adding a
                                                				new phone system, port group, and ports. Each Cisco Unified CM cluster is a
                                                				separate phone system integration.

If this is the first integration, the first phone system is automatically selected in the default user template. The users
                                                   that you add after creating this phone system integration are assigned to this phone system by default. However, for each
                                                   subsequent integration add the applicable new user templates for the new phone system.For details on adding new user templates,
                                                   or on selecting a user template when adding a new user, see the “User Templates” section in “User Attributes” chapter of the
                                                   System Administration Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

### Programming the Cisco Unified CallManager Phone System

Do the following procedures for
                              		programming the Cisco Unified Communications Manager phone system integration
                              		with Unity Connection:

#### Adding Partitions
                              	 and a Calling Search Space for Voice Mail Ports

Step 1

In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Class of
                                                   				  Control > and select > Partition .

Step 2

On the Find and List Partitions page, select Add New .

Step 3

On the Partition Configuration page, enter the name and
                                             			 description you want for the partition that contains all voice mail port
                                             			 directory numbers. For example, enter “VMRestrictedPT, Partition for voice mail
                                             			 port directory numbers.”

Step 4

Select Save .

Step 5

Select Add New .

Step 6

Enter the name and description you want for the partition that
                                             			 contains the hunt pilot, which is the voice mail pilot number. For example,
                                             			 enter “VMPilotNumberPT, Partition for the voice mail pilot number.”

Step 7

Select Save .

Step 8

Expand Call
                                                   				  Routing > Class of
                                                   				  Control > and select > Calling Search
                                                   				  Space .

Step 9

On the Find and List Calling Search Spaces page, select Add New .

Step 10

On the Calling Search Space Configuration page, in the Name
                                             			 field, enter a name for the calling search space that includes the partition
                                             			 created in Step 2 through Step 4 . For example,
                                             			 enter “VMRestrictedCSS.”

Step 11

Optionally, in the Description field, enter a description of the
                                             			 calling search space. For example, enter “Voice mail port directory numbers.”

Step 12

In the Available Partitions list, select the name of the
                                             			 partition created in Step 2 through Step 4 . For example,
                                             			 select “VMRestrictedPT.”

Step 13

Select the down arrow below the Available Partitions list.

The name of the partition appears in the Selected Partitions
                                                				list.

Step 14

Select Save .

Step 15

In the Related Links field, select Back to Find/List and select Go .

Step 16

On the Find and List Calling Search Spaces page, select Find .

Step 17

Select the name of the calling search space that is used by user
                                             			 phones.

Step 18

On the Calling Search Space Configuration page, in the Available
                                             			 Partitions list, select the name of the partition created in Step 5 through Step 7 . For example,
                                             			 select “VMPilotNumberPT.”

If the partition that contains the hunt pilot (which is the
                                                				voice mail pilot number) is not in the calling search space that is used by
                                                				user phones, the phones are not able to dial the Unity Connection server.

Step 19

Select the down arrow below the Available Partition list.

The name of the partition appears in the Selected Partitions
                                                				list.

Step 20

Select Save .

Step 21

Repeat Step 17 through Step 20 for each
                                             			 remaining calling search space that needs to access Unity Connection.

#### Adding a Device Pool for the Voice Mail Ports

Step 1

In Cisco Unified CM Administration, select System > and then select > Device Pool .

Step 2

On the Find and List Device Pools page,
                                             			 select Add New .

Step 3

On the Device Pool Configuration page, enter
                                             			 the following device pool settings.

Field

Setting

Device Pool
                                                               							 Settings

Device Pool Name

Enter Unity Connection Voice Mail
                                                               							 Ports or other description for this device pool.

Cisco Unified Communications Manager
                                                            						  Group

Select the Cisco Unified
                                                            						  Communications Manager group to assign to the voice mail ports in this device
                                                            						  pool.

Roaming
                                                               							 Sensitive Settings

Date/Time Group

Select the date/time group to assign
                                                            						  to the voice mail ports in this device pool.

Region

Select the Cisco Unified CM region
                                                            						  to assign to the voice mail ports in this device pool.

SRST Reference

If applicable, select the survivable
                                                            						  remote site telephony (SRST) reference to assign to the voice mail ports in
                                                            						  this device pool.

Step 4

Select Save .

#### Adding the Voice
                              	 Mail Ports on Cisco Unified CM

Step 1

In Cisco Unified CM Administration, expand Advanced Features > Voice
                                                   				  Mail > and select > Cisco Voice Mail Port
                                                   				  Wizard .

Step 2

On the What Would You Like to Do page, select Create a New Cisco Voice Mail Server and Add Ports to
                                                				It , then select Next .

Step 3

On the Cisco
                                             			 Voice Mail Server page, the name of the voice mail server appears. We recommend
                                             			 that you accept the default name for the voice mail server. If you need to use
                                             			 a different name, however, the name must have no more than nine characters.

The voice mail server name must match the Device Name Prefix
                                                				field in Unity Connection on the Port Group Basics page for the voice messaging
                                                				ports, with -VI appended to the end of the name. For example, if the Device
                                                				Name Prefix in Cisco Unified CM is CiscoUM, the voice mail server name in Unity
                                                				Connection should be CiscoUM-VI.

Step 4

Select Next .

Step 5

On the Cisco Voice Mail Ports page, select the number of voice
                                             			 mail ports that you want to add (it should not be more voice mail ports than
                                             			 the Unity Connection licenses enable), then select Next .

For a Unity Connection cluster, first enter the number of voice
                                                				mail ports for the publisher and then for the subscriber, selecting the
                                                				appropriate server for each creation process.

If you integrate Unity Connection with multiple Cisco Unified CM
                                                				clusters, the number you enter here cannot bring the total number of ports on
                                                				all Cisco Unified CM clusters integrated with Unity Connection to more than the
                                                				number of ports enabled by the Unity Connection licenses.

Step 6

On the Cisco Voice Mail Device Information page, enter the
                                             			 following voice mail device settings.

Field

Setting

Description

Enter Cisco Voice Mail Port or another description for the voice mail device.

Device Pool

Select the name of the device pool you created for the voice
                                                            						  mail ports. For example, select Unity Connection Voice Mail Ports.

Calling Search Space

Select the name of a calling search space that allows calls to
                                                            						  the user phones and any required network devices.

This calling search space must include partitions that contain
                                                            						  all devices Cisco Unity Connection needs to access (for example, during call
                                                            						  transfers, message notifications, and MWI activations).

AAR Calling Search Space

Accept the default of None .

Location

Select Hub_None .

Device Security Mode

Select the security mode that you want to use for the voice mail
                                                            						  ports. For details on the settings for Cisco Unified CM authentication and
                                                            						  encryption of the voice mail ports, see Cisco
                                                               							 Unified Communications Manager Authentication and Encryption of Cisco Unity
                                                               							 Connection Voice Messaging Ports .

Use Trusted Relay Point

Accept the default setting, or select another setting.

Step 7

Select Next .

Step 8

On the Cisco Voice Mail Directory Numbers page, enter the
                                             			 following voice mail directory number settings.

Field

Setting

Beginning Directory Number

Enter the extension number of the first voice mail port.

Partition

Select the name of the partition that you set up for all voice
                                                            						  mail port directory numbers. For example, select “VMRestrictedPT.”

Calling Search Space

Select the name of a calling search space that you set up to
                                                            						  contain the partition with all voice mail port directory numbers, as set in Step 9 of the “ Adding Partitions and a calling Search Space to
                                                               							 Contain Search Space to Contain the Voice Mail Ports ” procedure on
                                                            						  page 3-3. For example, select “VMRestrictedCSS.”

Because this calling search space is not used by user phones,
                                                            						  users are not able to dial the voice mail ports. However, users can dial the
                                                            						  voice mail pilot number.

AAR Group

Select the automated alternate routing (AAR) group for the voice
                                                            						  mail ports. The AAR group provides the prefix digits that are used to route
                                                            						  calls that are otherwise blocked due to insufficient bandwidth. If you select None , no rerouting of
                                                            						  blocked calls attempted.

Internal Caller ID
                                                            						  Display

Accept the default of VoiceMail .

This text appears on the
                                                            						  phone when the pilot number is dialed.

Internal Caller ID
                                                            						  Display (ASCII Format)

Accept the default of VoiceMail .

This text appears on the
                                                            						  phone when the pilot number is dialed.

External Number Mask

Leave this field blank,
                                                            						  or specify the mask used to format caller ID information for external
                                                            						  (outbound) calls. The mask can contain up to 50 characters. Enter the literal
                                                            						  digits that you want to appear in the caller ID information, and enter X for each digit in
                                                            						  the directory number of the device.

Step 9

Select Next .

Step 10

On the Do You Want to Add These Directory Numbers to a Line
                                             			 Group page, select No, I Add Them
                                                				Later , and select Next .

Step 11

On the Ready to Add Cisco Voice Mail Ports page, confirm that
                                             			 the settings for the voice mail ports are correct, and select Finish .

If the settings are not correct, select Back and enter the correct settings.

#### Adding the
                              	 Answering Voice Mail Ports to a Line Group

Step 1

In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Route/Hunt > and
                                                   				  select > Line
                                                   				  Group .

Step 2

On the Find and List Line Groups page, select Add New .

This line group contain directory numbers for voice mail ports
                                                				that answers calls. Directory numbers for voice mail ports that only dial out
                                                				(for example, to set MWIs) must not be included in this line group.

For a Unity Connection cluster, the line group contains
                                                				directory numbers for voice mail ports that answer calls on all servers in the
                                                				Unity Connection cluster. Directory numbers for voice mail ports that only dial
                                                				out (for example, to set MWIs) on all servers in the Unity Connection cluster
                                                				must not be included in this line group.

Step 3

On the Line Group Configuration page, enter the following
                                             			 settings.

Field

Setting

Line Group Name

Enter Unity Connection Answering
                                                               							 Ports or another unique name for line groups.

RNA Reversion Timeout

Accept the default of 10 .

Distribution Algorithm

(Without a Unity Connection cluster) Select Longest Idle Time .

(With a Unity Connection cluster configured) Select Top Down .

No Answer

Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List .

Busy

Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List .

Not Available

Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List .

Step 4

Under Line Group Member Information, in the Partition list,
                                             			 select the name of the partition that you set up for all voice mail port
                                             			 directory numbers. For example, select “VMRestrictedPT.”

Step 5

Select Find .

Step 6

In the Available DN/Route Partition list, select the first
                                             			 directory number of a voice mail port that answer calls, and select Add to Line Group .

The directory numbers in the Selected DN/Route Partition list
                                                				must appear in numerical sequence with the lowest number on top. Otherwise, the
                                                				integration does not function correctly.

Step 7

Repeat Step 6 for all
                                             			 remaining directory numbers of voice mail ports that answers calls.

Do not include directory numbers of voice mail ports that only
                                                				dial out (for example, to set MWIs). Otherwise, the integration does not
                                                				function correctly.

Step 8

Select Save .

#### Adding the Line Group to a Hunt List

Step 1

In Cisco Unified CM Administration, expand Call Routing > Route/Hunt > and select > Hunt List .

Step 2

On the Find and List Hunt Lists page, select Add New .

Step 3

On the Hunt List Configuration page, enter
                                             			 the following settings for the hunt list.

Field

Setting

Name

Enter Unity Connection Answering
                                                               							 Ports or another unique name for the hunt list.

Description

Enter Unity Connection ports that answer
                                                               							 calls or another description.

Cisco Unified Communications Manager
                                                            						  Group

Select Default or the name of the
                                                            						  Cisco Unified Communications Manager group that you are using.

Enable This Hunt List

Check this check box.

For Voice Mail Usage

Check this check box.

Step 4

Select Save .

Step 5

Under Hunt List Member Information page,
                                             			 select Add Line Group .

Step 6

On the Hunt List Detail Configuration page,
                                             			 in the Line Group list, select the line group you created for the directory
                                             			 numbers of voice mail ports that answers calls, then select Save .

In the hunt list, do not include line groups
                                                				with voice mail ports that Unity Connection use to dial out. Otherwise, the
                                                				integration not function correctly.

Step 7

When alerted that the line group has been
                                             			 inserted, select OK .

Step 8

On the Hunt List Configuration page, select Reset .

Step 9

When asked to confirm resetting the hunt
                                             			 list, select Reset .

Step 10

When alerted that the hunt list has been
                                             			 reset, select Close .

#### Adding the Hunt
                              	 List to a Hunt Pilot Number

Step 1

In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Route/Hunt > and
                                                   				  select > Hunt
                                                   				  Pilot .

Step 2

On the Find and List Hunt Pilots page, select Add New .

Step 3

On the Hunt Pilot Configuration page, enter the following
                                             			 settings for the hunt pilot.

Field

Setting

Hunt Pilot

Enter the hunt pilot number for the voice mail ports. The hunt
                                                            						  pilot number must be different from the extension numbers of the voice mail
                                                            						  ports.

The hunt pilot number is the extension number that users enter
                                                            						  to listen to their voice messages.

Route Partition

Select the name of the partition that you set up for the voice
                                                            						  mail pilot number. For example, select “VMPilotNumberPT.”

Description

Enter Unity Connection Hunt
                                                               							 Pilot or another description.

Numbering Plan

Accept the default setting, or select the numbering plan that
                                                            						  you have set up for your system.

Route Filter

Select None , or select the
                                                            						  name of the route filter that you set up for your system.

MLPP Precedence

Accept the default setting, or select another setting.

Hunt List

Select the hunt list of voice mail ports that answer calls,
                                                            						  which you set up in the Adding the Line Group to a Hunt List .

Route Option

Select Route This Pattern .

Provide Outside Dial Tone

Uncheck the check box.

Step 4

Select Save .

#### Specifying the MWI Directory Numbers

Step 1

In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Message Waiting .

Step 2

On the Find and List Message Waiting Numbers
                                             			 page, select Add New .

Step 3

On the Message Waiting Configuration page,
                                             			 enter the following settings for turning MWIs on.

Field

Setting

Message Waiting Number

Enter the unique extension that
                                                            						  turns MWIs on.

Partition

Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.”

Description

Enter DN to turn MWIs on or another
                                                            						  description.

Message Waiting Indicator

Select On .

Calling Search Space

Select a calling search space that
                                                            						  is used by user phones.

Step 4

Select Save .

Step 5

Select Add New .

Step 6

Enter the following settings for turning
                                             			 MWIs off.

Field

Setting

Message Waiting Number

Enter the unique extension that
                                                            						  turns MWIs off.

Partition

Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.”

Description

Enter DN to turn MWIs off or another
                                                            						  description.

Message Waiting Indicator

Select Off .

Calling Search Space

Select a calling search space that
                                                            						  is used by user phones.

Step 7

Select Save .

#### Add a Voice Mail Pilot Number for the Voice Mail Ports

In the following procedure, you add the voice
                                    		  mail pilot number, which is the extension that you dial to listen to your voice
                                    		  messages. Your Cisco IP phone automatically dials the voice mail pilot number
                                    		  when you press the Messages button.

Step 1

In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Voice Mail Pilot .

Step 2

On the Find and List Voice Mail Pilots page,
                                             			 select Add New .

Step 3

On the Voice Mail Pilot Configuration page,
                                             			 enter the following voice mail pilot number settings.

Field

Setting

Voice Mail Pilot Number

Enter the voice mail pilot number
                                                            						  that users dial to listen to their voice messages. This number must be the same
                                                            						  as the hunt pilot number that you entered when adding voice mail ports earlier.

Calling Search Space

Select the calling search space that
                                                            						  includes partitions containing the user phones and the partition you set up for
                                                            						  the voice mail pilot number.

Description

Enter Cisco Unity Connection Pilot or another description.

Make This the Default Voice Mail
                                                            						  Pilot for the System

Check this check box. When this
                                                            						  check box is checked, this voice mail pilot number replaces the current default
                                                            						  pilot number.

Step 4

Select Save .

#### Setting Up the Voice Mail Profile

Step 1

In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Voice Mail Profile .

Step 2

On the Find and List Voice Mail Profiles
                                             			 page, select Add New .

Step 3

On the Voice Mail Profile Configuration
                                             			 page, enter the following voice mail profile settings.

Field

Setting

Voice Mail Profile Name

Enter a name to identify the voice
                                                            						  mail profile.

Description

Enter Unity Connection Profile or
                                                            						  another description.

Voice Mail Pilot

Select one of the following:

The applicable voice mail pilot
                                                                  								number that you defined on the Voice Mail Pilot Configuration page

Use
                                                                     								  Default

Voice Mail Box Mask

When multitenant services are not
                                                            						  enabled on Cisco Unified CM, leave this field blank.

When multitenant services are
                                                            						  enabled, each tenant uses its own voice mail profile and must create a mask to
                                                            						  identify the extensions (directory numbers) in each partition that is shared
                                                            						  with other tenants. For example, one tenant can use a mask 972813XXXX, while
                                                            						  another tenant can use the mask 214333XXXX. Each tenant also uses its own
                                                            						  translation patterns for MWIs.

Make This the Default Voice Mail
                                                            						  Profile for the System

Check this check box to make this
                                                            						  voice mail profile the default.

When this check box is checked, this
                                                            						  voice mail profile replaces the current default voice mail profile.

Step 4

Select Save .

#### Setting Up the Voice Mail Server Service Parameters

Step 1

In Cisco Unified CM Administration, select System > and then select > Service Parameters .

Step 2

On the Service Parameters Configuration
                                             			 page, in the Server field, select the name of the Cisco Unified CM server.

Step 3

In the Service list, select Cisco CallManager . The
                                             			 list of parameters appears.

Step 4

Under Clusterwide Parameters (Feature -
                                             			 General), locate the Multiple Tenant MWI Modes parameter.

Step 5

If you use multiple tenant MWI notification,
                                             			 select True .

When this parameter is set to True, Cisco
                                                				Unified CM uses any configured translation patterns to convert voice mail
                                                				extensions into directory numbers when turning on or off an MWI.

Step 6

If you changed any settings, select Save . Otherwise, skip
                                             			 the remaining steps in this procedure.

Step 7

In the Navigation drop-down box, select Cisco Unified
                                                				Serviceability and select Go .

Step 8

In Cisco Unified Serviceability, on the
                                             			 Tools menu, select Control Center - Feature
                                                				Services .

Step 9

Under CM Services, select Cisco CallManager and
                                             			 select Restart .

### Creating a New
                           	 Integration with Cisco Unified CM

After ensuring that Cisco Unified Communications Manager and
                                 		  Unity Connection are ready for the integration, do the following procedure to
                                 		  set up the integration and to enter the port settings.

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System .

Step 2

On the Search Phone Systems page, under Display Name, select the
                                          			 name of the default phone system.

Step 3

On the Phone System Basics page, in the Phone System Name field,
                                          			 enter the descriptive name that you want for the phone system.

Step 4

If you want to use this phone system as the default for TRaP
                                          			 connections so that administrators and users without voicemail boxes can record
                                          			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                          			 another phone system as the default for TRaP connections, uncheck this check
                                          			 box.

Step 5

Select Save .

Step 6

On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go .

Step 7

On the New Port Group page, enter the following settings and
                                          			 select Save .

Field

Setting

Phone System

Select the name of the phone system that you entered in Step 3 .

Create From

Select Port Group Template and
                                                         						  select SCCP in the drop-down
                                                         						  box.

Display Name

Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want.

Device Name Prefix

Enter the prefix that Cisco Unified CM adds to the device name
                                                         						  for voice ports. This prefix must match the prefix used by Cisco Unified CM.

MWI On Extension

Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs on.

MWI Off Extension

Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs off.

IPv4 Address or Host Name

Enter the IPv4 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection.

You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv6 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank.

If you use Cisco Unified CM authentication and encryption, enter
                                                         						  an IP address or host name in this field. The CTL file used for encryption
                                                         						  between Unity Connection and Cisco Unified CM requires an IPv4 address or host
                                                         						  name, even if you are otherwise using IPv6 addressing.

IPv6 Address or Host Name

Enter the IPv6 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection

You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv4 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank.

The IPv6 address should be in canonical textual representation
                                                         						  formats proposed by Internet Engineering Task Force in RFC5952 standard for
                                                         						  rendering IPv6 addresses in text. For more details on IPv6 formats, please
                                                         						  refer the link https://tools.ietf.org/html/rfc5952#section-4

IP Address or Host Name

Enter the IP address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection.

Port

Enter the TCP port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting.

TLS Port

Enter the TLS port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting.

Step 8

On the Port Group Basics page, in the Related Links drop-down
                                          			 box, select Add Ports and select Go .

Step 9

On the New Port page, enter the following settings and select Save .

Field

Setting

Enabled

Check this check box.

Number of Ports

Enter the number of voice
                                                         						  messaging ports that you want to create in this port group.

Phone System

Select the name of the
                                                         						  phone system that you entered in Step
                                                            							 3 .

Port Group

Select the name of the
                                                         						  port group that you added in 7 .

Server

Select the name Unity
                                                         						  Connection server.

Security Mode

Select the Cisco
                                                         						  Unified CM security mode that you want to use for the voice messaging ports.

Step 10

On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration.

Step 11

On the Port Basics page, set the voice messaging port settings
                                          			 as applicable. The fields in the following table are the ones that you can
                                          			 change.

Field

Considerations

Enabled

Check this check box to
                                                         						  enable the port. The port is enabled during normal operation.

Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing.

Server

(For Unity Connection
                                                            							 clusters only) Select the name of the Unity Connection server that you want
                                                         						  to handle this port. For details, see Planning
                                                            							 the Voice Messaging Ports

Answer Calls

Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users.

Perform Message
                                                         						  Notification

Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports.

Send MWI Requests

Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports.

Allow TRAP Connections

Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports.

Outgoing Hunt Order

Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest.

Security Mode

Select the applicable
                                                         						  security mode:

Non-secure —The
                                                               								integrity and privacy of call-signaling messages is not ensured because
                                                               								call-signaling messages are sent as clear (unencrypted) text and connected to
                                                               								Cisco Unified CM through a non-authenticated port rather than an authenticated
                                                               								TLS port. In addition, the media stream is not encrypted.

Authenticated —The
                                                               								integrity of call-signaling messages is ensured because they are connected to
                                                               								Cisco Unified CM through an authenticated TLS port. However, the privacy of
                                                               								call-signaling messages is not ensured because they are sent as clear
                                                               								(unencrypted) text. In addition, the media stream is not encrypted.

Encrypted —The
                                                               								integrity and privacy of call-signaling messages is ensured on this port
                                                               								because they are connected to Cisco Unified CM through an authenticated TLS
                                                               								port, and the call-signaling messages are encrypted. In addition, the media
                                                               								stream is encrypted.

Caution

The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail.

The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates.

Step 12

Select Save .

Step 13

Select Next .

Step 14

Repeat Step 11 through 13 for all remaining voice messaging ports for the phone system.

Step 15

If Cisco Unity Connection does not connect to an AXL server,
                                          			 skip to Step 28 .
                                          			 Otherwise, expand Telephony
                                             				Integrations , then select Phone System .

Step 16

On the Search Phone Systems page, select the display name of the
                                          			 phone system that you created in 3 .

Step 17

On the Phone System Basics page, in the Edit menu, select Cisco Unified
                                             				Communications Manager AXL Servers .

Connecting to an AXL server is needed when Cisco Unity
                                             				Connection must have access to the Cisco Unified CM database for importing
                                             				Cisco Unified CM users and for changing certain phone settings for users of
                                             				Cisco Unity Connection personal call transfer rules.

If you plan to import Cisco Unified CM users, confirm that the
                                                         				  Primary Extension field on the End User Configuration page for each user is
                                                         				  filled in. Otherwise, the search does not find any users to select for
                                                         				  importing.

Step 18

On the Edit AXL Servers page, under AXL Servers, select Add New .

Step 19

Enter the following settings for the AXL server and select Save .

Field

Setting

Order

Enter the order of
                                                         						  priority for the AXL server. The lowest number is the primary AXL server, the
                                                         						  higher numbers are the secondary servers.

IP Address

Enter the IP address of
                                                         						  the AXL server.

Port

Enter the AXL server port
                                                         						  that Unity Connection connects to. This setting must match the port that the
                                                         						  AXL server uses.

Step 20

Repeat 18 and 19 for all remaining AXL servers.

Step 21

Under AXL Server Settings, enter the following settings and
                                          			 select Save .

Field

Setting

Username

Enter the username that
                                                         						  Unity Connection uses to sign in to the AXL server.

This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role.

Password

Enter the password for
                                                         						  the user that Unity Connection uses to sign in to the AXL server.

This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field.

Cisco Unified Communications Manager Version

Select the applicable setting that accurately describes the
                                                         						  following:

The version of Cisco Unified CM that you are integrating with
                                                               								Unity Connection.

Whether the AXL port is enabled for SSL.

If
                                                         						  you select the non-SSL version, the AXL port must be a non-SSL port (typically
                                                         						  port 80). If you select the SSL-enabled version, the AXL port must be an
                                                         						  SSL-enabled port (typically port 443 or port 8443).

Enable End User PIN Synchronization for Primary AXL Server

Check this check box to enable PIN synchronization between Unity
                                                         						  Connection and Cisco Unified CM for the users having same user ID (alias in
                                                         						  Unity Connection).

After enabling the feature whenever user updates the PIN on
                                                         						  Cisco Unity Connection, the PIN gets synchronized with Cisco Unified CM and
                                                         						  vice-versa.

Default setting: Check box is not checked.

For more information on PIN Synchronization, see the " PIN Synchronization between Unity Connection and Cisco Unified CM " section of the "User Settings" chapter of the System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

Ignore Certificate Errors

Check the check box to ignore certificate validation errors for
                                                         						  AXL Servers. When the check box is unchecked, Unity Connection validates the
                                                         						  certificate for the AXL servers. However, before checking the checkbox make
                                                         						  sure that the tomcat root certificate of Cisco Unified CM must be uploaded to
                                                         						  tomcat trust of Unity Connection server.

Default setting: Check box is checked.

For more information on certificates, see “ Security ” chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx.html .

Step 22

To add a corresponding application server to Cisco Unified CM,
                                          			 sign in to Cisco Unified CM Administration.

Step 23

In Cisco Unified CM Administration, navigate to System >
                                          			 Application Server page.

Step 24

On the Find and List Application Servers page, select Find to
                                          			 display all application servers.

Step 25

In the Name column, select the name of the Cisco Unity
                                          			 Connection server.

Step 26

On the Application Server Configuration page, in the Available
                                          			 Application User field, select the Cisco Unified CM application user that you
                                          			 used in 21 and select the down arrow to
                                          			 move it to the Selected Application User field.

Step 27

Select Save.

Step 28

In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Port Group .

Step 29

On the Search Port Groups page, select the display name of the
                                          			 port group that you created with the phone system integration in Step 7 .

By default, the display name for a port group is composed of the
                                                         				  phone system display name followed by an incrementing number.

Step 30

On the Port Group Basics page, on the Edit menu, select Servers .

Step 31

On the Edit Servers page, do the following substeps if the Cisco
                                          			 Unified CM cluster has secondary servers. Otherwise, skip to 32 .

Under Cisco Unified Communications Manager Servers, select Add .

Enter the following settings for the secondary Cisco Unified CM
                                                				  server and select Save .

Field

Setting

Order

Enter the order of
                                                               								priority for the Cisco Unified CM server. The lowest number is the primary
                                                               								Cisco Unified CM server, the higher numbers are the secondary servers.

IPv4 Address or Host Name

Enter the IPv4 address
                                                               								(or host name) of the secondary Cisco Unified CM server.

You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank.

IPv6 Address or Host Name

Enter the IPv6 address
                                                               								(or host name) of the secondary Cisco Unified CM server.

You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank.

IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later.

IP Address or Host Name

Enter the IP address (or
                                                               								host name) of the secondary Cisco Unified CM server.

Port

Enter the TCP port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting.

TLS Port

Enter the TLS port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting.

Server Type

Select Cisco Unified
                                                                  								  Communications Manager .

Repeat 31 for all remaining Cisco Unified CM servers in the cluster.

Step 32

Do the following substeps if the Cisco Unified CM cluster uses
                                          			 authentication or encryption for the voice messaging ports.

Under TFTP Servers, select Add .

Enter the following settings for the TFTP server and select Save .

Field

Setting

Order

Enter the order of
                                                               								priority for the TFTP server. The lowest number is the primary TFTP server, the
                                                               								higher numbers are the secondary servers.

IPv4 Address or Host Name

Enter the IPv4 address
                                                               								(or host name) of the TFTP server.

You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank.

IPv6 Address or Host Name

Enter the IPv6 address
                                                               								(or host name) of the TFTP server.

You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank.

IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later.

IP Address or Host Name

Enter the IP address (or
                                                               								host name) of the TFTP server.

Repeat 32 for all remaining TFTP servers in the Cisco Unified CM cluster.

Step 33

If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to 37 .

Step 34

On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk .

Step 35

On the New Phone System Trunk page, enter the following settings
                                          			 for the phone system trunk and select Save .

Field

Setting

From Phone System

Select the display name
                                                         						  of the phone system that you are creating a trunk for.

To Phone System

Select the display name
                                                         						  of the previously existing phone system that the trunk connects to.

Trunk Access Code

Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system.

Step 36

Repeat 34 and 35 for all remaining phone system trunks that you want to create.

Step 37

In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings.

If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again.

Step 38

In the Task Execution Results window, select Close .

| Note | If you are configuring MWI relay across trunks in a distributed phone system, you must see the Cisco Unified CM documentation
                                          for requirements and instructions. Configuring MWI relay across trunks does not involve Unity Connection settings. |
|---|---|

| Pre-requisites | Important Notes |
|---|---|
| Install
                                       				  the applicable version of Cisco Unified CM. | For
                                                						  compatible version of Cisco Unified CM, see the Compatibility Matrix:
                                                   							 Cisco Unity Connection at Setting Up a Cisco Unified Communications Manager SCCP Integration . |
| Install
                                       				  the applicable version of Unity Connection with a license that enables the
                                       				  applicable number of voice messaging ports. | For details on compatible
                                             						versions of Unity Connection, see the Compatibility Matrix for Cisco Unity
                                             						Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-device-support-tables-list.html . For details on installation tasks, see the “Installing Cisco Unity Connection” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection , Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html |
| The
                                          					 supported Phone system for SCCP integration are: Only
                                                   						  IP phones for the Cisco Unified CM extensions. Both
                                                   						  IP phones and SIP phones for the Cisco Unified CM extensions without a media
                                                   						  termination point (MTP) on the Cisco Unified CM server. | A LAN
                                                						  connection in each location is required where you plug the applicable phone
                                                						  into the network. For
                                                						  multiple Cisco Unified CM clusters, the capability for users to dial an
                                                						  extension on another Cisco Unified CM cluster without dialing a trunk access
                                                						  code or prefix. |
| If Unity
                                          					 Connection uses IPv6 or dual-mode (IPv4 and IPv6) to communicate with Cisco
                                          					 Unified CM, do the following subtasks: Enable
                                                						  IPv6 on the Unity Connection server. In
                                                						  Cisco Unity Connection Administration, on the System Settings > General Configuration page, select an
                                                						  option for IP Addressing Mode to control where Unity Connection listens for
                                                						  incoming traffic. You can select IPv4, IPv6, or IPv4 and IPv6. The setting
                                                						  defaults to IPv4. | See the “Ethernet IPv6 Configuration Settings” section in the “Security” chapter of the Cisco Unified Communications Operating
                                          System Administration Guide for Cisco Unity Connection at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . |

| Note | All the forwarded calls are routed to opening greeting instead
                                                				of subscriber greeting when Voice mail port, Voice mail pilot, and CTI route
                                                				point used for routing calls to Unity Connection are same as that of Phone DN
                                                				on call manager. |
|---|---|

| Note | An additional Cisco Unified CM cluster can be added by adding a
                                                				new phone system, port group, and ports. Each Cisco Unified CM cluster is a
                                                				separate phone system integration. |
|---|---|

| Note | If this is the first integration, the first phone system is automatically selected in the default user template. The users
                                                   that you add after creating this phone system integration are assigned to this phone system by default. However, for each
                                                   subsequent integration add the applicable new user templates for the new phone system.For details on adding new user templates,
                                                   or on selecting a user template when adding a new user, see the “User Templates” section in “User Attributes” chapter of the
                                                   System Administration Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Step 1 | In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Class of
                                                   				  Control > and select > Partition . |
|---|---|
| Step 2 | On the Find and List Partitions page, select Add New . |
| Step 3 | On the Partition Configuration page, enter the name and
                                             			 description you want for the partition that contains all voice mail port
                                             			 directory numbers. For example, enter “VMRestrictedPT, Partition for voice mail
                                             			 port directory numbers.” |
| Step 4 | Select Save . |
| Step 5 | Select Add New . |
| Step 6 | Enter the name and description you want for the partition that
                                             			 contains the hunt pilot, which is the voice mail pilot number. For example,
                                             			 enter “VMPilotNumberPT, Partition for the voice mail pilot number.” |
| Step 7 | Select Save . |
| Step 8 | Expand Call
                                                   				  Routing > Class of
                                                   				  Control > and select > Calling Search
                                                   				  Space . |
| Step 9 | On the Find and List Calling Search Spaces page, select Add New . |
| Step 10 | On the Calling Search Space Configuration page, in the Name
                                             			 field, enter a name for the calling search space that includes the partition
                                             			 created in Step 2 through Step 4 . For example,
                                             			 enter “VMRestrictedCSS.” |
| Step 11 | Optionally, in the Description field, enter a description of the
                                             			 calling search space. For example, enter “Voice mail port directory numbers.” |
| Step 12 | In the Available Partitions list, select the name of the
                                             			 partition created in Step 2 through Step 4 . For example,
                                             			 select “VMRestrictedPT.” |
| Step 13 | Select the down arrow below the Available Partitions list. The name of the partition appears in the Selected Partitions
                                                				list. |
| Step 14 | Select Save . |
| Step 15 | In the Related Links field, select Back to Find/List and select Go . |
| Step 16 | On the Find and List Calling Search Spaces page, select Find . |
| Step 17 | Select the name of the calling search space that is used by user
                                             			 phones. |
| Step 18 | On the Calling Search Space Configuration page, in the Available
                                             			 Partitions list, select the name of the partition created in Step 5 through Step 7 . For example,
                                             			 select “VMPilotNumberPT.” If the partition that contains the hunt pilot (which is the
                                                				voice mail pilot number) is not in the calling search space that is used by
                                                				user phones, the phones are not able to dial the Unity Connection server. |
| Step 19 | Select the down arrow below the Available Partition list. The name of the partition appears in the Selected Partitions
                                                				list. |
| Step 20 | Select Save . |
| Step 21 | Repeat Step 17 through Step 20 for each
                                             			 remaining calling search space that needs to access Unity Connection. |

| Step 1 | In Cisco Unified CM Administration, select System > and then select > Device Pool . |
|---|---|
| Step 2 | On the Find and List Device Pools page,
                                             			 select Add New . |
| Step 3 | On the Device Pool Configuration page, enter
                                             			 the following device pool settings. Table 1. Settings for the Device Pool
                                                      				Configuration Page Field Setting Device Pool
                                                               							 Settings Device Pool Name Enter Unity Connection Voice Mail
                                                               							 Ports or other description for this device pool. Cisco Unified Communications Manager
                                                            						  Group Select the Cisco Unified
                                                            						  Communications Manager group to assign to the voice mail ports in this device
                                                            						  pool. Roaming
                                                               							 Sensitive Settings Date/Time Group Select the date/time group to assign
                                                            						  to the voice mail ports in this device pool. Region Select the Cisco Unified CM region
                                                            						  to assign to the voice mail ports in this device pool. SRST Reference If applicable, select the survivable
                                                            						  remote site telephony (SRST) reference to assign to the voice mail ports in
                                                            						  this device pool. | Field | Setting | Device Pool
                                                               							 Settings | Device Pool Name | Enter Unity Connection Voice Mail
                                                               							 Ports or other description for this device pool. | Cisco Unified Communications Manager
                                                            						  Group | Select the Cisco Unified
                                                            						  Communications Manager group to assign to the voice mail ports in this device
                                                            						  pool. | Roaming
                                                               							 Sensitive Settings | Date/Time Group | Select the date/time group to assign
                                                            						  to the voice mail ports in this device pool. | Region | Select the Cisco Unified CM region
                                                            						  to assign to the voice mail ports in this device pool. | SRST Reference | If applicable, select the survivable
                                                            						  remote site telephony (SRST) reference to assign to the voice mail ports in
                                                            						  this device pool. |
| Field | Setting |
| Device Pool
                                                               							 Settings |
| Device Pool Name | Enter Unity Connection Voice Mail
                                                               							 Ports or other description for this device pool. |
| Cisco Unified Communications Manager
                                                            						  Group | Select the Cisco Unified
                                                            						  Communications Manager group to assign to the voice mail ports in this device
                                                            						  pool. |
| Roaming
                                                               							 Sensitive Settings |
| Date/Time Group | Select the date/time group to assign
                                                            						  to the voice mail ports in this device pool. |
| Region | Select the Cisco Unified CM region
                                                            						  to assign to the voice mail ports in this device pool. |
| SRST Reference | If applicable, select the survivable
                                                            						  remote site telephony (SRST) reference to assign to the voice mail ports in
                                                            						  this device pool. |
| Step 4 | Select Save . |

| Field | Setting |
|---|---|
| Device Pool
                                                               							 Settings |
| Device Pool Name | Enter Unity Connection Voice Mail
                                                               							 Ports or other description for this device pool. |
| Cisco Unified Communications Manager
                                                            						  Group | Select the Cisco Unified
                                                            						  Communications Manager group to assign to the voice mail ports in this device
                                                            						  pool. |
| Roaming
                                                               							 Sensitive Settings |
| Date/Time Group | Select the date/time group to assign
                                                            						  to the voice mail ports in this device pool. |
| Region | Select the Cisco Unified CM region
                                                            						  to assign to the voice mail ports in this device pool. |
| SRST Reference | If applicable, select the survivable
                                                            						  remote site telephony (SRST) reference to assign to the voice mail ports in
                                                            						  this device pool. |

| Step 1 | In Cisco Unified CM Administration, expand Advanced Features > Voice
                                                   				  Mail > and select > Cisco Voice Mail Port
                                                   				  Wizard . |
|---|---|
| Step 2 | On the What Would You Like to Do page, select Create a New Cisco Voice Mail Server and Add Ports to
                                                				It , then select Next . |
| Step 3 | On the Cisco
                                             			 Voice Mail Server page, the name of the voice mail server appears. We recommend
                                             			 that you accept the default name for the voice mail server. If you need to use
                                             			 a different name, however, the name must have no more than nine characters. Note The voice
                                                         				mail server name must match the Device Name Prefix field in Cisco Unity
                                                         				Connection on the Port Group Basics page for the voice messaging ports. The voice mail server name must match the Device Name Prefix
                                                				field in Unity Connection on the Port Group Basics page for the voice messaging
                                                				ports, with -VI appended to the end of the name. For example, if the Device
                                                				Name Prefix in Cisco Unified CM is CiscoUM, the voice mail server name in Unity
                                                				Connection should be CiscoUM-VI. | Note | The voice
                                                         				mail server name must match the Device Name Prefix field in Cisco Unity
                                                         				Connection on the Port Group Basics page for the voice messaging ports. |
| Note | The voice
                                                         				mail server name must match the Device Name Prefix field in Cisco Unity
                                                         				Connection on the Port Group Basics page for the voice messaging ports. |
| Step 4 | Select Next . |
| Step 5 | On the Cisco Voice Mail Ports page, select the number of voice
                                             			 mail ports that you want to add (it should not be more voice mail ports than
                                             			 the Unity Connection licenses enable), then select Next . For a Unity Connection cluster, first enter the number of voice
                                                				mail ports for the publisher and then for the subscriber, selecting the
                                                				appropriate server for each creation process. If you integrate Unity Connection with multiple Cisco Unified CM
                                                				clusters, the number you enter here cannot bring the total number of ports on
                                                				all Cisco Unified CM clusters integrated with Unity Connection to more than the
                                                				number of ports enabled by the Unity Connection licenses. |
| Step 6 | On the Cisco Voice Mail Device Information page, enter the
                                             			 following voice mail device settings. Table 2. Settings for the Cisco Voice Mail Device Information
                                                      				Page Field Setting Description Enter Cisco Voice Mail Port or another description for the voice mail device. Device Pool Select the name of the device pool you created for the voice
                                                            						  mail ports. For example, select Unity Connection Voice Mail Ports. Calling Search Space Select the name of a calling search space that allows calls to
                                                            						  the user phones and any required network devices. This calling search space must include partitions that contain
                                                            						  all devices Cisco Unity Connection needs to access (for example, during call
                                                            						  transfers, message notifications, and MWI activations). AAR Calling Search Space Accept the default of None . Location Select Hub_None . Device Security Mode Select the security mode that you want to use for the voice mail
                                                            						  ports. For details on the settings for Cisco Unified CM authentication and
                                                            						  encryption of the voice mail ports, see Cisco
                                                               							 Unified Communications Manager Authentication and Encryption of Cisco Unity
                                                               							 Connection Voice Messaging Ports . Use Trusted Relay Point Accept the default setting, or select another setting. | Field | Setting | Description | Enter Cisco Voice Mail Port or another description for the voice mail device. | Device Pool | Select the name of the device pool you created for the voice
                                                            						  mail ports. For example, select Unity Connection Voice Mail Ports. | Calling Search Space | Select the name of a calling search space that allows calls to
                                                            						  the user phones and any required network devices. This calling search space must include partitions that contain
                                                            						  all devices Cisco Unity Connection needs to access (for example, during call
                                                            						  transfers, message notifications, and MWI activations). | AAR Calling Search Space | Accept the default of None . | Location | Select Hub_None . | Device Security Mode | Select the security mode that you want to use for the voice mail
                                                            						  ports. For details on the settings for Cisco Unified CM authentication and
                                                            						  encryption of the voice mail ports, see Cisco
                                                               							 Unified Communications Manager Authentication and Encryption of Cisco Unity
                                                               							 Connection Voice Messaging Ports . | Use Trusted Relay Point | Accept the default setting, or select another setting. |
| Field | Setting |
| Description | Enter Cisco Voice Mail Port or another description for the voice mail device. |
| Device Pool | Select the name of the device pool you created for the voice
                                                            						  mail ports. For example, select Unity Connection Voice Mail Ports. |
| Calling Search Space | Select the name of a calling search space that allows calls to
                                                            						  the user phones and any required network devices. This calling search space must include partitions that contain
                                                            						  all devices Cisco Unity Connection needs to access (for example, during call
                                                            						  transfers, message notifications, and MWI activations). |
| AAR Calling Search Space | Accept the default of None . |
| Location | Select Hub_None . |
| Device Security Mode | Select the security mode that you want to use for the voice mail
                                                            						  ports. For details on the settings for Cisco Unified CM authentication and
                                                            						  encryption of the voice mail ports, see Cisco
                                                               							 Unified Communications Manager Authentication and Encryption of Cisco Unity
                                                               							 Connection Voice Messaging Ports . |
| Use Trusted Relay Point | Accept the default setting, or select another setting. |
| Step 7 | Select Next . |
| Step 8 | On the Cisco Voice Mail Directory Numbers page, enter the
                                             			 following voice mail directory number settings. Table 3. Settings for the Cisco Voice Mail Directory Numbers Page Field Setting Beginning Directory Number Enter the extension number of the first voice mail port. Partition Select the name of the partition that you set up for all voice
                                                            						  mail port directory numbers. For example, select “VMRestrictedPT.” Calling Search Space Select the name of a calling search space that you set up to
                                                            						  contain the partition with all voice mail port directory numbers, as set in Step 9 of the “ Adding Partitions and a calling Search Space to
                                                               							 Contain Search Space to Contain the Voice Mail Ports ” procedure on
                                                            						  page 3-3. For example, select “VMRestrictedCSS.” Because this calling search space is not used by user phones,
                                                            						  users are not able to dial the voice mail ports. However, users can dial the
                                                            						  voice mail pilot number. AAR Group Select the automated alternate routing (AAR) group for the voice
                                                            						  mail ports. The AAR group provides the prefix digits that are used to route
                                                            						  calls that are otherwise blocked due to insufficient bandwidth. If you select None , no rerouting of
                                                            						  blocked calls attempted. Internal Caller ID
                                                            						  Display Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. Internal Caller ID
                                                            						  Display (ASCII Format) Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. External Number Mask Leave this field blank,
                                                            						  or specify the mask used to format caller ID information for external
                                                            						  (outbound) calls. The mask can contain up to 50 characters. Enter the literal
                                                            						  digits that you want to appear in the caller ID information, and enter X for each digit in
                                                            						  the directory number of the device. | Field | Setting | Beginning Directory Number | Enter the extension number of the first voice mail port. | Partition | Select the name of the partition that you set up for all voice
                                                            						  mail port directory numbers. For example, select “VMRestrictedPT.” | Calling Search Space | Select the name of a calling search space that you set up to
                                                            						  contain the partition with all voice mail port directory numbers, as set in Step 9 of the “ Adding Partitions and a calling Search Space to
                                                               							 Contain Search Space to Contain the Voice Mail Ports ” procedure on
                                                            						  page 3-3. For example, select “VMRestrictedCSS.” Because this calling search space is not used by user phones,
                                                            						  users are not able to dial the voice mail ports. However, users can dial the
                                                            						  voice mail pilot number. | AAR Group | Select the automated alternate routing (AAR) group for the voice
                                                            						  mail ports. The AAR group provides the prefix digits that are used to route
                                                            						  calls that are otherwise blocked due to insufficient bandwidth. If you select None , no rerouting of
                                                            						  blocked calls attempted. | Internal Caller ID
                                                            						  Display | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. | Internal Caller ID
                                                            						  Display (ASCII Format) | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. | External Number Mask | Leave this field blank,
                                                            						  or specify the mask used to format caller ID information for external
                                                            						  (outbound) calls. The mask can contain up to 50 characters. Enter the literal
                                                            						  digits that you want to appear in the caller ID information, and enter X for each digit in
                                                            						  the directory number of the device. |
| Field | Setting |
| Beginning Directory Number | Enter the extension number of the first voice mail port. |
| Partition | Select the name of the partition that you set up for all voice
                                                            						  mail port directory numbers. For example, select “VMRestrictedPT.” |
| Calling Search Space | Select the name of a calling search space that you set up to
                                                            						  contain the partition with all voice mail port directory numbers, as set in Step 9 of the “ Adding Partitions and a calling Search Space to
                                                               							 Contain Search Space to Contain the Voice Mail Ports ” procedure on
                                                            						  page 3-3. For example, select “VMRestrictedCSS.” Because this calling search space is not used by user phones,
                                                            						  users are not able to dial the voice mail ports. However, users can dial the
                                                            						  voice mail pilot number. |
| AAR Group | Select the automated alternate routing (AAR) group for the voice
                                                            						  mail ports. The AAR group provides the prefix digits that are used to route
                                                            						  calls that are otherwise blocked due to insufficient bandwidth. If you select None , no rerouting of
                                                            						  blocked calls attempted. |
| Internal Caller ID
                                                            						  Display | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. |
| Internal Caller ID
                                                            						  Display (ASCII Format) | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. |
| External Number Mask | Leave this field blank,
                                                            						  or specify the mask used to format caller ID information for external
                                                            						  (outbound) calls. The mask can contain up to 50 characters. Enter the literal
                                                            						  digits that you want to appear in the caller ID information, and enter X for each digit in
                                                            						  the directory number of the device. |
| Step 9 | Select Next . |
| Step 10 | On the Do You Want to Add These Directory Numbers to a Line
                                             			 Group page, select No, I Add Them
                                                				Later , and select Next . |
| Step 11 | On the Ready to Add Cisco Voice Mail Ports page, confirm that
                                             			 the settings for the voice mail ports are correct, and select Finish . If the settings are not correct, select Back and enter the correct settings. |

| Note | The voice
                                                         				mail server name must match the Device Name Prefix field in Cisco Unity
                                                         				Connection on the Port Group Basics page for the voice messaging ports. |
|---|---|

| Field | Setting |
|---|---|
| Description | Enter Cisco Voice Mail Port or another description for the voice mail device. |
| Device Pool | Select the name of the device pool you created for the voice
                                                            						  mail ports. For example, select Unity Connection Voice Mail Ports. |
| Calling Search Space | Select the name of a calling search space that allows calls to
                                                            						  the user phones and any required network devices. This calling search space must include partitions that contain
                                                            						  all devices Cisco Unity Connection needs to access (for example, during call
                                                            						  transfers, message notifications, and MWI activations). |
| AAR Calling Search Space | Accept the default of None . |
| Location | Select Hub_None . |
| Device Security Mode | Select the security mode that you want to use for the voice mail
                                                            						  ports. For details on the settings for Cisco Unified CM authentication and
                                                            						  encryption of the voice mail ports, see Cisco
                                                               							 Unified Communications Manager Authentication and Encryption of Cisco Unity
                                                               							 Connection Voice Messaging Ports . |
| Use Trusted Relay Point | Accept the default setting, or select another setting. |

| Field | Setting |
|---|---|
| Beginning Directory Number | Enter the extension number of the first voice mail port. |
| Partition | Select the name of the partition that you set up for all voice
                                                            						  mail port directory numbers. For example, select “VMRestrictedPT.” |
| Calling Search Space | Select the name of a calling search space that you set up to
                                                            						  contain the partition with all voice mail port directory numbers, as set in Step 9 of the “ Adding Partitions and a calling Search Space to
                                                               							 Contain Search Space to Contain the Voice Mail Ports ” procedure on
                                                            						  page 3-3. For example, select “VMRestrictedCSS.” Because this calling search space is not used by user phones,
                                                            						  users are not able to dial the voice mail ports. However, users can dial the
                                                            						  voice mail pilot number. |
| AAR Group | Select the automated alternate routing (AAR) group for the voice
                                                            						  mail ports. The AAR group provides the prefix digits that are used to route
                                                            						  calls that are otherwise blocked due to insufficient bandwidth. If you select None , no rerouting of
                                                            						  blocked calls attempted. |
| Internal Caller ID
                                                            						  Display | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. |
| Internal Caller ID
                                                            						  Display (ASCII Format) | Accept the default of VoiceMail . This text appears on the
                                                            						  phone when the pilot number is dialed. |
| External Number Mask | Leave this field blank,
                                                            						  or specify the mask used to format caller ID information for external
                                                            						  (outbound) calls. The mask can contain up to 50 characters. Enter the literal
                                                            						  digits that you want to appear in the caller ID information, and enter X for each digit in
                                                            						  the directory number of the device. |

| Step 1 | In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Route/Hunt > and
                                                   				  select > Line
                                                   				  Group . |
|---|---|
| Step 2 | On the Find and List Line Groups page, select Add New . This line group contain directory numbers for voice mail ports
                                                				that answers calls. Directory numbers for voice mail ports that only dial out
                                                				(for example, to set MWIs) must not be included in this line group. For a Unity Connection cluster, the line group contains
                                                				directory numbers for voice mail ports that answer calls on all servers in the
                                                				Unity Connection cluster. Directory numbers for voice mail ports that only dial
                                                				out (for example, to set MWIs) on all servers in the Unity Connection cluster
                                                				must not be included in this line group. |
| Step 3 | On the Line Group Configuration page, enter the following
                                             			 settings. Table 4. Settings for the Line Group Configuration Page for Answering
                                                      				Ports Field Setting Line Group Name Enter Unity Connection Answering
                                                               							 Ports or another unique name for line groups. RNA Reversion Timeout Accept the default of 10 . Distribution Algorithm (Without a Unity Connection cluster) Select Longest Idle Time . (With a Unity Connection cluster configured) Select Top Down . No Answer Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . Busy Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . Not Available Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . | Field | Setting | Line Group Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for line groups. | RNA Reversion Timeout | Accept the default of 10 . | Distribution Algorithm | (Without a Unity Connection cluster) Select Longest Idle Time . (With a Unity Connection cluster configured) Select Top Down . | No Answer | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . | Busy | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . | Not Available | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Field | Setting |
| Line Group Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for line groups. |
| RNA Reversion Timeout | Accept the default of 10 . |
| Distribution Algorithm | (Without a Unity Connection cluster) Select Longest Idle Time . (With a Unity Connection cluster configured) Select Top Down . |
| No Answer | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Busy | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Not Available | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Step 4 | Under Line Group Member Information, in the Partition list,
                                             			 select the name of the partition that you set up for all voice mail port
                                             			 directory numbers. For example, select “VMRestrictedPT.” |
| Step 5 | Select Find . |
| Step 6 | In the Available DN/Route Partition list, select the first
                                             			 directory number of a voice mail port that answer calls, and select Add to Line Group . The directory numbers in the Selected DN/Route Partition list
                                                				must appear in numerical sequence with the lowest number on top. Otherwise, the
                                                				integration does not function correctly. |
| Step 7 | Repeat Step 6 for all
                                             			 remaining directory numbers of voice mail ports that answers calls. Do not include directory numbers of voice mail ports that only
                                                				dial out (for example, to set MWIs). Otherwise, the integration does not
                                                				function correctly. |
| Step 8 | Select Save . |

| Field | Setting |
|---|---|
| Line Group Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for line groups. |
| RNA Reversion Timeout | Accept the default of 10 . |
| Distribution Algorithm | (Without a Unity Connection cluster) Select Longest Idle Time . (With a Unity Connection cluster configured) Select Top Down . |
| No Answer | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Busy | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |
| Not Available | Accept the default of Try Next Member; Then, Try
                                                               							 Next Group in Hunt List . |

| Step 1 | In Cisco Unified CM Administration, expand Call Routing > Route/Hunt > and select > Hunt List . |
|---|---|
| Step 2 | On the Find and List Hunt Lists page, select Add New . |
| Step 3 | On the Hunt List Configuration page, enter
                                             			 the following settings for the hunt list. Table 5. Settings for the Hunt List Configuration
                                                      				Page for Answering Ports Field Setting Name Enter Unity Connection Answering
                                                               							 Ports or another unique name for the hunt list. Description Enter Unity Connection ports that answer
                                                               							 calls or another description. Cisco Unified Communications Manager
                                                            						  Group Select Default or the name of the
                                                            						  Cisco Unified Communications Manager group that you are using. Enable This Hunt List Check this check box. For Voice Mail Usage Check this check box. | Field | Setting | Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for the hunt list. | Description | Enter Unity Connection ports that answer
                                                               							 calls or another description. | Cisco Unified Communications Manager
                                                            						  Group | Select Default or the name of the
                                                            						  Cisco Unified Communications Manager group that you are using. | Enable This Hunt List | Check this check box. | For Voice Mail Usage | Check this check box. |
| Field | Setting |
| Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for the hunt list. |
| Description | Enter Unity Connection ports that answer
                                                               							 calls or another description. |
| Cisco Unified Communications Manager
                                                            						  Group | Select Default or the name of the
                                                            						  Cisco Unified Communications Manager group that you are using. |
| Enable This Hunt List | Check this check box. |
| For Voice Mail Usage | Check this check box. |
| Step 4 | Select Save . |
| Step 5 | Under Hunt List Member Information page,
                                             			 select Add Line Group . |
| Step 6 | On the Hunt List Detail Configuration page,
                                             			 in the Line Group list, select the line group you created for the directory
                                             			 numbers of voice mail ports that answers calls, then select Save . In the hunt list, do not include line groups
                                                				with voice mail ports that Unity Connection use to dial out. Otherwise, the
                                                				integration not function correctly. |
| Step 7 | When alerted that the line group has been
                                             			 inserted, select OK . |
| Step 8 | On the Hunt List Configuration page, select Reset . |
| Step 9 | When asked to confirm resetting the hunt
                                             			 list, select Reset . |
| Step 10 | When alerted that the hunt list has been
                                             			 reset, select Close . |

| Field | Setting |
|---|---|
| Name | Enter Unity Connection Answering
                                                               							 Ports or another unique name for the hunt list. |
| Description | Enter Unity Connection ports that answer
                                                               							 calls or another description. |
| Cisco Unified Communications Manager
                                                            						  Group | Select Default or the name of the
                                                            						  Cisco Unified Communications Manager group that you are using. |
| Enable This Hunt List | Check this check box. |
| For Voice Mail Usage | Check this check box. |

| Step 1 | In Cisco Unified CM Administration, expand Call
                                                   				  Routing > Route/Hunt > and
                                                   				  select > Hunt
                                                   				  Pilot . |
|---|---|
| Step 2 | On the Find and List Hunt Pilots page, select Add New . |
| Step 3 | On the Hunt Pilot Configuration page, enter the following
                                             			 settings for the hunt pilot. Table 6. Settings for Hunt Pilot Configuration Page Field Setting Hunt Pilot Enter the hunt pilot number for the voice mail ports. The hunt
                                                            						  pilot number must be different from the extension numbers of the voice mail
                                                            						  ports. The hunt pilot number is the extension number that users enter
                                                            						  to listen to their voice messages. Route Partition Select the name of the partition that you set up for the voice
                                                            						  mail pilot number. For example, select “VMPilotNumberPT.” Description Enter Unity Connection Hunt
                                                               							 Pilot or another description. Numbering Plan Accept the default setting, or select the numbering plan that
                                                            						  you have set up for your system. Route Filter Select None , or select the
                                                            						  name of the route filter that you set up for your system. MLPP Precedence Accept the default setting, or select another setting. Hunt List Select the hunt list of voice mail ports that answer calls,
                                                            						  which you set up in the Adding the Line Group to a Hunt List . Route Option Select Route This Pattern . Provide Outside Dial Tone Uncheck the check box. | Field | Setting | Hunt Pilot | Enter the hunt pilot number for the voice mail ports. The hunt
                                                            						  pilot number must be different from the extension numbers of the voice mail
                                                            						  ports. The hunt pilot number is the extension number that users enter
                                                            						  to listen to their voice messages. | Route Partition | Select the name of the partition that you set up for the voice
                                                            						  mail pilot number. For example, select “VMPilotNumberPT.” | Description | Enter Unity Connection Hunt
                                                               							 Pilot or another description. | Numbering Plan | Accept the default setting, or select the numbering plan that
                                                            						  you have set up for your system. | Route Filter | Select None , or select the
                                                            						  name of the route filter that you set up for your system. | MLPP Precedence | Accept the default setting, or select another setting. | Hunt List | Select the hunt list of voice mail ports that answer calls,
                                                            						  which you set up in the Adding the Line Group to a Hunt List . | Route Option | Select Route This Pattern . | Provide Outside Dial Tone | Uncheck the check box. |
| Field | Setting |
| Hunt Pilot | Enter the hunt pilot number for the voice mail ports. The hunt
                                                            						  pilot number must be different from the extension numbers of the voice mail
                                                            						  ports. The hunt pilot number is the extension number that users enter
                                                            						  to listen to their voice messages. |
| Route Partition | Select the name of the partition that you set up for the voice
                                                            						  mail pilot number. For example, select “VMPilotNumberPT.” |
| Description | Enter Unity Connection Hunt
                                                               							 Pilot or another description. |
| Numbering Plan | Accept the default setting, or select the numbering plan that
                                                            						  you have set up for your system. |
| Route Filter | Select None , or select the
                                                            						  name of the route filter that you set up for your system. |
| MLPP Precedence | Accept the default setting, or select another setting. |
| Hunt List | Select the hunt list of voice mail ports that answer calls,
                                                            						  which you set up in the Adding the Line Group to a Hunt List . |
| Route Option | Select Route This Pattern . |
| Provide Outside Dial Tone | Uncheck the check box. |
| Step 4 | Select Save . |

| Field | Setting |
|---|---|
| Hunt Pilot | Enter the hunt pilot number for the voice mail ports. The hunt
                                                            						  pilot number must be different from the extension numbers of the voice mail
                                                            						  ports. The hunt pilot number is the extension number that users enter
                                                            						  to listen to their voice messages. |
| Route Partition | Select the name of the partition that you set up for the voice
                                                            						  mail pilot number. For example, select “VMPilotNumberPT.” |
| Description | Enter Unity Connection Hunt
                                                               							 Pilot or another description. |
| Numbering Plan | Accept the default setting, or select the numbering plan that
                                                            						  you have set up for your system. |
| Route Filter | Select None , or select the
                                                            						  name of the route filter that you set up for your system. |
| MLPP Precedence | Accept the default setting, or select another setting. |
| Hunt List | Select the hunt list of voice mail ports that answer calls,
                                                            						  which you set up in the Adding the Line Group to a Hunt List . |
| Route Option | Select Route This Pattern . |
| Provide Outside Dial Tone | Uncheck the check box. |

| Step 1 | In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Message Waiting . |
|---|---|
| Step 2 | On the Find and List Message Waiting Numbers
                                             			 page, select Add New . |
| Step 3 | On the Message Waiting Configuration page,
                                             			 enter the following settings for turning MWIs on. Table 7. Settings for Turning MWIs On Field Setting Message Waiting Number Enter the unique extension that
                                                            						  turns MWIs on. Partition Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” Description Enter DN to turn MWIs on or another
                                                            						  description. Message Waiting Indicator Select On . Calling Search Space Select a calling search space that
                                                            						  is used by user phones. | Field | Setting | Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs on. | Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” | Description | Enter DN to turn MWIs on or another
                                                            						  description. | Message Waiting Indicator | Select On . | Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |
| Field | Setting |
| Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs on. |
| Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” |
| Description | Enter DN to turn MWIs on or another
                                                            						  description. |
| Message Waiting Indicator | Select On . |
| Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |
| Step 4 | Select Save . |
| Step 5 | Select Add New . |
| Step 6 | Enter the following settings for turning
                                             			 MWIs off. Table 8. Settings for Turning MWIs Off Field Setting Message Waiting Number Enter the unique extension that
                                                            						  turns MWIs off. Partition Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” Description Enter DN to turn MWIs off or another
                                                            						  description. Message Waiting Indicator Select Off . Calling Search Space Select a calling search space that
                                                            						  is used by user phones. | Field | Setting | Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs off. | Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” | Description | Enter DN to turn MWIs off or another
                                                            						  description. | Message Waiting Indicator | Select Off . | Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |
| Field | Setting |
| Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs off. |
| Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” |
| Description | Enter DN to turn MWIs off or another
                                                            						  description. |
| Message Waiting Indicator | Select Off . |
| Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |
| Step 7 | Select Save . |

| Field | Setting |
|---|---|
| Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs on. |
| Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” |
| Description | Enter DN to turn MWIs on or another
                                                            						  description. |
| Message Waiting Indicator | Select On . |
| Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |

| Field | Setting |
|---|---|
| Message Waiting Number | Enter the unique extension that
                                                            						  turns MWIs off. |
| Partition | Select the name of the partition
                                                            						  that you set up for the voice mail pilot number. For example, select
                                                            						  “VMPilotNumberPT.” |
| Description | Enter DN to turn MWIs off or another
                                                            						  description. |
| Message Waiting Indicator | Select Off . |
| Calling Search Space | Select a calling search space that
                                                            						  is used by user phones. |

| Step 1 | In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Voice Mail Pilot . |
|---|---|
| Step 2 | On the Find and List Voice Mail Pilots page,
                                             			 select Add New . |
| Step 3 | On the Voice Mail Pilot Configuration page,
                                             			 enter the following voice mail pilot number settings. Table 9. Settings for the Voice Mail Pilot
                                                      				Configuration Page Field Setting Voice Mail Pilot Number Enter the voice mail pilot number
                                                            						  that users dial to listen to their voice messages. This number must be the same
                                                            						  as the hunt pilot number that you entered when adding voice mail ports earlier. Calling Search Space Select the calling search space that
                                                            						  includes partitions containing the user phones and the partition you set up for
                                                            						  the voice mail pilot number. Description Enter Cisco Unity Connection Pilot or another description. Make This the Default Voice Mail
                                                            						  Pilot for the System Check this check box. When this
                                                            						  check box is checked, this voice mail pilot number replaces the current default
                                                            						  pilot number. | Field | Setting | Voice Mail Pilot Number | Enter the voice mail pilot number
                                                            						  that users dial to listen to their voice messages. This number must be the same
                                                            						  as the hunt pilot number that you entered when adding voice mail ports earlier. | Calling Search Space | Select the calling search space that
                                                            						  includes partitions containing the user phones and the partition you set up for
                                                            						  the voice mail pilot number. | Description | Enter Cisco Unity Connection Pilot or another description. | Make This the Default Voice Mail
                                                            						  Pilot for the System | Check this check box. When this
                                                            						  check box is checked, this voice mail pilot number replaces the current default
                                                            						  pilot number. |
| Field | Setting |
| Voice Mail Pilot Number | Enter the voice mail pilot number
                                                            						  that users dial to listen to their voice messages. This number must be the same
                                                            						  as the hunt pilot number that you entered when adding voice mail ports earlier. |
| Calling Search Space | Select the calling search space that
                                                            						  includes partitions containing the user phones and the partition you set up for
                                                            						  the voice mail pilot number. |
| Description | Enter Cisco Unity Connection Pilot or another description. |
| Make This the Default Voice Mail
                                                            						  Pilot for the System | Check this check box. When this
                                                            						  check box is checked, this voice mail pilot number replaces the current default
                                                            						  pilot number. |
| Step 4 | Select Save . |

| Field | Setting |
|---|---|
| Voice Mail Pilot Number | Enter the voice mail pilot number
                                                            						  that users dial to listen to their voice messages. This number must be the same
                                                            						  as the hunt pilot number that you entered when adding voice mail ports earlier. |
| Calling Search Space | Select the calling search space that
                                                            						  includes partitions containing the user phones and the partition you set up for
                                                            						  the voice mail pilot number. |
| Description | Enter Cisco Unity Connection Pilot or another description. |
| Make This the Default Voice Mail
                                                            						  Pilot for the System | Check this check box. When this
                                                            						  check box is checked, this voice mail pilot number replaces the current default
                                                            						  pilot number. |

| Step 1 | In Cisco Unified CM Administration, expand Advanced Features > Voice Mail > and select > Voice Mail Profile . |
|---|---|
| Step 2 | On the Find and List Voice Mail Profiles
                                             			 page, select Add New . |
| Step 3 | On the Voice Mail Profile Configuration
                                             			 page, enter the following voice mail profile settings. Table 10. Settings for the Voice Mail Profile
                                                      				Configuration Page Field Setting Voice Mail Profile Name Enter a name to identify the voice
                                                            						  mail profile. Description Enter Unity Connection Profile or
                                                            						  another description. Voice Mail Pilot Select one of the following: The applicable voice mail pilot
                                                                  								number that you defined on the Voice Mail Pilot Configuration page Use
                                                                     								  Default Voice Mail Box Mask When multitenant services are not
                                                            						  enabled on Cisco Unified CM, leave this field blank. When multitenant services are
                                                            						  enabled, each tenant uses its own voice mail profile and must create a mask to
                                                            						  identify the extensions (directory numbers) in each partition that is shared
                                                            						  with other tenants. For example, one tenant can use a mask 972813XXXX, while
                                                            						  another tenant can use the mask 214333XXXX. Each tenant also uses its own
                                                            						  translation patterns for MWIs. Make This the Default Voice Mail
                                                            						  Profile for the System Check this check box to make this
                                                            						  voice mail profile the default. When this check box is checked, this
                                                            						  voice mail profile replaces the current default voice mail profile. | Field | Setting | Voice Mail Profile Name | Enter a name to identify the voice
                                                            						  mail profile. | Description | Enter Unity Connection Profile or
                                                            						  another description. | Voice Mail Pilot | Select one of the following: The applicable voice mail pilot
                                                                  								number that you defined on the Voice Mail Pilot Configuration page Use
                                                                     								  Default | Voice Mail Box Mask | When multitenant services are not
                                                            						  enabled on Cisco Unified CM, leave this field blank. When multitenant services are
                                                            						  enabled, each tenant uses its own voice mail profile and must create a mask to
                                                            						  identify the extensions (directory numbers) in each partition that is shared
                                                            						  with other tenants. For example, one tenant can use a mask 972813XXXX, while
                                                            						  another tenant can use the mask 214333XXXX. Each tenant also uses its own
                                                            						  translation patterns for MWIs. | Make This the Default Voice Mail
                                                            						  Profile for the System | Check this check box to make this
                                                            						  voice mail profile the default. When this check box is checked, this
                                                            						  voice mail profile replaces the current default voice mail profile. |
| Field | Setting |
| Voice Mail Profile Name | Enter a name to identify the voice
                                                            						  mail profile. |
| Description | Enter Unity Connection Profile or
                                                            						  another description. |
| Voice Mail Pilot | Select one of the following: The applicable voice mail pilot
                                                                  								number that you defined on the Voice Mail Pilot Configuration page Use
                                                                     								  Default |
| Voice Mail Box Mask | When multitenant services are not
                                                            						  enabled on Cisco Unified CM, leave this field blank. When multitenant services are
                                                            						  enabled, each tenant uses its own voice mail profile and must create a mask to
                                                            						  identify the extensions (directory numbers) in each partition that is shared
                                                            						  with other tenants. For example, one tenant can use a mask 972813XXXX, while
                                                            						  another tenant can use the mask 214333XXXX. Each tenant also uses its own
                                                            						  translation patterns for MWIs. |
| Make This the Default Voice Mail
                                                            						  Profile for the System | Check this check box to make this
                                                            						  voice mail profile the default. When this check box is checked, this
                                                            						  voice mail profile replaces the current default voice mail profile. |
| Step 4 | Select Save . |

| Field | Setting |
|---|---|
| Voice Mail Profile Name | Enter a name to identify the voice
                                                            						  mail profile. |
| Description | Enter Unity Connection Profile or
                                                            						  another description. |
| Voice Mail Pilot | Select one of the following: The applicable voice mail pilot
                                                                  								number that you defined on the Voice Mail Pilot Configuration page Use
                                                                     								  Default |
| Voice Mail Box Mask | When multitenant services are not
                                                            						  enabled on Cisco Unified CM, leave this field blank. When multitenant services are
                                                            						  enabled, each tenant uses its own voice mail profile and must create a mask to
                                                            						  identify the extensions (directory numbers) in each partition that is shared
                                                            						  with other tenants. For example, one tenant can use a mask 972813XXXX, while
                                                            						  another tenant can use the mask 214333XXXX. Each tenant also uses its own
                                                            						  translation patterns for MWIs. |
| Make This the Default Voice Mail
                                                            						  Profile for the System | Check this check box to make this
                                                            						  voice mail profile the default. When this check box is checked, this
                                                            						  voice mail profile replaces the current default voice mail profile. |

| Step 1 | In Cisco Unified CM Administration, select System > and then select > Service Parameters . |
|---|---|
| Step 2 | On the Service Parameters Configuration
                                             			 page, in the Server field, select the name of the Cisco Unified CM server. |
| Step 3 | In the Service list, select Cisco CallManager . The
                                             			 list of parameters appears. |
| Step 4 | Under Clusterwide Parameters (Feature -
                                             			 General), locate the Multiple Tenant MWI Modes parameter. |
| Step 5 | If you use multiple tenant MWI notification,
                                             			 select True . When this parameter is set to True, Cisco
                                                				Unified CM uses any configured translation patterns to convert voice mail
                                                				extensions into directory numbers when turning on or off an MWI. |
| Step 6 | If you changed any settings, select Save . Otherwise, skip
                                             			 the remaining steps in this procedure. |
| Step 7 | In the Navigation drop-down box, select Cisco Unified
                                                				Serviceability and select Go . |
| Step 8 | In Cisco Unified Serviceability, on the
                                             			 Tools menu, select Control Center - Feature
                                                				Services . |
| Step 9 | Under CM Services, select Cisco CallManager and
                                             			 select Restart . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems page, under Display Name, select the
                                          			 name of the default phone system. |
| Step 3 | On the Phone System Basics page, in the Phone System Name field,
                                          			 enter the descriptive name that you want for the phone system. |
| Step 4 | If you want to use this phone system as the default for TRaP
                                          			 connections so that administrators and users without voicemail boxes can record
                                          			 and playback through the phone in Unity Connection web applications, check the Default TRAP Switch check box. If you want to use
                                          			 another phone system as the default for TRaP connections, uncheck this check
                                          			 box. |
| Step 5 | Select Save . |
| Step 6 | On the Phone System Basics page, in the Related Links drop-down
                                          			 box, select Add Port Group and select Go . |
| Step 7 | On the New Port Group page, enter the following settings and
                                          			 select Save . Table 11. Settings for the New Port Group Page Field Setting Phone System Select the name of the phone system that you entered in Step 3 . Create From Select Port Group Template and
                                                         						  select SCCP in the drop-down
                                                         						  box. Display Name Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. Device Name Prefix Enter the prefix that Cisco Unified CM adds to the device name
                                                         						  for voice ports. This prefix must match the prefix used by Cisco Unified CM. MWI On Extension Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs on. MWI Off Extension Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs off. IPv4 Address or Host Name Enter the IPv4 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv6 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. If you use Cisco Unified CM authentication and encryption, enter
                                                         						  an IP address or host name in this field. The CTL file used for encryption
                                                         						  between Unity Connection and Cisco Unified CM requires an IPv4 address or host
                                                         						  name, even if you are otherwise using IPv6 addressing. IPv6 Address or Host Name Enter the IPv6 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv4 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. The IPv6 address should be in canonical textual representation
                                                         						  formats proposed by Internet Engineering Task Force in RFC5952 standard for
                                                         						  rendering IPv6 addresses in text. For more details on IPv6 formats, please
                                                         						  refer the link https://tools.ietf.org/html/rfc5952#section-4 Note IPv6 is supported in Cisco Unified CM 7.1(2) and later. IP Address or Host Name Enter the IP address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. Port Enter the TCP port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. TLS Port Enter the TLS port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. | Field | Setting | Phone System | Select the name of the phone system that you entered in Step 3 . | Create From | Select Port Group Template and
                                                         						  select SCCP in the drop-down
                                                         						  box. | Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. | Device Name Prefix | Enter the prefix that Cisco Unified CM adds to the device name
                                                         						  for voice ports. This prefix must match the prefix used by Cisco Unified CM. | MWI On Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs on. | MWI Off Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs off. | IPv4 Address or Host Name | Enter the IPv4 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv6 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. If you use Cisco Unified CM authentication and encryption, enter
                                                         						  an IP address or host name in this field. The CTL file used for encryption
                                                         						  between Unity Connection and Cisco Unified CM requires an IPv4 address or host
                                                         						  name, even if you are otherwise using IPv6 addressing. | IPv6 Address or Host Name | Enter the IPv6 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv4 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. The IPv6 address should be in canonical textual representation
                                                         						  formats proposed by Internet Engineering Task Force in RFC5952 standard for
                                                         						  rendering IPv6 addresses in text. For more details on IPv6 formats, please
                                                         						  refer the link https://tools.ietf.org/html/rfc5952#section-4 Note IPv6 is supported in Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. | IP Address or Host Name | Enter the IP address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. | Port | Enter the TCP port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. | TLS Port | Enter the TLS port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. |
| Field | Setting |
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SCCP in the drop-down
                                                         						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| Device Name Prefix | Enter the prefix that Cisco Unified CM adds to the device name
                                                         						  for voice ports. This prefix must match the prefix used by Cisco Unified CM. |
| MWI On Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs on. |
| MWI Off Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs off. |
| IPv4 Address or Host Name | Enter the IPv4 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv6 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. If you use Cisco Unified CM authentication and encryption, enter
                                                         						  an IP address or host name in this field. The CTL file used for encryption
                                                         						  between Unity Connection and Cisco Unified CM requires an IPv4 address or host
                                                         						  name, even if you are otherwise using IPv6 addressing. |
| IPv6 Address or Host Name | Enter the IPv6 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv4 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. The IPv6 address should be in canonical textual representation
                                                         						  formats proposed by Internet Engineering Task Force in RFC5952 standard for
                                                         						  rendering IPv6 addresses in text. For more details on IPv6 formats, please
                                                         						  refer the link https://tools.ietf.org/html/rfc5952#section-4 Note IPv6 is supported in Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. |
| Port | Enter the TCP port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. |
| TLS Port | Enter the TLS port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. |
| Step 8 | On the Port Group Basics page, in the Related Links drop-down
                                          			 box, select Add Ports and select Go . |
| Step 9 | On the New Port page, enter the following settings and select Save . Table 12. Settings for the New Port Page Field Setting Enabled Check this check box. Number of Ports Enter the number of voice
                                                         						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. Phone System Select the name of the
                                                         						  phone system that you entered in Step
                                                            							 3 . Port Group Select the name of the
                                                         						  port group that you added in 7 . Server Select the name Unity
                                                         						  Connection server. Security Mode Select the Cisco
                                                         						  Unified CM security mode that you want to use for the voice messaging ports. | Field | Setting | Enabled | Check this check box. | Number of Ports | Enter the number of voice
                                                         						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. | Phone System | Select the name of the
                                                         						  phone system that you entered in Step
                                                            							 3 . | Port Group | Select the name of the
                                                         						  port group that you added in 7 . | Server | Select the name Unity
                                                         						  Connection server. | Security Mode | Select the Cisco
                                                         						  Unified CM security mode that you want to use for the voice messaging ports. |
| Field | Setting |
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                                         						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step
                                                            							 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in 7 . |
| Server | Select the name Unity
                                                         						  Connection server. |
| Security Mode | Select the Cisco
                                                         						  Unified CM security mode that you want to use for the voice messaging ports. |
| Step 10 | On the Search Ports page, select the display name of the first
                                          			 voice messaging port that you created for this phone system integration. Note By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. | Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
| Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
| Step 11 | On the Port Basics page, set the voice messaging port settings
                                          			 as applicable. The fields in the following table are the ones that you can
                                          			 change. Table 13. Settings for the Voice Messaging Ports Field Considerations Enabled Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. Server (For Unity Connection
                                                            							 clusters only) Select the name of the Unity Connection server that you want
                                                         						  to handle this port. For details, see Planning
                                                            							 the Voice Messaging Ports Answer Calls Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. Perform Message
                                                         						  Notification Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. Send MWI Requests Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. Allow TRAP Connections Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. Outgoing Hunt Order Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. Security Mode Select the applicable
                                                         						  security mode: Non-secure —The
                                                               								integrity and privacy of call-signaling messages is not ensured because
                                                               								call-signaling messages are sent as clear (unencrypted) text and connected to
                                                               								Cisco Unified CM through a non-authenticated port rather than an authenticated
                                                               								TLS port. In addition, the media stream is not encrypted. Authenticated —The
                                                               								integrity of call-signaling messages is ensured because they are connected to
                                                               								Cisco Unified CM through an authenticated TLS port. However, the privacy of
                                                               								call-signaling messages is not ensured because they are sent as clear
                                                               								(unencrypted) text. In addition, the media stream is not encrypted. Encrypted —The
                                                               								integrity and privacy of call-signaling messages is ensured on this port
                                                               								because they are connected to Cisco Unified CM through an authenticated TLS
                                                               								port, and the call-signaling messages are encrypted. In addition, the media
                                                               								stream is encrypted. Caution The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. Note For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption | Field | Considerations | Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. | Server | (For Unity Connection
                                                            							 clusters only) Select the name of the Unity Connection server that you want
                                                         						  to handle this port. For details, see Planning
                                                            							 the Voice Messaging Ports | Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. | Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. | Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. | Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. | Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. | Security Mode | Select the applicable
                                                         						  security mode: Non-secure —The
                                                               								integrity and privacy of call-signaling messages is not ensured because
                                                               								call-signaling messages are sent as clear (unencrypted) text and connected to
                                                               								Cisco Unified CM through a non-authenticated port rather than an authenticated
                                                               								TLS port. In addition, the media stream is not encrypted. Authenticated —The
                                                               								integrity of call-signaling messages is ensured because they are connected to
                                                               								Cisco Unified CM through an authenticated TLS port. However, the privacy of
                                                               								call-signaling messages is not ensured because they are sent as clear
                                                               								(unencrypted) text. In addition, the media stream is not encrypted. Encrypted —The
                                                               								integrity and privacy of call-signaling messages is ensured on this port
                                                               								because they are connected to Cisco Unified CM through an authenticated TLS
                                                               								port, and the call-signaling messages are encrypted. In addition, the media
                                                               								stream is encrypted. Caution The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. Note For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption | Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. | Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |
| Field | Considerations |
| Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. |
| Server | (For Unity Connection
                                                            							 clusters only) Select the name of the Unity Connection server that you want
                                                         						  to handle this port. For details, see Planning
                                                            							 the Voice Messaging Ports |
| Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. |
| Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. |
| Security Mode | Select the applicable
                                                         						  security mode: Non-secure —The
                                                               								integrity and privacy of call-signaling messages is not ensured because
                                                               								call-signaling messages are sent as clear (unencrypted) text and connected to
                                                               								Cisco Unified CM through a non-authenticated port rather than an authenticated
                                                               								TLS port. In addition, the media stream is not encrypted. Authenticated —The
                                                               								integrity of call-signaling messages is ensured because they are connected to
                                                               								Cisco Unified CM through an authenticated TLS port. However, the privacy of
                                                               								call-signaling messages is not ensured because they are sent as clear
                                                               								(unencrypted) text. In addition, the media stream is not encrypted. Encrypted —The
                                                               								integrity and privacy of call-signaling messages is ensured on this port
                                                               								because they are connected to Cisco Unified CM through an authenticated TLS
                                                               								port, and the call-signaling messages are encrypted. In addition, the media
                                                               								stream is encrypted. Caution The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. Note For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption | Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. | Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |
| Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. |
| Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |
| Step 12 | Select Save . |
| Step 13 | Select Next . |
| Step 14 | Repeat Step 11 through 13 for all remaining voice messaging ports for the phone system. |
| Step 15 | If Cisco Unity Connection does not connect to an AXL server,
                                          			 skip to Step 28 .
                                          			 Otherwise, expand Telephony
                                             				Integrations , then select Phone System . |
| Step 16 | On the Search Phone Systems page, select the display name of the
                                          			 phone system that you created in 3 . |
| Step 17 | On the Phone System Basics page, in the Edit menu, select Cisco Unified
                                             				Communications Manager AXL Servers . Connecting to an AXL server is needed when Cisco Unity
                                             				Connection must have access to the Cisco Unified CM database for importing
                                             				Cisco Unified CM users and for changing certain phone settings for users of
                                             				Cisco Unity Connection personal call transfer rules. Note If you plan to import Cisco Unified CM users, confirm that the
                                                         				  Primary Extension field on the End User Configuration page for each user is
                                                         				  filled in. Otherwise, the search does not find any users to select for
                                                         				  importing. | Note | If you plan to import Cisco Unified CM users, confirm that the
                                                         				  Primary Extension field on the End User Configuration page for each user is
                                                         				  filled in. Otherwise, the search does not find any users to select for
                                                         				  importing. |
| Note | If you plan to import Cisco Unified CM users, confirm that the
                                                         				  Primary Extension field on the End User Configuration page for each user is
                                                         				  filled in. Otherwise, the search does not find any users to select for
                                                         				  importing. |
| Step 18 | On the Edit AXL Servers page, under AXL Servers, select Add New . |
| Step 19 | Enter the following settings for the AXL server and select Save . Table 14. Settings for the AXL Servers Field Setting Order Enter the order of
                                                         						  priority for the AXL server. The lowest number is the primary AXL server, the
                                                         						  higher numbers are the secondary servers. IP Address Enter the IP address of
                                                         						  the AXL server. Port Enter the AXL server port
                                                         						  that Unity Connection connects to. This setting must match the port that the
                                                         						  AXL server uses. | Field | Setting | Order | Enter the order of
                                                         						  priority for the AXL server. The lowest number is the primary AXL server, the
                                                         						  higher numbers are the secondary servers. | IP Address | Enter the IP address of
                                                         						  the AXL server. | Port | Enter the AXL server port
                                                         						  that Unity Connection connects to. This setting must match the port that the
                                                         						  AXL server uses. |
| Field | Setting |
| Order | Enter the order of
                                                         						  priority for the AXL server. The lowest number is the primary AXL server, the
                                                         						  higher numbers are the secondary servers. |
| IP Address | Enter the IP address of
                                                         						  the AXL server. |
| Port | Enter the AXL server port
                                                         						  that Unity Connection connects to. This setting must match the port that the
                                                         						  AXL server uses. |
| Step 20 | Repeat 18 and 19 for all remaining AXL servers. |
| Step 21 | Under AXL Server Settings, enter the following settings and
                                          			 select Save . Table 15. Settings for the AXL Server Settings Field Setting Username Enter the username that
                                                         						  Unity Connection uses to sign in to the AXL server. Note This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. Password Enter the password for
                                                         						  the user that Unity Connection uses to sign in to the AXL server. Note This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. Cisco Unified Communications Manager Version Select the applicable setting that accurately describes the
                                                         						  following: The version of Cisco Unified CM that you are integrating with
                                                               								Unity Connection. Whether the AXL port is enabled for SSL. If
                                                         						  you select the non-SSL version, the AXL port must be a non-SSL port (typically
                                                         						  port 80). If you select the SSL-enabled version, the AXL port must be an
                                                         						  SSL-enabled port (typically port 443 or port 8443). Enable End User PIN Synchronization for Primary AXL Server Check this check box to enable PIN synchronization between Unity
                                                         						  Connection and Cisco Unified CM for the users having same user ID (alias in
                                                         						  Unity Connection). After enabling the feature whenever user updates the PIN on
                                                         						  Cisco Unity Connection, the PIN gets synchronized with Cisco Unified CM and
                                                         						  vice-versa. Default setting: Check box is not checked. For more information on PIN Synchronization, see the " PIN Synchronization between Unity Connection and Cisco Unified CM " section of the "User Settings" chapter of the System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html . Ignore Certificate Errors Check the check box to ignore certificate validation errors for
                                                         						  AXL Servers. When the check box is unchecked, Unity Connection validates the
                                                         						  certificate for the AXL servers. However, before checking the checkbox make
                                                         						  sure that the tomcat root certificate of Cisco Unified CM must be uploaded to
                                                         						  tomcat trust of Unity Connection server. Default setting: Check box is checked. For more information on certificates, see “ Security ” chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx.html . | Field | Setting | Username | Enter the username that
                                                         						  Unity Connection uses to sign in to the AXL server. Note This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. | Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. | Password | Enter the password for
                                                         						  the user that Unity Connection uses to sign in to the AXL server. Note This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. | Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. | Cisco Unified Communications Manager Version | Select the applicable setting that accurately describes the
                                                         						  following: The version of Cisco Unified CM that you are integrating with
                                                               								Unity Connection. Whether the AXL port is enabled for SSL. If
                                                         						  you select the non-SSL version, the AXL port must be a non-SSL port (typically
                                                         						  port 80). If you select the SSL-enabled version, the AXL port must be an
                                                         						  SSL-enabled port (typically port 443 or port 8443). | Enable End User PIN Synchronization for Primary AXL Server | Check this check box to enable PIN synchronization between Unity
                                                         						  Connection and Cisco Unified CM for the users having same user ID (alias in
                                                         						  Unity Connection). After enabling the feature whenever user updates the PIN on
                                                         						  Cisco Unity Connection, the PIN gets synchronized with Cisco Unified CM and
                                                         						  vice-versa. Default setting: Check box is not checked. For more information on PIN Synchronization, see the " PIN Synchronization between Unity Connection and Cisco Unified CM " section of the "User Settings" chapter of the System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html . | Ignore Certificate Errors | Check the check box to ignore certificate validation errors for
                                                         						  AXL Servers. When the check box is unchecked, Unity Connection validates the
                                                         						  certificate for the AXL servers. However, before checking the checkbox make
                                                         						  sure that the tomcat root certificate of Cisco Unified CM must be uploaded to
                                                         						  tomcat trust of Unity Connection server. Default setting: Check box is checked. For more information on certificates, see “ Security ” chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx.html . |
| Field | Setting |
| Username | Enter the username that
                                                         						  Unity Connection uses to sign in to the AXL server. Note This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. | Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. |
| Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. |
| Password | Enter the password for
                                                         						  the user that Unity Connection uses to sign in to the AXL server. Note This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. | Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. |
| Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. |
| Cisco Unified Communications Manager Version | Select the applicable setting that accurately describes the
                                                         						  following: The version of Cisco Unified CM that you are integrating with
                                                               								Unity Connection. Whether the AXL port is enabled for SSL. If
                                                         						  you select the non-SSL version, the AXL port must be a non-SSL port (typically
                                                         						  port 80). If you select the SSL-enabled version, the AXL port must be an
                                                         						  SSL-enabled port (typically port 443 or port 8443). |
| Enable End User PIN Synchronization for Primary AXL Server | Check this check box to enable PIN synchronization between Unity
                                                         						  Connection and Cisco Unified CM for the users having same user ID (alias in
                                                         						  Unity Connection). After enabling the feature whenever user updates the PIN on
                                                         						  Cisco Unity Connection, the PIN gets synchronized with Cisco Unified CM and
                                                         						  vice-versa. Default setting: Check box is not checked. For more information on PIN Synchronization, see the " PIN Synchronization between Unity Connection and Cisco Unified CM " section of the "User Settings" chapter of the System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html . |
| Ignore Certificate Errors | Check the check box to ignore certificate validation errors for
                                                         						  AXL Servers. When the check box is unchecked, Unity Connection validates the
                                                         						  certificate for the AXL servers. However, before checking the checkbox make
                                                         						  sure that the tomcat root certificate of Cisco Unified CM must be uploaded to
                                                         						  tomcat trust of Unity Connection server. Default setting: Check box is checked. For more information on certificates, see “ Security ” chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx.html . |
| Step 22 | To add a corresponding application server to Cisco Unified CM,
                                          			 sign in to Cisco Unified CM Administration. |
| Step 23 | In Cisco Unified CM Administration, navigate to System >
                                          			 Application Server page. |
| Step 24 | On the Find and List Application Servers page, select Find to
                                          			 display all application servers. |
| Step 25 | In the Name column, select the name of the Cisco Unity
                                          			 Connection server. |
| Step 26 | On the Application Server Configuration page, in the Available
                                          			 Application User field, select the Cisco Unified CM application user that you
                                          			 used in 21 and select the down arrow to
                                          			 move it to the Selected Application User field. |
| Step 27 | Select Save. |
| Step 28 | In Cisco Unity Connection Administration, expand Telephony
                                             				Integrations , then select Port Group . |
| Step 29 | On the Search Port Groups page, select the display name of the
                                          			 port group that you created with the phone system integration in Step 7 . Note By default, the display name for a port group is composed of the
                                                         				  phone system display name followed by an incrementing number. | Note | By default, the display name for a port group is composed of the
                                                         				  phone system display name followed by an incrementing number. |
| Note | By default, the display name for a port group is composed of the
                                                         				  phone system display name followed by an incrementing number. |
| Step 30 | On the Port Group Basics page, on the Edit menu, select Servers . |
| Step 31 | On the Edit Servers page, do the following substeps if the Cisco
                                          			 Unified CM cluster has secondary servers. Otherwise, skip to 32 . Under Cisco Unified Communications Manager Servers, select Add . Enter the following settings for the secondary Cisco Unified CM
                                                				  server and select Save . Table 16. Settings for the Cisco
                                                         					 Unified Communications Manager Servers Field Setting Order Enter the order of
                                                               								priority for the Cisco Unified CM server. The lowest number is the primary
                                                               								Cisco Unified CM server, the higher numbers are the secondary servers. IPv4 Address or Host Name Enter the IPv4 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. IPv6 Address or Host Name Enter the IPv6 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. IP Address or Host Name Enter the IP address (or
                                                               								host name) of the secondary Cisco Unified CM server. Port Enter the TCP port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. TLS Port Enter the TLS port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. Server Type Select Cisco Unified
                                                                  								  Communications Manager . Repeat 31 for all remaining Cisco Unified CM servers in the cluster. | Field | Setting | Order | Enter the order of
                                                               								priority for the Cisco Unified CM server. The lowest number is the primary
                                                               								Cisco Unified CM server, the higher numbers are the secondary servers. | IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. | IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the secondary Cisco Unified CM server. | Port | Enter the TCP port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. | TLS Port | Enter the TLS port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. | Server Type | Select Cisco Unified
                                                                  								  Communications Manager . |
| Field | Setting |
| Order | Enter the order of
                                                               								priority for the Cisco Unified CM server. The lowest number is the primary
                                                               								Cisco Unified CM server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. |
| IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the secondary Cisco Unified CM server. |
| Port | Enter the TCP port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. |
| Server Type | Select Cisco Unified
                                                                  								  Communications Manager . |
| Step 32 | Do the following substeps if the Cisco Unified CM cluster uses
                                          			 authentication or encryption for the voice messaging ports. Under TFTP Servers, select Add . Enter the following settings for the TFTP server and select Save . Table 17. Settings for the TFTP
                                                         					 Server Field Setting Order Enter the order of
                                                               								priority for the TFTP server. The lowest number is the primary TFTP server, the
                                                               								higher numbers are the secondary servers. IPv4 Address or Host Name Enter the IPv4 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. IPv6 Address or Host Name Enter the IPv6 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. IP Address or Host Name Enter the IP address (or
                                                               								host name) of the TFTP server. Repeat 32 for all remaining TFTP servers in the Cisco Unified CM cluster. | Field | Setting | Order | Enter the order of
                                                               								priority for the TFTP server. The lowest number is the primary TFTP server, the
                                                               								higher numbers are the secondary servers. | IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. | IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the TFTP server. |
| Field | Setting |
| Order | Enter the order of
                                                               								priority for the TFTP server. The lowest number is the primary TFTP server, the
                                                               								higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. |
| IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the TFTP server. |
| Step 33 | If another phone system integration exists, in Cisco Unity
                                          			 Connection Administration, expand Telephony
                                             				Integrations , then select Trunk .
                                          			 Otherwise, skip to 37 . |
| Step 34 | On the Search Phone System Trunks page, on the Phone System
                                          			 Trunk menu, select New Phone System
                                             				Trunk . |
| Step 35 | On the New Phone System Trunk page, enter the following settings
                                          			 for the phone system trunk and select Save . Table 18. Settings for the Phone System Trunk Field Setting From Phone System Select the display name
                                                         						  of the phone system that you are creating a trunk for. To Phone System Select the display name
                                                         						  of the previously existing phone system that the trunk connects to. Trunk Access Code Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. | Field | Setting | From Phone System | Select the display name
                                                         						  of the phone system that you are creating a trunk for. | To Phone System | Select the display name
                                                         						  of the previously existing phone system that the trunk connects to. | Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |
| Field | Setting |
| From Phone System | Select the display name
                                                         						  of the phone system that you are creating a trunk for. |
| To Phone System | Select the display name
                                                         						  of the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |
| Step 36 | Repeat 34 and 35 for all remaining phone system trunks that you want to create. |
| Step 37 | In the Related Links drop-down list, select Check Telephony
                                             				Configuration and select Go to confirm
                                          			 the phone system integration settings. If the test is not successful, the Task Execution Results
                                             				displays one or more messages with troubleshooting steps. After correcting the
                                             				problems, test the connection again. |
| Step 38 | In the Task Execution Results window, select Close . |

| Field | Setting |
|---|---|
| Phone System | Select the name of the phone system that you entered in Step 3 . |
| Create From | Select Port Group Template and
                                                         						  select SCCP in the drop-down
                                                         						  box. |
| Display Name | Enter a descriptive name for the port group. You can accept the
                                                         						  default name or enter the name that you want. |
| Device Name Prefix | Enter the prefix that Cisco Unified CM adds to the device name
                                                         						  for voice ports. This prefix must match the prefix used by Cisco Unified CM. |
| MWI On Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs on. |
| MWI Off Extension | Enter the extension that you specified in Cisco Unified CM
                                                         						  Administration for turning MWIs off. |
| IPv4 Address or Host Name | Enter the IPv4 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv6 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. If you use Cisco Unified CM authentication and encryption, enter
                                                         						  an IP address or host name in this field. The CTL file used for encryption
                                                         						  between Unity Connection and Cisco Unified CM requires an IPv4 address or host
                                                         						  name, even if you are otherwise using IPv6 addressing. |
| IPv6 Address or Host Name | Enter the IPv6 address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection You must enter an IP address or host name in this field, or an
                                                         						  IP address or host name in the IPv4 Address or Host Name field (or, if
                                                         						  applicable, enter information in both fields). You cannot leave both fields
                                                         						  blank. The IPv6 address should be in canonical textual representation
                                                         						  formats proposed by Internet Engineering Task Force in RFC5952 standard for
                                                         						  rendering IPv6 addresses in text. For more details on IPv6 formats, please
                                                         						  refer the link https://tools.ietf.org/html/rfc5952#section-4 Note IPv6 is supported in Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or host name) of the primary Cisco
                                                         						  Unified CM server that you are integrating with Unity Connection. |
| Port | Enter the TCP port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. |
| TLS Port | Enter the TLS port of the primary Cisco Unified CM server that
                                                         						  you are integrating with Unity Connection. We recommend that you use the
                                                         						  default setting. |

| Note | IPv6 is supported in Cisco Unified CM 7.1(2) and later. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box. |
| Number of Ports | Enter the number of voice
                                                         						  messaging ports that you want to create in this port group. Note For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. | Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. |
| Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. |
| Phone System | Select the name of the
                                                         						  phone system that you entered in Step
                                                            							 3 . |
| Port Group | Select the name of the
                                                         						  port group that you added in 7 . |
| Server | Select the name Unity
                                                         						  Connection server. |
| Security Mode | Select the Cisco
                                                         						  Unified CM security mode that you want to use for the voice messaging ports. |

| Note | For a Unity Connection cluster, you must enter the total number
                                                                  						  of voice messaging ports that is used by all Unity Connection servers. Later,
                                                                  						  each port is assigned to a specific Unity Connection server. |
|---|---|

| Note | By default, the display names for the voice messaging ports are
                                                      				composed of the port group display name followed by incrementing numbers. |
|---|---|

| Field | Considerations |
|---|---|
| Enabled | Check this check box to
                                                         						  enable the port. The port is enabled during normal operation. Uncheck this check box to
                                                         						  disable the port. When the port is disabled, calls to the port get a ringing
                                                         						  tone but are not answered. Typically, the port is disabled only by the
                                                         						  installer during testing. |
| Server | (For Unity Connection
                                                            							 clusters only) Select the name of the Unity Connection server that you want
                                                         						  to handle this port. For details, see Planning
                                                            							 the Voice Messaging Ports |
| Answer Calls | Check this check box to
                                                         						  designate the port for answering calls. These calls can be incoming calls from
                                                         						  unidentified callers or from users. |
| Perform Message
                                                         						  Notification | Check this check box to
                                                         						  designate the port for notifying users of messages. Assign Perform Message
                                                         						  Notification to the least busy ports. |
| Send MWI Requests | Check this check box to
                                                         						  designate the port for turning MWIs on and off. Assign Send MWI Requests to the
                                                         						  least busy ports. |
| Allow TRAP Connections | Check this check box so
                                                         						  that users can use the port for recording and playback through the phone in
                                                         						  Unity Connection web applications. Assign Allow TRAP Connections to the least
                                                         						  busy ports. |
| Outgoing Hunt Order | Enter the priority order
                                                         						  in which Unity Connection use the ports when dialing out (for example, if the
                                                         						  Perform Message Notification, Send MWI Requests, or Allow TRAP Connections
                                                         						  check box is checked). The highest numbers are used first. However, when
                                                         						  multiple ports have the same Outgoing Hunt Order number, Unity Connection use
                                                         						  the port that has been idle the longest. |
| Security Mode | Select the applicable
                                                         						  security mode: Non-secure —The
                                                               								integrity and privacy of call-signaling messages is not ensured because
                                                               								call-signaling messages are sent as clear (unencrypted) text and connected to
                                                               								Cisco Unified CM through a non-authenticated port rather than an authenticated
                                                               								TLS port. In addition, the media stream is not encrypted. Authenticated —The
                                                               								integrity of call-signaling messages is ensured because they are connected to
                                                               								Cisco Unified CM through an authenticated TLS port. However, the privacy of
                                                               								call-signaling messages is not ensured because they are sent as clear
                                                               								(unencrypted) text. In addition, the media stream is not encrypted. Encrypted —The
                                                               								integrity and privacy of call-signaling messages is ensured on this port
                                                               								because they are connected to Cisco Unified CM through an authenticated TLS
                                                               								port, and the call-signaling messages are encrypted. In addition, the media
                                                               								stream is encrypted. Caution The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. Note For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption | Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. | Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |
| Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. |
| Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |

| Caution | The Security Mode setting
                                                                           								  for Unity Connection voice messaging ports must match the security mode setting
                                                                           								  for the Cisco Unified CM ports. Otherwise, Cisco Unified CM authentication and
                                                                           								  encryption fail. The Unity Connection system clock must be synchronized with the
                                                                           								  Cisco Unified CM system clock for Cisco Unified CM authentication to function
                                                                           								  immediately. Otherwise, Cisco Unified CM reject the Unity Connection voice
                                                                           								  messaging ports until the Cisco Unified CM system clock has passed the time
                                                                           								  stamp in the Unity Connection device certificates. |
|---|---|

| Note | For requirements and additional information about
                                                                        								authentication and encryption with Cisco Unified CM and Unity Connection, see Cisco
                                                                           								  Unified Communications Manager Authentication and Encryption |
|---|---|

| Note | If you plan to import Cisco Unified CM users, confirm that the
                                                         				  Primary Extension field on the End User Configuration page for each user is
                                                         				  filled in. Otherwise, the search does not find any users to select for
                                                         				  importing. |
|---|---|

| Field | Setting |
|---|---|
| Order | Enter the order of
                                                         						  priority for the AXL server. The lowest number is the primary AXL server, the
                                                         						  higher numbers are the secondary servers. |
| IP Address | Enter the IP address of
                                                         						  the AXL server. |
| Port | Enter the AXL server port
                                                         						  that Unity Connection connects to. This setting must match the port that the
                                                         						  AXL server uses. |

| Field | Setting |
|---|---|
| Username | Enter the username that
                                                         						  Unity Connection uses to sign in to the AXL server. Note This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. | Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. |
| Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. |
| Password | Enter the password for
                                                         						  the user that Unity Connection uses to sign in to the AXL server. Note This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. | Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. |
| Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. |
| Cisco Unified Communications Manager Version | Select the applicable setting that accurately describes the
                                                         						  following: The version of Cisco Unified CM that you are integrating with
                                                               								Unity Connection. Whether the AXL port is enabled for SSL. If
                                                         						  you select the non-SSL version, the AXL port must be a non-SSL port (typically
                                                         						  port 80). If you select the SSL-enabled version, the AXL port must be an
                                                         						  SSL-enabled port (typically port 443 or port 8443). |
| Enable End User PIN Synchronization for Primary AXL Server | Check this check box to enable PIN synchronization between Unity
                                                         						  Connection and Cisco Unified CM for the users having same user ID (alias in
                                                         						  Unity Connection). After enabling the feature whenever user updates the PIN on
                                                         						  Cisco Unity Connection, the PIN gets synchronized with Cisco Unified CM and
                                                         						  vice-versa. Default setting: Check box is not checked. For more information on PIN Synchronization, see the " PIN Synchronization between Unity Connection and Cisco Unified CM " section of the "User Settings" chapter of the System Administration Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html . |
| Ignore Certificate Errors | Check the check box to ignore certificate validation errors for
                                                         						  AXL Servers. When the check box is unchecked, Unity Connection validates the
                                                         						  certificate for the AXL servers. However, before checking the checkbox make
                                                         						  sure that the tomcat root certificate of Cisco Unified CM must be uploaded to
                                                         						  tomcat trust of Unity Connection server. Default setting: Check box is checked. For more information on certificates, see “ Security ” chapter of Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 14 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/os_administration/guide/b_14cucosagx.html . |

| Note | This user must match the
                                                                     							 user name of a Cisco Unified CM application user who is assigned to the
                                                                     							 “Standard AXL API Access” role. |
|---|---|

| Note | This password must match
                                                                     							 the password of the Cisco Unified CM application user entered in the User Name
                                                                     							 field. |
|---|---|

| Note | By default, the display name for a port group is composed of the
                                                         				  phone system display name followed by an incrementing number. |
|---|---|

| Field | Setting |
|---|---|
| Order | Enter the order of
                                                               								priority for the Cisco Unified CM server. The lowest number is the primary
                                                               								Cisco Unified CM server, the higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. |
| IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the secondary Cisco Unified CM server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the secondary Cisco Unified CM server. |
| Port | Enter the TCP port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. |
| TLS Port | Enter the TLS port of the
                                                               								Cisco Unified CM server that you are integrating with Unity Connection. We
                                                               								recommend that you use the default setting. |
| Server Type | Select Cisco Unified
                                                                  								  Communications Manager . |

| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
|---|---|

| Field | Setting |
|---|---|
| Order | Enter the order of
                                                               								priority for the TFTP server. The lowest number is the primary TFTP server, the
                                                               								higher numbers are the secondary servers. |
| IPv4 Address or Host Name | Enter the IPv4 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv6
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. |
| IPv6 Address or Host Name | Enter the IPv6 address
                                                               								(or host name) of the TFTP server. You must enter an IP
                                                               								address or host name in this field, or an IP address or host name in the IPv4
                                                               								Address or Host Name field (or, if applicable, enter information in both
                                                               								fields). You cannot leave both fields blank. Note IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. | Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
| IP Address or Host Name | Enter the IP address (or
                                                               								host name) of the TFTP server. |

| Note | IPv6 is supported in
                                                                           								  Cisco Unified CM 7.1(2) and later. |
|---|---|

| Field | Setting |
|---|---|
| From Phone System | Select the display name
                                                         						  of the phone system that you are creating a trunk for. |
| To Phone System | Select the display name
                                                         						  of the previously existing phone system that the trunk connects to. |
| Trunk Access Code | Enter the extra digits
                                                         						  that Unity Connection must dial to transfer calls through the gateway to
                                                         						  extensions on the previously existing phone system. |