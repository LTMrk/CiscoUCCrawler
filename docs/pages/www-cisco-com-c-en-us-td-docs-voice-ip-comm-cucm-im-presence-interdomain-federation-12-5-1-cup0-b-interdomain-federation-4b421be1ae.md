---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-12-5-1-cup0-b-interdomain-federation-4b421be1ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/12_5_1/cup0_b_interdomain-federation-1251/cup0_b_interdomain-federation-1251_chapter_01100.html
retrieved_at: 2026-08-16T17:22:24.390680+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

# Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2024

Chapter: Load Balancer Configuration for Redundancy for SIP Federation

## Chapter: Load Balancer Configuration for Redundancy for SIP Federation

# Load Balancer Configuration for Redundancy for SIP Federation

This section explains the Load Balancer Configuration for Redundancy for SIP Federation.

## About the Load Balancer

For redundancy and high availability purposes, you can incorporate a load balancer into the federated network. The load balancer
                              is placed between the IM and Presence Service node and the Cisco Adaptive Security Appliance (see High Availability for SIP Federation ).

The load balancer terminates incoming TLS connections from Cisco Adaptive Security Appliance and initiates a new TLS connection to route the content to the appropriate backend IM and Presence Service node.

## IM and Presence Service Node Updates

When using a load balancer for redundancy, you must update settings on the IM and Presence Service publisher and subscriber nodes.

Task

Update the federation routing parameter

Log in to Cisco Unified IM and Presence
                                             										Administration , choose System > Service Parameters > Cisco SIP Proxy from the Service menu and enter these values:

Virtual IP Address - enter the virtual IP address
                                                											set on the load balancer

Server Name - set to the FQDN of the load
                                                      												balancer

Federation Routing IM and Presence Service
                                                         												FQDN - set to the FQDN of the load balancer.

Create a new TLS peer subject

Log in to Cisco Unified IM and Presence
                                                   												Administration, choose System > Security > TLS Peer Subjects .

Click Add New and enter these
                                                											values:

Peer Subject Name - enter the external
                                                      												FQDN of the load balancer

Description - enter the name of the load
                                                      												balancer

Add the TLS peer to the TLS peer subjects list

Log in to Cisco Unified IM and Presence
                                                   												Administration , choose System > Security > TLS Context Configuration .

Click Find .

Click Default_Cisco_UPS_SIP_Proxy_Peer_Auth_TLS_Context .

Move the load balancer federation-TLS peer subject for
                                                											the load balancer to the TLS peer subjects list.

## Cisco Adaptive Security Appliance Updates

When using a load balancer, the external domain still sends messages to the public IM and Presence Service address, but the Cisco Adaptive Security Appliance maps that address to a virtual IP address on the load balancer. Thus, when the Cisco Adaptive Security Appliance receives messages from the external domain, it forwards it to the load balancer. The load balancer then passes it on to the
                              appropriate IM and Presence Service nodes.

To support this configuration, you must make some changes to the Cisco Adaptive Security Appliance .

### Static PAT Message Updates

You must update the static PAT messages to include the load balancer details.

Task

Cisco Adaptive Security Appliance Release 8.2 Command

Cisco Adaptive Security Appliance Release 8.3 Command

Changes Required for the IM and Presence Service Publisher

Change the static PAT to use an arbitrary, unused port for the public IM and Presence Service address.

Change:

static 
                                                   (inside,outside) tcp public_imp_ip_address 
                                                   5061 routing_imp_private_ip_address 
                                                   5062 netmask 255.255.255.255

to:

static (inside,outside) 
                                                   tcp public_imp_ip_address 55061 routing_imp_publisher_ private_ip_address 5062 netmask 255.255.255.255

Change:

object service obj_tcp_source_eq_5061 # service 
                                                   tcp source eq 5061

nat (inside,outside) 
                                                   source static obj_host_routing_imp_private_ip_address obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_5061

to

object service obj_tcp_source_eq_55061 # service tcp source eq 55061

nat (inside,outside) 
                                                   source static obj_host_routing_imp_private_ip_address 
                                                   obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_55061

Add a new static PAT to allow messages sent to the public IM and Presence Service address to be forwarded to the virtual port address (on whichever port the load balancer is listening for TLS messages).

static (inside,outside) 
                                                   tcp public_imp_address 5061 load_balancer_vip 5062 netmask 255.255.255.255

object network obj_host_load_balancer_vip # host routing_imp_private_address

object service obj_tcp_source_eq_5061 # service tcp source eq 5061

nat (inside,outside) 
                                                   source static obj_host_load_balancer_vip 
                                                   obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_5061

Changes Required for IM and Presence Service Subscriber

Add a new access list for the load balancer virtual IP address. You must add an access list for each external domain that IM and Presence Service needs to access.

