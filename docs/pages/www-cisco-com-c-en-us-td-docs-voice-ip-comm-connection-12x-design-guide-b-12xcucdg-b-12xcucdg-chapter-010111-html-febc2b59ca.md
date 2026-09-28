---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-design-guide-b-12xcucdg-b-12xcucdg-chapter-010111-html-febc2b59ca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg/b_12xcucdg_chapter_010111.html
retrieved_at: 2026-08-17T02:35:08.812917+00:00
---

Design Guide for Cisco Unity Connection 12.x

# Design Guide for Cisco Unity Connection 12.x

Updated: August 17, 2017

Chapter: Migrating from
	 Cisco Unity to Cisco Unity Connection

## Chapter: Migrating from
	 Cisco Unity to Cisco Unity Connection

# Migrating from
                     	 Cisco Unity to Cisco Unity Connection

When migrating from Cisco Unity to Cisco Unity Connection there are two
                        		distinct strategies to choose from: flash cut or gradual.

A gradual migration allows the Unity Connection environment to be built
                        		up over time. Directory synchronization is established between the Cisco Unity
                        		and Unity Connection sites, allowing the two sites to function as a single
                        		Cisco Voicemail Organization. Users can then be migrated over in small batches.
                        		A gradual migration might be required for multi-node sites needing to reuse
                        		Cisco Unity hardware or for sites that need an extended timeline for building
                        		out the Unity Connection infrastructure.

A flash-cut strategy eliminates the implementation and management
                        		complexity that the internetworking requirement imposes on a gradual migration,
                        		which can greatly reduce the overhead of a migration. A flash-cut approach is
                        		particularly attractive to sites using only Cisco Unity release 7.0 or earlier,
                        		as there is no need to upgrade to Cisco Unity before the migration.

## Flash-Cut
                        	 Migration

At a high level, a flash-cut migration process would look like
                           		this:

Build the Cisco Unity Connection site as a parallel
                                 			 infrastructure.

Copy all user data and selected system distribution lists using
                                 			 the COBRAS briefcase mode. For more information, see Help for the COBRAS tool
                                 			 at http://www.ciscounitytools.com/Applications/General/COBRAS/Help/COBRAS.htm .

Redirect all voicemail pilot numbers and related phone system
                                 			 routing from Cisco Unity to Unity Connection.

Unity Connection becomes the production voicemail server.

The cut itself (steps 2 and 3 in the list above) should occur
                           		after hours or over a weekend, depending on the scale. For more information on
                           		implementing a flash cut, see the “ Migrating from Cisco Unity 4.x
                              		  and Later to Unity Connection 7.x and Later ” section of the “Maintaining
                           		Cisco Unity Connection Server” chapter of the Install, Upgrade, and Maintenance
                           		Guide for Cisco Unity Connection, Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/install_upgrade/guide/b_12xcuciumg.html .

See the following sections for additional details:

### Using COBRAS to Migrate Messages in a Flash-Cut Migration

COBRAS can be leveraged to copy messages from Cisco Unity to Unity Connection. If this is done, then the Cisco Unity servers
                              can be decommissioned immediately after the flash. However, there are several limitations that should be considered before
                              deciding to migrate messages. These are detailed in the COBRAS Help, at http://www.ciscounitytools.com/Applications/General/COBRAS/Help/COBRAS.htm .

An alternate approach is to maintain the Cisco Unity servers for a short period strictly to provide users with access to old
                              messages. For example, a typical message retention policy might allow 30 days of access before the servers are decommissioned.
                              Note that Cisco Unity allows users to reply to messages in this environment. This may be acceptable if Cisco Unity is in a
                              unified messaging configuration, as users can continue to see new messages in their email client. Otherwise, for example in
                              a voicemail-only environment, the Custom Key Map utility can be used to disable all options for “Send a message,” “Reply,”
                              “Forward message,” and “Reply to all.”

MWI functionality on Cisco Unity should be disabled in any post-cut dual environment. This prevents conflicts that occur when
                              two messaging systems attempt to control the same lamps. The Cisco Unity Bulk Edit utility can be used to disable MWIs for
                              all subscribers.

### Mitigating Day One Shock After a Flash-Cut Migration

A major concern with flash-cut migrations in general is that all users are exposed to a new system at once. Because almost
                              all user settings are preserved during a COBRAS briefcase move, the flash cut from Cisco Unity to Unity Connection eliminates
                              the potential flood of first-time enrollment activity that can easily overwhelm other voicemail migrations.

You can further mitigate the impact of the flash cut by building the full Unity Connection environment well in advance of
                              the cut. Users can then be given access and training on the production Unity Connection servers while Cisco Unity still acts
                              as the production messaging solution. This helps reduce day 1 loads and support cases as users have the opportunity to customize
                              personal settings over a period of time.

The duration of a pre-cut parallel environment needs to be a balance between minimizing costs of maintaining both environments
                              and providing sufficient time for users to familiarize themselves with Unity Connection.

