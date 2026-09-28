---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-cjab-b-feature-configuration-for-jabber-128-cjab-b-feature-confi-4b8f3e70d1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/cjab_b_feature-configuration-for-jabber-128/cjab_b_feature-configuration-for-jabber-128_chapter_011.html
retrieved_at: 2026-08-21T05:21:43.469122+00:00
---

Feature Configuration for Cisco Jabber 12.8

# Feature Configuration for Cisco Jabber 12.8

Updated: January 21, 2020

Chapter: Voice and Video

## Chapter: Voice and Video

# Voice and Video

## Meeting Controls for CMS Meetings

Applies to: All clients

Jabber provides meeting control functions through the Cisco Meeting Server (CMS) ActiveControl feature. The meeting control
                              functions include participant lists, muting participants, dropping participants, and changing the video layout.

To use ActiveControl requires the following in your deployment:

The call path between the endpoint and Meeting Server supports iX media end to end.

Appropriate permissions enabled in Meeting Server.

For more information on using CMS, see the Cisco Meeting Server, Deployments with Expressway Planning and Preparation Guide .

As of Release 12.5, Jabber can access Cisco Meeting Server conferences as a SIP device through ActiveControl. You can enter
                              an ActiveControl conference by either:

Dialing into a room that is configured on CMS

Merging two calls when a CMS room is configured as the conference bridge

### Before you begin

To set up ActiveControl, you need:

Cisco Meeting Server Release 2.3 or later

Cisco Unified Communications Manager 12.5.1.11900 or later

Cisco Expressway for Mobile and Remote Access X12.5.1 or later (Optional if Jabber is in your corporate network, not using
                                    MRA)

These are the releases with full support for ActiveControl. Earlier releases of Unified CM and Expressway did not support
                                          the control functions over Expressway.

Configure a SIP trunk in Cisco Unified Communications Manager with CMS to enable communication using SIP signals. For more
                                       information, see System Configuration Guide for Cisco Unified Communications Manager .

Configure a route pattern in Cisco Unified Communications Manager to route inbound and outbound SIP calls. For more information,
                                       see the Configure Call Routing chapter in System Configuration Guide for Cisco Unified Communications Manager .

Set up rules in CMS for outbound SIP call routing to the Cisco Unified Communications Manager server. For more information,
                                       see the Cisco Meeting Server with Cisco Unified Communications Manager Deployment Guide .

Configure your CMS space to manage your conference resources. For more information, see Cisco Meeting Server Release API Reference Guide .

## Meeting Controls for Webex Meetings

Set up Cisco Jabber so users can join Webex meetings from Jabber without having to launch Webex.

Configure your outgoing firewall to allow the following domains: *.ciscospark.com, *.wbx2.com, *.webex.com, *.clouddrive.com.

Configure a SIP trunk in Cisco Unified Communications Manager with Expressway for MRA and then Webex to enable communication
                                       using SIP signals. For more information, see System Configuration Guide for Cisco Unified Communications Manager .

Configure a route pattern in Cisco Unified Communications Manager to route inbound and outbound SIP calls. For more information,
                                       see the Configure Call Routing chapter in System Configuration Guide for Cisco Unified Communications Manager .

Set up rules in Webex for outbound SIP call routing to the Cisco Unified Communications Manager server. For more information,
                                       see the Cisco Meeting Server 2.3 with Cisco Unified Communications Manager Deployment Guide .

## Meeting Control for CMR Meetings

Applies to: All clients

Cisco Collaboration Meeting Rooms (CMR) Cloud provides easy access for users to join or start a Cisco Webex meeting. Cisco Jabber provides users with the ability to access the meeting either using Cisco Webex interface or join using video.

There's a limitation on CMR Cloud join experience for attendees of scheduled CMR Cloud meetings. This limitation a Mac users
                              and Windows users who haven't enabled Outlook calendar integration. Because of a server limitation, attendees for these deployment
                              scenarios can join the meeting only by using Cisco Webex. Hosts enjoy the full experience, as does anyone invited to join
                              ad hoc CMR Cloud meetings.

User in CTI control mode can join in directly, rather than by using Webex.

This table lists Jabber support for Cisco Meeting Server methods of joining meetings:

Join in Meeting

Jabber Support

Join in meeting from cross launch in Page

N

Join in meeting from Calendar

N

Join in meeting as SIP URL

Y

Join in meeting as HTTP link

Y

Join in meeting by meeting number

Y

Join in meeting using PIN (host and Guest)

Use Room Number instead

Rejoin in meetings

Y

As of Release 12.7, Jabber desktop users can choose to join meetings with Jabber or Webex. Administrators can configure a
                                          default for the client to use; in this case, the choice doesn't appear in the client.

This table lists the CMR controls that Cisco Jabber supports by client:

Control

Jabber for Windows

Jabber for Mac

Jabber for Android

Jabber for iPhone and iPad

Jabber Softphone for VDI

Device Indicator (Video and Audio)

Y

Y

N

N

Y

Active Speaker

Y

Y

Y

Y

Y

Participant List (Host and Guest)

Y

Y

Y

Y

Y

Assign Host

Y

Y

Y

Y

Y

Mute / Unmute

Y

Y

Y

Y

Y

Mute All / Unmute All

Y

Y

Y

Y

Y

Self-Mute / Unmute

Y

Y

Y

Y

Y

Drop Participant

Y

Y

Y

Y

Y

Admit People from Lobby

Y

Y

Y

Y

Y

Wait in Lobby

Y

Y

Y

Y

Y

End Meeting

Y

Y

Y

Y

Y

Leave Meeting and Assign Host

Y

Y

Y

Y

Y

Lock and Unlock Meeting

Y

Y

Y

Y

Y

Start and Stop Recording

Y

Y

Y

Y

Y

Copy Meeting Link

Y

Y

N

N

Y

Video Layout

Y

Y

Y

Y

Y

Desktop Sharing Send and Receive

Y

Y

Y

Y

Y

Sharing Layout Change

Y

Y

Y

Y

Y

Meeting Information

Y

Y

N

N

Y

Recording Pause / Resume

Y

Y

N

N

Y

Paired Participant with Teams

Y

Y

N

N

Y

Add Participant

N

N

N

N

N

Mobile Remote Access

Y

Y

Y

Y

Y

### Before you begin

WebEx Meeting Center videos (CMR) Cloud is available on Cisco Webex Meetings.

Configure the Collaboration Meeting Room options.

For more information, visit https://help.webex.com/ :

Site Administration— https://help.webex.com/en-us/6maub2/Configure-Webex-Meetings-in-Cisco-Webex-Site-Administration

Control Hub— https://help.webex.com/en-us/n8pgczj/Configure-Teleconferencing-Options-for-a-Webex-Site-in-Cisco-Webex-Control-Hub

Enable Collaboration Meeting Rooms for your users, on Cisco Webex Meetings.

Enable Common Identity (CI) for your Webex site.

If your Webex site isn't CI-enabled, users who join meetings from Jabber get audio and video controls only. They can also
                                          share their screens.

Collaboration
                                       			 Meeting Room features uses SIP URI, you must enable URI dialing for your users
                                       			 on Cisco Unified Communications Manager. For more information on URI dialing,
                                       			 see the URI
                                          				Dialing topic.

## Bridge
                        	 Escalations

Applies to: All clients

Bridge
                              		  escalations allow users to quickly escalate a group chat to a conference call.
                              		  Participants are automatically added without the need to merge them into the
                              		  conference call.

Enable bridge
                                       			 escalations in Cisco Jabber clients by setting the EnableBridgeConferencing parameter to true in the jabber-config.xml file.

(Optional)
                                       			 Specify a mask for the room URI in the UserBridgeUriAdmin parameter in the jabber-config.xml file. If you don't specify a mask
                                       			 the user can enter a DN or a SIP URI in the client.

Enable URI
                                       			 dialing to allow your users enter a SIP URI for the conference call number. For
                                       			 more information on URI dialing, see the URI
                                          				Dialing topic.

## Call Park

Applies to: All clients

You can use call park to place a call on hold and pick it up from another phone in a Cisco Unified Communications Manager system. Call park must be enabled and extension numbers must be defined on each Cisco Unified Communications Manager node in the cluster. You can define either a single directory number or a range of directory numbers for use as call park
                              extension numbers.

Complete the following tasks to enable call park. For detailed instructions, see the Feature Configuration Guide for Cisco Unified Communications Manager .

Configure cluster wide call park

Configure a partition

Create a partition to add a call park number.

Configure a call park number

Configure a call park number to use call park across nodes in a cluster.

You can define either a single directory number or a range of directory numbers for use as call park extension numbers. You
                                          can park only one call at each call park extension number.

### Configure Clusterwide Call Park

Choose System > Service
                                                				  Parameters .

Select the
                                          			 desired node as Server and the service as Cisco
                                             				CallManager (active).

Click the Advanced .

The advanced service parameters are displayed in the window.

In Clusterwide Parameter(Feature- General) section set the Enable cluster-wide Call
                                             				  Park Number/Ranges to True .

The default value is False. This parameter determines
                                             				  whether the Call Park feature is implemented clusterwide or restricted to a
                                             				  specific Unified CM node.

Set the Call Park Display Timer for each server in a
                                          				  cluster that has the Cisco CallManager service and Call Park configured.

The
                                             				  default is 10 seconds. This parameter determines how long a Call Park number
                                             				  displays on the phone that parked the call.

Set the Call Park Reversion Timer for each server in a cluster that has the service and Call Park configured.

The default is 60 seconds. This parameter determines the time that a call remains parked. When this timer expires, the parked
                                             call returns to the device that parked the call. If a hunt group member parks a call that comes through a hunt pilot, the
                                             call goes back to the hunt pilot when the Call Park Reversion Timer expires.

If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone.

Click Save .

Restart all and CTI Manager services.

### Configure a  Partition for Call Park

Configure
                                 		  partitions to create a logical grouping of directory numbers (DNs) and route
                                 		  patterns with similar reachability characteristics. Partitions facilitate call
                                 		  routing by dividing the route plan into logical subsets that are based on
                                 		  organization, location, and call type. You can configure multiple partitions.

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Click Add
                                             				New to create a new partition.

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

To create
                                          			 multiple partitions, use one line for each partition entry.

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

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

Click Save .

### Configure a Call Park Number

If you want to use
                                 		  Call Park across servers in a cluster, you must configure Call Park extension
                                 		  numbers on each server.

Ensure that each Call Park directory number, partition, and range is unique within the . Each to which devices are registered requires its own unique Call Park directory number and range. does not validate the Call Park numbers or range that you use to configure Call Park. To help identify invalid numbers or
                                 ranges and potential range overlaps, use the Dialed Number Analyzer tool.

Choose Call
                                                				  Routing > Call Park .

Perform one of
                                          			 the following tasks:

To add a
                                                   					 new Call Park number, click Add New .

To copy a
                                                   					 Call Park number, find the Call Park number or range of numbers and then click
                                                   					 the Copy icon.

To update
                                                   					 a Call Park number, find the Call Park number or range of numbers.

Configure the fields in the Call Park configuration fields. See Call Park Configuration Fields for more information about the fields and their configuration options.

To save the
                                          			 new or changed Call Park numbers in the database, click Save.

#### Call Park Configuration Fields

Field

Description

Call Park Number/Range

Enter the Call Park extension number. You can enter digits or
                                                					 the wildcard character X (the system allows one or two Xs). For example, enter
                                                					 5555 to define a single Call Park extension number of 5555 or enter 55XX to
                                                					 define a range of Call Park extension numbers from 5500 to 5599.

You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique.

You cannot overlap call park numbers between servers. Ensure that each server has its own number range.

The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phone A (registered to node A) calls
                                                            						phone  B (registered to node B) and the phone B user presses Park, phone B
                                                            						requires a call park range in the CSS that resides on node A. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers.

Description

Provide a brief description of this call park number. The
                                                					 description can include up to 50 characters in any language, but it cannot
                                                					 include double-quotes (“), percentage sign (%), ampersand (&), or angle
                                                					 brackets (<>).

Partition

If you want to use a partition to restrict access to the call
                                                					 park numbers, choose the desired partition from the drop-down list. If you do
                                                					 not want to restrict access to the call park numbers, choose <None> for
                                                					 the partition.

Make sure that the combination of call park extension number and partition is unique within the .

Using the drop-down list, choose the Cisco Unified Communications Manager to which these call park numbers apply.

## Call Pickup

Applies to: Cisco Jabber for Windows, Cisco Jabber for Mac, Cisco Jabber Softphone for VDI , Cisco Jabber for Android , Cisco Jabber for iPhone and iPad

The Call Pickup feature allows users to answer calls that come in on a directory number other than their own. Call pickup
                              groups have assigned directory numbers. Cisco Unified Communications Manager (Unified CM) automatically dials the appropriate
                              call pickup group number. Users select Pickup to answer the call.

To enable call pickup, you use these parameters in the jabber-config.xml file, depending on the types of call pickup that you support:

```
<Policies>
  <EnableCallPickup>true</EnableCallPickup>
  <EnableGroupCallPickup>true</EnableGroupCallPickup>
  <EnableOtherGroupPickup>true</EnableOtherGroupPickup>
  <EnableHuntGroup>true</EnableHuntGroup>
</Policies>
```

For more information about configuring call pickup, see the Feature Configuration Guide for Cisco Unified Communications Manager .

### Call Pickup Notifications

For multiple incoming calls, a notification, Call(s) available for pickup , appears. When the user answers a call, the user gets connected to the longest ringing call.

### Desk Phone Mode

In desk phone mode, the following limitations apply:

The Unified CM notification settings aren’t supported for the pickup group. The call pickup notification that displays is CallerA -> CallerB .

The Unified CM settings for audio and visual settings aren’t supported. The visual alerts always appear.

### Shared Line Behavior

For users that have a desk phone and also audio on computer with a shared line, the following limitations apply:

For an attempt to pick up a call using the client when no call is available, No call available for PickUp displays on the desk phone.

For an attempt to pick up a call using the desk phone when no call is available, No call available for PickUp displays on the client.

### User Not a Member of an Associated Group

For an incoming call to another pickup group where the user isn’t a member of an associated group:

You can use directed call pickup to pick up the incoming call.

Group pickup doesn’t work.

### Expected Behavior Using Group Call Pickup and Directed Call Pickup

The following are expected behaviors when using group call pickup and directed call pickup:

If you enter an invalid number:

Audio on computer mode—The conversation window appears and the user hears the annunciator immediately.

Desk phone mode—The conversation window, fast busy tone, or the annunciator occurs followed by the fast busy tone, Pickup failed error message.

If you enter a valid number with no active call available to pick up:

Audio on computer mode—Tone in the headset, no conversation window appears, and No call available for pickup error message.

Desk phone mode—No conversation window and No call available for pickup error message

If you enter a directory number of a phone in an associated group with no active call available to pick up:

Audio on computer mode—Tone in the headset, no conversation window appears, and No call available for pickup error message.

Desk phone mode—No conversation window and No call available for pickup error message

If you enter a directory number of a phone not in an associated group, but on the same Unified CM node:

Audio on computer mode—The conversation window appears and fast busy tone.

Desk phone mode—The conversation window appears, fast busy tone, and Pickup failed error message.

If you enter the first digits of a valid group:

Audio on computer mode—Tone in the headset, conversation window appears, and, after 15 seconds, the annunciator followed by
                                          the fast busy tone.

Desk phone mode—The conversation window appears, after 15 seconds, the annunciator, fast busy tone, and Pickup failed error message.

