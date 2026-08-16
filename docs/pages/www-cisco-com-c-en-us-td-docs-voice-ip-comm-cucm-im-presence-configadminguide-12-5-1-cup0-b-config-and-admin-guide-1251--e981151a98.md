---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-cup0-b-config-and-admin-guide-1251--e981151a98
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1/cup0_b_config-and-admin-guide-1251/cup0_b_config-and-admin-guide-1251_chapter_010110.html
retrieved_at: 2026-08-16T16:43:35.489737+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)

Updated: November 27, 2024

Chapter: Manage Chat

## Chapter: Manage Chat

# Manage Chat

## Manage Chat Overview

IM and Presence Service provides you with settings you can use to manage your chat rooms and to control who has access to
                           them. This includes the ability to:

Create new rooms, manage members and the configurations of the rooms they create.

Control access to persistent chat rooms so that only members of that room have access.

Assign Administrators to a chat room.

Invite other users to a room.

Determine the presence status of the members displayed within the room. The presence status displayed in a room confirms the
                                 attendance of the member in a room but may not reflect their overall presence status.

IM and Presence Service also lets you manage chat node aliases. Chat node aliases make it possible for your users to search
                           for specific chat rooms on specific nodes, and to join those chat rooms.

In addition,  the IM and Presence Service also stores transcripts and makes this chat room history available to room members,
                           including members who have just joined the chat room. You can configure how much of the existing archive you want to make
                           available to new and old members.  .

### Chat Node Alias Overview

Each chat node in a system must have a unique alias. Chat node aliases are unique addresses for each chat node so that users
                                 (in any domain) can search for specific chat rooms on specific nodes, and join chat in those rooms. Chat node aliases form
                                 a part of the unique ID for each chat room that is created on that node. For example, the alias conference-3-mycup.cisco.com gets used to name the chat room roomjid@conference-3-mycup.cisco.com that is created on that node.

There are two modes for assigning chat node aliases:

System-generated—The system automatically assigns a unique alias to each chat node. By default, the system auto-generates
                                       one alias per chat node by using the following naming convention: conference-x-clusterid.domain , where:

conference is a hardcoded keyword

x is the unique integer value that denotes the node ID

clusterid is the configured enterprise parameter

domain is the configured domain

For example, the system might assign: conference-3-mycup.cisco.com

Manual—You must disable system-generated aliases to be able to assign chat node aliases manually. With manually-assigned aliases,
                                       you have complete flexibility to name chat nodes using aliases that suit your specific requirements. For example, you might
                                       do this if the congerence-x-clusterid.domain naming convention does not suit your deployment needs.

#### Assigning Multiple Aliases per Node

You can associate more than one alias with each chat node on a per-node basis. Multiple aliases per node allows users to create
                                 additional chat rooms using these aliases. This functionality applies to both system-generated aliases and aliases that are
                                 created manually.

## Manage Chat Prerequisites

Ensure that you have persistent chat enabled.

## Manage Chat Task Flow

Step 1

Enable Chat Room Owners to Edit Chat Room Settings

Configure whether you want to allow chat room owners to be able to edit chat room settings. Otherwise, only administrators
                                          will be able to edit chat room settings.

Step 2

Allow Clients to Log Instant Message History

Configure whether you want to allow users to log instant message history locally on their computer.

Step 3

View External Database Text Conferencing Report

Use this procedure to view the External Database Text Conferencing Report that lets you view details on the persistent chat
                                          rooms.

Step 4

Edit chat room settings. Complete any of the following tasks, in any order, to update chat room settings:

If you update any of the Persistent Chat settings, on Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services to restart the Cisco XCP Text Conference Manager service.

Step 5

Reset Chat Rooms to System Defaults

Complete this optional task if you want to reset your chat configuration to the system defaults. Be aware that ad hoc chat
                                          is enabled by default, but persistent chat is disabled by default. Completing this task would disable persistent chat.

Step 6

Manage Chat Node Aliases

Aliases create a unique address for each chat node so that users (in any domain) can search for specific chat rooms on specific
                                          nodes, and join chat in those rooms. Each chat node in a system must have a unique alias.

Step 7

Clean External Database for Persistent Chat

Optional. Use the External Database Cleanup Utility to configure jobs that monitor the external database and delete expired
                                          records. This will ensure that there is always enough disk space for new records.

### Enable Chat Room Owners to Edit Chat Room Settings

Use this procedure if you want to allow chat room owners to be able to edit chat room settings.

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat .

Step 2

Configure a value for  the Room owners can change whether or not rooms are for members only check box.

- Checked—Chat room owners have administrative ability to  edit chat room settings.

- Unchecked—Only an administrator can edit chat room settings.

