---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-networking-guide-b-12xcucnetx-b-12xcucnetx-chapter-010-html-0154bd5f82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/networking/guide/b_12xcucnetx/b_12xcucnetx_chapter_010.html
retrieved_at: 2026-08-17T02:37:16.215517+00:00
---

Networking Guide for Cisco Unity Connection Release 12.x

# Networking Guide for Cisco Unity Connection Release 12.x

Updated: August 3, 2017

Chapter: Setting Up Networking Between Cisco Unity and Cisco Unity Connection

## Chapter: Setting Up Networking Between Cisco Unity and Cisco Unity Connection

# Setting Up Networking Between Cisco Unity and Cisco Unity Connection

## Setting Up an
                        	 Intersite Link Between Cisco Unity and Unity Connection Gateways

This section describes the prerequisites for setting up an
                           		intersite link to connect a Cisco Unity server, failover pair, or Digital
                           		Network to a Unity Connection server, cluster, or site, and provides a
                           		high-level task list of all of the tasks that you need to complete for the
                           		setup in the order in which they should be completed. If you are unfamiliar
                           		with intersite link concepts, you should first read the “ Overview
                              		  of Networking Concepts ” chapter and review the task list and procedures
                           		before beginning the setup.

### Prerequisites for
                           	 Linking Cisco Unity to a Digital Network

At least one Cisco Unity release 12.x server is already
                                    			 installed and connected to the network as applicable for your installation. You
                                    			 can link a single Cisco Unity server or a single Cisco Unity Digital Network to
                                    			 Unity Connection.

Your Cisco Unity and Microsoft Exchange environment must be meet
                                    			 the requirements listed in the “Cisco Unity Connection Networking Requirements”
                                    			 section of the Networking Options Requirements , available at http://www.cisco.com/en/US/docs/voice_ip_comm/unity/compatibility/matrix/cunetoptionsreqs.html.

The Cisco Unity server that acts as the gateway to the Unity
                                    			 Connection site must be able to route directly to the Unity Connection site
                                    			 gateway via HTTP on port 80 or HTTPS on port 443.

### Prerequisites for
                           	 Linking Unity Connection to a Digital Network

You can link a single Unity Connection 12.x server or cluster or
                                    			 a single Unity Connection site to a single Cisco Unity server, failover pair,
                                    			 or Digital Network. To link a Unity Connection site, all servers in the site
                                    			 must be running version 12.x.

If you are linking a Unity Connection site, the site has been
                                    			 set up according to the “ Setting
                                       				Up a Unity Connection Site ”.

The Unity Connection site must meet the requirements listed in
                                    			 the “ Requirements for Intersite
                                       				Networking ” section in the System Requirements for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

You have access to an account that has the Manage Servers
                                    			 privilege on the Unity Connection server that serves as the gateway. (The
                                    			 System Administrator and Technician roles each have this privilege.)

The Unity Connection server acts as the gateway to the
                                    			 Cisco Unity site must be able to route directly to the Cisco Unity site gateway
                                    			 via HTTP on port 80 or HTTPS on port 443.

## Task List for
                        	 Setting Up an Intersite Link Between Cisco Unity and Unity Connection
                        	 Gateways

Make decisions about your network topology and gather
                                 			 information needed to configure the intersite link. See the “Making
                                    				Deployment Decisions and Gathering Important Information” section on
                                    				page 3-3 .

Determine the Cisco Unity domain name used for messaging with
                                 			 Unity Connection. See the “Determining
                                    				Cisco Unity Interoperability Domain Name” section on page 3-4 .

Prepare the Cisco Unity gateway by configuring settings on the
                                 			 primary location page, checking permissions, and extending the Active Directory
                                 			 schema. See the “Preparing
                                    				Cisco Unity Gateway” section on page 3-4 .

If you have previously installed the Interoperability Gateway
                                 			 for Microsoft Exchange, do the following to ensure that it is properly
                                 			 configured:

If the Interoperability Gateway is installed on Exchange 2010 or
                                       				  2007, check the foreign connector configuration and configure a Send Connector
                                       				  and a Receive Connector. See the “Configuring
                                          					 a Previously Installed Interoperability Gateway for Unity Connection
                                          					 Interoperability on Exchange 2010 or 2007” section on page 3-7 .

If you have not previously installed the Interoperability
                                 			 Gateway for Microsoft Exchange, install and configure it. (If you are currently
                                 			 using or plan to use VPIM Networking or Trusted Internet locations on
                                 			 Cisco Unity, configure the Interoperability Gateway to handle these types of
                                 			 networking as well as Unity Connection interoperability.) For up-to-date
                                 			 version support and requirements for the Interoperability Gateway, see the
                                 			 Networking Options Requirements for Cisco Unity (Version 5.x and Later),
                                 			 available at http://www.cisco.com/en/US/docs/voice_ip_comm/unity/compatibility/matrix/cunetoptionsreqs.html .

If you uninstalled the Cisco Unity Voice Connector in task 4 . and
                                 			 you still require the Voice Connector to handle Bridge Networking and/or AMIS
                                 			 Networking, reinstall it with only those options configured. See the
                                 			 “Installing the Voice Connector” section of the applicable Release Notes for Cisco Unity Voice Connector for Microsoft
                                    				Exchange , available at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_release_notes_list.html .

Configure the Unity Connection gateway to accept SMTP
                                 			 connections from the Exchange server that delivers messages from Cisco Unity.
                                 			 See the “Configuring
                                    				SMTP Access on the Unity Connection Gateway” section on page 3-10 .

Download the Cisco Unity gateway configuration file. See the “Downloading
                                    				Cisco Unity Gateway Configuration File” section on page 3-11 .

On the Cisco Unity site gateway, set up a template to use when
                                 			 importing Unity Connection users into Cisco Unity. See the “Setting
                                    				Up a Template for Unity Connection Users on the Cisco Unity Gateway” section on
                                    				page 3-11 .

Begin linking the gateways by creating the intersite link in
                                 			 Cisco Unity Connection Administration on the Unity Connection gateway. See the “Creating
                                    				the Intersite Link on the Unity Connection Gateway” section on
                                    				page 3-12 .

Finish linking the gateways by creating the intersite link on
                                 			 the Cisco Unity gateway. See the “Creating
                                    				the Intersite Link on the Cisco Unity Gateway” section on page 3-14 .

Configure partitions and search spaces so that Cisco Unity
                                 			 Connection users can address to Cisco Unity users and vice versa. See the “Configuring
                                    				Partitions and Search Spaces for Cisco Unity and Unity Connection
                                    				Interoperability” section on page 3-15 .

Optionally, if you select to synchronize system distribution
                                 			 lists in either or both directions between the gateways, configure individual
                                 			 distribution lists to allow or prevent replication. See the “Configuring
                                    				Individual System Distribution Lists for Synchronization” section on
                                    				page 3-16 .

Optionally, extend identified subscriber messaging on the
                                 			 Cisco Unity servers to include Unity Connection Networking subscribers. See the “Extending
                                    				Cisco Unity Identified Subscriber Messaging to Include Unity Connection
                                    				Networking Subscribers” section on page 3-17 .

Optionally, set up cross-server sign-in, transfers, and live
                                 			 reply. See the “ Cross-Server
                                    				Sign-In, Transfers, and Live Reply ” chapter.

### Making Deployment Decisions and Gathering Important Information

Before you begin setting up Cisco Unity-Unity Connection interoperability, be sure to plan for the following, and gather the
                              applicable information:

If you have configured VPIM on your Cisco Unity servers using the Cisco Unity Voice Connector and its associated transport
                                    event sink, you must migrate your VPIM configuration to use the Interoperability Gateway for Microsoft Exchange rather than
                                    the Voice Connector. The Interoperability Gateway and the Voice Connector transport event sink cannot coexist when Cisco Unity
                                    is configured for interoperability with Cisco Unity Connection. If you are installing the Interoperability Gateway for the
                                    first time, be sure to configure it for both VPIM and Cisco Unity Connection Networking. The task list tell you when to uninstall
                                    the Voice Connector. (If you still require the Voice Connector to handle Bridge Networking and/or AMIS Networking, you reinstall
                                    it to handle those options.)

Select a single location on each site to act as a gateway to the other site. The gateways you select must have HTTP or HTTPS
                                    connectivity in order for directory synchronization to occur.

When selecting the Cisco Unity site gateway, if possible, select the server with the highest resources, lowest user count,
                                          and smallest amount of call activity. In particular, Platform Overlay 1 servers have CPU, memory, disk and MSDE/SQL Express
                                          limits that lower the ability of the server to handle synchronization overhead.

When selecting the Cisco Unity location, consider that all locations from the Unity Connection site belongs to the same Dialing
                                          Domain as the Cisco Unity site gateway.

### Determining Cisco Unity Interoperability Domain Name

In order for messages to be exchanged between Cisco Unity Connection and Cisco Unity, you need to decide on the domain name
                              that Unity Connection uses when addressing messages to Cisco Unity users. The domain name uniquely identifies the messaging
                              system. The domain name is configured as follows:

On the SMTP Domain Name field on the Network > Primary Location page in the Cisco Unity Administrator on the Cisco Unity gateway.

On the Interop Domain FQDN field in the Interoperability Gateway Administrator.

Additionally, based on the Interop Domain FQDN, the domain name is configured as follows:

