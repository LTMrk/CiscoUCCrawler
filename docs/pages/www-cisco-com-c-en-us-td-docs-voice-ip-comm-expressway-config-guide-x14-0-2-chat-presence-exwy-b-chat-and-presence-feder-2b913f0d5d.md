---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-chat-presence-exwy-b-chat-and-presence-feder-2b913f0d5d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/chat_presence/exwy_b_chat-and-presence-federation-using-expressway-X1402/exwy_m_xmpp-federation-through-expressway.html
retrieved_at: 2026-08-16T15:23:44.556545+00:00
---

Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

# Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: XMPP Federation through Expressway

## Chapter: XMPP Federation through Expressway

# XMPP Federation through Expressway

## XMPP Federation through Expressway

External XMPP federation enables users registered to Cisco Unified Communications Manager IM and Presence Service, to communicate
                           via the Expressway-E with users from a different XMPP deployment.

This section describes XMPP federation as managed through Expressway, but it can also be managed through the IM and Presence
                                       Service, as described later in this guide.

The diagram shows XMPP message routing from the on-premises IM & Presence server, through the Expressway-C and Expressway-E
                           Collaboration Edge solution, to the federated XMPP server. It also shows the ports and connections as the messages traverse
                           DMZ firewalls. The "example.com" organization is using an Expressway federation model (left of picture), while the "federated.com" organization (right of picture) is using an IM and Presence Service in DMZ federation model.

### Supported Systems XMPP through Expressway

Expressway-E supports XMPP federation with the following products:

Expressway X8.2 or later

Cisco Unified Communications Manager IM and Presence Service 9.1.1 or later

Cisco Webex Connect Release 6.x

Cisco Jabber 9.7 or later

Other XMPP standards-compliant servers

### Limitations

When using Expressway for XMPP federation, the Expressway-E handles the connection to the remote federation server and can
                                    only use Jabber IDs to manage XMPP messages. Expressway-E does not support XMPP address translation (of email addresses, for
                                    example).

If you, as an external user, try to chat with a user in an enterprise through federation, you must use the enterprise user’s
                                    Jabber ID to contact them through XMPP. If their Jabber ID does not match their email address (especially if their Jabber
                                    ID uses an internal user ID or domain) you are unable to have federation, as you won't know the enterprise user’s email address.
                                    We therefore recommend that enterprises configure their Unified CM nodes to use the same address for a user’s Jabber ID and
                                    email when using Expressway for XMPP federation. This limitation does not apply to users contacting each other within the
                                    enterprise (not using federation) even when federation is handled by Expressway-E. You can configure IM and Presence Service
                                    to use either the Jabber ID or the Directory URI (typically email) for non-federated use cases.

To make a user's Jabber ID resemble a user's email address, so that the federated partner can approximate email addresses
                                    for federation, set the following:

Unified CM Lightweight Directory Access Protocol (LDAP) attribute for User ID to be the user's sAMAccountName

IM and Presence Service presence domain to be the same as the email domain.

Your email address to the same as samaccountname@presencedomain.

Simultaneous internal federation managed by IM and Presence Service and external federation managed by Expressway is not supported.
                                    If only internal federation is required then you must use interdomain federation on IM and Presence Service. The available
                                    federation deployment configuration options are:

External federation only (managed by Expressway).

Internal federation only (managed by IM and Presence Service).

Internal and external federation managed by IM and Presence Service but requires you to configure your firewall to allow inbound
                                          connections.

### Prerequisites

Interdomain XMPP Federation must be disabled on the IM and Presence Service before you enable XMPP federation on Expressway:

Go to Cisco Unified CM IM and Presence Administration > Presence > Inter Domain Federation > XMPP Federation > Settings and ensure that XMPP Federation Node Status is set to Off .

XMPP federation is only supported on a single Expressway cluster.

An Expressway-C (cluster) and Expressway-E (cluster) must be configured for Mobile and Remote Access (MRA) to Unified Communications
                                    services, as described in the Mobile and Remote Access via Cisco Expressway Deployment Guide . If only XMPP federation is required (video calls and remote registration to Unified CM are not required), these items do
                                    not have to be configured:

Domains that support SIP registrations and provisioning on Unified CM or that support IM and Presence services on Unified CM

Unified CM servers (you must still configure the IM&P servers)

HTTP server allow list

The Federated communications are available to both on-premises clients (connected directly to IM and Presence Service) and
                                                off-premises clients (connected to IM and Presence Service through MRA).

SIP and XMPP federations are separate and do not impact on each other. For example, it's possible to deploy SIP federation
                                    on IM and Presence Service and external XMPP federation on Expressway.

If you deploy external XMPP federation through Expressway, do not activate the Cisco XCP XMPP federation Connection Manager
                                    feature service on the IM and Presence Service.

If you intend to use both Transport Layer Security (TLS) and group chat, the Expressway-C and Expressway-E server certificates
                                    must include in their list of subject alternate names the Chat Node Aliases that are configured on the IM and Presence Service servers. Use either the XMPPAddress or DNS formats.

The Expressway-C automatically includes the chat node aliases in its certificate signing requests (CSRs), providing it has
                                                discovered a set of IM and Presence Service servers.

When generating CSRs for the Expressway-E we recommend that you copy-paste the chat node aliases from the equivalent Generate CSR page on the Expressway-C. For details, see Server Certificate Requirements for Unified Communications .

### Task Flow for XMPP Federation through Expressway

This table outlines the tasks required to deploy XMPP federation on Expressway:

Task

See

Validate email addresses for federation

XMPP Federation through Expressway

Ensure IM and Presence Service is operational and has XMPP federation turned off

XMPP Federation through Expressway

Complete Server Certificate Requirements

Server Certificate Requirements for Unified Communications

Configure the local domains for XMPP federation on Expressway-C

Configuring Expressway for External XMPP Federation

Configure Expressway-E for XMPP federation

Configuring Expressway for External XMPP Federation

Configure how XMPP servers for federated domains and chat node aliases are located using either DNS lookups or static routes

Configuring Expressway for External XMPP Federation

Configure the allow and deny lists for federated domains and chat node aliases

Configuring Expressway for External XMPP Federation

Publish DNS SRV records for XMPP federation (if not using static routes)

DNS SRV Records for XMPP Federation

Check that the correct firewall ports are open

See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series Configuration Guides page.

Check the status of XMPP federation

Checking XMPP Federation Status

To troubleshoot your connection

Troubleshooting External XMPP Federation

### Server Certificate Requirements for Unified Communications

#### Cisco Unified Communications Manager Certificates

Two Cisco Unified Communications Manager certificates are significant for Mobile and Remote Access:

CallManager certificate

tomcat certificate

These certificates are automatically installed on the Cisco Unified Communications Manager and by default they are self-signed
                                 and have the same common name (CN).

