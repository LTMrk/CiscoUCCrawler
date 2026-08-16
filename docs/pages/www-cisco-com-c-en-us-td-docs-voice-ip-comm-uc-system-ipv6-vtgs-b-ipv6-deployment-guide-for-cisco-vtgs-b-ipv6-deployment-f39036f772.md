---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-f39036f772
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01.html
retrieved_at: 2026-08-16T18:21:37.286200+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: IPv6 Basics

## Chapter: IPv6 Basics

# IPv6 Basics

## IPv6 Basics Overview

This chapter provides an introduction to the basics of IPv6 addressing, including the various address types, address assignment
                           options, new DHCP features, and DNS. For further reading on IPv6, you can refer to the following documentation:

IPv6 Fundamentals: A Straightforward Approach to Understanding IPv6, 2nd Edition , a Cisco Press publication available as a: book or video .

IPv6 Design and Deployment LiveLessons , a Cisco Press publication available through Link

Other Cisco online documentation at Link .

## IPv6 Addressing

An IPv6 address consists of 8 sets of 16-bit hexadecimal values separated by colons (:), totaling 128 bits in length. For
                              example:

```
2001:0db8:1234:5678:9abc:def0:1234:5678
```

You can omit leading zeros. For consecutive zeros in contiguous blocks, you can use a double colon (::). Double colons can
                              appear only once in the address.

For example, here is the complete address:

```
2001:0db8:0000:130F:0000:0000:087C:140B
```

Here is the abbreviation:

```
2001:0db8:0:130F::87C:140B
```

As with IPv4 addresses, you can represent an IPv6 address network prefix the same way:

```
2001:db8:12::/64
```

## IPv6 Unicast Addresses: Network and Host IDs

IPv6 unicast addresses generally use 64 bits for the network ID and 64 bits for the host ID.

The network ID is administratively assigned. The host ID is configured manually or auto-configured by any of the following
                              methods:

Using a randomly generated number.

Using DHCPv6.

Using the Extended Unique Identifier (EUI-64) format. We commonly use the EUI-64 host ID format for devices such as Cisco
                                    IP Phones, gateways, and routers. This format, as illustrated, expands the device interface 48-bit MAC address to 64 bits
                                    by inserting FFFE into the middle 16 bits.

## Types of IPv6 Addresses

As with IPv4, IPv6 addresses are assigned to interfaces. However, unlike IPv4, an IPv6 interface is expected to have multiple
                              addresses. There are several types:

Unicast address—Identifies a single node or interface. Traffic destined for a unicast address is forwarded to a single interface.

Multicast address—Identifies a group of nodes or interfaces. Traffic destined for a multicast address is forwarded to all
                                       the nodes in the group.

Anycast address—Identifies a group of nodes or interfaces. Traffic destined to an anycast address is forwarded to the nearest
                                       node in the group. An anycast address is essentially a unicast address assigned to multiple devices with a host ID = 0000:0000:0000:0000.
                                       (Anycast addresses are not widely used today.)

With IPv6, broadcast addresses are no longer used. Broadcast addresses are too resource intensive, so IPv6 uses multicast
                              addresses instead.

### Address Scopes

An address scope defines the region where an address can be defined as a unique identifier of an interface. These scopes or
                                 regions are the link, the site network, and the global network, corresponding to link-local, unique local unicast, and global
                                 addresses.

### Global Unicast Addresses

Global unicast addresses are:

Routable and reachable across the Internet.

IPv6 addresses for widespread generic use.

Structured as a hierarchy to allow address aggregation.

Identified by their three high-level bits set to 001 (2000::/3).

The global routing prefix is assigned to a service provider by the Internet Assigned Numbers Authority (IANA). The site level
                                 aggregator (SLA), or subnet ID, is assigned to a customer by their service provider. The LAN ID represents individual networks
                                 within the customer site and is administered by the customer.

The Host or Interface ID has the same meaning for all unicast addresses. It is 64 bits long and is typically created by using
                                 the EUI-64 format.

