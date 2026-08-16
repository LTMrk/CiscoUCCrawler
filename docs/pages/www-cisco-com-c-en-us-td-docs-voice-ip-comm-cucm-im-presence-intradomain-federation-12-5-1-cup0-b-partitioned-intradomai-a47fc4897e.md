---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-intradomain-federation-12-5-1-cup0-b-partitioned-intradomai-a47fc4897e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/intradomain_federation/12_5_1/cup0_b_partitioned-intradomain-federation-1251/cup0_b_partitioned-intradomain-federation-1251_chapter_01.html
retrieved_at: 2026-08-16T16:16:02.487063+00:00
---

Partitioned Intradomain Federation Guide for the IM and Presence Service

# Partitioned Intradomain Federation Guide for the IM and Presence Service

Updated: January 17, 2019

Chapter: Planning for Integration

## Chapter: Planning for Integration

# Planning for Integration

## Supported
                        	 Partitioned Intradomain Federation Integrations

For partitioned
                              		  intradomain federation with Microsoft Lync or Skype for Business , you must configure TLS; TCP is not
                              		  supported. For more information, see Microsoft Lync Configuration for Partitioned Intradomain Federation or Skype for Business Configuration for Partitioned Intradomain Federation .

This
                              		  chapter describes the configuration steps for enabling partitioned intradomain
                              		  federation between IM and Presence
                                 			 Service and Microsoft Skype for Business /Lync/OCS .
                              		  The following Microsoft server platforms are supported:

Microsoft Skype for Business Server, 2015, Standard Edition and Enterprise Edition

Microsoft Lync
                                    				Server 2013, Standard Edition and Enterprise Edition

Microsoft Lync
                                    				Server 2010, Standard Edition and Enterprise Edition

Microsoft Office Communications
                                       				  Server 2007 Release 2, Standard Edition and Enterprise Edition

IM and
                                 			 Presence Service does not support an ASA in partitioned intradomain
                              		  federation.

If you have a
                                          			 mixed deployment of both Lync and OCS servers, you must run the user migration
                                          			 tools for the Lync users, and then run the user migration tools for the OCS
                                          			 users.

We recommended that you use the Federation Wizard to configure Partitioned Intradomain Federation. This Federation Wizard
                              allows you to automatically configure partitioned intradomain federation with Microsoft Lync or Skype for Business , by creating the Static Routes, Access Control Lists and TLS peers that are required for Partitioned Intradomain Federation
                              and provides the Windows server PowerShell CLI commands required to configure modifications on the Microsoft server.

To launch the Federation wizard from the Cisco Unified CM IM and Presence Administration, click Cisco Unified CM IM and Presence Service Administation > Presence > Federation Wizard .

However you can still manually configure this feature.

### Presence Web
                           	 Service API Support

The Presence Web
                                 		  Service is an open interface that allows client applications to share user
                                 		  presence information with IM and Presence Service . Third party developers use
                                 		  this interface to build client applications that can send and retrieve updates
                                 		  about the presence state of a user. Note the following restriction about
                                 		  Presence Web Service API support:

For
                                       				partitioned intradomain federation, you cannot use the Presence Web Service API
                                       				to obtain presence information from non-Cisco clients.

For more
                                 		  information about the Presence Web Service, see the IM and
                                    			 Presence Service Developer Guide at https://developer.cisco.com/site/collaboration/call-control/unified-presence/documentation/index.gsp .

### Limitations for Microsoft Lync Integrations

You already have intradomain federation configured for video with Cisco VCS or Cisco Expressway and want to add partitioned
                                             intradomain federation with IM and Presence Service: Microsoft Lync is integrated with Cisco VCS or Cisco Expressway and you have a static route configured on Lync to route video
                                          and voice traffic for the local Lync presence domain to Cisco VCS or Cisco Expressway. If you modify the static route to point
                                          to IM and Presence Service (a requirement for partitioned intradomain federation) you will break the existing video integration because the traffic
                                          that is intended for Cisco VCS or Cisco Expressway would instead be routed to IM and Presence Service . You cannot have both video integration and partitioned intradomain federation to IM and Presence Service.

