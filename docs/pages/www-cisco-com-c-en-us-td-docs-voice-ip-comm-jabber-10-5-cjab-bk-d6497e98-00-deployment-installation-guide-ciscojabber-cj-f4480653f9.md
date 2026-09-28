---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-10-5-cjab-bk-d6497e98-00-deployment-installation-guide-ciscojabber-cj-f4480653f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/10_5/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber_chapter_0101.html
retrieved_at: 2026-08-21T05:10:06.807473+00:00
---

Deployment and Installation Guide for Cisco Jabber, Release 10.5

# Deployment and Installation Guide for Cisco Jabber, Release 10.5

Updated: August 14, 2014

Chapter: Configure IM and Presence Service

## Chapter: Configure IM and Presence Service

# Configure IM and Presence Service

## Configure IM and Presence Service  for an On-Premises Deployment

### Configure IM and Presence Service for On-Premises Deployments with
                           	 Cisco Unified Communications Manager 10.5 and Later

Activate and Start Essential Services

Create a Service Profile

Prepopulate Contact Lists in Bulk

Enable Message Settings

Enable File Transfer

Prompts for Presence Subscription Requests

Temporary Presence

Configure Presence in Microsoft SharePoint 2010 and 2013

Configure Users with IM and Presence Service

Enable Presence for Calendar Events

Configure Persistent Chat

### Configure IM and
                           	 Presence Service for On-Premises Deployments with Cisco Unified Communications
                           	 Manager 9.x and Later

Activate and Start Essential Services

Create a Service Profile

Prepopulate Contact Lists in Bulk

Enable Message Settings

Enable File Transfers and Screen Captures

Prompts for Presence Subscription Requests

Temporary Presence

Add an IM and Presence Service

Apply an IM and Presence Service

Configure Presence in Microsoft SharePoint 2010 and 2013

Configure Users with IM and Presence Service

Enable Presence for Calendar Events

Configure Persistent Chat

### Configure IM and Presence Service for  On-Premises Deployments with Cisco Unified Communications Manager 8.x and Cisco Unified
                           Presence

Activate and Start Essential Services

Prepopulate Contact Lists in Bulk

Enable Message Settings

Specify Capabilities Assignments

Prompts for Presence Subscription Requests

Configure Presence in Microsoft SharePoint 2010 and 2013

Temporary Presence

Enable Presence for Calendar Events

### Activate and Start
                           	 Essential Services

Essential services
                                 		  enable communication between servers and provide capabilities to the client.

Open the Cisco
                                             				Unified IM and Presence Serviceability interface.

Select Tools > Control Center - Feature
                                                				  Services .

Select the
                                          			 appropriate server from the Server drop-down list.

Ensure the
                                          			 following services are started and activated:

- Cisco SIP Proxy

- Cisco Sync Agent

- Cisco XCP Authentication
                                                      					 Service

- Cisco XCP Connection
                                                      					 Manager

- Cisco XCP Text Conference
                                                      					 Manager

- Cisco Presence
                                                      					 Engine

Select Tools > Control Center - Network
                                                				  Services .

Select the
                                          			 appropriate server from the Server drop-down list.

Ensure Cisco
                                             				XCP Router Service is running.

### Create a Service
                           	 Profile

You create a service
                                 		  profile that contains the configuration settings for the services you add on 
                                 		  Cisco Unified Communications Manager.
                                 		  You add the service profile to the end user configuration for your users. The
                                 		  client can then retrieve settings for available services from the service
                                 		  profile.

#### Before you begin

Activate and Start Essential Services

Open the Cisco
                                             				Unified CM Administration interface.

Select User
                                                				  Management > User Settings > Service
                                                				  Profile .

The Find
                                                				  and List Service Profiles window opens.

Select Add
                                             				New .

The Service Profile Configuration window opens.

Enter settings
                                          			 on the Service
                                             				Profile Configuration window as follows:

Specify a
                                                				  unique name for the service profile in the Name field.

Select Make
                                                   					 this the default service profile for the system , if appropriate.

For phone mode, in the IM and Presence Profile section ensure
                                                         				  that the Primary field has <None> selected.

Select Save .

### Prepopulate Contact Lists in Bulk

You can pre-populate user contact lists with the Bulk
                                 		  Administration Tool (BAT).

In
                                 		  this way you can prepopulate contact lists for users so that they automatically
                                 		  have a set of contacts after the initial launch of the client.

Cisco Jabber supports up to 300 contacts in a client contact
                                 		  list.

Create a CSV
                                          			 file that defines the contact list you want to provide to users.

Use the BAT to
                                          			 import the contact list in bulk to a set of users.

For more
                                             				information about using BAT and the format of the CSV file, see the Deployment Guide for Cisco Unified Communications Manager IM
                                                				  & Presence for your release.

### Enable Message
                           	 Settings

Enable and configure instant messaging capabilities.

#### Before you begin

Prepopulate Contact Lists in Bulk .

Open the Cisco
                                             				Unified CM IM and Presence Administration interface.

Select Messaging > Settings .

Select the
                                          			 following options:

Enable instant
                                                         						messaging

Allow clients to log
                                                         						instant message history

Allow cut & paste in instant messages

Select other
                                          			 messaging settings as appropriate.

Select Save .

Cisco
                                                            					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
                                                            					 Communications Manager IM and Presence Service release 9.0.x:

Use DND status when user is
                                                                     							 on the phone

Use DND status when user is
                                                                     							 in a meeting

#### What to do next

If you have
                                          				Cisco Unified Communications Manager IM and Presence Service release 9.x and
                                          				later, Add an IM and Presence Service .

If you have
                                          				Cisco Unified Presence Release 8.6, Specify Capabilities Assignments .

### Specify
                           	 Capabilities Assignments

Complete the steps
                                 		  in this task to provide users with instant messaging and presence capabilities
                                 		  when using Cisco Unified Presence.

#### Before you begin

Enable Message Settings

Open the Cisco
                                             				Unified CM Administration interface.

Select System > Licensing > Capabilities
                                                				  Assignment .

