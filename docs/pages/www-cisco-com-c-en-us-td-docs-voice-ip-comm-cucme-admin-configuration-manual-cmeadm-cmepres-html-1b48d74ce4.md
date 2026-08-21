---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmepres-html-1b48d74ce4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmepres.html
retrieved_at: 2026-08-21T07:23:57.252322+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Presence Service

## Chapter: Presence Service

# Presence Service

## Prerequisites for Presence Service

Cisco Unified CME 4.1 or a later version.

## Restrictions for Presence Service

Presence features such as Busy Lamp Field (BLF) notification are
                                    			 supported for SIP trunks only; these features are not supported on H.323
                                    			 trunks.

Presence requires that SIP phones are configured with a directory
                                    			 number (using dn keyword in number command); direct line numbers are
                                    			 not supported.

## Information About Presence Service

### Presence
                           	 Service

A presence service,
                              		as defined in RFC 2778 and RFC 2779, is a system for finding, retrieving, and
                              		distributing presence information from a source, called a presence entity
                              		(presentity), to an interested party called a watcher. When you configure
                              		presence in a Cisco Unified CME system with a SIP WAN connection, a phone user,
                              		or watcher, can monitor the real-time status of another user at a directory
                              		number, the presentity. Presence enables the calling party to know before
                              		dialing whether the called party is available. For example, a directory
                              		application may show that a user is busy, saving the caller the time and
                              		inconvenience of not being able to reach someone.

Presence uses SIP
                              		SUBSCRIBE and NOTIFY methods to allow users and applications to subscribe to
                              		changes in the line status of phones in a Cisco Unified CME system. Phones act
                              		as watchers and a presentity is identified by a directory number on a phone.
                              		Watchers initiate presence requests (SUBSCRIBE messages) to obtain the line
                              		status of a presentity. Cisco Unified CME responds with the presentity’s
                              		status. Each time a status changes for a presentity, all watchers of this
                              		presentity are sent a notification message. SIP phones and trunks use SIP
                              		messages; SCCP phones use presence primitives in SCCP messages.

Presence supports
                              		Busy Lamp Field (BLF) notification features for speed-dial buttons and
                              		directory call lists for missed calls, placed calls, and received calls. SIP
                              		and SCCP phones that support the BLF speed-dial and BLF call-list features can
                              		subscribe to status change notification for internal and external directory
                              		numbers.

Figure 31-1 shows a Cisco Unified CME system supporting BLF notification for internal and
                              		external directory numbers. If the watcher and the presentity are not both
                              		internal to the Cisco Unified CME router, the subscribe message is handled by a
                              		presence proxy server.

The following line
                              		states display through BLF indicators on the phone:

Line is
                                    			 idle—Displays when this line is not being used.

Line is
                                    			 in-use—Displays when the line is in the ringing state and when a user is on the
                                    			 line, whether or not this line can accept a new call.

BLF indicator
                                    			 unknown—Phone is unregistered or this line is not allowed to be watched.

Cisco Unified CME
                              		acts as a presence agent for internal lines (both SIP and SCCP) and as a
                              		presence server for external watchers connected through a SIP trunk, providing
                              		the following functionality:

Processes
                                    			 SUBSCRIBE requests from internal lines to internal lines. Notifies internal
                                    			 subscribers of any status change.

Processes
                                    			 incoming SUBSCRIBE requests from a SIP trunk for internal SCCP and SIP lines.
                                    			 Notifies external subscribers of any status change.

Sends SUBSCRIBE
                                    			 requests to external presentities on behalf of internal lines. Relays status
                                    			 responses to internal lines.

Presence
                              		subscription requests from SIP trunks can be authenticated and authorized.
                              		Local subscription requests cannot be authenticated.

For configuration
                              		information, see How
                                 		  to Configure Presence Service .

### BLF Monitoring of
                           	 Ephone-DNs with DnD, Call Park, Paging, and Conferencing

In versions earlier
                              		than Cisco Unified CME 7.1, BLF monitoring does not provide notification of
                              		status changes when a monitored directory number becomes DND-enabled, and the
                              		Busy Lamp Field (BLF) indicators for directory numbers configured as call-park
                              		slots, paging numbers, or ad hoc or meet-me conference numbers display only the
                              		unknown line-status.

Cisco Unified CME 7.1 and later versions support idle, in-use,
                              		and unknown BLF status indicators for monitored ephone-dns configured as
                              		call-park slots, paging numbers, and ad hoc or meet-me conference numbers. This
                              		allows an administrator (watcher) to monitor a call-park slot to see if calls
                              		are parked and not yet retrieved, which paging number is available for paging,
                              		or which conference number is available for a conference.

An ephone-dn
                              		configured as a park-slot is not registered with any phone. In
                              		Cisco Unified CME 7.1 and later versions, if a monitored park-slot is idle, the
                              		BLF status shows idle on the watcher. If there is a call parked on the
                              		monitored park-slot, the BLF status indicates in-use. If the monitored
                              		park-slot is not enabled for BLF monitoring with the allow watch command, the BLF indicator for unknown status displays on the watcher.

An ephone-dn
                              		configured for paging or conferencing is also not registered with any phone.
                              		The indicators for the idle, in-use, and unknown BLF status are displayed for
                              		the monitored paging number and ad hoc or meet-me conference numbers, as with
                              		the call-park slots.

Cisco Unified CME 7.1 and later versions support the Do Not
                              		Disturb (DnD) BLF status indicator for ephone-dns in the DnD state. When a user
                              		presses the DnD softkey on an SCCP phone, all directory numbers assigned to the
                              		phone become DnD-enabled and a silent-ring is played for all calls to any
                              		directory number on the phone. If a monitored ephone-dn becomes DnD-enabled,
                              		the corresponding BLF speed-dial lamp (if available) on the watcher displays
                              		solid red with the DnD icon for both the idle and in-use BLF status.

The BLF status
                              		notification occurs if the monitored ephone-dn is:

The primary
                                    			 directory number on only one SCCP phone

A directory
                                    			 number that is not shared

A shared
                                    			 directory number and all associated phones are DnD-enabled

No new configuration
                              		is required to support these enhancements. For information on configuring BLF
                              		monitoring of directory numbers, see BLF
                                 		  Monitoring for Speed-Dials and Call Lists .

Table 31-1 compares the different BLF monitoring features that can be configured in
                              		Cisco Unified CME.

Monitor Mode
                                          				  (Button “m”)

Watch Mode
                                          				  (Button “w”)

BLF
                                          				  Monitoring

Basic Operation

SCCP phones
                                          				  only.

Watches a
                                          				  single ephone-dn instance.