### Call Pickup Using a Desk Phone That Isn’t in a Call Pickup Group

If a user attempts a call pickup from a desk phone that isn’t in a call pickup group, the conversation window appears for
                              a moment. Don’t configure users to use the call pickup feature if they aren’t members of a call pickup group.

### Original Recipient Information Not Available

When the Unified CM Auto Call Pickup Enabled setting is true, the recipient information isn’t available in the client when the call is picked up in audio-on-computer
                              mode. If the setting is false, the recipient information is available.

### Configure Call
                           	 Pickup Group

Call pickup groups
                                 		  allow users to pick up incoming calls in their own group.

Open the Cisco
                                             				Unified Communication Manager interface.

Select Call
                                                				  Routing > Call Pickup Group

The Find
                                                				  and List Call Pickup Groups window opens.

Select Add
                                             				New

The Call
                                                				  Pickup Group Configuration window opens.

Enter call
                                          			 pickup group information:

Specify a
                                                				  unique name for the call pickup group.

Specify a
                                                				  unique directory number for the call pickup group number.

Enter a
                                                				  description.

Select a
                                                				  partition.

(Optional) Configure the
                                          			 audio or visual notification in the Call
                                             				Pickup Group Notification Settings section.

Select the
                                                				  notification policy.

Specify
                                                				  the notification timer.

For further
                                             				information on call pickup group notification settings see the call pickup
                                             				topics in the relevant Cisco Unified Communications Manager documentation.

Select Save .

#### What to do next

Assign a call
                                 		  pickup group to directory numbers.

### Assign Directory
                           	 Number

Assign a call pickup group to a directory number. Only directory
                                 		  numbers that are assigned to a call pickup group can use call pickup, group
                                 		  call pickup, other group pickup, and directed call pickup.

#### Before you begin

Before you assign a call pickup group to a directory number, you must
                                 		  create the call pickup group.

Open the Cisco Unified Communications Manager
                                             				Administration interface.

Assign a call pickup group to a directory number using one of the
                                          			 following methods:

Select Call Routing > Directory Number , find and select your directory number and in the Call Forward and Call Pickup Settings area select the call pickup group
                                                   from the call pickup group drop down list.

Select Device > Phone , find and select your phone and in the Association Information list choose the directory number to which the call pickup group will be assigned.

To save the changes in the database, select Save .

### Configure Other
                           	 Call Pickup

Other Group Pickup allows users to pick up incoming calls in an   associated group. Cisco Unified Communications Manager
                                 		  automatically searches for the incoming call in the associated groups to make
                                 		  the call connection when the user selects Other Pickup .

#### Before you begin

Before you begin,
                                 		  configure call pickup groups.

Open the Cisco
                                             				Unified Communication Manager Administration interface.

Select Call
                                                				  Routing > Call Pickup Group

The Find
                                                				  and List Call Pickup Groups window opens.

Select your
                                          			 call pickup group.

The Call
                                                				  Pickup Group Configuration window opens.

In the Associated Call Pickup Group Information section,
                                          			 you can do the following:

Find call
                                                   					 pickup groups and add to current associated call pickup groups.

Reorder
                                                   					 associated call pickup groups or remove call pickup groups.

Select Save .

### Configure Directed
                           	 Call Pickup

Directed call
                                 		  pickup allows you to pick up a incoming call directly. The user enters the
                                 		  directory number in the client and selects Pickup . Cisco Unified Communications Manager uses
                                 		  the associated group mechanism to control if the user can pick up an incoming
                                 		  call using Directed Call Pickup.

To enable directed
                                 		  call pickup, the associated groups of the user must contain the pickup group to
                                 		  which the directory number belongs.

When the user
                                 		  invokes the feature and enters a directory number to pick up an incoming call,
                                 		  the user connects to the call that is incoming to the specified phone whether
                                 		  or not the call is the longest incoming call in the call pickup group to which
                                 		  the directory number belongs.

Configure call
                                          			 pickup groups and add associated groups. The associated groups list can include
                                          			 up to 10 groups.

For more
                                             				information, see topics related to defining a pickup group for Other Group
                                             				Pickup.

Enable the
                                          			 Auto Call Pickup Enabled service parameter to automatically answer calls for
                                          			 directed call pickups.

For more
                                             				information, see topics related to configuring Auto Call Pickup.

### Auto Call
                           	 Pickup

You can automate call pickup, group pickup, other group pickup, and
                                 		  directed call pickup by enabling the Auto Call Pickup Enabled service
                                 		  parameter.
                                 		When this parameter is enabled, 
                                 		  Cisco Unified Communications Manager automatically connects users to the incoming call in their own pickup group, in
                                 		  another pickup group, or a pickup group that is associated with their own group
                                 		  after users select the appropriate pickup on the phone. This action requires
                                 		  only one keystroke.

Auto call pickup connects the user to an incoming call in the group of
                                 		  the user. When the user selects Pickup on the client, 
                                 		  Cisco Unified Communications Manager
                                 		  locates the incoming call in the group and completes the call connection. If
                                 		  automation is not enabled, the user must select Pickup and answer the call, to make the call
                                 		  connection.

Auto group call pickup connects the user to an incoming call in
                                 		  another pickup group. The user enters the group number of another pickup group
                                 		  and selects Pickup on the client. Upon receiving the pickup
                                 		  group number, 
                                 		  Cisco Unified Communications Manager
                                 		  completes the call connection. If auto group call pickup is not enabled, dial
                                 		  the group number of another pickup group, select Pickup on the client, and answer the call to
                                 		  make the connection.

Auto other group pickup connects the user to an incoming call in a
                                 		  group that is associated with the group of the user. The user selects Other Pickup on the client. 
                                 		  Cisco Unified Communications Manager
                                 		  automatically searches for the incoming call in the associated groups in the
                                 		  sequence that the administrator enters in the Call Pickup Group Configuration window and completes the call connection after the call is found. If automation
                                 		  is not enabled, the user must select Other Pickup , and answer the call to make the
                                 		  call connection.

Auto directed call pickup connects the user to an incoming call in a
                                 		  group that is associated with the group of the user. The user enters the
                                 		  directory number of the ringing phone and selects Pickup on the client. Upon receiving the
                                 		  directory number, 
                                 		  Cisco Unified Communications Manager
                                 		  completes the call connection. If auto directed call pickup is not enabled, the
                                 		  user must dial the directory number of the ringing phone, select Pickup , and answer the call that will now ring
                                 		  on the user phone to make the connection.

For more information about Call Pickup , see the Feature Configuration Guide for Cisco Unified Communications
                                    Manager .

#### Configure Auto
                              	 Call Pickup

Open the Cisco Unified CM Administration interface.

Select System > Service
                                                   				  Parameters

Select your server from the Server drop down list and then select
                                             			 the Cisco Call Manager service from the Service
                                             			 drop down list.

In the Clusterwide Parameters (Feature - Call Pickup) section, select one of the following for Auto Call Pickup Enabled :

- true—The auto call pickup feature is enabled.

- false—The auto call pickup feature is not enabled. This is the
                                                						default value.

Select Save .

## Dial via
                        	 Office

Applies to: Cisco Jabber for Android, Cisco Jabber for iPhone and iPad

The following features are not supported if the Dial via Office-Reverse (DvO-R) feature is enabled:

URI dialing

Secure Phone

User-controlled voicemail avoidance, which can be used in conjunction with the DvO feature, is available only on Cisco Unified
                                       Communications Manager release 9.0 and later. Timer-controlled voicemail avoidance is available on Cisco Unified Communications
                                       Manager release 6.0 and later.

You can make DvO-R calls over Expressway for Mobile and Remote Access when you are outside corporate network. DvO-R is supported
                                       on Cisco Expressway X8.7 and Cisco Unified Communications Manager 11.0(1a)SU1.

The DvO feature is not supported when users connect to the corporate network using Expressway for Mobile and Remote Access.

The DvO feature allows users to initiate Cisco Jabber outgoing calls with their work number using the mobile voice network
                           for the device.

Cisco Jabber supports DvO-R (DvO-Reverse) calls, which
                           		works as follows:

User initiates a
                                 			 DvO-R call.

The client notifies Cisco Unified Communications Manager to call the mobile phone number.

Cisco Unified Communications Manager calls and connects to the mobile phone number.

Cisco Unified Communications Manager calls and connects to the number that the user dialed.

Cisco Unified Communications Manager connects the two segments.

The user and the
                                 			 called party continue as with an ordinary call.

Incoming calls use either Mobile Connect or the Voice over IP, depending on which Calling Options the user sets on the client.
                           Dial via Office does not require Mobile Connect to work. However, we recommend that you enable Mobile Connect to allow the
                           native mobile number to ring when someone calls the work number. From the Cisco Unified Communications Manager user pages,
                           users can enable and disable Mobile Connect, and adjust Mobile Connect behavior using settings (for example, the time of day
                           routing and Delay Before Ringing Timer settings). For information about setting up Mobile Connect, see the Set Up Mobile Connect topic.

The users do not receive incoming calls on Cisco Jabber in the following situations:

If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is not configured for their device, they will not receive
                                             incoming calls on Cisco Jabber.

If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is configured with the Ring Schedule , they will not receive incoming calls on Cisco Jabber beyond the time set in the Ring Schedule .

The following table
                           	 describes the calling methods used for incoming and outgoing calls. The calling
                           	 method (VoIP, Mobile Connect, DvO-R, or native cellular call) varies depending
                           	 on the selected Calling Options and the network connection.

Connection

Calling
                                       				Options

Voice over
                                       				IP

Mobile Voice
                                       				Network

Autoselect

Corporate
                                       				Wi-Fi

Outgoing:
                                       				VoIP

Incoming:
                                       				VoIP

Outgoing:
                                       				DvO-R

Incoming:
                                       				Mobile Connect

Outgoing:
                                       				VoIP

Incoming:
                                       				VoIP

Noncorporate
                                       				Wi-Fi

Mobile
                                       				Network (3G, 4G)

Outgoing:
                                       				DvO-R

Phone
                                       				Services are not registered

To set up Dial via
                           	 Office-Reverse (DvO-R), you must do the following:

Set up the Cisco Unified Communications Manager to support DvO-R. See the Set Up Cisco Unified Communications Manager to Support DvO topic for more information.

Enable DvO on each Cisco Dual Mode for iPhone or Android device. See the Set Up Dial via Office for Each Device topic for more information.

### Set Up Cisco
                           	 Unified Communications Manager to Support Dial via Office

To set up Cisco Unified Communications Manager to support
                                 		  Dial via Office-Reverse ( DvO-R), perform the following procedures:

Complete one
                                       				or both of the following procedures.

Set Up Enterprise Feature
                                                						Access Number

Set Up Mobility
                                                						Profile

Complete the Verify
                                          				  Device COP File Version procedure.

If necessary,
                                       				create application dial rules to allow the system to route calls to the Mobile
                                       				Identity phone number to the outbound gateway. Ensure that the format of the
                                       				Mobile Identity phone number matches the application dial rules.

#### Set Up Enterprise Feature Access Number

Use this procedure to set up an Enterprise Feature Access Number for all Cisco Jabber calls that are made using Dial via Office-Reverse.

The Enterprise Feature Access Number is the number that Cisco Unified Communications Manager uses to call the mobile phone
                                    and the dialed number unless a different number is set up in Mobility Profile for this purpose.

##### Before you begin

Reserve a Direct Inward Dial (DID) number to use as the Enterprise Feature Access Number (EFAN). This procedure is optional
                                          if you already set up a mobility profile.

Determine the required format for this number. The exact value you choose depends on the phone number that the gateway passes
                                          (for example, 7 digits or 10 digits).  The Enterprise Feature Access Number must be a routable number.

Open the Cisco Unified CM Administration interface.

Select Call Routing > Mobility > Enterprise Feature Access Number Configuration .

Select Add New .

In the Number field, enter the Enterprise Feature Access number.

Enter a DID number that is unique in the system.

To support dialing internationally, you can prepend this number with \+.

From the Route Partition drop-down list, choose the partition of the DID that
                                             is required for enterprise feature access.

This partition is set under System > Service Parameters , in the Clusterwide Parameters (System - Mobility) section,  in the Inbound Calling Search Space for Remote Destination setting. This setting points either to the Inbound Calling Search Space of the Gateway or Trunk, or to the Calling Search
                                                Space assigned on the Phone Configuration window for the device.

If the user sets up the DvO Callback Number with an alternate number, ensure that you set up the trunk Calling Search Space
                                                (CSS) to route to destination of the alternate phone number.

In the Description field, enter a description of the Mobility Enterprise Feature Access
                                             number.

(Optional) Check the Default Enterprise Feature Access Number check box if you want to make this Enterprise Feature Access number the default for this system.

Select Save .

#### Set Up Mobility Profile

Use this procedure to set up a mobility profile for Cisco Jabber devices. This procedure is optional if you already set up
                                    an Enterprise Feature Access Number.

Mobility profiles allow you to set up the Dial via Office-Reverse settings for a mobile client. After you set up a mobility
                                    profile, you can assign it to a user or to a group of users, such as the users in a region or location.

Open the Cisco Unified CM Administration interface.

Select Call Routing > Mobility > Mobility Profile .

In the Mobility Profile Information section, in the Name field, enter a descriptive name for the mobility profile.

In the Dial via Office-Reverse Callback section, in the Callback Caller ID field, enter the caller ID for the callback call that the client receives from Cisco Unified Communications Manager.

Click Save .

#### Verify Device COP
                              	 File Version

Use the following
                                    		  procedure to verify that you are using the correct device COP file for this
                                    		  release of 
                                    		  Cisco Jabber.

Open the Cisco
                                                				Unified CM Administration interface.

Select Device > Phone .

Click Add
                                                				New .

From the Phone Type drop-down list, choose Cisco Dual Mode for iPhone or Cisco Dual Mode for Android .

Click Next .

Scroll down to
                                             			 the Product Specific Configuration Layout section, and verify that you can see
                                             			 the Video Capabilities drop-down list.

If you can see
                                                				the Video Capabilities drop-down list, the COP file is already installed on
                                                				your system.

If you cannot
                                                				see the Video Capabilities drop-down list, locate and download the correct COP
                                                				file.

### Set Up Dial via Office for Each Device

Use the following procedures to set up Dial via Office - Reverse for each TCT or BOT device.

Add a Mobility Identity for each user.

Enable Dial via Office on each device.

If you enabled Mobile Connect, verify that Mobile Connect works. Dial the desk phone extension and check that the phone number
                                          that is specified in the associated Mobile Identity rings.

#### Add Mobility
                              	 Identity

Use this procedure
                                    		  to add a mobility identity to specify the mobile phone number of the mobile
                                    		  device as the destination number. This destination number is used by features
                                    		  such as Dial via Office or mobile connect.

You can specify
                                    		  only one number when you add a mobility identity. If you want to specify an
                                    		  alternate number such as a second mobile phone number for a mobile device, you
                                    		  can set up a remote destination. The mobility identity configuration
                                    		  characteristics are identical to those of the remote destination configuration.

Open the Cisco
                                                				Unified CM Administration interface.

Navigate to
                                             			 the device that you want to configure as follows:

Select Device > Phone .

Search
                                                   				  for the device that you want to configure.

Select
                                                   				  the device name to open the Phone Configuration window.

In the Associated Mobility Identity section, select Add a
                                                				New Mobility Identity .

Enter the
                                             			 mobile phone number as the destination number.

You must be able to rout this number to an outbound gateway. Generally, the number is the full
                                                				E.164 number.

