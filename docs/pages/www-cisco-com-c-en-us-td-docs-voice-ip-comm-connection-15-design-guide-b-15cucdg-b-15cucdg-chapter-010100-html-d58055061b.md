---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-guide-b-15cucdg-b-15cucdg-chapter-010100-html-d58055061b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg/b_15cucdg_chapter_010100.html
retrieved_at: 2026-08-17T02:15:14.495985+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: August 12, 2025

Chapter: Single
	 Inbox

## Chapter: Single
	 Inbox

# Single
                     	 Inbox

## About Single
                        	 Inbox

Single Inbox, one of the unified messaging features in Unity Connection, synchronizes voice messages in Unity Connection and
                           mailboxes of supported mail servers

The following are the supported mail servers with which you can integrate Unity Connection to enable unified messaging:

Microsoft Exchange Servers

Microsoft Office 365

Gmail Server

When a user is enabled for single inbox, all Unity Connection voice messages that are sent to the user, including those sent
                           from Cisco Unity Connection ViewMail for Microsoft Outlook, are first stored in Unity Connection and are immediately replicated
                           to the user’s correspnding Exchange/O365 mailbox.

Unity Connection 15 and later provides a new way to users for accessing the voice messages on their Gmail account. For this,
                           you need to configure unified messaging with Google Workspace to synchronize the voice messages between Unity Connection and Gmail server.

If you have configured single Inbox with Google Workspace, all Unity Connection voice messages that are sent to the user,
                           are first stored in Unity Connection and are then synchronized to the user's Gmail account.

For detailed explanation and configuration of Single Inbox, see “Configuring Unified Messaging” chapter in the Unified Messaging Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

For Unity Connection system requirements for Single Inbox, see “ Unified Messaging Requirements: Synchronizing Unity Connection and Exchange Mailboxes(Single Inbox) ” section of System Requirements for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

The synchronization of voice messages in Unity Connection and mail servers (single inbox) supports both the IPv4 and IPv6
                           addresses. However, the IPv6 address works only when Unity Connection platform is configured in dual (IPv4/IPv6) mode.

## Unified Messaging Services and Unified Messaging Accounts

When you configure unified messaging, including single inbox, you add one or more unified messaging services on each Unity
                           Connection server. Each unified messaging service specifies:

Which supported mail servers you want to access

Which unified messaging features you want to enable

With Exchange/Office 365 Servers

When you add unified messaging services with Exchnage/Office 365, consider the following:

Settings for unified messaging services allow you either to configure Unity Connection to communicate with a specific Exchange
                                 server, or configure Unity Connection to search for Exchange servers. If you have more than a few Exchange servers, you should
                                 use the option to search for Exchange servers. If you configure Unity Connection to communicate with specific Exchange servers,
                                 you must do the following:

Add another unified messaging service whenever you add another Exchange server.

Change Unity Connection user settings whenever you move Exchange mailboxes from one Exchange server to another.

There is no hard limit on the number of unified messaging services that you can create, but maintenance becomes time-consuming
                                 when you create more than a couple of dozen.

To enable unified messaging features for Unity Connection users, you add one or more unified messaging accounts for each user.
                                 For each unified messaging account, you specify a unified messaging service, which determines which unified messaging features
                                 the user can use.

If you do not want all users to have access to all unified messaging features, you can create multiple unified messaging services
                                 that enable different features or different combinations of features. For example, you might configure one unified messaging
                                 service that enables text to speech (TTS), another that enables access to Exchange calendars and contacts, and a third that
                                 enables single inbox. With this design, if you want a user to have access to all three features, you would create three unified
                                 messaging accounts for the user, one for each of the three unified messaging services.

You cannot create two unified messaging accounts that enable the same feature for the same user. For example, suppose you
                           add two unified messaging services:

One enables TTS and access to Exchange calendars and contacts.

The other enables TTS and single inbox.

If you create two unified messaging accounts for the user with the goal of giving the user access to all three features, you
                           must disable TTS in one of the unified messaging accounts.

When migrating from EWS to Microsoft Graph API-based integration for Office 365 during the upgrade to Cisco Unity Connection
                                       15SU4 or later releases, the Unified Messaging Service (UMS) may require up to 4 hours to achieve full stability and operational
                                       readiness.

With Google Workspace or Gmail Server

When you add unified messaging services with Google Workspace, consider the following:

Unified Messaging Service settings allows administrator to configure Unity Connection to communicate with Gmail Server.

