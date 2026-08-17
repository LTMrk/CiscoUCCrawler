---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-administration-guide-b-15cucsag-b-15cucsag-chapter-0110-html-5b73798827
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_0110.html
retrieved_at: 2026-08-17T02:19:26.669564+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 12, 2025

Chapter: Telephony
	 Integration

## Chapter: Telephony
	 Integration

# Telephony
                     	 Integration

## Introduction

Telephony Integration is a process that enables the
                           		communication between Cisco Unity Connection and the phone system, providing
                           		access to various features such as:

Calls to a user extension that does not answer are forwarded to
                                 			 the personal greeting of the user.

Messages left for a user activate the message waiting indicator
                                 			 (MWI) on the extension.

A user has easy access to messages by pressing a button on the
                                 			 phone and entering a password.

Calls to a user extension that is busy are forwarded to the busy
                                 			 greeting of the user.

Unity Connection receives caller ID information from the phone
                                 			 system (if available).

Unity Connection identifies the user who leaves a message during
                                 			 a forwarded internal call, based on the extension from which the call
                                 			 originated.

To know more about integrating Unity Connection with phone system, see the “ Integrating Cisco Unity Connection with the Phone System ” chapter of Design Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html

After understanding how the Unity Connection integrates with a
                           		phone system, you need to configure and edit the settings for phone system,
                           		ports, port group, trunk, and security in Unity Connection.

## Phone System

Cisco Unity Connection Administration identify multiple phone systems that integrate Unity Connection with Cisco Unified Communications
                           Manager. For a matrix of supported combinations, see the Multiple Phone System Integration Guide for Cisco Unity Connection at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

A phone system has one or more port groups that further have voice messaging ports.

Cisco Business Edition does not support adding or deleting phone system integrations.

### Configuring Phone
                           	 System Integration

The settings for a phone system can be modified after it is
                                 		  integrated with Unity Connection. The phone system settings identify the phone
                                 		  system with which Unity Connection integrates and regulate certain phone system
                                 		  features. (Integration configuration settings are located in the port groups
                                 		  that belong to the phone system.)

You can delete a phone system if it is no
                                 		  longer used by Unity Connection. Before a phone system is deleted, make sure to
                                 		  delete or reassign all of the following objects that are associated with the
                                 		  phone system to another phone system:

- All users (including MWI devices and
                                    			 notification devices)

- All user templates

- All systems

- All
                                    			 call handler templates

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System .

The Search Phone System page displays the currently configured
                                             				phone system integrations.

The port count is zero for the newly configured phone systems.
                                                         				  After adding ports to the specific phone system, the port count shows the
                                                         				  number of available voice ports.

Step 2

Configure a phone system (For more information on each field,
                                          			 see Help> This Page):

- To create a new phone system, select Add New . On the New Phone System page, enter the values of
                                    			 the required fields and select Save.

- Phone System Basics. See Phone System Basics .

- Cisco Unified Communications Manager AXL
                                          				  Servers. See Cisco Unified Communications Manager AXL Servers .

- Phone System Associations. See Phone System Associations .

After editing the settings, select Save.

- To delete a phone system, check the check
                                    			 box adjacent to the display name of the phone system that you want to delete.
                                    			 Select Delete Selected and OK to confirm deletion.

### Phone System Settings

### Phone System Basics

If you created the phone system integration to use the same voice messaging port to turn on and off an MWI the Use Same Port
                                    for Enabling and Disabling MWIs check box is checked. You can disable this configuration without leaving MWIs on when there
                                    are no voice messages for the user by un checking the Use Same Port for Enabling and Disabling MWIs and Force All MWIs Off for This Phone System check boxes.

If you want to synchronize all the MWIs for a phone system without affecting MWIs on other phone systems, select Run in front of Synchronize All MWIs on This Phone System option.

If you want to change the call loop detection settings to enable or disable the types of calls that are checked, set the applicable
                                    settings in Call Loop Detection Using DTMF and select Save .

Call loop occurs when the forwarded Unity Connection calls (for example, to notify a user that a message has been received)
                                                sometimes return back to Unity Connection.

### Cisco Unified
                           	 Communications Manager AXL Servers

AXL servers are supported only for Cisco Unified CM phone
                                 		  systems and are needed when Unity Connection must have access to the Cisco
                                 		  Unified CM database for:

Importing Cisco Unified CM users (In a Unity Connection cluster
                                       				configuration, you must be signed in to the publisher server to import Cisco
                                       				Unified CM user data).

Changing certain phone settings for users of Unity Connection
                                       				personal call transfer rules.

Cisco
                                             						Unity Connection

Cisco
                                             						Unified Communications Manager

version

8.x

9.x

10.x

11.x

8.x

Yes

Yes

Yes

No

9.x 1

Yes

Yes

Yes

No

10.x

Yes

Yes

Yes

No

11.x

Yes

Yes

Yes

Yes

### Configuring an AXL
                           	 Server in Unity Connection

Step 1

In Cisco
                                          			 Unity Connection Administration, expand Telephony
                                             				Integrations and select Phone
                                             				System .

On the Phone
                                             				Systems Basics page of the selected Cisco Unified CM phone system, in the Edit
                                             				menu, select Cisco
                                                				  Unified Communications Manager AXL Servers .

Step 2

Configure an
                                          			 AXL server (For more information on each field, see Help> This Page):

On the
                                                   					 Edit AXL Servers page, in the AXL Servers field, select Add
                                                      						New . Enter the values of the required fields and select Save.

- Sign in to Cisco Unified CM
                                                      						Administration, expand System
                                                         						  and select Application Server .

- On the Find and List
                                                      						Application Servers page, select Find to display all application servers .

- In the Name column, select
                                                      						the name of the Unity Connection server.

- On the Application Server
                                                      						Configuration page, in the Available Application User field, select the Cisco
                                                      						Unified CM application user and move it to the Selected Application User field.
                                                      						Select Save.

On the
                                                   					 Edit AXL Servers page, select the AXL server that you want to edit. Enter the
                                                   					 values of the required fields and select Save.

On the
                                                   					 Edit AXL Servers page, in AXL Servers field, check the check box next to the
                                                   					 AXL server that you want to delete. Select Delete
                                                      						Selected and OK to confirm deletion .

### Phone System Associations

