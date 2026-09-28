---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-intradomain-federation-12-5-1-cup0-b-partitioned-intradomai-a556326921
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/intradomain_federation/12_5_1/cup0_b_partitioned-intradomain-federation-1251/cup0_b_partitioned-intradomain-federation-1251_chapter_01001.html
retrieved_at: 2026-08-16T16:16:36.002464+00:00
---

Partitioned Intradomain Federation Guide for the IM and Presence Service

# Partitioned Intradomain Federation Guide for the IM and Presence Service

Updated: January 17, 2019

Chapter: Interdomain Federation and Intradomain Federation Deployment Integration

## Chapter: Interdomain Federation and Intradomain Federation Deployment Integration

# Interdomain Federation and Intradomain Federation Deployment Integration

## IM and Presence
                        	 Service Integration with Interdomain Federation Capability of Microsoft
                        	 Servers

You can
                              		  integrate IM and Presence Service with the interdomain
                              		  federation capability of Microsoft servers.

Microsoft
                              		  servers support interdomain federation with remote enterprises or public IM
                              		  providers. This interdomain federation capability is still available to Microsoft
                                 			 Lync or Microsoft Office
                                 			 Communicator users when partitioned intradomain federation is
                              		  configured between the Microsoft server and IM and Presence Service .

Furthermore, you can configure IM and Presence Service so that users who migrate to
                              		  an IM and Presence Service supported client can still use
                              		  the interdomain federation capability that is configured on the Microsoft
                              		  server.

For
                              		  information about configuring interdomain federation on IM and Presence Service , see Interdomain
                                 			 Federation for IM and Presence Service on Cisco Unified Communications
                                 			 Manager .

### Interactions and
                           	 Restrictions

- Do not use email for
                                    			 federation when you have an integrated interdomain and partitioned intradomain
                                    			 federation deployment. Email address for federation is not supported in
                                    			 deployments where partitioned intradomain federation is configured. Email
                                    			 address for federation is also not supported for interdomain federation if your
                                    			 deployment uses the interdomain federation capabilities of Skype for Business /Lync/OCS .
                                    			 Confirm that email address for federation is not enabled anywhere in the
                                    			 deployment in these deployment scenarios.

When
                                       				partitioned intradomain federation with the Microsoft server is enabled, it is
                                       				also possible to configure both SIP-based and XMPP-based interdomain federation
                                       				to remote domains on IM and Presence
                                          				  Service . However, this federation capability is available to users on IM and Presence
                                          				  Service supported clients only.

## IM and Presence
                        	 Service Integration with Interdomain Federation Capability of Microsoft
                        	 Servers

You can
                              		  integrate IM and Presence Service with the interdomain
                              		  federation capability of Microsoft servers.

Microsoft
                              		  servers support interdomain federation with remote enterprises or public IM
                              		  providers. This interdomain federation capability is still available to Microsoft
                                 			 Lync or Microsoft Office
                                 			 Communicator users when partitioned intradomain federation is
                              		  configured between the Microsoft server and IM and Presence Service .

Furthermore, you can configure IM and Presence Service so that users who migrate to
                              		  an IM and Presence Service supported client can still use
                              		  the interdomain federation capability that is configured on the Microsoft
                              		  server.

For
                              		  information about configuring interdomain federation on IM and Presence Service , see Interdomain
                                 			 Federation for IM and Presence Service on Cisco Unified Communications
                                 			 Manager .

## Remote Domain Setup
                        	 for Interdomain Federation through Intradomain Federation Connections on
                        	 Microsoft Servers

IM
                                 			 and Presence Service users can communicate with external domains
                              		  using either the existing Skype for Business /Lync/OCS interdomain federation connections or using connections to those external
                              		  domains that you configure directly on IM and Presence Service .

When you configure
                              		  interdomain federation through existing Microsoft server intradomain federation
                              		  connections, all requests to the remote domain are routed through the SIP
                              		  interface between IM and Presence Service and the Microsoft server. You
                              		  must configure the remote domain on IM and Presence Service to be a Microsoft server SIP
                              		  Federation domain before you proceed to configure interdomain federation
                              		  through existing intradomain federation connections. Do this for each remote
                              		  domain.