The Find
                                                				  and List Capabilities Assignments window opens.

Specify the
                                          			 appropriate filters in the Find
                                             				Capabilities Assignment where field and then select Find to retrieve a list of users.

Select the
                                          			 appropriate users from the list.

The Capabilities Assignment Configuration window opens.

Select both of
                                          			 the following in the Capabilities Assignment Configuration section:

- Enable CUP

- Enable CUPC

Select Save .

### Enable File
                           	 Transfers and Screen Captures

This applies to Cisco Unified Communication Manager IM and Presence Service 9.x, 10.0.x, and 10.5.1. You can enable or disable
                                 file transfers and screen captures using the Cisco XCP Router service on Cisco Unified Communications Manager IM and Presence
                                 Service. File transfers and screen captures parameter is enabled by default.

File transfers and screen captures are supported for both desktop and mobile clients.

Open the Cisco
                                             				Unified CM IM and Presence Administration interface.

Select System > Service
                                                				  Parameters .

Select the
                                          			 appropriate server from the Server drop-down list.

Select Cisco
                                             				XCP Router from the Service drop-down list.

The Service Parameter Configuration window opens.

Locate the Enable
                                             				file transfer parameter.

Select the
                                          			 appropriate value from the Parameter Value drop-down list.

If you
                                                            					 disable the setting on Cisco Unified Communications Manager IM and Presence
                                                            					 Service, you must also disable file transfers and screen captures in the client
                                                            					 configuration.

Select Save .

### Enable File Transfer

Open the Cisco Unified CM IM and Presence Administration interface.

Select Messaging > File Transfer .

In the File Transfer Configuration section, select Peer-to-Peer .

Select Save .

### Prompts
                           	 for Presence Subscription Requests

Applies to: All clients

You can enable or disable prompts for presence subscription requests from contacts within your organization. The client always
                                 prompts users for presence subscription requests from contacts outside your organization.

Users can choose to allow or block contacts from  inside your organization.

you select Allow users to view the availability of other users without being prompted for approval , the client automatically accepts all presence subscription requests without prompting users.

you do not select Allow users to view the availability of other users without being prompted for approval , the client prompts users for all presence subscription requests.

If users choose to block contacts, only their existing contacts can see their availability status. In other words, only those
                                                   contacts who have already subscribed to the user's presence can see their availability status.

When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                         However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list.

Users can choose the following options for contacts from outside your organization:

Have the client prompt them for each presence subscription request.

Block all contacts so that only their existing contacts can see their availability status. In other words, only those contacts
                                                   who have already subscribed to the user's presence can see their availability status.

#### Before you begin

This feature is
                                 		  supported for on-premises deployments and is only available on Cisco Unified Communications Manager, release 8.x or later.

Open the Cisco
                                             				Unified CM IM and Presence Administration interface.

Select Presence > Settings .

The Presence Settings window opens.

Select Allow users to view the availability of other users without being prompted for approval to disable prompts and automatically accept all presence subscription requests within your organization.

Selected—The client does not prompt users for presence subscription requests. The client automatically accepts all presence
                                                      subscription requests without prompting the users.

Cleared—The client prompts users to allow presence subscription requests. This setting requires users to allow other users
                                                      in your organization to view their availability status.

Select Save .

### Temporary
                           	 Presence

Applies to: All clients

Disable temporary
                                 		  presence to increase privacy control. When you configure this parameter, 
                                 		  Cisco Jabber displays availability status only to
                                 		  contacts in a user's contact list.

#### Before you begin

This feature is
                                 		  supported for on-premises deployment and requires 
                                 		  Cisco Unified Communications Manager, release 9.x or later.

Open the Cisco
                                             				Unified CM IM and Presence Administration interface.

Select Presence > Settings > Standard Configuration .

Uncheck Enable
                                             				ad-hoc presence subscriptions and then select Save .

Cisco Jabber does not display temporary presence.
                                             				Users can see availability status only for contacts in their contact list.

### Disable Temporary
                           	 Presence in Cisco Unified Presence

Disable temporary
                                 		  presence to increase privacy control. When you configure this parameter, 
                                 		  Cisco Jabber displays availability status only to
                                 		  contacts in a user's contact list.

#### Before you begin

This feature is
                                 		  supported for on-premises deployment and requires 
                                 		  Cisco Unified Communications Manager, release 8.x or later.

Open the Cisco
                                             				Unified Presence Administration interface.

Select Presence > Settings .

Uncheck Enable
                                             				ad-hoc presence subscriptions and then select Save .

Cisco Jabber does not display temporary presence.
                                             				Users can see availability status only for contacts in their contact list.

### Add an IM and
                           	 Presence Service

Provide users with
                                 		  IM and Presence Service capabilities.

Open the Cisco
                                             				Unified CM Administration interface.

Select User
                                                				  Management > User Settings > UC
                                                				  Service .

The Find
                                                				  and List UC Services window opens.

Select Add
                                             				New .

The UC
                                                				  Service Configuration window opens.

In the Add a UC
                                             				Service section, select IM and
                                             				Presence from the UC
                                             				Service Type drop-down list.

Select Next .

Provide details
                                          			 for the IM and Presence Service as follows:

Select Unified CM (IM and Presence) from the Product Type drop-down list.

Specify a
                                                				  name for the service in the Name field.

The name you
                                                   					 specify displays when you add the service to a profile. Ensure the name you
                                                   					 specify is unique, meaningful, and easy to identify.

Specify an
                                                				  optional description in the Description field.

Specify the
                                                				  instant messaging and presence service address in the Host
                                                   					 Name/IP Address field.

The
                                                               						service address must be a fully qualified domain name or IP address.

Select Save .

#### Apply an IM and
                              	 Presence Service

After you add an
                                    		  IM and Presence Service on 
                                    		  Cisco Unified Communications Manager,
                                    		  you must apply it to a service profile so that the client can retrieve the
                                    		  settings.

##### Before you begin

Add an IM and Presence Service

Open the Cisco Unified CM Administration interface.