Example:

```
2001:0DB8:BBBB:CCCC:0987:65FF:FE01:2345
```

### Unique Local Unicast Addresses

Unique local unicast addresses are:

Analogous to private IPv4 addresses (for example, 10.1.1.254)

Used for local communications, inter-site VPNs, and so forth

Not routable on the Internet (routing would require IPv6 NAT)

Global IDs do not have to be aggregated and are defined by the administrator of the local domain. Subnet IDs are also defined
                                 by the administrator of the local domain. Subnet IDs are typically defined using a hierarchical addressing plan to allow for
                                 route summarization.

The Host or Interface ID has the same meaning for all unicast addresses. It is 64 bits long and is typically created by using
                                 the EUI-64 format.

Example:

```
FD00:aaaa:bbbb:CCCC:0987:65FF:FE01:2345
```

### Link Local Unicast Addresses

Link local unicast addresses are:

Mandatory addresses that are used exclusively for communication between two IPv6 devices on the same link.

Automatically assigned by device when IPv6 is enabled.

Not routable addresses. Their scope is link-specific only.

Identified by the first 10 bits (FE80).

The remaining 54 bits of the network ID could be zero or any manually configured value. The interface ID has the same meaning
                                 for all unicast addresses. It is 64 bits long and is typically created by using the EUI-64 format.

Example:

```
FE80:0000:0000:0000:0987:65FF:FE01:2345
```

This address would generally be represented in shorthand notation as:

```
FE80::987:65FF:FE01:2345
```

### IPv6 Multicast Addresses

IPv6 multicast addresses have an 8-bit prefix, FF00::/8 (1111 1111). The second octet defines the lifetime and scope of the
                                 multicast address.

Multicast addresses are always destination addresses. Multicast addresses are used for router solicitations (RS), router advertisements
                                    (RA), DHCPv6, multicast applications, and so forth.

IPv6 clients do not require a default gateway configuration because routers are discovered using RSs and RAs.

Address

Scope

Meaning

FF01::1

Node-local

Same node

FF02::1

Link-local

All nodes on a link

FF01::2

Node-local

Same router

FF02::2

Link-local

All routers on a link

FF05::2

Site-local

All routers on the Internet

FF02::1:FFxx:xxxx

Link-local

Solicited node

For more information on IPv6 multicast addresses, refer to the IANA documentation: Link .

IPv6 multicast application is not developed in Collaboration products, and is not supported industry wide through service
                                             provider networks.

## Address Assignment for IPv6 Devices

### Manual Configuration

Because IPv6 addresses are so complex, you won't want to configure many of them manually. There's too much administrative
                                 overhead. But you might want static addresses for router interfaces and certain network resources.

### IPv6 Stateless Address Auto-Configuration (RFC2462)

One of the easiest ways to assign IP addresses is to set up IPv6 Stateless address auto-configuration (SLAAC) on an IPv6 router.

The network administrator configures the router to send Router Advertisement (RA) announcements onto the link. Then the on-link
                                 connected IPv6 nodes configure themselves with an IPv6 address and routing parameters.

They get the IPv6 network prefix from the link-local router's RAs. They create the IPv6 host ID by using the device's MAC
                                 address and the EUI-64 format for host IDs.

### DHCP for IPv6

IPv6 devices use multicast to acquire IP addresses and to find DHCPv6 servers. The basic DHCPv6 client-server concept is similar
                                 to DHCP for IPv4. If a client wants to receive configuration parameters, it sends out a request on the attached local network
                                 to detect available DHCPv6 servers.

The DHCPv6 client requests parameters from an available server. This is done using Solicit and Advertise message and well-known
                                       DHCPv6 multicast addresses.

The server responds with the requested information in a Reply message. As with DHCPv4, DHCPv6 uses an architectural concept
                                       of "options" to carry more parameters and information within DHCPv6 messages.