See
                              		  procedures related to adding a SIP federated domain in the Interdomain
                                 			 Federation for IM and Presence Service on Cisco Unified
                                 			 Communications Manager for detailed instructions on how to configure a
                              		  SIP federation domain.

Choose the following
                              		  options when you configure a SIP Federation domain for interdomain federation
                              		  using existing intradomain connections that are configured on Microsoft
                              		  servers:

For Domain Name,
                                    				enter the remote domain.

For Integration
                                    				Type, choose Inter-domain
                                       				  to OCS/Lync

Ensure that the Direct
                                       				  Federation check box is checked.

If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. These
                                          			 settings are cluster-wide; therefore you need to set them only on the IM
                                             				and Presence Service database publisher node within any given
                                          			 cluster.

### What To Do
                              		  Next

Configure a Static Route for a Remote Domain

## Configure a Static
                        	 Route for a Remote Domain

When you
                              		  integrate IM and Presence Service with Skype for Business /Lync/OCS interdomain federation capability, you must configure static routes on IM and
                                 			 Presence Service for each remote domain.

Caution

Email address for
                                          			 federation is not supported in deployments where partitioned intradomain
                                          			 federation is configured. Email address for federation is also not supported
                                          			 for interdomain federation if your deployment uses the interdomain federation
                                          			 capabilities of Microsoft servers. Confirm that email address for federation is
                                          			 not enabled anywhere in the deployment in these deployment scenarios.

For
                              		  Standard Edition Microsoft servers, the static routes must point to the IP
                              		  address of a specific Standard Edition server.

For
                              		  Enterprise Edition Microsoft servers, the static routes must point to a
                              		  specific Enterprise Edition front-end server.

If you are
                              		  using a Microsoft server's front-end load balancer, note the following:

- See the following URL for a
                                 			 list of load balancers: http://technet.microsoft.com/en-us/office/ocs/cc843611 .
                                 			 It is your responsibility to ensure that those load balancers are deployed and
                                 			 managed correctly. Cisco does not support the configuration of static routes to
                                 			 point to such load balancers.

- Cisco recommends that you
                                 			 configure static routes to bypass the front-end load balancer.

For High
                              		  Availability purposes, you can configure additional backup static routes for
                              		  each remote domain. The backup route has a lower priority and is used only if
                              		  the next hop address of the primary static route is unreachable.

If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. These
                                          			 settings are cluster-wide; therefore you need to set them only on the IM and Presence Service publisher node within any
                                          			 given cluster.

Step 1

Lin to the Cisco
                                          				Unified Communications Manager IM and Presence Administration user
                                       			 interface. Choose Presence > Routing > Static
                                             				  Routes .

Step 2

Click Add
                                          				New .

Step 3

Enter the
                                       			 destination pattern value so that the domain, or FQDN, is reversed. For
                                       			 example, if the domain is remote.com, the Destination Pattern value must be
                                       			 .com.remote

Step 4

Choose domain for the Route Type.

Step 5

In the Next Hop
                                       			 field, enter the IP address of the next hop.

Step 6

Set the Next Hop
                                       			 Port and the Protocol Type as follows:

For TLS
                                                					 Encryption:

Next Hop
                                                      						  Port number is 5061

Protocol
                                                      						  Type is TLS

For TCP:

Next Hop
                                                      						  Port number is 5060

Protocol
                                                      						  Type is TCP

Step 7

Enter the
                                       			 Priority value as follows:

For primary
                                                					 static routes, enter the default Priority value of 1 .

For backup
                                                					 static routes, enter a Priority value of greater than 1. (The lower the value,
                                                					 the higher the priority of the static route.)

Step 8

Leave the
                                       			 default values for all other parameters.

Step 9

Click Save .

## Remove IM and
                        	 Presence Service Integration with Microsoft Server Interdomain Federation
                        	 Capability

At some
                              		  stage, you may want to configure IM and Presence Service for interdomain federation
                              		  with one of the remote domains that you previously configured on Skype for Business /Lync/OCS .
                              		  The most likely scenario for this is when all Microsoft
                                 			 Lync or Microsoft Office
                                 			 Communicator users have been migrated to IM and Presence Service . At this point, the Microsoft
                              		  server deployment can be shut down, and any interdomain federation capability
                              		  can instead be enabled directly from IM and Presence Service .