You can view the list of all Unity Connection users associated with the phone system by selecting the Phone System Associations
                              option on the Edit menu of Phone System Basics page.

## Port

The voice messaging ports allow Unity Connection to receive calls (for example, to record a message) and make calls (for example
                           to send message notifications or to set MWIs).

Each voice messaging port belongs to only one port group. Port groups have their own voice messaging ports.

Ports are no longer licensed in the Unity Connection server. The ports are now configurable as per the hardware of the server
                                       deployed for installing Unity Connection.

### Configuring Ports

Voice messaging ports provide the connections for
                                 		  calls between Unity Connection and the phone system. You can add voice
                                 		  messaging ports after the phone system has been created.

Cisco Business Edition
                                    			 only: Before you add ports, you must have existing voice messaging ports in
                                 		  Cisco Unified CM Administration that do not belong to a port group.

This section includes information on configuring
                                 		  a port group for Unity Connection, define the settings for the ports, and save
                                 		  them.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations and select Port .

The Search Ports page displays the currently
                                             				configured ports.

Step 2

Configure ports (For more information on
                                          			 each field, see Help> This Page):

To add a port:

On the Search Ports page, select Add New .

On the New Port page, enter the values of
                                       				the required settings and select Save .

In Cisco Unity Connection Administration, in
                                       				the Related Links list, select Check Telephony Configuration , and select Go to confirm the phone system
                                       				integration settings.

If the test is not successful, the Task
                                       				Execution Results list displays one or more messages with troubleshooting
                                       				steps. After correcting the problems, check the configuration again.

Verify that there are appropriate number of
                                       				ports set to answer calls and an appropriate number of ports are set to dial
                                       				out otherwise the integration may not function correctly. See the “Usage of
                                       				Voicemail Ports in Cisco Unity Connection” section of the applicable
                                       				Cisco Unity Connection integration guide at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

To edit an existing port:

On the Search Ports page, select a port that
                                       				you want to edit.

On the Port Basics page, enter the values of
                                       				the required fields and select Save .

To delete one or more ports:

On the Search Ports page, check the check
                                       				box next to the voice messaging ports that you want to delete.

Select Delete Selected and OK to confirm
                                       				deletion.

### Viewing the Port Certificate

Port certificates for voice messaging ports
                                 		  are used only by SCCP integrations with Cisco Unified Communications Manager
                                 		  6.x and later and are required for authentication of the Unity Connection voice
                                 		  messaging ports. You can view the port certificate that helps in
                                 		  troubleshooting authentication and encryption problems.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations and select Port .

Step 2

On the Search Ports page, select the display
                                          			 name of the voice messaging port for which you want to see the device
                                          			 certificate.

Step 3

On the Port Basics page, select View Certificate .

Step 4

In the View Port Certificate window, the
                                          			 information from the port device certificate is displayed.

## Port Group

Port Groups are assigned voice messaging ports that define Unity Connection integration configuration settings. Most of the
                           phone system integrations need only one port group. However, you may need multiple port groups in the following scenarios:

For integration with phone systems through PIMG/TIMG units, each PIMG/TIMG unit is connected to one port group with the applicable
                                 voice messaging ports. For example, a system that uses five PIMG units requires five port groups, one port group for each
                                 PIMG unit.

For integrations with other phone systems, an additional port group with its own voice messaging ports may be used for testing
                                 a new configuration or for troubleshooting.

Cisco Business Edition only: Before you can add a port group, you must have the existing voice messaging ports in Cisco Unified CM Administration, which
                           do not belong to a port group.

You can create a maximum of 90 port groups if you are using only TUI (touchtone conversation) and VUI (voice-recognition)
                                       features of Unity Connection. However, if you are using all the features of Unity Connection, you are allowed to create a
                                       maximum of 60 port groups.

You can change the settings of a port group, which affects only the voice messaging ports of that port group. When you delete
                           a port group, any voice messaging port belonging to that port group are deleted at the same time. However, the phone system
                           to which the port group belongs is not deleted.

### Configuring Port
                           	 Group

This section includes information on configuring a port group
                                 		  for Unity Connection, define the settings of the port group, and save them.

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group .

The Search Port Groups page displays the currently configured
                                             				port groups.

Step 2

Configure port groups (For more information on each field, see
                                          			 Help> This Page):

To add a port group:

On the Search Port Groups page, select Add New.

On the New Port Group page, enter the values of the required
                                       				fields and select Save .

To edit a port group:

On the Search Port Groups page, select the port group name that
                                       				you want to edit.

On the Port Group Basics page, select Edit and change any of the
                                       				following settings:

Port Group Basics. For information, see Phone System Basics .

Servers. For information, see Servers .

Advanced Settings. For information, see Advanced Settings .

Codec Advertising. For information, see Codec Advertising .

Select Save after editing the settings.

To delete a port group:

On the Search Port Groups page, check the check box next to the
                                       				port group name of the port groups that you want to delete.

Select Delete Selected and OK to confirm deletion.

### Port Group Settings

You can change the settings of a port group after it has been added. Changes to the settings affect only the voice messaging
                              ports that belong to the port group.

#### Port Group Basics

##### Message Waiting Indicators (MWI)

An MWI is a flashing LCD panel or special dial tone on user phones, which allows the user to know that a voice message is
                                    waiting. The type of indicator depends on the phone system and the user phones. Phone systems that support message counts
                                    may also display the number of messages that the user has.

To change the MWI settings, on the Port Group Basics page of a selected port group, change the applicable settings in Message
                                    Waiting Indicator Settings and select Save .

##### Session Initiation Protocol (SIP) Settings

You can change the SIP settings after the phone system integration has been created.

Cisco Business Edition does not support phone system integrations that use SIP.

To change the SIP settings, on the Port Group Basics page of a selected port group, change the applicable settings in Session
                                    Initiation Protocol (SIP) Settings and select Save .

#### Servers

##### Cisco Unified Communications Manager Servers

For Cisco Unified Communications Manager integrations, Related Links helps you to integrate with one Cisco Unified CM server
                                    only. The secondary Cisco Unified CM server in the cluster must be added after the integration is completed. You can change
                                    the Cisco Unified CM server settings after the server has been added.

You can delete a Cisco Unified Communications Manager server when it is no longer used by the phone system integration. If
                                    you want to move a Cisco Unified CM server to another port group, you must delete the Cisco Unified CM server from one port
                                    group and add it to the second port group.

