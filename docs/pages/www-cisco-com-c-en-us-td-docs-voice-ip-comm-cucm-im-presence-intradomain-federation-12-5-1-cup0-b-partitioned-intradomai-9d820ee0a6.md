---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-intradomain-federation-12-5-1-cup0-b-partitioned-intradomai-9d820ee0a6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/intradomain_federation/12_5_1/cup0_b_partitioned-intradomain-federation-1251/cup0_b_partitioned-intradomain-federation-1251_chapter_00.html
retrieved_at: 2026-08-16T16:15:58.836733+00:00
---

Partitioned Intradomain Federation Guide for the IM and Presence Service

# Partitioned Intradomain Federation Guide for the IM and Presence Service

Updated: January 17, 2019

Chapter: Integration Overview

## Chapter: Integration Overview

# Integration Overview

## Partitioned
                        	 Intradomain Federation

More and more enterprises are
                              		  choosing Cisco Unified Communications Manager IM and Presence
                                 			 Service as their IM and availability platform. These enterprises
                              		  already have Microsoft
                                 			 Lync or Microsoft Office Communications
                                 			 Server (OCS) deployed and want to move their users over to an IM and Presence Service supported client.

During this
                              		  transition, it is important that these users who migrate to an IM and Presence Service supported client can continue
                              		  to share availability and instant messages with those users who are still using
                              		  the Microsoft servers. For more information about supported IM and Presence Service clients, see the "Software
                                 			 Requirements" section.

Partitioned intradomain
                              		  federation enables IM and Presence Service client users and Microsoft
                                 			 Lync or Microsoft Office
                                 			 Communicator users within the same enterprise to exchange presence
                              		  Availability and IM.

This integration allows both IM and Presence Service and the Microsoft server to
                              		  host a common domain or set of domains. Each user within those domains is
                              		  enabled on either IM and Presence Service or the Microsoft server.

Partitioned
                                          			 intradomain federation requires that a user is enabled on one system only. This
                                          			 integration does not support a user that is enabled on both IM and Presence Service and the Microsoft server at
                                          			 the same time.

IM and Presence Service uses the standard Session
                              		  Initiation Protocol (SIP RFC 3261) to provide partitioned intradomain
                              		  federation support for the following Microsoft server platforms:

Microsoft Skype for Business Server 2015, Standard Edition and Enterprise Edition

Microsoft Lync
                                    				Server 2013, Standard Edition and Enterprise Edition

Microsoft Lync
                                    				Server 2010, Standard Edition and Enterprise Edition

Microsoft Office Communications
                                       				  Server 2007 R2 Standard Edition and Enterprise Edition

The term
                                          			 Microsoft server is used in this document to refer to all supported Skype for Business, Lync and
                                          			 OCS platform types. Any information that is specific to a certain platform is
                                          			 identified.

### Partitioned
                           	 Federation Deployment Overview

The
                              		following figure shows a high-level sample deployment of IM and Presence Service and Microsoft OCS within the
                              		same domain. This example shows an OCS deployment, but it also applies to the
                              		other supported Microsoft servers.

Both single presence
                              		domain and multiple presence domain deployments are supported. For multiple
                              		presence domain deployments, you must configure identical presence domains on
                              		both systems.

### Single Domain
                           	 Example

In this example,
                              		users within the presence domain called synergy.com on both the IM
                                 		  and Presence Service node and the Microsoft Lync server are able to
                              		exchange Availability and IM using partitioned intradomain federation because
                              		the synergy.com presence domain is configured on both systems. The common
                              		active directory enables contact searches and display name resolution for all
                              		users on both systems.

Presence domains
                                          		  must be identical. For example, user1@abc.synergy.com cannot share IM and
                                          		  Availability with any of the federated users configured for intradomain
                                          		  federation on synergy.com. Move user1 from the abc.synergy.com presence domain
                                          		  to the synergy.com domain to enable user1 to participate in Partitioned
                                          		  Intradomain Federation in this example.

### Multiple Domain
                           	 Example

In this example,
                                 		  users within the presence domains called synergy.com and synergy.co.uk on both
                                 		  the IM and Presence Service node and the Microsoft Lync
                                 		  server are able to exchange Availability and IM using Intradomain Federation
                                 		  because those domains are configured on both systems. The common active
                                 		  directory enables contact searches and display presence name resolution for all
                                 		  users on both systems. See the following figure.

### Multiple Domain
                           	 Misconfiguration Example

In this example,
                              		users on the domains called synergy.com and synergy.co.uk are properly
                              		configured for partitioned intradomain federation and can exchange IM and
                              		Availability. However, users within the domain called synergy.online.com on the
                              		Lync server are unable to exchange Availability and IM with users in the
                              		federated IM and Presence Service system because the
                              		synergy.online.com domain is not configured on the IM and Presence
                                 		  Service node. See the following figure.

To enable
                              		synergy.online.com users to exchange Availability and IM with users in the
                              		federated IM and Presence Service system, add a domain called
                              		synergy.online.com to the IM and Presence Service node.

You can configure
                                          		  additional presence domains on the IM and Presence Service system even if no users are
                                          		  initially assigned to those domains.

## Partitioned
                        	 Intradomain Federation Configuration

IM and Presence Service node

Microsoft
                                       				server

User migration

Tip

See the
                                          			 detailed configuration workflows for the start-to-finish steps needed to enable
                                          			 partitioned intradomain federation and for links to the procedures that are
                                          			 performed at each step of the process.

Cisco recommends
                              		  that you back up the Microsoft server user contact list information before
                              		  proceeding to configure partitioned intradomain federation between IM and Presence
                                 			 Service and your Microsoft server.

Task

O =
                                          					 Optional

M =
                                          					 Mandatory

Ensure
                                          					 that all required domains are configured on the IM and Presence
                                             						Service node and verify that matching domains are configured on the
                                          					 Microsoft servers

M

Enable
                                          					 partitioned intradomain federation

M

Set up
                                          					 static routes to the Microsoft server

M

Set up
                                          					 access control lists

M

Set up TLS for the Skype for Business server

M

Set up
                                          					 TLS for the Lync server (required if you are using a Lync server)

M

Set up TLS
                                          					 for the OCS server

