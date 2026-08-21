---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su1-cup0-b-config-and-admin-guide-1-b7ca68ee74
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su1/cup0_b_config-and-admin-guide-1251su1/cup0_b_config-and-admin-guide-1251su1_chapter_01111.html
retrieved_at: 2026-08-21T09:01:38.473850+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU1

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU1

Updated: November 27, 2024

Chapter: Configure Ad Hoc and Persistent Chat

## Chapter: Configure Ad Hoc and Persistent Chat

# Configure Ad Hoc and Persistent Chat

## Group Chat Rooms Overview

Group chat is an instant messaging session between more than two users. IM and Presence Service supports group chat in either
                           ad hoc chat rooms or persistent chat rooms. Support for ad hoc chat rooms is enabled by default once you enable instant messaging,
                           but you must configure the system to support persistent chat rooms.

### Ad Hoc Chat Rooms

Ad hoc chat rooms are group chat sessions that remain in existence only as long as one person is still connected to the chat
                              room. Ad hoc chat rooms are deleted from the system when the last user leaves the room. Records of the instant message conversation
                              are not maintained permanently. Once instant messaging is enabled, ad hoc chat rooms are enabled by default.

Ad hoc chat rooms are public rooms by default, but can be reconfigured to be private. However, how users can join public or
                              private ad hoc rooms depends on the type of XMPP client in use.

Cisco Jabber users must be invited in order to join any ad hoc chat room (public or private)

Users on third-party XMPP clients can be invited in order to join any ad hoc chat room (public or private), or they can search
                                    for public-only ad hoc rooms to join via room discovery service.

### Persistent Chat Rooms

Persistent chat rooms are group chat sessions that remain in existence even after all users have left the room. Users are
                              expected to return to the same room over time to continue the discussion.

Persistent chat rooms are created so that users can collaborate and share knowledge on a specific topic, search through archives
                              of what was said on that topic (if this feature is enabled on IM and Presence Service), and then participate in the discussion
                              of that topic in real-time.

You must configure the system for Persistent Chat Rooms. In addition, persistent chat requires that you deploy an external
                              database

Persistent chat rooms are supported by both desktop and mobile Jabber clients, including both IOS and Android clients. For
                              mobile clients, you must be running a minimum Jabber release of 12.1(0).

## Group Chat Prerequisites

### Ad Hoc Chat Prerequisites

If you are deploying ad hoc chat rooms, make sure that instant messaging is enabled. For details, see Enable Instant Messaging .

### Persistent Chat Prerequisites

If you are deploying persistent chat rooms:

Make sure that instant messaging is enabled. For details, see Enable Instant Messaging .

You must deploy an external database. For database setup and support information, see the Database Setup Guide for IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

Decide whether you are going to deploy High Availability for Persistent Chat. This deployment type adds redundancy and failover
                                    to your persistent chat rooms. However, the external database requirements are slightly different than if you deploy the feature
                                    without High Availability.

For Persistent Chat deployments, we recommend that you deploy a minimum OVA of 15,000 users.

## Group Chat  and Persistent Chat Task Flow

Step 1

Configure Group Chat System Administrators

Add system administrators to manage the persistent chat system.

Step 2

Configure Chat Room Settings

Configure basic chat room settings. Optionally, enable Persistent Chat.

Step 3

Restart the Cisco XCP Text Conference Manager

If you are deploying Persistent Chat, make sure that the Cisco XCP Text Conference Manager service is running.

Step 4

Set up External Database for Persistent Chat

For Persistent Chat, you must configure a unique external database instance for each node.

If you are deploying High Availability for Persistent Chat, you can skip the remaining tasks in this chapter as the database
                                                      requirements are slighlty different when HA is deployed.

Step 5

Add External Database Connection

In the IM and Presence Service, set up a connection to your external database.

### Configure Group Chat System Administrators

Add system administrators to manage the persistent chat system.

Step 1

Choose Messaging > Group Chat System Administrators .

Step 2

Check Enable Group Chat System Administrators .

Restart the Cisco XCP Router when the setting is enabled or disabled. Once the System Administrator setting is enabled, you
                                             can add system administrators dynamically.

