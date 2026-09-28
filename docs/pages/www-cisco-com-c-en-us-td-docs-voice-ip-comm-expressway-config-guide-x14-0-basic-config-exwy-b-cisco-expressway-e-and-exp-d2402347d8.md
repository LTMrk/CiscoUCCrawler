---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-d2402347d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_routing-configuration.html
retrieved_at: 2026-08-16T15:27:41.353067+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Routing Configuration

## Chapter: Routing Configuration

# Routing Configuration

## Pre-search Transforms

Pre-search transform configuration allows the destination alias (called address) in an incoming search request to be modified.
                           The Expressway applies the transformation before any searches are sent to external zones.

The pre-search transform configuration described in this document is used to standardize destination aliases originating from
                           both H.323 and SIP devices. This means that the same call searches work for calls from both H.323 and SIP endpoints.

For example, if the called address is an H.323 E.164 alias “01234”, the Expressway automatically appends the configured domain
                           name (in this case example.com) to the called address (that is, 01234@example.com making it into a URI), before attempting
                           to set up the call.

Use pre-search transforms with care, because they apply to all signaling messages. If they match, they will affect the routing
                                 of Unified Communications messages, provisioning and presence requests as well as call requests.

Transformations can also be carried out in search rules. Consider whether it's best to use a pre-search transform or a search
                                 rule to modify the called address to be looked up.

## Search Rules

Search rules define how the Expressway routes calls (to destination zones, such as to Unified CM, or another Expressway, or
                           Meeting Server) in specific call scenarios. When a search rule is matched, the destination alias can be modified according
                           to the conditions defined in the search rule.

The search rules described in this document are used to ensure that endpoints can dial H.323 devices that have registered
                           E.164 numbers or H.323 IDs without a domain portion. The search rules first search for received destination aliases without
                           the domain portion of the URI, and then search with the full URI.

The search rules described here are used to enable the following routing combinations:

Calling party

Called party

Registered devices (Expressway-C or Expressway-E)

Registered devices (Expressway-C or Expressway-E)

Registered devices (Expressway-C or Expressway-E)

External domains and un-registered devices (via Expressway-E using DNS zone)

Registered devices (Expressway-C or Expressway-E)

Public external IP addresses (via Expressway-E)

External domains and un-registered devices

Registered devices (Expressway-C or Expressway-E)

The routing configuration in this document searches for destination aliases that have valid SIP URIs. That is, using a valid
                           SIP domain, such as <id@domain> .

You can configure routing which enables calls to unregistered devices on an internal network (routing to the addresses of
                           IP of the devices) by configuring a search rule with a mode of Any IP address with target Local Zone. However this is not recommended (and not described in this document). The best practice is to register
                           all devices and route using destination aliases.

## Task 8: Configuring Transforms

The pre-search transform configuration described in this document is used to standardize destination aliases originating from
                           both H.323 and SIP devices.

The following transform modifies the destination alias of all call attempts made to destination aliases which do not contain
                           an ‘@’. The old destination alias has @example.com appended to it, thus standardizing all called destination aliases into
                           a SIP URI format.

### To Configure the Transform

Go to Configuration > Dial plan > Transforms .

Click New .

Configure the transform fields as follows:

Expressway-C

Expressway-E

Priority

Enter 1

Same as Expressway-C

Description

Enter Transform destination aliases to URI format

Pattern type

Regex

Pattern string

Enter ([^@]*)

Pattern behavior

Replace

Replace string

Enter \1@example.com

State

Enabled

Click Create transform .

## Task 9: Configuring Local Zone Search Rules

Go to Configuration > Dial plan > Search rules .

First disable the supplied default search rule ( LocalZoneMatch ), as follows:

Select the check box next to LocalZoneMatch .

Click Disable .

Click OK .

Click New .

Configure the search rule fields as follows:

Expressway-C

Expressway-E

Rule name

Enter Local zone – full URI

Same as Expressway-C

Description

Enter Search local zone for SIP devices with a domain

Priority

Enter 50

Any

Source

Any

Request must be authenticated

No

Mode

Alias pattern match

Pattern type

Regex

Pattern string

Enter (.+)@example.com.*

Pattern behavior

Leave

On successful match

Continue

Target

LocalZone

State

Enabled

Click Create search rule .

