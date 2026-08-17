---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-b-15cucsag-b-12xcucsag-chapter-0111-html-290e969da0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/b_15cucsag/b_12xcucsag_chapter_0111.html
retrieved_at: 2026-08-17T03:45:56.628444+00:00
---

System Administration Guide

# System Administration Guide

Updated: June 27, 2023

Chapter: Call
	 Management

## Chapter: Call
	 Management

# Call
                     	 Management

## Call Management Elements

Call Management in Cisco Unity Connection is combination of different call management elements that can be used to customize
                              how your system handles the calls and collect input from callers.

Unity Connection provides the following elements for managing incoming and outgoing calls:

Components

Usage

Call Handlers

Answer calls and take messages; provide menus of options (for example, “For customer service press 1, for sales press 2...”);
                                          route calls to the users and other call handlers; and play audiotext (prerecorded information).

Directory Handlers

Provide access to a corporate directory by playing an audio list that users and outside callers use to reach a users and leave
                                          messages.

Interview Handlers

Collect information from callers by playing a series of questions and then recording the answers.

Call Routing Tables

Allow you to define how calls are initially routed, based on criteria such as the phone number of the caller and the schedule.
                                          When you have set up call handlers, interview handlers, directory handlers, and extensions for users, you can route the calls
                                          to the applicable person or handler by editing the call routing tables.

Restriction Tables

Control outgoing calls by allowing you to specify the numbers that Unity Connection can dial for transferring calls, for notifying
                                          users of messages, and for delivering faxes.

Schedules and Holidays

Define business, nonbusiness, and holiday hours for the organization for the purpose of controlling which set of call routing
                                          rules, greetings, or transfer options is currently active.

All of these elements can be used as building blocks. You can use or customize the default objects in Unity Connection, or
                              add new objects and combine them to create the caller experience.

## Call Management Plan

Call management plan shows how the handlers connect to one another, include a menu of one-key dialing options and all possible
                           navigation choices (such as reaching a call handler by dialing an extension or via a routing rule). You can also include the
                           predefined Unity Connection call handlers in your plan.

### Creating a Call
                           	 Management Plan

When you have considered how your call management plan ought to
                              		work, you can create a sketch to connect the handlers.

The figure below shows a sample call management map that makes
                              		use of the automated attendant.

### Implementing a Call Management Plan

After you map your plan, write detailed scripts for the greeting of each call handler that is used during the recording session.

When you are ready to set up your system of call handlers, first create the call handlers to which the calls are routed. You
                              select these “destination” call handlers when you create the call handlers that route calls to them. Before creating the call
                              handlers, you also need to create accounts for the users to which call handlers transfer the calls.

Using above figure as an example, you first create a user account for Kelly Bader, and the handlers for Place an Order, Order
                              Status, and Job Listings. Then you create the handlers for the Order Department and Human Resources.

In addition to mapping call handlers, you also need to plan call routing tables. The above figure, for example, all new call
                              handlers are reached through the Opening Greeting. You can also assign extensions to some of your call handlers and to route
                              incoming calls to those extensions using a call routing table.

## System Call Handlers

Call handlers are used to answer calls, greet callers with recorded prompts and provide them with information and options,
                           route calls, and take messages. You can use the predefined Unity Connection call handlers, or can create unlimited new call
                           handlers.

Each call handler that you add in Unity Connection is based on a template known as Call Handler Template.

You may want to use call handlers in the following ways:

As an automated attendant—A call handler can be used in place of a human operator to answer and direct calls by playing greetings
                                 and responding to key presses. The automated attendant can provide a menu of options (for example, “For Sales, press 1; for
                                 Service, press 2; for our business hours, press 3.”).

To offer prerecorded audiotext—A call handler can be used to provide information that customers request frequently (for example,
                                 “Our normal business hours are Monday through Friday, 8 a.m. to 5 p.m.”), or to play a prerecorded message that all callers
                                 hear before they can interact with the system.

As a message recipient—A call handler can be used to take messages for the organization (for example, “All of our customer
                                 service representatives are busy. Please state your name, phone number, and account number, this returns your call as soon
                                 as possible.”).

To transfer calls—A call handler can be used to route callers to a user (for example, after hours, you could transfer calls
                                 that come to a technical support call handler directly to the mobile phone of the person who is on call), or to another call
                                 handler.

Unity Connection supports 40,000 system call handlers.

### Call Handler Templates

Each call handler that you add in Unity Connection is based on a template. Settings from the template are applied as when
                              you create a call handler. Unity Connection includes predefined templates that you can edit. You can also create additional
                              call handler templates.

For each template, you should consider enabling the transfer, caller input, greetings, and message settings that is needed
                              for the call handlers that you create.

If you change settings on a call handler template, the new settings are in effect only for new call handlers that are created
                                          using that template.

Deleting a call handler template does not affect any call handlers that were based on that template when they were created.

#### Default Call Handler Templates

Unity Connection has one default call handler template that has settings suitable for most call handlers. You can edit the
                                 default call handler template but cannot delete it.

System Call Handler Template

The settings on this template are suitable for most call handlers.

#### Configuring Call Handler Templates

This section includes information on configuring
                                    		  a call handler template for Unity Connection, defining the settings for the
                                    		  call handler template, and saving them.

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Templates > and select > Call Handler Templates .

The Search Call Handler Templates page
                                                				displays the currently configured call handler templates.

Step 2

Configure a call handler template (For
                                             			 information on each field, see Help> This Page):

To add a call handler template, select
                                                      					 Add New. The New Call Handler Template page appears. Enter the applicable
                                                      					 settings and select Save.

To edit a call handler template, select
                                                      					 the call handler template. On the Edit Call Handler Template Basics page,
                                                      					 select the applicable settings from the Edit menu:

Call Handler Template Basics

Transfer Rules

Caller Input

Greetings

Post Greeting Recording

Message Settings

To delete a call handler template, do
                                                      					 the following:

In the Search Call Handler Templates
                                                      					 page, select the call handler template that you want to delete.

Select Delete Selected and then select
                                                      					 OK to confirm deletion.

### Default System Call Handlers

Unity Connection includes the following predefined call handlers that you can edit but not delete.

You should at least edit the greetings for these call handlers.

Opening Greeting

Acts as an automated attendant, playing the greeting that callers first hear when they call your organization, and performing
                                             the actions you specify. The Opening Greeting Call Routing rule transfers all incoming calls to the Opening Greeting call
                                             handler.

By default, the Opening Greeting call handler allows callers to press * to reach the Sign-In conversation, or press # to reach
                                             the Operator call handler. Messages left in the Opening Greeting call handler are sent to the Undeliverable Messages distribution
                                             list.

Operator

Calls are routed to this call handler when callers press “0” or do not press any key (the default setting). You can configure
                                             the Operator call handler so that callers can leave a message or can be transferred to a live operator.

By default, the Operator call handler allows callers to press * to reach the Sign-In conversation, or press # to reach the
                                             Opening Greeting call handler. Messages left in the Operator call handler are sent to the mailbox for the Operator user.

Goodbye

Plays a short goodbye message and then hangs up if there is no caller input.

By default, the Goodbye call handler allows callers to press * to reach the Sign-In conversation, or press # to reach the
                                             Opening Greeting call handler. If you change the After Greeting action from Hang Up to Take Message, messages left in the
                                             Goodbye call handler are sent to the Undeliverable Messages distribution list.

### Configuring System Call Handlers

This section includes information on configuring
                                 		  a system call handler for Unity Connection, define the settings for call
                                 		  handler and save them.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Call Management and
                                          			 select System Call Handler .

The Search Call Handlers page displays the
                                             				currently configured call handlers.

Step 2

Configure a system call handler (For
                                          			 information on each field, see Help > This Page):

To add a system call handler:

On the Search Call Handlers page, select Add
                                       				New.

On the New Call Handler page, enter the
                                       				applicable settings and select Save.

To edit a system call handler:

On the Search Call Handlers page, select the
                                       				call handler that you want to edit. To edit multiple system call handlers,
                                       				check the applicable check boxes and select Bulk Edit.

On the Edit Call Handler Basics page, select
                                       				the Edit menu and then edit any of the following settings:

Call Handler Basics.

Transfer Rules. See Transfer Rules, page 8-6 .

Caller Input. See Caller
                                                						Input, page 8-6 .

Greetings. See Greetings,
                                                						page 8-6 .

Post Greeting Recording.

Message Settings. See Message Settings, page 8-7 .

Call Handler Owners. See Call Handler Owners, page 8-7 .

After editing the settings, select Save .

To delete a system call handler:

On the System Call Handlers page, select the
                                       				system call handler to delete.

Select Show Dependencies to search the
                                       				database objects that have dependencies on the call handler you want to delete.
                                       				From the dependencies search results, follow links to the affected objects and
                                       				reassign the dependency to another call handler.

Select Delete Selected.

Call Handler Settings

### Transfer Rules

The transfer rules for a system call handler specify how Unity Connection transfer the calls that reach the call handler from
                              the automated attendant.

When a call is transferred to the call handler, Unity Connection first checks the applicable transfer rule to determine where
                              to transfer the call—either to the call handler greeting, or to an extension.

You configure a transfer rule to transfer the call to the greeting if you want to provide the caller with a prerecorded menu
                              of options or an informational message.

Each call handler has three transfer rules that you can customize:

Standard: This is for standard hours

Closed: This is for closed (nonbusiness and holiday) hours of the active schedule

Alternate: This transfer rule when enabled, overrides the standard and closed transfer rules and is in effect at all times.

### Caller Input

The caller input settings define actions that Unity Connection takes in response to phone keys pressed by callers during a
                              call handler greeting. Using the settings on the Edit Greeting page for each individual greeting, you can specify whether
                              the greeting allows caller input and whether callers can perform transfers.

### Greetings

You can configure individual call handler greetings to allow callers to transfer to numbers that are not associated with Unity
                                 Connection users or call handlers while the greeting is playing.

Each system call handler can have up to seven greetings.

The default greetings are:

Standard

Plays at all the times unless overridden by another greeting. You cannot disable the standard greeting.

Closed

Plays during the closed (nonbusiness) hours defined for the active schedule. A closed greeting overrides the standard greeting.

Holiday