If there are
                                          				  multiple ephone-dns with the same extension (such as in an overlay), this mode
                                          				  watches only a single ephone-dn (specified with the button command using m keyword).

Does not
                                          				  indicate DND state of the phone.

SCCP phones
                                          				  only.

Watches all
                                          				  activity on the phone for which the designated ephone-dn is the primary
                                          				  extension.

(The
                                          				  ephone-dn is “primary” for a phone if the extension appears on button 1 or on
                                          				  the button indicated by the auto-line command.)

Ephone-dn
                                          				  can be shared but cannot be the primary extension on any other phone.

Indicates
                                          				  DND state of the phone.

SCCP and SIP
                                          				  phones.

Watches all
                                          				  ephone-dn instances with the same (primary) extension number. The BLF lamp is
                                          				  on if any instance of the monitored extension is in use.

Indicates
                                          				  DND state of the phone.

BLF monitoring is supported only if the presence entity (presentity) is an SCCP phone. If you enable DND on a SIP phone, LED
                                                      doesn’t glow. Hence, the phone user or administrator (watcher) isn’t notified.

Can not
                                          				  distinguish which phone is using the ephone-dn if the DN is shared across
                                          				  multiple phones.

Designed for
                                          				  cases where ephone-dns are shared across multiple phones.

Each phone
                                          				  must have a unique primary ephone-dn.

Used to
                                          				  indicate that a specific phone is in use as opposed (button m) to indicating
                                          				  that a specific ephone-dn is in use.

Cannot
                                          				  distinguish which phone is using the ephone-dn, if the DN is shared across
                                          				  multiple phones.

Local vs. Remote

Monitors
                                          				  only DNs on the local Cisco Unified CME system.

Can only
                                          				  monitor DNs that are on the local Cisco Unified CME system

Can monitor
                                          				  extension numbers on a remote Cisco Unified CME using SIP Subscribe and Notify.
                                          				  Cannot monitor local and remote at the same time.

### Device-Based BLF
                           	 Monitoring

Device-based BLF
                              		monitoring provides a phone user or administrator (watcher) information about
                              		the status of a monitored phone (presentity). Cisco Unified CME 4.1 and later
                              		versions support BLF monitoring of directory numbers associated with speed-dial
                              		buttons, call logs, and directory listings. Cisco Unified CME 7.1 and later
                              		versions support device-based BLF monitoring, allowing a watcher to monitor the
                              		status of a phone, not only a line on the phone.

To identify the
                              		phone being monitored for BLF status, Cisco Unified CME selects the phone with
                              		the monitored directory number assigned to the first button, or the directory
                              		number whose button is selected by the auto-line command (SCCP only). If more than one phone uses the same number as its primary
                              		directory number, the phone with the lowest phone tag is monitored for BLF
                              		status.

For Extension
                              		Mobility phones, the first number configured in the user profile indicates the
                              		primary directory number of the Extension Mobility phone. If the Extension
                              		Mobility phone is being monitored, the BLF status of the corresponding phone is
                              		sent to the watcher when an extension-mobility user logs in or out, is idle, or
                              		busy.

If a shared
                              		directory number is busy on a monitored SCCP phone, and the monitored device is
                              		on-hook, the monitored phone is considered idle.

When a monitored
                              		phone receives a page, if the paging directory number is also monitored, the
                              		BLF status of the paging directory number shows busy on the watcher.

If device-based
                              		monitoring is enabled on a directory number configured as a call-park slot, and
                              		there is a call parked on this park-slot, the device-based BLF status indicates
                              		busy.

All directory
                              		numbers associated with a phone are in the DnD state when the DnD softkey is
                              		pressed. If a monitored phone becomes DnD-enabled, watchers are notified of the
                              		DnD status change.

For configuration
                              		information, see BLF
                                 		  Monitoring for Speed-Dials and Call Lists or SIP:
                                 		  Enabling BLF Monitoring for Speed-Dials and Call Lists .

### Phone User
                           	 Interface for BLF-Speed-Dial

Cisco Unified CME  8.5 and later versions allows the extension mobility (EM) users to configure dn-based Busy Lamp Field (BLF)-speed-dial
                              settings directly on the phone through the services feature button. BLF-speed-dial settings are added or modified (changed
                              or deleted) on the phone using a menu available with the Services button. Any changes to the BLF-speed-dial settings made
                              through the phone user interface are applied to the user's profile in extension mobility. You can configure the BLF-speed-dial
                              menu for SCCP phones using the blf-speed-dial command in ephone or ephone-template mode. For more information, see Enabling BLF-Speed-Dial Menu .

For information on how phone users configure BLF-speed-dial using the phone user-interface, see the Cisco Unified IP Phone documentation for Cisco Unified CME .

For phones that do not have EM feature, the BLF-speed-dial service is available in service url page. You can disable the BLF-speed-
                              dial feature using the no phone-ui blf-speed-dial command on phones that do not have Extension Mobility.

## Configure Presence Service

### Enable Presence
                           	 for Internal Lines

Perform the
                                 		  following steps to enable the router to accept incoming presence requests from
                                 		  internal watchers and SIP trunks.

The command presence call-list is an optional configuration, and it is not required to enable Presence on Unified CME. To enable a phone to monitor the
                                             line status of directory numbers or call list, such as a missed calls, placed calls, or received calls list, you can configure presence call-list .

Restriction

A presentity can be identified by a directory number only.

BLF monitoring indicates the line status only.

Instant Messaging is not supported.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- presence enable

- exit

- presence

- max-subscription number

- presence call-list

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP
                                             				user-agent configuration mode to configure the user agent.

Step 4

presence enable

#### Example:

```
Router(config-sip-ua)# presence enable
```

Allows the
                                             				router to accept incoming presence requests.

Step 5

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP
                                             				user-agent configuration mode.

Step 6

presence

#### Example:

```
Router(config)# presence
```

Enables
                                             				presence service and enters presence configuration mode.

Step 7

max-subscription number

#### Example:

```
Router(config-presence)# max-subscription 128
```

(Optional) Sets the maximum number of concurrent watch sessions that are allowed.

number —Maximum watch sessions. Range: 100 to the maximum number of directory numbers supported on the router platform. Type ? to display range. Default: 100.

Step 8

presence call-list

#### Example:

```
Router(config-presence)# presence call-list
```

(Optional) Globally enables BLF monitoring for directory numbers in call lists and directories on all locally registered phones.

Only directory numbers that you enable for watching with the allow watch command display BLF status indicators.

This
                                                   					 command enables the BLF call-list feature globally. To enable the feature for a
                                                   					 specific phone, see BLF
                                                      						Monitoring for Speed-Dials and Call Lists .

Step 9

end

#### Example:

```
Router(config-presence)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable a Directory Number to be Watched

To enable a line associated with a directory number to be monitored by
                                 		  a phone registered to a Cisco Unified CME router, perform the following steps.
                                 		  The line is enabled as a presentity and phones can subscribe to its line status
                                 		  through the BLF call-list and BLF speed-dial features. There is no restriction
                                 		  on the type of phone that can have its lines monitored; any line on any IP
                                 		  phone or on an analog phone on supported voice gateways can be a presentity.

Restriction

A presentity is identified by a directory number only.

BLF monitoring indicates the line status only.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ] or voice register dn dn-tag

- number number

- allow watch

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

ephone-dn dn-tag [ dual-line ] or voice register dn dn-tag

#### Example:

```
Router(config)# ephone-dn 1
```

```
Router(config)# voice register dn 1
```

Enters the configuration mode to define a directory number for an
                                             				IP phone, intercom line, voice port, or a message-waiting indicator (MWI).

dn-tag —identifies a particular
                                                   					 directory number during configuration tasks. Range is 1 to the maximum number
                                                   					 of directory numbers allowed on the router platform, or the maximum defined by
                                                   					 the max-dn command. Type ? to display range.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 3001
```

```
Router(config-register-dn)# number 3001
```

Associates a phone number with a directory number to be assigned
                                             				to an IP phone in Cisco Unified CME.

number —String of up to 16 characters
                                                   					 that represents an E.164 telephone number.

Step 5

allow watch

#### Example:

```
Router(config-ephone-dn)# allow watch
```

```
Router(config-register-dn)# allow watch
```

Allows the phone line associated with this directory number to be
                                             				monitored by a watcher in a presence service.

This command can also be configured in ephone-dn template
                                                   					 configuration mode and applied to one or more phones. The ephone-dn
                                                   					 configuration has priority over the ephone-dn template configuration.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

```
Router(config-register-dn)# end
```

Exits to privileged EXEC mode.

### Enable BLF Monitor
                           	 for Speed-Dials and Call Lists Using SCCP Phones

A watcher can
                                 		  monitor the status of lines associated with internal and external directory
                                 		  numbers (presentities) through the BLF speed-dial and BLF call-list presence
                                 		  features. To enable the BLF notification features on an IP phone using SCCP,
                                 		  perform the following steps.

Restriction

Device-based
                                                   				  BLF monitoring for call lists is not supported.

Device-based
                                                   				  BLF-speed-dial monitoring is not supported for a remote watcher or presentity.

BLF Call-List

Not supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, 7931, 7940, 7960, or 7985, Cisco Unified IP Phone Expansion
                                                   Modules, or Cisco Unified IP Conference Stations.

BLF Speed-Dial

Not supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, or 7985, or Cisco Unified IP Conference Stations.

Cisco Unified IP Phone 7931

BLF status is displayed through monitor lamp only; BLF status icons are not displayed.

#### Before you begin

Presence must
                                       				be enabled on the Cisco Unified CME router. See Enabling
                                          				  Presence for Internal Lines .

A directory
                                       				number must be enabled as a presentity with the allow watch command to provide BLF status notification. See Enabling
                                          				  a Directory Number to be Watched .

Device-based
                                       				monitoring requires Cisco Unified CME 7.1 or a later version. All directory
                                       				numbers associated with the monitored phone must be configured with the allow watch command. Otherwise, if any of the directory numbers
                                       				is missing this configuration, an incorrect status could be reported to the
                                       				watcher.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- button button-number { separator } dn-tag [ , dn-tag ... ] [ button-number { x } overlay-button-number ] [ button-number ... ]

- blf-speed-dial tag
                                       				  number label string [ device ]

- presence
                                       				  call-list

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode to set phone-specific parameters for a SIP phone.

phone-tag —Unique sequence number of the phone to
                                                   					 be configured. Range is version and platform-dependent; type ? to display
                                                   					 range. You can modify the upper limit for this argument with the max-ephones command.

Step 4

button button-number { separator } dn-tag [ , dn-tag ... ] [ button-number { x } overlay-button-number ] [ button-number ... ]

#### Example:

```
Router(config-ephone)# button 1:10 2:11 3b12 4o13,14,15
```

Associates a
                                             				button number and line characteristics with a directory number on the phone.

button-number —Number of a line button on an IP
                                                   					 phone.

separator —Single character that denotes the type
                                                   					 of characteristics to be associated with the button.

dn-tag —Unique sequence number of the ephone-dn
                                                   					 that you want to appear on this button. For overlay lines (separator is o or c ), this
                                                   					 argument can contain up to 25 ephone-dn tags, separated by commas.

x —Separator
                                                   					 that creates an overlay rollover button.

overlay-button-number— Number of the overlay button
                                                   					 that should overflow to this button.

Step 5

blf-speed-dial tag
                                                				  number label string [ device ]

#### Example:

```
Router(config-ephone)# blf-speed-dial 3 3001 label sales device
```

Enables BLF
                                             				monitoring of a directory number associated with a speed-dial number on the
                                             				phone.

tag —Number
                                                   					 that identifies the speed-dial index. Range: 1 to 33.

number —Telephone number to speed dial.

string —Alphanumeric label that identifies the
                                                   					 speed-dial button. String can contain a maximum of 30 characters.

device —(Optional) Enables phone-based monitoring.
                                                   					 This keyword is supported in Cisco Unified CME 7.1 and later versions.

Step 6

presence
                                                				  call-list

#### Example:

```
Router(config-ephone)# presence call-list
```

Enables BLF
                                             				monitoring of directory numbers that appear in call lists and directories on
                                             				this phone.

For a
                                                   					 directory number to be monitored, it must have the allow watch command enabled.

To
                                                   					 enable BLF monitoring for call lists on all phones in this Cisco Unified CME
                                                   					 system, use this command in presence mode. See Enable Presence for Internal Lines .

Step 7

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows that the directory numbers for extensions 2001 and 2003 are
                                 		  allowed to be watched and the BLF status of these numbers display on phone 1.

```
ephone-dn  201
number 2001
allow watch
!
!
ephone-dn  203
number 2003
allow watch
!
!
ephone  1
mac-address 0012.7F54.EDC6
blf-speed-dial 2 201 label "sales" device
blf-speed-dial 3 203 label "service" device
button  1:100 2:101 3b102
```

#### What to do next

If you are done
                                 		  modifying parameters for SCCP phones in Cisco Unified CME, generate a new
                                 		  configuration profile by using the create
                                       				cnf-files command and then restart the phones with the restart command. See SCCP:
                                    			 Generating Configuration Files for SCCP Phones and SCCP:
                                    			 Using the restart Command .

### Enable BLF
                           	 Monitoring for Speed-Dials and Call Lists on SIP Phones