There is no hard limit on the number of unified messaging services that you can create, but maintenance becomes time-consuming
                                 when you create more than a couple of dozen.

To enable unified messaging features for Unity Connection users, you add one or more unified messaging accounts for each user.
                                 For each unified messaging account, you specify a unified messaging service, which determines which unified messaging features
                                 the user can use.

For Google Workspace, 1400 unified messaging accounts are supported with a unified messaging service.

If you do not want all users to have access to all unified messaging features, you can create multiple unified messaging services
                                 that enable different features or different combinations of features.

You cannot create two unified messaging accounts that enable the same feature for the same user.

## Associating Exchange/Office 365 Email Addresses with Users

Unity Connection figures out who the sender and
                           		recipient are for Unity Connection voice messages that are sent using ViewMail
                           		for Outlook doing the following:

When you install Cisco Unity Connection ViewMail for Microsoft Outlook version 11.5 or later, you specify the Unity Connection
                                 server on which the user’s Unity Connection mailbox is stored. ViewMail for Outlook always sends new voice messages, forwards,
                                 and replies to that Unity Connection server.

When you configure single inbox for a user, you specify:

The user’s Exchange email address. This is how Unity Connection knows which Exchange/Office 365 mailbox to synchronize with.
                                       You can choose to have Unity Connection automatically create an SMTP proxy address for the user using the Corporate Email
                                       Address field in Unity Connection Administration.

An SMTP proxy address for the user, which is typically the
                                       				  user’s Exchange email address. When the user sends a voice message using
                                       				  ViewMail for Outlook, the From address is the sender’s Exchange email address,
                                       				  and the To address is the recipient’s Exchange email address. Unity Connection
                                       				  uses the SMTP proxy address to associate the From address with the Unity
                                       				  Connection user who sent the message and the To address with the Unity
                                       				  Connection user who is the intended recipient.

Integrating Unity Connection with Active Directory can simplify
                           		populating Unity Connection user data with Exchange email addresses. For more
                           		information, see the Active Directory Considerations for Single Inbox .

## Deploying Single Inbox

How you deploy single inbox depends on the Unity Connection configuration. See the applicable section:

### Deploying Single
                           	 Inbox for One Unity Connection Server

In a deployment that includes one Unity Connection server, the server connects with one or  few mail servers. For example,
                              you can configure a Unity Connection server to access mailboxes on an Exchange 2016 and Exchange Server 2019 server.

### Deploying Single Inbox for a Unity Connection Cluster

You deploy a Unity Connection cluster much the same way you deploy a Unity Connection server. Configuration data is replicated
                              between the two servers in the cluster, so you can change configuration settings on either server.

For Exchange/Office 365, the Unity Connection Mailbox Sync service, which is required for single inbox to function, runs only
                              on the active server and is considered a critical service. If you stop this service, the active server fails over to the secondary
                              server, and the Unity Connection Mailbox Sync service starts running on the new acting primary server.

For Google Workspace, the Unity Connection Google Workspace Sync service is required for single inbox to function. It  runs
                              only on the active server and is considered a critical service. If you stop this service, the active server fails over to
                              the secondary server, and the Unity Connection Google Workspace Sync service starts running on the new acting primary server.

If there are IP restrictions on the network, such as a firewall, consider the connectivity of both Unity Connection servers
                              to the supported mail servers.

### Deploying Single Inbox for a Unity Connection Intrasite Network

Unified messaging services are not replicated among Unity Connection servers in an intrasite network, so they must be configured
                              separately on each server in the network.

## Single Inbox Affecting Scalability

Single Inbox does not affect the number of user accounts that can be homed on a Unity Connection server.

Allowing Unity Connection or Exchange mailboxes larger than 2 GB can affect Unity Connection and Exchange performance.

## Network Considerations for Single Inbox

### Firewalls

If a Unity Connection server is separated by a firewall from Exchange servers, you must open the applicable ports in the firewall.
                              If a Unity Connection cluster is configured, you must open the same ports in the firewall for both Unity Connection servers.
                              For more information, see the “ IP Communications Required by Cisco Unity Connection ” chapter of the Security Guide for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html

### Bandwidth

For bandwidth requirements for single inbox, see the “ Unified Messaging Requirements: Synchronizing Unity Connection and Exchange Mailboxes ” section of System Requirements for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Latency

Latency is closely intertwined with the number of
                              		connections (also known as synchronization threads or threads) that Unity
                              		Connection uses to synchronize Unity Connection and Exchange mailboxes. In a
                              		low-latency environment, fewer connections are required; conversely, in a
                              		high-latency environment, more connections are required to keep up with the
                              		number of operations that need to be synchronized to Exchange.

