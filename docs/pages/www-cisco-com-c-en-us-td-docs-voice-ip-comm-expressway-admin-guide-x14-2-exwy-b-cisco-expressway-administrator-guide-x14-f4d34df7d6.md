---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x14-2-exwy-b-cisco-expressway-administrator-guide-x14-f4d34df7d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/exwy_b_cisco-expressway-administrator-guide-x142/exwy_m_bandwidth-control-x142.html
retrieved_at: 2026-08-16T22:38:41.516362+00:00
---

Cisco Expressway Administrator Guide (X14.2)

# Cisco Expressway Administrator Guide (X14.2)

Updated: August 11, 2022

Chapter: Bandwidth Control

## Chapter: Bandwidth Control

# Bandwidth Control

## About Bandwidth Control

The Expressway allows you to control the amount of bandwidth used by endpoints on your network. This is done by grouping endpoints
                              into subzones, and then using links and pipes to apply limits to the bandwidth that can be used:

Within each subzone

Between a subzone and another subzone

Between a subzone and a zone

Bandwidth limits may be set on a call-by-call basis and/or on a total concurrent usage basis. This flexibility allows you
                              to set appropriate bandwidth controls on individual components of your network.

Calls will fail if links are not configured correctly. You can check whether a call will succeed, and what bandwidth will
                              be allocated to it, using the command xCommand CheckBandwidth .

For specific information about how bandwidth is managed across peers in a cluster, see Sharing Bandwidth Across Peers .

### Example network deployment

The following diagram shows a typical network deployment:

A broadband LAN between the Enterprise and the internet, where high bandwidth calls are acceptable

A pipe to the internet (Pipe A) with restricted bandwidth

Two satellite offices, Branch and Home, each with their own internet connections and restricted pipes

In this example each pool of endpoints has been assigned to a different subzone, so that suitable limitations can be applied
                              to the bandwidth used within and between each subzone based on the amount of bandwidth they have available via their internet
                              connections.

## Configuring Bandwidth Controls

The Bandwidth configuration page ( Configuration > Bandwidth > Configuration ) is used to specify how the Expressway behaves in situations when it receives a call with no bandwidth specified, and when
                              it receives a call that requests more bandwidth than is currently available.

The configurable options are:

Field

Description

Usage tips

Default call bandwidth (kbps)

The bandwidth to use for calls for which no bandwidth value has been specified by the system that initiated the call.

It also defines the minimum bandwidth to use on SIP to H.323 interworked calls.

This value cannot be blank. The default value is 384kbps.

Usually, when a call is initiated the endpoint will include in the request the amount of bandwidth it wants to use.

Downspeed per call mode

Determines what happens if the per-call bandwidth restrictions on a subzone or pipe mean that there is insufficient bandwidth available to place a call at the requested
                                          rate.

On : The call will be downspeeded.

Off : The call will not be placed.

Downspeed total mode

Determines what happens if the total bandwidth restrictions on a subzone or pipe mean that there is insufficient bandwidth available to place a call at the requested
                                          rate.

On : The call will be downspeeded.

Off : The call will not be placed.

### About Downspeeding

If bandwidth control is in use, there may be situations when there is insufficient bandwidth available to place a call at
                              the requested rate. By default (and assuming that there is some bandwidth still available) the Expressway will still attempt
                              to connect the call, but at a reduced bandwidth – this is known as downspeeding .

Downspeeding can be configured so that it is applied in either or both of the following scenarios:

When the requested bandwidth for the call exceeds the lowest per-call limit for the subzone or pipes.

When placing the call at the requested bandwidth would mean that the total bandwidth limits for that subzone or pipes would
                                    be exceeded.

You can turn off downspeeding, in which case if there is insufficient bandwidth to place the call at the originally requested
                              rate, the call will not be placed at all. This could be used if, when your network is nearing capacity, you would rather a
                              call failed to connect at all than be connected at a lower than requested speed. In this situation endpoint users will get
                              one of the following messages, depending on the system that initiated the search:

"Exceeds Call Capacity"

"Gatekeeper Resources Unavailable"

## About Subzones

The Local Zone is made up of subzones. Subzones are used to control the bandwidth used by various parts of your network, and
                              to control the Expressway's registration, authentication and media encryption policies.

