---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-networking-guide-b-15cucnetx-b-15cucnetx-chapter-00-html-9087800c0b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx/b_15cucnetx_chapter_00.html
retrieved_at: 2026-08-17T03:32:42.102839+00:00
---

Networking Guide for Cisco Unity Connection Release 15

# Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Overview of Networking Concepts

## Chapter: Overview of Networking Concepts

# Overview of Networking Concepts

## Overview of Networking Concepts

### Overview

Each Cisco Unity Connection server or cluster has a maximum
                              		number of users that it can serve. When the messaging needs of your
                              		organization require more than one Unity Connection server or cluster, or
                              		combine multiple Unity Connection directories or internetwork Unity Connection
                              		with Cisco Unity, you need a way to form a Cisco voicemail organization.

A Cisco voicemail organization can be formed when you link Unity
                              		Connection servers or clusters together to form sites, and link a Unity
                              		Connection site with another Unity Connection site or with a Cisco Unity site.

### About Unity
                           	 Connection Sites and Intrasite Links

You can join two or more Unity Connection servers or clusters (up to a maximum of ten) to form a well connected network, referred
                              to as a Unity Connection site. The servers joined to the site are referred to as locations. (When a Unity Connection cluster
                              is configured, the cluster counts as one location in the site.) Within a site, each location uses SMTP to exchange directory
                              synchronization information and messages directly with every other location. Each location is said to be linked to every other
                              location in the site via an intrasite link. Figure 1 illustrates a site of five Unity Connection locations joined by intrasite links.

The Unity Connection site concept was known as a Digital Network in Unity Connection release 7.x. You can join 7.x locations
                              and 8.x locations in the same Unity Connection site (intrasite links), as long as you do not link the site to any other site
                              (intersite links require that each Unity Connection location be at release 15).

Each Unity Connection server or cluster is represented in the
                              		site as a single Unity Connection location, which is created locally during
                              		installation and cannot be deleted from the server itself. When you join the
                              		server (or cluster) to an existing location in a site, a Unity Connection
                              		location is automatically created for the server (or cluster) on all other
                              		locations in the site and these locations begin to perform directory
                              		synchronization with the new location. A Unity Connection location can only
                              		belong to a single site.

### About Cisco
                           	 Voicemail Organizations and Intersite Links

You can use an intersite link to connect one Unity Connection
                              		site to another Unity Connection site, allowing you to scale your organization
                              		from ten locations to a maximum of 20. You can also use an intersite link to
                              		connect a Unity Connection server or site to a Cisco Unity server or
                              		Cisco Unity digital network. The linked sites are referred to as a Cisco
                              		voicemail organization.

To create an intersite link, you select a single location from
                              		each site to act as a gateway to the other site. All directory synchronization
                              		communications pass between the two site gateways, thereby limiting the
                              		connectivity requirements and bandwidth usage to the link between those two
                              		site gateway locations.

Only one intersite link is supported per site. So, you can link
                              		a single Unity Connection site to a single Cisco Unity site, or a single Unity
                              		Connection site to another Unity Connection site.

#### About Linking Two
                              	 Unity Connection Sites

When you link two Unity Connection sites with an intersite link,
                                 		the gateway for each site is responsible for collecting information about all
                                 		changes to the local site directory, and for polling the remote site gateway
                                 		periodically to obtain information about updates to the remote site directory.
                                 		The gateways use the HTTP or HTTPS protocol to exchange directory
                                 		synchronization updates.

Each site gateway is also responsible for transmitting messages
                                 		that are addressed to recipients at the remote site and for receiving messages
                                 		that are addressed to recipients in its own site. Intersite messages are
                                 		transmitted and received using SMTP.

When you use a Unity Connection cluster as a site gateway, only
                                 		the publisher server in the cluster participates in directory synchronization
                                 		over the intersite link. However, the subscriber server continues to provide
                                 		message exchange over the intersite link if the publisher server is down.