Plays during the specific dates and times specified in the schedule of holidays associated with the active schedule. A holiday
                                             greeting overrides the standard and closed greetings.

Internal

Plays for internal callers only. It can provide information that only co-worker needs to know. An internal greeting overrides
                                             the standard, closed, and holiday greetings. Not all phone system integrations provide the support necessary for an internal
                                             greeting.

Busy

Plays when the extension is busy. A busy greeting overrides the standard, closed, internal, and holiday greetings.

Not all phone system integrations provide the support necessary for a busy greeting.

Alternate

Can be used for a variety of special situations, such as vacations or a leave. An alternate greeting overrides all other greetings.

Error

Plays if the caller enters invalid digits. This may happen if the digits do not match an extension, the extension is not found
                                             in the search scope, or the caller is otherwise restricted from dialing the digits. You cannot disable the error greeting.

The system default error recording is, “I did not recognize that as a valid entry.” By default, after the error greeting plays,
                                             Unity Connection replays the greeting.

Call handler greetings can be recorded in multiple languages when the language for the call handler is inherited from the
                                             caller. For example, if Unity Connection is configured to provide prompts in French and Spanish, it is possible to record
                                             the standard greeting in both languages so that Spanish- and French-speaking callers can hear the greeting in their own language.

### Message Settings

The message settings specify who receives messages for the call handler, whether messages are marked for dispatch delivery,
                              the maximum recording length for messages from outside callers, what callers can do when leaving messages, whether their messages
                              are automatically marked secure, and what action to take next on a call after a message is left.

### Call Handler Owners

Call handler owners select a different call handler greeting or record the call handler greetings from the System Call Handlers
                              > Greetings page in Cisco Unity Connection Administration, or they can use the Cisco Unity Greetings Administrator to do so
                              by phone.

With Unity Connection 10.5 and later, both the users and distribution lists can be added as the call handler owners. However,
                                          only the local users (not the members of nested distribution lists) in a distribution list can added as call handler owners.

## Directory Handlers

Directory handlers are used to provide access to a corporate directory that callers can use to reach Unity Connection users
                              with mailboxes. When a caller searches for a username or part of a name, a directory handler looks for the extension and routes
                              the call to the appropriate user.

Directory handlers do not have greetings so you should use call handlers to route callers to a directory handler. Then use
                              the call handler greetings to explain caller the options for each directory handler.

Each directory handler contains settings that specify how it searches for names, what it does when it finds one or more matches,
                              and what it does when it detects no caller input.

There are two types of directory handlers:

Phone Keypad

Callers enter search information or extensions using the phone keypad. For this type of directory handler, you can specify
                                          how it searches for names, what it does when it finds one or more matches, and what it does when it detects no caller input.

Voice Enabled

Callers say the first name and last name of the Unity Connection user that they want to reach, or enter an extension by saying
                                          the individual digits in the extension. The voice directory handler can also include alternate names in searches. The voice-recognition
                                          option is required in order to create voice-enabled directory handlers.

Users who are listed in the directory are available to outside callers but administrator-defined contacts are only available
                                          to users who are signed in to Unity Connection. User-defined contacts are only available to the Unity Connection users who
                                          defined them.

For this type of directory handler, users cannot be accessed using directory handlers unless they have a display name specified
                                                      and the List in Directory check box is checked for them on the User Basics page.

You can create both phone-keypad and voice-enabled directory handlers on the same system.

### Default Directory Handler

Unity Connection includes one default directory handler that is System Directory Handler that you can edit but cannot delete.
                              By default, this directory handler is configured to search all users who have mailboxes on the system, in last name, first
                              name order.

Callers use the phone keypad to interact with the default System Directory Handler. There is no default voice-enabled directory
                              handler.

By default, directory handler is accessed when callers press 4 during the Opening call handler greeting.

### Configuring Directory Handlers

This section includes information to configure a
                                 		  directory handler for Unity Connection, define the settings for the directory
                                 		  handler, and save them.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Call Management and select Directory Handlers.

The Search Directory Handlers page displays
                                             				the currently configured directory handlers.

Step 2

Configure a directory handler, (For
                                          			 information on each field, see Help> This Page):

To add a directory handler:

On the Search Directory Handlers page,
                                                   					 select Add New.

On the New Directory Handler page, enter
                                                   					 the applicable settings and select Save.

To edit a directory handler:

On the Search Directory Handlers page,
                                                   					 select the directory handler you want to edit. To edit multiple system
                                                   					 directory handlers, check the applicable check boxes and select Bulk Edit.

On the Edit Directory Handler Basics
                                                   					 page, select the Edit menu and then select any of the following settings:

Directory Handler Basics

Caller Input

Greetings

After editing the settings, select
                                                         						  Save before leaving the page.

To delete a directory handler:

On the Directory Handlers page, select
                                                   					 the directory handler to delete.

Select Show Dependencies to search the
                                                   					 database objects that have dependencies on the directory handler you want to
                                                   					 delete. From the dependencies search results, follow links to the affected
                                                   					 objects and reassign the dependency to another directory handler.

Select Delete Selected.

### Routing Calls to a Voice Directory Handler

If you are setting up a voice directory handler,
                                 		  see the following task list for configuring Cisco Unified Communications
                                 		  Manager to route a phone number from Cisco Unified CM to the Unity Connection
                                 		  voice directory.

Step 1

In Cisco Unified Communications Manager
                                          			 Administration, add the ports that you want to use for the voice-type directory
                                          			 handler to a new line group.

Step 2

Add the line group to a new hunt list.

Step 3

Add the hunt list to a new hunt pilot to
                                          			 which calls for the voice-type directory handler is routed.

Step 4

In Cisco Unity Connection Administration,
                                          			 configure the ports to route calls to the voice-type directory

handler.

Step 5

For details on configuring Cisco Unified CM,
                                          			 see the Cisco Unified CM documentation at

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html .

## Interview Handlers

Interview handlers collects information from callers by playing a series of questions that you have recorded, and then recording
                           the answers offered by callers.

You can specify who receives the messages for the interview handler, whether the message is marked for dispatch delivery,
                           the message is marked urgent, and what actions to take next on the call when a message is left.

If an interview handler is referenced by other objects in Unity Connection (for example, a caller input key on a call handler
                           sends calls to the interview handler), you are not allowed to delete the interview handler until you have changed the settings
                           on the other objects to remove references of the interview handler that you want to delete. If you try and delete an interview
                           handler without first changing settings on objects, the delete operation fails.

If you delete an interview handler that was referenced by one or more call handlers, be sure to rerecord the call handler
                           greetings so that callers hear the appropriate information about input options.

With Cisco Unity Connection Release 14SU1 and later, the maximum recording time for one Interview Handler Question is 300
                                       seconds.

If you want to record Interview Handler Question of length more than 300 seconds, you should record multiple questions.The
                                       maximum number of questions that can be recorded on Unity Connection is 20.

### Configuring Interview Handlers

To configure a interview handler for Unity
                                 		  Connection, define the settings for the interview handler and save them.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Call Management and select Interview Handlers.

The Search Interview Handlers page displays
                                             				the currently configured interview handlers.

Step 2

Configure an interview handler, (For
                                          			 information on each field, see Help> This Page):

To add an interview handler:

On the Search Interview Handlers page,
                                       				select Add New.

On the New Interview Handler page, enter the
                                       				applicable settings and select Save.

To edit a directory handler:

On the Search Interview Handlers page, select
                                 		  the interview handlers that you want to edit. To edit multiple system directory
                                 		  handlers, check the applicable check boxes and select Bulk Edit. Enter the
                                 		  applicable settings and select Save.

To delete an interview handler:

On the Interview Handlers page, select the
                                       				interview handler to delete.

Select Show Dependencies to search the
                                       				database objects that have dependencies on the interview handler you want to
                                       				delete. From the dependencies search results, follow links to the affected
                                       				objects and reassign the dependency to another interview handler.

Select Delete Selected.

## Dial Plan

Partitions and search spaces provide a way to segregate the global dial and message addressing space within Unity Connection.
                           A partition comprises a logical grouping of objects that are identifiable by extension, name or SMTP address. A search space
                           contains an ordered list of partitions.

### Default Partition and Search Space in Unity Connection

When you install or upgrade to the Unity Connection server, all objects, such as users and user templates that belong to a
                              partition are placed in a partition named <Server Name> Partition. Similarly, all objects that are configured to use search
                              spaces use a search space named <Server Name> Search Space (which includes <Server Name> Partition as its sole member). In
                              addition, all templates are configured to use this partition and search space where applicable. Thus, by default, Unity Connection
                              uses only one server-wide partition and search space. You can rename or delete the default partition and search space and
                              edit the default search space by changing the description or partition membership.

Changing the system default partition and search space do not affect any objects or templates that have already been created.

#### Changing the System Default Partition and Search Space

Step 1

In Cisco Unity Connection Administration,
                                             			 expand System Settings and
                                             			 select General Configuration .

Step 2

In the Edit General Configuration page, in
                                             			 the Default Partition field, select the name of the new default partition.

Step 3

In the Default Search Scope field, select
                                             			 the name of the new default search space and select Save .

### Partitions

In Unity Connection, you create partitions as a way to group together objects to which callers and users can address messages
                              or place calls while interacting with Unity Connection. One or more partitions can be grouped together as members of a search
                              space and a partition can be a member of more than one search space. The following types of objects belong to a partition:

Users with mailboxes (primary extension)

User alternate extensions

Contacts (including VPIM contacts)

System distribution lists

System call handlers

Directory handlers

Interview handlers

VPIM locations

In addition, you can use user templates, contact templates, and system call handler templates to set the partition membership
                              for new objects of similar types.

Extensions must be unique within a partition, although partitions can contain objects that do not have an associated extension
                              (for example, some contacts and system distribution lists). The names of objects do not have to be unique within a partition.
                              Administrator-defined contact phone numbers also do not need to be unique within a partition.

In general, objects can only be a member of a single partition, although a user can have a primary extension in one partition
                              and an alternate extension in a different partition. If there are alternate names defined for the user, the alternate names
                              are available in each partition where the user has an extension.

When you change partition of an alternate extension in a bulk edit mode, the primary extension of the user is taken as an
                                          alternate extension. If primary extension already exist in the changed partition then it throws an error message with the
                                          duplicate extension.