If you
                                                            				  enable the Dial via Office — Reverse feature for a user, you must enter a
                                                            				  destination number for the user's mobility identity.

The
                                                                     						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
                                                                     						network and VPN.

The
                                                                     						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
                                                                     						network.

The
                                                                     						logs do not indicate why the phone service cannot connect.

Enter the
                                             			 initial values for call timers.

These values
                                                				ensure that calls are not routed to the mobile service provider voicemail
                                                				before they ring in the client on the mobile device. You can adjust these
                                                				values to work with the end user's mobile network. For more information, see
                                                				the online help in Cisco Unified Communications Manager.

The following is an example of mobility Identity timers'
                                                				  information in Cisco Unified Communications Manager 9.x.

Setting

Suggested Initial Value

Answer Too Soon Timer

3000

Answer Too Late Timer

20000

Delay Before Ringing Timer

0

This setting does not apply to DvO-R calls.

The following is an example of mobility Identity timers'
                                                				  information in Cisco Unified Communications Manager 10.x.

Setting

Suggested Initial Value

Wait * before ringing this phone when my business line
                                                            							 is dialed.*

0.0 seconds

Prevent this call from going straight to this phone's
                                                            							 voicemail by using a time delay of * to detect when calls go straight to
                                                            							 voicemail.*

3.0 seconds

Stop ringing this phone after * to avoid connecting to
                                                            							 this phone's voicemail.*

20.0 seconds

Do one of the
                                             			 following:

- Cisco Unified
                                                				Communications Manager release 9 or earlier —  Check the Enable Mobile Connect check box.

- Cisco Unified
                                                				Communications Manager release 10 —  Check the Enable Single Number Reach check box.

If you are
                                             			 setting up the Dial via Office feature, in the Mobility Profile drop-down list,
                                             			 select one of the following options.

Option

Description

Leave
                                                         				  blank

Choose
                                                         					 this option if you want users to use the Enterprise Feature Access Number
                                                         					 (EFAN).

Mobility
                                                         				  Profile

Choose the
                                                         					 mobility profile that you just created if you want users to use a mobility
                                                         					 profile instead of an EFAN.

Set up the
                                             			 schedule for routing calls to the mobile number.

Select Save .

#### Enable Dial via
                              	 Office on Each Device

Use this procedure
                                    		  to enable Dial via Office on each device.

Open the Cisco
                                                				Unified CM Administration interface.

Navigate to
                                             			 the device that you want to configure as follows:

Select Device > Phone .

Search for
                                                   				  the device that you want to configure.

Select the
                                                   				  device name to open the Phone Configuration window.

In the Device
                                                			 Information section, check the 
                                             			 Enable
                                             				Cisco Unified Mobile Communicator check box.

In the Protocol Specific Information section, in the Rerouting Calling Search Space drop-down list,
                                             			 select a Calling Search Space (CSS) that can route the call to the DvO callback
                                             			 number.

In the Product
                                                			 Specific Configuration Layout section, set the Dial
                                                				via Office drop-down list to Enabled .

Select Save .

Select Apply
                                                				Config .

Instruct the
                                             			 user to sign out of the client and then to sign back in again to access the
                                             			 feature.

DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from
                                                            the Cisco Unified Communications Manager administrative interface fixes this issue.

##### What to do next

Test this feature.

## Far End Camera
                        	 Control (FECC)

Applies to: All clients except Cisco Jabber Softphone for VDI

In calls that
                              		  support far-end camera control (FECC), you can adjust the far-end camera to
                              		  give you a better view during video calls. FECC is available to users if the
                              		  endpoint that they are calling supports it.

You can configure
                              		  whether users can access FECC-enabled endpoints. Disabling the configuration
                              		  parameter means that users are not provided with the ability to control far-end
                              		  camera endpoints, even if the endpoint is capable. From a user experience, with
                              		  FECC disabled, it works the same as dialing in to an endpoint that is not FECC
                              		  enabled.

To disable FECC,
                              		  set the EnableFecc parameter to false . For more information about this parameter, see the Parameters Reference Guide .

### Limitations

FECC is only
                              		  supported in point-to-point calls, but not in group calls or conferences where
                              		  multiple video connections are connecting to the same bridge.

FECC is only
                              		  supported in Softphone mode.

## Flexible DSCP
                        	 Values

Applies to: Cisco Jabber for Mac, Cisco Jabber for Android, Cisco Jabber for iPhone and iPad

Flexible Differentiated
                              		Services Code Point (DSCP) allows you to specify different DSCP
                              		values to separate the audio and video streams on the network.

The EnableDSCPPacketMarking parameter is used to enable or disable DSCP packet marking in the client.

You can
                              		configure the DSCP values for audio calls, video calls, audio portion for video
                              		calls, and audio portion for telepresence calls separately. For better bandwidth management and to  protect audio
                              		stream degradation, separate the audio stream from the
                              		higher-bandwidth video stream. This can help when the network is congested or the call quality
                              		is impacted.

DSCP values are configured on Cisco Unified Communications Manager. For more information, see the Configure Flexible DSCP Marking and Video Promotion Policy section of the System Configuration Guide for Cisco Unified Communications Manager .

## Hunt Group

Applies to all clients

A Hunt Group is a group of lines that are organized hierarchically, so that if the first number in the hunt group list is
                              busy, the system dials the second number. If the second number is busy, the system dials the next number, and so on. Every
                              hunt group has a pilot number that is also called as hunt pilot. A hunt pilot contains a hunt pilot number and an associated
                              hunt list. Hunt pilots provide flexibility in network design. They work with route filters and hunt lists to direct calls
                              to specific devices and to include, exclude, or modify specific digit patterns.

A hunt pilot number is the number that a user dials. A hunt list contains a set of line groups in a specific order. A line
                              group comprises a group of directory numbers in a specific order. The order controls the progress of the search for available
                              directory numbers for incoming calls. A single-line group can appear in multiple hunt lists.

Unified Communications Manager (Unified CM) identifies a call that is to be routed through a defined hunt list, Unified CM
                              finds the first available device on the basis of the order of the line groups that a hunt list defines.

You can let a user sign in and out of hunt groups by configuring EnableHuntGroup parameter. You can control whether users can decline calls from hunt groups with the PreventDeclineOnHuntCall parameter. For more information, see the Parameters Reference Guide for Cisco Jabber .

Unified CM 9.x and later allows configuring of automatic sign out of a hunt member when there is no answer. Once the user
                              is signed out, the system displays a sign out notification whether the user is auto-signed out, manually signed out, or signed
                              out by the Unified CM administrator.

### Limitation

Desktop clients must use audio on computer mode before users can sign in to or out of hunt groups.

### Line Group

A line group allows you to designate the order in which directory
                                 		  numbers are chosen. 
                                 		  Cisco Unified Communications Manager
                                 		  distributes a call to an idle or available member of a line group based on the
                                 		  call distribution algorithm and on the Ring No Answer (RNA) Reversion timeout
                                 		  setting.

Users cannot pick up calls to a DN that belongs to a line group by
                                 		  using the directed call pickup feature.

#### Configure Line
                              	 Group

##### Before you begin

Configure directory numbers.

Open the Cisco
                                                				Unified CM Administration interface.

Select Call
                                                   				  Routing > Route/Hunt > Line
                                                   				  Group .

The Find
                                                   				  and List Line Groups window opens.

Select Add
                                                				New .

The Line
                                                   				  Group Configuration window opens.

Enter settings
                                             			 in the Line
                                                				Group Information section as follows:

Specify a
                                                      					 unique name in the Line Group Name field.

Specify
                                                      					 number of seconds for RNA Reversion Timeout .

Select a Distribution Algorithm to apply to the line group.

Enter settings
                                             			 in the Hunt Options section as follows:

Select
                                                      						  a value for No Answer from the drop-down list.

Select Automatically Logout Hunt Member on No Answer to configure auto logout of the hunt list.

Select
                                                      						  a value for Busy from the drop-down list.

Select
                                                      						  a value for Not Available from the drop-down list.

In the Line
                                                				Group Member Information section, you can do the following:

Find
                                                      					 directory numbers or route partitions to add to the line group.

Reorder
                                                      					 the directory numbers or route partitions in the line group.

Remove
                                                      					 directory numbers or route partitions from the line group.

Select Save .

##### What to do next

Configure a hunt
                                    		  list and add the line group to the hunt list.

### Hunt List

A hunt list contains a set of line groups in a specific order. A hunt
                                 		  list associates with one or more hunt pilots and determines the order in which
                                 		  those line groups are accessed. The order controls the progress of the search
                                 		  for available directory numbers for incoming calls.

A hunt list comprises a collection of directory numbers as defined by
                                 		  line groups. After 
                                 		  Cisco Unified Communications Manager
                                 		  determines a call that is to be routed through a defined hunt list, 
                                 		  Cisco Unified Communications Manager
                                 		  finds the first available device on the basis of the order of the line group(s)
                                 		  that a hunt list defines.

A hunt list can contain only line groups. Each hunt list should have at least one line group. Each line group includes at
                                 least one directory number. A single line group can appear in multiple hunt lists.

The group call pickup feature and directed call pickup feature do not work with hunt lists.

#### Configure Hunt
                              	 List

Open the Cisco Unified CM Administration interface.

Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  List .

The Find and Hunt List Groups window opens.

Select Add New .

The Hunt List Configuration window opens.

Enter settings in the Hunt List Information section as follows:

Specify a unique name in the Name field.

Enter a description for the Hunt List.

Select a Cisco Unified Communications Manager
                                                         						Group from the drop-down list.

The system selects Enable this Hunt List by default for a
                                                      					 new hunt list when the hunt list is saved.

If this hunt list is to be used for voice mail, select For Voice Mail Usage .

Select Save to add the hunt list.

##### What to do next

Add line groups to the hunt list.

#### Add Line Group to
                              	 Hunt List

##### Before you begin

You must configure line groups and configure a hunt list.

Open the Cisco Unified CM Administration interface.

Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  List .

The Find and Hunt List Groups window opens.

Locate the hunt list to which you want to add a line group.

To add a line group, select Add Line Group .

The Hunt List Detail Configuration window
                                                				displays.

Select a line group from the Line Group drop-down list.

To add the line group, select Save .

To add additional line groups, repeat Step 4 to Step 6.

Select Save.

To reset the hunt list, select Reset . When the dialog box appears, select Reset .

### Hunt Pilot

A hunt pilot comprises a string of digits (an address) and a set of associated digit manipulations that route calls to a hunt
                                 list. Hunt pilots provide flexibility in network design. They work in conjunction with route filters and hunt lists to direct
                                 calls to specific devices and to include, exclude, or modify specific digit patterns. For more information about hunt pilots,
                                 see the System Configuration Guide for Cisco Unified Communications Manager .

For more detailed information on the configuration options for hunt pilots, see the relevant Cisco Unified Communications Manager documentation .

#### Configure Hunt
                              	 Pilot

Open the Cisco
                                                				Unified CM Administration interface.

Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  Pilot .

The Find
                                                   				  and List Hunt Pilots window opens.

Select Add
                                                				New .

The Hunt
                                                   				  Pilot Configuration window opens.

Enter the hunt
                                             			 pilot, including numbers and wildcards.

Select a hunt
                                             			 list from the Hunt
                                                				List drop-down list.

Enter any
                                             			 additional configurations in the Hunt
                                                				Pilot Configuration window. For more information on hunt pilot
                                             			 configuration settings, see the relevant 
                                             			 Cisco Unified Communications Manager documentation.

Select Save .

## Jabber to Jabber
                        	 Call

Applies to: All clients except Cisco Jabber Softphone for VDI

Jabber to Jabber voice and video calling provides basic calling capabilities between two Cisco Jabber clients without using Cisco Unified Communications Manager . If Cisco Jabber users are not registered with Cisco Unified Communications Manager , they can still make Jabber to Jabber calls from Cisco Jabber.

Jabber to Jabber calling is only supported for users who authenticate to the Cisco Webex Messenger service.

For Cisco Jabber for Windows clients, we recommend running Internet Explorer 10 or greater while using the Jabber to Jabber calling feature. Using the feature with previous versions of Internet Explorer or with Internet Explorer in Compatibility
                                                Mode can cause issues. These issues are with Cisco Jabber client login (non-SSO setup) or Jabber to Jabber calling capability (SSO setup).

### Jabber to Jabber Call Experience

A Jabber to Jabber call does not support all the features of a Cisco Unified Communication Manager call. Users can make a Jabber to Jabber call with only one contact at a time. In a Jabber to Jabber call, users can experience any of the following scenarios:

Cisco Jabber for mobile clients does not support HD video in portrait mode. To achieve HD video, you need to rotate the phone
                                    from portrait to landscape mode during the call.

If two users start a Jabber to Jabber call to each other at the same time, the call is automatically connected. In such case, users do not receive any incoming
                                    call notification.

When users are on a Jabber to Jabber call and start another call, the ongoing call ends immediately, even if the person they called does not answer.

When on a Jabber to Jabber call and they receive an incoming Jabber to Jabber call, the End Call And Answer option is displayed. When they select this button, the ongoing Jabber to Jabber call ends and the incoming call is answered.

For Jabber to Jabber calls on Cisco Jabber for mobile clients:

Cisco Jabber for mobile clients does not support HD video in portrait mode. To achieve HD video, you need to rotate the phone
                                          from portrait to landscape mode during the call.

When users are on a Jabber to Jabber call and they make a phone call, the ongoing Jabber to Jabber call ends immediately, even if the remote party does not answer.

When users are on a mobile call, they cannot answer any Jabber to Jabber call. The incoming Jabber to Jabber call is listed as a missed call.

When users are on a Jabber to Jabber call and they receive an incoming mobile call:

On an iPhone, the Jabber to Jabber call ends immediately, even if they do not answer the call.

On an Android phone, the Jabber to Jabber call ends immediately when they answer the incoming mobile call.

### Supported In-Call Features

The following features are supported during a Jabber to Jabber call:

End a Jabber to Jabber call

Mute or unmute the audio

Start or stop the video

Volume control

Open or close or move the self-video

Switch to front or back camera. This feature is only supported on the Cisco Jabber mobile clients.

### Jabber to Jabber Call Cloud Deployment

Cloud deployment for Jabber to Jabber call uses the SDP/HTTPS setup. For cloud deployment, ensure the following:

Install the following root certificate to use the Jabber to Jabber call feature: GoDaddy Class 2 Certification Authority Root Certificate . To resolve any warnings about this certificate name, install the required GoDaddy certificate.

Include the following servers in the proxy server bypass list:

https://locus-a.wbx2.com/locus/api/v1

https://conv-a.wbx2.com/conversation/api/v1

For information on proxy server lists, see the Configure Proxy Settings in the Cisco Jabber Deployment Guides.

Enable the range of media ports and protocols for RTP/SRTP over UDP: 33434-33598 and 8000-8100. For Jabber to Jabber call setup over HTTPS, enable port 443.

Before you enable the Jabber to Jabber calling feature, complete the following tasks:

Contact the Cisco Customer Support team or your Cisco Customer Success Manager to request that your organization is added
                                          to the Cisco Common Identity server. This process to add users to the Common Identity server takes some time to complete and
                                          is necessary to access Jabber to Jabber calling capabilities.

For Single Sign On (SSO) users, you must set up SSO for Common Identity. For more information about configuring SSO, see
                                          the Cisco Webex Messenger documentation at this link: https://www.cisco.com/c/en/us/support/unified-communications/webex-messenger/products-installation-guides-list.html .