Cisco Business Edition does not support adding or deleting secondary Cisco Unified CM servers.

##### Configuring Cisco Unified Communications Manager Server

Step 1

In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations and select Port Group .

The Search Port Groups page displays the
                                                   				currently configured Cisco Unified CM servers. On the Port Group Basics page of
                                                   				a selected port group, select Edit and select Servers.

Step 2

Configure a Cisco Unified Communications Manager Server (For
                                                			 information on each field, see Help> This Page):

To add a secondary Cisco Unified CM
                                                         					 server, on the Edit Servers page, in the Cisco Unified Communications Manager
                                                         					 Servers list, select Add. Enter the values of the required fields and select
                                                         					 Save.

To edit a Cisco Unified CM server, on
                                                         					 the Edit Servers page, in Cisco Unified Communications Manager Servers, enter
                                                         					 the values of the required fields and select Save.

To delete a Cisco Unified CM server, in
                                                         					 Cisco Unified Communications Manager Servers, check the check box next to the
                                                         					 Cisco Unified CM servers that you want to delete. Select Delete Selected and OK to confirm the deletion.

##### TFTP Servers

For Cisco Unified Communications Manager integrations, TFTP servers are required only when the Cisco Unified CM cluster uses
                                    authentication and encryption for the Unity Connection voice messaging ports. You must add a TFTP server after you create
                                    the Cisco Unified CM phone system integration.

You can change the TFTP server settings after the server has been added. You can also delete a TFTP server when it is no longer
                                    used by the port group.

##### Configuring a TFTP Server in Unity Connection

Step 1

In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations and select Port Group .

The Search Port Groups page displays the
                                                   				currently configured TFTP servers.On the Port Group Basics page of a selected
                                                   				port group, select Edit> Servers.

Step 2

Configure a TFTP server (For more information on each field, see
                                                			 Help> This Page):

To add a TFTP server:

On the Edit Servers page, in the TFTP
                                                         					 Servers field, select Add .

Enter the values of the required fields
                                                         					 and select Save .

To edit a TFTP server:

On the Edit Servers page, in TFTP
                                                         					 Servers, enter the values of the required fields and select Save .

To delete a TFTP server:

On the Edit Servers page, in TFTP Servers, check the
                                                               						  checkbox next to the TFTP server that you want to delete.

- Select Delete Selected and OK to confirm the deletion.

##### SIP Server

For a phone system integration with Cisco Unified Communications Manager through a SIP trunk or with another SIP server, you
                                    can add SIP server after the phone system has been created. You can change the SIP server settings after the server has been
                                    added. A SIP server can be deleted if it is no longer used by a port group.

Cisco Business Edition does not support SIP servers.

##### Configuring a SIP
                                 	 Server

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group .

Step 2

Configure a SIP server (For more information on each field, see
                                                			 Help> This Page):

- On the Edit
                                                            						Servers page, in the SIP Servers field, select Add .

- Enter the values
                                                            						of the required fields and select Save .

- On the Edit
                                                            						Servers page, in the SIP Servers field, select the SIP server you want to edit.

- Change the values
                                                            						of the required fields and select Save .

- On the Edit
                                                            						Servers page, in the SIP Servers field, check the check box next to the SIP
                                                            						server that you want to delete.

Delete Selected

OK to confirm deletion.

##### PIMG/TIMG
                                 	 Units

If the phone systems are integrated through PIMG/TIMG units,
                                    		each PIMG/TIMG unit is created in a separate port group. You can add, change,
                                    		or delete PIMG/TIMG units after the phone system integration has been created.

In Unity Connection, integration with multiple phone systems is
                                                		  supported only with Cisco Business Edition 6000/7000.

##### Configuring
                                 	 PIMG/TIMG Units

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group .

Step 2

Configure a PIMG/TIMG unit (For more information on each field,
                                                			 see Help> This Page):

To add a PIMG/TIMG unit, in Port Group Search Results, select Add New . On the New Port Group page, in the Phone System
                                                         					 field, select the phone system for which you want to add a PIMG/TIMG unit.
                                                         					 Enter the applicable settings and select Save .

To edit a PIMG/TIMG unit, select the display name of the port
                                                         					 group for which you want to change PIMG/TIMG settings. On the Port Group Basics
                                                         					 page, in PIMG Settings, enter the applicable settings and select Save .

To delete a PIMG/TMG unit, in Port Group Search Results, check
                                                         					 the check box next to the port group for the PIMG/TIMG unit that you want to
                                                         					 delete. Select Delete Selected and then select OK to confirm deletion.

#### Advanced Settings

The port group advanced
                                 		settings control the settings that are not often used, such as delays and MWI
                                 		usage. Do not change the default values of port group advanced settings.

Normalization controls automatic volume
                                 		adjustments for recording messages. For enabling or disabling normalization,
                                 		make sure to leave normalization enabled and do not change the value of the
                                 		Target Decibel Level for Recordings and Messages field in System Settings > General Configuration .

##### Editing Port Group Advanced Settings

Step 1

In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations ,
                                                			 and then select Port Group .

On the Search Port Groups page, select the
                                                   				display name of the port group for which you want to change the advanced
                                                   				settings.

Step 2

On the Port Group Basics page, on the Edit menu, select Advanced Settings and do
                                                			 the following:

To edit a port group, change the
                                                         					 applicable settings in Port Group Advanced Settings and select Save .

To enable or disable normalization,
                                                         					 change the applicable settings in Audio Normalization for Recordings and
                                                         					 Messages and select Save .

#### Codec Advertising

For calls, Unity Connection advertises the audio or video format (or codec) that is preferred for the media stream with the
                                 phone system.

For the following reasons, Unity Connection should use the same audio or video format for the media stream that the phone
                                 system uses:

To reduce the need for transcoding the media stream from one audio or video format to another.

To minimize the performance impact on the Unity Connection server and on the phone system.

To preserve the audio or video quality of calls.

When Unity Connection advertises a different audio or video format other than the one used by the phone system, the phone
                                 system transcodes the media stream.

##### Changing the Audio
                                 	 or Video Format Used for Calls

Step 1

In Cisco Unity Connection Administration, expand Telephony
                                                			 Integrations, and then select Port Group.

Step 2

