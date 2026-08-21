---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--1d6f8cb911
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_01000.html
retrieved_at: 2026-08-21T14:35:21.130732+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Phone Features and Setup

## Chapter: Phone Features and Setup

# Phone Features and Setup

## Phone Features and Setup Overview

After you install Cisco Unified IP Phones in your network, configure their network settings, and add them to Cisco Unified
                           Communications Manager, you must use the Cisco Unified Communications Manager Administration application to configure telephony
                           features, optionally modify phone templates, set up services, and assign users.

This chapter provides an overview of these configuration and setup procedures. Cisco Unified Communications Manager documentation
                           provides detailed instructions for these procedures.

To list supported features for all phones or for a particular phone model on your Cisco Unified Communications Manager, you
                           can generate a Unified CM Phone Feature List report on Cisco Unified Reporting.

For suggestions about how to provide users with information about features, and what information to provide, see Cisco IP Phone User Support .

For information about setting up phones in non-English environments, see International User Support .

## Cisco IP Phone User Support

If you are a system administrator, you are likely the primary source of information for Cisco IP Phone users in your network
                              or company. It is important to provide current and thorough information to end users.

To successfully use some of the features on the Cisco IP Phone (including Services and voice message system options), users
                              must receive information from you or from your network team or must be able to contact you for assistance. Make sure to provide
                              users with the names of people to contact for assistance and with instructions for contacting those people.

We recommend that you create a web page on your internal support site that provides end users with important information about
                              their Cisco IP Phones.

Consider including the following types of information on this site:

User guides for all Cisco IP Phone models that you support

Information on how to access the Cisco Unified Communications Self Care Portal

List of features supported

User guide or quick reference for your voicemail system

## Telephony Features

CiscoUnified IP Phones provide traditional telephony functionality, such as call forwarding and transferring, redialing, conference
                              calling, and voice messaging system access. CiscoUnified IP phones also provide a variety of other features.

As with other network devices, you must configure CiscoUnified IP Phones to prepare them to access CiscoUnifiedCommunications
                              Manager and the rest of the IP network. By using DHCP, you have fewer settings to configure on a phone, but if your network
                              requires it, you can manually configure an IP address, TFTP server, subnet information, and so on.

Finally, because the CiscoUnified IP Phone is a network device, you can obtain detailed status information from it directly.
                              This information can assist you with troubleshooting any problems users might encounter when using their IP phones.

You can modify additional settings for the CiscoUnified IP
                              		Phone from Cisco Unified Communications Manager Administration. Use Cisco
                              		Unified Communications Manager Administration to set up phone registration
                              		criteria and calling search spaces, among other tasks. See the "Telephony
                                 		  Features" section in this document and the CiscoUnifiedCommunications
                              		Manager documentation for additional information.

For more information about CiscoUnified Communications Manager
                              		Administration, see the  CiscoUnifiedCommunications Manager documentation,
                              		including Cisco UnifiedCommunications Manager Administration Guide .
                              		You can also use the context-sensitive help available within the application
                              		for guidance.

After you add CiscoUnified IP Phones to
                              		  CiscoUnifiedCommunications Manager, you can add functionality to the phones.
                              		  The following table includes a list of supported telephony features, many of
                              		  which you can configure using CiscoUnifiedCommunications Manager
                              		  Administration.

For information about using most of these features on the
                              		  phone, see the Cisco Unified SIP Phone 3905 User Guide for Cisco Unified Communications Manager .

CiscoUnified Communications Manager Administration also provides
                                          			 several service parameters that you can use to configure various telephony
                                          			 functions. For more information on accessing and configuring service
                                          			 parameters, refer to Cisco UnifiedCommunications Manager Administration
                                             				Guide .

For more information on the functions of a service, select the name
                                          			 of the parameter or the question mark help button in the Service
                                          				Parameter Configuration window.

Feature

Description

Audible Message Waiting Indicator (AMWI)

A stutter tone from the handset or speakerphone indicates that
                                          					 a user has one or more new voice messages on a line.

See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter.

Auto Answer

Connects incoming calls automatically after a ring or two.

Auto Answer works with the speakerphone.

See  the Cisco Unified Communications Manager Administration
                                             						Guide , "Directory Number Configuration" chapter.

Block External to External Transfer

Prevents users from transferring an external call to another
                                          					 external number.

See  the Cisco Unified Communications
                                             						Manager Features and Services Guide , "External Call Transfer Restrictions" chapter.

Call Forward