Step 3

Click Add New .

Step 4

Enter an IM address.

Example

The IM address must be in the format of name@domain.

Step 5

Enter a Nickname and Description .

Step 6

Click Save .

#### What to do next

Configure Chat Room Settings

### Configure Chat Room Settings

Configure basic chat room settings such as Room Member and Occupancy settings, and the maximum number of users per room.

Optionally, you can enable Persistent Chat by checking the Enable Persistent Chat check box.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Messaging > Group Chat and Persistent Chat

Step 2

Configure whether you want the system to manage chat node aliases by checking or unchecking the System automatically manages primary group chat server aliases check box.

- Checked—The system assigns chat node aliases automatically. This is the default value.

- Unchecked—Administrators can assign their own chat node aliases.

Step 3

Check the Enable Persistent Chat check box if you want your chat rooms to remain in existence after all partipants have left the room.

This is a cluster-wide setting. If persistent chat is enabled on any node in the cluster, clients in any cluster will be able
                                                         to discover the Text Conference instance on the node and chat rooms hosted on that node.

Users from a remote cluster can discover Text Conference instances and chat rooms in the local cluster even if Persistent
                                                         Chat is not enabled for the remote cluster.

Step 4

If you have chosen to enabled Persistent Chat, configure values for each to the following fields:

- Maximum number of persistent chat rooms allowed

- Number of connections to the database

- Database connection heartbeat interval (seconds)

- Timeout value for persistent chat rooms (minutes)

Do not set the Database Connection Heartbeat Interval value to zero without contacting Cisco support. The heartbeat interval is typically used to keep connections open through
                                                         firewalls.

Step 5

Under Room Settings , assign a maximum number of rooms.

Step 6

Complete the remaining settings in the Group Chat and Persistent Chat Settings window. For help with the fields and their settings, refer to the online help.

Step 7

Click Save .

#### What to do next

Restart the Cisco XCP Text Conference Manager

### Restart the Cisco XCP Text Conference Manager

If you have edited your chat settings or added one or more aliases to a chat node, restart the Cisco XCP Text Conference Manager service.

Step 1

In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services .

Step 2

From the Server drop-down list, choose the IM and Presence node and click Go .

Step 3

In the IM and Presence Service section, click the Cisco XCP Text Conference Manager radio button and click Start or Restart .

Step 4

Click OK when a message indicates that restarting may take a while.

Step 5

(Optional) Click Refresh if you want to verify that the service has fully restarted.

#### What to do next

If you are deploying High Availability for Persistent Chat, proceed to High Availability for Persistent Chat Task Flow .

Otherwise, Set up External Database for Persistent Chat .

### Set up External Database for Persistent Chat

This topic covers Persistent Chat without High Availability. If you are deploying High Availability for Persistent Chat, refer
                                             to that chapter instead for external database setup info.

If you are configuring persistent chat rooms, you must set up a separate external database instance for each node that hosts
                                 persistent chat rooms. In addition:

If persistent chat is enabled, an external database must be associated with the Text Conference Manager service, and the database
                                       must be active and reachable or the Text Conference Manager will not start.

If you use an external database for persistent chat logging, make sure that your database is large enough to handle the volume
                                       of information. Archiving all the messages in a chat room is optional, but will increase traffic on the node and consume disk
                                       space.

Use the External Database Cleanup Utility to set up jobs that monitor the database size and delete expired records automatically.

Before you configure the number of connections to the external database, consider the number of IMs you are writing and the
                                       overall volume of traffic that results. The number of connections that you configure will allow the system to scale. While
                                       the system defaults suit most installations, you may want to adapt the parameters for your specific deployment.

For instructions on how to set up an external database, see External Database Setup Guide for IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

#### What to do next

Add External Database Connection

### Add External Database Connection

Configure a connection to the Persistent Chat external database from the IM and Presence Service. A minimum of one unique
                                 logical external database instance (tablespace) is required for the entire IM and Presence Service intercluster.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Messaging > External Servers Setup > External Databases .

Step 2

Click Add New .

Step 3

In the Database Name field, enter the name of external database instance.

Step 4