Step 3

Click Save .

Step 4

In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services .

Step 5

Restart the Cisco XCP Text Conference Manager service.

### Allow Clients to Log Instant Message History

You can prevent or allow users to log instant message history locally on their computer. On the client side, the application
                                 must support this functionality; it must enforce the prevention of instant message logging

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings .

Step 2

Configure the log instant message history setting as follows:

- To allow users of client applications to log instant message history on IM and Presence Service, check Allow clients to log instant message history (on supported clients only) .

- To prevent users of client applications from logging instant message history on IM and Presence Service, uncheck Allow clients to log instant message history (on supported clients only) .

Step 3

Click Save .

### View External Database Text Conferencing Report

Use this procedure to view the External Database Text Conferencing Report. This report lets you view details of the persistent
                                 and ad-hoc chat rooms in your deployment.

Step 1

Log into Cisco Unified CM IM and Presence Administration .

Step 2

Choose Messaging > Group Chat and Persistent Chat .

Step 3

Under Persistent Chat Database Assignment , click the Room Report button.

Step 4

Use the filter tools if you want to limit the selection to rooms that meet specific criteria.

Step 5

Click Find .

Step 6

Select a specific chat room to view details for that room.

The number of records fetched from the database depends on the value selected from "Records Fetched" drop-down list.

### Configure Chat Room Settings

#### Set Number of Chat Rooms

Use room settings to limit the number of rooms that users can create. Limiting the number of chat rooms helps the performance
                                    of the system and allows it to scale. Limiting the number of rooms also helps to mitigate any possible service-level attacks.

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat .

Step 2

To change the maximum number of chat rooms that are allowed, enter a value in the field for Maximum number of rooms allowed . The default is set to 5500.

Step 3

Click Save .

#### Configure Chat Room Member Settings

Member settings allow control over the membership in chat rooms. Such a control is useful for users to mitigate service-level
                                    attacks that can be prevented by restricting membership. Configure the member settings as required.

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat .

Step 2

Configure the room member settings as described in Room Member Settings.

Step 3

Click Save .

Step 4

In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services .

Step 5

Restart the Cisco XCP Text Conference Manager service.

##### Room Member Settings

Persistent chat rooms inherit their settings when you create the room. Later changes do not apply to existing rooms. Those
                                                   changes only apply to rooms created after the changes take effect.

Field

Description

Rooms are for members only by default

Check this check box if you want rooms to be created as members-only rooms by default. Members-only rooms are accessible only
                                                   by users on an allowed list configured by the room owner or administrator. The check box is unchecked by default.

The allowed list contains the list of members who are allowed in the room. It is created by the owner or administrator of
                                                               the members-only room.

Only moderators can invite people to members-only rooms

Check this check box if you want to configure the room so that only moderators are allowed to invite users to the room. If
                                                   this check box is unchecked, members can invite other users to join the room. The check box is checked by default.

Room owners can change whether or not rooms are for members only

Check this check box  if you want to configure the room so that room owners are allowed to change whether or not rooms are
                                                   for members only. The check box is checked by default.

A room owner is the user who creates the room or a user who has been designated by the room creator or owner as someone with
                                                               owner status (if allowed). A room owner is allowed to change the room configuration and destroy the room, in addition to all
                                                               other administrator abilities.

Room owners can change whether or not only moderators can invite people to members-only rooms

Check this check box if you want to configure the room so that room owners can allow members to invite other users to the
                                                   room. The check box is checked by default.

Users can add themselves to rooms as members

Check this check box if you want to configure the room so that any user can request to join the room at any time. If this
                                                   check box is checked, the room has an open membership. The check box is unchecked by default.

Room owners can change whether users can add themselves to rooms as members

Check this check box if you want to configure the room so that room owners have the ability to change the setting that is
                                                   listed in Step 5 at any time. The check box is unchecked by default.

#### Configure Availability Settings

Availability settings determine the visibility of a user within a room.

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat .

Step 2

Configure the availability member settings as described in Availability Settings.

Step 3

Click Save .

Step 4

In Cisco Unified IM and Presence Serviceablity , choose Tools > Control Center - Feature Services .

Step 5

Restart the Cisco XCP Text Conference Manager service.

##### Availability Settings

Field

Description

Members and administrators who are not in a room are still visible in the room

Check this check box if you want to keep users on the room roster even if they are currently offline. The check box is checked
                                                   by default.

If the administrator leaves the chat room, the administrator's userid will still be visible in the chat room. The user needs
                                                               to close and reopen the chat room to refresh the user's list.

Room owners can change whether members and administrators who are not in a room are still visible in the room

Check this check box if you want to allow room owners the ability to change the visibility of a member or administrator. The
                                                   check box is checked by default.