Allows users to redirect incoming calls to another number. The
                                          					 Call Forward All option is supported. 
                                          				  Users hear a stutter tone after going off-hook if the Call Forward
                                          					 All feature is configured on the phone.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter

- Cisco
                                                						  Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter

- Customize the Self Care Portal Display

Call Forward All Loop Breakout

Detects and prevents Call Forward All loops. When a Call
                                          					 Forward All loop is detected, the Call Forward All configuration is ignored and
                                          					 the call rings through.

See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter.

Call Forward All Loop Prevention

Prevents a user from configuring a Call Forward All
                                          					 destination directly on the phone that creates a Call Forward All loop or that
                                          					 creates a Call Forward All chain with more hops than the existing Forward
                                          					 Maximum Hop Count service parameter allows.

See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter.

Call Forward Destination Override

Allows you to override Call Forward All (CFA) in cases where
                                          					 the CFA target places a call to the CFA initiator. This feature allows the CFA
                                          					 target to reach the CFA initiator for important calls. The override works
                                          					 whether the CFA target phone number is internal or external.

See  the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

Call Pickup

Allows users to answer a call that is ringing on a co-worker's
                                          					 phone by redirecting the call to their phone

You can configure an audio alert for the primary line on the
                                          					 phone. This alert notifies the users that a call is ringing in their pickup
                                          					 group.

See  the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Call Pickup" chapter.

Call Waiting

Indicates (and allows users to answer) an incoming call that
                                          					 rings while on another call.

The phone sounds the call waiting tone (single beep) and the
                                          					 phone screen displays the second incoming call.

See Cisco
                                             						  Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

cBarge

Allows a user to join a non-private call on a shared phone
                                          					 line. cBarge adds a user to a call and converts it into a conference, allowing
                                          					 the user and other parties to access conference features.

For more information, see the Cisco
                                             						  UnifiedCommunications Manager Features and Services Guide "Barge and Privacy" chapter.

Conference

- Allows a user to
                                             						talk simultaneously with multiple parties by calling each participant
                                             						individually.

- Allows a
                                             						non-initiator in a standard (adhoc) conference to add participants; also
                                             						allows any conference participant to join together two standard conferences on
                                             						the same line.

The service parameter, Advance Adhoc Conference, (disabled by
                                          					 default in Cisco Unified Communications Manager Administration) allows you to
                                          					 enable these features.

See:

CiscoUnified Communications Manager System Guide, "Conference Bridges" chapter.

Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter.

Be sure to inform your users whether these features are
                                                      						activated.

Forced Authorization Codes (FAC)

Controls the types of calls that certain users can place.

For more information, see  the Cisco UnifiedCommunications Manager Features and
                                             						Services Guide , "Client Matter Codes" and "Forced Authorization Codes" chapters.

Group Call Pickup

Allows a user to answer a call that is ringing on a directory
                                          					 number in another group.

For more information, see the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Call Pickup" chapter.

Hold/Resume

Allows the user to move a connected call from an active state
                                          					 to a held state by using the Hold/Resume button. The user resumes a held call
                                          					 by pressing the Hold/Resume button, speaker button, or going off-hook.

No configuration required unless you want to use music on
                                          					 hold. See "Music-On-Hold" in this table for information.

Hookflash Timer

Controls the length of time before the hookflash indicates a
                                          					 timeout (or call disconnect).

See Cisco
                                             						  Unified Communications Manager Administration Guide , "Cisco Unified IP Phone Configuration" chapter.

Line Text Label

Sets a text label for a phone line instead of the directory number.

See Set the Label for a Line .

Message Waiting

Defines directory numbers for message-waiting on and
                                          					 message-waiting off indicator. A directly connected voice-messaging system uses
                                          					 the specified directory number to set or to clear a message-waiting indication
                                          					 for a particular Cisco Unified IP Phone.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , "Message Waiting Configuration" chapter

- Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail
                                                						  Connectivity to Cisco Unified Communications Manager" chapter.

Message Waiting Indicator

A light on the phone that indicates that a user has one or
                                          					 more new voice messages.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , "Message Waiting Configuration" chapter

- Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail Connectivity to Cisco Unified Communications
                                                						  Manager" chapter

Music On Hold

Plays music while callers are on hold.

See the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Music On Hold" chapter.

Mute

Mutes the microphone from the handset or speakerphone.

No configuration required.

On-hook Call Transfer

Allows a user to press the Transfer button and then go on-hook
                                          					 to complete a call transfer.

See 
                                          					 the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phones" chapter.

Plus Dialing