From the Database Type drop-down, select the type of external
                                          database that you are deploying.

Step 5

Enter the User Name and Password information for the
                                          database.

Step 6

In the Hostname field, enter the hostname or IP address of the database.

Step 7

Complete the remaining settings in the External Database
                                             Settings window. For help with the fields and their settings, refer
                                          to the online help.

Step 8

Click Save .

Step 9

Repeat this procedure to create connections to each external
                                          database instance.

## Group Chat and Persistent Chat Interactions and Restrictions

Feature Interaction

Restriction

Archiving room joins

Archiving room joins and leaves is optional because it will increase traffic and consume space on the external database server.

Chat with anonymous rooms

If you are deploying chat via Cisco Jabber (either group chat or persistent chat), make sure that the Rooms are anonymous by default and Room owners can change whether or not rooms are anonymous options are not selected in the Group Chat and Persistent Chat Settings window. If either check box is checked, chat will fail

Database Connection Issues

If the connection with the external database fails after the Text Conference Manager service has started, the Text Conference
                                          Manager service will remain active and functional, however, messages will no longer be written to the database and new persistent
                                          rooms cannot be created until the connection recovers.

OVA Requirements

If you are deploying Persistent Chat or Intercluster Peering, the minimum OVA size that you can deploy for these features
                                          is the 5000 user OVA. It’s recommended that you deploy at least the 15,000 user OVA. Centralized Deployments may require the
                                          25,000 user OVA, depending on the size of the user base. For additional details on OVA options and user capacities, refer
                                          to the following site:

Persistent chat character limit with Microsoft SQL Server

Chat messages where the message body (includes HTML tags + text message) exceeds 4000 characters are not delivered. These
                                          messages are rejected and are not archived. This issue exists when Microsoft SQL Server is used as the external database for
                                          releases 11.5(1)SU3 onward. See CSCvd89705 for additional detail.

Persistent Chat for Jabber Mobile where a peer cluster is running a non-supported release

Persistent chat for Jabber mobile is introduced with 11.5(1)SU5 and is not supported on earlier 11.5(1)SU releases. This feature
                                          is also not supported for 12.0(1) or 12.0(1)SU1.

If you have Persistent Chat for Jabber mobile deployed in this release, and you also have intercluster peering set up with
                                          peer clusters that do not support persistent chat rooms for Jabber Mobile, the following conditions apply for Jabber mobile
                                          clients:

If the persistent chat room is hosted on a non-supported release, such as 11.5(1):

A Jabber mobile client that is homed from the supported cluster can join persistent chat rooms hosted on the non-supported
                                                cluster, but will have no option to mute the room. They will see a Global Mute option, but it will not work.

A Jabber mobile client that is homed on the non-supported peer cluster will be unable to join any persistent chat rooms.

If the persistent chat room is hosted on a supported release, such as 11.5(1)SU5:

A Jabber mobile client participant that is homed on the supported cluster will have all persistent chat on mobile functionality.

A Jabber mobile client from a non-supported peer cluster will be unable to join persistent chat rooms.

The search feature for Persistent Chat does not work when the Jabber Configuration file (jabber-config.xml) is set to disable the IM History.

In a split-brain scenario, When the subscriber or publisher detects its peer Text Conferencing service or any node is down,
                                          then the subscriber or publisher attempts a transition from normal to backup.

During this operation if loading of the peer's chat rooms fails to connect to external database, then the Cisco XCP Text Conferencing
                                          service will shutdown.

The maximum number of Persistent Chat Rooms supported on an IM&P deployment is 5000 per subcluster.

If High Availability is enabled, it is recommended to create a maximum of 2500 rooms per node. (though the system allows to
                                          create upto maximum of 5000 rooms per node). If more than 2500 rooms are configured per node in a High Availability deployment,
                                          then during failover, there would be more than 5000 rooms hosted on the backup node. This might result in unexpected performance
                                          issues depending on the traffic load.

The load of 5000 rooms on the system also depends on the number of participants in the room, the rate of message exchange
                                          in the rooms and the size of messages. Use Cisco Collaboration Sizing tool to ensure you have the right OVA setup for your
                                          Persistent Chat Deployment. For Information on  Collaboration Sizing tool, Please refer: https://cucst.cloudapps.cisco.com/landing

