---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-26058b8ae7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_b_pre-installation-planning-guide-for-cisco_chapter_01100.html
retrieved_at: 2026-08-22T00:11:36.162938+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

Updated: February 4, 2020

Chapter: IP Address Worksheets

## Chapter: IP Address Worksheets

# IP Address Worksheets

This chapter provides worksheets you can use to record IP addresses for
                        		the visible and private networks. You also need to define static routes for
                        		some of the nodes in the Unified ICM system.

## Visible Network IP
                        	 Address Requirements

The table titled Visible Network IP Address
                                 			 Requirements lists the IP address requirements for Unified ICM node connections
                              		  to the visible network. The Unified ICM nodes are listed as duplexed pairs (for
                              		  example, CallRouter A and CallRouter B). You may or may not have duplexed nodes
                              		  in your configuration. Supply IP addresses only for the nodes you have in your
                              		  configuration.

Node

Location

Address Type

IP Address

CallRouter A

High
                                          					 Priority

Low Priority

Default IP
                                          					 Gateway

Netmask

CallRouter B

High
                                          					 Priority

Low Priority

Default IP
                                          					 Gateway

Netmask

Logger A

Normal Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

Logger B

Normal Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

Central Site
                                          					 IP Router

Normal data

Remote
                                          					 Contact Center Site IP Route

Normal data

PG1A

Normal Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

PG1B

Normal
                                          					 Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

PG2A

Normal
                                          					 Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

PG2B

Normal
                                          					 Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

PG3A

Normal
                                          					 Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

PG3B

Normal
                                          					 Data

RAS 1

RAS 2

Default IP
                                          					 Gateway1

Netmask

AW1

Normal
                                          					 Data

Default IP
                                          					 Gateway1

Netmask

AW2

Normal
                                          					 Data

Default IP
                                          					 Gateway1

Netmask

## Private Network IP Address Requirements

The table titled Private Network IP
                                 Address Requirements lists the IP address requirements for Unified ICM
                              node connections to the private network. The Unified ICM nodes are listed as
                              duplexed pairs (for example, CallRouter A and CallRouter B). You may or may not
                              have duplexed nodes in your configuration. You need to supply IP addresses only
                              for the nodes you have in your configuration.

Node

Location

Address Type

IP Address

CallRouter A

High Priority

Low
                                          Priority

Default IP Gateway

Netmask

CallRouter B

High Priority

Low
                                          Priority

Default IP Gateway

Netmask

Logger A

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

Logger B

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

Central Site IP Router

Normal
                                          Data

Remote Contact Center Site IP Router

Normal
                                          Data

PG1A

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

PG1B

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

PG2A

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

PG2B

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

PG3A

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

PG3B

Normal Data

RAS 1

RAS 2

Default IP
                                          Gateway1

Netmask

Modem Tel.
                                          Number

AW 1

Normal Data

Default IP
                                          Gateway1

Netmask

AW
                                          2

Modem
                                          Tel. Number

Normal Data

Default IP
                                          Gateway1

Netmask

## Signaling Access Network IP requirements

The table titled Signaling Access
                                 Network IP Requirements lists the IP address requirements for Unified
                              ICM node connections to the Signaling Access Network. The Unified ICM nodes are
                              listed as duplexed pairs (for example, CallRouter A and CallRouter B). You may
                              or may not have duplexed nodes in your configuration. You need to supply IP
                              addresses only for the nodes you have in your configuration

Node

Location

Address Type

IP
                                          Address

CallRouter A

Normal data

CallRouter B

Normal
                                          data

Network Gateway 1A

Normal
                                          data

Network Gateway 1B

Normal
                                          data

## Static Route Requirements

The IP routers used in the Unified ICM networks must have static
                              		  routes defined in order to provide the necessary connectivity between the
                              		  visible LAN at the central site and the visible LANs at remote contact center
                              		  sites. The static route ensures that the IP router can forward traffic from the
                              		  central site to the remote site. In addition, CallRouters and Loggers must have
                              		  a static route defined for the remote private LAN. This static route ensures
                              		  that private network traffic is segregated from visible network traffic.

You must define all the static routes required in your configuration.
                              		  However, you cannot define these static routes until you have assigned all
                              		  Unified ICM nodes IP addresses.

Node

Network

Static Route

Central Site Visible Network IP Router—Side A and Side B

Visible

Define one static route for the visible LAN at each remote
                                          					 contact center site and each administrator site. If the central sites are
                                          					 geographically separated, add another static route for the other central site.

Central Site Private Network IP Router—Side A and Side B

Private

Define one static route for the private LAN at the other
                                          					 central site.

CallRouter—Side A and Side B

Private

If the sides of the central controller are geographically
                                          					 separated, define one static route for the subnet address of the private LAN on
                                          					 the other side of the central controller.

