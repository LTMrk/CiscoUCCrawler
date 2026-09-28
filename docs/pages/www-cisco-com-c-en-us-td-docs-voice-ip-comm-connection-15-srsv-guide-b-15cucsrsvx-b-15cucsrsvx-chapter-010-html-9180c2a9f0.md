---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-srsv-guide-b-15cucsrsvx-b-15cucsrsvx-chapter-010-html-9180c2a9f0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/srsv/guide/b_15cucsrsvx/b_15cucsrsvx_chapter_010.html
retrieved_at: 2026-08-16T18:46:51.797748+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: December 18, 2023

Chapter: Cisco Unity Connection SRSV Administration

## Chapter: Cisco Unity Connection SRSV Administration

# Cisco Unity Connection SRSV Administration

## Introduction

Cisco Unity Connection SRSV Administration is the web interface used for managing the administrative tasks, such as configuring
                           subscribers or implementing a call management plan on the branch (Unity Connection SRSV) server.

## Users

There are two types of users in a Unity Connection SRSV server:

Users

Definition

Administrators

The administrators are the users privileged to login in to Cisco Unity Connection SRSV Administration. The administrator users
                                          created on Unity Connection SRSV are not synchronized with the central Cisco Unity Connection server.

Subscribers

The subscribers are the remote users created on the central Unity Connection server and synchronized with the Unity Connection
                                          SRSV server.

You cannot modify any subscriber related information on the branch server. If any update is required, it should be done on
                                                      the central Unity Connection server.

### Finding Users

Cisco Unity Connection SRSV Administration allows you to find users based on the search criteria you enter. You can search
                              the Administrators and the Subscribers on Unity Connection SRSV using the Search feature. The Search Administrators page lists
                              the administrator users and you can search a particular administrator name from the list. The Search Subscribers page lists
                              all the subscribers available in Unity Connection SRSV.

The search results, by default, returns all the administrators detail. By default, the administrator can view 25 records per
                              page and can select rows per page from the drop-down list. The maximum limit is 250 search results on one page. The administrator
                              can perform custom search on the Name field using the following options:

Begins with

Contains

Ends with

Is Exactly

Is Empty

Is Not Empty

### Configuring an Administrator Account in Cisco Unity Connection SRSV
                           	 Administration

You can create, modify, or delete administrator
                                 		  accounts using Cisco Unity Connection SRSV Administration. However, you cannot
                                 		  modify or delete default administrator accounts.

Step 1

In Cisco Unity Connection SRSV
                                          			 Administration, expand Users > and select > Administrators . The Search Administrators page displays the currently
                                          			 configured administrators.

Step 2

Configure an administrator (For more
                                          			 information on each field, see Help> This Page):

To add an administrator account:

On the Search Administrators page, select Add New .

On the New Administrator page, enter the
                                       				values of the required fields and select Save.

To edit an existing administrator account:

On the Search Administrators page, select
                                       				the applicable administrator account.

On the Edit Administrator page, modify the
                                       				values of the required fields and select Save.

On the Edit Administrator page, select Edit
                                       				and then either select Change Password or Roles.

On the Change Password page or Edit Roles
                                       				page, modify the value of the required fields and select Save.

To delete an existing administrator account:

On the Search Administrator page, check the
                                       				check boxes to select the applicable administrator accounts that you want to
                                       				delete.

Select Delete Selected and OK to confirm
                                       				deletion.

## Templates

Each call handler that you add in Unity Connection SRSV is based on a template. Settings from the call handler template are
                           applied on a call handler. Most of the call handler settings are applied using the default call handler template. The administrator
                           is allowed to create new templates.

Before you create call handlers, review the settings in the template that you plan to use and determine whether you need to
                           make changes or create new templates. For each template, you should consider enabling the transfer, caller input, greetings,
                           and message settings that are needed for the call handlers that you plan to create. Note that if you change settings on a
                           call handler template, the new settings are applicable only for new call handlers that are created using that template. Changes
                           to template settings do not affect existing call handlers.