#### Configuring
                              	 Partitions

This section includes information on configuring a partition for
                                    		  Unity Connection, defining the settings and saving them. After creating a
                                    		  partition, you can assign various objects, such as users and user templates as
                                    		  partition members.

Step 1

In Cisco Unity Connection Administration, expand Dial
                                                   				  Plan > and select Partitions .

Step 2

The Search Partitions page displays the currently configured
                                             			 partitions.

Step 3

Configure partitions (For more information on each field, see
                                             			 Help> This Page):

To add a partition, select Add New .

On the New Partition page, enter a name for the partition and
                                                      					 select Save.

The Edit Partition page appears, you can optionally add a
                                                      					 description and select Save.

You can change the name or description of a partition. To change
                                                                  						the partition membership, you must edit the individual member objects.

To edit a partition, select the partition you want to edit. On
                                                      					 the Edit Partition page, change the settings as applicable and select Save .

To delete a partition, check the check boxes next to the display
                                                      					 name of the partitions that you want to delete. Select Delete Selected and OK
                                                      					 to confirm deletion.

You can delete a partition when the partition is empty (there
                                                                  						are no objects that are members of the partition) and when the partition is not
                                                                  						configured as the system default partition. If you attempt to delete a
                                                                  						partition that is not empty, Unity Connection warns you that the partition is
                                                                  						in use and does not allow the deletion.

### Search
                           	 Spaces

Search spaces are used to define the search scope of objects,
                              		such as users and distribution lists that a user or outside caller can reach
                              		while interacting with Unity Connection. For example, the search scope that is
                              		applied to a user identifies which users, distribution lists, or VPIM contacts
                              		the user can address messages to. The search scope that is applied to a user
                              		also identifies which users and contacts the user can call by name dialing when
                              		using the voice-recognition conversation.

The following types of objects can use a search space for the
                              		search scope:

Users with mailboxes

Routing rules (both direct and forwarded)

System call handlers

Phone directory handlers

Voice-enabled directory handlers

VPIM locations

In addition, you can use user templates, contact templates, and
                              		system call handler templates to set the search scope for new objects of
                              		similar types. A search space is comprised of one or more ordered partitions.

When Unity Connection searches for an object on behalf of a
                              		caller, it searches the partitions in the order in which they are arranged in
                              		the search space. While extensions must be unique within a partition, they do
                              		not need to be unique within a search space, so you can use search spaces to
                              		handle dial plans that have overlapping extensions.

For information on VPIM and networking concepts, see the Networking chapter.

#### Search Space Example for Automated Attendant

In an organization, you have installed a Unity Connection server that is setup as an automated attendant to handle the calls
                                 for customer service department and take voice messages for users. All the employees of the organization have a primary extension
                                 in Employee partition and the employees of customer service department have alternate extensions in Customer Service partition.

The Unity Connection server is configured with the following search spaces and associated partition membership:

Search Space

Partition Membership (in Order)

Employees search space

Employee, Customer Service

Customer Service search space

Customer Service

In addition, two routing rules are configured. As per the first routing rule, when outside callers call in to Unity Connection,
                                 they use the Customer Service search space. The system call handlers and directory handlers with which the outside callers
                                 interact are configured to use Customer Service search space. As per the second routing rule, all the employees of the organization
                                 use Employee search space when they call each other within the organization.

In this example, when users call and sign in to Unity Connection, they can address messages or place calls to any other user
                                 at the company. However, when outside callers call Unity Connection and reach the automated attendant, they can reach only
                                 the employees with alternate extensions in the Customer Service partition.

#### Multiple Site Search Space Example

An organization has three digitally networked Unity Connection locations serving three sites: Headquarters, Regional-East,
                                 and Regional-West.

The configuration is as follows:

Unity Connection is configured with the following search spaces and associated partitions:

Search Space

Partition Membership (in Order)

Headquarters-SS

HQ, Primary, RE, RW

Regional-East-SS

RE, Primary

Regional-West-SS

RW, Primary

The following user accounts are set up:

User

Home Server

Search Space of User

Primary Extension and Partition

Alternate Extension and Partition

Alex Abade

Headquarters

Headquarters-SS

85553001, Primary

3001, HQ

Chris Brown

Headquarters

Headquarters-SS

85553002, Primary

3002, HQ

Pat Smith

Regional-East

Regional-East-SS

82223001, Primary

3001, RE

Shannon Johnson

Regional-East

Regional-East-SS

82223002, Primary

3002, RE

Robin Smith

Regional-West

Regional-West-SS

87773001, Primary

3001, RW

Terry Jones

Regional-West

Regional-West-SS

87773333, Primary

3333, RW

There is a VPIM server that is configured as a VPIM location on the Headquarters server: VPIM-South. This VPIM location has
                                       a Dial ID of 8468 and is configured to allow blind addressing, to belong to the Primary partition, and to use the Headquarters-SS
                                       search space.

The Attempt Sign In direct routing rule and the Attempt Forward forwarded routing rule on each server are configured to use
                                       the same search space as the users on that server. (For example, the rules on the Headquarters server use the Headquarters-SS
                                       search space.)

In this example, users at one site can address other users in the same site using 4-digit extensions. Users can blind address
                                 messages to a VPIM mailbox by entering 8468 plus the mailbox number on the remote system. Messages sent by users at the VPIM-South
                                 VPIM location can be delivered to any user in the HQ, Primary, RE, or RW partitions.

#### How Search Spaces Work

Search spaces are applied to the following components:

Users: Users can reach only the objects in a partition that is part of a search space defined as the search scope for the
                                       user. This search space need not include any partitions that contain the primary or alternate extensions of the user.

If a user addresses a message by extension and there are overlapping extensions in different partitions in the search space,
                                 Unity Connection searches the partitions in the search space in the order that they appear in the Assigned Partitions list
                                 in Cisco Unity Connection Administration and returns the first result found.

The search scope of a user defines the objects that a user can reach when addressing a message by extension or name, adding
                                 members to a private distribution list, adding names to an addressing priority list, placing a call to another user by calling
                                 the name, addressing a message to a VPIM contact, an blind addressing a message to a VPIM location.

Call Routing Rules: When a call comes in to Unity Connection, it is first checked against the applicable routing rules table,
                                       depending on whether the caller dialed directly into Unity Connection or was forwarded from an extension. When Unity Connection
                                       matches the call to a routing rule in the applicable table based on the parameters of the call, the configuration of the routing
                                       rule determines the initial search scope of the call.

To facilitate setting the correct search scope on a call routing rule, you can set up routing rule conditions to select a
                                 rule based on the port of the incoming call, the phone system, the dialed number, or other criteria. If you are setting up
                                 multiple partitions and multiple search spaces, you must carefully consider the impact of the search scope that is configured
                                 for each call routing rule. Consider the following considerations related to setting the search scope with call routing rules:

Unity Connection uses the search space defined as the initial scope of the call to identify whether the call is from a user
                                       and if so, which user. If a user calls from an extension that is in a partition that is not a member of the search space set
                                       as the initial search scope for the call, the call is not identified as coming from the user. If the extension of the user
                                       overlaps with an extension in another partition that also appears in this search space, the call is identified as coming from
                                       the first object that Unity Connection finds when searching the partitions in the order that they appear in the search space.

Users who call to sign in to Unity Connection do not have the search scope set to the search space defined for the user profile
                                       until they have successfully completed the sign-in process.

System Distribution Lists: You can use search spaces to limit user access to send messages to distribution lists because you
                                       assign a partition to each distribution list. If you assign a distribution list in a partition that is not part of the search
                                       scope of a particular group of users, the users are not able to find the distribution list to address messages to it. For
                                       example, you can create a new partition called “Distribution Lists Partition” and configure the allvoicemailusers, allvoicemailenabledcontacts,
                                       and undeliverablemessages to use this partition. To grant certain users access to send to the lists, you can create a new
                                       search space that includes both the default partition and the “Distribution Lists Partition,” and assign this search space
                                       as the search scope for the users.

System Call Handlers: Unity Connection uses the call handler search scope to match extensions that are dialed from the call
                                       handler to users, administrator defined contacts, and remote contacts at VPIM locations. You can set the scope of the handler
                                       to either inherit the search scope that is already set on the call (from a previous handler or from a call routing rule) or
                                       to use the particular search scope that you specify.

Directory Handlers: Unity Connection uses the directory handler search scope to define the objects that callers who reach
                                       the directory handler can find or hear. For phone directory handlers, you can set the scope to the entire server, a particular
                                       class of service, a system distribution list, or a search space (either inherited from the call or specified for the directory
                                       handler). For voice enabled directory handlers, you can set the scope to the entire server or to a search space (either inherited
                                       from the call or specified for the directory handler).

When callers search a directory handler for a particular name, if the scope of the directory handler is set to a search space,
                                 Unity Connection searches each partition in the search space and returns a list of all of the objects that match the name.

Interview Handlers: Each interview handler is associated with a partition, so that it can be included in a search space and
                                       callers can reach it from other parts of the conversation. Because interview handlers do not involve dialing or addressing
                                       to users or other objects, they do not have a search scope defined.

Networking: When you network a Unity Connection server with other Unity Connection locations, the partitions and search spaces
                                       that are configured on the server replicate to all other Unity Connection locations on the network. A Unity Connection network
                                       supports up to 10K partitions and 10K search spaces shared among all of the locations in the network.

VPIM Locations: Each VPIM location belongs to a single partition. If a VPIM location allows blind addressing and the partition
                                       to which the location belongs is in the search space for a user, the user can blind address to a user on the remote VPIM system.
                                       To blind address, the user addresses the message to the Dial ID of the VPIM location followed by the remote user mailbox number.
                                       For example, to reach mailbox 1000 at VPIM location 555, the user would address the message to 5551000.

The partition of the VPIM location is used as the partition of automatically-created VPIM contacts if the VPIM location is
                                 configured for automatic contact creation. You can also change the partition of VPIM contacts independent of the associated
                                 VPIM location. Each VPIM location also has a search scope. When Unity Connection receives a message from a sender at a VPIM
                                 location, Unity Connection searches the search space that is defined as the search scope for the location to determine the
                                 message recipient by matching the extension in the To: address field with a Unity Connection user.