When an endpoint registers with the Expressway it is allocated to an appropriate subzone, determined by subzone membership rules based on endpoint IP address ranges or alias pattern matches.

You can create and configure subzones through the Subzones page ( Configuration > Local Zone > Subzones ).

The Expressway automatically creates the following special subzones, which you cannot delete:

The Default Subzone

The Traversal Subzone

The Cluster Subzone (only applies if the Expressway is in a cluster)

### Default links between subzones

The Expressway is shipped with the Default Subzone and Traversal Subzone (and Default Zone) already created, and with links
                              between them. If the Expressway is added to a cluster then default links to the Cluster Subzone are also established automatically.
                              You can delete or amend these default links if you need to model restrictions of your network.

### About the Traversal Subzone

The Traversal Subzone is a conceptual subzone. No endpoints can be registered to the Traversal Subzone; its sole purpose is
                              to control the bandwidth used by traversal calls.

The Traversal Subzone page ( Configuration > Local Zone > Traversal Subzone ) allows you to place bandwidth restrictions on calls being handled by the Traversal Subzone and to configure the range of
                              ports used for the media in traversal calls.

#### Configuring Bandwidth Limitations

All traversal calls pass through the Traversal Subzone, so by applying bandwidth limitations to the Traversal Subzone you
                                 can control how much processing of media the Expressway will perform at any one time. These limitations can be applied on
                                 a total concurrent usage basis, and on a per-call basis.

See Applying Bandwidth Limitations to Subzones for more details.

#### Configuring the Traversal Subzone Ports

On Configuration > Local Zone > Traversal Subzone you can configure the range of ports used for media in traversal calls.

##### What is a valid range to use?

You can define the media port range anywhere within the range 1024 to 65533. Traversal media port start must be an even number and Traversal media port end must be an odd number, because ports are allocated in pairs and the first port allocated in each pair is even.

##### How big should the range be?

Up to 48 ports could be required for a single traversal call, and you can have up to 75 concurrent traversal calls on a small
                                    system (M5-based), 100 on a medium system, or 500 on a large system. The default range is thus 48*500 = 24000 ports.

If you want to reduce the range, be aware that Expressway raises an alarm if the range is not big enough to meet the nominal
                                    maximum of 48 ports per call for the licensed number of rich media sessions. You may need to increase the range again if you
                                    add new licenses.

##### Why are 48 ports required for each call?

The nominal maximum number of ports allocated per call = max number of ports per allocation * max number of allocation instances.
                                    This is 8 * 6 = 48, and those numbers are derived as follows:

Each call can have up to 5 types of media; video (RTP/RTCP), audio (RTP/RTCP), second/duo video (RTP/RTCP), presentation (BFCP),
                                    and far end camera control (H.224). If all these media types are in the call, then the call requires 8 ports; 3 RTP/RTCP pairs,
                                    1 for BFCP, and 1 for H.224.

Each call has at least two legs (inbound to Expressway and outbound from Expressway), requiring two instances of port allocation.
                                    A further four instances of allocation are required if the call is routed via the B2BUA. In this case, ports are allocated
                                    at the following points:

Inbound to the local proxy from the source

Outbound from the local proxy to the local B2BUA

Inbound to the local B2BUA from the local proxy

Outbound from the local B2BUA to the local proxy

Inbound to the local proxy from the local B2BUA

Outbound from the local proxy to the destination

In practice, you probably won't reach the maximum number of concurrent traversal calls, have them all routed through the B2BUA,
                                    and have all the possible types of media in every call. However, we defined the default range to accommodate this extreme
                                    case, and the Expressway raises an alarm if the total port requirement could exceed the port range you specify.

##### What is the default range?

The default media traversal port range is 36000 to 59999, and is set on the Expressway-C at Configuration > Local Zones > Traversal Subzone . In Large Expressway systems the first 12 ports in the range – 36000 to 36011 by default – are always reserved for multiplexed
                                    traffic. The Expressway-E listens on these ports. You cannot configure a distinct range of demultiplex listening ports on
                                    Large systems: they always use the first 6 pairs in the media port range. On Small/Medium systems you can explicitly specify
                                    which 2 ports listen for multiplexed RTP/RTCP traffic, on the Expressway-E ( Configuration > Traversal > Ports ). If you choose not to configure a particular pair of ports ( Use configured demultiplexing ports = No ), then the Expressway-E will listen on the first pair of ports in the media traversal port range (36000 and 36001 by default).