Select User Management > User Settings > Service Profile .

The Find and List Service Profiles window opens.

Find and select your service profile.

The Service Profile Configuration window opens.

In the IM and Presence Profile section, select up to three services from the following drop-down lists:

Primary

Secondary

Tertiary

Click Save .

Add users to the service profile.

Select User Management > End User .

The Find and List Users dialog box opens.

Specify the appropriate filters in the Find User where field and then select Find to find a user.

Click the user in the list.

The End User Configuration window appears.

Under the Service Settings area, check the Home Cluster check box.

Check the Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) check box.

Select your service profile from the UC Service Profile drop-down list.

Click Save .

### Configure Presence
                           	 in Microsoft SharePoint 2010 and 2013

If your
                                 		  organization defines users' profiles where their IM address is different from
                                 		  their email address, then additional configuration is required to enable
                                 		  presence integration between the client and Microsoft SharePoint 2010 and 2013.

#### Before you begin

For Cisco Jabber for Windows clients only.

Ensure that
                                       				all sites are in sync with Microsoft SharePoint Central Administration (CA).

Ensure that
                                       				synchronization between Microsoft SharePoint and Active Directory is set up.

If you have
                                          			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                          			 with the following information:

For the SIP Address profile field, leave it blank.

In the Work email profile field, enter the user profile.
                                                				  For example, john4mail@example.pst .

If you have
                                          			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                          			 with the following information:

For the SIP Address profile field, enter the user profile.
                                                				  For example, john4mail@example.pst

In the Work email profile field, leave it blank.

### Configure Users with IM and Presence Service

You can enable users for IM and Presence.

#### Configure Users
                              	 Individually

Enable instant
                                    		  messaging and presence service and add your service profile to individual users.

Open the Cisco
                                                				Unified CM Administration interface.

Select User
                                                   				  Management > End User .

The Find
                                                   				  and List Users window opens.

Specify the
                                             			 appropriate filters in the Find
                                                				User where field and then select Find to retrieve a list of users.

Select the
                                             			 appropriate username from the list.

The End
                                                   				  User Configuration window opens.

Locate the Service
                                                				Settings section and do the following:

Select Home Cluster .

Select Enable User for Unified CM IM and Presence .

Select your
                                                   				  service profile from the UC
                                                      					 Service Profile drop-down list.

Cisco Unified Communications Manager release 9.x only—If the user has
                                                                     						  only instant messaging and presence capabilities (IM only), select Use Default . 
                                                                     						  Cisco Unified Communications Manager release version 9.x applies the default
                                                                     						  service profile regardless of what you select from the UC Service Profile drop-down list.

Select Save .

#### Configure Users in Bulk

Enable instant messaging and presence and add your service profile to multiple users.

Open the Cisco Unified CM Administration interface.

Select Bulk Administration > Users > Update Users > Query .

The Find and List Users To Update window opens.

Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users.

Select Next .

The Update Users Configuration window opens.

Select both of the Enable User for Unified CM IM and Presence check boxes.

There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select
                                                               both check boxes.

Select the UC Service Profile check box and then select your service profile from the drop-down list.

Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities
                                                               (IM only), you must select Use Default .

For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless
                                                               of what you select from the UC Service Profile drop-down list.

In the Job Information section, specify if you want to run the job immediately or at a later time.

Select Submit .

### Enable Presence
                           	 for Calendar Events

This feature is not available for the Cisco Jabber mobile
                                                      					 clients.

- This preference is disabled
                                                   				  by default.

- As of this release, users
                                                   				  must enable the preference individually after deployment. You cannot enable
                                                   				  this preference for multiple users with a bulk task.

Log in to the Cisco
                                             				Unified CM IM and Presence User Options page.

The user
                                             				options page is located at: https:// server_name : port_number /cupuser/showHome.do

Select User
                                                				  Options > Preferences .

Navigate to
                                          			 the Calendar Settings section of the Preferences page.

Select On from the drop-down menu for the Include Calendar information in my Presence Status field.

Select Save .

Log out and
                                          			 close the Cisco
                                             				Unified CM IM and Presence User Options page.

Calendar events
                                 		  change the user's availability status in the client. For example, when meetings
                                 		  occur in the calendar, the availability status is automatically set to In a
                                    			 meeting .

### Configure
                           	 Persistent Chat

Persistent chat
                                 		  must be enabled and configured on Cisco Unified Communications Manager IM and
                                 		  Presence Service before it can be used by the client.

#### Before you begin

For Cisco Jabber desktop clients Persistent chat is available on Cisco Unified Communications Manager IM and Presence Service
                                 10.0 and later.

Refer to Database
                                    			 Setup for IM and Presence Service on Cisco Unified Communications
                                    			 Manager for your release for information on the database configuration
                                 		  necessary to support the persistent chat feature. Database configuration must
                                 		  be performed before continuing with this task.

Local chat message archiving must be enabled for persistent chat. Local chat message archiving is enabled on Cisco Unified
                                 Communications Manager IM and Presence Service using the Allow clients to log instant message history setting, for more information, see the Enable Message Settings topic from the On-Premises Deployment Guide .

Open the Cisco
                                             				Unified CM IM and Presence Administration interface.

Select Messaging > Group Chat and Persistent
                                                				  Chat .

Select Enable
                                             				Persistent Chat .

Ensure the
                                          			 settings How
                                             				many users can be in a room at one time and How
                                             				many hidden users can be in a room at one time under the Occupancy Settings section contain the same,
                                          			 non-zero value.

Configure the remaining settings as appropriate for your persistent chat deployment. We recommend the persistent chat settings
                                          in the following table.

Persistent Chat Setting

Recommended Value

Notes

System automatically manages primary group chat server aliases

Disabled

Enable persistent chat

Enabled

Archive all room joins and exits

Administrator Defined

This value is not currently used by for persistent chat.

Archive all room messages

Enabled

Allow only group chat system administrators to create persistent chat rooms

Administrator Defined

Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment.

Maximum number of persistent chat rooms allowed

