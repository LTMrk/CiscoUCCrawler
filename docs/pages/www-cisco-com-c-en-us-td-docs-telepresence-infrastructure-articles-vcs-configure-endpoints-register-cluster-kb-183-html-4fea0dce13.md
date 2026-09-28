---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-infrastructure-articles-vcs-configure-endpoints-register-cluster-kb-183-html-4fea0dce13
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/infrastructure/articles/vcs_configure_endpoints_register_cluster_kb_183.html
retrieved_at: 2026-08-21T12:30:38.641417+00:00
---

Cisco TelePresence Video Communication Server (VCS) Configuring endpoints to register to a cluster of Cisco VCSs

# Cisco TelePresence Video Communication Server (VCS)

## Configuring endpoints to register to a cluster of Cisco VCSs

### Configuring endpoints to register to a cluster of Cisco TelePresence Video Communication Servers (Cisco VCSs)

When your Cisco VCS is configured as part of a cluster with one or more peers
(also known as Alternates), endpoints need to be able to reach the
other peers if their primary Cisco VCS becomes unavailable. The H.323
protocol supports this failover re-registration process automatically,
but SIP does not.

The way in which you should configure your endpoints and DNS records
depends on the protocol and the functionality supported by your
endpoints.

#### Initial registration process (SIP and H.323 endpoints)

In order of preference, for providing resilience of connectivity of endpoints to a cluster of Cisco VCSs, you are
recommended to use the following registration methods for SIP and H.323
endpoints:

- SIP Outbound : (SIP only)
from software version X6, the Cisco VCS supports "SIP Outbound" (RFC 5626). This allows endpoints that support SIP Outbound to register and maintain connections to multiple peers.

- DNS SRV records :
if the endpoint supports DNS SRV, set up a DNS SRV record for the
DNS name of the cluster, giving each cluster peer an equal weighting
and priority. The endpoint should be configured with the DNS name
of the cluster. On startup the endpoint issues a DNS SRV request and
receives back the addresses of each cluster peer. It will then try
and register with each peer in turn.

- DNS round-robin :
if the endpoint does not support DNS SRV, set up a DNS
A-record for the DNS name of the cluster and configure it to
supply a round-robin list of IP addresses for each cluster
peer. The endpoint should be configured with the DNS name of the
cluster. On startup the endpoint performs a DNS A-record lookup
and receives back an address of a peer taken from the round-robin list.
The endpoint will try and register with that peer. If that peer is not
available, the endpoint performs another DNS lookup and
the server will respond with the next peer in the list. This
is repeated until the endpoint registers with a Cisco VCS.

- Static IP address :
if the cluster does not have a DNS name, configure the endpoint with
the IP address of one of the peers. On startup the endpoint will try
and register with the Cisco VCS at that address. If the Cisco VCS does not respond,
the endpoint will continue trying that same address at regular
intervals.

H.323 endpoints: connection failures

SIP endpoints: connection failures

How SIP endpoints behave if they lose connection to their primary Cisco VCS depends on their initial registration method:

- SIP Outbound : the endpoint will use one of its other connections.

- DNS SRV records : the endpoint uses the DNS SRV entry to find a new Cisco VCS to re-register to.

- DNS round-robin : the endpoint performs another DNS lookup to
find a new Cisco VCS to re-register to (the DNS server providing the next Cisco VCS peer in the
round-robin sequence).

- Static IP address : the endpoint will keep trying to register to that same Cisco VCS until it is accessible again.

For more detailed information about configuring endpoints to work with a Cisco VCS cluster,
refer to the "Cluster Creation and Maintenance" Deployment Guide (document number D14367).

#### This article applies to the following products:

- Cisco Video Communication Server