We recommend using CA-signed certificates. However, if you do use self-signed certificates, the two certificates must have
                                 different common names. The Expressway does not allow two self-signed certificates with the same CN. So, if the CallManager and tomcat self-signed certificates have the same CN in the Expressway's trusted CA list, the Expressway can only trust one of them.
                                 This means that either secure HTTP or secure SIP, between Expressway-C and Cisco Unified Communications Manager, will fail.

Also, when generating tomcat certificate signing requests for any products in the Cisco Collaboration Systems Release 10.5.2, you need to be aware of CSCus47235 . You need to work around this issue to ensure that the FQDNs of the nodes are in the certificates as Subject Alternative
                                 Name (SAN) entries. The Expressway X8.5.3 Release Note on the Release Notes page has details of the workarounds.

#### IM and Presence Service Certificates

Two IM and Presence Service certificates are significant if you use XMPP:

cup-xmpp certificate

tomcat certificate

We recommend using CA-signed certificates. However, if you do use self-signed certificates, the two certificates must have
                                 different common names. The Expressway does not allow two self-signed certificates with the same CN. If the cup-xmpp and tomcat (self-signed) certificates have the same CN, Expressway only trusts one of them, and some TLS attempts between Cisco Expressway-E
                                 and IM and Presence Service servers will fail. For more details, see CSCve56019 .

#### Expressway Certificates

The Expressway certificate signing request (CSR) tool prompts for and incorporates the relevant Subject Alternative Name (SAN)
                                 entries as appropriate for the Unified Communications features that are supported on that Expressway.

The following table shows which CSR alternative name elements apply to which Unified Communications features:

Add these items as subject alternative names

When generating a CSR for these purposes

Mobile and Remote Access

Jabber Guest

XMPP Federation

Business to Business Calls

Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified
                                             CM SIP registration domains)

Required on Expressway- E only

-

-

-

XMPP federation domains

-

-

Required on Expressway- E only

-

IM and Presence chat node aliases (federated group chat)

-

-

Required

-

Unified CM phone security profile names

Required on Expressway- E only

-

-

-

(Clustered systems only) Expressway cluster name

Required on Expressway- E only

Required on Expressway- E only

Required on Expressway- E only

-

You may need to produce a new server certificate for the Expressway-C if chat node aliases are added or renamed. Or when IM
                                                   and Presence nodes are added or renamed, or new TLS phone security profiles are added.

You must produce a new Expressway-E certificate if new chat node aliases are added to the system, or if the Unified CM or
                                                   XMPP federation domains are modified.

You must restart the Expressway for any new uploaded server certificate to take effect.

More details about the individual feature requirements per Expressway-C / Expressway-E are described below.

##### Expressway-C Server Certificate Requirements

The Expressway-C server certificate needs to include the following elements in its list of subject alternate names:

Unified CM phone security profile names : The names of the Phone Security Profiles in Unified CM that are configured for encrypted TLS and are used for devices requiring remote access. Use the FQDN format
                                          and separate multiple entries with commas.

Having the secure phone profiles as alternative names means that Unified CM can communicate via TLS with the Expressway-C
                                          when it is forwarding messages from devices that use those profiles.

IM and Presence chat node aliases (federated group chat) : The Chat Node Aliases (e.g. chatroom1.example.com) that are configured on the IM and Presence servers. These are required only for Unified Communications
                                          XMPP federation deployments that intend to support group chat over TLS with federated contacts.

The Expressway-C automatically includes the chat node aliases in the CSR, providing it has discovered a set of IM&P servers.

We recommend that you use DNS format for the chat node aliases when generating the CSR. You must include the same chat node
                                          aliases in the Expressway-E server certificate's alternative names.

##### Expressway-E Server Certificate Requirements

The Expressway-E server certificate needs to include the following elements in its list of subject alternative names (SAN):

Unified CM registrations domains : All the domains which are configured on the Expressway-C for Unified CM registrations. Required for secure communications
                                          between endpoint devices and Expressway-E.

The Unified CM registration domains used in the Expressway configuration and Expressway-E certificate, are used by Mobile
                                          and Remote Access clients to lookup the _collab-edge DNS SRV record during service discovery. They enable MRA registrations on Unified CM and are primarily for service discovery.

These service discovery domains may or may not match the SIP registration domains. It depends on the deployment, and they
                                          don't have to match. One example is a deployment that uses a .local or similar private domain with Unified CM on the internal
                                          network, and public domain names for the Expressway-E FQDN and service discovery. In this case, you need to include the public
                                          domain names in the Expressway-E certificate as SANs. There is no need to include the private domain names used on Unified
                                          CM. You only need to list the edge domain as a SAN.

Select the DNS format and manually specify the required FQDNs. Separate the FQDNs by commas if you need multiple domains. You may select CollabEdgeDNS format instead, which simply adds the prefix collab-edge . to the domain that you enter. This format is recommended if you do not want to include your top-level domain as a SAN (see
                                          example in following screenshot).

XMPP federation domains : The domains used for point-to-point XMPP federation. These are configured on the IM&P servers and should also be configured
                                          on the Expressway-C as domains for XMPP federation.

Select the DNS format and manually specify the required FQDNs. Separate the FQDNs by commas if you need multiple domains. Do not use the XMPPAddress format as it may not be supported by your CA and may be discontinued in future versions of the Expressway software.

IM and Presence chat node aliases (federated group chat) : The same set of Chat Node Aliases as entered on the Expressway-C's certificate. They are only required for voice and presence deployments which will support
                                          group chat over TLS with federated contacts.

You can copy the list of chat node aliases from the equivalent Generate CSR page on the Expressway-C.

See Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page.

### Configuring Expressway for External XMPP Federation

This section describes how to configure the Expressway for external XMPP federation.

#### Before You Begin

Make sure that the items specified in "Prerequisites" are complete.

Some supporting systems configuration needs to be in place:

DNS. An internal DNS configured with forward and reverse lookups for Expressway-E, Expressway-C.

External DNS. An external DNS configured with forward lookup for the Expressway-E cluster FQDN.

Traversal Zones. A traversal server zone (Expressway-E) and a traversal client zone (Expressway-C).

NTP. All servers must be internally synchronized to the same time source.

#### Configuring Local Domains for XMPP Federation on Expressway-C

You must configure the local domain names for which you want to provide XMPP federated services.

On Expressway-C, go to Configuration > Domains .

Click New (or click View/Edit if the required domain already exists).

Enter your local Domain name to be federated.

Set XMPP federation to On .

Click Save .

Repeat for any other local domains requiring federation.

A single Expressway cluster can support multiple IM and Presence Service clusters using the same presence domain.

XMPP federation of multiple IM and Presence Service clusters with multiple Expressway clusters is not supported.

Each IM and Presence Service cluster needs to be discovered by Expressway-C.

#### Configuring Expressway-E  for XMPP Federation

We recommend that XMPP federation configuration changes are made "out of hours" . Enabling XMPP federation will restart the XCP router on all Expressway-E systems within the cluster. This will temporarily
                                    interrupt any existing mobile and remote access IM&P client sessions. Depending on the number of clients, full client reconnection
                                    may take several minutes. (See Impact of Configuration Changes on a Live System for more information.)