Figure 2 illustrates the role of the site gateways and the intersite link in connecting
                                 		two Unity Connection sites.

### About VPIM
                           	 Networking

Unity Connection supports the
                              		Voice Profile for Internet Mail (VPIM) protocol, which is an industry standard
                              		that allows different voice messaging systems to exchange voice and text
                              		messages over the Internet or any TCP/IP network. VPIM is based on the Simple
                              		Mail Transfer Protocol (SMTP) and the Multi-Purpose Internet Mail Extension
                              		(MIME) protocol.

Unity Connection 15 supports up to 10 VPIM locations and 100,000 VPIM contacts in the Unity Connection directory. These same
                              limits apply either to the directory of a single Unity Connection server or cluster pair, or to the global directory in a
                              site.

If you deploy VPIM in a Unity Connection networking site, you
                              		should designate a single Unity Connection location in the site as the
                              		bridgehead to handle the configuration of VPIM locations and contacts. The VPIM
                              		location data and all contacts at the VPIM location (including automatically
                              		created contacts) are replicated from the bridgehead to other locations within
                              		the site. When a VPIM message is sent by a user who is homed on a Unity
                              		Connection location other than the bridgehead, the message first passes to the
                              		bridgehead, which handles forwarding the message to the destination server.
                              		Likewise, messages from VPIM contacts are received by the bridgehead and
                              		relayed to the home server of the Unity Connection recipient.

If you deploy VPIM in a Cisco Voicemail Organization, you must
                              		independently configure each site for VPIM. VPIM locations and contacts are not
                              		replicated across intersite links, and site gateways do not relay VPIM messages
                              		to other sites.

For detailed information about VPIM networking, see the “VPIM Networking” chapter.

### Directory
                           	 Synchronization

Each location in a Unity Connection site or Cisco Voicemail
                              		Organization has its own directory of users and other objects that were created
                              		on the location and are said to be “homed” on that location. The collection of
                              		objects and object properties that are replicated among locations and sites is
                              		referred to as the global directory.

See the following sections for details on the specific objects
                              		and object properties that are replicated during directory synchronization:

Replication
                                       				Within a Unity Connection Site

Replication
                                       				Between Two Unity Connection Sites

#### Replication Within
                              	 a Unity Connection Site

Within a Unity Connection site, each location replicates the
                                    		  objects and object properties shown in Table 1 from its directory to every other location:

Replicated Object

Replicated Properties

Users with mailboxes

Alias

First name, last name, display name, alternate names

Extension, cross-server transfer extension, and alternate
                                                      						  extensions

Directory listing status

Partition

Recorded name

SMTP address and SMTP proxy addresses

System contacts

All properties

System distribution lists

All properties, including list membership

Partitions

All properties

Search spaces

All properties, including membership

Unity Connection location

Display name

Host address

SMTP domain name

Unity Connection version

VPIM location

All properties except Contact Creation settings (contact
                                                					 creation is handled on the Unity Connection location that homes the VPIM
                                                					 location)

In most cases, you can use replicated objects just as you would
                                    		  use local objects; for example, you can assign a remote user to be the message
                                    		  recipient of a system call handler, or configure the search scope of a user to
                                    		  use a remote search space. Note the following exceptions:

System call handler owners must be local users.

Objects that belong to a partition (users, contacts, handlers,
                                          				system distribution lists, and VPIM locations) can only belong to local
                                          				partitions. You can, however, add a remote partition to a local search space.

When a replicated object that is homed on a Unity Connection
                                    		  location is added, modified or deleted, the location sends an object change
                                    		  request containing details about the change to all other locations. The object
                                    		  change requests for a given location are ordered and tracked with a number
                                    		  known as the Unique Sequence Number (USN). For each change, the location
                                    		  increments the USN by one, and notes the change in its database. When a remote
                                    		  location receives an object change request with a USN value that is one higher
                                    		  than the previous request it received from the sender, it updates its copy of
                                    		  the Unity Connection directory accordingly, and increments its tracked copy of
                                    		  the USN for the sender. If a remote location misses one or more changes and
                                    		  receives a change request with a USN that is more than one higher than the
                                    		  previous request it received from this location, it can retrieve the missed
                                    		  changes by requesting the USN values that it missed.

