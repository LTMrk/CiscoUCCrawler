---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-manager-assistant-user-guide-1251-cucm-b-4607477012
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_manager-assistant-user-guide-1251/cucm_b_manager-assistant-user-guide-1251_chapter_0101.html
retrieved_at: 2026-08-21T01:28:51.279664+00:00
---

Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: For Managers—Using Your Phone with Manager Assistant

## Chapter: For Managers—Using Your Phone with Manager Assistant

# For Managers—Using Your Phone with Manager Assistant

## For Managers—Using Your Phone with Manager Assistant

This chapter describes how to use your phone with the Manager Assistant in the shared-line and proxy-line modes. Your system
                              administrator is responsible for choosing the shared-line or proxy-line mode, and you need to identify the mode before you
                              begin using the Manager Assistant.

## Use Your Phone with the Manager Assistant in the Shared-Line Mode

In the shared-line mode, you and your assistant are assigned the same directory number, and your assistant uses the shared
                              number to handle calls for you.

The Manager Assistant provides these features for managers who are configured for shared-line mode:

Enhanced call-handling features on your Cisco Unified IP Phone—Provides softkeys and a status window on your phone LCD screen.

Intercom capabilities—Enables you to place intercom calls to your assistant and receive them from him or her.

Web-based feature configuration—Enables you to customize the divert target using the Manager Configuration window. or, your assistant can configure this feature for you from the Assistant Console.

## Divert and Transfer Call

Managers can use the Manager Assistant softkeys on your phone to divert, transfer, and generally handle active calls:

You can redirect an incoming call immediately to another number

You can press the Redirect softkey to divert a call that is ringing, connected, or on hold from the phone to another phone number that has been set
                                    up as the divert target. You or your assistant can change this target from the Manager Configuration window.

## Use Your Phone with the Manager Assistant in the Proxy-line Mode

When you use the Manager Assistant in the proxy-line mode, you are assigned a directory number and your assistant is assigned
                              an alternate directory number to use as a proxy number (line) to handle calls for you.

Your system administrator is responsible for choosing the shared-line or proxy-line mode, and you must identify the mode before
                              you begin using Manager Assistant.

The Manager Assistant provides these features for managers who are configured for the proxy-line mode:

Call-routing—Selectively redirects incoming calls to your phone or to your assistant’s phone based on your custom filter list.

Enhanced call-handling and monitoring features on your Cisco Unified IP Phone—Provides new softkeys and a status window on
                                    your phone LCD screen.

Intercom capabilities—Enables you to place intercom calls to and receive intercom calls from your assistant.

Web-based feature configuration—Enables you to customize some manager features, such as the divert target, using the Manager Configuration window. If you prefer, your assistant can configure these features for you from the Assistant Console.

### Understand
                           	 Assistant Selection

As a manager, you
                                 		  are logged in automatically to the Manager Assistant feature unless you are
                                 		  configured to use Cisco Extension Mobility.

To handle your
                                 		  calls, your assistant must log in to the Assistant Console and remain online.
                                 		  Your active assistant is the one who is handling calls for you currently. If
                                 		  that assistant logs out or goes offline, the Manager Assistant attempts to
                                 		  assign another assistant to you.

If the system
                                             			 administrator changes username, preferred location, or password, then you are
                                             			 not logged off. For user-ID changes, neither the manager nor the assistant is
                                             			 logged off when that manager's user ID is changed. However, an assistant is
                                             			 logged off the assistant's phone and the Assistant Console when that
                                             			 assistant's user ID is changed.

#### Identifying
                                 		  Your Active Assistant

If you have
                                 		  multiple assistants, you can identify which assistant is currently active by
                                 		  pressing the Services button on your phone and selecting Assistant Service . Item 3 identifies your active
                                 		  assistant. For more information on active assistant status, refer to Table 1 .

#### Assigning Your
                                 		  Default Assistant

When possible, the
                                 		  Manager Assistant assigns your default assistant to serve as your active
                                 		  assistant. If that assistant is unavailable (offline or logged out), the
                                 		  Manager Assistant assigns another assistant until your default assistant logs
                                 		  in or restores online availability.

You (or your
                                 		  assistant) can choose your default assistant from the Manager
                                    			 Configuration window.

#### Changing
                                 		  Assistants