For cloud deployments, Jabber to Jabber calling is configured on the Cisco Webex Messenger Administration tool with one of the following methods:

Using the P2P settings in the Configuration Tab section. For more information, see the Cisco Webex Messenger Administrator's Guide .

Using the Internal VoIP and External VoIP settings in the policy editor for Cisco Webex Messenger Administration tool. You can control the video services for Jabber
                                    to Jabber calls using the Internal Video and External Video policy actions. For more information, see the Policy Editor section of the Cisco Webex Messenger Administration Guide. Jabber to Jabber calling can be enabled for groups of users or all users.

### Jabber to Jabber
                           	 Hybrid Mode

#### Jabber to
                                 		  Jabber Call Experience in Hybrid Mode

In addition to the
                                 		  limitations for Jabber to Jabber, the following are the scenarios that occur
                                 		  when using Jabber to Jabber calls and Cisco Unified Communications Manager
                                 		  calls:

When users
                                       				are on a Jabber to Jabber call and make a Cisco Unified Communications Manager
                                       				call, the ongoing Jabber to Jabber call ends immediately, even if the remote
                                       				party does not answer.

When users
                                       				are on a Jabber to Jabber call and resume a Cisco Unified Communications
                                       				Manager call from on hold, the Jabber to Jabber call ends immediately.

When users
                                       				are on a Jabber to Jabber call and receive an incoming Cisco Unified
                                       				Communications Manager call, a notification with an End Call And Answer button displays. If your user
                                       				selects this button the ongoing Jabber to Jabber call ends and the incoming
                                       				call is answered.

When users
                                       				receive a Cisco Unified Communications Manager call, they can place the ongoing
                                       				Cisco Unified Communications Manager call on hold to answer the new call.

When users
                                       				are on a Cisco Unified Communications Manager call and they choose to make a
                                       				Jabber to Jabber call, the Cisco Unified Communications Manager call is put on
                                       				hold immediately, even if the participant in the Jabber to Jabber call does not
                                       				answer the call.

When users
                                       				are on a Cisco Unified Communications Manager call and they answer an incoming
                                       				Jabber to Jabber call, the Cisco Unified Communications Manager call is put on
                                       				hold immediately.

If your
                                       				user’s line is configured on Cisco Unified Communications Manager to
                                       				auto-answer calls and they receive an incoming Cisco Unified Communications
                                       				Manager call when they are on a Jabber to Jabber call, the Jabber to Jabber
                                       				call ends immediately without notification and the Cisco Unified Communications
                                       				Manager call is answered.

### Jabber to Jabber Bandwidth

Specifies the maximum bandwidth (in kilobits per second)  to be used for Jabber to Jabber calls. The video quality (resolution)
                                 of the call is lowered so that it meets the bandwidth limit.   This feature is configured using the J2JMaxBandwidthKbps parameter.

For more information on parameters, see the Parameter Reference Guide for your release.

## Let Users Without Voicemail Ignore Calls

Applies to: All clients.

You can choose a NoVoicemail profile for users who don't have voicemail configured. Jabber displays an Ignore call option for these users.

### Configure a Device with No Voicemail

From Cisco Unified CM IM and Presence Administration , go to Device > Phone .

Find and select the device.

In the Association Information , choose the directory number.

In the Directory Number Settings , choose NoVoicemail for Voice Mail Profile .

Click Save and then select Apply Config .

## Move to Mobile

Applies to: Cisco Jabber for Android, Cisco Jabber for iOS

Users can transfer
                              		  an active VoIP call from 
                              		  Cisco Jabber to their mobile phone number on the
                              		  mobile network. This feature is useful when a user on a call leaves the Wi-Fi
                              		  network (for example, leaving the building to walk out to the car), or if there
                              		  are voice quality issues over the Wi-Fi network.

The Move to Mobile feature requires a mobile telephone network connection with a phone number. Users must have a TCT or BOT
                                          device.

There are two
                              			 ways to enable this feature. You can also disable it.

Implementation Method

Description

Instructions

Handoff DN

The
                                          						mobile device calls 
                                          						Cisco Unified Communications Manager using the mobile network.

This
                                          						method requires a Direct Inward Dial (DID) number.

The
                                          						service provider must deliver the DID digits exactly as configured.
                                          						Alternately, for Cisco IOS gateways with H.323 or SIP communication to 
                                          						Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
                                          						the inbound called-party number at the gateway, presenting the digits to 
                                          						Cisco Unified Communications Manager exactly as configured on the handoff
                                          						DN.

This method does not work for iPod Touch devices.

See the Enable Handoff from VoIP to Mobile Network topic.

Mobility Softkey

Cisco Unified Communications Manager calls the phone number of the PSTN
                                          						mobile service provider for the mobile device.

See the Enable Transfer from VoIP to Mobile Network topic.

None of the above

Disable this feature if you do not want to make it available to
                                          					 users.

Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the TCT device page.

Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the BOT device page.

### Enable Handoff from VoIP to Mobile Network

Set up a directory number that Cisco Unified Communications Manager can use to hand off active calls from VoIP to the mobile
                              network. Match the user's caller ID with the Mobility Identity to ensure that Cisco Unified Communications Manager can recognize
                              the user. Set up the TCT device and mobile device to support handoff from VoIP to the mobile network.

Set up a directory number that Cisco Unified Communications Manager can use to hand off active calls from VoIP to the mobile
                              network. Match the user's caller ID with the Mobility Identity to ensure that Cisco Unified Communications Manager can recognize
                              the user. Set up the BOT device and mobile device to support handoff from VoIP to the mobile network.

#### Set Up Handoff DN

##### Before you begin

Determine the required
                                    		values. The values that you choose depend on the phone number that the gateway
                                    		passes (for example, seven digits or ten digits).

Open the Cisco Unified CM Administration interface.

Select Call Routing > Mobility > Handoff Configuration .

Enter the 
                                             			 Handoff Number for the Direct Inward Dial
                                             			 (DID) number that the device uses to hand off a VoIP call to the mobile
                                             			 network.

The service provider must deliver the DID digits exactly as
                                                				configured. Alternately, for Cisco IOS gateways with H.323 or SIP communication
                                                				to Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
                                                				the inbound called-party number at the gateway, presenting the digits to Cisco Unified Communications Manager exactly
                                                as configured on the handoff number.

You cannot use translation patterns or other similar
                                                            				  manipulations within Cisco Unified Communications Manager to match the inbound
                                                            				  DID digits to the configured Handoff DN.

Select the Route Partition for the handoff DID.

This partition should be present in the Remote Destination inbound
                                                				Calling Search Space (CSS), which points to either the Inbound CSS of the Gateway or Trunk, or the Remote Destination
                                                CSS.

This feature does not use the remaining options on this page.

Select Save .

#### Match Caller ID with Mobility Identity

To ensure that only authorized phones can initiate outbound
                                    		  calls, calls must originate from a phone that is set up in the system. To do
                                    		  this, the system attempts to match the caller ID of the requesting phone number
                                    		  with an existing Mobility Identity. By default, when a device initiates the
                                    		  Handoff feature, the caller ID that is passed from the gateway to Cisco Unified Communications Manager must exactly match
                                    the Mobility Identity number that you
                                    		  entered for that device.

However, your system may be set up such that these numbers
                                    		  do not match exactly. For example, Mobility Identity numbers may include a
                                    		  country code while caller ID does not. If so, you must set up the system to
                                    		  recognize a partial match.

Be sure to account for situations in which the
                                    		  same phone number may exist in different area codes or in different countries.
                                    		  Also, be aware that service providers can identify calls with a variable number
                                    		  of digits, which may affect partial matching. For example, local calls may be
                                    		  identified using seven digits (such as 555 0123) while out-of-area calls may be
                                    		  identified using ten digits (such as 408 555 0199).

##### Before you begin

Set up the Mobility Identity. See the Add Mobility Identity topic.

To determine whether you need
                                    			 to complete this procedure, perform the following steps. Dial
                                    				  in to the system from the mobile device and compare the caller ID value with the Destination Number in
                                    				  the Mobility Identity. If the numbers do not match, you must perform this
                                    				  procedure. Repeat this procedure for devices that are issued in all expected locales and
                                    				  area codes.

Open the Cisco Unified CM Administration interface.

Select System > Service Parameters .

Select the active server.

Select the Cisco CallManager (Active) service.

Scroll down to the Clusterwide Parameters (System - Mobility) section.

Select Matching Caller ID with Remote Destination and
                                             			 read essential information about this value.

Select Partial Match for Matching Caller ID with Remote
                                                				Destination .

Select Number of Digits for Caller ID Partial Match and read the essential requirements for this value.

Enter the required number of digits to ensure partial matches.

Select Save .

#### Set Up User and
                              	 Device Settings for Handoff

##### Before you begin

Set up the
                                          				user device on the 
                                          				Cisco Unified Communications Manager.

Set up the
                                          				user with a Mobility Identity.

In the Cisco Unified CM Administration interface, go to the TCT Device page, and select Use Handoff DN Feature for the Transfer to Mobile Network option.

Do not assign this method for iPod Touch devices. Use the Mobility Softkey method instead.

In the Cisco Unified CM Administration interface, go to the BOT Device page, and select Use Handoff DN Feature for the Transfer to Mobile Network option.

On the iOS device, tap Settings > Phone > Show My Caller ID to verify that Caller ID is on.

On some Android device and operating system combinations, you can verify that the Caller ID is on. On the Android device,
                                             open the Phone application and tap Menu > Call Settings > Additional settings > Caller ID > Show Number .

Test this
                                             			 feature.

### Enable Transfer
                           	 from VoIP to Mobile Network

Open the Cisco
                                             				Unified CM Administration interface.

For
                                          			 system-level settings, check that the Mobility softkey appears when the phone
                                          			 is in the connected and on-hook call states.

Select Device > Device
                                                      						Settings > Softkey Template .

Select the
                                                				  same softkey template that you selected when you configured the device for
                                                				  Mobile Connect.

In the Related Links drop-down list at the upper right,
                                                				  select Configure Softkey Layout and select Go .

In the
                                                				  call state drop-down list, select the On Hook state and verify that the
                                                				  Mobility key is in the list of selected softkeys.

In the
                                                				  call state drop-down list, select the Connected state and verify that the
                                                				  Mobility key is in the list of selected softkeys.

Navigate to
                                          			 the device that you want to configure as follows:

Select Device > Phone .

Search for
                                                				  the device that you want to configure.

Select the
                                                				  device name to open the Phone Configuration window.

For the
                                          			 per-user and per-device settings in 
                                          			 Cisco Unified Communications Manager, set the specific device to use the
                                          			 Mobility softkey when the device transfers calls to the mobile voice network.
                                          			 Ensure that you have set up both Mobility Identity and Mobile Connect for the
                                          			 mobile device. After the transfer feature is working, users can enable and
                                          			 disable Mobile Connect at their convenience without affecting the feature.

If the device is an iPod Touch, you can configure a Mobility Identity using an alternate phone number such as the mobile phone
                                             of the user.

Select the Owner User ID on the device page.

Select the Mobility User ID . The value usually matches that of
                                                				  the Owner User ID.

In the
                                                				  Product Specific Configuration Layout section, for the Transfer to Mobile
                                                				  Network option, select Use Mobility Softkey or Use HandoffDN Feature .

In the User
                                          			 Locale field, choose English, United States .

Select Save .

Select Apply Config .

Instruct the user to sign out of the client and then to sign back
                                          			 in again to access the feature.

#### What to do next

Test your settings
                                 		  by transferring an active call from VoIP to the mobile network.

## Multiline

Applies to: Cisco Jabber for Windows, Cisco Jabber for Mac, and Cisco Jabber Softphone for VDI

You can configure multiple phone lines for your users to perform daily Cisco Jabber tasks. You can add up to 8 phone lines
                              for each user. You can configure multiline for your users on Cisco Services Framework (CSF) device.

Multiline is supported on Cisco Unified Communications Manager release 11.5 SU3 and later. However, if you are using Cisco
                              Unified Communications Manager release 11.5 SU3 and Cisco Unified Communications Manager release 12.0, you must manually install
                              the Cisco Options Package (COP) file on all cluster nodes and restart Cisco Unified Communications Manager to enable multiline.

After you have installed and configured Multiline, your users can:

Select a preferred line for making calls.

View missed calls and voicemails.

Use call forwarding, transfers, and conference calls on all lines.

Assign custom ringtones to each line.

Multiline supports the following features on all lines:

CTI control for the desk phone

Far End Camera Control (FECC) and Binary Floor Control Protocol (BFCP)

Hunt groups

Call recording and silent monitoring

Shared line, dial rules, and directory lookup

Accessory manager

If Multiline is enabled, these features are only available on the primary line:

Call pickup

Extend & Connect

### Configure Multiline

#### Before you begin

Create and add user profiles in Cisco Unified Communications Manager.

For Cisco Jabber Softphone for VDI , merge call functionality requires the following configuration:

Set Join And Direct Transfter Policy to Same line, across line enable .

Check the Override Enterprise Settings check box.

From Cisco Unified CM Administration , go to Device > Phone , and find and select the device.

For each line you want to configure:

Click Add a new DN , enter a Directory Number .

Add any additional configurations and click Save .

### Enable Multiline MRA Access

Go to VCS-C.

Select VSC-C configuration > Unified Communication > Configuration > SIP Path headers and set it to On .

## Personal
                        	 Rooms

Applies to: All clients

A personal room is a virtual conference room that is always available and can be used to meet with people. Cisco Jabber uses
                              the personal room feature of Cisco Webex Meetings to allow users to easily meet with their contacts using the Start meeting option in the client.

Personal Rooms are enabled by default for users on Cisco Webex Meetings. For more information see the Cisco Webex Meetings
                                       documentation available here: https://www.cisco.com/c/en/us/support/conferencing/webex-meeting-center/products-installation-and-configuration-guides-list.html

Users can configure their personal rooms for all instant meetings by selecting Use Personal Room for all my instant meetings in Cisco Webex Meetings.

## Push Notification Service for Cisco Jabber Video and Voice Calls

Applies to: Cisco Jabber for iPhone and iPad.

Cisco Jabber users can receive push notification for Jabber voice and video calls. This feature works when the device is locked,
                              whether Cisco Jabber runs in the background or foreground, and whether the Cisco Jabber IM service is connected. For Release 11.9 and earlier, Cisco Jabber used VoIP-sockets to contact the Unified CM server periodically. Incoming calls
                                 reached Jabber through the VoIP sockets. From Release 12.1 onwards, the Apple Push Notification (APN) implementation supports push notification for users with AES enabled. Users continue to receive push notification even if the VoIP-sockets are disabled.

If the user manually terminates Jabber with the push notification service enabled, then the ForceLogoutTimerMobile parameter does not function. We recommend that you disable the push notification service if you want to use the ForceLogoutTimerMobile parameter.

### Prerequisites

Cisco Unified Communications Manager 11.5.1 SU3 version or later

Cisco Expressway X8.10

Jabber registers to APN services during the sign-in process. Users must sign in to Jabber to receive the push notifications
                              service.

### How Push Notifications Are Delivered to Jabber

### Supported Services

On-Premises and Cloud deployment modes

Phone-only and Full UC modes

Shared line (You can pick the call from one device and transfer it to Jabber using Hold and Resume functions)

CallKit (You can switch between Jabber calls, Jabber to native calls, and native to Jabber calls)

### Limitations

If an incoming call disconnects before Jabber retrieves the call from the Unified CM server, then the missed call or call
                                    history is not recorded.

