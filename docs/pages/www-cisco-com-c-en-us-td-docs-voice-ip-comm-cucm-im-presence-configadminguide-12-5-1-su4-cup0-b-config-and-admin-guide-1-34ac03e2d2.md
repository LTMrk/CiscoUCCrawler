---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su4-cup0-b-config-and-admin-guide-1-34ac03e2d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su4/cup0_b_config-and-admin-guide-1251su4/cup0_b_config-and-admin-guide-1251su3_chapter_01001.html
retrieved_at: 2026-08-16T16:45:15.466548+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: November 27, 2024

Chapter: Configure Advanced Routing

## Chapter: Configure Advanced Routing

# Configure Advanced Routing

## Advanced Routing Overview

Configure advanced routing to determine how the system establishes the following types of connections:

Intracluster   connections between IM and Presence Service nodes within a cluster.

Intercluster   connections between IM and Presence Service clusters that share the same presence domain.

SIP static routes for federation connections between different presence
                                 domains. Static routes are a fixed path and take precedence over dynamic routes.

### Intracluster and Intercluster Connections

There are two modes to establish intercluster and intracluster connections:

Multicast DNS (MDNS)—MDNS routing uses DNS records to set up the connections between the nodes. You can use MDNS routing when
                                    all nodes in the cluster are in the same multicast domain.

Router-to-router (the default option)—Router-to-router  uses IP address and user information to dynamically configure connections
                                    between the nodes. Use router-to-router connections when the nodes in the cluster are not in the same multicast domain, or
                                    when they are in different subnets.

## Advanced Routing Prerequisites

Before you configure your routing, make sure that your system meets these requirements. The requirement depends on which type
                              of routing method you want to use: MDNS routing or router-to-router:

### MDNS Routing Prerequisites

The following prerequisites exist:

You must have multicast DNS configured in the IOS network. When multicast DNS is disabled in the network, MDNS packets cannot
                                    reach the other nodes in a cluster. In some networks, multicast is enabled by default or enabled in a certain area of the
                                    network.  For example, it may be enabled in an area that contains the nodes that form the cluster. In these networks, you
                                    do not need to perform any additional configuration in your network to use MDNS routing. If multicast DNS is disabled in your
                                    network, you must perform a configuration change to your network equipment to use MDNS routing.

Make sure that all nodes are in the same multicast domain.

### Router-to-Router Prerequisites

If DNS is available in the network then you can use IP addresses, hostnames or FQDNs  as for your cluster node names. However,
                              if DNS is not available in your network, you must use IP addresses for node names.

If you need to reset your node names to use IP addresses, refer to the "Node Name Change" topics in the Changing the IP Address and Hostname for Cisco Unified Communications Manager and IM and Presence Service guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Advanced Routing Configuration Task Flow

Step 1

Configure the Routing Communication Method

The Routing Communication type determines the routing method the IM and Presence Service uses to establish router connections
                                          between cluster nodes. For single node IM and Presence Service deployments, we recommend that you leave the routing communication
                                          type at the default setting..

Step 2

Restart the Cisco XCP Router

If you edited the Routing Communication Type, you must restart the Cisco XCP Router.

Step 3

Configure Secure Router-to-Router Communications .

Optional. If you have Router-to-Router communication configured, you can configure  secure TLS connections between XMPP routers
                                          in the same cluster or different clusters.

You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                                      performance

Step 4

Configure the Cluster ID

If you use MDNS routing, confirm that the Cluster ID is shared by all nodes within the cluster and that the value is unique
                                          for each cluster. If required, you can use this procedure to update the Cluster ID.

Step 5

Configure Throttling Rate for Presence Updates

Optional. Configure the rate of availability (presence) changes sent to the Cisco XCP Router in messages per second. This
                                          setting helps to prevent an overload when the IM and Presence Service throttles the rate of availability (presence) changes
                                          to meet the configured value.

Step 6

Configure Static Routes

Complete these tasks if you want to configure static routes.

### Configure the Routing Communication Method

The Routing Communication type determines the routing method the IM and Presence Service uses to establish router connections
                                 between cluster nodes. For single node IM and Presence Service deployments, we recommend that you leave the routing communication
                                 type at the default setting.