MWI functionality should be disabled on the Unity Connection servers during any pre-cut time. MWI functionality needs to be
                              enabled on Unity Connection when the flash cut is performed.

## Gradual Migration
                        	 Using Intersite Networking

At a high level, the process of using a Cisco Voicemail
                           		Organization to link Cisco Unity and Cisco Unity Connection would look like
                           		this:

- Upgrade Cisco Unity as
                                    				needed to meet minimum requirements for Intersite networking.

- Install and configure at
                                    				least one Cisco Unity Connection 12.x server.

- Begin initial preparation
                                    				of search spaces and partitions on Unity Connection. (For design
                                    				considerations, see the Partition Considerations section.)

- Join the Cisco Unity and
                                    				Unity Connection sites with an intersite link.

- Complete the configuration
                                    				of search spaces and partitions on Unity Connection.

- Complete the initial
                                    				configuration of distribution lists. (For design considerations, see the Distribution List Management section.)

- Set up intersite
                                    				cross-server features.

- Use COBRAS hot mode to move
                                    				user accounts to Unity Connection.

- Reconfigure user phones to
                                    				use Unity Connection pilot numbers.

- Optionally, configure
                                    				access for migrated users to their old voice messages on the Cisco Unity
                                    				server, and instruct users on how to access archived mailboxes.

- Decommission (uninstall)
                              		  each Cisco Unity server when all users on the server are migrated and archived
                              		  mailboxes have expired.

For a high level overview of a Cisco Voicemail Organization that
                           		links Cisco Unity and Cisco Unity Connection sites, see the “ Overview of Networking
                              		  Concepts ” chapter of the Networking Guide for Cisco Unity Connection Release 12.x , at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/networking/guide/b_12xcucnetx.html .

It is critical that the migration be viewed as a one-way flow.
                           		All associated tools, such as COBRAS and PDL Builder, are intended to assist in
                           		moving objects from the Cisco Unity site to Unity Connection. There is no
                           		automated process to move users or distribution lists in the reverse direction,
                           		from Unity Connection to Cisco Unity.

In most cases a gradual migration should focus on moving
                           		subscribers from one Cisco Unity location at a time. This helps to reduce the
                           		cost and complexity of the overall Cisco Voicemail Organization. When all
                           		subscribers for a given location are migrated, the Cisco Unity server can be
                           		decommissioned and repurposed. A decommissioned server may even be repurposed
                           		as a Unity Connection server if it meets the platform requirements for Unity
                           		Connection (see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html ).

### Pre-Existing Dual
                           	 Environments Using VPIM

With earlier releases of Cisco Unity and Unity Connection it was
                              		possible to maintain a mixed environment using VPIM networking. These mixed
                              		environments can be greatly enhanced by utilizing the intersite networking
                              		features available in Unity Connection Release 11.x. When the VPIM link has
                              		been replaced by an intersite link, the general migration process can follow a
                              		gradual migration as detailed in the Gradual Migration Using Intersite Networking section.

Note that it is not necessary to entirely remove the VPIM link
                              		between the two sites. Leaving the VPIM link in place preserves routing for
                              		users who reply to messages that were sent previously. However, pre-existing
                              		VPIM contacts on both sides of the network may cause addressing conflicts.
                              		These contacts should be hidden or deleted. Also, VPIM on both sides must be
                              		configured not to automatically create VPIM contacts.

For example, consider an installation where John Smith is a
                              		Unity Connection user with extension 1234. In the pre-existing VPIM environment
                              		a VPIM contact account was created for John Smith and assigned extension 1234
                              		within Cisco Unity. When intersite networking is established, Cisco Unity
                              		attempts to create a new Unity Connection contact for John Smith. In some cases
                              		this creation fails entirely due to conflicts with the existing VPIM account.
                              		In other cases, the Unity Connection contact is created, but the primary
                              		extension for John Smith (1234) is not associated with the new account.

On Unity Connection, existing VPIM contacts can be hidden from
                              		users by reassigning them to a partition that is not addressable from any
                              		search space. Note that VPIM accounts at the Cisco Unity site cannot as easily
                              		be hidden. Also, existing VPIM accounts on Cisco Unity may prevent the proper
                              		intersite replication of corresponding Unity Connection users. To avoid
                              		addressing and synchronization conflicts, in Cisco Unity, delete all VPIM
                              		contacts that are associated with the Unity Connection location. This of course
                              		means that existing messages addressed from the VPIM contacts are no longer
                              		associated with the contact.

Any distribution lists—either system or private—that contain
                              		VPIM contacts should be updated to use the replicated Unity Connection
                              		Networking subscribers instead. Note that such updates must be performed
                              		manually. Cisco Unity distribution lists that contain VPIM contacts lose those
                              		members when the VPIM contacts are deleted. In the reverse direction it is
                              		possible for Unity Connection distribution lists to continue delivering
                              		messages via VPIM. However, even this becomes problematic as users are migrated
                              		to Unity Connection. The VPIM contacts on Unity Connection are not
                              		automatically updated during a COBRAS hot-mode migration. If a Unity Connection
                              		distribution list contains a VPIM contact for a migrated Cisco Unity
                              		subscriber, messages to that list is delivered to the archived mailbox of the
                              		subscriber on Cisco Unity.