|  | Configuring endpoints to register to a cluster of Cisco TelePresence Video Communication Servers (Cisco VCSs) When your Cisco VCS is configured as part of a cluster with one or more peers
(also known as Alternates), endpoints need to be able to reach the
other peers if their primary Cisco VCS becomes unavailable. The H.323
protocol supports this failover re-registration process automatically,
but SIP does not. The way in which you should configure your endpoints and DNS records
depends on the protocol and the functionality supported by your
endpoints. Initial registration process (SIP and H.323 endpoints) In order of preference, for providing resilience of connectivity of endpoints to a cluster of Cisco VCSs, you are
recommended to use the following registration methods for SIP and H.323
endpoints: SIP Outbound : (SIP only)
from software version X6, the Cisco VCS supports "SIP Outbound" (RFC 5626). This allows endpoints that support SIP Outbound to register and maintain connections to multiple peers. DNS SRV records :
if the endpoint supports DNS SRV, set up a DNS SRV record for the
DNS name of the cluster, giving each cluster peer an equal weighting
and priority. The endpoint should be configured with the DNS name
of the cluster. On startup the endpoint issues a DNS SRV request and
receives back the addresses of each cluster peer. It will then try
and register with each peer in turn. DNS round-robin :
if the endpoint does not support DNS SRV, set up a DNS
A-record for the DNS name of the cluster and configure it to
supply a round-robin list of IP addresses for each cluster
peer. The endpoint should be configured with the DNS name of the
cluster. On startup the endpoint performs a DNS A-record lookup
and receives back an address of a peer taken from the round-robin list.
The endpoint will try and register with that peer. If that peer is not
available, the endpoint performs another DNS lookup and
the server will respond with the next peer in the list. This
is repeated until the endpoint registers with a Cisco VCS. Static IP address :
if the cluster does not have a DNS name, configure the endpoint with
the IP address of one of the peers. On startup the endpoint will try
and register with the Cisco VCS at that address. If the Cisco VCS does not respond,
the endpoint will continue trying that same address at regular
intervals. H.323 endpoints: connection failures For each registration method listed above, on registering with the Cisco VCS, the
Cisco VCS  responds with an H.323 “Alternate Gatekeepers” list containing the addresses of Cisco VCS cluster peer members. If the endpoint loses connection with the Cisco VCS it will select another peer from the “Alternate Gatekeepers” list and try to re-register with that Cisco VCS. SIP endpoints: connection failures How SIP endpoints behave if they lose connection to their primary Cisco VCS depends on their initial registration method: SIP Outbound : the endpoint will use one of its other connections. DNS SRV records : the endpoint uses the DNS SRV entry to find a new Cisco VCS to re-register to. DNS round-robin : the endpoint performs another DNS lookup to
find a new Cisco VCS to re-register to (the DNS server providing the next Cisco VCS peer in the
round-robin sequence). Static IP address : the endpoint will keep trying to register to that same Cisco VCS until it is accessible again. For more detailed information about configuring endpoints to work with a Cisco VCS cluster,
refer to the "Cluster Creation and Maintenance" Deployment Guide (document number D14367). This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_183 | Configuring endpoints to register to a cluster of Cisco TelePresence Video Communication Servers (Cisco VCSs) When your Cisco VCS is configured as part of a cluster with one or more peers
(also known as Alternates), endpoints need to be able to reach the
other peers if their primary Cisco VCS becomes unavailable. The H.323
protocol supports this failover re-registration process automatically,
but SIP does not. The way in which you should configure your endpoints and DNS records
depends on the protocol and the functionality supported by your
endpoints. Initial registration process (SIP and H.323 endpoints) In order of preference, for providing resilience of connectivity of endpoints to a cluster of Cisco VCSs, you are
recommended to use the following registration methods for SIP and H.323
endpoints: SIP Outbound : (SIP only)
from software version X6, the Cisco VCS supports "SIP Outbound" (RFC 5626). This allows endpoints that support SIP Outbound to register and maintain connections to multiple peers. DNS SRV records :
if the endpoint supports DNS SRV, set up a DNS SRV record for the
DNS name of the cluster, giving each cluster peer an equal weighting
and priority. The endpoint should be configured with the DNS name
of the cluster. On startup the endpoint issues a DNS SRV request and
receives back the addresses of each cluster peer. It will then try
and register with each peer in turn. DNS round-robin :
if the endpoint does not support DNS SRV, set up a DNS
A-record for the DNS name of the cluster and configure it to
supply a round-robin list of IP addresses for each cluster
peer. The endpoint should be configured with the DNS name of the
cluster. On startup the endpoint performs a DNS A-record lookup
and receives back an address of a peer taken from the round-robin list.
The endpoint will try and register with that peer. If that peer is not
available, the endpoint performs another DNS lookup and
the server will respond with the next peer in the list. This
is repeated until the endpoint registers with a Cisco VCS. Static IP address :
if the cluster does not have a DNS name, configure the endpoint with
the IP address of one of the peers. On startup the endpoint will try
and register with the Cisco VCS at that address. If the Cisco VCS does not respond,
the endpoint will continue trying that same address at regular
intervals. H.323 endpoints: connection failures For each registration method listed above, on registering with the Cisco VCS, the
Cisco VCS  responds with an H.323 “Alternate Gatekeepers” list containing the addresses of Cisco VCS cluster peer members. If the endpoint loses connection with the Cisco VCS it will select another peer from the “Alternate Gatekeepers” list and try to re-register with that Cisco VCS. SIP endpoints: connection failures How SIP endpoints behave if they lose connection to their primary Cisco VCS depends on their initial registration method: SIP Outbound : the endpoint will use one of its other connections. DNS SRV records : the endpoint uses the DNS SRV entry to find a new Cisco VCS to re-register to. DNS round-robin : the endpoint performs another DNS lookup to
find a new Cisco VCS to re-register to (the DNS server providing the next Cisco VCS peer in the
round-robin sequence). Static IP address : the endpoint will keep trying to register to that same Cisco VCS until it is accessible again. For more detailed information about configuring endpoints to work with a Cisco VCS cluster,
refer to the "Cluster Creation and Maintenance" Deployment Guide (document number D14367). This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_183 | June 16th, 2011 | TAA_KB_183 |  |
|---|---|---|---|---|---|
| Configuring endpoints to register to a cluster of Cisco TelePresence Video Communication Servers (Cisco VCSs) When your Cisco VCS is configured as part of a cluster with one or more peers
(also known as Alternates), endpoints need to be able to reach the
other peers if their primary Cisco VCS becomes unavailable. The H.323
protocol supports this failover re-registration process automatically,
but SIP does not. The way in which you should configure your endpoints and DNS records
depends on the protocol and the functionality supported by your
endpoints. Initial registration process (SIP and H.323 endpoints) In order of preference, for providing resilience of connectivity of endpoints to a cluster of Cisco VCSs, you are
recommended to use the following registration methods for SIP and H.323
endpoints: SIP Outbound : (SIP only)
from software version X6, the Cisco VCS supports "SIP Outbound" (RFC 5626). This allows endpoints that support SIP Outbound to register and maintain connections to multiple peers. DNS SRV records :
if the endpoint supports DNS SRV, set up a DNS SRV record for the
DNS name of the cluster, giving each cluster peer an equal weighting
and priority. The endpoint should be configured with the DNS name
of the cluster. On startup the endpoint issues a DNS SRV request and
receives back the addresses of each cluster peer. It will then try
and register with each peer in turn. DNS round-robin :
if the endpoint does not support DNS SRV, set up a DNS
A-record for the DNS name of the cluster and configure it to
supply a round-robin list of IP addresses for each cluster
peer. The endpoint should be configured with the DNS name of the
cluster. On startup the endpoint performs a DNS A-record lookup
and receives back an address of a peer taken from the round-robin list.
The endpoint will try and register with that peer. If that peer is not
available, the endpoint performs another DNS lookup and
the server will respond with the next peer in the list. This
is repeated until the endpoint registers with a Cisco VCS. Static IP address :
if the cluster does not have a DNS name, configure the endpoint with
the IP address of one of the peers. On startup the endpoint will try
and register with the Cisco VCS at that address. If the Cisco VCS does not respond,
the endpoint will continue trying that same address at regular
intervals. H.323 endpoints: connection failures For each registration method listed above, on registering with the Cisco VCS, the
Cisco VCS  responds with an H.323 “Alternate Gatekeepers” list containing the addresses of Cisco VCS cluster peer members. If the endpoint loses connection with the Cisco VCS it will select another peer from the “Alternate Gatekeepers” list and try to re-register with that Cisco VCS. SIP endpoints: connection failures How SIP endpoints behave if they lose connection to their primary Cisco VCS depends on their initial registration method: SIP Outbound : the endpoint will use one of its other connections. DNS SRV records : the endpoint uses the DNS SRV entry to find a new Cisco VCS to re-register to. DNS round-robin : the endpoint performs another DNS lookup to
find a new Cisco VCS to re-register to (the DNS server providing the next Cisco VCS peer in the
round-robin sequence). Static IP address : the endpoint will keep trying to register to that same Cisco VCS until it is accessible again. For more detailed information about configuring endpoints to work with a Cisco VCS cluster,
refer to the "Cluster Creation and Maintenance" Deployment Guide (document number D14367). This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_183 | June 16th, 2011 | TAA_KB_183 |  |
| June 16th, 2011 | TAA_KB_183 |