In addition to the USN, each location has another associated
                                    		  number known as the Replication Set. The Replication Set value is used to track
                                    		  the set of changes to which a USN belongs. The Replication Set value is
                                    		  automatically changed during an upgrade, restore, or rollback operation. This
                                    		  ensures that any changes to the database as a result of the operation are
                                    		  replicated to the network. For example, if Location A receives a message with
                                    		  replication set 10 and USN 5 from Location B, and then receives a message with
                                    		  replication set 9and USN 5 from Location B, it knows to ignore the message with
                                    		  replication set 9 because it is a lower number and the message predates the
                                    		  message with replication set 10. If Location A receives another message from
                                    		  Location B with replication set 10 and USN 5 again, Location A knows this is a
                                    		  duplicate message and can ignore it.

When a bulk operation is in progress on a location, replication
                                    		  is paused on that location until the operation completes.

#### Replication
                              	 Between Two Unity Connection Sites

As shown in Table 2 ,
                                    		  the same objects and object properties are replicated between two Unity
                                    		  Connection sites as within a single Unity Connection site, with the following
                                    		  exceptions:

System contacts are not replicated between sites.

For each site, you can select whether to synchronize all system
                                          				distribution lists that are homed on the remote site. Also, for each individual
                                          				list, you can select whether the list is offered for replication to the remote
                                          				site.

System distribution list membership is not replicated between
                                          				sites.

VPIM locations (and contacts) are not replicated between sites.

Replicated Object

Replicated Properties

Users with mailboxes

Alias

First name, last name, display name, alternate names

Extension, cross-server transfer extension, and alternate
                                                            						  extensions

Directory listing status

Partition

Recorded name 1

SMTP address and SMTP proxy addresses

System distribution lists 2

Alias

Display name

Extension

Partition

Recorded name 1

Partitions

All properties

Search spaces

All properties

Unity Connection locations

Display name

Host address

SMTP domain name

Unity Connection version

Just as with intrasite links, you can use replicated objects
                                    		  from a remote site just as you would use local objects, except that call
                                    		  handler owners must be local users, and objects that belong to a partition can
                                    		  only belong to local partitions.

Intersite replication is accomplished by means of a Feeder
                                    		  service and a Reader service running on each site gateway. The Reader service
                                    		  periodically polls the remote site gateway for any directory changes since the
                                    		  last poll interval. The Feeder service checks the change tracking database for
                                    		  directory changes and responds to poll requests with the necessary information.

On each site gateway, you can configure the schedule on which
                                    		  the Reader polls the remote Feeder for directory data, and the schedule on
                                    		  which it polls for recorded names. In Cisco Unity Connection Administration on
                                    		  a site gateway, you can access the schedules on the Tools > Task Management
                                    		  page selecting either the Synchronize Directory With Remote Network task or the
                                    		  Synchronize Voice Names With Remote Network task. Alternatively, you can access
                                    		  either task using the Related Links field on the Edit Intersite Link page.

When the Synchronize Voice Names With Remote Network task is
                                    		  enabled, the reader process recorded name files for remote users and system
                                    		  distribution lists (if applicable). Once a recorded name is created for a
                                    		  remote object on the local site, it is updated only if the remote and local
                                    		  filenames for the recorded name differ. If, for example, you change the
                                    		  outgoing codec for recorded names on the remote site gateway, the local site
                                    		  does not update its files because the change does not affect filenames. In
                                    		  order to pull updated copies of recorded names in this case, you must clear all
                                    		  existing recorded names from the local site gateway and then do a full
                                    		  resynchronization using the Clear Recorded Names button and the Resync All
                                    		  button on the Search Intersite Links page in Unity
                                    		  Connection Administration.Replication Between Cisco Unity and Unity Connection
                                    		  Sites

