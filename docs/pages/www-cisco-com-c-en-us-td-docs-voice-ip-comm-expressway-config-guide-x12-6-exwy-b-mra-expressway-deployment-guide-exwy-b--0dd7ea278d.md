---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--0dd7ea278d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_0100.html
retrieved_at: 2026-08-16T15:34:51.809175+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: MRA Infrastructure Requirements

## Chapter: MRA Infrastructure Requirements

# MRA Infrastructure Requirements

## Required Versions

MRA through Cisco Expressway requires the following components. These are minimum requirements, and some individual MRA features need later software versions which are specified, where applicable, in the
                              relevant part of the guide.

### Infrastructure Product Versions

Product

MRA Support

Legacy Authentication (LDAP)

Legacy Authentication with SSO

OAuth  with Refresh

OAuth Refresh with SSO

APNS

Expressway

X8.1.1

X8.1.1

X8.5.1

X8.10.1

X8.10.1

X8.10.1

Unified CM

10.0

-

SAML SSO: 10.5(1)

11.5(1) SU3

10.5(2)

11.5(1) SU3

CUCM IM & P (optional)

10.0

-

SAML SSO: 10.5(1)

11.5(1) SU3

10.5(2)

11.5(1) SU3

Cisco Unity Connection (optional)

10.0

-

Clusterwide SAML SSO: 11.5(1)

Per node SSO: OpenAM: 8.6(2) SAML SSO: 10.0(1)

-

-

NA

## Configuration Recommendations and Requirements

### IP Addresses

Assign separate IP addresses to the Expressway-C and the Expressway-E. Do not use a shared address for both elements, as the
                                 firewall cannot distinguish between them.

### Network Domain

The ideal scenario for MRA is to have a single domain with a split DNS configuration, and this is the recommended approach.
                                 This is not always possible, so there are some other approaches to deal with various alternative scenarios.

The domain to which the calls are routed must match with the MRA domain to which the endpoints were registered. For example,
                                             if endpoints are registered with the domain exp.example.com , the calls must be routed to this domain, and it must not be routed to the domain cluster1.exp.example.com .

### DNS

#### Single Domain with Split DNS - Recommended

A single domain means that you have a common domain ( example.com ) with separate internal and external DNS servers. This allows DNS names to be resolved differently by clients on different
                                 networks depending on DNS configuration, and aligns with basic Jabber service discovery requirements.

#### Dual Domain without Split DNS

From X12.5, the Cisco Expressway Series supports the case where MRA clients use an external domain to lookup the _collab-edge SRV record, and the _cisco-uds SRV record for that same external domain cannot be resolved by the Expressway-C. This is typically the case when split DNS
                                 is not available for the external domain. And prior to X12.5 this required a pinpoint subdomain or some other DNS workaround
                                 on the Expressway-C, to satisfy the client requirements for resolving the _cisco-uds record.

Limitation : This case is not supported for Unified CM nodes identified by IP addresses, only for FQDNs.

This feature also supports a secondary case, for MRA deployments that only allow Jabber access over MRA even if users are
                                 working on-premises. In this case only one domain is required and typically the DNS records are publicly resolvable (although
                                 this is not required if MRA access is disallowed for users when off premises). The change in X12.5 means that there is no
                                 need to have a _cisco-uds._tcp.<external-domain> DNS SRV record available to Cisco Expressway-C or to the Jabber clients.

#### Single Domain without Split DNS

Deployments that require Jabber clients to always connect over MRA also benefit from the X12.5 update that no longer requires the Expressway-C to resolve
                                 the _cisco-uds DNS SRV record. So administrators only need to configure the _collab-edge DNS SRV record, and Jabber clients using service discovery will only have the option of connecting over MRA.

#### URL for Cisco Meeting Server Web Proxy and MRA domain cannot be the same

If you use both the CMS Web Proxy service and MRA on the same Expressway, the following configuration items must be assigned
                                 different values per service. If you try to use the same value, the service that was configured first will work, but the other
                                 one will fail:

MRA domain(s). The domain(s) configured on Expressway and enabled for Unified CM registration

CMS Web Proxy URL link. Defined in the Expressway "Guest account client URI" setting on the Expressway > Configuration > Unified Communications > Cisco Meeting Server page.

#### Multiple External Domains for Mobile and Remote Access