Deleting a call handler template does not affect the existing call handler settings based on that template.

### Configuring a Call
                           	 Handler Template in Cisco Unity Connection SRSV Administration

You can create, modify, or delete the new call handler templates
                                 		  using Cisco Unity Connection SRSV Administration. However, you cannot modify or
                                 		  delete the existing call handler templates.

Step 1

In Cisco Unity Connection SRSV Administration, expand Templates > and select > Call Handler
                                                				  Templates . The Search Call Handler Templates page
                                          			 displays the currently configured call handler templates.

Step 2

Configure a call handler template (For more information on each
                                          			 field, see Help> This Page):

To add a call handler template:

On the Search Call Handler Templates page, select Add New .

On the New Call Handler Templates page, enter the values of the
                                                         						  required fields and select Save.

To edit an existing call handler template:

On the Search Call Handler Templates page, select the applicable
                                                         						  call handler template.

On the Edit Call Handler Templates page, modify the values of
                                                         						  the required fields and select Save.

On the Edit Call Handler Templates page, in the Edit menu,
                                                         						  select any of the following settings that you want to edit and then select
                                                         						  Save:

Transfer Rules

Caller Input

Greetings

Message Settings

For more information on call
                                                                           								  handler template settings, see the Call Handler Settings, page 3-5 section.

To delete an existing call handler template:

On the Search Call Handler Templates page, check the check boxes
                                                         						  to select the applicable call handler templates that you want to delete.

Select Delete Selected and OK to confirm deletion.

## Distribution Lists

System distribution lists are used to send voicemails to multiple users. The members of a system distribution list typically
                           are the 	users who need the same information on a regular basis, such as employees in a department or members of a team. On
                           the branch server, sending a message to a distribution list is supported only when the distribution list is selected in the
                           Message Recipient property of the call handler.

When you send a message to a distribution list, you receive the notification confirming that the message has been sent to
                           the distribution list. However, the members of the distribution list receive the message only after the restoration of WAN
                           outage and successful upload of the message on the central Unity Connection server.

Composing a new message that is addressed to a distribution list is not supported on the branch server.

You cannot create, modify, or delete any distribution list related information on the branch server. If an update is required,
                           then it should be done at the central Unity Connection server.

## Call Management

The call management plan describes how the handlers connect to one another through the telephony user interface. Cisco Unity
                           Connection SRSV Administration includes a menu of one-key dialing options and all possible navigation choices configurable
                           by the Connection SRSV subscribers, such as reaching a call handler by dialing an extension or via a routing rule.

### System Call
                           	 Handlers

Unity Connection SRSV provides three predefined call handlers that can be modified but not deleted. For more information on
                              the predefined call handlers, see the “ Default System Call Handlers ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection, Release 15, available
                              at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

### To Configure a
                           	 Call Handler in Cisco Unity Connection SRSV Administration

After you have created or updated the call handler templates
                                 		  that you plan to use, you are ready to create call handlers. After a call
                                 		  handler has been created, you may need to adjust the settings. The tools in
                                 		  Cisco Unity Connection SRSV Administration allows you to modify either a single
                                 		  call handler or multiple call handlers at a time.

Step 1

In Cisco Unity Connection SRSV Administration, expand Call Management and select System Call Handlers . The Search Call Handlers page
                                          			 displays the currently configured call handlers.

Step 2

Configure a call handler (For more information on each field,
                                          			 see Help> This Page):

To add a call handler:

On the Search Call Handlers page, select Add New .

On the New Call Handlers page, enter the values of the required
                                                         						  fields and select Save.

To edit an existing call handler:

On the Search Call Handlers page, select the applicable call
                                                         						  handler.

On the Edit Call Handler page, modify the values of the required
                                                         						  fields and select Save.

On the Edit Call Handler page, in the Edit menu, select any of
                                                         						  the following settings that you want to edit and then select Save:

Transfer Rules

Caller Input

Greetings

Message Settings