Allows the user to dial E.164 numbers prefixed with a + sign.

To dial the + sign, the user needs to press and hold
                                          					 the * key for at least 1 second. This applies to dialing
                                          					 the first digit for both on-hook or off-hook calls.

Requires no configuration.

Private Line Automated Ringdown (PLAR)

The Cisco UnifiedCommunications Manager administrator can
                                          					 configure a phone number that the Cisco UnifiedIPPhone dials as soon as the
                                          					 handset goes off-hook. This can be useful for phones that are designated for
                                          					 calling emergency or hotline numbers.

See the Cisco Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter.

Redial

Allows users to call the most recently dialed phone number by
                                          					 pressing the Redial button.

No configuration required.

Shared Line

Allows a user to have multiple phones that share the same
                                          					 phone number or allows a user to share a phone number with a coworker.

See the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

Telnet

You can use Telnet to connect to your Cisco Unified IP Phone
                                          					 for use in troubleshooting and phone maintenance.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , " Cisco Unified
                                                						  IP Phone Configuration" chapter

- Cisco
                                                						  Unified Communications Manager Administration Guide , "SIP Profile Configuration Settings" chapter

Time-of-Day Routing

Restricts access to specified telephony features by time
                                          					 period.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , "Time Period Configuration" chapter

- Cisco
                                                						  Unified Communications Manager System Guide , "Time-of-Day Routing" chapter

Time Zone Update

Updates the Cisco Unified IP Phone with time zone changes.

See the Cisco Unified Communications Manager Administration
                                             						Guide , "Time Group Configuration" chapter.

Transfer

Allows users to redirect connected calls from their phones to
                                          					 another number.

No configuration required.

Voice Messaging System

Enables callers to leave messages if calls are unanswered.

See:

- Cisco
                                                						  Unified Communications Manager Administration Guide , " Cisco
                                                						  Voice-Mail Port Configuration" chapter

- Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail Connectivity to Cisco Unified Communications
                                                						  Manager" chapter

## Disable
                        	 Speakerphone

By
                              		  default, the speakerphone is enabled on the Cisco IP Phone.

You can
                              		  disable the speakerphone by using Cisco Unified Communications Manager
                              		  Administration. 
                              		When
                              		  the speakerphone is disabled, the Redial, New Call, and Forward All softkeys
                              		  are not displayed on the phones when the user presses the speakerphone button.
                              		  The softkey labels are dimmed or removed.

Step 1

From Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone .

Step 2

Select the
                                       			 phone you want to modify.

Step 3

In the Phone
                                       			 Configuration window for the phone, check the Disable Speakerphone check box.

Step 4

Select Save .

## Control Phone Web Page Access

For security purposes, access to the phone web pages is
                              		  disabled by default. This practice prevents access to the phone web pages and the  Cisco Unified Communications Self Care
                              Portal.

Some features, such as Cisco Quality Report Tool, do not function
                                          			 properly without access to the phone web pages. Disabling web access also
                                          			 affects any serviceability application that relies on web access, such as
                                          			 CiscoWorks.

Step 1

In Cisco Unified Communications Manager Administration, choose Device > Phone .

Step 2

Specify the criteria to find the phone and select Find , or select Find to display a list of all phones.

Step 3

Select the device name to open the Phone Configuration window for
                                       			 the device.

Step 4

Scroll to the Product Specific Configuration area.

Step 5

To enable access, from the Web Access drop-down list, choose Enabled .

Step 6

To disable access, from the Web Access drop-down list, choose Disabled .

Step 7

Select Save .

## Set the Label for a Line

You can set up a phone to display a text label instead of the directory number. Use this label to identify the line by name
                              or function.  For example, if your user shares lines on the phone, you could identify the line with the name of the person
                              that shares the line.

When adding a label to a key expansion module, only the first 25 characters are displayed on a line.

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone to be configured.

Step 3

Locate the line instance and set the Line Text Label field.

Step 4

(Optional) If the label needs to be applied to other devices that share the line, check the Update Shared Device
                                       Settings check box and click Propagate Selected .

Step 5

Select Save .

| Note | CiscoUnified Communications Manager Administration also provides
                                          			 several service parameters that you can use to configure various telephony
                                          			 functions. For more information on accessing and configuring service
                                          			 parameters, refer to Cisco UnifiedCommunications Manager Administration
                                             				Guide . For more information on the functions of a service, select the name
                                          			 of the parameter or the question mark help button in the Service
                                          				Parameter Configuration window. |
|---|---|

