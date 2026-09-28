---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-0100-html-7c5765f599
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_0100.html
retrieved_at: 2026-08-17T02:16:38.787093+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting Call Transfers and Call Forwarding

## Chapter: Troubleshooting Call Transfers and Call Forwarding

# Troubleshooting Call Transfers and Call Forwarding

### Troubleshooting Call Transfers and Call Forwarding

## Calls Not
                        	 Transferred to the Correct Greeting

When calls are not transferred to
                           		the correct greeting, use the following task list to determine the cause and to
                           		resolve the problem.

Following are the tasks to troubleshoot call transfers to wrong
                           		greetings:

Confirm that the forward timer in the phone system is
                                 			 synchronized with the Rings to Wait For setting in Cisco Unity Connection. See
                                 			 the “Confirm
                                    				that Forward Timer in the Phone System is in Synch with the Rings to Wait For
                                    				Setting in Unity Connection” section .

Confirm that the phone system programming enables callers to
                                 			 hear the personal greeting of the user. See the “Confirm
                                    				that Phone System Integration Enables Playing the User Personal Greeting for
                                    				Callers” section .

Confirm that the busy greeting is supported and enabled. See the “Confirming
                                    				that Busy Greeting is Supported and Enabled” section .

Confirm that the caller reaches the intended destination based
                                 			 on the search scope. See the “Confirming
                                    				that Search Scope Configuration Sends Call to Intended Destination”
                                    				section .

Make sure that * or the pattern you want to allow is not
                                 			 mentioned in the Default System Transfer or Default transfer restriction
                                 			 tables. To verify this, navigate to System Settings > Restriction Tables and
                                 			 select the restriction table in which you want to verify the settings.

For call transfer problems that occur on newly installed
                                             				systems, see the applicable Integration Guide for Cisco Unity Connection , at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

If you encounter a call transfer problem that is not described
                           		in this chapter, contact the Cisco Technical Assistance Center (TAC).

### Confirm that Forward Timer in the Phone System is in Synch with the Rings to Wait For Setting in Unity Connection

For supervised transfers, the number of rings that Cisco Unity Connection waits before routing a call to a user personal greeting
                              (or to another extension) can be reconfigured. If the phone system is programmed to forward calls, confirm that the phone
                              system waits longer to forward a call than Unity Connection waits before taking a message.

If the phone system is forwarding the call to another extension before Unity Connection can take a message, the following
                              may occur:

The caller does not hear the beginning of the user personal greeting. (For example, the user greeting is “Hi, this is Maria
                                    Ramirez. Please leave a message after the tone.” But the caller hears only “...message after the tone.”)

The call is forwarded to another phone (for example, the operator) rather than to the personal greeting of the user.

The call is forwarded to the opening greeting.

The caller hears only ringing.

### Synchronizing the Forward Timer and the Rings to Wait For
                           	 Setting

Step 1

In the phone system programming, find and
                                          			 note the setting of the forward timer.

Step 2

In Cisco Unity Connection Administration,
                                          			 expand Users > and select Users . On the Search
                                          			 Users page, select the alias of the user whose calls are not being routed to
                                          			 the correct greeting.

Step 3

On the Edit User Basics page, on the Edit
                                          			 menu, select Transfer Rules .

Step 4

On the Transfer Rules page, select the name
                                          			 of the active transfer rule.

Step 5

On the Edit Transfer Rule page, under
                                          			 Transfer Action, confirm that the Extension or URI option
                                          			 is selected for the Transfer Calls To field and that the extension number is
                                          			 correct.

Step 6

In the Transfer Type list, confirm that Supervise Transfer is
                                          			 selected.

Step 7

In the Rings to Wait For field, the setting
                                          			 should be two rings fewer than the setting of the forward timer of the phone
                                          			 system, which you noted in Step 1 . This setting is
                                          			 typically not greater than four. It specifies the number of rings that Unity
                                          			 Connection waits before routing the call to the personal greeting of the user.

If the settings do not meet the parameters, either reprogram the
                                             				phone system so that it waits longer before forwarding unanswered calls, or
                                             				change the Rings to Wait For field setting so that Unity Connection routes the
                                             				call before the phone system forwards it and select Save.