If you have both Cisco Jabber and Cisco Webex Teams installed, the application that first receives the incoming call displays
                                    the callkit.

Users receive no notifications for peer-to-peer communications.

If you kill or suspend Jabber and you answer an incoming call, Jabber starts a connection to Unified CM. In this case, you
                                    might see a "call connecting" phase.

### Enable Push Notification Service on Cisco Unified Communications Manager

Go to Cisco Unified CM Administration > Advanced Features > Cisco Cloud Onboarding .

From the Notification Settings, check Enable Push Notification .

Click Save .

## Single Number Reach

Applies to: All clients.

With Single Number Reach (SNR), a user can automatically forward calls from their work number to their mobile phone if:

Cisco Jabber isn't available.

After Jabber becomes available again and connects to the corporate network, Unified CM sends calls to the Jabber client, rather
                                    than using SNR.

Jabber mobile users select Mobile Voice Network or Autoselect and they're outside their Wi-Fi network.

A user can select or clear their SNR destination number from Cisco Jabber.

### Enable Single Number Reach

Use the following procedure to enable single number reach for your users.

#### Before you begin

Make sure that the user has a device already assigned to them.

Open the Cisco
                                             				Unified CM Administration interface.

Configure the end user for single number reach as follows:

Go to User Management > End User , search for the user and click their name.

In the Mobility Information section, check the Enable Mobility check box.

On Cisco Unified Communications Manager Release 9.0 and earlier, specify the Primary User Device.

Click Save .

Create their remote destination profile.

Go to Device > Device Settings > Remote Destination Profile > Add New .

Enter the required values and click Save .

Click Add a New Directory Number and enter the directory number of the desk phone to associate with the remote destination profile.

Click Save .

Click Add a New Remote Destination , enter the number for your remote destination in Destination number and choose the User ID .

Click Enable Unified Mobility features, and click the following options:

Enable Single Number Reach

Enable Move to Mobile

Click Save .

#### Limitations

For Cisco TelePresence Video Communication Server Control (VCS) versions earlier than 8.10.X, you need to configure the following
                                    to enable the single number reach for your users who are using Cisco Jabber over Mobile and Remote Access.

From Cisco TelePresence Video Communication Server Control (VCS), choose Configuration > Unified Communications > HTTP allow list > Editable inbound rules

Click New to create a new entry

Enter the following details:

Description—Enter the required description.

URL—Enter the URL details. For example, https://[CUCM domain name]: port number .

Allowed Methods—Check the default value. For example, GET, POST, PUT

Match Type—Choose Prefix match from the drop-down list.

Click Save .

## URI Dialing

Applies to: All clients

You can use the URI dialing feature for on-premises deployments. URI dialing requires Cisco Unified Communications Manager,
                              Release 9.1(2) or later.

The mobile clients don't support URI dialing when you enable the Dial via Office-Reverse feature.

You enable this feature in the jabber-config.xml file with the EnableSIPURIDialling parameter.

Example: <EnableSIPURIDialling>True</EnableSIPURIDialling>

For more information on the values of the parameter, see the Parameters Reference Guide .

URI dialing allows users to make calls and resolve contacts with Uniform Resource Identifiers (URI). For example, a user whose
                              name is Adam McKenzie has the following SIP URI associated with his directory number: amckenzi@example.com . URI dialing enables users to call Adam with his SIP URI, rather than his directory number.

For detailed information on URI dialing requirements and advanced configuration including ILS setup, see the URI Dialing section of the System Configuration Guide for Cisco Unified Communications Manager .

### Associate URIs to Directory Numbers

When users make URI calls, Cisco Unified Communications Manager routes the inbound calls to the directory numbers associated
                                 to the URIs. For this reason, you must associate URIs with directory numbers. You can either automatically populate directory
                                 numbers with URIs or configure directory numbers with URIs.

#### Automatically Populate  Directory Numbers with URIs

When you add users to Cisco Unified Communications Manager, you populate the Directory URI field with a valid SIP URI. Cisco Unified Communications Manager saves that SIP URI in the end user configuration.

When you specify primary extensions for users, Cisco Unified Communications Manager populates the directory URI from the end
                                    user configuration to the directory number configuration. In this way, automatically populates the directory URI for the user's
                                    directory number.  Cisco Unified Communications Manager also places the URI in the default partition, which is Directory URI .

The following task outlines, at a high level, the steps to configure Cisco Unified Communications Manager so that directory
                                    numbers inherit URIs:

Add devices.

Add directory numbers to the devices.

Associate users with the devices.

Specify primary extensions for users.

##### What to do next

Verify that the directory URIs are associated with the directory numbers.

##### Configure
                                 	 Directory Numbers with URIs

You can specify
                                       		  URIs for directory numbers that are not associated with users. You should
                                       		  configure directory numbers with URIs for testing and evaluation purposes only.

To configure
                                       		  directory numbers with URIs, do the following:

Open the Cisco
                                                   				Unified CM Administration interface.

Select Call
                                                      				  Routing > Directory Number .

The Find
                                                      				  and List Directory Numbers window opens.

Find and
                                                			 select the appropriate directory number.

The Directory Number Configuration window opens.

Locate the Directory URIs section.

Specify a
                                                			 valid SIP URI in the URI column.

Select the
                                                			 appropriate partition from the Partition column.

You cannot
                                                                  					 manually add URIs to the system Directory URI partition. You should add the URI to
                                                                  					 the same route partition as the directory number.

Add the
                                                			 partition to the appropriate calling search space so that users can place calls
                                                			 to the directory numbers.

Select Save .

#### Associate the Directory URI Partition

You must associate the default partition into which Cisco Unified Communications Manager places URIs with a partition that
                                    contains directory numbers.

To enable URI dialing, you must associate the default directory URI partition with a partition that contains directory numbers.

If you do not already have a partition for directory numbers within a calling search space, you should create a partition
                                                   and configure it as appropriate.

Open the Cisco Unified CM Administration interface.

Select System > Enterprise Parameters .

The Enterprise Parameters Configuration window opens.

Locate the End User Parameters section.

In the Directory URI Alias Partition row, select the appropriate partition from the drop-down list.

Click Save .

The default directory URI partition is associated with the partition that contains directory numbers. As a result, Cisco Unified
                                    Communications Manager can route incoming URI calls to the correct directory numbers.

You should ensure the partition is in the appropriate calling search space so that users can place calls to the directory
                                    numbers.

### Enable FQDN in SIP
                           	 Requests for Contact Resolution

To enable contact
                                 		  resolution with URIs, you must ensure that 
                                 		  Cisco Unified Communications Manager uses the fully qualified domain name
                                 		  (FQDN) in SIP requests.

Open the Cisco
                                             				Unified CM Administration interface.

Select Device > Device
                                                				  Settings > SIP Profile .

The Find
                                                				  and List SIP Profiles window opens.

Find and
                                          			 select the appropriate SIP profile.

You cannot
                                                            					 edit the default SIP profile. If required, you should create a copy of the
                                                            					 default SIP profile that you can modify.

Select Use
                                             				Fully Qualified Domain Name in SIP Requests and then select Save .

#### What to do next

Associate the SIP
                                 		  profile with all devices that have primary extensions to which you associate
                                 		  URIs.

## Voicemail Avoidance

Applies to: All clients

Voicemail avoidance is a feature that prevents calls from being answered by the mobile service provider voice mail. This feature
                           is useful if a user receives a Mobile Connect call from the enterprise on the mobile device. It is also useful when an incoming
                           DvO-R call is placed to the mobile device.

You can set up voicemail avoidance in one of two ways:

Timer-controlled —(Default) With this method, you set timers on the Cisco Unified Communications Manager to determine if the call is answered
                                 by the mobile user or mobile service provider voicemail.

User-controlled —With this method, you set Cisco Unified Communications Manager to require that a user presses any key on the keypad of the
                                 device to generate a DTMF tone before the call can proceed.

If you deploy DvO-R, Cisco recommends that you also set user-controlled voicemail avoidance. If you set user-controlled Voicemail
                           Avoidance, this feature applies to both DvO-R and Mobile Connect calls.

For more information about voicemail avoidance, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Features and Services Guide for your release.

### Set Up
                           	 Timer-Controlled Voicemail Avoidance

Set up the timer
                                 		  control method by setting the Answer
                                    			 Too Soon Timer and Answer
                                    			 Too Late Timer on either the Mobility Identity or the Remote
                                 		  Destination. For more information, see the Add Mobility
                                    			 Identity or Add Remote
                                    			 Destination (Optional) topics.

#### Before you begin

Timer-controlled voicemail avoidance is supported on 
                                 		  Cisco Unified Communications Manager, release 6.0 and later.

### Set Up
                           	 User-Controlled Voicemail Avoidance

User-controlled
                                             			 voicemail avoidance is available on 
                                             			 Cisco Unified Communications Manager, release 9.0 and later.

Set up
                                 		  User-Controlled Voicemail Avoidance as follows:

Set up Cisco
                                       				Unified Communications Manager using the Set Up 
                                          				  Cisco Unified Communications Manager to Support Voicemail
                                          				  Avoidance topic.

Set up the
                                       				device using one of the following topics:

Enable Voicemail Avoidance
                                                						on Mobility Identity

Enable Voicemail Avoidance
                                                						on Remote Destination

Cisco does not
                                             			 support user-controlled voicemail avoidance when using DvO-R with alternate
                                             			 numbers that the end user sets up in the client. An alternate number is any
                                             			 phone number that the user enters in the DvO Callback Number field on the
                                             			 client that does not match the phone number that you set up on the user's
                                             			 Mobility Identity.

If you set up
                                             			 this feature with alternate numbers, the 
                                             			 Cisco Unified Communications Manager connects the DvO-R calls even if the
                                             			 callback connects to a wrong number or a voicemail system.

#### Set Up Cisco
                              	 Unified Communications Manager to Support Voicemail Avoidance

Use this procedure
                                    		  to set up the 
                                    		  Cisco Unified Communications Manager to support user-controlled Voicemail
                                    		  Avoidance.

Open the Cisco
                                                				Unified CM Administration interface.

Select System > Service
                                                   				  Parameters .

In the Server drop-down list, select the active 
                                             			 Cisco Unified Communications Manager.

In the Service drop-down list, select the Cisco
                                                				Call Manager (Active) service.

Configure the
                                             			 settings in the Clusterwide Parameters (System - Mobility Single Number Reach
                                                				Voicemail) section.

The settings
                                                            				  in this section are not specific to 
                                                            				  Cisco Jabber. For information about how to
                                                            				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
                                                            				  release.

Click Save .

#### Enable Voicemail
                              	 Avoidance on Mobility Identity

Use this procedure
                                    		  to enable user-controlled voicemail avoidance for the end user's mobility
                                    		  identity.

##### Before you begin

Set up the
                                          				annunciator on the 
                                          				Cisco Unified Communications Manager. For more information, see the Annunciator setup section in the Cisco Unified Communications Manager Administrator Guide for your
                                          				release.

If you set up
                                          				a Media Resource Group on the 
                                          				Cisco Unified Communications Manager, set up the annunciator on the Media
                                          				Resource Group. For more information, see the Media
                                             				  resource group setup section in the Cisco Unified Communications Manager Administrator Guide for your
                                          				release.

Open the Cisco
                                                				Unified CM Administration interface.

Navigate to
                                             			 the device that you want to configure as follows:

Select Device > Phone .

Search for
                                                   				  the device that you want to configure.

Select the
                                                   				  device name to open the Phone Configuration window.

In the Associated Mobility Identity section, click the link
                                             			 for the Mobility Identity.

To ensure
                                                            				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
                                                            				  that the end user enters in the 
                                                            				  Cisco Jabber client must match the Destination
                                                            				  Number that you enter on the Mobility Identity Configuration screen.

Set the
                                             			 policies as follows:

- Cisco Unified Communications Manager  release 9 
                                                				   — In the Single Number Reach Voicemail Policy drop-down list,
                                                					 select User Control .

- Cisco Unified Communications Manager release 10 without Dial via Office 
                                                				   — In the Single Number Reach Voicemail Policy drop-down list,
                                                					 select User Control .

- In the Single Number Reach Voicemail Policy drop-down list,
                                                      						  select Timer Control .

- In the Dial-via-Office Reverse Voicemail Policy drop-down
                                                      						  list, select User Control .

Click Save .

#### Enable Voicemail
                              	 Avoidance on Remote Destination

Use this procedure
                                    		  to enable user-controlled voicemail avoidance for the end user's remote
                                    		  destination.

##### Before you begin

Set up the
                                          				annunciator on the 
                                          				Cisco Unified Communications Manager. For more information, see the Annunciator setup section in the 
                                          				Cisco Unified Communications Manager Administrator Guide for your
                                          				release.

If you set up
                                          				a Media Resource Group on the 
                                          				Cisco Unified Communications Manager, set up the annunciator on the Media
                                          				Resource Group. For more information, see the Media
                                             				  resource group setup section in the 
                                          				Cisco Unified Communications Manager Administrator Guide for your
                                          				release.

Open the Cisco
                                                				Unified CM Administration interface.

Navigate to
                                             			 the device that you want to configure as follows:

Select Device > Phone .

Search for
                                                   				  the device that you want to configure.

Select the
                                                   				  device name to open the Phone Configuration window.

In the Associated Remote Destinations section, click the
                                             			 link for the associated remote destination.

Set the
                                             			 policies as follows:

- Cisco Unified Communications Manager
                                                					 release 9
                                                				   — In the Single Number Reach Voicemail Policy drop-down list, select User Control .

- Cisco Unified Communications Manager
                                                					 release 10 without Dial via Office
                                                				  — In the Single Number Reach Voicemail Policy drop-down list, select User Control .

- In the Single Number Reach Voicemail Policy drop-down list, select Timer Control .

- In the Dial-via-Office Reverse Voicemail
                                                         							 Policy drop-down list, select User Control .

Click Save .

## Voice Messages

Applies to: All clients

The voicemail screen includes these extra options:

Users can record voice messages without making a call and then send the message. Users can select recipients from the voicemail
                                    server's catalog.

Users can directly reply to the sender of a voicemail or to all recipients of that message.

Users can forward voicemails to new recipients.

The voicemail server's administrator can also create distribution lists to which users can send messages.

### Show Sent Voice Messages

Applies to: Cisco Jabber for Windows and Mac

If you set a retention period for sent messages in Cisco Unity Connection, users can access their sent voice messages in Jabber.

In Unity Connection Administration , go to Messaging Configuration .

Set Sent Messages: Retention Period (in Days) to a positive number to enable this feature.

## Auto Answer Calls

You can configure a CSF device to auto answer incoming Jabber calls. In Unified CM, you can set the device to either auto
                              answer with a headset or with a speakerphone.

Do not configure auto answer on a shared line unless all the connected devices support auto answer.

If you also enable zip tones, the zip tone only plays with Jabber when the CSF device auto answers with a headset. Zip tones
                                          do not play when a speakerphone auto answers the call.

## Jabber with Cisco Unified Contact Center

You can use Cisco Jabber as an agent phone in a contact center environment. We support the following Cisco Unified Contact
                              Center features with Jabber:

CTI Servitude —Unified Contact Center deployments can control a Jabber softphone through CTI.

Auto Answer —You can configure auto answer for a Jabber CSF device in Unified CM. But, all devices on a shared line must support auto
                                    answer.

Zip Tone —You can use zip tones with auto answer with a headset. Auto answer with a speakerphone doesn't support zip tones.

Whisper Announcement —You can use whisper announcement to play an introductory message to the agent.

Silent Monitoring —A supervisor can monitor an incoming call.