## Task 10: Configuring the Traversal Zone

The traversal zone configuration defines a connection between the Expressway-C and Expressway-E platforms. A traversal zone
                           connection allows firewall traversal for signaling and media between the two platforms. Expressway-C is configured with a
                           traversal client zone. Expressway-E is configured with a traversal server zone.

Which type of traversal zone?

If your deployment is for business to business calling, use a traversal zone.

If your deployment is for mobile and remote access, use a Unified Communications traversal zone (see next section).

Chained firewall traversal

For business-to-business Expressway deployments, you can configure firewall traversal chaining. As well as acting as a traversal
                           server, Expressway-E can act as a traversal client to another Expressway-E.

If you chain two Expressway-Es for example (pictured), the first Expressway-E is a traversal server for the Expressway-C.
                           That first Expressway-E is also a traversal client of the second Expressway-E. The second Expressway-E is a traversal server
                           for the first Expressway-E.

Traversal chaining is not supported for Mobile and Remote Access deployments.

This capability was formally introduced to the Cisco Expressway Series in version X8.10. It has been possible with the Cisco
                                             TelePresence VCS since firewall traversal was introduced.

Traversal zones for Unified Communications

If you need Unified Communications features like mobile and remote access or Jabber Guest, a secure traversal zone connection
                           must exist between Expressway-C and Expressway-E:

The Expressway-C and Expressway-E must be configured with a zone of type Unified Communications traversal . This automatically configures an appropriate traversal zone (a traversal client zone when selected on Expressway-C or a
                                 traversal server zone when selected on Expressway-E) that uses SIP TLS with TLS verify mode set to On , and Media encryption mode set to Force encrypted .

Both Expressways must trust each other's server certificate. As each Expressway acts both as a client and as a server you
                                 must ensure that each Expressway’s certificate is valid both as a client and as a server.

If an H.323 or a non-encrypted connection is also required, a separate pair of traversal zones must be configured.

### To Configure the Traversal Zone:

Go to Configuration > Zones > Zones .

Click New .

Configure the fields as follows. Leave all other fields with default values:

Expressway-C

Expressway-E

Name

Enter TraversalZone

Enter TraversalZone

Type

Traversal client

Traversal client

Username

Enter exampleauth

Enter exampleauth

Password

Enter ex4mpl3.c0m

Not applicable

H.323 Mode

On

On

H.323 Protocol

Assent

Assent

H.323 Port

Enter 6001

Enter 6001

H.323 H.460.19 demultiplexing mode

Not applicable

Off

SIP Mode

On

On

SIP Port

Enter 7001

Enter 7001

SIP Transport

TLS

TLS

SIP TLS verify mode

Off

Off

SIP Accept proxied registrations

Allow

Off

Location Peer 1 address

Enter 192.0.2.2

Not applicable

Click Create zone .

### Configuring Authentication Credentials in Expressway-E

Go to Configuration > Authentication > Devices > Local database .

Click New .

Configure the fields as follows:

Expressway-C

Expressway-E

Name

Not applicable

Enter exampleauth

Password

Not applicable

Enter ex4mpl3.c0m

Click Create credential .

## Neighboring Between Expressway Clusters

You can neighbor your local Expressway cluster to a remote cluster. The remote cluster might be a neighbor, traversal client,
                           or traversal server to the local system. When a call is received on the local Expressway and is passed via the relevant zone
                           to the remote cluster, it gets routed to whichever peer in that neighbor cluster has the lowest resource usage (peers in maintenance
                           mode are not considered). That peer then forwards the call to one of the following:

A locally registered endpoint, if the endpoint is registered to that peer

A peer, if the endpoint is registered to another peer in the cluster

An external zone, if the endpoint is located elsewhere

Configuration instructions are provided in the Expressway Administrator Guide .

## Task 11: Configuring Traversal Zone Search Rules

Go to Configuration > Dial plan > Search rules .

Click New .

Configure the fields as follows:

Expressway-C

Expressway-E

Rule name

"Traversal zone search rule" for example

"Traversal zone search rule" for example

Description

"Search traversal zone - EXPe" for example

"Search traversal zone - EXPc" for example

Priority

100

100

Protocol

Any

Any

Source

Any

Any

Request must be authenticated

No

No

Mode

Any alias

Any alias

On successful match

