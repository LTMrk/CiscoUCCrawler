---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-administration-guide-b-14cucsag-b-14cucsag-chapter-010011-html-e9e58ad475
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag/b_14cucsag_chapter_010011.html
retrieved_at: 2026-08-17T02:26:46.300625+00:00
---

System Administration Guide

# System Administration Guide

Updated: December 18, 2025

Chapter: Tools

## Chapter: Tools

# Tools

This chapter provides a brief descriptions and procedures for accessing different tools and utilities for administering Cisco Unity
                        Connection.

## Task Management Tool

The Task Definition page lists a variety of system maintenance and troubleshooting tasks that Unity Connection automatically
                           runs on a regular schedule. Tasks can be run at the same time as backups and anti-virus scans.

The default settings and schedules for each task are optimized for functionality and performance. You should not change the
                           default settings and schedules.

Caution

Some tasks are critical to Unity Connection functionality. Disabling or changing the frequency of critical tasks may adversely
                                       affect performance or cause Unity Connection to stop functioning.

### Viewing and
                           	 Managing Tasks Using Task Management Tool

Step 1

In Cisco Unity Connection Administration, expand Tools and select Task Management .

The Task Definitions page displays the Task Names.

Step 2

To view and manage tasks (For more information, see Help> This
                                          			 Page):

To view the Task Execution Results of any task, select the
                                                   					 applicable task. The Task Definition Basics page displays the Time Started and
                                                   					 Time Completed of the task.

To manage any task:

On the Task Definition Basics page of the applicable task,
                                                         						  select Edit> Task Schedules.

Enter the values of the required fields and select Save.

## Bulk
                        	 Administration Tool

The Bulk Administration Tool (BAT) allows you to create, edit,
                           		and delete multiple user accounts, contacts, distribution lists, distribution
                           		list members, unified messaging accounts, branches, or video service accounts
                           		by importing information contained in a comma separated value (CSV) file. In
                           		addition, it allows you to export information about users, contacts,
                           		distribution lists, or unified messaging accounts from Unity Connection to a
                           		CSV file.

When export operation is running using Bulk Administration Tool (BAT), make sure that there is no delete operation performed
                                       using any other tool or API.

CSV is a common text file format for moving data from one data
                           		store to another. For example, importing from a CSV file can be useful for
                           		transferring information from a corporate directory to Unity Connection.
                           		Transferring the information allows users with voice mailboxes to add corporate
                           		directory users who are not Unity Connection users to their address books and
                           		to then create call-routing rules based on calls from such contacts.

For small numbers of users up to a few hundred, it may be faster
                           		and easier to use the Import Users functionality to create Unity Connection
                           		users from an LDAP directory. See the Using Import Users and Synch Users Functionalities .

The information in this section is not applicable for updating
                                       		  user accounts, system distribution lists, or system distribution list members
                                       		  in Cisco Business Edition.

### Configuring the
                           	 Objects Using BAT

Step 1

In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool .

Step 2

On the Bulk Administration Tool page, in the Select Operation
                                          			 section, select the applicable option:

Create

Update

Delete

Export

Step 3

In the Select Object Type section, select the applicable option:

Users

Users With Mailbox

System Contacts

Distribution Lists

Distribution List Members

Unified Messaging Accounts

Branches

Video Service Accounts

Step 4

(When Creating Users or Users with Mailbox only): In the Override
                                          			 CSV Fields When Creating User Accounts section, select the applicable option.

Step 5

In the Select File section, in the CSV File field, enter the full
                                          			 path of the CSV input file.

Step 6

In the Failed Objects Filename field, enter the name of the failed
                                          			 objects report file. For example, enter errors.csv .

Step 7

Select Submit .

BAT begins configuring the select object and displays the
                                 		  summary page when the operation has completed.

If the operation results in any failures, you can immediately
                                 		  inspect the failed objects report file by selecting Download the Failed Objects
                                 		  File. For information about correcting errors, see the Correcting Errors Using Failed Objects File .

### Constructing Input
                           	 CSV Files

BAT supports only UTF-8 and UTF-16 character set encoding for
                              		the text in the CSV file.

To quickly construct an input CSV file, you can use BAT to
                              		export the applicable type of user, contact, system distribution list, system
                              		distribution list members, unified messaging accounts, or video service
                              		accounts, and use the resulting output CSV file as a template.

The following example shows a CSV file for creating voicemail
                              		users. To construct the file as shown in the example, you need to first export
                              		the voicemail users to a CSV file, remove the unwanted columns and data from
                              		the file, and then add the TemplateAlias column and the applicable data.

The DisplayName is an optional field and the data for this field
                                          		  is missing for several users.

Example CSV Input File for Creating Voicemail Users

Alias,DisplayName,FirstName,LastName,TemplateAlias,Extension,ListInDirectory

iwinkler,"Winkler,
                              		Ian",Ian,Winkler,VoiceMailUserTemplate,5321,1 jsmith,,John,Smith,VoiceMailUserTemplate,5126,1 cjones,"Jones,
                              		Cris",Cris,Jones,VoiceMailUserTemplate,5249,1 dalbert,,Dan,Albert,VoiceMailUserTemplate,5299,1 jlee,"Lee,
                              		Jane",Jane,Lee,VoiceMailUserTemplate,5324,1 jthompson,"Thompson,
                              		Jim",Jim,Thompson,VoiceMailUserTemplate,5029,1 swong,"Wong,
                              		Sara",Sara,Wong,VoiceMailUserTemplate,5260,1 rhunter,"Hunter,
                              		Russ",Russ,Hunter,VoiceMailUserTemplate,5229,1 cashmore,,Carol,Ashmore,VoiceMailUserTemplate,5403,1 lcarson,"Carson,
                              		Lauren",Lauren,Carson,VoiceMailUserTemplate,5999,1

Whether you edit an output CSV file or create a CSV file from
                              		scratch, use the following guidelines, along with the tables in the Required and Optional CSV Fields in BAT section to construct a valid input CSV file for use with the BAT:

The first row in the CSV file must contain column headings that
                                    			 identify the type of data in each column and the information in the subsequent
                                    			 rows must contain the data that you want to import.

Ensure that commas separate the data in each row in the CSV
                                    			 file, including the column headings in the first row. Do not use a tab, spaces,
                                    			 or a semicolon to separate values in the file.

Although the data must be arranged in the same order as the
                                    			 column heading, the order in which you arrange the columns is not important.

If the CSV file includes a column that you want BAT to ignore,
                                    			 use the column heading “Junk.”

If any data includes a space, quotes, or commas, specify it
                                    			 within quotes.

The data in the CSV file should not include double-quotes
                              		because it can cause problems with interactions with external servers. If the
                              		data does include double-quotes, place an additional double-quote next to each
                              		double-quote. For example, if the data is My “Spare Phone”, the entry must be
                              		My ““Spare Phone””.

Column headings are not case sensitive, but they must be spelled
                                    			 as indicated in the tables in the Required and Optional CSV Fields in BAT section. Columns that are designated not applicable (N/A) for an operation are
                                    			 ignored.

(Applicable only to Unity Connection configurations) For
                                    			 creating user accounts, most optional fields that are listed in the CSV field
                                    			 tables correspond to settings defined in a user template. For example, for
                                    			 voicemail users, the default template includes class of service (COS), call
                                    			 transfer, and message notification settings. When data for a particular user
                                    			 setting is not included in the CSV file, BAT uses settings in the user template
                                    			 that you specify in the required field TemplateAlias. For this reason, you
                                    			 should review the settings in the user template that you use to create the
                                    			 accounts before adding any of the optional column headers to your CSV file. If
                                    			 a value for an optional field is not included in the CSV file and if the
                                    			 template does not specify a default value, then the value for the field is not
                                    			 set.

If you specify an administrator template for TemplateAlias, the
                                    			 users do not have mailboxes

To explicitly set the value of a field to empty (or to null, if
                                    			 allowed), use the expression %null% for the value in the CSV file.

You should not include more than 5,000 records in an input CSV
                                    			 file.

### Correcting Errors
                           	 Using Failed Objects File

When you run BAT, it copies each record that it cannot process
                              		to a failed objects report file, along with the reason that the record was not
                              		processed correctly. For example, in the following CSV file, the first record
                              		includes an invalid entry for the Country field, and the second record
                              		specifies a template that is not a voicemail user template:

Alias, City, PostalCode, State, Country, TemplateAlias

Jsmith, Beverly Hills, 90210, Ca., United States,
                              		VoiceMailUserTemplate BRobertson, Seattle, 98121, WA, US, AdminUserTemplate

Using this file to create users with voice mailboxes produces
                              		the following failed objects file:

FailureReason, alias, city, postalcode, state, country,
                              		templatealias United States is invalid for column Country|, Jsmith, Beverly
                              		Hills, 90210, Ca., United States, VoiceMailUserTemplate Object not found or is
                              		not a template: Parameter = [@TemplateObjectId], Table =
                              		[vw_SubscriberTemplate], Column = [Alias,ObjectId]|, BRobertson, Seattle,
                              		98121, WA, US, AdminUserTemplate

The FailureReason column, which provides information about the
                              		invalid data, is added before the first column.

To correct errors, do the following procedure to edit the failed
                              		objects file, rename it, and use it as the input file when you re-run BAT.

Note that depending on the type of problem with the data in the
                              		CSV file, for each problem record, BAT may report multiple errors or only the
                              		first error encountered. Therefore, after you correct errors, BAT may detect
                              		additional errors in the same record when the data is processed again. Thus,
                              		you may need to repeat the correction process, which is running the tool and
                              		correcting an error, several times to find and correct all errors.

### Correcting Errors
                           	 Using the Failed Objects File

Step 1

If the Bulk Administration Tool operation results in any
                                          			 failures, you can immediately inspect the failed objects report file by
                                          			 selecting Download the Failed Objects File.

Step 2

Open the file and correct all problems with the data, as
                                          			 indicated by the information in the FailureReason column for each record.

Step 3

Remove the FailureReason column or change the heading to “junk.”

Step 4

Save the file as a CSV file with a new name after editing the
                                          			 data.

Step 5

Run BAT again with the CSV file that you saved in Step 4 as the
                                          			 input file.

Each time that you run BAT, the failed objects file is
                                                         				  overwritten (unless you specify a new name for the file each time you run the
                                                         				  tool).

Step 6

Repeat this procedure until all records are processed without
                                          			 error.

If you have navigated away from the Bulk Administration Tool
                                                         				  page, you can go back and select the Display Last Operation button to bring up
                                                         				  a download link for the output file from the previous operation. If you need a
                                                         				  failed objects file from more than one previous operation, you can use the
                                                         				  Command Line Interface (CLI) command “file view activelog cuc/<filename>”
                                                         				  to view failed object files. For more information on using CLI commands, see
                                                         				  the applicable Cisco Unified Communications Operating System Administration
                                                         				  Guide for Cisco Unity Connection. The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .

## Custom Keypad Mapping Tool

The Custom Keypad Mapping tool allows you to edit the key mappings that are associated with the Custom Keypad Mapping conversations.
                           Within each of these conversations—which are assigned to individual users or user templates on the Phone Menu page in Cisco Unity
                           Connection Administration—there are eight different menus that can be customized. Changing keypad mappings using this tool
                           does not affect any of the other Unity Connection conversation versions.

You can assign any one-, two-, or three-key sequence to any defined option for the Main menu, the Message Playback menu (the
                           message header, body and footer can be mapped separately), the After Message menu, the Settings menu, the Message Settings
                           menu, and the Preferences menu. You can customize which options are voiced in each menu and the order in which they are offered.

### Using the Custom
                           	 Keypad Mapping Tool

The Custom Keypad Mapping tool is divided into eight tabs
                                 		  that represent eight different conversation menus that can be customized. On
                                 		  each of these menu tabs you can:

Customize which key or keys are assigned to each menu option.
                                       				Leaving a key assignment blank disables that option for the menu.

Configure whether the option is voiced in the menu. This allows
                                       				you to assign a key or keys to an option but not have it presented verbally in
                                       				the menu. The option would still be enabled for that menu and Unity Connection
                                       				would respond appropriately if the assigned key is pressed, but the user would
                                       				not hear the option in the menu.

Configure the order in which
                                       				the menu items are offered to users. This is done by selecting the radio button
                                       				of the row that you want to reorder and then using either the Up or Down arrows
                                       				or the Move To button to arrange the menu items. The order in which the options
                                       				appear in the tool is the order in which they are presented to the user by
                                       				phone regardless of which keys are mapped to the options

Step 1

In Cisco Unity Connection Administration, expand Tools and select Custom Keypad Mapping.

Step 2

On the Search Custom Keypad Mappings page, select the applicable
                                          			 custom keypad mapping conversation.

Unity Connection supports six Custom Keypad Mappings.

Step 3

On the Edit Custom Keypad Mapping page, select the applicable
                                          			 tab to select the menu for which you would like to change key assignments.

Step 4

Change key assignments as applicable. (For guidelines on allowed
                                          			 entries, see the Guidelines for Assigning Keys to Menu Options .)

Step 5

Select Save.

When changes are saved, all new calls that use this conversation
                                             				follow the new key mapping settings.

Step 6

Repeat Step 3 through Step 5 for each menu that you want to
                                          			 customize.

#### Guidelines for Assigning Keys to Menu Options

The only characters allowed are: 0 – 9, *, # or blank.

A maximum of 3 digits is allowed for each menu option.

Duplicate key entries are not allowed for any unique menu. (For example, you cannot map the “1” key to both Hear New Messages
                                       and Send a Message in the Main menu. However, you can map the “1” key to Hear New Messages in the Main menu and also to Greetings
                                       in the Settings menu.)

Leaving a key assignment blank disables that option for the menu.

When you leave a key assignment blank, uncheck the Option Voiced in Menu check box.

When changes are saved, all new calls that use the conversation follow the new key mapping settings.

#### Setting a Keypad
                              	 Mapping to Match an Existing Conversation Mapping

You can change the key mappings
                                    		  for all menus to match that of an existing conversation. For example, you can
                                    		  have all of the key mappings for a selected custom keypad mapping replaced with
                                    		  the mappings of Optional Conversation 1. This can be useful if you want to make
                                    		  a small number of changes to an existing conversation and do not want to
                                    		  manually remap every option.

Step 1

In Cisco Unity Connection Administration, expand Tools and select Custom Keypad Mapping .

Step 2

On the Search Custom Keypad Mappings page, select the applicable
                                             			 custom keypad mapping conversation.

Step 3

On any tab of the Edit Custom Keypad Mapping page, in the Reset
                                             			 Mappings on All Tabs To list, select the conversation that you want to use and
                                             			 select Reset.

Step 4

When asked to confirm that you want to replace all key mappings
                                             			 with those of the selected conversation before continuing, select OK.

### Conversation Menus in Custom Keypad Mapping Tool

The Custom Keypad Mapping tool is divided into eight tabs that represent eight different conversation menus that can be customized.
                              The Message Playback menu is represented on three tabs because the messages contain three distinct parts: the message header,
                              the message body, and the message footer. The options on these three tabs are identical, but you may want to map different
                              options to different keys for certain parts.

#### Main Menu
                              	 Tab

The Main menu is what users hear immediately after they sign in
                                    		  and hear their message counts (if applicable).

See the table for a list of options that can be mapped.

Option

Description

Play New Messages

Takes users to the new (unread) message stack.

Send a Message

Takes users to the Send Message menu.

Review Old Messages

Takes users to the saved message stack. If applicable, users are
                                                					 also offered an opportunity to review deleted messages.

Change Setup Options

Takes users to the Settings menu where they can configure
                                                					 settings for greetings, transfer rules, and alternate contact numbers, and
                                                					 access their message settings and preferences.

Find Messages

Takes users to the Message Locator feature where they can search
                                                					 for new messages by the calling number or name of the sender.

This option is offered only when the Finding Messages With
                                                					 Message Locator feature is enabled for each user on the Phone Menu page.

List Meetings

Lists the time, meeting organizer, and subject for all current
                                                					 and upcoming meetings.

For Cisco Unified MeetingPlace and Cisco Unified MeetingPlace
                                                					 Express meetings, the user is offered the option to join current meetings.

Integrations with Cisco Unified MeetingPlace Express are not
                                                            						supported in Unity Connection.

Play External Messages

Provides the count of messages that are stored on an external
                                                					 message store.

The user is offered the option to listen to these messages.

Manage Call Handler Greetings

Allows users to access the Greetings Administrator conversation
                                                					 to change greetings for call handlers that have been assigned an extension.

Users who are assigned to the Greetings Administrator role on
                                                					 the Edit Roles page can change the greetings for any system call handler.

Users who are not assigned to the Greetings Administrator role
                                                					 can change the greetings only for call handlers that they own.

Call a Number

Allows users to access the User System Transfer conversation and
                                                					 dial any number that is allowed by their transfer restriction table.

Manage Broadcast Messages

Allows users to access the Broadcast Message Administration
                                                					 conversation.

This option is offered only when the Send or Update Broadcast
                                                					 Messages setting is configured for each user on the Send Message Settings page.

Repeat Menu Options

Plays the Main menu again.

Help

Plays the Main menu Help.

Cancel or Back Up

Exits the user mailbox.

By default, when users exit their mailboxes they are sent to the
                                                					 Opening Greeting call handler. However, you can customize the exit behavior by
                                                					 changing the When Exiting the Conversation setting on the Phone Menu page for
                                                					 each user.