For more information on
                                                                           								  call handler settings, see the Call Handler Settings, page 3-5 section.

To delete an existing call handler:

On the Search Call Handlers page, check the check boxes to
                                                         						  select the applicable call handler that you want to delete.

Select Delete Selected and OK to confirm deletion.

### Call Handler Settings

Following are the settings applicable to both call handler templates and call handlers:

#### Transfer Rules

The system transfers allow callers to dial numbers not associated with a user, contact, call handler, or other entity. For
                                 example, when a user calls into a Unity Connection SRSV voicemail system, the call from auto attendant is transferred to a
                                 call handler. The call handler can transfer calls to a number of extensions, such as a lobby extension or a conference room
                                 extension.

The call transfer settings of a call handler specifies how Unity Connection SRSV transfers calls. The calls reaches the call
                                 handler through the automated attendant. Following are the three transfer rules that you can customize in Unity Connection
                                 SRSV:

Standard

Closed (non business and holiday hours of active schedule)

Alternate

The alternate transfer rule, when enabled, overrides the standard and closed transfer rules and is in effect at all times.

When a call is transferred to the call handler, Unity Connection SRSV first checks the applicable transfer rule to determine
                                 where to transfer the call—either to the call handler greeting, or to an extension.

While transferring the call to the call handler greeting, Unity Connection SRSV plays the applicable greeting (standard, closed,
                                 holiday, internal, busy, or alternate) based on the situation and the greetings that are enabled for that duration. Transfer
                                 rules can be configured to provide the callers with a prerecorded menu of options or an informational message by transferring
                                 the call to the applicable greeting.

To route callers to a specific user or to another call handler, you configure the transfer rule to transfer the call to the
                                 extension of the user or the call handler. When transferring a call to a user extension, Unity Connection SRSV can either
                                 release the call to the phone system, or it can supervise the transfer. When Unity Connection SRSV is set to supervise transfers,
                                 it can provide call screening and call holding options on indirect calls as mentioned below:

With call screening, Unity Connection SRSV can ask for the name of the caller before connecting to a user. The user can then
                                       hear who is calling and can accept or refuse the call depending on who the call is for.

With call holding, when the phone is busy, Unity Connection SRSV can ask callers to hold. Each caller on hold uses a Unity
                                       Connection SRSV port and a phone system port, and therefore the total number of callers that can be holding in the queue at
                                       a single point of time is limited by the number of available ports.

The default wait time in the call holding queue for the first caller in the queue is 25 seconds. If the caller is still on
                                 hold after this amount of time, Unity Connection SRSV asks whether the caller wants to continue holding, leave a message,
                                 or try another extension. If the caller does not press a key on the phone keypad or say a voice command to indicate that he
                                 or she wants to continue holding, leave a message, or dial another extension, the caller is transferred back to the Opening
                                 Greeting. Subsequent callers in the holding queue are told how many other callers are in the queue ahead of them, in addition
                                 to these options.

#### Caller Input

Caller input settings define actions that Unity Connection SRSV takes in response to phone keys pressed by callers during
                                 a call handler greeting. Using the settings on the Edit Greeting page for any greeting, you can also specify whether the greeting
                                 allows caller input and whether callers can perform transfers. Alternatively, you can define caller input keys and options
                                 that apply to all the call handler greetings using the Caller Input page for the call handler.

One-key dialing enables you to designate a single digit to represent a user extension, alternate contact number, call handler,
                                 interview handler, or directory handler. Instead of entering the full extension, the caller presses a single key during a
                                 call handler greeting and Unity Connection SRSV responds accordingly. By specifying different keys as caller input options,
                                 you can offer callers a menu of choices in the call handler greeting.

Configuring the transfer to alternate contact number action on one or more keys of a call handler allows you to quickly set
                                 up a simple audio-text tree that callers can use to transfer to specific non-user extensions on the phone system or to specific
                                 external numbers, without having to create separate call handlers for each number. When transferring a caller to an alternate
                                 contact number, Unity Connection SRSV can either supervise the transfer or release the call to the phone system.

