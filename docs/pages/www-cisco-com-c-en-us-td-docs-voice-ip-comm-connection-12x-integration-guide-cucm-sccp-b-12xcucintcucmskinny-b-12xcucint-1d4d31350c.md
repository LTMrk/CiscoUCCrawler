---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-integration-guide-cucm-sccp-b-12xcucintcucmskinny-b-12xcucint-1d4d31350c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/cucm_sccp/b_12xcucintcucmskinny/b_12xcucintcucmskinny_chapter_0100.html
retrieved_at: 2026-08-16T18:40:36.934211+00:00
---

Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Manager SCCP Integration Guide for Cisco Unity Connection Release 12.x

Updated: August 2, 2017

Chapter: Testing the
	 Integration

## Chapter: Testing the
	 Integration

# Testing the
                     	 Integration

To test whether
                        		Cisco Unity Connection and the phone system are integrated correctly, do the
                        		following procedures:

If any of the steps
                        		indicate a failure, see the following documentation as applicable:

- The " Installing Cisco Unity
                              			 Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity
                              			 Connection , Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

- Troubleshooting Guide for
                              			 Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html .

## Testing the
                        	 Integration

To test whether
                           		Cisco Unity Connection and the phone system are integrated correctly, do the
                           		following procedures:

If any of the steps
                           		indicate a failure, see the following documentation as applicable:

- The " Installing Cisco Unity
                                 			 Connection " chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity
                                 			 Connection , Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

- Troubleshooting Guide for
                                 			 Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html .

### Testing the
                           	 Telephony Integration

Go to
                                          			 Telephony Integrations and select Phone System on Cisco Unity Connection
                                          			 Administration.

Select the
                                          			 Phone System from the list for which configuration needs to be tested.

In the
                                          			 Related Links drop-down list, select Check
                                             				Telephony Configuration and select Go to
                                          			 confirm the phone system integration settings.

In the Task
                                          			 Execution Results window, select Close .

### Setting Up the
                           	 Test Configuration

Set up two test extensions (Phone 1 and Phone 2) on the same
                                          			 phone system with which Unity Connection is connected.

Set Phone 1 to forward calls to the Unity Connection pilot
                                          			 number when calls are not answered.

In Cisco Unity Connection Administration, expand Users and select Users .

On the Search Users page, select the display name of a user to
                                          			 use for testing. The extension for this user must be the extension for Phone 1.

On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box.

In the Voice Name field, record a recorded name for the test
                                          			 user.

Select Save .

On the Edit menu, click Message Waiting Indicators .

On the Message Waiting Indicators page, click the message
                                          			 waiting indicator. If no message waiting indication is in the table, click Add New .

On the Edit Message Waiting Indicator page, enter the following
                                          			 settings.

Field

Setting

Enabled

Check this check box to enable MWIs for the test user.

Display Name

Accept the default or enter a different name.

Inherit User’s Extension

Check this check box to enable MWIs on Phone 1.

Select Save .

On the Edit menu, select Transfer Options .

On the Transfer Options page, select the active option.

On the Edit Transfer Option page, under Transfer Action, select
                                          			 the Extension option and enter the extension of Phone 1.

In the Transfer Type field, select Release to Switch and select Save .

Minimize the Cisco Unity Connection Administration window.

Do not close the Cisco Unity Connection Administration window
                                             				because you use it again in a later procedure.

Sign in to the Real-Time Monitoring Tool (RTMT).

On the Unity Connection menu, select Port Monitor . The Port Monitor tool appears in the
                                          			 right pane.

In the right pane, select Start Polling . The Port Monitor display which port
                                          			 is handling the calls that you make.

### Testing an External Call with Release Transfer

From Phone 2, enter the access code
                                          			 necessary to get an outside line, and then enter the number outside callers use
                                          			 to dial directly to Unity Connection.

In the Port Monitor, note which port handles
                                          			 this call.

When you hear the opening greeting, enter
                                          			 the extension for Phone 1. Hearing the opening greeting means that the port is
                                          			 configured correctly.

Confirm that Phone 1 rings and that you hear
                                          			 a ringback tone on Phone 2. Hearing a ringback tone means that Unity Connection
                                          			 correctly released the call and transferred it to Phone 1.

