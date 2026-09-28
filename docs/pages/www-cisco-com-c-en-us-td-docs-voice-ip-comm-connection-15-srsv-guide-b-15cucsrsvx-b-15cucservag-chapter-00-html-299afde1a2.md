---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-srsv-guide-b-15cucsrsvx-b-15cucservag-chapter-00-html-299afde1a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/srsv/guide/b_15cucsrsvx/b_15cucservag_chapter_00.html
retrieved_at: 2026-08-16T18:46:43.254380+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: December 18, 2023

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Overview

Cisco Unity Connection Survivable Remote Site Voicemail (Cisco Unity
                           		Connection SRSV) provides cost-effective backup voicemail and auto attendant
                           		services for remote sites, such as branch offices or small sites.

When a branch site is unable to access the central voicemail server due
                           		to network interruptions (WAN outages), Unity Connection SRSV ensures that all
                           		the remote sites continue to have voicemail services and outside callers have
                           		the same experience as when they are communicating with the central Unity
                           		Connection.

After restoring the network connection to the central site, all the
                           		voicemails received by subscribers at the branch site are automatically
                           		uploaded to the central server.

## Components of
                        	 SRSV

Unity Connection
                           		SRSV has two sites, namely, the central site and the branch site. Each site has
                           		essential components to deliver messaging and voicemail services.

Following are the
                           		two sites in a Unity Connection SRSV topology:

The central
                                 			 site has Cisco Unified Communications Manager that provides call processing
                                 			 between central Unity Connection server and Cisco Unified CM. Unity Connection
                                 			 is integrated with a Cisco Unified CM server to deliver integrated messaging
                                 			 and voicemail services.

The Cisco
                                 			 Unified Messaging Gateway (UMG) SRSV module at the central site handles the
                                 			 voicemail provisioning between the central and remote sites as well as
                                 			 voicemail upload from the remote site to the central location after the network
                                 			 service is restored.

The branch site
                                 			 either has a Cisco Unified Survivable Remote Site Telephony (SRST) router or
                                 			 Cisco Unified CM Express (CUCME-SRST) that handles call processing during WAN
                                 			 outages or any other network interruptions. The Unity Connection SRSV server
                                 			 provides backup voicemail solutions to the branch site during WAN outages.

## SRSV
                        	 Topologies

The conventions
                              		  for all the SRSV topologies are:

Convention

Description

CUC

Cisco
                                          						Unity Connection

CCM

Cisco
                                          						Unified Communications Manager (Cisco Unified CM)

CCM-phone

The
                                          						phones registered with Cisco Unified CM at the central site.

SRST-
                                          						phone

The
                                          						phones registered with SRST router at the branch site.

CUCME-phone

The
                                          						phones registered with CUCME-SRST router at the branch site.

Each topology has
                              		  a SRST router is deployed at the branch site. When a WAN outage occurs or there
                              		  is a loss in PSTN connectivity, the IP phones on the remote site get registered
                              		  with a SRST router. The IP phones then display SRST Enabled mode on the
                              		  screens. The Unity Connection SRSV at the branch site remains in the idle state
                              		  and is ready to receive calls from the SRST router.

Following are the
                              		  three topolgies supported with Unity Connection SRSV:

The Figure 1 shows a topology in which the SRST router remains idle and waits for the IP phones to register with it. When the WAN outage
                                    occurs, the branch office IP phones registered with the central Cisco Unified CM detect the loss of connectivity and register
                                    with the SRST router. Now, all the incoming calls to the branch are handled by SRST. SRST forwards the unanswered calls (either
                                    busy or no answer) to the SRSV voicemail server that allows the caller to leave a voicemail for the user at the branch site.
                                    As a result, the branch office voicemail continues to work during WAN outages when the central office voicemail system is
                                    unreachable.

However, when
                                    				the WAN connection is restored, the IP phones automatically register with the
                                    				central Cisco Unified CM. All the calls are then managed by Cisco Unified CM
                                    				and the no answer or busy calls are forwarded to the central Unity Connection
                                    				voicemail system. All the voicemails stored on the branch get automatically
                                    				synchronized with the central Unity Connection server.

The Figure 2 shows a topology in which CUCME-SRST (also known as SRST Fallback Mode) router remains in the idle state and waits for the
                                    IP phones to register with it. When a WAN outage occurs or PSTN connectivity goes down, the phones on the remote site get
                                    registered with the CUCME- SRST router. As a result, the branch office voicemail continues to work during WAN outages when
                                    the central office voicemail system is unreachable.