On Expressway-E, go to Configuration > Unified Communications .

Set XMPP federation support to On .

When you apply this change, you may need to restart the XCP Routers on the IM&P server(s). The other settings on this page
                                                do not require a restart.

Configure the remaining fields as described in the table below.

Click Save .

Your changes are applied. If you toggled XMPP federation support , you will be required to confirm that you want to restart the XCP router on the Expressway-C.

You may also need to restart the Unified CM IM&P XCP router services that are connected to the associated Expressway-C.

Log on to each IM and Presence server to check for notifications that you need to restart the XCP Routers. If you do need
                                             to restart them:

In Cisco Unified IM and Presence Serviceability , go to Tools > Control Center - Network Services .

Scroll down to the IM and Presence Services section and select Cisco XCP Router .

Click Restart .

This causes a restart of all XCP services on the IM and Presence Service. The service restart may take several minutes.

Repeat on each IM and Presence server.

You could use the utils service CLI option (accessed via the Cisco Unified IM and Presence Operating System) to restart the services instead.

Settings

Description

Use static routes

Indicates whether a controlled list of static routes are used to locate the federated XMPP domains and chat node aliases,
                                                            rather than DNS lookups.

See Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located .

Dialback secret

Enter the dialback secret to use for identity verification with federated XMPP servers. If you have multiple Expressway-E
                                                            systems in the same deployment, they must all be configured with the same dialback secret.

For more information about server dialback, see http://xmpp.org/extensions/xep-0220.html

Security mode

Indicates if a TLS connection to federated XMPP servers is required, preferred, or not required.

TLS required : The system guarantees a secure (encrypted) connection with the foreign domain.

TLS optional : The system attempts to establish a TLS connection with the foreign domain. If it fails to establish a TLS connection, it
                                                                  reverts to TCP.

No TLS : The system will not establish a TLS connection with the foreign domain. It uses a non-encrypted connection to federate with
                                                                  the foreign domain.

In all cases, server dialback is used to verify the identity of the foreign server. The foreign server must be configured
                                                            to use server dialback.

SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server.

The default, and recommended setting, is TLS required .

Require client-side security certificates

Controls whether the certificate presented by the external client is verified against the Expressway's current trusted CA
                                                            list and, if loaded, the revocation list.

This setting does not apply if Security mode is No TLS .

The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting.

Privacy mode

Controls whether restrictions are applied to the set of federated domains and chat node aliases.

Off : No restrictions are applied.

Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list.

Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list.

Any domains or chat node aliases that are configured as static routes are included automatically in the allow list.

The default is Allow list .

See Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases .

#### Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located

You can use DNS lookups to locate the XMPP servers for federated domains and chat node aliases, or you can configure the addresses
                                 of specific XMPP servers.

##### To Use DNS Lookups

On Expressway-E, go to Configuration > Unified Communications .

Set Use static routes to Off .

Click Save .

All XMPP federated partners must publish in DNS the addresses of their XMPP servers as described in DNS SRV Records for XMPP Federation .

##### To Use Static Routes

Contact the partners with whom you are federating to get a list of their chat node aliases.

On Expressway-E, go to Configuration > Unified Communications .

Set Use static routes to On and click Save .

Click Configure static routes for federated XMPP domains .

On the Federated static routes page, click New .

Enter the details of the static route:

Field

Description

Domain

The federated XMPP domain or chat node alias.

Address

The IP address or Fully Qualified Domain Name (FQDN) of an XMPP server for this federated domain or chat node alias.

Click Save .

Add as many additional static routes as required.

You can specify additional routes to alternative addresses for the same domain or chat node alias (all routes have an equal
                                                   priority).

If there are no static routes defined for a federated domain or chat node alias, the system will use DNS instead.

If static routes are defined for the federated domain or chat node alias, but the remote system cannot be contacted over those
                                                                     routes, the system will not fall back to DNS.

If Privacy mode is set to Allow list and Use static routes is On , any domains (or chat node aliases) that are configured as static routes are included automatically in the allow list.

#### Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases

The allow and deny lists are used to control restrictions to the set of federated domains and chat node aliases. If Privacy mode is set to Allow list or Deny list , you must add the domains and chat node aliases with which you want to allow or deny federated connections. This function
                                    manages restrictions at the domain / chat node alias level.

Individual user-based privacy is controlled by each client / end-user.

Allow list and deny list modes are mutually exclusive. A domain/alias cannot be allowed and denied at the same time.

When federation is first enabled, Privacy mod e is set to Allow list by default. In effect this puts the system in "lockdown" mode — you will not be allowed to connect with any federated domains or chat node aliases until you add them to the allow
                                    list, configure static routes, or change the Privacy mode setting.

On Expressway-E, go to Configuration > Unified Communications .

Set Privacy mode as appropriate:

Off : No restrictions are applied.

Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list.

Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list.

Click Save .

To manage the domains and chat node aliases in the allow or deny lists, click either Federation allow list or Federation deny list as appropriate.

In the resulting page you can add, modify, or delete the items in the allow/deny list. Wildcards or regexes are not allowed
                                                in the names; it must be an exact match.

All domains and chat node aliases that are configured as static routes are included automatically in the allow list.

### Delayed Cisco XCP Router Restart

The delayed Cisco XCP Router restart feature is part of Cisco Hosted Collaboration Solution (HCS) and is only available when
                              the Expressway-E is in multitenant mode. The Expressway-E enters multitenant mode when you add a second Unified CM traversal
                              zone with a new SIP domain.

In multitenant mode, you must configure the system hostname on the System > DNS page of the Cisco Expressway-E to match the hostname configured in DNS (case-specific before X8.10.1, case insensitive from
                                          X8.10.1). Otherwise Cisco Jabber clients will be unable to register successfully for MRA.

Multitenancy allows a service provider to share an Expressway-E cluster among multiple tenants. Each tenant has a dedicated
                              Expressway-C cluster that connects to the shared Expressway-E cluster.

Certain configuration changes on the Expressway-E cluster, or a customer’s Expressway-C cluster, require a restart of the
                              Cisco XCP Router on each Expressway-E in the shared cluster. The restart is required for Cisco XCP Router configuration changes
                              to take effect across all nodes in a multitenant Expressway-E cluster. The restart affects all users across all customers.

To reduce the frequency of this restart, and the impact on users, you can use the delayed Cisco XCP Router restart feature.

Without the delayed restart feature enabled, the restart happens automatically and occurs each time you save any configuration
                                          change that affects the Cisco XCP Router. If multiple configuration changes are required, resulting in several restarts of
                                          the Cisco XCP Router, it can adversely affect users. We strongly recommend that multitenant customers enable the delayed Cisco
                                          XCP Router restart feature.

The delayed restart feature lets you control when the restart takes place. You can make a batch of configuration changes -
                              followed by a single Cisco XCP Router restart – and apply all the changes at once. A delayed restart generates the latest
                              configuration and performs a Cisco XCP Router restart on each node in the multitenant Cisco Expressway-E cluster.

