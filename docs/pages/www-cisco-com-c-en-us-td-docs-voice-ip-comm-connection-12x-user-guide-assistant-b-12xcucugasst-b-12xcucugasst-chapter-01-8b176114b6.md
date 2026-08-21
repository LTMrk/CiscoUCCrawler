---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-user-guide-assistant-b-12xcucugasst-b-12xcucugasst-chapter-01-8b176114b6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/assistant/b_12xcucugasst/b_12xcucugasst_chapter_0111.html
retrieved_at: 2026-08-21T07:55:14.845081+00:00
---

User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

# User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 12.x)

Updated: August 8, 2017

Chapter: Managing Your Personal Greetings

## Chapter: Managing Your Personal Greetings

# Managing Your Personal Greetings

## About Personal Greetings

Cisco Unity Connection allows you to record up to six personal greetings. You can enable as many greetings as you want, and
                           you can specify how long you want a greeting enabled.

With a multilingual system, you have the option of providing your personal greetings in multiple languages—your default language
                           and other languages available on your system. Note that you use the phone keypad to manage greetings in languages other than
                           your default language; you cannot use voice commands.

The six personal greetings and how they work are described below. Note that Connection plays the greetings that you enable
                           for the applicable situation, while some greetings override other greetings when they are enabled.

Alternate Greeting

Enable the alternate greeting to play during a specific time period when you want to indicate special circumstances, such
                           as when you are on vacation. (For example, “I will be out of the office until <date>.”) When it is enabled, the alternate
                           greeting overrides all other greetings.

Your Connection administrator specifies whether the system transfers callers to your greeting without ringing your phone,
                           whether callers are able to skip your greeting, and whether callers can leave you a message when your alternate greeting is
                           enabled. The Alternate Greeting page in the Messaging Assistant web tool indicates the caller options that your administrator
                           has enabled for you, if any. Note that caller options do not apply when an outside caller or another Connection user dials
                           your extension directly.

Other Connection users do not hear your alternate greeting when they send messages to you by phone. In addition to enabling
                                       your alternate greeting, consider changing your recorded name to include information that you are out of the office. Your
                                       recorded name plays when users address messages to you and when callers look you up in the directory.

The Cisco PCA Home page displays a reminder when you have your alternate greeting turned on. You can also configure Connection
                           to remind you when your alternate greeting is enabled after you sign in by phone.

Busy Greeting

Enable the busy greeting to indicate when you are on the phone. (For example, “I am currently on another line, please leave
                           a message.”) When it is enabled, the busy greeting overrides the standard, closed, and internal greetings when your phone
                           is busy.

Note that not all phone systems provide the support necessary for the Connection busy greeting to work. For assistance, talk
                           to your Connection administrator.

Internal Greeting

Enable the internal greeting to provide information that coworkers need to know. (For example, “I will be in conference room
                           B until noon today.”) When it is enabled, the internal greeting overrides the standard and off-hours greetings, and plays
                           only to callers within your organization when you do not answer your phone.

Note that not all phone systems provide the support necessary for the Connection internal greeting to work. For assistance,
                           talk to your Connection administrator.

Closed Greeting

Enable the closed greeting if you want Connection to play a special greeting during the nonbusiness hours that your Connection
                           administrator specified for your organization. (For example, “Sorry, I am not available to answer your call. Company office
                           hours are <times>.”) When it is enabled, the closed greeting overrides the standard greeting during nonbusiness hours.

Standard Greeting

The standard greeting plays during the business hours that your Connection administrator specified for your organization,
                           or in other situations when no other greeting is enabled. By design, the standard greeting cannot be disabled.

Holiday Greeting

Enable the holiday greeting if you want Connection to play a special greeting during a holiday. (For example, “Happy holiday.
                           I am not available to answer your call. I will be out of the office from <date> to <date>.”) When it is enabled, the holiday
                           greeting overrides the standard greeting during nonbusiness hours.

## Changing Personal
                        	 Greetings

When you turn on a
                              		  personal greeting, you specify how long you want it available for use. Cisco
                              		  Unity Connection plays the greeting in the applicable situation until the date
                              		  and time that you specified arrives, and then the greeting is automatically
                              		  turned off. For example, you can set your alternate greeting to stop playing on
                              		  the day that you return from a vacation.

You can also set a
                              		  greeting to play indefinitely, which is useful when you turn on a busy or a
                              		  closed greeting.

You can turn off a
                              		  greeting at any time. When a greeting is off, Connection no longer plays it,
                              		  although the recording is not erased.

With a
                                          			 multilingual system, you use the Messaging Assistant web tool to manage only
                                          			 the greetings in your default language. You manage greetings in other languages
                                          			 by phone, and your input style must be set to the phone keypad (Keys Only
                                          			 option).

In the
                                       			 Messaging Assistant, from the Greetings menu, select View
                                          				Greetings .

On the Greetings
                                       			 page, select the greeting you want to change.

To turn off the
                                       			 greeting, on the <Name> Greeting page, select Disabled , then skip to Step 5.

Or

To turn on the
                                          				greeting, select the applicable option:

Greeting
                                                   					 plays indefinitely.

Greeting
                                                   					 plays until the date and time you specify, when Connection automatically
                                                   					 disables the greeting.

In the Callers
                                       			 Hear section, select the applicable option:

To record
                                                   					 your own greeting, select Record on the available interface under the field
                                                   					 and record your greeting; when you finish recording, select Stop .