Administrator Defined

Number of connections to the database

Default Value

Database connection heartbeat interval (seconds)

Default Value

Timeout value for persistent chat rooms (minutes)

Default Value

Maximum number of rooms allowed

Default Value

Rooms are for members only by default

Disabled

Room owners can change whether or not rooms are for members only

Enabled

Cisco Jabber requires this value to be Enabled.

Only moderators can invite people to members-only rooms

Enabled

Cisco Jabber requires this value to be Enabled.

Room owners can change whether or not only moderators can invite people to members-only rooms

Enabled

Users can add themselves to rooms as members

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether users can add themselves to rooms as members

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Members and administrators who are not in a room are still visible in the room

Enabled

Cisco Jabber requires this value to be Enabled.

Room owners can change whether members and administrators who are not in a room are still visible in the room

Enabled

Rooms are backwards-compatible with older clients

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether rooms are backwards-compatible with older clients

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Rooms are anonymous by default

Disabled

This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms.

Room owners can change whether or not rooms are anonymous

Disabled

This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms.

Lowest participation level a user can have to invite others to the room

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change the lowest participation level a user can have to invite others to the room

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

How many users can be in a room at one time

Administrator Defined

Cisco recommends using the default value.

How many hidden users can be in a room at one time

Administrator Defined

Default maximum occupancy for a room

Default Value

Room owners can change default maximum occupancy for a room

Default Value

Lowest participation level a user can have to send a private message from within the room

Default Value

Room owners can change the lowest participation level a user can have to send a private message from within the room

Default Value

Lowest participation level a user can have to change a room's subject

Moderator

Room owners can change the lowest participation level a user can have to change a room's subject

Disabled

Remove all XHTML formatting from messages

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change XHTML formatting setting

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Rooms are moderated by default

Disabled

This value is not currently used by Cisco Jabber for persistent chat.

Room owners can change whether rooms are moderated by default

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

Maximum number of messages that can be retrieved from the archive

Default Value

Number of messages in chat history displayed by default

Administrator Defined

Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue
                                                         to use their originally configured value.

Room owners can change the number of messages displayed in chat history

Default Value

This value is not currently used by Cisco Jabber for persistent chat.

#### What to do next

Ensure you configure any client-specific parameters for persistent chat. For more information, see the Client parameters section of the latest Parameters Reference Guide for Cisco Jabber .

Enable file transfer in chat rooms. For more information, see Enable File Transfer and Screen Captures for Group Chats and Chat Rooms .

## Configure IM and Presence Service for Cloud-Based Deployments

Configure IM and Presence Service

Configure Presence in Microsoft SharePoint 2010 and 2013

Configure Privacy Options

### Configure IM and
                           	 Presence Service

When users
                                 		  successfully authenticate to the 
                                 		  Cisco WebEx Messenger
                                 		  service, they get IM and Presence Service capabilities. You can
                                 		  optionally configure IM and Presence Service federation with the 
                                 		  Cisco WebEx Administration Tool.

### Configure Presence
                           	 in Microsoft SharePoint 2010 and 2013

If your
                                 		  organization defines users' profiles where their IM address is different from
                                 		  their email address, then additional configuration is required to enable
                                 		  presence integration between the client and Microsoft SharePoint 2010 and 2013.

#### Before you begin

For Cisco Jabber for Windows clients only.

Ensure that
                                       				all sites are in sync with Microsoft SharePoint Central Administration (CA).

Ensure that
                                       				synchronization between Microsoft SharePoint and Active Directory is set up.

If you have
                                          			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                          			 with the following information:

For the SIP Address profile field, leave it blank.

In the Work email profile field, enter the user profile.
                                                				  For example, john4mail@example.pst .

If you have
                                          			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                          			 with the following information:

For the SIP Address profile field, enter the user profile.
                                                				  For example, john4mail@example.pst

In the Work email profile field, leave it blank.

### Configure Privacy Options

You can specify the default settings for presence subscription requests in cloud-based deployments.

Open the Cisco WebEx Administration Tool.

Select the Configuration tab.

Select General IM in the Connect Client section.

Select the appropriate options for contact list requests as follows:

Option

Description

Select Allow users to set "Options for contact list requests"

Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change
                                                      the default option in the Options window.

Do not select Allow users to set "Options for contact list requests"

You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings
                                                      are not available in the Options window.

Accept requests automatically from all contacts

Accept requests automatically from contacts in my organization

Prompt me for each request

The options for configuring how the client handles contact list requests are as follows:

- Accept requests automatically from all contacts — The client automatically accepts presence subscription requests from any
                                             domain. If you specify this setting, users from any domain can automatically add users to their contact list and view their
                                             availability status.

When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                            However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list.

- Prompt me for each request — The client prompts users to accept each presence subscription request.

Select Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate and Start Essential Services |  |
| Step 2 | Create a Service Profile |  |
| Step 3 | Prepopulate Contact Lists in Bulk |  |
| Step 4 | Enable Message Settings |  |
| Step 5 | Enable File Transfer |  |
| Step 6 | Prompts for Presence Subscription Requests |  |
| Step 7 | Temporary Presence |  |
| Step 8 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 9 | Configure Users with IM and Presence Service |  |
| Step 10 | Enable Presence for Calendar Events |  |
| Step 11 | Configure Persistent Chat |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate and Start Essential Services |  |
| Step 2 | Create a Service Profile |  |
| Step 3 | Prepopulate Contact Lists in Bulk |  |
| Step 4 | Enable Message Settings |  |
| Step 5 | Enable File Transfers and Screen Captures |  |
| Step 6 | Prompts for Presence Subscription Requests |  |
| Step 7 | Temporary Presence |  |
| Step 8 | Add an IM and Presence Service |  |
| Step 9 | Apply an IM and Presence Service |  |
| Step 10 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 11 | Configure Users with IM and Presence Service |  |
| Step 12 | Enable Presence for Calendar Events |  |
| Step 13 | Configure Persistent Chat |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate and Start Essential Services |  |
| Step 2 | Prepopulate Contact Lists in Bulk |  |
| Step 3 | Enable Message Settings |  |
| Step 4 | Specify Capabilities Assignments |  |
| Step 5 | Prompts for Presence Subscription Requests |  |
| Step 6 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 7 | Temporary Presence |  |
| Step 8 | Enable Presence for Calendar Events |  |