Rooms are backwards-compatible with older clients

Check this check box if you want the service to function well with older Group Chat 1.0 clients. The check box is unchecked
                                                   by default.

Room owners can change whether rooms are backwards-compatible with older clients

Check this check box if you want to allow room owners the ability to control backward compatibility of the chat rooms. The
                                                   check box is unchecked by default.

Rooms are anonymous by default

Check this check box if you want the room to display the user nickname but keep the Jabber ID private. The check box is unchecked
                                                   by default.

Room owners can change whether or not rooms are anonymous

Check this check box if you want to allow room owners to control the anonymity level of the user Jabber ID. The check box
                                                   is unchecked by default.

#### Configure Occupancy Settings

Occupancy settings determine how many users can be in a chat room at a given time.

Step 1

To change the system maximum number of users that are allowed in a room, enter a value in the field for How many users can be in a room at one time . The default value is set to 1000.

The total number of users in a room should not exceed the value that you set. The total number of users in a room includes
                                                            both normal users and hidden users.

Step 2

To change the number of hidden users that are allowed in a room, enter a value in the field for How many hidden users can be in a room at one time . Hidden users are not visible to others, cannot send a message to the room, and do not send presence updates. Hidden users
                                             can see all messages in the room and receive presence updates from others. The default value is 1000.

Step 3

To change the default maximum number of users that are allowed in a room, enter a value in the field for Default maximum occupancy for a room . The default value is set to 50 and cannot be any higher than the value that is set in Step 1.

Step 4

Check Room owners can change default maximum occupancy for a room if you want to allow room owners to change the default maximum room occupancy. The check box is checked by default.

Step 5

Click Save .

#### Configure Chat Message Settings

Use Chat Message settings to give privileges to users based on their role. For the most part, roles exist in a visitor-to-moderator
                                    hierarchy. For example, a participant can do anything a visitor can do, and a moderator can do anything a participant can
                                    do.

The check box is checked by default.

Step 1

From the drop-down list for Lowest participation level a user can have to send a private message from within the room , choose one:

- Visitor allows visitors, participants, and moderators to send a private message to other users in the room.This is the default setting.

- Participant allows participants and moderators to send a private message to other users in the room.

- Moderator allows only moderators to send a private message to other users in the room.

Step 2

Check Room owners can change the lowest participation level a user can have to send a private message from within the room if you want to allow room owners to change the minimum participation level for private messages. The check box is checked
                                             by default.

Step 3

From the drop-down list for Lowest participation level a user can have to change a room's subject, choose one:

Participant allows participants and moderators to change the room's subject. This is the default setting.

Moderator allows only moderators to change the room's subject.

Visitors are not permitted to change the room subject.

Step 4

Check Room owners can change the lowest participation level a user can have to change a room's subject if you want to allow room owners to change the minimum participation level for updating a room's subject.

Step 5

Check Remove all XHTML formatting from messages if you want to remove all Extensible Hypertext Markup Language (XHTML) from messages. The check box is unchecked by default.

Step 6

Check Room owners can change XHTML formatting setting if you want to allow room owners to change the XHTML formatting setting. The check box is unchecked by default.

Step 7

Click Save .

#### Configure Moderated Room Settings

Moderated rooms provide the ability for moderators to grant and revoke the voice privilege within a room (in the context of
                                    Group Chat, voice refers to the ability to send chat messages to the room). Visitors cannot send instant messages in moderated
                                    rooms.

Step 1

Check Rooms are moderated by default if you want to enforce the role of moderator in a room. The check box is unchecked by default.

Step 2

Check Room owners can change whether rooms are moderated by default if you want to allow room owners the ability to change whether rooms are moderated. The check box is checked by default.

Step 3

Click Save .

#### Configure History Settings

Use History settings to set the default and maximum values of messages that are retrieved and displayed in the rooms, and
                                    to control the number of messages that can be retrieved through a history query. When a user joins a room, the user is sent
                                    the message history of the room. History settings determine the number of previous messages that the user receives.

Step 1

To change the maximum number of messages that users can retrieve from the archive, enter a value in the field for Maximum number of messages that can be retrieved from the archive . The default value is set to 100. It serves as a limit for the next setting.

Step 2

To change the number of previous messages displayed when a user joins a chat room, enter a value in the field for Number of messages in chat history displayed by default . The default value is set to 15 and cannot be any higher than the value that is set in Step 1.

Step 3

Check Room owners can change the number of messages displayed in chat history if you want to allow room owners to change the number of previous messages displayed when a user joins a chat room. The check
                                             box is unchecked by default.

Step 4

Click Save .

### Reset Chat Rooms to System Defaults