You already have integration with Microsoft Exchange Unified Messaging and want to add partitioned intradomain federation
                                             with IM and Presence Service: You have a Microsoft Lync server configured for Unified Messaging to Microsoft Exchange (either on-premises, or to the cloud
                                          (Office365). If you add a static route from Lync for the local Lync presence domain to point to IM and Presence Service (a requirement for partitioned intradomain federation), Unified Messaging integration between Lync and Microsoft Exchange
                                          for the domain will be terminated because all Unified Messaging SIP traffic for that domain will be routed to IM and Presence Service . You cannot have both integration to Microsoft Exchange Unified Messaging and partitioned intradomain federation to IM and Presence Service .

Neither Microsoft Exchange Unified Messaging nor Cisco VCS (or Cisco Expressway) integrations are supported with partitioned
                                             intradomain federation if you are sharing the same domain between Microsoft Lync and IM and Presence Service .

## Hardware
                        	 Requirements

The following Cisco hardware is required:

IM
                                       				  and Presence Service node. For IM and Presence
                                       				  Service hardware support, refer to the IM and Presence
                                       				  Service compatibility matrix.

Cisco Unified Communications Manager node. For Cisco Unified Communications Manager hardware support,
                                    				refer to the compatibility information for Cisco Unified Communications Manager document
                                    				available on Cisco.com.

In
                                          			 Release 10.0(1) and later, Cisco supports only virtualized deployments of Cisco Unified Communications Manager (Unified
                                          			 Communications Manager) and IM and Presence Service on Cisco Unified Computing
                                          			 System servers, or on a Cisco-approved third-party server configuration. In
                                          			 Release 10.0(1) and later, Cisco does not support deployments of Cisco Unified Communications Manager or IM and Presence Service on Cisco Media Convergence
                                          			 Server servers.

For more
                                          			 information about the deployment of Cisco Unified Communications Manager or IM and Presence Service in a virtualized environment,
                                          			 see: http://docwiki.cisco.com/wiki/Unified_Communications_in_a_Virtualized_Environment .

## Software
                        	 Requirements

The
                              		  following sections outline the software required for partitioned intradomain
                              		  federation.

### Server
                           	 Software

The
                                 		  following server software is required for partitioned intradomain federation:

#### Cisco
                                 		  Software

IM
                                          				  and Presence Service

Cisco Unified Communications
                                          				  Manager

#### Microsoft
                                 		  Software

Depending on the
                                       				deployment, one of:

Microsoft Skype for Business Server, 2015, Standard Edition and Enterprise Edition

Microsoft
                                             					 Lync Server 2013, Standard Edition or Enterprise Edition

Microsoft
                                             					 Lync Server 2010, Standard Edition or Enterprise Edition

Microsoft Office Communications
                                                						Server 2007 Release 2, Standard or Enterprise Edition

Depending on the
                                       				deployment, one of:

Lync
                                             					 Administrative Tools (optional install item available during installation of
                                             					 Lync)

OCS
                                             					 Administrative Tools (optional install item available during installation of
                                             					 OCS)

Microsoft Active
                                       				Directory

#### Other
                                 		  Software

Each of the user migration
                                 		  tools that Cisco provides requires that at least version 2.0 of the .NET
                                 		  Framework is installed on the server where you are running the tool. While
                                 		  attempting to run any of the user migration tools you may receive the following
                                 		  error: "Application failed to initialize properly". The reason for this error
                                 		  is that you are attempting to run the user migration tools without the .NET 2.0
                                 		  or newer Framework installed.

The .NET 2.0 Framework comes
                                 		  installed as standard on Windows Server 2003 R2 or newer.

### Client
                           	 Software

The client
                                 		  software required for partitioned intradomain federation deployment between the IM and Presence Service and Skype for Business /Lync/OCS depends on your deployment. You can have any combination of IM and Presence Service supported clients in a
                                 		  partitioned intradomain federation deployment.

#### IM and Presence
                              	 Service Supported Clients

The
                                    		  following IM and Presence Service clients are supported in a
                                    		  partitioned intradomain federation deployment between IM and Presence Service and Skype for Business /Lync/OCS :

##### Cisco
                                    		  Software

Cisco
                                             				  Unified Personal Communicator Release 8.5

Cisco
                                             				  Jabber for Mac

Cisco Jabber for
                                             				  Windows

Cisco
                                             				  Jabber IM for Mobile (iPhone, Android, Blackberry)

Cisco
                                             				  Jabber for iPad

Cisco
                                             				  Jabber for Cius

For version
                                                			 compatibility for all Cisco Jabber clients, see the appropriate Cisco Jabber client documentation.

If the Directory URI IM
                                                			 address scheme is used in your deployment, your client software must support
                                                			 Directory URI.

##### Third-Party
                                    		  Software

Third-party
                                    		  XMPP clients

#### Microsoft Server
                              	 Supported Clients

Depending
                                    		  on the deployment, the following clients are supported:

Skype for Business 2015

Microsoft Lync
                                          				2013

Microsoft Lync
                                          				2010

Microsoft Office Communicator 2007 Release 2

Microsoft Office Communicator 2005

Communicator Web Access 2007 Release 2

Communicator Web
                                          				Access 2005

##### Related
                                    		  Topic

Hardware Requirements

## Integration
                        	 Preparation

It is
                              		  essential that you plan carefully for the configuration of partitioned
                              		  intradomain federation between IM and Presence
                                 			 Service and Skype for Business /Lync/OCS .
                              		  Read the items in this section before you begin any configuration for this
                              		  integration.

### Presence
                           	 Domains

Partitioned Intradomain
                                 		  Federation, by its nature, supports integration between IM and Presence Service and the Microsoft server
                                 		  within a common presence domain that is configured on both systems. Both IM and Presence Service and the Microsoft server
                                 		  support the configuration of multiple presence domains. However, any Microsoft
                                    			 Lync or Microsoft Office
                                    			 Communicator users that are not configured for a matching IM and Presence Service domain cannot participate in
                                 		  partitioned Intradomain federation communications.

For example, in the following
                                 		  figure, users who are configured in the synergy.online.com domain cannot share
                                 		  IM availability or emails with IM and Presence
                                    			 Service users who are configured in synergy.com and synergy.co.uk
                                 		  domains because the synergy.online.com domain is not configured on IM and Presence Service . You must add the
                                 		  synergy.online.com domain to IM and Presence Service before those users can share
                                 		  availability with the other users in intradomain federation.

### User
                           	 Migration

If users
                                 		  are being migrated from Skype for Business /Lync/OCS to the IM and Presence
                                    			 Service as part of this integration, consider the information below.

If users are being migrated
                                 		  from Lync/OCS to IM and Presence Service as part of this integration, please be aware that IM and Presence Service maintains the Microsoft server identities of
                                 		  users when the Directory URI IM address scheme is configured, which can in turn
                                 		  be mapped to the Lync SIP URI.

To use the
                                             			 Directory URI IM address scheme, all clients on the IM and Presence Service cluster must support Directory
                                             			 URI.

For more information about
                                 		  planning for user migration, see topics related to planning for user migration.

### DNS
                           	 Configuration

Domain
                                 		  Name System (DNS) "A" records must
                                 		  be published within the enterprise for all IM and Presence Service nodes and Skype for Business /Lync/OCS servers.

Microsoft
                                 		  servers must be able to resolve Fully Qualified Domain Names (FQDN) and IP
                                 		  addresses for all IM and Presence Service nodes.

Likewise, IM and Presence Service nodes must be able
                                 		  to resolve FQDNs and IP addresses for all Microsoft server and pool FQDNs.

### Certificate
                           	 Authority Server

If TLS
                                 		  encryption is enabled as part of this partitioned intradomain federation
                                 		  integration, an external or internal Certificate Authority (CA) may be used to
                                 		  sign security certificates on IM and Presence Service and Skype for Business /Lync/OCS .
                                 		  Cisco recommends that you use the same CA to sign the Microsoft server and the IM and Presence Service certificates. If not, the root
                                 		  certificates for each CA must be uploaded onto the Microsoft server and the IM and Presence Service nodes.

### High
                           	 Availability

You need
                                 		  to consider how you are going to configure availability in your partitioned
                                 		  intradomain federation deployment.

If you
                                 		  wish to make your IM and Presence
                                    			 Service partitioned intradomain federation capability highly
                                 		  available, you can deploy a load balancer in front of your designated (routing) IM and Presence Service nodes.

To deploy load
                                             			 balancing (for example, round robin), a hardware load balancer needs to be
                                             			 installed. The static route in IM and Presence Service points to the load balancer.

#### Related
                                 		  Topic

High Availability for Intradomain Federation

## Prerequisite
                        	 Configuration for IM and Presence Service

You must
                              		  complete the following tasks on the IM and Presence Service before you begin to configure
                              		  partitioned intradomain federation.

Install and
                                    				configure IM and Presence
                                       				  Service .

Perform the
                                    				following checks to ensure that your IM and Presence Service system is operating properly:

Run the IM and Presence
                                             						Service System Configuration Troubleshooter.

Check that
                                          					 you can add local contacts to the Jabber client of IM and Presence
                                             						Service .

Check that
                                          					 your clients are receiving availability states from the IM and Presence
                                             						Service node.

## Additional
                        	 Configuration for Routing IM and Presence Service Node

In
                              		  multi-server deployments, an IM and Presence Service node must be dedicated as the
                              		  Routing IM and Presence Service node. This means that it is a
                              		  front-end server that accepts all new inbound SIP requests from the Skype for Business /Lync/OCS and routes them onwards to the IM and Presence Service node on which the request
                              		  recipient is homed.

Cisco
                              		  recommends that you do not assign any users to the Routing IM and Presence Service node; as this ensures that the
                              		  Routing IM and Presence Service node has the capacity to
                              		  handle the volume of SIP traffic from the Microsoft server.

Because no
                              		  users are assigned to the Routing IM and Presence Service node, you can deactivate many
                              		  of the feature services to free up resources on the Routing IM and Presence Service node. Deactivate the following
                              		  feature services on the Routing IM and Presence Service node:

Cisco Presence
                                    				Engine

Cisco XCP Text
                                    				Conference Manager

Cisco XCP Web
                                    				Connection Manager

Cisco XCP
                                    				Connection Manager

Cisco XCP SIP
                                    				Federation Connection Manager

Cisco XCP XMPP
                                    				Federation Connection Manager

Cisco XCP
                                    				Message Archiver

Cisco XCP
                                    				Directory Service

Cisco XCP
                                    				Authentication Service

### Related
                              		  Topic

Configure the Routing Node

## Plan Services
                        	 Restarts during Off-Peak Periods

During the
                              		  integration process, you need to restart the Skype for Business /Lync/OCS server front-end services. Plan to perform the services restart during off-peak
                              		  periods, such as during a maintenance window, to minimize the impact to users.
                              		  For more information, see the partitioned intradomain federation configuration
                              		  workflows and topics related to restarting services for your server type.

| Note | If you have a
                                          			 mixed deployment of both Lync and OCS servers, you must run the user migration
                                          			 tools for the Lync users, and then run the user migration tools for the OCS
                                          			 users. |
|---|---|

| Note | Neither Microsoft Exchange Unified Messaging nor Cisco VCS (or Cisco Expressway) integrations are supported with partitioned
                                             intradomain federation if you are sharing the same domain between Microsoft Lync and IM and Presence Service . |
|---|---|

| Note | In
                                          			 Release 10.0(1) and later, Cisco supports only virtualized deployments of Cisco Unified Communications Manager (Unified
                                          			 Communications Manager) and IM and Presence Service on Cisco Unified Computing
                                          			 System servers, or on a Cisco-approved third-party server configuration. In
                                          			 Release 10.0(1) and later, Cisco does not support deployments of Cisco Unified Communications Manager or IM and Presence Service on Cisco Media Convergence
                                          			 Server servers. For more
                                          			 information about the deployment of Cisco Unified Communications Manager or IM and Presence Service in a virtualized environment,
                                          			 see: http://docwiki.cisco.com/wiki/Unified_Communications_in_a_Virtualized_Environment . |
|---|---|

| Note | For version
                                                			 compatibility for all Cisco Jabber clients, see the appropriate Cisco Jabber client documentation. If the Directory URI IM
                                                			 address scheme is used in your deployment, your client software must support
                                                			 Directory URI. |
|---|---|

| Note | To use the
                                             			 Directory URI IM address scheme, all clients on the IM and Presence Service cluster must support Directory
                                             			 URI. |
|---|---|

| Note | To deploy load
                                             			 balancing (for example, round robin), a hardware load balancer needs to be
                                             			 installed. The static route in IM and Presence Service points to the load balancer. |
|---|---|