On the Search Port Groups page, select the port group that
                                                			 belongs to the phone system integration for which you want to change the audio
                                                			 or video format of the media stream.

Step 3

On the Port Group Basics page, select Edit, and then select
                                                			 Codec Advertising.

Step 4

On the Edit Codec Advertising page, select the Up and Down
                                                			 arrows to move the codec between the Advertised Codec box and the Unadvertised
                                                			 Codecs box, and then select Save.

Step 5

(Only SIP integrations) If you want to change the packet size
                                                			 that is used by the advertised codecs, select the applicable packet setting for
                                                			 each codec in the Packet Size list, and then select Save.

## Trunk

When multiple phone systems are integrated with Cisco Unity Connection, you can configure a phone system trunk so that calls
                           on one phone system can be transferred to extensions on another phone system. Phone system trunks are accessed by dialing
                           extra digits (for example, dialing 9) before dialing the extension.

Cisco Business Edition does not support phone system trunks.

### Configuring Trunk

If another phone system
                                 		  integration exists, you can add a phone system trunk to provide access of calls
                                 		  from one phone system to extensions on the other phone system. You can add
                                 		  phone system trunks after the phone system integration has been created.

Phone system
                                 		  trunk settings cannot be changed. However, you can delete the phone system
                                 		  trunk that you want to change and add a new phone system trunk with the
                                 		  settings that you want. A phone system trunk can be deleted when it is no
                                 		  longer used by a phone system integration.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 and then select Trunk .

The Search Phone System Trunks page displays
                                             				the currently configured phone system trunks.

Step 2

Configure a phone system trunk (For
                                          			 information on each field, see Help> This Page):

To add a new phone system trunk, in
                                                				  Phone System Trunk Search Results, select Add New . On the New Phone System
                                                				  Trunk page, enter the applicable settings and select Save .

To delete a phone system trunk, in Phone
                                                				  System Trunk Search Results, check the check box next to the phone system trunk
                                                				  that you want to delete. Select Delete Selected . Select OK to
                                                				  confirm deletion.

## Speech Connect
                        	 Port

Speech Connect uses voice-enabled directory handlers that allow
                           		both the employees and outside callers to speak the name of an employee and
                           		instantly get connected, without navigating to an audio-text tree, and without
                           		knowing the extension of the employee. For easy access, you can configure a
                           		Speech Connect speed dial on user phones.

Speech Connect port can be configured as per the hardware
                           		profile of the virtual machine deployed for installing Unity Connection.

### Configuring a Speech Connect Port

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations, and then select Speech Connect Port.

The Speech Connect Port Configuration page
                                             				displays the currently configured speech connect ports.

Step 2

In New Speech Connect Port, select the Unity Connection server
                                          			 from the Server drop down list and in the Number of Ports field, enter the
                                          			 number of Speech Connect ports that you want to configure.

Step 3

Select Save.

## Audio and Video
                        	 Format Using Phone

Cisco Unity
                           		Connection advertises the audio format (or codec) that is preferred for the
                           		media stream with the phone system.

Consider the following when setting the audio format:

When Unity Connection advertises a different audio format than
                                 			 the one used by the phone system, the phone system transcodes the media stream.

Unity Connection should use the same audio format for the media
                                 			 stream that the phone system uses for the following reasons:

To reduce the need for transcoding the media stream from one
                                       				  audio format to another.

To minimize the performance impact on the Unity Connection
                                       				  server and on the phone system.

To preserve the audio quality of the calls.

For more information on audio format codecs, see the “Audio Codecs” section in the “Sizing and Scaling Cisco Unity Connection
                           Servers” chapter of the Design Guide for Cisco Unity Connection available at, https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg.html .

### Configuring the
                           	 Audio and Video Format

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations , and then select Port Group .

Step 2

On the Search Port Groups page, select the port group that
                                          			 belongs to the phone system integration for which you want to change the audio
                                          			 format of the media stream.

Step 3

On the Port Group Basics page, on the Edit menu, select Codec Advertising .

Step 4

On the Edit Codec Advertising page, select the Up and Down
                                          			 arrows to change the order of the codecs or to move codecs between the
                                          			 Advertised Codec box and the Unadvertised Codecs box.

If only one codec is in the Advertised Codecs box, Cisco Unity
                                             				Connection sends the media stream in that audio format. The phone system
                                             				transcodes if it does not use this audio format.

If two or more codecs are in the Advertised Codecs box, Unity
                                             				Connection advertises its preference for the first codec in the list. It sends
                                             				the media stream in the audio format from the list that the phone system
                                             				selects.

Step 5

Select Save .

Step 6

(All integrations except SCCP) If you want to change the
                                          			 packet size that is used by the advertised codecs, on the Port Group Basics
                                          			 page, under Advertised Codec Settings, select the applicable packet setting for
                                          			 each codec in the Packet Size list, and select Save .

Step 7

(Only SIP integrations) If you want to change the packet size
                                          			 that is used by the advertised codecs, on the Port Group Basics page, under
                                          			 Advertised Codec Settings, select the applicable packet setting for each codec
                                          			 in the Packet Size list, and select Save.

For both the audio and video calls, change the packet size for the codecs G711, G729, and G722 in Cisco Unified Communications
                                             Manager and the remaining codecs is changed in Cisco Unity Connection Administration.

In SIP integration, you can also send comfort noise packets through telephony. For information on how to send comfort noise
                                                         packets, see Configuring Unity Connection to Send Noise Packets section.

Step 8

On the Port Group menu, select Search Port Groups .

Step 9

Repeat Step 2 through Step 8 for all remaining port groups that
                                          			 belong to the phone system integration for which you want to change the audio
                                          			 format of the media stream.

#### Configuring Unity Connection to Send Comfort Noise Packets every second during Record

In SIP integration, you can configure Unity Connection to send comfort noise packets through telephony interface. Do the following
                                    procedure for configuring Unity Connection to send comfort noise packets:

Step 1

In Cisco Unity Connection Administration, navigate System Settings > Advanced > Telephony . On the Telephony Configuration page, check the Vad Enabled check box.

By default, VAD is enabled on the system.

Step 2

Execute below CLI command:

```
run cuc dbquery unitydirdb execute procedure csp_configurationmodify(pfullname='System.Mixer.EnableSendSIDPacketsDuringRecord',pvaluebool=1)
```