| Step 1 | Open the Cisco
                                             				Unified IM and Presence Serviceability interface. |
|---|---|
| Step 2 | Select Tools > Control Center - Feature
                                                				  Services . |
| Step 3 | Select the
                                          			 appropriate server from the Server drop-down list. |
| Step 4 | Ensure the
                                          			 following services are started and activated: Cisco SIP Proxy Cisco Sync Agent Cisco XCP Authentication
                                                      					 Service Cisco XCP Connection
                                                      					 Manager Cisco XCP Text Conference
                                                      					 Manager Cisco Presence
                                                      					 Engine |
| Step 5 | Select Tools > Control Center - Network
                                                				  Services . |
| Step 6 | Select the
                                          			 appropriate server from the Server drop-down list. |
| Step 7 | Ensure Cisco
                                             				XCP Router Service is running. |

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                                				  Management > User Settings > Service
                                                				  Profile . The Find
                                                				  and List Service Profiles window opens. |
| Step 3 | Select Add
                                             				New . The Service Profile Configuration window opens. |
| Step 4 | Enter settings
                                          			 on the Service
                                             				Profile Configuration window as follows: Specify a
                                                				  unique name for the service profile in the Name field. Select Make
                                                   					 this the default service profile for the system , if appropriate. Note For phone mode, in the IM and Presence Profile section ensure
                                                         				  that the Primary field has <None> selected. | Note | For phone mode, in the IM and Presence Profile section ensure
                                                         				  that the Primary field has <None> selected. |
| Note | For phone mode, in the IM and Presence Profile section ensure
                                                         				  that the Primary field has <None> selected. |
| Step 5 | Select Save . |

| Note | For phone mode, in the IM and Presence Profile section ensure
                                                         				  that the Primary field has <None> selected. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Create a CSV
                                          			 file that defines the contact list you want to provide to users. |  |
| Step 2 | Use the BAT to
                                          			 import the contact list in bulk to a set of users. | For more
                                             				information about using BAT and the format of the CSV file, see the Deployment Guide for Cisco Unified Communications Manager IM
                                                				  & Presence for your release. |

| Step 1 | Open the Cisco
                                             				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Settings . |
| Step 3 | Select the
                                          			 following options: Enable instant
                                                         						messaging Allow clients to log
                                                         						instant message history Allow cut & paste in instant messages |
| Step 4 | Select other
                                          			 messaging settings as appropriate. |
| Step 5 | Select Save . Important Cisco
                                                            					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
                                                            					 Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is
                                                                     							 on the phone Use DND status when user is
                                                                     							 in a meeting | Important | Cisco
                                                            					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
                                                            					 Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is
                                                                     							 on the phone Use DND status when user is
                                                                     							 in a meeting |
| Important | Cisco
                                                            					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
                                                            					 Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is
                                                                     							 on the phone Use DND status when user is
                                                                     							 in a meeting |

| Important | Cisco
                                                            					 Jabber does not support the following settings on the Presence Settings window on Cisco Unified
                                                            					 Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is
                                                                     							 on the phone Use DND status when user is
                                                                     							 in a meeting |
|---|---|

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Licensing > Capabilities
                                                				  Assignment . The Find
                                                				  and List Capabilities Assignments window opens. |
| Step 3 | Specify the
                                          			 appropriate filters in the Find
                                             				Capabilities Assignment where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
                                          			 appropriate users from the list. The Capabilities Assignment Configuration window opens. |
| Step 5 | Select both of
                                          			 the following in the Capabilities Assignment Configuration section: Enable CUP Enable CUPC |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco
                                             				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select System > Service
                                                				  Parameters . |
| Step 3 | Select the
                                          			 appropriate server from the Server drop-down list. |
| Step 4 | Select Cisco
                                             				XCP Router from the Service drop-down list. The Service Parameter Configuration window opens. |
| Step 5 | Locate the Enable
                                             				file transfer parameter. |
| Step 6 | Select the
                                          			 appropriate value from the Parameter Value drop-down list. Remember If you
                                                            					 disable the setting on Cisco Unified Communications Manager IM and Presence
                                                            					 Service, you must also disable file transfers and screen captures in the client
                                                            					 configuration. | Remember | If you
                                                            					 disable the setting on Cisco Unified Communications Manager IM and Presence
                                                            					 Service, you must also disable file transfers and screen captures in the client
                                                            					 configuration. |
| Remember | If you
                                                            					 disable the setting on Cisco Unified Communications Manager IM and Presence
                                                            					 Service, you must also disable file transfers and screen captures in the client
                                                            					 configuration. |
| Step 7 | Select Save . |

| Remember | If you
                                                            					 disable the setting on Cisco Unified Communications Manager IM and Presence
                                                            					 Service, you must also disable file transfers and screen captures in the client
                                                            					 configuration. |
|---|---|

| Step 1 | Open the Cisco Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > File Transfer . |
| Step 3 | In the File Transfer Configuration section, select Peer-to-Peer . |
| Step 4 | Select Save . |

| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                         However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
|---|---|

| Step 1 | Open the Cisco
                                             				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings . The Presence Settings window opens. |
| Step 3 | Select Allow users to view the availability of other users without being prompted for approval to disable prompts and automatically accept all presence subscription requests within your organization. This option has the following values: Selected—The client does not prompt users for presence subscription requests. The client automatically accepts all presence
                                                      subscription requests without prompting the users. Cleared—The client prompts users to allow presence subscription requests. This setting requires users to allow other users
                                                      in your organization to view their availability status. |
| Step 4 | Select Save . |

| Step 1 | Open the Cisco
                                             				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings > Standard Configuration . |