It is recommended to have your rooms balanced equally among both the nodes in a subcluster. And if you have more than one
                                          subcluster in a IM&P Cluster, it is recommended to also load balance the rooms across all the subclusters. Currently IM&P
                                          doesn't have a mechanism to automatically load balance the rooms. The responsibility of load balancing the room lies with
                                          the users creating the rooms. During room creation, users have to ensure that they use the jabber feature to automatically
                                          select a random node for a room creation.

Making ad hoc chat rooms private

Ad hoc chat rooms are public by default, but can be configured to be for members only with the following configuration:

From Cisco Unified CM IM and Presence Administration, choose Messaging > Group Chat and Persistent Chat .

Check the Rooms are for members only by default check box.

Uncheck the Room owners can change whether or not rooms are for members onl y check box.

Uncheck the Only moderators can invite people to members-only rooms check box.

Click Save .

Restart the Cisco XCP Text Conference service.

When you configure Ad hoc chat rooms as private on IM and Presence, persistent chat rooms also become private.

## Persistent Chat Examples (without HA)

The following two examples illustrate the Persistent Chat feature along with intercluster peering where High Availability for Persistent Chat is not deployed .

Cisco recommends that if you are deploying Persistent Chat, you should display High Availability for Persistent Chat in order
                                          to add redundancy to your persistent chat rooms.

### Persistent Chat (without HA) Enabled on all Intercluster Nodes

Persistent Chat (without HA) is enabled on all nodes in an intercluster  network. All nodes have an
                              external database associated for Persistent Chat, thereby allowing
                              all nodes to host persistent chat rooms.

The Cisco Text Conferencing service is running on all
                              nodes in either cluster, allowing all users in either cluster to join persistent chat rooms
                              that are hosted on any node in either cluster.

### Persistent Chat (without HA) Enabled in one Cluster of Intercluster Network

Only nodes in Cluster
                              1 are configured for Persistent Chat (without HA) and have external databases. External databases are not required in Cluster 2 as the nodes are not configured to host persistent
                              chat rooms.

However, the Cisco Text
                              Conference Manager service is running on all nodes in either cluster, thereby
                              allowing all users in either cluster to join the persistent chat rooms
                              that are hosted in Cluster 1.

## Persistent Chat Boundaries in IM and Presence

This section describes the matrix representing persistent chat (PChat) boundaries in IM and Presence with examples to clarify
                           various dependencies.

The following assumptions are made for deriving the persistent chat boundaries:

With respect to the number of rooms per alias/server/subcluster/cluster:

The server may contain several text conferencing aliases.

A subcluster contains two servers (nodes).

A cluster may have up to three subclusters.

If high availabilty (HA) is enabled, all supported room numbers are halved. The maximum allowed value for the Maximum number of persistent chat rooms allowed is 2500.

Example: Assuming 100 users per rooms in average, the IM and Presence service can support:

3500 persistent chat rooms per server without HA, or

1750 persistent chat rooms per server with HA.

Assuming one message per room per minute, up to 273 persistent chat rooms can be active per server.

The following are some examples to clarify these dependencies:

Rooms supported per time slice can be increased at the expense of the total number of rooms supported by using the following
                           formula:

Average Number of Users per Room

Number of PChat Rooms Supported

Rooms Supported Per Time Slice

Message Frequency = 1/min

Rooms Supported Per Time Slice

Message Frequency = 3/min

2

5000

100%

100%

5

5000

100%

58%

10

5000

99%

33%

15

5000

69%

23%

20

5000

53%

18%

30

5000

36%

12%

50

5000

22%

7%

100

3497

16%

5%

200

2064

14%

5%

500

926

12%

4%

1,000

482

12%

4%

It is assumed that 30% of the users have two devices/clients.

Example for 25K OVA:

Average Number of Users per Room = 10

Message frequency = 3/ min

Current Number of Rooms Supported = 5000

Current Rooms Supported per Time Slice = 33%

New Rooms Supported per Time Slice = 50%