access-list ent_lber_to_external_ocs extended 
                                                   permit tcp host subscriber_private_ip_address host external_domain_public_ip_address 5061

access-list ent_lcs_to_lber_routg_imp extended 
                                                   permit tcp host external_domain_public_ip_address host imp_public_ip_address 65061

Add a new access list for a extended permit tcp hos external domain to initiate messages to a IM and Presence Service server when the load balancer virtual IP address is in place. You must add an access list for each external domain that
                                             needs to access IM and Presence Service .

### Access List Updates

To support the load balancer, you also need to update the access lists on the Cisco Adaptive Security Appliance specific to your deployment scenario.

The IM and Presence Service public IP address refers to the public IP address of the IM and Presence Service domain as configured on the Cisco Adaptive Security Appliance , and as it appears in the DNS record. This record shows the FQDN of the load balancer containing the public IP of the Cisco Adaptive Security Appliance .

Procedures

Deployment Scenario: An IM and Presence Service node federating with one or more external domains

Task

Configuration Example

Add a new access list for the new load balancer virtual IP address. You must add an access list for each external domain that IM and Presence Service needs to access.

Publisher:

Cisco Adaptive Security Appliance Release 8.2 and 8.3 Command:

access-list ent_lber_to_external_ocs extended permit tcp host virtual_IP_address host external_domain_public_ip_address eq 5061

Add a new access list for an external domain to initiate messages to a IM and Presence Service node when the load balancer virtual IP address is in place. You must add an access list for each external domain that needs
                                             to access IM and Presence Service .

Publisher:

Cisco Adaptive Security Appliance Release 8.2 Command:

access-list ent_lcs_to_lber_routgimp extended permit tcp host external_domain_public_ip_address host imp_public_ip_address eq 5062

Cisco Adaptive Security Appliance Release 8.3 Command:

access-list ent_external_server_to_lb extended permit tcp host external_public_address host loadbalancer_virtual_ip_address eq
                                                   5062

For each access list, add a new class to incorporate the new access list.

class ent_lber_to_external_ocs match access-list ent_lber_to_external_ocs

For each class, make an entry in the policy-map global_policy for messages initiated by the IM and Presence Service .

policy-map global_policy class ent_lber_to_external_ocs inspect sip sip_inspect tls-proxy ent_imp_to_external

For each class, make an entry in the policy-map global_policy for messages initiated on an external domain.

policy-map global_policy class ent_lcs_to_lber_routgimp inspect sip sip_inspect tls-proxy ent_external_to_imp

Deployment Scenario: IM and Presence Service to IM and Presence Service Federation, where the external domain has added one or more intercluster IM and Presence Service nodes

Task

Configuration Example

The external domain Adaptive Security Appliance must allow access to the arbitrary ports that were selected for our local domain publisher and subscriber.

access-list ent_imp_to_externalPubimpwlber extended permit tcp host external_domain_private_imp_address host public_imp_address_local_domain 55061

access-list ent_imp_to_externalSubimpwlber extended permit tcp host external_domain_private_imp_address host public_imp_address_local_domain  65061

For each access list, add a new class to incorporate the new access list.

--

For each class, make an entry in the policy-map global_policy.

--

Related Information -

Access List Configuration Requirements

### TLS Proxy Instance Updates

Update the TLS proxy instances on the Cisco Adaptive Security Appliance .

Change:

tls-proxy ent_external_to_imp server trust-point msoft_public_fqdn

client trust-point imp_proxy

client cipher-suite aes128-sha1 aes256-sha1 3des-sha1 null-sha1

tls-proxy ent_imp_to_external

server trust-point imp_proxy

client trust-point msoft_public_fqdn

client cipher-suite aes128-sha1 aes256-sha1 3des-sha1 null-sha1

to:

tls-proxy ent_external_to_imp server trust-point msoft_public_fqdn

client trust-point msoft_public_fqdn

client cipher-suite aes128-sha1 aes256-sha1 3des-sha1 null-sha1

tls-proxy ent_imp_to_external

server trust-point msoft_public_fqdn

client trust-point msoft_public_fqdn

client cipher-suite aes128-sha1 aes256-sha1 3des-sha1 null-sha1

## CA-Signed Security Certificate Updates

When adding the load balancer to the configuration, you must also generate CA-signed security certificates between the load
                              balancer, the Cisco Adaptive Security Appliance , and the IM and Presence Service node as described in these sections:

### Security Certificate Configuration Between the Load Balancer and Cisco Adaptive Security Appliance

This topic provides an overview of the required steps for configuring the security certificate between the load balancer and
                                 the Cisco Adaptive Security Appliance .

Task