Callers can also bypass one-key dialing. You set the system to pause a certain number of seconds for additional key presses
                                 before routing the call according to the one-key dialing menu you have set up. These pauses allow callers to press full extension
                                 IDs to bypass one-key dialing menus, even during the handler greeting.

Further, you can lock certain keys to take the caller directly to the action programmed for that key without waiting for an
                                 additional key press.

You should not lock any key that matches the first digit of user extensions; otherwise, callers are not able to enter an extension
                                             to reach a user.

You can simulate abbreviated extensions using prepended digits for call handlers and user mailboxes. When such digits are
                                 defined, they are prepended to any extension that a caller dials while listening to the greeting for the call handler or user
                                 mailbox.

Unity Connection SRSV first attempts to route the call to the prepended extension. If the prepended extension is not valid,
                                 Unity Connection SRSV attempts to route the call to the dialed extension. In the following example, the call handler named
                                 Sales is configured with the prepended digits 123. When a caller dials 1000 while listening to the greeting for the Sales
                                 call handler, Unity Connection SRSV attempts to route the call to extension 1231000; if the prepended extension is not valid,
                                 Unity Connection SRSV attempts to route the call to extension 1000. (Note that if extension 1000 is not a valid extension
                                 and the greeting for the Sales call handler is configured to allow transfers to numbers not associated with users or call
                                 handlers, Unity Connection SRSV performs a release transfer to 1231000.)

Abbreviated extensions can be used as a way for an organization to segment users into different groups. For example, suppose
                                 a company has two departments: Engineering and Marketing. The company uses six digit extensions, and all extensions in Engineering
                                 begin with 10 and all extensions in Marketing begin with 11. Call handlers could be created for Engineering and for Marketing,
                                 and each call handler could be configured to prepend a 10 or a 11, as applicable, to any extension dialed from that call handler.
                                 When set up this way, users would only have to enter the last four digits of a user extension.

#### Greetings

Each call handler can have up to seven greetings. The greeting settings specify which greetings are enabled, how long they
                                 are enabled, the greeting source, and the actions that Unity Connection SRSV takes during and after each greeting. When a
                                 greeting is enabled, Unity Connection SRSV plays the greeting in the applicable situation until the specified date and time
                                 arrives, and then the greeting is automatically disabled. A greeting can also be enabled to play indefinitely.

Call handler greetings can be recorded in multiple languages.

You can customize how Unity Connection SRSV handles calls to call handlers that have the alternate greeting enabled.

Following are the functionalities supported by Unity Connection SRSV with an alternate greeting enabled:

Transfer callers directly to the greeting without ringing the extension that is assigned to the call handler (as applicable)
                                       whenever calls are transferred from the automated attendant or a directory handler to the user extension. (The phone rings
                                       if an outside caller or another Unity Connection SRSV user dials a user extension directly.)

Prevents all callers from skipping the greeting.

Prevents all callers from leaving messages (when the call handler is set up to take message).

Unity Connection SRSV plays the greetings that you customized according to the requirements but some greetings override other
                                                   greetings when they are enabled during that duration.

The below table describes how greetings work when a call is placed:

Standard

Plays at all times unless overridden by another greeting. You cannot disable the standard greeting.

Closed

Plays during the closed (non-business) hours defined for the active schedule. A closed greeting overrides the standard greeting,
                                             and thus limits the standard greeting to the open hours defined for the active schedule.

Error

Plays if the caller enters invalid digits. This can happen if the digits do not match an extension, the extension is not found
                                             in the search scope, or the caller is otherwise restricted from dialing the digits. You cannot disable the error greeting.

The system default error recording is, “I did not recognize that as a valid entry.” By default, after the error greeting plays,
                                             Unity Connection replays the greeting that was playing when the caller entered the invalid digits.

Call handler owners can select a different call handler greeting or record the call handler greetings either from the System
                                 Call Handlers > Greetings page in Cisco Unity Connection SRSV Administration or using the Cisco Unity Greetings Administrator
                                 on a phone.