Result:

New Rooms Supported = 5000 * 33/50 =3300

Average Number of Users per Room

Number of PChat Rooms Supported

Rooms Supported Per Time Slice

Message Frequency = 1/min

Rooms Supported Per Time Slice

Message Frequency = 3/min

2

5000

100%

80%

5

5000

100%

41%

10

5000

67%

22%

15

5000

46%

15%

20

5000

35%

12%

30

5000

24%

8%

50

5000

14%

5%

100

3497

10%

3%

200

2064

9%

3%

500

926

8%

3%

1,000

482

7%

2%

It is assumed that 30% of the users have two devices/clients.

Example for 15K OVA:

Average Number of Users per Room = 5

Message frequency = 3/ min

Current Number of Rooms Supported = 5000

Current Rooms Supported per Time Slice = 41%

New Rooms Supported per Time Slice = 50%

Result:

New Rooms Supported = 5000 * 41/50 =4100

Average Number of Users per Room

Number of PChat Rooms Supported

Rooms Supported Per Time Slice

Message Frequency = 1/min

Rooms Supported Per Time Slice

Message Frequency = 3/min

2

5000

94%

31%

5

5000

53%

18%

10

4654

33%

11%

15

4261

26%

9%

20

3929

21%

7%

30

3399

17%

6%

50

2677

13%

4%

100

1748

10%

3%

200

1032

9%

3%

500

463

8%

3%

1,000

241

7%

2%

It is assumed that 30% of the users have two devices/clients.

Example for 5K OVA:

Average Number of Users per Room = 2

Message frequency = 3/ min

Current Number of Rooms Supported = 5000

Current Rooms Supported per Time Slice = 31%

New Rooms Supported per Time Slice = 50%

Result:

New Rooms Supported = 5000 * 31/50 =3100

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Group Chat System Administrators | Add system administrators to manage the persistent chat system. |
| Step 2 | Configure Chat Room Settings | Configure basic chat room settings. Optionally, enable Persistent Chat. |
| Step 3 | Restart the Cisco XCP Text Conference Manager | If you are deploying Persistent Chat, make sure that the Cisco XCP Text Conference Manager service is running. |
| Step 4 | Set up External Database for Persistent Chat | For Persistent Chat, you must configure a unique external database instance for each node. Note If you are deploying High Availability for Persistent Chat, you can skip the remaining tasks in this chapter as the database
                                                      requirements are slighlty different when HA is deployed. | Note | If you are deploying High Availability for Persistent Chat, you can skip the remaining tasks in this chapter as the database
                                                      requirements are slighlty different when HA is deployed. |
| Note | If you are deploying High Availability for Persistent Chat, you can skip the remaining tasks in this chapter as the database
                                                      requirements are slighlty different when HA is deployed. |
| Step 5 | Add External Database Connection | In the IM and Presence Service, set up a connection to your external database. |

| Note | If you are deploying High Availability for Persistent Chat, you can skip the remaining tasks in this chapter as the database
                                                      requirements are slighlty different when HA is deployed. |
|---|---|

| Step 1 | Choose Messaging > Group Chat System Administrators . |
|---|---|
| Step 2 | Check Enable Group Chat System Administrators . Restart the Cisco XCP Router when the setting is enabled or disabled. Once the System Administrator setting is enabled, you
                                             can add system administrators dynamically. |
| Step 3 | Click Add New . |
| Step 4 | Enter an IM address. Example The IM address must be in the format of name@domain. |
| Step 5 | Enter a Nickname and Description . |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Messaging > Group Chat and Persistent Chat |
|---|---|
| Step 2 | Configure whether you want the system to manage chat node aliases by checking or unchecking the System automatically manages primary group chat server aliases check box. Checked—The system assigns chat node aliases automatically. This is the default value. Unchecked—Administrators can assign their own chat node aliases. |
| Step 3 | Check the Enable Persistent Chat check box if you want your chat rooms to remain in existence after all partipants have left the room. Note This is a cluster-wide setting. If persistent chat is enabled on any node in the cluster, clients in any cluster will be able
                                                         to discover the Text Conference instance on the node and chat rooms hosted on that node. Users from a remote cluster can discover Text Conference instances and chat rooms in the local cluster even if Persistent
                                                         Chat is not enabled for the remote cluster. | Note | This is a cluster-wide setting. If persistent chat is enabled on any node in the cluster, clients in any cluster will be able
                                                         to discover the Text Conference instance on the node and chat rooms hosted on that node. Users from a remote cluster can discover Text Conference instances and chat rooms in the local cluster even if Persistent
                                                         Chat is not enabled for the remote cluster. |
