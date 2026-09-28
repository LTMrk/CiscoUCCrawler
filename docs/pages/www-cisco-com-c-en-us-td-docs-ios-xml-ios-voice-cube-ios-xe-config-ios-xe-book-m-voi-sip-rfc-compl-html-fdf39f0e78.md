---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-rfc-compl-html-fdf39f0e78
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-rfc-compl.html
retrieved_at: 2026-08-16T15:48:17.082448+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP: RFC 2782 Compliance with DNS SRV Queries

## Chapter: SIP: RFC 2782 Compliance with DNS SRV Queries

# SIP: RFC 2782 Compliance with DNS SRV Queries

## Overview

Effective with Cisco IOS XE Release 2.5, the Domain Name System Server (DNS SRV) query used to determine the IP address of
                           the user endpoint is modified in compliance with RFC 2782 (which supersedes RFC 2052). The DNS SRV query prepends the protocol
                           label with an underscore "_" character to reduce the risk of duplicate names being used for unrelated purposes. The form compliant
                           with RFC 2782 is the default style.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP: RFC 2782 Compliance of DNS SRV Queries

Cisco IOS XE Release 2.5

Effective with Cisco IOS XE Release 2.5, the DNS SRV query used to determine the IP address of the user endpoint is modified
                                             in compliance with RFC 2782 (which supersedes RFC 2052). The DNS SRV query prepends the protocol label with an underscore
                                             "_" character to reduce the risk of duplicate names being used for unrelated purposes. The form compliant with RFC 2782 is
                                             the default style.

The following command was introduced or modified: srv version .

## SIP RFC 2782 Compliance with DNS SRV Queries

Session Initiation Protocol (SIP) on Cisco VoIP gateways uses the DNS SRV query to determine the IP address of the user endpoint.
                           The query string has a prefix in the form of "protocol.transport." and is attached to the fully qualified domain name (FQDN)
                           of the next hop SIP server. This prefix style originated in RFC 2052. Beginning with Cisco IOS XE Release 2.5, a second style,
                           in compliance with RFC 2782, prepends the protocol label with an underscore "_"; for example, "_protocol._transport." The
                           addition of the underscore reduces the risk of the same name being used for unrelated purposes. The form compliant with RFC
                           2782 is the default style.

The DNS SRV lookup is always attempted first for a Fully Qualified Domain Name (FQDN). If the DNS SRV lookup fails CUBE falls
                                       back to A-AAAA lookup. If you manually add a port number to a FQDN, the CUBE performs an A-AAAA lookup instead of  SRV lookup.

Example:

'session target dns:cisco.com' would perform an SRV lookup and 'session target dns:cisco.com:5060' would perform an A-AAAA
                                       lookup.

### Configure DNS Server Query Format RFC 2782 Compliance with DNS SRV Queries

Compliance with RFC 2782 changes the DNS SVR protocol label style. RFC 2782 updates RFC 2052 by prepending the protocol label
                                 with an underscore character. The prefix format compliant with RFC 2782 is the default format. However, backward compatibility
                                 is available, allowing newer versions of Cisco IOS software to work with older networks that support only RFC 2052 DNS SVR
                                 prefix style.

To configure the format of DNS SRV queries to comply with RFC 2782, complete this task.

You do not have to perform this task if you want to use the default RFC 2782 format.

### SUMMARY STEPS

- enable

- configure terminal

- interface type number

- sip-ua

- srv version { 1 | 2 }

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

interface type number

#### Example:

```
Router(config)# interface gigabitethernet 0/0/0
```

Configures an interface type and enters interface configuration mode

Step 4

sip-ua

#### Example:

```
Router(config-if)# sip-ua
```

Enters SIP UA configuration mode.

Step 5

srv version { 1 | 2 }

#### Example:

```
Router(config-sip-ua)# srv version 2
```

Generates DNS SRV queries in either RFC 2782 or RFC 2052 format.

1 --The query is set to the domain name prefix of protocol.transport. (RFC 2052 style).

2 --The query is set to the domain name prefix of _protocol._transport. (RFC 2782 style). This is the default.

Step 6

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits the current configuration mode.

## Configure DNS Server Lookups

Following is the example to configure '_sip._udp.'.

```
!
dial-peer voice 1 voip
 session protocol sipv2
 session transport udp
 session target dns:cisco.com
!
```

Following are the examples to configure '_sip._tcp.'.