Administrator Defined Contacts: Each administrator defined contact belongs to a partition. When a contact is configured with
                                       phone numbers that callers can use to call the contact using voice commands, voice-recognition users with search space includes
                                       the partition of the contact are able to call the contact; users with search space does not include this partition are not
                                       able to call the contact. In addition, the contact is reachable by callers who reach any voice-enabled directory handler with
                                       search scope uses or inherits a search space that includes this partition (or if the directory handler search scope is set
                                       to the entire server).

#### Configuring Search Spaces

This section includes information on configuring
                                    		  a search spaces for Unity Connection, defining the settings and saving them.

Step 1

In Cisco Unity Connection Administration,
                                             			 expand Dial Plan and select Search Spaces .

Step 2

Configuring search spaces (For more
                                             			 information on each field, see Help> This Page):

To add new search space, select Add New .

On the New Search Space page, enter a
                                                      					 name for the search space and select Save.

In the Edit Search Space page, enter a
                                                      					 description for the search space and select Save .

To edit a search space, select the name
                                                      					 of the search space that you want to edit. On the Edit Search Space page,
                                                      					 change the settings as applicable and select Save.

To delete a search space, check the
                                                      					 check box next to the display names of the search spaces that you want to
                                                      					 delete. Select Delete Selected and OK to confirm deletion.

You cannot delete more than 50 search
                                                      					 spaces simultaneously.

## Call Routing

Call routing is used to route incoming calls to the operator or to specific subscribers, call handlers, directory handlers,
                           or interview handlers. Also, call routing is used to route subscribers to the subscriber logon conversation.

### Default Call Routing Rules

Unity Connection has two call routing tables—one for direct calls and other for forwarded calls—that handle calls from users
                              and from unidentified callers.

Direct rules handle calls from users and unidentified callers that are dialed directly to Unity Connection. The predefined
                                    direct routing rules are:

Attempt Sign-In—Calls from users are routed to the user sign-in conversation.

With Unity Connection 10.0(1) and later, a user can play and record both video and audio greetings, when login via Attempt
                                                      Sign-in.

Opening Greeting—Calls from unidentified callers are routed to the Opening Greeting.

Forwarded rules handle calls that are forwarded to Unity Connection from either a user extension

or from an extension that is not associated with a user account (such as a conference room). The

predefined forwarded routing rules are:

Attempt Forward—All calls forwarded from a user extension are routed to the user greeting.

With Unity Connection 10.0(1) and later, a user can play both video and audio greetings, when the calling user receives unanswered
                                                call.

Opening Greeting—Calls forwarded from an extension that is not associated with a user account are routed to the Opening Greeting.

You can change the order of the Attempt Sign-In and Attempt Forward rules relative to additional rules that you add in the
                              respective routing tables. The Opening Greeting rule is always the last entry for both tables. You cannot delete the predefined
                              rules.

When you create a new rule, you need to specify only the criteria that are used to route the calls. You can leave the other
                              fields on the page blank because the blank field matches everything.

### Configuring Call Routing Rules

This section includes information on configuring
                                 		  call routing rules in Unity Connection, define the settings for the routing
                                 		  rules, and save them.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand Call Management> Call Routing .

If you want to configure routing rules
                                                   					 for direct calls, select Direct Routing Rules. The Direct Routing Rules page
                                                   					 displays the default and currently configured routing rules.

If you want to configure routing rules
                                                   					 for forwarded calls, select Forwarded Routing Rules. The Forwarded Routing
                                                   					 Rules page displays the default and currently configured routing rules.

Step 2

Configure a routing rule in the direct or forwarded routing rules:
                                          			 (For information on each field, see Help> This Page):

To add a routing rule, select Add New.

On New Direct Routing Rule page or New
                                                   					 Forwarded Routing Rule page, enter the applicable settings and select Save.

To add the routing rule condition,
                                                   					 select Add New on the Edit Routing Rule page.

Edit the routing rule condition settings
                                                   					 and select Save.

To delete a routing rule, do the
                                                   					 following:

On the Search Contacts page, select the
                                                   					 routing rule to delete.

Select Delete Selected.

### Call Routing Tables

Call routing tables are used to route incoming calls to the operator or to specific users, call handlers, directory handlers,
                              or interview handlers. In addition, call routing tables are used to route users to the user sign-in conversation.

You can add new rules and change the order of the rules in the respective routing tables. You can change the order of the
                              Attempt Sign-In and Attempt Forward rules relative to additional rules that you add in the respective routing tables, but
                              the Opening Greeting rule is always the last entry for both tables. You cannot delete the predefined rules.

Call routing tables consist of a series of rules that let you route incoming calls based on the information that Cisco Unity
                              Connection may have about a call, such as the calling phone number (ANI or caller ID), the trunk or port on which the call
                              comes in, the dialed phone number (DNIS), the forwarding station, and the schedule.

When Unity Connection receives a call, it first determines if it is a direct or forwarded call based on the call information
                              that is sent by the phone system, and then applies the applicable call routing table. If the call information matches all
                              of the conditions for the first rule, the call is routed as specified in the rule. If any of the conditions specified in the
                              first rule are not met, the call information is then compared to the conditions of the second rule, and so on, until a rule
                              is found that matches all the characteristics of the call.

The integration between the phone system and Unity Connection determines the information that is provided about a call (for
                              example, call type, port, trunk, calling number, and dialed number). The schedule is determined by the date and time that
                              the call is received.

The following examples show how call routing tables are used in Unity Connection to route calls.

Example 1

In below table, calls that meet the criteria specified in the Operator rule settings—any direct external call received while
                              the Weekdays schedule is active—are transferred to the operator. Calls that do not meet this criteria are routed as specified
                              by one of the other call routing rules in the table. In this case, any direct external calls received on the weekends are
                              routed to the Opening Greeting, according to the Opening Greeting call routing rule.

Rule

Status

Dialed  Number

Calling  Number

Phone  System

Port

Schedule

Send Call To

Operator

Active

Any

Any

Any

Any

Weekdays

Attempt transfer for operator

Attempt Sign-In

Active

Any

Any

Any

Any

Always

Attempt Sign-In

Opening Greeting

Active

Any

Any

Any

Any

Always

Attempt transfer for Opening Greeting

Example 2

In below table, calls forwarded from specific extensions—1234 and 5678—are routed according to the Product Info and Customer
                              Service rules, respectively. Calls that do not match the extension (or forwarding station) in either of the first two rules
                              are routed according to the two remaining rules.

Rule

Status

Dialed  Number

Calling  Number

Forwarding Station

Phone  System

Port

Schedule

Send Call To

Customer Service

Active

Any

Any

5678

Any

Any

Always

Attempt transfer for Customer Service

Product Info

Active

Any

Any

1234

Any

Any

Always

Send to greeting for Product Info

Attempt Forward

Active

Any

Any

Any

Any

Any

Always

Attempt Forward

Opening Greeting

Active

Any

Any

Any

Any

Any

Always

Attempt transfer for Opening Greeting

### Using Routing Rules with the Route from Next Call Routing Rule Action

In a user profile or call handler, you can configure the After Greeting action, the After Message action, or the action of
                              a caller input key to apply the Route from Next Call Routing Rule action to calls. This action causes Cisco Unity Connection
                              to continue processing the call according to the applicable call routing table (direct or forwarded, depending on how the
                              call was received from the phone system) starting at the rule immediately after the rule that Unity Connection previously
                              applied to the call. If the call was already processed according to the final rule in the table, the final rule is applied
                              again.

For example, you might want to have Unity Connection always play a standard greeting or legal disclaimer to all callers, whether
                              they call Unity Connection directly or are forwarded by an extension. The greeting plays before callers can take any other
                              action—for example, leaving a message or signing in. To do so, you do the following tasks:

Create a new call handler and record the message as the alternate greeting.

Enable the alternate greeting, configure it to ignore caller input during the greeting, and then configure the After Greeting
                                    action with the Route from Next Call Routing Rule call action.

Add a new direct call routing rule to send all direct calls to the new call handler (with Go Directly to Greetings selected)
                                    and verify that the rule appears at the top of the direct call routing table.

Add a new forwarded call routing rule to send all forwarded calls to the same new call handler (again with Go Directly to
                                    Greetings selected) and verify that the rule appears at the top of the forwarded call routing table.

Once the system is configured in this way, all calls—no matter where they come from or how they get to the system—hear this
                              greeting in its entirety and then proceed directly to their original destination.

## Restriction
                        	 Tables

Restriction tables allow you to
                           		control which phone numbers or URIs the users and administrators can use for:

Transferring calls—including both the numbers or URIs users can
                                 			 enter for transferring their calls, and the numbers or URIs that outside
                                 			 callers can enter when using Caller system transfers.

Recording and playback by phone from Cisco Unity Connection
                                 			 applications, when the phone is the designated recording and playback device in
                                 			 the Media Player.

Delivering faxes to a fax machine.

Sending message notifications.

Creating user-defined alternate extensions—including the
                                 			 extensions that Unity Connection offers to add automatically on behalf of
                                 			 users.

For example, you can specify that users have calls transferred
                           		only to internal extensions or that faxes are delivered only to local phone
                           		numbers. (Restriction tables do not affect the phone numbers that users can
                           		dial directly from their phones when they are not interacting with Unity
                           		Connection.)

Each class of service specifies for its members a restriction
                           		table for call transfers, one for message notification, and one for fax
                           		deliveries. The restriction table can be the same for all three, or different
                           		for each.

### How Restriction Tables Work

When a user uses the Messaging Assistant or the Unity Connection conversation to attempt to change a phone number that is
                              used for call transfer, message notification, or fax delivery, or when signed-in users use the Unity Connection conversation
                              to perform User system transfers to a number that they specify, Unity Connection applies the restriction table associated
                              with the class of service of the user to verify that the phone number entered is allowed.

For example, if a user uses the Unity Connection Messaging Assistant to enter a phone number to set up a message notification
                              device, Unity Connection applies the restriction table that is associated with the class of service of that user, and displays
                              an error message if the phone number is not allowed.But when an administrator changes a message notification number for a
                              user using Cisco Unity Connection Administration, Unity Connection does not apply any restriction table to the number. Therefore,
                              an administrator can, when necessary, override the limitations of the class of service of a particular user.