Switch Between Using the Phone Keypad and Using Voice Commands

Allows users to toggle between the touchtone and
                                                					 voice-recognition conversations:

When users are listening to the touchtone conversation, and
                                                      						  press the applicable keys, they are immediately switched to the
                                                      						  voice-recognition conversation.

When users are listening to the voice-recognition conversation,
                                                      						  and press the applicable keys, they are immediately switched to the touchtone
                                                      						  conversation.

Note that the toggle persists until the user toggles back, or
                                                					 until the end of the call.

In case of a video call, the toggle key is not supported as
                                                            						Unity Connection 10.0(1) and later always plays touchtone conversation.

Change Alternate Greeting

Allows users to change alternate greetings by activating and
                                                					 re-recording.

In case of a video call, when users are listening to the main
                                                					 menu options and press the applicable key, Unity Connection plays your
                                                					 alternate video greeting and asks you to re-record your alternate greeting. For
                                                					 more details on enabling alternate greetings for each user, see the Task List for Configuring Video Messaging section.

#### Message Playback
                              	 Menu Tabs

Message Playback Menu tabs include Message Header, Message Body,
                                    		  and Message Footer tabs that you can use to customize the conversation
                                    		  settings, such as defining the speed and volume of the message header via TUI.
                                    		  When a message is played in the Unity Connection user conversation, there are
                                    		  three separate parts: the header, the body, and the footer. By default, the
                                    		  message header contains the message number and the sender information. The
                                    		  message body is the actual recording of the message. The message footer is the
                                    		  time stamp.

The contents of the header and footer sections can be modified
                                    		  on the Playback Message Settings page. For example, the message number, the
                                    		  sender information, the sender extension, and the time stamp can be added or
                                    		  removed from the header. These settings are controlled by the check boxes under
                                    		  the “Before Playing Each Message, Play” section on the Playback Message
                                    		  Settings page. For the message footer, you have the option of playing the time
                                    		  stamp after the message; you can exclude it altogether or have it played as
                                    		  part of the header. This option is controlled with the check box under the
                                    		  “After Playing Each Message, Play” section on the Playback Message Settings
                                    		  page. If you choose not to play the time stamp after the message, the effect is
                                    		  to have no footer to the message. In Unity Connection, the “After Playing Each
                                    		  Message, Play” section now includes the sender information, extension or ANI,
                                    		  and the message number, in addition to the time the message was sent and
                                    		  message duration.

The Custom Keypad Mapping tool includes separate tabs for each
                                    		  part of the message. As a best practice, you should map the same keys to each
                                    		  option for all three parts. However, in some cases it may be useful to map the
                                    		  same key to different actions. For example, during the message header you might
                                    		  want to press the “1” key to skip to the start of the message body, and during
                                    		  the message body press the “1” key to skip to the message footer.

The same message playback key mappings are used when listening
                                    		  to new messages, saved messages, and deleted messages, rather than separate
                                    		  mappings for each message stack. Keep this in mind as you are deciding on key
                                    		  mapping preferences, particularly for options such as marking messages as new
                                    		  (unread) or saved (read).

Message playback options are not voiced in a menu format by
                                    		  phone, but they are listed if the user presses the key that is mapped to the
                                    		  Help option. The Custom Keypad Mapping tool allows you to configure which items
                                    		  are voiced in the Help.

See the below table for a list of options that can be mapped.

Option

Description

Repeat Message

Jumps to the beginning of the header portion of the message.

Save

Skips to the next message and marks the current message as
                                                					 saved.

Delete

Deletes the message that is currently being played.

The user class of service determines whether the message is
                                                					 moved to the deleted items folder or is deleted permanently.

Slow Playback

Slows down the message that is currently being played. Pressing
                                                					 the mapped key slows the message playback by 50 percent.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user.

Fast Playback

Speeds up the message that is currently being played. Pressing
                                                					 the mapped key speeds the message playback by 50 percent. Pressing the key
                                                					 again speeds the message playback by 100 percent.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user.

Reset Speed to Default

Resets the speed of the message that is currently being played
                                                					 to the default message playback speed setting for the user.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user.

Change Volume

Cycles the volume of the message that is currently being played
                                                					 through three volume levels: normal, loud, and quiet.If the Save Speed and
                                                					 Volume Changes Made by User setting is enabled on the System Settings >
                                                					 Advanced > Conversation Configuration page, the last change made to playback
                                                					 volume is saved as the default playback volume for the user.

Reset Volume to Default

Resets the volume of the message that is currently being played
                                                					 to the default message playback volume setting for the user.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user.

Quieter Playback

Decreases the volume of the message that is currently being
                                                					 played.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user.

Louder Playback

Increases the volume of the message that is currently being
                                                					 played.

If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user.

Pause/Resume

Pauses playback of the message, or resumes playback when the
                                                					 message is already paused.

Rewind

Jumps backward in the message that is currently being played.

By default, the message rewinds five seconds. You can adjust the
                                                					 rewind time on the Playback Message Settings page.

Fast-Forward

Jumps forward in the message that is currently being played.

By default, the message fast-forwards five seconds. You can
                                                					 adjust the fast-forward time on the Playback Message Settings page.

Skip to After Message Menu

Jumps directly to the After Message menu.

Skip Message, Save As Is

Skips to the next message in the stack and leaves the message in
                                                					 the state it was in. When a new message is skipped, it is saved as unread; when
                                                					 a saved message is skipped, it remains saved; and when a deleted message is
                                                					 skipped, it remains deleted.

Save as New

Skips to the next message in the stack and marks the message as
                                                					 new. When this option is selected, if a user skips messages when listening to
                                                					 saved or deleted messages, the messages are marked as unread and are moved to
                                                					 the new message stack.

Play Message By Number

Asks the user to enter the number of a message in the current
                                                					 stack (new, saved, or deleted messages) and then takes the user directly to
                                                					 that message. For users who have large numbers of messages, this is a useful
                                                					 way to jump ahead or back in the stacks.

This option is offered only when the Enable Go to Message
                                                					 setting is enabled on the System Settings > Advanced > Conversation page.

Go to Previous Message

Takes the user to the previous message in the stack.

Go to Next Message

Takes the user to the next message in the stack. The message the
                                                					 user was listening to is left in the state it was in (new, saved, or deleted).
                                                					 Go to Next Message functions the same as the Skip Message, Save As Is option.

Cancel or Back Up

Terminates message playback and goes up a menu level. Users who
                                                					 are listening to new or saved messages go to the Main menu. Users who are
                                                					 listening to deleted messages go to the Deleted Message Option menu.

Reply

Replies to the sender of the message. Only the sender receives
                                                					 the reply. Other recipients of the original message do not receive the reply.

This option is available only when the message is from another
                                                					 user; users cannot reply to outside caller messages.

Reply to All

Replies to all recipients of the message.

Call the Sender

Terminates message playback, signs users out of their mailboxes,
                                                					 and transfers users to the person who left the message. This feature is also
                                                					 known as Live Reply. This key option is used to return calls to both users and
                                                					 unidentified callers.

This option is available only when the user is assigned to a
                                                					 class of service that has enabled either the Users Can Reply to Messages from
                                                					 Other Users by Calling Them or the Users Can Reply to Messages from
                                                					 Unidentified Callers by Calling Them setting.

Forward Message

Allows the user to forward the message to another user or
                                                					 distribution list.

Forward Original Message

Forwards the original voice message and removes any forwarded
                                                					 introductions that may have been added to the message by previous forwards.

Skip to End

Jumps to the beginning of the message footer.

When the After Playing Each Message, Play options are not
                                                					 enabled for the user on the Playback Message Settings page, these options
                                                					 effectively skips to the end of the message and goes directly to the After
                                                					 Message menu.

Replay Message

Jumps to the beginning of the message body, effectively
                                                					 repeating the message. If you assign a key to this option for the message
                                                					 header, it allows users to skip the header and jump right to the message.

Play Message Properties

Plays the properties of the message that is currently being
                                                					 played. This includes the sender information (including ANI if it is provided
                                                					 for outside callers) and the time that the message was sent.

Operator

Signs users out of their mailboxes and sends them to the
                                                					 Operator call handler. The message is left in the state that it was in.

Go to First Message

Jumps to the first message of the message stack. Unity
                                                					 Connection plays the “First message” prompt as an audible cue to the user.

Go to Last Message

Jumps to the last message of the message stack. Unity Connection
                                                					 plays the “Last message” prompt as an audible cue to the user.

List Message Recipients

Lists all recipients of the current message.

Toggle Urgency Flag

Toggles the priority flag on a received message between urgent
                                                					 and normal.

Users who want to identify the high-priority messages among all
                                                					 of their received messages may be interested in this functionality. By default,
                                                					 Unity Connection plays messages that are marked urgent first.