Cisco Expressway supports Mobile and Remote Access with multiple external domains. With this deployment, you will have more
                                 than one external domain where your MRA clients may reside. Expressway-E must be able to connect to all of them. To configure
                                 this deployment, do the following:

For Expressway-E:

Configure your external DNS with two or more entries for the _collab_edge SRV record. The record must point to both Expressway-E
                                       hostname and domains. For example:

Expressway-E.hostname.domain1

Expressway-E.hostname.domain2

For the Certificate Signing Request, include both Expressway-E FQDNs.

For Expressway-C:

For internal DNS, add A and PTR records that point to both Expressway-E FQDNs. Add these records to all Expressway-C nodes.

Configure the _cisco_uds SRV record for every domain to point to your Unified Communications Manager clusters.

On the Domains page of Expressway-C, add each of the internal domains that point to the Unified Communications Manager cluster.

#### SRV Records

This section summarizes the public (external) and local (internal) DNS requirements for MRA. For more information, see the Cisco Jabber Planning Guide for your version on the Jabber Install and Upgrade Guides page .

#### Public DNS (External Domains)

The public, external DNS must be configured with _collab-edge._tls.<domain> SRV records so that endpoints can discover the Expressway-Es to use for Mobile and Remote Access. You also need SIP service
                                    records for general deployment (not specifically for MRA).

Domain

Service

Protocol

Priority

Weight

Port

Target host

example.com

collab-edge

tls

10

10

8443

expe1.example.com

example.com

collab-edge

tls

10

10

8443

expe2.example.com

example.com

sips

tcp

10

10

5061

expe1.example.com

example.com

sips

tcp

10

10

5061

expe2.example.com

#### Local DNS (Internal Domains)

Although we recommend that the local, internal DNS is configured with _cisco-uds._tcp.<domain> SRV records, from X12.5 this
                                    is no longer a requirement .

From version X8.8, if you use the IM and Presence Service over MRA (or any XMPP federation that uses XCP TLS connections between
                                                Expressway-C and Expressway-E), you must create forward and reverse DNS entries for each Expressway-E system . This is so that Expressway-C systems making TLS connections to them can resolve the Expressway-E FQDNs and validate the
                                                Expressway-E certificates. This requirement affects only the internal, LAN-side interface and does not apply to the external
                                                IP-side.

Domain

Service

Protocol

Priority

Weight

Port

Target host

example.com

cisco-uds

tcp

10

10

8443

cucmserver1.example.com

example.com

cisco-uds

tcp

10

10

8443

cucmserver2.example.com

Create internal DNS records, for both forward and reverse lookups, for all Unified Communications nodes used with MRA. This
                                    allows Expressway-C to find the nodes when IP addresses or hostnames are used instead of FQDNs.

Ensure that the cisco-uds SRV records are NOT resolvable outside of the internal network, otherwise the Jabber client will
                                    not start MRA negotiation via the Expressway-E.

### Firewall Configuration

Ensure that the relevant ports are configured on your firewalls between your internal network (where the Expressway-C is
                                       located) and the DMZ (where the Expressway-E is located) and between the DMZ and the public internet.

No inbound ports are required to be opened on the internal firewall. The internal firewall must allow the following outbound
                                       connections from Expressway-C to Expressway-E: SIP: TCP 7001; Traversal Media: UDP 2776 to 2777 (or 36000 to 36011 for large
                                       VM/appliance); XMPP: TCP 7400; HTTPS (tunneled over SSH between C and E): TCP 2222.

The external firewall must allow the following inbound connections to Expressway: SIP: TCP 5061; HTTPS: TCP 8443; XMPP: TCP
                                       5222; Media: UDP 36002 to 59999.

For more information, see Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series configuration guides page .

Do not use a shared address for the Expressway-E and the Expressway-C, as the firewall cannot distinguish between them. If
                                       you use static NAT for IP addressing on the Expressway-E, make sure that any NAT operation on the Expressway-C does not resolve
                                       to the same traffic IP address. We do not support shared NAT addresses between Expressway-E and Expressway-C.

The traversal zone on the Expressway-C points to the Expressway-E through the Peer address field on the traversal zone, which specifies the address of the Expressway-E server.

For dual NIC deployments, you can specify the Expressway-E address using a FQDN that resolves to the IP address of the internal
                                             interface. With split DNS you can optionally use the same FQDN as is available on the public DNS. If you don't use split DNS
                                             you must use a different FQDN.