| Step 3 | Uncheck Enable
                                             				ad-hoc presence subscriptions and then select Save . Cisco Jabber does not display temporary presence.
                                             				Users can see availability status only for contacts in their contact list. |

| Step 1 | Open the Cisco
                                             				Unified Presence Administration interface. |
|---|---|
| Step 2 | Select Presence > Settings . |
| Step 3 | Uncheck Enable
                                             				ad-hoc presence subscriptions and then select Save . Cisco Jabber does not display temporary presence.
                                             				Users can see availability status only for contacts in their contact list. |

| Step 1 | Open the Cisco
                                             				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                                				  Management > User Settings > UC
                                                				  Service . The Find
                                                				  and List UC Services window opens. |
| Step 3 | Select Add
                                             				New . The UC
                                                				  Service Configuration window opens. |
| Step 4 | In the Add a UC
                                             				Service section, select IM and
                                             				Presence from the UC
                                             				Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details
                                          			 for the IM and Presence Service as follows: Select Unified CM (IM and Presence) from the Product Type drop-down list. Specify a
                                                				  name for the service in the Name field. The name you
                                                   					 specify displays when you add the service to a profile. Ensure the name you
                                                   					 specify is unique, meaningful, and easy to identify. Specify an
                                                				  optional description in the Description field. Specify the
                                                				  instant messaging and presence service address in the Host
                                                   					 Name/IP Address field. Important The
                                                               						service address must be a fully qualified domain name or IP address. | Important | The
                                                               						service address must be a fully qualified domain name or IP address. |
| Important | The
                                                               						service address must be a fully qualified domain name or IP address. |
| Step 7 | Select Save . |

| Important | The
                                                               						service address must be a fully qualified domain name or IP address. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | In the IM and Presence Profile section, select up to three services from the following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Click Save . |
| Step 6 | Add users to the service profile. Select User Management > End User . The Find and List Users dialog box opens. Specify the appropriate filters in the Find User where field and then select Find to find a user. Click the user in the list. The End User Configuration window appears. Under the Service Settings area, check the Home Cluster check box. Check the Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) check box. Select your service profile from the UC Service Profile drop-down list. |
| Step 7 | Click Save . |

| Step 1 | If you have
                                          			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                          			 with the following information: For the SIP Address profile field, leave it blank. In the Work email profile field, enter the user profile.
                                                				  For example, john4mail@example.pst . |
|---|---|
| Step 2 | If you have
                                          			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                          			 with the following information: For the SIP Address profile field, enter the user profile.
                                                				  For example, john4mail@example.pst In the Work email profile field, leave it blank. |

| Step 1 | Open the Cisco
                                                				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                                   				  Management > End User . The Find
                                                   				  and List Users window opens. |
| Step 3 | Specify the
                                             			 appropriate filters in the Find
                                                				User where field and then select Find to retrieve a list of users. |
| Step 4 | Select the
                                             			 appropriate username from the list. The End
                                                   				  User Configuration window opens. |
| Step 5 | Locate the Service
                                                				Settings section and do the following: Select Home Cluster . Select Enable User for Unified CM IM and Presence . Select your
                                                   				  service profile from the UC
                                                      					 Service Profile drop-down list. Important Cisco Unified Communications Manager release 9.x only—If the user has
                                                                     						  only instant messaging and presence capabilities (IM only), select Use Default . 
                                                                     						  Cisco Unified Communications Manager release version 9.x applies the default
                                                                     						  service profile regardless of what you select from the UC Service Profile drop-down list. | Important | Cisco Unified Communications Manager release 9.x only—If the user has
                                                                     						  only instant messaging and presence capabilities (IM only), select Use Default . 
                                                                     						  Cisco Unified Communications Manager release version 9.x applies the default
                                                                     						  service profile regardless of what you select from the UC Service Profile drop-down list. |
| Important | Cisco Unified Communications Manager release 9.x only—If the user has
                                                                     						  only instant messaging and presence capabilities (IM only), select Use Default . 
                                                                     						  Cisco Unified Communications Manager release version 9.x applies the default
                                                                     						  service profile regardless of what you select from the UC Service Profile drop-down list. |
| Step 6 | Select Save . |

| Important | Cisco Unified Communications Manager release 9.x only—If the user has
                                                                     						  only instant messaging and presence capabilities (IM only), select Use Default . 
                                                                     						  Cisco Unified Communications Manager release version 9.x applies the default
                                                                     						  service profile regardless of what you select from the UC Service Profile drop-down list. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Bulk Administration > Users > Update Users > Query . The Find and List Users To Update window opens. |
| Step 3 | Specify the appropriate filters in the Find User where field and then select Find to retrieve a list of users. |
| Step 4 | Select Next . The Update Users Configuration window opens. |
| Step 5 | Select both of the Enable User for Unified CM IM and Presence check boxes. Important There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select
                                                               both check boxes. | Important | There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select
                                                               both check boxes. |
| Important | There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select
                                                               both check boxes. |
| Step 6 | Select the UC Service Profile check box and then select your service profile from the drop-down list. Important Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities
                                                               (IM only), you must select Use Default . For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless
                                                               of what you select from the UC Service Profile drop-down list. | Important | Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities
                                                               (IM only), you must select Use Default . For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless
                                                               of what you select from the UC Service Profile drop-down list. |
| Important | Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities
                                                               (IM only), you must select Use Default . For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless
                                                               of what you select from the UC Service Profile drop-down list. |
| Step 7 | In the Job Information section, specify if you want to run the job immediately or at a later time. |
| Step 8 | Select Submit . |

| Important | There are two check boxes for Enable User for Unified CM IM and Presence . To disable instant messaging and presence, you select one check box. To enable instant messaging and presence, you select
                                                               both check boxes. |
|---|---|

| Important | Cisco Unified Communications Manager release 9.x only —  If the user has only instant messaging and presence capabilities
                                                               (IM only), you must select Use Default . For IM only users — Cisco Unified Communications Manager release 9.x always applies the default service profile regardless
                                                               of what you select from the UC Service Profile drop-down list. |
|---|---|

