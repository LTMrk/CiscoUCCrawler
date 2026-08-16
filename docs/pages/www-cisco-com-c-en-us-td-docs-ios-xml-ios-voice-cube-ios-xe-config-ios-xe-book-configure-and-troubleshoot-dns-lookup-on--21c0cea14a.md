---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-configure-and-troubleshoot-dns-lookup-on--21c0cea14a
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/configure-and-troubleshoot-dns-lookup-on-cube.html
retrieved_at: 2026-08-16T15:45:34.063551+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure and Troubleshoot DNS Resolution

## Chapter: Configure and Troubleshoot DNS Resolution

# Configure and Troubleshoot DNS Resolution

## Overview

The Domain Name System  (DNS) is a distributed database in which you can map hostnames to IP addresses through the DNS protocol
                           from a DNS server. Each unique IP address can have an associated hostname. The conversion from a hostname to an IP address
                           is required when hostnames are used as target endpoints under the dial-peers of the CUBE to route the calls out.

This section describes how a DNS lookup takes place in CUBE to determine the IP address that corresponds to the hostnames used for Session Initiation Protocol (SIP) calls.

## Feature Information

The following table provides release information about the feature or features that are described in this module. This table
                              lists only the software release that introduced support for a given feature in a given software release train. Unless noted
                              otherwise, subsequent releases of that software release train also support that feature.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator
                              enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco
                              Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Feature Name

Releases

Feature Information

Configure and Troubleshoot DNS Resolution

Cisco IOS XE Cupertino
                                                17.8.1a

Describes how Domain Name System (DNS) lookup takes place in CUBE to determine the IP address that corresponds to the hostnames used for Session Initiation Protocol (SIP) calls.

## DNS Record Type

CUBE can resolve the following DNS record types:

Service Record: SRV record is a specification of data in the DNS that defines the hostname and port number of servers for
                                 specified services. The SRV Resource Record (RR) allows you to use several servers for a single domain to move services from
                                 host to host. The SRV RR also allows you to designate some hosts as primary servers and others as backups for a service.

Address Record (A Record): Maps a 32-bit IPv4 address to a Fully Qualified Domain Name (FQDN).

IPv6 Address Record (AAAA) Record: Maps a 128-bit IPv6 address to an FQDN.

## Select the SRV Format Version

CUBE resolves SRV records in compliance with RFC2782 by default. In this case, protocol labels are prefixed with an underscore,
                              for example "_sip._udp.example.com". To accommodate older systems, where the underscore is not used, CUBE may be configured
                              to use SRV version 1.

Session Initiation Protocol (SIP) on Cisco VoIP gateways uses the DNS SRV query to determine the IP address of the user endpoint.
                              The query string has a prefix in the form of "protocol.transport." and is attached to the fully qualified domain name (FQDN)
                              of the next hop SIP server. This prefix style originated in RFC 2052. Beginning with Cisco IOS XE Release 2.5, a second style,
                              in compliance with RFC 2782, prepends the protocol label with an underscore "_"; for example, "_protocol._transport." The
                              addition of the underscore reduces the risk of the same name being used for unrelated purposes. The form compliant with RFC
                              2782 is the default style.

The DNS SRV lookup is always attempted first for a Fully Qualified Domain Name (FQDN). If the DNS SRV lookup fails CUBE falls
                                          back to A-AAAA lookup. If you manually add a port number to an FQDN, the CUBE performs an A-AAAA lookup instead of the SRV
                                          lookup.

Example:

'session target dns: cisco.com' would perform an SRV lookup and 'session target dns:cisco.com:5060' performs an A-AAAA lookup.

To change the SRV format version, perform the following:

You do not have to perform this task if you want to use the default RFC 2782 format.

### SUMMARY STEPS

- enable

- configure terminal

- interface type number

- sip-ua

- srv version {1|2}

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

interface type number

### Example:

```
Router(config)# interface gigabitethernet 0/0/0
```

Configures an interface type and enters interface configuration mode.

Step 4

sip-ua

Step 5

srv version {1|2}

Configures the SRV version. The default version is 'srv version 2'.

Step 6

exit

## Load Balance Among SRV Records

This section lists precedence order of the records among multiple SRV entries for the same domain name.

The SRV records follow the following format:

```
_service._proto.name TTL class type of record priority weight port target
```

for example:

```
_sip._tcp.example.com 86400 IN SRV 10 60 5060 bigbox.example.com
_sip._tcp.example.com 86400 IN SRV 10 20 5060 smallbox1.example.com
_sip._tcp.example.com 86400 IN SRV 10 20 5060 smallbox2.example.com
_sip._tcp.example.com 86400 IN SRV 20  0 5060 backupbox.example.com
```

The priority field in the preceding example determines the precedence of the record's data use. Clients must use the SRV records
                           with the lowest priority value first, and fallback to the records of higher value if the connection fails. If a service has
                           multiple SRV records with the same priority value, the clients must load balance them in proportion to the values of their
                           weight fields.