| Note | This is a cluster-wide setting. If persistent chat is enabled on any node in the cluster, clients in any cluster will be able
                                                         to discover the Text Conference instance on the node and chat rooms hosted on that node. Users from a remote cluster can discover Text Conference instances and chat rooms in the local cluster even if Persistent
                                                         Chat is not enabled for the remote cluster. |
| Step 4 | If you have chosen to enabled Persistent Chat, configure values for each to the following fields: Maximum number of persistent chat rooms allowed Number of connections to the database Database connection heartbeat interval (seconds) Timeout value for persistent chat rooms (minutes) Note Do not set the Database Connection Heartbeat Interval value to zero without contacting Cisco support. The heartbeat interval is typically used to keep connections open through
                                                         firewalls. | Note | Do not set the Database Connection Heartbeat Interval value to zero without contacting Cisco support. The heartbeat interval is typically used to keep connections open through
                                                         firewalls. |
| Note | Do not set the Database Connection Heartbeat Interval value to zero without contacting Cisco support. The heartbeat interval is typically used to keep connections open through
                                                         firewalls. |
| Step 5 | Under Room Settings , assign a maximum number of rooms. |
| Step 6 | Complete the remaining settings in the Group Chat and Persistent Chat Settings window. For help with the fields and their settings, refer to the online help. |
| Step 7 | Click Save . |

| Note | This is a cluster-wide setting. If persistent chat is enabled on any node in the cluster, clients in any cluster will be able
                                                         to discover the Text Conference instance on the node and chat rooms hosted on that node. Users from a remote cluster can discover Text Conference instances and chat rooms in the local cluster even if Persistent
                                                         Chat is not enabled for the remote cluster. |
|---|---|

| Note | Do not set the Database Connection Heartbeat Interval value to zero without contacting Cisco support. The heartbeat interval is typically used to keep connections open through
                                                         firewalls. |
|---|---|

| Step 1 | In Cisco Unified IM and Presence Serviceability , choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | From the Server drop-down list, choose the IM and Presence node and click Go . |
| Step 3 | In the IM and Presence Service section, click the Cisco XCP Text Conference Manager radio button and click Start or Restart . |
| Step 4 | Click OK when a message indicates that restarting may take a while. |
| Step 5 | (Optional) Click Refresh if you want to verify that the service has fully restarted. |

| Note | This topic covers Persistent Chat without High Availability. If you are deploying High Availability for Persistent Chat, refer
                                             to that chapter instead for external database setup info. |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Messaging > External Servers Setup > External Databases . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Database Name field, enter the name of external database instance. |
| Step 4 | From the Database Type drop-down, select the type of external
                                          database that you are deploying. |
| Step 5 | Enter the User Name and Password information for the
                                          database. |
| Step 6 | In the Hostname field, enter the hostname or IP address of the database. |
| Step 7 | Complete the remaining settings in the External Database
                                             Settings window. For help with the fields and their settings, refer
                                          to the online help. |
| Step 8 | Click Save . |
| Step 9 | Repeat this procedure to create connections to each external
                                          database instance. |

| Feature Interaction | Restriction |
|---|---|
| Archiving room joins | Archiving room joins and leaves is optional because it will increase traffic and consume space on the external database server. |
| Chat with anonymous rooms | If you are deploying chat via Cisco Jabber (either group chat or persistent chat), make sure that the Rooms are anonymous by default and Room owners can change whether or not rooms are anonymous options are not selected in the Group Chat and Persistent Chat Settings window. If either check box is checked, chat will fail |
| Database Connection Issues | If the connection with the external database fails after the Text Conference Manager service has started, the Text Conference
                                          Manager service will remain active and functional, however, messages will no longer be written to the database and new persistent
                                          rooms cannot be created until the connection recovers. |
