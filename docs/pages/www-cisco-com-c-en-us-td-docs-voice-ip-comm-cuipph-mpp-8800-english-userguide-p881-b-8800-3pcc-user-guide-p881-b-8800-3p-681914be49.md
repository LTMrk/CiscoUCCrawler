---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-userguide-p881-b-8800-3pcc-user-guide-p881-b-8800-3p-681914be49
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/userguide/p881_b_8800-3pcc-user-guide/p881_b_8800-3pcc-user-guide-110_chapter_01011.html
retrieved_at: 2026-08-21T02:35:44.737229+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

# Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Updated: November 19, 2025

Chapter: Voicemail

## Chapter: Voicemail

# Voicemail

## Your Personal Voicemail Account

You can access your personal voice messages directly from your phone. But your administrator must set up your voicemail account,
                           and may also set up your phone to access the voicemail system.

The Messages button on your phone acts as a speed dial into the voicemail system.

When you aren’t at your desk, you can call your voicemail system to access your voicemail. Your administrator can give you
                           the voicemail system phone number.

Because each voicemail system is different, we can't tell you how to use your voicemail system. For information about your
                           voicemail commands, see the voicemail system user documentation or contact your administrator.

### Set up Voicemail on Your Phone

Step 1

Press Applications .

Step 2

Select User preferences > Call preferences .

Step 3

Enter your personal voicemail phone number in Voice mail .

Step 4

Press Set .

## Find out if you have new voicemail messages Your Personal

To find out if you have new voicemail messages, look for one of these signs:

The light strip on your handset is solid red.

The number of missed calls and voicemail messages is displayed on your screen. If you have more than 99 new messages, a plus
                                 (+) sign is displayed.

An exclamation mark (!) indicates urgent voicemail messages.

Cisco IP Phone 6800 Series, 7800 Series, and 8800 Series: You will also hear a stutter tone played from your handset, headset, or speakerphone when you use a phone line. This stutter
                           tone is line-specific. You only hear it when you use a line that has voice messages.

Cisco IP Conference Phone 7832 and 8832: You will hear a stutter tone played from the speakerphone when you use the phone line. You only hear it when the line has
                           a voice message.

## Access Your Personal your voicemail

Step 1

Press Messages .

Step 2

Do one of the following actions:

- 6800: Press Messages or Messages .

- 7800 and 8800: Press Messages .

- 7832 and 8832: Press Messages .

Step 3

Follow the voice prompts.

For details on voicemail features and PIN rules, see Set up and manage your voicemail .

## Access Your Personal Audio Voicemail

Depending upon how your administrator has set up your phone, you can retrieve your personal voicemail without viewing a list
                              of messages. This option is useful if you prefer a list of voicemail messages, but you occasionally access your messages without
                              the visual prompts.

Step 1

In the screen, press the Audio softkey.

Step 2

When prompted, enter your voicemail credentials.

## Phone Behavior
                        	 with Voicemail Setting

This table lists
                              		  the phone behavior in various scenarios when the Handset
                                 			 LED Alert field in the Configuration Utility is set to Voicemail.

Starting State

Event

LED
                                          						Status After Event

LED
                                          						Turn Off Criteria

No
                                          						Voicemail, No Missed Call

There is
                                          						no active call and a call is missed or a call is on hold and the call is
                                          						missed.

LED Off

-

No
                                          						Voicemail, No Missed Call

Voicemail comes in

LED On

User
                                          						calls the voicemail to retrieve a message.

Voicemail

There is
                                          						no active call and a call is missed or a call is on hold and the call is
                                          						missed.

LED On

User
                                          						calls the voicemail to retrieve a message.

Missed
                                          						Call

Voicemail comes in

LED On

User
                                          						calls the voicemail to retrieve a message.

No
                                          						Voicemail, No Missed Call

No event

LED Off

-

## Phone Behavior
                        	 with Voicemail and Missed Call Configuration Setting

This table lists
                              		  the phone behavior in various scenarios when the Handset
                                 			 LED Alert field in the Configuration Utility is set to Voicemail, Missed Call .

Starting State

Event

LED
                                             						Status After Event

LED
                                             						Turn Off Criteria

No
                                             						Voicemail, No Missed Call

There is
                                             						no active call and a call is missed or a call is on hold and the call is
                                             						missed.

LED On

User
                                             						interacts with the phone.

No
                                             						Voicemail, No Missed Call

Voicemail comes in

LED On

User
                                             						calls the voicemail to retrieve a message.

Voicemail