If you install the Interoperability Gateway on an Exchange 2010 or 2007 server:

As the SMTP AddressSpace domain on the Interoperability Gateway Foreign Connector. (This value is set automatically, based
                                          on the Interop Domain FQDN, when the Interoperability Gateway Foreign Connector is created or modified using the Interoperability
                                          Gateway Administrator.)

As the DomainName on the Interoperability Gateway Accepted Domain. (This value is set automatically, based on the Interop
                                          Domain FQDN, when the Interoperability Gateway Accepted Domain is created or modified using the Interoperability Gateway Administrator.)

If you install the Interoperability Gateway on an Exchange 2003 server:

As the SMTP Address Space domain in the Interoperability Gateway SMTP Connector.

As the SMTP Email Address Policy on the Interoperability Gateway Recipient Policy.

If you have previously installed the Interoperability Gateway for Microsoft Exchange to handle VPIM or Trusted Internet subscribers
                              on Cisco Unity, use the interoperability domain that was selected during that process, unless it matches the Cisco Unity Connection
                              gateway SMTP domain.

If you have not previously installed the Interoperability Gateway to handle other networking features, the interoperability
                              domain name can be whatever you would like it to be. As a best practice, however, you should use a name that follows the format
                              <Name>.<DomainName>, where <Name> is a descriptive term and <DomainName> is the domain name of your organization, for example,
                              interop.mydomain.com. Note however that the interoperability domain name that you select must meet the following requirements:

It should not match any SMTP domain used in the Exchange organization to which Cisco Unity belongs for any purpose other than
                                    for routing messages through the Interoperability Gateway for Microsoft Exchange.

It must not match the SMTP domain of the Unity Connection site gateway. (You can check the SMTP domain on the System Settings >
                                    SMTP Configuration > Server page in Cisco Unity Connection Administration on the Unity Connection gateway.)

### Preparing Cisco Unity Gateway

Do the procedures in the following sections to prepare the Cisco Unity gateway:

#### Configuring
                              	 Primary Location Profile Page on Cisco Unity Gateway

In the Cisco Unity Administrator on the Cisco Unity gateway, go
                                             			 to the Network > Primary
                                                   				  Location > Profile page.

Enter a meaningful name for the location.

If a Dial ID has not been entered, enter one. The Dial ID
                                             			 identifies this location to Cisco Unity and is required to save changes to the
                                             			 page.

For the Dialing Domain name:

If your installation consists of only one Cisco Unity server,
                                                      					 create a dialing domain name.

If your installation consists of multiple Cisco Unity servers
                                                      					 networked via Digital Networking, and if this server is integrated with the
                                                      					 same phone system as other networked Cisco Unity servers, you may have already
                                                      					 added this server to a dialing domain. If not, enter the dialing domain name,
                                                      					 or select it from the available list. The list contains names of dialing domain
                                                      					 names already configured on at least one other Cisco Unity server in the
                                                      					 network.

Note that the dialing domain name is case sensitive and must be
                                                      					 entered exactly the same on all of the servers. To ensure that all servers are
                                                      					 correctly added to the same dialing domain, enter the dialing domain name on
                                                      					 one Cisco Unity server and wait for the name to replicate to the other
                                                      					 Cisco Unity servers. By doing so, you also confirm that replication is working
                                                      					 correctly among the servers. The time that it takes for the primary location
                                                      					 data from other Cisco Unity servers to be reflected on the local server depends
                                                      					 on your network configuration and replication schedule.

In the SMTP Domain Name field, enter the interoperability domain
                                             			 name that you previously select in the “Determining
                                                				Cisco Unity Interoperability Domain Name” section on page 3-4 .

Select the Save icon.

#### Checking
                              	 Cisco Unity Permissions to Create Unity Connection Users

During Cisco Unity installation, when you run the Cisco Unity
                                 		Permissions wizard to grant the necessary permissions to the installation and
                                 		service accounts, if you did not check the Set Permissions Required by AMIS,
                                 		Cisco Unity Bridge, and VPIM check box on the Choose Whether to Enable Voice
                                 		Messaging Interoperability page, do the “Setting
                                    		  Permissions to Create Cisco Unity Connection Users on Cisco Unity” procedure on
                                    		  page 3-5 .

For more information on running the Permissions wizard, see the
                                 		Permissions wizard Help file, PWHelp_<language>.htm, in the directory in
                                 		which the Permissions wizard is installed.

#### Setting
                              	 Permissions to Create Cisco Unity Connection Users on Cisco Unity

Sign in to the gateway server using an account that:

Is a member of the Domain Admins group in the domain that the
                                                      					 Cisco Unity server belongs to, or that has permissions equivalent to the
                                                      					 default permissions for the Domain Admins group.

Is either an Exchange Full Administrator or a member of the
                                                      					 Domain Admins group in the domain that contains all of the domains from which
                                                      					 you want to import Cisco Unity subscribers.

Re-run the Permissions wizard, and follow the on-screen prompts
                                             			 until the Choose Whether to Enable Voice Messaging Interoperability page
                                             			 appears.

Check the Set Permissions Required by AMIS, Cisco Unity Bridge, and
                                                				VPIM check box.

Follow the on-screen prompts to complete the Permissions wizard.

#### Extending the Active Directory Schema

Before Cisco Unity is installed, the Active Directory schema is extended to store Cisco Unity-specific information. To support
                                 interoperability with Cisco Unity Connection, the schema must be further extended.

To see the schema changes that need to be made to support Cisco Unity Connection interoperability, browse to the directory
                                 Schema\LdifScripts on Cisco Unity Disc 1, and view the file vpimgateway.ldf. (The extensions needed for Cisco Unity Connection
                                 interoperability are the same as those needed for VPIM Networking.)

Do the following procedure only if you did not already modify the Active Directory schema to support VPIM Networking. You
                                 can verify whether the schema has already been modified by examining the log file that is generated each time the schema is
                                 updated. A shortcut to the directory where the log file is located is placed on the Windows desktop.

#### Extending the
                              	 Active Directory Schema for Cisco Unity Connection Interoperability and VPIM
                              	 Networking

Confirm that all domain controllers are on line before making
                                             			 the schema updates. Schema replication occurs only when all domain controllers
                                             			 are on line.

On the domain controller that is the schema master, sign in
                                             			 using an account that is a member of the Schema Administrators group.

On Cisco Unity DVD 1 or CD 1, or from the location to which you
                                             			 saved the downloaded Cisco Unity CD 1 image files, browse to the directory ADSchemaSetup , and double-click ADSchemaSetup.exe .

In the dialog box, double-click a row to select the language in
                                             			 which you view the ADSchemaSetup.

Check the Exchange VPIM and Connection Networking Connector check box, uncheck the other check boxes, and then select OK .

When the LDAP Data Interchange Format (LDIF) scripts have
                                             			 finished running, select OK .

When the schema extension has finished, Ldif.log and LDif.err
                                             			 files are saved to the desktop. View the contents of the files to confirm that
                                             			 the extension completed successfully.

Wait for the changes to the schema to replicate throughout the
                                             			 forest before adding information to the primary location and to delivery
                                             			 locations. Changes to the schema may take 15 minutes or more to replicate.

### Configuring a
                           	 Previously Installed Interoperability Gateway for Unity Connection
                           	 Interoperability on Exchange 2010 or 2007

In order for messages to be exchanged between Cisco Unity and
                                 		  Cisco Unity Connection via the Interoperability Gateway for Microsoft Exchange,
                                 		  a valid Foreign Connector must be present on the Exchange 2010 or 2007 server
                                 		  to properly route messages through the Interoperability Gateway. In addition,
                                 		  the Exchange organization to which your Cisco Unity servers belong must be
                                 		  allowed to send mail to and receive mail from the SMTP bridgehead servers in
                                 		  the remote network. In the case where the remote network is a Cisco Unity
                                 		  Connection site, depending on your configuration, mail may be sent and received
                                 		  directly with the Unity Connection site gateway or with a smart host or other
                                 		  relay outside of the Exchange organization that handles SMTP connections on
                                 		  behalf of the Unity Connection gateway.

In this section, first do the below given procedure .

If you are already familiar with how to configure the Exchange
                                 		  organization to allow messages to be sent and received with the Cisco Unity
                                 		  Connection gateway, smart host, or relay, skip the remaining procedures and
                                 		  handle the message delivery configuration based on rules and practices
                                 		  established in your organization. Otherwise, do the remaining two procedures:

Procedures

Open the Interoperability Gateway Administrator. (In the Windows
                                          			 Start Menu, browse to Start > Programs > Cisco > IGE
                                                				  Admin .)

If the Interoperability Gateway is installed on Exchange 2010,
                                             				the Interoperability Gateway Administrator prompts you to enter account
                                             				credentials. Use an account that has Full Exchange Administrator privileges.

In the top pane of the Administrator, under Address
                                             				Spaces , confirm whether the UCI
                                             				(Cisco Unity-Connection Interoperability) check box is checked. If it is
                                          			 already checked, close the Interoperability Gateway Administrator and continue
                                          			 with the next task in the task list. If it is not checked, check it.

In the tree control at left in the Interoperability Gateway
                                          			 Administrator, select Foreign Connector .

If a Foreign Connector has not previously been created that
                                          			 covers the interoperability domain and the UCI feature address space that you
                                          			 checked in Step 2 ,
                                          			 a warning message displays in red at the top of the Foreign Connector pane.