#### Message Settings

The message settings for a particular call handler greeting allows you to do the following:

Configure the call handler to take a message after playing the greeting.

You can specify who receives messages for the call handler, whether messages are marked for dispatch delivery.

Define the maximum recording length for messages from outside callers.

Decide what callers can do when leaving messages, whether the messages are automatically marked secure, and what action to
                                       take next on a call after a message is left.

For some integrations, you can set up Unity Connection SRSV so that as a caller records a message, a warning prompt is played
                                                   before the caller reaches the maximum allowable message length.

### Directory Handlers

You cannot create or delete directory handlers on the branch server. However, you can update the settings, if required.

#### Modifying a Directory Handler in Cisco Unity Connection
                              	 Administration

Step 1

In Cisco Unity Connection SRSV
                                             			 Administration, expand Call Management and
                                             			 select Directory Handlers . The
                                             			 Search Directory Handlers page displays the currently configured directory
                                             			 handlers.

Step 2

To edit a directory handler (For more
                                             			 information on each field, see Help> This Page):

On the Search Directory Handlers page,
                                                   				  select the applicable directory handler that you want to update.

On the Edit Directory Handler page,
                                                   				  enter the values of the required fields and select Save.

On the Edit Directory Handler page, in
                                                   				  the Edit menu, select any of the following settings that you want to edit and
                                                   				  then select Save:

Caller Input

Greetings

## Networking

A branch server can be connected only to a single Unity Connection server. The Central Server Configuration page allows you
                           to configure the IP address of the central Unity Connection server.

### To Configure the Central Unity Connection Server

Step 1

In Cisco Unity Connection SRSV
                                          			 Administration, expand Networking > and select Central Server
                                             				Configuration .

Step 2

On the Central Server Configuration page,
                                          			 enter the values of the required fields and select Save . (For information
                                          			 on each field, see Help> This Page).

System Settings

## Schedules

The Search Schedules page displays the default schedules configured on the central Unity Connection server. You can create,
                           modify, or delete schedules on the branch server.

You cannot delete the default schedules on the branch server.

### Configuring
                           	 Schedules in Cisco Unity Connection SRSV Administration

Step 1

In Cisco Unity Connection SRSV Administration, expand System
                                          			 Settings and select Schedules. The Search Schedules page displays the currently
                                          			 configured schedules.

Step 2

Configure a schedule (For more information on each field, see
                                          			 Help> This Page):

To add a schedule:

On the Search Schedules page, select Add New.

On the New Schedule page, enter the Display Name and select
                                                         						  Save.

In the Schedule Details menu, select Add New to enter the
                                                         						  schedule specifications and select Save.

To edit a schedule:

On the Search Schedule page, select the schedule you want to
                                                         						  modify.

On the Edit Schedule Basics page, modify the values of the
                                                         						  required fields and select Save.

To delete a schedule:

On the Search Schedule page, check the check boxes to select the
                                                         						  schedules that you want to delete.

Select Delete Selected and OK to confirm deletion.

## Conversations

The Conversation Configuration page allows you to configure multiple IP address to connect to the Port Status Monitor and
                           to enable the Port Status Monitor output. For more information on each field, see Help> This Page.

## Enterprise Parameters

Enterprise parameters for Unity Connection SRSV provide default settings that apply to all services in Cisco Unified Serviceability.
                           You cannot add or delete enterprise parameters.You can update the existing enterprise parameters.

Many of the enterprise parameters rarely require change. Do not change an enterprise parameter unless you completely understand
                                       the feature you are changing or the Cisco Technical Assistance Center (Cisco TAC) specifies the change.

### Configuring Enterprise Parameters in Cisco Unified
                           	 Serviceability

Step 1

In Cisco Unity Connection SRSV
                                          			 Administration, expand System Settings and select Enterprise Parameters.

Step 2

On the Enterprise Parameters page, enter the
                                          			 applicable settings. To set all service parameters to the default values,
                                          			 select Set to Default.