Continue

Continue

Target

Traversal zone

Traversal zone

State

Enabled

Enabled

We recommend not using any-alias within search rule on Expressway-E as it can lead to denial-of-service (DoS).

Click Create search rule .

## Task 12: Configuring the DNS Zone

The DNS zone is used to search for externally hosted systems (such as for business to business calling). Destination aliases
                           are searched for by a name using a DNS lookup.

### To Configure the DNS Zone:

Sign in to the Expressway-E.

Go to Configuration > Zones > Zones .

Click New .

Configure the fields as follows (leave all other fields with default values):

Field name

Value

Name

Enter DNSZone for example

Type

DNS

H.323 Mode

On

SIP Mode

On

Fallback transport protocol

TCP

Include address record

Off

Click Create zone .

## Task 13: Configuring DNS Zone Search Rules

The DNS search rule defines when the DNS zone should be searched.

A specific regular expression is configured which will prevent searches being made using the DNS zone (i.e. on the public
                           internet) for destination addresses (URIs) using any SIP domains which are configured on the local network (local domains).

### To Create the Search Rules to Route via DNS:

Sign in to the Expressway-E.

Go to Configuration > Dial plan > Search rules .

Click New .

Configure the fields as follows:

Field name

Value

Rule name

Enter DNS zone search rule for example

Description

Enter Search DNS zone (external calling) for example

Priority

150

Protocol

Any

Source

All zones

Request must be authenticated

No

Mode

Alias pattern match

Pattern type

Regex

Pattern string

<(?!.*@example\.com.*$).*>

Pattern behavior

Leave

On successful match

Continue

Target

DNSZone

State

Enabled

Click Create search rule .

The regular expression used to prevent local domains being searched via the DNS zone can be broken down into the following
                                                         components:

(.*) = match all pattern strings

(?!.*@example\.com.*$).* = do not match any pattern strings ending in @example.com

In the deployment example, calls destined for @cisco.com would be searched via the DNS zone, whereas calls destined for @example.com would not.

## Task 14: Configuring External (Unknown) IP Address Routing

The following configuration defines how an Expressway routes calls (and other requests) to external IP addresses. An external
                           IP address is an IP address which is not "known" to the Expressway and therefore assumed to be a publicly routable address.

Known IP addresses are addresses defined in a subzone (using a subzone membership subnet rule).

All requests destined for external IP addresses, originating at the Expressway-C are routed to the Expressway-E using a search
                                 rule.

The Expressway-E then attempts to open a connection directly to the IP address.

### To Configure How the Expressway Handles Calls to Unknown IP Addresses:

Go to Configuration > Dial plan > Configuration .

Configure the fields as follows:

Expressway-C

Expressway-E

Calls to unknown IP addresses

Indirect

Direct

Click Save .

### To Create the Search Rules to Route Calls to IP addresses to the Expressway-E:

Go to Configuration > Dial plan > Search rules .

Click New .

Configure the fields as follows:

Expressway-C

Expressway-E

Rule name

Enter External IP address search rule

Not applicable

Description

Enter Route external IP address

Not applicable

Priority

Enter 100

Not applicable

Protocol

Any

Not applicable

Source

Any

Not applicable

Request must be authenticated

No

Not applicable

Mode

Any IP address

Not applicable

On successful match

Continue

Not applicable

Target

TraversalZone

Not applicable

State

Enabled

Not applicable

Click Create search rule .

| Calling party | Called party |
|---|---|
| Registered devices (Expressway-C or Expressway-E) | Registered devices (Expressway-C or Expressway-E) |
| Registered devices (Expressway-C or Expressway-E) | External domains and un-registered devices (via Expressway-E using DNS zone) |
| Registered devices (Expressway-C or Expressway-E) | Public external IP addresses (via Expressway-E) |
| External domains and un-registered devices | Registered devices (Expressway-C or Expressway-E) |