Generate CA-signed certificate for the load balancer on the Cisco Adaptive Security Appliance .

Use the crypto ca enroll command and specify the FQDN of the load balancer.

Import the CA-signed certificate from the Cisco Adaptive Security Appliance to the load balancer.

Refer to your load balancer documentation.

Generate a CA-signed certificate for the Cisco Adaptive Security Appliance on the load balancer.

Refer to your load balancer documentation.

Import the CA-signed certificate from the load balancer to the Cisco Adaptive Security Appliance .

Use the crypto ca trustpoint command.

To verify that the certificate was imported, use the show crypto ca certificate command.

Related Information -

Configure a Certificate on the Cisco Adaptive Security Appliance Using SCEP

Import an IM and Presence Service Certificate into the Cisco Adaptive Security Appliance

Security Certificate Exchange Between Cisco Adaptive Security Appliance and Microsoft Access Edge (External Interface) with
                                    Microsoft CA

### Security Certificate Configuration Between the Load Balancer and IM and Presence Service Node

This topic provides an overview of the required steps for configuring the security certificate between the load balancer and
                                 the IM and Presence Service nodes.

Task

Generate a CA-signed certificate on both the publisher and subscriber nodes.

Follow the instructions to exchange certificates using CA-signed certificates.

Import the CA-signed certificates (from the publisher and subscriber nodes) to the load balancer

Refer to your load balancer documentation.

## Microsoft Component Updates

You must update some Microsoft components with the load
                              		  balancer details.

Task

Update all instances of the FQDN to correspond to
                                          						the load balancer FQDN.

Update the domain name in the IM Provider list
                                          						with the load balancer.

On the external Access Edge server, choose Start > Administrative
                                                      								  Tools > Computer Management .

In the left pane, right-click Microsoft Office Communications Server
                                                   								2007 .

Click the IM Provider tab.

Click Add .

Check 
                                                							 the check box for Allow the IM service provider .

Define the network address of the IM service
                                          						provider as the public FQDN of the load balancer

| Task | Procedure |
|---|---|
| Update the federation routing parameter | Log in to Cisco Unified IM and Presence
                                             										Administration , choose System > Service Parameters > Cisco SIP Proxy from the Service menu and enter these values: Virtual IP Address - enter the virtual IP address
                                                											set on the load balancer Server Name - set to the FQDN of the load
                                                      												balancer Federation Routing IM and Presence Service
                                                         												FQDN - set to the FQDN of the load balancer. |
| Create a new TLS peer subject | Log in to Cisco Unified IM and Presence
                                                   												Administration, choose System > Security > TLS Peer Subjects . Click Add New and enter these
                                                											values: Peer Subject Name - enter the external
                                                      												FQDN of the load balancer Description - enter the name of the load
                                                      												balancer |
| Add the TLS peer to the TLS peer subjects list | Log in to Cisco Unified IM and Presence
                                                   												Administration , choose System > Security > TLS Context Configuration . Click Find . Click Default_Cisco_UPS_SIP_Proxy_Peer_Auth_TLS_Context . Move the load balancer federation-TLS peer subject for
                                                											the load balancer to the TLS peer subjects list. |

| Task | Cisco Adaptive Security Appliance Release 8.2 Command | Cisco Adaptive Security Appliance Release 8.3 Command |
|---|---|---|
| Changes Required for the IM and Presence Service Publisher |  |
| Change the static PAT to use an arbitrary, unused port for the public IM and Presence Service address. | Change: static 
                                                   (inside,outside) tcp public_imp_ip_address 
                                                   5061 routing_imp_private_ip_address 
                                                   5062 netmask 255.255.255.255 to: static (inside,outside) 
                                                   tcp public_imp_ip_address 55061 routing_imp_publisher_ private_ip_address 5062 netmask 255.255.255.255 | Change: object service obj_tcp_source_eq_5061 # service 
                                                   tcp source eq 5061 nat (inside,outside) 
                                                   source static obj_host_routing_imp_private_ip_address obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_5061 to object service obj_tcp_source_eq_55061 # service tcp source eq 55061 nat (inside,outside) 
                                                   source static obj_host_routing_imp_private_ip_address 
                                                   obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_55061 |
| Add a new static PAT to allow messages sent to the public IM and Presence Service address to be forwarded to the virtual port address (on whichever port the load balancer is listening for TLS messages). | static (inside,outside) 
                                                   tcp public_imp_address 5061 load_balancer_vip 5062 netmask 255.255.255.255 | object network obj_host_load_balancer_vip # host routing_imp_private_address object service obj_tcp_source_eq_5061 # service tcp source eq 5061 nat (inside,outside) 
                                                   source static obj_host_load_balancer_vip 
                                                   obj_host_public_imp_ip_address service obj_tcp_source_eq_5062
                                                   obj_tcp_source_eq_5061 |