Step 3

To view a list of enterprise parameters and
                                          			 descriptions, select the ? button on the right side of the page and select
                                          			 Save. (For more information on each field, see Help> This Page).

## Plugins

Application plugins extend the functionality of Unity Connection SRSV. For example, the Real-Time Monitoring Tool (RTMT) allows
                           you to monitor the health of the system remotely through tools, such as, performance-monitoring counters and Port Monitor.

Before you install any plugin, you must disable all intrusion detection or anti-virus services that run on the server where
                                       you install the plugin.

### Installing a Plugin

Step 1

In Cisco Unity Connection SRSV
                                          			 Administration, expand System Settings and select Plugins.

Step 2

On the Search Plugins page, select Find.

Step 3

For the plugin that you want to install,
                                          			 select Download and follow the on-screen instructions for installing the
                                          			 plugin.

## Telephony Integrations

Telephony integration allows the callers to leave messages for the users and access messages left between the branch server
                           and the phone system.

### Phone System

You cannot create or delete phone system integrations on a branch server.

#### Modifying Phone System Integration

Step 1

In Cisco Unity Connection SRSV
                                             			 Administration, expand Telephony Integrations and select Phone System.

Step 2

On the Search Phone Systems page, select the
                                             			 phone system that you want to modify.

Step 3

On the Phone System Basics page, modify the
                                             			 values of the required fields and select Save. (For information on each field,
                                             			 see Help> This Page).

### Port Group

You can create, modify, or delete the port groups on a branch server. For more information on port group, see the “ Port Group ” section of the “Telephony Integrations” chapter in the System Administration Guide for Cisco Unity Connection, Release 15,
                              available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

You need to configure the port group for a branch server on
                                          		  Cisco Unity Connection SRSV Administration.

### Port

You can create, modify, or delete ports on a branch server. For more information on ports, see the “ Port ” section of the “Telephony Integrations” chapter of the System Administration Guide for Cisco Unity Connection, Release 15,
                              available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

You need to configure the ports for a branch server on
                                          		  Cisco Unity Connection SRSV Administration.

### Security

You can generate new certificates and security profiles on a branch server when Cisco Unified Communications Manager is authenticated
                              and encrypted for Unity Connection SRSV voicemail ports. For more information on security, see the “ Security ” section of the “Telephony Integrations” chapter of the System Administration Guide for Cisco Unity Connection, Release 15,
                              available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag/b_15cucsag_chapter_0110.html .

You need to configure the certificates for a branch server on
                                          		  Cisco Unity Connection SRSV Administration.

## Tools

Cisco Unity Connection SRSV Administration on the branch server allows you to modify the settings of the custom keypad mapping
                           tool originally configured on a central Unity Connection server. For more information on custom keypad mapping, see the “ Custom Keypad Mapping Tool ” section of the “Tools” chapter of the System Administration Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

| Users | Definition |
|---|---|
| Administrators | The administrators are the users privileged to login in to Cisco Unity Connection SRSV Administration. The administrator users
                                          created on Unity Connection SRSV are not synchronized with the central Cisco Unity Connection server. |
| Subscribers | The subscribers are the remote users created on the central Unity Connection server and synchronized with the Unity Connection
                                          SRSV server. Note You cannot modify any subscriber related information on the branch server. If any update is required, it should be done on
                                                      the central Unity Connection server. | Note | You cannot modify any subscriber related information on the branch server. If any update is required, it should be done on
                                                      the central Unity Connection server. |
| Note | You cannot modify any subscriber related information on the branch server. If any update is required, it should be done on
                                                      the central Unity Connection server. |

| Note | You cannot modify any subscriber related information on the branch server. If any update is required, it should be done on
                                                      the central Unity Connection server. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV
                                          			 Administration, expand Users > and select > Administrators . The Search Administrators page displays the currently
                                          			 configured administrators. |
|---|---|
| Step 2 | Configure an administrator (For more
                                          			 information on each field, see Help> This Page): |