| Step 1 | Go to Configuration > Dial plan > Transforms . |
|---|---|
| Step 2 | Click New . |
| Step 3 | Configure the transform fields as follows: Expressway-C Expressway-E Priority Enter 1 Same as Expressway-C Description Enter Transform destination aliases to URI format Pattern type Regex Pattern string Enter ([^@]*) Pattern behavior Replace Replace string Enter \1@example.com State Enabled |  | Expressway-C | Expressway-E | Priority | Enter 1 | Same as Expressway-C | Description | Enter Transform destination aliases to URI format | Pattern type | Regex | Pattern string | Enter ([^@]*) | Pattern behavior | Replace | Replace string | Enter \1@example.com | State | Enabled |
|  | Expressway-C | Expressway-E |
| Priority | Enter 1 | Same as Expressway-C |
| Description | Enter Transform destination aliases to URI format |
| Pattern type | Regex |
| Pattern string | Enter ([^@]*) |
| Pattern behavior | Replace |
| Replace string | Enter \1@example.com |
| State | Enabled |
| Step 4 | Click Create transform . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Priority | Enter 1 | Same as Expressway-C |
| Description | Enter Transform destination aliases to URI format |
| Pattern type | Regex |
| Pattern string | Enter ([^@]*) |
| Pattern behavior | Replace |
| Replace string | Enter \1@example.com |
| State | Enabled |

| Step 1 | Go to Configuration > Dial plan > Search rules . |
|---|---|
| Step 2 | First disable the supplied default search rule ( LocalZoneMatch ), as follows: Select the check box next to LocalZoneMatch . Click Disable . Click OK . |
| Step 3 | Click New . |
| Step 4 | Configure the search rule fields as follows: Expressway-C Expressway-E Rule name Enter Local zone – full URI Same as Expressway-C Description Enter Search local zone for SIP devices with a domain Priority Enter 50 Protocol Any Source Any Request must be authenticated No Mode Alias pattern match Pattern type Regex Pattern string Enter (.+)@example.com.* Pattern behavior Leave On successful match Continue Target LocalZone State Enabled |  | Expressway-C | Expressway-E | Rule name | Enter Local zone – full URI | Same as Expressway-C | Description | Enter Search local zone for SIP devices with a domain | Priority | Enter 50 | Protocol | Any | Source | Any | Request must be authenticated | No | Mode | Alias pattern match | Pattern type | Regex | Pattern string | Enter (.+)@example.com.* | Pattern behavior | Leave | On successful match | Continue | Target | LocalZone | State | Enabled |
|  | Expressway-C | Expressway-E |
| Rule name | Enter Local zone – full URI | Same as Expressway-C |
| Description | Enter Search local zone for SIP devices with a domain |
| Priority | Enter 50 |
| Protocol | Any |
| Source | Any |
| Request must be authenticated | No |
| Mode | Alias pattern match |
| Pattern type | Regex |
| Pattern string | Enter (.+)@example.com.* |
| Pattern behavior | Leave |
| On successful match | Continue |
| Target | LocalZone |
| State | Enabled |
| Step 5 | Click Create search rule . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Rule name | Enter Local zone – full URI | Same as Expressway-C |
| Description | Enter Search local zone for SIP devices with a domain |
| Priority | Enter 50 |
| Protocol | Any |
| Source | Any |
| Request must be authenticated | No |
| Mode | Alias pattern match |
| Pattern type | Regex |
| Pattern string | Enter (.+)@example.com.* |
| Pattern behavior | Leave |
| On successful match | Continue |
| Target | LocalZone |
| State | Enabled |

| Note | Traversal chaining is not supported for Mobile and Remote Access deployments. This capability was formally introduced to the Cisco Expressway Series in version X8.10. It has been possible with the Cisco
                                             TelePresence VCS since firewall traversal was introduced. |
|---|---|