When you link a Cisco Unity site and a Unity Connection site, a
                                    		  contact (known as a Unity Connection Networking subscriber in the Cisco Unity
                                    		  Administrator) is added to the Cisco Unity directory and to Active Directory
                                    		  for each Unity Connection user. Likewise, a user (known as a Cisco Unity user
                                    		  in Cisco Unity Connection Administration) is added to the Unity Connection site
                                    		  global directory for each Cisco Unity user. Unity Connection system contacts
                                    		  and VPIM contacts are not replicated to Cisco Unity, nor are Cisco Unity
                                    		  networking contacts (AMIS, Bridge, VPIM, Internet, or Trusted Internet
                                    		  subscribers) replicated to Unity Connection.

A system distribution list may be replicated from one site to
                                    		  another if the local site is configured to pull lists from the remote site, and
                                    		  if the list itself is configured to allow replication to other sites. Lists
                                    		  that contain system contacts or networking contacts cannot be configured to
                                    		  allow replication to other sites. For those lists that are replicated, only the
                                    		  list name and other information used in addressing are replicated; list
                                    		  membership is not replicated.

Table 3 lists the objects that are replicated between Cisco Unity and Unity Connection
                                    		  sites, and the object properties that are replicated.

Replicated Object

Replicated Properties

Unity Connection users with mailboxes

Alias

First name, last name,
                                                      						  display name, alternate names

Extension, cross-server
                                                      						  transfer extension, and alternate extensions 3

Directory listing status

Recorded name 4

SMTP address and SMTP
                                                      						  proxy addresses

Cisco Unity users

Alias

First name, last name,
                                                      						  display name, alternate names

Extension, transfer
                                                      						  extension, and alternate extensions

Directory listing status

Recorded name 4

System distribution lists 5

Alias

Display name

Extension 3

Recorded name 4

Locations

Display name

Host address

SMTP domain name

Intersite replication is accomplished by means of a Feeder
                                    		  service and a Reader service running on each site gateway. The Reader service
                                    		  periodically polls the remote site gateway for any directory changes since the
                                    		  last poll interval. The Feeder service checks the change tracking database for
                                    		  directory changes and responds to poll requests with the necessary information.

On the Unity Connection site gateway, you can configure the
                                    		  schedule on which the Reader polls the remote Feeder for directory data, and
                                    		  the schedule on which it polls for recorded names. In Cisco Unity Connection
                                    		  Administration on a site gateway, you can access the schedules on the
                                    		  Tools > Task Management page selecting either the Synchronize Directory With
                                    		  Remote Network task or the Synchronize Voice Names With Remote Network task.
                                    		  Alternatively, you can access either task using the Related Links field on the
                                    		  Edit Intersite Link page.

On the Cisco Unity site gateway, you can enable or disable
                                    		  synchronization of recorded names, and configure the interval at which the
                                    		  Reader polls the Unity Connection Feeder for directory updates and recorded
                                    		  names. Note that unlike the Unity Connection Reader, which has separate
                                    		  configurable schedules for polling directory data and recorded names, the
                                    		  Cisco Unity Reader polls for both (if recorded name synchronization is enabled)
                                    		  during each cycle.