| Note | Deleting a call handler template does not affect the existing call handler settings based on that template. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV Administration, expand Templates > and select > Call Handler
                                                				  Templates . The Search Call Handler Templates page
                                          			 displays the currently configured call handler templates. |
|---|---|
| Step 2 | Configure a call handler template (For more information on each
                                          			 field, see Help> This Page): To add a call handler template: On the Search Call Handler Templates page, select Add New . On the New Call Handler Templates page, enter the values of the
                                                         						  required fields and select Save. To edit an existing call handler template: On the Search Call Handler Templates page, select the applicable
                                                         						  call handler template. On the Edit Call Handler Templates page, modify the values of
                                                         						  the required fields and select Save. On the Edit Call Handler Templates page, in the Edit menu,
                                                         						  select any of the following settings that you want to edit and then select
                                                         						  Save: Transfer Rules Caller Input Greetings Message Settings Note For more information on call
                                                                           								  handler template settings, see the Call Handler Settings, page 3-5 section. To delete an existing call handler template: On the Search Call Handler Templates page, check the check boxes
                                                         						  to select the applicable call handler templates that you want to delete. Select Delete Selected and OK to confirm deletion. | Note | For more information on call
                                                                           								  handler template settings, see the Call Handler Settings, page 3-5 section. |
| Note | For more information on call
                                                                           								  handler template settings, see the Call Handler Settings, page 3-5 section. |

| Note | For more information on call
                                                                           								  handler template settings, see the Call Handler Settings, page 3-5 section. |
|---|---|

| Note | Composing a new message that is addressed to a distribution list is not supported on the branch server. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV Administration, expand Call Management and select System Call Handlers . The Search Call Handlers page
                                          			 displays the currently configured call handlers. |
|---|---|
| Step 2 | Configure a call handler (For more information on each field,
                                          			 see Help> This Page): To add a call handler: On the Search Call Handlers page, select Add New . On the New Call Handlers page, enter the values of the required
                                                         						  fields and select Save. To edit an existing call handler: On the Search Call Handlers page, select the applicable call
                                                         						  handler. On the Edit Call Handler page, modify the values of the required
                                                         						  fields and select Save. On the Edit Call Handler page, in the Edit menu, select any of
                                                         						  the following settings that you want to edit and then select Save: Transfer Rules Caller Input Greetings Message Settings Note For more information on
                                                                           								  call handler settings, see the Call Handler Settings, page 3-5 section. To delete an existing call handler: On the Search Call Handlers page, check the check boxes to
                                                         						  select the applicable call handler that you want to delete. Select Delete Selected and OK to confirm deletion. | Note | For more information on
                                                                           								  call handler settings, see the Call Handler Settings, page 3-5 section. |
| Note | For more information on
                                                                           								  call handler settings, see the Call Handler Settings, page 3-5 section. |

| Note | For more information on
                                                                           								  call handler settings, see the Call Handler Settings, page 3-5 section. |
|---|---|

| Note | The alternate transfer rule, when enabled, overrides the standard and closed transfer rules and is in effect at all times. |
|---|---|

| Note | You should not lock any key that matches the first digit of user extensions; otherwise, callers are not able to enter an extension
                                             to reach a user. |
|---|---|

| Note | Call handler greetings can be recorded in multiple languages. |
|---|---|

| Note | Unity Connection SRSV plays the greetings that you customized according to the requirements but some greetings override other
                                                   greetings when they are enabled during that duration. |
|---|---|

| Standard | Plays at all times unless overridden by another greeting. You cannot disable the standard greeting. |
|---|---|
| Closed | Plays during the closed (non-business) hours defined for the active schedule. A closed greeting overrides the standard greeting,
                                             and thus limits the standard greeting to the open hours defined for the active schedule. |
| Error | Plays if the caller enters invalid digits. This can happen if the digits do not match an extension, the extension is not found
                                             in the search scope, or the caller is otherwise restricted from dialing the digits. You cannot disable the error greeting. The system default error recording is, “I did not recognize that as a valid entry.” By default, after the error greeting plays,
                                             Unity Connection replays the greeting that was playing when the caller entered the invalid digits. |