Call Recording —You can send a recording stream to a recording server that Cisco Unified Contact Center supports.

Jabber doesn't support Extension Mobility in contact center deployments.

| Note | These are the releases with full support for ActiveControl. Earlier releases of Unified CM and Expressway did not support
                                          the control functions over Expressway. |
|---|---|

| Step 1 | Configure a SIP trunk in Cisco Unified Communications Manager with CMS to enable communication using SIP signals. For more
                                       information, see System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Configure a route pattern in Cisco Unified Communications Manager to route inbound and outbound SIP calls. For more information,
                                       see the Configure Call Routing chapter in System Configuration Guide for Cisco Unified Communications Manager . |
| Step 3 | Set up rules in CMS for outbound SIP call routing to the Cisco Unified Communications Manager server. For more information,
                                       see the Cisco Meeting Server with Cisco Unified Communications Manager Deployment Guide . |
| Step 4 | Configure your CMS space to manage your conference resources. For more information, see Cisco Meeting Server Release API Reference Guide . |

| Step 1 | Configure your outgoing firewall to allow the following domains: *.ciscospark.com, *.wbx2.com, *.webex.com, *.clouddrive.com. |
|---|---|
| Step 2 | Configure a SIP trunk in Cisco Unified Communications Manager with Expressway for MRA and then Webex to enable communication
                                       using SIP signals. For more information, see System Configuration Guide for Cisco Unified Communications Manager . |
| Step 3 | Configure a route pattern in Cisco Unified Communications Manager to route inbound and outbound SIP calls. For more information,
                                       see the Configure Call Routing chapter in System Configuration Guide for Cisco Unified Communications Manager . |
| Step 4 | Set up rules in Webex for outbound SIP call routing to the Cisco Unified Communications Manager server. For more information,
                                       see the Cisco Meeting Server 2.3 with Cisco Unified Communications Manager Deployment Guide . |

| Join in Meeting | Jabber Support |
|---|---|
| Join in meeting from cross launch in Page | N |
| Join in meeting from Calendar | N |
| Join in meeting as SIP URL | Y |
| Join in meeting as HTTP link | Y |
| Join in meeting by meeting number | Y |
| Join in meeting using PIN (host and Guest) | Use Room Number instead |
| Rejoin in meetings | Y |

| Note | As of Release 12.7, Jabber desktop users can choose to join meetings with Jabber or Webex. Administrators can configure a
                                          default for the client to use; in this case, the choice doesn't appear in the client. |
|---|---|

| Control | Jabber for Windows | Jabber for Mac | Jabber for Android | Jabber for iPhone and iPad | Jabber Softphone for VDI |
|---|---|---|---|---|---|
| Device Indicator (Video and Audio) | Y | Y | N | N | Y |
| Active Speaker | Y | Y | Y | Y | Y |
| Participant List (Host and Guest) | Y | Y | Y | Y | Y |
| Assign Host | Y | Y | Y | Y | Y |
| Mute / Unmute | Y | Y | Y | Y | Y |
| Mute All / Unmute All | Y | Y | Y | Y | Y |
| Self-Mute / Unmute | Y | Y | Y | Y | Y |
| Drop Participant | Y | Y | Y | Y | Y |
| Admit People from Lobby | Y | Y | Y | Y | Y |
| Wait in Lobby | Y | Y | Y | Y | Y |
| End Meeting | Y | Y | Y | Y | Y |
| Leave Meeting and Assign Host | Y | Y | Y | Y | Y |
| Lock and Unlock Meeting | Y | Y | Y | Y | Y |
| Start and Stop Recording | Y | Y | Y | Y | Y |
| Copy Meeting Link | Y | Y | N | N | Y |
| Video Layout | Y | Y | Y | Y | Y |
| Desktop Sharing Send and Receive | Y | Y | Y | Y | Y |
| Sharing Layout Change | Y | Y | Y | Y | Y |
| Meeting Information | Y | Y | N | N | Y |
| Recording Pause / Resume | Y | Y | N | N | Y |
| Paired Participant with Teams | Y | Y | N | N | Y |
| Add Participant | N | N | N | N | N |
| Mobile Remote Access | Y | Y | Y | Y | Y |

| Step 1 | Configure the Collaboration Meeting Room options. For more information, visit https://help.webex.com/ : Site Administration— https://help.webex.com/en-us/6maub2/Configure-Webex-Meetings-in-Cisco-Webex-Site-Administration Control Hub— https://help.webex.com/en-us/n8pgczj/Configure-Teleconferencing-Options-for-a-Webex-Site-in-Cisco-Webex-Control-Hub |
|---|---|
| Step 2 | Enable Collaboration Meeting Rooms for your users, on Cisco Webex Meetings. |
| Step 3 | Enable Common Identity (CI) for your Webex site. If your Webex site isn't CI-enabled, users who join meetings from Jabber get audio and video controls only. They can also
                                          share their screens. |
| Step 4 | Collaboration
                                       			 Meeting Room features uses SIP URI, you must enable URI dialing for your users
                                       			 on Cisco Unified Communications Manager. For more information on URI dialing,
                                       			 see the URI
                                          				Dialing topic. |

| Step 1 | Enable bridge
                                       			 escalations in Cisco Jabber clients by setting the EnableBridgeConferencing parameter to true in the jabber-config.xml file. |
|---|---|
| Step 2 | (Optional)
                                       			 Specify a mask for the room URI in the UserBridgeUriAdmin parameter in the jabber-config.xml file. If you don't specify a mask
                                       			 the user can enter a DN or a SIP URI in the client. |
| Step 3 | Enable URI
                                       			 dialing to allow your users enter a SIP URI for the conference call number. For
                                       			 more information on URI dialing, see the URI
                                          				Dialing topic. |

| Step 1 | Configure cluster wide call park [Optional] Configure call park for the entire cluster, or use the procedure in Step 3 to configure call park on individual
                                       nodes within the cluster. |
|---|---|
| Step 2 | Configure a partition Create a partition to add a call park number. |
| Step 3 | Configure a call park number Configure a call park number to use call park across nodes in a cluster. You can define either a single directory number or a range of directory numbers for use as call park extension numbers. You
                                          can park only one call at each call park extension number. |

| Step 1 | Choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | Select the
                                          			 desired node as Server and the service as Cisco
                                             				CallManager (active). |
| Step 3 | Click the Advanced . The advanced service parameters are displayed in the window. |
| Step 4 | In Clusterwide Parameter(Feature- General) section set the Enable cluster-wide Call
                                             				  Park Number/Ranges to True . The default value is False. This parameter determines
                                             				  whether the Call Park feature is implemented clusterwide or restricted to a
                                             				  specific Unified CM node. |
| Step 5 | Set the Call Park Display Timer for each server in a
                                          				  cluster that has the Cisco CallManager service and Call Park configured. The
                                             				  default is 10 seconds. This parameter determines how long a Call Park number
                                             				  displays on the phone that parked the call. |
| Step 6 | Set the Call Park Reversion Timer for each server in a cluster that has the service and Call Park configured. The default is 60 seconds. This parameter determines the time that a call remains parked. When this timer expires, the parked
                                             call returns to the device that parked the call. If a hunt group member parks a call that comes through a hunt pilot, the
                                             call goes back to the hunt pilot when the Call Park Reversion Timer expires. Note If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. | Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
| Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
| Step 7 | Click Save . |
| Step 8 | Restart all and CTI Manager services. |

| Note | If you enter a Call Park Reversion Timer value that is less than the Call Park Display Timer, Call Park numbers may not display
                                                         on the phone. |
|---|---|

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

| Step 1 | Choose Call
                                                				  Routing > Call Park . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: To add a
                                                   					 new Call Park number, click Add New . To copy a
                                                   					 Call Park number, find the Call Park number or range of numbers and then click
                                                   					 the Copy icon. To update
                                                   					 a Call Park number, find the Call Park number or range of numbers. The
                                          			 Call Park number configuration window displays. |
| Step 3 | Configure the fields in the Call Park configuration fields. See Call Park Configuration Fields for more information about the fields and their configuration options. |
| Step 4 | To save the
                                          			 new or changed Call Park numbers in the database, click Save. |

| Field | Description |
|---|---|
| Call Park Number/Range | Enter the Call Park extension number. You can enter digits or
                                                					 the wildcard character X (the system allows one or two Xs). For example, enter
                                                					 5555 to define a single Call Park extension number of 5555 or enter 55XX to
                                                					 define a range of Call Park extension numbers from 5500 to 5599. Note You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. Note You cannot overlap call park numbers between servers. Ensure that each server has its own number range. Note The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phone A (registered to node A) calls
                                                            						phone  B (registered to node B) and the phone B user presses Park, phone B
                                                            						requires a call park range in the CSS that resides on node A. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. | Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. | Note | You cannot overlap call park numbers between servers. Ensure that each server has its own number range. | Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phone A (registered to node A) calls
                                                            						phone  B (registered to node B) and the phone B user presses Park, phone B
                                                            						requires a call park range in the CSS that resides on node A. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
| Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. |
| Note | You cannot overlap call park numbers between servers. Ensure that each server has its own number range. |
| Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phone A (registered to node A) calls
                                                            						phone  B (registered to node B) and the phone B user presses Park, phone B
                                                            						requires a call park range in the CSS that resides on node A. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
| Description | Provide a brief description of this call park number. The
                                                					 description can include up to 50 characters in any language, but it cannot
                                                					 include double-quotes (“), percentage sign (%), ampersand (&), or angle
                                                					 brackets (<>). |
| Partition | If you want to use a partition to restrict access to the call
                                                					 park numbers, choose the desired partition from the drop-down list. If you do
                                                					 not want to restrict access to the call park numbers, choose <None> for
                                                					 the partition. Note Make sure that the combination of call park extension number and partition is unique within the . | Note | Make sure that the combination of call park extension number and partition is unique within the . |
| Note | Make sure that the combination of call park extension number and partition is unique within the . |
|  | Using the drop-down list, choose the Cisco Unified Communications Manager to which these call park numbers apply. |

| Note | You can create a maximum of 100 Call Park numbers with one
                                                            						call park range definition. Make sure that the call park numbers are unique. |
|---|---|

| Note | You cannot overlap call park numbers between servers. Ensure that each server has its own number range. |
|---|---|

| Note | The call park range is selected from the list of servers
                                                            						where the call originates. For example, if phone A (registered to node A) calls
                                                            						phone  B (registered to node B) and the phone B user presses Park, phone B
                                                            						requires a call park range in the CSS that resides on node A. In a multinode
                                                            						environment where phones and gateways communicate with various nodes and where
                                                            						calls that originate from any server may need to be parked, the phones require
                                                            						a CSS that contains call park ranges from all servers. |
|---|---|

| Note | Make sure that the combination of call park extension number and partition is unique within the . |
|---|---|

| Step 1 | Open the Cisco
                                             				Unified Communication Manager interface. |
|---|---|
| Step 2 | Select Call
                                                				  Routing > Call Pickup Group The Find
                                                				  and List Call Pickup Groups window opens. |
| Step 3 | Select Add
                                             				New The Call
                                                				  Pickup Group Configuration window opens. |
| Step 4 | Enter call
                                          			 pickup group information: Specify a
                                                				  unique name for the call pickup group. Specify a
                                                				  unique directory number for the call pickup group number. Enter a
                                                				  description. Select a
                                                				  partition. |
| Step 5 | (Optional) Configure the
                                          			 audio or visual notification in the Call
                                             				Pickup Group Notification Settings section. Select the
                                                				  notification policy. Specify
                                                				  the notification timer. For further
                                             				information on call pickup group notification settings see the call pickup
                                             				topics in the relevant Cisco Unified Communications Manager documentation. |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified Communications Manager
                                             				Administration interface. |
|---|---|
| Step 2 | Assign a call pickup group to a directory number using one of the
                                          			 following methods: Select Call Routing > Directory Number , find and select your directory number and in the Call Forward and Call Pickup Settings area select the call pickup group
                                                   from the call pickup group drop down list. Select Device > Phone , find and select your phone and in the Association Information list choose the directory number to which the call pickup group will be assigned. |
| Step 3 | To save the changes in the database, select Save . |

| Step 1 | Open the Cisco
                                             				Unified Communication Manager Administration interface. |
|---|---|
| Step 2 | Select Call
                                                				  Routing > Call Pickup Group The Find
                                                				  and List Call Pickup Groups window opens. |
| Step 3 | Select your
                                          			 call pickup group. The Call
                                                				  Pickup Group Configuration window opens. |
| Step 4 | In the Associated Call Pickup Group Information section,
                                          			 you can do the following: Find call
                                                   					 pickup groups and add to current associated call pickup groups. Reorder
                                                   					 associated call pickup groups or remove call pickup groups. |
| Step 5 | Select Save . |

| Step 1 | Configure call
                                          			 pickup groups and add associated groups. The associated groups list can include
                                          			 up to 10 groups. For more
                                             				information, see topics related to defining a pickup group for Other Group
                                             				Pickup. |
|---|---|
| Step 2 | Enable the
                                          			 Auto Call Pickup Enabled service parameter to automatically answer calls for
                                          			 directed call pickups. For more
                                             				information, see topics related to configuring Auto Call Pickup. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service
                                                   				  Parameters |
| Step 3 | Select your server from the Server drop down list and then select
                                             			 the Cisco Call Manager service from the Service
                                             			 drop down list. |
| Step 4 | In the Clusterwide Parameters (Feature - Call Pickup) section, select one of the following for Auto Call Pickup Enabled : true—The auto call pickup feature is enabled. false—The auto call pickup feature is not enabled. This is the
                                                						default value. |
| Step 5 | Select Save . |

| Important | The following features are not supported if the Dial via Office-Reverse (DvO-R) feature is enabled: URI dialing Secure Phone User-controlled voicemail avoidance, which can be used in conjunction with the DvO feature, is available only on Cisco Unified
                                       Communications Manager release 9.0 and later. Timer-controlled voicemail avoidance is available on Cisco Unified Communications
                                       Manager release 6.0 and later. You can make DvO-R calls over Expressway for Mobile and Remote Access when you are outside corporate network. DvO-R is supported
                                       on Cisco Expressway X8.7 and Cisco Unified Communications Manager 11.0(1a)SU1. The DvO feature is not supported when users connect to the corporate network using Expressway for Mobile and Remote Access. |
|---|---|

| Note | The users do not receive incoming calls on Cisco Jabber in the following situations: If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is not configured for their device, they will not receive
                                             incoming calls on Cisco Jabber. If users select the Mobile Voice Network calling option on any network and the Single Number Reach (SNR) is configured with the Ring Schedule , they will not receive incoming calls on Cisco Jabber beyond the time set in the Ring Schedule . |
|---|---|

| Connection | Calling
                                       				Options |
|---|---|
| Voice over
                                       				IP | Mobile Voice
                                       				Network | Autoselect |
| Corporate
                                       				Wi-Fi | Outgoing:
                                       				VoIP | Incoming:
                                       				VoIP | Outgoing:
                                       				DvO-R | Incoming:
                                       				Mobile Connect | Outgoing:
                                       				VoIP | Incoming:
                                       				VoIP |
| Noncorporate
                                       				Wi-Fi |
| Mobile
                                       				Network (3G, 4G) | Outgoing:
                                       				DvO-R | Incoming: Mobile Connect |
| Phone
                                       				Services are not registered | Outgoing Native Cellular
                                    			 Call |