If you do not have enough connections, users
                              		experience delays in synchronizing messages and in synchronizing message
                              		changes between Unity Connection and Exchange (for example, turning message
                              		waiting indicators off when the last voice message has been heard). However,
                              		configuring more connections is not necessarily better. In a low-latency
                              		environment, a busy Unity Connection server with a large number of connections
                              		to Exchange may significantly increase the processor load on the Exchange
                              		servers.

See the following sections for calculating the
                              		number of connections needed:

#### Calculating the Number of Connections for One Unity Connection
                              	 Server

If you have one Unity Connection server with 2,000 or fewer users, and if round-trip latency between the Unity Connection
                                 and Exchange servers is 80 milliseconds or less, do not change the number of connections unless you encounter synchronization
                                 delays. The default setting of four connections are sufficient in most environments to ensure good single-inbox synchronization
                                 performance.

If you have one Unity Connection server with more
                                 		than 2,000 users or more than 80 milliseconds of round-trip latency, use this
                                 		formula to calculate the number of connections:

Number of connections =
                                    		   (Number of Unity Connection single-inbox users * (latency in milliseconds +
                                    		  15) ) / 50,000

If you have more than one Exchange mailbox servers, the number of Unity Connection single-inbox users is the largest number
                                 of single-inbox users who are assigned to one mailbox server. For example, suppose your Unity Connection server has 4,000
                                 users and they are all single-inbox users. You have three Exchange mailbox servers, with 2,000 users on one mailbox server
                                 and 1,000 users on each of the other two mailbox servers. For this calculation, the number of Unity Connection single-inbox
                                 users is 2,000.

For example, if your Unity Connection server has 2,000 users and 10 milliseconds of latency, and all of the mailboxes are
                                 homed on one Exchange server, you would not change the number of connections:

Number of connections =
                                    		  (2,000 * (10 + 15)) / 50,000 = 50,000 / 50,000 = 1 connection  (no change to
                                    		  the default value of four connections)

If your Unity Connection server has 2,000 Office 365 single-inbox users and 185 milliseconds of latency, you should increase
                                 the number of connections to 8:

Number of connections = (2,000 * (185 + 15)) / 50,000 = 400,000 / 50,000 = 8 connections

#### Calculating the Number of Connections for a Unity Connection Cluster

If both Unity Connection servers in a cluster are in the same location, so they have the same latency when synchronizing with
                                 Exchange or Office 365, you can calculate the number of connections the same way you do for one Unity Connection server.

If one server in a cluster is collocated with the Exchange or Office 365 servers and the other is in a remote location:

Install the publisher server in the location with the Exchange or Office 365. The publisher server should always be the primary
                                       server unless the server is offline for maintenance or is unavailable for some other reason.

Calculate the number of connections for the publisher server, meaning the Unity Connection server with lower latency. If you
                                       calculate for the server with higher latency, during peak usage, synchronization may increase the processor load on the Exchange
                                       or Office 365 to unacceptable levels.

When the remote server becomes the active server, for example, because you are upgrading Unity Connection, you may encounter
                                 significant synchronization delays. When you calculate the number of connections for the Unity Connection server that is collocated
                                 with Exchange, you are optimizing for the server with lower latency. This number of connections may not be able to keep up
                                 with the number of operations that need to be synchronized to Exchange or Office 365. The maintenance operations that require
                                 activating the subscriber server should be performed during non-business hours and you should limit the amount of time that
                                 the subscriber server is the active server.

#### Calculating the Number of Connections for a Unity Connection Server Synchronizing with an Exchange CAS Array

Unity Connection is most likely to require a large number of connections with Exchange or Office 365 when connecting with
                                 a large CAS array. For example, when the Unity Connection server has 12,000 single-inbox users and the latency is 10 milliseconds,
                                 you would increase the number of connections to six:

Number of connections = (12,000 * (10 + 15)) / 50,000 = 300,000 / 50,000 = 6 connections

If your Exchange environment includes both a large CAS array and one or more Exchange or Office 365 servers that are not in
                                 the array, and if the calculated number of connections for the CAS array differs significantly from the number of connections
                                 for the individual Exchange or Office 365 servers, you may want to consider adding a Unity Connection server that is dedicated
                                 to the separate Exchange or Office 365 servers. Setting the number of connections to the lower value for the standalone Exchange
                                 or Office 365 server means synchronization delays for the CAS array, while setting the number of connections to the higher
                                 value for the CAS array means a higher processor load on the standalone Exchange or Office 365 servers.