| Feature | Description |
|---|---|
| Audible Message Waiting Indicator (AMWI) | A stutter tone from the handset or speakerphone indicates that
                                          					 a user has one or more new voice messages on a line. See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter. |
| Auto Answer | Connects incoming calls automatically after a ring or two. Auto Answer works with the speakerphone. See  the Cisco Unified Communications Manager Administration
                                             						Guide , "Directory Number Configuration" chapter. |
| Block External to External Transfer | Prevents users from transferring an external call to another
                                          					 external number. See  the Cisco Unified Communications
                                             						Manager Features and Services Guide , "External Call Transfer Restrictions" chapter. |
| Call Forward | Allows users to redirect incoming calls to another number. The
                                          					 Call Forward All option is supported. 
                                          				  Users hear a stutter tone after going off-hook if the Call Forward
                                          					 All feature is configured on the phone. See: Cisco
                                                						  Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter Cisco
                                                						  Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter Customize the Self Care Portal Display |
| Call Forward All Loop Breakout | Detects and prevents Call Forward All loops. When a Call
                                          					 Forward All loop is detected, the Call Forward All configuration is ignored and
                                          					 the call rings through. See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter. |
| Call Forward All Loop Prevention | Prevents a user from configuring a Call Forward All
                                          					 destination directly on the phone that creates a Call Forward All loop or that
                                          					 creates a Call Forward All chain with more hops than the existing Forward
                                          					 Maximum Hop Count service parameter allows. See  the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter. |
| Call Forward Destination Override | Allows you to override Call Forward All (CFA) in cases where
                                          					 the CFA target places a call to the CFA initiator. This feature allows the CFA
                                          					 target to reach the CFA initiator for important calls. The override works
                                          					 whether the CFA target phone number is internal or external. See  the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| Call Pickup | Allows users to answer a call that is ringing on a co-worker's
                                          					 phone by redirecting the call to their phone You can configure an audio alert for the primary line on the
                                          					 phone. This alert notifies the users that a call is ringing in their pickup
                                          					 group. See  the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Call Pickup" chapter. |
| Call Waiting | Indicates (and allows users to answer) an incoming call that
                                          					 rings while on another call. The phone sounds the call waiting tone (single beep) and the
                                          					 phone screen displays the second incoming call. See Cisco
                                             						  Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| cBarge | Allows a user to join a non-private call on a shared phone
                                          					 line. cBarge adds a user to a call and converts it into a conference, allowing
                                          					 the user and other parties to access conference features. For more information, see the Cisco
                                             						  UnifiedCommunications Manager Features and Services Guide "Barge and Privacy" chapter. |
| Conference | Allows a user to
                                             						talk simultaneously with multiple parties by calling each participant
                                             						individually. Allows a
                                             						non-initiator in a standard (adhoc) conference to add participants; also
                                             						allows any conference participant to join together two standard conferences on
                                             						the same line. The service parameter, Advance Adhoc Conference, (disabled by
                                          					 default in Cisco Unified Communications Manager Administration) allows you to
                                          					 enable these features. See: CiscoUnified Communications Manager System Guide, "Conference Bridges" chapter. Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phone" chapter. Note Be sure to inform your users whether these features are
                                                      						activated. | Note | Be sure to inform your users whether these features are
                                                      						activated. |
| Note | Be sure to inform your users whether these features are
                                                      						activated. |
| Forced Authorization Codes (FAC) | Controls the types of calls that certain users can place. For more information, see  the Cisco UnifiedCommunications Manager Features and
                                             						Services Guide , "Client Matter Codes" and "Forced Authorization Codes" chapters. |
| Group Call Pickup | Allows a user to answer a call that is ringing on a directory
                                          					 number in another group. For more information, see the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Call Pickup" chapter. |
| Hold/Resume | Allows the user to move a connected call from an active state
                                          					 to a held state by using the Hold/Resume button. The user resumes a held call
                                          					 by pressing the Hold/Resume button, speaker button, or going off-hook. No configuration required unless you want to use music on
                                          					 hold. See "Music-On-Hold" in this table for information. |
| Hookflash Timer | Controls the length of time before the hookflash indicates a
                                          					 timeout (or call disconnect). See Cisco
                                             						  Unified Communications Manager Administration Guide , "Cisco Unified IP Phone Configuration" chapter. |