| Important | This feature is not available for the Cisco Jabber mobile
                                                      					 clients. This preference is disabled
                                                   				  by default. As of this release, users
                                                   				  must enable the preference individually after deployment. You cannot enable
                                                   				  this preference for multiple users with a bulk task. |
|---|---|

| Step 1 | Log in to the Cisco
                                             				Unified CM IM and Presence User Options page. The user
                                             				options page is located at: https:// server_name : port_number /cupuser/showHome.do |
|---|---|
| Step 2 | Select User
                                                				  Options > Preferences . The Preferences page opens. |
| Step 3 | Navigate to
                                          			 the Calendar Settings section of the Preferences page. |
| Step 4 | Select On from the drop-down menu for the Include Calendar information in my Presence Status field. |
| Step 5 | Select Save . |
| Step 6 | Log out and
                                          			 close the Cisco
                                             				Unified CM IM and Presence User Options page. |

| Step 1 | Open the Cisco
                                             				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Group Chat and Persistent
                                                				  Chat . |
| Step 3 | Select Enable
                                             				Persistent Chat . |
| Step 4 | Ensure the
                                          			 settings How
                                             				many users can be in a room at one time and How
                                             				many hidden users can be in a room at one time under the Occupancy Settings section contain the same,
                                          			 non-zero value. |
| Step 5 | Configure the remaining settings as appropriate for your persistent chat deployment. We recommend the persistent chat settings
                                          in the following table. Persistent Chat Setting Recommended Value Notes System automatically manages primary group chat server aliases Disabled Enable persistent chat Enabled Archive all room joins and exits Administrator Defined This value is not currently used by for persistent chat. Archive all room messages Enabled Allow only group chat system administrators to create persistent chat rooms Administrator Defined Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. Maximum number of persistent chat rooms allowed Administrator Defined Number of connections to the database Default Value Database connection heartbeat interval (seconds) Default Value Timeout value for persistent chat rooms (minutes) Default Value Maximum number of rooms allowed Default Value Rooms are for members only by default Disabled Room owners can change whether or not rooms are for members only Enabled Cisco Jabber requires this value to be Enabled. Only moderators can invite people to members-only rooms Enabled Cisco Jabber requires this value to be Enabled. Room owners can change whether or not only moderators can invite people to members-only rooms Enabled Users can add themselves to rooms as members Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether users can add themselves to rooms as members Disabled This value is not currently used by Cisco Jabber for persistent chat. Members and administrators who are not in a room are still visible in the room Enabled Cisco Jabber requires this value to be Enabled. Room owners can change whether members and administrators who are not in a room are still visible in the room Enabled Rooms are backwards-compatible with older clients Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether rooms are backwards-compatible with older clients Disabled This value is not currently used by Cisco Jabber for persistent chat. Rooms are anonymous by default Disabled This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. Room owners can change whether or not rooms are anonymous Disabled This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. Lowest participation level a user can have to invite others to the room Default Value This value is not currently used by Cisco Jabber for persistent chat. Room owners can change the lowest participation level a user can have to invite others to the room Disabled This value is not currently used by Cisco Jabber for persistent chat. How many users can be in a room at one time Administrator Defined Cisco recommends using the default value. How many hidden users can be in a room at one time Administrator Defined Default maximum occupancy for a room Default Value Room owners can change default maximum occupancy for a room Default Value Lowest participation level a user can have to send a private message from within the room Default Value Room owners can change the lowest participation level a user can have to send a private message from within the room Default Value Lowest participation level a user can have to change a room's subject Moderator Room owners can change the lowest participation level a user can have to change a room's subject Disabled Remove all XHTML formatting from messages Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change XHTML formatting setting Disabled This value is not currently used by Cisco Jabber for persistent chat. Rooms are moderated by default Disabled This value is not currently used by Cisco Jabber for persistent chat. Room owners can change whether rooms are moderated by default Default Value This value is not currently used by Cisco Jabber for persistent chat. Maximum number of messages that can be retrieved from the archive Default Value Number of messages in chat history displayed by default Administrator Defined Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue
                                                         to use their originally configured value. Room owners can change the number of messages displayed in chat history Default Value This value is not currently used by Cisco Jabber for persistent chat. Note Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to
                                                      rooms created after the change has taken effect. | Persistent Chat Setting | Recommended Value | Notes | System automatically manages primary group chat server aliases | Disabled |  | Enable persistent chat | Enabled |  | Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. | Archive all room messages | Enabled |  | Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. | Maximum number of persistent chat rooms allowed | Administrator Defined |  | Number of connections to the database | Default Value |  | Database connection heartbeat interval (seconds) | Default Value |  | Timeout value for persistent chat rooms (minutes) | Default Value |  | Maximum number of rooms allowed | Default Value |  | Rooms are for members only by default | Disabled |  | Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. | Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. | Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  | Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. | Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  | Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. | Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. | Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. | How many hidden users can be in a room at one time | Administrator Defined |  | Default maximum occupancy for a room | Default Value |  | Room owners can change default maximum occupancy for a room | Default Value |  | Lowest participation level a user can have to send a private message from within the room | Default Value |  | Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  | Lowest participation level a user can have to change a room's subject | Moderator |  | Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  | Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. | Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Maximum number of messages that can be retrieved from the archive | Default Value |  | Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue
                                                         to use their originally configured value. | Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. | Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to
                                                      rooms created after the change has taken effect. |
| Persistent Chat Setting | Recommended Value | Notes |
| System automatically manages primary group chat server aliases | Disabled |  |
| Enable persistent chat | Enabled |  |
| Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. |
| Archive all room messages | Enabled |  |
| Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. |
| Maximum number of persistent chat rooms allowed | Administrator Defined |  |
| Number of connections to the database | Default Value |  |
| Database connection heartbeat interval (seconds) | Default Value |  |
| Timeout value for persistent chat rooms (minutes) | Default Value |  |
| Maximum number of rooms allowed | Default Value |  |
| Rooms are for members only by default | Disabled |  |
| Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. |
| Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  |
| Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  |
| Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. |
| How many hidden users can be in a room at one time | Administrator Defined |  |
| Default maximum occupancy for a room | Default Value |  |
| Room owners can change default maximum occupancy for a room | Default Value |  |
| Lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Lowest participation level a user can have to change a room's subject | Moderator |  |
| Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  |
| Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Maximum number of messages that can be retrieved from the archive | Default Value |  |
| Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue
                                                         to use their originally configured value. |
| Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to
                                                      rooms created after the change has taken effect. |

| Persistent Chat Setting | Recommended Value | Notes |
|---|---|---|
| System automatically manages primary group chat server aliases | Disabled |  |
| Enable persistent chat | Enabled |  |
| Archive all room joins and exits | Administrator Defined | This value is not currently used by for persistent chat. |
| Archive all room messages | Enabled |  |
| Allow only group chat system administrators to create persistent chat rooms | Administrator Defined | Cisco recommends using the value Enabled unless Cisco Unified Personal Communicator is deployed in the enterprise environment. |
| Maximum number of persistent chat rooms allowed | Administrator Defined |  |
| Number of connections to the database | Default Value |  |
| Database connection heartbeat interval (seconds) | Default Value |  |
| Timeout value for persistent chat rooms (minutes) | Default Value |  |
| Maximum number of rooms allowed | Default Value |  |
| Rooms are for members only by default | Disabled |  |
| Room owners can change whether or not rooms are for members only | Enabled | Cisco Jabber requires this value to be Enabled. |
| Only moderators can invite people to members-only rooms | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether or not only moderators can invite people to members-only rooms | Enabled |  |
| Users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether users can add themselves to rooms as members | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Members and administrators who are not in a room are still visible in the room | Enabled | Cisco Jabber requires this value to be Enabled. |
| Room owners can change whether members and administrators who are not in a room are still visible in the room | Enabled |  |
| Rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are backwards-compatible with older clients | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are anonymous by default | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Room owners can change whether or not rooms are anonymous | Disabled | This value is not currently supported by Cisco Jabber for persistent chat. Cisco Jabber cannot join anonymous rooms. |
| Lowest participation level a user can have to invite others to the room | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change the lowest participation level a user can have to invite others to the room | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| How many users can be in a room at one time | Administrator Defined | Cisco recommends using the default value. |
| How many hidden users can be in a room at one time | Administrator Defined |  |
| Default maximum occupancy for a room | Default Value |  |
| Room owners can change default maximum occupancy for a room | Default Value |  |
| Lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Room owners can change the lowest participation level a user can have to send a private message from within the room | Default Value |  |
| Lowest participation level a user can have to change a room's subject | Moderator |  |
| Room owners can change the lowest participation level a user can have to change a room's subject | Disabled |  |
| Remove all XHTML formatting from messages | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change XHTML formatting setting | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Rooms are moderated by default | Disabled | This value is not currently used by Cisco Jabber for persistent chat. |
| Room owners can change whether rooms are moderated by default | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |
| Maximum number of messages that can be retrieved from the archive | Default Value |  |
| Number of messages in chat history displayed by default | Administrator Defined | Cisco recommends a value between 15 and 50. The Number of messages in chat history displayed by default setting does not apply retroactively to persistent chat rooms. Rooms created before the setting is changed will continue
                                                         to use their originally configured value. |
| Room owners can change the number of messages displayed in chat history | Default Value | This value is not currently used by Cisco Jabber for persistent chat. |

| Note | Persistent Chat rooms inherit their settings at the time of creation. Values changed after a room is created only apply to
                                                      rooms created after the change has taken effect. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM and Presence Service |  |
| Step 2 | Configure Presence in Microsoft SharePoint 2010 and 2013 |  |
| Step 3 | Configure Privacy Options |  |

| Step 1 | If you have
                                          			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                          			 with the following information: For the SIP Address profile field, leave it blank. In the Work email profile field, enter the user profile.
                                                				  For example, john4mail@example.pst . |
|---|---|
| Step 2 | If you have
                                          			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                          			 with the following information: For the SIP Address profile field, enter the user profile.
                                                				  For example, john4mail@example.pst In the Work email profile field, leave it blank. |

| Step 1 | Open the Cisco WebEx Administration Tool. |
|---|---|
| Step 2 | Select the Configuration tab. |
| Step 3 | Select General IM in the Connect Client section. The General IM pane opens. |
| Step 4 | Select the appropriate options for contact list requests as follows: Option Description Select Allow users to set "Options for contact list requests" Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change
                                                      the default option in the Options window. Do not select Allow users to set "Options for contact list requests" You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings
                                                      are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request The options for configuring how the client handles contact list requests are as follows: Accept requests automatically from all contacts — The client automatically accepts presence subscription requests from any
                                             domain. If you specify this setting, users from any domain can automatically add users to their contact list and view their
                                             availability status. Accept requests automatically from contacts in my organization — The client automatically accepts presence subscription requests
                                             only from users in the domains you specify. To specify a domain, select Domain(s) in the System Settings section on the Configuration tab. Note When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                            However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. Prompt me for each request — The client prompts users to accept each presence subscription request. | Option | Description | Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change
                                                      the default option in the Options window. | Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings
                                                      are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request | Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                            However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
| Option | Description |
| Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change
                                                      the default option in the Options window. |
| Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings
                                                      are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request |
| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                            However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
| Step 5 | Select Save . |

| Option | Description |
|---|---|
| Select Allow users to set "Options for contact list requests" | Accept requests automatically from contacts in my organization automatically becomes the default option to configure how the client handles presence subscription requests. Users can change
                                                      the default option in the Options window. |
| Do not select Allow users to set "Options for contact list requests" | You configure how the client handles presence subscription requests. Users cannot change this configuration. The settings
                                                      are not available in the Options window. Select one of the following options: Accept requests automatically from all contacts Accept requests automatically from contacts in my organization Prompt me for each request |

| Note | When searching for contacts in your organization, users can see the temporary availability status of all users in the organization.
                                                            However, if User A blocks User B, User B cannot see the temporary availability status of User A in the search list. |
|---|---|