### Selecting Site
                           	 Gateways

When establishing an intersite link between Cisco Unity and
                              		Unity Connection for a gradual migration, a server at each site must be
                              		designated as the site gateway. When networking has been established between
                              		the two sites, reassigning the role of site gateway to another server is not a
                              		simple task. Therefore, careful selection of the site gateways is critical. For
                              		basic prerequisites and considerations, see the “ Setting Up Networking between
                                 		  Cisco Unity and Cisco Unity Connection Servers ” chapter of the
                              		Networking Guide for Cisco Unity Connection Release 12.x , at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/networking/guide/b_12xcucnetx.html .

At the Cisco Unity site, care should be taken to select a server
                              		that can maintain the role of site gateway for the duration of the migration.
                              		For example, any server that is to be repurposed as a Unity Connection server
                              		during the migration should not be selected. Also, if multiple dialing domains
                              		exist on the Cisco Unity site, selection of the site gateway affects the
                              		resulting dial plan (see the “Fitting
                                 		  Unity Connection Partitions into Dialing Domains” section on page 9-4 for additional details).

The role of site gateway does place nontrivial additional load
                              		on the server. Therefore, servers with the most available resources should be
                              		selected whenever possible. System load testing exposed performance impacts on
                              		the Cisco Unity site gateway related to the processing of directory information
                              		to and from the remote site. These impacts can be minimized using a Platform
                              		Overlay 2 or 3 server as the site gateway. Impact can also be reduced by
                              		minimizing the number of regular subscribers or users homed on site gateways.

While there are no minimum bandwidth requirements between the
                              		two site gateways, HTTP or HTTPS connectivity is required. A DNS environment
                              		allows FQDN resolution between the two site gateways. As long as this minimal
                              		connectivity can be met, priority should be given to other criteria discussed
                              		above.

### Partition Considerations

Within the Cisco Unity site, dialing domains offer a very basic form of partitioning. When multiple dialing domains exist,
                              extra planning is needed in deciding how the dialing domain topology is integrated with Unity Connection search spaces and
                              partitions.

See the following sub-sections for additional details:

#### Fitting Unity
                              	 Connection Partitions into Dialing Domains

When networked with a Cisco Unity site, each Unity Connection
                                 		location has just a single partition that is made available in Cisco Unity. At
                                 		the Cisco Unity site, all Unity Connection locations are assigned to the
                                 		dialing domain of the site gateway. Cisco Unity attempts to add all incoming
                                 		extensions from Unity Connection into this single dialing domain. Because
                                 		extensions within a dialing domain must be unique, the collection of all
                                 		partitions chosen across the Unity Connection site should not contain
                                 		duplicates of any extension. When the collection includes duplicate extensions,
                                 		or extensions that already exist in the Cisco Unity site gateway dialing
                                 		domain, one or more extensions are omitted from the Cisco Unity directory.

Figure 9-1 depicts a
                                 		Cisco Voicemail Organization consisting of two Unity Connection locations with
                                 		two partitions each, and three Cisco Unity locations in two dialing domains. In
                                 		this case, Partition A1 is selected as the partition from which user extensions
                                 		map to the dialing domain for Unity Connection A (in Cisco Unity Connection
                                 		Administration this is known as the Local Partition That Cisco Unity Users Can
                                 		Address to By Extension), and Partition B1 is selected to map to the dialing
                                 		domain for Unity Connection B. All extensions from these partitions map to
                                 		Dialing Domain 1 because the Cisco Unity site gateway, Cisco Unity X, is a
                                 		member of Dialing Domain 1. These partitions should be chosen such that the
                                 		extensions are unique across Partition A1, Partition B1, and Dialing Domain 1.
                                 		Other partitions, such as Partition A2 and Partition B2, are not used by
                                 		Cisco Unity. Any extensions in those partitions are not available to users on
                                 		Cisco Unity.

For additional information on the local partition that
                                 		Cisco Unity users can address to by extension, see the “About Linking
                                 		Cisco Unity Connection and Cisco Unity Sites” section and the “Cisco Unity
                                 		Dialing Domains and Cisco Unity Connection Users” section in the “Overview of
                                 		Networking Concepts in Cisco Unity Connection 12.x” chapter of the Networking
                                 		Guide for Cisco Unity Connection Release 12.x , at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/networking/guide/b_12xcucnetx.html .

Cisco Unity automated attendant searches always treat imported.
                                 		Unity Connection users as remote users. Therefore, the automated attendant
                                 		search scope should be set to dialing domain on every Cisco Unity server.
                                 		Callers within alternate dialing domains at the Cisco Unity site are not able
                                 		to contact Unity Connection users through automated attendant searches.