If you have
                                 		  multiple assistants and more than one of them is available online, you can
                                 		  override the automatic selection by choosing your active assistant manually.

To see the
                                 		  assistant list, select item 3 from the Manager
                                    			 Status menu. Then you can select another assistant. For more
                                 		  information on changing assistants, refer to Table 1 .

#### When
                                 		  Assistants are Not Available

If all of your
                                 		  assistants are unavailable, the Assistant icon (left-most icon) in the Manager
                                    			 Status menu on your phone appears crossed out. Your call-handling
                                 		  support resumes as soon as one of your assistants logs in.

### Use the Manager Status Menu on Your Phone

To open the Manager Status menu on your phone, press the Services button and choose Assistant Service . The table describes Manager Status menu items and associated tasks.

Menu Item Number

Menu Item

What it does

1

Filter

Toggles call filtering off and on.

2

Filter Mode

Toggles between Inclusive or Exclusive filters.

3

Assistant

Displays your active assistant and other available assistants.

### Use the Status
                           	 Window

The Manager Status menu appears on the LCD screen of your Cisco
                                    			 Unified IP Phone .

There are two
                                 		  areas within the Manager Status menu:

- Assistant Watch area—The
                                    			 top part of the status window displaying the caller ID and the elapsed time for
                                    			 a call that an assistant is handling for you. For more information on Assistant
                                    			 Watch, see the Assistant
                                    		  Watch Messages table.

- Assistant and Features
                                    			 area—The largest portion of the status window displaying icons to indicate the
                                    			 presence of an active assistant and the on/off status of your features. For
                                    			 more information on Assistant Features, see the  Message Status Icons on the
                                    			 Cisco Unified IP Phones table.

The status window
                                 		  is not visible when you are using your phone to place or receive calls.

Press the SetWtch softkey to toggle Assistant Watch off and on.

Message

Meaning

“Assistant
                                             					 Watch - ON”

Assistant
                                             					 Watch is on but no connected or incoming calls are being redirected to your
                                             					 assistant at this time.

“Assistant
                                             					 Watch - OFF”

Assistant
                                             					 Watch is off. To set it to on, press the SetWtch softkey.

“Call
                                             					 from” followed by caller ID

An
                                             					 incoming call was redirected to your assistant and is currently ringing on your
                                             					 assistant’s phone. You can intercept the call now.

Caller ID
                                             					 and a timer

The
                                             					 assistant answered the incoming call. The timer begins when the assistant
                                             					 answers, or otherwise handles, the call.

“Filtering
                                             					 Down”

Call
                                             					 Filtering feature is unavailable at this time.

The icons for
                                             			 the Cisco Unified IP Phones with black and white LCD screens are the same as
                                             			 for the phones with colored screens, except as noted in the table.

Feature

Description

Assistant
                                             					 Available

The
                                             					 assistant icon resembles a person and is located on the left side of your
                                             					 status window. The icon indicates that an active assistant is ready to take
                                             					 your calls.

Assistant
                                             					 Unavailable

The
                                             					 assistant-unavailable icon resembles a person with a line across it. This
                                             					 indicates that all of your assistants are unavailable.

To
                                             					 identify your active assistant, press the Services button on your Cisco Unified IP Phone and
                                             					 then select Assistant Service .

Call
                                             					 Filter Enabled

A window
                                             					 with a pass-through green arrow and deflected red arrow indicate that filtering
                                             					 is on.

For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Enabled icon is a mesh-filled circle.

Call
                                             					 Filter Disabled

A
                                             					 crossed-out window with a pass-through green arrow and deflected red arrow
                                             					 indicates that filtering is off.

To toggle
                                             					 the filter off and on, select Filter from the Manager Status menu. You can configure call
                                             					 filtering from the Manager Configuration window.

For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Disabled icon is a hollow circle.

Do Not
                                             					 Disturb Enabled

A
                                             					 crossed-out bell indicates that the feature is on (ringer is disabled).

Do Not
                                             					 Disturb Disabled

A bell
                                             					 indicates that the feature is off (ringer is enabled).

To
                                             					 enable/disable the DND feature and turn your ringer on or off, press the DND softkey.

Divert All
                                             					 Enabled