O

Deactivate
                                          					 non-essential services on the dedicated routing server (if applicable)

M

Task

O = Optional

M = Mandatory

Configure TLS Static Route to IM and Presence Service routing node

M

Configure Trusted Applications: Add IM and Presence Service as a trusted application and add IM and Presence cluster nodes
                                          to a trusted server pool

M

Publish the topology

M

Exchange Certificates

M

Task

O =
                                          					 Optional

M =
                                          					 Mandatory

Ensure
                                          					 that all required Lync domains are configured and verify that matching domains
                                          					 are configured on IM and Presence
                                             						Service nodes

M

Set up
                                          					 static routes to the IM and Presence
                                             						Service node

M

Set up
                                          					 host authorization

M

Publish
                                          					 the topology

M

Set up TLS

M

Task

O =
                                          					 Optional

M =
                                          					 Mandatory

Ensure
                                          					 that all required domains are configured on the OCS server and verify that
                                          					 matching domains are configured on the IM and Presence Service nodes

M

Enable
                                          					 SIP port

M

Set up
                                          					 static routes to IM and Presence
                                             						Service node

M

Set up
                                          					 host authorization

M

Set up
                                          					 TLS

O

Task

O =
                                          					 Optional

M =
                                          					 Mandatory

Download
                                          					 tools

M

Disable
                                          					 Lync subscriber notification pop-ups

M

Set
                                          					 unlimited contact list sizes and watcher sizes

M

Enable
                                          					 auto authorization of subscriber requests

M

Verify
                                          					 that the local IM and Presence
                                             						Service domains match the Microsoft server domains for the migrating
                                          					 users

M

If applicable, rename contact IDs in IM and Presence
                                             						Service contact lists for any Microsoft server SIP URIs formats that
                                          					 were modified

O

Provision Microsoft server users on Cisco Unified
                                             						Communications Manager

M

Back up
                                          					 user Microsoft server contact list information

M

Export
                                          					 contact lists for users

M

Disable
                                          					 users on Microsoft server

M

Verify
                                          					 that user accounts are disabled

M

Delete
                                          					 user data from database for migrating users

Depending on your Microsoft server deployment, you may have to
                                                      						perform this procedure on multiple databases.

M

Import
                                          					 contact lists for migrating users in to IM and Presence
                                             						Service

M

Reset
                                          					 maximum contact list and watcher size

M

Re-enable Lync subscriber notification pop-ups

M

## Availability

This section describes Availability functionality.

### Availability
                           	 Subscriptions and Policy

This section
                              		describes call flows for IM and Presence Service and Microsoft Lync or Microsoft
                                 		  Office Communicator .

#### Subscription to an
                              	 IM and Presence Service User

When a
                                    		  Microsoft Lync or Microsoft Office
                                       			 Communicator user wishes to view the availability of an IM and Presence Service client user, a SIP SUBSCRIBE
                                    		  request is routed from Skype for Business /Lync/OCS to IM and Presence
                                       			 Service . IM and Presence Service accepts the incoming
                                    		  subscription and places it in a pending state. Privacy policy is then applied
                                    		  to this incoming subscription request.

Privacy policy
                                                			 applied to subscriptions from Microsoft server users in a partitioned
                                                			 intradomain federation deployment is identical to the privacy policy applied to
                                                			 subscriptions from IM and Presence Service client users.

IM and Presence Service checks whether
                                    		  auto-authorization is enabled or whether the IM and Presence Service client user has previously
                                    		  blocked or allowed presence subscriptions from the Microsoft server user. If
                                    		  either case is true, IM and Presence Service auto-handles policy decision
                                    		  for the subscription request. Otherwise, the IM and Presence Service client user receives an alert
                                    		  regarding the new subscription.

If the
                                    		  subscription is denied, polite blocking is implemented. This means that the
                                    		  presence state of the user appears as offline to the Microsoft server user. If
                                    		  the subscription is authorized, IM and Presence
                                       			 Service sends availability updates to the Microsoft server user and
                                    		  the IM and Presence Service client user also has the
                                    		  option to add the Microsoft server user to their roster.

#### Subscription to
                              	 Microsoft Lync or Microsoft Office Communicator User

When an IM and Presence
                                       			 Service client user wishes to view the availability of a Microsoft
                                    		  Lync or Microsoft Office
                                       			 Communicator user, a SIP SUBSCRIBE request is routed from IM and Presence Service to Skype for Business /Lync/OCS .
                                    		  The Microsoft server accepts the incoming subscription. Policy is then applied
                                    		  to this incoming subscription request.

If the
                                    		  Microsoft server user has previously accepted a subscription from this IM and Presence Server user, the subscription is
                                    		  auto-accepted and availability is returned to the IM and Presence Service client user in line with the
                                    		  policy level applied by the Microsoft server user. If not, the Microsoft server
                                    		  user receives an alert regarding the new subscription. The Microsoft server
                                    		  user can then accept or block the IM and Presence Service client user.

The Microsoft
                                                			 server performs a refresh SIP SUBSCRIBE approximately every 1 hour and 45
                                                			 minutes. Therefore, if an IM and Presence Service node restarts, the maximum
                                                			 duration a Microsoft Lync or Microsoft Office
                                                   				Communicator user is without the availability status of the IM and Presence Service contacts is approximately two
                                                			 hours.

If the Microsoft
                                                			 server restarts, the maximum duration an IM and Presence Service client is without available
                                                			 status of Microsoft Lync or Microsoft Office
                                                   				Communicator contacts is approximately 2 hours.

#### Jabber for Windows Does not Display Lync/OCS Federated Contacts

A Jabber for Windows user will not see presence information for Lync/OCS federated contacts in their directory search results,
                                 until they have first added such Lync/OCS contacts to their contact list.

This is due to a protocol limitation between Jabber, which is XMPP-based, and Lync/OCS, which is SIP-based. When Jabber displays
                                 the results of a directory search it sends an XMPP Temporary Subscription request for each entry which is not already in its
                                 contact list. Because there is no equivalent SIP request, these requests are blocked when they reach the SIP Federation Gateway.