#### Increasing the Number of Connections

If you have more than 2000 users on a Unity Connection server or more than 80 milliseconds of latency, you can increase the
                                 number of connections from the default value of four. Note the following:

The maximum number of connections is 64.

Never decrease the number of connections to fewer than four.

After you change the number of connections, you must restart the Unity Connection Mailbox Sync service in Cisco Unity Connection
                                       Serviceability for the change to take effect.

As Unity Connection is optimized in future versions, the optimum number of the connections for a specific environment may
                                       change.

If you have more than one Unity Connection server synchronizing with the same Exchange server or CAS array, you may increase
                                       the processor load on the Exchange CAS servers to unacceptable levels.

To increase the number of connections that Unity Connection uses for synchronizing with each Exchange server, run the following
                                 CLI command (when a Unity Connection cluster is configured, you can run the command on either server):

run cuc dbquery unitydirdb EXECUTE PROCEDURE csp_ConfigurationModifyLong (pFullName='System.Messaging.MbxSynch.MbxSynchThreadCountPerUMServer',
                                    pValue=< value >)

where < value > is the number of connections that you want Unity Connection to use.

To determine the current number of connections that Unity Connection is configured to use, run the following CLI command:

run cuc dbquery unitydirdb select fullname, value from vw_configuration where fullname = 'System.Messaging.MbxSynch.MbxSynchThreadCountPerUMServer'

### Load Balancing

By default, the Unity Connection Mailbox Sync
                              		service uses four threads (four HTTP or HTTPS connections) for each CAS server
                              		or CAS array that Unity Connection is configured to synchronize with. Note the
                              		following:

The threads are torn down and recreated every
                                    			 60 seconds.

All of the requests come from the same IP
                                    			 address. Configure the load balancer to distribute load from the same IP
                                    			 address to multiple servers in the CAS array.

Unity Connection does not maintain session
                                    			 cookies between requests.

If the load balancer for the existing CAS
                                    			 array does not produce the desired result with the load profile that the Unity
                                    			 Connection Mailbox Sync service puts on it, you can set up a dedicated CAS
                                    			 server or CAS array to handle the Unity Connection load.

## Microsoft Exchange Considerations for Single Inbox

### Unified Messaging
                           	 Services Account Accessing Exchange Mailboxes

Single inbox and the other unified messaging features require
                              		that you create an Active Directory account (called the unified messaging
                              		services account throughout the Unity Connection documentation) and grant the
                              		account the rights necessary for Unity Connection to perform operations on
                              		behalf of users. No user credentials are stored in the Unity Connection
                              		database; this is a change from Unity Connection 8.0, for which TTS access to
                              		Exchange email and access to Exchange calendars and contacts required that you
                              		enter each user’s Active Directory alias and password.

Using the unified messaging services account to access Exchange
                              		mailboxes simplifies administration. However, you must secure the account to
                              		prevent unauthorized access to Exchange mailboxes.

The operations that the account performs and the permissions that the account requires are documented in the “Configuring Unified Messaging” chapter in the Unified Messaging Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

### Deploying Exchange Servers

We tested single-inbox with Exchange using standard Exchange deployment practices, which are thoroughly documented on the
                              Microsoft website. If you are not following Microsoft deployment guidelines for Active Directory and Exchange, you should
                              enable single inbox gradually, for small groups of users, and closely monitor Active Directory and Exchange performance as
                              you add more single-inbox users.

### Mailbox-Size
                           	 Quotas and Message Aging

By default, when a user deletes a voice message in Unity
                              		Connection, the message is sent to the Unity Connection deleted items folder
                              		and synchronized with the Outlook Deleted Items folder. When the message is
                              		deleted from the Unity Connection deleted items folder (the user can do this
                              		manually, or you can configure message aging to do it automatically), it is
                              		also deleted from the Outlook Deleted Items folder.

If you are adding the single-inbox feature to an existing
                              		system, and if you have configured Unity Connection to permanently delete
                              		messages without saving them in the deleted items folder, messages that users
                              		delete using the Web Inbox or using the Unity Connection phone interface are
                              		still permanently deleted. However, messages that users delete using Outlook
                              		are only moved to the deleted items folder in Unity Connection, not permanently
                              		deleted. This is true regardless of which Outlook folder the message is in when
                              		the user deletes it. (Even when a user deletes a voice message from the Outlook
                              		Deleted Items folder, the message is only moved to the deleted items folder in
                              		Unity Connection.)