An arrow
                                             					 deflected by a barrier indicates that the feature is on (calls are being
                                             					 redirected away from your phone).

Divert All
                                             					 Disabled

A
                                             					 crossed-out arrow deflected by a barrier indicates that the feature is off
                                             					 (calls are being directed to your phone).

To
                                             					 enable/disable the Divert All feature, press the DivAll softkey. The initial default target for this
                                             					 feature is your selected assistant. You can change the target from the Manager Configuration window.

#### Use the Status
                              	 Window for Cisco Desktop Collaboration Experience Phones

The status window
                                    		  is not visible when you are using your phone to place or receive calls.

Do Not Disturb and Set Assistant Watch softkey options are not available on Cisco Desktop Collaboration Experience Phones .

Feature

Description

Assistant
                                                					 Available

The
                                                					 assistant availability is displayed using the name of the assistant.

Assistant
                                                					 Unavailable

This message is displayed when no assistants are available.

To
                                                					 identify your active assistant, press the Services button on your phone and then select Assistant Service .

Call
                                                					 Filter On

To toggle
                                                					 the filter off and on, select Filter from the Manager Status menu. You can configure call
                                                					 filtering from the Manager Configuration window.

Call
                                                					 Filter Off

To
                                                					 toggle the filter off and on, select Filter from the Manager Status menu. You can configure call
                                                					 filtering from the Manager Configuration window.

Divert
                                                					 On

The
                                                					 "Divert on" message is displayed below the assistant's name.

Divert
                                                					 Off

The
                                                					 "Divert off" message is displayed below the assistant's name.

### Configure Alert
                           	 Tone for Incoming Calls

Incoming calls
                                 		  appear on the manager’s phone screen but ring only on the assistant’s phone.
                                 		  Use this procedure to add an audio alert to incoming calls on the manager’s
                                 		  phone.

Press the Services button.

Select Alert
                                             				Tone and set
                                          			 
                                          			 to On .

The alert
                                             				sounds once per call.

The alert tone
                                 		  does not play for incoming calls in these instances:

The alert tone
                                       				for your phone is turned off from the assistant’s phone or the Assistant
                                       				Console.

The Assistant
                                       				Watch feature is off.

You set calls
                                       				to redirect to your assistant automatically.

### Intercept the Call Ringing on the Assistant’s Phone

To intercept a call that is ringing on your assistant’s phone and to redirect the call to your own phone, press the Intrcpt softkey on your Cisco Unified IP Phone .

To successfully intercept the call, you must press the Intrcpt softkey before your assistant answers the call. You cannot intercept calls that have already connected.

When a call for you is ringing on your assistant’s phone, you can see the text “Call from” and the caller ID in the Assistant Watch portion of the status window on your phone.

### Redirect an Incoming Call to Another Number Immediately

To redirect a call that is ringing, connected, or on hold from your phone to another phone, press the Redirect softkey. By default, the Redirect feature redirects calls to your selected assistant. However, you or your assistant can
                                 substitute any phone number as the divert target.

If the assistant is the designated divert target and if you have Assistant Watch on, you can verify that the call has been redirected to your assistant by looking at the status window on your LCD screen.

The Redirect feature and the Divert All (DivAll) feature share the same divert target. You or your assistant can change this
                                 target from the Manager Configuration window.

### Redirect All Calls to Another Number

To toggle the Divert All (DivAll) feature on or off, press the DivAll softkey. When this feature is on, DivAll redirects your incoming calls to another phone. For the icons, see Table 2 table.

Unlike Redirect , which you invoke on a call-by-call basis, DivAll enables you to redirect all future incoming calls until you set the feature to off.

By default, the DivAll target is your selected assistant. However, you or your assistant can substitute any phone number as the divert target. For
                                 example, if you plan to be away from the office and you want to receive your calls during this time, you can set the Divert
                                 All target to your cell phone number.

DivAll applies to all of your lines that your assistant can manage, not calls that your assistant cannot access or calls that you
                                 receive on an intercom call.

The DivAll and Redirect features share the same divert target. You or your assistant can change this target from the Manager Configuration window.

If you have both call filtering and DivAll enabled, the Manager Assistant first applies call filtering to an incoming call. Call filtering directs the call to you or
                                 to your assistant (depending on filter settings.) Next, the Manager Assistant applies DivAll to those calls that filtering has directed to you. The DivAll feature redirects those calls to the DivAll target.