Caution

You must configure the routing communication type before you complete your cluster configuration and start to accept user
                                             traffic into your IM and Presence Service deployment.

#### Before you begin

If you want to use MDNS routing, MDNS must be enabled throughout your IOS network.

Step 1

On the IM and Presence database publisher node, log in to Cisco Unified CM IM and Presence Administration.

Step 2

Choose System > Service Parameters .

Step 3

From the Server drop-down list box, select an IM and Presence Service node.

Step 4

From the Service drop-down list box, choose Cisco XCP Router

Step 5

Under XCP Router Global Settings (Clusterwide) , select a routing type  for the Routing Communication Type service parameter:

Multicast DNS (MDNS) —Choose this method if the nodes in your cluster are in the same multicast domain.

Router-to-Router (auto) —Choose this method if the nodes in your cluster are not in the same multicast domain. This is the default setting.

When you use  router-to-router connections, your deployment will incur additional performance overhead while IM and Presence Service establishes the XCP route fabric.

Step 6

Click Save .

#### What to do next

If you edited this setting, you must Restart the Cisco XCP Router

### Restart the Cisco XCP Router

If you edited the Routing Communication Type, restart the Cisco XCP Router service

#### Before you begin

Configure the Routing Communication Method

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server list, choose the node on which you want to reactivate services and click Go .

Step 3

In the IM and Presence Services area, select Cisco XCP Router .

Step 4

Click Restart .

#### What to do next

If you have Router-to-Router routing configured, Configure Secure Router-to-Router Communications .

If you have MDNS routing configured, Configure the Cluster ID .

### Configure Secure Router-to-Router Communications

If you have Router-to-Router communication configured, you can use this optional procedure to use secure TLS connections between XMPP routers in the same
                                 cluster or different clusters. The IM and Presence Service automatically replicates the XMPP certificate within the cluster,
                                 and across clusters, as an XMPP trust certificate.

You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                             performance.

Step 1

From Cisco Unified CM IM and Presence Administration, choose System > Security > Settings .

Step 2

Check the Enable XMPP Router-to-Router Secure Mode check box.

Step 3

Click Save .

#### What to do next

Configure Throttling Rate for Presence Updates

### Configure the Cluster ID

If you use MDNS routing, confirm that the Cluster ID is shared by all nodes within the cluster and that the value is unique for each cluster. If required, you can use this procedure
                                 to update the Cluster ID .

At installation, the system assigns a default
                                             unique Cluster ID to each IM and Presence Service cluster.
                                             Cisco recommends that
                                             you leave the default setting value, unless it's necessary to change it.

Step 1

On the IM and Presence Service database publisher node, log in to Cisco Unified CM IM and Presence Administration.

Step 2

Choose Presence > Settings > Standard Configuration .

Step 3

Check  the value in the Cluster ID field. If you need to edit the ID, enter the new value.

IM and Presence Service does not permit the underscore character (_) in the Cluster ID value. Ensure the Cluster ID value
                                             does not contain this character.

Step 4

Click Save .

#### What to do next

Configure Throttling Rate for Presence Updates

### Configure Throttling Rate for Presence Updates

Use this optional procedure to configure the rate of availability (presence) changes sent to the Cisco XCP Router in messages
                                 per second. This configuration may help to prevent an overload when the IM and Presence Service throttles the rate of availability
                                 (presence) changes back to meet the configured value.

Step 1

In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters .

Step 2

From the Server drop-down list box, choose the IM and Presence Service node.

Step 3

From the Service drop-down list box, choose Cisco Presence Engine .

Step 4

In the Clusterwide Parameters (Parameters that apply to all servers) section, edit the Presence Change Throttle Rate service parameter. The valid range is 10 – 100 with a default setting of 50.

Step 5

Click Save .

#### What to do next

If you want to configure a SIP static route for federation connections, Configure Static Routes .

### Configure Static Routes

Step 1

Configure SIP Proxy Server Settings

Configure your SIP Proxy Server settings. For WAN Deployments, Cisco recommends that you enable TCP method event routing
                                             on IM and Presence Service.

Step 2

Configure Route Embed Templates on IM and Presence Service

If your static route includes an embedded wildcard, you must configure a route embed template.