Cisco Unity subscriber-addressing searches and directory handler
                                 		searches treat imported Unity Connection users as if they are homed on the
                                 		Cisco Unity site gateway. On the site gateway, Unity Connection users are found
                                 		even if the scope is restricted to local server. For all other servers, a local
                                 		server scope does not return any Unity Connection users. Dialing domain or
                                 		global directory should be selected as the scope for these types of searches in
                                 		order to provide consistent behavior between the site gateway and non site
                                 		gateway servers.

#### Fitting Dialing
                              	 Domains into Cisco Unity Connection Partitions

Cisco Unity Connection does not carry over dialing domain
                                 		information from Cisco Unity. For each Cisco Unity location, Unity Connection
                                 		creates a dedicated partition, as shown in Figure 9-2 . You might
                                 		have several Cisco Unity locations in a dialing domain, with a global,
                                 		non-overlapping dial plan. Unity Connection does not see this. It only sees the
                                 		individual locations and creates distinct partitions for you to manage.

Figure 9-2 depicts the
                                 		same Cisco Voicemail Organization shown in Figure 9-1 .
                                 		In this case, looking from the perspective of mapping Cisco Unity objects into
                                 		Unity Connection partitions, we see that three new partitions are created on
                                 		the Unity Connection A, the site gateway, when the sites are linked. Each
                                 		partition corresponds to a Cisco Unity location. The new partitions are then
                                 		replicated via intrasite networking to Unity Connection B.

When intersite networking is initially configured between
                                 		Cisco Unity and Unity Connection, users who are homed on Unity Connection are
                                 		not able to dial or address messages to users on Cisco Unity. This is because
                                 		the Unity Connection search spaces do not contain the partitions that were
                                 		auto-generated for Cisco Unity locations. After initial replication completes,
                                 		Unity Connection search spaces must be modified to include the new partitions.
                                 		This needs to be done at each Unity Connection location in the network. In most
                                 		basic topologies, this might mean simply adding the new partitions to the
                                 		default search space on each server. In complex environments consideration must
                                 		also be given to all search spaces used by call handlers, directory handlers,
                                 		call routing rules, and users. For example, the search space of a Unity
                                 		Connection user must include the Cisco Unity partitions in order for that user
                                 		to add remote site users to a private distribution list.

When users are migrated from Cisco Unity to Unity Connection
                                 		they can be assigned to any local partition on the Unity Connection server.
                                 		After a Cisco Unity server is fully migrated it is possible to remove the
                                 		location from the network. If this is done, the auto-generated partition for
                                 		that location then disappears. Therefore, focusing the user migration to one
                                 		Cisco Unity server at a time can help reduce complexity at the Unity Connection
                                 		site.

#### Migrating Away
                              	 from Dialing Domains

An intermediate goal of the migration might be to eliminate the
                                 		need for multiple dialing domains. Doing so reduces the complexity of an
                                 		organization and typically allows for more flexible dial plans. This is most
                                 		effective when all servers in a dialing domain can be migrated simultaneously.
                                 		If a subset of the dialing domain is migrated, connectivity between those users
                                 		and the remaining dialing domain members may be disrupted. The users migrated
                                 		can be provided with search spaces that allow access to any Cisco Unity
                                 		Connection user as well as access to Cisco Unity subscribers in any dialing
                                 		domain. However, any Unity Connection partition that is associated with those
                                 		migrated users can only be mapped to the dialing domain of the Cisco Unity site
                                 		gateway.

In some cases dialing domains are used to intentionally
                                 		segregate users, for example to provide limited tenant services. In this case,
                                 		the dialing domain of the Cisco Unity site gateway should be migrated first. If
                                 		users from another dialing domain are migrated, Cisco Unity is not able to
                                 		provide the same level of segregation.

Example

Before beginning the user migration from Cisco Unity to
                                 		Cisco Unity Connection, Kelly and Avery are homed on Cisco Unity X, the site
                                 		gateway, in Dialing Domain 1. Chris and Robin are homed on Cisco Unity Z in
                                 		Dialing Domain 2. As shown in Figure 9-3 , Kelly and
                                 		Avery can find Unity Connection users in directory handler searches and address
                                 		to them using their extensions in Partition A1, but they cannot reach Chris and
                                 		Robin by the same means. Chris and Robin can address to each other but cannot
                                 		address to Kelly or Avery or to users on Unity Connection A.

When Kelly is migrated to Cisco Unity Connection A using COBRAS
                                 		hot mode, during the migration process, Partition A1 is selected for the target
                                 		partition. This means that all existing extensions and alternate extensions for
                                 		Kelly is also assigned to Partition A1. Because Partition A1 is replicated into
                                 		Dialing Domain 1 of Cisco Unity, all dialing and addressing scopes within the
                                 		Cisco Unity site that previously controlled access to Kelly are still
                                 		effective, so Avery can still reach Kelly as usual, as shown in Figure 9-4 . Similarly,
                                 		Kelly can be assigned to a search space that maintains the same level of access
                                 		that she had before the move. Of course the search space can also be made more
                                 		granular or even provide additional access.