Step 3

Restart Connection Mixer service for the changes to take effect.

Caution

It is recommended to peform the given steps during off peak hours as it require restart of a "Connection Mixer" critical service.

In case of a cluster, execute CLI command only on publisher server and make sure that database replication is working fine
                                                      for the cluster.

Restart the Connection Mixer service on both the nodes.

### Configuring Unity Connection to clean up Inactive Calls caused by Phone Inactivity

Cisco Unity Connection can be configured to clean up the inactive call after five minutes of phone inactivity to conserve
                                 resources.

Enabling this configuration helps prevent the ports from congestion by performing call cleanup for inactive and unresponsive
                                 endpoints. It also reduces the frequency of ICMP floods caused by such endpoints . Do the following procedure for configuring
                                 Unity Connection to activate this behavior :

Step 1

The configuration is disabled by default. To enable it, execute the following CLI command :

```
run cuc dbquery unitydirdb execute procedure csp_configurationmodify(pfullname='System.Mixer.EnableEpInactivityDetection',pvaluebool=1)
```

Step 2

Restart the Connection Mixer service for the changes to take effect.

Caution

It is recommended to perform the given steps during off hours as it require restart of a Connection Mixer service.

In case of a cluster, execute CLI command only on publisher node and make sure that database replication is working fine for
                                                   the cluster.

Restart the Connection Mixer service on both the nodes of cluster.

## Security

Certificates and security profile can be managed when Cisco Unified Communications Manager authentication and encryption is
                           configured for Unity Connection voice messaging ports.

### Viewing and Saving Unity Connection Root Certificate

The root certificate is used by SCCP integrations with Cisco Unified Communications Manager 7.x and later and SIP trunk integrations
                              with Cisco Unified CM 7.0 and later. It is required for authentication of the Unity Connection voice messaging ports. You
                              can view the root certificate that helps in troubleshooting authentication and encryption problems.

#### Viewing and Save
                              	 the Unity Connection Root Certificate

Step 1

In Cisco Unity Connection Administration, expand Telephony Integrations > Security , and then select Root Certificate .

Step 2

To view the root certificate, on the View Root Certificate page,
                                             			 the information from the root certificate is displayed.

Step 3

To save the root certificate as a file, on the View Root
                                             			 Certificate page, right-click the Right-Click to Save the Certificate as a File link,
                                             			 and select Save Target As .

In the Save As dialog box, browse to the location where you want
                                                   				  to save the Unity Connection root certificate as a file and in the File Name
                                                   				  field, confirm that the extension is .pem (rather than .htm) for Cisco
                                                   				  Unified CM 5.x or later. Select Save .

Caution

In the Download Complete dialog box, select Close . The Unity Connection root certificate file is ready
                                                   				  to be copied to all Cisco Unified CM servers in this Cisco Unified CM phone
                                                   				  system integration. For instructions, see the applicable Cisco Unified CM
                                                   				  integration guide at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

### Configuring a SIP Security Profile (Cisco Unified Communications Manager SIP Trunk Integrations Only)

The SIP security profile is used only by SIP trunk integrations with Cisco Unified CM 7.0 and later, and is required for authentication
                              of the Unity Connection voice messaging ports. You can change a SIP security profile after it is created. You can delete a
                              SIP security profile when the Cisco Unified CM server is no longer configured for authentication of the Unity Connection voice
                              messaging ports.

#### Adding a SIP Security Profile (Cisco Unified Communications Manager
                              	 SIP Trunk Integrations Only

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Telephony
                                                   				  Integrations > Security , and then select SIP Security Profile .

The Search SIP Security Profiles page
                                                				displays the currently configured SIP security profiles.

Step 2

Configure a SIP security profile (For information, see Help>
                                             			 This Page):

To add a SIP security profile:

On the Search SIP Security Profiles
                                                      					 page, select Add New .

On the New SIP Security Profile page, in
                                                      					 the Port field, enter the port number that the Cisco Unified CM server uses for
                                                      					 SIP trunk authentication and encryption of the voice messaging ports.

To encrypt the call signaling messages,
                                                      					 check the Do TLS check box and select Save .

To edit a SIP security profile:

On the Search SIP Security Profiles
                                                      					 page, select the name of the SIP security profile that you want to edit.

On the Edit SIP Security Profile page,
                                                      					 enter the applicable settings and select Save .

To delete a SIP security profile:

On the Search SIP Security Profiles
                                                      					 page, check the check box next to the display name of the SIP security profile
                                                      					 that you want to delete.

Select Delete Selected and then select
                                                      					 OK.

## IPv6 in Unity
                        	 Connection (Cisco Unified Communications Manager Integrations Only)

Unity Connection supports IPv6
                           		addressing with Cisco Unified Communications Manager phone system integrations
                           		using SCCP or SIP:

IPv6 support is disabled by default. When you enable IPv6, you
                                 			 can configure Unity Connection to obtain an IPv6 address either through router
                                 			 advertisement, through DHCP, or by manually configuring an address. You can
                                 			 also configure the mode in which Unity Connection listens for incoming
                                 			 traffic—IPv4, IPv6, or both IPv4 and IPv6.

For SCCP integrations with Cisco Unified CM, if Unity Connection
                                 			 is configured to listen for the incoming IPv4 and IPv6 traffic, you can
                                 			 configure the addressing mode that Unity Connection uses for call control
                                 			 signaling for each port group to use either IPv4 or IPv6. (This mode is also
                                 			 used when connecting to a TFTP server.)

For SIP integrations with Cisco Unified CM, if Unity Connection
                                 			 is configured to listen for the incoming IPv4 and IPv6 traffic, you can
                                 			 configure the addressing mode that Unity Connection uses for call control
                                 			 signaling for each port group to use either IPv4 or IPv6. (This mode is also
                                 			 used when connecting to a TFTP server.) In addition, you can configure the
                                 			 addressing mode that Unity Connection uses for media for each port group to use
                                 			 either IPv4 or IPv6.

For instructions on enabling and configuring IPv6 for an existing Cisco Unified CM integration, see the “ Upgrading Cisco Unity Connection ” chapter in Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

For instructions on enabling and configuring IPv6 while setting
                           		up a new Cisco Unified CM integration, see the applicable Cisco Unified CM
                           		integration guide at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