When the Synchronize Voice Names With Remote Network task is
                                    		  enabled, the Reader processes the recorded name files for remote users and
                                    		  system distribution lists (if applicable). When a recorded name has been
                                    		  created for a remote object on the local site, it is updated only if the remote
                                    		  and local filenames for the recorded name differ. If, for example, you change
                                    		  the outgoing codec for recorded names on the remote site gateway, the local
                                    		  site does not update its files because the change does not affect filenames. In
                                    		  order to pull updated copies of recorded names from Cisco Unity to Unity
                                    		  Connection, you must clear all existing recorded names from the Unity
                                    		  Connection site gateway using the Clear Recorded Names button on the
                                    		  Networking > Links > Search Intersite Links page in Unity
                                    		  Connection Administration. In order to pull updated copies of recorded names
                                    		  from Unity Connection to Cisco Unity, use the Clear Voice Names button on the
                                    		  Network > Unity Connection Networking Profile page in the Cisco Unity
                                    		  Administrator.

### Directory Size
                           	 Limits

The Unity Connection global directory (the entire collection of local and replicated objects) is subject to certain size limits.
                              The same limits apply both to a single Unity Connection site or to a Cisco Voicemail Organization of linked sites (regardless
                              of whether a Unity Connection site is linked to another Unity Connection site or to a Cisco Unity site). In a Cisco Voicemail
                              Organization, exceeding the limits affects the ability to link sites together, and to replicate additional directory objects
                              across the intersite link when the sites have been linked. In Unity Connection 15, there are separate limits on the number
                              of users and contacts and on the number of system distribution lists.

The size limits at the time of Unity Connection 15 are:

A combined total of 100,000 users and system contacts (both
                                    			 contacts associated with a VPIM location and those not associated with a
                                    			 location)

100,000 system distribution lists

25,000 users per system distribution list

1.5 million total list members across all system distribution
                                          				  lists

20 levels of nesting (where one system distribution list is
                                          				  included as a member of another list)

When you attempt to link a Unity Connection site to another
                              		Unity Connection site or to a Cisco Unity site, both the user and system
                              		contact limit and the system distribution list limit are checked by the Unity
                              		Connection site gateway. If the combined number of users and contacts on the
                              		gateway after the link is created would exceed the user and contact limit, or
                              		the combined number of system distribution lists on the gateway would exceed
                              		the list limit, you cannot link the sites. (Note that the global directory
                              		sizes of two sites do not necessarily match after they are linked because
                              		contacts are not replicated across the intersite link. However, each Unity
                              		Connection site is still subject to the maximum size limits, which include
                              		system contacts.)

Consider the following example of the user and system contact
                              		limit check. Unity Connection site A has 40,000 users and 5,000 system
                              		contacts, and Unity Connection site B has 50,000 users and 15,000 contacts. If
                              		you linked these sites together, the global directory on Unity Connection site
                              		A would have 95,000 user and contact objects (40,000 plus 5,000 plus 50,000).
                              		However, the global directory on Unity Connection site B would have a total of
                              		105,000 user and contact objects (50,000 plus 15,000 plus 40,000). Attempting
                              		to join these two sites would fail because the user and contact limit is
                              		exceeded on site B. However, attempting to join Unity Connection site A with a
                              		Cisco Unity site that has 50,000 users and 15,000 networking contacts would
                              		succeed, because the Unity Connection site global directory of 95,000 user and
                              		contact objects would not exceed the 100,000 user and system contact limit.

In addition to checking the limits at the time two sites are
                              		joined, each Unity Connection site gateway also checks the user and system
                              		contacts limit and the system distribution lists limit each time the Reader
                              		service runs. If the limits have been exceeded by five percent or more, the
                              		Reader service is no longer able to create new directory objects for remote
                              		site objects. It continues to make changes to existing objects or delete them
                              		if they are removed from the remote site. This state is therefore known as
                              		“delete mode.” In order to get the Reader out of delete mode, you must remove a
                              		sufficient quantity of objects of the appropriate type to get to less than five
                              		percent above the limit (for example, remove remote users, local users, or
                              		local system contacts if the user and system contact limit has been exceeded,
                              		or remove local or remote system distribution lists if the system distribution
                              		list limit has been exceeded.)

### Messaging

See the following sections for details on how messaging is handled in specific networking situations:

#### How Messages to
                              	 System Distribution Lists are Handled Within a Unity Connection Site

Because system distribution lists
                                 		are replicated among locations in a Unity Connection site, a user can address
                                 		messages to any system distribution list at any location, as long as the list
                                 		is reachable in the user search scope.

When a user addresses a message to a system
                                 		distribution list, the local Unity Connection location parses the distribution
                                 		list membership. The sending location delivers the message directly to local
                                 		users on the list. If there are remote Unity Connection users on the list, the
                                 		sending location delivers the message to each location that homes these remote
                                 		users. If there are VPIM users on the list, the sending server either delivers
                                 		the message to the VPIM destination if the VPIM location is homed locally, or
                                 		passes it to the server on which the location is homed and that server handles
                                 		forwarding the message to the destination server.

Unity Connection includes the following predefined
                                 		system distribution lists: All Voicemail Users, Undeliverable Messages, and All
                                 		Voicemail-Enabled Contacts. Each Unity Connection server in your organization
                                 		has a distinct version of each of these lists. If you have not changed the
                                 		names of these lists to be unique, during initial replication each server
                                 		automatically adds the remote server name to the display name of any remote
                                 		lists whose names overlap with local list names.

By default, the predefined lists on each Unity
                                 		Connection location have the same recorded name, and the All Voicemail Users
                                 		and All Voicemail-Enabled Contacts lists have the same extension at each
                                 		location (the Undeliverable Messages list by default is not assigned an
                                 		extension, because users do not typically address messages to this list). When
                                 		setting up a Unity Connection site, you should consider modifying the recorded
                                 		name of each All Voicemail Users list and each All Voicemail-Enabled Contacts
                                 		list; if you do not, users can hear a confusing list of choices when they
                                 		address messages by name to one of these lists. When users address by extension
                                 		to a list whose extension overlaps that of another list, they reach the first
                                 		list that is located when Unity Connection searches the partitions of the user
                                 		search space in order.

Tip

#### How Messages to System Distribution Lists are Handled Between Sites

With intersite networking (either between Unity Connection sites or between Cisco Unity and Unity Connection sites), replication
                                 of system distribution lists is optional, and when lists are replicated, only the information needed to address a message
                                 to the list is replicated. Therefore, when a user addresses a message to a system distribution list that is homed in another
                                 site, the message is routed to the remote site gateway (if the remote site is a Unity Connection site) or to the Interoperability
                                 Gateway for Microsoft Exchange (if the remote site is a Cisco Unity site). At this point, the system distribution list recipient
                                 is handled as though the message originated within the remote site.

It is possible to nest system distribution lists such that a local list contains remote lists as members. For example, you
                                 could nest the All Voicemail Users distribution list from one site within the All Voicemail Users list of the other site.
                                 (If you are networking Cisco Unity with Unity Connection, note that Unity Connection users may be automatically created as
                                 members of the All Subscribers list or other lists depending on the template that you specify when creating the intersite
                                 link.) When you nest a remote list as a member of a local list, you should follow the given practices:

Avoid nesting local lists as members of the remote list.

Do not allow the local list to replicate to the remote site.

### Cross-Server
                           	 Sign-In, Transfers, and Live Reply

In order to limit
                                 		  replication traffic and keep the directory size manageable, only a subset of
                                 		  user information is replicated from the home location of the user to other
                                 		  locations. For this reason, only the user home location has information about
                                 		  call transfer settings, greetings, and other specific details for the user. In
                                 		  order for a location to properly handle calls destined for a user on a
                                 		  different location, the location that receives the call must hand off the call
                                 		  to the home location of the user. The purpose of the cross-server features is
                                 		  to make the user experience in a networked environment almost the same as in a
                                 		  single server environment, as shown in Table 4 .

Feature

Description

Cross-server sign-in