| Line Text Label | Sets a text label for a phone line instead of the directory number. See Set the Label for a Line . |
| Message Waiting | Defines directory numbers for message-waiting on and
                                          					 message-waiting off indicator. A directly connected voice-messaging system uses
                                          					 the specified directory number to set or to clear a message-waiting indication
                                          					 for a particular Cisco Unified IP Phone. See: Cisco
                                                						  Unified Communications Manager Administration Guide , "Message Waiting Configuration" chapter Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail
                                                						  Connectivity to Cisco Unified Communications Manager" chapter. |
| Message Waiting Indicator | A light on the phone that indicates that a user has one or
                                          					 more new voice messages. See: Cisco
                                                						  Unified Communications Manager Administration Guide , "Message Waiting Configuration" chapter Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail Connectivity to Cisco Unified Communications
                                                						  Manager" chapter |
| Music On Hold | Plays music while callers are on hold. See the Cisco Unified Communications Manager Features and
                                             						Services Guide , "Music On Hold" chapter. |
| Mute | Mutes the microphone from the handset or speakerphone. No configuration required. |
| On-hook Call Transfer | Allows a user to press the Transfer button and then go on-hook
                                          					 to complete a call transfer. See 
                                          					 the Cisco Unified Communications Manager System Guide , "Cisco Unified IP Phones" chapter. |
| Plus Dialing | Allows the user to dial E.164 numbers prefixed with a + sign. To dial the + sign, the user needs to press and hold
                                          					 the * key for at least 1 second. This applies to dialing
                                          					 the first digit for both on-hook or off-hook calls. Requires no configuration. |
| Private Line Automated Ringdown (PLAR) | The Cisco UnifiedCommunications Manager administrator can
                                          					 configure a phone number that the Cisco UnifiedIPPhone dials as soon as the
                                          					 handset goes off-hook. This can be useful for phones that are designated for
                                          					 calling emergency or hotline numbers. See the Cisco Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter. |
| Redial | Allows users to call the most recently dialed phone number by
                                          					 pressing the Redial button. No configuration required. |
| Shared Line | Allows a user to have multiple phones that share the same
                                          					 phone number or allows a user to share a phone number with a coworker. See the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| Telnet | You can use Telnet to connect to your Cisco Unified IP Phone
                                          					 for use in troubleshooting and phone maintenance. See: Cisco
                                                						  Unified Communications Manager Administration Guide , " Cisco Unified
                                                						  IP Phone Configuration" chapter Cisco
                                                						  Unified Communications Manager Administration Guide , "SIP Profile Configuration Settings" chapter |
| Time-of-Day Routing | Restricts access to specified telephony features by time
                                          					 period. See: Cisco
                                                						  Unified Communications Manager Administration Guide , "Time Period Configuration" chapter Cisco
                                                						  Unified Communications Manager System Guide , "Time-of-Day Routing" chapter |
| Time Zone Update | Updates the Cisco Unified IP Phone with time zone changes. See the Cisco Unified Communications Manager Administration
                                             						Guide , "Time Group Configuration" chapter. |
| Transfer | Allows users to redirect connected calls from their phones to
                                          					 another number. No configuration required. |
| Voice Messaging System | Enables callers to leave messages if calls are unanswered. See: Cisco
                                                						  Unified Communications Manager Administration Guide , " Cisco
                                                						  Voice-Mail Port Configuration" chapter Cisco
                                                						  Unified Communications Manager System Guide , "Voice Mail Connectivity to Cisco Unified Communications
                                                						  Manager" chapter |

| Note | Be sure to inform your users whether these features are
                                                      						activated. |
|---|---|

| Step 1 | From Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Select the
                                       			 phone you want to modify. |
| Step 3 | In the Phone
                                       			 Configuration window for the phone, check the Disable Speakerphone check box. |
| Step 4 | Select Save . |

| Note | Some features, such as Cisco Quality Report Tool, do not function
                                          			 properly without access to the phone web pages. Disabling web access also
                                          			 affects any serviceability application that relies on web access, such as
                                          			 CiscoWorks. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| Step 2 | Specify the criteria to find the phone and select Find , or select Find to display a list of all phones. |
| Step 3 | Select the device name to open the Phone Configuration window for
                                       			 the device. |
| Step 4 | Scroll to the Product Specific Configuration area. |
| Step 5 | To enable access, from the Web Access drop-down list, choose Enabled . |
| Step 6 | To disable access, from the Web Access drop-down list, choose Disabled . |
| Step 7 | Select Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone to be configured. |
| Step 3 | Locate the line instance and set the Line Text Label field. |
| Step 4 | (Optional) If the label needs to be applied to other devices that share the line, check the Update Shared Device
                                       Settings check box and click Propagate Selected . |
| Step 5 | Select Save . |