The User-Defined and Automatically-Added Alternate Extensions restriction table functions similarly to other restriction tables
                              in that it restricts the numbers the users can use to create alternate extensions for themselves through interfaces such as
                              the Cisco Personal Communications Assistant or via an API call. It can also restrict a number from being offered as an alternate
                              extension when a user frequently calls Unity Connection and signs in from the number. (The table is named Excluded Extensions
                              for Automatically-Added Alternate Extensions, and does not apply to alternate extensions that users create for themselves
                              in Cisco PCA.) Unlike other restriction tables, this restriction table applies to all users and therefore is not associated
                              with a class of service. It also applies when administrators use Unity Connection Administration to change user-defined alternate
                              extensions, but does not apply when administrators enter or change administrator-defined alternate extensions.

Each row of a restriction table is made up of a dial string. Each dial string consists of a call pattern and a setting that
                              specifies whether numbers that match the call pattern can be called. In most cases, the restriction table is applied when
                              a user attempts to change a number that is controlled by a restriction table, not when Unity Connection tries to complete
                              a transfer or delivery. In the case of Caller system transfers, which allow unauthenticated callers to transfer to a number
                              that they specify, Unity Connection checks the specified number against the Default System Transfer table. By default, this
                              table blocks all numbers, in order to protect against toll fraud and unauthorized use.

When a restriction table is applied to a number (such as a pager number for a message notification), Unity Connection compares
                              the number with the call pattern of the first dial string in the restriction table. If the number does not match the call
                              pattern, Unity Connection then compares the number with the call pattern in the second dial string, and so on, until it finds
                              a match. When Unity Connection finds a match, it either permits or restricts calling the number as specified in the dial string.

Restriction tables are commonly used to permit or restrict calls to the following:

Specific numbers, such as an extension.

Numbers that are greater than or less than a specific length.

Numbers that contain a specific digit or pattern of digits, such as an external access code followed by a long-distance access
                                    code.

For example, the restriction table below restricts most long distance phone numbers, but permits extensions starting with
                              “91.” In this case, if a user enters “9123” as a transfer number, Unity Connection first compares the number to the call pattern
                              in Dial String 0, which restricts all numbers that begin with “91” and are followed by at least seven digits. Because the
                              number entered does not match the call pattern, Unity Connection then compares the number to Dial String 1, which restricts
                              all numbers that begin with “9011” and are followed by at least seven digits. Finally, Unity Connection compares the number
                              to the last dial string, which contains the wildcard character that matches all numbers of any length. Because the Allow This
                              String field is set to Yes for this dial string, Unity Connection permits this number to be used.

Dial String

Call Pattern

Allow This String

0

91???????*

No

1

9011???????*

No

2

*

Yes

The restriction table below restricts long distance phone numbers and numbers with fewer than four digits. In this example,
                              “9” is the external access code for the phone system, and “1” is the long-distance access code. Dial String 0 restricts any
                              number beginning with “91,” while numbers fewer than four digits in length are restricted by Dial String 2. Thus, the only
                              numbers permitted by this restriction table have at least four digits, and are not long distance phone numbers.

Dial String

Call Pattern

Allow This String

0

91*

No

1

????*

Yes

2

*

No

In Unity Connection 10.5(1) and later, you can also restrict the call pattern of a URI. For example, you can restrict the
                                          call pattern that starts the user portion with “abc” and belongs to the hostname “dummy.com” (such as, abc*@dummy.com).

### Default
                           	 Restriction Table

Unity Connection comes with the
                                 		  following predefined restriction tables that you can edit (including changing
                                 		  their names) but not delete. By default, each of these restriction tables
                                 		  prevents access to long distance phone numbers.

In Unity Connection 10.5 and later, you can restrict URIs along
                                             			 with the phone numbers.

Default Fax

Restricts numbers for fax delivery.

Default Outdial

Restricts numbers for message notifications. Also restricts the
                                             						user extensions that Unity Connection dials when the phone is selected as the
                                             						recording and playback device in the Media Player.

Default System
                                             						Transfer

Restricts numbers that can be used for Caller system transfers,
                                             						which allow unidentified callers to transfer to a number that they specify. For
                                             						example, callers may want to dial a lobby or conference room phone that is not
                                             						associated with a Unity Connection user. By default, the table does not allow
                                             						Unity Connection to dial any numbers.

Default Transfer

Restricts numbers for call transfers.

User-Defined and Automatically-Added Alternate Extensions

Restricts the numbers the users can use to create alternate
                                             						extensions for themselves through interfaces such as the Cisco Personal
                                             						Communications Assistant or via an API call. Also restricts numbers from being
                                             						offered as alternate extensions. For example, you might block a lobby or
                                             						conference room extension so that users who frequently call Unity Connection
                                             						from those shared phones are not automatically prompted to add the number as an
                                             						alternate extension.

Excluded Extensions for Automatically Added Alternate Extensions

Restricts numbers from being offered as alternate extensions.
                                             						For example, you might add a lobby or conference room extension so that users
                                             						who frequently call Unity Connection from those shared phones are not
                                             						automatically prompted to add the number as an alternate extension.

### Configuring Restriction Tables

You can edit the predefined restriction tables, and you can create up to 100 new ones. You can also add up to 50 dial strings
                                 to a table. New dial strings are automatically inserted into the restriction table as Dial String 0. Note that the order of
                                 the dial strings is very important because Unity Connection sequentially compares a phone number to the call patterns in the
                                 restriction table, starting with Dial String 0. If a number matches more than one call pattern, the number is handled according
                                 to the first call pattern it matches.

You can indicate call patterns by entering
                                 		  specific numbers or using the following special characters as wildcards:

*

Matches zero or more alphanumeric
                                             						strings.

?

Matches exactly one digit or
                                             						character. Use? as a placeholder for a single digit.

#

Corresponds to the # key on the phone.

By default, all restriction tables have * as the
                                 		  call pattern in the last dial string of the table. You cannot edit this call
                                 		  pattern setting, as it prevents a case in which the entered number does not
                                 		  match any call pattern in the table. However, you can change the Blocked field
                                 		  setting for this dial string to either permit or restrict a number.

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings > and select Restriction Tables .

The Search Restriction Tables page displays
                                             				the currently configured restriction tables.

Step 2

Configure a restriction table (For
                                          			 information on each field, see Help> This Page):

To add a restriction table:

On the Search Restriction Tables page,
                                       				select Add New.

On the New Restriction Table page, enter the
                                       				values of the required fields.

On the Edit Restriction Table page, add
                                       				patterns to the restriction table and select Save.

To edit a restriction table:

On the Search Restriction Tables page,
                                       				select the restriction table that you want to delete.

On the Edit Restriction Tables page, change
                                       				the settings as applicable.

To change the order of the patterns, select Change Order . To move a pattern within
                                       				the list, on the Change Restriction Pattern Order page, select the pattern,
                                       				then select the down or up arrows as applicable.

When you have finished with the changes,
                                       				select Save

To delete a restriction table:

On the Search Restriction Tables page, check
                                       				the check box adjacent to the display name of the restriction table that you
                                       				want to delete.

Select Delete Selected and OK to confirm deletion.

If the restriction table you are
                                                   				  attempting to delete is referenced by a class of service, you receive an error
                                                   				  message and are not able to delete the table until you find and remove the
                                                   				  reference.

## Schedules

Unity Connection use schedules to determine which user transfer rule to apply and which user greeting to play. You must review
                           the active schedule specified in the user template before adding a user. You either need to edit an existing user template
                           or create a new user template to specify a different schedule.

If you change the active schedule specified on a user template, the existing users based on that template are not assigned
                                       to the new schedule.

When you edit an existing schedule, the changes are applied to both new and existing users of that schedule. Therefore, you
                           can edit the schedule settings before and after you create user accounts. You can also re-assign a user to a different schedule
                           at any time.

### Default Schedules

Unity Connection has the following predefined schedules that you can edit but cannot delete:

All Hours: This schedule is configured to be active 24 hours a day, seven days a week, and with no holidays. The routing rules
                                    that follow this schedule are always active and the call handlers that use this schedule never use closed hour transfer settings
                                    or play closed greetings.

Weekdays: This schedule is configured to be active from 8 a.m. to 5 p.m. (in the timezone of the Unity Connection server)
                                    from Monday through Friday. It is also configured to observe any days and times that are set in the default Holidays schedule.

Voice Recognition Update: This schedule dictates the times and days when the Unity Connection voice recognition transport
                                    utility can automatically rebuild the voice recognition name grammars if there are pending changes. By default, all days and
                                    times are active for this schedule but re-building large names affects the system performance adversely.

### Configuring Schedules

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings and select Schedules.

The Search Schedules page appears displaying the currently
                                             				configured schedules.

Step 2

Configure a schedule (For more information on each field, see
                                          			 Help> This Page):

To add a schedule:

On the Search Schedules page, select Add
                                                   					 New.

On the New Schedule page, enter the
                                                   					 Display Name and select Save.

On the Edit Schedule Basics page, enter
                                                   					 the values of the required fields and select Save.

To edit an existing schedule:

On the Search Schedules page, select the
                                                   					 schedule that you want to edit.

On the Edit Schedule Basics page, enter
                                                   					 the values of the required fields and select Save.

If you remove schedule details from a
                                                               						schedule, the schedule is never active.

To delete a schedule:

On the Search Schedules page, check the
                                                   					 check boxes to select the schedule you want to delete and select Show
                                                   					 Dependencies.

Assign the dependent Unity Connection
                                                   					 components to any other schedule.

Select Delete Selected and OK to confirm
                                                   					 deletion.

## Holiday Schedules

You can setup a holiday schedule that can be played on Unity Connection users or call management components for a specified
                              date and time. The date and time depends on the timezone assigned to the Unity Connection server.

When a holiday schedule is in effect, Unity Connection only plays the holiday greeting (if enabled) and observes closed hour
                              transfer rules. You can set up several years of holidays at a time. There is a default Holiday schedule that can be modified
                              but cannot be deleted.

For each schedule that you create or edit, you can identify multiple ranges of hours and days that make up the standard and
                              closed hours, and associate a holiday schedule that defines specific holiday dates and times:

Standard hours