However, when
                                    				the WAN connection is restored, the IP phones automatically register with the
                                    				central Cisco Unified CM. All the calls are then managed by Cisco Unified CM
                                    				and the no answer or busy calls are forwarded to the central Unity Connection
                                    				voicemail system. All the voicemails stored on the branch get automatically
                                    				synchronized with the central Unity Connection server.

The Figure 3 shows a topology where multiple CUCME-SRST and SRSV devices are paired for load balancing at the survivable branch site.
                                    In this scenario, the administrator divides the branch users between CUCME-SRST-1 and CUCME-SRST-2. The central Unity Connection
                                    server sends the appropriate configuration of the users to SRSV-1 and SRSV-2 at the branch site.

When a WAN
                                    				outage occurs or PSTN goes down, each SRSV device handles the calls directed to
                                    				it from the paired CUCME-SRST device. As a result, the branch office voicemail
                                    				continues to work during WAN outages when the central office voicemail system
                                    				is unreachable.

However, when
                                    				the WAN connection is restored, the IP phones automatically register with the
                                    				central Cisco Unified CM. All the calls are then managed by Cisco Unified CM
                                    				and the no answer or busy calls are forwarded to the central Unity Connection
                                    				voicemail system. All the voicemails stored on the branch get automatically
                                    				synchronized with the central Unity Connection server.

Cisco Unified Enhanced SRST (E-SRST) is used to deploy advanced Cisco Unified CM telephony features in survivable mode. The
                                                E-SRST feature is not required if you are using original SRST and not provisioning advanced telephony features for use in
                                                survivable mode. For more information on E-SRST, see the " Enhanced Survivable Remote Site Telephony (E-SRST) " section of the "Overview of Cisco Unified Messaging Gateway Release 8.5" chapter of the Cisco Unified Messaging Gateway
                                                8.5 Administrator Guide at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/umg/rel8_5/admin_guide/UMGadmin.html .

MWI functionality for the branch site users is supported only if Unity Connection SRSV is SIP integrated with the SRST router.

## Accessing Unity Connection SRSV Using Phone

When you access the Unity
                           		Connection SRSV server using phone, you hear the Unity Connection SRSV
                           		conversation that includes the recorded instructions and system prompts that
                           		guide you to receive messages.

### Using the Phone
                           	 Keypad with the Unity Connection SRSV Conversation

You can press any of the keys on phone keypad to access the Unity
                              		Connection SRSV server. There are several versions of the Unity Connection SRSV
                              		conversation, each providing different keypad mappings for the Unity Connection
                              		SRSV menu options. (For example, you might press 3 to delete a message in one
                              		version but press 7 to delete a message in another version.)

The Unity Connection SRSV administrator determines the conversation
                              		version that you hear. Typically, an administrator selects a conversation that
                              		has a keypad mapping familiar to the user.

### Calling Unity
                           	 Connection SRSV

You can call
                                 		  Unity Connection SRSVeither from your desk phone or any another phone within
                                 		  your organization.

Step 1

Dial the
                                          			 applicable number to call Unity Connection SRSV.

Step 2

If you are
                                          			 calling from any other phone in your organization which is not registered as
                                          			 your known extension in Unity Connection SRSV, press * (star key) when Unity
                                          			 Connection SRSV answers.

Step 3

When
                                          			 prompted, enter your ID and press # (pound key) to continue.

Step 4

Enter your
                                          			 Unity Connection SRSV PIN and press # to login in to your account.

### Sending
                           	 Voicemails

You can send voicemails to other
                              		Unity Connection SRSVusers without dialing their extensions.

Tip

### Managing
                           	 Receipts

Following types of receipts can be
                              		managed when working with Unity Connection SRSV:

NondeliveryReciept message
                                    			 informs you when your message is not delivered to the intended recipient. When
                                    			 you check messages, Unity Connection SRSV plays receipts along with your other
                                    			 messages. You can play and delete receipts in the same way as other messages
                                    			 but you cannot reply to or forward the receipts.

- Read Receipts: Unity
                                 		  Connection SRSV plays a list of the recipients who read the message you sent.
                                 		  For nondelivery receipts (NDRs), Unity Connection SRSV identifies recipients
                                 		  whose mailboxes did not accept the message.

After Unity Connection SRSV plays an NDR, you can hear the original
                              		message and resend it to the recipient(s) who failed to receive it. You can
                              		record an introduction, modify the recipient list, and change delivery options
                              		when resending a message. Once you resend the message, Unity Connection SRSV
                              		automatically deletes the NDR.