Step 8

To change the default Rings to Wait For value for future users,
                                          			 expand Templates and select User Templates .

If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made.

Step 9

On the Search User Templates page, select the alias of the user
                                          			 template that you want to change.

If the user template does not appear in
                                                         				  the search results table, set the applicable parameters in the search fields at
                                                         				  the top of the page, and select Find .

Step 10

On the Edit User Template Basics page, on the Edit menu, select Transfer Rules .

Step 11

On the Transfer Rules page, select the name of the active transfer
                                          			 rule.

Step 12

On the Edit Transfer Rule page, under Transfer Action, confirm
                                          			 that the Extension option is
                                          			 selected for the Transfer Calls To field.

Step 13

In the Transfer Type list, confirm that Supervise Transfer is
                                          			 selected.

Step 14

In the Rings to Wait For field, enter the same setting that you
                                          			 entered in Step 7 .

Step 15

Select Save .

### Confirm that Phone System Integration Enables Playing the User Personal Greeting for Callers

When callers hear the opening greeting rather than the user personal greeting, confirm that the phone system integration is
                              correctly set up. If the settings are not correct, call forward to personal greeting and easy message access are not enabled.

### Verifying the Phone System Integration Settings

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations .

Step 2

Confirm that the settings for the phone
                                          			 system, port group, and ports match those indicated in the applicable
                                          			 Integration Guide for Cisco Unity Connection , at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

Step 3

Correct any incorrect settings for the phone
                                          			 system integration.

Step 4

Confirm that the extension that the caller
                                          			 reached is the same as the primary or alternate extension of the user.

Step 5

If callers still hear the opening greeting
                                          			 after dialing the user extension, contact Cisco TAC.

### Confirming that
                           	 Busy Greeting is Supported and Enabled

When a call arrives at a busy extension and is
                              		forwarded to Unity Connection, phone systems typically send the reason for
                              		forwarding (the extension is busy) along with the call.

If Unity Connection does not play the user busy greeting for the
                              		caller, the cause may be one of the following:

The phone system does not provide the necessary call information
                                    			 to support the busy greeting. See the “Integration Functionality” section in
                                    			 the applicable Integration Guide for Cisco Unity Connection , at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html .

The user has not enabled the busy greeting. See the User Guide for the Cisco Unity Connection Phone Interface, Release 14, at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html or the

User Guide for the Cisco Unity Connection Messaging Assistant Web Tool, Release 14, at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/assistant/b_14cucugasst.html .

The alternate greeting for the user is enabled and overrides the busy greeting. See the User Guide for the Cisco Unity Connection
                                    Phone Interface (Release 14) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/phone/b_14cucugphone.html or the User Guide for the Cisco Unity Connection Messaging Assistant Web Tool (Release 14) at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/assistant/b_14cucugasst.html .

### Confirming that
                           	 Search Scope Configuration Sends Call to Intended Destination

If a caller enters digits to transfer to an extension from the
                              		automated attendant or from a user greeting and reaches an unintended
                              		destination, check the search scope of the call at the point where the caller
                              		enters the digits. Unity Connection uses the search scope to match the
                              		extension that the caller dials to an object with this extension, such as a
                              		user, contact, or remote contact at a VPIM location. In particular, if your
                              		dial plan includes overlapping extensions, it is possible for the caller to
                              		enter an extension that matches multiple users or other Unity Connection
                              		objects and be transferred to a different object than the caller expects to
                              		reach.

To make a match by extension, Unity Connection checks the search
                              		space that is currently defined as the search scope for the call. Unity
                              		Connection searches the partitions in this search space in the order that they
                              		appear in the Assigned Partitions list in Cisco Unity Connection
                              		Administration, and returns the first result found.

The search scope of the call when the caller reaches a system
                              		call handler is defined by the Search Scope setting on the Call Handler Basics
                              		page for the handler, and may either be explicitly set to a particular search
                              		space, or may be set to inherit the search space from the call, in which case
                              		it may have been set by a previous handler or by the last call routing rule
                              		that processed the call. When a user greeting is played, the search scope of
                              		the call is defined by the Search Scope setting on the User Basics page for the
                              		user in Cisco Unity Connection Administration.

