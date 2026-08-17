---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-administration-guide-b-12xcucsag-b-12xcucsag-chapter-01-html-512db33fae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag/b_12xcucsag_chapter_01.html
retrieved_at: 2026-08-17T02:31:00.446476+00:00
---

System Administration Guide

# System Administration Guide

Updated: August 1, 2017

Chapter: Accessibility

## Chapter: Accessibility

# Accessibility

## Overview

Cisco Unity Connection supports various shortcut keys and features that provides easy access to web applications, such as
                           Cisco Unity Connection Administration and Web Inbox.

## Shortcut Keys for
                        	 Cisco Unity Connection Administration

Following
                              		  are the details on the usage of shortcut keys for Cisco Unity Connection
                              		  Administration:

The administrator can use the TAB key to navigate all links, all
                                    				form fields, and widgets in the sequential order. After login, when the
                                    				administrator first presses the TAB key then focus comes on top of the tree
                                    				labeled as Cisco Unity Connection. Then by pressing the TAB key again, the
                                    				administrator can traverse all links, all form fields, and widgets.

At any time if the administrator wants to navigate to the page
                                    				corresponding to the tree link, then press the 'ENTER' key after selecting the
                                    				link using the TAB key.

Once focus goes to page frame, then by pressing TAB key you can
                                    				traverse all visual adds on that page.

The administrator can move the focus from any of the page/form
                                    				to the top of the tree by the “Ctrl+Alt+t” key. This shortcut key focuses the
                                    				top tree label Cisco Unity Connection and from there you can traverse all tree
                                    				links using the TAB key.

The Ctrl+Alt+t shortcut can be used at anywhere in the tree and
                                    				pages to focus tree label Cisco Unity Connection.

The shortcut keys work on Windows and MAC operating system.

Item

Internet Explorer

Mozilla Firefox

Safari/Chrome

Usage

Forward navigation of links, form fields, and widget on Unity
                                          						Connection Administration

TAB

TAB

Note: The TAB key does not work on MAC for any hyperlink
                                          						navigation. To make it work, the administrator needs to do some configuration
                                          						changes in Firefox specified in Enabling TAB Key Navigation for Hyperlink On MAC section.

TAB

The TAB key is used to navigate all links, all form fields, and
                                          						widget in the forward sequence.

To select or de-select radio button you can use any Arrow key.

Focus on the top of Unity Connection Administration tree

Ctrl+Alt+t

Ctrl+Alt+t

Ctrl+Alt+t

This shortcut key is used to bring focus back on the top of tree
                                          						in the Unity Connection Administration page.

Backward navigation of links, form fields, and widget on Unity
                                          						Connection Administration

Shift+TAB

Shift+TAB

Shift+TAB

This combination of key is used to navigate links, form fields,
                                          						and widget in the backward sequence.

Navigate menu item

Left or Right arrow key

Left or Right arrow key

Left or Right arrow key

First bring focus on any menu item using TAB or Shift+TAB and
                                          						then use the Left or Right arrow key to navigate to all the menu items.

Navigate drop down list Item

Up or Down arrow key

Up or Down arrow key

Up or Down arrow key

First bring focus on the drop down list using TAB or Shift+TAB
                                          						and then use Up or Down arrow key to navigate to all the items in the list.

Expand and Collapse tree in Unity Connection Administration

ENTER Key

ENTER Key

ENTER Key

First bring focus on tree node then press ENTER to expand and
                                          						collapse the tree for fast navigation

### Enabling TAB Key Navigation for Hyperlink On Safari

The TAB key does not work on the Safari browser
                                 		  for hyperlink navigation. Therefore, left most tree is not accessible in the
                                 		  Unity Connection Administration page through the TAB key directly. To make the
                                 		  tree accessible through TAB key it is required to change the following browser
                                 		  settings on Safari.

Step 1

Click goto Preferences> Advanced.

Step 2

Select the Press tab to highlight each item
                                          			 on a web page check box to make the tree links accessible using the TAB key.

### Enabling TAB Key Navigation for Hyperlink On MAC

Step 1

Open the Firefox browser and type
                                          			 about:config in the address bar.

Step 2

Press 'ENTER' key.

Step 3

Accept the security warning.

Step 4

From the list of configuration parameters.
                                          			 Try to search for "accessibility.tabfocus".

Step 5

If it is not listed then add this parameter
                                          			 as an "integer" and give its value "7".

Step 6

Refresh the page and use TAB key for page
                                          			 navigation.

If there is a DTMF number in the display
                                                         				  name then the part of the name after DTMF digit does not play as recorded name.

## Other Unity Connection Features

Other Unity Connection Features that can improve the Accessibility for the end user:

### Speech
                           	 Connect