Use this procedure if you want to reset your group chat settings for both ad hoc and persistent chat rooms to the system defaults..

Ad hoc chat is enabled by default, but persistent chat is disabled by default. Completing this task will disable persistent
                                             chat

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings .

Step 2

Click Set to Default .

Step 3

Click Save .

### Chat Node Alias Management

#### Manage Chat Node Aliases

Complete these tasks to manage chat node aliases for your cluster. You can have the system manage aliases automatically, or
                                    you can update them yourself.

Step 1

Assign Mode for Managing Chat Aliases

Assign whether you want the system to manage chat node aliases or whether you want to do it manually.

Step 2

Add Chat Node Alias Manually

Add, edit, or delete chat node aliases for your cluster.

#### Assign Mode for Managing Chat Aliases

Configure whether you want the system to assign chat node aliases automatically using the conference-x-clusterid.domain naming convention, or whether you want to assign them manually.

##### Before you begin

For information on chat node aliases, see Chat Node Alias Overview .

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat .

Step 2

Enable or disable system-generated aliases:

If you want the system to assign chat node aliases automatically, check System Automatically Manages Primary Group Chat Server Aliases .

Tip

Choose Messaging > Group Chat Server Alias Mapping to verify that the system-generated alias is listed under Primary Group Chat Server Aliases.

If you want to assign chat node aliases manually, uncheck System Automatically Manages Primary Group Chat Server Aliases .

##### What to do next

Even if you configure a system-generated alias for a chat node, you can associate more than one alias with the node if required.

If you are federating with external domains, you may want to inform federated parties that the aliases have changed and new
                                          aliases are available. To advertise all aliases externally, configure DNS and publish the aliases as DNS records.

If you update any of the system-generated alias configuration, perform one of these actions:
                                          Restart the Cisco XCP Text Conference Manager.

To add, edit, or delete a chat node alias, Add Chat Node Alias Manually .

#### Add Chat Node Alias Manually

Use this procedure to manually add, edit, or delete chat node aliases. To manually manage chat node aliases, you must turn
                                    off the default setting, which uses system-generated aliases. If you turn off a system-generated alias, the existing alias
                                    ( conference-x-clusterid.domain ) reverts to a standard, editable alias listed under Conference Server Aliases. This maintains the old alias and the chat
                                    room addresses that are associated with that alias.

You can manually assign multiple aliases to chat nodes. Even if a system-generated alias already exists for a chat node, you
                                    can associate additional aliases to the node manually.

For manually-managed aliases, it is the responsibility of the administrator to manually update the alias list if the Cluster
                                    ID or domain changes. System-generated aliases will incorporate the changed values automatically.

Although it is not mandatory, we recommend that you always include the domain when you assign a new chat node alias to a node.
                                                Use this convention for additional aliases, newalias.domain. Choose Cisco Unified CM IM and Presence Administration > Presence Settings > Advanced Settings to see the domain.

##### Before you begin

Step 1

In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat Server Alias Mapping .

Step 2

Click Find .

The Group Chat Server Alias window displays the existing node aliases.

Step 3

To add a new alias:

Click Add New .

In the Group Chat Server Alias field, enter a new alias.

From the Server Name drop-down list box, select the server to which you want to assign the alias.

Click Save .

Step 4

To edit an existing alias:

Select the alias.

Enter your updates and click Save .

Step 5

To delete an alias, select the alias and click Delete Selected .

##### What to do next

Turn on the Cisco XCP Text Conference Manager.

##### Chat Node Alias Troubleshooting Tips

Every chat node alias must be unique. The system will prevent you from creating duplicate chat node aliases across the cluster.

A chat node alias name cannot match the IM and Presence domain name.

Delete old aliases only if you no longer need to maintain the address of chat rooms via the old alias.

If you are federating with external domains, you may want to inform federated parties that the aliases have changed and new
                                             aliases are available. To advertise all aliases externally, configure DNS and publish the aliases as DNS records.

If you update any of the chat node alias configuration, restart the Cisco XCP Text Conference Manager.

### Clean External Database for Persistent Chat

Configure jobs that monitor the external database and delete
                                 expired records. This will ensure that there is always enough disk
                                 space for new records.

To clean database tables for Persistent Chat, make
                                 sure to select the Text Conference (TC) feature under Feature
                                    Tables .

Step 1

Log into Cisco Unified CM IM and Presence Administration on the database publisher node.

Step 2

Choose Messaging > External Server Setup > External Database Jobs .

Step 3

Click Clear External DB .

Step 4

Do one of the following:

- For manual cleanup of an external database that connects to the publisher node, select Same Cup Node .