Leaving Phone 1 unanswered, confirm that the
                                          			 state of the port handling the call changes to “Idle.” This state means that
                                          			 release transfer is successful.

Confirm that, after the number of rings that
                                          			 the phone system is set to wait, the call is forwarded to Unity Connection and
                                          			 that you hear the greeting for the test user. Hearing the greeting means that
                                          			 the phone system forwarded the unanswered call and the call-forward information
                                          			 to Unity Connection, which correctly interpreted the information.

On the Port Monitor, note which port handles
                                          			 this call.

Leave a message for the test user and hang
                                          			 up Phone 2.

In the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended.

Confirm that the MWI on Phone 1 is
                                          			 activated. The activated MWI means that the phone system and Unity Connection
                                          			 are successfully integrated for turning on MWIs.

### Testing Listening to Messages

From Phone 1, enter the internal pilot
                                          			 number for Unity Connection.

When asked for your password, enter the
                                          			 password for the test user. Hearing the request for your password means that
                                          			 the phone system sent the necessary call information to Unity Connection, which
                                          			 correctly interpreted the information.

Confirm that you hear the recorded name for
                                          			 the test user (if you did not record a name for the test user, you hear the
                                          			 extension number for Phone 1). Hearing the recorded name means that Unity
                                          			 Connection correctly identified the user by the extension.

Listen to the message.

After listening to the message, delete the
                                          			 message.

Confirm that the MWI on Phone 1 is
                                          			 deactivated. The deactivated MWI means that the phone system and Unity
                                          			 Connection are successfully integrated for turning off MWIs.

Hang up Phone 1.

On the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended.

### Setting Up Supervised Transfer on Cisco Unity Connection

In Cisco Unity Connection Administration, on
                                          			 the Edit Transfer Option page of the test user, in the Transfer Type field,
                                          			 select Supervise Transfer .

In the Rings to Wait For field, enter 3 .

Select Save .

Minimize the Cisco Unity Connection
                                          			 Administration window.

Do not close the Unity Connection
                                             				Administration window because you use it again in a later procedure.

### Testing Supervised Transfer

From Phone 2, enter the access code
                                          			 necessary to get an outside line, and then enter the number outside callers use
                                          			 to dial directly to Unity Connection.

On the Port Monitor, note which port handles
                                          			 this call.

When you hear the opening greeting, enter
                                          			 the extension for Phone 1. Hearing the opening greeting means that the port is
                                          			 configured correctly.

Confirm that Phone 1 rings and that you do
                                          			 not hear a ringback tone on Phone 2. Instead, you should hear the indication
                                          			 your phone system uses to mean that the call is on hold (for example, music).

Leaving Phone 1 unanswered, confirm that the
                                          			 state of the port handling the call remains “Busy.” This state and hearing an
                                          			 indication that you are on hold mean that Unity Connection is supervising the
                                          			 transfer.

Confirm that, after three rings, you hear
                                          			 the greeting for the test user. Hearing the greeting means that Unity
                                          			 Connection successfully recalled the supervised-transfer call.

During the greeting, hang up Phone 2.

On the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended.

Select Stop Polling and exit
                                          			 RTMT.

### Deleting the Test User

In Cisco Unity Connection Administration,
                                          			 expand Users and select Users .

On the Search Users page, check the check
                                          			 box to the left of the test user.

Select Delete Selected .

### Testing Cisco
                           	 Unified CM Authentication and Encryption

If Unity Connection is set up for Cisco Unified CM
                                 		  authentication or encryption, do the following procedure.

From Phone 1, dial the internal pilot number for Cisco Unity
                                          			 Connection.

Confirm that the authentication icon and/or the encryption icon
                                          			 appear on the LCD of the phone.

Hang up Phone 1.

If any of the above steps indicate a failure, see the following
                                 		  documentation as applicable:

The “ Installing Cisco Unity
                                          				  Connection ” chapter of the Install, Upgrade, and Maintenance Guide for
                                       				Cisco Unity Connection, Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

Troubleshooting Guide for Cisco Unity Connection Release 12.x , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Go to
                                          			 Telephony Integrations and select Phone System on Cisco Unity Connection
                                          			 Administration. |  |