If you do not see this warning, and a valid Foreign Connector is
                                             				displayed in the list box on the upper left side of the pane, close the
                                             				Interoperability Gateway Administrator and continue with the next task in the
                                             				task list.

If you do see the warning, you can modify the existing Foreign
                                             				Connector that was created when the Interoperability Gateway for Microsoft
                                             				Exchange was initially installed. To do so, do the following substeps:

In the list of Foreign Connectors that are homed on the server
                                                				  and contain at least one address space that pertains to Cisco Unity networking
                                                				  (at the upper left), select the existing Foreign Connector.

Select Modify below the list box.

On the Execute Shell Command screen, select Run .

Close the
                                          			 Interoperability Gateway Administrator.

#### Configuring a Send
                              	 Connector for a Remote Voice Messaging System (Exchange 2010 or 2007
                              	 Only)

On the Exchange server on which the Interoperability Gateway is
                                             			 installed, open the Exchange Management Shell.

In the left-hand pane, expand Organization Configuration and select Hub Transport .

In the main Hub Transport pane, select the Send Connectors tab.

In the Actions pane, under Hub Transport, select New Send Connector .

In the New SMTP Send Connector wizard, on the Introduction page,
                                             			 enter a Name for the new connector.

Under Select the Intended Use for this Send Connector ,
                                             			 select Custom , then select Next .

On the Address space page, select Add .

For Address, enter the SMTP domain of the remote network, then
                                             			 select OK .

Select Next .

On the Network settings page, select Route Mail through the Following Smart Hosts .

Select Add .

For IP Address, enter the IP address of the Unity Connection
                                             			 gateway if messages are routed directly to the gateway, or of a smart host or
                                             			 other relay if one is configured to deliver messages from the Exchange
                                             			 organization to the Unity Connection gateway.

Select OK .

Select Next to continue to the next page.

On the Configure Smart Host Authentication Settings Page, select
                                             			 the type of authentication to use when sending mail between the Exchange
                                             			 organization and the Unity Connection gateway.

Select Next to continue to the next page.

On the Source Server page, the local Exchange server should be
                                             			 listed by default. Select Next to continue.

Confirm the settings on the New Connector page and select New to add the new connector.

Select Finish to exit the wizard.

On the Send Connectors tab, right-click the connector that you
                                             			 created and select Properties .

Set the Protocol Logging Level to Verbose .

Select OK to close the properties window.

#### Configuring a
                              	 Receive Connector for a Remote Voice Messaging System (Exchange 2010 or 2007
                              	 Only)

On the Exchange server on which the Interoperability Gateway is
                                             			 installed, open the Exchange Management Shell.

In the left-hand pane, expand Server Configuration and select Hub Transport .

In the upper Hub Transport pane, select the local Exchange
                                             			 server from the list of servers.

In the lower pane, confirm that the title of the pane is the
                                             			 name of the local Exchange server, then select the Receive Connectors tab.

In the Actions pane, under the local server name, select New Receive Connector .

In the New SMTP Send Connector wizard, on the Introduction page,
                                             			 enter a name for the new connector.

Under Select the Intended Use for this Send Connector, select Custom , then select Next .

On the Local Network settings page enter the fully qualified
                                             			 domain name of the local server in the Specify the FQDN this Connector Provide
                                             			 in Response to HELO or EHLO: field.

Select Next to continue to the next page.

On the Remote Network settings page, in the list box, select 0.0.0.0-255.255.255.255 , then select Edit .

If messages are received directly from the Unity Connection
                                             			 gateway, enter the IP address of the gateway as both the Start Address and End
                                             			 Address value. If a smart host or other relay external to the Exchange
                                             			 organization delivers messages on behalf of the Unity Connection gateway, enter
                                             			 the IP address of the smart host or relay as both the Start Address and End
                                             			 Address value.

Select OK .

Select Next to continue to the next page.

Confirm the settings on the New Connector page, then select New to add the new connector.

Select Finish to exit the wizard.

On the Receive Connectors tab, right-click the connector that
                                             			 you created and select Properties .

Set the Protocol Logging Level to Verbose .

Select the Permission Groups tab.

Check the Anonymous Users check box.

Select OK to close the properties window.

### Configuring SMTP
                           	 Access on the Unity Connection Gateway

The Cisco Unity Connection SMTP server running on each system
                                 		  has an IP access list that controls which IP addresses are allowed to establish
                                 		  connections to it. Incoming SMTP connections are automatically accepted from
                                 		  some servers, such as the systemwide smart host that is defined on the System
                                 		  Settings > SMTP Configuration > Smart Host page, and any Unity Connection
                                 		  or Cisco Unity locations that are part of the same site or Cisco voicemail
                                 		  organization.

If messages from Cisco Unity users are delivered to the Unity
                                 		  Connection gateway by one or more servers that are not already defined either
                                 		  as the systemwide smart host or as a Cisco Unity location (this would be the
                                 		  case, for example, in a very simple configuration with a single Cisco Unity
                                 		  server that also hosts the Interoperability Gateway for Microsoft Exchange and
                                 		  the entire Exchange organization) or in the IP access list, do the following
                                 		  procedure to add the IP address of the delivery servers to the Unity Connection
                                 		  gateway IP access list.

Do the following procedure to configure SMTP access on the Unity
                                 		  Connection gateway

In Cisco Unity Connection Administration on the Cisco Unity
                                          			 Connection gateway, expand System Settings > SMTP
                                                				  Configuration , then select Server .

On the Edit menu, select Search IP Address Access List .

Select Add New .

On the New Access IP Address page, enter the IP address of the
                                          			 server that delivers messages on behalf of the Cisco Unity site.

Select Save .

On the Access IP Address page, check the Allow Unity Connection check box.

Select Save .

Repeat Step 2 through Step 7 for
                                          			 each additional server that delivers messages on behalf of the Cisco Unity
                                          			 site.

### Downloading
                           	 Cisco Unity Gateway Configuration File

When linking Cisco Unity and Unity Connection gateways, you
                                 		  download the configuration file for each gateway and load it on the other
                                 		  gateway. Start by downloading the Cisco Unity configuration file to a location
                                 		  where you can access it from Cisco Unity Connection Administration on the Unity
                                 		  Connection gateway.

Do the following procedure:

In the Cisco Unity Administrator on the Cisco Unity site
                                          			 gateway, browse to Network and select Unity Connection Networking .

Select Download to download the local site configuration
                                          			 file.

Save the file to a location on your hard drive, or on media that
                                          			 you can use to copy the file to the Cisco Unity gateway. Note that the file
                                          			 contains a public key certificate and should be treated as sensitive data.

### Setting Up a
                           	 Template for Unity Connection Users on the Cisco Unity Gateway

While creating an intersite link on the Cisco Unity gateway, you
                              		must select the template that the Cisco Unity gateway uses to create directory
                              		objects for Unity Connection users. You should review existing templates or
                              		create a new template specifically for Unity Connection users prior to creating
                              		the link.

The template that you select affects a number of important
                              		settings, such as:

Public distribution list membership —Unity Connection
                                    			 users are added as list members in any Cisco Unity public distribution lists
                                    			 that are configured for the template.

Show Subscriber in Email Server Address Book —Controls
                                    			 whether Unity Connection users are listed in the Outlook address book.

Class of Service —Although most of the class of service
                                    			 settings do not affect the Unity Connection users directly, the Unity
                                    			 Connection users are considered members of the class of service and therefore
                                    			 can affect search results in cases where the class of service is used as the
                                    			 search scope of an object such as a directory handler.

You can review existing templates in the Cisco Unity
                              		Administrator by going to any Subscribers > Subscriber Template page and
                              		selecting the Find icon. To create a new template, do the following procedure.

#### Creating a New
                              	 Template for Cisco Unity Connection Users on the Cisco Unity Gateway

In the Cisco Unity Administrator, go to any Subscribers > Subscriber
                                                   				  Template page.

Select the Add icon.

In the Add a Subscriber Template dialog box, enter a name.

Select New Template or Based on Existing Template . If you select Based on
                                             			 Existing Template, select the applicable template in the Based On field.

Select Add .

On the Profile page, select a Class of Service and check or
                                             			 uncheck the Show Subscriber in Email Server Address Book check
                                             			 box, as applicable.

Select the Distribution Lists page.

On the Distribution Lists page, to assign all new users based on
                                             			 this template to a public distribution list, select the list in the Public
                                             			 Distribution Lists box, then select > .

To remove a distribution list from those to which new users are
                                                				added, select the list, then select >> .

Select the Save icon.

### Creating the
                           	 Intersite Link on the Unity Connection Gateway

Do the following procedure to create the intersite link on the
                                 		  Cisco Unity Connection gateway.

If the site gateway is a Unity Connection cluster, do the
                                 		  procedure only on the publisher server. The publisher server must be acting
                                 		  primary when you do the procedure.

In Cisco Unity Connection Administration on the Cisco Unity
                                          			 Connection gateway, expand Networking , expand Links , then select Intersite Links .

Select Add .

On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                             				Manually Exchanging Configuration Files .

Select Download and save the Unity Connection site
                                          			 configuration file to a location on your hard drive, or on media that you can
                                          			 use to copy the file to the Cisco Unity gateway. Note that the file contains a
                                          			 public key certificate and should be treated as sensitive data.

