---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-appendix-0100001-h-ea0473f549
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_appendix_0100001.html
retrieved_at: 2026-08-17T02:40:35.263907+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting
	 Media Player

## Chapter: Troubleshooting
	 Media Player

# Troubleshooting
                     	 Media Player

This chapter contains the troubleshooting scenarios of Media Player with
                        		resolution.

## Using the Phone
                        	 Device for Playback and Recording in Media Player

The Media Player
                           		supports the phone as a playback and recording device. The phone device is
                           		always available to users. Using Number or URI field, users can configure the
                           		active phone number for the phone device (the default value is the primary
                           		Unity Connection extension of the user).

The phone device
                           		sends requests over the network to the Unity Connection server to call the
                           		active phone number. When the phone answers, the phone device proceeds with
                           		either playing back or recording the voice recording. The call can fail for
                           		these reasons:

- Either no active phone
                              		  number value is defined, or it is defined incorrectly.

- The phone system to which
                              		  the user is assigned does not have any TRAP ports enabled.

- All TRAP-capable ports on
                              		  the phone system are busy.

- No phone system is
                              		  designated to handle TRAP connections.

Problems with the Phone
                              		  Device Ringing the Phone for Playback or Recording of a Voice Message

Use the
                           		troubleshooting information in this section if the phone device either does not
                           		ring the phone, or rings the phone only once for playback or recording of voice
                           		messages:

- The phone number dialed by
                                 			 the Media Player is not the expected number -Confirm that the active phone
                              		  number specified in the Media Player is correct. To do this, check the Active
                              		  Phone Number value for the Primary Extension or Other Number in the Number or
                              		  URI field on the Media Player.

When a phone
                                 			 system is not designated to handle TRAP connections, the following error
                                 			 appears.

Could not
                                 			 establish a phone conversation.

The server
                                 			 reports the following:

Code: 26

Description:
                                 			 Cannot find a switch to route the call

Follow the steps in the Designating a Phone System to Handle TRAP Connections section.

### Designating a
                           	 Phone System to Handle TRAP Connections

Step 1

In Cisco Unity Connection
                                          			 Administration, expand Telephony Integrations , then select Phone System .

Step 2

On the Search Phone Systems
                                          			 page, select the name of the phone system that you want to handle TRAP
                                          			 connections.

Step 3

On the Phone System Basics
                                          			 page, check the Default TRAP Switch check box and select Save .

## Problem Uploading
                        	 a File in the Media Player

When you attempt to use a previously recorded WAV file (for example, an announcement that was recorded earlier) rather than
                           making a new recording using a phone or computer, the Media Player may display the following error message while saving the
                           page:

"Audio format not
                           		supported"

To resolve this
                           		problem, do one of the following:

Convert the WAV file to another audio format (for example, convert it to the G.711 audio format).

- Use a WAV file that is
                              		  recorded in a supported audio format.

- Make the recording using a
                              		  phone.

## Unknown Error
                        	 Appears while Using Media Player with Phone

While using Media
                           		Player for record, play, upload and download, the Media Player may display the
                           		following error message when phone is used as a playback and recording device:

"Unknown error.
                           		Please contact to System Administrator"

If you receive the
                           		above error message, you need to enable the VMREST (all levels) traces and see
                           		the diag_Tomcat_*.uc log file to troubleshoot the problem.

| Note | The reason
                                          			 for the delay is that the phone system waits to determine that the entire phone
                                          			 number has been dialed before it connects the call. |
|---|---|

| Step 1 | In Cisco Unity Connection
                                          			 Administration, expand Telephony Integrations , then select Phone System . |
|---|---|
| Step 2 | On the Search Phone Systems
                                          			 page, select the name of the phone system that you want to handle TRAP
                                          			 connections. |
| Step 3 | On the Phone System Basics
                                          			 page, check the Default TRAP Switch check box and select Save . |

| Note | You must Save the
                                       		  page after uploading the WAV file on the Media Player. |
|---|---|