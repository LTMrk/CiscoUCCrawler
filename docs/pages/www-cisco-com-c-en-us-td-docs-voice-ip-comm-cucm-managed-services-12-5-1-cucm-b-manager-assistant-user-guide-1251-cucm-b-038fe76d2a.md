---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-manager-assistant-user-guide-1251-cucm-b-038fe76d2a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_manager-assistant-user-guide-1251/cucm_b_manager-assistant-user-guide-1251_chapter_01.html
retrieved_at: 2026-08-21T01:28:33.762845+00:00
---

Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Introduction

The Unified Communications Manager Assistant application (called Manager Assistant) provides call-routing and other call-management features to help managers
                              and assistants handle phone calls more effectively.

Assistants and managers can experience large phone-call volumes from inside and outside the Unified Communications Manager IP Phone network. A maximum of 3500 assistants and 3500 managers (7000 total users) can be configured within a Cisco Unified Communications Manager network.

## Manager Assistant
                        	 Overview

Within the
                              		  framework of the Manager Assistant, it is helpful to understand the three key
                              		  components—managers, assistants, and the Assistant Console. These components
                              		  are as follows:

Manager—A user
                                    				whose incoming calls are intercepted and redirected to an assistant. At least
                                    				one assistant supports a manager. Managers can use Manager Assistant directly
                                    				on their Cisco Unified IP Phone by configuring features
                                    				in the Manager Configuration window or ask assistants
                                    				to configure the preferences.

Assistant—A
                                    				user who handles calls for a manager, such as the manager’s assistant. An
                                    				assistant can support as many as 33 managers. Incoming calls to a manager can
                                    				be intercepted and redirected to an assistant automatically or manually. The
                                    				assistant can then answer, transfer, divert, and manage the calls.

Assistant
                                    				Console—Assistants can use this application on their computers to perform most
                                    				Manager Assistant features:

Place,
                                          					 answer, transfer, put on hold, end, divert, or add conference participants to a
                                          					 call

Monitor a
                                          					 manager’s call activity and feature status

Enable or
                                          					 disable manager features

Configure
                                          					 manager features

## Shared-Line and
                        	 Proxy-Line Modes Overview

The Manager
                              		  Assistant operates in two modes—shared-line and proxy-line. The features
                              		  available to you are based on the mode that your system administrator chose for
                              		  your Manager Assistant configuration.

Shared-line mode—Only the Do Not Disturb option appears on the
                                                   				  screen.

Proxy-line mode—Multiple options appear on the screen.

### Use Manager
                           	 Assistant in Shared-Line Mode

If your system
                                 		  administrator configured the Manager Assistant in the shared-line mode, the
                                 		  manager and assistant share a directory number, such as 8001, and share a line.
                                 		  When a call comes in on 8001, it rings on both phones, and the assistant
                                 		  handles these calls for the manager.

When Manager
                                 		  Assistant is in this mode, assistants and managers have these capabilities:

If you are an
                                       				assistant, you do not need to be logged in to receive calls. Calls to your
                                       				manager ring on your phone automatically.

If you are a
                                       				manager, you can share your directory number with up to 10 assistants, and any
                                       				of these assistants can answer and handle a call.

These Manager
                                 		  Assistant features do not apply in the shared-line mode. The assistant cannot
                                 		  see or access these call features on the Assistant Console application:

Assistant
                                       				Selection

Assistant
                                       				Watch—The manager’s phone does not have this softkey.

Call
                                       				Filtering—The manager’s phone does not have this softkey.

Divert All—The
                                       				assistant’s and manager’s phones do not have this softkey.

### Use Manager
                           	 Assistant in Proxy-Line Mode

If your system
                                 		  administrator configured Manager Assistant in the proxy-line mode, the manager
                                 		  and assistant do not share a directory number. The assistant handles calls for
                                 		  a manager using a proxy number (line), which is not the manager’s directory
                                 		  number. The proxy number is an alternate number that the system chooses and it
                                 		  represents the manager’s actual directory number.

When Manager
                                 		  Assistant is in the proxy-line mode, a manager and an assistant have access to
                                 		  all call features in Manager Assistant, including Assistant
                                    		  Selection , Assistant
                                    		  Watch , Call
                                    		  Filtering , and Divert
                                    		  All and have these capabilities.