This behavior is expected, because if the XMPP Temporary Subscription request was converted to a SIP SUBSCRIBE request, then
                                 each Lync/OCS contact who appears in the directory search result would receive a popup message asking them to allow the Jabber
                                 user to see their presence information, as occurs when a Jabber user adds a contact. This solution would result in poor user
                                 experience.

### Availability Mapping
                           	 States

The
                                 		  following table shows the availability mapping states from Microsoft
                                    			 Lync or Microsoft Office
                                    			 Communicator to the following IM and Presence Service supported clients:

Cisco Jabber for
                                          				  Windows

Cisco
                                          				  Jabber for Mac

Cisco
                                          				  Jabber for iPad

Cisco Jabber IM
                                       				for Mobile (iPhone, Android, Blackberry)

Cisco
                                          				  Unified Personal Communicator Release 8.x

Third-party
                                       				XMPP clients

Microsoft Lync or Microsoft Office
                                                						Communicator

Setting

Cisco
                                                						Jabber 1

Setting

Cisco
                                                						Unified Personal Communicator

8.x
                                             					 Setting

Third-Party XMPP Clients

Setting

Available

Available

Available

Available

Away

Away

Away

Away

Be
                                             					 Right Back

Away

Away

Away

Busy

Busy

Busy

Busy

Do
                                             					 Not Disturb

Busy

Busy

Busy

Appear Offline

Offline

Offline

Offline

Offline

Offline

Offline

Offline

The
                                 		  following table shows the availability mapping states from all supported Cisco Jabber clients to Microsoft
                                    			 Lync or Microsoft Office
                                    			 Communicator .

Cisco
                                                						Unified Personal Communicator

Release
                                             					 8.x Setting

Microsoft Lync or Microsoft Office
                                                						Communicator

Setting

Available

Available

Busy

Busy

On
                                             					 the Phone

Busy

Meeting

Busy

Away

Away

Do
                                             					 Not Disturb

Busy

Offline

Offline

Offline—On the Phone

Offline

Offline—Meeting

Offline

Offline—Out of Office

Offline

The
                                 		  following table shows the availability mapping states from Cisco Jabber to Microsoft
                                    			 Lync or Microsoft Office
                                    			 Communicator .

Cisco Jabber 2

Setting

Microsoft Lync or Microsoft Office
                                                						Communicator

Setting

Available

Available

Away

Away

Do Not Disturb

Busy

Out of Office

Offline

Offline

Offline

The
                                 		  following table shows the availability mapping states from third-party XMPP
                                 		  clients to Microsoft
                                    			 Lync or Microsoft Office
                                    			 Communicator .

Third-Party XMPP

Setting

Microsoft Lync or Microsoft Office
                                                						Communicator

Setting

Available

Available

Away

Away

Extended Away

Away

Do Not Disturb

Busy

Offline

Offline

## Instant
                        	 Messaging

Partitioned intradomain federation supports point-to-point IM
                              		  between the IM and Presence
                                 			 Service client users and Microsoft Lync or Microsoft Office
                                 			 Communicator users. This includes support for the following IM
                              		  features:

Plain text IM
                                    				format

Typing
                                    				indication

Basic emoticons

SIP
                              		  Session Mode IM is used to transfer messages and typing indications between the IM and Presence Service and the Microsoft server.

When an IM and Presence Service client user sends an IM to a
                              		  Microsoft server user, if no existing IM session is established between these
                              		  two users, IM and Presence Service sends a SIP INVITE message to
                              		  the Microsoft server to establish a new session. This session is used for any
                              		  subsequent SIP MESSAGE or SIP INFO (typing indication) traffic from either of
                              		  these two users.

The IM and Presence Service client users and third-party
                                          			 XMPP client users can begin an IM conversation with a Microsoft server user
                                          			 even if they do not have availability.

When a
                              		  Microsoft user sends an IM to an IM and Presence Service client user, if no existing IM
                              		  session is established between these two users, the Microsoft server sends a
                              		  SIP INVITE message to the IM and Presence Service . This session is used for any
                              		  subsequent SIP MESSAGE or SIP INFO (typing indication) traffic from either of
                              		  these two users.

Due to the
                                          			 proprietary nature of Microsoft server group chat functionality, partitioned
                                          			 intradomain federation does not support group chat between the IM and Presence Service client users and Microsoft
                                             				Lync or Microsoft Office
                                             				Communicator users.

## Request
                        	 Routing

This section
                           		describes request routing for IM and Presence
                              		  Service to Skype for Business /Lync/OCS and for Skype for Business /Lync/OCS to IM and Presence Service .

### IM and Presence Service Request Routing

To allow the IM and Presence
                                 Service to send SIP requests to the Microsoft
                                 front-end server, configure static routes on the IM and Presence Service. For each IM and
                                 Presence Service domain, configure a TLS static route that points to the IP address of a Microsoft server
                                 of front-end load balancer (for Enterprise Edition MS servers
                                 only).

To allow the  IM and Presence Service-originated SIP requests to be received by the Microsoft server without an authentication
                                 requirement,  on the Microsoft server, add the IM and Presence Service as a trusted application. In addition, add the IM and
                                 Presence Service cluster nodes to a trusted servers pool.

#### Routing Modes

For routing SIP requests from IM and Presence Service to the Microsoft servers, partitioned intradomain federation provides
                                 two routing modes that you can configure in your IM and Presence Service setup:

Basic Routing

Advanced Routing

#### Basic Routing Mode
                              	 for Partitioned Intradomain Federation

Basic Routing is the
                                    		  default routing mode for partitioned intradomain federation. When Basic Routing
                                    		  is enabled, IM and Presence Service routes a request to Skype for Business /Lync/OCS if the request recipient is within any of the domains in the IM and Presence Service cluster but is not a licensed IM and Presence Service user.

The
                                    		  following figure shows the sequence of the routing request from IM and Presence Service to the Microsoft server when
                                    		  Basic Routing is configured. This figure shows an example of an OCS deployment,
                                    		  but it also applies to the other supported Microsoft servers.

1

Ann, a Cisco Jabber 8.x
                                                				  user, sends a request to Bob, who is a Microsoft Office
                                                   					 Communicator user in the same presence domain.

2