Select Browse and upload the Cisco Unity configuration file
                                          			 that you downloaded in the Downloading
                                             				the Cisco Unity Gateway Configuration File .

For Transfer Protocol settings, decide whether you want to
                                          			 enable SSL to encrypt directory synchronization traffic between Cisco Unity and
                                          			 Cisco Unity Connection.

For Synchronization Settings, check the Include Distribution
                                          			 Lists When Synchronizing Directory Data check box to have system distribution
                                          			 lists that are created on the Cisco Unity site replicated to Unity Connection
                                          			 so that Unity Connection users can address messages to them. (Note that only
                                          			 the list name and other information used in addressing are replicated.)

To convert recorded names from this site to a different encoding
                                          			 when synchronizing them with the remote site, check the Convert Outgoing Recorded Names To check box, and
                                          			 select the codec to use.

Do not select G711 a-law format when setting up an intersite
                                                         				  link to a Cisco Unity site gateway.

By default, two tasks that each run on their own schedule to
                                          			 pull directory data and recorded names from Cisco Unity to Unity Connection are
                                          			 enabled immediately after you create the intersite link. To disable either type
                                          			 of directory synchronization until you manually edit and enable the applicable
                                          			 synchronization task, uncheck the Enable Task to Synchronize Directory Data After the
                                             				Join or Enable Task to Synchronize Recorded Names After the
                                             				Join check boxes.

You should perform the initial synchronization outside of normal
                                             				business hours to avoid peak traffic times. In particular, if your Cisco Unity
                                             				site gateway is a Platform Overlay 1 server, the synchronization activity can
                                             				cause noticeable delays in the user conversation.

For Intersite Routing, select the appropriate option:

Route to this Remote Site Through —Enter the specific IP
                                                   					 address or fully-qualified domain name of a Microsoft Exchange server in your
                                                   					 organization that can accept SMTP messages and route them to the
                                                   					 Interoperability Gateway for Microsoft Exchange. The host must be able to
                                                   					 accept SMTP messages sent from the Unity Connection gateway to addresses at the
                                                   					 interoperability domain.

Route to this Remote Site Through SMTP Smart Host (If One Is
                                                      						Defined) —Routes outgoing messages to the host that is defined on the System
                                                   					 Settings > SMTP Configuration > Smart Host page. If you select this
                                                   					 option, the smart host must be defined, and must be able to accept SMTP
                                                   					 messages sent from the Unity Connection gateway to addresses at the
                                                   					 interoperability domain. If the smart host is not defined, a non-delivery
                                                   					 receipt (NDR) is sent to the message sender.

Route to this Remote Site Through the Remote Site
                                                      						Gateway —Routes outgoing messages to the Cisco Unity gateway. Use this
                                                   					 option only if Microsoft Exchange is installed on the Cisco Unity server and
                                                   					 the server is able to accept SMTP messages sent from the Unity Connection
                                                   					 gateway to addresses at the interoperability domain.

Select Link .

### Creating the
                           	 Intersite Link on the Cisco Unity Gateway

Do the following procedure to create the intersite link on the
                                 		  Cisco Unity gateway.

If the site gateway is a failover pair, do the procedure only on
                                 		  the primary server. The primary server must be active when you do the
                                 		  procedure.

In the Cisco Unity Administrator on the Cisco Unity site
                                          			 gateway, browse to Network and select Unity Connection Networking .

On the Unity Connection Networking page, in the Remote
                                          			 Configuration File field, select Browse and upload the Unity Connection configuration file that
                                          			 you downloaded in Step 4 of the Creating the Intersite Link on the Unity Connection Gateway .

Select Add .

For Template, select the template that you selected or created
                                          			 in the “Setting
                                             				Up a Template for Unity Connection Users on the Cisco Unity Gateway” section on
                                             				page 3-11 . The template is used to create Cisco Unity directory objects
                                          			 for Unity Connection users so that Cisco Unity users can address messages to
                                          			 them. You must select a template before you can create the intersite link.

Optionally, enter a Display Name Suffix. When the Cisco Unity
                                          			 site gateway creates directory objects for Unity Connection users and any
                                          			 replicated system distribution lists, this suffix is placed at the end of the
                                          			 display names of the objects. This can help Cisco Unity users locate the proper
                                          			 contact to use for addressing messages in Microsoft Outlook or other clients
                                          			 that access the directory, particularly if Unity Connection users already have
                                          			 Active Directory accounts prior to creating the intersite link.

Check the
                                          			 Synchronize Distribution Lists check box to have system distribution lists that
                                          			 are created on the Unity Connection site replicated to Cisco Unity so that
                                          			 Cisco Unity users can address messages to them. (Note that only the list name
                                          			 and other information used in addressing are replicated.)

Check the Synchronize Voice Names check box to have
                                          			 Cisco Unity synchronize voice names for Unity Connection users and system
                                          			 distribution lists.

If you enabled
                                          			 SSL in Step 6 of the Creating
                                             				the Intersite Link on the Unity Connection Gateway , check the Use
                                             				Secure Sockets Layer (SSL) check box. If the Unity Connection site
                                          			 gateway is using a self-signed certificate (the default for Unity Connection),
                                          			 also check the Use
                                             				Self-Signed Certificates check box.

For Outbound
                                          			 Audio Conversion, if you want to convert voice names to a different format
                                          			 before sending them to the Unity Connection site gateway, select a codec in the
                                          			 Voice Names field.

Review and
                                          			 continue entering settings, as applicable.

When you have
                                          			 finished entering settings, select the Save icon.

Select Join .

### Configuring
                           	 Partitions and Search Spaces for Cisco Unity and Unity Connection
                           	 Interoperability

When you initially set up the intersite link between Unity
                                 		  Connection and Cisco Unity, Unity Connection users are not able to address
                                 		  messages to Cisco Unity users, because the Cisco Unity users are placed in
                                 		  newly-created partitions (based on their home Cisco Unity server) that are not
                                 		  a member of any Unity Connection search spaces.

After initial replication completes between the gateways and
                                 		  Cisco Unity objects are replicated throughout the Unity Connection site, you
                                 		  can reconfigure your search spaces to include the Cisco Unity partitions. (Note
                                 		  that you cannot assign Cisco Unity Connection users or other objects to a
                                 		  partition that was created for Cisco Unity users.)

In addition, for each Unity Connection location, you can specify
                                 		  the Local Partition That Cisco Unity Users Can Address To By Extension. Only
                                 		  extensions belonging to this partition are replicated to Cisco Unity. These
                                 		  extensions can be used for message addressing as well as auto-attendant dialing
                                 		  at the Cisco Unity site. Replicated extensions are added to the Dialing Domain
                                 		  of the Cisco Unity site gateway. Because extensions within a Dialing Domain
                                 		  must be unique, the collection of all partitions selected across the Unity
                                 		  Connection site should not contain duplicates of any extension. When the
                                 		  collection includes duplicate extensions, or extensions that already exist in
                                 		  the Cisco Unity site gateway Dialing Domain, one or more extensions are omitted
                                 		  from the Cisco Unity directory. Warnings appear in the Cisco Unity application
                                 		  event log indicating the owner of each omitted extension. After remedying any
                                 		  conflicts, you may need to do a manual resynchronization on the Cisco Unity
                                 		  site gateway (by selecting Total Sync on the Network > Connection Networking
                                 		  Profile page in Cisco Unity Administrator) in order to update the extensions.

It is possible for a Connection user to not have any extensions
                                 		  belonging to the Local Partition That Cisco Unity Users Can Address To By
                                 		  Extension configured on the server on which the user is homed. In this case,
                                 		  Cisco Unity users need to use dial-by-name for addressing messages to such
                                 		  Unity Connection users. Also, callers at the Cisco Unity site can only reach
                                 		  the user via dial-by-name Directory Handlers.

To configure the Local Partition That Cisco Unity Users Can
                                 		  Address To By Extension, do the following procedure on each Unity Connection
                                 		  server.

Do the following procedure to configure the partition that Cisco Unity
                                 		  users can address to for a Cisco Unity Connection location :

In Cisco Unity Connection Administration (on any location),
                                          			 expand Networking > and select Locations .

Expand Local Site and select the display name of the local
                                          			 location (the location on which you are accessing Unity
                                          			 Connection Administration).

Under Local Partition That Cisco Unity Users Can Address To By
                                          			 Extension, for Partition, select the name of the partition to use.

Select Save .

Repeat Step 1 through Step 4 on each
                                          			 Unity Connection location in the site.

### Configuring
                           	 Individual System Distribution Lists for Synchronization

If you checked the Include Distribution Lists When Synchronizing
                              		Directory Data check box in Step 7 of the " Creating
                                 		  the Intersite Link on the Unity Connection Gateway ", system distribution
                              		lists created on Cisco Unity can be replicated to Cisco Unity Connection so
                              		that Unity Connection users can address to them. However, by default,
                              		individual Cisco Unity system distribution lists are not marked for
                              		synchronization. To mark them, use the Public Distribution List Builder tool,
                              		located in the Cisco Unity Tools Depot. (The option to set or unset
                              		synchronization for lists is referred to as “Configuring distribution lists for
                              		Connection Networking.”)