| Note | For some integrations, you can set up Unity Connection SRSV so that as a caller records a message, a warning prompt is played
                                                   before the caller reaches the maximum allowable message length. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV
                                             			 Administration, expand Call Management and
                                             			 select Directory Handlers . The
                                             			 Search Directory Handlers page displays the currently configured directory
                                             			 handlers. |
|---|---|
| Step 2 | To edit a directory handler (For more
                                             			 information on each field, see Help> This Page): On the Search Directory Handlers page,
                                                   				  select the applicable directory handler that you want to update. On the Edit Directory Handler page,
                                                   				  enter the values of the required fields and select Save. On the Edit Directory Handler page, in
                                                   				  the Edit menu, select any of the following settings that you want to edit and
                                                   				  then select Save: Caller Input Greetings |

| Step 1 | In Cisco Unity Connection SRSV
                                          			 Administration, expand Networking > and select Central Server
                                             				Configuration . |
|---|---|
| Step 2 | On the Central Server Configuration page,
                                          			 enter the values of the required fields and select Save . (For information
                                          			 on each field, see Help> This Page). |

| Note | You cannot delete the default schedules on the branch server. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV Administration, expand System
                                          			 Settings and select Schedules. The Search Schedules page displays the currently
                                          			 configured schedules. |
|---|---|
| Step 2 | Configure a schedule (For more information on each field, see
                                          			 Help> This Page): To add a schedule: On the Search Schedules page, select Add New. On the New Schedule page, enter the Display Name and select
                                                         						  Save. In the Schedule Details menu, select Add New to enter the
                                                         						  schedule specifications and select Save. To edit a schedule: On the Search Schedule page, select the schedule you want to
                                                         						  modify. On the Edit Schedule Basics page, modify the values of the
                                                         						  required fields and select Save. To delete a schedule: On the Search Schedule page, check the check boxes to select the
                                                         						  schedules that you want to delete. Select Delete Selected and OK to confirm deletion. |

| Note | Many of the enterprise parameters rarely require change. Do not change an enterprise parameter unless you completely understand
                                       the feature you are changing or the Cisco Technical Assistance Center (Cisco TAC) specifies the change. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV
                                          			 Administration, expand System Settings and select Enterprise Parameters. |
|---|---|
| Step 2 | On the Enterprise Parameters page, enter the
                                          			 applicable settings. To set all service parameters to the default values,
                                          			 select Set to Default. |
| Step 3 | To view a list of enterprise parameters and
                                          			 descriptions, select the ? button on the right side of the page and select
                                          			 Save. (For more information on each field, see Help> This Page). |

| Note | Before you install any plugin, you must disable all intrusion detection or anti-virus services that run on the server where
                                       you install the plugin. |
|---|---|

| Step 1 | In Cisco Unity Connection SRSV
                                          			 Administration, expand System Settings and select Plugins. |
|---|---|
| Step 2 | On the Search Plugins page, select Find. |
| Step 3 | For the plugin that you want to install,
                                          			 select Download and follow the on-screen instructions for installing the
                                          			 plugin. |

| Step 1 | In Cisco Unity Connection SRSV
                                             			 Administration, expand Telephony Integrations and select Phone System. |
|---|---|
| Step 2 | On the Search Phone Systems page, select the
                                             			 phone system that you want to modify. |
| Step 3 | On the Phone System Basics page, modify the
                                             			 values of the required fields and select Save. (For information on each field,
                                             			 see Help> This Page). |

| Note | You need to configure the port group for a branch server on
                                          		  Cisco Unity Connection SRSV Administration. |
|---|---|

| Note | You need to configure the ports for a branch server on
                                          		  Cisco Unity Connection SRSV Administration. |
|---|---|

| Note | You need to configure the certificates for a branch server on
                                          		  Cisco Unity Connection SRSV Administration. |
|---|---|