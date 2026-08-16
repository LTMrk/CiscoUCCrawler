---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-767dc1718a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_configuration-details.html
retrieved_at: 2026-08-16T15:28:01.462281+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Configuration Details

## Chapter: Configuration Details

# Configuration Details

## Configuration Details

This appendix summarizes the configuration required for the Expressway-C and Expressway-E, in three sections:

Configuration for Expressway-C only

Configuration for Expressway-E only

Configuration for both Expressway-C and Expressway-E

## Expressway-C Configuration Details

Configuration item

Value

Expressway page

System configuration

System name

EXPc

System > Administration

LAN1 IPv4 address

10.0.0.2

System > Network interfaces > IP

IPv4 gateway

10.0.0.1

System > Network interfaces > IP

LAN1 subnet mask

255.255.255.0

System > Network interfaces > IP

DNS server address 1

10.0.0.11

System > DNS

DNS server address 2

10.0.0.12

System > DNS

DNS Domain name

internal-domain.net

System > DNS

DNS System host name

expc

System > DNS

NTP server 1

pool.ntp.org

System > Time

Time zone

GMT

System > Time

Protocol configuration

SIP domain name

example.com

Configuration > Domains

Traversal zone

Zone Name

TraversalZone

Configuration > Zones > Zones

Zone Type

Traversal client

Configuration > Zones > Zones

Protocol SIP port

7001

Configuration > Zones > Zones

Protocol H.323 port

6001

Configuration > Zones > Zones

Location Peer 1 address

192.0.2.2

Configuration > Zones > Zones

Authentication username

exampleauth

Configuration > Zones > Zones

Authentication password

ex4mpl3.c0m

Configuration > Authentication > Devices > Local database

Traversal search rule

Rule name

Traversal zone search rule

Configuration > Dial plan > Search rules

Description

Search traversal zone (Expressway-C)

Configuration > Dial plan > Search rules

Priority

100

Configuration > Dial plan > Search rules

Source

Any

Configuration > Dial plan > Search rules

Mode

Any alias

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

TraversalZone

Configuration > Dial plan > Search rules

Direct IP search rule

Rule name

External IP address search rule

Configuration > Dial plan > Search rules

Description

Route external IP address

Configuration > Dial plan > Search rules

Priority

100

Configuration > Dial plan > Search rules

Source

Any

Configuration > Dial plan > Search rules

Mode

Any IP address

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

TraversalZone

Configuration > Dial plan > Search rules

IP call routing

Calls to unknown IP addresses

Indirect

Configuration > Dial plan > Configuration

## Expressway-E Configuration Details

Configuration item

Value

Expressway page

System configuration

System name

EXPe

System > Administration

LAN1 IPv4 address

192.0.2.2

System > Network interfaces > IP

IPv4 gateway

192.0.2.1

System > Network interfaces > IP

LAN1 subnet mask

255.255.255.0

System > Network interfaces > IP

DNS server address 1

194.72.6.57

System > DNS

DNS server address 2

194.73.82.242

System > DNS

DNS Domain name

example.com

System > DNS

DNS System host name

expe

System > DNS

NTP server 1

pool.ntp.org

System > Time

Time zone

GMT

System > Time

Protocol configuration

SIP domain name

example.com

Configuration > Domains

Traversal zone

Zone Name

TraversalZone

Configuration > Zones > Zones

Zone Type

Traversal server

Configuration > Zones > Zones

Client authentication username

exampleauth

Configuration > Zones > Zones

Protocol SIP port

7001

Configuration > Zones > Zones

Protocol H.323 port

6001

Configuration > Zones > Zones

Name

exampleauth

Configuration > Authentication > Devices > Local database

Password

ex4mpl3.c0m

Configuration > Authentication > Devices > Local database

Traversal zone search rule

Rule name

Traversal zone search rule

Configuration > Dial plan > Search rules

Description

Search traversal zone (Expressway-E)

Configuration > Dial plan > Search rules

Priority

100

Configuration > Dial plan > Search rules

Source

Any

Configuration > Dial plan > Search rules

Mode

Any alias

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

TraversalZone

Configuration > Dial plan > Search rules

DNS zone

Zone Name

DNSZone

Configuration > Zones

Zone Type

DNS

Configuration > Zones > Zones

DNS zone search rule

Rule name

DNS zone search rule

Configuration > Dial plan > Search rules

Zone name