If you checked the Synchronize Distribution Lists check box in Step 6 of the " Creating
                                 		  an Intersite Link on the Cisco Unity Gateway ", system distribution lists
                              		created on Unity Connection can be replicated to Cisco Unity. However, in order
                              		for information about an individual list to be offered to the Cisco Unity site,
                              		the Replicate to Remote Sites Over Intersite Links check box must be checked on
                              		the Edit Distribution List Basics page for a list. By default, Replicate to
                              		Remote Sites Over Intersite Links is checked, so individual Unity Connection
                              		system distribution lists are marked for synchronization by default. However,
                              		in order to allow contacts as members of a system distribution list, you must
                              		uncheck Replicate to Remote Sites Over Intersite Links, so if you have lists
                              		that have been configured to allow contacts as members, they are not offered
                              		for replication to the remote site.

To disable synchronization for an individual list, uncheck
                              		Replicate to Remote Sites Over Intersite Links. To enable synchronization for
                              		an individual list, remove any contacts that have been added as members and
                              		check the Replicate to Remote Sites Over Intersite Links check box. To enable
                              		or disable synchronization for multiple lists at once, you can use either Bulk
                              		Edit or the Bulk Administration Tool.

### Extending Cisco
                           	 Unity Identified Subscriber Messaging to Include UnityConnection Networking
                           	 Subscribers

When a user on the Unity Connection site calls a
                              		Cisco Unity user and leaves a message, by default Cisco Unity do not identify
                              		the message as being from the Unity Connection user. For Cisco Unity to
                              		identify callers whose calling number matches the extension or alternate
                              		extension of a Unity Connection user, identified subscriber messaging (ISM)
                              		must be extended to networking contacts. (If you are also using other types of
                              		networking, such as VPIM, you may already have enabled ISM for networking
                              		contacts.)

Enabling ISM to include Unity Connection
                              		Networking subscribers and other networking contacts requires the following:

The automated attendant search scope on each
                                    			 server must be set to the dialing domain. On each server, verify that the Set
                                    			 Auto Attendant Search Scope field is set to Dialing Domain on the Network >
                                    			 Primary Location > Profile page in Cisco Unity Administrator.

Identified subscriber messaging must be
                                    			 enabled on each server. (ISM is enabled for “regular” subscribers by default.)
                                    			 On each server, verify that the Disable Identified Subscriber Messaging check
                                    			 box is unchecked on the System > Configuration > Settings page in
                                    			 Cisco Unity Administrator. (This setting is stored in the registry. If the
                                    			 system is using failover, verify the setting on both the primary and secondary
                                    			 servers.)

#### Extending
                              	 Identified Messaging to Include Unity Connection Networking Subscribers

On the Cisco Unity server desktop, double-click the Cisco Unity
                                             			 Tools Depot icon. (If the location is using failover, start the procedure on
                                             			 the primary server.)

In the left pane, under Administrative Tools,
                                             			 double-click Advanced Settings
                                                				Tool .

In the Unity Settings pane, click Networking - Enable Identified Subscriber Messaging (ISM) for
                                                				AMIS, Bridge, VPIM and Trusted Internet Subscribers .

In the New Value list, click 1 , then click Set .

When prompted, click OK .

Click Exit .

Restart Cisco Unity for the registry setting to take effect.

If the location is using failover, repeat Step 1 through Step 7 on the
                                             			 secondary server.

Repeat Step 1 through Step 8 on each
                                             			 Cisco Unity location in the site.

## Notable Behavior in Networking Cisco Unity and Unity Connection

This section provides information about notable expected behavior associated with Cisco Unity and Unity Connection networking.

### Effects of
                           	 Changing Cisco Unity Administrator Configuration Settings on the
                           	 Interoperability Gateway for Microsoft Exchange

The Interoperability Gateway for Microsoft Exchange gets
                              		information about Cisco Unity networking locations by communicating with the
                              		web services resource on a server running Cisco Unity 10.x. For example, when
                              		evaluating an outgoing secure message, the Interoperability Gateway looks up
                              		the configuration for the destination to determine whether the message should
                              		be decrypted and sent or returned as undeliverable. In the Cisco Unity
                              		Administrator, you configure this and other location-specific settings on the
                              		Connection Networking profile for a Cisco Unity Connection site.

To understand how your topology dictates when changes to
                              		configuration settings made in the Cisco Unity Administrator takes effect in
                              		the Interoperability Gateway, and for information on how to expedite the
                              		process, see the “ The
                                 		  Interoperability Gateway for Microsoft Exchange with Cisco Unity 8.x ”
                              		section in the “Troubleshooting Networking in Cisco Unity 8.x” chapter of the Troubleshooting Guide for Cisco Unity Release 8.x at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/unity/8x/troubleshooting/guide/8xcutsgx/8xcutsg060.html#wp1017196 .

### Unity Connection
                           	 Users Not Listed in the Directory in Exchange 2010 or 2007
                           	 Organizations

When Cisco Unity is installed in an Active Directory forest that
                              		does not contain any servers running Exchange 2003 or earlier, public
                              		distribution lists and contact objects created by the Cisco Unity server do not
                              		have a value written to the showInAddressBook attribute. As a result, those
                              		objects are not available in an address book that is accessed through a mail
                              		client, such as Microsoft Outlook. In a Cisco Unity Connection Networking
                              		deployment, this affects all users and distribution lists that are replicated
                              		from Unity Connection.

For instructions on how to update address lists to include Unity
                              		Connection objects, see the “Public Distribution Lists and Networking
                              		Subscribers Created by Cisco Unity Are Not Listed in the Directory” section in
                              		the applicable 12.x or later version of the Release Notes for Cisco Unity at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_release_notes_list.html .

### Differences in User Experience Between Cisco Unity and Unity Connection

When you network Cisco Unity and Unity Connection, and particularly when you migrate users from Cisco Unity to Cisco Unity
                              Connection, users may notice differences in behavior between the two products. Unity Connection turns on the message waiting
                              indicator (MWI) for new receipts; Cisco Unity does not.

### Display of Cisco Unity User Address Information

Unity Connection users who use applications such as Cisco Unity Connection ViewMail for IBM Lotus Notes, Cisco Unity Connection
                              ViewMail for Microsoft Outlook, and Visual Voicemail may see system-generated SMTP addresses for Cisco Unity users. For example,
                              when viewing a message received by a Cisco Unity user, the sender is identified by display name, and the system-generated
                              address is displayed along with the display name.

### Feature Support Limitations

The following features are not supported across intersite links between Cisco Unity and Unity Connection sites:

License pooling

Relay of messages to or from VPIM, AMIS, Bridge, or system contacts, including blind addressing to such contacts

Broadcast messages

Dispatch messages

Message recall

### Manual Resynchronization on the Unity Connection Site Gateway Runs Both Directory and Voice Name Synchronization Tasks

The Resync All button on the Search Intersite Links page in Cisco Unity Connection Administration starts the Synchronize Directory
                              With Remote Network task. When that task completes, it automatically starts the Synchronize Voice Names With Remote Network
                              task. These tasks normally run independently on separate schedules.

### No Results Found When a Unity Connection Directory Handler Search Scope is Set to a Remote System Distribution List

If you set the Search Scope of a Unity Connection directory handler to system distribution List and select a list that is
                              homed on the Cisco Unity site, no results are returned when callers reach the handler and attempt a search. This happens because
                              list membership is not replicated across intersite links. (This behavior does not apply to voice-enabled directory handlers,
                              which do not have the option to use a system distribution list as the search scope.)

### Outbound SMTP Authentication

Unity Connection does not support outbound SMTP authentication. If the Exchange environment in use by Cisco Unity requires
                              authentication, you must configure the Unity Connection site gateway to route messages.

### Users May Receive Multiple Copies of a Message Sent to Multiple Distribution Lists

When a message is sent to multiple distribution lists, under some circumstances, when the message traverses an intersite link,
                              users who are members of more than one of the lists may receive multiple copies of the message.

### ViewMail for Microsoft Outlook and Body Text in Voice Messages

When Cisco Unity ViewMail for Microsoft Outlook users type text in the body of a voice message, the text is not received by
                              Unity Connection users. Likewise, when Cisco Unity Connection ViewMail for Microsoft Outlook users type text in the body of
                              a message, the text is not received by Cisco Unity users. However, recipients on the same type of system do receive the text
                              (Cisco Unity users receive text sent by other Cisco Unity users, and Unity Connection users receive text sent by other Unity
                              Connection users).

| Step 1 | In the Cisco Unity Administrator on the Cisco Unity gateway, go
                                             			 to the Network > Primary
                                                   				  Location > Profile page. |
|---|---|
| Step 2 | Enter a meaningful name for the location. |
| Step 3 | If a Dial ID has not been entered, enter one. The Dial ID
                                             			 identifies this location to Cisco Unity and is required to save changes to the
                                             			 page. |
| Step 4 | For the Dialing Domain name: If your installation consists of only one Cisco Unity server,
                                                      					 create a dialing domain name. If your installation consists of multiple Cisco Unity servers
                                                      					 networked via Digital Networking, and if this server is integrated with the
                                                      					 same phone system as other networked Cisco Unity servers, you may have already
                                                      					 added this server to a dialing domain. If not, enter the dialing domain name,
                                                      					 or select it from the available list. The list contains names of dialing domain
                                                      					 names already configured on at least one other Cisco Unity server in the
                                                      					 network. Note that the dialing domain name is case sensitive and must be
                                                      					 entered exactly the same on all of the servers. To ensure that all servers are
                                                      					 correctly added to the same dialing domain, enter the dialing domain name on
                                                      					 one Cisco Unity server and wait for the name to replicate to the other
                                                      					 Cisco Unity servers. By doing so, you also confirm that replication is working
                                                      					 correctly among the servers. The time that it takes for the primary location
                                                      					 data from other Cisco Unity servers to be reflected on the local server depends
                                                      					 on your network configuration and replication schedule. |
