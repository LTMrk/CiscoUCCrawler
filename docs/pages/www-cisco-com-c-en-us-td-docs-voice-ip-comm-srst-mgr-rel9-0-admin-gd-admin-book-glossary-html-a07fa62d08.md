---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-glossary-html-a07fa62d08
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/glossary.html
retrieved_at: 2026-08-21T23:40:33.606188+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Glossary

## Chapter: Glossary

### Glossary

AAA

Authentication, authorization, and accounting. Specifies the failover functionality that you can optionally configure for the authentication server.

backup and restore

Captures the configuration of Cisco Unified SRST Manager so that it can be restored later in case the Cisco Unified SRST Manager configuration becomes corrupted.

capability

Defines what functions a group can perform.

central call agent

Generic term for the Cisco Unified Communications Manager.

central voicemail server

Generic term for the Cisco Unity Connection.

Cisco Unified SRST Manager GUI

Provides the primary administrative interface for configuring Cisco Unified SRST Manager or Enhanced Survivable Remote Site Telephony (E-SRST) . You can access the Cisco Unified SRST Manager graphical user interface from either Firefox or Internet Explorer.

Cisco Unified Communications Manager

A call agent.

Cisco Unified SRST

Cisco Unified Survivable Remote Site Telephony. A system, made up of a central office and one or more branch offices, that provides telephony services during a WAN outage.

cluster

A group of connected devices, such as Cisco Unity Connection, that are managed as a single entity. The devices can be in the same location, or they can be distributed across a network. Any server in the cluster can do the job of any other server in the cluster.

DER

A binary TLS certificate type.

Display Name

User’s name displayed within Cisco Unified SRST Manager applications.

Domain name system (DNS) server

The DNS server provides translation from hostnames to IP addresses.

Enhanced Survivable Remote Site Telephony (E-SRST)

Provides automated remote site provisioning of the following advanced telephony features in survivable mode by gathering the information from Cisco Unified Communications Manager about:

- End-user phones and extensions (speed dials, lines, softkeys)

- Voicemail and call forward configuration

- Call routing restrictions (local and long distance, and time of day)

- Call park and group call park

- Call pickup

- Hunt groups

Group ID

Name of a group of users, usually created to assign members to a Cisco Unified SRST Manager.

log file

A file that lists actions that have occurred.

NAT

Network Address Translation

Network time protocol (NTP)

Used to set the system time to avoid manual configuration of the time. Using NTP helps the system to keep the system time synchronized with the NTP server in case there is a drift in the system clock. NTP typically provides accuracy within a millisecond on LANs and up to a few tens of milliseconds on WANs relative to Coordinated Universal Time. Typical NTP configurations utilize multiple redundant servers and diverse network paths to achieve high accuracy and reliability.

operation

A set of CLI commands or GUI functions.

Password

A Cisco Unified SRST Manager password consists of letters and numbers and is at least 3 characters but not more than 32 characters long.

Password options

For the password used by the user to access the Cisco Unified SRST Manager GUI, select one of the following:

Generate a Random Password—To have Cisco Unified SRST Manager generate a random password.

Blank Password—To leave the password blank.

Password Specified Below—To specify a password for the user. (Default and Recommended)

PAT

Port Address Translation. Network address translation ( NAT ) variant where a single public address is shared for multiple private network devices and port translation is used to expose private services to the public network.

PEM

Privacy Enhanced Mail. A TLS certificate type. It is a Base64 encoded DER certificate, enclosed between “-----BEGIN CERTIFICATE-----” and “-----END CERTIFICATE-----”.

pilot number

The number used to reach a desired service such as voicemail or auto attendant. Typically this number is not visible on IP phones as it is hidden behind the voicemail button on the phone which dials the pilot automatically.

Primary E.164 number

User or group’s primary telephone number, including area code.

privilege

A set of operations that are grouped together. Privileges are assigned to users.

provisioning

The processing performed by Cisco Unified SRST Manager to configure branch site devices for SRST or E-SRST services. The process involves retrieving information from Cisco Unified Communications Manager and converting it to IOS commands for the branch router.

REST

A programmatic interface.

Rights

Member or Owner.

secondary node

A replica of the primary node. It is configured for use in case the primary node fails.

site

A site is created on Cisco Unified SRST Manager based on the existence of a Cisco Unified SRST reference configured on the Cisco Unified Communications Manager.

SMTP

Simple Mail Transfer Protocol (SMTP). standard for e-mail transmissions across the Internet. Formally SMTP is defined in RFC 821 (STD 10) as amended by RFC 1123 (STD 3) chapter 5. The protocol used today is also known as ESMTP and defined in RFC 2821.

SRST

See Cisco Unified SRST.

SRST reference

A gateway that can provide limited Cisco Unified Communications Manager functionality when all other Cisco Unified Communications Manager servers for a device are unreachable.

trace buffer

Collection of debug traces for system activity.

User ID

Alphanumeric user identifier.