Cross-server sign-in allows administrators to provide users who
                                             					 are homed on different locations with one phone number that they can call to
                                             					 sign in. When calling from outside the organization, users—no matter which is
                                             					 their home server—call the same number and are transferred to the applicable
                                             					 home server to sign in.

Cross-server transfer

Cross-server transfer enables calls from the automated attendant
                                             					 or from a directory handler of one server to be transferred to a user on
                                             					 another server, according to the call transfer and screening settings of the
                                             					 called user.

Cross-server live reply

Cross-server live reply allows users who listen to their
                                             					 messages by phone to reply to a message from a user on another server by
                                             					 calling the user (according to the call transfer and screening settings of the
                                             					 called user).

The cross-server features can be enabled both within a site and
                                 		  across the entire Cisco voicemail organization. For more information and
                                 		  instructions on enabling the cross-server features, see the “ Cross-Server
                                    			 Sign-In, Transfers, and Live Reply ” chapter.

### Addressing and Dial Plan Considerations

See the following sections for addressing and dial plan considerations in specific networking situations:

#### Addressing Options for Non-Networked Phone Systems

If your organization has a separate phone system for each location, users at one location dial a complete phone number, not
                                 just an extension, when calling someone at another location. When users sign in to send messages to users on another networked
                                 location, the number that they enter when addressing a message by extension depends on whether the numbering plans overlap
                                 across locations.

When user extensions on one location overlap with user extensions on another location, you can provide unique extensions for
                                 each user by setting up alternate extensions for each user account. For each user, enter a number for the alternate extension
                                 that is the same as the full phone number for the user, and make sure that the alternate extension is in a partition that
                                 is a member of the search spaces that users at other locations use. Once this has been set up, when users sign in to send
                                 messages, the number that they enter when addressing messages is the same number that they use when calling.

When numbering plans do not overlap across networked locations—that is, when user extensions are unique across locations—users
                                 can enter an extension when addressing a message to a user who is associated with another location. Optionally, as a convenience
                                 for users in this circumstance, you may select to add alternate extensions to each user account, so that users do not need
                                 to remember two different numbers—one for calling a user directly, and one for addressing a message. However, if you do not
                                 set up alternate extensions, be sure to tell users to use the extension instead of the full phone number when addressing messages
                                 to users who are associated with another location.

Note that alternate extensions have other purposes beyond their use in networking, such as handling multiple line appearances
                                 on user phones.

#### Identified User Messaging

When a user calls another user, and the call is forwarded to the greeting of the called user, the ability of Unity Connection
                                 to identify that it is a user who is leaving a message is referred to as identified user messaging. Because Unity Connection
                                 is able to identify the caller as a user:

Unity Connection plays the internal greeting of the called user when the caller leaves a message.

Unity Connection plays the recorded name of the user who left the message when the recipient listens to the message.

Unity Connection allows the recipient to record a reply.

It is important to note the difference between the following two circumstances:

A user signs in to Unity Connection, and then records and sends a message. In this circumstance, when the user has signed
                                       in, Unity Connection can identify the message as being from the user, regardless of which location the message recipient is
                                       homed on. In this case, the phone system is not involved and the recipient phone does not ring. Instead, the message is sent
                                       via networking message exchange (using SMTP).

A user places a phone call to another user, and then leaves a message. This circumstance is the basis of identified user messaging.

As long as identified user messaging is enabled on a Unity Connection location, Unity Connection is able to identify both
                                 local and remote users. Note, however, that for identified user messaging to work in both cases, the initial search scope
                                 of the call must be set to a search space that locates the correct user based on the calling extension, regardless of whether
                                 the caller is a local or remote user.

If a user calls from an extension that is in a partition that is not a member of the search space that was set as the initial
                                 search scope for the call, the call is not identified as coming from the user. If the extension of the user overlaps with
                                 an extension in another partition that also appears in this search space, the call is identified as coming from the first
                                 object that Unity Connection finds when searching the partitions in the order that they appear in the search space.