When a restart of the Cisco XCP Router occurs, all XMPP clients (such as Cisco Jabber) across all customers go offline for
                              a few minutes and then reconnect. Because of this impact, we recommend that you take advantage of the delayed restart capability.

Once enabled, you can carry out the restart manually or set it to be schedule-based. In either mode, you can initiate the
                              restart at any time and the system determines which Cisco XCP Router instances require a restart, performing the restart only
                              as needed. When you set the restart to be scheduled, the restart happens at the scheduled time, but again only as needed.
                              We recommend doing the Cisco XCP Router restart during off-peak hours whenever possible.

Nodes on the latest configuration are not impacted. This action disconnects all external XCP-based users connected through
                                                the delayed nodes during the restart.

All nodes will be on the latest configuration after the restart.

More information about multitenancy, see Multitenancy with Cisco Expressway on the Cisco Hosted Collaboration Solution page.

#### How to Configure Delayed Restarts

Use the following methods to configure delayed restarts.

##### To Configure the Delayed Cisco XCP Router Restart

Go to Configuration > Unified Communications > Delayed Cisco XCP Router restart .

Under Configuration , turn Delayed Cisco XCP Router restart On .

If you do not enable Scheduled Restart, you must initiate the restart manually using the Restar t button.

Configuration changes do not happen automatically.

##### To Schedule the Restart

Under Configuration , turn Scheduled Restart On and set the time that all nodes in the multi-tenant Expressway-E cluster are updated each day. Only nodes that are not running
                                                on the latest configuration are impacted.

Set the time that the restart takes place each day using the Scheduled restart time (UTC) option.

#### Configuration Changes That Require a Restart of the Cisco XCP Router

If you make any system configuration changes in the following areas a restart of the Cisco XCP Router takes place:

XMPP federation

Internal/external Ethernet

Hostname or IP address

DNS

NTP

Option keys

QoS

Clustering

Zones

MRA

Domains

Maintenance mode

Cisco XCP Router delayed restart

Cisco XCP Router / XMPP changes through networking

Server-to-server communication to IM and Presence Service

Changes to the logging flags for any of the above

More information about configuration changes, see Impact of Configuration Changes on a Live System in the Cisco Unified Communications XMPP Federation guide.

### DNS SRV Records for XMPP Federation

If federating parties are not using static routes to access federated XMPP services, suitable DNS SRV records must be published.

#### _xmpp-server records

You must publish an _xmpp-server DNS SRV record in DNS for your local domain so that remote enterprises can access your federated XMPP services.

For example:

Domain

Service

Protocol

Priority

Weight

Port

Target host

ciscoexample.com

xmpp-server

tcp

0

0

5269

expe.ciscoexample.com

Similarly, to allow federating parties to discover a particular XMPP federated domain (if they are not using static routes),
                                 the federated enterprise must publish an _xmpp-server DNS SRV record in its public DNS server.

For example:

Domain

Service

Protocol

Priority

Weight

Port

Target host

federated.com

xmpp-server

tcp

0

0

5269

xmppserver.federated.com

All enterprises must publish the service on port 5269. The published FQDNs must also be resolvable in DNS to an IP address.

#### Group Chat

If you configure the Group Chat feature on a Unified CM IM&P server in an XMPP federation deployment, you must publish DNS
                                 SRV records for the federated chat node aliases.

To allow IM and Presence Service to discover a particular XMPP federated chat node alias, the federated enterprise must publish
                                 an _xmpp-server DNS SRV record in its public DNS server. Similarly, IM and Presence Service must publish the same DNS SRV record in DNS for
                                 its domain.

For example:

Domain

Service

Protocol

Priority

Weight

Port

Target host

chatroom1.example.com

xmpp-server

tcp

0

0

5269

expe.ciscoexample.com

Both enterprises must publish the service on port 5269. The published FQDN must also be resolvable to an IP address in DNS.

Alternatively, to use group chat aliases on federated servers, you can configure static routes on the Expressway-E ( Configuration > Unified Communications > Federated static routes ) for each chat node alias.

The chat node aliases are configured on Unified CM IM&P Administration ( Messaging > Group Chat Server Alias Mapping ).

Internal users do not need to use DNS to discover chat nodes; they get the chat room details from their local IM&P servers.

If you are using group chat over TLS, ensure that the Expressway-C and Expressway-E server certificate include in their list
                                                   of subject alternate names (using either XMPPAddress or DNS formats) all of the Chat Node Aliases that are configured on the
                                                   IM and Presence Service servers.

See "Chat configuration on IM and Presence" for more information about point-to-point instant messaging and group chat.

### Checking XMPP Federation Status

XMPP federation status information is available on the Expressway-E only.

You can go to Status > Unified Communications to check the primary status of the XMPP federation service.

Normally, XMPP Federation should be Active.

If there are problems with the service, such as connectivity issues with the Expressway-C, the status will show as Inactive . In this case, you should also review the Unified Communications status page on the associated Expressway- C for more guidance
                              as to what is causing the problem.

#### Viewing Federated Connections

To view the current federated connections being managed by the Expressway-E:

On the Expressway-E, go to Status > Unified Communications .

Click View federated connections in the Advanced status information section.

This shows all the current connections passing through that Expressway-E.

It displays the IP Address of the client, and the Direction ( Incoming or Outgoing ) of the communication.

Connections are closed after 10 minutes of inactivity.

In clustered systems:

An aggregated view is not displayed; only connections routed through the current peer are displayed.

In 2-way connections, the inbound and outbound communications may be managed by different peers.

### Troubleshooting External XMPP Federation

This section describes how to troubleshoot an external XMPP federation deployment and describes the impact of making configuration
                              changes on a live system.

#### Checking System Status

If you encounter issues with the XMPP federation status service, check the Status > Unified Communications page on both the Expressway-C and the Expressway-E. This will highlight any basic connection or configuration problem and
                                 provide information and links to help correct the problem.

#### General Configuration Checklist

Ensure that the following Expressway configuration items are specified correctly:

Port 5269 is open in both directions between the internet and Expressway-E in the DMZ.

DNS settings: host name, domain name and default DNS server ( System > DNS ).

An accessible NTP server ( System > Time ).

An active Unified Communications traversal zone on the Expressway-C and its associated Expressway-E ( Status > Zones ).

Unified Communications mode is set to Mobile and remote access on both the Expressway-C and the Expressway-E ( Configuration > Unified Communications > Configuration ).

XMPP federation support is On on the Expressway-E ( Configuration > Unified Communications > Configuration ).

If static routes are enabled, ensure that the appropriate routes for the federated XMPP domains have been added to the Expressway-E
                                       ( Configuration > Unified Communications > Federated static routes ).

At least one domain is configured on the Expressway-C with XMPP federation set to On ( Configuration > Domains ).

IM &Presence servers have been discovered on the Expressway-Cand have an active status ( Configuration > Unified Communications > IM and Presence servers ).

#### Discovery, Connectivity and Firewall Issues