The hours and days that make up the normal business hours, when the organization is open. Standard hours can include multiple
                                          time ranges and different time ranges on different days. (For example, standard hours for an organization might be Monday
                                          through Friday from 8 a.m. to 12 p.m. and 1 p.m. to 5 p.m., to accommodate a lunch break, and Saturday from 9 a.m. to 1 p.m.)

Standard transfer rules are in effect during the days and time ranges you add to the standard schedule; standard user and
                                          call handler greetings play during standard hours.

Closed hours

The hours and days not identified as standard hours are considered nonbusiness hours, when the organization is closed.

Closed user and call handler transfer rules operate at all times not specified by the standard schedule—including holidays;
                                          closed user and call handler greetings play according to the closed schedule.

Holidays

When a Holiday setting is in effect, Unity Connection plays holiday greetings (if enabled) and observes closed hours transfer
                                          rules. You can set up several years of holidays at a time. Because many holidays occur on different dates each year, confirm
                                          that the holiday schedule remains accurate annually.

Closed user and call handler transfer rules operate at all times not specified by the standard schedule—including holidays;
                                          holiday greetings for users and call handlers also play during this time period.

### Configuring Holiday Schedules

Step 1

In Cisco Unity Connection Administration,
                                          			 expand System Settings and select Holiday Schedules.

The Search Holiday Schedules page appears
                                             				displaying the currently configured holiday schedules.

Step 2

Configure a holiday schedule (Fore more information on each field,
                                          			 see Help> This Page):

To add a holiday schedule:

On the Search Holiday Schedules page,
                                                   					 select Add New.

On the New Holiday Schedule page, enter
                                                   					 the Display Name and select Save.

On the Edit Holiday Schedule Basics
                                                   					 page, enter the values of the required fields and select Save.

To edit an existing schedule:

On the Search Holiday Schedule page,
                                                   					 select the schedule that you want to edit.

On the Edit Holiday Schedule Basics
                                                   					 page, enter the values of the required fields and select Save.

To delete a schedule:

On the Search Holiday Schedule page,
                                                   					 select the schedule that you want to delete.

Select Delete Selected and OK to confirm
                                                   					 deletion.

## Custom Recordings

Unity Connection allows you to record and play multiple customized recordings in various languages, after message is send
                           or greeting is played.

In Cisco Unity Connection Administration, after the message is sent, you have the options to play no recording, default system
                           recording, or custom recordings.

The Play After Message Recording and Custom Recording options can be set for the following:

Users

User Templates

Call Handlers

Call Handler Templates

### Configuring Custom
                           	 Recordings

This section includes information on configuring a custom
                                 		  recording for Unity Connection, define the settings for the custom recording
                                 		  and save them.

Step 1

In Cisco Unity Connection Administration, expand Call Management
                                          			 and select Custom Recordings.

The Search Custom Recordings page displays the currently
                                             				recorded custom recordings.

Step 2

Configure a custom recording: (For information on each field,
                                          			 see Help> This Page):

To add a custom recording:

On the Search Custom Recording page, select Add New.

On New Custom Recording page, enter the display name and select
                                                   					 Save.

On the Edit Custom Recording page, select the language in which
                                                   					 you want to record and select Play/Record. When you are finished with the
                                                   					 recording, select Save.

To record each custom recording, you need to use the Media
                                                               						Player on the Edit Custom Recording page.

To edit a custom recording:

On the Search Custom Recordings page, select the custom
                                                   					 recording that you want to edit.

On the Edit Custom Recording page, edit the custom recording
                                                   					 settings and select Save.

To delete a custom recording:

On the Search Custom Recording page, select the custom recording
                                                   					 that you want to delete.

Select Delete Selected and OK to confirm deletion.

## Default Automated Attendant Behavior

The following example uses the default Unity Connection automated attendant configuration to illustrate a call flow through
                           various call management elements. It illustrates some of the default behavior that you can expect if you have not changed
                           the call management configuration after installing Unity Connection.

Consider an outside caller that does not have a Unity Connection mailbox dials the main phone number in Unity Connection at
                           9:00 a.m. on a Monday morning. The following steps describes the call flow:

Information from the phone system indicates that the call is a direct call from an outside caller. Unity Connection checks
                                 the call routing rules for a rule that matches the call. The Direct routing rules table contains two entries: Attempt Sign
                                 In and Opening Greeting. For the Attempt Sign-In rule, Unity Connection attempts to match the caller phone number with the
                                 extension or alternate extension of a Unity Connection user. When this fails, Unity Connection tries the next routing rule,
                                 the Opening Greeting rule.

The Opening Greeting call routing rule matches any incoming call at any time of day. It is configured to attempt to route
                                 the call to the Opening Greeting call handler.

Unity Connection checks the transfer option settings for the Opening Greeting call handler. Because the call came in during
                                 the Weekdays active schedule, the standard transfer options apply. These specify to send the call to the greeting for this
                                 call handler. (Note that if the Opening Greeting call routing rule had been configured to send the call to the greeting for
                                 the Opening Greeting call handler rather than attempting to transfer to it, this step would be skipped).

Because the call came in during the Weekdays active schedule from a phone number that did not match an internal Unity Connection
                                 user, Unity Connection plays the standard greeting for the call handler: “Hello: Cisco Unity Connection Messaging System.
                                 From a touchtone phone you may dial an extension at any time. For a directory of extensions, press 4. Otherwise, please hold
                                 for an operator.”

While the greeting plays, as the greeting indicates, the caller can enter digits to reach a user extension. The caller input
                                 settings on the Opening Greeting call handler also define several one-key dialing actions that can be taken—for example, when
                                 the caller presses key 4, Unity Connection is configured to send the call to the System Directory Handler if no other keys
                                 are pressed within the time configured to wait for additional digits.

If no digits are entered, Unity Connection proceeds with the after greeting action for the Standard greeting on this call
                                 handler, which is configured to attempt to transfer the call to the Operator call handler.

The Operator call handler is also configured for the Weekdays active schedule, and once again, Unity Connection checks the
                                 standard transfer options for the call handler, which specify to transfer to the call handler greeting. The greeting plays:
                                 “Sorry, the operator is not available.”

The after greeting action for this greeting directs Unity Connection to take a message. The message settings for this call
                                 handler specify that the Operator user receives the message, and that after the caller leaves the message, Unity Connection
                                 should hang up.

| Components | Usage |
|---|---|
| Call Handlers | Answer calls and take messages; provide menus of options (for example, “For customer service press 1, for sales press 2...”);
                                          route calls to the users and other call handlers; and play audiotext (prerecorded information). |
| Directory Handlers | Provide access to a corporate directory by playing an audio list that users and outside callers use to reach a users and leave
                                          messages. |
| Interview Handlers | Collect information from callers by playing a series of questions and then recording the answers. |
| Call Routing Tables | Allow you to define how calls are initially routed, based on criteria such as the phone number of the caller and the schedule.
                                          When you have set up call handlers, interview handlers, directory handlers, and extensions for users, you can route the calls
                                          to the applicable person or handler by editing the call routing tables. |
| Restriction Tables | Control outgoing calls by allowing you to specify the numbers that Unity Connection can dial for transferring calls, for notifying
                                          users of messages, and for delivering faxes. |
| Schedules and Holidays | Define business, nonbusiness, and holiday hours for the organization for the purpose of controlling which set of call routing
                                          rules, greetings, or transfer options is currently active. |

| Note | Unity Connection supports 40,000 system call handlers. |
|---|---|

| Note | If you change settings on a call handler template, the new settings are in effect only for new call handlers that are created
                                          using that template. |
|---|---|

| System Call Handler Template | The settings on this template are suitable for most call handlers. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Templates > and select > Call Handler Templates . The Search Call Handler Templates page
                                                				displays the currently configured call handler templates. |
|---|---|
| Step 2 | Configure a call handler template (For
                                             			 information on each field, see Help> This Page): To add a call handler template, select
                                                      					 Add New. The New Call Handler Template page appears. Enter the applicable
                                                      					 settings and select Save. To edit a call handler template, select
                                                      					 the call handler template. On the Edit Call Handler Template Basics page,
                                                      					 select the applicable settings from the Edit menu: Call Handler Template Basics Transfer Rules Caller Input Greetings Post Greeting Recording Message Settings To delete a call handler template, do
                                                      					 the following: In the Search Call Handler Templates
                                                      					 page, select the call handler template that you want to delete. Select Delete Selected and then select
                                                      					 OK to confirm deletion. |

| Note | You should at least edit the greetings for these call handlers. |
|---|---|

| Opening Greeting | Acts as an automated attendant, playing the greeting that callers first hear when they call your organization, and performing
                                             the actions you specify. The Opening Greeting Call Routing rule transfers all incoming calls to the Opening Greeting call
                                             handler. By default, the Opening Greeting call handler allows callers to press * to reach the Sign-In conversation, or press # to reach
                                             the Operator call handler. Messages left in the Opening Greeting call handler are sent to the Undeliverable Messages distribution
                                             list. |
|---|---|
| Operator | Calls are routed to this call handler when callers press “0” or do not press any key (the default setting). You can configure
                                             the Operator call handler so that callers can leave a message or can be transferred to a live operator. By default, the Operator call handler allows callers to press * to reach the Sign-In conversation, or press # to reach the
                                             Opening Greeting call handler. Messages left in the Operator call handler are sent to the mailbox for the Operator user. |
| Goodbye | Plays a short goodbye message and then hangs up if there is no caller input. By default, the Goodbye call handler allows callers to press * to reach the Sign-In conversation, or press # to reach the
                                             Opening Greeting call handler. If you change the After Greeting action from Hang Up to Take Message, messages left in the
                                             Goodbye call handler are sent to the Undeliverable Messages distribution list. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Call Management and
                                          			 select System Call Handler . The Search Call Handlers page displays the
                                             				currently configured call handlers. |
|---|---|
| Step 2 | Configure a system call handler (For
                                          			 information on each field, see Help > This Page): |

| Note | Each system call handler can have up to seven greetings. |
|---|---|

| Standard | Plays at all the times unless overridden by another greeting. You cannot disable the standard greeting. |
|---|---|
| Closed | Plays during the closed (nonbusiness) hours defined for the active schedule. A closed greeting overrides the standard greeting. |
| Holiday | Plays during the specific dates and times specified in the schedule of holidays associated with the active schedule. A holiday
                                             greeting overrides the standard and closed greetings. |