Because Bob is within the local presence domain but is not a
                                                				  licensed IM and Presence
                                                   					 Service client user, IM and Presence
                                                   					 Service translates the request and routes it to OCS.

3

The OCS server forwards the request to Bob’s Microsoft Office
                                                   					 Communicator client.

- For recipients who are not
                                                   				provisioned on either the IM and Presence
                                                      				  Service or a Microsoft server, any such request that is forwarded to
                                                   				the Microsoft server is in turn returned by the Microsoft server to IM and Presence
                                                      				  Service .

IM and Presence
                                                         					 Service has built-in loop detection to reject any requests that loop
                                                      				  back from the Microsoft server in this manner.

#### Advanced Routing
                              	 Mode for Partitioned Intradomain Federation

Advanced Routing
                                    		  ensures less traffic between IM and Presence Service and Skype for Business /Lync/OCS in deployments in which there are a large number of unprovisioned or unknown
                                    		  contacts in the IM and Presence Service database. However, Advanced
                                    		  Routing does add an additional storage overhead on each IM and Presence Service cluster because each cluster
                                    		  must store all Microsoft Lync or Microsoft Office
                                       			 Communicator users so that the Advanced Routing logic can be applied.

Configure Advanced Routing for partitioned intradomain
                                    		  federation only when you have a single-cluster IM and Presence Service deployment and Cisco Unified
                                       			 Communications Manager synchronizes its users from the same Active
                                    		  Directory that the Microsoft server uses. When more than one IM and Presence Service cluster is deployed, you must
                                    		  use the default basic routing method.

For Advanced
                                    		  Routing, the list of users synchronized from Active Directory must include all
                                    		  Microsoft Lync or Microsoft Office
                                       			 Communicator users.

When Advanced
                                    		  Routing is enabled, IM and Presence Service routes the request to the
                                    		  Microsoft server when both of the following conditions are met:

The request
                                          				recipient is within one of the IM and Presence
                                             				  Service domains but is not a licensed IM and Presence
                                             				  Service user

The request
                                          				recipient has a valid Microsoft Lync or Microsoft Office
                                             				  Communicator SIP address stored in the IM and Presence
                                             				  Service database.

### Microsoft Server Request Routing

To route SIP requests from the Microsoft server (Skype for Business/Lync/OCS) to the IM and Presence Service, configure TLS static routes on the Microsoft server for each IM and Presence Service domain:

For  chat-only deployments, point the static route to the designated IM and Presence Service routing node.

For  chat+calling deployments with Lync, point the static route to the Expressway Gateway

To allow Microsoft server SIP requests to be received without an authentication requirement,  on the IM and Presence Service,
                                 configure an access control list that includes the Microsoft server.

The Microsoft server has just a single routing mode in a partitioned intradomain federation deployment. The Microsoft server
                                 routes requests to either the  IM and Presence Service routing node (for chat-only deployments) or the Expressway Gateway
                                 (for chat+calling Lync deployments) if the request recipient is within one of the Microsoft server managed IM and availability
                                 domains, but is not a Microsoft Lync or Microsoft Office Communicator user.

#### Routing Examples

The
                                 		  following figure shows the sequence of the routing request from a Microsoft
                                 		  server to IM and Presence Service . This figure shows an example
                                 		  of an OCS deployment, but it also applies to chat-only deployments  with Lync.

1

Bob, a Microsoft Office
                                                   						  Communicator user, sends a request to Ann, who is a Cisco Jabber user.

3

IM and Presence
                                                   						  Service accepts the request and forwards it to Ann’s home IM and Presence
                                                   						  Service node.

2

Because Ann is within a
                                                						local presence domain but is not a Microsoft Office
                                                   						  Communicator user, the Microsoft server routes the request to IM and Presence
                                                   						  Service .

4

IM and Presence
                                                   						  Service translates the request and forwards it to Ann’s Cisco Jabber client.

For recipients who
                                             			 are not provisioned on either the IM and Presence
                                                				Service or the Microsoft server, any such requests that are forwarded
                                             			 by the Microsoft server to IM and Presence
                                                				Service are rejected by IM and Presence
                                                				Service .

## Intercluster and
                        	 Multinode Deployments

### Microsoft-originated Requests

When Skype for Business /Lync/OCS requests an Availability
                              subscription or IM conversation with IM and Presence Service, the Microsoft
                              server routes the SIP request to:

For chat-only deployments, the Microsoft server routes SIP
                                    requests to the IM and Presence Service routing node. The routing node
                                    forwards the SIP request to the cluster node that homes the recipient.
                                    The cluster node responds to the routing node, which then forwards
                                    the SIP response back to the Microsoft servers.

For chat+calling deployments, there is no routing node. Instead, the Microsoft server sends the
                                    SIP request to the Expressway Gateway. The Expressway Gateway
                                    forwards the SIP request to the IM and Presence Service cluster. The IM
                                    and Presence Service cluster node returns the SIP response directly to the
                                    Microsoft serversy.

### IM and PresenceService-originated Requests

When an IM and Presence cluster node
                              requests an Availability subscription or IM conversation with a
                              Microsoft Lync user, the cluster node sends the SIP request
                              directly to the Microsoft server. The Microsoft server returns the
                              SIP response directly to the IM and Presence Service cluster node that
                              initiated the message. For both chat-only and chat + calling
                              scenarios, any IM and Presence Service cluster node can send SIP requests
                              directly to the Microsoft server.

## Interdomain
                        	 Federation

IM and Presence
                                 			 Service supports interdomain federation. This feature is also
                              		  available when IM and Presence Service is configured for partitioned
                              		  intradomain federation. However, any interdomain federation that is configured
                              		  on IM and Presence Service is available only to IM and Presence Service client users.

If the Skype for Business /Lync/OCS deployment is already configured for SIP interdomain federation through an
                              		  Access Edge/Access Proxy server, Microsoft Lync or Microsoft Office
                                 			 Communicator users can continue to use this federation capability. It
                              		  is also possible to configure the IM and Presence Service and the Microsoft server so
                              		  that IM and Presence Service client users can take
                              		  advantage of such existing federation capability.

It is not
                                                				  supported to configure both the IM and Presence
                                                   					 Service and the Microsoft server to federate directly with the same
                                                				  remote domain.