You can trace the search scope of a call by enabling the CDE
                              		micro trace (level 4 Search Space). For detailed instructions on enabling the
                              		traces and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting .

## Problems with Call Transfers (Cisco Unified Communications Manager Express SCCP Integrations Only)

In Cisco Unified Communications Manager Express SCCP integrations only, call transfers may not work correctly (for example,
                           the call may be dropped or the caller may be left on hold indefinitely). A possible cause for this problem is that the phone
                           system integration is not correctly configured for Cisco Unified Communications Manager Express.

### Configuring the SCCP Integration for Cisco Unified Communications
                           	 Manager Express

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 then select Port Group .

Step 2

On the Search Port Groups page, select the
                                          			 port group name that is used by the Cisco Unified CM Express SCCP integration.

Step 3

On the Port Group Basics page, on the Edit
                                          			 menu, select Servers .

Step 4

Under Cisco Unified Communications Manager
                                          			 Servers, in the Server Type column, select Cisco Unified Communications Manager
                                             				Express and select Save .

## User Hears a Reorder Tone When Answering a Notification Call

Unity Connection requires a minimum Rings to Wait For setting of three rings to properly transfer a call or to make a message
                           notification call. If the number of rings to wait is set to fewer than three for notification devices or call handlers, a
                           user may hear the reorder tone instead of the Unity Connection conversation when called by Unity Connection.

### Correcting the Rings to Wait For Setting

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Users , then select Users . On the Search
                                          			 Users page, select the alias of the user who is hearing a reorder tone when
                                          			 answering a call from Unity Connection.

Step 2

On the Edit User Basics page, on the Edit
                                          			 menu, select Notification Devices .

Step 3

On the Notification Devices page, select the
                                          			 display name of a notification device.

Step 4

On the Edit Notification Device page, under
                                          			 Phone Settings, set the Rings to Wait field to three or more rings and select Save .

Step 5

On the User menu, select Notification Devices .

Step 6

Repeat Step 3 through Step 5 for each remaining
                                          			 notification device.

Step 7

To change the default Rings To Wait value
                                          			 for future users, expand Templates and select User Templates .

If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made.

Step 8

On the Search User Templates page, select
                                          			 the alias of the user template that you want to change.

Step 9

On the Edit User Template Basics page, on
                                          			 the Edit menu, select Notification Devices .

Step 10

On the Notification Devices page, select the
                                          			 display name of a notification device.

Step 11

On the Edit Notification Device page, under
                                          			 Phone Settings, set the Rings to Wait field to three or more rings and select Save .

Step 12

On the User menu, select Notification Devices .

Step 13

Repeat Step 10 through Step 12 for each remaining
                                          			 notification device.

Step 14

Expand Call Management , then
                                          			 select System Call Handlers .

Step 15

On the Search Call Handlers page, select the
                                          			 display name of a call handler.

Step 16

On the Edit Call Handler Basics page, on the
                                          			 Edit menu, select Transfer Rules .

Step 17

View the Standard, Alternate, and Closed
                                          			 rules. In the Transfer Type field, if Supervise Transfer is selected for any of
                                          			 the rules, confirm that the Rings to Wait For field is set to three or more
                                          			 rings.

If Rings to Wait For is set correctly, and
                                             				the user still hears a reorder tone when answering a call from Unity
                                             				Connection, contact Cisco TAC.

## Troubleshooting
                        	 Directory Handler Searches

Use the troubleshooting information in this section if
                           		callers report that they are unable to locate one or more users in a directory
                           		handler. See the following possible causes:

The users are not configured to be listed in the directory.
                                 			 Verify the List in Directory setting on the Edit User Basics page for each user
                                 			 in Cisco Unity Connection Administration is selected, or use Bulk Edit to
                                 			 configure the setting for multiple users at the same time.

The search scope of the directory handler does not include the
                                 			 users. See the “Users
                                    				Not Found in the Search Scope of Directory Handler” section on page 5-6 .

For voice-enabled directory handlers, the voice-recognition
                                 			 engine does not recognize the names. See the Voice Commands Recognized But Names Not Recognized .

### Users Not Found in the Search Scope of Directory Handler