A watcher can
                                 		  monitor the status of lines associated with internal and external directory
                                 		  numbers (presentities) through the BLF speed-dial and BLF call-list presence
                                 		  features. To enable the BLF notification features on a SIP phone, perform the
                                 		  following steps.

Restriction

Device-based
                                                   				  BLF-speed-dial monitoring is not supported for a remote watcher or presentity.

TCP based,
                                                   				  device-based BLF-speed-dial monitoring is not supported on Unified CME.

BLF Call-List

Not
                                                   				  supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, 7931, 7940, 7960,
                                                   				  or 7985, Cisco Unified IP Phone Expansion Modules, or Cisco Unified IP
                                                   				  Conference Stations.

BLF Speed-Dial

Not
                                                   				  supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, or 7985, or
                                                   				  Cisco Unified IP Conference Stations.

#### Before you begin

Presence must
                                       				be enabled on the Cisco Unified CME router. See Enabling
                                          				  Presence for Internal Lines .

A directory
                                       				number must be enabled as a presentity with the allow watch command to provide BLF status notification. See Enabling
                                          				  a Directory Number to be Watched .

SIP phones
                                       				must be configured with a directory number under voice register pool
                                       				configuration mode (use dn keyword in number command); direct line numbers are not supported.

Device-based
                                       				monitoring requires Cisco Unified CME 7.1 or a later version. All directory
                                       				numbers associated with the monitored phone must be configured with the allow watch command. Otherwise, if any of the directory numbers is missing this
                                       				configuration, an incorrect status could be reported to the watcher.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- number tag dn dn-tag

- blf-speed-dial tag number label string [ device ]

- presence
                                       				  call-list

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

pool-tag —Unique sequence number of the SIP phone
                                                   					 to be configured. Range is version and platform-dependent; type ? to display
                                                   					 range. You can modify the upper limit for this argument with the max-pool command.

Step 4

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 2
```

Assigns a
                                             				directory number to the SIP phone.

tag—identifier when there are multiple number commands. Range: 1 to 10.

dn-tag —Directory number tag that was defined using
                                                   					 the voice register
                                                         						  dn command.

Step 5

blf-speed-dial tag number label string [ device ]

#### Example:

```
Router(config-register-pool)# blf-speed-dial 3 3001 label sales device
```

Enables BLF
                                             				monitoring of a directory number associated with a speed-dial number on the
                                             				phone.

tag —Number
                                                   					 that identifies the speed-dial index. Range: 1 to 7.

number —Telephone number to speed dial.

string —Alphanumeric label that identifies the
                                                   					 speed-dial button. The string can contain a maximum of 30 characters.

device —(Optional) Enables phone-based monitoring.
                                                   					 This keyword is supported in Cisco Unified CME 7.1 and later versions.

Step 6

presence
                                                				  call-list

#### Example:

```
Router(config-register-pool)# presence call-list
```

Enables BLF
                                             				monitoring of directory numbers that appear in call lists and directories on
                                             				this phone.

For a
                                                   					 directory number to be monitored, it must have the allow watch command enabled.

To
                                                   					 enable BLF monitoring for call lists on all phones in this Cisco Unified CME
                                                   					 system, use this command in presence mode. See Enabling
                                                      						Presence for Internal Lines .

Step 7

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for SIP phones in Cisco Unified CME, generate a new
                                 		  configuration profile by using the create
                                       				profile command and then restart the phones with the restart command. See SIP:
                                    			 Generating Configuration Profiles for SIP Phones and SIP:
                                    			 Using the restart Command .

### Enable
                           	 BLF-Speed-Dial Menu

Restriction

EM user
                                                   				  cannot modify the logout profile from phone user interface (UI).

Extension
                                                   				  Mobility (EM) users must log into EM profile to update BLF-speed-dial number.

#### Before you begin

Cisco Unified
                                       				CME 8.5 or later versions.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- blf-speed-dial [ index index
                                       				  number ]
                                       				  [ phone-number number ] [ label label
                                       				  text ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone
                                             				configuration mode.

phone-tag—Unique number of the phone for which you want to
                                                   					 configure BLF-speed-dial numbers.

Step 4

blf-speed-dial [ index index
                                                				  number ]
                                                				  [ phone-number number ] [ label label
                                                				  text ]

#### Example:

```
Router(config-ephone)#blf-speed-dial 1 2001 label "customer support"
```

Creates an
                                             				entry for a BLF-speed-dial number on this phone.

BLF-speed-dial index—Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 75.

phone
                                                   					 number—Telephone number or extension to be dialed.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Presence
                           	 to Watch External Lines

To enable internal
                                 		  watchers to monitor external directory numbers on a remote Cisco Unified CME
                                 		  router, perform the following steps.

#### Before you begin

Presence service
                                 		  must be enabled for internal lines. See Enabling
                                    			 Presence for Internal Lines .

### SUMMARY STEPS

- enable

- configure terminal

- presence

- server ip-address

- allow subscribe

- watcher all

- sccp blf-speed-dial retry-interval seconds limit number

- exit

- voice register global

- authenticate presence

- authenticate credential tag
                                       				  location

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

presence

#### Example:

```
Router(config)# presence
```

Enables
                                             				presence service and enters presence configuration mode.

Step 4

server ip-address

#### Example:

```
Router(config-presence)# server 10.10.10.1
```

Specifies the
                                             				IP address of a presence server for sending presence requests from internal
                                             				watchers to external presentities.

Step 5

allow subscribe

#### Example:

```
Router(config-presence)# allow subscribe
```

Allows
                                             				internal watchers to monitor external directory numbers.

Step 6

watcher all

#### Example:

```
Router(config-presence)# watcher all
```

Allows
                                             				external watchers to monitor internal directory numbers.

Step 7

sccp blf-speed-dial retry-interval seconds limit number

#### Example:

```
Router(config-presence)# sccp blf-speed-dial retry-interval 90 limit number 15
```

(Optional)
                                             				Sets the retry timeout for BLF monitoring of speed-dial numbers on phones
                                             				running SCCP.

seconds —Retry timeout in seconds. Range: 60 to
                                                   					 3600. Default: 60.

number —Maximum number of retries.
                                                   					 Range: 10 to 100. Default: 10.

Step 8

exit

#### Example:

```
Router(config-presence)# exit
```

Exits presence
                                             				configuration mode.

Step 9

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment.

Step 10

authenticate presence

#### Example:

```
Router(config-register-global)# authenticate presence
```

(Optional)
                                             				Enables authentication of incoming presence requests from a remote presence
                                             				server.

Step 11

authenticate credential tag
                                                				  location

#### Example:

```
Router(config-register-global)# authenticate credential 1 flash:cred1.csv
```

(Optional)
                                             				Specifies the credential file to use for authenticating presence subscription
                                             				requests.

tag —Number
                                                   					 that identifies the credential file to use for presence authentication. Range:
                                                   					 1 to 5.

location —Name and location of the credential file
                                                   					 in URL format. Valid storage locations are TFTP, HTTP, and flash memory.

Step 12

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Verify Presence
                           	 Configuration

Step 1

show running-config

Use this
                                             				command to verify your configuration.

```
Router# show running-config !
voice register global
 mode cme
 source-address 10.1.1.2 port 5060
 load 7971 SIP70.8-0-1-11S
 load 7970 SIP70.8-0-1-11S
 load 7961GE SIP41.8-0-1-0DEV
 load 7961 SIP41.8-0-1-0DEV
 authenticate presence
 authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
 create profile sync 0004550081249644