| OVA Requirements | If you are deploying Persistent Chat or Intercluster Peering, the minimum OVA size that you can deploy for these features
                                          is the 5000 user OVA. It’s recommended that you deploy at least the 15,000 user OVA. Centralized Deployments may require the
                                          25,000 user OVA, depending on the size of the user base. For additional details on OVA options and user capacities, refer
                                          to the following site: Note It’s strongly recommended to deploy at least the 15,000 user OVA on all IMP nodes. https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html | Note | It’s strongly recommended to deploy at least the 15,000 user OVA on all IMP nodes. |
| Note | It’s strongly recommended to deploy at least the 15,000 user OVA on all IMP nodes. |
| Persistent chat character limit with Microsoft SQL Server | Chat messages where the message body (includes HTML tags + text message) exceeds 4000 characters are not delivered. These
                                          messages are rejected and are not archived. This issue exists when Microsoft SQL Server is used as the external database for
                                          releases 11.5(1)SU3 onward. See CSCvd89705 for additional detail. |
| Persistent Chat for Jabber Mobile where a peer cluster is running a non-supported release | Persistent chat for Jabber mobile is introduced with 11.5(1)SU5 and is not supported on earlier 11.5(1)SU releases. This feature
                                          is also not supported for 12.0(1) or 12.0(1)SU1. If you have Persistent Chat for Jabber mobile deployed in this release, and you also have intercluster peering set up with
                                          peer clusters that do not support persistent chat rooms for Jabber Mobile, the following conditions apply for Jabber mobile
                                          clients: If the persistent chat room is hosted on a non-supported release, such as 11.5(1): A Jabber mobile client that is homed from the supported cluster can join persistent chat rooms hosted on the non-supported
                                                cluster, but will have no option to mute the room. They will see a Global Mute option, but it will not work. A Jabber mobile client that is homed on the non-supported peer cluster will be unable to join any persistent chat rooms. If the persistent chat room is hosted on a supported release, such as 11.5(1)SU5: A Jabber mobile client participant that is homed on the supported cluster will have all persistent chat on mobile functionality. A Jabber mobile client from a non-supported peer cluster will be unable to join persistent chat rooms. Note The search feature for Persistent Chat does not work when the Jabber Configuration file (jabber-config.xml) is set to disable the IM History. | Note | The search feature for Persistent Chat does not work when the Jabber Configuration file (jabber-config.xml) is set to disable the IM History. |
| Note | The search feature for Persistent Chat does not work when the Jabber Configuration file (jabber-config.xml) is set to disable the IM History. |
| External Database connectivity and Cisco XCP Text Conferencing service | In a split-brain scenario, When the subscriber or publisher detects its peer Text Conferencing service or any node is down,
                                          then the subscriber or publisher attempts a transition from normal to backup. During this operation if loading of the peer's chat rooms fails to connect to external database, then the Cisco XCP Text Conferencing
                                          service will shutdown. |
| Number of Persistent chat rooms supported if High Availability is configured | The maximum number of Persistent Chat Rooms supported on an IM&P deployment is 5000 per subcluster. If High Availability is enabled, it is recommended to create a maximum of 2500 rooms per node. (though the system allows to
                                          create upto maximum of 5000 rooms per node). If more than 2500 rooms are configured per node in a High Availability deployment,
                                          then during failover, there would be more than 5000 rooms hosted on the backup node. This might result in unexpected performance
                                          issues depending on the traffic load. The load of 5000 rooms on the system also depends on the number of participants in the room, the rate of message exchange
                                          in the rooms and the size of messages. Use Cisco Collaboration Sizing tool to ensure you have the right OVA setup for your
                                          Persistent Chat Deployment. For Information on  Collaboration Sizing tool, Please refer: https://cucst.cloudapps.cisco.com/landing It is recommended to have your rooms balanced equally among both the nodes in a subcluster. And if you have more than one
                                          subcluster in a IM&P Cluster, it is recommended to also load balance the rooms across all the subclusters. Currently IM&P
                                          doesn't have a mechanism to automatically load balance the rooms. The responsibility of load balancing the room lies with
                                          the users creating the rooms. During room creation, users have to ensure that they use the jabber feature to automatically
                                          select a random node for a room creation. |