| Internal | Plays for internal callers only. It can provide information that only co-worker needs to know. An internal greeting overrides
                                             the standard, closed, and holiday greetings. Not all phone system integrations provide the support necessary for an internal
                                             greeting. |
| Busy | Plays when the extension is busy. A busy greeting overrides the standard, closed, internal, and holiday greetings. Not all phone system integrations provide the support necessary for a busy greeting. |
| Alternate | Can be used for a variety of special situations, such as vacations or a leave. An alternate greeting overrides all other greetings. |
| Error | Plays if the caller enters invalid digits. This may happen if the digits do not match an extension, the extension is not found
                                             in the search scope, or the caller is otherwise restricted from dialing the digits. You cannot disable the error greeting. The system default error recording is, “I did not recognize that as a valid entry.” By default, after the error greeting plays,
                                             Unity Connection replays the greeting. |

| Note | Call handler greetings can be recorded in multiple languages when the language for the call handler is inherited from the
                                             caller. For example, if Unity Connection is configured to provide prompts in French and Spanish, it is possible to record
                                             the standard greeting in both languages so that Spanish- and French-speaking callers can hear the greeting in their own language. |
|---|---|

| Note | With Unity Connection 10.5 and later, both the users and distribution lists can be added as the call handler owners. However,
                                          only the local users (not the members of nested distribution lists) in a distribution list can added as call handler owners. |
|---|---|

| Phone Keypad | Callers enter search information or extensions using the phone keypad. For this type of directory handler, you can specify
                                          how it searches for names, what it does when it finds one or more matches, and what it does when it detects no caller input. |
|---|---|
| Voice Enabled | Callers say the first name and last name of the Unity Connection user that they want to reach, or enter an extension by saying
                                          the individual digits in the extension. The voice directory handler can also include alternate names in searches. The voice-recognition
                                          option is required in order to create voice-enabled directory handlers. Users who are listed in the directory are available to outside callers but administrator-defined contacts are only available
                                          to users who are signed in to Unity Connection. User-defined contacts are only available to the Unity Connection users who
                                          defined them. Note For this type of directory handler, users cannot be accessed using directory handlers unless they have a display name specified
                                                      and the List in Directory check box is checked for them on the User Basics page. | Note | For this type of directory handler, users cannot be accessed using directory handlers unless they have a display name specified
                                                      and the List in Directory check box is checked for them on the User Basics page. |
| Note | For this type of directory handler, users cannot be accessed using directory handlers unless they have a display name specified
                                                      and the List in Directory check box is checked for them on the User Basics page. |

| Note | For this type of directory handler, users cannot be accessed using directory handlers unless they have a display name specified
                                                      and the List in Directory check box is checked for them on the User Basics page. |
|---|---|

| Note | You can create both phone-keypad and voice-enabled directory handlers on the same system. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Call Management and select Directory Handlers. The Search Directory Handlers page displays
                                             				the currently configured directory handlers. |
|---|---|
| Step 2 | Configure a directory handler, (For
                                          			 information on each field, see Help> This Page): To add a directory handler: On the Search Directory Handlers page,
                                                   					 select Add New. On the New Directory Handler page, enter
                                                   					 the applicable settings and select Save. To edit a directory handler: On the Search Directory Handlers page,
                                                   					 select the directory handler you want to edit. To edit multiple system
                                                   					 directory handlers, check the applicable check boxes and select Bulk Edit. On the Edit Directory Handler Basics
                                                   					 page, select the Edit menu and then select any of the following settings: Directory Handler Basics Caller Input Greetings After editing the settings, select
                                                         						  Save before leaving the page. To delete a directory handler: On the Directory Handlers page, select
                                                   					 the directory handler to delete. Select Show Dependencies to search the
                                                   					 database objects that have dependencies on the directory handler you want to
                                                   					 delete. From the dependencies search results, follow links to the affected
                                                   					 objects and reassign the dependency to another directory handler. Select Delete Selected. |

| Step 1 | In Cisco Unified Communications Manager
                                          			 Administration, add the ports that you want to use for the voice-type directory
                                          			 handler to a new line group. |
|---|---|
| Step 2 | Add the line group to a new hunt list. |
| Step 3 | Add the hunt list to a new hunt pilot to
                                          			 which calls for the voice-type directory handler is routed. |
| Step 4 | In Cisco Unity Connection Administration,
                                          			 configure the ports to route calls to the voice-type directory handler. |
| Step 5 | For details on configuring Cisco Unified CM,
                                          			 see the Cisco Unified CM documentation at http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html . |

| Note | With Cisco Unity Connection Release 14SU1 and later, the maximum recording time for one Interview Handler Question is 300
                                       seconds. If you want to record Interview Handler Question of length more than 300 seconds, you should record multiple questions.The
                                       maximum number of questions that can be recorded on Unity Connection is 20. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Call Management and select Interview Handlers. The Search Interview Handlers page displays
                                             				the currently configured interview handlers. |
|---|---|
| Step 2 | Configure an interview handler, (For
                                          			 information on each field, see Help> This Page): |

| Note | Changing the system default partition and search space do not affect any objects or templates that have already been created. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand System Settings and
                                             			 select General Configuration . |
|---|---|
| Step 2 | In the Edit General Configuration page, in
                                             			 the Default Partition field, select the name of the new default partition. |
| Step 3 | In the Default Search Scope field, select
                                             			 the name of the new default search space and select Save . |

| Note | When you change partition of an alternate extension in a bulk edit mode, the primary extension of the user is taken as an
                                          alternate extension. If primary extension already exist in the changed partition then it throws an error message with the
                                          duplicate extension. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Dial
                                                   				  Plan > and select Partitions . |
|---|---|
| Step 2 | The Search Partitions page displays the currently configured
                                             			 partitions. |
| Step 3 | Configure partitions (For more information on each field, see
                                             			 Help> This Page): To add a partition, select Add New . On the New Partition page, enter a name for the partition and
                                                      					 select Save. The Edit Partition page appears, you can optionally add a
                                                      					 description and select Save. Note You can change the name or description of a partition. To change
                                                                  						the partition membership, you must edit the individual member objects. To edit a partition, select the partition you want to edit. On
                                                      					 the Edit Partition page, change the settings as applicable and select Save . To delete a partition, check the check boxes next to the display
                                                      					 name of the partitions that you want to delete. Select Delete Selected and OK
                                                      					 to confirm deletion. Note You can delete a partition when the partition is empty (there
                                                                  						are no objects that are members of the partition) and when the partition is not
                                                                  						configured as the system default partition. If you attempt to delete a
                                                                  						partition that is not empty, Unity Connection warns you that the partition is
                                                                  						in use and does not allow the deletion. | Note | You can change the name or description of a partition. To change
                                                                  						the partition membership, you must edit the individual member objects. | Note | You can delete a partition when the partition is empty (there
                                                                  						are no objects that are members of the partition) and when the partition is not
                                                                  						configured as the system default partition. If you attempt to delete a
                                                                  						partition that is not empty, Unity Connection warns you that the partition is
                                                                  						in use and does not allow the deletion. |
| Note | You can change the name or description of a partition. To change
                                                                  						the partition membership, you must edit the individual member objects. |
| Note | You can delete a partition when the partition is empty (there
                                                                  						are no objects that are members of the partition) and when the partition is not
                                                                  						configured as the system default partition. If you attempt to delete a
                                                                  						partition that is not empty, Unity Connection warns you that the partition is
                                                                  						in use and does not allow the deletion. |

| Note | You can change the name or description of a partition. To change
                                                                  						the partition membership, you must edit the individual member objects. |
|---|---|

| Note | You can delete a partition when the partition is empty (there
                                                                  						are no objects that are members of the partition) and when the partition is not
                                                                  						configured as the system default partition. If you attempt to delete a
                                                                  						partition that is not empty, Unity Connection warns you that the partition is
                                                                  						in use and does not allow the deletion. |
|---|---|

| Search Space | Partition Membership (in Order) |
|---|---|
| Employees search space | Employee, Customer Service |
| Customer Service search space | Customer Service |

| Search Space | Partition Membership (in Order) |
|---|---|
| Headquarters-SS | HQ, Primary, RE, RW |
| Regional-East-SS | RE, Primary |
| Regional-West-SS | RW, Primary |

| User | Home Server | Search Space of User | Primary Extension and Partition | Alternate Extension and Partition |
|---|---|---|---|---|
| Alex Abade | Headquarters | Headquarters-SS | 85553001, Primary | 3001, HQ |
| Chris Brown | Headquarters | Headquarters-SS | 85553002, Primary | 3002, HQ |
| Pat Smith | Regional-East | Regional-East-SS | 82223001, Primary | 3001, RE |
| Shannon Johnson | Regional-East | Regional-East-SS | 82223002, Primary | 3002, RE |
| Robin Smith | Regional-West | Regional-West-SS | 87773001, Primary | 3001, RW |
| Terry Jones | Regional-West | Regional-West-SS | 87773333, Primary | 3333, RW |

| Step 1 | In Cisco Unity Connection Administration,
                                             			 expand Dial Plan and select Search Spaces . |
|---|---|
| Step 2 | Configuring search spaces (For more
                                             			 information on each field, see Help> This Page): To add new search space, select Add New . On the New Search Space page, enter a
                                                      					 name for the search space and select Save. In the Edit Search Space page, enter a
                                                      					 description for the search space and select Save . To edit a search space, select the name
                                                      					 of the search space that you want to edit. On the Edit Search Space page,
                                                      					 change the settings as applicable and select Save. To delete a search space, check the
                                                      					 check box next to the display names of the search spaces that you want to
                                                      					 delete. Select Delete Selected and OK to confirm deletion. Note You can delete a search space even when there are objects
                                                               					 using it; however, in this case you must select a replacement search space.
                                                               					 Objects that had a search scope set to the deleted search space are changed to
                                                               					 use the replacement search space instead. You cannot delete more than 50 search
                                                      					 spaces simultaneously. | Note | You can delete a search space even when there are objects
                                                               					 using it; however, in this case you must select a replacement search space.
                                                               					 Objects that had a search scope set to the deleted search space are changed to
                                                               					 use the replacement search space instead. |