The Speech Connect feature provides a speech-enabled enhancement
                              		to the automated attendant functionality. Speech Connect uses voice-enabled
                              		directory handlers to allow both Unity Connection users and outside callers to
                              		do the following:

Speak out the name of an employee (Unity Connection user) and
                                    			 instantly be connected, without navigating an audio-text tree and without
                                    			 knowing the extension of the employee.

For easy access to employees, configure a Speech Connect speed
                                    			 dial on user phones.

If multiple employees have the same name or if Speech Connect
                                    			 does not have a perfect match for the name spoken by the caller, it presents
                                    			 numerous name choices for the caller and can include additional information
                                    			 such as the employee location or department. Speech Connect also plays the
                                    			 recorded name of the employee in his or her own voice, if available, making it
                                    			 easier for the caller to choose among multiple names.

For more information about setting up directory handlers, see
                              		the Call Management chapter.

### Cisco SpeechView

The SpeechView feature allows you to receive voice messages in your mailbox in the form of text. When a voice message arrives,
                              it is delivered to the mailbox of the recipient with a blank text attachment. The text attachment is updated with the transcription
                              text when the transcription service completes the transcription. If there was a problem with the transcription, then an error
                              message is received in the text attachment of the voice message.

Only the first 500 characters of a voice message are transcribed and the remaining message is truncated. However, the users
                              have access to the original recording in its entirety.

SpeechView is a feature of the unified messaging solution. Therefore, the original audio version of each voice message remains
                              available to you anytime.

### TTY
                           	 Overview

A TTY prompt set, available in U.S. English (ENX) only, can be
                              		installed and used just like any other supported phone language. When the TTY
                              		prompt set is installed, the subscribers and outside callers that use TTY can
                              		call in to Unity Connection and use the same features that a hearing caller can
                              		use. However, note the following limitations:

G.711 MuLaw must be selected as the message recording and
                                    			 storage codec because the Unity Connection TTY prompt set is not compatible
                                    			 with G.729a or other message recording and storage codecs.

A dedicated phone number must be set up for use by outside
                                    			 callers with TTY. All greetings, prompts, and subscriber names accessible from
                                    			 this number must be created with the TTY prompt set.

TTY is a TUI language only. At present, there is no compatible
                                    			 Text to Speech (TTS) language for TTY. The TTY prompt set is also not suitable
                                    			 for use as a GUI language.

TTY tones are not available for use in navigating through the
                                    			 Unity Connection conversation. Some TTY phones do not have the capability to
                                    			 send DTMF tones. In this case, TTY users may need to use the phone keypad for
                                    			 system navigation.

Due to recording and playback limitations, the TTY prompt set
                                    			 cannot be used in interview handlers.

TTY phones do not display the voice names but simply playback
                                    			 the voice names.

Use TTY angel to display voice name as text and replace them in
                                    			 Unity Connection. For more information on TTY angel, see the TTY Angel Help at http://www.ciscounitytools.com/Applications/General/TTYAngel/TTYAngel.html .

- It is recommended to disable
                                 		  the comfort noise on Cisco Unity Connection Administration for better quality
                                 		  conversation using ipTTY device. To disable the comfort noise, navigate to System Settings > Advanced > Telephony and uncheck the "Vad Enabled" check box. For
                                 		  information on how to use ipTTY device, see the ipTTY Configuration Guide for Cisco UCM 9.x at https://docs.google.com/document/d/1CmS0aTN7hIFqlZ_PvjKqTlhgK5xV8IPNTmi8cgsbn6w/edit?pref=2&pli=1 .

#### Setting Up Cisco
                              	 Unity Connection to Use the TTY Prompt Set

To set up Unity
                                    		  Connection for TTY, do the following tasks.

Step 1

Obtain a
                                             			 dial-in number that will be used exclusively for outside callers with TTY to
                                             			 call in to Unity Connection. Set up the phone system and integration as
                                             			 required.

Step 2

Install TTY
                                             			 devices for subscribers, as needed.

Step 3

Install the
                                             			 ENX language on the Unity Connection server.

Step 4

Confirm that
                                             			 G.711 is selected as the Unity Connection message recording and storage code.

Step 5

Create a TTY
                                             			 subscriber template. This template will be used when creating subscriber
                                             			 accounts for all subscriber who will use TTY. You may also want to create a TTY
                                             			 class of service, on which you disable Text to Speech for these subscribers.

Step 6

Create a
                                             			 routing rule for the TTY dial-in number.

Step 7

Create an
                                             			 opening greeting call handler for the TTY dial-in number.

Step 8

Set up
                                             			 additional TTY call handlers as needed.

Step 9