Observe the following:

If using DNS lookup, check that _xmpp-server public DNS records exist for the domains and chat node aliases of all federated parties, and that they use port 5269.

Check that port 5269 is open in both directions between the internet and Expressway-E in the DMZ.

If the Expressway-C cannot connect to XCP on the Expressway-E remote host:

Check that the firewall has not blocked port 7400.

If the Expressway-E is running dual network interfaces, ensure that the traversal zone on the Expressway-C is connected to
                                             the internally-facing interface on the Expressway-E.

Be aware that inbound and outbound connections can be routed through different cluster peers.

If the address of an IM and Presence Service node has changed, or a new peer has been added to an IM and Presence Service
                                       cluster, go to Configuration > Unified Communications > IM and Presence Service nodes and click Refresh Servers . You must then save the updated configuration.

If an IM and Presence Service node fails over to a different node after an outage, the affected users are not dynamically moved to the other node . Expressway does not support this functionality, and it has not been tested.

#### Certificates and Secure TLS Connections

If you have configured secure TLS connections, ensure that:

Valid server certificates are installed, they are in date and not revoked.

Both the remote and local server certificates must contain a valid domain in the Subject Alternative Name (SAN). This applies
                                       even if Require client-side security certificates is disabled.

If Require client-side security certificates is enabled, ensure that the server certificate is signed by a CA and is not locally signed.

Certificate Authority (CA) certificates are installed.

If you are using group chat over TLS, ensure that the Expressway-C and Expressway-E server certificates include in their list
                                       of subject alternate names (using either XMPPAddress or DNS formats) all of the Chat Node Aliases that are configured on the IM and Presence servers.

Ensure that compatible security settings (TLS required, optional, no TLS) exist on your system and the remote federated system.

See Server Certificate Requirements for Unified Communications for more information.

#### Checking the Event Log

Check the Event Log on the Expressway-E for XMPP events.

Events related to XMPP federation are tagged with Module="XMPPFederation" . There are no XMPP-related logs on the Expressway-C.

#### Performing Diagnostic Logging

When performing diagnostic logging ( Maintenance > Diagnostics > Diagnostic logging ), set the develop.xcp.federation support log ( Maintenance > Diagnostics > Advanced > Support Log configuration ) to debug level.

#### Disabling Interdomain XMPP Federation on Unified CM IM&P

##### Before you begin

You must choose whether to enable Interdomain XMPP Federation on IM and Presence Service or on Expressway.

To disable Interdomain Federation on IM and Presence Service, perform the following operations in exactly the order shown:

Disable Interdomain Federation on the IM&P servers:

Go to Cisco Unified CM IM and Presence Administration > Presence > Inter Domain Federation > XMPP Federation > Settings .

Set XMPP Federation Node Status to Off .

Refresh the set of discovered IM&P servers on Expressway-C.

Restart all of the Unified CM IM&P XCP Router services that are connected to that Expressway-C.

#### Impact of Configuration Changes on a Live System

In general, we recommend that XMPP federation configuration changes are made "out of hours" . This section describes the impact that configuration changes will have on current clients using XMPP federation and any
                                 Jabber clients using mobile and remote access.

##### Expressway-C Configuration Changes

Domains

Any domain configuration changes, when one or more existing domains are configured for IM and Presence services on Unified CM or XMPP Federation will result in an automatic restart of the XCP router on both Expressway-C and Expressway-E.

The end-user impact is temporary loss of federation and any Jabber clients using mobile and remote access will be temporarily
                                    disconnected. The clients will automatically reconnect after a short period.

Unified Communications mode

Setting the Unified Communications mode to Off or to Jabber Guest services’ will stop the XCP router on both Expressway-C and Expressway-E.

This will remove the Expressway-E XMPP federation node from all discovered IM&P servers. A notification will appear on the
                                          IM&P administration interface to restart the XCP router on all affected IM&P nodes.

The end-user impact is that all IM&P sessions will be disconnected. That is, there is a loss of federation, IM&P sessions
                                          over mobile and remote access will be disconnected, and sessions directly homed on the IM&P node will be dropped. When the
                                          XCP router is restarted on each IM&P node, all XCP functionality on that node will be disrupted.

Discovered IM & Presence Servers

Adding or deleting an IM & Presence publisher will require a restart of the XCP router on each IM & Presence node associated
                                    with that publisher only if XMPP Federation is enabled.

This will cause a restart of the XCP router on Expressway-C.

The end-user impact should be minimal. They will be unable to send or receive IM & Presence updates for a few seconds.

##### Expressway-E Configuration Changes

Unified Communications Mode

Setting the Unified Communications mode to Off or to Jabber Guest services’ will stop the XCP router on both Expressway-C and Expressway-E.

This will remove the Expressway-E XMPP federation node from all discovered IM&P servers. A notification will appear on the
                                          IM&P administration interface to restart the XCP router on all affected IM&P nodes.

The end-user impact is that all IM&P sessions will be disconnected. That is, there is a loss of federation, IM&P sessions
                                          over mobile and remote access will be disconnected, and sessions directly homed on the IM&P node will be dropped. When the
                                          XCP router is restarted on each IM&P node, all XCP functionality on that node will be disrupted.

Turning the Unified Communications Mode back to On will reinsert the XMPP federation node and have the same impact on the IM&P servers.

XMPP Federation Support

Changing the XMPP federation support setting will restart the Expressway-E XCP router.

This will result in the addition/removal of the Expressway-E XMPP federation node from all discovered IM & Presence servers.
                                          A notification will appear on the IM&P administration interface to restart the XCP router on all affected IM&P nodes.

The end-user impact is that all IM&P sessions will be disconnected. That is, there is a loss of federation, IM&P sessions
                                          over mobile and remote access will be disconnected, and sessions directly homed on the IM&P node will be dropped. When the
                                          XCP router is restarted on each IM&P node, all XCP functionality on that node will be disrupted.

Other XMPP Federation Settings

Changing any of the other XMPP federation settings, such as static routes, security and privacy settings, or the allow/deny
                                    lists, will only result in a restart of the XMPP Federation Connection Manager service on the Expressway- E.

End-users may notice a temporary disruption to federation; any mobile and remote access IM&P sessions will remain connected.

##### Client Reconnection Times After Loss of Service

The time taken for a client to reconnect to the XMPP service depends on the re-login limits specified in the Cisco Server Recovery Manager service parameters on the IM&P server.

See the High Availability Client Login Profiles section in Configuration and Administration of IM and Presence Service on Cisco Unified Communications Manager for the IM&P version that you are running.

#### Temporary or Partial Loss of IM and Presence Service Federation

XMPP federation for IM and Presence Service via Expressway relies on a persistent TCP connection to the federated server.
                                 If a federated server becomes unavailable due to a graceful shutdown, Expressway will immediately seek to reestablish a connection
                                 with the federated server or with another server advertised by the federated partner.