You should do one or both of the following to prevent the hard
                              		disk on the Unity Connection server from filling up with deleted messages:

Configure mailbox-size quotas, so that Unity Connection prompts
                                    			 users to delete messages when their mailboxes approach a specified size.

Configure message aging to permanently delete messages in the
                                    			 Unity Connection deleted items folder.

### Coordinating Mailbox-Size Quotas and Message Aging Settings in Unity
                           	 Connection and Exchange

You can configure mailbox-size quotas and message
                              		aging in Exchange just as you can in Unity Connection. When you are configuring
                              		single inbox, confirm that the mailbox-size quotas and message aging in the two
                              		applications do not conflict. For example, suppose that you configure Unity
                              		Connection to delete voice messages that are more than 14 days old, and you
                              		configure Exchange to delete messages that are more than 30 days old. A user
                              		who returns from a three-week vacation finds emails in the Outlook Inbox for
                              		the entire period but finds voice messages only for the last two weeks.

When you configure Unity Connection single inbox,
                              		you need to increase the mailbox-size quotas for the corresponding Exchange
                              		mailboxes. You should increase the quota for Exchange mailboxes by the size of
                              		the quota for Unity Connection mailboxes.

Exchange can be configured to tombstone or retain
                              		messages that have been permanently deleted; when single inbox is configured,
                              		this includes Unity Connection voice messages in Exchange mailboxes. Ensure
                              		that this is the desired outcome for voice messages based on your enterprise
                              		policies.

### Moving Exchange
                           	 Mailboxes

If you configure unified messaging services to access specific
                              		Exchange servers, Unity Connection can only detect mailbox moves between
                              		Exchange servers for some versions of Exchange. In configurations in which
                              		Unity Connection cannot detect mailbox moves, when you move Exchange mailboxes
                              		between Exchange servers, you need to add new unified messaging accounts for
                              		the affected users and delete the old unified messaging accounts.

For the affected versions of Exchange, if you frequently move
                              		mailboxes between Exchange servers for load balancing, You should configure
                              		unified messaging services to search for Exchange servers. This allows Unity
                              		Connection to automatically detect the new location of mailboxes that have been
                              		moved.

For information on which versions of Exchange are affected, see the “ Moving and Restoring Exchange Mailboxes ” chapter of the Unified Messaging Guide for Cisco Unity Connection , Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html

### Exchange
                           	 Clustering

Unity Connection supports using single inbox with Exchange 2016 or Exchange 2019 Database Availability Groups (DAG) for high
                              availability if the DAGs are deployed according to Microsoft recommendations. Unity Connection also supports connecting to
                              a CAS array for high availability.

For more information, see “ Unified Messaging Requirements: Synchronizing Unity Connection and Exchange Mailboxes ” section of System Requirements for Cisco Unity Connection, Release 15, at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Single Inbox Affecting Exchange Performance

Single inbox has a minor effect on Exchange performance in direct relationship to the number of users. For more information,
                              see the white paper at http://www.cisco.com/en/US/prod/collateral/voicesw/ps6789/ps5745/ps6509/solution_overview_c22-713352.html .

### Exchange Autodiscover Service

If you configure unified messaging services to search for Exchange servers, do not disable the Exchange autodiscover service,
                              or Unity Connection cannot find Exchange servers, and unified messaging features do not work. (The autodiscover service is
                              enabled by default.)

### Exchange Server 2016 and Exchange Server 2019

For information on Exchange Server, 2016 and 2019 requirements when single inbox is configured, see the “ Unified Messaging Requirements: Synchronizing Unity Connection and Exchange Mailboxes ” section of System Requirements for Cisco Unity Connection, Release 15, at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

When you are using Exchange 2016 or Exchange 2019 you need to:

Assign the application impersonation management role to the
                                    			 unified messaging services accounts.

Configure EWS limits for the unified messaging users.

## Google Workspace Considerations for Single Inbox

Unified Messaging Services Account Accessing Gmail Server

Single inbox and the other unified messaging features require that you create an Active Directory account (called the unified
                           messaging services account) and grant the account the rights necessary for Unity Connection to perform operations on behalf
                           of users. No user credentials are stored in the Unity Connection database

Using the unified messaging services account to access Gmail server simplifies administration. However, you must secure the
                           account to prevent unauthorized access to Gmail server.

For information on the operations that the account performs and the permissions that the account requires, see “ Configuring Unified Messaging ” chapter in the Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html

Deploying Google Workspace