| Step 1 | Go to Configuration > Zones > Zones . |
|---|---|
| Step 2 | Click New . |
| Step 3 | Configure the fields as follows. Leave all other fields with default values: Expressway-C Expressway-E Name Enter TraversalZone Enter TraversalZone Type Traversal client Traversal client Username Enter exampleauth Enter exampleauth Password Enter ex4mpl3.c0m Not applicable H.323 Mode On On H.323 Protocol Assent Assent H.323 Port Enter 6001 Enter 6001 H.323 H.460.19 demultiplexing mode Not applicable Off SIP Mode On On SIP Port Enter 7001 Enter 7001 SIP Transport TLS TLS SIP TLS verify mode Off Off SIP Accept proxied registrations Allow Off Location Peer 1 address Enter 192.0.2.2 Not applicable |  | Expressway-C | Expressway-E | Name | Enter TraversalZone | Enter TraversalZone | Type | Traversal client | Traversal client | Username | Enter exampleauth | Enter exampleauth | Password | Enter ex4mpl3.c0m | Not applicable | H.323 Mode | On | On | H.323 Protocol | Assent | Assent | H.323 Port | Enter 6001 | Enter 6001 | H.323 H.460.19 demultiplexing mode | Not applicable | Off | SIP Mode | On | On | SIP Port | Enter 7001 | Enter 7001 | SIP Transport | TLS | TLS | SIP TLS verify mode | Off | Off | SIP Accept proxied registrations | Allow | Off | Location Peer 1 address | Enter 192.0.2.2 | Not applicable |
|  | Expressway-C | Expressway-E |
| Name | Enter TraversalZone | Enter TraversalZone |
| Type | Traversal client | Traversal client |
| Username | Enter exampleauth | Enter exampleauth |
| Password | Enter ex4mpl3.c0m | Not applicable |
| H.323 Mode | On | On |
| H.323 Protocol | Assent | Assent |
| H.323 Port | Enter 6001 | Enter 6001 |
| H.323 H.460.19 demultiplexing mode | Not applicable | Off |
| SIP Mode | On | On |
| SIP Port | Enter 7001 | Enter 7001 |
| SIP Transport | TLS | TLS |
| SIP TLS verify mode | Off | Off |
| SIP Accept proxied registrations | Allow | Off |
| Location Peer 1 address | Enter 192.0.2.2 | Not applicable |
| Step 4 | Click Create zone . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Name | Enter TraversalZone | Enter TraversalZone |
| Type | Traversal client | Traversal client |
| Username | Enter exampleauth | Enter exampleauth |
| Password | Enter ex4mpl3.c0m | Not applicable |
| H.323 Mode | On | On |
| H.323 Protocol | Assent | Assent |
| H.323 Port | Enter 6001 | Enter 6001 |
| H.323 H.460.19 demultiplexing mode | Not applicable | Off |
| SIP Mode | On | On |
| SIP Port | Enter 7001 | Enter 7001 |
| SIP Transport | TLS | TLS |
| SIP TLS verify mode | Off | Off |
| SIP Accept proxied registrations | Allow | Off |
| Location Peer 1 address | Enter 192.0.2.2 | Not applicable |

| Step 1 | Go to Configuration > Authentication > Devices > Local database . |
|---|---|
| Step 2 | Click New . |
| Step 3 | Configure the fields as follows: Expressway-C Expressway-E Name Not applicable Enter exampleauth Password Not applicable Enter ex4mpl3.c0m |  | Expressway-C | Expressway-E | Name | Not applicable | Enter exampleauth | Password | Not applicable | Enter ex4mpl3.c0m |
|  | Expressway-C | Expressway-E |
| Name | Not applicable | Enter exampleauth |
| Password | Not applicable | Enter ex4mpl3.c0m |
| Step 4 | Click Create credential . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Name | Not applicable | Enter exampleauth |
| Password | Not applicable | Enter ex4mpl3.c0m |

| Step 1 | Go to Configuration > Dial plan > Search rules . |
|---|---|
| Step 2 | Click New . |
| Step 3 | Configure the fields as follows: Expressway-C Expressway-E Rule name "Traversal zone search rule" for example "Traversal zone search rule" for example Description "Search traversal zone - EXPe" for example "Search traversal zone - EXPc" for example Priority 100 100 Protocol Any Any Source Any Any Request must be authenticated No No Mode Any alias Any alias 1 On successful match Continue Continue Target Traversal zone Traversal zone State Enabled Enabled 1 This example routes any alias across the traversal zone towards the Expressway-C. You can be more selective by adding search
                                             rules or configuring call policy. Note We recommend not using any-alias within search rule on Expressway-E as it can lead to denial-of-service (DoS). |  | Expressway-C | Expressway-E | Rule name | "Traversal zone search rule" for example | "Traversal zone search rule" for example | Description | "Search traversal zone - EXPe" for example | "Search traversal zone - EXPc" for example | Priority | 100 | 100 | Protocol | Any | Any | Source | Any | Any | Request must be authenticated | No | No | Mode | Any alias | Any alias 1 | On successful match | Continue | Continue | Target | Traversal zone | Traversal zone | State | Enabled | Enabled | Note | We recommend not using any-alias within search rule on Expressway-E as it can lead to denial-of-service (DoS). |