| Step 5 | In the SMTP Domain Name field, enter the interoperability domain
                                             			 name that you previously select in the “Determining
                                                				Cisco Unity Interoperability Domain Name” section on page 3-4 . |
| Step 6 | Select the Save icon. |

| Tip | If you do not know
                                          		whether you checked the check box, run the Permissions wizard in report mode.
                                          		For more information, see the Report Mode Help file,
                                          		PWReportHelp_<language>.htm, in the directory in which the Permissions
                                          		wizard is installed. |
|---|---|

| Step 1 | Sign in to the gateway server using an account that: Is a member of the Domain Admins group in the domain that the
                                                      					 Cisco Unity server belongs to, or that has permissions equivalent to the
                                                      					 default permissions for the Domain Admins group. Is either an Exchange Full Administrator or a member of the
                                                      					 Domain Admins group in the domain that contains all of the domains from which
                                                      					 you want to import Cisco Unity subscribers. |
|---|---|
| Step 2 | Re-run the Permissions wizard, and follow the on-screen prompts
                                             			 until the Choose Whether to Enable Voice Messaging Interoperability page
                                             			 appears. |
| Step 3 | Check the Set Permissions Required by AMIS, Cisco Unity Bridge, and
                                                				VPIM check box. |
| Step 4 | Follow the on-screen prompts to complete the Permissions wizard. |

| Step 1 | Confirm that all domain controllers are on line before making
                                             			 the schema updates. Schema replication occurs only when all domain controllers
                                             			 are on line. |
|---|---|
| Step 2 | On the domain controller that is the schema master, sign in
                                             			 using an account that is a member of the Schema Administrators group. |
| Step 3 | On Cisco Unity DVD 1 or CD 1, or from the location to which you
                                             			 saved the downloaded Cisco Unity CD 1 image files, browse to the directory ADSchemaSetup , and double-click ADSchemaSetup.exe . |
| Step 4 | In the dialog box, double-click a row to select the language in
                                             			 which you view the ADSchemaSetup. |
| Step 5 | Check the Exchange VPIM and Connection Networking Connector check box, uncheck the other check boxes, and then select OK . |
| Step 6 | When the LDAP Data Interchange Format (LDIF) scripts have
                                             			 finished running, select OK . |
| Step 7 | When the schema extension has finished, Ldif.log and LDif.err
                                             			 files are saved to the desktop. View the contents of the files to confirm that
                                             			 the extension completed successfully. |
| Step 8 | Wait for the changes to the schema to replicate throughout the
                                             			 forest before adding information to the primary location and to delivery
                                             			 locations. Changes to the schema may take 15 minutes or more to replicate. |

| Step 1 | Open the Interoperability Gateway Administrator. (In the Windows
                                          			 Start Menu, browse to Start > Programs > Cisco > IGE
                                                				  Admin .) If the Interoperability Gateway is installed on Exchange 2010,
                                             				the Interoperability Gateway Administrator prompts you to enter account
                                             				credentials. Use an account that has Full Exchange Administrator privileges. |
|---|---|
| Step 2 | In the top pane of the Administrator, under Address
                                             				Spaces , confirm whether the UCI
                                             				(Cisco Unity-Connection Interoperability) check box is checked. If it is
                                          			 already checked, close the Interoperability Gateway Administrator and continue
                                          			 with the next task in the task list. If it is not checked, check it. |
| Step 3 | In the tree control at left in the Interoperability Gateway
                                          			 Administrator, select Foreign Connector . |
| Step 4 | If a Foreign Connector has not previously been created that
                                          			 covers the interoperability domain and the UCI feature address space that you
                                          			 checked in Step 2 ,
                                          			 a warning message displays in red at the top of the Foreign Connector pane. If you do not see this warning, and a valid Foreign Connector is
                                             				displayed in the list box on the upper left side of the pane, close the
                                             				Interoperability Gateway Administrator and continue with the next task in the
                                             				task list. If you do see the warning, you can modify the existing Foreign
                                             				Connector that was created when the Interoperability Gateway for Microsoft
                                             				Exchange was initially installed. To do so, do the following substeps: In the list of Foreign Connectors that are homed on the server
                                                				  and contain at least one address space that pertains to Cisco Unity networking
                                                				  (at the upper left), select the existing Foreign Connector. Select Modify below the list box. On the Execute Shell Command screen, select Run . |
| Step 5 | Close the
                                          			 Interoperability Gateway Administrator. |

| Step 1 | On the Exchange server on which the Interoperability Gateway is
                                             			 installed, open the Exchange Management Shell. |
|---|---|
| Step 2 | In the left-hand pane, expand Organization Configuration and select Hub Transport . |
| Step 3 | In the main Hub Transport pane, select the Send Connectors tab. |
| Step 4 | In the Actions pane, under Hub Transport, select New Send Connector . |
| Step 5 | In the New SMTP Send Connector wizard, on the Introduction page,
                                             			 enter a Name for the new connector. |
| Step 6 | Under Select the Intended Use for this Send Connector ,
                                             			 select Custom , then select Next . |
| Step 7 | On the Address space page, select Add . |
| Step 8 | For Address, enter the SMTP domain of the remote network, then
                                             			 select OK . |
| Step 9 | Select Next . |
| Step 10 | On the Network settings page, select Route Mail through the Following Smart Hosts . |
| Step 11 | Select Add . |
| Step 12 | For IP Address, enter the IP address of the Unity Connection
                                             			 gateway if messages are routed directly to the gateway, or of a smart host or
                                             			 other relay if one is configured to deliver messages from the Exchange
                                             			 organization to the Unity Connection gateway. |
| Step 13 | Select OK . |
| Step 14 | Select Next to continue to the next page. |
| Step 15 | On the Configure Smart Host Authentication Settings Page, select
                                             			 the type of authentication to use when sending mail between the Exchange
                                             			 organization and the Unity Connection gateway. |
| Step 16 | Select Next to continue to the next page. |
| Step 17 | On the Source Server page, the local Exchange server should be
                                             			 listed by default. Select Next to continue. |
| Step 18 | Confirm the settings on the New Connector page and select New to add the new connector. |
| Step 19 | Select Finish to exit the wizard. |
| Step 20 | On the Send Connectors tab, right-click the connector that you
                                             			 created and select Properties . |
| Step 21 | Set the Protocol Logging Level to Verbose . |
| Step 22 | Select OK to close the properties window. |

| Step 1 | On the Exchange server on which the Interoperability Gateway is
                                             			 installed, open the Exchange Management Shell. |
|---|---|
| Step 2 | In the left-hand pane, expand Server Configuration and select Hub Transport . |
| Step 3 | In the upper Hub Transport pane, select the local Exchange
                                             			 server from the list of servers. |
| Step 4 | In the lower pane, confirm that the title of the pane is the
                                             			 name of the local Exchange server, then select the Receive Connectors tab. |
| Step 5 | In the Actions pane, under the local server name, select New Receive Connector . |
| Step 6 | In the New SMTP Send Connector wizard, on the Introduction page,
                                             			 enter a name for the new connector. |
| Step 7 | Under Select the Intended Use for this Send Connector, select Custom , then select Next . |
| Step 8 | On the Local Network settings page enter the fully qualified
                                             			 domain name of the local server in the Specify the FQDN this Connector Provide
                                             			 in Response to HELO or EHLO: field. |
| Step 9 | Select Next to continue to the next page. |
| Step 10 | On the Remote Network settings page, in the list box, select 0.0.0.0-255.255.255.255 , then select Edit . |
| Step 11 | If messages are received directly from the Unity Connection
                                             			 gateway, enter the IP address of the gateway as both the Start Address and End
                                             			 Address value. If a smart host or other relay external to the Exchange
                                             			 organization delivers messages on behalf of the Unity Connection gateway, enter
                                             			 the IP address of the smart host or relay as both the Start Address and End
                                             			 Address value. |
| Step 12 | Select OK . |
| Step 13 | Select Next to continue to the next page. |
| Step 14 | Confirm the settings on the New Connector page, then select New to add the new connector. |
| Step 15 | Select Finish to exit the wizard. |
| Step 16 | On the Receive Connectors tab, right-click the connector that
                                             			 you created and select Properties . |
| Step 17 | Set the Protocol Logging Level to Verbose . |
| Step 18 | Select the Permission Groups tab. |
| Step 19 | Check the Anonymous Users check box. |
| Step 20 | Select OK to close the properties window. |

| Note | If
                                          		  you are unsure whether adding the IP address of the delivery servers to the
                                          		  Unity Connection gateway IP access list is necessary, do the procedure.
                                          		  Explicitly adding the address of a server for which SMTP connections are
                                          		  automatically accepted does not negatively impact the SMTP server. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration on the Cisco Unity
                                          			 Connection gateway, expand System Settings > SMTP
                                                				  Configuration , then select Server . |
|---|---|
| Step 2 | On the Edit menu, select Search IP Address Access List . |
| Step 3 | Select Add New . |
| Step 4 | On the New Access IP Address page, enter the IP address of the
                                          			 server that delivers messages on behalf of the Cisco Unity site. |