.
.
.
presence
 server 10.1.1.4
 sccp blf-speed-dial retry-interval 70 limit 20
 presence call-list
 max-subscription 128
 watcher all
 allow subscribe
!
sip-ua
 presence enable
```

Step 2

show presence global

Use this
                                             				command to display presence configuration settings.

```
Router# show presence global Presence Global Configuration Information:
=============================================
Presence feature enable            : TRUE
Presence allow external watchers   : FALSE
Presence max subscription allowed  : 100
Presence number of subscriptions   : 0
Presence allow external subscribe  : FALSE
Presence call list enable          : TRUE
Presence server IP address         : 0.0.0.0
Presence sccp blfsd retry interval : 60
Presence sccp blfsd retry limit    : 10
Presence router mode               : CME mode
```

Step 3

show presence subscription [ details | presentity telephone-number | subid subscription-id summary ]

Use this
                                             				command to display information about active presence subscriptions.

```
Router# show presence subscription summary Presence Active Subscription Records Summary: 15 subscription
Watcher                  Presentity               SubID Expires SibID  Status
======================== ======================== ====== ======= ====== ======
6002@10.4.171.60         6005@10.4.171.34         1 3600    0      idle
6005@10.4.171.81         6002@10.4.171.34         6 3600    0      idle
6005@10.4.171.81         6003@10.4.171.34         8 3600    0      idle
6005@10.4.171.81         6002@10.4.171.34         9 3600    0      idle
6005@10.4.171.81         6003@10.4.171.34         10 3600    0      idle
6005@10.4.171.81         6001@10.4.171.34         12 3600    0      idle
6001@10.4.171.61         6003@10.4.171.34         15 3600    0      idle
6001@10.4.171.61         6002@10.4.171.34         17 3600    0      idle
6003@10.4.171.59         6003@10.4.171.34         19 3600    0      idle
6003@10.4.171.59         6002@10.4.171.34         21 3600    0      idle
6003@10.4.171.59         5001@10.4.171.34         23 3600    24     idle
6002@10.4.171.60         6003@10.4.171.34         121 3600    0      idle 
6002@10.4.171.60         5002@10.4.171.34         128 3600    129    idle
6005@10.4.171.81         1001@10.4.171.34         130 3600    131    busy
6005@10.4.171.81         7005@10.4.171.34         132 3600    133    idle
```

### Troubleshooting
                           	 Presence Service

You can use the
                              		following commands to troubleshoot presence service:

debug presence { all | asnl | errors | event | info | timer | trace | xml }

debug ephone blf [ mac-address mac-address ]

## Configuration Examples for Presence Service

### Example for Configuring Presence in Cisco Unified CME

```
Router# show running-config Building configuration...
		 
		Current configuration : 5465 bytes
		!
		version 12.4
		service timestamps debug datetime msec
		service timestamps log datetime msec
		no service password-encryption
		!
		hostname CME-3825
		!
		boot-start-marker
		boot-end-marker
		!
		logging buffered 2000000 debugging
		enable password lab
		!
		no aaa new-model
		!
		resource policy
		!
		no network-clock-participate slot 1 
		no network-clock-participate slot 2 
		ip cef
		!
		!
		no ip domain lookup
		!
		voice-card 1
		no dspfarm
		!
		voice-card 2
		no dspfarm
		!
		!
		voice service voip 
		allow-connections sip to sip
		h323
		sip
		registrar server expires max 240 min 60
		!
		voice register global
		mode cme
		source-address 11.1.1.2 port 5060
		load 7971 SIP70.8-0-1-11S
		load 7970 SIP70.8-0-1-11S
		load 7961GE SIP41.8-0-1-0DEV
		load 7961 SIP41.8-0-1-0DEV
		authenticate presence
		authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
		create profile sync 0004550081249644
		!
		voice register dn  1
		number 2101
		allow watch
		!
		voice register dn  2
		number 2102
		allow watch
		!
		voice register pool  1
		id mac 0015.6247.EF90
		type 7971
		number 1 dn 1
		blf-speed-dial 1 1001 label "1001"
		!
		voice register pool  2
		id mac 0012.0007.8D82
		type 7912
		number 1 dn 2
		!
		interface GigabitEthernet0/0
		description $ETH-LAN$$ETH-SW-LAUNCH$$INTF-INFO-GE 0/0$
		ip address 11.1.1.2 255.255.255.0
		duplex full
		speed 100
		media-type rj45
		no negotiation auto
		!
		interface GigabitEthernet0/1
		no ip address
		shutdown
		duplex auto
		speed auto
		media-type rj45
		negotiation auto
		!
		ip route 0.0.0.0 0.0.0.0 11.1.1.1
		!
		ip http server
		!
		!
		!
		tftp-server flash:Jar41sccp.8-0-0-103dev.sbn
		tftp-server flash:cvm41sccp.8-0-0-102dev.sbn
		tftp-server flash:SCCP41.8-0-1-0DEV.loads
		tftp-server flash:P00303010102.bin
		tftp-server flash:P00308000100.bin
		tftp-server flash:P00308000100.loads
		tftp-server flash:P00308000100.sb2
		tftp-server flash:P00308000100.sbn
		tftp-server flash:SIP41.8-0-1-0DEV.loads
		tftp-server flash:apps41.1-1-0-82dev.sbn
		tftp-server flash:cnu41.3-0-1-82dev.sbn
		tftp-server flash:cvm41sip.8-0-0-103dev.sbn
		tftp-server flash:dsp41.1-1-0-82dev.sbn
		tftp-server flash:jar41sip.8-0-0-103dev.sbn
		tftp-server flash:P003-08-1-00.bin
		tftp-server flash:P003-08-1-00.sbn
		tftp-server flash:P0S3-08-1-00.loads
		tftp-server flash:P0S3-08-1-00.sb2
		tftp-server flash:CP7912080000SIP060111A.sbin
		tftp-server flash:CP7912080001SCCP051117A.sbin
		tftp-server flash:SCCP70.8-0-1-11S.loads
		tftp-server flash:cvm70sccp.8-0-1-13.sbn
		tftp-server flash:jar70sccp.8-0-1-13.sbn
		tftp-server flash:SIP70.8-0-1-11S.loads
		tftp-server flash:apps70.1-1-1-11.sbn
		tftp-server flash:cnu70.3-1-1-11.sbn
		tftp-server flash:cvm70sip.8-0-1-13.sbn
		tftp-server flash:dsp70.1-1-1-11.sbn
		tftp-server flash:jar70sip.8-0-1-13.sbn
		!
		control-plane
		!
		dial-peer voice 2001 voip
		preference 2
		destination-pattern 1...
		session protocol sipv2
		session target ipv4:11.1.1.4
		dtmf-relay sip-notify
		!
		presence
		server 11.1.1.4
		sccp blf-speed-dial retry-interval 70 limit 20
		presence call-list
		max-subscription 128
		watcher all
		allow subscribe
		!
		sip-ua 
		authentication username jack password 021201481F
		presence enable
		!
		!
		telephony-service
		load 7960-7940 P00308000100
		load 7941GE SCCP41.8-0-1-0DEV
		load 7941 SCCP41.8-0-1-0DEV
		load 7961GE SCCP41.8-0-1-0DEV
		load 7961 SCCP41.8-0-1-0DEV
		load 7971 SCCP70.8-0-1-11S
		load 7970 SCCP70.8-0-1-11S
		load 7912 CP7912080000SIP060111A.sbin
		max-ephones 100
		max-dn 300
		ip source-address 11.1.1.2 port 2000
		url directories http://11.1.1.2/localdirectory
		max-conferences 6 gain -6
		call-forward pattern .T
		transfer-system full-consult
		transfer-pattern .T
		create cnf-files version-stamp Jan 01 2002 00:00:00
		!
		!
		ephone-dn  1  dual-line
		number 2001
		allow watch
		!
		!
		ephone-dn  2  dual-line
		number 2009
		allow watch
		application default
		!
		!
		ephone-dn  3
		number 2005
		allow watch
		!
		!
		ephone-dn  4  dual-line
		number 2002
		!
		!
		ephone  1
		mac-address 0012.7F57.62A5
		fastdial 1 1002
		blf-speed-dial 1 2101 label "2101"
		blf-speed-dial 2 1003 label "1003"
		blf-speed-dial 3 2002 label "2002"
		type 7960
		button  1:1 2:2
		!
		!
		!
		ephone  3
		mac-address 0015.6247.EF91
		blf-speed-dial 2 1003 label "1003"
		type 7971
		button  1:3 2:4
		!
		!
		!
		line con 0
		exec-timeout 0 0
		password lab
		stopbits 1
		line aux 0
		stopbits 1
		line vty 0 4
		password lab
		login    
		!
		scheduler allocate 20000 1000
		!
		end