|  | Expressway-C | Expressway-E |
| Rule name | "Traversal zone search rule" for example | "Traversal zone search rule" for example |
| Description | "Search traversal zone - EXPe" for example | "Search traversal zone - EXPc" for example |
| Priority | 100 | 100 |
| Protocol | Any | Any |
| Source | Any | Any |
| Request must be authenticated | No | No |
| Mode | Any alias | Any alias 1 |
| On successful match | Continue | Continue |
| Target | Traversal zone | Traversal zone |
| State | Enabled | Enabled |
| Note | We recommend not using any-alias within search rule on Expressway-E as it can lead to denial-of-service (DoS). |
| Step 4 | Click Create search rule . Figure 2. Traversal Zone Search Rule on Expressway-C Figure 3. Traversal Zone Search Rule on Expressway-E |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Rule name | "Traversal zone search rule" for example | "Traversal zone search rule" for example |
| Description | "Search traversal zone - EXPe" for example | "Search traversal zone - EXPc" for example |
| Priority | 100 | 100 |
| Protocol | Any | Any |
| Source | Any | Any |
| Request must be authenticated | No | No |
| Mode | Any alias | Any alias 1 |
| On successful match | Continue | Continue |
| Target | Traversal zone | Traversal zone |
| State | Enabled | Enabled |

| Note | We recommend not using any-alias within search rule on Expressway-E as it can lead to denial-of-service (DoS). |
|---|---|

| Step 1 | Sign in to the Expressway-E. |
|---|---|
| Step 2 | Go to Configuration > Zones > Zones . |
| Step 3 | Click New . |
| Step 4 | Configure the fields as follows (leave all other fields with default values): Field name Value Name Enter DNSZone for example Type DNS H.323 Mode On SIP Mode On Fallback transport protocol TCP Include address record Off | Field name | Value | Name | Enter DNSZone for example | Type | DNS | H.323 Mode | On | SIP Mode | On | Fallback transport protocol | TCP | Include address record | Off |
| Field name | Value |
| Name | Enter DNSZone for example |
| Type | DNS |
| H.323 Mode | On |
| SIP Mode | On |
| Fallback transport protocol | TCP |
| Include address record | Off |
| Step 5 | Click Create zone . |

| Field name | Value |
|---|---|
| Name | Enter DNSZone for example |
| Type | DNS |
| H.323 Mode | On |
| SIP Mode | On |
| Fallback transport protocol | TCP |
| Include address record | Off |

| Step 1 | Sign in to the Expressway-E. |
|---|---|
| Step 2 | Go to Configuration > Dial plan > Search rules . |
| Step 3 | Click New . |
| Step 4 | Configure the fields as follows: Field name Value Rule name Enter DNS zone search rule for example Description Enter Search DNS zone (external calling) for example Priority 150 Protocol Any Source All zones Request must be authenticated No Mode Alias pattern match Pattern type Regex Pattern string <(?!.*@example\.com.*$).*> Pattern behavior Leave On successful match Continue Target DNSZone State Enabled | Field name | Value | Rule name | Enter DNS zone search rule for example | Description | Enter Search DNS zone (external calling) for example | Priority | 150 | Protocol | Any | Source | All zones | Request must be authenticated | No | Mode | Alias pattern match | Pattern type | Regex | Pattern string | <(?!.*@example\.com.*$).*> | Pattern behavior | Leave | On successful match | Continue | Target | DNSZone | State | Enabled |
| Field name | Value |
| Rule name | Enter DNS zone search rule for example |
| Description | Enter Search DNS zone (external calling) for example |
| Priority | 150 |
| Protocol | Any |
| Source | All zones |
| Request must be authenticated | No |
| Mode | Alias pattern match |
| Pattern type | Regex |
| Pattern string | <(?!.*@example\.com.*$).*> |
| Pattern behavior | Leave |
| On successful match | Continue |
| Target | DNSZone |
| State | Enabled |
| Step 5 | Click Create search rule . Note The regular expression used to prevent local domains being searched via the DNS zone can be broken down into the following
                                                         components: (.*) = match all pattern strings (?!.*@example\.com.*$).* = do not match any pattern strings ending in @example.com In the deployment example, calls destined for @cisco.com would be searched via the DNS zone, whereas calls destined for @example.com would not. | Note | The regular expression used to prevent local domains being searched via the DNS zone can be broken down into the following
                                                         components: (.*) = match all pattern strings (?!.*@example\.com.*$).* = do not match any pattern strings ending in @example.com In the deployment example, calls destined for @cisco.com would be searched via the DNS zone, whereas calls destined for @example.com would not. |