| Step 5 | Select Save . |
| Step 6 | On the Access IP Address page, check the Allow Unity Connection check box. |
| Step 7 | Select Save . |
| Step 8 | Repeat Step 2 through Step 7 for
                                          			 each additional server that delivers messages on behalf of the Cisco Unity
                                          			 site. |

| Step 1 | In the Cisco Unity Administrator on the Cisco Unity site
                                          			 gateway, browse to Network and select Unity Connection Networking . |
|---|---|
| Step 2 | Select Download to download the local site configuration
                                          			 file. |
| Step 3 | Save the file to a location on your hard drive, or on media that
                                          			 you can use to copy the file to the Cisco Unity gateway. Note that the file
                                          			 contains a public key certificate and should be treated as sensitive data. |

| Step 1 | In the Cisco Unity Administrator, go to any Subscribers > Subscriber
                                                   				  Template page. |
|---|---|
| Step 2 | Select the Add icon. |
| Step 3 | In the Add a Subscriber Template dialog box, enter a name. |
| Step 4 | Select New Template or Based on Existing Template . If you select Based on
                                             			 Existing Template, select the applicable template in the Based On field. |
| Step 5 | Select Add . |
| Step 6 | On the Profile page, select a Class of Service and check or
                                             			 uncheck the Show Subscriber in Email Server Address Book check
                                             			 box, as applicable. |
| Step 7 | Select the Distribution Lists page. |
| Step 8 | On the Distribution Lists page, to assign all new users based on
                                             			 this template to a public distribution list, select the list in the Public
                                             			 Distribution Lists box, then select > . To remove a distribution list from those to which new users are
                                                				added, select the list, then select >> . |
| Step 9 | Select the Save icon. |

| Step 1 | In Cisco Unity Connection Administration on the Cisco Unity
                                          			 Connection gateway, expand Networking , expand Links , then select Intersite Links . |
|---|---|
| Step 2 | Select Add . |
| Step 3 | On the New Intersite Link page, select Link to Cisco Unity Site or Cisco Unity Connection Site by
                                             				Manually Exchanging Configuration Files . |
| Step 4 | Select Download and save the Unity Connection site
                                          			 configuration file to a location on your hard drive, or on media that you can
                                          			 use to copy the file to the Cisco Unity gateway. Note that the file contains a
                                          			 public key certificate and should be treated as sensitive data. |
| Step 5 | Select Browse and upload the Cisco Unity configuration file
                                          			 that you downloaded in the Downloading
                                             				the Cisco Unity Gateway Configuration File . |
| Step 6 | For Transfer Protocol settings, decide whether you want to
                                          			 enable SSL to encrypt directory synchronization traffic between Cisco Unity and
                                          			 Cisco Unity Connection. Caution To enable SSL, you must configure the
                                                         				  Cisco Unity server to use SSL, which affects multiple applications that access
                                                         				  the Cisco Unity server. See the applicable version of the Security Guide for Cisco Unity at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_maintenance_guides_list.html . | Caution | To enable SSL, you must configure the
                                                         				  Cisco Unity server to use SSL, which affects multiple applications that access
                                                         				  the Cisco Unity server. See the applicable version of the Security Guide for Cisco Unity at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_maintenance_guides_list.html . |
| Caution | To enable SSL, you must configure the
                                                         				  Cisco Unity server to use SSL, which affects multiple applications that access
                                                         				  the Cisco Unity server. See the applicable version of the Security Guide for Cisco Unity at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_maintenance_guides_list.html . |
| Step 7 | For Synchronization Settings, check the Include Distribution
                                          			 Lists When Synchronizing Directory Data check box to have system distribution
                                          			 lists that are created on the Cisco Unity site replicated to Unity Connection
                                          			 so that Unity Connection users can address messages to them. (Note that only
                                          			 the list name and other information used in addressing are replicated.) Note In order for individual system distribution lists to be offered
                                                      				for synchronization by the Cisco Unity gateway, they must also be marked to
                                                      				allow synchronization. By default, individual Cisco Unity system distribution
                                                      				lists are not marked to allow synchronization. The task list alerts you when
                                                      				and how to enable individual lists for synchronization. | Note | In order for individual system distribution lists to be offered
                                                      				for synchronization by the Cisco Unity gateway, they must also be marked to
                                                      				allow synchronization. By default, individual Cisco Unity system distribution
                                                      				lists are not marked to allow synchronization. The task list alerts you when
                                                      				and how to enable individual lists for synchronization. |
| Note | In order for individual system distribution lists to be offered
                                                      				for synchronization by the Cisco Unity gateway, they must also be marked to
                                                      				allow synchronization. By default, individual Cisco Unity system distribution
                                                      				lists are not marked to allow synchronization. The task list alerts you when
                                                      				and how to enable individual lists for synchronization. |
| Step 8 | To convert recorded names from this site to a different encoding
                                          			 when synchronizing them with the remote site, check the Convert Outgoing Recorded Names To check box, and
                                          			 select the codec to use. Note Verify that the codec you select is the correct one for the
                                                      				Cisco Unity site gateway. If you need to change the recording format after
                                                      				creating the intersite link, you must clear all recorded names and then
                                                      				resynchronize all directory data and names using the Clear Recorded Names and
                                                      				Resync All buttons on the Networking > Intersite Links > Search Intersite
                                                      				Links page in Cisco Unity Connection Administration.This can have a heavy
                                                      				performance impact and should only be performed during non-business hours. Do not select G711 a-law format when setting up an intersite
                                                         				  link to a Cisco Unity site gateway. | Note | Verify that the codec you select is the correct one for the
                                                      				Cisco Unity site gateway. If you need to change the recording format after
                                                      				creating the intersite link, you must clear all recorded names and then
                                                      				resynchronize all directory data and names using the Clear Recorded Names and
                                                      				Resync All buttons on the Networking > Intersite Links > Search Intersite
                                                      				Links page in Cisco Unity Connection Administration.This can have a heavy
                                                      				performance impact and should only be performed during non-business hours. Do not select G711 a-law format when setting up an intersite
                                                         				  link to a Cisco Unity site gateway. |
| Note | Verify that the codec you select is the correct one for the
                                                      				Cisco Unity site gateway. If you need to change the recording format after
                                                      				creating the intersite link, you must clear all recorded names and then
                                                      				resynchronize all directory data and names using the Clear Recorded Names and
                                                      				Resync All buttons on the Networking > Intersite Links > Search Intersite
                                                      				Links page in Cisco Unity Connection Administration.This can have a heavy
                                                      				performance impact and should only be performed during non-business hours. Do not select G711 a-law format when setting up an intersite
                                                         				  link to a Cisco Unity site gateway. |
| Step 9 | By default, two tasks that each run on their own schedule to
                                          			 pull directory data and recorded names from Cisco Unity to Unity Connection are
                                          			 enabled immediately after you create the intersite link. To disable either type
                                          			 of directory synchronization until you manually edit and enable the applicable
                                          			 synchronization task, uncheck the Enable Task to Synchronize Directory Data After the
                                             				Join or Enable Task to Synchronize Recorded Names After the
                                             				Join check boxes. You should perform the initial synchronization outside of normal
                                             				business hours to avoid peak traffic times. In particular, if your Cisco Unity
                                             				site gateway is a Platform Overlay 1 server, the synchronization activity can
                                             				cause noticeable delays in the user conversation. |
| Step 10 | For Intersite Routing, select the appropriate option: Route to this Remote Site Through —Enter the specific IP
                                                   					 address or fully-qualified domain name of a Microsoft Exchange server in your
                                                   					 organization that can accept SMTP messages and route them to the
                                                   					 Interoperability Gateway for Microsoft Exchange. The host must be able to
                                                   					 accept SMTP messages sent from the Unity Connection gateway to addresses at the
                                                   					 interoperability domain. Route to this Remote Site Through SMTP Smart Host (If One Is
                                                      						Defined) —Routes outgoing messages to the host that is defined on the System
                                                   					 Settings > SMTP Configuration > Smart Host page. If you select this
                                                   					 option, the smart host must be defined, and must be able to accept SMTP
                                                   					 messages sent from the Unity Connection gateway to addresses at the
                                                   					 interoperability domain. If the smart host is not defined, a non-delivery
                                                   					 receipt (NDR) is sent to the message sender. Route to this Remote Site Through the Remote Site
                                                      						Gateway —Routes outgoing messages to the Cisco Unity gateway. Use this
                                                   					 option only if Microsoft Exchange is installed on the Cisco Unity server and
                                                   					 the server is able to accept SMTP messages sent from the Unity Connection
                                                   					 gateway to addresses at the interoperability domain. |
| Step 11 | Select Link . |

| Caution | To enable SSL, you must configure the
                                                         				  Cisco Unity server to use SSL, which affects multiple applications that access
                                                         				  the Cisco Unity server. See the applicable version of the Security Guide for Cisco Unity at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_maintenance_guides_list.html . |
|---|---|

| Note | In order for individual system distribution lists to be offered
                                                      				for synchronization by the Cisco Unity gateway, they must also be marked to
                                                      				allow synchronization. By default, individual Cisco Unity system distribution
                                                      				lists are not marked to allow synchronization. The task list alerts you when
                                                      				and how to enable individual lists for synchronization. |
|---|---|