If you configure call forward all on your phone, all of your incoming calls are forwarded to the call-forward number that
                                 you entered. Your calls are not filtered to your assistant, and they are not redirected to your divert target.

### Transfer a Call to Voice-Messaging Service

To send a call immediately from your phone to your voice-messaging service, press the TrnsfVM softkey. You can transfer a call on hold to your voice messaging service.

### Use Call
                           	 Filtering

Call filtering
                                 		  redirects your incoming calls selectively to your assistant, based on the
                                 		  caller ID and these configurations and settings:

Filter Mode

Filter Lists

Filter on/off
                                       				status

Call-Filtering
                                 		  Settings table describes these filter settings.

The initial
                                 		  default settings are such that Inclusive call filtering is on and filter lists
                                 		  are empty, so all of your incoming calls are redirected to your assistant. To
                                 		  customize filtering, see Create Filter Lists for a Manager .

For your assistant
                                 		  to handle your calls, call filtering must be enabled. If you have both call
                                 		  filtering and Divert All (DivAll) enabled, the Manager Assistant first applies
                                 		  call filtering to an incoming call. Call filtering directs the call to you or
                                 		  to your assistant (depending on filter settings). Next, the Manager Assistant
                                 		  applies DivAll to those calls that filtering has directed to you. The DivAll
                                 		  feature redirects those calls to the DivAll target.

For example, you
                                 		  can set up a inclusive filter to receive only family calls. Your assistant then
                                 		  handles all other calls. If you have plans to be away from your office, you can
                                 		  set the DivAll target to your mobile phone number, enable Divert All, and
                                 		  receive the calls from your family on your mobile phone. Your assistant still
                                 		  receives all of the other calls.

When you configure
                                 		  call forward all on your phone, all your incoming calls are forwarded to the
                                 		  call-forward number that you entered. Your calls are not filtered to your
                                 		  assistant and they are not redirected to your divert target.

Setting

Purpose

Where to
                                             					 find it

Notes

Filter
                                             					 Mode

Use the
                                             					 filter mode setting to toggle between Inclusive and Exclusive filter lists. For
                                             					 more information, see Table 1 .

Toggle
                                             					 between Inclusive and Exclusive filter lists from the Manager Status menu on your phone’s LCD screen.

By initial
                                             					 default, the Inclusive filter is active.

Assistants
                                             					 can control the filter mode for you from the Assistant Console.

Filter
                                             					 Lists

Filter
                                             					 lists consist of one or more phone numbers (partial or entire). When you get a
                                             					 new call and filtering is on, the Manager Assistant compares the caller ID to
                                             					 the numbers in your active list. Depending on whether the numbers match and
                                             					 which filter list is active (Inclusive or Exclusive), the Manager Assistant
                                             					 then routes the call to you or to your assistant.

Create
                                             					 filter lists from the Manager Configuration window. Choose the Inclusive or Exclusive Filter tab.

Your
                                             					 assistant can set up filter lists for you. By default, filter lists are empty.

Filter
                                             					 on/off status

The filter
                                             					 on/off setting toggles call filtering on or off.

When the
                                             					 feature is on, all of your incoming calls are intercepted and redirected
                                             					 according to filter settings.

Toggle
                                             					 filtering on and off from the Manager Status menu on your phone LCD screen.
                                             					 Press the Services button and choose Assistant Service and then select Filter .

The
                                             					 default setting for the filter is On.

A circle icon in
                                 		  the Manager
                                    			 Status menu indicates if the call filtering feature is on or off:

On =
                                       				Mesh-filled circle icon.

Off = Hollow
                                       				circle.

## Handle Calls in Cisco Desktop Collaboration Experience Phones

Calls placed from
                              		  the manager's phone activate the following softkey options:

Softkey

Description

Conference

Enables
                                             						you to add conference participants to a call.

Hold

Puts the
                                             						call on hold.

Transfer
                                             						to VM

Redirects a ringing or connected call to the manager’s voice-messaging system.

Transfer
                                             						to other number

Redirects a selected call to a predetermined target number. You
                                             						can redirect a call that is ringing, connected, or on hold.

To
                                             						Assistant