The DHCPv6 client knows whether to use DHCPv6 based upon the instruction from a router on its link-local network. The default
                                 gateway has two configurable bits in its Router Advertisement (RA) available for this purpose:

O bit—When this bit is set, the client can use DHCPv6 to retrieve other configuration parameters (for example, TFTP server
                                       address or DNS server address) but not the client's IP address.

M bit—When this bit is set, the client can use DHCPv6 to retrieve a managed IPv6 address and other configuration parameters
                                       from a DHCPv6 server.

#### Stateless DHCP

Stateless DHCPv6, which is specified by RFC3736, is a combination of Stateless address auto-configuration (SLAAC) and Dynamic
                                    Host Configuration Protocol (DHCP) for IPv6.

When a router sends an RA with the O bit set but does not set the M bit, the client can use SLAAC to obtain its IPv6 address
                                    and use DHCPv6 to obtain additional information, such as TFTP server address or DNS server address. This mechanism is known
                                    as Stateless DHCPv6 because the DHCPv6 server does not have to track the client address bindings.

### IPv6 Address Assignment Table

To automatically configure IP phones with IPv6 address assignment, use the following configuration in Unified CM and in router
                                 Routing Advertisement (RA).

Address Assignment Method

Auto_config parameter on Unified CM

M-bit

O-bit

IPv6 address Stateless prefix from RA and DHCP to pull TFTP and DNS address

On

Off

On

Invalid configuration

On

Off

Off

Invalid configuration

Off

Off

On

Invalid configuration

Off

Off

Off

## DNS for IPv6

Cisco Unified Communications Manager (Unified CM) uses DNS name-to-address resolution in the following cases:

If DNS names are used to define Unified CM servers (not supported)

If SIP route patterns use DNS names to define destinations

If SIP trunks use DNS names to define trunk destinations

For IPv6, the principles of DNS are the same as for IPv4, with the following exceptions:

The nomenclature is different (AAAA records are used instead of A records).

DNS name-to-address queries can return multiple IPv6 addresses.

Resolution of:

IPv4

IPv6

Hostname to IP address

A record:

www.abc.test. A 192.168.30.1

AAAA record:

www.abc.test AAAA 2001:db8:C18:1::2

IP address to hostname

PTR record:

1.30.168.192.in-addr.arpa. PTR

www.abc.test.

PTR record:

2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.8.1.c.0.

8.b.d.0.1.0.0.2.ip6.arpa PTR www.abc.test.

### Customers Also Viewed

- IPv6 Deployment Guide --- IPv6 Introduction

| Note | IPv6 clients do not require a default gateway configuration because routers are discovered using RSs and RAs. |
|---|---|

| Address | Scope | Meaning |
|---|---|---|
| FF01::1 | Node-local | Same node |
| FF02::1 | Link-local | All nodes on a link |
| FF01::2 | Node-local | Same router |
| FF02::2 | Link-local | All routers on a link |
| FF05::2 | Site-local | All routers on the Internet |
| FF02::1:FFxx:xxxx | Link-local | Solicited node |

| Note | IPv6 multicast application is not developed in Collaboration products, and is not supported industry wide through service
                                             provider networks. |
|---|---|

| Address Assignment Method | Auto_config parameter on Unified CM | M-bit | O-bit |
|---|---|---|---|
| IPv6 address Stateless prefix from RA and DHCP to pull TFTP and DNS address | On | Off | On |
| Invalid configuration | On | Off | Off |
| Invalid configuration | Off | Off | On |
| Invalid configuration | Off | Off | Off |

| Resolution of: | IPv4 | IPv6 |
|---|---|---|
| Hostname to IP address | A record: www.abc.test. A 192.168.30.1 | AAAA record: www.abc.test AAAA 2001:db8:C18:1::2 |
| IP address to hostname | PTR record: 1.30.168.192.in-addr.arpa. PTR www.abc.test. | PTR record: 2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.0.0.0.8.1.c.0. 8.b.d.0.1.0.0.2.ip6.arpa PTR www.abc.test. |