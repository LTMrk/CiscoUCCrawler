---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-networking-guide-b-15cucnetx-b-15cucnetx-chapter-01-html-32e73145dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnetx/b_15cucnetx_chapter_01.html
retrieved_at: 2026-08-17T03:32:47.000845+00:00
---

Networking Guide for Cisco Unity Connection Release 15

# Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Setting Up Networking Between Cisco Unity Connection Servers

## Chapter: Setting Up Networking Between Cisco Unity Connection Servers

# Setting Up Networking Between Cisco Unity Connection Servers

## Setting Up a Unity
                        	 Connection Site

This section describes the prerequisites for setting up a
                           		Cisco Unity Connection site, and provides a high-level task list of all of the
                           		tasks that you need to complete for the setup, and the order in which they
                           		should be completed. If you are unfamiliar with Unity Connection site concepts,
                           		you should first read the “ Overview
                              		  of Networking Concepts ” chapter and then review the task list and
                           		procedures before beginning the setup.

You can link up to ten Unity Connection locations in a single site. If you have more than 10 locations, set up two sites and
                           link them together. (In order to link sites, all servers in each site must be running Unity Connection version 15. You cannot
                           link more than two sites together.) For procedures, see the “Linking Two Unity Connection Sites” section .

### Prerequisites for
                           	 Setting Up a Unity Connection Site

Before starting the setup, verify that the following
                              		prerequisites have been met on each server that joins the site (for clusters,
                              		verify these prerequisites for the publisher server):

The server meets the requirements listed in the “ Requirements for Intrasite Networking ” section of the System Requirements for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

Unity Connection is already installed.

The servers networked together are directly accessible through
                                    			 TCP/IP port 25 (SMTP), or SMTP messages are routable through an SMTP smart
                                    			 host.

For Unity Connection clusters, you must have a smart host
                                    			 available to resolve the SMTP domain of the cluster to both the publisher and
                                    			 subscriber servers in order for message traffic to reach the cluster subscriber
                                    			 server in the event that the publisher server is down.

In addition, before setting up a Unity Connection site, you should be familiar with the concepts in the “ Dial Plan ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

### Task List for
                           	 Setting Up a Unity Connection Site

Use this task list to set up a networking site between Unity
                              		Connection servers or clusters. The cross-references take you to detailed
                              		procedures.

If you have a Unity Connection cluster, do the tasks only on the
                              		publisher server.

Make decisions about your networking deployment approach and
                                    			 gather information needed to configure the site. See the “Making
                                       				Deployment Decisions and Gathering Needed Information for Setting Up a Site”
                                       				section .

Check the display name of each server that you are joining to
                                    			 the site, and modify it if it is not unique, or if you want to select a more
                                    			 descriptive name. Also check the SMTP domain of each server that you are
                                    			 joining to the site, and modify it if it is not unique. See the “Verifying
                                       				Each Unity Connection Server has a Unique Display Name and SMTP Domain”
                                       				section .

If the display name of a server matches the display name of
                                    			 another server on the site, the server cannot join the site. Likewise, if the
                                    			 SMTP domain matches the SMTP domain of another server on the site, the server
                                    			 cannot join the site.

Start by linking two Unity Connection servers together to create
                                    			 a site, then link additional servers to any location in the site. See the “Linking
                                       				Unity Connection Servers with an Intrasite Link” section .

If any servers in the site require a smart host to transmit and
                                    			 receive SMTP messages from other servers (for example, because a firewall
                                    			 separates the servers, or because the servers are part of a Unity Connection
                                    			 cluster), configure the smart host, and configure the applicable locations to
                                    			 route through the host. See the “Configuring
                                       				a Smart Host” section .

For each cluster that you have added to the network, add the IP
                                    			 address of the subscriber server to the IP address access list on every other
                                    			 location on the network; this ensures that other locations can receive message
                                    			 traffic from the subscriber server if the publisher server is down. See the “Configuring
                                       				SMTP Access for Cluster Subscriber Servers” section .

Verify that replication is complete among locations. See the “Checking
                                       				Replication Status Within a Site” section on page 2-11 .

Configure search spaces at each location to allow users who are
                                    			 homed at the location to address to users at other locations. See the “Configuring
                                       				Search Spaces for Unity Connection Sites” section on page 2-12 .

Secure the site so that message transmissions are not
                                    			 misdirected. See the “Securing
                                       				the Unity Connection Site” section on page 2-12 .

Optionally, set up cross-server features. See the “ Cross-Server
                                       				Sign-In, Transfers, and Live Reply ” chapter.

Test the site. See the “Testing
                                       				the Intrasite Setup” section on page 2-12 .

Optionally, set up a site-wide All Users distribution list. See
                                    			 the “Creating
                                       				a Site-Wide All Voicemail Users Distribution List” section on page 2-14 .

If any servers in the site were previously configured as VPIM
                                    			 locations on other servers in the network, clean up the unused VPIM locations.
                                    			 See the “Cleaning
                                       				Up Unused Unity Connection VPIM Locations and Contacts” section on
                                       				page 2-15 .

If you have not already done so, set up VPIM Networking to
                                    			 connect the Unity Connection locations to any other VPIM-compatible voice
                                    			 messaging systems. See the “ VPIM
                                       				Networking ” chapter.

Optionally, create a mapping of which users are homed on which
                                    			 location. See the “Mapping
                                       				Users to Their Home Locations” section on page 2-15 .

Optionally, if you have a large site that includes locations running Unity Connection 14, review the advanced settings available
                                    on the System Settings > Advanced > Intrasite Networking page in Cisco Unity Connection Administration in case you need to
                                    tune the communications between the Unity Connection Digital Networking Replication Agent services on these locations.

Also note that the Limit Number of Simultaneous Incoming
                              		Connections and Limit Number of Simultaneous Outgoing Connections fields on the
                              		System Settings > SMTP Configuration > Server page in Unity
                              		Connection Administration affect the replication agent (and also affect
                              		intrasite messaging between users as well as other features that use SMTP for
                              		message transmission).

### Procedures for Setting Up a Unity Connection Site

#### Making Deployment
                              	 Decisions and Gathering Needed Information for Setting Up a Site

Before you begin setting up a site, be sure to plan for the
                                 		following, and gather the applicable information:

If your network includes voice messaging servers that do not meet the prerequisites for joining a Unity Connection site but
                                       support the Voice Profile for Internet Mail (VPIM) protocol (for example, Cisco Business Edition, Unity Connection servers,
                                       or other VPIM-compatible systems), use VPIM Networking to connect them.

Follow the given approaches:

Unless your servers are already configured for VPIM, set up the
                                             				  site first, then set up VPIM Networking.

Select a single Unity Connection location in the site to handle
                                             				  the configuration of VPIM locations and contacts. This location is referred to
                                             				  as the “bridgehead.” The VPIM location and contact objects are replicated from
                                             				  the bridgehead to all digitally networked Unity Connection locations so that
                                             				  those locations can address VPIM messages; the networked locations then forward
                                             				  the messages to the bridgehead for delivery to the remote voice messaging
                                             				  server. Managing these objects from a single location simplifies maintenance
                                             				  tasks and avoids potential overlaps in contact information that could cause
                                             				  confusion to users when they attempt to address messages.

If you have already configured VPIM locations on multiple
                                             				  systems that are joining a site, delete duplicate VPIM locations from all but
                                             				  one server before setting up the site. For instructions, see the “ Removing
                                                					 a VPIM Location ” section.

If you are migrating a VPIM location to a Unity Connection site (for example, because you used VPIM Networking to connect
                                             two or more Unity Connection servers and have upgraded the servers to Unity Connection 15) set up the Unity Connection site
                                             first. After the directory is fully replicated and you have tested message exchange between the Unity Connection locations,
                                             remove the VPIM locations and VPIM contacts that represent the migrated servers and their users. The task list reminds you
                                             when to do this task.

By default, every Unity Connection location (server or cluster)
                                       			 includes several predefined system distribution lists, which you can modify but
                                       			 not delete. If you have not renamed these lists so that the list names are
                                       			 unique on each location, or if you have added additional lists whose names are
                                       			 identical across locations, during initial replication each location
                                       			 automatically adds the remote server name to the display name of any remote
                                       			 lists whose names overlap with local list names. (The default lists are All
                                       			 Voicemail Users, Undeliverable Messages, and All Voicemail-Enabled Contacts.)
                                       			 This can cause confusion when local users try to address to those remote lists.

To solve this problem, you can use one of the following
                                       			 approaches:

If you want to maintain separate lists on each location, you can
                                             				  modify the name of each list on its home location so that it is unique (for
                                             				  example “All Voicemail Users on <Location Name>”) and notify your users
                                             				  of the new list names for each server. If you select this approach, you should
                                             				  also modify the recorded name of each list to indicate its source.

Alternatively, after setting up the site, you can create a
                                             				  master list that includes all users on all networked locations. The task list
                                             				  includes instructions on when and how to do this task.

If you want to synchronize Unity Connection user data with user
                                       			 data in an LDAP directory, you should configure Unity Connection for
                                       			 integration with the LDAP directory prior to setting up the site, to simplify
                                       			 testing and troubleshooting.

Make note of the following information about each server that is
                                       			 joining the network:

The IP address or fully qualified domain name (FQDN) of the
                                             				  server.

The user name and password of a user account that is assigned to
                                             				  the System Administrator role.

The dial strings that other servers use to call this server, if
                                             				  cross-server sign-in or transfer is configured on other servers to hand off
                                             				  calls to this server.

#### Verifying Each
                              	 Unity Connection Server has a Unique Display Name and SMTP Domain

Each Unity Connection server that you join to a Unity Connection
                                    		  site must have a unique display name. The display name must be unique both
                                    		  among Unity Connection locations and among VPIM locations. If the display name
                                    		  is not unique, the server cannot join the site. For new Unity Connection
                                    		  installations, the display name is typically the same as the host name of the
                                    		  server; however, if you changed the display name or upgraded the server from
                                    		  Unity Connection 2.x (which uses “Local VMS” as the default display name), you
                                    		  may need to change the display name so that it does not overlap with other
                                    		  locations on the network.

Tip

Each Unity Connection server that you join to the site must also
                                    		  have a unique SMTP domain, both among Unity Connection locations and among VPIM
                                    		  locations. By default, the SMTP domain is configured during installation to
                                    		  include the hostname of the server, in order to insure that it is unique.
                                    		  However, if the SMTP domains of multiple servers have been modified to the same
                                    		  value, you must change the domains to unique values before joining the servers
                                    		  in a site.