| Note | You can delete a search space even when there are objects
                                                               					 using it; however, in this case you must select a replacement search space.
                                                               					 Objects that had a search scope set to the deleted search space are changed to
                                                               					 use the replacement search space instead. |

| Note | You can delete a search space even when there are objects
                                                               					 using it; however, in this case you must select a replacement search space.
                                                               					 Objects that had a search scope set to the deleted search space are changed to
                                                               					 use the replacement search space instead. |
|---|---|

| Note | With Unity Connection 10.0(1) and later, a user can play and record both video and audio greetings, when login via Attempt
                                                      Sign-in. |
|---|---|

| Note | With Unity Connection 10.0(1) and later, a user can play both video and audio greetings, when the calling user receives unanswered
                                                call. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand Call Management> Call Routing . If you want to configure routing rules
                                                   					 for direct calls, select Direct Routing Rules. The Direct Routing Rules page
                                                   					 displays the default and currently configured routing rules. If you want to configure routing rules
                                                   					 for forwarded calls, select Forwarded Routing Rules. The Forwarded Routing
                                                   					 Rules page displays the default and currently configured routing rules. |
|---|---|
| Step 2 | Configure a routing rule in the direct or forwarded routing rules:
                                          			 (For information on each field, see Help> This Page): To add a routing rule, select Add New. On New Direct Routing Rule page or New
                                                   					 Forwarded Routing Rule page, enter the applicable settings and select Save. To add the routing rule condition,
                                                   					 select Add New on the Edit Routing Rule page. Edit the routing rule condition settings
                                                   					 and select Save. To delete a routing rule, do the
                                                   					 following: On the Search Contacts page, select the
                                                   					 routing rule to delete. Select Delete Selected. |

| Rule | Status | Dialed  Number | Calling  Number | Phone  System | Port | Schedule | Send Call To |
|---|---|---|---|---|---|---|---|
| Operator | Active | Any | Any | Any | Any | Weekdays | Attempt transfer for operator |
| Attempt Sign-In | Active | Any | Any | Any | Any | Always | Attempt Sign-In |
| Opening Greeting | Active | Any | Any | Any | Any | Always | Attempt transfer for Opening Greeting |

| Rule | Status | Dialed  Number | Calling  Number | Forwarding Station | Phone  System | Port | Schedule | Send Call To |
|---|---|---|---|---|---|---|---|---|
| Customer Service | Active | Any | Any | 5678 | Any | Any | Always | Attempt transfer for Customer Service |
| Product Info | Active | Any | Any | 1234 | Any | Any | Always | Send to greeting for Product Info |
| Attempt Forward | Active | Any | Any | Any | Any | Any | Always | Attempt Forward |
| Opening Greeting | Active | Any | Any | Any | Any | Any | Always | Attempt transfer for Opening Greeting |

| Dial String | Call Pattern | Allow This String |
|---|---|---|
| 0 | 91???????* | No |
| 1 | 9011???????* | No |
| 2 | * | Yes |

| Dial String | Call Pattern | Allow This String |
|---|---|---|
| 0 | 91* | No |
| 1 | ????* | Yes |
| 2 | * | No |

| Note | In Unity Connection 10.5(1) and later, you can also restrict the call pattern of a URI. For example, you can restrict the
                                          call pattern that starts the user portion with “abc” and belongs to the hostname “dummy.com” (such as, abc*@dummy.com). |
|---|---|

| Note | In Unity Connection 10.5 and later, you can restrict URIs along
                                             			 with the phone numbers. |
|---|---|

| Default Fax | Restricts numbers for fax delivery. |
|---|---|
| Default Outdial | Restricts numbers for message notifications. Also restricts the
                                             						user extensions that Unity Connection dials when the phone is selected as the
                                             						recording and playback device in the Media Player. |
| Default System
                                             						Transfer | Restricts numbers that can be used for Caller system transfers,
                                             						which allow unidentified callers to transfer to a number that they specify. For
                                             						example, callers may want to dial a lobby or conference room phone that is not
                                             						associated with a Unity Connection user. By default, the table does not allow
                                             						Unity Connection to dial any numbers. |
| Default Transfer | Restricts numbers for call transfers. |
| User-Defined and Automatically-Added Alternate Extensions | Restricts the numbers the users can use to create alternate
                                             						extensions for themselves through interfaces such as the Cisco Personal
                                             						Communications Assistant or via an API call. Also restricts numbers from being
                                             						offered as alternate extensions. For example, you might block a lobby or
                                             						conference room extension so that users who frequently call Unity Connection
                                             						from those shared phones are not automatically prompted to add the number as an
                                             						alternate extension. |
| Excluded Extensions for Automatically Added Alternate Extensions | Restricts numbers from being offered as alternate extensions.
                                             						For example, you might add a lobby or conference room extension so that users
                                             						who frequently call Unity Connection from those shared phones are not
                                             						automatically prompted to add the number as an alternate extension. |

| * | Matches zero or more alphanumeric
                                             						strings. |
|---|---|
| ? | Matches exactly one digit or
                                             						character. Use? as a placeholder for a single digit. |
| # | Corresponds to the # key on the phone. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings > and select Restriction Tables . The Search Restriction Tables page displays
                                             				the currently configured restriction tables. |
|---|---|
| Step 2 | Configure a restriction table (For
                                          			 information on each field, see Help> This Page): |

| Note | If the restriction table you are
                                                   				  attempting to delete is referenced by a class of service, you receive an error
                                                   				  message and are not able to delete the table until you find and remove the
                                                   				  reference. |
|---|---|

| Note | If you change the active schedule specified on a user template, the existing users based on that template are not assigned
                                       to the new schedule. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings and select Schedules. The Search Schedules page appears displaying the currently
                                             				configured schedules. |
|---|---|
| Step 2 | Configure a schedule (For more information on each field, see
                                          			 Help> This Page): To add a schedule: On the Search Schedules page, select Add
                                                   					 New. On the New Schedule page, enter the
                                                   					 Display Name and select Save. On the Edit Schedule Basics page, enter
                                                   					 the values of the required fields and select Save. To edit an existing schedule: On the Search Schedules page, select the
                                                   					 schedule that you want to edit. On the Edit Schedule Basics page, enter
                                                   					 the values of the required fields and select Save. Note If you remove schedule details from a
                                                               						schedule, the schedule is never active. To delete a schedule: On the Search Schedules page, check the
                                                   					 check boxes to select the schedule you want to delete and select Show
                                                   					 Dependencies. Assign the dependent Unity Connection
                                                   					 components to any other schedule. Select Delete Selected and OK to confirm
                                                   					 deletion. | Note | If you remove schedule details from a
                                                               						schedule, the schedule is never active. |
| Note | If you remove schedule details from a
                                                               						schedule, the schedule is never active. |

| Note | If you remove schedule details from a
                                                               						schedule, the schedule is never active. |
|---|---|

| Standard hours | The hours and days that make up the normal business hours, when the organization is open. Standard hours can include multiple
                                          time ranges and different time ranges on different days. (For example, standard hours for an organization might be Monday
                                          through Friday from 8 a.m. to 12 p.m. and 1 p.m. to 5 p.m., to accommodate a lunch break, and Saturday from 9 a.m. to 1 p.m.) Standard transfer rules are in effect during the days and time ranges you add to the standard schedule; standard user and
                                          call handler greetings play during standard hours. |
|---|---|
| Closed hours | The hours and days not identified as standard hours are considered nonbusiness hours, when the organization is closed. Closed user and call handler transfer rules operate at all times not specified by the standard schedule—including holidays;
                                          closed user and call handler greetings play according to the closed schedule. |
| Holidays | When a Holiday setting is in effect, Unity Connection plays holiday greetings (if enabled) and observes closed hours transfer
                                          rules. You can set up several years of holidays at a time. Because many holidays occur on different dates each year, confirm
                                          that the holiday schedule remains accurate annually. Closed user and call handler transfer rules operate at all times not specified by the standard schedule—including holidays;
                                          holiday greetings for users and call handlers also play during this time period. |

| Step 1 | In Cisco Unity Connection Administration,
                                          			 expand System Settings and select Holiday Schedules. The Search Holiday Schedules page appears
                                             				displaying the currently configured holiday schedules. |
|---|---|
| Step 2 | Configure a holiday schedule (Fore more information on each field,
                                          			 see Help> This Page): To add a holiday schedule: On the Search Holiday Schedules page,
                                                   					 select Add New. On the New Holiday Schedule page, enter
                                                   					 the Display Name and select Save. On the Edit Holiday Schedule Basics
                                                   					 page, enter the values of the required fields and select Save. To edit an existing schedule: On the Search Holiday Schedule page,
                                                   					 select the schedule that you want to edit. On the Edit Holiday Schedule Basics
                                                   					 page, enter the values of the required fields and select Save. To delete a schedule: On the Search Holiday Schedule page,
                                                   					 select the schedule that you want to delete. Select Delete Selected and OK to confirm
                                                   					 deletion. |

| Step 1 | In Cisco Unity Connection Administration, expand Call Management
                                          			 and select Custom Recordings. The Search Custom Recordings page displays the currently
                                             				recorded custom recordings. |
|---|---|
| Step 2 | Configure a custom recording: (For information on each field,
                                          			 see Help> This Page): To add a custom recording: On the Search Custom Recording page, select Add New. On New Custom Recording page, enter the display name and select
                                                   					 Save. On the Edit Custom Recording page, select the language in which
                                                   					 you want to record and select Play/Record. When you are finished with the
                                                   					 recording, select Save. Note To record each custom recording, you need to use the Media
                                                               						Player on the Edit Custom Recording page. To edit a custom recording: On the Search Custom Recordings page, select the custom
                                                   					 recording that you want to edit. On the Edit Custom Recording page, edit the custom recording
                                                   					 settings and select Save. To delete a custom recording: On the Search Custom Recording page, select the custom recording
                                                   					 that you want to delete. Select Delete Selected and OK to confirm deletion. | Note | To record each custom recording, you need to use the Media
                                                               						Player on the Edit Custom Recording page. |
| Note | To record each custom recording, you need to use the Media
                                                               						Player on the Edit Custom Recording page. |

| Note | To record each custom recording, you need to use the Media
                                                               						Player on the Edit Custom Recording page. |
|---|---|