Send to Fax Machine for Printing

Sends the message to a fax machine. This option is available for
                                                					 fax messages and any message that has an attachment that can be sent to a fax
                                                					 machine.

This option is available only when the fax is configured as an
                                                					 external service for the user.

Help

Plays Help for all of the options that are mapped to a key, and
                                                					 for which the Option Voiced in Help check box is checked.

Play Message Attachments

Describes the files that are attached to the message. Files in
                                                					 compatible formats are played or read.

#### After Message Menu
                              	 Tab

The After Message menu plays after the user has listened to a
                                    		  message.

See the below table for a list of options that can be mapped.

Option

Description

Repeat Message

Plays the message again, starting with the header.

Save

Marks the message as saved (read) and moves to the next message
                                                					 in the stack. When the user is listening to a deleted message, this option
                                                					 moves the message to the saved message stack.

Delete

Deletes the message that is currently being played.

The user class of service determines whether the message is
                                                					 moved to the deleted items folder or is deleted permanently.

Reply

Replies to the sender of the message. Only the sender receives
                                                					 the reply; other recipients of the original message do not receive the reply.

This option is available only when the message is from another
                                                					 user; users cannot reply to outside caller messages.

Forward Message

Allows the user to forward the message to another user or
                                                					 distribution list.

Forward Original Message

Forwards the original voice message and removes any forwarded
                                                					 introductions that may have been added to the message by previous forwards.

Save as New

Marks the message as new (unread) and moves to the next message
                                                					 in the stack. When the user is listening to a saved or deleted message, this
                                                					 option moves the message to the new message stack.

Rewind

Jumps backward into the message.

By default, the message rewinds five seconds. You can adjust the
                                                					 rewind time on the Playback Message Settings page.

Send to Fax Machine for Printing

Sends the message to a fax machine. This option is available for
                                                					 fax messages and any message that has an attachment that can be sent to a fax
                                                					 machine.

This option is available only when fax is configured as an
                                                					 external service for the user.

Play Message Properties

Plays the properties of the current message. This includes the
                                                					 sender information (including ANI if it is provided for outside callers) and
                                                					 the time that the message was sent.

Cancel or Back Up

Exits the After Message menu and goes up a menu level. Users who
                                                					 are listening to new or saved messages go to the Main menu. Users who are
                                                					 listening to deleted messages go to the Deleted Message Option menu.

Help

Plays the After Message menu Help.

Operator

Signs users out of their mailboxes and sends them to the
                                                					 operator call handler. The message is left in the state it was in.

Play Message Attachments

Describes the files that are attached to the message. Files in
                                                					 compatible formats are played or read.

Play Message By Number

Asks the user to enter the number of a message in the current
                                                					 stack (new, saved, or deleted messages) and then takes the user directly to
                                                					 that message. For users who have large numbers of messages, this is a useful
                                                					 way to jump ahead or back in the stacks.

This option is available only when the Enable Go to Message
                                                					 setting is enabled on the System Settings > Advanced > Conversations
                                                					 page.

Go to Previous Message

Takes the user to the previous message in the stack.

Go to Next Message

Takes the user to the next message in the stack. The message the
                                                					 user was listening to is left in the state that it was in (new, saved, or
                                                					 deleted). Go to Next Message functions the same as the Skip Message, Save As Is
                                                					 option.

Save As Is

Goes to the next message in the stack and leaves the message in
                                                					 the state that it was in. New messages are saved as unread; saved messages
                                                					 remain saved; and deleted messages remain deleted.

Go to First Message

Jumps to the first message of the message stack. Unity
                                                					 Connection plays the “First message” prompt as an audible cue to the user.

Go to Last Message

Jumps to the last message of the message stack. Unity Connection
                                                					 plays the “Last message” prompt as an audible cue to the user.

Toggle Urgency Flag

Toggles the priority flag on a received message between urgent
                                                					 and normal.

Users who want to identify the high-priority messages among all
                                                					 of their received messages may be interested in this functionality. By default,
                                                					 Unity Connection plays messages that are marked urgent first.

Call the Sender

Terminates message playback, signs users out of their mailboxes,
                                                					 and transfers users to the person who left the message. This feature is also
                                                					 known as Live Reply. This key option is used to return calls to both other
                                                					 users and unidentified callers.

This option is available only when the user is assigned to a
                                                					 class of service that has enabled either the Users Can Reply to Messages from
                                                					 Other Users by Calling Them or the Users Can Reply to Messages from
                                                					 Unidentified Callers by Calling Them setting.

Skip Message, Save As Is

Skips to the next message in the stack and leaves the message in
                                                					 the state it was in. When a new message is skipped, it is saved as unread; when
                                                					 a saved message is skipped, it remains saved; and when a deleted message is
                                                					 skipped, it remains deleted.

List Message Recipients

Lists all recipients of the current message.

Reply to All

Replies to all recipients of the message.

#### Settings Menu
                              	 Tab

The Settings menu is what users hear when they choose Change
                                    		  Setup Options from the Main menu. See the below table for a list of options
                                    		  that can be mapped.

Option

Description

Greetings

Allows users to edit their greetings.

Message Settings

Takes users to the Message Settings menu.

Preferences

Takes users to the Preferences menu.

Transfer Settings

Allows users to edit their transfer rules.

Alternate Contact Numbers

Allows users to change their alternate contact phone numbers.

This option is available for a user only when an administrator
                                                					 has configured one or more caller input keys to transfer to an alternate
                                                					 contact number on the user Edit Caller Input page.

Repeat Menu

Plays the Settings menu again.

Help

Plays the Settings menu Help.

Cancel or Back Up

Exits the Settings menu and goes up a menu level to the Main
                                                					 menu.

Change Alternate Greeting

Allows users to change alternate greetings by activating and
                                                					 re-recording.

In case of a video call, when users are listening to the main
                                                					 menu options and press the applicable key, Unity Connection plays your
                                                					 alternate video greeting and asks you to re-record your alternate greeting.

#### Message Settings
                              	 Menu Tab

The Message Settings menu is what users hear when they choose
                                    		  Message Settings from the Settings menu.

See the below table for a list of options that can be mapped.

Option

Description

Message Notification

Allows users to edit the settings for their message notification
                                                					 devices.

Fax Delivery

Allows users to change the phone number of the fax machine to
                                                					 which they can send faxes for printing.

Menu Style

Allows users to switch between the full or brief menu styles.

Private Lists

Allows users to edit their private lists.

Addressing Priority List

Allows users to review and add or remove names from their
                                                					 addressing priority list.

Repeat Menu

Plays the Message Settings menu again.

Help

Plays the Message Settings menu Help.

Cancel or Back Up

Exits the Message Settings menu and goes up a menu level to the
                                                					 Settings menu.

#### Preferences Menu
                              	 Tab

The Preferences menu is what users hear when they choose
                                    		  Preferences from the Settings menu.

See the below table for a list of options that can be mapped.

Option

Description

Change Phone Password

Allows users to edit their phone PINs.

This option is not available for a user when the User Cannot
                                                					 Change check box is checked on the user Edit Password Settings page.

Change Recorded Name

Allows users to record names.

This option is available only when the user is assigned to a
                                                					 class of service that has enabled the Allow Recording of Name option.

Change Directory Listing

Allows users to choose whether or not they want to be listed in
                                                					 the directory.

This option is available only when the user is assigned to a
                                                					 class of service that has enabled the Allow Users to Choose to Be Listed in the
                                                					 Directory option.

Edit User-Defined Alternate Extensions

Allows users to list and delete their alternate extensions. Also
                                                					 allows users to add the current number they are calling from as an alternate
                                                					 extension (if it is not already an alternate extension and does not match a
                                                					 blocked pattern in the User-Defined or Automatically-Added Alternate Extensions
                                                					 restriction table).

Repeat Menu

Plays the Preferences menu again.

Help

Plays the Preferences menu Help.

Cancel or Back Up

Exits the Preferences menu and goes up a menu level to the
                                                					 Settings menu.

### Documenting Your
                           	 Keymap

The Wallet
                              		Card wizard is available for creating a PDF file of a wallet card based on your
                              		custom keypad mappings. For details, see the Wallet Card Wizard .

## Migrate
                        	 Utilities

The Migrate Utilities tool includes Migrate Users and Migrate Messages to migrate users and messages respectively, from Cisco Unity
                           9.x or later to Unity Connection 15. However, you should use the Cisco Unified Backup and Restore Application Suite (COBRAS)
                           tool to quickly migrate huge amount of data as COBRAS does not require you to configure a secure shell (SSH) server application.

You can only migrate messages if you have first migrated the
                                       		  user data.

### Accessing the
                           	 Migrate Utilities

For a task list that enumerates the steps for migrating from Cisco Unity to Unity Connection 15 either using COBRAS or Migrate
                                 Messages and Migrate Users utilities, see the “Maintaining Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