```
!
dial-peer voice 1 voip
 session protocol sipv2
 session transport tcp
 session target dns:cisco.com
!
```

```
!
dial-peer voice 1 voip
 session protocol sipv2
 session transport tcp tls
 session target dns:cisco.com
!
```

Following is the example to configure '_sips._tcp.'.

```
!
dial-peer voice 1 voip
 session protocol sipv2
 session transport tcp tls
 session target dns:cisco.com
 voice-class sip url sips
!
```

From Cisco IOS XE Release 16.12.3 onwards, CUBE sends '_sips._tcp.' query when the transport is TLS. The '_sips._tcp.' query is independent of the URI scheme—sip or sips.
                              Following is the example to configure '_sips._tcp.'.

```
!
dial-peer voice 1 voip
 session protocol sipv2
 session transport tcp tls
 session target dns:cisco.com
!
```

Following is the sample configuration for a local DNS SRV.

```
!
ip name-server 172.18.110.64
!
ip domain lookup 
!
ip host 1.cisco.com 10.10.10.1
ip host 2.cisco.com 10.10.10.2
ip host 3.cisco.com 10.10.10.3
!
ip host _sip._tcp.cisco.com srv 1 50 5061 1.cisco.com
ip host _sip._tcp.cisco.com srv 1 50 5061 2.cisco.com
ip host _sip._tcp.cisco.com srv 1 50 5061 3.cisco.com
!
ip host _sips._tcp.cisco.com srv 1 50 5061 1.cisco.com
ip host _sips._tcp.cisco.com srv 1 50 5061 2.cisco.com
ip host _sips._tcp.cisco.com srv 1 50 5061 3.cisco.com
!
ip host _sip._udp.cisco.com srv 1 50 5060 1.cisco.com
ip host _sip._udp.cisco.com srv 1 50 5060 2.cisco.com
ip host _sip._udp.cisco.com srv 1 50 5060 3.cisco.com
!
ip host _sip._tcp.cisco.com srv 1 50 5060 1.cisco.com
ip host _sip._tcp.cisco.com srv 1 50 5060 2.cisco.com
ip host _sip._tcp.cisco.com srv 1 50 5060 3.cisco.com
!
```

## Verifying

The following example shows sample is output from the show sip-ua status command used to verify the style of DNS server queries:

```
Router# show sip-ua status SIP User Agent Status 
SIP User Agent for UDP : ENABLED 
SIP User Agent for TCP : ENABLED 
SIP User Agent bind status(signaling): DISABLED 
SIP User Agent bind status(media): DISABLED 
SIP max-forwards : 6 
SIP DNS SRV version: 1 (rfc 2052)
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP: RFC 2782 Compliance of DNS SRV Queries | Cisco IOS XE Release 2.5 | Effective with Cisco IOS XE Release 2.5, the DNS SRV query used to determine the IP address of the user endpoint is modified
                                             in compliance with RFC 2782 (which supersedes RFC 2052). The DNS SRV query prepends the protocol label with an underscore
                                             "_" character to reduce the risk of duplicate names being used for unrelated purposes. The form compliant with RFC 2782 is
                                             the default style. The following command was introduced or modified: srv version . |

| Note | The DNS SRV lookup is always attempted first for a Fully Qualified Domain Name (FQDN). If the DNS SRV lookup fails CUBE falls
                                       back to A-AAAA lookup. If you manually add a port number to a FQDN, the CUBE performs an A-AAAA lookup instead of  SRV lookup. Example: 'session target dns:cisco.com' would perform an SRV lookup and 'session target dns:cisco.com:5060' would perform an A-AAAA
                                       lookup. |
|---|---|

| Note | You do not have to perform this task if you want to use the default RFC 2782 format. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | interface type number Example: Router(config)# interface gigabitethernet 0/0/0 | Configures an interface type and enters interface configuration mode |
| Step 4 | sip-ua Example: Router(config-if)# sip-ua | Enters SIP UA configuration mode. |
| Step 5 | srv version { 1 \| 2 } Example: Router(config-sip-ua)# srv version 2 | Generates DNS SRV queries in either RFC 2782 or RFC 2052 format. 1 --The query is set to the domain name prefix of protocol.transport. (RFC 2052 style). 2 --The query is set to the domain name prefix of _protocol._transport. (RFC 2782 style). This is the default. |
| Step 6 | exit Example: Router(config-sip-ua)# exit | Exits the current configuration mode. |