Search DNS zone (external DNS)

Configuration > Dial plan > Search rules

Priority

150

Configuration > Dial plan > Search rules

Source

All zones

Configuration > Dial plan > Search rules

Mode

Alias pattern match

Configuration > Dial plan > Search rules

Pattern type

Regex

Configuration > Dial plan > Search rules

Pattern string

(?!.*@example\.com.*$).*

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

DNSZone

Configuration > Dial plan > Search rules

IP call routing

Calls to unknown IP addresses

Direct

Configuration > Dial plan > Configuration

## Expressway-C and Expressway-E Configuration Details

Configuration item

Value

Expressway page

Transform

Pattern string

([^@]*)

Configuration > Dial plan > Transforms

Pattern type

Regex

Configuration > Dial plan > Transforms

Pattern behavior

Replace

Configuration > Dial plan > Transforms

Replace string

\1@example.com

Configuration > Dial plan > Transforms

Local search rule 1

Rule name

Local zone – no domain

Configuration > Dial plan > Search rules

Priority

48

Configuration > Dial plan > Search rules

Source

Any

Configuration > Dial plan > Search rules

Mode

Alias pattern match

Configuration > Dial plan > Search rules

Pattern type

Regex

Configuration > Dial plan > Search rules

Pattern string

(.+)@example\.com.*

Configuration > Dial plan > Search rules

Pattern behavior

Replace

Configuration > Dial plan > Search rules

Replace string

\1

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

LocalZone

Configuration > Dial plan > Search rules

Local search rule 2

Rule name

Local zone – full URI

Configuration > Dial plan > Search rules

Priority

50

Configuration > Dial plan > Search rules

Source

Any

Configuration > Dial plan > Search rules

Mode

Alias pattern match

Configuration > Dial plan > Search rules

Pattern type

Regex

Configuration > Dial plan > Search rules

Pattern string

(.+)@example\.com.*

Configuration > Dial plan > Search rules

Pattern behavior

Leave

Configuration > Dial plan > Search rules

On successful match

Continue

Configuration > Dial plan > Search rules

Target

LocalZone

Configuration > Dial plan > Search rules

| Configuration item | Value | Expressway page |
|---|---|---|
| System configuration |
| System name | EXPc | System > Administration |
| LAN1 IPv4 address | 10.0.0.2 | System > Network interfaces > IP |
| IPv4 gateway | 10.0.0.1 | System > Network interfaces > IP |
| LAN1 subnet mask | 255.255.255.0 | System > Network interfaces > IP |
| DNS server address 1 | 10.0.0.11 | System > DNS |
| DNS server address 2 | 10.0.0.12 | System > DNS |
| DNS Domain name | internal-domain.net | System > DNS |
| DNS System host name | expc | System > DNS |
| NTP server 1 | pool.ntp.org | System > Time |
| Time zone | GMT | System > Time |
| Protocol configuration |
| SIP domain name | example.com | Configuration > Domains |
| Traversal zone |
| Zone Name | TraversalZone | Configuration > Zones > Zones |
| Zone Type | Traversal client | Configuration > Zones > Zones |
| Protocol SIP port | 7001 | Configuration > Zones > Zones |
| Protocol H.323 port | 6001 | Configuration > Zones > Zones |
| Location Peer 1 address | 192.0.2.2 | Configuration > Zones > Zones |
| Authentication username | exampleauth | Configuration > Zones > Zones |
| Authentication password | ex4mpl3.c0m | Configuration > Authentication > Devices > Local database |
| Traversal search rule |
| Rule name | Traversal zone search rule | Configuration > Dial plan > Search rules |
| Description | Search traversal zone (Expressway-C) | Configuration > Dial plan > Search rules |
| Priority | 100 | Configuration > Dial plan > Search rules |
| Source | Any | Configuration > Dial plan > Search rules |
| Mode | Any alias | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | TraversalZone | Configuration > Dial plan > Search rules |
| Direct IP search rule |
| Rule name | External IP address search rule | Configuration > Dial plan > Search rules |
| Description | Route external IP address | Configuration > Dial plan > Search rules |
| Priority | 100 | Configuration > Dial plan > Search rules |
| Source | Any | Configuration > Dial plan > Search rules |
| Mode | Any IP address | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | TraversalZone | Configuration > Dial plan > Search rules |
| IP call routing |  |  |
| Calls to unknown IP addresses | Indirect | Configuration > Dial plan > Configuration |