See the
                                                				  document Interdomain Federation for IM
                                                      						and Presence Service on Cisco Unified Communications Manager for more
                                                				  information about interdomain federation.

## High Availability
                        	 for Intradomain Federation

Partitioned intradomain federation supports high availability
                              		  for request routing between IM and Presence
                                 			 Service and Skype for Business /Lync/OCS .

### High Availability
                           	 for IM and Presence Service to Microsoft Server Request Routing

As
                                 		  mentioned earlier, SIP static routes must be configured on IM and Presence Service to enable basic intradomain
                                 		  federation connectivity between IM and Presence Service and Skype for Business /Lync/OCS .

To provide
                                 		  high availability for integration with Microsoft servers, you can configure
                                 		  multiple SIP static routes for each address pattern on IM and Presence Service .

You can
                                 		  assign priority values to these static routes, as required, to define primary
                                 		  and backup static routes. Highest Priority routes are attempted first. If those
                                 		  routes are not available, the request is re-sent using the backup route as
                                 		  shown in the following figure. This figure shows an example of an OCS
                                 		  deployment, but it also applies to the other supported Microsoft servers.

1

When routing to a Microsoft server, IM and Presence
                                                   						  Service finds the highest-priority static route and attempts to send
                                                						the request to the next hop address that is configured for that route.

2

If that next hop is not available, IM and Presence
                                                   						  Service falls back to the next-highest priority static route and
                                                						attempts to send the request to the associated next hop address.

In the
                                 		  case of Enterprise Edition Microsoft servers, you can deploy a front-end load
                                 		  balancer. In such cases, you can configure SIP static routes on IM and Presence Service to point to the IP address of
                                 		  the Microsoft server's front-end load balancer. The front-end load balancer
                                 		  provides high availability within its associated Microsoft server pool as shown
                                 		  in the following figure. This figure shows an example of an OCS deployment, but
                                 		  it also applies to other Microsoft servers.

1

When routing to a Microsoft server, IM and Presence
                                                   						  Service finds a static route that points to the OCS front-end load
                                                						balancer.

2

The Microsoft server's front-end load balancer then routes
                                                						onward to one of the active front-end servers within the pool.

See the
                                 		  following URL for a list of approved load balancers: http://technet.microsoft.com/en-us/office/ocs/cc843611 .
                                 		  It is your responsibility to ensure that those load balancers are deployed and
                                 		  managed correctly.

Cisco does not
                                             			 support the configuration of static routes to point to load balancers. Cisco
                                             			 recommends that you configure static routes to bypass the front-end load
                                             			 balancer.

### High Availability
                           	 for Microsoft Server to IM and Presence Service Request Routing

SIP static
                                 		  routes must be configured on Skype for Business /Lync/OCS to enable basic intradomain federation connectivity between Microsoft server
                                 		  and IM and Presence Service .

However,
                                 		  Microsoft servers support configuration of only a single SIP static route for
                                 		  each domain, which means that the static route can point to just a single IM and
                                    			 Presence Service node.

Therefore,
                                 		  to achieve high availability when IM and Presence Service is integrated with a Microsoft
                                 		  server, you must incorporate a load balancer between the IM and Presence Service node and Microsoft server as
                                 		  shown in the following figure. This figure shows an example of an OCS
                                 		  deployment, but it also applies to the other Microsoft servers.

1

The load balancer works in Active/Backup mode. It routes
                                                						requests to the primary IM and Presence
                                                   						  Service node while that server is running and uses heartbeat
                                                						signaling to check if the IM and Presence
                                                   						  Service node is alive.

2

If the IM and Presence
                                                   						  Service fails, the load balancer ensures that all subsequent requests
                                                						are routed to the backup IM and Presence
                                                   						  Service node.

## Contact
                        	 Search

Partitioned intradomain federation allows for full search
                              		  capabilities on both IM and Presence Service -supported clients and Microsoft
                                 			 Lync or Microsoft Office
                                 			 Communicator .

Active
                              		  Directory (AD) searches by IM and Presence Service -supported clients return users
                              		  regardless of where they are provisioned. Microsoft server Address Book
                              		  searches continue to return all Microsoft server users and also any IM and Presence Service client users who have migrated
                              		  to IM and Presence Service .

Contact
                              		  Card information is available on both clients for all contacts.

If an IM and Presence Service client user was never
                                          			 provisioned on the Microsoft server, you must perform an Active Directory
                                          			 update to the msRTCSIP-PrimaryUserAddress field for such users to ensure that
                                          			 the user is available for the Microsoft server searches.

## User
                        	 Migration

At a high
                              		  level, the administrative flow for user migration is as follows:

Verify Skype for Business /Lync/OCS SIP URI format for migrating users.

If applicable,
                                    				rename contact IDs in IM and Presence
                                       				  Service contact lists.

License and
                                    				assign migrating Microsoft server users to 
                                    				the IM and Presence
                                       				  Service .

Back up
                                    				Microsoft server data for migrating Microsoft server users.

Export Microsoft
                                    				server contact lists for each of the migrating Microsoft server users.

Disable
                                    				Microsoft server user accounts for migrating Microsoft server users.

Delete Microsoft
                                    				server user data for migrating Microsoft server users.

Import Microsoft
                                    				server contact lists into the IM and Presence
                                       				  Service database for the migrated users.

Deploy 
                                    				an IM and Presence
                                       				  Service supported client on migrated users’ desktops.

To further aid the
                              		  migration process for administrators, a number of tools are available with this
                              		  feature.

IM
                                       				  and Presence Service client users and Microsoft Lync or Microsoft Office
                                       				  Communicator users share the same presence domain.

Users can
                                    				exchange Availability and Instant Messaging within that shared domain.

Users can search
                                    				for and add contacts regardless of where the user or contact is provisioned.

IM
                                       				  and Presence Service IM addresses can be set to match the Lync SIP
                                    				URI (msRTCSIP-PrimaryUserAddress) so that the user's identity is maintained
                                    				throughout the migration.

For more information about
                              		  configuring IM addresses and user migration, see Configuration and Administration of IM and Presence Service on
                                 				  Cisco Unified Communications Manager .

### IM Address Examples