If you are an
                                       				assistant, you must log in to the Assistant Console and be online to receive
                                       				calls on your phone that come in to your manager. You can use the Assistant
                                       				Console for all call-handling features, such as answering or transferring
                                       				calls.

If you are a
                                       				manager, you can set up filters to sort and filter incoming calls to your
                                       				assistant.

## Identify Mode on Manager’s Phone

To identify the
                              		  mode on a manager’s phone, reset the LCD display on the phone by picking up the
                              		  receiver and replacing it.

If you see a
                              		  single bell (or crossed-out bell) icon in the status window of the LCD display,
                              		  you are using Manager Assistant in the shared-line mode. See the following
                              		  figure.(The icon is black and white on some Cisco Unified IP Phone models.)

If you see
                              		  multiple icons in the status window of the LCD display, you are using Manager
                              		  Assistant in the proxy-line mode. See the following figure.(The icons are black
                              		  and white on some Cisco Unified IP Phone models.)

## Identify Mode on the Assistant Console

On the Assistant
                              		  Console, use this procedure to identify the Manager Assistant mode.

Log in to the Assistant Console . 
                                       		  See Log In and Out of the Assistant Console .

Find the
                                       			 extension number adjacent to a manager’s name in the My
                                          				Calls panel. 
                                       		  See Use My Calls Panel .

For the same
                                       			 manager, find the extension number adjacent to the telephone icon in the Call
                                          				Details column in the My
                                          				Manager ’s panel. See Use the My Managers Panel .

If you cannot
                                          				see a number adjacent to the telephone icon, increase the column width by
                                          				clicking and dragging the Call
                                             				  Details heading border.

Verify whether
                                       			 the manager’s and assistant’s extension numbers are the same or different:

Extensions
                                                					 that are the same—Shared-line mode: You can see four headings in the My
                                                   				Manager ’s panel- Manager , Intercom , DND , and Call
                                                   				Details .

Extensions
                                                				  that are different—Proxy-line mode: You can see the headings that you see in
                                                				  the shared-line mode and four additional headings:— Divert All , Assistant
                                                   				Watch , Filter
                                                   				Calls , and Filter
                                                   				Mode .

## Support for Other
                        	 Languages

The Manager
                              		  Assistant supports several different languages, including Arabic and Hebrew.

(If Arabic or
                              		  Hebrew are used, the Manager Assistant application screens change to reflect
                              		  the right-to-left direction of these languages.)

For more
                              		  information on using different languages with your phone, contact your system
                              		  administrator.

| Note | Note that before
                                          			 you begin using the Manager Assistant, you need to identify which mode your
                                          			 system administrator chose. To do this, check the Manager Settings application screen: Shared-line mode—Only the Do Not Disturb option appears on the
                                                   				  screen. Proxy-line mode—Multiple options appear on the screen. |
|---|---|

| Step 1 | Log in to the Assistant Console . 
                                       		  See Log In and Out of the Assistant Console . |
|---|---|
| Step 2 | Find the
                                       			 extension number adjacent to a manager’s name in the My
                                          				Calls panel. 
                                       		  See Use My Calls Panel . |
| Step 3 | For the same
                                       			 manager, find the extension number adjacent to the telephone icon in the Call
                                          				Details column in the My
                                          				Manager ’s panel. See Use the My Managers Panel . If you cannot
                                          				see a number adjacent to the telephone icon, increase the column width by
                                          				clicking and dragging the Call
                                             				  Details heading border. |
| Step 4 | Verify whether
                                       			 the manager’s and assistant’s extension numbers are the same or different: Extensions
                                                					 that are the same—Shared-line mode: You can see four headings in the My
                                                   				Manager ’s panel- Manager , Intercom , DND , and Call
                                                   				Details . Extensions
                                                				  that are different—Proxy-line mode: You can see the headings that you see in
                                                				  the shared-line mode and four additional headings:— Divert All , Assistant
                                                   				Watch , Filter
                                                   				Calls , and Filter
                                                   				Mode . |