| Step 2 | Select the
                                          			 Phone System from the list for which configuration needs to be tested. |  |
| Step 3 | In the
                                          			 Related Links drop-down list, select Check
                                             				Telephony Configuration and select Go to
                                          			 confirm the phone system integration settings. | If the test
                                          			 is not successful, the Task Execution Results displays one or more messages
                                          			 with troubleshooting steps. After correcting the problems, test the connection
                                          			 again. |
| Step 4 | In the Task
                                          			 Execution Results window, select Close . |  |

| Step 1 | Set up two test extensions (Phone 1 and Phone 2) on the same
                                          			 phone system with which Unity Connection is connected. |
|---|---|
| Step 2 | Set Phone 1 to forward calls to the Unity Connection pilot
                                          			 number when calls are not answered. Caution The phone system must forward calls to the Unity
                                                      				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                                      				fail. | Caution | The phone system must forward calls to the Unity
                                                      				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                                      				fail. |
| Caution | The phone system must forward calls to the Unity
                                                      				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                                      				fail. |
| Step 3 | In Cisco Unity Connection Administration, expand Users and select Users . |
| Step 4 | On the Search Users page, select the display name of a user to
                                          			 use for testing. The extension for this user must be the extension for Phone 1. |
| Step 5 | On the Edit User Basics page, uncheck the Set for Self-enrollment at Next Login check box. |
| Step 6 | In the Voice Name field, record a recorded name for the test
                                          			 user. |
| Step 7 | Select Save . |
| Step 8 | On the Edit menu, click Message Waiting Indicators . |
| Step 9 | On the Message Waiting Indicators page, click the message
                                          			 waiting indicator. If no message waiting indication is in the table, click Add New . |
| Step 10 | On the Edit Message Waiting Indicator page, enter the following
                                          			 settings. Table 1. Settings for the Edit MWI Page Field Setting Enabled Check this check box to enable MWIs for the test user. Display Name Accept the default or enter a different name. Inherit User’s Extension Check this check box to enable MWIs on Phone 1. | Field | Setting | Enabled | Check this check box to enable MWIs for the test user. | Display Name | Accept the default or enter a different name. | Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Field | Setting |
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |
| Step 11 | Select Save . |
| Step 12 | On the Edit menu, select Transfer Options . |
| Step 13 | On the Transfer Options page, select the active option. |
| Step 14 | On the Edit Transfer Option page, under Transfer Action, select
                                          			 the Extension option and enter the extension of Phone 1. |
| Step 15 | In the Transfer Type field, select Release to Switch and select Save . |
| Step 16 | Minimize the Cisco Unity Connection Administration window. Do not close the Cisco Unity Connection Administration window
                                             				because you use it again in a later procedure. |
| Step 17 | Sign in to the Real-Time Monitoring Tool (RTMT). |
| Step 18 | On the Unity Connection menu, select Port Monitor . The Port Monitor tool appears in the
                                          			 right pane. |
| Step 19 | In the right pane, select Start Polling . The Port Monitor display which port
                                          			 is handling the calls that you make. |

| Caution | The phone system must forward calls to the Unity
                                                      				Connection pilot number in no fewer than four rings. Otherwise, the test may
                                                      				fail. |
|---|---|

| Field | Setting |
|---|---|
| Enabled | Check this check box to enable MWIs for the test user. |
| Display Name | Accept the default or enter a different name. |
| Inherit User’s Extension | Check this check box to enable MWIs on Phone 1. |

| Step 1 | From Phone 2, enter the access code
                                          			 necessary to get an outside line, and then enter the number outside callers use
                                          			 to dial directly to Unity Connection. |
|---|---|
| Step 2 | In the Port Monitor, note which port handles
                                          			 this call. |
| Step 3 | When you hear the opening greeting, enter
                                          			 the extension for Phone 1. Hearing the opening greeting means that the port is
                                          			 configured correctly. |
| Step 4 | Confirm that Phone 1 rings and that you hear
                                          			 a ringback tone on Phone 2. Hearing a ringback tone means that Unity Connection
                                          			 correctly released the call and transferred it to Phone 1. |