Now suppose Chris is also migrated to Unity Connection. Even if
                                 		none of Chris’s extensions are placed into Partition A1 (the partition that
                                 		replicates to Cisco Unity), Chris still have a contact account created by
                                 		Cisco Unity within Dialing Domain 1, as shown in Figure 9-4 . This means
                                 		that Avery can now locate Chris when using dial by name with a directory
                                 		handler or during subscriber message addressing. Robin is still unable to reach
                                 		Kelly or Avery through directory handlers and subscriber message addressing,
                                 		and can no longer reach Chris through these means.

### Interworking with Other Voice Messaging Networks

A Cisco Unity environment can use other voice messaging network types (Bridge, AMIS, VPIM, or Trusted Internet). However,
                              messages from Cisco Unity Connection users cannot be relayed to remote subscribers who are associated with these other Cisco Unity
                              delivery locations. Instead, direct networking to these other locations must be established independently from the Unity Connection
                              site.

#### VPIM

A direct VPIM link can be established between the Cisco Unity
                                 		Connection site and any other remote messaging network, although the VPIM link
                                 		between Cisco Unity and the external system must also be maintained, as shown
                                 		in Figure 9-5 . Relaying
                                 		messages across the intersite link to VPIM contacts is not possible in either
                                 		direction. The servers acting as the VPIM bridgehead at each site can also act
                                 		as the site gateway, though they do not need to.

As users are migrated from Cisco Unity to Unity Connection, the
                                 		external VPIM system needs to be updated. The exact steps required depend on
                                 		the specific system. Typically, contacts or message routing are managed
                                 		according to the extension of each user. Therefore, migrating users in groups
                                 		within continuous extension ranges is desirable. The administrative work
                                 		required at the external system may become onerous if migrated users span
                                 		multiple disjointed extension ranges.

#### Non-VPIM

System contacts can be manually created in Cisco Unity Connection that correspond to the Trusted Internet Subscribers on Cisco Unity.

Unity Connection does not support Bridge or AMIS networking. If a remote messaging system supports only Bridge or AMIS networking,
                                 Unity Connection users are not able to address to users on those systems.

### Distribution List Management

In a mixed Cisco Unity and Cisco Unity Connection network, directory synchronization can be configured to include system distribution
                              lists. When this is done only addressing and routing information for the distribution lists is shared. Membership information
                              for each list is stored and managed at the site where the list was created. However, with some careful advanced planning,
                              it is possible to limit most list management activity to one site. This reduces the need to jump between Cisco Unity and Unity
                              Connection administration for list maintenance.

#### System Distribution List Management on Unity Connection