If, however, the federated server fails abruptly, it can take up to 15 minutes for Expressway to discover the TCP connection
                                 outage and attempt reconnection. During this time, a partial or full loss of IM and Presence Service connectivity with the
                                 federated partner may occur.

| Note | This section describes XMPP federation as managed through Expressway, but it can also be managed through the IM and Presence
                                       Service, as described later in this guide. |
|---|---|

| Note | The Federated communications are available to both on-premises clients (connected directly to IM and Presence Service) and
                                                off-premises clients (connected to IM and Presence Service through MRA). |
|---|---|

| Note | The Expressway-C automatically includes the chat node aliases in its certificate signing requests (CSRs), providing it has
                                                discovered a set of IM and Presence Service servers. |
|---|---|

| Task | See |
|---|---|
| Validate email addresses for federation | XMPP Federation through Expressway |
| Ensure IM and Presence Service is operational and has XMPP federation turned off | XMPP Federation through Expressway |
| Complete Server Certificate Requirements | Server Certificate Requirements for Unified Communications |
| Configure the local domains for XMPP federation on Expressway-C | Configuring Expressway for External XMPP Federation |
| Configure Expressway-E for XMPP federation | Configuring Expressway for External XMPP Federation |
| Configure how XMPP servers for federated domains and chat node aliases are located using either DNS lookups or static routes | Configuring Expressway for External XMPP Federation |
| Configure the allow and deny lists for federated domains and chat node aliases | Configuring Expressway for External XMPP Federation |
| Publish DNS SRV records for XMPP federation (if not using static routes) | DNS SRV Records for XMPP Federation |
| Check that the correct firewall ports are open | See the Cisco Expressway IP Port Usage Configuration Guide , for your version, on the Cisco Expressway Series Configuration Guides page. |
| Check the status of XMPP federation | Checking XMPP Federation Status |
| To troubleshoot your connection | Troubleshooting External XMPP Federation |

| Add these items as subject alternative names | When generating a CSR for these purposes |
|---|---|
|  |  |  |
| Mobile and Remote Access | Jabber Guest | XMPP Federation | Business to Business Calls |
| Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified
                                             CM SIP registration domains) | Required on Expressway- E only | - | - | - |
| XMPP federation domains | - | - | Required on Expressway- E only | - |
| IM and Presence chat node aliases (federated group chat) | - | - | Required | - |
| Unified CM phone security profile names | Required on Expressway- E only | - | - | - |
| (Clustered systems only) Expressway cluster name | Required on Expressway- E only | Required on Expressway- E only | Required on Expressway- E only | - |

| Note | You may need to produce a new server certificate for the Expressway-C if chat node aliases are added or renamed. Or when IM
                                                   and Presence nodes are added or renamed, or new TLS phone security profiles are added. You must produce a new Expressway-E certificate if new chat node aliases are added to the system, or if the Unified CM or
                                                   XMPP federation domains are modified. You must restart the Expressway for any new uploaded server certificate to take effect. |
|---|---|

| Note | You can copy the list of chat node aliases from the equivalent Generate CSR page on the Expressway-C. |
|---|---|

| Step 1 | On Expressway-C, go to Configuration > Domains . |
|---|---|
| Step 2 | Click New (or click View/Edit if the required domain already exists). |
| Step 3 | Enter your local Domain name to be federated. |
| Step 4 | Set XMPP federation to On . |
| Step 5 | Click Save . |
| Step 6 | Repeat for any other local domains requiring federation. Note A single Expressway cluster can support multiple IM and Presence Service clusters using the same presence domain. XMPP federation of multiple IM and Presence Service clusters with multiple Expressway clusters is not supported. Each IM and Presence Service cluster needs to be discovered by Expressway-C. | Note | A single Expressway cluster can support multiple IM and Presence Service clusters using the same presence domain. XMPP federation of multiple IM and Presence Service clusters with multiple Expressway clusters is not supported. Each IM and Presence Service cluster needs to be discovered by Expressway-C. |
| Note | A single Expressway cluster can support multiple IM and Presence Service clusters using the same presence domain. XMPP federation of multiple IM and Presence Service clusters with multiple Expressway clusters is not supported. Each IM and Presence Service cluster needs to be discovered by Expressway-C. |

| Note | A single Expressway cluster can support multiple IM and Presence Service clusters using the same presence domain. XMPP federation of multiple IM and Presence Service clusters with multiple Expressway clusters is not supported. Each IM and Presence Service cluster needs to be discovered by Expressway-C. |
|---|---|

| Step 1 | On Expressway-E, go to Configuration > Unified Communications . |
|---|---|
| Step 2 | Set XMPP federation support to On . When you apply this change, you may need to restart the XCP Routers on the IM&P server(s). The other settings on this page
                                                do not require a restart. |
| Step 3 | Configure the remaining fields as described in the table below. |
| Step 4 | Click Save . Your changes are applied. If you toggled XMPP federation support , you will be required to confirm that you want to restart the XCP router on the Expressway-C. You may also need to restart the Unified CM IM&P XCP router services that are connected to the associated Expressway-C. |
| Step 5 | Log on to each IM and Presence server to check for notifications that you need to restart the XCP Routers. If you do need
                                             to restart them: In Cisco Unified IM and Presence Serviceability , go to Tools > Control Center - Network Services . Scroll down to the IM and Presence Services section and select Cisco XCP Router . Click Restart . This causes a restart of all XCP services on the IM and Presence Service. The service restart may take several minutes. Repeat on each IM and Presence server. You could use the utils service CLI option (accessed via the Cisco Unified IM and Presence Operating System) to restart the services instead. Table 1. Settings for XMPP Federation Settings Description Use static routes Indicates whether a controlled list of static routes are used to locate the federated XMPP domains and chat node aliases,
                                                            rather than DNS lookups. See Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located . Dialback secret Enter the dialback secret to use for identity verification with federated XMPP servers. If you have multiple Expressway-E
                                                            systems in the same deployment, they must all be configured with the same dialback secret. For more information about server dialback, see http://xmpp.org/extensions/xep-0220.html Security mode Indicates if a TLS connection to federated XMPP servers is required, preferred, or not required. TLS required : The system guarantees a secure (encrypted) connection with the foreign domain. TLS optional : The system attempts to establish a TLS connection with the foreign domain. If it fails to establish a TLS connection, it
                                                                  reverts to TCP. No TLS : The system will not establish a TLS connection with the foreign domain. It uses a non-encrypted connection to federate with
                                                                  the foreign domain. In all cases, server dialback is used to verify the identity of the foreign server. The foreign server must be configured
                                                            to use server dialback. Note SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. The default, and recommended setting, is TLS required . Require client-side security certificates Controls whether the certificate presented by the external client is verified against the Expressway's current trusted CA
                                                            list and, if loaded, the revocation list. This setting does not apply if Security mode is No TLS . Note The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. Privacy mode Controls whether restrictions are applied to the set of federated domains and chat node aliases. Off : No restrictions are applied. Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list. Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list. Note Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. The default is Allow list . See Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases . | Settings | Description | Use static routes | Indicates whether a controlled list of static routes are used to locate the federated XMPP domains and chat node aliases,
                                                            rather than DNS lookups. See Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located . | Dialback secret | Enter the dialback secret to use for identity verification with federated XMPP servers. If you have multiple Expressway-E
                                                            systems in the same deployment, they must all be configured with the same dialback secret. For more information about server dialback, see http://xmpp.org/extensions/xep-0220.html | Security mode | Indicates if a TLS connection to federated XMPP servers is required, preferred, or not required. TLS required : The system guarantees a secure (encrypted) connection with the foreign domain. TLS optional : The system attempts to establish a TLS connection with the foreign domain. If it fails to establish a TLS connection, it
                                                                  reverts to TCP. No TLS : The system will not establish a TLS connection with the foreign domain. It uses a non-encrypted connection to federate with
                                                                  the foreign domain. In all cases, server dialback is used to verify the identity of the foreign server. The foreign server must be configured
                                                            to use server dialback. Note SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. The default, and recommended setting, is TLS required . | Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. | Require client-side security certificates | Controls whether the certificate presented by the external client is verified against the Expressway's current trusted CA
                                                            list and, if loaded, the revocation list. This setting does not apply if Security mode is No TLS . Note The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. | Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. | Privacy mode | Controls whether restrictions are applied to the set of federated domains and chat node aliases. Off : No restrictions are applied. Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list. Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list. Note Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. The default is Allow list . See Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases . | Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |
| Settings | Description |
| Use static routes | Indicates whether a controlled list of static routes are used to locate the federated XMPP domains and chat node aliases,
                                                            rather than DNS lookups. See Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located . |
| Dialback secret | Enter the dialback secret to use for identity verification with federated XMPP servers. If you have multiple Expressway-E
                                                            systems in the same deployment, they must all be configured with the same dialback secret. For more information about server dialback, see http://xmpp.org/extensions/xep-0220.html |
| Security mode | Indicates if a TLS connection to federated XMPP servers is required, preferred, or not required. TLS required : The system guarantees a secure (encrypted) connection with the foreign domain. TLS optional : The system attempts to establish a TLS connection with the foreign domain. If it fails to establish a TLS connection, it
                                                                  reverts to TCP. No TLS : The system will not establish a TLS connection with the foreign domain. It uses a non-encrypted connection to federate with
                                                                  the foreign domain. In all cases, server dialback is used to verify the identity of the foreign server. The foreign server must be configured
                                                            to use server dialback. Note SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. The default, and recommended setting, is TLS required . | Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. |
| Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. |
| Require client-side security certificates | Controls whether the certificate presented by the external client is verified against the Expressway's current trusted CA
                                                            list and, if loaded, the revocation list. This setting does not apply if Security mode is No TLS . Note The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. | Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. |
| Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. |
| Privacy mode | Controls whether restrictions are applied to the set of federated domains and chat node aliases. Off : No restrictions are applied. Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list. Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list. Note Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. The default is Allow list . See Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases . | Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |
| Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |

| Settings | Description |
|---|---|
| Use static routes | Indicates whether a controlled list of static routes are used to locate the federated XMPP domains and chat node aliases,
                                                            rather than DNS lookups. See Configuring How XMPP Servers for Federated Domains and Chat Node Aliases Are Located . |
| Dialback secret | Enter the dialback secret to use for identity verification with federated XMPP servers. If you have multiple Expressway-E
                                                            systems in the same deployment, they must all be configured with the same dialback secret. For more information about server dialback, see http://xmpp.org/extensions/xep-0220.html |
| Security mode | Indicates if a TLS connection to federated XMPP servers is required, preferred, or not required. TLS required : The system guarantees a secure (encrypted) connection with the foreign domain. TLS optional : The system attempts to establish a TLS connection with the foreign domain. If it fails to establish a TLS connection, it
                                                                  reverts to TCP. No TLS : The system will not establish a TLS connection with the foreign domain. It uses a non-encrypted connection to federate with
                                                                  the foreign domain. In all cases, server dialback is used to verify the identity of the foreign server. The foreign server must be configured
                                                            to use server dialback. Note SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. The default, and recommended setting, is TLS required . | Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. |
| Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. |
| Require client-side security certificates | Controls whether the certificate presented by the external client is verified against the Expressway's current trusted CA
                                                            list and, if loaded, the revocation list. This setting does not apply if Security mode is No TLS . Note The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. | Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. |
| Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. |
| Privacy mode | Controls whether restrictions are applied to the set of federated domains and chat node aliases. Off : No restrictions are applied. Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list. Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list. Note Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. The default is Allow list . See Configuring the Allow and Deny Lists for Federated Domains and Chat Node Aliases . | Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |
| Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |

| Note | SASL External is not a supported configuration on the local server. Foreign servers may be configured to use SASL, but SASL
                                                                        exchanges will not be supported by the local server. |
|---|---|

| Note | The federated domain name and any chat node aliases must be present in the certificate's subject alternate name, regardless
                                                                        of this setting. |
|---|---|

| Note | Any domains or chat node aliases that are configured as static routes are included automatically in the allow list. |
|---|---|

| Step 1 | On Expressway-E, go to Configuration > Unified Communications . |
|---|---|
| Step 2 | Set Use static routes to Off . |
| Step 3 | Click Save . Note All XMPP federated partners must publish in DNS the addresses of their XMPP servers as described in DNS SRV Records for XMPP Federation . | Note | All XMPP federated partners must publish in DNS the addresses of their XMPP servers as described in DNS SRV Records for XMPP Federation . |
| Note | All XMPP federated partners must publish in DNS the addresses of their XMPP servers as described in DNS SRV Records for XMPP Federation . |

| Note | All XMPP federated partners must publish in DNS the addresses of their XMPP servers as described in DNS SRV Records for XMPP Federation . |
|---|---|

| Step 1 | Contact the partners with whom you are federating to get a list of their chat node aliases. |
|---|---|
| Step 2 | On Expressway-E, go to Configuration > Unified Communications . |
| Step 3 | Set Use static routes to On and click Save . |
| Step 4 | Click Configure static routes for federated XMPP domains . |
| Step 5 | On the Federated static routes page, click New . |
| Step 6 | Enter the details of the static route: Field Description Domain The federated XMPP domain or chat node alias. Address The IP address or Fully Qualified Domain Name (FQDN) of an XMPP server for this federated domain or chat node alias. | Field | Description | Domain | The federated XMPP domain or chat node alias. | Address | The IP address or Fully Qualified Domain Name (FQDN) of an XMPP server for this federated domain or chat node alias. |
| Field | Description |
| Domain | The federated XMPP domain or chat node alias. |
| Address | The IP address or Fully Qualified Domain Name (FQDN) of an XMPP server for this federated domain or chat node alias. |
| Step 7 | Click Save . |
| Step 8 | Add as many additional static routes as required. You can specify additional routes to alternative addresses for the same domain or chat node alias (all routes have an equal
                                                   priority). Note If there are no static routes defined for a federated domain or chat node alias, the system will use DNS instead. If static routes are defined for the federated domain or chat node alias, but the remote system cannot be contacted over those
                                                                     routes, the system will not fall back to DNS. If Privacy mode is set to Allow list and Use static routes is On , any domains (or chat node aliases) that are configured as static routes are included automatically in the allow list. | Note | If there are no static routes defined for a federated domain or chat node alias, the system will use DNS instead. If static routes are defined for the federated domain or chat node alias, but the remote system cannot be contacted over those
                                                                     routes, the system will not fall back to DNS. If Privacy mode is set to Allow list and Use static routes is On , any domains (or chat node aliases) that are configured as static routes are included automatically in the allow list. |