If you are migrating a server from VPIM Networking to intrasite
                                    		  or intersite networking, it is likely that the display name or SMTP domain of
                                    		  the server overlaps with the VPIM location configured for the server. If the
                                    		  domain name overlaps, you need to disrupt messaging to the VPIM location while
                                    		  doing the migration—either by changing the SMTP domain of the VPIM location, or
                                    		  by removing the VPIM location. (To remove the VPIM location, see the " Removing
                                       			 a VPIM Location " section.)

Do the following
                                    		  procedure to Verify each Unity Connection server :

Step 1

Check the Display Name of the first server:

In Cisco Unity Connection Administration on the first server,
                                                   				  expand Networking and select Locations .

On the Search Locations page, note the Display Name of the local
                                                   				  server. Make a list of all Display Names that you can consult later.

Step 2

Check the SMTP domain of the first server:

Expand System Settings > SMTP Configuration and select Server .

On the SMTP Server Configuration page, note the SMTP Domain of
                                                   				  the local server.

Step 3

Check the Display Name and SMTP Domain Name of all VPIM
                                             			 locations homed on the local server:

Expand Networking and select VPIM .

On the Search VPIM Locations page, note the Display Name of each
                                                   				  VPIM location.

Select the first VPIM location in the table. On the Edit VPIM
                                                   				  Location page, note the SMTP Domain Name of the VPIM location.

Select Next and note the SMTP Domain Name of the next VPIM
                                                   				  location.

Repeat Step 3d. for each remaining VPIM location.

Step 4

Repeat Step 1 through Step 3 on each location that is joined to the site.

Step 5

If the Display Name of a location conflicts with that of another
                                             			 location, or you want to modify a name to be more descriptive, change one of
                                             			 the display names:

To change the Display Name of a Unity Connection location,
                                                      					 follow Step 6 .

To change the Display Name of a VPIM location, follow Step 7 .

If the Display Names are all unique, skip to Step 9 .

Step 6

Change the Display Name of the Unity Connection location:

On the server for which you want to change the Display Name,
                                                   				  expand Networking and select Locations .

Select the Display Name of the local server.

On the Edit Location page, modify the Display Name value, and
                                                   				  select Save .

Step 7

To change the Display Name of a VPIM location:

On the server on which the VPIM location is homed, expand Networking and select VPIM .

On the Search VPIM Locations page, select the Display Name of
                                                   				  the location that you want to change.

On the Edit VPIM Location page, edit the Display Name value and
                                                   				  select Save .

Step 8

If there are any remaining Display Name conflicts, repeat Step 5 as necessary to
                                             			 resolve each conflict.

Step 9

If the SMTP domain of a server conflicts with that of another
                                             			 location, change one of the domain names:

To change the SMTP Domain of a Unity Connection location, follow Step 10 .

To change the SMTP Domain Name of a VPIM location, follow Step 11 .

Step 10

To change the SMTP Domain of a Unity Connection location:

Expand System Settings > SMTP Configuration , then select Server .

On the SMTP Server Configuration page, select Change SMTP Domain , change the value of the SMTP Domain
                                                   				  field, and select Save .

Select OK to confirm the change.

Step 11

To change the SMTP Domain Name of a VPIM location:

On the server on which the VPIM location is homed, expand Networking and select VPIM .

Select the Display Name of the VPIM location for which you want
                                                   				  to change the SMTP Domain Name.

On the Edit VPIM Location page, change the value of the SMTP
                                                   				  Domain Name field, and select Save .

Changing the SMTP Domain Name of a VPIM location may disrupt
                                                      					 messaging with the remote voice messaging system.

Step 12

If there are any remaining SMTP domain conflicts, repeat Step 9 as necessary to
                                             			 resolve each conflict.

#### Linking Unity Connection Servers with an Intrasite Link

To create a Unity Connection site, you start by linking two servers together via an intrasite link. Each server becomes a
                                 location in the new site. (When a Unity Connection cluster is linked to a site, the cluster counts as one location in the
                                 site.)

When you add a Unity Connection server to an existing Unity Connection site of two or more locations, you link the server
                                 to a single location in the site; the server that you are adding receives a list of all the other locations in the site, exchanges
                                 information with each location, and begins replicating directory information with each location.

This section contains two procedures. You should start by doing the first procedure; if Cisco Unity Connection Administration
                                 does not indicate that the servers have successfully been linked in the first procedure, do the second procedure. Then, repeat
                                 the process for each additional server that you are adding to the site.

#### Automatically
                              	 Joining Two Unity Connection Servers

Step 1

In Cisco Unity Connection Administration (on either server), expand Networking > Links > and select Intrasite Links . (In Cisco Unity Connection, expand Networking , then select Unity Connection Locations .)

Step 2

Select Join Site . (In Unity Connection, select Join Unity Connection Network .)

Step 3

On the Join Site page, select Automatically Join the Site . (In Unity Connection, on the Join Unity Connection Network page, select Automatically Join the Network .)

Step 4

In the Remote Location field, enter the IP address or
                                             			 fully-qualified domain name (FQDN) of the Unity Connection server to connect to
                                             			 in order to create the site.

Step 5

In the Remote User Name field, enter the user name of an
                                             			 administrator at the location specified in the Remote Location field. The
                                             			 administrator user account must be assigned the System Administrator role.

Step 6

In the Remote Password field, enter the password for the
                                             			 administrator specified in the Remote User Name field.

Step 7

Select Auto Join Site . (In Unity Connection, select Auto Join Network .)

Step 8

When prompted, select OK to confirm. If the status message indicates that
                                             			 you have successfully joined the network and need to activate and start the
                                             			 Unity Connection Digital Networking Replication Agent, continue with Step 9 .
                                             			 Otherwise, skip the rest of this procedure and continue with the “Manually
                                                				Joining Two Unity Connection Servers” procedure .

Step 9

On either server, in Cisco Unity Connection Serviceability, select Tools > Service Management . (For information on using Cisco Unity Connection Serviceability, see the Administration Guide for Cisco Unity Connection Serviceability Release 15 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .)

Step 10

In the Server list, select the Unity Connection server, and
                                             			 select Go .

Step 11

Under Optional Services, locate the Connection Digital
                                             			 Networking Replication Agent and select Activate .

Step 12

Repeat Step 9 through Step 11 on the other server.

#### Manually Joining
                              	 Two Unity Connection Servers

Step 1

In Cisco Unity Connection Administration (on either server),
                                             			 expand Networking > Links > and select Intrasite Links . This server is referred to as the
                                             			 first server for the remainder of the procedure, and the other server is
                                             			 referred to as the second server. (In Unity Connection 7.x, expand Networking , then select Unity Connection Locations .)

Step 2

Select Join Site . (In Unity Connection 7.x, select Join Unity Connection Network .)

Step 3

On the Join Site page, select Manually Join the Site . (In Unity Connection 7.x,
                                             			 select Manually Join the Network .)

Step 4

Select Download and save the first server configuration
                                             			 file to a location on your hard drive, or on media that you can use to copy the
                                             			 file to the second server.

Step 5

Browse to Unity Connection Administration on the second server.

Step 6

In Unity Connection Administration on the second server, expand Networking > Links > and select Intrasite Links . (In Unity Connection 7.x, expand Networking , then select Unity Connection Locations .)

Step 7

Select Join Site . (In Unity Connection 7.x, select Join Unity Connection Network .)

Step 8

On the Join Site page, select Manually Join the Site . (In Unity Connection 7.x,
                                             			 select Manually Join the Network .)

Step 9

Select Download , and save the second server configuration
                                             			 file to a location on your hard drive, or on media that you can use to copy the
                                             			 file to the second server.

Step 10

In the Select the Remote Configuration File to Upload field,
                                             			 select Browse and browse to the copy of the configuration
                                             			 file that you downloaded from the first server in Step 4 .

Step 11

Select Upload .

Step 12

In Unity Connection Administration on the first server, in the
                                             			 Select the Remote Configuration File to Upload field, select Browse and browse to your local copy of the
                                             			 configuration file that you downloaded from the second server in Step 9 .

Step 13

Select Upload .

Step 14

On either server, in Cisco Unity Connection Serviceability,
                                             			 select Tools > Service
                                                   				  Management .

Step 15

In the Server list, select the Unity Connection server, and
                                             			 select Go .

Step 16

Under Optional Services, locate the Unity Connection Digital
                                             			 Networking Replication Agent and select Activate .

Step 17

Repeat Step 14 through Step 16 on the
                                             			 other server.

#### Configuring a Smart Host

SMTP is used to transmit both directory information and messages between Unity Connection locations in a site.

If any pair of locations in the site cannot transmit and receive SMTP messages directly (for example, because a firewall separates
                                 the servers), you must configure these locations to route these messages through an SMTP smart host.

In addition, for each Unity Connection cluster that you add to the site, you must configure all other network locations to
                                 route to the cluster through a smart host in order for message traffic to reach the cluster subscriber server in the event
                                 that the publisher server is down, and configure the smart host to resolve the SMTP domain of the cluster to the IP addresses
                                 of both the publisher and subscriber servers. For example, a network has a single smart host and the following three locations:

ServerA, which is not a cluster member

Cluster 1, which is made up of ServerB, a publisher, and ServerC, a subscriber

Cluster 2, which is made up of ServerD, a publisher, and ServerE, a subscriber

In order to create a Unity Connection site, you would join ServerA, ServerB and ServerD together to form the site. Note the
                                 following:

On ServerA, you would configure the Unity Connection locations for ServerB (which represents cluster 1) and ServerD (which
                                       represents cluster 2) to route through the smart host.

On Server B (the cluster 1 publisher), you would configure the Unity Connection location for ServerD (which represents cluster
                                       2) to route through the smart host.

On ServerD (the cluster 2 publisher), you would configure the Unity Connection location for ServerB (which represents cluster
                                       1) to route through the smart host.

On the smart host, you would configure the SMTP domain name of cluster 1 to resolve to the IP addresses of both ServerB and
                                       ServerC (for example, using DNS MX records). You would also configure the SMTP domain name of cluster 2 to resolve to both
                                       ServerD and ServerE.

Do the following tasks for each server that requires routing to other locations through a smart host:

Configure the SMTP smart host to accept messages from the Unity Connection server. If your site includes Unity Connection
                                       clusters, also configure the smart host to resolve the SMTP domain of the cluster to the IP addresses of both the publisher
                                       and subscriber servers. See the documentation for the SMTP server application that you are using.

Configure the Unity Connection server to relay messages to the smart host. See the “Configuring Unity Connection to Relay Messages to a Smart Host” procedure on page 2-9 .

Configure the Unity Connection server to route messages to the other Unity Connection locations through the smart host. See
                                       the “Configuring Unity Connection to Route Inter-Location Messages through the Smart Host” procedure on page 2-9 .

#### Configuring Unity
                              	 Connection to Relay Messages to a Smart Host

Step 1

In Cisco Unity Connection Administration, expand System Settings > SMTP
                                                   				  Configuration and select Smart Host .

Step 2

In the Smart Host field, enter the IP address or fully
                                             			 qualified domain name of the SMTP smart host server. (Enter the fully qualified
                                             			 domain name of the server only if DNS is configured.)

To avoid infinite loop of SMTP notification in the mailbox, do not enter the IP address or fully qualified domain name of
                                                            the following server as SMTP smart host:

The localhost in case of standalone server

The publisher and subscriber server in case of a cluster

The servers that are networked together

Step 3

Select Save .

#### Configuring Unity
                              	 Connection to Route Inter-Location Messages through the Smart Host

Step 1

In Cisco Unity Connection Administration, expand Networking and
                                             			 select Locations .

Step 2

Select the name of a location that requires routing through a
                                             			 smart host.

Step 3

Check the Route to This Remote Location Through SMTP Smart
                                                				Host check box.

Step 4

Select Save .

Step 5

Repeat Step 1 through Step 4 for
                                             			 each additional location that requires routing through the smart host.

#### Configuring SMTP
                              	 Access for Cluster Subscriber Servers

When you create a site that includes a Unity Connection cluster
                                 		server pair, you join only the publisher server of the pair to the site. In
                                 		order for all locations on the network to communicate directly with the cluster
                                 		subscriber server in the event that it has Primary status, you must configure
                                 		all network locations (except for the publisher server that is clustered with
                                 		the subscriber server) to allow SMTP connections from the subscriber server.

Direct SMTP connectivity is needed so that locations can
                                 		continue to receive user message traffic from the cluster while the publisher
                                 		server does not have Primary status, in cases where routing from the cluster to
                                 		other locations is not done via a smart host. Direct SMTP connectivity with the
                                 		subscriber server does not impact directory updates, because directory updates
                                 		are only replicated from the publisher server.

For example, a network has the following three locations:

ServerA, which is not a cluster member

Cluster 1, which is made up of ServerB, a publisher, and
                                       			 ServerC, a subscriber

Cluster 2, which is made up of ServerD, a publisher, and
                                       			 ServerE, a subscriber

In order to create a site, you would join ServerA, ServerB and
                                 		ServerD together. For direct SMTP access, the following steps are required:

On ServerA, you would need to add the IP addresses of both
                                       			 ServerC and ServerE (the two subscriber servers) to the IP address access list
                                       			 so that ServerA can communicate with either subscriber server if it has Primary
                                       			 status.

On ServerB (the cluster 1 publisher), you would add the IP
                                       			 address of ServerE (the cluster 2 subscriber) to the IP address access list;
                                       			 and on ServerD (the cluster 2 publisher), you would add the IP address of
                                       			 ServerC (the cluster 1 subscriber) to the IP address access list.

Alternatively, you can configure each cluster location to route
                                 		messages to every other location through a smart host; when you do this, the
                                 		other Unity Connection locations do not need to accept SMTP connections
                                 		directly from the cluster subscriber in the event that it has Primary status,
                                 		because the cluster subscriber establishes the SMTP connection with the smart
                                 		host rather than directly with every other location. In the example above, the
                                 		alternate configuration would entail the following:

On ServerB (the cluster1 publisher), you would configure a smart
                                       			 host, and configure the Unity Connection locations for ServerA and ServerD (the
                                       			 cluster 2 publisher) to route through the smart host.

On ServerD (the cluster 2 publisher), you would configure a
                                       			 smart host, and configure the Unity Connection locations for ServerA and
                                       			 ServerB (the cluster 1 publisher) to route through the smart host.

For instructions on configuring routing through a smart host,
                                 		see the “Configuring
                                    		  a Smart Host” section on page 2-8 . Note that when more than one cluster
                                 		is joined to a single site, you should have already configured each cluster to
                                 		route messages to other clusters through the smart host; in this case, all you
                                 		need do in addition is to configure the cluster to route through the smart host
                                 		to any servers that are not configured as clusters.

#### Configuring Direct
                              	 SMTP Access for Cluster Subscriber Servers

Step 1

On a network location, in Cisco Unity Connection Administration,
                                             			 expand System Settings > SMTP
                                                   				  Configuration and select Server .

Step 2

On the Edit menu, select Search IP Address Access List .

Step 3

Select Add New .

Step 4

On the New Access IP Address page, enter the IP address of a
                                             			 cluster subscriber server at another location on the network.

Do not enter the IP address of the subscriber server on the
                                                            				  publisher server that it is paired with.

Step 5

Select Save .

Step 6

On the Access IP Address page, check the Allow Unity Connection check box.

Step 7

Select Save .

Step 8

Repeat Step 2 through Step 7 for
                                             			 each additional subscriber server on the network (other than the subscriber
                                             			 server that is paired with the server you are configuring).

Step 9

Repeat Step 1 through Step 8 on each
                                             			 network location.

#### Checking
                              	 Replication Status Within a Site

When initial replication begins among locations, it can take a
                                 		few minutes to a few hours for data to be fully replicated between all
                                 		locations, depending on the size of your directory.

The Unity Connection Intrasite Links and Locations pages in
                                 		Cisco Unity Connection Administration can provide information about the status
                                 		of replication between locations. Do the following procedure to check
                                 		replication status in Unity Connection Administration.

Tip

##### Checking
                                 	 Replication Status Within a Site Using Cisco Unity Connection
                                 	 Administration

Step 1

In Cisco Unity Connection Administration on a server that is joined to the network, expand Networking > Links and select Intrasite Links .

Step 2

On the Search Intrasite Links
                                                			 page, in the Intrasite Links table, the Push Directory column indicates whether
                                                			 a directory push to the remote location from the location you are accessing is
                                                			 in progress. The Pull Directory column indicates whether a directory pull from
                                                			 the remote location is in progress.

For example, if an
                                                   				administrator initiates a Push Directory To request from ServerA to ServerB,
                                                   				the Unity Connection Administration on ServerA shows that a directory push to
                                                   				ServerB is in progress, and the Unity Connection Administration on ServerB
                                                   				shows that a directory pull from ServerA is in progress.

Caution

Step 3

To get more information about the status of replication with a particular remote location, expand Networking and select Locations , then select the display name of the location.

Step 4

On the Edit Location page, the Last USN Sent, Last USN Received,
                                                			 and Last USN Acknowledged fields indicate the sequence numbers of replication
                                                			 messages sent to and from the remote location. If the Last USN Sent value is
                                                			 higher than the Last USN Acknowledged value, the remote location is not
                                                			 currently fully synchronized with this location; in this case, the Last USN
                                                			 Acknowledged value should continue to increase periodically. (Note that the
                                                			 Last USN Sent value may also increase periodically.)

#### Configuring Search
                              	 Spaces for Unity Connection Sites

When you initially set up a site between locations, users who
                                 		are homed on one location are not able to address messages to users at other
                                 		locations, because the users on each location are in separate partitions and
                                 		use search spaces that do not contain the partitions of users on the other
                                 		locations. After initial replication completes between the locations, you can
                                 		reconfigure your search spaces to include partitions that are homed on other
                                 		servers, and you can change the search scope of users, routing rules, call
                                 		handlers, directory handlers, and VPIM locations to use a search space that is
                                 		homed on a remote location. (Note that while both partitions and search spaces
                                 		are replicated between locations, you cannot assign users or other objects to a
                                 		partition that is homed on another location.)

At a minimum, if you have not made any changes to the default
                                 		partitions and search spaces on any server, at each location you can add the
                                 		default partition of each remote Unity Connection location to the search space
                                 		that local users are using. For example, in a network of three servers named
                                 		ServerA, ServerB, and ServerC with no changes to the system defaults, in
                                 		Cisco Unity Connection Administration on ServerA you would add the “ServerB
                                 		Partition” and “ServerC Partition” default partitions as members of the
                                 		“ServerA Search Space” default search space; in Unity Connection Administration
                                 		on ServerB you would add “ServerA Partition” and “ServerC Partition” to
                                 		“ServerB Search Space,” and so on.

For instructions on adding partitions to search spaces, see the “ Dial Plan ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

#### Securing the Unity Connection Site

No user credentials are transmitted as part of intrasite communications. However, in order to protect the security of SMTP
                                 addresses that are contained in the messages, make sure that any smart hosts that are involved in SMTP message transmission
                                 between Unity Connection locations are configured to route messages properly, as it may be possible to extract SMTP addresses
                                 from the messages. See the documentation for the SMTP server application that you are using for instructions.

#### Testing the Intrasite Setup

To test the site configuration, create test user accounts or use existing user accounts on each Unity Connection location.
                                 When setting up user accounts in Cisco Unity Connection Administration to be used in the tests, be sure to do the following
                                 for each account:

Record a voice name.

Record and enable an internal greeting.

On the User Basics page, for Search Scope, select a search space that includes the partitions of remote users.

On the User Basics page, check the List in Directory check box.

On the Playback Message Settings page, check the Before Playing Each Message, Play the Sender's Information check box.

Optionally, if you plan to enable and test cross-server live reply, ensure that the account belongs to a class of service
                                       for which the Users Can Reply to Messages from Other Users by Calling Them check box is checked on the Edit Class of Service >
                                       Message Options page. (The check box is not checked by default.)

Do the following tests to confirm that the site is functioning properly:

#### Verifying
                              	 Messaging Between Users on Different Unity Connection Locations

Step 1

Sign in to a Unity Connection location as a user.

Step 2

Follow the prompts to record and send messages to users who are
                                             			 associated with other Unity Connection locations.

Step 3

Sign in to the applicable Unity Connection location as the
                                             			 recipient user to verify that the message was received.

Step 4

Repeat Step 1 through Step 3 in the
                                             			 opposite direction.

#### Verifying Call
                              	 Transfers From the Automated Attendant to Users on Other Unity Connection
                              	 Locations

Step 1

From a non-user phone, call a Unity Connection location that has
                                             			 been configured to handle outside callers, and enter the extension of a user
                                             			 who is associated with another Unity Connection location.

Step 2

Verify that you reach the correct user phone.

#### Verifying Call
                              	 Transfers from a Directory Handler to Users on Other Unity Connection
                              	 Locations

Step 1

From a non-user phone, call a Unity Connection location that has
                                             			 been configured to handle outside callers, and transfer to a directory handler.

Step 2

Verify that you can find a user who is associated with another
                                             			 Unity Connection location in the phone directory, and that the directory
                                             			 handler transfers the call to the correct user phone.

#### Verifying
                              	 Identified User Messaging Between Networked Users (When Identified User
                              	 Messaging is Enabled)

Step 1

Verify that Unity Connection plays an internal greeting for
                                             			 users who leave messages, by doing the following sub-steps:

From a user phone, call a user who is associated with another
                                                   				  Unity Connection location, and allow the call to be forwarded to Unity
                                                   				  Connection.

Verify that the internal greeting plays.

Leave a test message.

Step 2

Verify that users are identified when the recipient listens to a
                                             			 message, by doing the following sub-steps:

Sign in to the applicable Unity Connection location as the
                                                   				  recipient user and listen to the test message that you recorded in Step 1 .

Verify that the user conversation announces who the message is
                                                   				  from by playing the recorded voice name of the sending user.

After listening to the message, verify that the user
                                                   				  conversation allows you to reply to the message.

#### Verifying Live
                              	 Reply Between Users on Different Unity Connection Locations

Step 1

From a user phone, call a user who is associated with another
                                             			 Unity Connection location, and allow the call to be forwarded to voicemail.

Step 2

Leave a message.

Step 3

Sign in to the applicable Unity Connection location as the
                                             			 recipient user and listen to the test message that you recorded in Step 2 .

Step 4

After listening to the message, verify that the user conversation allows you to live reply to the message by saying “Call
                                             sender” or using the applicable key presses for the user conversation type. (To find the key presses for a particular conversation,
                                             see the “ Cisco Unity Connection Phone Menus and Voice Commands ” chapter of the User Guide for the Cisco Unity Connection Phone Interface, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/phone/b_15cucugphone.html .)

Step 5

Verify that the live reply call is correctly transferred to the
                                             			 phone of the user who left the message.

#### Creating a
                              	 Site-Wide All Voicemail Users Distribution List

If you would like to create a master distribution list that
                                 		includes all users on all servers in the site, do the following tasks:

On each location in the site, rename the All Voicemail Users list with a unique name (for example All Voicemail Users on <Location
                                       Name>). For instructions, see the “ System Distribution List ” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Create a new All Voicemail Users system distribution list on one
                                       			 location to use as the master list.

Add the lists from all locations as members of the master list.

Put all lists except the master list in partitions that do not
                                       			 belong to a search space that users use, so that they cannot address to any
                                       			 list except the master. For example, on each location, create a new partition
                                       			 called Hidden DLs on <Location Name> and put the list homed at that
                                       			 location in that partition. (By default, new partitions are not a member of any
                                       			 search space.)

Tip

#### Cleaning Up Unused
                              	 Unity Connection VPIM Locations and Contacts

After migrating a Unity Connection server from VPIM Networking
                                 		to being a member of a site, you should delete the VPIM location for the server
                                 		on any other servers in the site that were previously using VPIM Networking to
                                 		exchange messages with the server. Likewise, you should delete any VPIM
                                 		locations on the server that represent other Unity Connection locations in the
                                 		site. In order to successfully delete the VPIM locations, you must first delete
                                 		all contacts that are associated with the location.

Note that when you delete the VPIM contacts that represent Unity
                                 		Connection users, the contacts are removed from distribution lists; consider
                                 		reviewing and updating distribution list membership on each server to include
                                 		remote users as applicable. Also consider notifying users that they need to
                                 		update the membership of any private lists that include contacts on the server
                                 		being migrated.

For instructions on deleting a VPIM location and the associated
                                 		VPIM contacts, see the “ Removing
                                    		  a VPIM Location ”

#### Mapping Users to
                              	 Their Home Locations

Each server or cluster handles a distinct group of users. In
                                 		large organizations, it is possible that more than one server or cluster is in
                                 		use at the same physical location. In this case, you need to determine which
                                 		user accounts to create on each of the servers (the “home” server or location
                                 		for each user), and keep a record of the mapping. This record is needed for the
                                 		following reasons:

User phones must forward calls to the system on which the users
                                       			 are homed.

If user phones have a “Messages” or a speed-dial button that
                                       			 dials the number to access voicemail, the buttons must be configured to call
                                       			 the system on which the users are homed.

If you do not configure cross-server sign-in, users must dial
                                       			 the pilot number of the server or cluster that they are associated with to
                                       			 check their messages; in this case, you need to tell users the correct number
                                       			 to dial when calling their home server.

To create a record of the mapping, run the Users report on each Unity Connection location. The information in this report
                                 includes the user name and primary location. For more information, see the “ Reports ” section of the “Advanced System Settings” chapter in the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

## Linking Two Unity
                        	 Connection Sites

Unity Connection 15 supports linking up to two sites with an intersite link. In order to link sites, all servers in each site
                           must be running Unity Connection version 10.x.

You can link up to 10 Unity Connection servers and/or clusters
                           		in a single site, and link two sites together. (Only one intersite link is
                           		supported per site.) If either site consists of more than one server or
                           		cluster, set up the sites before linking them. For procedures, see the “Setting
                              		  Up a Unity Connection Site” section on page 2-1 .

### Prerequisites

If either or both sites consist of more than one server or
                                    			 cluster, set up the sites according to the “Setting
                                       				Up a Unity Connection Site” section on page 2-1 .

Verify that each server is running Unity Connection version 15.

Check the size of your directory against the limits in the
                                    			 System Requirements for Cisco Unity Connection.

The two locations (one in each site) that act as the gateways
                                    			 between the sites must be able to route directly to each other through TCP/IP
                                    			 port 25 (SMTP), or SMTP messages must be routable through an SMTP smart host.
                                    			 In addition, both gateways must be able to route to each other via HTTP on port
                                    			 80 or HTTPS on port 443.

Identify an account that you use to access Cisco Unity
                                    			 Connection Administration. The account must have the Manage Servers privilege.
                                    			 (The System Administrator and Technician roles each have this privilege.)

### Task List for
                           	 Linking Unity Connection Sites

Use this task list to set up an intersite link between two Unity
                              		Connection sites (referred to as an intersite link). The cross-references take
                              		you to detailed procedures.

If you have a Unity Connection cluster, do the tasks only on the
                              		publisher server.

Decide which location in each site is the site gateway and
                                    			 determine how messages are routed between the gateways. See the “Determining
                                       				the Site Gateway Locations and SMTP Routing Between Gateways” section on
                                       				page 2-17 .

Check the display name of each server in each site, and modify
                                    			 it if it is not unique among all the locations in both sites, or if you want to
                                    			 select a more descriptive name. Also check the SMTP domain of each server, and
                                    			 modify it if it is not unique. For a procedure, see the “Verifying
                                       				Each Unity Connection Server has a Unique Display Name and SMTP Domain” section
                                       				on page 2-4 .

Create the link. See the " Creating
                                       				the Intersite Link " section.

Verify that replication is complete between the sites. See the “Checking
                                       				the Status of Synchronization Between Unity Connection Sites and Configuring
                                       				Task Schedules” section on page 2-20 .

Configure search spaces between sites. See the “Configuring
                                       				Search Spaces Between Unity Connection Sites” section on page 2-21 .

Optionally, if you select to synchronize system distribution
                                    			 lists in either or both directions between the gateways, configure individual
                                    			 distribution lists to allow or prevent replication. See the “Configuring
                                       				Individual System Distribution Lists for Synchronization” section on
                                       				page 2-22 .

Optionally, set up an organization-wide All Users distribution
                                    			 list. See the “Creating
                                       				an Organization-Wide All Voicemail Users Distribution List” section on
                                       				page 2-22 .

Optionally, set up cross-server features between the locations.
                                    			 See the “Cross-Server
                                       				Sign-In, Transfers, and Live Reply” chapter.

For each site, if any servers in the remote site were previously
                                    			 configured as VPIM locations on other servers in the local site, clean up the
                                    			 unused VPIM locations. See the “Cleaning
                                       				Up Unused Unity Connection VPIM Locations and Contacts” section on
                                       				page 2-15 .

### Procedures for Linking Unity Connection Sites

#### Determining the Site Gateway Locations and SMTP Routing Between Gateways

To create an intersite link, you select a single location on each site to act as a gateway to the other site. All intersite
                                 communications (both for directory synchronization and for message exchange) pass between the two gateways, thereby limiting
                                 the connectivity requirements and bandwidth usage to the link between those two locations. In order for directory synchronization
                                 and message exchange to occur between the two sites, the gateways you select must have the following connectivity with each
                                 other:

HTTPS (if you select to encrypt the connection) or HTTP connectivity, for directory synchronization.

SMTP connectivity, for message exchange.

Once you have selected the gateway locations, determine how to route SMTP messages between them. In each direction, you can
                                 route messages directly or use an SMTP smart host. Use an SMTP smart host in the following situations:

The gateways are separated by a firewall that blocks SMTP transmissions.

Either or both of the gateways are Unity Connection clusters.

When a gateway is a cluster, you must configure the opposite gateway to route to the cluster through a smart host in order
                                 for message traffic to reach the cluster subscriber server in the event that the publisher server is down, and configure the
                                 smart host to resolve the SMTP domain of the cluster to the IP addresses of both the publisher and subscriber servers. In
                                 this case, you should route traffic in both directions through the smart host.

#### Creating the
                              	 Intersite Link

This section contains two procedures:

If your Unity Connection site gateways route
                                       			 SMTP messages directly with each other, do the “ Automatically
                                          				Linking Two Unity Connection Site Gateways ” .

If your Unity Connection site gateways require
                                       			 a smart host for routing SMTP messages (for example, because they are separated
                                       			 by a firewall, or because either or both gateways are clusters), do the “Manually
                                          				Linking Two Unity Connection Site Gateways” procedure on page 2-18 .

##### Automatically
                                 	 Linking Two Unity Connection Site Gateways

Step 1

In Cisco Unity Connection Administration (on
                                                			 either server), expand Networking > Links > and select Intersite Links .

Step 2

On the Search Intersite Links page, select Add .

Step 3

On the New Intersite Link page, select Link
                                                			 to Cisco Unity Connection Site Using Automatic Configuration Exchange Between
                                                			 Servers.

Step 4

In the SMTP routing warning message window,
                                                			 select OK .

Step 5

In the Hostname field, enter the IP address
                                                			 or fully-qualified domain name (FQDN) of the remote Unity Connection site
                                                			 gateway to link to.

Step 6

In the Username field, enter the user name
                                                			 of an administrator at the location specified in the Hostname field. The
                                                			 administrator account must be assigned to a role that has the Manage Servers
                                                			 privilege. (The System Administrator and Technician roles have this privilege.)

Step 7

In the Password field, enter the password
                                                			 for the administrator specified in the Username field.

Step 8

For Transfer Protocol settings, decide
                                                			 whether you want to enable SSL to encrypt directory synchronization traffic
                                                			 between the sites.

Step 9

For Synchronization Settings, check the
                                                			 Include Distribution Lists When Synchronizing Directory Data check box to pull
                                                			 information about remote system distribution lists to the local site so that
                                                			 users can address messages to them. (Note that only the list name and other
                                                			 information used in addressing are replicated.)

In order for local system distribution
                                                               				  lists to be offered to the remote site for synchronization, they must also be
                                                               				  marked to allow synchronization. By default, Unity Connection system
                                                               				  distribution lists are marked to allow synchronization, although this setting
                                                               				  may have been changed. The task list alerts you when and how to enable lists
                                                               				  for synchronization.

Step 10

To convert recorded names from this site to
                                                			 a different encoding when synchronizing them with the remote site, check the Convert Outgoing Recorded Names
                                                   				to check box, and select the codec to use.

Step 11

By default, two tasks that each run on their
                                                			 own schedule for data and recorded name directory synchronization from the
                                                			 remote site are enabled immediately after you create the intersite link. To
                                                			 disable either type of directory synchronization until you manually edit and
                                                			 enable the applicable synchronization task, uncheck the Enable Task to Synchronize Directory
                                                   				Data After the Join or Enable Task to Synchronize Recorded
                                                   				Names After the Join check boxes.

Step 12

Select Link .

Step 13

When prompted, select OK to confirm.

##### Manually Linking
                                 	 Two Unity Connection Site Gateways

Step 1

In Cisco Unity Connection Administration (on either site
                                                			 gateway), expand Networking > Links and select Intersite Links . This server is referred to as the
                                                			 first site gateway for the remainder of the procedure, and the other gateway is
                                                			 referred to as the second site gateway.

Step 2

On the Search Intersite Links page, select Add .

Step 3

On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                                   				Manually Exchanging Configuration Files .

Step 4

Select Download and save the first site gateway
                                                			 configuration file to a location on your hard drive, or on media that you can
                                                			 use to copy the file to the second site gateway.

Step 5

Browse to Unity Connection Administration on the second site
                                                			 gateway.

Step 6

In Unity Connection Administration on the second site gateway,
                                                			 expand Networking , expand Links , then select Intersite Links .

Step 7

On the Search Intersite Links page, select Add .

Step 8

On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                                   				Manually Exchanging Configuration Files .

Step 9

Select Download , and save the second site gateway
                                                			 configuration file to a location on your hard drive, or on media that you can
                                                			 use to copy the file to the second site gateway.

Step 10

In the Remote Site Configuration File field, select Browse and browse to the copy of the configuration
                                                			 file that you downloaded from the first site gateway in Step 4 .

Step 11

For Transfer Protocol settings, decide whether you want to
                                                			 enable SSL to encrypt the data passed between the site gateways when the local
                                                			 reader service synchronizes with the remote gateway (local reader requests and
                                                			 remote feeder responses).

Step 12

For Synchronization Settings, check the Include Distribution
                                                			 Lists When Synchronizing Directory Data check box to pull information about
                                                			 remote system distribution lists to the local site so that users can address
                                                			 messages to them. (Note that only the list name and other information used in
                                                			 addressing are replicated.)

In order for local system distribution lists to be offered to
                                                               				  the remote site for synchronization, they must also be marked to allow
                                                               				  synchronization. By default, Unity Connection system distribution lists are
                                                               				  marked to allow synchronization, although this setting may have been changed.
                                                               				  The task list alerts you when and how to enable lists for synchronization.

Step 13

To convert recorded names from this site to a different encoding
                                                			 when synchronizing them with the remote site, check the Convert Outgoing Recorded Names to check box, and
                                                			 select the codec to use.

Step 14

By default, two tasks that each run on their own schedule for
                                                			 data and recorded name directory synchronization from the remote site are
                                                			 enabled immediately after you create the intersite link. To disable either type
                                                			 of directory synchronization until you manually edit and enable the applicable
                                                			 synchronization task, uncheck the Enable Task to Synchronize Directory Data After the
                                                   				Join or Enable Task to Synchronize Recorded Names After the
                                                   				Join check boxes.

Step 15

For Intersite Routing, select the appropriate option:

Route to this Remote Site Through—Enter the specific IP address
                                                         					 or fully-qualified domain name of a smart host that can properly route messages
                                                         					 sent to addresses at the SMTP domain of the remote site gateway.

Route to this Remote Site Through SMTP Smart Host (If One Is
                                                         					 Defined)—Routes outgoing messages to the host defined on the System
                                                         					 Settings > SMTP Configuration > Smart Host page. If you select this
                                                         					 option, the smart host must be defined, and must be able to properly route
                                                         					 messages sent to addresses at the SMTP domain of the remote site gateway. If
                                                         					 the smart host is not defined, a non-delivery receipt (NDR) is sent to the
                                                         					 message sender.

Route to this Remote Site Through the Remote Site Gateway—Routes
                                                         					 outgoing messages directly to the remote site gateway SMTP server. Do not use
                                                         					 this option if the remote gateway is a cluster, or if the gateways are
                                                         					 separated by a firewall.

Step 16

Select Link .

Step 17

In Unity Connection Administration on the first site gateway, in
                                                			 the Select the Remote Configuration File to Upload field, select Browse and browse to your local copy of the
                                                			 configuration file that you downloaded from the second server in Step 9 .

Step 18

Repeat Step 11 through Step 15 on the
                                                			 first site gateway.

Step 19

Select Link .

#### Checking the
                              	 Status of Synchronization Between Unity Connection Sites and Configuring Task
                              	 Schedules

When initial synchronization begins between site gateways, it
                                    		  can take a few minutes to a few hours for data to be fully replicated to each
                                    		  gateway, and from there to all locations in the site, depending on the size of
                                    		  your directory.

On each site gateway, there are two tasks which control the
                                    		  schedule on which the Reader polls the remote Feeder for directory data, and
                                    		  the schedule on which it polls for recorded names. By default, the tasks run
                                    		  every 15 minutes. If you unchecked the Enable Task to Synchronize Directory
                                    		  Data After the Join or Enable Task to Synchronize Recorded Names After the Join
                                    		  check boxes while linking the sites, you must configure the schedule and enable
                                    		  the task before synchronization can begin.

You can use the Edit Intersite Link page and the Task Schedule
                                    		  page in Cisco Unity Connection Administration to determine whether
                                    		  synchronization is progressing successfully or has completed. Do the following
                                    		  procedure to check synchronization status between sites, and to configure
                                    		  schedules for the two synchronization tasks.

Step 1

In Cisco Unity Connection Administration on a site gateway,
                                             			 expand Networking > Links and select Intersite Links .

Step 2

On the Search Intersite Links page, select the Display Name of
                                             			 the intersite link.

Step 3

On the Edit Intersite Link page, check the values of the
                                             			 following fields:

Time of Last Synchronization—Indicates the time stamp of the
                                                      					 last time the local reader service attempted to poll the remote site gateway
                                                      					 feeder service for directory changes on the remote site, regardless of whether
                                                      					 a response was received.

Time of Last Error—Indicates the time stamp of the last time the
                                                      					 local reader service encountered an error while attempting to poll the remote
                                                      					 site gateway feeder service. If the value of this field is 0, or if the Time of
                                                      					 Last Synchronization value is later than the Time of Last Error value,
                                                      					 replication is likely to be progressing without problems.

Object Count—Indicates the number of objects (users, system
                                                      					 distribution lists if applicable, partitions, search spaces and Unity
                                                      					 Connection locations) that the local site gateway has synchronized from the
                                                      					 remote site.

Step 4

View the Remote Site Directory Synchronization Task, and enable
                                             			 it or change the schedule, if necessary:

From the Edit Intersite Link page, in the Related Links box in
                                                   				  the upper right corner of the page, select Remote Site Directory Synchronization Task and select Go .

On the Task Schedule page, enable the task if it has not yet
                                                   				  been enabled, and modify the schedule so that the task runs at the desired
                                                   				  interval or time.

Select Save .

To view the task execution history, select Edit > Task Definition Basics . On this page you can
                                                   				  determine whether the task has not started, is in progress, or has completed.
                                                   				  If the task has completed you can select either the Time Started or Time
                                                   				  Completed to view the detailed task results.

Step 5

From the Task Definition Basics page, select Task
                                                   				  Definition > Task
                                                   				  Definitions to go to the list of all tasks.

Step 6

View the Synchronize Voice Names With Remote Network task, and
                                             			 enable it or change the schedule, if necessary:

On the Task Definitions page, select Synchronize Voice Names With Remote Network .

Select Edit > Task Schedules .

On the Task Schedule page, enable the task if it has not yet
                                                   				  been enabled, and modify the schedule so that the task runs at the desired
                                                   				  interval or time.

Select Save .

To view the task execution history, select Edit > Task Definition Basics . On this page you can
                                                   				  determine whether the task has not started, is in progress, or has completed.
                                                   				  If the task has completed you can select either the Time Started or Time
                                                   				  Completed to view the detailed task results.

#### Configuring Search
                              	 Spaces Between Unity Connection Sites

When you initially set up a link between the sites, users who
                                 		are homed on a location in one site are not able to address messages to users
                                 		at locations in the other site, because the users are in separate partitions
                                 		and use search spaces that do not contain the partitions of users on the
                                 		locations in the other site. After initial replication completes between the
                                 		sites, you can reconfigure your search spaces to include partitions that are
                                 		homed on the remote site, and you can change the search scope of users, routing
                                 		rules, call handlers, directory handlers, and VPIM locations to use a search
                                 		space that is homed on a location in the remote site. (Note that while both
                                 		partitions and search spaces are replicated between locations, you cannot
                                 		assign users or other objects to a partition that is homed on another
                                 		location.)

At a minimum, if you have not made any changes to the default
                                 		partitions and search spaces on any server, at each location you can add the
                                 		default partition of each remote site location to the search space that local
                                 		users are using. For example, in an organization where site 1 contains ServerA,
                                 		ServerB, and ServerC and site 2 contains Server D, with no changes to the
                                 		system defaults, in Cisco Unity Connection Administration on ServerA, ServerB,
                                 		and ServerC you would add the “ServerD Partition” default partition as a member
                                 		of the “ServerA Search Space,” “ServerB Search Space,” and “ServerC Search
                                 		Space” default search spaces, respectively; in Unity Connection Administration
                                 		on ServerD you would add “ServerA Partition, “ServerB Partition,” and “ServerC
                                 		Partition” to “ServerD Search Space,” and so on.

For instructions on adding partitions to search spaces, see the “ Dial Plan ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

#### Configuring
                              	 Individual System Distribution Lists for Synchronization

If you checked the Include Distribution Lists When Synchronizing
                                 		Directory Data check box in Step 9 of the “ Automatically
                                    		  Linking Two Unity Connection Site Gateways ” or Step 12 of the " Manually
                                    		  Linking Two Unity Connection Site Gateways ", information about system
                                 		distribution lists created on the remote site can be pulled to the local site.
                                 		However, in order for information about an individual list to be offered to
                                 		another site, the Replicate to Remote Sites Over Intersite Links check box must
                                 		be checked on the Edit Distribution List Basics page for a list. By default,
                                 		Replicate to Remote Sites Over Intersite Links is checked, so individual Unity
                                 		Connection system distribution lists are marked for synchronization by default.
                                 		However, in order to allow contacts as members of a system distribution list,
                                 		you must uncheck Replicate to Remote Sites Over Intersite Links, so if you have
                                 		lists that have been configured to allow contacts as members, they are not
                                 		offered for replication to the remote site.

To disable synchronization for an individual list, uncheck
                                 		Replicate to Remote Sites Over Intersite Links check box. To enable
                                 		synchronization for an individual list, remove any contacts that have been
                                 		added as members and check the Replicate to Remote Sites Over Intersite Links
                                 		check box. To enable or disable synchronization for multiple lists at once, you
                                 		can use either Bulk Edit or the Bulk Administration Tool.

#### Creating an
                              	 Organization-Wide All Voicemail Users Distribution List

If you would like to create a master distribution list that
                                 		includes all users on all servers in both sites, do the following tasks:

On each location in each site, if you have not done so already, rename the All Voicemail Users list with a unique name (for
                                       example All Voicemail Users on <Server Name>). For instructions, see the “ System Distribution List ” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Select one location in the organization to host the master list.
                                       			 Create a new All Voicemail Users system distribution list on one location to
                                       			 use as the master list.

Add the lists from all locations in both sites as members of the
                                       			 master list.

Put all lists except the master list in partitions that do not
                                       			 belong to a search space that users use, so that they cannot address to any
                                       			 list except the master. For example, on each location, create a new partition
                                       			 called Hidden DLs on <Server Name> and put the list homed at that
                                       			 location in that partition. (By default, new partitions are not a member of any
                                       			 search space.)

## Notable Behavior in Networked Unity Connection Servers

### No Results Found When a Directory Handler Search Scope is Set to a Remote System Distribution List in Intersite Networking

If you set the Search Scope of a directory handler to System Distribution List and select a list that is homed on the remote
                              site, no results are returned when callers reach the handler and attempt a search. This happens because list membership is
                              not replicated across intersite links. (This behavior does not apply to voice-enabled directory handlers, which do not have
                              the option to use a system distribution list as the search scope.)

### Users Receiving Multiple Copies of Message Sent to Multiple Distribution Lists in Intersite Networking

When a message is sent to multiple distribution lists, under some circumstances, when the message traverses an intersite link,
                              users who are members of more than one of the lists may receive multiple copies of the message.

### Networked Broadcast Messages Not Supported

Broadcast messages cannot be sent to multiple locations within a site or between sites.

### Networked Dispatch Messages Not Supported

Dispatch messaging is not supported across locations. Dispatch messages addressed to recipients at other locations within
                              a site are delivered to remote users as regular messages. Dispatch messages addressed to remote site recipients are not delivered.
                              You should configure dispatch messaging only when the message recipient is a system distribution list that does not include
                              users on other networked locations.

### Manual Resynchronization Runs Both Directory and Voice Name Synchronization Tasks

The Resync All button on the Search Intersite Links page starts the Synchronize Directory With Remote Network task. When that
                              task completes, it automatically starts the Synchronize Voice Names With Remote Network task. These tasks normally run independently
                              on separate schedules.

### Replication with Unity Connection Clusters

When you add a Cisco Unity Connection cluster to a site or link two sites, you create the intrasite or intersite link only
                              on the publisher server of the pair. Directory updates made on a cluster subscriber server are replicated only from the cluster
                              publisher server. If all locations in the site (and all intersite gateways, if applicable) are properly configured, voice
                              messages continue to be sent to and from the cluster even when the subscriber server has Primary status or the publisher server
                              is shut down. However, in order to keep the directory current on the publisher server, the publisher server should not remain
                              shut down for an extended period of time.

### Adding Remote Users as Private Distribution List Members

When creating private lists, users can add members from other locations if allowed by their search scope, in which case the
                              same set of users who are reachable when addressing a message or placing a call can also be added as members of a private
                              list. Private lists are not replicated to other locations; when a user addresses a message to a private list, the home location
                              of the user expands the distribution list and addresses messages to each individual recipient on the list.

Consider notifying users in the event that the following members are inadvertently removed from their lists:

When you delete a Unity Connection location, remote users at that location are removed from all private lists.

When a VPIM contact becomes a Unity Connection user, the contact is removed from all private lists.

| Note | For each Unity
                                             			 Connection cluster that you have added to the site, you must configure all
                                             			 other locations to route to the cluster through a smart host in order for
                                             			 message traffic to reach the cluster subscriber server in the event that the
                                             			 publisher server is down. (You also configure the smart host to resolve the
                                             			 SMTP domain of the cluster to both the publisher and subscriber servers.) |
|---|---|

| Tip | Select a display name for each server that is descriptive and
                                             		  that helps you identify the location when it is listed among all locations in
                                             		  the organization in Cisco Unity Connection Administration. |
|---|---|

| Step 1 | Check the Display Name of the first server: In Cisco Unity Connection Administration on the first server,
                                                   				  expand Networking and select Locations . On the Search Locations page, note the Display Name of the local
                                                   				  server. Make a list of all Display Names that you can consult later. |
|---|---|
| Step 2 | Check the SMTP domain of the first server: Expand System Settings > SMTP Configuration and select Server . On the SMTP Server Configuration page, note the SMTP Domain of
                                                   				  the local server. |
| Step 3 | Check the Display Name and SMTP Domain Name of all VPIM
                                             			 locations homed on the local server: Expand Networking and select VPIM . On the Search VPIM Locations page, note the Display Name of each
                                                   				  VPIM location. Select the first VPIM location in the table. On the Edit VPIM
                                                   				  Location page, note the SMTP Domain Name of the VPIM location. Select Next and note the SMTP Domain Name of the next VPIM
                                                   				  location. Repeat Step 3d. for each remaining VPIM location. |
| Step 4 | Repeat Step 1 through Step 3 on each location that is joined to the site. |
| Step 5 | If the Display Name of a location conflicts with that of another
                                             			 location, or you want to modify a name to be more descriptive, change one of
                                             			 the display names: To change the Display Name of a Unity Connection location,
                                                      					 follow Step 6 . To change the Display Name of a VPIM location, follow Step 7 . If the Display Names are all unique, skip to Step 9 . |
| Step 6 | Change the Display Name of the Unity Connection location: On the server for which you want to change the Display Name,
                                                   				  expand Networking and select Locations . Select the Display Name of the local server. On the Edit Location page, modify the Display Name value, and
                                                   				  select Save . |
| Step 7 | To change the Display Name of a VPIM location: On the server on which the VPIM location is homed, expand Networking and select VPIM . On the Search VPIM Locations page, select the Display Name of
                                                   				  the location that you want to change. On the Edit VPIM Location page, edit the Display Name value and
                                                   				  select Save . |
| Step 8 | If there are any remaining Display Name conflicts, repeat Step 5 as necessary to
                                             			 resolve each conflict. |
| Step 9 | If the SMTP domain of a server conflicts with that of another
                                             			 location, change one of the domain names: To change the SMTP Domain of a Unity Connection location, follow Step 10 . To change the SMTP Domain Name of a VPIM location, follow Step 11 . |
| Step 10 | To change the SMTP Domain of a Unity Connection location: Expand System Settings > SMTP Configuration , then select Server . On the SMTP Server Configuration page, select Change SMTP Domain , change the value of the SMTP Domain
                                                   				  field, and select Save . Select OK to confirm the change. |
| Step 11 | To change the SMTP Domain Name of a VPIM location: On the server on which the VPIM location is homed, expand Networking and select VPIM . Select the Display Name of the VPIM location for which you want
                                                   				  to change the SMTP Domain Name. On the Edit VPIM Location page, change the value of the SMTP
                                                   				  Domain Name field, and select Save . Changing the SMTP Domain Name of a VPIM location may disrupt
                                                      					 messaging with the remote voice messaging system. |
| Step 12 | If there are any remaining SMTP domain conflicts, repeat Step 9 as necessary to
                                             			 resolve each conflict. |

| Step 1 | In Cisco Unity Connection Administration (on either server), expand Networking > Links > and select Intrasite Links . (In Cisco Unity Connection, expand Networking , then select Unity Connection Locations .) |
|---|---|
| Step 2 | Select Join Site . (In Unity Connection, select Join Unity Connection Network .) |
| Step 3 | On the Join Site page, select Automatically Join the Site . (In Unity Connection, on the Join Unity Connection Network page, select Automatically Join the Network .) |
| Step 4 | In the Remote Location field, enter the IP address or
                                             			 fully-qualified domain name (FQDN) of the Unity Connection server to connect to
                                             			 in order to create the site. |
| Step 5 | In the Remote User Name field, enter the user name of an
                                             			 administrator at the location specified in the Remote Location field. The
                                             			 administrator user account must be assigned the System Administrator role. |
| Step 6 | In the Remote Password field, enter the password for the
                                             			 administrator specified in the Remote User Name field. |
| Step 7 | Select Auto Join Site . (In Unity Connection, select Auto Join Network .) |
| Step 8 | When prompted, select OK to confirm. If the status message indicates that
                                             			 you have successfully joined the network and need to activate and start the
                                             			 Unity Connection Digital Networking Replication Agent, continue with Step 9 .
                                             			 Otherwise, skip the rest of this procedure and continue with the “Manually
                                                				Joining Two Unity Connection Servers” procedure . |
| Step 9 | On either server, in Cisco Unity Connection Serviceability, select Tools > Service Management . (For information on using Cisco Unity Connection Serviceability, see the Administration Guide for Cisco Unity Connection Serviceability Release 15 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .) |
| Step 10 | In the Server list, select the Unity Connection server, and
                                             			 select Go . |
| Step 11 | Under Optional Services, locate the Connection Digital
                                             			 Networking Replication Agent and select Activate . |
| Step 12 | Repeat Step 9 through Step 11 on the other server. |

| Step 1 | In Cisco Unity Connection Administration (on either server),
                                             			 expand Networking > Links > and select Intrasite Links . This server is referred to as the
                                             			 first server for the remainder of the procedure, and the other server is
                                             			 referred to as the second server. (In Unity Connection 7.x, expand Networking , then select Unity Connection Locations .) |
|---|---|
| Step 2 | Select Join Site . (In Unity Connection 7.x, select Join Unity Connection Network .) |
| Step 3 | On the Join Site page, select Manually Join the Site . (In Unity Connection 7.x,
                                             			 select Manually Join the Network .) |
| Step 4 | Select Download and save the first server configuration
                                             			 file to a location on your hard drive, or on media that you can use to copy the
                                             			 file to the second server. |
| Step 5 | Browse to Unity Connection Administration on the second server. |
| Step 6 | In Unity Connection Administration on the second server, expand Networking > Links > and select Intrasite Links . (In Unity Connection 7.x, expand Networking , then select Unity Connection Locations .) |
| Step 7 | Select Join Site . (In Unity Connection 7.x, select Join Unity Connection Network .) |
| Step 8 | On the Join Site page, select Manually Join the Site . (In Unity Connection 7.x,
                                             			 select Manually Join the Network .) |
| Step 9 | Select Download , and save the second server configuration
                                             			 file to a location on your hard drive, or on media that you can use to copy the
                                             			 file to the second server. |
| Step 10 | In the Select the Remote Configuration File to Upload field,
                                             			 select Browse and browse to the copy of the configuration
                                             			 file that you downloaded from the first server in Step 4 . |
| Step 11 | Select Upload . |
| Step 12 | In Unity Connection Administration on the first server, in the
                                             			 Select the Remote Configuration File to Upload field, select Browse and browse to your local copy of the
                                             			 configuration file that you downloaded from the second server in Step 9 . |
| Step 13 | Select Upload . |
| Step 14 | On either server, in Cisco Unity Connection Serviceability,
                                             			 select Tools > Service
                                                   				  Management . |
| Step 15 | In the Server list, select the Unity Connection server, and
                                             			 select Go . |
| Step 16 | Under Optional Services, locate the Unity Connection Digital
                                             			 Networking Replication Agent and select Activate . |
| Step 17 | Repeat Step 14 through Step 16 on the
                                             			 other server. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > SMTP
                                                   				  Configuration and select Smart Host . |
|---|---|
| Step 2 | In the Smart Host field, enter the IP address or fully
                                             			 qualified domain name of the SMTP smart host server. (Enter the fully qualified
                                             			 domain name of the server only if DNS is configured.) Note To avoid infinite loop of SMTP notification in the mailbox, do not enter the IP address or fully qualified domain name of
                                                            the following server as SMTP smart host: The localhost in case of standalone server The publisher and subscriber server in case of a cluster The servers that are networked together | Note | To avoid infinite loop of SMTP notification in the mailbox, do not enter the IP address or fully qualified domain name of
                                                            the following server as SMTP smart host: The localhost in case of standalone server The publisher and subscriber server in case of a cluster The servers that are networked together |
| Note | To avoid infinite loop of SMTP notification in the mailbox, do not enter the IP address or fully qualified domain name of
                                                            the following server as SMTP smart host: The localhost in case of standalone server The publisher and subscriber server in case of a cluster The servers that are networked together |
| Step 3 | Select Save . |

| Note | To avoid infinite loop of SMTP notification in the mailbox, do not enter the IP address or fully qualified domain name of
                                                            the following server as SMTP smart host: The localhost in case of standalone server The publisher and subscriber server in case of a cluster The servers that are networked together |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Networking and
                                             			 select Locations . |
|---|---|
| Step 2 | Select the name of a location that requires routing through a
                                             			 smart host. |
| Step 3 | Check the Route to This Remote Location Through SMTP Smart
                                                				Host check box. |
| Step 4 | Select Save . |
| Step 5 | Repeat Step 1 through Step 4 for
                                             			 each additional location that requires routing through the smart host. |

| Step 1 | On a network location, in Cisco Unity Connection Administration,
                                             			 expand System Settings > SMTP
                                                   				  Configuration and select Server . |
|---|---|
| Step 2 | On the Edit menu, select Search IP Address Access List . |
| Step 3 | Select Add New . |
| Step 4 | On the New Access IP Address page, enter the IP address of a
                                             			 cluster subscriber server at another location on the network. Note Do not enter the IP address of the subscriber server on the
                                                            				  publisher server that it is paired with. | Note | Do not enter the IP address of the subscriber server on the
                                                            				  publisher server that it is paired with. |
| Note | Do not enter the IP address of the subscriber server on the
                                                            				  publisher server that it is paired with. |
| Step 5 | Select Save . |
| Step 6 | On the Access IP Address page, check the Allow Unity Connection check box. |
| Step 7 | Select Save . |
| Step 8 | Repeat Step 2 through Step 7 for
                                             			 each additional subscriber server on the network (other than the subscriber
                                             			 server that is paired with the server you are configuring). |
| Step 9 | Repeat Step 1 through Step 8 on each
                                             			 network location. |

| Note | Do not enter the IP address of the subscriber server on the
                                                            				  publisher server that it is paired with. |
|---|---|

| Tip | On Unity Connection 15 locations, you can also use the Voice Network Map tool in Cisco Unity Connection Serviceability to
                                          check replication status. With the tool, you can quickly locate replication problems in a site, and get information about
                                          the status of replication between any two locations in the site. For more details, select Help > This Page from within the
                                          tool, or see the “ Understanding the Voice Network Map Tool ” section of the “Using the Voice Network Map Tool” chapter of the Administration Guide for Cisco Unity Connection Serviceability Release 15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration on a server that is joined to the network, expand Networking > Links and select Intrasite Links . |
|---|---|
| Step 2 | On the Search Intrasite Links
                                                			 page, in the Intrasite Links table, the Push Directory column indicates whether
                                                			 a directory push to the remote location from the location you are accessing is
                                                			 in progress. The Pull Directory column indicates whether a directory pull from
                                                			 the remote location is in progress. For example, if an
                                                   				administrator initiates a Push Directory To request from ServerA to ServerB,
                                                   				the Unity Connection Administration on ServerA shows that a directory push to
                                                   				ServerB is in progress, and the Unity Connection Administration on ServerB
                                                   				shows that a directory pull from ServerA is in progress. Caution Initial replication happens automatically. Do
                                                               				  not initiate a directory push or pull while initial replication is in progress. Note Once initial replication is complete, changes are automatically
                                                            				synchronized between locations as they occur, even when the Push Directory and
                                                            				Pull Directory columns display a status of Idle. | Caution | Initial replication happens automatically. Do
                                                               				  not initiate a directory push or pull while initial replication is in progress. | Note | Once initial replication is complete, changes are automatically
                                                            				synchronized between locations as they occur, even when the Push Directory and
                                                            				Pull Directory columns display a status of Idle. |
| Caution | Initial replication happens automatically. Do
                                                               				  not initiate a directory push or pull while initial replication is in progress. |
| Note | Once initial replication is complete, changes are automatically
                                                            				synchronized between locations as they occur, even when the Push Directory and
                                                            				Pull Directory columns display a status of Idle. |
| Step 3 | To get more information about the status of replication with a particular remote location, expand Networking and select Locations , then select the display name of the location. |
| Step 4 | On the Edit Location page, the Last USN Sent, Last USN Received,
                                                			 and Last USN Acknowledged fields indicate the sequence numbers of replication
                                                			 messages sent to and from the remote location. If the Last USN Sent value is
                                                			 higher than the Last USN Acknowledged value, the remote location is not
                                                			 currently fully synchronized with this location; in this case, the Last USN
                                                			 Acknowledged value should continue to increase periodically. (Note that the
                                                			 Last USN Sent value may also increase periodically.) |

| Caution | Initial replication happens automatically. Do
                                                               				  not initiate a directory push or pull while initial replication is in progress. |
|---|---|

| Note | Once initial replication is complete, changes are automatically
                                                            				synchronized between locations as they occur, even when the Push Directory and
                                                            				Pull Directory columns display a status of Idle. |
|---|---|

| Step 1 | Sign in to a Unity Connection location as a user. |
|---|---|
| Step 2 | Follow the prompts to record and send messages to users who are
                                             			 associated with other Unity Connection locations. |
| Step 3 | Sign in to the applicable Unity Connection location as the
                                             			 recipient user to verify that the message was received. |
| Step 4 | Repeat Step 1 through Step 3 in the
                                             			 opposite direction. |

| Step 1 | From a non-user phone, call a Unity Connection location that has
                                             			 been configured to handle outside callers, and enter the extension of a user
                                             			 who is associated with another Unity Connection location. |
|---|---|
| Step 2 | Verify that you reach the correct user phone. |

| Step 1 | From a non-user phone, call a Unity Connection location that has
                                             			 been configured to handle outside callers, and transfer to a directory handler. |
|---|---|
| Step 2 | Verify that you can find a user who is associated with another
                                             			 Unity Connection location in the phone directory, and that the directory
                                             			 handler transfers the call to the correct user phone. |

| Step 1 | Verify that Unity Connection plays an internal greeting for
                                             			 users who leave messages, by doing the following sub-steps: From a user phone, call a user who is associated with another
                                                   				  Unity Connection location, and allow the call to be forwarded to Unity
                                                   				  Connection. Verify that the internal greeting plays. Leave a test message. |
|---|---|
| Step 2 | Verify that users are identified when the recipient listens to a
                                             			 message, by doing the following sub-steps: Sign in to the applicable Unity Connection location as the
                                                   				  recipient user and listen to the test message that you recorded in Step 1 . Verify that the user conversation announces who the message is
                                                   				  from by playing the recorded voice name of the sending user. After listening to the message, verify that the user
                                                   				  conversation allows you to reply to the message. |

| Step 1 | From a user phone, call a user who is associated with another
                                             			 Unity Connection location, and allow the call to be forwarded to voicemail. |
|---|---|
| Step 2 | Leave a message. |
| Step 3 | Sign in to the applicable Unity Connection location as the
                                             			 recipient user and listen to the test message that you recorded in Step 2 . |
| Step 4 | After listening to the message, verify that the user conversation allows you to live reply to the message by saying “Call
                                             sender” or using the applicable key presses for the user conversation type. (To find the key presses for a particular conversation,
                                             see the “ Cisco Unity Connection Phone Menus and Voice Commands ” chapter of the User Guide for the Cisco Unity Connection Phone Interface, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/phone/b_15cucugphone.html .) |
| Step 5 | Verify that the live reply call is correctly transferred to the
                                             			 phone of the user who left the message. |

| Tip | To
                                          		avoid users generate large amounts of voice message traffic using reply-all to
                                          		reply to messages sent to the master list, you should use search spaces to
                                          		restrict access to the master list to a small subset of users. These users can
                                          		use a search space that is essentially identical to the search space that other
                                          		users use, except for the addition of the partition containing the master list. |
|---|---|

| Note | When you automatically link two gateways, the
                                                   				settings that you select are configured for both gateways. After creating the
                                                   				link, you can change most settings on either gateway. Or, you can use the
                                                   				manual procedure to configure the settings differently on each gateway. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration (on
                                                			 either server), expand Networking > Links > and select Intersite Links . |
|---|---|
| Step 2 | On the Search Intersite Links page, select Add . |
| Step 3 | On the New Intersite Link page, select Link
                                                			 to Cisco Unity Connection Site Using Automatic Configuration Exchange Between
                                                			 Servers. |
| Step 4 | In the SMTP routing warning message window,
                                                			 select OK . |
| Step 5 | In the Hostname field, enter the IP address
                                                			 or fully-qualified domain name (FQDN) of the remote Unity Connection site
                                                			 gateway to link to. |
| Step 6 | In the Username field, enter the user name
                                                			 of an administrator at the location specified in the Hostname field. The
                                                			 administrator account must be assigned to a role that has the Manage Servers
                                                			 privilege. (The System Administrator and Technician roles have this privilege.) |
| Step 7 | In the Password field, enter the password
                                                			 for the administrator specified in the Username field. |
| Step 8 | For Transfer Protocol settings, decide
                                                			 whether you want to enable SSL to encrypt directory synchronization traffic
                                                			 between the sites. |
| Step 9 | For Synchronization Settings, check the
                                                			 Include Distribution Lists When Synchronizing Directory Data check box to pull
                                                			 information about remote system distribution lists to the local site so that
                                                			 users can address messages to them. (Note that only the list name and other
                                                			 information used in addressing are replicated.) Note When you enable system distribution list
                                                            				synchronization, you cannot disable it after the link is created except by
                                                            				removing and recreating the intersite link. In order for local system distribution
                                                               				  lists to be offered to the remote site for synchronization, they must also be
                                                               				  marked to allow synchronization. By default, Unity Connection system
                                                               				  distribution lists are marked to allow synchronization, although this setting
                                                               				  may have been changed. The task list alerts you when and how to enable lists
                                                               				  for synchronization. | Note | When you enable system distribution list
                                                            				synchronization, you cannot disable it after the link is created except by
                                                            				removing and recreating the intersite link. In order for local system distribution
                                                               				  lists to be offered to the remote site for synchronization, they must also be
                                                               				  marked to allow synchronization. By default, Unity Connection system
                                                               				  distribution lists are marked to allow synchronization, although this setting
                                                               				  may have been changed. The task list alerts you when and how to enable lists
                                                               				  for synchronization. |
| Note | When you enable system distribution list
                                                            				synchronization, you cannot disable it after the link is created except by
                                                            				removing and recreating the intersite link. In order for local system distribution
                                                               				  lists to be offered to the remote site for synchronization, they must also be
                                                               				  marked to allow synchronization. By default, Unity Connection system
                                                               				  distribution lists are marked to allow synchronization, although this setting
                                                               				  may have been changed. The task list alerts you when and how to enable lists
                                                               				  for synchronization. |
| Step 10 | To convert recorded names from this site to
                                                			 a different encoding when synchronizing them with the remote site, check the Convert Outgoing Recorded Names
                                                   				to check box, and select the codec to use. Note If you select a codec at this step, the same codec
                                                            				is configured on both gateways, which means that recorded names are sent in a
                                                            				format that differs from the recording format for at least one of the two
                                                            				gateways. If this is not your intention, do not change the setting now. You can
                                                            				change the setting later on the Edit Intersite Link page on either gateway. | Note | If you select a codec at this step, the same codec
                                                            				is configured on both gateways, which means that recorded names are sent in a
                                                            				format that differs from the recording format for at least one of the two
                                                            				gateways. If this is not your intention, do not change the setting now. You can
                                                            				change the setting later on the Edit Intersite Link page on either gateway. |
| Note | If you select a codec at this step, the same codec
                                                            				is configured on both gateways, which means that recorded names are sent in a
                                                            				format that differs from the recording format for at least one of the two
                                                            				gateways. If this is not your intention, do not change the setting now. You can
                                                            				change the setting later on the Edit Intersite Link page on either gateway. |
| Step 11 | By default, two tasks that each run on their
                                                			 own schedule for data and recorded name directory synchronization from the
                                                			 remote site are enabled immediately after you create the intersite link. To
                                                			 disable either type of directory synchronization until you manually edit and
                                                			 enable the applicable synchronization task, uncheck the Enable Task to Synchronize Directory
                                                   				Data After the Join or Enable Task to Synchronize Recorded
                                                   				Names After the Join check boxes. |
| Step 12 | Select Link . |
| Step 13 | When prompted, select OK to confirm. |

| Note | When you enable system distribution list
                                                            				synchronization, you cannot disable it after the link is created except by
                                                            				removing and recreating the intersite link. In order for local system distribution
                                                               				  lists to be offered to the remote site for synchronization, they must also be
                                                               				  marked to allow synchronization. By default, Unity Connection system
                                                               				  distribution lists are marked to allow synchronization, although this setting
                                                               				  may have been changed. The task list alerts you when and how to enable lists
                                                               				  for synchronization. |
|---|---|

| Note | If you select a codec at this step, the same codec
                                                            				is configured on both gateways, which means that recorded names are sent in a
                                                            				format that differs from the recording format for at least one of the two
                                                            				gateways. If this is not your intention, do not change the setting now. You can
                                                            				change the setting later on the Edit Intersite Link page on either gateway. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration (on either site
                                                			 gateway), expand Networking > Links and select Intersite Links . This server is referred to as the
                                                			 first site gateway for the remainder of the procedure, and the other gateway is
                                                			 referred to as the second site gateway. |
|---|---|
| Step 2 | On the Search Intersite Links page, select Add . |
| Step 3 | On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                                   				Manually Exchanging Configuration Files . |
| Step 4 | Select Download and save the first site gateway
                                                			 configuration file to a location on your hard drive, or on media that you can
                                                			 use to copy the file to the second site gateway. |
| Step 5 | Browse to Unity Connection Administration on the second site
                                                			 gateway. |
| Step 6 | In Unity Connection Administration on the second site gateway,
                                                			 expand Networking , expand Links , then select Intersite Links . |
| Step 7 | On the Search Intersite Links page, select Add . |
| Step 8 | On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                                   				Manually Exchanging Configuration Files . |
| Step 9 | Select Download , and save the second site gateway
                                                			 configuration file to a location on your hard drive, or on media that you can
                                                			 use to copy the file to the second site gateway. |
| Step 10 | In the Remote Site Configuration File field, select Browse and browse to the copy of the configuration
                                                			 file that you downloaded from the first site gateway in Step 4 . |
| Step 11 | For Transfer Protocol settings, decide whether you want to
                                                			 enable SSL to encrypt the data passed between the site gateways when the local
                                                			 reader service synchronizes with the remote gateway (local reader requests and
                                                			 remote feeder responses). |
| Step 12 | For Synchronization Settings, check the Include Distribution
                                                			 Lists When Synchronizing Directory Data check box to pull information about
                                                			 remote system distribution lists to the local site so that users can address
                                                			 messages to them. (Note that only the list name and other information used in
                                                			 addressing are replicated.) Note When you
                                                            				enable system distribution list synchronization, you cannot disable it after
                                                            				the link is created except by removing and recreating the intersite link. In order for local system distribution lists to be offered to
                                                               				  the remote site for synchronization, they must also be marked to allow
                                                               				  synchronization. By default, Unity Connection system distribution lists are
                                                               				  marked to allow synchronization, although this setting may have been changed.
                                                               				  The task list alerts you when and how to enable lists for synchronization. | Note | When you
                                                            				enable system distribution list synchronization, you cannot disable it after
                                                            				the link is created except by removing and recreating the intersite link. In order for local system distribution lists to be offered to
                                                               				  the remote site for synchronization, they must also be marked to allow
                                                               				  synchronization. By default, Unity Connection system distribution lists are
                                                               				  marked to allow synchronization, although this setting may have been changed.
                                                               				  The task list alerts you when and how to enable lists for synchronization. |
| Note | When you
                                                            				enable system distribution list synchronization, you cannot disable it after
                                                            				the link is created except by removing and recreating the intersite link. In order for local system distribution lists to be offered to
                                                               				  the remote site for synchronization, they must also be marked to allow
                                                               				  synchronization. By default, Unity Connection system distribution lists are
                                                               				  marked to allow synchronization, although this setting may have been changed.
                                                               				  The task list alerts you when and how to enable lists for synchronization. |
| Step 13 | To convert recorded names from this site to a different encoding
                                                			 when synchronizing them with the remote site, check the Convert Outgoing Recorded Names to check box, and
                                                			 select the codec to use. |
| Step 14 | By default, two tasks that each run on their own schedule for
                                                			 data and recorded name directory synchronization from the remote site are
                                                			 enabled immediately after you create the intersite link. To disable either type
                                                			 of directory synchronization until you manually edit and enable the applicable
                                                			 synchronization task, uncheck the Enable Task to Synchronize Directory Data After the
                                                   				Join or Enable Task to Synchronize Recorded Names After the
                                                   				Join check boxes. |
| Step 15 | For Intersite Routing, select the appropriate option: Route to this Remote Site Through—Enter the specific IP address
                                                         					 or fully-qualified domain name of a smart host that can properly route messages
                                                         					 sent to addresses at the SMTP domain of the remote site gateway. Route to this Remote Site Through SMTP Smart Host (If One Is
                                                         					 Defined)—Routes outgoing messages to the host defined on the System
                                                         					 Settings > SMTP Configuration > Smart Host page. If you select this
                                                         					 option, the smart host must be defined, and must be able to properly route
                                                         					 messages sent to addresses at the SMTP domain of the remote site gateway. If
                                                         					 the smart host is not defined, a non-delivery receipt (NDR) is sent to the
                                                         					 message sender. Route to this Remote Site Through the Remote Site Gateway—Routes
                                                         					 outgoing messages directly to the remote site gateway SMTP server. Do not use
                                                         					 this option if the remote gateway is a cluster, or if the gateways are
                                                         					 separated by a firewall. |
| Step 16 | Select Link . |
| Step 17 | In Unity Connection Administration on the first site gateway, in
                                                			 the Select the Remote Configuration File to Upload field, select Browse and browse to your local copy of the
                                                			 configuration file that you downloaded from the second server in Step 9 . |
| Step 18 | Repeat Step 11 through Step 15 on the
                                                			 first site gateway. |
| Step 19 | Select Link . |

| Note | When you
                                                            				enable system distribution list synchronization, you cannot disable it after
                                                            				the link is created except by removing and recreating the intersite link. In order for local system distribution lists to be offered to
                                                               				  the remote site for synchronization, they must also be marked to allow
                                                               				  synchronization. By default, Unity Connection system distribution lists are
                                                               				  marked to allow synchronization, although this setting may have been changed.
                                                               				  The task list alerts you when and how to enable lists for synchronization. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration on a site gateway,
                                             			 expand Networking > Links and select Intersite Links . |
|---|---|
| Step 2 | On the Search Intersite Links page, select the Display Name of
                                             			 the intersite link. |
| Step 3 | On the Edit Intersite Link page, check the values of the
                                             			 following fields: Time of Last Synchronization—Indicates the time stamp of the
                                                      					 last time the local reader service attempted to poll the remote site gateway
                                                      					 feeder service for directory changes on the remote site, regardless of whether
                                                      					 a response was received. Time of Last Error—Indicates the time stamp of the last time the
                                                      					 local reader service encountered an error while attempting to poll the remote
                                                      					 site gateway feeder service. If the value of this field is 0, or if the Time of
                                                      					 Last Synchronization value is later than the Time of Last Error value,
                                                      					 replication is likely to be progressing without problems. Object Count—Indicates the number of objects (users, system
                                                      					 distribution lists if applicable, partitions, search spaces and Unity
                                                      					 Connection locations) that the local site gateway has synchronized from the
                                                      					 remote site. |
| Step 4 | View the Remote Site Directory Synchronization Task, and enable
                                             			 it or change the schedule, if necessary: From the Edit Intersite Link page, in the Related Links box in
                                                   				  the upper right corner of the page, select Remote Site Directory Synchronization Task and select Go . On the Task Schedule page, enable the task if it has not yet
                                                   				  been enabled, and modify the schedule so that the task runs at the desired
                                                   				  interval or time. Select Save . To view the task execution history, select Edit > Task Definition Basics . On this page you can
                                                   				  determine whether the task has not started, is in progress, or has completed.
                                                   				  If the task has completed you can select either the Time Started or Time
                                                   				  Completed to view the detailed task results. |
| Step 5 | From the Task Definition Basics page, select Task
                                                   				  Definition > Task
                                                   				  Definitions to go to the list of all tasks. |
| Step 6 | View the Synchronize Voice Names With Remote Network task, and
                                             			 enable it or change the schedule, if necessary: On the Task Definitions page, select Synchronize Voice Names With Remote Network . Select Edit > Task Schedules . On the Task Schedule page, enable the task if it has not yet
                                                   				  been enabled, and modify the schedule so that the task runs at the desired
                                                   				  interval or time. Select Save . To view the task execution history, select Edit > Task Definition Basics . On this page you can
                                                   				  determine whether the task has not started, is in progress, or has completed.
                                                   				  If the task has completed you can select either the Time Started or Time
                                                   				  Completed to view the detailed task results. |

| Note | In order to add lists from the remote site, the gateway of the
                                                			 site on which the master list is homed must have the Include Distribution Lists
                                                			 When Synchronizing Directory Data check box checked on the Edit Intersite Link
                                                			 page, and the lists from each location in the remote site must have the
                                                			 Replicate to Remote Sites Over Intersite Links check box checked on the Edit
                                                			 Distribution List Basics page. |
|---|---|