To deply the Google Workspace in Unity Connection, you need to perform few steps on Google Cloud Platform (GCP) Console.

For detailed steps to deploy Google Workspace, see “ Configuring Unified Messaging ” chapter in the Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html

Mailbox-Size Quotas and Message Aging

To prevent the hard disk on the Unity Connection server from filling up with deleted messages, you should do the following:

Configure mailbox-size quotas, so that Unity Connection prompts users to delete messages when their mailboxes approach a specified
                                 size.

Configure message aging to permanently delete messages in the Unity Connection deleted items folder.

You can also configure mailbox-size quotas and message aging on Gmail server just as you can set in Unity Connection. When
                           you configure Unity Connection single inbox, you need to increase the mailbox-size quotas for the corresponding Gmail server.
                           You should increase the quota for Gmail server by the size of the quota for Unity Connection mailboxes.

## Active Directory
                        	 Considerations for Single Inbox

### For Exchange/Office 365

Note the following Active Directory considerations for Exchange/Office 365:

Unity Connection does not require that you extend the Active Directory schema for single inbox.

If the Active Directory forest includes more than ten domain controllers, and if you have configured Unity Connection to search
                                    for Exchange servers, you should deploy sites in Microsoft Sites and Services and that you follow Microsoft guidelines for
                                    geospatially separating domain controllers and global catalog servers.

A Unity Connection server can access Exchange servers in more than one forest. You must create one or more unified messaging
                                    services for each forest.

You can configure an LDAP integration with Active Directory for data synchronization and for authentication, although it is
                                    not required for single inbox or for any of the other unified messaging features.

If you have already configured an LDAP integration, you are not required to change the LDAP integration to use single inbox.
                              However, if you synchronized the Cisco Unified Communications Manager Mail ID field with the LDAP sAMAccountName instead of
                              with the LDAP mail field, you may want to change the LDAP integration. During the integration process, this causes values
                              in the LDAP mail field to appear in the Corporate Email Address field in Unity Connection.

Unified messaging requires that you enter the Exchange email address for each Unity Connection user. On the Unified Messaging
                              Account page, each user can be configured to use either of the following values:

The Corporate Email Address specified on the User Basics page

The email address specified on the Unified Messaging Account page

Automatically populating the Corporate Email Address field with the value of the LDAP mail field is easier than populating
                              the email address field on the Unified Messaging Account page using Unity Connection Administration or the Bulk Administration
                              Tool. With a value in the Corporate Email Address field, you can also easily add an SMTP proxy address, which is required
                              for single inbox; see the “Associating Exchange Email Addresses with Users” section.

For information on how to change LDAP directory configurations, see the “ LDAP ” chapter of the System Administration Guide for Cisco Unity Connection , Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

### For Google Workspace

Note the following Active Directory considerations for Google Workspace:

Unity Connection does not require that you extend the Active Directory schema for single inbox.

You can configure an LDAP integration with Active Directory for data synchronization and for authentication, although it is
                                    not required for single inbox or for any of the other unified messaging features.

If you have already configured an LDAP integration, you are not required to change the LDAP integration to use single inbox.
                              However, if you synchronized the Cisco Unified Communications Manager Mail ID field with the LDAP sAMAccountName instead of
                              with the LDAP mail field, you may want to change the LDAP integration. During the integration process, this causes values
                              in the LDAP mail field to appear in the Corporate Email Address field in Unity Connection.

Unified messaging requires that you enter the Gmail account address for each Unity Connection user. On the Unified Messaging
                              Account page, each user can be configured to use either of the following values:

The Corporate Email Address specified on the User Basics page

The email address specified on the Unified Messaging Account page

Automatically populating the Corporate Email Address field with the value of the LDAP mail field is easier than populating
                              the email address field on the Unified Messaging Account page using Unity Connection Administration or the Bulk Administration
                              Tool. With a value in the Corporate Email Address field, you can also easily add an SMTP proxy address, which is required
                              for single inbox.

For information on how to change LDAP directory configurations, see the “ LDAP ” chapter of the System Administration Guide for Cisco Unity Connection , Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html

## Using Secure Messaging with Single Inbox

If you do not want Unity Connection voice messages stored in supported mail servers or archived for discoverability or compliance
                           reasons but you still want single-inbox functionality, you can configure secure messaging. Enabling secure messaging for selected
                           users or for all users on a Unity Connection server prevents the recorded part of voice messages from being synchronized with
                           the mail servers configured for those users.

### Secure Messaging with Exchange/Office 365