#### Managing Receipts
                              	 Using Phone Keypad

Step 1

Call and sign
                                             			 in to Unity Connection SRSV.

Step 2

From the Main
                                             			 menu, select Play New Messages and then select Receipts.

Step 3

Follow the
                                             			 prompts to manage your receipt.

### Finding Messages
                           	 Using Phone Keypad

As you listen to
                                 		  your messages, you can use the Go to Message option to find a particular
                                 		  message by entering the number of the message.

Step 1

Call and sign
                                          			 in to Unity Connection SRSV.

Step 2

From the Main
                                          			 menu, select either Play New Messages or Review Old Messages.

Step 3

Press the Go
                                          			 to Message shortcut keys.

Tip

Step 4

When
                                          			 prompted, enter the message number followed by #.

Step 5

Follow the
                                          			 prompts to manage the message after you have listened to it.

### Managing Deleted
                           	 Messages

Unity Connection SRSV saves your
                              		deleted messages that you can play, restore, or permanently delete. Deleting
                              		messages permanently can be an important way to reduce the size of your
                              		mailbox, especially if Unity Connection SRSV is not set up to automatically
                              		delete messages once they reach a certain age.

Ask your Unity Connection SRSV administrator if the system is set up to
                              		enforce a message-retention policy. Unity Connection SRSV neither indicates
                              		when a message-retention policy is enforced nor does it warn you before
                              		messages are permanently deleted as a result of the policy. If Unity Connection
                              		SRSV is not set up to do so, make sure that you permanently delete messages
                              		periodically.

#### Permanently
                              	 Deleting Messages Using Phone Keypad

Step 1

Call and sign
                                             			 in to Unity Connection SRSV.

Step 2

From the Main
                                             			 menu, select Review Old Messages and then select Deleted Messages.

Step 3

Follow the
                                             			 prompts to review your deleted messages and delete them individually, or to
                                             			 delete all messages at once.

### Checking Deleted
                           	 Messages

You can play your deleted messages, just as you can play new and saved
                              		messages. You can also restore a deleted message as a new or saved message.

By default, the most recent messages are played first. Note that you
                              		cannot enable the Message Type menu or specify a playback order by message type
                              		for deleted messages.

#### Checking Deleted
                              	 Messages Using Phone Keypad

Step 1

Call and sign
                                             			 in to Unity Connection SRSV.

Step 2

At the Main
                                             			 menu, select Review Old Messages and then select Deleted Messages.

Step 3

Follow the
                                             			 prompts to manage a deleted message after you have listened to it.

### Changing Alternate
                           	 Contact Numbers

To specify an alternate contact
                              		number outside your organization, begin with the access code needed to make an
                              		external call (for example, 9). For long-distance numbers, include the
                              		applicable dialing codes (for example, 1 and the area code).

### Specifying
                           	 Playback Settings

Playback settings allow you to
                              		change the playback volume and the playback speed of:

- An individual message when you are
                                 		  listening to it.

- The conversation of your
                                 		  current phone session at any point while Unity Connection SRSV is playing a
                                 		  prompt.

Changes in individual message playback do not affect playback of other
                              		messages you hear during the same phone session. Changes in conversation
                              		playback remain applicable until you hang up the phone; the next time you call
                              		Unity Connection SRSV, playback settings are reset to the defaults.

#### Changing Playback
                              	 Volume for Individual Messages

As you listen to a message by
                                 		phone, you can adjust the volume for that message. The changes to the message
                                 		playback do not affect the playback volume of other messages that you hear
                                 		during the same phone session.

#### Changing Playback Volume for an Individual Message Using Phone
                              	 Keypad

The key that you press to adjust
                                    		  playback volume depends on your conversation. Ask your system administrator
                                    		  which key is assigned to change playback volume. While listening to a message,
                                    		  toggle among the following volume settings:

#### Changing Playback
                              	 Speed for Individual Messages

As you listen to a message by
                                    		  phone, you can adjust the playback speed for that message. Changes do not
                                    		  affect the playback speed of other messages that you hear during the same phone
                                    		  session.

The key that you press to adjust playback speed depends on your
                                    		  conversation. Ask your system administrator which keys are assigned to increase
                                    		  and decrease playback speed. While listening to a message, use the following
                                    		  speed settings:

#### Changing Playback
                              	 Volume for the Unity Connection Conversation