- For manual cleanup of an external database that connects to a subscriber node, select Other Cup Node and then select the external database details.

- If you are configuring the system to monitor and clean the external database automatically, check the Automatic Clean-up radio button.

We recommend that you run a manual cleanup prior to setting up the automatic cleanup.

Step 5

Set the Number of Days that you want to go back for file deletion. For example, if you enter 90, the system deletes records that are older than
                                          90 days.

Step 6

Click Update Schema to create the Indexes and stored procedures for the database.

Step 7

Set the Number of Days that you want to go back for file deletion. For example, if you enter 90 , the system deletes records that are older than 90 days.

Step 8

In the Feature Tables section, select each feature for which you want to clean records:

- Text Conference (TC) —Select this option to clean database tables for the Persistent Chat feature.

- Message Archiver (MA) —Select this option to clean database tables for the Message Archiver feature.

- Managed File Transfer (MFT) —Select this option to clean database tables for the Managed File Transfer feature

Step 9

Click Submit Clean-up Job .

If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button.

## Manage Chat Interactions

Changing chat node aliases can make the chat rooms in the database unaddressable and prevent your users from finding existing
                              chat rooms.

Note these results before you change the constituent parts of aliases or other node dependencies:

Cluster ID - This value is part of the fully qualified cluster name (FQDN). Changing the Cluster ID (choose System > Presence
                                    Topology: Settings) causes the FQDN to incorporate the new value and the system-managed alias to automatically change across
                                    the cluster. For manually-managed aliases, it is the responsibility of the Administrator to manually update the alias list
                                    if the Cluster ID changes.

Domain - This value is part of the FQDN. Changing the Domain (choose Presence > Presence Settings) causes the FQDN to incorporate
                                    the new value and the system-managed alias to automatically change across the cluster. For manually-managed aliases, it is
                                    the responsibility of the Administrator to manually update the alias list if the Domain changes.

Connection between the chat node and external database - The chat node will not start if persistent chat is enabled and you
                                    do not maintain the correct connection with the external database.

Deletion of a chat node — If you delete a node associated with an existing alias from the Presence Topology, chat rooms created
                                    using the old alias may not be addressable unless you take further action.

We recommend that you do not change existing aliases without considering the wider implications of your changes, namely:

Make sure that you maintain the address of old chat nodes in the database so that users can locate existing chat rooms via
                                    the old alias, if required.

If there is federation with external domains, you may need to publish the aliases in DNS to inform theusers in those domains
                                    that the aliases have changed and new addresses are available. This depends on whether or not you want to advertise all aliases
                                    externally.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Chat Room Owners to Edit Chat Room Settings | Configure whether you want to allow chat room owners to be able to edit chat room settings. Otherwise, only administrators
                                          will be able to edit chat room settings. |
| Step 2 | Allow Clients to Log Instant Message History | Configure whether you want to allow users to log instant message history locally on their computer. |
| Step 3 | View External Database Text Conferencing Report | Use this procedure to view the External Database Text Conferencing Report that lets you view details on the persistent chat
                                          rooms. |
| Step 4 | Edit chat room settings. Complete any of the following tasks, in any order, to update chat room settings: | Note If you update any of the Persistent Chat settings, on Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services to restart the Cisco XCP Text Conference Manager service. | Note | If you update any of the Persistent Chat settings, on Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services to restart the Cisco XCP Text Conference Manager service. |
| Note | If you update any of the Persistent Chat settings, on Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services to restart the Cisco XCP Text Conference Manager service. |
| Step 5 | Reset Chat Rooms to System Defaults | Complete this optional task if you want to reset your chat configuration to the system defaults. Be aware that ad hoc chat
                                          is enabled by default, but persistent chat is disabled by default. Completing this task would disable persistent chat. |
| Step 6 | Manage Chat Node Aliases | Aliases create a unique address for each chat node so that users (in any domain) can search for specific chat rooms on specific
                                          nodes, and join chat in those rooms. Each chat node in a system must have a unique alias. |
| Step 7 | Clean External Database for Persistent Chat | Optional. Use the External Database Cleanup Utility to configure jobs that monitor the external database and delete expired
                                          records. This will ensure that there is always enough disk space for new records. |

| Note | If you update any of the Persistent Chat settings, on Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services to restart the Cisco XCP Text Conference Manager service. |
|---|---|

| Note | The availability of configuring these settings from the client also depends on the client implementation and whether the client
                                          is providing an interface in which to configure these settings. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat . |
|---|---|
| Step 2 | Configure a value for  the Room owners can change whether or not rooms are for members only check box. Checked—Chat room owners have administrative ability to  edit chat room settings. Unchecked—Only an administrator can edit chat room settings. |
| Step 3 | Click Save . |
| Step 4 | In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services . |
| Step 5 | Restart the Cisco XCP Text Conference Manager service. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings . |
|---|---|
| Step 2 | Configure the log instant message history setting as follows: To allow users of client applications to log instant message history on IM and Presence Service, check Allow clients to log instant message history (on supported clients only) . To prevent users of client applications from logging instant message history on IM and Presence Service, uncheck Allow clients to log instant message history (on supported clients only) . |
| Step 3 | Click Save . |

| Step 1 | Log into Cisco Unified CM IM and Presence Administration . |
|---|---|
| Step 2 | Choose Messaging > Group Chat and Persistent Chat . |
| Step 3 | Under Persistent Chat Database Assignment , click the Room Report button. |
| Step 4 | Use the filter tools if you want to limit the selection to rooms that meet specific criteria. |
| Step 5 | Click Find . |
| Step 6 | Select a specific chat room to view details for that room. Note The number of records fetched from the database depends on the value selected from "Records Fetched" drop-down list. | Note | The number of records fetched from the database depends on the value selected from "Records Fetched" drop-down list. |
| Note | The number of records fetched from the database depends on the value selected from "Records Fetched" drop-down list. |

| Note | The number of records fetched from the database depends on the value selected from "Records Fetched" drop-down list. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat . |
|---|---|
| Step 2 | To change the maximum number of chat rooms that are allowed, enter a value in the field for Maximum number of rooms allowed . The default is set to 5500. |
| Step 3 | Click Save . |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat . |
|---|---|
| Step 2 | Configure the room member settings as described in Room Member Settings. |
| Step 3 | Click Save . |
| Step 4 | In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services . |
| Step 5 | Restart the Cisco XCP Text Conference Manager service. |

| Note | Persistent chat rooms inherit their settings when you create the room. Later changes do not apply to existing rooms. Those
                                                   changes only apply to rooms created after the changes take effect. |
|---|---|

| Field | Description |
|---|---|
| Rooms are for members only by default | Check this check box if you want rooms to be created as members-only rooms by default. Members-only rooms are accessible only
                                                   by users on an allowed list configured by the room owner or administrator. The check box is unchecked by default. Note The allowed list contains the list of members who are allowed in the room. It is created by the owner or administrator of
                                                               the members-only room. | Note | The allowed list contains the list of members who are allowed in the room. It is created by the owner or administrator of
                                                               the members-only room. |
| Note | The allowed list contains the list of members who are allowed in the room. It is created by the owner or administrator of
                                                               the members-only room. |
| Only moderators can invite people to members-only rooms | Check this check box if you want to configure the room so that only moderators are allowed to invite users to the room. If
                                                   this check box is unchecked, members can invite other users to join the room. The check box is checked by default. |
| Room owners can change whether or not rooms are for members only | Check this check box  if you want to configure the room so that room owners are allowed to change whether or not rooms are
                                                   for members only. The check box is checked by default. Note A room owner is the user who creates the room or a user who has been designated by the room creator or owner as someone with
                                                               owner status (if allowed). A room owner is allowed to change the room configuration and destroy the room, in addition to all
                                                               other administrator abilities. | Note | A room owner is the user who creates the room or a user who has been designated by the room creator or owner as someone with
                                                               owner status (if allowed). A room owner is allowed to change the room configuration and destroy the room, in addition to all
                                                               other administrator abilities. |
| Note | A room owner is the user who creates the room or a user who has been designated by the room creator or owner as someone with
                                                               owner status (if allowed). A room owner is allowed to change the room configuration and destroy the room, in addition to all
                                                               other administrator abilities. |
| Room owners can change whether or not only moderators can invite people to members-only rooms | Check this check box if you want to configure the room so that room owners can allow members to invite other users to the
                                                   room. The check box is checked by default. |
| Users can add themselves to rooms as members | Check this check box if you want to configure the room so that any user can request to join the room at any time. If this
                                                   check box is checked, the room has an open membership. The check box is unchecked by default. |
| Room owners can change whether users can add themselves to rooms as members | Check this check box if you want to configure the room so that room owners have the ability to change the setting that is
                                                   listed in Step 5 at any time. The check box is unchecked by default. |

| Note | The allowed list contains the list of members who are allowed in the room. It is created by the owner or administrator of
                                                               the members-only room. |
|---|---|

| Note | A room owner is the user who creates the room or a user who has been designated by the room creator or owner as someone with
                                                               owner status (if allowed). A room owner is allowed to change the room configuration and destroy the room, in addition to all
                                                               other administrator abilities. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat . |
|---|---|
| Step 2 | Configure the availability member settings as described in Availability Settings. |
| Step 3 | Click Save . |
| Step 4 | In Cisco Unified IM and Presence Serviceablity , choose Tools > Control Center - Feature Services . |
| Step 5 | Restart the Cisco XCP Text Conference Manager service. |

| Field | Description |
|---|---|
| Members and administrators who are not in a room are still visible in the room | Check this check box if you want to keep users on the room roster even if they are currently offline. The check box is checked
                                                   by default. Note If the administrator leaves the chat room, the administrator's userid will still be visible in the chat room. The user needs
                                                               to close and reopen the chat room to refresh the user's list. | Note | If the administrator leaves the chat room, the administrator's userid will still be visible in the chat room. The user needs
                                                               to close and reopen the chat room to refresh the user's list. |
| Note | If the administrator leaves the chat room, the administrator's userid will still be visible in the chat room. The user needs
                                                               to close and reopen the chat room to refresh the user's list. |
| Room owners can change whether members and administrators who are not in a room are still visible in the room | Check this check box if you want to allow room owners the ability to change the visibility of a member or administrator. The
                                                   check box is checked by default. |
| Rooms are backwards-compatible with older clients | Check this check box if you want the service to function well with older Group Chat 1.0 clients. The check box is unchecked
                                                   by default. |
| Room owners can change whether rooms are backwards-compatible with older clients | Check this check box if you want to allow room owners the ability to control backward compatibility of the chat rooms. The
                                                   check box is unchecked by default. |
| Rooms are anonymous by default | Check this check box if you want the room to display the user nickname but keep the Jabber ID private. The check box is unchecked
                                                   by default. |
| Room owners can change whether or not rooms are anonymous | Check this check box if you want to allow room owners to control the anonymity level of the user Jabber ID. The check box
                                                   is unchecked by default. |

| Note | If the administrator leaves the chat room, the administrator's userid will still be visible in the chat room. The user needs
                                                               to close and reopen the chat room to refresh the user's list. |
|---|---|

| Step 1 | To change the system maximum number of users that are allowed in a room, enter a value in the field for How many users can be in a room at one time . The default value is set to 1000. Note The total number of users in a room should not exceed the value that you set. The total number of users in a room includes
                                                            both normal users and hidden users. | Note | The total number of users in a room should not exceed the value that you set. The total number of users in a room includes
                                                            both normal users and hidden users. |
|---|---|---|---|
| Note | The total number of users in a room should not exceed the value that you set. The total number of users in a room includes
                                                            both normal users and hidden users. |
| Step 2 | To change the number of hidden users that are allowed in a room, enter a value in the field for How many hidden users can be in a room at one time . Hidden users are not visible to others, cannot send a message to the room, and do not send presence updates. Hidden users
                                             can see all messages in the room and receive presence updates from others. The default value is 1000. |
| Step 3 | To change the default maximum number of users that are allowed in a room, enter a value in the field for Default maximum occupancy for a room . The default value is set to 50 and cannot be any higher than the value that is set in Step 1. |
| Step 4 | Check Room owners can change default maximum occupancy for a room if you want to allow room owners to change the default maximum room occupancy. The check box is checked by default. |
| Step 5 | Click Save . |

| Note | The total number of users in a room should not exceed the value that you set. The total number of users in a room includes
                                                            both normal users and hidden users. |
|---|---|

| Step 1 | From the drop-down list for Lowest participation level a user can have to send a private message from within the room , choose one: Visitor allows visitors, participants, and moderators to send a private message to other users in the room.This is the default setting. Participant allows participants and moderators to send a private message to other users in the room. Moderator allows only moderators to send a private message to other users in the room. |
|---|---|
| Step 2 | Check Room owners can change the lowest participation level a user can have to send a private message from within the room if you want to allow room owners to change the minimum participation level for private messages. The check box is checked
                                             by default. |
| Step 3 | From the drop-down list for Lowest participation level a user can have to change a room's subject, choose one: Participant allows participants and moderators to change the room's subject. This is the default setting. Moderator allows only moderators to change the room's subject. Visitors are not permitted to change the room subject. |
| Step 4 | Check Room owners can change the lowest participation level a user can have to change a room's subject if you want to allow room owners to change the minimum participation level for updating a room's subject. |
| Step 5 | Check Remove all XHTML formatting from messages if you want to remove all Extensible Hypertext Markup Language (XHTML) from messages. The check box is unchecked by default. |
| Step 6 | Check Room owners can change XHTML formatting setting if you want to allow room owners to change the XHTML formatting setting. The check box is unchecked by default. |
| Step 7 | Click Save . |