For Exchange/Office 365, Unity Connection sends a decoy message that tells users they have a voice message. If Cisco Unity
                              Connection ViewMail for Microsoft Outlook is installed, the message is streamed directly from Unity Connection. If ViewMail
                              for Outlook is not installed, the decoy message contains only an explanation of secure messages.

### Secure Messaging with Google Workspace

For Google Workspace, secure message is not synchronized with Gmail server. Instead, Unity Connection sends a text message
                              to Gmail account of a user. The text message indicates that the user can access secure message through Telephony User Interface
                              (TUI) of Unity Connection.

The user get the "This message has been marked secure. Log on to Connection by phone to retrieve the message." text message
                              on the Gmail account.

## Client Access to Voice Messages in Exchange Mailboxes

You can use the following client applications to access Unity Connection voice messages in Exchange mailboxes:

### Cisco Unity
                           	 Connection ViewMail for Microsoft Outlook

When single inbox is configured, users have the best experience when they are using Microsoft Outlook for their email application
                              and when Cisco Unity Connection ViewMail for Microsoft Outlook version 8.5 or later is installed. ViewMail for Outlook is
                              an add-in that allows voice messages to be heard and composed from within Microsoft Outlook 2016.

Versions of ViewMail for Outlook prior to 8.5 are not able to
                              		access voice messages that are synchronized into Exchange by the single inbox
                              		feature.

You can simplify the deployment of ViewMail for Outlook using
                              		mass-deployment technologies that use MSI packages. For information on
                              		customizing ViewMail for Outlook–specific settings, see the “Customizing
                              		ViewMail for Outlook Setup” section in the Release Notes for Cisco Unity
                              		Connection ViewMail for Microsoft Outlook Release 8.5(3) or
                              		later at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

When you enable single inbox (SIB) using unified messaging
                              		service, a new Voice Outbox folder appears under the Outbox folder in Outlook.
                              		Unity Connection creates this folder in Exchange and uses it to deliver voice
                              		messages to Unity Connection; this allows Unity Connection and ViewMail for
                              		Outlook to monitor a separate folder for delivery of voice messages.

For more information about ViewMail for Outlook, see:

Quick Start Guide for Cisco ViewMail for Microsoft Outlook
                                       				(Release 8.5 and Later) at http://www.cisco.com/en/US/docs/voice_ip_comm/connection/vmo/quick_start/guide/85xcucqsgvmo.html .

Release Notes for Cisco Unity Connection ViewMail for Microsoft
                                    			 Outlook Release 8.5(3) or later at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

### Web Inbox

The Unity Connection Web Inbox is a web application that allows
                              		users to hear and compose Unity Connection voice messages from any computer or
                              		device that has internet access to Unity Connection. Note the following:

Web Inbox can be embedded into other applications as a gadget.

For playback, Web Inbox uses HTML 5 for audio playback when .wav
                                    			 playback is available. Otherwise, it uses QuickTime.

Cisco Unity Connection uses Web Real-Time Communication(Web RTC) to record voice messages using HTML5 in Web Inbox. Web RTC provides web browsers and mobile applications with real-time communication (RTC) via simple application
                                    programming interfaces (APIs).

TRaP, or playback from a telephone integrated with a telephony integration can be used for playback or recording.

New message notifications or events come through via Unity
                                    			 Connection.

Web Inbox is hosted in the Tomcat application on Unity Connection.

By default, when the Web Inbox session is idle for longer than the 30 minutes, Cisco Unity Connection disconnects the Web
                                    Inbox session. To configure the session timeout settings perform the following steps :

In Cisco Unity Connection Administration, expand System Settings and select Advanced.

In the Advanced Settings select PCA . Configure Cisco PCA session timeout to desired value and select Save.

For more information on Web Inbox, see Quick Start Guide for Cisco Unity Connection Web Inbox at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/quick_start/guide/b_15cucqsgminiinbox.html .

### Blackberry and Other Mobile Applications

Note the following about using mobile clients to access Unity Connection voice messages:

Mobile clients such as Blackberry devices are supported with single inbox.

Clients that use Active Sync technology and can playback encoded .wav files are supported with single inbox. The encoding
                                    need to be known, because some codecs are not supported across all mobile devices.

Cisco Mobility applications can be used to check voice mail directly in Unity Connection as in previous releases. However,
                                    these applications currently are not supported with single inbox.

Mobile users can only compose voice messages if they have a Cisco Mobility application or if they call into the Unity Connection
                                    server.

### IMAP Email Clients and Other Email Clients