| Note | The regular expression used to prevent local domains being searched via the DNS zone can be broken down into the following
                                                         components: (.*) = match all pattern strings (?!.*@example\.com.*$).* = do not match any pattern strings ending in @example.com In the deployment example, calls destined for @cisco.com would be searched via the DNS zone, whereas calls destined for @example.com would not. |

| Field name | Value |
|---|---|
| Rule name | Enter DNS zone search rule for example |
| Description | Enter Search DNS zone (external calling) for example |
| Priority | 150 |
| Protocol | Any |
| Source | All zones |
| Request must be authenticated | No |
| Mode | Alias pattern match |
| Pattern type | Regex |
| Pattern string | <(?!.*@example\.com.*$).*> |
| Pattern behavior | Leave |
| On successful match | Continue |
| Target | DNSZone |
| State | Enabled |

| Note | The regular expression used to prevent local domains being searched via the DNS zone can be broken down into the following
                                                         components: (.*) = match all pattern strings (?!.*@example\.com.*$).* = do not match any pattern strings ending in @example.com In the deployment example, calls destined for @cisco.com would be searched via the DNS zone, whereas calls destined for @example.com would not. |
|---|---|

| Step 1 | Go to Configuration > Dial plan > Configuration . |
|---|---|
| Step 2 | Configure the fields as follows: Expressway-C Expressway-E Calls to unknown IP addresses Indirect Direct Figure 4. Expressway-C Figure 5. Expressway-E |  | Expressway-C | Expressway-E | Calls to unknown IP addresses | Indirect | Direct |
|  | Expressway-C | Expressway-E |
| Calls to unknown IP addresses | Indirect | Direct |
| Step 3 | Click Save . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Calls to unknown IP addresses | Indirect | Direct |

| Step 1 | Go to Configuration > Dial plan > Search rules . |
|---|---|
| Step 2 | Click New . |
| Step 3 | Configure the fields as follows: Expressway-C Expressway-E Rule name Enter External IP address search rule Not applicable Description Enter Route external IP address Not applicable Priority Enter 100 Not applicable Protocol Any Not applicable Source Any Not applicable Request must be authenticated No Not applicable Mode Any IP address Not applicable On successful match Continue Not applicable Target TraversalZone Not applicable State Enabled Not applicable |  | Expressway-C | Expressway-E | Rule name | Enter External IP address search rule | Not applicable | Description | Enter Route external IP address | Not applicable | Priority | Enter 100 | Not applicable | Protocol | Any | Not applicable | Source | Any | Not applicable | Request must be authenticated | No | Not applicable | Mode | Any IP address | Not applicable | On successful match | Continue | Not applicable | Target | TraversalZone | Not applicable | State | Enabled | Not applicable |
|  | Expressway-C | Expressway-E |
| Rule name | Enter External IP address search rule | Not applicable |
| Description | Enter Route external IP address | Not applicable |
| Priority | Enter 100 | Not applicable |
| Protocol | Any | Not applicable |
| Source | Any | Not applicable |
| Request must be authenticated | No | Not applicable |
| Mode | Any IP address | Not applicable |
| On successful match | Continue | Not applicable |
| Target | TraversalZone | Not applicable |
| State | Enabled | Not applicable |
| Step 4 | Click Create search rule . |

|  | Expressway-C | Expressway-E |
|---|---|---|
| Rule name | Enter External IP address search rule | Not applicable |
| Description | Enter Route external IP address | Not applicable |
| Priority | Enter 100 | Not applicable |
| Protocol | Any | Not applicable |
| Source | Any | Not applicable |
| Request must be authenticated | No | Not applicable |
| Mode | Any IP address | Not applicable |
| On successful match | Continue | Not applicable |
| Target | TraversalZone | Not applicable |
| State | Enabled | Not applicable |