Record
                                             			 greetings in TTY by using the TTY Angel, or by using the Media Player and a TTY
                                             			 phone as a recording and playback device. You will need to record the following
                                             			 greetings, as applicable: the opening greeting, additional call handler
                                             			 greetings, and subscriber greetings.

Step 10

Test the TTY
                                             			 dial-in number, opening greeting, call handlers, and all subscriber devices to
                                             			 confirm correct operation for both incoming and outgoing TTY calls.

| Item | Internet Explorer | Mozilla Firefox | Safari/Chrome | Usage |
|---|---|---|---|---|
| Forward navigation of links, form fields, and widget on Unity
                                          						Connection Administration | TAB | TAB Note: The TAB key does not work on MAC for any hyperlink
                                          						navigation. To make it work, the administrator needs to do some configuration
                                          						changes in Firefox specified in Enabling TAB Key Navigation for Hyperlink On MAC section. | TAB | The TAB key is used to navigate all links, all form fields, and
                                          						widget in the forward sequence. To select or de-select radio button you can use any Arrow key. |
| Focus on the top of Unity Connection Administration tree | Ctrl+Alt+t | Ctrl+Alt+t | Ctrl+Alt+t | This shortcut key is used to bring focus back on the top of tree
                                          						in the Unity Connection Administration page. |
| Backward navigation of links, form fields, and widget on Unity
                                          						Connection Administration | Shift+TAB | Shift+TAB | Shift+TAB | This combination of key is used to navigate links, form fields,
                                          						and widget in the backward sequence. |
| Navigate menu item | Left or Right arrow key | Left or Right arrow key | Left or Right arrow key | First bring focus on any menu item using TAB or Shift+TAB and
                                          						then use the Left or Right arrow key to navigate to all the menu items. |
| Navigate drop down list Item | Up or Down arrow key | Up or Down arrow key | Up or Down arrow key | First bring focus on the drop down list using TAB or Shift+TAB
                                          						and then use Up or Down arrow key to navigate to all the items in the list. |
| Expand and Collapse tree in Unity Connection Administration | ENTER Key | ENTER Key | ENTER Key | First bring focus on tree node then press ENTER to expand and
                                          						collapse the tree for fast navigation |

| Step 1 | Click goto Preferences> Advanced. |
|---|---|
| Step 2 | Select the Press tab to highlight each item
                                          			 on a web page check box to make the tree links accessible using the TAB key. |

| Step 1 | Open the Firefox browser and type
                                          			 about:config in the address bar. |
|---|---|
| Step 2 | Press 'ENTER' key. |
| Step 3 | Accept the security warning. |
| Step 4 | From the list of configuration parameters.
                                          			 Try to search for "accessibility.tabfocus". |
| Step 5 | If it is not listed then add this parameter
                                          			 as an "integer" and give its value "7". |
| Step 6 | Refresh the page and use TAB key for page
                                          			 navigation. Note If there is a DTMF number in the display
                                                         				  name then the part of the name after DTMF digit does not play as recorded name. | Note | If there is a DTMF number in the display
                                                         				  name then the part of the name after DTMF digit does not play as recorded name. |
| Note | If there is a DTMF number in the display
                                                         				  name then the part of the name after DTMF digit does not play as recorded name. |

| Note | If there is a DTMF number in the display
                                                         				  name then the part of the name after DTMF digit does not play as recorded name. |
|---|---|

| Step 1 | Obtain a
                                             			 dial-in number that will be used exclusively for outside callers with TTY to
                                             			 call in to Unity Connection. Set up the phone system and integration as
                                             			 required. |
|---|---|
| Step 2 | Install TTY
                                             			 devices for subscribers, as needed. |
| Step 3 | Install the
                                             			 ENX language on the Unity Connection server. |
| Step 4 | Confirm that
                                             			 G.711 is selected as the Unity Connection message recording and storage code. |
| Step 5 | Create a TTY
                                             			 subscriber template. This template will be used when creating subscriber
                                             			 accounts for all subscriber who will use TTY. You may also want to create a TTY
                                             			 class of service, on which you disable Text to Speech for these subscribers. |
| Step 6 | Create a
                                             			 routing rule for the TTY dial-in number. |
| Step 7 | Create an
                                             			 opening greeting call handler for the TTY dial-in number. |
| Step 8 | Set up
                                             			 additional TTY call handlers as needed. |
| Step 9 | Record
                                             			 greetings in TTY by using the TTY Angel, or by using the Media Player and a TTY
                                             			 phone as a recording and playback device. You will need to record the following
                                             			 greetings, as applicable: the opening greeting, additional call handler
                                             			 greetings, and subscriber greetings. |
| Step 10 | Test the TTY
                                             			 dial-in number, opening greeting, call handlers, and all subscriber devices to
                                             			 confirm correct operation for both incoming and outgoing TTY calls. |