Redirects a selected call to the assistant.

End

Ends the
                                             						connected call.

## Use the Intercom Feature to Speak to Assistant

The Intercom feature is an optional feature that enables you to speak to your assistant over an intercom line. The system
                              administrator configures this feature.

If this feature is not available on your phone, contact your system administrator.

To place an intercom call, press the Intercom button that corresponds to your assistant.

When you initiate the call, your assistant’s speakerphone answers automatically. You can begin talking using your speakerphone,
                                       headset, or handset. To speak to you, the assistant must press the Intercom button on their IP phone.

The following applies for all Cisco Unified IP phones except for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G:

In the shared-line mode, the current active assistant is the target for your intercom call. If no assistants are active when
                                                you log in, no target exists for your call.

In the proxy-line mode, various outcomes are possible after you initiate the call:

If a default assistant is configured and available, that assistant is the target for your call. If that assistant is unavailable,
                                                      the next available assistant becomes the target. If no assistants are active when you log in, the default assistant remains
                                                      the target.

If a default assistant is not configured, the current active assistant becomes the target. If that active assistant goes offline
                                                      while you are logged in, the next available assistant becomes the target. If no other assistants are available, the assistant
                                                      that went offline remains the target.

If a default assistant is not configured and no assistants are active at the time you log in, no target exists for your call.

Only for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G, if your assistant is busy on another
                                                      call, the intercom call rings on the assistant’s phone, and the assistant must answer it manually to hear the intercom. (This
                                                      is also the case when your assistant places an intercom call to you at a time when you are on another call.) For other phones,
                                                      the assistant does not need to answer the call to hear the intercom, as described at the beginning of this step.

To end the intercom call, hang up the phone (or push the Speaker or Headset button).

## Mute the Ringer on
                        	 Your Phone

To mute the ringer
                              		  on your phone, press the DND softkey to toggle the Do Not Disturb (DND)
                              		  feature on or off. (If the DND feature is not available on your phone, contact
                              		  your system administrator.)

When this feature
                              		  is on, the ringer is disabled on your Cisco
                                 			 Unified IP Phone . The DND feature disables the ringer for all lines
                              		  on the phone. (Intercom is not affected by the DND feature.) The initial
                              		  default setting is off.

The DND feature is
                              		  represented by a bell icon in the Manager
                                 			 Assistant status window on the LCD screen of your Cisco
                                 			 Unified IP Phone . For the icons, see Table 2 .

## Use Cisco
                        	 Extension Mobility

To use the Manager Assistant with Cisco Extension mobility, log in to 
                              		  Cisco Extension Mobility and in the Services menu, select Assistant Service .

For more information about the Cisco Extension Mobility feature, see the 
                              		  Cisco Unified IP Phone guides .

| Note | If the system
                                             			 administrator changes username, preferred location, or password, then you are
                                             			 not logged off. For user-ID changes, neither the manager nor the assistant is
                                             			 logged off when that manager's user ID is changed. However, an assistant is
                                             			 logged off the assistant's phone and the Assistant Console when that
                                             			 assistant's user ID is changed. |
|---|---|

| Menu Item Number | Menu Item | What it does |
|---|---|---|
| 1 | Filter | Toggles call filtering off and on. |
| 2 | Filter Mode | Toggles between Inclusive or Exclusive filters. |
| 3 | Assistant | Displays your active assistant and other available assistants. |

| Message | Meaning |
|---|---|
| “Assistant
                                             					 Watch - ON” | Assistant
                                             					 Watch is on but no connected or incoming calls are being redirected to your
                                             					 assistant at this time. |
| “Assistant
                                             					 Watch - OFF” | Assistant
                                             					 Watch is off. To set it to on, press the SetWtch softkey. |
| “Call
                                             					 from” followed by caller ID | An
                                             					 incoming call was redirected to your assistant and is currently ringing on your
                                             					 assistant’s phone. You can intercept the call now. |
| Caller ID
                                             					 and a timer | The
                                             					 assistant answered the incoming call. The timer begins when the assistant
                                             					 answers, or otherwise handles, the call. |
| “Filtering
                                             					 Down” | Call
                                             					 Filtering feature is unavailable at this time. |

| Note | The icons for
                                             			 the Cisco Unified IP Phones with black and white LCD screens are the same as
                                             			 for the phones with colored screens, except as noted in the table. |