| Changes Required for IM and Presence Service Subscriber |
| Add a new access list for the load balancer virtual IP address. You must add an access list for each external domain that IM and Presence Service needs to access. | access-list ent_lber_to_external_ocs extended 
                                                   permit tcp host subscriber_private_ip_address host external_domain_public_ip_address 5061 access-list ent_lcs_to_lber_routg_imp extended 
                                                   permit tcp host external_domain_public_ip_address host imp_public_ip_address 65061 |
| Add a new access list for a extended permit tcp hos external domain to initiate messages to a IM and Presence Service server when the load balancer virtual IP address is in place. You must add an access list for each external domain that
                                             needs to access IM and Presence Service . |

| Note | The IM and Presence Service public IP address refers to the public IP address of the IM and Presence Service domain as configured on the Cisco Adaptive Security Appliance , and as it appears in the DNS record. This record shows the FQDN of the load balancer containing the public IP of the Cisco Adaptive Security Appliance . |
|---|---|

| Task | Configuration Example |
|---|---|
| Add a new access list for the new load balancer virtual IP address. You must add an access list for each external domain that IM and Presence Service needs to access. | Publisher: Cisco Adaptive Security Appliance Release 8.2 and 8.3 Command: access-list ent_lber_to_external_ocs extended permit tcp host virtual_IP_address host external_domain_public_ip_address eq 5061 |
| Add a new access list for an external domain to initiate messages to a IM and Presence Service node when the load balancer virtual IP address is in place. You must add an access list for each external domain that needs
                                             to access IM and Presence Service . | Publisher: Cisco Adaptive Security Appliance Release 8.2 Command: access-list ent_lcs_to_lber_routgimp extended permit tcp host external_domain_public_ip_address host imp_public_ip_address eq 5062 Cisco Adaptive Security Appliance Release 8.3 Command: access-list ent_external_server_to_lb extended permit tcp host external_public_address host loadbalancer_virtual_ip_address eq
                                                   5062 |
| For each access list, add a new class to incorporate the new access list. | class ent_lber_to_external_ocs match access-list ent_lber_to_external_ocs |
| For each class, make an entry in the policy-map global_policy for messages initiated by the IM and Presence Service . | policy-map global_policy class ent_lber_to_external_ocs inspect sip sip_inspect tls-proxy ent_imp_to_external |
| For each class, make an entry in the policy-map global_policy for messages initiated on an external domain. | policy-map global_policy class ent_lcs_to_lber_routgimp inspect sip sip_inspect tls-proxy ent_external_to_imp |

| Task | Configuration Example |
|---|---|
| The external domain Adaptive Security Appliance must allow access to the arbitrary ports that were selected for our local domain publisher and subscriber. | access-list ent_imp_to_externalPubimpwlber extended permit tcp host external_domain_private_imp_address host public_imp_address_local_domain 55061 access-list ent_imp_to_externalSubimpwlber extended permit tcp host external_domain_private_imp_address host public_imp_address_local_domain  65061 |
| For each access list, add a new class to incorporate the new access list. | -- |
| For each class, make an entry in the policy-map global_policy. | -- |

| Task | Procedure |
|---|---|
| Generate CA-signed certificate for the load balancer on the Cisco Adaptive Security Appliance . | Use the crypto ca enroll command and specify the FQDN of the load balancer. |
| Import the CA-signed certificate from the Cisco Adaptive Security Appliance to the load balancer. | Refer to your load balancer documentation. |
| Generate a CA-signed certificate for the Cisco Adaptive Security Appliance on the load balancer. | Refer to your load balancer documentation. |
| Import the CA-signed certificate from the load balancer to the Cisco Adaptive Security Appliance . | Use the crypto ca trustpoint command. To verify that the certificate was imported, use the show crypto ca certificate command. |

| Task | Procedure |
|---|---|
| Generate a CA-signed certificate on both the publisher and subscriber nodes. | Follow the instructions to exchange certificates using CA-signed certificates. |
| Import the CA-signed certificates (from the publisher and subscriber nodes) to the load balancer | Refer to your load balancer documentation. |

| Task | Procedure |
|---|---|
| Update all instances of the FQDN to correspond to
                                          						the load balancer FQDN. |  |
| Update the domain name in the IM Provider list
                                          						with the load balancer. | On the external Access Edge server, choose Start > Administrative
                                                      								  Tools > Computer Management . In the left pane, right-click Microsoft Office Communications Server
                                                   								2007 . Click the IM Provider tab. Click Add . Check 
                                                							 the check box for Allow the IM service provider . Define the network address of the IM service
                                          						provider as the public FQDN of the load balancer |