| Incoming Mobile Connect |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Enterprise Feature Access Number Configuration . |
| Step 3 | Select Add New . |
| Step 4 | In the Number field, enter the Enterprise Feature Access number. Enter a DID number that is unique in the system. To support dialing internationally, you can prepend this number with \+. |
| Step 5 | From the Route Partition drop-down list, choose the partition of the DID that
                                             is required for enterprise feature access. This partition is set under System > Service Parameters , in the Clusterwide Parameters (System - Mobility) section,  in the Inbound Calling Search Space for Remote Destination setting. This setting points either to the Inbound Calling Search Space of the Gateway or Trunk, or to the Calling Search
                                                Space assigned on the Phone Configuration window for the device. If the user sets up the DvO Callback Number with an alternate number, ensure that you set up the trunk Calling Search Space
                                                (CSS) to route to destination of the alternate phone number. |
| Step 6 | In the Description field, enter a description of the Mobility Enterprise Feature Access
                                             number. |
| Step 7 | (Optional) Check the Default Enterprise Feature Access Number check box if you want to make this Enterprise Feature Access number the default for this system. |
| Step 8 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Mobility Profile . |
| Step 3 | In the Mobility Profile Information section, in the Name field, enter a descriptive name for the mobility profile. |
| Step 4 | In the Dial via Office-Reverse Callback section, in the Callback Caller ID field, enter the caller ID for the callback call that the client receives from Cisco Unified Communications Manager. |
| Step 5 | Click Save . |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . |
| Step 3 | Click Add
                                                				New . |
| Step 4 | From the Phone Type drop-down list, choose Cisco Dual Mode for iPhone or Cisco Dual Mode for Android . |
| Step 5 | Click Next . |
| Step 6 | Scroll down to
                                             			 the Product Specific Configuration Layout section, and verify that you can see
                                             			 the Video Capabilities drop-down list. If you can see
                                                				the Video Capabilities drop-down list, the COP file is already installed on
                                                				your system. If you cannot
                                                				see the Video Capabilities drop-down list, locate and download the correct COP
                                                				file. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add a Mobility Identity for each user. |  |
| Step 2 | Enable Dial via Office on each device. |  |
| Step 3 | If you enabled Mobile Connect, verify that Mobile Connect works. Dial the desk phone extension and check that the phone number
                                          that is specified in the associated Mobile Identity rings. |  |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
                                             			 the device that you want to configure as follows: Select Device > Phone . Search
                                                   				  for the device that you want to configure. Select
                                                   				  the device name to open the Phone Configuration window. |
| Step 3 | In the Associated Mobility Identity section, select Add a
                                                				New Mobility Identity . |
| Step 4 | Enter the
                                             			 mobile phone number as the destination number. You must be able to rout this number to an outbound gateway. Generally, the number is the full
                                                				E.164 number. Note If you
                                                            				  enable the Dial via Office — Reverse feature for a user, you must enter a
                                                            				  destination number for the user's mobility identity. If you
                                                            				  enable Dial via Office — Reverse and leave the destination number empty in the
                                                            				  mobility identity: The
                                                                     						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
                                                                     						network and VPN. The
                                                                     						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
                                                                     						network. The
                                                                     						logs do not indicate why the phone service cannot connect. | Note | If you
                                                            				  enable the Dial via Office — Reverse feature for a user, you must enter a
                                                            				  destination number for the user's mobility identity. If you
                                                            				  enable Dial via Office — Reverse and leave the destination number empty in the
                                                            				  mobility identity: The
                                                                     						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
                                                                     						network and VPN. The
                                                                     						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
                                                                     						network. The
                                                                     						logs do not indicate why the phone service cannot connect. |
| Note | If you
                                                            				  enable the Dial via Office — Reverse feature for a user, you must enter a
                                                            				  destination number for the user's mobility identity. If you
                                                            				  enable Dial via Office — Reverse and leave the destination number empty in the
                                                            				  mobility identity: The
                                                                     						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
                                                                     						network and VPN. The
                                                                     						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
                                                                     						network. The
                                                                     						logs do not indicate why the phone service cannot connect. |
| Step 5 | Enter the
                                             			 initial values for call timers. These values
                                                				ensure that calls are not routed to the mobile service provider voicemail
                                                				before they ring in the client on the mobile device. You can adjust these
                                                				values to work with the end user's mobile network. For more information, see
                                                				the online help in Cisco Unified Communications Manager. The following is an example of mobility Identity timers'
                                                				  information in Cisco Unified Communications Manager 9.x. Setting Suggested Initial Value Answer Too Soon Timer 3000 Answer Too Late Timer 20000 Delay Before Ringing Timer 0 Note This setting does not apply to DvO-R calls. The following is an example of mobility Identity timers'
                                                				  information in Cisco Unified Communications Manager 10.x. Setting Suggested Initial Value Wait * before ringing this phone when my business line
                                                            							 is dialed.* 0.0 seconds Prevent this call from going straight to this phone's
                                                            							 voicemail by using a time delay of * to detect when calls go straight to
                                                            							 voicemail.* 3.0 seconds Stop ringing this phone after * to avoid connecting to
                                                            							 this phone's voicemail.* 20.0 seconds | Setting | Suggested Initial Value | Answer Too Soon Timer | 3000 | Answer Too Late Timer | 20000 | Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. | Setting | Suggested Initial Value | Wait * before ringing this phone when my business line
                                                            							 is dialed.* | 0.0 seconds | Prevent this call from going straight to this phone's
                                                            							 voicemail by using a time delay of * to detect when calls go straight to
                                                            							 voicemail.* | 3.0 seconds | Stop ringing this phone after * to avoid connecting to
                                                            							 this phone's voicemail.* | 20.0 seconds |
| Setting | Suggested Initial Value |
| Answer Too Soon Timer | 3000 |
| Answer Too Late Timer | 20000 |
| Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. |
| Note | This setting does not apply to DvO-R calls. |
| Setting | Suggested Initial Value |
| Wait * before ringing this phone when my business line
                                                            							 is dialed.* | 0.0 seconds |
| Prevent this call from going straight to this phone's
                                                            							 voicemail by using a time delay of * to detect when calls go straight to
                                                            							 voicemail.* | 3.0 seconds |
| Stop ringing this phone after * to avoid connecting to
                                                            							 this phone's voicemail.* | 20.0 seconds |
| Step 6 | Do one of the
                                             			 following: Cisco Unified
                                                				Communications Manager release 9 or earlier —  Check the Enable Mobile Connect check box. Cisco Unified
                                                				Communications Manager release 10 —  Check the Enable Single Number Reach check box. |
| Step 7 | If you are
                                             			 setting up the Dial via Office feature, in the Mobility Profile drop-down list,
                                             			 select one of the following options. Option Description Leave
                                                         				  blank Choose
                                                         					 this option if you want users to use the Enterprise Feature Access Number
                                                         					 (EFAN). Mobility
                                                         				  Profile Choose the
                                                         					 mobility profile that you just created if you want users to use a mobility
                                                         					 profile instead of an EFAN. | Option | Description | Leave
                                                         				  blank | Choose
                                                         					 this option if you want users to use the Enterprise Feature Access Number
                                                         					 (EFAN). | Mobility
                                                         				  Profile | Choose the
                                                         					 mobility profile that you just created if you want users to use a mobility
                                                         					 profile instead of an EFAN. |
| Option | Description |
| Leave
                                                         				  blank | Choose
                                                         					 this option if you want users to use the Enterprise Feature Access Number
                                                         					 (EFAN). |
| Mobility
                                                         				  Profile | Choose the
                                                         					 mobility profile that you just created if you want users to use a mobility
                                                         					 profile instead of an EFAN. |
| Step 8 | Set up the
                                             			 schedule for routing calls to the mobile number. |
| Step 9 | Select Save . |

| Note | If you
                                                            				  enable the Dial via Office — Reverse feature for a user, you must enter a
                                                            				  destination number for the user's mobility identity. If you
                                                            				  enable Dial via Office — Reverse and leave the destination number empty in the
                                                            				  mobility identity: The
                                                                     						phone service cannot connect if the user selects the Autoselect calling option while using a mobile data
                                                                     						network and VPN. The
                                                                     						phone service cannot connect if the user selects the Mobile Voice Network calling option on any type of
                                                                     						network. The
                                                                     						logs do not indicate why the phone service cannot connect. |
|---|---|

| Setting | Suggested Initial Value |
|---|---|
| Answer Too Soon Timer | 3000 |
| Answer Too Late Timer | 20000 |
| Delay Before Ringing Timer | 0 Note This setting does not apply to DvO-R calls. | Note | This setting does not apply to DvO-R calls. |
| Note | This setting does not apply to DvO-R calls. |

| Note | This setting does not apply to DvO-R calls. |
|---|---|

| Setting | Suggested Initial Value |
|---|---|
| Wait * before ringing this phone when my business line
                                                            							 is dialed.* | 0.0 seconds |
| Prevent this call from going straight to this phone's
                                                            							 voicemail by using a time delay of * to detect when calls go straight to
                                                            							 voicemail.* | 3.0 seconds |
| Stop ringing this phone after * to avoid connecting to
                                                            							 this phone's voicemail.* | 20.0 seconds |

| Option | Description |
|---|---|
| Leave
                                                         				  blank | Choose
                                                         					 this option if you want users to use the Enterprise Feature Access Number
                                                         					 (EFAN). |
| Mobility
                                                         				  Profile | Choose the
                                                         					 mobility profile that you just created if you want users to use a mobility
                                                         					 profile instead of an EFAN. |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
                                             			 the device that you want to configure as follows: Select Device > Phone . Search for
                                                   				  the device that you want to configure. Select the
                                                   				  device name to open the Phone Configuration window. |
| Step 3 | In the Device
                                                			 Information section, check the 
                                             			 Enable
                                             				Cisco Unified Mobile Communicator check box. |
| Step 4 | In the Protocol Specific Information section, in the Rerouting Calling Search Space drop-down list,
                                             			 select a Calling Search Space (CSS) that can route the call to the DvO callback
                                             			 number. |
| Step 5 | In the Product
                                                			 Specific Configuration Layout section, set the Dial
                                                				via Office drop-down list to Enabled . |
| Step 6 | Select Save . |
| Step 7 | Select Apply
                                                				Config . |
| Step 8 | Instruct the
                                             			 user to sign out of the client and then to sign back in again to access the
                                             			 feature. Note DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from
                                                            the Cisco Unified Communications Manager administrative interface fixes this issue. | Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from
                                                            the Cisco Unified Communications Manager administrative interface fixes this issue. |
| Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from
                                                            the Cisco Unified Communications Manager administrative interface fixes this issue. |

| Note | DVO enabled devices may encounter issues registering with Cisco Unified Communications Manager. Resetting the device from
                                                            the Cisco Unified Communications Manager administrative interface fixes this issue. |
|---|---|

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
                                                   				  Routing > Route/Hunt > Line
                                                   				  Group . The Find
                                                   				  and List Line Groups window opens. |
| Step 3 | Select Add
                                                				New . The Line
                                                   				  Group Configuration window opens. |
| Step 4 | Enter settings
                                             			 in the Line
                                                				Group Information section as follows: Specify a
                                                      					 unique name in the Line Group Name field. Specify
                                                      					 number of seconds for RNA Reversion Timeout . Select a Distribution Algorithm to apply to the line group. |
| Step 5 | Enter settings
                                             			 in the Hunt Options section as follows: Select
                                                      						  a value for No Answer from the drop-down list. Select Automatically Logout Hunt Member on No Answer to configure auto logout of the hunt list. Select
                                                      						  a value for Busy from the drop-down list. Select
                                                      						  a value for Not Available from the drop-down list. |
| Step 6 | In the Line
                                                				Group Member Information section, you can do the following: Find
                                                      					 directory numbers or route partitions to add to the line group. Reorder
                                                      					 the directory numbers or route partitions in the line group. Remove
                                                      					 directory numbers or route partitions from the line group. |
| Step 7 | Select Save . |

| Note | The group call pickup feature and directed call pickup feature do not work with hunt lists. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  List . The Find and Hunt List Groups window opens. |
| Step 3 | Select Add New . The Hunt List Configuration window opens. |
| Step 4 | Enter settings in the Hunt List Information section as follows: Specify a unique name in the Name field. Enter a description for the Hunt List. Select a Cisco Unified Communications Manager
                                                         						Group from the drop-down list. The system selects Enable this Hunt List by default for a
                                                      					 new hunt list when the hunt list is saved. If this hunt list is to be used for voice mail, select For Voice Mail Usage . |
| Step 5 | Select Save to add the hunt list. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  List . The Find and Hunt List Groups window opens. |
| Step 3 | Locate the hunt list to which you want to add a line group. |
| Step 4 | To add a line group, select Add Line Group . The Hunt List Detail Configuration window
                                                				displays. |
| Step 5 | Select a line group from the Line Group drop-down list. |
| Step 6 | To add the line group, select Save . |
| Step 7 | To add additional line groups, repeat Step 4 to Step 6. |
| Step 8 | Select Save. |
| Step 9 | To reset the hunt list, select Reset . When the dialog box appears, select Reset . |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  Pilot . The Find
                                                   				  and List Hunt Pilots window opens. |
| Step 3 | Select Add
                                                				New . The Hunt
                                                   				  Pilot Configuration window opens. |
| Step 4 | Enter the hunt
                                             			 pilot, including numbers and wildcards. |
| Step 5 | Select a hunt
                                             			 list from the Hunt
                                                				List drop-down list. |
| Step 6 | Enter any
                                             			 additional configurations in the Hunt
                                                				Pilot Configuration window. For more information on hunt pilot
                                             			 configuration settings, see the relevant 
                                             			 Cisco Unified Communications Manager documentation. |
| Step 7 | Select Save . |

| Note | Jabber to Jabber calling is only supported for users who authenticate to the Cisco Webex Messenger service. For Cisco Jabber for Windows clients, we recommend running Internet Explorer 10 or greater while using the Jabber to Jabber calling feature. Using the feature with previous versions of Internet Explorer or with Internet Explorer in Compatibility
                                                Mode can cause issues. These issues are with Cisco Jabber client login (non-SSO setup) or Jabber to Jabber calling capability (SSO setup). |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration , go to Device > Phone . |
|---|---|
| Step 2 | Find and select the device. |
| Step 3 | In the Association Information , choose the directory number. |
| Step 4 | In the Directory Number Settings , choose NoVoicemail for Voice Mail Profile . |
| Step 5 | Click Save and then select Apply Config . |

| Note | The Move to Mobile feature requires a mobile telephone network connection with a phone number. Users must have a TCT or BOT
                                          device. |
|---|---|

| Implementation Method | Description | Instructions |
|---|---|---|
| Handoff DN | The
                                          						mobile device calls 
                                          						Cisco Unified Communications Manager using the mobile network. This
                                          						method requires a Direct Inward Dial (DID) number. The
                                          						service provider must deliver the DID digits exactly as configured.
                                          						Alternately, for Cisco IOS gateways with H.323 or SIP communication to 
                                          						Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
                                          						the inbound called-party number at the gateway, presenting the digits to 
                                          						Cisco Unified Communications Manager exactly as configured on the handoff
                                          						DN. This method does not work for iPod Touch devices. | See the Enable Handoff from VoIP to Mobile Network topic. |
| Mobility Softkey | Cisco Unified Communications Manager calls the phone number of the PSTN
                                          						mobile service provider for the mobile device. | See the Enable Transfer from VoIP to Mobile Network topic. |
| None of the above | Disable this feature if you do not want to make it available to
                                          					 users. | Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the TCT device page. Select Disabled for the Transfer to Mobile Network option in the Product Specific Configuration Layout section of the BOT device page. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call Routing > Mobility > Handoff Configuration . |