Step 3

Configure Static Routes on IM and Presence Service

Configure static route settings.

#### Configure SIP Proxy Server Settings

Step 1

In Cisco Unified CM IM and Presence Administration , choose Presence > Routing > Settings .

Step 2

Choose On for the Method/Event Routing Status. For WAN deployments, Cisco recommends that you configure TCP method event routing on
                                             IM and Presence Service.

Step 3

Choose Default SIP Proxy TCP Listener for the Preferred Proxy Server.

Step 4

Click Save .

#### Configure Route Embed Templates on IM and Presence Service

If your static route includes an embedded wildcard, you must configure a route embed template.

Step 1

In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters .

Step 2

From the Server drop-down, select an IM and Presence Service node.

Step 3

From the Service drop-down, select Cisco SIP Proxy .

Step 4

Under Routing Parameters (Clusterwide) , enter your template in the RouteEmbedTemplate field. You can define up to five templates. There is no limit to the number of static routes that you can define for a single
                                             route embed template.

Step 5

Click Save .

##### What to do next

Configure Static Routes on IM and Presence Service

##### Route Embed Templates

You must define a route embed template for any static route pattern that contains embedded wildcards. The route embed template
                                       contains information about the leading digits, the digit length, and location of the embedded wildcards. Before you define
                                       a route embed template, consider the sample templates we provide below.

When you define a route embed template, the characters that follow the “.” must match actual telephony digits in the static
                                       route. In the sample route embed templates below, we represent these characters with “x”.

Sample Route Embed Template A

Route embed template: 74..78xxxxx*

With this template, IM and Presence Service will enable this set of static routes with embedded wildcards:

Destination Pattern

Next Hop Destination

74..7812345*

1.2.3.4:5060

74..7867890*

5.6.7.8.9:5060

74..7811993*

10.10.11.37:5060

With this template, IM and Presence Service will not enable these static route entries:

73..7812345* (The initial string is not ‘74’ as the template defines)

74..781* (The destination pattern digit length does not match the template)

74…7812345* (The number of wildcards does not match the template)

Sample Route Embed Template B

Route embed template: 471….xx*

With this template, IM and Presence Service will enable this set of static routes with embedded wildcards:

Destination Pattern

Next Hop Destination

471….34*

20.20.21.22

471…55*

21.21.55.79

With this template, IM and Presence Service will not enable these static route entries:

47…344* (The initial string is not ‘471’ as the template defines)

471…4* (The string length does not match template)

471.450* (The number of wildcards does not match template)

#### Configure Static Routes on IM and Presence Service

Use this procedure to set up your static routes. For help with the fields and their settings, refer to the online help.

Step 1

In Cisco Unified CM IM and Presence Administration , choose Routing > Static Routes .

Step 2

Click Add New .

Step 3

in the Destination Pattern , enter the route pattern.

Step 4

In the Next Hop field, enter the IP Address, FQDN or hostname of the next hop server.

Step 5

In the Next Hop Port , enter the destination port on the Next Hop server. The default port is 5060.

Step 6

From the Route Type drop-down, select the type of route: User or Domain .

Step 7

From the Protocol Type drop-down list box, select the protocol for the static route: TCP , UDP , or TLS .

Step 8

Complete the remaining fields in the Static Route Configuration window.

Step 9

Click Save .

##### Static Route Parameters Settings

The following table lists the static route parameter settings that you can configure for IM and Presence Service.

Field

Description

Destination Pattern

This field specifies the pattern of the incoming number, up to a maximum of 255 characters.

The SIP proxy allows only 100 static routes to have an identical route pattern. If you exceed this limit, IM and Presence
                                                   Service logs an error.

Wildcard Usage

You can use “.” as a wildcard for a single character and “*” as a wildcard for multiple characters.

IM and Presence Service supports embedded '.' wildcard characters in static routes. However, you must define route embed templates
                                                   for static routes that contain embedded wildcards. Any static route that contains an embedded wildcard must match at least
                                                   one route embed template. See the route embed template topic (referenced in the Related Topics section below) for information
                                                   about defining route embed templates.

For phones:

A dot can exist at the end of the pattern, or embedded in a pattern. If you embed the dot in a pattern, you must create a
                                                         route embed template to match the pattern.

An asterisk can only exist at the end of the pattern.

For IP addresses and host names:

You can use an asterisk as part of the a host name.

The dot acts as a literal value in a host name.

An escaped asterisk sequence, \*, matches a literal * and can exist anywhere.

Description

Specifies the description of a particular static route, up to a maximum of 255 characters.

Next Hop

Specifies the domain name or IP address of the destination (next hop) and can be either a Fully Qualified Domain Name (FQDN)
                                                   or dotted IP address.

IM and Presence Service supports DNS SRV-based call routing. To specify DNS SRV as the next hop for a static route, set this
                                                   parameter to the DNS SRV name.

Next Hop Port

Specifies the port number of the destination (next hop). The default port is 5060.

IM and Presence Service supports DNS SRV-based call routing. To specify DNS SRV as the next hop for a static route, set the
                                                   next hop port parameter to 0.

Route Type

Specifies the route type: User or Domain. The default value is user.

For example, in the SIP URI “sip:19194762030@myhost.com” request, the user part is “19194762030”, and the host part is “myhost.com”.
                                                   If you choose User as the route type, IM and Presence Service uses the user-part value “19194762030” for routing SIP traffic.
                                                   If you choose the Domain as the route type, IM and Presence Service uses “myhost.com” for routing SIP traffic.

Protocol Type

Specifies the protocol type for this route, TCP, UDP, or TLS. The default value is TCP.

Priority

Specifies the route priority level. Lower values indicate higher priority. The default value is 1.

Value range: 1-65535

Weight

Specifies the route weight. Use this parameter only if two or more routes have the same priority. Higher values indicate which
                                                   route has the higher priority.

Value range: 1-65535

Example: Consider these three routes with associated priorities and weights:

1, 20

1, 10

2, 50

In this example, the static routes are listed in the correct order. The priority route is based on the lowest value priority,
                                                   that is 1. Given that two routes share the same priority, the weight parameter with the highest value decides the priority
                                                   route. In this example, IM and Presence Service directs SIP traffic to both routes configured with a priority value of 1,
                                                   and distributes the traffic according to weight; The route with a weight of 20 receives twice as much traffic as the route
                                                   with a weight of 10. Note that in this example, IM and Presence Service will only attempt to use the route with priority 2,
                                                   if it has tried both priority 1 routes and both failed.

Allow Less-Specific Route

Specifies that the route can be less specific. The default setting is On.

In Service

Specifies whether this route has been taken out of service. Specifies whether this route has been taken out of service.

Block Route Check Box

Check to block the static route. The default setting is Unblocked.

| Note | Cisco recommends MDNS routing because it can seamlessly support new XCP routers joining the XCP route fabric. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure the Routing Communication Method | The Routing Communication type determines the routing method the IM and Presence Service uses to establish router connections
                                          between cluster nodes. For single node IM and Presence Service deployments, we recommend that you leave the routing communication
                                          type at the default setting.. |
| Step 2 | Restart the Cisco XCP Router | If you edited the Routing Communication Type, you must restart the Cisco XCP Router. |
| Step 3 | Configure Secure Router-to-Router Communications . | Optional. If you have Router-to-Router communication configured, you can configure  secure TLS connections between XMPP routers
                                          in the same cluster or different clusters. Note You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                                      performance | Note | You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                                      performance |
| Note | You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                                      performance |
| Step 4 | Configure the Cluster ID | If you use MDNS routing, confirm that the Cluster ID is shared by all nodes within the cluster and that the value is unique
                                          for each cluster. If required, you can use this procedure to update the Cluster ID. |
| Step 5 | Configure Throttling Rate for Presence Updates | Optional. Configure the rate of availability (presence) changes sent to the Cisco XCP Router in messages per second. This
                                          setting helps to prevent an overload when the IM and Presence Service throttles the rate of availability (presence) changes
                                          to meet the configured value. |
| Step 6 | Configure Static Routes | Complete these tasks if you want to configure static routes. |

| Note | You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                                      performance |
|---|---|

| Caution | You must configure the routing communication type before you complete your cluster configuration and start to accept user
                                             traffic into your IM and Presence Service deployment. |