The first three records share a priority of 10, so the weight field's value is used by clients to determine which server (host
                           and port combination) to contact. The sum of all three values is 100, so bigbox.example.com is used 60 percent of time. The
                           two hosts, smallbox1 and smallbox2 are used for 40 percent of requests total, with half of them sent to smallbox1 and the
                           other half to smallbox2. If bigbox is unavailable, these two machines share the load equally since each is selected 50 percent
                           of the time.

If all the three servers with priority 10 are unavailable, the record with the next lowest priority value is chosen that is
                           backupbox.example.com.

## Configure SRV Records

The following example shows how to configure SRV resource records that can be resolved locally for CUBE session targets:

```
ip host _sip._udp.cmgroup1.lab.local srv 1 50 5060 cucm1.lab.local
ip host _sip._udp.cmgroup1.lab.local srv 1 50 5060 cucm2.lab.local
ip host _sip._udp.cmgroup1.lab.local srv 1 50 5060 cucm3.lab.local
```

A or AAAA records must be configured for each SRV resource record. Refer to the " A and AAAA records on CUBE " section for details.

## Configure A and AAAA Records

The following is the command syntax to configure A and AAAA records:

ip host <domain_name> <IPv4/IPv6 Address of the corresponding domain name>

The following are some A record examples:

```
ip host cucm1.lab.local 10.0.0.1
```

```
ip host cucm2.lab.local 10.0.0.2
```

```
ip host cucm3.lab.local 10.0.0.3
```

```
ip host cucm3.lab.local ipv6:2001:DB8:0:0:8:800:200C:417A
```

## DNS Queries with VRF Configuration

While processing a SIP call, if a hostname has to be resolved, only the VRF associated with the SIP call is used during DNS
                           resolutions. Refer to VRF Aware DNS for SIP Calls for details.

## Verify the DNS Configuration on CUBE

The following show commands are used to verify the DNS configuration on CUBE :

show hosts : Displays the default domain name, the style of name lookup service, a list of name server hosts and the cached list of hostnames
                                 and addresses specific to a particular DNS view or for all configured DNS views.

```
ISR4321#show hosts
Default domain is lab.cisco.com
Name servers are 10.106.108.170

NAME                           TTL  CLASS  TYPE  Priority  Weight  Port  DATA/ADDRESS
---------------------------------------------------------------------------------------------------------------------------
_sip._udp.cmgroup1.lab.local    10   IN     SRV     1       50     5060  cucm3.lab.local
_sip._udp.cmgroup1.lab.local    10   IN     SRV     1       50     5060  cucm2.lab.local
_sip._udp.cmgroup1.lab.local    10   IN     SRV     1       50     5060  cucm1.lab.local
```

show ip dns servers : Displays the details about the list of DNS servers that are configured on CUBE .

```
ISR4321#show ip dns servers 

   IP            VRF      TTL(s)   RTT(ms)  RTO(ms)  EDNS  DNSSEC  RECURSION
-----------------------------------------------------------------------------
10.106.108.170            791      1000     64000     Yes    Yes     Yes
```

show ip dns view : Displays the information about a particular DNS view or about all configured DNS views. It includes the number of DNS views
                                 with details like a default domain name, list of name server hosts, and so on.

```
ISR4321#show ip dns view
DNS View default parameters:
DNS Resolver settings:
  Domain lookup is enabled
  Default domain name: lab.cisco.com
  Domain search list:
  Domain name-servers:
    10.106.108.170
DNS Server settings:
  Forwarding of queries is enabled
  Forwarder addresses:
```

## Troubleshoot DNS Configuration

Use the following commands to troubleshoot DNS:

debug ccsip info

debug ip domain detail all

debug ip dns view

debug ip dns view-list

debug ip dns name-list

debug ip domain detail all

debug ip udp

| Feature Name | Releases | Feature Information |
|---|---|---|
| Configure and Troubleshoot DNS Resolution | Cisco IOS XE Cupertino
                                                17.8.1a | Describes how Domain Name System (DNS) lookup takes place in CUBE to determine the IP address that corresponds to the hostnames used for Session Initiation Protocol (SIP) calls. |

| Note | The DNS SRV lookup is always attempted first for a Fully Qualified Domain Name (FQDN). If the DNS SRV lookup fails CUBE falls
                                          back to A-AAAA lookup. If you manually add a port number to an FQDN, the CUBE performs an A-AAAA lookup instead of the SRV
                                          lookup. Example: 'session target dns: cisco.com' would perform an SRV lookup and 'session target dns:cisco.com:5060' performs an A-AAAA lookup. |
|---|---|

| Note | You do not have to perform this task if you want to use the default RFC 2782 format. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | interface type number Example: Router(config)# interface gigabitethernet 0/0/0 | Configures an interface type and enters interface configuration mode. |
| Step 4 | sip-ua |  |
| Step 5 | srv version {1\|2} | Configures the SRV version. The default version is 'srv version 2'. |
| Step 6 | exit |  |

| Note | A or AAAA records must be configured for each SRV resource record. Refer to the " A and AAAA records on CUBE " section for details. |
|---|---|