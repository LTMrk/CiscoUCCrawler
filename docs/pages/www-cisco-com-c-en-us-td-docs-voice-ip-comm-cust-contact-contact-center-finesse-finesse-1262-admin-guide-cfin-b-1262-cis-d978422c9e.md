---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1262-admin-guide-cfin-b-1262-cis-d978422c9e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1262/admin/guide/cfin_b_1262_cisco-finesse-administration-guide/cfin_m_1261-supported-cisco-unified-communications-os.html
retrieved_at: 2026-08-21T15:56:15.586862+00:00
---

Cisco Finesse Administration Guide, Release 12.6(2)

# Cisco Finesse Administration Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Supported Cisco Unified Communications OS Services

## Chapter: Supported Cisco Unified Communications OS Services

- Supported Cisco Unified Communications OS Services

- Supported Cisco Unified Communications OS Services

# Supported Cisco Unified Communications OS Services

## Supported Cisco Unified Communications OS Services

The following sections list the Cisco Unified Communications OS services that Cisco Finesse supports. For more information
                              about CLI commands, see Command Line Interface Guide for Cisco Unified Communications Solutions .

Other commands listed in the Command Line Interface Guide for Cisco Unified Communications Solutions are not tested or qualified for Finesse. Some of those commands may return only platform-specific information. Others may
                                          not work for Finesse. Finesse supports only the commands from the guide that are listed here.

Some of these commands may warn about invalidating a software license. As Finesse is not a licensed server, you can disregard
                                          these warnings.

### File Commands

file check

file delete

file get

file list

file search

file tail

file view

### Show Commands

show account

show date

show disk usage

show hardware

show logins

show myself

show network

show network ipprefs

show open

show packages

show perf

show status

show tech all

show tech dberrcode

show tech gateway

show tech locales

show tech params

show tech prefs

show tech repltimeout

show tech runtime

show tech systables

show tech systems

show tech version

show timezone

show trace

show version

show network ipv6 settings

show tls server min-version

show tls client min-version

### Utils Commands

utils core active list

utils core inactive list

utils csa enable

utils csa disable

utils csa status

utils dbreplication clusterreset

utils dbreplication dropadmindb

utils dbreplication forcedatasyncsub

utils dbreplication reset

utils dbreplication runtimestate

utils dbreplication setrepltimeout

utils dbreplication stop

utils diagnose test

utils firewall ipv4

utils iostat

utils network arp

utils network capture eth0

utils network connectivity

utils network host

utils network ping

utils network traceroute

utils ntp

utils ntp config

utils ntp restart

utils ntp server add

utils ntp server delete

utils ntp server list

utils ntp status

utils ntp start

utils remote_account

utils reset_application_ui_administrator_name

utils reset_application_ui_administrator_password

utils service

utils system

utils system boot

utils system restart

utils system upgrade

utils vmtools status

### Set Commands

set network ipv6 gateway

set network ipv6 service disable

set network ipv6 service enable

set network ipv6 static_address

set tls server min-version <version>

set tls client min-version <version>

Cisco SNMP integration with Finesse is restricted to platform MIBs. Finesse does not have any application-specific MIBs.

| Note | Other commands listed in the Command Line Interface Guide for Cisco Unified Communications Solutions are not tested or qualified for Finesse. Some of those commands may return only platform-specific information. Others may
                                          not work for Finesse. Finesse supports only the commands from the guide that are listed here. Some of these commands may warn about invalidating a software license. As Finesse is not a licensed server, you can disregard
                                          these warnings. |
|---|---|

| Note | Cisco SNMP integration with Finesse is restricted to platform MIBs. Finesse does not have any application-specific MIBs. |
|---|---|