Step 1

In Cisco Unity Connection Administration, expand Tools and select Migration Utilities.

Step 2

Expand Migration Utilities , then select the applicable
                                          			 option ( Migrate Users > or > Migrate
                                                				  Messages ).

## Grammar Statistics Tool

The Grammar Statistics tool shows information about all of the dynamic name grammars that are used by the Unity Connection
                           voice-recognition conversation to match caller utterances to the names of objects on the system (for example, usernames and
                           alternate names, distribution list names, and so on). When administrators add or change names on the Unity Connection system,
                           the names are not recognized by the voice-recognition conversation until they are compiled in the grammars.

For each name grammar, the tool displays information such as the finish time of the last grammar recompilation, the total
                           number of unique items in the grammar, whether there are updates pending to the grammar, and whether the grammar is currently
                           in the process of being recompiled.

By default, Unity Connection recompiles grammars when administrators add named objects or change object names on the system
                           (unless a bulk operation is in progress, in which case Unity Connection waits ten minutes for the operation to complete before
                           recompiling the grammars), or when there are more than five changes requested in a minute. If the grammars have grown to the
                           point where the name grammar recompilation process is affecting the performance of your Unity Connection server during busy
                           periods, you can edit the default Voice Recognition Update Schedule (under System Settings > Schedules in Cisco Unity Connection
                           Administration) to limit the times and days when the Unity Connection voice-recognition transport utility can automatically
                           rebuild the voice-recognition name grammars. By default, all the days and times are active for this schedule; if you edit
                           the schedule but want to override the schedule while it is inactive and force an immediate recompilation of all grammars,
                           or if you want to force recompilation during the ten minute wait period after a bulk operation has been initiated, you can
                           select the Rebuild Grammars button on the Grammar Statistics tool.

## SMTP Address Search

The SMTP Address Search tool allows you to search a particular object, such as a user or a distribution list, based on the
                           SMTP address of the object. For example, if there are two users with the same display name in different domains, you can search
                           the desired user by specifying the complete SMTP address.

## Show Dependency Results

The Show Dependency Results page provides a way to view the results of the most recent dependency search.

When database objects such as user accounts are referenced by other objects in Unity Connection (for example, if a user is
                           set to be a recipient of messages left in an interview handler, or if a call handler is set to transfer incoming calls to
                           a user phone), you cannot delete the referenced objects until you have changed settings on the dependent objects.

To determine the dependencies of an object that you want to delete, select the Show Dependencies option on the search page
                           for the object type. The option initiates a search for database objects that are dependent on the object you want to delete.
                           From the dependency search results, follow links to the dependent objects and reassign the dependencies. When all dependencies
                           have been reassigned, you can delete the object.

Some dependency searches can take several minutes, depending on the object being searched. While a search is in progress,
                           if you browse to another page, or your browser session times out, navigate to Tools > Show Dependency Results to view the
                           dependency search results.

## Other Administrative Tools

In addition to the tools that appear on Unity Connection Administration interface, Unity Connection provides the following
                           tools, which you can use to monitor system performance:

### Remote Database Administration Tools