| Configuration item | Value | Expressway page |
|---|---|---|
| System configuration |
| System name | EXPe | System > Administration |
| LAN1 IPv4 address | 192.0.2.2 | System > Network interfaces > IP |
| IPv4 gateway | 192.0.2.1 | System > Network interfaces > IP |
| LAN1 subnet mask | 255.255.255.0 | System > Network interfaces > IP |
| DNS server address 1 | 194.72.6.57 | System > DNS |
| DNS server address 2 | 194.73.82.242 | System > DNS |
| DNS Domain name | example.com | System > DNS |
| DNS System host name | expe | System > DNS |
| NTP server 1 | pool.ntp.org | System > Time |
| Time zone | GMT | System > Time |
| Protocol configuration |
| SIP domain name | example.com | Configuration > Domains |
| Traversal zone |
| Zone Name | TraversalZone | Configuration > Zones > Zones |
| Zone Type | Traversal server | Configuration > Zones > Zones |
| Client authentication username | exampleauth | Configuration > Zones > Zones |
| Protocol SIP port | 7001 | Configuration > Zones > Zones |
| Protocol H.323 port | 6001 | Configuration > Zones > Zones |
| Name | exampleauth | Configuration > Authentication > Devices > Local database |
| Password | ex4mpl3.c0m | Configuration > Authentication > Devices > Local database |
| Traversal zone search rule |
| Rule name | Traversal zone search rule | Configuration > Dial plan > Search rules |
| Description | Search traversal zone (Expressway-E) | Configuration > Dial plan > Search rules |
| Priority | 100 | Configuration > Dial plan > Search rules |
| Source | Any | Configuration > Dial plan > Search rules |
| Mode | Any alias | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | TraversalZone | Configuration > Dial plan > Search rules |
| DNS zone |
| Zone Name | DNSZone | Configuration > Zones |
| Zone Type | DNS | Configuration > Zones > Zones |
| DNS zone search rule |
| Rule name | DNS zone search rule | Configuration > Dial plan > Search rules |
| Zone name | Search DNS zone (external DNS) | Configuration > Dial plan > Search rules |
| Priority | 150 | Configuration > Dial plan > Search rules |
| Source | All zones | Configuration > Dial plan > Search rules |
| Mode | Alias pattern match | Configuration > Dial plan > Search rules |
| Pattern type | Regex | Configuration > Dial plan > Search rules |
| Pattern string | (?!.*@example\.com.*$).* | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | DNSZone | Configuration > Dial plan > Search rules |
| IP call routing |
| Calls to unknown IP addresses | Direct | Configuration > Dial plan > Configuration |

| Configuration item | Value | Expressway page |
|---|---|---|
| Transform |
| Pattern string | ([^@]*) | Configuration > Dial plan > Transforms |
| Pattern type | Regex | Configuration > Dial plan > Transforms |
| Pattern behavior | Replace | Configuration > Dial plan > Transforms |
| Replace string | \1@example.com | Configuration > Dial plan > Transforms |
| Local search rule 1 |
| Rule name | Local zone – no domain | Configuration > Dial plan > Search rules |
| Priority | 48 | Configuration > Dial plan > Search rules |
| Source | Any | Configuration > Dial plan > Search rules |
| Mode | Alias pattern match | Configuration > Dial plan > Search rules |
| Pattern type | Regex | Configuration > Dial plan > Search rules |
| Pattern string | (.+)@example\.com.* | Configuration > Dial plan > Search rules |
| Pattern behavior | Replace | Configuration > Dial plan > Search rules |
| Replace string | \1 | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | LocalZone | Configuration > Dial plan > Search rules |
| Local search rule 2 |
| Rule name | Local zone – full URI | Configuration > Dial plan > Search rules |
| Priority | 50 | Configuration > Dial plan > Search rules |
| Source | Any | Configuration > Dial plan > Search rules |
| Mode | Alias pattern match | Configuration > Dial plan > Search rules |
| Pattern type | Regex | Configuration > Dial plan > Search rules |
| Pattern string | (.+)@example\.com.* | Configuration > Dial plan > Search rules |
| Pattern behavior | Leave | Configuration > Dial plan > Search rules |
| On successful match | Continue | Configuration > Dial plan > Search rules |
| Target | LocalZone | Configuration > Dial plan > Search rules |