If callers are unable to find specific users in a directory handler, check the search scope of the directory handler on the
                              Edit Directory Handler Basics page in Cisco Unity Connection Administration. The search scope of a phone directory handler
                              can be set to the entire server; to a specific class of service, system distribution list or search space; or to the search
                              space of the call at the point that the caller reaches the directory handler. The search scope of a voice-enabled directory
                              handler can be set to the entire server, to a specific search space, or to the search space of the call at the point that
                              the caller reaches the directory handler.

If the search scope is set to the entire server, the user or users must be homed on the server on which the directory handler
                              resides in order to be reachable from the directory handler.

If the search scope is set to a specific class of service, system distribution list, or search space, you can use Connection Administration
                              to determine whether the target users belong to the class of service or distribution list or to a partition that is a member
                              of the search space.

If the search scope is set to inherit the search space from the call, determine which search scope is in use when callers
                              have difficulty reaching users in the directory handler. Note that depending on how the call comes in to the system and is
                              routed, the search scope can differ from one call to another and can change during the course of the call. See the “Using Traces to Determine the Search Space Used During a Call” section on page 5-8 for instructions on using traces to determine the inherited search scope.

## Troubleshooting
                        	 Message Addressing

Message addressing involves the ability to
                           		select a desired recipient or recipients when creating a new message. This
                           		section covers some problems that the users might experience with message
                           		addressing:

For additional information about troubleshooting message
                                       		  addressing when it involves remote recipients at VPIM locations or at other
                                       		  digitally networked Unity Connection locations, see the Troubleshooting Networking chapter.

### Users Unable to Address Desired Recipients

If a user is unable to find one or more desired recipients when attempting to address a message, start by verifying that the
                              recipient user or contact account exists and that the name spelling or extension that the user is entering is correct.

If the user is attempting to blind address a message to a VPIM location by entering a number that is made up of the VPIM location
                              DTMF Access ID and the mailbox number of the recipient, or by saying the digits of the mailbox number and the display name
                              of the VPIM location (for example, “five five at Seattle office”), confirm that blind addressing is enabled for the VPIM location
                              by checking the Allow Blind Addressing check box on the VPIM Location page in Cisco Unity Connection Administration.

If you have verified that the recipient account exists and matches the user search criteria or that blind addressing is enabled,
                              and the user still cannot address to the desired recipient, the most likely cause is that the user search space does not include
                              the partition of the target user, VPIM contact, or VPIM location. If the VPIM contact partition does not match the partition
                              of the VPIM location to which the contact belongs, the search results depend on the method used to address the message as
                              well as the partition and search space configuration. When users address messages to a VPIM mailbox by entering a VPIM location
                              DTMF Access ID plus a remote user mailbox number, or when voice-recognition users say a name and location (for example, “John
                              Smith in Seattle”), the action is allowed or denied based on the partition of the VPIM location. However, when users address
                              to a VPIM contact using spell-by-name or by entering the local extension of the contact, or when voice-recognition users say
                              the name of a contact without the location (for example, “John Smith”), the action is allowed or denied based on the partition
                              of the VPIM contact, regardless of whether the partition of the VPIM location is out of scope for the user.

### Users Unable to Address a System Distribution List

When a user cannot address messages to a system distribution list, consider the following possible causes:

The user must be given the correct class of service rights on the Class of Service > Edit Class of Service page in Cisco Unity
                                    Connection Administration. The class of service that the user is assigned to must have the Allow Users to Send Messages to
                                    System Distribution Lists check box checked.

The user must know how to address to the list. If the user is using the phone keypad conversation, the user can enter the
                                    display name or extension of the list. If the user is using the voice-recognition conversation, the user can say the display
                                    name or one of the alternate names defined for the list in Connection Administration.

As with other types of addressing, in order for a user to address messages to a system distribution list, the list must belong
                                    to a partition that is a member of the search space that is defined as the user search scope. Note that the distribution list
                                    members receive the message regardless of whether they are individually addressable in the search scope of the sending user.

### Unexpected Results Returned When a User Addresses by Extension