A database proxy can be enabled to allow the use of some Windows-based remote database administration tools that are available
                              on the Cisco Unity Tools website ( http://ciscounitytools.com ), where updates to the utilities are frequently posted between Cisco Unity Connection releases.

You can sign up to be notified when the utilities posted on the Cisco Unity Tools website are updated. Go to http://ciscounitytools.com and select Sign Up Here.

#### Enabling Database Access for Remote Administration Tools

In order to use the remote tools, you must first enable remote database access. As opening up database access for remote administration
                                 tools can introduce a security risk to your system, several layers of security are involved with enabling access:

The username and password of a user with the Remote Administrator role is required to run remote tools.

The Unity Connection Database Proxy service is disabled by default.

##### Assigning the
                                 	 Remote Administrator Role to One or More Users

Step 1

In Cisco Unity Connection Administration, expand Users and
                                                			 select Users.

Step 2

On the Search Users page, find the applicable user account.

As a best practice, do not use the default system administrator
                                                               				  user account for remote access. Instead, use a different administrative user
                                                               				  account to avoid the default system administrator account become locked due to
                                                               				  too many failed authentication attempts.

Step 3

On the Edit User Basics page, in the Edit menu, select Roles.

Step 4

On the Edit Roles page, in the Available Roles field, select Remote Administrator , then select the Up arrow to
                                                			 move it into the Assigned Roles field.

Step 5

Select Save .

Step 6

Repeat Step 2 through Step 5 for each user who needs access to
                                                			 remote administration tools.

### Starting the
                           	 Database Proxy Service

Step 1

In Cisco Unity Connection Serviceability, expand Tools and
                                          			 select Service Management.

Step 2

In the Optional Services section, find the Unity Connection
                                          			 Database Proxy row and select Activate.

### Cisco Unified Backup and Restore Application Suite (COBRAS)

Cisco Unified Backup and Restore Application Suite (COBRAS) is the application you use to migrate data and messages from Unity
                              Connection 1.2 to 15. Download the latest version, and view training videos and Help at http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html .

Alternatively, you can use the Unity Connection Migrate Messages and Migrate Users utilities to migrate messages and user
                              data when you are migrating from Cisco Unity 4.0(4) and earlier and you cannot upgrade to Cisco Unity 4.0(5) or later for
                              some reason. For more information, see the “Migrate Utilities” section on page 19-17 .

Migration in a Tenant Partitioned environment using COBRAS tool allows the administrator to export the data from a non-partitioned
                                          Unity Connection system or a Tenant-Partitioned Unity Connection system. For more information on each scenario and on migration
                                          process using COBRAS tools, refer to http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html link.

For a task list that enumerates the steps for migrating from Cisco Unity or from Unity Connection 7.x to Unity Connection
                              15 either using COBRAS or Migrate Messages and Migrate Users utilities, see the “Backing Up and Restoring Cisco Unity Connection
                              Components” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Cisco Voice Technology Group Subscription Tool

You can use the Cisco Voice Technology Group Subscription tool to be notified by email of any Cisco Unity Connection software
                              updates. To subscribe, go to the Cisco Voice Technology Group Subscription Tool page at http://www.cisco.com/cgi-bin/Software/Newsbuilder/Builder/VOICE.cgi .

### Cisco Utilities Database Link for Informix (CUDLI)

The Cisco Utilities Database Link for Informix (CUDLI) tool allows you to navigate the Cisco Unity Connection database, learn
                              about the purpose of data in a particular table or column, and jump between referenced objects in the database. It also shows
                              stored procedures and includes a custom query builder.

Download the tool and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/CUDLI/CUDLI.html .

### Unity Connection User Data Dump (CUDD)

The Unity Connection User Data Dump (CUDD) allows you to export specific information about users to a file that can then be
                              viewed or imported into another application such as a database utility or Excel. When the data is exported, the tool automatically
                              creates a header row that lists the data type found in each column of the output, for ease of import into other programs.

Download the tool and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/UserDataDump/UserDataDump.html .

### Wallet Card Wizard

The Wallet Card wizard is available for creating a PDF file of a wallet card based on any of the Unity Connection conversations,
                              including custom keypad mappings. The templates in the wizard list frequently use menu options and shortcuts for managing
                              Unity Connection messages and user preferences by phone; the wizard fills in the applicable keys based on the conversation
                              that you specify. The resulting PDF is formatted as a wallet card that can be printed, then cut out and folded by users.

The wizard also allows you to customize technical support information and instructions for signing in to Unity Connection.
                              The Wallet Card wizard is a Windows-based remote database administration tool. Download the tool and view Help at http://www.ciscounitytools.com/Applications/CxN/WalletCardWizard/WalletCardWizard.html .

| Caution | Some tasks are critical to Unity Connection functionality. Disabling or changing the frequency of critical tasks may adversely
                                       affect performance or cause Unity Connection to stop functioning. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Task Management . | The Task Definitions page displays the Task Names. |
| Step 2 | To view and manage tasks (For more information, see Help> This
                                          			 Page): | To view the Task Execution Results of any task, select the
                                                   					 applicable task. The Task Definition Basics page displays the Time Started and
                                                   					 Time Completed of the task. To manage any task: On the Task Definition Basics page of the applicable task,
                                                         						  select Edit> Task Schedules. Enter the values of the required fields and select Save. |

| Note | When export operation is running using Bulk Administration Tool (BAT), make sure that there is no delete operation performed
                                       using any other tool or API. |
|---|---|

| Note | The information in this section is not applicable for updating
                                       		  user accounts, system distribution lists, or system distribution list members
                                       		  in Cisco Business Edition. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool . |
|---|---|
| Step 2 | On the Bulk Administration Tool page, in the Select Operation
                                          			 section, select the applicable option: Create Update Delete Export |
| Step 3 | In the Select Object Type section, select the applicable option: Users Users With Mailbox System Contacts Distribution Lists Distribution List Members Unified Messaging Accounts Branches Video Service Accounts |
| Step 4 | (When Creating Users or Users with Mailbox only): In the Override
                                          			 CSV Fields When Creating User Accounts section, select the applicable option. |
| Step 5 | In the Select File section, in the CSV File field, enter the full
                                          			 path of the CSV input file. Note If you are importing a CSV file that you created
                                                      				by exporting data from Unity Connection, you may need to manually create the
                                                      				ContactTemplateAlias column header, if applicable, and manually enter data, as
                                                      				this column header is not included in an export. | Note | If you are importing a CSV file that you created
                                                      				by exporting data from Unity Connection, you may need to manually create the
                                                      				ContactTemplateAlias column header, if applicable, and manually enter data, as
                                                      				this column header is not included in an export. |
| Note | If you are importing a CSV file that you created
                                                      				by exporting data from Unity Connection, you may need to manually create the
                                                      				ContactTemplateAlias column header, if applicable, and manually enter data, as
                                                      				this column header is not included in an export. |
| Step 6 | In the Failed Objects Filename field, enter the name of the failed
                                          			 objects report file. For example, enter errors.csv . |
| Step 7 | Select Submit . |

| Note | If you are importing a CSV file that you created
                                                      				by exporting data from Unity Connection, you may need to manually create the
                                                      				ContactTemplateAlias column header, if applicable, and manually enter data, as
                                                      				this column header is not included in an export. |
|---|---|

| Note | The DisplayName is an optional field and the data for this field
                                          		  is missing for several users. |
|---|---|

| Step 1 | If the Bulk Administration Tool operation results in any
                                          			 failures, you can immediately inspect the failed objects report file by
                                          			 selecting Download the Failed Objects File. |
|---|---|
| Step 2 | Open the file and correct all problems with the data, as
                                          			 indicated by the information in the FailureReason column for each record. |
| Step 3 | Remove the FailureReason column or change the heading to “junk.” |
| Step 4 | Save the file as a CSV file with a new name after editing the
                                          			 data. |
| Step 5 | Run BAT again with the CSV file that you saved in Step 4 as the
                                          			 input file. Note Each time that you run BAT, the failed objects file is
                                                         				  overwritten (unless you specify a new name for the file each time you run the
                                                         				  tool). | Note | Each time that you run BAT, the failed objects file is
                                                         				  overwritten (unless you specify a new name for the file each time you run the
                                                         				  tool). |
| Note | Each time that you run BAT, the failed objects file is
                                                         				  overwritten (unless you specify a new name for the file each time you run the
                                                         				  tool). |
| Step 6 | Repeat this procedure until all records are processed without
                                          			 error. Note If you have navigated away from the Bulk Administration Tool
                                                         				  page, you can go back and select the Display Last Operation button to bring up
                                                         				  a download link for the output file from the previous operation. If you need a
                                                         				  failed objects file from more than one previous operation, you can use the
                                                         				  Command Line Interface (CLI) command “file view activelog cuc/<filename>”
                                                         				  to view failed object files. For more information on using CLI commands, see
                                                         				  the applicable Cisco Unified Communications Operating System Administration
                                                         				  Guide for Cisco Unity Connection. The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . | Note | If you have navigated away from the Bulk Administration Tool
                                                         				  page, you can go back and select the Display Last Operation button to bring up
                                                         				  a download link for the output file from the previous operation. If you need a
                                                         				  failed objects file from more than one previous operation, you can use the
                                                         				  Command Line Interface (CLI) command “file view activelog cuc/<filename>”
                                                         				  to view failed object files. For more information on using CLI commands, see
                                                         				  the applicable Cisco Unified Communications Operating System Administration
                                                         				  Guide for Cisco Unity Connection. The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . |
| Note | If you have navigated away from the Bulk Administration Tool
                                                         				  page, you can go back and select the Display Last Operation button to bring up
                                                         				  a download link for the output file from the previous operation. If you need a
                                                         				  failed objects file from more than one previous operation, you can use the
                                                         				  Command Line Interface (CLI) command “file view activelog cuc/<filename>”
                                                         				  to view failed object files. For more information on using CLI commands, see
                                                         				  the applicable Cisco Unified Communications Operating System Administration
                                                         				  Guide for Cisco Unity Connection. The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . |

| Note | Each time that you run BAT, the failed objects file is
                                                         				  overwritten (unless you specify a new name for the file each time you run the
                                                         				  tool). |
|---|---|

| Note | If you have navigated away from the Bulk Administration Tool
                                                         				  page, you can go back and select the Display Last Operation button to bring up
                                                         				  a download link for the output file from the previous operation. If you need a
                                                         				  failed objects file from more than one previous operation, you can use the
                                                         				  Command Line Interface (CLI) command “file view activelog cuc/<filename>”
                                                         				  to view failed object files. For more information on using CLI commands, see
                                                         				  the applicable Cisco Unified Communications Operating System Administration
                                                         				  Guide for Cisco Unity Connection. The guide is available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Custom Keypad Mapping. |
|---|---|
| Step 2 | On the Search Custom Keypad Mappings page, select the applicable
                                          			 custom keypad mapping conversation. Note Unity Connection supports six Custom Keypad Mappings. | Note | Unity Connection supports six Custom Keypad Mappings. |
| Note | Unity Connection supports six Custom Keypad Mappings. |
| Step 3 | On the Edit Custom Keypad Mapping page, select the applicable
                                          			 tab to select the menu for which you would like to change key assignments. |
| Step 4 | Change key assignments as applicable. (For guidelines on allowed
                                          			 entries, see the Guidelines for Assigning Keys to Menu Options .) |
| Step 5 | Select Save. When changes are saved, all new calls that use this conversation
                                             				follow the new key mapping settings. |
| Step 6 | Repeat Step 3 through Step 5 for each menu that you want to
                                          			 customize. |

| Note | Unity Connection supports six Custom Keypad Mappings. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Custom Keypad Mapping . |
|---|---|
| Step 2 | On the Search Custom Keypad Mappings page, select the applicable
                                             			 custom keypad mapping conversation. |
| Step 3 | On any tab of the Edit Custom Keypad Mapping page, in the Reset
                                             			 Mappings on All Tabs To list, select the conversation that you want to use and
                                             			 select Reset. |
| Step 4 | When asked to confirm that you want to replace all key mappings
                                             			 with those of the selected conversation before continuing, select OK. |

| Option | Description |
|---|---|
| Play New Messages | Takes users to the new (unread) message stack. |
| Send a Message | Takes users to the Send Message menu. |
| Review Old Messages | Takes users to the saved message stack. If applicable, users are
                                                					 also offered an opportunity to review deleted messages. |
| Change Setup Options | Takes users to the Settings menu where they can configure
                                                					 settings for greetings, transfer rules, and alternate contact numbers, and
                                                					 access their message settings and preferences. |
| Find Messages | Takes users to the Message Locator feature where they can search
                                                					 for new messages by the calling number or name of the sender. This option is offered only when the Finding Messages With
                                                					 Message Locator feature is enabled for each user on the Phone Menu page. |
| List Meetings | Lists the time, meeting organizer, and subject for all current
                                                					 and upcoming meetings. For Cisco Unified MeetingPlace and Cisco Unified MeetingPlace
                                                					 Express meetings, the user is offered the option to join current meetings. Note Integrations with Cisco Unified MeetingPlace Express are not
                                                            						supported in Unity Connection. | Note | Integrations with Cisco Unified MeetingPlace Express are not
                                                            						supported in Unity Connection. |
| Note | Integrations with Cisco Unified MeetingPlace Express are not
                                                            						supported in Unity Connection. |
| Play External Messages | Provides the count of messages that are stored on an external
                                                					 message store. The user is offered the option to listen to these messages. |
| Manage Call Handler Greetings | Allows users to access the Greetings Administrator conversation
                                                					 to change greetings for call handlers that have been assigned an extension. Users who are assigned to the Greetings Administrator role on
                                                					 the Edit Roles page can change the greetings for any system call handler. Users who are not assigned to the Greetings Administrator role
                                                					 can change the greetings only for call handlers that they own. |
| Call a Number | Allows users to access the User System Transfer conversation and
                                                					 dial any number that is allowed by their transfer restriction table. |
| Manage Broadcast Messages | Allows users to access the Broadcast Message Administration
                                                					 conversation. This option is offered only when the Send or Update Broadcast
                                                					 Messages setting is configured for each user on the Send Message Settings page. |
| Repeat Menu Options | Plays the Main menu again. |
| Help | Plays the Main menu Help. |
| Cancel or Back Up | Exits the user mailbox. By default, when users exit their mailboxes they are sent to the
                                                					 Opening Greeting call handler. However, you can customize the exit behavior by
                                                					 changing the When Exiting the Conversation setting on the Phone Menu page for
                                                					 each user. |
| Switch Between Using the Phone Keypad and Using Voice Commands | Allows users to toggle between the touchtone and
                                                					 voice-recognition conversations: When users are listening to the touchtone conversation, and
                                                      						  press the applicable keys, they are immediately switched to the
                                                      						  voice-recognition conversation. When users are listening to the voice-recognition conversation,
                                                      						  and press the applicable keys, they are immediately switched to the touchtone
                                                      						  conversation. Note that the toggle persists until the user toggles back, or
                                                					 until the end of the call. Note In case of a video call, the toggle key is not supported as
                                                            						Unity Connection 10.0(1) and later always plays touchtone conversation. | Note | In case of a video call, the toggle key is not supported as
                                                            						Unity Connection 10.0(1) and later always plays touchtone conversation. |
| Note | In case of a video call, the toggle key is not supported as
                                                            						Unity Connection 10.0(1) and later always plays touchtone conversation. |
| Change Alternate Greeting | Allows users to change alternate greetings by activating and
                                                					 re-recording. In case of a video call, when users are listening to the main
                                                					 menu options and press the applicable key, Unity Connection plays your
                                                					 alternate video greeting and asks you to re-record your alternate greeting. For
                                                					 more details on enabling alternate greetings for each user, see the Task List for Configuring Video Messaging section. |

| Note | Integrations with Cisco Unified MeetingPlace Express are not
                                                            						supported in Unity Connection. |
|---|---|

| Note | In case of a video call, the toggle key is not supported as
                                                            						Unity Connection 10.0(1) and later always plays touchtone conversation. |
|---|---|

| Option | Description |
|---|---|
| Repeat Message | Jumps to the beginning of the header portion of the message. |
| Save | Skips to the next message and marks the current message as
                                                					 saved. |
| Delete | Deletes the message that is currently being played. The user class of service determines whether the message is
                                                					 moved to the deleted items folder or is deleted permanently. |
| Slow Playback | Slows down the message that is currently being played. Pressing
                                                					 the mapped key slows the message playback by 50 percent. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Fast Playback | Speeds up the message that is currently being played. Pressing
                                                					 the mapped key speeds the message playback by 50 percent. Pressing the key
                                                					 again speeds the message playback by 100 percent. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Reset Speed to Default | Resets the speed of the message that is currently being played
                                                					 to the default message playback speed setting for the user. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
| Change Volume | Cycles the volume of the message that is currently being played
                                                					 through three volume levels: normal, loud, and quiet.If the Save Speed and
                                                					 Volume Changes Made by User setting is enabled on the System Settings >
                                                					 Advanced > Conversation Configuration page, the last change made to playback
                                                					 volume is saved as the default playback volume for the user. |
| Reset Volume to Default | Resets the volume of the message that is currently being played
                                                					 to the default message playback volume setting for the user. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Quieter Playback | Decreases the volume of the message that is currently being
                                                					 played. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Louder Playback | Increases the volume of the message that is currently being
                                                					 played. Note If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. | Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
| Pause/Resume | Pauses playback of the message, or resumes playback when the
                                                					 message is already paused. |
| Rewind | Jumps backward in the message that is currently being played. By default, the message rewinds five seconds. You can adjust the
                                                					 rewind time on the Playback Message Settings page. |
| Fast-Forward | Jumps forward in the message that is currently being played. By default, the message fast-forwards five seconds. You can
                                                					 adjust the fast-forward time on the Playback Message Settings page. |
| Skip to After Message Menu | Jumps directly to the After Message menu. |
| Skip Message, Save As Is | Skips to the next message in the stack and leaves the message in
                                                					 the state it was in. When a new message is skipped, it is saved as unread; when
                                                					 a saved message is skipped, it remains saved; and when a deleted message is
                                                					 skipped, it remains deleted. |
| Save as New | Skips to the next message in the stack and marks the message as
                                                					 new. When this option is selected, if a user skips messages when listening to
                                                					 saved or deleted messages, the messages are marked as unread and are moved to
                                                					 the new message stack. |
| Play Message By Number | Asks the user to enter the number of a message in the current
                                                					 stack (new, saved, or deleted messages) and then takes the user directly to
                                                					 that message. For users who have large numbers of messages, this is a useful
                                                					 way to jump ahead or back in the stacks. This option is offered only when the Enable Go to Message
                                                					 setting is enabled on the System Settings > Advanced > Conversation page. |
| Go to Previous Message | Takes the user to the previous message in the stack. |
| Go to Next Message | Takes the user to the next message in the stack. The message the
                                                					 user was listening to is left in the state it was in (new, saved, or deleted).
                                                					 Go to Next Message functions the same as the Skip Message, Save As Is option. |
| Cancel or Back Up | Terminates message playback and goes up a menu level. Users who
                                                					 are listening to new or saved messages go to the Main menu. Users who are
                                                					 listening to deleted messages go to the Deleted Message Option menu. |
| Reply | Replies to the sender of the message. Only the sender receives
                                                					 the reply. Other recipients of the original message do not receive the reply. This option is available only when the message is from another
                                                					 user; users cannot reply to outside caller messages. |
| Reply to All | Replies to all recipients of the message. |
| Call the Sender | Terminates message playback, signs users out of their mailboxes,
                                                					 and transfers users to the person who left the message. This feature is also
                                                					 known as Live Reply. This key option is used to return calls to both users and
                                                					 unidentified callers. This option is available only when the user is assigned to a
                                                					 class of service that has enabled either the Users Can Reply to Messages from
                                                					 Other Users by Calling Them or the Users Can Reply to Messages from
                                                					 Unidentified Callers by Calling Them setting. |
| Forward Message | Allows the user to forward the message to another user or
                                                					 distribution list. |
| Forward Original Message | Forwards the original voice message and removes any forwarded
                                                					 introductions that may have been added to the message by previous forwards. |
| Skip to End | Jumps to the beginning of the message footer. When the After Playing Each Message, Play options are not
                                                					 enabled for the user on the Playback Message Settings page, these options
                                                					 effectively skips to the end of the message and goes directly to the After
                                                					 Message menu. |
| Replay Message | Jumps to the beginning of the message body, effectively
                                                					 repeating the message. If you assign a key to this option for the message
                                                					 header, it allows users to skip the header and jump right to the message. |
| Play Message Properties | Plays the properties of the message that is currently being
                                                					 played. This includes the sender information (including ANI if it is provided
                                                					 for outside callers) and the time that the message was sent. |
| Operator | Signs users out of their mailboxes and sends them to the
                                                					 Operator call handler. The message is left in the state that it was in. |
| Go to First Message | Jumps to the first message of the message stack. Unity
                                                					 Connection plays the “First message” prompt as an audible cue to the user. |
| Go to Last Message | Jumps to the last message of the message stack. Unity Connection
                                                					 plays the “Last message” prompt as an audible cue to the user. |
| List Message Recipients | Lists all recipients of the current message. |
| Toggle Urgency Flag | Toggles the priority flag on a received message between urgent
                                                					 and normal. Users who want to identify the high-priority messages among all
                                                					 of their received messages may be interested in this functionality. By default,
                                                					 Unity Connection plays messages that are marked urgent first. |
| Send to Fax Machine for Printing | Sends the message to a fax machine. This option is available for
                                                					 fax messages and any message that has an attachment that can be sent to a fax
                                                					 machine. This option is available only when the fax is configured as an
                                                					 external service for the user. |
| Help | Plays Help for all of the options that are mapped to a key, and
                                                					 for which the Option Voiced in Help check box is checked. |
| Play Message Attachments | Describes the files that are attached to the message. Files in
                                                					 compatible formats are played or read. |

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
|---|---|

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
|---|---|

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback speed is saved as the default playback
                                                            						speed for the user. |
|---|---|

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
|---|---|

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
|---|---|

| Note | If the Save Speed and Volume Changes Made by User setting is
                                                            						enabled on the System Settings > Advanced > Conversation Configuration
                                                            						page, the last change made to playback volume is saved as the default playback
                                                            						volume for the user. |
|---|---|

| Option | Description |
|---|---|
| Repeat Message | Plays the message again, starting with the header. |
| Save | Marks the message as saved (read) and moves to the next message
                                                					 in the stack. When the user is listening to a deleted message, this option
                                                					 moves the message to the saved message stack. |
| Delete | Deletes the message that is currently being played. The user class of service determines whether the message is
                                                					 moved to the deleted items folder or is deleted permanently. |
| Reply | Replies to the sender of the message. Only the sender receives
                                                					 the reply; other recipients of the original message do not receive the reply. This option is available only when the message is from another
                                                					 user; users cannot reply to outside caller messages. |
| Forward Message | Allows the user to forward the message to another user or
                                                					 distribution list. |
| Forward Original Message | Forwards the original voice message and removes any forwarded
                                                					 introductions that may have been added to the message by previous forwards. |
| Save as New | Marks the message as new (unread) and moves to the next message
                                                					 in the stack. When the user is listening to a saved or deleted message, this
                                                					 option moves the message to the new message stack. |
| Rewind | Jumps backward into the message. By default, the message rewinds five seconds. You can adjust the
                                                					 rewind time on the Playback Message Settings page. |
| Send to Fax Machine for Printing | Sends the message to a fax machine. This option is available for
                                                					 fax messages and any message that has an attachment that can be sent to a fax
                                                					 machine. This option is available only when fax is configured as an
                                                					 external service for the user. |
| Play Message Properties | Plays the properties of the current message. This includes the
                                                					 sender information (including ANI if it is provided for outside callers) and
                                                					 the time that the message was sent. |
| Cancel or Back Up | Exits the After Message menu and goes up a menu level. Users who
                                                					 are listening to new or saved messages go to the Main menu. Users who are
                                                					 listening to deleted messages go to the Deleted Message Option menu. |
| Help | Plays the After Message menu Help. |
| Operator | Signs users out of their mailboxes and sends them to the
                                                					 operator call handler. The message is left in the state it was in. |
| Play Message Attachments | Describes the files that are attached to the message. Files in
                                                					 compatible formats are played or read. |
| Play Message By Number | Asks the user to enter the number of a message in the current
                                                					 stack (new, saved, or deleted messages) and then takes the user directly to
                                                					 that message. For users who have large numbers of messages, this is a useful
                                                					 way to jump ahead or back in the stacks. This option is available only when the Enable Go to Message
                                                					 setting is enabled on the System Settings > Advanced > Conversations
                                                					 page. |
| Go to Previous Message | Takes the user to the previous message in the stack. |
| Go to Next Message | Takes the user to the next message in the stack. The message the
                                                					 user was listening to is left in the state that it was in (new, saved, or
                                                					 deleted). Go to Next Message functions the same as the Skip Message, Save As Is
                                                					 option. |
| Save As Is | Goes to the next message in the stack and leaves the message in
                                                					 the state that it was in. New messages are saved as unread; saved messages
                                                					 remain saved; and deleted messages remain deleted. |
| Go to First Message | Jumps to the first message of the message stack. Unity
                                                					 Connection plays the “First message” prompt as an audible cue to the user. |
| Go to Last Message | Jumps to the last message of the message stack. Unity Connection
                                                					 plays the “Last message” prompt as an audible cue to the user. |
| Toggle Urgency Flag | Toggles the priority flag on a received message between urgent
                                                					 and normal. Users who want to identify the high-priority messages among all
                                                					 of their received messages may be interested in this functionality. By default,
                                                					 Unity Connection plays messages that are marked urgent first. |
| Call the Sender | Terminates message playback, signs users out of their mailboxes,
                                                					 and transfers users to the person who left the message. This feature is also
                                                					 known as Live Reply. This key option is used to return calls to both other
                                                					 users and unidentified callers. This option is available only when the user is assigned to a
                                                					 class of service that has enabled either the Users Can Reply to Messages from
                                                					 Other Users by Calling Them or the Users Can Reply to Messages from
                                                					 Unidentified Callers by Calling Them setting. |
| Skip Message, Save As Is | Skips to the next message in the stack and leaves the message in
                                                					 the state it was in. When a new message is skipped, it is saved as unread; when
                                                					 a saved message is skipped, it remains saved; and when a deleted message is
                                                					 skipped, it remains deleted. |
| List Message Recipients | Lists all recipients of the current message. |
| Reply to All | Replies to all recipients of the message. |

| Option | Description |
|---|---|
| Greetings | Allows users to edit their greetings. |
| Message Settings | Takes users to the Message Settings menu. |
| Preferences | Takes users to the Preferences menu. |
| Transfer Settings | Allows users to edit their transfer rules. |
| Alternate Contact Numbers | Allows users to change their alternate contact phone numbers. This option is available for a user only when an administrator
                                                					 has configured one or more caller input keys to transfer to an alternate
                                                					 contact number on the user Edit Caller Input page. |
| Repeat Menu | Plays the Settings menu again. |
| Help | Plays the Settings menu Help. |
| Cancel or Back Up | Exits the Settings menu and goes up a menu level to the Main
                                                					 menu. |
| Change Alternate Greeting | Allows users to change alternate greetings by activating and
                                                					 re-recording. In case of a video call, when users are listening to the main
                                                					 menu options and press the applicable key, Unity Connection plays your
                                                					 alternate video greeting and asks you to re-record your alternate greeting. |

| Option | Description |
|---|---|
| Message Notification | Allows users to edit the settings for their message notification
                                                					 devices. |
| Fax Delivery | Allows users to change the phone number of the fax machine to
                                                					 which they can send faxes for printing. |
| Menu Style | Allows users to switch between the full or brief menu styles. |
| Private Lists | Allows users to edit their private lists. |
| Addressing Priority List | Allows users to review and add or remove names from their
                                                					 addressing priority list. |
| Repeat Menu | Plays the Message Settings menu again. |
| Help | Plays the Message Settings menu Help. |
| Cancel or Back Up | Exits the Message Settings menu and goes up a menu level to the
                                                					 Settings menu. |

| Option | Description |
|---|---|
| Change Phone Password | Allows users to edit their phone PINs. This option is not available for a user when the User Cannot
                                                					 Change check box is checked on the user Edit Password Settings page. |
| Change Recorded Name | Allows users to record names. This option is available only when the user is assigned to a
                                                					 class of service that has enabled the Allow Recording of Name option. |
| Change Directory Listing | Allows users to choose whether or not they want to be listed in
                                                					 the directory. This option is available only when the user is assigned to a
                                                					 class of service that has enabled the Allow Users to Choose to Be Listed in the
                                                					 Directory option. |
| Edit User-Defined Alternate Extensions | Allows users to list and delete their alternate extensions. Also
                                                					 allows users to add the current number they are calling from as an alternate
                                                					 extension (if it is not already an alternate extension and does not match a
                                                					 blocked pattern in the User-Defined or Automatically-Added Alternate Extensions
                                                					 restriction table). |
| Repeat Menu | Plays the Preferences menu again. |
| Help | Plays the Preferences menu Help. |
| Cancel or Back Up | Exits the Preferences menu and goes up a menu level to the
                                                					 Settings menu. |

| Note | You can only migrate messages if you have first migrated the
                                       		  user data. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Migration Utilities. |
|---|---|
| Step 2 | Expand Migration Utilities , then select the applicable
                                          			 option ( Migrate Users > or > Migrate
                                                				  Messages ). |

| Note | You can sign up to be notified when the utilities posted on the Cisco Unity Tools website are updated. Go to http://ciscounitytools.com and select Sign Up Here. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users and
                                                			 select Users. |
|---|---|
| Step 2 | On the Search Users page, find the applicable user account. Note As a best practice, do not use the default system administrator
                                                               				  user account for remote access. Instead, use a different administrative user
                                                               				  account to avoid the default system administrator account become locked due to
                                                               				  too many failed authentication attempts. | Note | As a best practice, do not use the default system administrator
                                                               				  user account for remote access. Instead, use a different administrative user
                                                               				  account to avoid the default system administrator account become locked due to
                                                               				  too many failed authentication attempts. |
| Note | As a best practice, do not use the default system administrator
                                                               				  user account for remote access. Instead, use a different administrative user
                                                               				  account to avoid the default system administrator account become locked due to
                                                               				  too many failed authentication attempts. |
| Step 3 | On the Edit User Basics page, in the Edit menu, select Roles. |
| Step 4 | On the Edit Roles page, in the Available Roles field, select Remote Administrator , then select the Up arrow to
                                                			 move it into the Assigned Roles field. |
| Step 5 | Select Save . |
| Step 6 | Repeat Step 2 through Step 5 for each user who needs access to
                                                			 remote administration tools. |

| Note | As a best practice, do not use the default system administrator
                                                               				  user account for remote access. Instead, use a different administrative user
                                                               				  account to avoid the default system administrator account become locked due to
                                                               				  too many failed authentication attempts. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, expand Tools and
                                          			 select Service Management. |
|---|---|
| Step 2 | In the Optional Services section, find the Unity Connection
                                          			 Database Proxy row and select Activate. |

| Note | Migration in a Tenant Partitioned environment using COBRAS tool allows the administrator to export the data from a non-partitioned
                                          Unity Connection system or a Tenant-Partitioned Unity Connection system. For more information on each scenario and on migration
                                          process using COBRAS tools, refer to http://www.ciscounitytools.com/Applications/General/COBRAS/COBRAS.html link. |
|---|---|