```

## Feature
                        	 Information for Presence Service

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature Name

Cisco Unified CME Version

Modification

Phone User
                                       				  Interface for BLF-Speed-Dial

8.5

Added
                                       				  support for BLF Speed Dial through Phone User Interface.

BLF
                                       				  Monitoring

7.1

Added
                                             						support for device-based BLF monitoring.

Added
                                             						support for BLF Monitoring of ephone-DNs with DnD, Call Park, Paging, and
                                             						Conferencing

Presence
                                       				  Service

4.1

Presence
                                       				  with BLF was introduced.

| Monitor Mode
                                          				  (Button “m”) | Watch Mode
                                          				  (Button “w”) | BLF
                                          				  Monitoring |
|---|---|---|
| Basic Operation |
| SCCP phones
                                          				  only. Watches a
                                          				  single ephone-dn instance. If there are
                                          				  multiple ephone-dns with the same extension (such as in an overlay), this mode
                                          				  watches only a single ephone-dn (specified with the button command using m keyword). Does not
                                          				  indicate DND state of the phone. | SCCP phones
                                          				  only. Watches all
                                          				  activity on the phone for which the designated ephone-dn is the primary
                                          				  extension. (The
                                          				  ephone-dn is “primary” for a phone if the extension appears on button 1 or on
                                          				  the button indicated by the auto-line command.) Ephone-dn
                                          				  can be shared but cannot be the primary extension on any other phone. Indicates
                                          				  DND state of the phone. | SCCP and SIP
                                          				  phones. Watches all
                                          				  ephone-dn instances with the same (primary) extension number. The BLF lamp is
                                          				  on if any instance of the monitored extension is in use. Indicates
                                          				  DND state of the phone. Note BLF monitoring is supported only if the presence entity (presentity) is an SCCP phone. If you enable DND on a SIP phone, LED
                                                      doesn’t glow. Hence, the phone user or administrator (watcher) isn’t notified. | Note | BLF monitoring is supported only if the presence entity (presentity) is an SCCP phone. If you enable DND on a SIP phone, LED
                                                      doesn’t glow. Hence, the phone user or administrator (watcher) isn’t notified. |
| Note | BLF monitoring is supported only if the presence entity (presentity) is an SCCP phone. If you enable DND on a SIP phone, LED
                                                      doesn’t glow. Hence, the phone user or administrator (watcher) isn’t notified. |
| Shared Lines |
| Can not
                                          				  distinguish which phone is using the ephone-dn if the DN is shared across
                                          				  multiple phones. | Designed for
                                          				  cases where ephone-dns are shared across multiple phones. Each phone
                                          				  must have a unique primary ephone-dn. Used to
                                          				  indicate that a specific phone is in use as opposed (button m) to indicating
                                          				  that a specific ephone-dn is in use. | Cannot
                                          				  distinguish which phone is using the ephone-dn, if the DN is shared across
                                          				  multiple phones. |
| Local vs. Remote |
| Monitors
                                          				  only DNs on the local Cisco Unified CME system. | Can only
                                          				  monitor DNs that are on the local Cisco Unified CME system | Can monitor
                                          				  extension numbers on a remote Cisco Unified CME using SIP Subscribe and Notify.
                                          				  Cannot monitor local and remote at the same time. |

| Note | BLF monitoring is supported only if the presence entity (presentity) is an SCCP phone. If you enable DND on a SIP phone, LED
                                                      doesn’t glow. Hence, the phone user or administrator (watcher) isn’t notified. |
|---|---|

| Note | The command presence call-list is an optional configuration, and it is not required to enable Presence on Unified CME. To enable a phone to monitor the
                                             line status of directory numbers or call list, such as a missed calls, placed calls, or received calls list, you can configure presence call-list . |
|---|---|

| Restriction | A presentity can be identified by a directory number only. BLF monitoring indicates the line status only. Instant Messaging is not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters SIP
                                             				user-agent configuration mode to configure the user agent. |
| Step 4 | presence enable Example: Router(config-sip-ua)# presence enable | Allows the
                                             				router to accept incoming presence requests. |
| Step 5 | exit Example: Router(config-sip-ua)# exit | Exits SIP
                                             				user-agent configuration mode. |
| Step 6 | presence Example: Router(config)# presence | Enables
                                             				presence service and enters presence configuration mode. |
| Step 7 | max-subscription number Example: Router(config-presence)# max-subscription 128 | (Optional) Sets the maximum number of concurrent watch sessions that are allowed. number —Maximum watch sessions. Range: 100 to the maximum number of directory numbers supported on the router platform. Type ? to display range. Default: 100. |
| Step 8 | presence call-list Example: Router(config-presence)# presence call-list | (Optional) Globally enables BLF monitoring for directory numbers in call lists and directories on all locally registered phones. Only directory numbers that you enable for watching with the allow watch command display BLF status indicators. This
                                                   					 command enables the BLF call-list feature globally. To enable the feature for a
                                                   					 specific phone, see BLF
                                                      						Monitoring for Speed-Dials and Call Lists . |
| Step 9 | end Example: Router(config-presence)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | A presentity is identified by a directory number only. BLF monitoring indicates the line status only. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] or voice register dn dn-tag Example: Router(config)# ephone-dn 1 or Router(config)# voice register dn 1 | Enters the configuration mode to define a directory number for an
                                             				IP phone, intercom line, voice port, or a message-waiting indicator (MWI). dn-tag —identifies a particular
                                                   					 directory number during configuration tasks. Range is 1 to the maximum number
                                                   					 of directory numbers allowed on the router platform, or the maximum defined by
                                                   					 the max-dn command. Type ? to display range. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 3001 or Router(config-register-dn)# number 3001 | Associates a phone number with a directory number to be assigned
                                             				to an IP phone in Cisco Unified CME. number —String of up to 16 characters
                                                   					 that represents an E.164 telephone number. |
| Step 5 | allow watch Example: Router(config-ephone-dn)# allow watch or Router(config-register-dn)# allow watch | Allows the phone line associated with this directory number to be
                                             				monitored by a watcher in a presence service. This command can also be configured in ephone-dn template
                                                   					 configuration mode and applied to one or more phones. The ephone-dn
                                                   					 configuration has priority over the ephone-dn template configuration. |
| Step 6 | end Example: Router(config-ephone-dn)# end or Router(config-register-dn)# end | Exits to privileged EXEC mode. |

| Restriction | Device-based
                                                   				  BLF monitoring for call lists is not supported. Device-based
                                                   				  BLF-speed-dial monitoring is not supported for a remote watcher or presentity. BLF Call-List Not supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, 7931, 7940, 7960, or 7985, Cisco Unified IP Phone Expansion
                                                   Modules, or Cisco Unified IP Conference Stations. BLF Speed-Dial Not supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, or 7985, or Cisco Unified IP Conference Stations. Cisco Unified IP Phone 7931 BLF status is displayed through monitor lamp only; BLF status icons are not displayed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode to set phone-specific parameters for a SIP phone. phone-tag —Unique sequence number of the phone to
                                                   					 be configured. Range is version and platform-dependent; type ? to display
                                                   					 range. You can modify the upper limit for this argument with the max-ephones command. |
| Step 4 | button button-number { separator } dn-tag [ , dn-tag ... ] [ button-number { x } overlay-button-number ] [ button-number ... ] Example: Router(config-ephone)# button 1:10 2:11 3b12 4o13,14,15 | Associates a
                                             				button number and line characteristics with a directory number on the phone. button-number —Number of a line button on an IP
                                                   					 phone. separator —Single character that denotes the type
                                                   					 of characteristics to be associated with the button. dn-tag —Unique sequence number of the ephone-dn
                                                   					 that you want to appear on this button. For overlay lines (separator is o or c ), this
                                                   					 argument can contain up to 25 ephone-dn tags, separated by commas. x —Separator
                                                   					 that creates an overlay rollover button. overlay-button-number— Number of the overlay button
                                                   					 that should overflow to this button. |
| Step 5 | blf-speed-dial tag
                                                				  number label string [ device ] Example: Router(config-ephone)# blf-speed-dial 3 3001 label sales device | Enables BLF
                                             				monitoring of a directory number associated with a speed-dial number on the
                                             				phone. tag —Number
                                                   					 that identifies the speed-dial index. Range: 1 to 33. number —Telephone number to speed dial. string —Alphanumeric label that identifies the
                                                   					 speed-dial button. String can contain a maximum of 30 characters. device —(Optional) Enables phone-based monitoring.
                                                   					 This keyword is supported in Cisco Unified CME 7.1 and later versions. |
| Step 6 | presence
                                                				  call-list Example: Router(config-ephone)# presence call-list | Enables BLF
                                             				monitoring of directory numbers that appear in call lists and directories on
                                             				this phone. For a
                                                   					 directory number to be monitored, it must have the allow watch command enabled. To
                                                   					 enable BLF monitoring for call lists on all phones in this Cisco Unified CME
                                                   					 system, use this command in presence mode. See Enable Presence for Internal Lines . |
| Step 7 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Device-based
                                                   				  BLF-speed-dial monitoring is not supported for a remote watcher or presentity. TCP based,
                                                   				  device-based BLF-speed-dial monitoring is not supported on Unified CME. BLF Call-List Not
                                                   				  supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, 7931, 7940, 7960,
                                                   				  or 7985, Cisco Unified IP Phone Expansion Modules, or Cisco Unified IP
                                                   				  Conference Stations. BLF Speed-Dial Not
                                                   				  supported on Cisco Unified IP Phone 7905, 7906, 7911, 7912, or 7985, or
                                                   				  Cisco Unified IP Conference Stations. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. pool-tag —Unique sequence number of the SIP phone
                                                   					 to be configured. Range is version and platform-dependent; type ? to display
                                                   					 range. You can modify the upper limit for this argument with the max-pool command. |
| Step 4 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 2 | Assigns a
                                             				directory number to the SIP phone. tag—identifier when there are multiple number commands. Range: 1 to 10. dn-tag —Directory number tag that was defined using
                                                   					 the voice register
                                                         						  dn command. |
| Step 5 | blf-speed-dial tag number label string [ device ] Example: Router(config-register-pool)# blf-speed-dial 3 3001 label sales device | Enables BLF
                                             				monitoring of a directory number associated with a speed-dial number on the
                                             				phone. tag —Number
                                                   					 that identifies the speed-dial index. Range: 1 to 7. number —Telephone number to speed dial. string —Alphanumeric label that identifies the
                                                   					 speed-dial button. The string can contain a maximum of 30 characters. device —(Optional) Enables phone-based monitoring.
                                                   					 This keyword is supported in Cisco Unified CME 7.1 and later versions. |
| Step 6 | presence
                                                				  call-list Example: Router(config-register-pool)# presence call-list | Enables BLF
                                             				monitoring of directory numbers that appear in call lists and directories on
                                             				this phone. For a
                                                   					 directory number to be monitored, it must have the allow watch command enabled. To
                                                   					 enable BLF monitoring for call lists on all phones in this Cisco Unified CME
                                                   					 system, use this command in presence mode. See Enabling
                                                      						Presence for Internal Lines . |
| Step 7 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | EM user
                                                   				  cannot modify the logout profile from phone user interface (UI). Extension
                                                   				  Mobility (EM) users must log into EM profile to update BLF-speed-dial number. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 10 | Enters ephone
                                             				configuration mode. phone-tag—Unique number of the phone for which you want to
                                                   					 configure BLF-speed-dial numbers. |
| Step 4 | blf-speed-dial [ index index
                                                				  number ]
                                                				  [ phone-number number ] [ label label
                                                				  text ] Example: Router(config-ephone)#blf-speed-dial 1 2001 label "customer support" | Creates an
                                             				entry for a BLF-speed-dial number on this phone. BLF-speed-dial index—Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 75. phone
                                                   					 number—Telephone number or extension to be dialed. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | presence Example: Router(config)# presence | Enables
                                             				presence service and enters presence configuration mode. |
| Step 4 | server ip-address Example: Router(config-presence)# server 10.10.10.1 | Specifies the
                                             				IP address of a presence server for sending presence requests from internal
                                             				watchers to external presentities. |
| Step 5 | allow subscribe Example: Router(config-presence)# allow subscribe | Allows
                                             				internal watchers to monitor external directory numbers. |
| Step 6 | watcher all Example: Router(config-presence)# watcher all | Allows
                                             				external watchers to monitor internal directory numbers. |
| Step 7 | sccp blf-speed-dial retry-interval seconds limit number Example: Router(config-presence)# sccp blf-speed-dial retry-interval 90 limit number 15 | (Optional)
                                             				Sets the retry timeout for BLF monitoring of speed-dial numbers on phones
                                             				running SCCP. seconds —Retry timeout in seconds. Range: 60 to
                                                   					 3600. Default: 60. number —Maximum number of retries.
                                                   					 Range: 10 to 100. Default: 10. |
| Step 8 | exit Example: Router(config-presence)# exit | Exits presence
                                             				configuration mode. |
| Step 9 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment. |
| Step 10 | authenticate presence Example: Router(config-register-global)# authenticate presence | (Optional)
                                             				Enables authentication of incoming presence requests from a remote presence
                                             				server. |
| Step 11 | authenticate credential tag
                                                				  location Example: Router(config-register-global)# authenticate credential 1 flash:cred1.csv | (Optional)
                                             				Specifies the credential file to use for authenticating presence subscription
                                             				requests. tag —Number
                                                   					 that identifies the credential file to use for presence authentication. Range:
                                                   					 1 to 5. location —Name and location of the credential file
                                                   					 in URL format. Valid storage locations are TFTP, HTTP, and flash memory. |
| Step 12 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show running-config Use this
                                             				command to verify your configuration. Router# show running-config !
voice register global
 mode cme
 source-address 10.1.1.2 port 5060
 load 7971 SIP70.8-0-1-11S
 load 7970 SIP70.8-0-1-11S
 load 7961GE SIP41.8-0-1-0DEV
 load 7961 SIP41.8-0-1-0DEV
 authenticate presence
 authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
 create profile sync 0004550081249644
.
.
.
presence
 server 10.1.1.4
 sccp blf-speed-dial retry-interval 70 limit 20
 presence call-list
 max-subscription 128
 watcher all
 allow subscribe
!
sip-ua
 presence enable |
|---|---|
| Step 2 | show presence global Use this
                                             				command to display presence configuration settings. Router# show presence global Presence Global Configuration Information:
=============================================
Presence feature enable            : TRUE
Presence allow external watchers   : FALSE
Presence max subscription allowed  : 100
Presence number of subscriptions   : 0
Presence allow external subscribe  : FALSE
Presence call list enable          : TRUE
Presence server IP address         : 0.0.0.0
Presence sccp blfsd retry interval : 60
Presence sccp blfsd retry limit    : 10
Presence router mode               : CME mode |
| Step 3 | show presence subscription [ details \| presentity telephone-number \| subid subscription-id summary ] Use this
                                             				command to display information about active presence subscriptions. Router# show presence subscription summary Presence Active Subscription Records Summary: 15 subscription
Watcher                  Presentity               SubID Expires SibID  Status
======================== ======================== ====== ======= ====== ======
6002@10.4.171.60         6005@10.4.171.34         1 3600    0      idle
6005@10.4.171.81         6002@10.4.171.34         6 3600    0      idle
6005@10.4.171.81         6003@10.4.171.34         8 3600    0      idle
6005@10.4.171.81         6002@10.4.171.34         9 3600    0      idle
6005@10.4.171.81         6003@10.4.171.34         10 3600    0      idle
6005@10.4.171.81         6001@10.4.171.34         12 3600    0      idle
6001@10.4.171.61         6003@10.4.171.34         15 3600    0      idle
6001@10.4.171.61         6002@10.4.171.34         17 3600    0      idle
6003@10.4.171.59         6003@10.4.171.34         19 3600    0      idle
6003@10.4.171.59         6002@10.4.171.34         21 3600    0      idle
6003@10.4.171.59         5001@10.4.171.34         23 3600    24     idle
6002@10.4.171.60         6003@10.4.171.34         121 3600    0      idle 
6002@10.4.171.60         5002@10.4.171.34         128 3600    129    idle
6005@10.4.171.81         1001@10.4.171.34         130 3600    131    busy
6005@10.4.171.81         7005@10.4.171.34         132 3600    133    idle |

| Feature Name | Cisco Unified CME Version | Modification |
|---|---|---|
| Phone User
                                       				  Interface for BLF-Speed-Dial | 8.5 | Added
                                       				  support for BLF Speed Dial through Phone User Interface. |
| BLF
                                       				  Monitoring | 7.1 | Added
                                             						support for device-based BLF monitoring. Added
                                             						support for BLF Monitoring of ephone-DNs with DnD, Call Park, Paging, and
                                             						Conferencing |
| Presence
                                       				  Service | 4.1 | Presence
                                       				  with BLF was introduced. |