In situations where numbering plans overlap across locations, it is therefore possible to have a user leave a message that
                                 is incorrectly identified as coming from another user with the same extension in a different partition. Because the initial
                                 search scope of the call is based on call routing rules, to avoid this situation, use the following configuration guidelines:

Maintain a separate search space for each location in which the partition containing its users appears first in the search
                                       space. (By default, each Unity Connection server uses its own default partition and default search space, which are replicated
                                       to other locations when the server is networked.)

On each location, set up forwarded call routing rules specific to every other location by specifying a routing rule condition
                                       that applies only to calls from that location (for example, based on the port or phone system of the incoming call). Configure
                                       the rule to set the search scope of the call to the search space in which the partition containing users at the location appears
                                       first.

| Note | In order to link two Unity Connection sites, all servers in each site must be running Unity Connection version 15. |
|---|---|

| Replicated Object | Replicated Properties |
|---|---|
| Users with mailboxes | Alias First name, last name, display name, alternate names Extension, cross-server transfer extension, and alternate
                                                      						  extensions Directory listing status Partition Recorded name SMTP address and SMTP proxy addresses |
| System contacts | All properties |
| System distribution lists | All properties, including list membership |
| Partitions | All properties |
| Search spaces | All properties, including membership |
| Unity Connection location | Display name Host address SMTP domain name Unity Connection version |
| VPIM location | All properties except Contact Creation settings (contact
                                                					 creation is handled on the Unity Connection location that homes the VPIM
                                                					 location) |

| Replicated Object | Replicated Properties |
|---|---|
| Users with mailboxes | Alias First name, last name, display name, alternate names Extension, cross-server transfer extension, and alternate
                                                            						  extensions Directory listing status Partition Recorded name 1 SMTP address and SMTP proxy addresses |
| System distribution lists 2 | Alias Display name Extension Partition Recorded name 1 |
| Partitions | All properties |
| Search spaces | All properties |
| Unity Connection locations | Display name Host address SMTP domain name Unity Connection version |

| Replicated Object | Replicated Properties |
|---|---|
| Unity Connection users with mailboxes | Alias First name, last name,
                                                      						  display name, alternate names Extension, cross-server
                                                      						  transfer extension, and alternate extensions 3 Directory listing status Recorded name 4 SMTP address and SMTP
                                                      						  proxy addresses |
| Cisco Unity users | Alias First name, last name,
                                                      						  display name, alternate names Extension, transfer
                                                      						  extension, and alternate extensions Directory listing status Recorded name 4 |
| System distribution lists 5 | Alias Display name Extension 3 Recorded name 4 |
| Locations | Display name Host address SMTP domain name |

| Note | Additional directory object limits exist, and the directory object limits may have been updated since the time of release.
                                       For detailed and up-to-date limit information, see the System Requirements for Cisco Unity Connection Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html . |
|---|---|

| Tip | Distribution lists can be nested such that a distribution
                                          		list contains other lists. You can create one master All Voicemail Users
                                          		distribution list for a site that contains the All Voicemail Users list of each
                                          		Unity Connection location. |
|---|---|

| Feature | Description |
|---|---|
| Cross-server sign-in | Cross-server sign-in allows administrators to provide users who
                                             					 are homed on different locations with one phone number that they can call to
                                             					 sign in. When calling from outside the organization, users—no matter which is
                                             					 their home server—call the same number and are transferred to the applicable
                                             					 home server to sign in. |
| Cross-server transfer | Cross-server transfer enables calls from the automated attendant
                                             					 or from a directory handler of one server to be transferred to a user on
                                             					 another server, according to the call transfer and screening settings of the
                                             					 called user. |
| Cross-server live reply | Cross-server live reply allows users who listen to their
                                             					 messages by phone to reply to a message from a user on another server by
                                             					 calling the user (according to the call transfer and screening settings of the
                                             					 called user). |