| Note | If there are no static routes defined for a federated domain or chat node alias, the system will use DNS instead. If static routes are defined for the federated domain or chat node alias, but the remote system cannot be contacted over those
                                                                     routes, the system will not fall back to DNS. If Privacy mode is set to Allow list and Use static routes is On , any domains (or chat node aliases) that are configured as static routes are included automatically in the allow list. |

| Field | Description |
|---|---|
| Domain | The federated XMPP domain or chat node alias. |
| Address | The IP address or Fully Qualified Domain Name (FQDN) of an XMPP server for this federated domain or chat node alias. |

| Note | If there are no static routes defined for a federated domain or chat node alias, the system will use DNS instead. If static routes are defined for the federated domain or chat node alias, but the remote system cannot be contacted over those
                                                                     routes, the system will not fall back to DNS. If Privacy mode is set to Allow list and Use static routes is On , any domains (or chat node aliases) that are configured as static routes are included automatically in the allow list. |
|---|---|

| Step 1 | On Expressway-E, go to Configuration > Unified Communications . |
|---|---|
| Step 2 | Set Privacy mode as appropriate: Off : No restrictions are applied. Allow list : Federation is allowed only with the domains and chat node aliases specified in the allow list. Deny list : Federation is allowed with any domain or chat node alias except for those specified in the deny list. |
| Step 3 | Click Save . |
| Step 4 | To manage the domains and chat node aliases in the allow or deny lists, click either Federation allow list or Federation deny list as appropriate. In the resulting page you can add, modify, or delete the items in the allow/deny list. Wildcards or regexes are not allowed
                                                in the names; it must be an exact match. Note All domains and chat node aliases that are configured as static routes are included automatically in the allow list. | Note | All domains and chat node aliases that are configured as static routes are included automatically in the allow list. |
| Note | All domains and chat node aliases that are configured as static routes are included automatically in the allow list. |

| Note | All domains and chat node aliases that are configured as static routes are included automatically in the allow list. |
|---|---|

| Note | In multitenant mode, you must configure the system hostname on the System > DNS page of the Cisco Expressway-E to match the hostname configured in DNS (case-specific before X8.10.1, case insensitive from
                                          X8.10.1). Otherwise Cisco Jabber clients will be unable to register successfully for MRA. |
|---|---|

| Note | Without the delayed restart feature enabled, the restart happens automatically and occurs each time you save any configuration
                                          change that affects the Cisco XCP Router. If multiple configuration changes are required, resulting in several restarts of
                                          the Cisco XCP Router, it can adversely affect users. We strongly recommend that multitenant customers enable the delayed Cisco
                                          XCP Router restart feature. |
|---|---|

| Note | Nodes on the latest configuration are not impacted. This action disconnects all external XCP-based users connected through
                                                the delayed nodes during the restart. All nodes will be on the latest configuration after the restart. |
|---|---|

| Important | More information about multitenancy, see Multitenancy with Cisco Expressway on the Cisco Hosted Collaboration Solution page. |
|---|---|

| Step 1 | Go to Configuration > Unified Communications > Delayed Cisco XCP Router restart . |
|---|---|
| Step 2 | Under Configuration , turn Delayed Cisco XCP Router restart On . |
| Step 3 | If you do not enable Scheduled Restart, you must initiate the restart manually using the Restar t button. Configuration changes do not happen automatically. |

| Step 1 | Under Configuration , turn Scheduled Restart On and set the time that all nodes in the multi-tenant Expressway-E cluster are updated each day. Only nodes that are not running
                                                on the latest configuration are impacted. |
|---|---|
| Step 2 | Set the time that the restart takes place each day using the Scheduled restart time (UTC) option. |

| Important | More information about configuration changes, see Impact of Configuration Changes on a Live System in the Cisco Unified Communications XMPP Federation guide. |
|---|---|

| Domain | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| ciscoexample.com | xmpp-server | tcp | 0 | 0 | 5269 | expe.ciscoexample.com |

| Domain | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| federated.com | xmpp-server | tcp | 0 | 0 | 5269 | xmppserver.federated.com |

| Domain | Service | Protocol | Priority | Weight | Port | Target host |
|---|---|---|---|---|---|---|
| chatroom1.example.com | xmpp-server | tcp | 0 | 0 | 5269 | expe.ciscoexample.com |

| Note | The chat node aliases are configured on Unified CM IM&P Administration ( Messaging > Group Chat Server Alias Mapping ). Internal users do not need to use DNS to discover chat nodes; they get the chat room details from their local IM&P servers. If you are using group chat over TLS, ensure that the Expressway-C and Expressway-E server certificate include in their list
                                                   of subject alternate names (using either XMPPAddress or DNS formats) all of the Chat Node Aliases that are configured on the
                                                   IM and Presence Service servers. |
|---|---|

| Step 1 | On the Expressway-E, go to Status > Unified Communications . |
|---|---|
| Step 2 | Click View federated connections in the Advanced status information section. This shows all the current connections passing through that Expressway-E. It displays the IP Address of the client, and the Direction ( Incoming or Outgoing ) of the communication. Connections are closed after 10 minutes of inactivity. Note In clustered systems: An aggregated view is not displayed; only connections routed through the current peer are displayed. In 2-way connections, the inbound and outbound communications may be managed by different peers. | Note | In clustered systems: An aggregated view is not displayed; only connections routed through the current peer are displayed. In 2-way connections, the inbound and outbound communications may be managed by different peers. |
| Note | In clustered systems: An aggregated view is not displayed; only connections routed through the current peer are displayed. In 2-way connections, the inbound and outbound communications may be managed by different peers. |

| Note | In clustered systems: An aggregated view is not displayed; only connections routed through the current peer are displayed. In 2-way connections, the inbound and outbound communications may be managed by different peers. |
|---|---|

| Step 1 | Disable Interdomain Federation on the IM&P servers: Go to Cisco Unified CM IM and Presence Administration > Presence > Inter Domain Federation > XMPP Federation > Settings . Set XMPP Federation Node Status to Off . |
|---|---|
| Step 2 | Refresh the set of discovered IM&P servers on Expressway-C. |
| Step 3 | Restart all of the Unified CM IM&P XCP Router services that are connected to that Expressway-C. |

| Note | Turning the Unified Communications Mode back to On will reinsert the XMPP federation node and have the same impact on the IM&P servers. |
|---|---|