|---|---|

| Feature | Description |
|---|---|
| Assistant
                                             					 Available | The
                                             					 assistant icon resembles a person and is located on the left side of your
                                             					 status window. The icon indicates that an active assistant is ready to take
                                             					 your calls. |
| Assistant
                                             					 Unavailable | The
                                             					 assistant-unavailable icon resembles a person with a line across it. This
                                             					 indicates that all of your assistants are unavailable. To
                                             					 identify your active assistant, press the Services button on your Cisco Unified IP Phone and
                                             					 then select Assistant Service . |
| Call
                                             					 Filter Enabled | A window
                                             					 with a pass-through green arrow and deflected red arrow indicate that filtering
                                             					 is on. Note For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Enabled icon is a mesh-filled circle. | Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Enabled icon is a mesh-filled circle. |
| Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Enabled icon is a mesh-filled circle. |
| Call
                                             					 Filter Disabled | A
                                             					 crossed-out window with a pass-through green arrow and deflected red arrow
                                             					 indicates that filtering is off. To toggle
                                             					 the filter off and on, select Filter from the Manager Status menu. You can configure call
                                             					 filtering from the Manager Configuration window. Note For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Disabled icon is a hollow circle. | Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Disabled icon is a hollow circle. |
| Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Disabled icon is a hollow circle. |
| Do Not
                                             					 Disturb Enabled | A
                                             					 crossed-out bell indicates that the feature is on (ringer is disabled). |
| Do Not
                                             					 Disturb Disabled | A bell
                                             					 indicates that the feature is off (ringer is enabled). To
                                             					 enable/disable the DND feature and turn your ringer on or off, press the DND softkey. |
| Divert All
                                             					 Enabled | An arrow
                                             					 deflected by a barrier indicates that the feature is on (calls are being
                                             					 redirected away from your phone). |
| Divert All
                                             					 Disabled | A
                                             					 crossed-out arrow deflected by a barrier indicates that the feature is off
                                             					 (calls are being directed to your phone). To
                                             					 enable/disable the Divert All feature, press the DivAll softkey. The initial default target for this
                                             					 feature is your selected assistant. You can change the target from the Manager Configuration window. |

| Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Enabled icon is a mesh-filled circle. |
|---|---|

| Note | For the
                                                         						Cisco Unified IP Phones with black-and-white LCD screens, the Call Filter Disabled icon is a hollow circle. |
|---|---|

| Note | Do Not Disturb and Set Assistant Watch softkey options are not available on Cisco Desktop Collaboration Experience Phones . |
|---|---|

| Feature | Description |
|---|---|
| Assistant
                                                					 Available | The
                                                					 assistant availability is displayed using the name of the assistant. |
| Assistant
                                                					 Unavailable | This message is displayed when no assistants are available. To
                                                					 identify your active assistant, press the Services button on your phone and then select Assistant Service . |
| Call
                                                					 Filter On | To toggle
                                                					 the filter off and on, select Filter from the Manager Status menu. You can configure call
                                                					 filtering from the Manager Configuration window. |
| Call
                                                					 Filter Off | To
                                                					 toggle the filter off and on, select Filter from the Manager Status menu. You can configure call
                                                					 filtering from the Manager Configuration window. |
| Divert
                                                					 On | The
                                                					 "Divert on" message is displayed below the assistant's name. |
| Divert
                                                					 Off | The
                                                					 "Divert off" message is displayed below the assistant's name. |

| Step 1 | Press the Services button. |
|---|---|
| Step 2 | Select Alert
                                             				Tone and set
                                          			 
                                          			 to On . The alert
                                             				sounds once per call. |

| Setting | Purpose | Where to
                                             					 find it | Notes |
|---|---|---|---|
| Filter
                                             					 Mode | Use the
                                             					 filter mode setting to toggle between Inclusive and Exclusive filter lists. For
                                             					 more information, see Table 1 . | Toggle
                                             					 between Inclusive and Exclusive filter lists from the Manager Status menu on your phone’s LCD screen. | By initial
                                             					 default, the Inclusive filter is active. Assistants
                                             					 can control the filter mode for you from the Assistant Console. |