Changes to the Use configured demultiplexing ports setting need a system restart to take effect.

### Configuring the Default Subzone

The Default Subzone page ( Configuration > Local Zone > Default Subzone ) is used to place bandwidth restrictions on calls involving endpoints in the Default Subzone, and to specify the Default
                                 Subzone's registration, authentication and media encryption policies.

When an endpoint registers with the Expressway, its IP address and alias is checked against the subzone membership rules and
                                 it is assigned to the appropriate subzone. If no subzones have been created, or the endpoint’s IP address or alias does not
                                 match any of the subzone membership rules, it is assigned to the Default Subzone (subject to the Default Subzone's Registration policy and Authentication policy ).

The use of a Default Subzone on its own (without any other manually created subzones) is suitable only if you have uniform
                                 bandwidth available between all your endpoints.

Your Local Zone contains two or more different networks with different bandwidth limitations, you should configure separate
                                             subzones for each different part of the network.

#### Default Subzone configuration options

The Default Subzone can be configured in the same manner as any other manually created subzone .

### Configuring Subzones

The Subzones page ( Configuration > Local Zone > Subzones ) lists all the subzones that have been configured on the Expressway, and allows you to create, edit and delete subzones.
                                 For each subzone, it shows how many membership rules it has, how many devices are currently registered to it, and the current
                                 number of calls and bandwidth in use. Up to 1000 subzones can be configured.

After configuring a subzone you should set up the Subzone membership rules which control which subzone an endpoint device is assigned to when it registers with the Expressway as opposed to defaulting
                                 to the Default Subzone .

The configurable options are:

Field / section

Description

Registration policy

When an endpoint registers with the Expressway, its IP address and alias is checked against the subzone membership rules and
                                             it is assigned to the appropriate subzone. If no subzones have been created, or the endpoint’s IP address or alias does not
                                             match any of the subzone membership rules, it is assigned to the Default Subzone.

In addition to using a registration restriction policy to control whether an endpoint can register with the Expressway, you can also configure a subzone's Registration policy as to whether it will accept registrations assigned to it via the subzone membership rules.

This provides additional flexibility when defining your registration policy. For example you can:

Deny registrations based on IP address subnet. You can do this by creating a subzone with associated membership rules based
                                                   on an IP address subnet range, and then setting that subzone to deny registrations.

Configure the Default Subzone to deny registrations. This would cause any registration requests that do not match any of the
                                                   subzone membership rules, and hence fall into the Default Subzone, to be denied.

Registration requests have to fulfill any registration restriction policy rules before any subzone membership and subzone
                                                         registration policy rules are applied.

Authentication policy

The Authentication policy setting controls how the Expressway challenges incoming messages to the Default Subzone. See Authentication policy for more information.

Media encryption mode

The Media encryption mode setting controls the media encryption capabilities for SIP calls flowing through the subzone. See Configuring Media Encryption Policy for more information.

If H.323 is enabled and the subzone has a media encryption mode of Force encrypted or Force unencrypted , any H.323 and SIP to H.323 interworked calls through this subzone will ignore this mode.

ICE support for media

Controls whether ICE messages are supported by the devices in this subzone.

Bandwidth controls

When configuring your subzones you can apply bandwidth limits to:

Individual calls between two endpoints within the subzone.

Individual calls between an endpoint within the subzone and another endpoint outside of the subzone.

The total of calls to or from endpoints within the subzone.

See Applying Bandwidth Limitations to Subzones for information about how bandwidth limits are set and managed.

### Configuring Subzone Membership Rules

The Subzone membership rules page ( Configuration > Local Zone > Subzone membership rules ) is used to configure the rules that determine, based on the address of the device, to which subzone an endpoint is assigned when it registers with the Expressway.

The page lists all the subzone membership rules that have been configured on the Expressway, and lets you create, edit, delete,
                                 enable and disable rules. Rule properties include:

Rule name and description

Priority

The subnet or alias pattern matching configuration

The subzone to which endpoints whose addresses satisfy this rule are assigned

If an endpoint’s IP address or registration alias does not match any of the membership rules, it is assigned to the Default Subzone .

Up to 3000 subzone membership rules can be configured.

The configurable options are:

Field

Description

Usage tips

Rule name

A descriptive name for the membership rule.

Description

An optional free-form description of the rule.

The description appears as a tooltip if you hover your mouse pointer over a rule in the list.

Priority

The order in which the rules are applied (and thus to which subzone the endpoint is assigned) if an endpoint's address satisfies
                                             multiple rules.

The rules with the highest priority (1, then 2, then 3 and so on) are applied first. If multiple Subnet rules have the same priority, the rule with the largest prefix length is applied first. Alias pattern match rules at the same priority are searched in configuration order.

Type

Determines how a device's address is checked:

Subnet : assigns the device if its IP address falls within the configured IP address subnet.

Alias pattern match : assigns the device if its alias matches the configured pattern.

Pattern matching is useful, for example, for home workers on dynamic IP addresses; rather than having to continually update
                                             the subnet to match what has been allocated, you can match against their alias instead.

Subnet address and Prefix length

These two fields together determine the range of IP addresses that will belong to this subzone.

The Address range field shows the range of IP addresses to be allocated to this subzone, based on the combination of the Subnet address and Prefix length .

Applies only if the Type is Subnet .

Pattern type

How the Pattern string must match the alias for the rule to be applied. Options are:

Exact : The entire string must exactly match the alias character for character.

Prefix : The string must appear at the beginning of the alias.

Suffix : The string must appear at the end of the alias.

Regex : Treats the string as a regular expression .

Applies only if the Type is Alias pattern match.

Pattern string

The pattern against which the alias is compared.

Applies only if the Type is Alias pattern match .

Target subzone

The subzone to which an endpoint is assigned if its address satisfies this rule.

State

Indicates if the rule is enabled or not.

Use this setting to test configuration changes, or to temporarily disable certain rules. Any disabled rules still appear in
                                             the rules list but are ignored.

### Applying Bandwidth Limitations to Subzones

You can apply bandwidth limits to the Default Subzone, Traversal Subzone and all manually configured subzones. The limits
                                 you can apply vary depending on the type of subzone, as follows:

Limitation

Description

Can be applied to

Total

Limits the total concurrent bandwidth being used by all endpoints in the subzone at any one time. In the case of the Traversal
                                             Subzone, this is the maximum bandwidth available for all concurrent traversal calls.

Default Subzone

Traversal Subzone

Manually configured subzones

Calls entirely within...

Limits the bandwidth of any individual call between two endpoints within the subzone.

Default Subzone

Manually configured subzones

Calls into or out of...

Limits the bandwidth of any individual call between an endpoint in the subzone, and an endpoint in another subzone or zone.

Default Subzone

Manually configured subzones

Calls handled by...

The maximum bandwidth available to any individual traversal call.

Traversal Subzone

For all the above limitations, the Bandwidth restriction setting has the following effect:

No bandwidth : No bandwidth is allocated and therefore no calls can be made.

Limited : Limits are applied. You must also enter a value in the corresponding bandwidth (kbps) field.

Unlimited : No restrictions are applied to the amount of bandwidth being used.

Use subzone bandwidth limits if you want to configure the bandwidth available between one specific subzone and all other subzones or zones.

Use pipes if you want to configure the bandwidth available between one specific subzone and another specific subzone or zone.

If your bandwidth configuration is such that multiple types of bandwidth restrictions are placed on a call (for example, if
                                 there are subzone bandwidth limits and pipe limits), the lowest limit will always apply to that call.

#### How different bandwidth limitations are managed

In situations where there are differing bandwidth limitations applied to the same link, the lower limit will always be the
                                 one used when routing the call and taking bandwidth limitations into account.

For example, Subzone A may have a per call inter bandwidth of 128. This means that any calls between Subzone A and any other
                                 subzone or zone will be limited to 128kbps. However, Subzone A also has a link configured between it and Subzone B. This link
                                 uses a pipe with a limit of 512kbps. In this situation, the lower limit of 128kbps will apply to calls between the two, regardless
                                 of the larger capacity of the pipe.

In the reverse situation, where Subzone A has a per call inter bandwidth limit of 512kbps and a link to Subzone B with a pipe
                                 of 128kbps, any calls between the two subzones will still be limited to 128kbps.

#### Bandwidth consumption of traversal calls

A non-traversal call between two endpoints within the same subzone would consume from that subzone the amount of bandwidth
                                 of that call.

A traversal call between two endpoints within the same subzone must, like all traversal calls, pass through the Traversal
                                 Subzone. This means that such calls consume an amount of bandwidth from the originating subzone’s total concurrent allocation
                                 that is equal to twice the bandwidth of the call – once for the call from the subzone to the Traversal Subzone, and again
                                 for the call from the Traversal Subzone back to the originating subzone. In addition, as this call passes through the Traversal
                                 Subzone, it will consume an amount of bandwidth from the Traversal Subzone equal to that of the call.

## Links and Pipes

### Configuring Links

Links connect local subzones with other subzones and zones. For a call to take place, the endpoints involved must each reside
                                 in subzones or zones that have a link between them. The link does not need to be direct; the two endpoints may be linked via
                                 one or more intermediary subzones.

Links are used to calculate how a call is routed over the network and therefore which zones and subzones are involved and
                                 how much bandwidth is available. If multiple routes are possible, your Expressway will perform the bandwidth calculations
                                 using the one with the fewest links.

The Links page ( Configuration > Bandwidth > Links ) lists all existing links and allows you to create, edit and delete links.

The following information is displayed:

Field

Description

Name

The name of the link. Automatically created links have names based on the nodes that the link is between.

Node 1 and Node 2

The Traversal Subzone and the zone that the link is between.

The two subzones, or one subzone and one zone, that the link is between.

Pipe 1 and Pipe 2

Any pipes that have been used to apply bandwidth limitations to the link. See Applying Pipes to Links for more information.

In order to apply a pipe, you must first have created it via the Pipes page.

Calls

Shows the total number of calls currently traversing the link.

Bandwidth used

Shows the total amount of bandwidth currently being consumed by all calls traversing the link.

You can configure up to 3000 links. Some links are created automatically when a subzone or zone is created.

### Default Links

If a subzone has no links configured, then endpoints within the subzone are only able to call other endpoints within the same
                                 subzone. For this reason, the Expressway comes shipped with a set of pre-configured links and will also automatically create
                                 new links each time you create a new subzone.

#### Pre-configured links

The Expressway is shipped with the Default Subzone, Traversal Subzone and Default Zone already created, and with default links
                                 pre-configured between them as follows: DefaultSZtoTraversalSZ , DefaultSZtoDefaultZ and TraversalSZtoDefaultZ . If the Expressway is in a cluster, an additional link, DefaultSZtoClusterSZ , between the Default Subzone and the Cluster Subzone is also established.

You can edit any of these default links in the same way you would edit manually configured links. If any of these links have
                                 been deleted you can re-create them, either:

Manually through the web interface

Automatically by using the CLI command xCommand DefaultLinksAdd

#### Automatically created links

Whenever a new subzone or zone is created, links are automatically created as follows:

New zone/subzone type

Default links are created to...

Subzone

Default Subzone and Traversal Subzone

Neighbor zone

Default Subzone and Traversal Subzone

DNS zone

Default Subzone and Traversal Subzone

ENUM zone

Default Subzone and Traversal Subzone

Traversal client zone

Traversal Subzone

Traversal server zone

Traversal Subzone

Along with the pre-configured default links this ensures that, by default, any new subzone or zone has connectivity to all
                                 other subzones and zones. You may rename, delete and amend any of these default links.

Calls will fail if links are not configured correctly. You can check whether a call will succeed, and what bandwidth will
                                             be allocated to it, using the CLI command xCommand CheckBandwidth .

### Configuring Pipes

Pipes are used to control the amount of bandwidth used on calls between specific subzones and zones. The limits can be applied
                                 to the total concurrent bandwidth used at any one time, or to the bandwidth used by any individual call.

To apply these limits, you must first create a pipe and configure it with the required bandwidth limitations. Then when configuring
                                 links you assign the pipe to one or more links. Calls using the link will then have the pipe’s bandwidth limitations applied
                                 to them. See Applying Pipes to Links for more information.

The Pipes page ( Configuration > Bandwidth > Pipes ) lists all the pipes that have been configured on the Expressway and allows you to create, edit and delete pipes.

The following information is displayed:

Field

Description

Name

The name of the pipe.

Total bandwidth

The upper limit on the total bandwidth used at any one time by all calls on all links to which this pipe is applied.

Per call bandwidth

The maximum bandwidth of any one call on the links to which this pipe is applied.

Calls

Shows the total number of calls currently traversing all links to which the pipe is applied.

Bandwidth used

Shows the total amount of bandwidth currently being consumed by all calls traversing all links to which the pipe is applied.

You can configure up to 1000 pipes.

See Applying Bandwidth Limitations to Subzones for more information about how the bandwidth limits are set and managed.

### Applying Pipes to Links

Pipes are used to restrict the bandwidth of a link. When a pipe is applied to a link, it restricts the bandwidth of calls
                                 made between the two nodes of the link - the restrictions apply to calls in either direction. Normally a single pipe would
                                 be applied to a single link. However, one or more pipes may be applied to one or more links, depending on how you want to
                                 model your network.

#### One pipe, one link

Applying a single pipe to a single link is useful when you want to apply specific limits to calls between a subzone and another
                                 specific subzone or zone.

#### One pipe, two or more links

Each pipe may be applied to multiple links. This is used to model the situation where one site communicates with several other
                                 sites over the same broadband connection to the Internet. A pipe should be configured to represent the broadband connection,
                                 and then applied to all the links. This allows you to configure the bandwidth options for calls in and out of that site.

In the diagram below, Pipe A has been applied to two links: the link between the Default Subzone and the Home Office subzone,
                                 and the link between the Default Subzone and the Branch Office subzone. In this case, Pipe A represents the Head Office’s
                                 broadband connection to the internet, and would have total and per-call restrictions placed on it.

#### Two pipes, one link

Each link may have up to two pipes associated with it. This is used to model the situation where the two nodes of a link are
                                 not directly connected, for example two sites that each have their own broadband connection to the Internet. Each connection
                                 should have its own pipe, meaning that a link between the two nodes should be subject to the bandwidth restrictions of both
                                 pipes.

In the diagram below, the link between the Default Subzone and the Home Office Subzone has two pipes associated with it: Pipe
                                 A, which represents the Head Office’s broadband connection to the internet, and Pipe B, which represents the Home Office’s
                                 dial-up connection to the internet. Each pipe would have bandwidth restrictions placed on it to represent its maximum capacity,
                                 and a call placed via this link would have the lower of the two bandwidth restrictions applied.

## Bandwidth Control Examples

### Without a Firewall

In the example below, there are three geographically separate offices: Head, Branch and Home. All endpoints in the Head Office
                                 register with the Expressway-C, as do those in the Branch and Home offices.

Each of the three offices is represented as a separate subzone on the Expressway, with bandwidth configured according to local
                                 policy.

The enterprise’s leased line connection to the Internet, and the DSL connections to the remote offices are modeled as separate
                                 pipes.

There are no firewalls involved in this scenario, so direct links can be configured between each of the offices. Each link
                                 is then assigned two pipes, representing the Internet connections of the offices at each end of the link.

In this scenario, a call placed between the Home Office and Branch Office will consume bandwidth from the Home and Branch
                                 subzones and on the Home and Branch pipes (Pipe B and Pipe C). The Head Office’s bandwidth budget will be unaffected by the
                                 call.

| Field | Description | Usage tips |
|---|---|---|
| Default call bandwidth (kbps) | The bandwidth to use for calls for which no bandwidth value has been specified by the system that initiated the call. It also defines the minimum bandwidth to use on SIP to H.323 interworked calls. This value cannot be blank. The default value is 384kbps. | Usually, when a call is initiated the endpoint will include in the request the amount of bandwidth it wants to use. |
| Downspeed per call mode | Determines what happens if the per-call bandwidth restrictions on a subzone or pipe mean that there is insufficient bandwidth available to place a call at the requested
                                          rate. On : The call will be downspeeded. Off : The call will not be placed. |  |
| Downspeed total mode | Determines what happens if the total bandwidth restrictions on a subzone or pipe mean that there is insufficient bandwidth available to place a call at the requested
                                          rate. On : The call will be downspeeded. Off : The call will not be placed. |  |

| Note | Changes to the Use configured demultiplexing ports setting need a system restart to take effect. |
|---|---|

| Note | Your Local Zone contains two or more different networks with different bandwidth limitations, you should configure separate
                                             subzones for each different part of the network. |
|---|---|

| Field / section | Description |
|---|---|
| Registration policy | When an endpoint registers with the Expressway, its IP address and alias is checked against the subzone membership rules and
                                             it is assigned to the appropriate subzone. If no subzones have been created, or the endpoint’s IP address or alias does not
                                             match any of the subzone membership rules, it is assigned to the Default Subzone. In addition to using a registration restriction policy to control whether an endpoint can register with the Expressway, you can also configure a subzone's Registration policy as to whether it will accept registrations assigned to it via the subzone membership rules. This provides additional flexibility when defining your registration policy. For example you can: Deny registrations based on IP address subnet. You can do this by creating a subzone with associated membership rules based
                                                   on an IP address subnet range, and then setting that subzone to deny registrations. Configure the Default Subzone to deny registrations. This would cause any registration requests that do not match any of the
                                                   subzone membership rules, and hence fall into the Default Subzone, to be denied. Note Registration requests have to fulfill any registration restriction policy rules before any subzone membership and subzone
                                                         registration policy rules are applied. | Note | Registration requests have to fulfill any registration restriction policy rules before any subzone membership and subzone
                                                         registration policy rules are applied. |
| Note | Registration requests have to fulfill any registration restriction policy rules before any subzone membership and subzone
                                                         registration policy rules are applied. |
| Authentication policy | The Authentication policy setting controls how the Expressway challenges incoming messages to the Default Subzone. See Authentication policy for more information. |
| Media encryption mode | The Media encryption mode setting controls the media encryption capabilities for SIP calls flowing through the subzone. See Configuring Media Encryption Policy for more information. Note If H.323 is enabled and the subzone has a media encryption mode of Force encrypted or Force unencrypted , any H.323 and SIP to H.323 interworked calls through this subzone will ignore this mode. | Note | If H.323 is enabled and the subzone has a media encryption mode of Force encrypted or Force unencrypted , any H.323 and SIP to H.323 interworked calls through this subzone will ignore this mode. |
| Note | If H.323 is enabled and the subzone has a media encryption mode of Force encrypted or Force unencrypted , any H.323 and SIP to H.323 interworked calls through this subzone will ignore this mode. |
| ICE support for media | Controls whether ICE messages are supported by the devices in this subzone. |
| Bandwidth controls | When configuring your subzones you can apply bandwidth limits to: Individual calls between two endpoints within the subzone. Individual calls between an endpoint within the subzone and another endpoint outside of the subzone. The total of calls to or from endpoints within the subzone. See Applying Bandwidth Limitations to Subzones for information about how bandwidth limits are set and managed. |

| Note | Registration requests have to fulfill any registration restriction policy rules before any subzone membership and subzone
                                                         registration policy rules are applied. |
|---|---|

| Note | If H.323 is enabled and the subzone has a media encryption mode of Force encrypted or Force unencrypted , any H.323 and SIP to H.323 interworked calls through this subzone will ignore this mode. |
|---|---|

| Note | If an endpoint’s IP address or registration alias does not match any of the membership rules, it is assigned to the Default Subzone . |
|---|---|

| Field | Description | Usage tips |
|---|---|---|
| Rule name | A descriptive name for the membership rule. |  |
| Description | An optional free-form description of the rule. | The description appears as a tooltip if you hover your mouse pointer over a rule in the list. |
| Priority | The order in which the rules are applied (and thus to which subzone the endpoint is assigned) if an endpoint's address satisfies
                                             multiple rules. | The rules with the highest priority (1, then 2, then 3 and so on) are applied first. If multiple Subnet rules have the same priority, the rule with the largest prefix length is applied first. Alias pattern match rules at the same priority are searched in configuration order. |
| Type | Determines how a device's address is checked: Subnet : assigns the device if its IP address falls within the configured IP address subnet. Alias pattern match : assigns the device if its alias matches the configured pattern. | Pattern matching is useful, for example, for home workers on dynamic IP addresses; rather than having to continually update
                                             the subnet to match what has been allocated, you can match against their alias instead. |
| Subnet address and Prefix length | These two fields together determine the range of IP addresses that will belong to this subzone. The Address range field shows the range of IP addresses to be allocated to this subzone, based on the combination of the Subnet address and Prefix length . | Applies only if the Type is Subnet . |
| Pattern type | How the Pattern string must match the alias for the rule to be applied. Options are: Exact : The entire string must exactly match the alias character for character. Prefix : The string must appear at the beginning of the alias. Suffix : The string must appear at the end of the alias. Regex : Treats the string as a regular expression . | Applies only if the Type is Alias pattern match. |
| Pattern string | The pattern against which the alias is compared. | Applies only if the Type is Alias pattern match . |
| Target subzone | The subzone to which an endpoint is assigned if its address satisfies this rule. |  |
| State | Indicates if the rule is enabled or not. | Use this setting to test configuration changes, or to temporarily disable certain rules. Any disabled rules still appear in
                                             the rules list but are ignored. |

| Limitation | Description | Can be applied to |
|---|---|---|
| Total | Limits the total concurrent bandwidth being used by all endpoints in the subzone at any one time. In the case of the Traversal
                                             Subzone, this is the maximum bandwidth available for all concurrent traversal calls. | Default Subzone Traversal Subzone Manually configured subzones |
| Calls entirely within... | Limits the bandwidth of any individual call between two endpoints within the subzone. | Default Subzone Manually configured subzones |
| Calls into or out of... | Limits the bandwidth of any individual call between an endpoint in the subzone, and an endpoint in another subzone or zone. | Default Subzone Manually configured subzones |
| Calls handled by... | The maximum bandwidth available to any individual traversal call. | Traversal Subzone |

| Field | Description |
|---|---|
| Name | The name of the link. Automatically created links have names based on the nodes that the link is between. |
| Node 1 and Node 2 | The Traversal Subzone and the zone that the link is between. The two subzones, or one subzone and one zone, that the link is between. |
| Pipe 1 and Pipe 2 | Any pipes that have been used to apply bandwidth limitations to the link. See Applying Pipes to Links for more information. Note In order to apply a pipe, you must first have created it via the Pipes page. | Note | In order to apply a pipe, you must first have created it via the Pipes page. |
| Note | In order to apply a pipe, you must first have created it via the Pipes page. |
| Calls | Shows the total number of calls currently traversing the link. |
| Bandwidth used | Shows the total amount of bandwidth currently being consumed by all calls traversing the link. |

| Note | In order to apply a pipe, you must first have created it via the Pipes page. |
|---|---|

| New zone/subzone type | Default links are created to... |
|---|---|
| Subzone | Default Subzone and Traversal Subzone |
| Neighbor zone | Default Subzone and Traversal Subzone |
| DNS zone | Default Subzone and Traversal Subzone |
| ENUM zone | Default Subzone and Traversal Subzone |
| Traversal client zone | Traversal Subzone |
| Traversal server zone | Traversal Subzone |

| Note | Calls will fail if links are not configured correctly. You can check whether a call will succeed, and what bandwidth will
                                             be allocated to it, using the CLI command xCommand CheckBandwidth . |
|---|---|

| Field | Description |
|---|---|
| Name | The name of the pipe. |
| Total bandwidth | The upper limit on the total bandwidth used at any one time by all calls on all links to which this pipe is applied. |
| Per call bandwidth | The maximum bandwidth of any one call on the links to which this pipe is applied. |
| Calls | Shows the total number of calls currently traversing all links to which the pipe is applied. |
| Bandwidth used | Shows the total amount of bandwidth currently being consumed by all calls traversing all links to which the pipe is applied. |