| Step 5 | Leaving Phone 1 unanswered, confirm that the
                                          			 state of the port handling the call changes to “Idle.” This state means that
                                          			 release transfer is successful. |
| Step 6 | Confirm that, after the number of rings that
                                          			 the phone system is set to wait, the call is forwarded to Unity Connection and
                                          			 that you hear the greeting for the test user. Hearing the greeting means that
                                          			 the phone system forwarded the unanswered call and the call-forward information
                                          			 to Unity Connection, which correctly interpreted the information. |
| Step 7 | On the Port Monitor, note which port handles
                                          			 this call. |
| Step 8 | Leave a message for the test user and hang
                                          			 up Phone 2. |
| Step 9 | In the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended. |
| Step 10 | Confirm that the MWI on Phone 1 is
                                          			 activated. The activated MWI means that the phone system and Unity Connection
                                          			 are successfully integrated for turning on MWIs. |

| Step 1 | From Phone 1, enter the internal pilot
                                          			 number for Unity Connection. |
|---|---|
| Step 2 | When asked for your password, enter the
                                          			 password for the test user. Hearing the request for your password means that
                                          			 the phone system sent the necessary call information to Unity Connection, which
                                          			 correctly interpreted the information. |
| Step 3 | Confirm that you hear the recorded name for
                                          			 the test user (if you did not record a name for the test user, you hear the
                                          			 extension number for Phone 1). Hearing the recorded name means that Unity
                                          			 Connection correctly identified the user by the extension. |
| Step 4 | Listen to the message. |
| Step 5 | After listening to the message, delete the
                                          			 message. |
| Step 6 | Confirm that the MWI on Phone 1 is
                                          			 deactivated. The deactivated MWI means that the phone system and Unity
                                          			 Connection are successfully integrated for turning off MWIs. |
| Step 7 | Hang up Phone 1. |
| Step 8 | On the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended. |

| Step 1 | In Cisco Unity Connection Administration, on
                                          			 the Edit Transfer Option page of the test user, in the Transfer Type field,
                                          			 select Supervise Transfer . |
|---|---|
| Step 2 | In the Rings to Wait For field, enter 3 . |
| Step 3 | Select Save . |
| Step 4 | Minimize the Cisco Unity Connection
                                          			 Administration window. Do not close the Unity Connection
                                             				Administration window because you use it again in a later procedure. |

| Step 1 | From Phone 2, enter the access code
                                          			 necessary to get an outside line, and then enter the number outside callers use
                                          			 to dial directly to Unity Connection. |
|---|---|
| Step 2 | On the Port Monitor, note which port handles
                                          			 this call. |
| Step 3 | When you hear the opening greeting, enter
                                          			 the extension for Phone 1. Hearing the opening greeting means that the port is
                                          			 configured correctly. |
| Step 4 | Confirm that Phone 1 rings and that you do
                                          			 not hear a ringback tone on Phone 2. Instead, you should hear the indication
                                          			 your phone system uses to mean that the call is on hold (for example, music). |
| Step 5 | Leaving Phone 1 unanswered, confirm that the
                                          			 state of the port handling the call remains “Busy.” This state and hearing an
                                          			 indication that you are on hold mean that Unity Connection is supervising the
                                          			 transfer. |
| Step 6 | Confirm that, after three rings, you hear
                                          			 the greeting for the test user. Hearing the greeting means that Unity
                                          			 Connection successfully recalled the supervised-transfer call. |
| Step 7 | During the greeting, hang up Phone 2. |
| Step 8 | On the Port Monitor, confirm that the state
                                          			 of the port handling the call changes to “Idle.” This state means that the port
                                          			 was successfully released when the call ended. |
| Step 9 | Select Stop Polling and exit
                                          			 RTMT. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Users and select Users . |
|---|---|
| Step 2 | On the Search Users page, check the check
                                          			 box to the left of the test user. |
| Step 3 | Select Delete Selected . |

| Step 1 | From Phone 1, dial the internal pilot number for Cisco Unity
                                          			 Connection. |
|---|---|
| Step 2 | Confirm that the authentication icon and/or the encryption icon
                                          			 appear on the LCD of the phone. |
| Step 3 | Hang up Phone 1. |