| Filter
                                             					 Lists | Filter
                                             					 lists consist of one or more phone numbers (partial or entire). When you get a
                                             					 new call and filtering is on, the Manager Assistant compares the caller ID to
                                             					 the numbers in your active list. Depending on whether the numbers match and
                                             					 which filter list is active (Inclusive or Exclusive), the Manager Assistant
                                             					 then routes the call to you or to your assistant. | Create
                                             					 filter lists from the Manager Configuration window. Choose the Inclusive or Exclusive Filter tab. | Your
                                             					 assistant can set up filter lists for you. By default, filter lists are empty. |
| Filter
                                             					 on/off status | The filter
                                             					 on/off setting toggles call filtering on or off. When the
                                             					 feature is on, all of your incoming calls are intercepted and redirected
                                             					 according to filter settings. | Toggle
                                             					 filtering on and off from the Manager Status menu on your phone LCD screen.
                                             					 Press the Services button and choose Assistant Service and then select Filter . | The
                                             					 default setting for the filter is On. |

| Softkey | Description |
|---|---|
| Conference | Enables
                                             						you to add conference participants to a call. |
| Hold | Puts the
                                             						call on hold. |
| Transfer
                                             						to VM | Redirects a ringing or connected call to the manager’s voice-messaging system. |
| Transfer
                                             						to other number | Redirects a selected call to a predetermined target number. You
                                             						can redirect a call that is ringing, connected, or on hold. |
| To
                                             						Assistant | Redirects a selected call to the assistant. |
| End | Ends the
                                             						connected call. |

| Note | If this feature is not available on your phone, contact your system administrator. |
|---|---|

| Step 1 | To place an intercom call, press the Intercom button that corresponds to your assistant. |
|---|---|
| Step 2 | When you initiate the call, your assistant’s speakerphone answers automatically. You can begin talking using your speakerphone,
                                       headset, or handset. To speak to you, the assistant must press the Intercom button on their IP phone. The following applies for all Cisco Unified IP phones except for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G: In the shared-line mode, the current active assistant is the target for your intercom call. If no assistants are active when
                                                you log in, no target exists for your call. In the proxy-line mode, various outcomes are possible after you initiate the call: If a default assistant is configured and available, that assistant is the target for your call. If that assistant is unavailable,
                                                      the next available assistant becomes the target. If no assistants are active when you log in, the default assistant remains
                                                      the target. If a default assistant is not configured, the current active assistant becomes the target. If that active assistant goes offline
                                                      while you are logged in, the next available assistant becomes the target. If no other assistants are available, the assistant
                                                      that went offline remains the target. If a default assistant is not configured and no assistants are active at the time you log in, no target exists for your call. Note Only for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G, if your assistant is busy on another
                                                      call, the intercom call rings on the assistant’s phone, and the assistant must answer it manually to hear the intercom. (This
                                                      is also the case when your assistant places an intercom call to you at a time when you are on another call.) For other phones,
                                                      the assistant does not need to answer the call to hear the intercom, as described at the beginning of this step. | Note | Only for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G, if your assistant is busy on another
                                                      call, the intercom call rings on the assistant’s phone, and the assistant must answer it manually to hear the intercom. (This
                                                      is also the case when your assistant places an intercom call to you at a time when you are on another call.) For other phones,
                                                      the assistant does not need to answer the call to hear the intercom, as described at the beginning of this step. |
| Note | Only for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G, if your assistant is busy on another
                                                      call, the intercom call rings on the assistant’s phone, and the assistant must answer it manually to hear the intercom. (This
                                                      is also the case when your assistant places an intercom call to you at a time when you are on another call.) For other phones,
                                                      the assistant does not need to answer the call to hear the intercom, as described at the beginning of this step. |
| Step 3 | To end the intercom call, hang up the phone (or push the Speaker or Headset button). |

| Note | Only for the Cisco Unified IP Phones 7961G-GE, 7961G, 7960G, 7941G-GE, 7941G, and 7940G, if your assistant is busy on another
                                                      call, the intercom call rings on the assistant’s phone, and the assistant must answer it manually to hear the intercom. (This
                                                      is also the case when your assistant places an intercom call to you at a time when you are on another call.) For other phones,
                                                      the assistant does not need to answer the call to hear the intercom, as described at the beginning of this step. |
|---|---|