| Making ad hoc chat rooms private | Ad hoc chat rooms are public by default, but can be configured to be for members only with the following configuration: From Cisco Unified CM IM and Presence Administration, choose Messaging > Group Chat and Persistent Chat . Check the Rooms are for members only by default check box. Uncheck the Room owners can change whether or not rooms are for members onl y check box. Uncheck the Only moderators can invite people to members-only rooms check box. Click Save . Restart the Cisco XCP Text Conference service. Note When you configure Ad hoc chat rooms as private on IM and Presence, persistent chat rooms also become private. | Note | When you configure Ad hoc chat rooms as private on IM and Presence, persistent chat rooms also become private. |
| Note | When you configure Ad hoc chat rooms as private on IM and Presence, persistent chat rooms also become private. |

| Note | It’s strongly recommended to deploy at least the 15,000 user OVA on all IMP nodes. |
|---|---|

| Note | The search feature for Persistent Chat does not work when the Jabber Configuration file (jabber-config.xml) is set to disable the IM History. |
|---|---|

| Note | When you configure Ad hoc chat rooms as private on IM and Presence, persistent chat rooms also become private. |
|---|---|

| Note | Cisco recommends that if you are deploying Persistent Chat, you should display High Availability for Persistent Chat in order
                                          to add redundancy to your persistent chat rooms. |
|---|---|

| Average Number of Users per Room | Number of PChat Rooms Supported | Rooms Supported Per Time Slice Message Frequency = 1/min | Rooms Supported Per Time Slice Message Frequency = 3/min |
|---|---|---|---|
| 2 | 5000 | 100% | 100% |
| 5 | 5000 | 100% | 58% |
| 10 | 5000 | 99% | 33% |
| 15 | 5000 | 69% | 23% |
| 20 | 5000 | 53% | 18% |
| 30 | 5000 | 36% | 12% |
| 50 | 5000 | 22% | 7% |
| 100 | 3497 | 16% | 5% |
| 200 | 2064 | 14% | 5% |
| 500 | 926 | 12% | 4% |
| 1,000 | 482 | 12% | 4% |

| Note | It is assumed that 30% of the users have two devices/clients. |
|---|---|

| Average Number of Users per Room | Number of PChat Rooms Supported | Rooms Supported Per Time Slice Message Frequency = 1/min | Rooms Supported Per Time Slice Message Frequency = 3/min |
|---|---|---|---|
| 2 | 5000 | 100% | 80% |
| 5 | 5000 | 100% | 41% |
| 10 | 5000 | 67% | 22% |
| 15 | 5000 | 46% | 15% |
| 20 | 5000 | 35% | 12% |
| 30 | 5000 | 24% | 8% |
| 50 | 5000 | 14% | 5% |
| 100 | 3497 | 10% | 3% |
| 200 | 2064 | 9% | 3% |
| 500 | 926 | 8% | 3% |
| 1,000 | 482 | 7% | 2% |

| Note | It is assumed that 30% of the users have two devices/clients. |
|---|---|

| Average Number of Users per Room | Number of PChat Rooms Supported | Rooms Supported Per Time Slice Message Frequency = 1/min | Rooms Supported Per Time Slice Message Frequency = 3/min |
|---|---|---|---|
| 2 | 5000 | 94% | 31% |
| 5 | 5000 | 53% | 18% |
| 10 | 4654 | 33% | 11% |
| 15 | 4261 | 26% | 9% |
| 20 | 3929 | 21% | 7% |
| 30 | 3399 | 17% | 6% |
| 50 | 2677 | 13% | 4% |
| 100 | 1748 | 10% | 3% |
| 200 | 1032 | 9% | 3% |
| 500 | 463 | 8% | 3% |
| 1,000 | 241 | 7% | 2% |

| Note | It is assumed that 30% of the users have two devices/clients. |
|---|---|