| A |  |
|---|---|
| AAA | Authentication, authorization, and accounting. Specifies the failover functionality that you can optionally configure for the authentication server. |

| B |  |
|---|---|
| backup and restore | Captures the configuration of Cisco Unified SRST Manager so that it can be restored later in case the Cisco Unified SRST Manager configuration becomes corrupted. |

| C |  |
|---|---|
| capability | Defines what functions a group can perform. |
| central call agent | Generic term for the Cisco Unified Communications Manager. |
| central voicemail server | Generic term for the Cisco Unity Connection. |
| Cisco Unified SRST Manager GUI | Provides the primary administrative interface for configuring Cisco Unified SRST Manager or Enhanced Survivable Remote Site Telephony (E-SRST) . You can access the Cisco Unified SRST Manager graphical user interface from either Firefox or Internet Explorer. |
| Cisco Unified Communications Manager | A call agent. |
| Cisco Unified SRST | Cisco Unified Survivable Remote Site Telephony. A system, made up of a central office and one or more branch offices, that provides telephony services during a WAN outage. |
| cluster | A group of connected devices, such as Cisco Unity Connection, that are managed as a single entity. The devices can be in the same location, or they can be distributed across a network. Any server in the cluster can do the job of any other server in the cluster. |

| D |  |
|---|---|
| DER | A binary TLS certificate type. |
| Display Name | User’s name displayed within Cisco Unified SRST Manager applications. |
| Domain name system (DNS) server | The DNS server provides translation from hostnames to IP addresses. |

| E |  |
|---|---|
| Enhanced Survivable Remote Site Telephony (E-SRST) | Provides automated remote site provisioning of the following advanced telephony features in survivable mode by gathering the information from Cisco Unified Communications Manager about: End-user phones and extensions (speed dials, lines, softkeys) Voicemail and call forward configuration Call routing restrictions (local and long distance, and time of day) Call park and group call park Call pickup Hunt groups |

| G |  |
|---|---|
| Group ID | Name of a group of users, usually created to assign members to a Cisco Unified SRST Manager. |

| L |  |
|---|---|
| log file | A file that lists actions that have occurred. |

| N |  |
|---|---|
| NAT | Network Address Translation |
| Network time protocol (NTP) | Used to set the system time to avoid manual configuration of the time. Using NTP helps the system to keep the system time synchronized with the NTP server in case there is a drift in the system clock. NTP typically provides accuracy within a millisecond on LANs and up to a few tens of milliseconds on WANs relative to Coordinated Universal Time. Typical NTP configurations utilize multiple redundant servers and diverse network paths to achieve high accuracy and reliability. |

| O |  |
|---|---|
| operation | A set of CLI commands or GUI functions. |

| P |  |
|---|---|
| Password | A Cisco Unified SRST Manager password consists of letters and numbers and is at least 3 characters but not more than 32 characters long. |
| Password options | For the password used by the user to access the Cisco Unified SRST Manager GUI, select one of the following: Generate a Random Password—To have Cisco Unified SRST Manager generate a random password. Blank Password—To leave the password blank. Password Specified Below—To specify a password for the user. (Default and Recommended) |
| PAT | Port Address Translation. Network address translation ( NAT ) variant where a single public address is shared for multiple private network devices and port translation is used to expose private services to the public network. |
| PEM | Privacy Enhanced Mail. A TLS certificate type. It is a Base64 encoded DER certificate, enclosed between “-----BEGIN CERTIFICATE-----” and “-----END CERTIFICATE-----”. |
| pilot number | The number used to reach a desired service such as voicemail or auto attendant. Typically this number is not visible on IP phones as it is hidden behind the voicemail button on the phone which dials the pilot automatically. |
| Primary E.164 number | User or group’s primary telephone number, including area code. |
| privilege | A set of operations that are grouped together. Privileges are assigned to users. |
| provisioning | The processing performed by Cisco Unified SRST Manager to configure branch site devices for SRST or E-SRST services. The process involves retrieving information from Cisco Unified Communications Manager and converting it to IOS commands for the branch router. |

| R |  |
|---|---|
| REST | A programmatic interface. |
| Rights | Member or Owner. |

| S |  |
|---|---|
| secondary node | A replica of the primary node. It is configured for use in case the primary node fails. |
| site | A site is created on Cisco Unified SRST Manager based on the existence of a Cisco Unified SRST reference configured on the Cisco Unified Communications Manager. |
| SMTP | Simple Mail Transfer Protocol (SMTP). standard for e-mail transmissions across the Internet. Formally SMTP is defined in RFC 821 (STD 10) as amended by RFC 1123 (STD 3) chapter 5. The protocol used today is also known as ESMTP and defined in RFC 2821. |
| SRST | See Cisco Unified SRST. |
| SRST reference | A gateway that can provide limited Cisco Unified Communications Manager functionality when all other Cisco Unified Communications Manager servers for a device are unreachable. |

| T |  |
|---|---|
| trace buffer | Collection of debug traces for system activity. |

| U |  |
|---|---|
| User ID | Alphanumeric user identifier. |