To remove
                              		  an IM and Presence Service integration with Microsoft
                              		  server interdomain federation capability, you must complete Remove Static Route for Remote Domain and Remove the SIP Federation Domain .

### Remove Static Route
                           	 for Remote Domain

Step 1

Log in to the Cisco Unified IM and Presence
                                             				  Administration user interface. Choose Presence > Routing > Static
                                                				  Routes .

Step 2

Choose the
                                          			 appropriate static route from the list provided. If no list is shown, click Find .

Step 3

Click Delete Selected .

Step 4

Click OK to confirm the deletion.

#### What to do next

Remove the SIP Federation Domain

### Remove the SIP
                           	 Federation Domain

If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. These
                                             			 settings are cluster-wide; therefore you need to set them only on the IM and Presence Service database publisher node within
                                             			 any given cluster.

Step 1

Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Inter-Domain
                                                				  Federation > SIP Federation .

Step 2

Choose the
                                          			 domain from the list provided. If no list is shown, click Find .

Step 3

Click Delete
                                             				Selected .

Step 4

Click OK to confirm the deletion.

#### What to do next

After you
                                 		  remove the static route to the remote domain and remove the SIP federation
                                 		  domain, you can proceed to configure IM and Presence Service for interdomain federation
                                 		  with the remote domain. See Interdomain
                                    			 Federation for IM and Presence Service on Cisco Unified Communications Manager for more
                                 		  information.

| Note | If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. These
                                          			 settings are cluster-wide; therefore you need to set them only on the IM
                                             				and Presence Service database publisher node within any given
                                          			 cluster. |
|---|---|

| Caution | Email address for
                                          			 federation is not supported in deployments where partitioned intradomain
                                          			 federation is configured. Email address for federation is also not supported
                                          			 for interdomain federation if your deployment uses the interdomain federation
                                          			 capabilities of Microsoft servers. Confirm that email address for federation is
                                          			 not enabled anywhere in the deployment in these deployment scenarios. |
|---|---|

| Note | If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. These
                                          			 settings are cluster-wide; therefore you need to set them only on the IM and Presence Service publisher node within any
                                          			 given cluster. |
|---|---|

| Step 1 | Lin to the Cisco
                                          				Unified Communications Manager IM and Presence Administration user
                                       			 interface. Choose Presence > Routing > Static
                                             				  Routes . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Enter the
                                       			 destination pattern value so that the domain, or FQDN, is reversed. For
                                       			 example, if the domain is remote.com, the Destination Pattern value must be
                                       			 .com.remote |
| Step 4 | Choose domain for the Route Type. |
| Step 5 | In the Next Hop
                                       			 field, enter the IP address of the next hop. |
| Step 6 | Set the Next Hop
                                       			 Port and the Protocol Type as follows: For TLS
                                                					 Encryption: Next Hop
                                                      						  Port number is 5061 Protocol
                                                      						  Type is TLS For TCP: Next Hop
                                                      						  Port number is 5060 Protocol
                                                      						  Type is TCP |
| Step 7 | Enter the
                                       			 Priority value as follows: For primary
                                                					 static routes, enter the default Priority value of 1 . For backup
                                                					 static routes, enter a Priority value of greater than 1. (The lower the value,
                                                					 the higher the priority of the static route.) |
| Step 8 | Leave the
                                       			 default values for all other parameters. |
| Step 9 | Click Save . |

| Step 1 | Log in to the Cisco Unified IM and Presence
                                             				  Administration user interface. Choose Presence > Routing > Static
                                                				  Routes . |
|---|---|
| Step 2 | Choose the
                                          			 appropriate static route from the list provided. If no list is shown, click Find . |
| Step 3 | Click Delete Selected . |
| Step 4 | Click OK to confirm the deletion. |

| Note | If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. These
                                             			 settings are cluster-wide; therefore you need to set them only on the IM and Presence Service database publisher node within
                                             			 any given cluster. |
|---|---|

| Step 1 | Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Inter-Domain
                                                				  Federation > SIP Federation . |
|---|---|
| Step 2 | Choose the
                                          			 domain from the list provided. If no list is shown, click Find . |
| Step 3 | Click Delete
                                             				Selected . |
| Step 4 | Click OK to confirm the deletion. |