If a user addresses a message by extension and hears an unexpected match, the most common cause can be the search space configuration.
                              To make a match by extension, Unity Connection checks the search space of the user who is addressing the message. Unity Connection
                              searches the partitions in this search space in the order that they appear in the Assigned Partitions list in Cisco Unity
                              Connection Administration, and returns the first result found. If your dial plan includes overlapping extensions, it is possible
                              for the user to enter an extension that matches multiple users or other Unity Connection objects and hear a match result that
                              is different from what the user expects.

To resolve the issue, you may need to review the order of partitions in the search space that is assigned to the user, either
                              in Connection Administration or using the Dial Plan Report and Dial Search Scope Report in Cisco Unity Connection Serviceability.
                              If the search space is set up correctly according to your dial plan, you can recommend that the user address messages by spelling
                              or saying the name of the recipient; in this case, if there are multiple matches on the name, Unity Connection returns each
                              match.

## Caller is Not Getting Prompt in Expected Language

If a caller is not get prompt in expected language, check the following:

If the locales are installed on both the servers in case of a
                                 			 cluster.

If the caller is an outside caller for unity connection, then he
                                 			 will always listen prompts in system default language of that unity connection.

If the call handler language settings of the caller is set to
                                 			 “Inherit Language from Caller”, then for an internal caller, the prompts are
                                 			 played in the caller set language.

If the caller is an Unity Connection user and logs in to his/her
                                 			 mailbox, then the caller always listen prompts in caller set language.

## Using Traces to
                        	 Determine the Search Space Used During a Call

The search scope of a call is initially set to a particular
                           		search space by the call routing rule that first processes the call, although
                           		the scope may change during the course of the call.

To determine which search space is being used at each point in a
                           		call, enable the CDE micro trace (level 4 Search Space). For detailed
                           		instructions on enabling the traces and viewing the trace logs, see the Using Diagnostic Traces for Troubleshooting .

| Note | For call transfer problems that occur on newly installed
                                             				systems, see the applicable Integration Guide for Cisco Unity Connection , at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html . |
|---|---|

| Step 1 | In the phone system programming, find and
                                          			 note the setting of the forward timer. |
|---|---|
| Step 2 | In Cisco Unity Connection Administration,
                                          			 expand Users > and select Users . On the Search
                                          			 Users page, select the alias of the user whose calls are not being routed to
                                          			 the correct greeting. |
| Step 3 | On the Edit User Basics page, on the Edit
                                          			 menu, select Transfer Rules . |
| Step 4 | On the Transfer Rules page, select the name
                                          			 of the active transfer rule. |
| Step 5 | On the Edit Transfer Rule page, under
                                          			 Transfer Action, confirm that the Extension or URI option
                                          			 is selected for the Transfer Calls To field and that the extension number is
                                          			 correct. |
| Step 6 | In the Transfer Type list, confirm that Supervise Transfer is
                                          			 selected. |
| Step 7 | In the Rings to Wait For field, the setting
                                          			 should be two rings fewer than the setting of the forward timer of the phone
                                          			 system, which you noted in Step 1 . This setting is
                                          			 typically not greater than four. It specifies the number of rings that Unity
                                          			 Connection waits before routing the call to the personal greeting of the user. If the settings do not meet the parameters, either reprogram the
                                             				phone system so that it waits longer before forwarding unanswered calls, or
                                             				change the Rings to Wait For field setting so that Unity Connection routes the
                                             				call before the phone system forwards it and select Save. |
| Step 8 | To change the default Rings to Wait For value for future users,
                                          			 expand Templates and select User Templates . Note If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. | Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
| Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
| Step 9 | On the Search User Templates page, select the alias of the user
                                          			 template that you want to change. Note If the user template does not appear in
                                                         				  the search results table, set the applicable parameters in the search fields at
                                                         				  the top of the page, and select Find . | Note | If the user template does not appear in
                                                         				  the search results table, set the applicable parameters in the search fields at
                                                         				  the top of the page, and select Find . |
| Note | If the user template does not appear in
                                                         				  the search results table, set the applicable parameters in the search fields at
                                                         				  the top of the page, and select Find . |
| Step 10 | On the Edit User Template Basics page, on the Edit menu, select Transfer Rules . |
| Step 11 | On the Transfer Rules page, select the name of the active transfer
                                          			 rule. |