| Configuring endpoints to register to a cluster of Cisco TelePresence Video Communication Servers (Cisco VCSs) When your Cisco VCS is configured as part of a cluster with one or more peers
(also known as Alternates), endpoints need to be able to reach the
other peers if their primary Cisco VCS becomes unavailable. The H.323
protocol supports this failover re-registration process automatically,
but SIP does not. The way in which you should configure your endpoints and DNS records
depends on the protocol and the functionality supported by your
endpoints. Initial registration process (SIP and H.323 endpoints) In order of preference, for providing resilience of connectivity of endpoints to a cluster of Cisco VCSs, you are
recommended to use the following registration methods for SIP and H.323
endpoints: SIP Outbound : (SIP only)
from software version X6, the Cisco VCS supports "SIP Outbound" (RFC 5626). This allows endpoints that support SIP Outbound to register and maintain connections to multiple peers. DNS SRV records :
if the endpoint supports DNS SRV, set up a DNS SRV record for the
DNS name of the cluster, giving each cluster peer an equal weighting
and priority. The endpoint should be configured with the DNS name
of the cluster. On startup the endpoint issues a DNS SRV request and
receives back the addresses of each cluster peer. It will then try
and register with each peer in turn. DNS round-robin :
if the endpoint does not support DNS SRV, set up a DNS
A-record for the DNS name of the cluster and configure it to
supply a round-robin list of IP addresses for each cluster
peer. The endpoint should be configured with the DNS name of the
cluster. On startup the endpoint performs a DNS A-record lookup
and receives back an address of a peer taken from the round-robin list.
The endpoint will try and register with that peer. If that peer is not
available, the endpoint performs another DNS lookup and
the server will respond with the next peer in the list. This
is repeated until the endpoint registers with a Cisco VCS. Static IP address :
if the cluster does not have a DNS name, configure the endpoint with
the IP address of one of the peers. On startup the endpoint will try
and register with the Cisco VCS at that address. If the Cisco VCS does not respond,
the endpoint will continue trying that same address at regular
intervals. H.323 endpoints: connection failures For each registration method listed above, on registering with the Cisco VCS, the
Cisco VCS  responds with an H.323 “Alternate Gatekeepers” list containing the addresses of Cisco VCS cluster peer members. If the endpoint loses connection with the Cisco VCS it will select another peer from the “Alternate Gatekeepers” list and try to re-register with that Cisco VCS. SIP endpoints: connection failures How SIP endpoints behave if they lose connection to their primary Cisco VCS depends on their initial registration method: SIP Outbound : the endpoint will use one of its other connections. DNS SRV records : the endpoint uses the DNS SRV entry to find a new Cisco VCS to re-register to. DNS round-robin : the endpoint performs another DNS lookup to
find a new Cisco VCS to re-register to (the DNS server providing the next Cisco VCS peer in the
round-robin sequence). Static IP address : the endpoint will keep trying to register to that same Cisco VCS until it is accessible again. For more detailed information about configuring endpoints to work with a Cisco VCS cluster,
refer to the "Cluster Creation and Maintenance" Deployment Guide (document number D14367). This article applies to the following products: Cisco Video Communication Server June 16th, 2011 TAA_KB_183 | June 16th, 2011 | TAA_KB_183 |  |
|---|---|---|---|
| June 16th, 2011 | TAA_KB_183 |

| June 16th, 2011 | TAA_KB_183 |
|---|---|