For single NIC with static NAT (this deployment is NOT recommended), you must specify the Expressway-E address using a FQDN
                                             that resolves to the public IP address. This also means that the external firewall must allow traffic from the Expressway-C
                                             to the external FQDN of the Expressway-E.  This is known as NAT reflection, and may not be supported by all types of firewalls.

For more information, see the "Advanced networking deployments" appendix in the Expressway Basic Configuration (Expressway-C with Expressway-E) Deployment Guide

### Bandwidth Restrictions

The Maximum Session Bit Rate for Video Calls on the default region on Cisco Unified Communications Manager is 384 kbps by default. The Default call bandwidth on Expressway-C is also 384 kbps by default. These settings may be too low to deliver the expected video quality for MRA-connected
                                 devices.

### IM and Presence Service

If you are using an IM&P server that is earlier than 11.5(1)SU3, make sure the minimum TLS version for the XMPP service is
                                             1.0 (on newer Expressway installations the default is TLS 1.2). Instructions for configuring TLS versions and cipher suites
                                             are in the Expressway Administrator Guide.

Ensure that the Cisco AXL Web Service is active on the IM and Presence Service publishers that  discovers other IM and Presence Service nodes for remote access. To check this, select the Cisco Unified Serviceability application and go to Tools > Service Activation .

If you are deploying Mobile and Remote Access with multiple IM and Presence Service clusters, you must configure Intercluster peer links between the clusters, and the Intercluster Sync Agent (ICSA) must be
                                 active on all clusters. This ensures that the user database is replicated between clusters, allowing Expressway-C to correctly
                                 route XMPP traffic.

For details of the correct configuration, refer to the chapter "Intercluster Peer Configuration" in Configuration and Administration of IM and Presence Service on Cisco Unified Communications Manager . You can find the correct document for your version at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

| Product | MRA Support | Legacy Authentication (LDAP) | Legacy Authentication with SSO | OAuth  with Refresh | OAuth Refresh with SSO | APNS |
|---|---|---|---|---|---|---|
| Expressway | X8.1.1 | X8.1.1 | X8.5.1 | X8.10.1 | X8.10.1 | X8.10.1 |
| Unified CM | 10.0 | - | SAML SSO: 10.5(1) | 11.5(1) SU3 | 10.5(2) | 11.5(1) SU3 |
| CUCM IM & P (optional) | 10.0 | - | SAML SSO: 10.5(1) | 11.5(1) SU3 | 10.5(2) | 11.5(1) SU3 |
| Cisco Unity Connection (optional) | 10.0 | - | Clusterwide SAML SSO: 11.5(1) Per node SSO: OpenAM: 8.6(2) SAML SSO: 10.0(1) | - | - | NA |

| Note | The domain to which the calls are routed must match with the MRA domain to which the endpoints were registered. For example,
                                             if endpoints are registered with the domain exp.example.com , the calls must be routed to this domain, and it must not be routed to the domain cluster1.exp.example.com . |
|---|---|

| Domain | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| example.com | collab-edge | tls | 10 | 10 | 8443 | expe1.example.com |
| example.com | collab-edge | tls | 10 | 10 | 8443 | expe2.example.com |
| example.com | sips | tcp | 10 | 10 | 5061 | expe1.example.com |
| example.com | sips | tcp | 10 | 10 | 5061 | expe2.example.com |

| Important | From version X8.8, if you use the IM and Presence Service over MRA (or any XMPP federation that uses XCP TLS connections between
                                                Expressway-C and Expressway-E), you must create forward and reverse DNS entries for each Expressway-E system . This is so that Expressway-C systems making TLS connections to them can resolve the Expressway-E FQDNs and validate the
                                                Expressway-E certificates. This requirement affects only the internal, LAN-side interface and does not apply to the external
                                                IP-side. |
|---|---|

| Domain | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| example.com | cisco-uds | tcp | 10 | 10 | 8443 | cucmserver1.example.com |
| example.com | cisco-uds | tcp | 10 | 10 | 8443 | cucmserver2.example.com |

| Note | If you are using an IM&P server that is earlier than 11.5(1)SU3, make sure the minimum TLS version for the XMPP service is
                                             1.0 (on newer Expressway installations the default is TLS 1.2). Instructions for configuring TLS versions and cipher suites
                                             are in the Expressway Administrator Guide. |
|---|---|