| Step 12 | On the Edit Transfer Rule page, under Transfer Action, confirm
                                          			 that the Extension option is
                                          			 selected for the Transfer Calls To field. |
| Step 13 | In the Transfer Type list, confirm that Supervise Transfer is
                                          			 selected. |
| Step 14 | In the Rings to Wait For field, enter the same setting that you
                                          			 entered in Step 7 . |
| Step 15 | Select Save . |

| Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
|---|---|

| Note | If the user template does not appear in
                                                         				  the search results table, set the applicable parameters in the search fields at
                                                         				  the top of the page, and select Find . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations . |
|---|---|
| Step 2 | Confirm that the settings for the phone
                                          			 system, port group, and ports match those indicated in the applicable
                                          			 Integration Guide for Cisco Unity Connection , at http://www.cisco.com/en/US/products/ps6509/products_installation_and_configuration_guides_list.html . |
| Step 3 | Correct any incorrect settings for the phone
                                          			 system integration. |
| Step 4 | Confirm that the extension that the caller
                                          			 reached is the same as the primary or alternate extension of the user. |
| Step 5 | If callers still hear the opening greeting
                                          			 after dialing the user extension, contact Cisco TAC. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Telephony Integrations ,
                                          			 then select Port Group . |
|---|---|
| Step 2 | On the Search Port Groups page, select the
                                          			 port group name that is used by the Cisco Unified CM Express SCCP integration. |
| Step 3 | On the Port Group Basics page, on the Edit
                                          			 menu, select Servers . |
| Step 4 | Under Cisco Unified Communications Manager
                                          			 Servers, in the Server Type column, select Cisco Unified Communications Manager
                                             				Express and select Save . |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Users , then select Users . On the Search
                                          			 Users page, select the alias of the user who is hearing a reorder tone when
                                          			 answering a call from Unity Connection. |
|---|---|
| Step 2 | On the Edit User Basics page, on the Edit
                                          			 menu, select Notification Devices . |
| Step 3 | On the Notification Devices page, select the
                                          			 display name of a notification device. |
| Step 4 | On the Edit Notification Device page, under
                                          			 Phone Settings, set the Rings to Wait field to three or more rings and select Save . |
| Step 5 | On the User menu, select Notification Devices . |
| Step 6 | Repeat Step 3 through Step 5 for each remaining
                                          			 notification device. |
| Step 7 | To change the default Rings To Wait value
                                          			 for future users, expand Templates and select User Templates . Note If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. | Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
| Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
| Step 8 | On the Search User Templates page, select
                                          			 the alias of the user template that you want to change. |
| Step 9 | On the Edit User Template Basics page, on
                                          			 the Edit menu, select Notification Devices . |
| Step 10 | On the Notification Devices page, select the
                                          			 display name of a notification device. |
| Step 11 | On the Edit Notification Device page, under
                                          			 Phone Settings, set the Rings to Wait field to three or more rings and select Save . |
| Step 12 | On the User menu, select Notification Devices . |
| Step 13 | Repeat Step 10 through Step 12 for each remaining
                                          			 notification device. |
| Step 14 | Expand Call Management , then
                                          			 select System Call Handlers . |
| Step 15 | On the Search Call Handlers page, select the
                                          			 display name of a call handler. |
| Step 16 | On the Edit Call Handler Basics page, on the
                                          			 Edit menu, select Transfer Rules . |
| Step 17 | View the Standard, Alternate, and Closed
                                          			 rules. In the Transfer Type field, if Supervise Transfer is selected for any of
                                          			 the rules, confirm that the Rings to Wait For field is set to three or more
                                          			 rings. If Rings to Wait For is set correctly, and
                                             				the user still hears a reorder tone when answering a call from Unity
                                             				Connection, contact Cisco TAC. |

| Note | If you change settings in a user template,
                                                         				  the settings are not changed for existing users whose accounts were created
                                                         				  from that template. Changing the template settings affects only the users who
                                                         				  are added after the template changes are made. |
|---|---|

| Note | For additional information about troubleshooting message
                                       		  addressing when it involves remote recipients at VPIM locations or at other
                                       		  digitally networked Unity Connection locations, see the Troubleshooting Networking chapter. |
|---|---|