There is
                                             						no active call and a call is missed or a call is on hold and the call is
                                             						missed.

LED On

User
                                             						interacts with the phone and calls the voicemail to retrieve a message.

Missed
                                             						Call

Voicemail comes in

LED On

User
                                             						interacts with the phone and calls the voicemail to retrieve a message.

No
                                             						Voicemail, No Missed Call

No event

LED Off

-

## Voice Messages States of Monitored Voicemail Accounts

You can see the voicemail messages state of a voicemail account of a user or group on a line key or on an expansion module button .

The scope of the monitored voicemail account:

an extension-associated voicemail account that is configured on the phone

a voicemail account that is different from any extension-associated voicemail account

To check if your SIP proxy provides the support, contact your administrator.

A monitored voicemail account displays one of these icons beside the line key or expansion module button :

: There are no voicemail messages for the monitored account.

: There are new voicemail messages. The number of messages displays adjacent to the name of the monitored account. For example, (4) VM 3300 shows there are four voicemail messages for the monitored account VM 3300 .

: The new voicemail messages contain at least one urgent message.

: The line failed to register to the voicemail server.

The line button LED also changes color to indicate the state of the monitored line. The default LED color and pattern for
                              the states are:

No message: solid green

New messages: solid red

Urgent messages: solid red

Registration Failed: solid amber

To customize the LED behaviour, contact your administrator.

### Access Monitored Voicemail Account Messages

#### Before you begin

Your administrator must configure either a line key on the phone or an expansion module button to monitor a voicemail account.

Your administrator must assign speed dial to the configured key.

There are new messages for the monitored voicemail account.

Step 1

Press the line key on the phone or the expansion module button .

You may be prompted to enter the monitored voicemail account ID and PIN.

Step 2

Follow the voice prompts.

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Call preferences . |
| Step 3 | Enter your personal voicemail phone number in Voice mail . |
| Step 4 | Press Set . |

| Step 1 | Press Messages . |
|---|---|
| Step 2 | Do one of the following actions: 6800: Press Messages or Messages . 7800 and 8800: Press Messages . 7832 and 8832: Press Messages . |
| Step 3 | Follow the voice prompts. Note For details on voicemail features and PIN rules, see Set up and manage your voicemail . | Note | For details on voicemail features and PIN rules, see Set up and manage your voicemail . |
| Note | For details on voicemail features and PIN rules, see Set up and manage your voicemail . |

| Note | For details on voicemail features and PIN rules, see Set up and manage your voicemail . |
|---|---|

| Step 1 | In the screen, press the Audio softkey. |
|---|---|
| Step 2 | When prompted, enter your voicemail credentials. |

| Starting State | Event | LED
                                          						Status After Event | LED
                                          						Turn Off Criteria |
|---|---|---|---|
| No
                                          						Voicemail, No Missed Call | There is
                                          						no active call and a call is missed or a call is on hold and the call is
                                          						missed. | LED Off | - |
| No
                                          						Voicemail, No Missed Call | Voicemail comes in | LED On | User
                                          						calls the voicemail to retrieve a message. |
| Voicemail | There is
                                          						no active call and a call is missed or a call is on hold and the call is
                                          						missed. | LED On | User
                                          						calls the voicemail to retrieve a message. |
| Missed
                                          						Call | Voicemail comes in | LED On | User
                                          						calls the voicemail to retrieve a message. |
| No
                                          						Voicemail, No Missed Call | No event | LED Off | - |

| Starting State | Event | LED
                                             						Status After Event | LED
                                             						Turn Off Criteria |
|---|---|---|---|
| No
                                             						Voicemail, No Missed Call | There is
                                             						no active call and a call is missed or a call is on hold and the call is
                                             						missed. | LED On | User
                                             						interacts with the phone. |
| No
                                             						Voicemail, No Missed Call | Voicemail comes in | LED On | User
                                             						calls the voicemail to retrieve a message. |
| Voicemail | There is
                                             						no active call and a call is missed or a call is on hold and the call is
                                             						missed. | LED On | User
                                             						interacts with the phone and calls the voicemail to retrieve a message. |
| Missed
                                             						Call | Voicemail comes in | LED On | User
                                             						interacts with the phone and calls the voicemail to retrieve a message. |
| No
                                             						Voicemail, No Missed Call | No event | LED Off | - |

| Step 1 | Press the line key on the phone or the expansion module button . You may be prompted to enter the monitored voicemail account ID and PIN. |
|---|---|
| Step 2 | Follow the voice prompts. |