If users use IMAP email clients or other email clients to access Unity Connection voice messages that have been synchronize
                              to Exchange by the single-inbox feature, note the following:

Unity Connection voice messages appear in the inbox as emails with .wav file attachments.

To compose voice messages, users must either call into Unity Connection or use a recording device and an application that
                                    can produce .wav files.

Replies to voice messages are not synchronized into the recipient’s Exchange mailbox.

### Restoring Exchange
                           	 Mailboxes with Single Inbox

If you need
                              		to restore one or more Exchange mailboxes, you must disable single inbox for
                              		the Unity Connection users whose mailboxes are being restored.

Caution

For more information, see the “ Moving and Restoring Exchange Mailboxes ” chapter of the Unified Messaging Guide for Cisco Unity Connection , Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

## Client Access to Voice Messages for Google Workspace

If you have configured unified messaging with Google Workspace, a user can access the voice messages on the Gmail account.
                           All Unity Connection voice messages that are sent to the user, are first stored in the Unity Connection and then synchronized
                           to the Gmail server with label VoiceMessages. It creates a folder "VoiceMessages" on the Gmail account of the user. All the
                           voice messages sent for the user, are stored in the VoiveMessages folder.

In case server connectivity is down or some temporary error occurs, then two retries are allowed to send the message. This
                           is also applicable for multiple recipients (Multiple To, Multiple CC and Multiple BCC).

## Cisco Voicemail for Gmail

Cisco Voicemail for Gmail provides a visual interface for an enriched experience with voicemails at Gmail. With this extension, user can perform the
                           following :

Compose a voicemail from within Gmail.

Play the received voicemail without the need of any external player.

Compose a voicemail in reply-to a received message.

Compose a voicemail while forwarding a received message.

For more information, see the Cisco Voicemail for Gmail section of the "Introduction to Unified Messaging" chapter of the Unified Messaging Guide for Cisco Unity Connection Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html .

| Note | When migrating from EWS to Microsoft Graph API-based integration for Office 365 during the upgrade to Cisco Unity Connection
                                       15SU4 or later releases, the Unified Messaging Service (UMS) may require up to 4 hours to achieve full stability and operational
                                       readiness. |
|---|---|

| Note | For Google Workspace, 1400 unified messaging accounts are supported with a unified messaging service. |
|---|---|

| Note | For better user experience, the round trip latency
                                       		between Unity Connection and Office 365 server should not be more than 250 ms. |
|---|---|

| Note | The maximum number of connections is 64. Never reduce the
                                          		number of connections to fewer than four. |
|---|---|

| Note | This formula is based on conservative assumptions about
                                          		user activity, and about Unity Connection and Exchange or Office 365
                                          		performance, but the assumptions may not be true in all environments. For
                                          		example, if you are experiencing single-inbox synchronization delays after
                                          		setting the number of connections to the calculated value, and if the Exchange
                                          		servers have available CPU, you may want to increase the number of connections
                                          		beyond the calculated value. |
|---|---|

| Note | Cisco Unity Connection is not responsible for
                                             			 troubleshooting the load balancer issues as it is an external third party
                                             			 software. For further assistance, please contact the Load Balancer support
                                             			 team. |
|---|---|

| Note | Beginning with Cisco Unity Connection 10.0(1) and later releases, when the mailbox size of a user starts reaching its specified
                                             threshold limit on Unity Connection, the user receives a quota notification message. For more information on mailbox quota
                                             alert text, see the “ Controlling the Size of Mailboxes "  section of the “Message Storage” chapter of the System Administration Guide for Cisco Unity Connection, Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Note | By default, Unity Connection allows outside callers to
                                       		leave voice messages regardless of the mailbox-size quota for recipient
                                       		mailboxes. You can change this setting when you configure system-wide quota
                                       		settings. |
|---|---|

| Note | When
                                       		you move an email message from any Outlook folder to the Voicemail Outbox
                                       		folder, the email message is moved to the Deleted Items folder. The user may
                                       		retrieve that deleted email message from the Deleted Items folder. |
|---|---|

| Note | Web Inbox supports both the IPv4 and IPv6 addresses. However, the IPv6 address works only when Connection platform is configured
                                             in Dual (IPv4/IPv6) mode. |
|---|---|

| Caution | If
                                       		you do not disable single inbox for Unity Connection users whose Exchange
                                       		mailboxes are being restored, Unity Connection do not resynchronize voice
                                       		messages that were received between the time that the backup from which you are
                                       		restoring was created and the time that the restore is complete. |
|---|---|