|---|---|

| Step 1 | On the IM and Presence database publisher node, log in to Cisco Unified CM IM and Presence Administration. |
|---|---|
| Step 2 | Choose System > Service Parameters . |
| Step 3 | From the Server drop-down list box, select an IM and Presence Service node. |
| Step 4 | From the Service drop-down list box, choose Cisco XCP Router |
| Step 5 | Under XCP Router Global Settings (Clusterwide) , select a routing type  for the Routing Communication Type service parameter: Multicast DNS (MDNS) —Choose this method if the nodes in your cluster are in the same multicast domain. Router-to-Router (auto) —Choose this method if the nodes in your cluster are not in the same multicast domain. This is the default setting. Note When you use  router-to-router connections, your deployment will incur additional performance overhead while IM and Presence Service establishes the XCP route fabric. | Note | When you use  router-to-router connections, your deployment will incur additional performance overhead while IM and Presence Service establishes the XCP route fabric. |
| Note | When you use  router-to-router connections, your deployment will incur additional performance overhead while IM and Presence Service establishes the XCP route fabric. |
| Step 6 | Click Save . |

| Note | When you use  router-to-router connections, your deployment will incur additional performance overhead while IM and Presence Service establishes the XCP route fabric. |
|---|---|

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server list, choose the node on which you want to reactivate services and click Go . |
| Step 3 | In the IM and Presence Services area, select Cisco XCP Router . |
| Step 4 | Click Restart . |

| Note | You should enable this option only if the IM and Presence Service runs over an unsecure network as this option may degrade
                                             performance. |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose System > Security > Settings . |
|---|---|
| Step 2 | Check the Enable XMPP Router-to-Router Secure Mode check box. |
| Step 3 | Click Save . |

| Note | At installation, the system assigns a default
                                             unique Cluster ID to each IM and Presence Service cluster.
                                             Cisco recommends that
                                             you leave the default setting value, unless it's necessary to change it. |
|---|---|

| Step 1 | On the IM and Presence Service database publisher node, log in to Cisco Unified CM IM and Presence Administration. |
|---|---|
| Step 2 | Choose Presence > Settings > Standard Configuration . |
| Step 3 | Check  the value in the Cluster ID field. If you need to edit the ID, enter the new value. IM and Presence Service does not permit the underscore character (_) in the Cluster ID value. Ensure the Cluster ID value
                                             does not contain this character. |
| Step 4 | Click Save . If you edited the Cluster ID , the new setting replicates to all cluster nodes. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list box, choose the IM and Presence Service node. |
| Step 3 | From the Service drop-down list box, choose Cisco Presence Engine . |
| Step 4 | In the Clusterwide Parameters (Parameters that apply to all servers) section, edit the Presence Change Throttle Rate service parameter. The valid range is 10 – 100 with a default setting of 50. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure SIP Proxy Server Settings | Configure your SIP Proxy Server settings. For WAN Deployments, Cisco recommends that you enable TCP method event routing
                                             on IM and Presence Service. |
| Step 2 | Configure Route Embed Templates on IM and Presence Service | If your static route includes an embedded wildcard, you must configure a route embed template. |
| Step 3 | Configure Static Routes on IM and Presence Service | Configure static route settings. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Presence > Routing > Settings . |
|---|---|
| Step 2 | Choose On for the Method/Event Routing Status. For WAN deployments, Cisco recommends that you configure TCP method event routing on
                                             IM and Presence Service. |
| Step 3 | Choose Default SIP Proxy TCP Listener for the Preferred Proxy Server. |
| Step 4 | Click Save . |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, select an IM and Presence Service node. |
| Step 3 | From the Service drop-down, select Cisco SIP Proxy . |
| Step 4 | Under Routing Parameters (Clusterwide) , enter your template in the RouteEmbedTemplate field. You can define up to five templates. There is no limit to the number of static routes that you can define for a single
                                             route embed template. |
| Step 5 | Click Save . |

| Destination Pattern | Next Hop Destination |
|---|---|
| 74..7812345* | 1.2.3.4:5060 |
| 74..7867890* | 5.6.7.8.9:5060 |
| 74..7811993* | 10.10.11.37:5060 |