| Note | Cisco Business Edition does not support adding or deleting phone system integrations. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Phone System . The Search Phone System page displays the currently configured
                                             				phone system integrations. Note The port count is zero for the newly configured phone systems.
                                                         				  After adding ports to the specific phone system, the port count shows the
                                                         				  number of available voice ports. | Note | The port count is zero for the newly configured phone systems.
                                                         				  After adding ports to the specific phone system, the port count shows the
                                                         				  number of available voice ports. |
|---|---|---|---|
| Note | The port count is zero for the newly configured phone systems.
                                                         				  After adding ports to the specific phone system, the port count shows the
                                                         				  number of available voice ports. |
| Step 2 | Configure a phone system (For more information on each field,
                                          			 see Help> This Page): |

| Note | The port count is zero for the newly configured phone systems.
                                                         				  After adding ports to the specific phone system, the port count shows the
                                                         				  number of available voice ports. |
|---|---|

| Note | Call loop occurs when the forwarded Unity Connection calls (for example, to notify a user that a message has been received)
                                                sometimes return back to Unity Connection. |
|---|---|

| Cisco
                                             						Unity Connection | Cisco
                                             						Unified Communications Manager |  |
|---|---|---|
| version | 8.x | 9.x | 10.x | 11.x |
| 8.x | Yes | Yes | Yes | No |
| 9.x 1 | Yes | Yes | Yes | No |
| 10.x | Yes | Yes | Yes | No |
| 11.x | Yes | Yes | Yes | Yes |

| Note | AXL servers are
                                          		  not supported for Cisco Unified Communications Manager Express integrations or
                                          		  Cisco Business Edition. |
|---|---|

| Step 1 | In Cisco
                                          			 Unity Connection Administration, expand Telephony
                                             				Integrations and select Phone
                                             				System . On the Phone
                                             				Systems Basics page of the selected Cisco Unified CM phone system, in the Edit
                                             				menu, select Cisco
                                                				  Unified Communications Manager AXL Servers . |
|---|---|
| Step 2 | Configure an
                                          			 AXL server (For more information on each field, see Help> This Page): To add an AXL server: On the
                                                   					 Edit AXL Servers page, in the AXL Servers field, select Add
                                                      						New . Enter the values of the required fields and select Save. Note Make
                                                            					 sure that the username entered on Edit AXL Server page must match the username
                                                            					 of a Cisco Unified CM application user who is assigned to the "Standard AXL API
                                                            					 Access" role. Also, the password must match the password of the Cisco Unified
                                                            					 CM application username. To add a corresponding
                                                				  application server in Cisco Unified CM: Sign in to Cisco Unified CM
                                                      						Administration, expand System
                                                         						  and select Application Server . On the Find and List
                                                      						Application Servers page, select Find to display all application servers . In the Name column, select
                                                      						the name of the Unity Connection server. On the Application Server
                                                      						Configuration page, in the Available Application User field, select the Cisco
                                                      						Unified CM application user and move it to the Selected Application User field.
                                                      						Select Save. To edit an AXL server
                                                				  integration: On the
                                                   					 Edit AXL Servers page, select the AXL server that you want to edit. Enter the
                                                   					 values of the required fields and select Save. To delete an AXL server: On the
                                                   					 Edit AXL Servers page, in AXL Servers field, check the check box next to the
                                                   					 AXL server that you want to delete. Select Delete
                                                      						Selected and OK to confirm deletion . | Note | Make
                                                            					 sure that the username entered on Edit AXL Server page must match the username
                                                            					 of a Cisco Unified CM application user who is assigned to the "Standard AXL API
                                                            					 Access" role. Also, the password must match the password of the Cisco Unified
                                                            					 CM application username. |
| Note | Make
                                                            					 sure that the username entered on Edit AXL Server page must match the username
                                                            					 of a Cisco Unified CM application user who is assigned to the "Standard AXL API
                                                            					 Access" role. Also, the password must match the password of the Cisco Unified
                                                            					 CM application username. |

| Note | Make
                                                            					 sure that the username entered on Edit AXL Server page must match the username
                                                            					 of a Cisco Unified CM application user who is assigned to the "Standard AXL API
                                                            					 Access" role. Also, the password must match the password of the Cisco Unified
                                                            					 CM application username. |
|---|---|

| Note | Ports are no longer licensed in the Unity Connection server. The ports are now configurable as per the hardware of the server
                                       deployed for installing Unity Connection. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations and select Port . The Search Ports page displays the currently
                                             				configured ports. |
|---|---|
| Step 2 | Configure ports (For more information on
                                          			 each field, see Help> This Page): |

| Note | (Applicable to Release 15 SU2 or later) Authenticated Security mode is not supported on the Unity Connection server when the minimum TLS version is configured as
                                          1.3. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations and select Port . |
|---|---|
| Step 2 | On the Search Ports page, select the display
                                          			 name of the voice messaging port for which you want to see the device
                                          			 certificate. |
| Step 3 | On the Port Basics page, select View Certificate . |
| Step 4 | In the View Port Certificate window, the
                                          			 information from the port device certificate is displayed. |

| Note | You can create a maximum of 90 port groups if you are using only TUI (touchtone conversation) and VUI (voice-recognition)
                                       features of Unity Connection. However, if you are using all the features of Unity Connection, you are allowed to create a
                                       maximum of 60 port groups. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group . The Search Port Groups page displays the currently configured
                                             				port groups. |
|---|---|
| Step 2 | Configure port groups (For more information on each field, see
                                          			 Help> This Page): |

| Note | (Applicable to Release 15 SU2 or later) Authenticated Security mode is not supported on the Unity Connection server when the minimum TLS version is configured as
                                          1.3. |
|---|---|

| Note | Cisco Business Edition does not support phone system integrations that use SIP. |
|---|---|

| Note | Cisco Business Edition does not support adding or deleting secondary Cisco Unified CM servers. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations and select Port Group . The Search Port Groups page displays the
                                                   				currently configured Cisco Unified CM servers. On the Port Group Basics page of
                                                   				a selected port group, select Edit and select Servers. |