The following table provides samples of the IM address options that are available for the IM and Presence Service .

IM and Presence Service Default Domain : cisco.com

User : John Smith

Userid : js12345

Mailid : jsmith@cisco-sales.com

SIPURI : john.smith@webex.com

IM Address Format

Directory URI Mapping

IM Address

<userid>@<domain>

n/a

js12345@cisco.com

Directory URI

mailid

jsmith@cisco-sales.com

Directory URI

msRTCSIP-PrimaryUserAddress

john.smith@webex.com

For more information about configuring IM addresses, see Configuration and Administration of IM and Presence Service on
                                    				  Cisco Unified Communications Manager .

### User Migration
                           	 Tools

IM and Presence
                                    			 Service provides tools for the following Skype for Business /Lync/OCS user migration steps:

Export Microsoft
                                       				server contact lists for each of the migrating Microsoft server users.

Disable
                                       				Microsoft server user accounts for migrating Microsoft server users.

Delete Microsoft
                                       				server user data for migrating Microsoft server users.

Import Microsoft
                                       				server contact lists into the IM and Presence
                                          				  Service database for the migrated users.

Rename the
                                       				contact IDs of migrated users in the IM and Presence
                                          				  Service database.

While
                                                   				  attempting to run any of the user migration tools you may receive the following
                                                   				  error: "Application failed to initialize properly". The reason for this error
                                                   				  is that you are attempting to run the user migration tools without the .NET 4.0
                                                   				  Framework installed. Each of the user migration tools that Cisco provides
                                                   				  requires that at least version 2.0 of the .NET Framework is installed on the
                                                   				  server where you are running the tool.

The .NET 2.0
                                                   				  Framework comes installed as standard on Windows Server 2003 R2 or newer.

The Export,
                                                   				  Disable and Delete tools are provided in a zip file on cisco.com. The Import
                                                   				  tool is accessible through the Cisco Unified CM IM and Presence Administration user
                                                   				  interface.

#### Export Microsoft
                                 		  Server Contact Lists for Each of the Migrating Microsoft Server Users

This IM and Presence Service tool allows for bulk export of
                                 		  contact lists from the Microsoft server. The exported contact lists are written
                                 		  to a comma-separated values (CSV) file that is acceptable to the IM and Presence Service Contact List Import Bulk
                                 		  Administration Tool (BAT). The combination of these tools allows for end-to-end
                                 		  administrative bulk contact list migration.

#### Disable
                                 		  Microsoft Server User Accounts for Migrating Microsoft Server Users

IM and Presence Service contains a tool to disable the
                                 		  Microsoft server user accounts in bulk. This tool disables Microsoft server
                                 		  accounts by connecting to Active Directory and modifying the user’s Microsoft
                                 		  server-specific attributes as required.

#### Delete Microsoft
                                 		  Server user Data for Migrating OCS Users

Microsoft
                                 		  server users must be deleted from the Microsoft servers to allow partitioned
                                 		  intradomain federation routing from the Microsoft server to IM and Presence Service . However, when users are
                                 		  deleted from the Microsoft servers, they are removed from the contact list of
                                 		  any Microsoft Lync or Microsoft Office
                                    			 Communicator users also. This IM and Presence Service tool deletes Microsoft server
                                 		  user data in bulk, while ensuring that the users are not removed from the
                                 		  contact list of Microsoft Lync or Microsoft Office
                                    			 Communicator users.

#### Import Microsoft
                                 		  Server Contact Lists into the IM and Presence Service Database for the Migrated
                                 		  Users

The IM and Presence Service BAT supports bulk contact list
                                 		  import. It takes a CSV file as input for this bulk import. When used in
                                 		  conjunction with the Microsoft server Export Contact List tool, it allows for
                                 		  contact list migration from a Microsoft server to IM and Presence Service .

#### Rename the
                                 		  Contact IDs of Migrated Users in the IM and Presence Service Database

The IM and Presence Service BAT supports migrations where
                                 		  the SIP URI formats on IM and Presence Service and the Microsoft server
                                 		  differ. In previous releases of IM and Presence Service , you must change the SIP URI
                                 		  of all the migrating Microsoft server users to match the IM and Presence Service SIP URI format before you
                                 		  migrate the first batch of users. With this release, you can change the SIP URI
                                 		  of migrating users just before you migrate each batch of users from the
                                 		  Microsoft server to IM and Presence Service . The Bulk Administration Tool
                                 		  takes a CSV file with the list of migrated users as input and updates the
                                 		  contact lists for all users that have the migrated users as contacts.

Running the user
                                             			 migration tools has no affect on the capabilities of other Microsoft server
                                             			 users who are signed into Microsoft Lync or Microsoft Office
                                                				Communicator . However, Cisco recommends that you run the user
                                             			 migration tools during a scheduled maintenance window to reduce the load on the
                                             			 Microsoft server and Active Directory system.

#### Migration Utilities for Microsoft Users

IM and Presence Service provides a single utility, the Migration Utilities for Microsoft Users, which you can use for the
                                 Lync/OCS migration steps mentioned in the User Migration Tools section. We recommend that you use this utility to perform
                                 these migration steps.

The Migration Utilities for Microsoft Users is available to download on cisco.com.

For further information see the Migration Utilities for Microsoft Users guide.

| Note | Partitioned
                                          			 intradomain federation requires that a user is enabled on one system only. This
                                          			 integration does not support a user that is enabled on both IM and Presence Service and the Microsoft server at
                                          			 the same time. |
|---|---|

| Note | The term
                                          			 Microsoft server is used in this document to refer to all supported Skype for Business, Lync and
                                          			 OCS platform types. Any information that is specific to a certain platform is
                                          			 identified. |
|---|---|

| Note | Presence domains
                                          		  must be identical. For example, user1@abc.synergy.com cannot share IM and
                                          		  Availability with any of the federated users configured for intradomain
                                          		  federation on synergy.com. Move user1 from the abc.synergy.com presence domain
                                          		  to the synergy.com domain to enable user1 to participate in Partitioned
                                          		  Intradomain Federation in this example. |
|---|---|

| Note | You can configure
                                          		  additional presence domains on the IM and Presence Service system even if no users are
                                          		  initially assigned to those domains. |