| Destination Pattern | Next Hop Destination |
|---|---|
| 471….34* | 20.20.21.22 |
| 471…55* | 21.21.55.79 |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Routing > Static Routes . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | in the Destination Pattern , enter the route pattern. |
| Step 4 | In the Next Hop field, enter the IP Address, FQDN or hostname of the next hop server. |
| Step 5 | In the Next Hop Port , enter the destination port on the Next Hop server. The default port is 5060. |
| Step 6 | From the Route Type drop-down, select the type of route: User or Domain . |
| Step 7 | From the Protocol Type drop-down list box, select the protocol for the static route: TCP , UDP , or TLS . |
| Step 8 | Complete the remaining fields in the Static Route Configuration window. |
| Step 9 | Click Save . |

| Field | Description |
|---|---|
| Destination Pattern | This field specifies the pattern of the incoming number, up to a maximum of 255 characters. The SIP proxy allows only 100 static routes to have an identical route pattern. If you exceed this limit, IM and Presence
                                                   Service logs an error. Wildcard Usage You can use “.” as a wildcard for a single character and “*” as a wildcard for multiple characters. IM and Presence Service supports embedded '.' wildcard characters in static routes. However, you must define route embed templates
                                                   for static routes that contain embedded wildcards. Any static route that contains an embedded wildcard must match at least
                                                   one route embed template. See the route embed template topic (referenced in the Related Topics section below) for information
                                                   about defining route embed templates. For phones: A dot can exist at the end of the pattern, or embedded in a pattern. If you embed the dot in a pattern, you must create a
                                                         route embed template to match the pattern. An asterisk can only exist at the end of the pattern. For IP addresses and host names: You can use an asterisk as part of the a host name. The dot acts as a literal value in a host name. An escaped asterisk sequence, \*, matches a literal * and can exist anywhere. |
| Description | Specifies the description of a particular static route, up to a maximum of 255 characters. |
| Next Hop | Specifies the domain name or IP address of the destination (next hop) and can be either a Fully Qualified Domain Name (FQDN)
                                                   or dotted IP address. IM and Presence Service supports DNS SRV-based call routing. To specify DNS SRV as the next hop for a static route, set this
                                                   parameter to the DNS SRV name. |
| Next Hop Port | Specifies the port number of the destination (next hop). The default port is 5060. IM and Presence Service supports DNS SRV-based call routing. To specify DNS SRV as the next hop for a static route, set the
                                                   next hop port parameter to 0. |
| Route Type | Specifies the route type: User or Domain. The default value is user. For example, in the SIP URI “sip:19194762030@myhost.com” request, the user part is “19194762030”, and the host part is “myhost.com”.
                                                   If you choose User as the route type, IM and Presence Service uses the user-part value “19194762030” for routing SIP traffic.
                                                   If you choose the Domain as the route type, IM and Presence Service uses “myhost.com” for routing SIP traffic. |
| Protocol Type | Specifies the protocol type for this route, TCP, UDP, or TLS. The default value is TCP. |
| Priority | Specifies the route priority level. Lower values indicate higher priority. The default value is 1. Value range: 1-65535 |
| Weight | Specifies the route weight. Use this parameter only if two or more routes have the same priority. Higher values indicate which
                                                   route has the higher priority. Value range: 1-65535 Example: Consider these three routes with associated priorities and weights: 1, 20 1, 10 2, 50 In this example, the static routes are listed in the correct order. The priority route is based on the lowest value priority,
                                                   that is 1. Given that two routes share the same priority, the weight parameter with the highest value decides the priority
                                                   route. In this example, IM and Presence Service directs SIP traffic to both routes configured with a priority value of 1,
                                                   and distributes the traffic according to weight; The route with a weight of 20 receives twice as much traffic as the route
                                                   with a weight of 10. Note that in this example, IM and Presence Service will only attempt to use the route with priority 2,
                                                   if it has tried both priority 1 routes and both failed. |
| Allow Less-Specific Route | Specifies that the route can be less specific. The default setting is On. |
| In Service | Specifies whether this route has been taken out of service. Specifies whether this route has been taken out of service. |
| Block Route Check Box | Check to block the static route. The default setting is Unblocked. |