You can use voice commands to
                                    		  change the volume of the Unity Connection SRSV conversation at any point while
                                    		  Unity Connection SRSV is playing prompts. (You cannot use the phone keypad to
                                    		  adjust the conversation volume.)

Changes last until you hang up the phone; the next time you call
                                    		  Unity Connection SRSV, the volume is reset to the default setting.

#### Changing Playback
                              	 Speed for the Unity Connection Conversation

You can use voice commands to
                                 		change the speed of the Unity Connection SRSV conversation at any point while
                                 		Unity Connection SRSV is playing prompts. (You cannot use the phone keypad to
                                 		adjust the conversation speed.)

Changes last until you hang up the phone; the next time you call Unity
                                 		Connection SRSV, the speed is reset to the default setting.

### Phone Menus for the Classic Conversation

#### Main Menu and
                              	 Shortcuts

While listening to the Main
                                    		  menu, press:

Review deleted messages

(Not available on some systems)

#### During Message
                              	 Menu and Shortcuts

While listening to a message,
                                    		  press:

Change volume

(Not available on some systems)

Restore as saved

(Not available on some systems)

Save or restore as new

(Not available on some systems)

#### After Message Menu
                              	 and Shortcuts

After listening to a message,
                                    		  press:

Save or restore as saved

(Not available on some systems)

#### Recording
                              	 Menu

Use the following keys while you
                                    		  record a message:

#### After Message Menu and Shortcuts (Alternate Keypad Mapping N)

After listening
                                    		  to a message, press:

Call the
                                                						sender

(Not
                                                						available on some systems)

Save or
                                                						restore as saved

(Not
                                                						available on some systems)

Save or
                                                						restore as new

(Not
                                                						available on some systems)

#### Recording Menu (Alternate Keypad Mapping N)

Use the following keys while you
                                    		  record messages, names, and greetings:

## Provisioning Data Synchronization between Central Unity Connection and
                        	 Unity Connection SRSV

Following is the list of data
                           		synchronized between the central Unity Connection and Unity Connection SRSV:

- FirstName

- LastName

- Alias

- DisplayName

- Language

- DtmfAccessId

- SmptAddress

- VoiceName

- Undeletable

- ObjectId

- callhandlerobjectid

- initials

- title

- employeeId

- address

- building

- city

- state

- postalcode

- country

- timezone

- department

- manager

- billingId

- emailAddress

- useDefaultTimeZone

- useDefaultLanguage

- saySenderExtension

- sayAni

- saySender

- listInDirectory

- Fetch voicename for the
                              		  user

- Fetch user PIN

- Fetch users' MWI display
                              		  name and status

- Fetch message settings for
                              		  the user

- Fetch greeting for the
                              		  user: While changing the greeting for a user on the central server, check the
                              		  Sync Provisioning check box on the central server to synchronize the new
                              		  greeting to the branch server.

- Fetch distribution list: If
                              		  the Replicate to SRSV Branch check box is checked on the Edit Distribution List
                              		  Settings page on the central server, the distribution list data is synchronized
                              		  with the branch server.

## Limitations and Restrictions

### Voicemail
                           	 Limitations and Restrictions

Unity Connection SRSV has several
                              		voicemail limitations and restrictions:

The following features are not
                                    			 supported with Unity Connection SRSV:

- Fax support

- Addressing contacts

- Dispatch messages

- Scheduled base
                                       				services, such as alternate greetings and notifications.

- Advanced telephony
                                       				features, such as call screening and call transfer.

- Updating spoken name,
                                       				distribution lists, or PINs through the touchtone conversation users
                                       				functionality.

- Touchtone conversation
                                       				users administration interfaces, such as broadcast or greeting administration.

- Private distribution
                                       				lists.

- Text-to-speech or voice
                                       				recognition features.

- Customizing the
                                       				voicemail flow for touchtone conversation users (TUI).

- VPIM

- IMAP

- Single Inbox

- Cisco Personal
                                       				Communications Assistant and Web Inbox.

- The Compose, Forward, and
                                 		  Reply to voicemails functionalities are not supported with Unity Connection
                                 		  SRSV. Only the Ring No Answer or Call Forward Busy functionalities are
                                 		  supported.

- The voicemail
                                 		  synchronization is supported only via central Unity Connection server. The
                                 		  voicemails received on central Unity Connection server are not replicated to
                                 		  the Unity Connection SRSV.