Because the long term goal of a migration is to have everything on Cisco Unity Connection, it may be beneficial to move most,
                                 if not all, voicemail distribution lists, including membership, to Unity Connection right away. This can be done using Public
                                 Distribution List Builder (see Public Distribution List Builder Help for details, at http://ciscounitytools.com/Applications/Unity/PublicDistributionListBuilder/Help/PublicDLBuilder.htm ). When a distribution list is created in Unity Connection, intersite networking can allow both Cisco Unity and Unity Connection
                                 users access to the list. The original list on Cisco Unity should then be removed.

Note that distribution lists that use subscriber templates for membership cannot be managed fully on Unity Connection. This
                                 is because Unity Connection does not use templates when creating contacts for replicated Cisco Unity subscribers. However,
                                 distribution list nesting can be used to manage template-based distribution lists that span both sites.

Example

A “Sales Staff” distribution list on Cisco Unity is populated using a corresponding subscriber template. When intersite networking
                                 is introduced, the Cisco Unity Sales Staff list cannot be migrated over to Unity Connection because new sales staff may still
                                 be added to the Cisco Unity site during the gradual migration. Instead, a corresponding “Sales Staff” template and distribution
                                 list are created on Unity Connection. The distribution list on Unity Connection is configured to replicate to remote sites
                                 over intersite links.

On Cisco Unity, the “Sales Staff” distribution list is renamed to “Sales Staff – Unity only.” If previously enabled, the “Show
                                 Distribution List in Email Server Address Book” attribute is removed. Using Public Distribution List Builder, the “Sales Staff
                                 – Unity only” distribution list is marked for replication to Unity Connection.

When the “Sales Staff – Unity only” distribution list has replicated from Cisco Unity to Unity Connection, it can then be
                                 added as a nested member of the “Sales Staff” distribution list on Unity Connection. The list on Unity Connection is now the
                                 master “Sales Staff” distribution list. Users on Unity Connection address to it directly while those on Cisco Unity address
                                 to it via its replicated object, which by default shows up on Cisco Unity as “Sales Staff – Voicemail.” When a new mailbox
                                 is created using the sales staff template at either site, that mailbox is immediately a recipient of the master “Sales Staff”
                                 distribution list.

Note that managing voicemail distribution lists on Unity Connection becomes problematic when Cisco Unity is a unified messaging
                                 deployment and Unity Connection users are using ViewMail for Outlook within the same Active Directory. The groups that Cisco Unity
                                 creates in Active Directory for replicated Unity Connection system distribution lists can complicate matters for Unity Connection
                                 users when they address messages via ViewMail for Outlook or other email clients. Unity Connection users who try to address
                                 messages to such lists receive a non-delivery receipt in response. Currently, Unity Connection does not provide a way to mitigate
                                 the issue for synchronized distribution lists using SMTP proxy addresses like you can for Unity Connection users.

#### Public Distribution List Management on Cisco Unity

When Cisco Unity and Unity Connection are both
                                 		integrated (or unified in the case of Cisco Unity) it may be desirable to
                                 		manage system distribution lists at the Cisco Unity site. This allows them to
                                 		be fully synchronized with Active Directory. Distribution lists can be
                                 		selectively enabled for directory replication to Unity Connection.

Distribution lists populated via subscriber
                                 		templates can be handled in a way similar to that discussed in the “System
                                    		  Distribution List Management on Unity Connection” section on page 9-10 .
                                 		Template-based lists from Unity Connection can be nested into corresponding
                                 		lists on Cisco Unity. In this case the Cisco Unity lists become the master
                                 		lists. Partitions and search spaces can be used to hide the sub-lists on Unity
                                 		Connection from users.

Example

A “Sales Staff” distribution list on Cisco Unity
                                 		is populated using a corresponding subscriber template. When Unity Connection
                                 		Networking is introduced, the Cisco Unity Sales Staff distribution list cannot
                                 		be migrated over to Unity Connection because new sales staff may still be added
                                 		to the Cisco Unity site during the gradual migration. Instead, a corresponding
                                 		“Sales Staff – Unity Connection Only” template and distribution list are
                                 		created on Unity Connection. This list on Unity Connection is configured to
                                 		replicate to remote sites over intersite links. The list is assigned to a
                                 		partition which is not addressable by users.

When the Unity Connection distribution list is
                                 		replicated to Cisco Unity, its display name appears as “Sales Staff – Unity
                                 		Connection Only – voicemail.” The “Show Distribution List in Email Server
                                 		Address Book” attribute should be removed for this list. It can then be added
                                 		as a nested member of the Cisco Unity “Sales Staff” distribution list. The
                                 		Cisco Unity “Sales Staff” distribution list is marked for replication to Unity
                                 		Connection using the Public Distribution List Builder tool.

The distribution list on Cisco Unity is now the
                                 		master “Sales Staff” distribution list. Users on Cisco Unity address to it
                                 		directly while those on Unity Connection address to it via its replicated
                                 		object, which by default shows up on Unity Connection as “Sales Staff.” When a
                                 		new mailbox is created using the sales staff template at either site, that
                                 		mailbox is immediately a recipient of the master “Sales Staff” distribution
                                 		list.

Note that this method for managing voicemail
                                 		distribution lists limits dial plan flexibility. All distribution lists that
                                 		are replicated from Cisco Unity to Unity Connection are assigned to the same
                                 		auto-generated partition as all other objects from the Cisco Unity location. If
                                 		greater granularity for search scope partitioning is needed, distribution lists
                                 		need to be managed at the Unity Connection site.

Another caveat of managing distribution lists
                                 		within Unity Connection occurs as users are migrated to Unity Connection.
                                 		Distribution list membership within Cisco Unity is not adjusted when COBRAS hot
                                 		mode is used to migrate users. Messages to the distribution list continue to be
                                 		delivered to the Exchange mailboxes of the migrated users. While these messages
                                 		are accessible via the archived subscriber account, the situation may cause
                                 		confusion for users. (See the “Archived
                                    		  Mailboxes” section on page 9-13 for additional details.)

#### Hybrid Distribution List Management

Managing distribution lists entirely on one site
                                 		or the other is often not possible. In addition to the caveats mentioned in the “System
                                    		  Distribution List Management on Unity Connection” section on page 9-10 and the “Public
                                    		  Distribution List Management on Cisco Unity” section on page 9-10 ,
                                 		distribution lists that contain contacts cannot be replicated. This is because
                                 		messages that are sent across an intersite link cannot be further relayed to
                                 		remote mailboxes that are not part of the Cisco Voicemail Organization. If a
                                 		user at the remote site were to attempt addressing to such a list, a
                                 		non-delivery receipt (NDR) would be generated for each undeliverable contact
                                 		within the list.

Example

Suppose the Cisco Unity “Sales Staff” distribution
                                 		list from the previous examples also contains VPIM contacts in addition to
                                 		mailbox users. In order to use templates at both sites for populating a master
                                 		“Sales Staff” list, two separate distribution lists are maintained at each
                                 		site. Each site has a “Sales Staff – <site>” list that contains only
                                 		users from the local site, and each list is assigned to the corresponding
                                 		template at each site. (The list can be hidden from users but must be
                                 		configured to replicate across the intersite link.) Next, each site also has a
                                 		“Sales Staff” master distribution list. The master lists contain both “Sales
                                 		Staff – <site>” lists plus any remote contacts such as VPIM users. The
                                 		two master lists are not replicated between the sites. Users at each site must
                                 		address to the corresponding local master list.

#### Nesting Distribution Lists

Nesting of distribution lists can be extremely useful. However, it is important to be aware of list membership when nesting.
                                 In each of the distribution list examples in the “System Distribution List Management on Unity Connection” section on page 9-10 , the “Public Distribution List Management on Cisco Unity” section on page 9-10 , and the “Hybrid Distribution List Management” section on page 9-11 , two categories of lists are used at each site. The first category is local lists that are created with the intent of having
                                 list membership limited to the local site. The display names for the local lists should follow a naming convention that helps
                                 identify their role. The second category of lists is the master lists. The membership for the master lists includes objects
                                 from both sites. When nesting lists, a master list should never be nested inside another list. Following a well-defined naming
                                 convention can help ensure nesting loops are not created.

Additionally, any list that contains external contacts, such as VPIM subscribers, should not be nested within any list that
                                 is replicated. A naming convention for list display names could be extended to flag these lists. This would serve as a reminder
                                 to avoid placing such lists within a list that is intended for replication.

#### Private Distribution Lists

When users are migrated from Cisco Unity to Cisco Unity Connection, some private distribution list membership information
                                 may be lost. Backups only include membership information about full subscribers (users with mailboxes) and public distribution
                                 lists. Members of the private distribution list that are remote contacts (including Unity Connection users) or other private
                                 lists are not included in the private list membership backup.

Also, if a migrated user was included as a member of a private distribution list owned by a Cisco Unity subscriber who has
                                 not been migrated, that private distribution list is not automatically updated during the migration. Unless the distribution
                                 list is manually edited, messages sent to it continues to be delivered to the archived mailbox of the migrated user on Cisco Unity.

### Messaging
                           	 Options

For an overview of message routing between Cisco Unity and Unity
                              		Connection sites, see the “ Configuring Partitions and
                                 		  Search Spaces for Cisco Unity and Cisco Unity Connection
                                 		  Interoperability ” section in the “Setting Up Networking Between Cisco
                              		Unity and Cisco Unity Connection” chapter of the Networking Guide for
                              		Cisco Unity Connection, Release 12.x , at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/networking/guide/b_12xcucnetx.html .

### Secure Messages

Cisco Unity and Unity Connection use different methods for securing messages. In particular, Unity Connection is not able
                              to decrypt secure messages that are sent from Cisco Unity. Therefore, by default, messages marked as secure is not sent between
                              the systems.

Optionally, you can configure both systems to enable delivery of secure messages between sites. However, in order for this
                              to occur, all secure messages must be unencrypted as they traverse the network. An x-header is placed on the messages indicating
                              whether they are intended to be secure. This allows the receiving site to apply secure handling of the messages when they
                              arrive. For example, Cisco Unity can be configured to encrypt inbound messages that are flagged as secure as soon as they
                              arrive.

### Transcoding

Both Cisco Unity and Unity Connection can be
                              		configured to transcode all messages sent to the remote site. This may be
                              		required, for example, if the messages are stored locally in a format not
                              		supported at the remote site. However, use of the transcoding feature is likely
                              		to reduce audio quality of the messages. This is particularly noticeable if a
                              		message traverses between sites multiple times, for example, by being forwarded
                              		between sites, or when a distribution list contains remote users.

Example

Consider the master “Sales Staff” distribution
                              		list on Unity Connection from the “System
                                 		  Distribution List Management on Unity Connection” section on page 9-10 .
                              		A Cisco Unity user is able to send messages to this list using the replicated
                              		“Sales Staff – voicemail” list found on Cisco Unity. The message is first
                              		routed across to the Unity Connection site, introducing possible transcoding
                              		degradation. Unity Connection members of the list receive the message in this
                              		state. But then the message is further routed back across to Cisco Unity so
                              		that it can be delivered to members of the “Sales Staff – Unity only”
                              		distribution list. This introduces a second generation of transcoding
                              		degradation. We now have up to two generations of degradation for a message
                              		that, in the end, was sent between two users on the same messaging system.

### Archived Mailboxes

When COBRAS hot mode is used to migrate batches of users from Cisco Unity to Unity Connection, the user mailboxes on Cisco Unity
                              are preserved but set to an archived state. These mailboxes are hidden in the directories and cannot be directly addressed
                              to by other users. Because messages are not moved as part of the migration process, the archived mailboxes allow users to
                              access their messages for a period of time on the Cisco Unity server.

Because distribution list membership is not automatically updated when users are migrated, archived mailboxes can still receive
                              new messages. The archived mailboxes should be manually purged from all Cisco Unity distribution lists, both public and private.
                              For public distribution lists an alternate solution is to use the Public Distribution List Builder tool to move lists from
                              Cisco Unity to Unity Connection. Even if the list already has archived mailboxes as members, Public Distribution List Builder
                              maps and replaces those members with the correct corresponding user on Unity Connection.

The archived mailboxes are hidden in the Cisco Unity Administrator. The only administrative tasks available for these mailboxes
                              are password resets and deletes. These tasks can be done using the Bulk Password Reset and Bulk Subscriber Delete tools. For
                              additional information about the tools, see the respective tool Help at http://www.ciscounitytools.com/Applications/Unity/BulkPWReset/Help/BulkPWReset.htm and at http://www.ciscounitytools.com/Applications/Unity/BulkSubscriberDelete403/Help/BulkSubDelete.htm .

### Voice Name Replication

Replication of recorded voice names between Cisco Unity and Unity Connection is optional. It can be enabled in one direction,
                              both directions, or not at all. Additionally, the voice names can be converted to a different codec when they are replicated
                              between sites. For example, if disk space is a concern at one site the names can be converted to a more compressed format.

At the Unity Connection site, Text to Speech is automatically used for users who do not have recorded names. This applies
                              to remote Cisco Unity users also. This feature may provide a reasonable alternative to transcoding if disk space required
                              for remote Cisco Unity users is a concern on Unity Connection.

Often, new users on Unity Connection choose not to record their own voice names because of the Unity Connection Text to Speech
                              feature. However, Cisco Unity does not have this Text to Speech feature, so users without recorded voice names are not accessible
                              through directory handlers. Recorded voice names are also valuable during message addressing. Therefore, it generally is a
                              good idea to encourage Unity Connection users to record their voice names and to enable voice name replication to Cisco Unity.

## Common Elements in Flash-Cut and Gradual Migration Strategies

Certain considerations apply regardless of the type of migration strategy you choose. See the following sub-sections for additional
                           details:

### Key Mapping

One thing COBRAS does not migrate is custom key map configurations. COBRAS tracks the name of the conversation that subscribers
                              are associated with and tries to restore that on the import. However, if a key map conversation on Cisco Unity does not match
                              the mapping of the corresponding key map on Cisco Unity Connection, users end up with a different sounding conversation. It
                              is up to the administrator to verify that key mapping data is configured on the target system as needed.

### Speech Connect for
                           	 Cisco Unity

Cisco Unity typically synchronizes data to an external Speech
                              		Connect for Cisco Unity server via Active Directory. This synchronization ends
                              		when users are migrated because Cisco Unity Connection does not push any data
                              		to Active Directory. Therefore, maintaining the external Speech Connect for
                              		Cisco Unity servers may require importing manually-generated employee data
                              		files.

Some limited synchronization is available during a gradual
                              		migration. When users are created or migrated to Unity Connection, they are
                              		replicated across the intersite link to Cisco Unity, which in turn pushes them
                              		into Active Directory as Contacts. The Speech Connect for Cisco Unity server
                              		can then import them automatically if it is configured to pull both Users and
                              		Contacts. One caveat of this configuration is that the transfer extension used
                              		by Speech Connect for Cisco Unity originates from the Cross-Server Transfer
                              		Extension on Unity Connection. This field can only be managed by system
                              		administrators. The Speech Connect for Cisco Unity server cannot be
                              		synchronized with any basic or personal transfer rules configured by or for
                              		Unity Connection users.

A better approach may be to replace the external Speech Connect
                              		for Cisco Unity servers entirely with the Speech Connect for Unity Connection
                              		solution, which utilizes the standard Unity Connection voice-enabled directory
                              		handlers and does not require a separate server. The Speech Connect for
                              		Cisco Unity servers can then be decommissioned, reducing maintenance and
                              		administrative costs associated with the additional servers. The Unity
                              		Connection solution even provides additional features not available in Speech
                              		Connect for Cisco Unity, such as disambiguation by city and/or department name.
                              		Unlike Speech Connect for Cisco Unity, the Unity Connection solution also uses
                              		partitions and personal transfer rules for users. In a gradual migration, the
                              		search scope of directory handlers can be set to include both Cisco Unity and
                              		Unity Connection users. Enabling cross-server transfer routing for the remote
                              		locations also allows the speech-enabled automated attendant to use the current
                              		transfer rules for Cisco Unity subscribers.

Note that there is no name tuning service available for Unity
                              		Connection. Also, the telephony port capacity of the Unity Connection server
                              		must be sufficiently provisioned to accommodate call loads that previously were
                              		distributed between Cisco Unity and the external Speech Connect servers.

### Migrating from Cisco Unity for Domino to Unity Connection

A gradual migration using intersite networking is not possible with Cisco Unity for IBM Lotus Domino. This is because intersite
                              networking requires at least one server at the Cisco Unity site. Release 8.x of Cisco Unity is not supported with a Domino
                              message store.

It is possible to establish VPIM networking between a Cisco Unity for Domino site and Unity Connection. This would allow some
                              interworking between sites should a full flash-cut migration not be possible. COBRAS can then be used for migrating users
                              to the Unity Connection site. However, only COBRAS briefcase mode is available in this case. For more detail on COBRAS, see
                              COBRAS Help at http://www.ciscounitytools.com/Applications/General/COBRAS/Help/COBRAS.htm . In addition, considerations from the “Pre-Existing Dual Environments Using VPIM” section on page 9-3 apply in this scenario.