|---|---|
| Step 2 | Configure a Cisco Unified Communications Manager Server (For
                                                			 information on each field, see Help> This Page): To add a secondary Cisco Unified CM
                                                         					 server, on the Edit Servers page, in the Cisco Unified Communications Manager
                                                         					 Servers list, select Add. Enter the values of the required fields and select
                                                         					 Save. To edit a Cisco Unified CM server, on
                                                         					 the Edit Servers page, in Cisco Unified Communications Manager Servers, enter
                                                         					 the values of the required fields and select Save. To delete a Cisco Unified CM server, in
                                                         					 Cisco Unified Communications Manager Servers, check the check box next to the
                                                         					 Cisco Unified CM servers that you want to delete. Select Delete Selected and OK to confirm the deletion. |

| Step 1 | In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations and select Port Group . The Search Port Groups page displays the
                                                   				currently configured TFTP servers.On the Port Group Basics page of a selected
                                                   				port group, select Edit> Servers. |
|---|---|
| Step 2 | Configure a TFTP server (For more information on each field, see
                                                			 Help> This Page): To add a TFTP server: On the Edit Servers page, in the TFTP
                                                         					 Servers field, select Add . Enter the values of the required fields
                                                         					 and select Save . To edit a TFTP server: On the Edit Servers page, in TFTP
                                                         					 Servers, enter the values of the required fields and select Save . To delete a TFTP server: On the Edit Servers page, in TFTP Servers, check the
                                                               						  checkbox next to the TFTP server that you want to delete. Select Delete Selected and OK to confirm the deletion. |

| Note | Cisco Business Edition does not support SIP servers. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group . The Search Port Groups page displays the currently configured SIP
                                                			 servers.On the Port Group Basics page of a selected port group, select Edit and
                                                			 then select Servers. |
|---|---|
| Step 2 | Configure a SIP server (For more information on each field, see
                                                			 Help> This Page): To add a SIP server: On the Edit
                                                            						Servers page, in the SIP Servers field, select Add . Enter the values
                                                            						of the required fields and select Save . To edit a SIP server: On the Edit
                                                            						Servers page, in the SIP Servers field, select the SIP server you want to edit. Change the values
                                                            						of the required fields and select Save . To delete a SIP
                                                      				  server: On the Edit
                                                            						Servers page, in the SIP Servers field, check the check box next to the SIP
                                                            						server that you want to delete. Select Delete Selected and OK to confirm deletion. |

| Note | In Unity Connection, integration with multiple phone systems is
                                                		  supported only with Cisco Business Edition 6000/7000. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations and select Port Group . The Search Port Groups page displays the currently configured
                                                			 PIMG/ TIMG units. |
|---|---|
| Step 2 | Configure a PIMG/TIMG unit (For more information on each field,
                                                			 see Help> This Page): To add a PIMG/TIMG unit, in Port Group Search Results, select Add New . On the New Port Group page, in the Phone System
                                                         					 field, select the phone system for which you want to add a PIMG/TIMG unit.
                                                         					 Enter the applicable settings and select Save . To edit a PIMG/TIMG unit, select the display name of the port
                                                         					 group for which you want to change PIMG/TIMG settings. On the Port Group Basics
                                                         					 page, in PIMG Settings, enter the applicable settings and select Save . To delete a PIMG/TMG unit, in Port Group Search Results, check
                                                         					 the check box next to the port group for the PIMG/TIMG unit that you want to
                                                         					 delete. Select Delete Selected and then select OK to confirm deletion. |

| Step 1 | In Cisco Unity Connection Administration,
                                                			 expand Telephony Integrations ,
                                                			 and then select Port Group . On the Search Port Groups page, select the
                                                   				display name of the port group for which you want to change the advanced
                                                   				settings. |
|---|---|
| Step 2 | On the Port Group Basics page, on the Edit menu, select Advanced Settings and do
                                                			 the following: To edit a port group, change the
                                                         					 applicable settings in Port Group Advanced Settings and select Save . To enable or disable normalization,
                                                         					 change the applicable settings in Audio Normalization for Recordings and
                                                         					 Messages and select Save . |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony
                                                			 Integrations, and then select Port Group. |
|---|---|
| Step 2 | On the Search Port Groups page, select the port group that
                                                			 belongs to the phone system integration for which you want to change the audio
                                                			 or video format of the media stream. |
| Step 3 | On the Port Group Basics page, select Edit, and then select
                                                			 Codec Advertising. |
| Step 4 | On the Edit Codec Advertising page, select the Up and Down
                                                			 arrows to move the codec between the Advertised Codec box and the Unadvertised
                                                			 Codecs box, and then select Save. |
| Step 5 | (Only SIP integrations) If you want to change the packet size
                                                			 that is used by the advertised codecs, select the applicable packet setting for
                                                			 each codec in the Packet Size list, and then select Save. |

| Note | Cisco Business Edition does not support phone system trunks. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 and then select Trunk . The Search Phone System Trunks page displays
                                             				the currently configured phone system trunks. |
|---|---|
| Step 2 | Configure a phone system trunk (For
                                          			 information on each field, see Help> This Page): To add a new phone system trunk, in
                                                				  Phone System Trunk Search Results, select Add New . On the New Phone System
                                                				  Trunk page, enter the applicable settings and select Save . To delete a phone system trunk, in Phone
                                                				  System Trunk Search Results, check the check box next to the phone system trunk
                                                				  that you want to delete. Select Delete Selected . Select OK to
                                                				  confirm deletion. |

| Note | By default Unity Connection provide two system generated Speech Connect ports. These ports are not mapped to actual licenses.
                                    To use Speech Connect Port functionality properly, you must install proper licenses on Prime License Manager. For more information
                                    on the Licenses, see " Managing Licenses " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html available at |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations, and then select Speech Connect Port. The Speech Connect Port Configuration page
                                             				displays the currently configured speech connect ports. |
|---|---|
| Step 2 | In New Speech Connect Port, select the Unity Connection server
                                          			 from the Server drop down list and in the Number of Ports field, enter the
                                          			 number of Speech Connect ports that you want to configure. |
| Step 3 | Select Save. |

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations , and then select Port Group . |
|---|---|
| Step 2 | On the Search Port Groups page, select the port group that
                                          			 belongs to the phone system integration for which you want to change the audio
                                          			 format of the media stream. |