Logger—Side A and Side B

Private

If the sides of the central controller are geographically
                                          					 separated, define one static route for the subnet address of the private LAN on
                                          					 the other side of the central controller.

PG (all PGs)

Visible

One of the two IP routers at a contact center is targeted as
                                          					 the default gateway for the PG. However, the PG needs IP connectivity to both
                                          					 sides of the central controller. Therefore, for each PG you must define a
                                          					 static route to the other IP router (that is, to the IP router that is not
                                          					 targeted as the PG's default gateway IP router).

Remote Contact Center IP Routers

Visible

For each IP router, define a static route to one side of the
                                          					 central controller (to the central site visible network IP router).

Admin Site IP Routers

Visible

For each Admin Site IP router, define a static route to one
                                          					 side of the central controller (to the central site visible network IP router).

| Node | Location | Address Type | IP Address |
|---|---|---|---|
| CallRouter A |  | High
                                          					 Priority |  |
|  |  | Low Priority |  |
|  |  | Default IP
                                          					 Gateway |  |
|  |  | Netmask |  |
| CallRouter B |  | High
                                          					 Priority |  |
|  |  | Low Priority |  |
|  |  | Default IP
                                          					 Gateway |  |
|  |  | Netmask |  |
| Logger A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| Logger B |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| Central Site
                                          					 IP Router |  | Normal data |  |
| Remote
                                          					 Contact Center Site IP Route |  | Normal data |  |
| PG1A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| PG1B |  | Normal
                                          					 Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| PG2A |  | Normal
                                          					 Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| PG2B |  | Normal
                                          					 Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| PG3A |  | Normal
                                          					 Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| PG3B |  | Normal
                                          					 Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| AW1 |  | Normal
                                          					 Data |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |
| AW2 |  | Normal
                                          					 Data |  |
|  |  | Default IP
                                          					 Gateway1 |  |
|  |  | Netmask |  |

| Node | Location | Address Type | IP Address |
|---|---|---|---|
| CallRouter A |  | High Priority |  |
|  |  | Low
                                          Priority |  |
|  |  | Default IP Gateway |  |
|  |  | Netmask |  |
| CallRouter B |  | High Priority |  |
|  |  | Low
                                          Priority |  |
|  |  | Default IP Gateway |  |
|  |  | Netmask |  |
| Logger A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| Logger B |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| Central Site IP Router |  | Normal
                                          Data |  |
| Remote Contact Center Site IP Router |  | Normal
                                          Data |  |
| PG1A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| PG1B |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| PG2A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| PG2B |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| PG3A |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| PG3B |  | Normal Data |  |
|  |  | RAS 1 |  |
|  |  | RAS 2 |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
|  |  | Modem Tel.
                                          Number |  |
| AW 1 |  | Normal Data |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |
| AW
                                          2 |  | Modem
                                          Tel. Number |  |
|  |  | Normal Data |  |
|  |  | Default IP
                                          Gateway1 |  |
|  |  | Netmask |  |

| Node | Location | Address Type | IP
                                          Address |
|---|---|---|---|
| CallRouter A |  | Normal data |  |
| CallRouter B |  | Normal
                                          data |  |
| Network Gateway 1A |  | Normal
                                          data |  |
| Network Gateway 1B |  | Normal
                                          data |  |

| Node | Network | Static Route |
|---|---|---|
| Central Site Visible Network IP Router—Side A and Side B | Visible | Define one static route for the visible LAN at each remote
                                          					 contact center site and each administrator site. If the central sites are
                                          					 geographically separated, add another static route for the other central site. |
| Central Site Private Network IP Router—Side A and Side B | Private | Define one static route for the private LAN at the other
                                          					 central site. |
| CallRouter—Side A and Side B | Private | If the sides of the central controller are geographically
                                          					 separated, define one static route for the subnet address of the private LAN on
                                          					 the other side of the central controller. |
| Logger—Side A and Side B | Private | If the sides of the central controller are geographically
                                          					 separated, define one static route for the subnet address of the private LAN on
                                          					 the other side of the central controller. |
| PG (all PGs) | Visible | One of the two IP routers at a contact center is targeted as
                                          					 the default gateway for the PG. However, the PG needs IP connectivity to both
                                          					 sides of the central controller. Therefore, for each PG you must define a
                                          					 static route to the other IP router (that is, to the IP router that is not
                                          					 targeted as the PG's default gateway IP router). |
| Remote Contact Center IP Routers | Visible | For each IP router, define a static route to one side of the
                                          					 central controller (to the central site visible network IP router). |
| Admin Site IP Routers | Visible | For each Admin Site IP router, define a static route to one
                                          					 side of the central controller (to the central site visible network IP router). |