- The voicemail upload is not
                                 		  synchronized with the registration of phones with Cisco Unified Communications
                                 		  Manager.

- The call handler
                                 		  configuration is not included in the provisioning data and this data is not
                                 		  synchronized between the central Unity Connection and the Unity Connection SRSV
                                 		  server.

- The system transfers for non
                                 		  user extensions cannot be accomplished in Unity Connection SRSV. because the
                                 		  Allow Transfers to Numbers Not Associated with Users or Call Handlers setting
                                 		  on the Edit Greeting page of a user in Cisco Unity Connection Administration is
                                 		  not present in Unity Connection SRSV.

- Few central Unity Connection
                                 		  server class of service (COS) features, such as distribution list access and
                                 		  message deletion behavior are provisioned for all Unity Connection SRSV users.

- The subscribers cannot log
                                 		  in to Cisco Unity Connection SRSV Administration until they set up their
                                 		  voicemail preferences at central Unity Connection server.

- The Live Record and Live
                                 		  Reply functionalities are not supported.

### Auto-Attendant
                           	 Limitations

The auto-attendant configuration
                              		is done at branch site only. There is no synchronization required from central
                              		Unity Connection server. The auto-attendants help internal and external callers
                              		locate users or departments in an organization and transfer calls to them.

Following are the auto-attendant features not supported with Unity
                              		Connection SRSV:

- Partitions or search spaces

- Advanced calling features,
                                 		  such as call screening

- Interview handlers

- Dispatch messages

### Network Address Translation (NAT) Restrictions

- NAT is supported only at branch
                                 		  locations and not at the central Unity Connection server.

- Only one Unity Connection
                                 		  SRSV can be provisioned at each NAT site.

- Only static NAT and Port
                                 		  Address Translation (PAT) are supported.

- Dynamic NAT is not
                                 		  supported.

### Backup and Restore
                           	 Limitations

To avoid creating duplicate email
                              		messages, we do not recommend taking the Disaster Recovery System backup of
                              		data on Unity Connection SRSV.

### Distribution Lists Limitations

- The voicemails sent to distribution
                                 		  lists in survivable mode are sent to members only after WAN is recovered.

- The system does not
                                 		  provision spoken names for distribution lists.

- The system does not
                                 		  provision recorded names for distribution lists.

- Only public distribution
                                 		  lists are supported.

| Note | Cisco
                                             				Unified CM is integrated with a Unity Connection server either using Skinny
                                             				Call Control Protocol (SCCP) or Session Initiation Protocol (SIP). |
|---|---|

| Convention | Description |
|---|---|
| CUC | Cisco
                                          						Unity Connection |
| CCM | Cisco
                                          						Unified Communications Manager (Cisco Unified CM) |
| CCM-phone | The
                                          						phones registered with Cisco Unified CM at the central site. |
| SRST-
                                          						phone | The
                                          						phones registered with SRST router at the branch site. |
| CUCME-phone | The
                                          						phones registered with CUCME-SRST router at the branch site. |

| Note | Cisco Unified Enhanced SRST (E-SRST) is used to deploy advanced Cisco Unified CM telephony features in survivable mode. The
                                                E-SRST feature is not required if you are using original SRST and not provisioning advanced telephony features for use in
                                                survivable mode. For more information on E-SRST, see the " Enhanced Survivable Remote Site Telephony (E-SRST) " section of the "Overview of Cisco Unified Messaging Gateway Release 8.5" chapter of the Cisco Unified Messaging Gateway
                                                8.5 Administrator Guide at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/umg/rel8_5/admin_guide/UMGadmin.html . MWI functionality for the branch site users is supported only if Unity Connection SRSV is SIP integrated with the SRST router. |
|---|---|

| Step 1 | Dial the
                                          			 applicable number to call Unity Connection SRSV. |
|---|---|
| Step 2 | If you are
                                          			 calling from any other phone in your organization which is not registered as
                                          			 your known extension in Unity Connection SRSV, press * (star key) when Unity
                                          			 Connection SRSV answers. |
| Step 3 | When
                                          			 prompted, enter your ID and press # (pound key) to continue. |
| Step 4 | Enter your
                                          			 Unity Connection SRSV PIN and press # to login in to your account. |

| Tip | Unity Connection SRSV plays a list of matches that you
                                       		can navigate through quickly. Press # to select a recipient from a list; press
                                       		7 to skip to the previous name and 9 to skip to the next name; and press 77 to
                                       		skip to the beginning of a list and 99 to skip to the end of a list. |