| Step 3 | On the Port Group Basics page, on the Edit menu, select Codec Advertising . |
| Step 4 | On the Edit Codec Advertising page, select the Up and Down
                                          			 arrows to change the order of the codecs or to move codecs between the
                                          			 Advertised Codec box and the Unadvertised Codecs box. If only one codec is in the Advertised Codecs box, Cisco Unity
                                             				Connection sends the media stream in that audio format. The phone system
                                             				transcodes if it does not use this audio format. If two or more codecs are in the Advertised Codecs box, Unity
                                             				Connection advertises its preference for the first codec in the list. It sends
                                             				the media stream in the audio format from the list that the phone system
                                             				selects. |
| Step 5 | Select Save . |
| Step 6 | (All integrations except SCCP) If you want to change the
                                          			 packet size that is used by the advertised codecs, on the Port Group Basics
                                          			 page, under Advertised Codec Settings, select the applicable packet setting for
                                          			 each codec in the Packet Size list, and select Save . |
| Step 7 | (Only SIP integrations) If you want to change the packet size
                                          			 that is used by the advertised codecs, on the Port Group Basics page, under
                                          			 Advertised Codec Settings, select the applicable packet setting for each codec
                                          			 in the Packet Size list, and select Save. For both the audio and video calls, change the packet size for the codecs G711, G729, and G722 in Cisco Unified Communications
                                             Manager and the remaining codecs is changed in Cisco Unity Connection Administration. Note In SIP integration, you can also send comfort noise packets through telephony. For information on how to send comfort noise
                                                         packets, see Configuring Unity Connection to Send Noise Packets section. | Note | In SIP integration, you can also send comfort noise packets through telephony. For information on how to send comfort noise
                                                         packets, see Configuring Unity Connection to Send Noise Packets section. |
| Note | In SIP integration, you can also send comfort noise packets through telephony. For information on how to send comfort noise
                                                         packets, see Configuring Unity Connection to Send Noise Packets section. |
| Step 8 | On the Port Group menu, select Search Port Groups . |
| Step 9 | Repeat Step 2 through Step 8 for all remaining port groups that
                                          			 belong to the phone system integration for which you want to change the audio
                                          			 format of the media stream. |

| Note | In SIP integration, you can also send comfort noise packets through telephony. For information on how to send comfort noise
                                                         packets, see Configuring Unity Connection to Send Noise Packets section. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, navigate System Settings > Advanced > Telephony . On the Telephony Configuration page, check the Vad Enabled check box. Note By default, VAD is enabled on the system. | Note | By default, VAD is enabled on the system. |
|---|---|---|---|
| Note | By default, VAD is enabled on the system. |
| Step 2 | Execute below CLI command: run cuc dbquery unitydirdb execute procedure csp_configurationmodify(pfullname='System.Mixer.EnableSendSIDPacketsDuringRecord',pvaluebool=1) |
| Step 3 | Restart Connection Mixer service for the changes to take effect. |

| Note | By default, VAD is enabled on the system. |
|---|---|

| Caution | It is recommended to peform the given steps during off peak hours as it require restart of a "Connection Mixer" critical service. |
|---|---|

| Note | In case of a cluster, execute CLI command only on publisher server and make sure that database replication is working fine
                                                      for the cluster. Restart the Connection Mixer service on both the nodes. |
|---|---|

| Step 1 | The configuration is disabled by default. To enable it, execute the following CLI command : run cuc dbquery unitydirdb execute procedure csp_configurationmodify(pfullname='System.Mixer.EnableEpInactivityDetection',pvaluebool=1) |
|---|---|
| Step 2 | Restart the Connection Mixer service for the changes to take effect. |

| Caution | It is recommended to perform the given steps during off hours as it require restart of a Connection Mixer service. |
|---|---|

| Note | In case of a cluster, execute CLI command only on publisher node and make sure that database replication is working fine for
                                                   the cluster. Restart the Connection Mixer service on both the nodes of cluster. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Telephony Integrations > Security , and then select Root Certificate . |
|---|---|
| Step 2 | To view the root certificate, on the View Root Certificate page,
                                             			 the information from the root certificate is displayed. |
| Step 3 | To save the root certificate as a file, on the View Root
                                             			 Certificate page, right-click the Right-Click to Save the Certificate as a File link,
                                             			 and select Save Target As . In the Save As dialog box, browse to the location where you want
                                                   				  to save the Unity Connection root certificate as a file and in the File Name
                                                   				  field, confirm that the extension is .pem (rather than .htm) for Cisco
                                                   				  Unified CM 5.x or later. Select Save . Caution The certificate must be saved as a file with
                                                               					 the correct extension otherwise Cisco Unified CM does not recognize the
                                                               					 certificate. In the Download Complete dialog box, select Close . The Unity Connection root certificate file is ready
                                                   				  to be copied to all Cisco Unified CM servers in this Cisco Unified CM phone
                                                   				  system integration. For instructions, see the applicable Cisco Unified CM
                                                   				  integration guide at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html . | Caution | The certificate must be saved as a file with
                                                               					 the correct extension otherwise Cisco Unified CM does not recognize the
                                                               					 certificate. |
| Caution | The certificate must be saved as a file with
                                                               					 the correct extension otherwise Cisco Unified CM does not recognize the
                                                               					 certificate. |

| Caution | The certificate must be saved as a file with
                                                               					 the correct extension otherwise Cisco Unified CM does not recognize the
                                                               					 certificate. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Telephony
                                                   				  Integrations > Security , and then select SIP Security Profile . The Search SIP Security Profiles page
                                                				displays the currently configured SIP security profiles. |
|---|---|
| Step 2 | Configure a SIP security profile (For information, see Help>
                                             			 This Page): To add a SIP security profile: On the Search SIP Security Profiles
                                                      					 page, select Add New . On the New SIP Security Profile page, in
                                                      					 the Port field, enter the port number that the Cisco Unified CM server uses for
                                                      					 SIP trunk authentication and encryption of the voice messaging ports. To encrypt the call signaling messages,
                                                      					 check the Do TLS check box and select Save . To edit a SIP security profile: On the Search SIP Security Profiles
                                                      					 page, select the name of the SIP security profile that you want to edit. On the Edit SIP Security Profile page,
                                                      					 enter the applicable settings and select Save . To delete a SIP security profile: On the Search SIP Security Profiles
                                                      					 page, check the check box next to the display name of the SIP security profile
                                                      					 that you want to delete. Select Delete Selected and then select
                                                      					 OK. |