| Step 3 | Enter the 
                                             			 Handoff Number for the Direct Inward Dial
                                             			 (DID) number that the device uses to hand off a VoIP call to the mobile
                                             			 network. The service provider must deliver the DID digits exactly as
                                                				configured. Alternately, for Cisco IOS gateways with H.323 or SIP communication
                                                				to Cisco Unified Communications Manager, you can use Cisco IOS to manipulate
                                                				the inbound called-party number at the gateway, presenting the digits to Cisco Unified Communications Manager exactly
                                                as configured on the handoff number. Note You cannot use translation patterns or other similar
                                                            				  manipulations within Cisco Unified Communications Manager to match the inbound
                                                            				  DID digits to the configured Handoff DN. | Note | You cannot use translation patterns or other similar
                                                            				  manipulations within Cisco Unified Communications Manager to match the inbound
                                                            				  DID digits to the configured Handoff DN. |
| Note | You cannot use translation patterns or other similar
                                                            				  manipulations within Cisco Unified Communications Manager to match the inbound
                                                            				  DID digits to the configured Handoff DN. |
| Step 4 | Select the Route Partition for the handoff DID. This partition should be present in the Remote Destination inbound
                                                				Calling Search Space (CSS), which points to either the Inbound CSS of the Gateway or Trunk, or the Remote Destination
                                                CSS. This feature does not use the remaining options on this page. |
| Step 5 | Select Save . |

| Note | You cannot use translation patterns or other similar
                                                            				  manipulations within Cisco Unified Communications Manager to match the inbound
                                                            				  DID digits to the configured Handoff DN. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service Parameters . |
| Step 3 | Select the active server. |
| Step 4 | Select the Cisco CallManager (Active) service. |
| Step 5 | Scroll down to the Clusterwide Parameters (System - Mobility) section. |
| Step 6 | Select Matching Caller ID with Remote Destination and
                                             			 read essential information about this value. |
| Step 7 | Select Partial Match for Matching Caller ID with Remote
                                                				Destination . |
| Step 8 | Select Number of Digits for Caller ID Partial Match and read the essential requirements for this value. |
| Step 9 | Enter the required number of digits to ensure partial matches. |
| Step 10 | Select Save . |

| Step 1 | In the Cisco Unified CM Administration interface, go to the TCT Device page, and select Use Handoff DN Feature for the Transfer to Mobile Network option. Do not assign this method for iPod Touch devices. Use the Mobility Softkey method instead. |
|---|---|
| Step 2 | In the Cisco Unified CM Administration interface, go to the BOT Device page, and select Use Handoff DN Feature for the Transfer to Mobile Network option. |
| Step 3 | On the iOS device, tap Settings > Phone > Show My Caller ID to verify that Caller ID is on. |
| Step 4 | On some Android device and operating system combinations, you can verify that the Caller ID is on. On the Android device,
                                             open the Phone application and tap Menu > Call Settings > Additional settings > Caller ID > Show Number . |
| Step 5 | Test this
                                             			 feature. |

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | For
                                          			 system-level settings, check that the Mobility softkey appears when the phone
                                          			 is in the connected and on-hook call states. Select Device > Device
                                                      						Settings > Softkey Template . Select the
                                                				  same softkey template that you selected when you configured the device for
                                                				  Mobile Connect. In the Related Links drop-down list at the upper right,
                                                				  select Configure Softkey Layout and select Go . In the
                                                				  call state drop-down list, select the On Hook state and verify that the
                                                				  Mobility key is in the list of selected softkeys. In the
                                                				  call state drop-down list, select the Connected state and verify that the
                                                				  Mobility key is in the list of selected softkeys. |
| Step 3 | Navigate to
                                          			 the device that you want to configure as follows: Select Device > Phone . Search for
                                                				  the device that you want to configure. Select the
                                                				  device name to open the Phone Configuration window. |
| Step 4 | For the
                                          			 per-user and per-device settings in 
                                          			 Cisco Unified Communications Manager, set the specific device to use the
                                          			 Mobility softkey when the device transfers calls to the mobile voice network.
                                          			 Ensure that you have set up both Mobility Identity and Mobile Connect for the
                                          			 mobile device. After the transfer feature is working, users can enable and
                                          			 disable Mobile Connect at their convenience without affecting the feature. If the device is an iPod Touch, you can configure a Mobility Identity using an alternate phone number such as the mobile phone
                                             of the user. Select the Owner User ID on the device page. Select the Mobility User ID . The value usually matches that of
                                                				  the Owner User ID. In the
                                                				  Product Specific Configuration Layout section, for the Transfer to Mobile
                                                				  Network option, select Use Mobility Softkey or Use HandoffDN Feature . |
| Step 5 | In the User
                                          			 Locale field, choose English, United States . |
| Step 6 | Select Save . |
| Step 7 | Select Apply Config . |
| Step 8 | Instruct the user to sign out of the client and then to sign back
                                          			 in again to access the feature. |

| Important | For Cisco Jabber Softphone for VDI , merge call functionality requires the following configuration: Set Join And Direct Transfter Policy to Same line, across line enable . Check the Override Enterprise Settings check box. |
|---|---|

| Step 1 | From Cisco Unified CM Administration , go to Device > Phone , and find and select the device. |
|---|---|
| Step 2 | For each line you want to configure: Click Add a new DN , enter a Directory Number . Add any additional configurations and click Save . |

| Step 1 | Go to VCS-C. |
|---|---|
| Step 2 | Select VSC-C configuration > Unified Communication > Configuration > SIP Path headers and set it to On . |

| Step 1 | Personal Rooms are enabled by default for users on Cisco Webex Meetings. For more information see the Cisco Webex Meetings
                                       documentation available here: https://www.cisco.com/c/en/us/support/conferencing/webex-meeting-center/products-installation-and-configuration-guides-list.html |
|---|---|
| Step 2 | Users can configure their personal rooms for all instant meetings by selecting Use Personal Room for all my instant meetings in Cisco Webex Meetings. |

| Note | If the user manually terminates Jabber with the push notification service enabled, then the ForceLogoutTimerMobile parameter does not function. We recommend that you disable the push notification service if you want to use the ForceLogoutTimerMobile parameter. |
|---|---|

| Step 1 | Go to Cisco Unified CM Administration > Advanced Features > Cisco Cloud Onboarding . |
|---|---|
| Step 2 | From the Notification Settings, check Enable Push Notification . |
| Step 3 | Click Save . |

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | Configure the end user for single number reach as follows: Go to User Management > End User , search for the user and click their name. In the Mobility Information section, check the Enable Mobility check box. On Cisco Unified Communications Manager Release 9.0 and earlier, specify the Primary User Device. Click Save . |
| Step 3 | Create their remote destination profile. Go to Device > Device Settings > Remote Destination Profile > Add New . Enter the required values and click Save . Click Add a New Directory Number and enter the directory number of the desk phone to associate with the remote destination profile. Click Save . Click Add a New Remote Destination , enter the number for your remote destination in Destination number and choose the User ID . Click Enable Unified Mobility features, and click the following options: Enable Single Number Reach Enable Move to Mobile Click Save . |

| Step 1 | From Cisco TelePresence Video Communication Server Control (VCS), choose Configuration > Unified Communications > HTTP allow list > Editable inbound rules |
|---|---|
| Step 2 | Click New to create a new entry |
| Step 3 | Enter the following details: Description—Enter the required description. URL—Enter the URL details. For example, https://[CUCM domain name]: port number . Allowed Methods—Check the default value. For example, GET, POST, PUT Match Type—Choose Prefix match from the drop-down list. |
| Step 4 | Click Save . |

| Important | The mobile clients don't support URI dialing when you enable the Dial via Office-Reverse feature. |
|---|---|

| Step 1 | Add devices. |
|---|---|
| Step 2 | Add directory numbers to the devices. |
| Step 3 | Associate users with the devices. |
| Step 4 | Specify primary extensions for users. |

| Step 1 | Open the Cisco
                                                   				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Call
                                                      				  Routing > Directory Number . The Find
                                                      				  and List Directory Numbers window opens. |
| Step 3 | Find and
                                                			 select the appropriate directory number. The Directory Number Configuration window opens. |
| Step 4 | Locate the Directory URIs section. |
| Step 5 | Specify a
                                                			 valid SIP URI in the URI column. |
| Step 6 | Select the
                                                			 appropriate partition from the Partition column. Note You cannot
                                                                  					 manually add URIs to the system Directory URI partition. You should add the URI to
                                                                  					 the same route partition as the directory number. | Note | You cannot
                                                                  					 manually add URIs to the system Directory URI partition. You should add the URI to
                                                                  					 the same route partition as the directory number. |
| Note | You cannot
                                                                  					 manually add URIs to the system Directory URI partition. You should add the URI to
                                                                  					 the same route partition as the directory number. |
| Step 7 | Add the
                                                			 partition to the appropriate calling search space so that users can place calls
                                                			 to the directory numbers. |
| Step 8 | Select Save . |

| Note | You cannot
                                                                  					 manually add URIs to the system Directory URI partition. You should add the URI to
                                                                  					 the same route partition as the directory number. |
|---|---|

| Important | To enable URI dialing, you must associate the default directory URI partition with a partition that contains directory numbers. If you do not already have a partition for directory numbers within a calling search space, you should create a partition
                                                   and configure it as appropriate. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Enterprise Parameters . The Enterprise Parameters Configuration window opens. |
| Step 3 | Locate the End User Parameters section. |
| Step 4 | In the Directory URI Alias Partition row, select the appropriate partition from the drop-down list. |
| Step 5 | Click Save . |

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device
                                                				  Settings > SIP Profile . The Find
                                                				  and List SIP Profiles window opens. |
| Step 3 | Find and
                                          			 select the appropriate SIP profile. Remember You cannot
                                                            					 edit the default SIP profile. If required, you should create a copy of the
                                                            					 default SIP profile that you can modify. | Remember | You cannot
                                                            					 edit the default SIP profile. If required, you should create a copy of the
                                                            					 default SIP profile that you can modify. |
| Remember | You cannot
                                                            					 edit the default SIP profile. If required, you should create a copy of the
                                                            					 default SIP profile that you can modify. |
| Step 4 | Select Use
                                             				Fully Qualified Domain Name in SIP Requests and then select Save . |

| Remember | You cannot
                                                            					 edit the default SIP profile. If required, you should create a copy of the
                                                            					 default SIP profile that you can modify. |
|---|---|

| Important | User-controlled
                                             			 voicemail avoidance is available on 
                                             			 Cisco Unified Communications Manager, release 9.0 and later. |
|---|---|

| Important | Cisco does not
                                             			 support user-controlled voicemail avoidance when using DvO-R with alternate
                                             			 numbers that the end user sets up in the client. An alternate number is any
                                             			 phone number that the user enters in the DvO Callback Number field on the
                                             			 client that does not match the phone number that you set up on the user's
                                             			 Mobility Identity. If you set up
                                             			 this feature with alternate numbers, the 
                                             			 Cisco Unified Communications Manager connects the DvO-R calls even if the
                                             			 callback connects to a wrong number or a voicemail system. |
|---|---|

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service
                                                   				  Parameters . |
| Step 3 | In the Server drop-down list, select the active 
                                             			 Cisco Unified Communications Manager. |
| Step 4 | In the Service drop-down list, select the Cisco
                                                				Call Manager (Active) service. |
| Step 5 | Configure the
                                             			 settings in the Clusterwide Parameters (System - Mobility Single Number Reach
                                                				Voicemail) section. Note The settings
                                                            				  in this section are not specific to 
                                                            				  Cisco Jabber. For information about how to
                                                            				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
                                                            				  release. | Note | The settings
                                                            				  in this section are not specific to 
                                                            				  Cisco Jabber. For information about how to
                                                            				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
                                                            				  release. |
| Note | The settings
                                                            				  in this section are not specific to 
                                                            				  Cisco Jabber. For information about how to
                                                            				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
                                                            				  release. |
| Step 6 | Click Save . |

| Note | The settings
                                                            				  in this section are not specific to 
                                                            				  Cisco Jabber. For information about how to
                                                            				  configure these settings, see the Confirmed Answer and DvO VM detection section in the Cisco Unified Communications Manager Administrator Guide for your
                                                            				  release. |
|---|---|

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
                                             			 the device that you want to configure as follows: Select Device > Phone . Search for
                                                   				  the device that you want to configure. Select the
                                                   				  device name to open the Phone Configuration window. |
| Step 3 | In the Associated Mobility Identity section, click the link
                                             			 for the Mobility Identity. Note To ensure
                                                            				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
                                                            				  that the end user enters in the 
                                                            				  Cisco Jabber client must match the Destination
                                                            				  Number that you enter on the Mobility Identity Configuration screen. | Note | To ensure
                                                            				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
                                                            				  that the end user enters in the 
                                                            				  Cisco Jabber client must match the Destination
                                                            				  Number that you enter on the Mobility Identity Configuration screen. |
| Note | To ensure
                                                            				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
                                                            				  that the end user enters in the 
                                                            				  Cisco Jabber client must match the Destination
                                                            				  Number that you enter on the Mobility Identity Configuration screen. |
| Step 4 | Set the
                                             			 policies as follows: Cisco Unified Communications Manager  release 9 
                                                				   — In the Single Number Reach Voicemail Policy drop-down list,
                                                					 select User Control . Cisco Unified Communications Manager release 10 without Dial via Office 
                                                				   — In the Single Number Reach Voicemail Policy drop-down list,
                                                					 select User Control . Cisco Unified Communications Manager release 10 with Dial via Office In the Single Number Reach Voicemail Policy drop-down list,
                                                      						  select Timer Control . In the Dial-via-Office Reverse Voicemail Policy drop-down
                                                      						  list, select User Control . |
| Step 5 | Click Save . |

| Note | To ensure
                                                            				  that the Voicemail Avoidance feature works correctly, the DvO Callback Number
                                                            				  that the end user enters in the 
                                                            				  Cisco Jabber client must match the Destination
                                                            				  Number that you enter on the Mobility Identity Configuration screen. |
|---|---|

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Navigate to
                                             			 the device that you want to configure as follows: Select Device > Phone . Search for
                                                   				  the device that you want to configure. Select the
                                                   				  device name to open the Phone Configuration window. |
| Step 3 | In the Associated Remote Destinations section, click the
                                             			 link for the associated remote destination. |
| Step 4 | Set the
                                             			 policies as follows: Cisco Unified Communications Manager
                                                					 release 9
                                                				   — In the Single Number Reach Voicemail Policy drop-down list, select User Control . Cisco Unified Communications Manager
                                                					 release 10 without Dial via Office
                                                				  — In the Single Number Reach Voicemail Policy drop-down list, select User Control . Cisco Unified Communications Manager
                                                					 release 10 with Dial via Office In the Single Number Reach Voicemail Policy drop-down list, select Timer Control . In the Dial-via-Office Reverse Voicemail
                                                         							 Policy drop-down list, select User Control . |
| Step 5 | Click Save . |

| Step 1 | In Unity Connection Administration , go to Messaging Configuration . |
|---|---|
| Step 2 | Set Sent Messages: Retention Period (in Days) to a positive number to enable this feature. |

| Note | If you also enable zip tones, the zip tone only plays with Jabber when the CSF device auto answers with a headset. Zip tones
                                          do not play when a speakerphone auto answers the call. |
|---|---|

| Note | Jabber doesn't support Extension Mobility in contact center deployments. |
|---|---|