| Step 1 | Check Rooms are moderated by default if you want to enforce the role of moderator in a room. The check box is unchecked by default. |
|---|---|
| Step 2 | Check Room owners can change whether rooms are moderated by default if you want to allow room owners the ability to change whether rooms are moderated. The check box is checked by default. |
| Step 3 | Click Save . |

| Step 1 | To change the maximum number of messages that users can retrieve from the archive, enter a value in the field for Maximum number of messages that can be retrieved from the archive . The default value is set to 100. It serves as a limit for the next setting. |
|---|---|
| Step 2 | To change the number of previous messages displayed when a user joins a chat room, enter a value in the field for Number of messages in chat history displayed by default . The default value is set to 15 and cannot be any higher than the value that is set in Step 1. |
| Step 3 | Check Room owners can change the number of messages displayed in chat history if you want to allow room owners to change the number of previous messages displayed when a user joins a chat room. The check
                                             box is unchecked by default. |
| Step 4 | Click Save . |

| Note | Ad hoc chat is enabled by default, but persistent chat is disabled by default. Completing this task will disable persistent
                                             chat |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Settings . |
|---|---|
| Step 2 | Click Set to Default . |
| Step 3 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Assign Mode for Managing Chat Aliases | Assign whether you want the system to manage chat node aliases or whether you want to do it manually. |
| Step 2 | Add Chat Node Alias Manually | Add, edit, or delete chat node aliases for your cluster. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat and Persistent Chat . |
|---|---|
| Step 2 | Enable or disable system-generated aliases: If you want the system to assign chat node aliases automatically, check System Automatically Manages Primary Group Chat Server Aliases . Tip Choose Messaging > Group Chat Server Alias Mapping to verify that the system-generated alias is listed under Primary Group Chat Server Aliases. If you want to assign chat node aliases manually, uncheck System Automatically Manages Primary Group Chat Server Aliases . | Tip | Choose Messaging > Group Chat Server Alias Mapping to verify that the system-generated alias is listed under Primary Group Chat Server Aliases. |
| Tip | Choose Messaging > Group Chat Server Alias Mapping to verify that the system-generated alias is listed under Primary Group Chat Server Aliases. |

| Tip | Choose Messaging > Group Chat Server Alias Mapping to verify that the system-generated alias is listed under Primary Group Chat Server Aliases. |
|---|---|

| Note | Although it is not mandatory, we recommend that you always include the domain when you assign a new chat node alias to a node.
                                                Use this convention for additional aliases, newalias.domain. Choose Cisco Unified CM IM and Presence Administration > Presence Settings > Advanced Settings to see the domain. |
|---|---|

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Messaging > Group Chat Server Alias Mapping . |
|---|---|
| Step 2 | Click Find . The Group Chat Server Alias window displays the existing node aliases. |
| Step 3 | To add a new alias: Click Add New . In the Group Chat Server Alias field, enter a new alias. From the Server Name drop-down list box, select the server to which you want to assign the alias. Click Save . |
| Step 4 | To edit an existing alias: Select the alias. Enter your updates and click Save . |
| Step 5 | To delete an alias, select the alias and click Delete Selected . |

| Step 1 | Log into Cisco Unified CM IM and Presence Administration on the database publisher node. |
|---|---|
| Step 2 | Choose Messaging > External Server Setup > External Database Jobs . |
| Step 3 | Click Clear External DB . |
| Step 4 | Do one of the following: For manual cleanup of an external database that connects to the publisher node, select Same Cup Node . For manual cleanup of an external database that connects to a subscriber node, select Other Cup Node and then select the external database details. If you are configuring the system to monitor and clean the external database automatically, check the Automatic Clean-up radio button. Note We recommend that you run a manual cleanup prior to setting up the automatic cleanup. | Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
| Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
| Step 5 | Set the Number of Days that you want to go back for file deletion. For example, if you enter 90, the system deletes records that are older than
                                          90 days. |
| Step 6 | Click Update Schema to create the Indexes and stored procedures for the database. Note You need to update the schema only the first time that you run the job. | Note | You need to update the schema only the first time that you run the job. |
| Note | You need to update the schema only the first time that you run the job. |
| Step 7 | Set the Number of Days that you want to go back for file deletion. For example, if you enter 90 , the system deletes records that are older than 90 days. |
| Step 8 | In the Feature Tables section, select each feature for which you want to clean records: Text Conference (TC) —Select this option to clean database tables for the Persistent Chat feature. Message Archiver (MA) —Select this option to clean database tables for the Message Archiver feature. Managed File Transfer (MFT) —Select this option to clean database tables for the Managed File Transfer feature |
| Step 9 | Click Submit Clean-up Job . Note If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. | Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |
| Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |

| Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
|---|---|

| Note | You need to update the schema only the first time that you run the job. |
|---|---|

| Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |
|---|---|