To use the
                                                   					 prerecorded system greeting.

To have
                                                   					 callers hear a tone to signal that they should leave a message

Select Save .

## Enabling Users to Playback Video Greetings

To allow the playback of video greetings for each user, enable the My Personal Recording option in the Callers See section.

For More information on video greetings, see the "Configuring Video Services" chapter in the User Moves, Adds, and Changes
                           Guide of Cisco Unity Connection.

You choose from one of the following sources to specify what callers see when a video greeting is enabled:

Unity Connection plays a video greeting that you have recorded.

Cisco Unity Connection prompts callers to wait for a tone before recording their video greeting. This check box is enabled
                                       only when Call Action is set to "Take Message" in After Greeting field. When the option is set to System Default Greeting,
                                       the checkbox remains disabled and checked.

You can disable a video greeting at any time. When a video greeting is disabled, Connection no longer plays it, although
                           the recording is not erased.

| Tip | Other Connection users do not hear your alternate greeting when they send messages to you by phone. In addition to enabling
                                       your alternate greeting, consider changing your recorded name to include information that you are out of the office. Your
                                       recorded name plays when users address messages to you and when callers look you up in the directory. |
|---|---|

| Note | With a
                                          			 multilingual system, you use the Messaging Assistant web tool to manage only
                                          			 the greetings in your default language. You manage greetings in other languages
                                          			 by phone, and your input style must be set to the phone keypad (Keys Only
                                          			 option). |
|---|---|

| Step 1 | In the
                                       			 Messaging Assistant, from the Greetings menu, select View
                                          				Greetings . |
|---|---|
| Step 2 | On the Greetings
                                       			 page, select the greeting you want to change. |
| Step 3 | To turn off the
                                       			 greeting, on the <Name> Greeting page, select Disabled , then skip to Step 5. Or To turn on the
                                          				greeting, select the applicable option: Option Description Enabled with No End Date and
                                                   					 Time Greeting
                                                   					 plays indefinitely. Enabled
                                                   					 Until Greeting
                                                   					 plays until the date and time you specify, when Connection automatically
                                                   					 disables the greeting. | Option | Description | Enabled with No End Date and
                                                   					 Time | Greeting
                                                   					 plays indefinitely. | Enabled
                                                   					 Until | Greeting
                                                   					 plays until the date and time you specify, when Connection automatically
                                                   					 disables the greeting. |
| Option | Description |
| Enabled with No End Date and
                                                   					 Time | Greeting
                                                   					 plays indefinitely. |
| Enabled
                                                   					 Until | Greeting
                                                   					 plays until the date and time you specify, when Connection automatically
                                                   					 disables the greeting. |
| Step 4 | In the Callers
                                       			 Hear section, select the applicable option: Option Description My Personal
                                                   					 Recording To record
                                                   					 your own greeting, select Record on the available interface under the field
                                                   					 and record your greeting; when you finish recording, select Stop . Note For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. System Default
                                                   					 Greeting To use the
                                                   					 prerecorded system greeting. Nothing To have
                                                   					 callers hear a tone to signal that they should leave a message | Option | Description | My Personal
                                                   					 Recording | To record
                                                   					 your own greeting, select Record on the available interface under the field
                                                   					 and record your greeting; when you finish recording, select Stop . Note For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. | Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. | System Default
                                                   					 Greeting | To use the
                                                   					 prerecorded system greeting. | Nothing | To have
                                                   					 callers hear a tone to signal that they should leave a message |
| Option | Description |
| My Personal
                                                   					 Recording | To record
                                                   					 your own greeting, select Record on the available interface under the field
                                                   					 and record your greeting; when you finish recording, select Stop . Note For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. | Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. |
| Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. |
| System Default
                                                   					 Greeting | To use the
                                                   					 prerecorded system greeting. |
| Nothing | To have
                                                   					 callers hear a tone to signal that they should leave a message |
| Step 5 | Select Save . |

| Option | Description |
|---|---|
| Enabled with No End Date and
                                                   					 Time | Greeting
                                                   					 plays indefinitely. |
| Enabled
                                                   					 Until | Greeting
                                                   					 plays until the date and time you specify, when Connection automatically
                                                   					 disables the greeting. |

| Option | Description |
|---|---|
| My Personal
                                                   					 Recording | To record
                                                   					 your own greeting, select Record on the available interface under the field
                                                   					 and record your greeting; when you finish recording, select Stop . Note For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. | Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. |
| Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. |
| System Default
                                                   					 Greeting | To use the
                                                   					 prerecorded system greeting. |
| Nothing | To have
                                                   					 callers hear a tone to signal that they should leave a message |

| Note | For release 11.0 (1) and earlier, you must select the
                                                               						option Play\Record under the field to load the Media Master. |
|---|---|

| My Personal Greeting | Unity Connection plays a video greeting that you have recorded. Note Recording a video greeting does not enable it. | Note | Recording a video greeting does not enable it. |
|---|---|---|---|
| Note | Recording a video greeting does not enable it. |
| Play the "Record Your Message at the Tone" Prompt | Cisco Unity Connection prompts callers to wait for a tone before recording their video greeting. This check box is enabled
                                       only when Call Action is set to "Take Message" in After Greeting field. When the option is set to System Default Greeting,
                                       the checkbox remains disabled and checked. |

| Note | Recording a video greeting does not enable it. |
|---|---|