| Note | Verify that the codec you select is the correct one for the
                                                      				Cisco Unity site gateway. If you need to change the recording format after
                                                      				creating the intersite link, you must clear all recorded names and then
                                                      				resynchronize all directory data and names using the Clear Recorded Names and
                                                      				Resync All buttons on the Networking > Intersite Links > Search Intersite
                                                      				Links page in Cisco Unity Connection Administration.This can have a heavy
                                                      				performance impact and should only be performed during non-business hours. Do not select G711 a-law format when setting up an intersite
                                                         				  link to a Cisco Unity site gateway. |
|---|---|

| Caution | When you do Step 12 in the following procedure, synchronization of Unity Connection objects to
                                          		  Cisco Unity begins automatically. You should do this step outside of normal
                                          		  business hours to avoid peak traffic times. In particular, if your Cisco Unity
                                          		  site gateway is a Platform Overlay 1 server, the synchronization activity can
                                          		  cause noticeable delays in the user conversation. |
|---|---|

| Step 1 | In the Cisco Unity Administrator on the Cisco Unity site
                                          			 gateway, browse to Network and select Unity Connection Networking . |
|---|---|
| Step 2 | On the Unity Connection Networking page, in the Remote
                                          			 Configuration File field, select Browse and upload the Unity Connection configuration file that
                                          			 you downloaded in Step 4 of the Creating the Intersite Link on the Unity Connection Gateway . |
| Step 3 | Select Add . |
| Step 4 | For Template, select the template that you selected or created
                                          			 in the “Setting
                                             				Up a Template for Unity Connection Users on the Cisco Unity Gateway” section on
                                             				page 3-11 . The template is used to create Cisco Unity directory objects
                                          			 for Unity Connection users so that Cisco Unity users can address messages to
                                          			 them. You must select a template before you can create the intersite link. |
| Step 5 | Optionally, enter a Display Name Suffix. When the Cisco Unity
                                          			 site gateway creates directory objects for Unity Connection users and any
                                          			 replicated system distribution lists, this suffix is placed at the end of the
                                          			 display names of the objects. This can help Cisco Unity users locate the proper
                                          			 contact to use for addressing messages in Microsoft Outlook or other clients
                                          			 that access the directory, particularly if Unity Connection users already have
                                          			 Active Directory accounts prior to creating the intersite link. Tip If you do not want to append a suffix to Unity Connection user
                                                         				  and system distribution list objects, delete the default text in the Display
                                                         				  Name Suffix field and leave the field blank. | Tip | If you do not want to append a suffix to Unity Connection user
                                                         				  and system distribution list objects, delete the default text in the Display
                                                         				  Name Suffix field and leave the field blank. |
| Tip | If you do not want to append a suffix to Unity Connection user
                                                         				  and system distribution list objects, delete the default text in the Display
                                                         				  Name Suffix field and leave the field blank. |
| Step 6 | Check the
                                          			 Synchronize Distribution Lists check box to have system distribution lists that
                                          			 are created on the Unity Connection site replicated to Cisco Unity so that
                                          			 Cisco Unity users can address messages to them. (Note that only the list name
                                          			 and other information used in addressing are replicated.) Note In order
                                                      				for individual system distribution lists to be offered for synchronization by
                                                      				the Unity Connection gateway, they must also be marked to allow
                                                      				synchronization. By default, individual Unity Connection system distribution
                                                      				lists are marked to allow synchronization, although this setting may have been
                                                      				changed. The task list alerts you when and how to enable individual lists for
                                                      				synchronization. | Note | In order
                                                      				for individual system distribution lists to be offered for synchronization by
                                                      				the Unity Connection gateway, they must also be marked to allow
                                                      				synchronization. By default, individual Unity Connection system distribution
                                                      				lists are marked to allow synchronization, although this setting may have been
                                                      				changed. The task list alerts you when and how to enable individual lists for
                                                      				synchronization. |
| Note | In order
                                                      				for individual system distribution lists to be offered for synchronization by
                                                      				the Unity Connection gateway, they must also be marked to allow
                                                      				synchronization. By default, individual Unity Connection system distribution
                                                      				lists are marked to allow synchronization, although this setting may have been
                                                      				changed. The task list alerts you when and how to enable individual lists for
                                                      				synchronization. |
| Step 7 | Check the Synchronize Voice Names check box to have
                                          			 Cisco Unity synchronize voice names for Unity Connection users and system
                                          			 distribution lists. |
| Step 8 | If you enabled
                                          			 SSL in Step 6 of the Creating
                                             				the Intersite Link on the Unity Connection Gateway , check the Use
                                             				Secure Sockets Layer (SSL) check box. If the Unity Connection site
                                          			 gateway is using a self-signed certificate (the default for Unity Connection),
                                          			 also check the Use
                                             				Self-Signed Certificates check box. |
| Step 9 | For Outbound
                                          			 Audio Conversion, if you want to convert voice names to a different format
                                          			 before sending them to the Unity Connection site gateway, select a codec in the
                                          			 Voice Names field. Note Verify that the codec you select is the correct one for the
                                                         				  Unity Connection site gateway. If you need to change the recording format after
                                                         				  creating the intersite link, you must clear all recorded names and then
                                                         				  resynchronize all directory data and names using the Clear Voice Names and
                                                         				  Total Sync buttons on the Networking > Unity Connection Networking >
                                                         				  Profile page in the Cisco Unity Administrator. This can have a heavy
                                                         				  performance impact and should only be done during non-business hours. | Note | Verify that the codec you select is the correct one for the
                                                         				  Unity Connection site gateway. If you need to change the recording format after
                                                         				  creating the intersite link, you must clear all recorded names and then
                                                         				  resynchronize all directory data and names using the Clear Voice Names and
                                                         				  Total Sync buttons on the Networking > Unity Connection Networking >
                                                         				  Profile page in the Cisco Unity Administrator. This can have a heavy
                                                         				  performance impact and should only be done during non-business hours. |
| Note | Verify that the codec you select is the correct one for the
                                                         				  Unity Connection site gateway. If you need to change the recording format after
                                                         				  creating the intersite link, you must clear all recorded names and then
                                                         				  resynchronize all directory data and names using the Clear Voice Names and
                                                         				  Total Sync buttons on the Networking > Unity Connection Networking >
                                                         				  Profile page in the Cisco Unity Administrator. This can have a heavy
                                                         				  performance impact and should only be done during non-business hours. |
| Step 10 | Review and
                                          			 continue entering settings, as applicable. |
| Step 11 | When you have
                                          			 finished entering settings, select the Save icon. |
| Step 12 | Select Join . |

| Tip | If you do not want to append a suffix to Unity Connection user
                                                         				  and system distribution list objects, delete the default text in the Display
                                                         				  Name Suffix field and leave the field blank. |
|---|---|

| Note | In order
                                                      				for individual system distribution lists to be offered for synchronization by
                                                      				the Unity Connection gateway, they must also be marked to allow
                                                      				synchronization. By default, individual Unity Connection system distribution
                                                      				lists are marked to allow synchronization, although this setting may have been
                                                      				changed. The task list alerts you when and how to enable individual lists for
                                                      				synchronization. |
|---|---|

| Note | Verify that the codec you select is the correct one for the
                                                         				  Unity Connection site gateway. If you need to change the recording format after
                                                         				  creating the intersite link, you must clear all recorded names and then
                                                         				  resynchronize all directory data and names using the Clear Voice Names and
                                                         				  Total Sync buttons on the Networking > Unity Connection Networking >
                                                         				  Profile page in the Cisco Unity Administrator. This can have a heavy
                                                         				  performance impact and should only be done during non-business hours. |
|---|---|

| Note | By
                                          		  default, for each Unity Connection location, the default <Server Name>
                                          		  Partition is used as the Local Partition That Cisco Unity Users Can Address To
                                          		  By Extension. Cisco Unity users cannot address messages by extension to any
                                          		  Unity Connection users who do not have an extension in this partition. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration (on any location),
                                          			 expand Networking > and select Locations . |
|---|---|
| Step 2 | Expand Local Site and select the display name of the local
                                          			 location (the location on which you are accessing Unity
                                          			 Connection Administration). |
| Step 3 | Under Local Partition That Cisco Unity Users Can Address To By
                                          			 Extension, for Partition, select the name of the partition to use. |
| Step 4 | Select Save . |
| Step 5 | Repeat Step 1 through Step 4 on each
                                          			 Unity Connection location in the site. |

| Step 1 | On the Cisco Unity server desktop, double-click the Cisco Unity
                                             			 Tools Depot icon. (If the location is using failover, start the procedure on
                                             			 the primary server.) |
|---|---|
| Step 2 | In the left pane, under Administrative Tools,
                                             			 double-click Advanced Settings
                                                				Tool . |
| Step 3 | In the Unity Settings pane, click Networking - Enable Identified Subscriber Messaging (ISM) for
                                                				AMIS, Bridge, VPIM and Trusted Internet Subscribers . |
| Step 4 | In the New Value list, click 1 , then click Set . |
| Step 5 | When prompted, click OK . |
| Step 6 | Click Exit . |
| Step 7 | Restart Cisco Unity for the registry setting to take effect. |
| Step 8 | If the location is using failover, repeat Step 1 through Step 7 on the
                                             			 secondary server. |
| Step 9 | Repeat Step 1 through Step 8 on each
                                             			 Cisco Unity location in the site. |