|---|---|

| Tip | See the
                                          			 detailed configuration workflows for the start-to-finish steps needed to enable
                                          			 partitioned intradomain federation and for links to the procedures that are
                                          			 performed at each step of the process. |
|---|---|

| Task | O =
                                          					 Optional M =
                                          					 Mandatory |
|---|---|
| Ensure
                                          					 that all required domains are configured on the IM and Presence
                                             						Service node and verify that matching domains are configured on the
                                          					 Microsoft servers | M |
| Enable
                                          					 partitioned intradomain federation | M |
| Set up
                                          					 static routes to the Microsoft server | M |
| Set up
                                          					 access control lists | M |
| Set up TLS for the Skype for Business server | M |
| Set up
                                          					 TLS for the Lync server (required if you are using a Lync server) | M |
| Set up TLS
                                          					 for the OCS server | O |
| Deactivate
                                          					 non-essential services on the dedicated routing server (if applicable) | M |

| Task | O = Optional M = Mandatory |
|---|---|
| Configure TLS Static Route to IM and Presence Service routing node | M |
| Configure Trusted Applications: Add IM and Presence Service as a trusted application and add IM and Presence cluster nodes
                                          to a trusted server pool | M |
| Publish the topology | M |
| Exchange Certificates | M |

| Task | O =
                                          					 Optional M =
                                          					 Mandatory |
|---|---|
| Ensure
                                          					 that all required Lync domains are configured and verify that matching domains
                                          					 are configured on IM and Presence
                                             						Service nodes | M |
| Set up
                                          					 static routes to the IM and Presence
                                             						Service node | M |
| Set up
                                          					 host authorization | M |
| Publish
                                          					 the topology | M |
| Set up TLS | M |

| Task | O =
                                          					 Optional M =
                                          					 Mandatory |
|---|---|
| Ensure
                                          					 that all required domains are configured on the OCS server and verify that
                                          					 matching domains are configured on the IM and Presence Service nodes | M |
| Enable
                                          					 SIP port | M |
| Set up
                                          					 static routes to IM and Presence
                                             						Service node | M |
| Set up
                                          					 host authorization | M |
| Set up
                                          					 TLS | O |

| Task | O =
                                          					 Optional M =
                                          					 Mandatory |
|---|---|
| Download
                                          					 tools | M |
| Disable
                                          					 Lync subscriber notification pop-ups | M |
| Set
                                          					 unlimited contact list sizes and watcher sizes | M |
| Enable
                                          					 auto authorization of subscriber requests | M |
| Verify
                                          					 that the local IM and Presence
                                             						Service domains match the Microsoft server domains for the migrating
                                          					 users | M |
| If applicable, rename contact IDs in IM and Presence
                                             						Service contact lists for any Microsoft server SIP URIs formats that
                                          					 were modified | O |
| Provision Microsoft server users on Cisco Unified
                                             						Communications Manager | M |
| Back up
                                          					 user Microsoft server contact list information | M |
| Export
                                          					 contact lists for users | M |
| Disable
                                          					 users on Microsoft server | M |
| Verify
                                          					 that user accounts are disabled | M |
| Delete
                                          					 user data from database for migrating users Note Depending on your Microsoft server deployment, you may have to
                                                      						perform this procedure on multiple databases. | Note | Depending on your Microsoft server deployment, you may have to
                                                      						perform this procedure on multiple databases. | M |
| Note | Depending on your Microsoft server deployment, you may have to
                                                      						perform this procedure on multiple databases. |
| Import
                                          					 contact lists for migrating users in to IM and Presence
                                             						Service | M |
| Reset
                                          					 maximum contact list and watcher size | M |
| Re-enable Lync subscriber notification pop-ups | M |

| Note | Depending on your Microsoft server deployment, you may have to
                                                      						perform this procedure on multiple databases. |
|---|---|

| Note | Privacy policy
                                                			 applied to subscriptions from Microsoft server users in a partitioned
                                                			 intradomain federation deployment is identical to the privacy policy applied to
                                                			 subscriptions from IM and Presence Service client users. |
|---|---|

| Note | The Microsoft
                                                			 server performs a refresh SIP SUBSCRIBE approximately every 1 hour and 45
                                                			 minutes. Therefore, if an IM and Presence Service node restarts, the maximum
                                                			 duration a Microsoft Lync or Microsoft Office
                                                   				Communicator user is without the availability status of the IM and Presence Service contacts is approximately two
                                                			 hours. If the Microsoft
                                                			 server restarts, the maximum duration an IM and Presence Service client is without available
                                                			 status of Microsoft Lync or Microsoft Office
                                                   				Communicator contacts is approximately 2 hours. |
|---|---|

| Microsoft Lync or Microsoft Office
                                                						Communicator Setting | Cisco
                                                						Jabber 1 Setting | Cisco
                                                						Unified Personal Communicator 8.x
                                             					 Setting | Third-Party XMPP Clients Setting |
|---|---|---|---|
| Available | Available | Available | Available |
| Away | Away | Away | Away |
| Be
                                             					 Right Back | Away | Away | Away |
| Busy | Busy | Busy | Busy |
| Do
                                             					 Not Disturb | Busy | Busy | Busy |
| Appear Offline | Offline | Offline | Offline |
| Offline | Offline | Offline | Offline |

| Cisco
                                                						Unified Personal Communicator Release
                                             					 8.x Setting | Microsoft Lync or Microsoft Office
                                                						Communicator Setting |
|---|---|
| Available | Available |
| Busy | Busy |
| On
                                             					 the Phone | Busy |
| Meeting | Busy |
| Away | Away |
| Do
                                             					 Not Disturb | Busy |
| Offline | Offline |
| Offline—On the Phone | Offline |
| Offline—Meeting | Offline |
| Offline—Out of Office | Offline |

| Cisco Jabber 2 Setting | Microsoft Lync or Microsoft Office
                                                						Communicator Setting |
|---|---|
| Available | Available |
| Away | Away |
| Do Not Disturb | Busy |
| Out of Office | Offline |
| Offline | Offline |

| Third-Party XMPP Setting | Microsoft Lync or Microsoft Office
                                                						Communicator Setting |