|---|---|

| Step 1 | Call and sign
                                             			 in to Unity Connection SRSV. |
|---|---|
| Step 2 | From the Main
                                             			 menu, select Play New Messages and then select Receipts. |
| Step 3 | Follow the
                                             			 prompts to manage your receipt. |

| Step 1 | Call and sign
                                          			 in to Unity Connection SRSV. |
|---|---|
| Step 2 | From the Main
                                          			 menu, select either Play New Messages or Review Old Messages. |
| Step 3 | Press the Go
                                          			 to Message shortcut keys. Tip Ask your Unity Connection SRSV administrator for the shortcut keys that you use
                                                      				to hear the prompt for entering the message number. | Tip | Ask your Unity Connection SRSV administrator for the shortcut keys that you use
                                                      				to hear the prompt for entering the message number. |
| Tip | Ask your Unity Connection SRSV administrator for the shortcut keys that you use
                                                      				to hear the prompt for entering the message number. |
| Step 4 | When
                                          			 prompted, enter the message number followed by #. |
| Step 5 | Follow the
                                          			 prompts to manage the message after you have listened to it. |

| Tip | Ask your Unity Connection SRSV administrator for the shortcut keys that you use
                                                      				to hear the prompt for entering the message number. |
|---|---|

| Step 1 | Call and sign
                                             			 in to Unity Connection SRSV. |
|---|---|
| Step 2 | From the Main
                                             			 menu, select Review Old Messages and then select Deleted Messages. |
| Step 3 | Follow the
                                             			 prompts to review your deleted messages and delete them individually, or to
                                             			 delete all messages at once. |

| Step 1 | Call and sign
                                             			 in to Unity Connection SRSV. |
|---|---|
| Step 2 | At the Main
                                             			 menu, select Review Old Messages and then select Deleted Messages. |
| Step 3 | Follow the
                                             			 prompts to manage a deleted message after you have listened to it. |

| Note | To adjust the conversation speed or volume, you can only use the
                                       		voice commands not the phone keypad. |
|---|---|

| Option | Description |
|---|---|
| Press key once | Increases the volume |
| Press key again | Decreases the volume |
| Press key again | Returns the volume to normal |

| Option | Description |
|---|---|
| Press decrease key | Slow message playback |
| Press increase key once | Fast message playback |
| Press increase key again | Faster message playback |

| Action | Key(s) |
|---|---|
| Hear new messages | 1 |
| Review saved messages | 3, 1 |
| Review deleted messages (Not available on some systems) | 3, 2 |

| Action | Key(s) |
|---|---|
| Restart message | 1 |
| Play message by number | 1 2 |
| Play previous message | 1 4 |
| Play next message | 6 |
| Save | 2 |
| Delete | 3 |
| Slow playback | 4 |
| Change volume (Not available on some systems) | 5 |
| Fast playback | 6 |
| Rewind message | 7 |
| Pause or resume | 8 |
| Fast-forward | 9 |
| Fast-forward to end | # |
| Restore as saved (Not available on some systems) | #2 |
| Save or restore as new (Not available on some systems) | #6 |
| Play message properties | #9 |
| Skip message, save as is | ## |
| Cancel or back up | * |
| Help | 0 |

| Action | Key(s) |
|---|---|
| Replay message | 1 |
| Play message by number | 1 2 |
| Play previous message | 1 4 |
| Save or restore as saved (Not available on some systems) | 2 |
| Delete | 3 |
| Forward message | 5 |
| Save or Restore as new | 6 |
| Rewind | 7 |
| Play Message Properties | 9 |
| Save as i | # |
| Cancel or back up | * |
| Help | 0 |

| Action | Key(s) |
|---|---|
| Pause or resume | 8 |
| End a recording | # |

| Action | Key(s) |
|---|---|
| Rewind | 4 |
| Save As is | 6 |
| Call the
                                                						sender (Not
                                                						available on some systems) | 9 |
| Play message properties | 7 0 |
| Reply | 7 1 |
| Replay Messages | 7 2 |
| Forward Message | 7 3 |
| Reply to All | 7 4 |
| Delete | 7 6 |
| Save or
                                                						restore as saved (Not
                                                						available on some systems) | 7 7 |
| Save or
                                                						restore as new (Not
                                                						available on some systems) | 7 8 |
| Cancel or back up | * |
| Operator | 0 |

| Action | Key(s) |
|---|---|
| Pause or resume | 8 |
| End a recording | # |