|---|---|
| Available | Available |
| Away | Away |
| Extended Away | Away |
| Do Not Disturb | Busy |
| Offline | Offline |

| Note | The IM and Presence Service client users and third-party
                                          			 XMPP client users can begin an IM conversation with a Microsoft server user
                                          			 even if they do not have availability. |
|---|---|

| Note | Due to the
                                          			 proprietary nature of Microsoft server group chat functionality, partitioned
                                          			 intradomain federation does not support group chat between the IM and Presence Service client users and Microsoft
                                             				Lync or Microsoft Office
                                             				Communicator users. |
|---|---|

| 1 | Ann, a Cisco Jabber 8.x
                                                				  user, sends a request to Bob, who is a Microsoft Office
                                                   					 Communicator user in the same presence domain. |
|---|---|
| 2 | Because Bob is within the local presence domain but is not a
                                                				  licensed IM and Presence
                                                   					 Service client user, IM and Presence
                                                   					 Service translates the request and routes it to OCS. |
| 3 | The OCS server forwards the request to Bob’s Microsoft Office
                                                   					 Communicator client. |

| Note | For recipients who are not
                                                   				provisioned on either the IM and Presence
                                                      				  Service or a Microsoft server, any such request that is forwarded to
                                                   				the Microsoft server is in turn returned by the Microsoft server to IM and Presence
                                                      				  Service . IM and Presence
                                                         					 Service has built-in loop detection to reject any requests that loop
                                                      				  back from the Microsoft server in this manner. |
|---|---|

| 1 | Bob, a Microsoft Office
                                                   						  Communicator user, sends a request to Ann, who is a Cisco Jabber user. | 3 | IM and Presence
                                                   						  Service accepts the request and forwards it to Ann’s home IM and Presence
                                                   						  Service node. |
|---|---|---|---|
| 2 | Because Ann is within a
                                                						local presence domain but is not a Microsoft Office
                                                   						  Communicator user, the Microsoft server routes the request to IM and Presence
                                                   						  Service . | 4 | IM and Presence
                                                   						  Service translates the request and forwards it to Ann’s Cisco Jabber client. |

| Note | For recipients who
                                             			 are not provisioned on either the IM and Presence
                                                				Service or the Microsoft server, any such requests that are forwarded
                                             			 by the Microsoft server to IM and Presence
                                                				Service are rejected by IM and Presence
                                                				Service . |
|---|---|

| Note | It is not
                                                				  supported to configure both the IM and Presence
                                                   					 Service and the Microsoft server to federate directly with the same
                                                				  remote domain. See the
                                                				  document Interdomain Federation for IM
                                                      						and Presence Service on Cisco Unified Communications Manager for more
                                                				  information about interdomain federation. |
|---|---|

| 1 | When routing to a Microsoft server, IM and Presence
                                                   						  Service finds the highest-priority static route and attempts to send
                                                						the request to the next hop address that is configured for that route. | 2 | If that next hop is not available, IM and Presence
                                                   						  Service falls back to the next-highest priority static route and
                                                						attempts to send the request to the associated next hop address. |
|---|---|---|---|

| 1 | When routing to a Microsoft server, IM and Presence
                                                   						  Service finds a static route that points to the OCS front-end load
                                                						balancer. | 2 | The Microsoft server's front-end load balancer then routes
                                                						onward to one of the active front-end servers within the pool. |
|---|---|---|---|

| Note | Cisco does not
                                             			 support the configuration of static routes to point to load balancers. Cisco
                                             			 recommends that you configure static routes to bypass the front-end load
                                             			 balancer. |
|---|---|

| 1 | The load balancer works in Active/Backup mode. It routes
                                                						requests to the primary IM and Presence
                                                   						  Service node while that server is running and uses heartbeat
                                                						signaling to check if the IM and Presence
                                                   						  Service node is alive. | 2 | If the IM and Presence
                                                   						  Service fails, the load balancer ensures that all subsequent requests
                                                						are routed to the backup IM and Presence
                                                   						  Service node. |
|---|---|---|---|

| Note | If an IM and Presence Service client user was never
                                          			 provisioned on the Microsoft server, you must perform an Active Directory
                                          			 update to the msRTCSIP-PrimaryUserAddress field for such users to ensure that
                                          			 the user is available for the Microsoft server searches. |
|---|---|

| IM and Presence Service Default Domain : cisco.com User : John Smith Userid : js12345 Mailid : jsmith@cisco-sales.com SIPURI : john.smith@webex.com |
|---|
| IM Address Format | Directory URI Mapping | IM Address |
| <userid>@<domain> | n/a | js12345@cisco.com |
| Directory URI | mailid | jsmith@cisco-sales.com |
| Directory URI | msRTCSIP-PrimaryUserAddress | john.smith@webex.com |

| Note | While
                                                   				  attempting to run any of the user migration tools you may receive the following
                                                   				  error: "Application failed to initialize properly". The reason for this error
                                                   				  is that you are attempting to run the user migration tools without the .NET 4.0
                                                   				  Framework installed. Each of the user migration tools that Cisco provides
                                                   				  requires that at least version 2.0 of the .NET Framework is installed on the
                                                   				  server where you are running the tool. The .NET 2.0
                                                   				  Framework comes installed as standard on Windows Server 2003 R2 or newer. The Export,
                                                   				  Disable and Delete tools are provided in a zip file on cisco.com. The Import
                                                   				  tool is accessible through the Cisco Unified CM IM and Presence Administration user
                                                   				  interface. |
|---|---|

| Note | This migration
                                          		  tool is only required when the IM Address format on IM and Presence Service differs from the Microsoft
                                          		  server. From IM and Presence Service Release 10.0, it is possible
                                          		  to configure IM and Presence Service to ensure there is no mismatch
                                          		  in IM Address formats between the two systems. |
|---|---|

| Note | Running the user
                                             			 migration tools has no affect on the capabilities of other Microsoft server
                                             			 users who are signed into Microsoft Lync or Microsoft Office
                                                				Communicator . However, Cisco recommends that you run the user
                                             			 migration tools during a scheduled maintenance window to reduce the load on the
                                             			 Microsoft server and Active Directory system. |
|---|---|