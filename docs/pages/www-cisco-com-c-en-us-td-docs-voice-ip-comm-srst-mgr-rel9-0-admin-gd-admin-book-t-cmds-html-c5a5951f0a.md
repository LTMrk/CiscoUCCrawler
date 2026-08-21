---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-t-cmds-html-c5a5951f0a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/t_cmds.html
retrieved_at: 2026-08-21T23:40:29.908598+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: T

## Chapter: T

- trace

## T

Note For information about other CLI commands that are not listed in this document, see Cisco Unity Express Command Reference for 3.0 and Later Versions.

trace

## trace

To view trace messages, use the trace command in EXEC mode.

trace {module {entity {activity}}}

### Syntax Description

module

Trace module values. Can be any combination of the values listed in Table 19 . Entering all gives information for all the modules.

entity

Entity values. Each module has one or more entity values associated with it. Can be any combination of the values for that particular module. See Table 19 . Entering all gives information for all the entities.

activity

Activity values. Each entity has one or more activity values associated with it. Can be any combination of the values for that particular entity. See Table 19 . Entering all gives information for all the activities.

Table 19 lists all the modules, entities, and activities.

Table 19 Module, Entity, and Activity Values

aaa

authorization

jaas

Used for authentication, authorization, and accounting (AAA) debugging

pam

authentication

jaas

pam

acct

service

queue

library

dns

cache

daemon

Domain Name Service (DNS) debugging

localzone

startup

ethconfig

enablecheck

dns_check

debug

ipv4_check

hostname_check

results

dns_query

resolver

send

receive

server

ask

answer

management

agent

debug

Management debugging

webInterface

group

save

GUI debugging

delete

read

user

save

delete

read

aaa

read

privileges

action

axl

delete

post

read

backupRestore

serverConfiguration

restore

backup

controller

startup

request

session

login

logout

webInterface (continued)

sysdb

get

GUI debugging (continued)

set

providerStart

providerGet

providerStop

providerSet

database

query

connection

results

sysdb

producer

nodeDetach

Interprocess communication debugging

nodeAttach

timeLimit

nodeHandle

mkdir

attrCreate

attrDelete

rmdir

lock

acquire

release

wait

traversal

directory

attribute

node

misc

allocation

provider

stop

other

events

deadline

get

startup

commit

check

utility

metaInfo

dealloc

chdir

nameLookup

consumer

set

Interprocess communication debugging (continued)

get

nameLookup

limitsManager

platform

xdebug

System limits debugging

debug

info

warning

crash

error

cli

xdebug

debug

info

warning

crash

error

api

xdebug

debug

info

warning

crash

error

sysdb

xdebug

debug

info

warning

crash

error

license

xdebug

debug

info

warning

crash

error

utilities

xdebug

debug

info

warning

crash

error

limitsManager (continued)

feature

xdebug

System limits debugging (continued)

debug

info

warning

crash

error

mainthread

xdebug

debug

info

warning

crash

error

operation

manager

ucid

Command authorization debugging

operation

license

debug

core_errors

CSL debugging

events

core_events

ipc

errors

agent_info

agent_error

agent_all

core_all

monitor

monitor-license

BackupRestore

BackupRestore

CONF

Backup and restore debugging

SERVER

INIT

OPERATION

HISTORY

dbclient

debug

level0

Database client debugging

level1

level2

level3

level4

level5

sysdb

set

get

commit

database

transaction

query

garbageCollect

connection

largeobject

mgmt

execute

results

superthread

main

startup

Core Java services debugging

parser

parse

snmp

JNI

Net-SNMP

SNMP debugging

agent

debug

rest

base_resources

info

Common REST interface debugging

warn

error

common

info

warn

error

security

policy

password

PIN and password authentication policy debugging

pin

ntp

ntp

loopstatus

Network time protocol debugging

clkselect

clkadj

clockstatus

packets

clkvalidity

peerstats

event

loopfilter

srsx

gui

actions

SRSx GUI debugging

error

cli

debug

SRSx CLI debugging

error

mgmt

debug

SRSx management interface debugging

error

service-point

info

SRSx service point debugging

trace

debug

warning

error

site-manager

info

SRSx site manager debugging

trace

debug

warning

error

srst-engine

info

E-SRST provisioning engine debugging

trace

debug

warning

error

all

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Examples

The following example illustrates the use of the trace srsx srst-engine command:

### Related Commands

log console monitor

Enables log monitor events for debugging.

| module | Trace module values. Can be any combination of the values listed in Table 19 . Entering all gives information for all the modules. |
|---|---|
| entity | Entity values. Each module has one or more entity values associated with it. Can be any combination of the values for that particular module. See Table 19 . Entering all gives information for all the entities. |
| activity | Activity values. Each entity has one or more activity values associated with it. Can be any combination of the values for that particular entity. See Table 19 . Entering all gives information for all the activities. |

| Module Name | Entity Name | Activity Name | Description |
|---|---|---|---|
| aaa | authorization | jaas | Used for authentication, authorization, and accounting (AAA) debugging |
| pam |
| authentication | jaas |
| pam |
| acct | service |
| queue |
| library |
| dns | cache | daemon | Domain Name Service (DNS) debugging |
| localzone |
| startup |
| ethconfig |
| enablecheck | dns_check |
| debug |
| ipv4_check |
| hostname_check |
| results |
| dns_query |
| resolver | send |
| receive |
| server | ask |
| answer |
| management | agent | debug | Management debugging |
| webInterface | group | save | GUI debugging |
| delete |
| read |
| user | save |
| delete |
| read |
| aaa | read |
| privileges | action |
| axl | delete |
| post |
| read |
| backupRestore | serverConfiguration |
| restore |
| backup |
| controller | startup |
| request |
| session | login |
| logout |
| webInterface (continued) | sysdb | get | GUI debugging (continued) |
| set |
| providerStart |
| providerGet |
| providerStop |
| providerSet |
| database | query |
| connection |
| results |
| sysdb | producer | nodeDetach | Interprocess communication debugging |
| nodeAttach |
| timeLimit |
| nodeHandle |
| mkdir |
| attrCreate |
| attrDelete |
| rmdir |
| lock | acquire |
| release |
| wait |
| traversal | directory |
| attribute |
| node |
| misc | allocation |
| provider | stop |
| other |
| events |
| deadline |
| get |
| startup |
| commit |
| check |
| utility | metaInfo |
| dealloc |
| chdir |
| nameLookup |
| consumer | set | Interprocess communication debugging (continued) |
| get |
| nameLookup |
| limitsManager | platform | xdebug | System limits debugging |
| debug |
| info |
| warning |
| crash |
| error |
| cli | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| api | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| sysdb | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| license | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| utilities | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| limitsManager (continued) | feature | xdebug | System limits debugging (continued) |
| debug |
| info |
| warning |
| crash |
| error |
| mainthread | xdebug |
| debug |
| info |
| warning |
| crash |
| error |
| operation | manager | ucid | Command authorization debugging |
| operation |
| license | debug | core_errors | CSL debugging |
| events |
| core_events |
| ipc |
| errors |
| agent_info |
| agent_error |
| agent_all |
| core_all |
| monitor | monitor-license |
| BackupRestore | BackupRestore | CONF | Backup and restore debugging |
| SERVER |
| INIT |
| OPERATION |
| HISTORY |
| dbclient | debug | level0 | Database client debugging |
| level1 |
| level2 |
| level3 |
| level4 |
| level5 |
| sysdb | set |
| get |
| commit |
| database | transaction |
| query |
| garbageCollect |
| connection |
| largeobject |
| mgmt |
| execute |
| results |
| superthread | main | startup | Core Java services debugging |
| parser | parse |
| snmp | JNI | Net-SNMP | SNMP debugging |
| agent | debug |
| rest | base_resources | info | Common REST interface debugging |
| warn |
| error |
| common | info |
| warn |
| error |
| security | policy | password | PIN and password authentication policy debugging |
| pin |
| ntp | ntp | loopstatus | Network time protocol debugging |
| clkselect |
| clkadj |
| clockstatus |
| packets |
| clkvalidity |
| peerstats |
| event |
| loopfilter |
| srsx | gui | actions | SRSx GUI debugging |
| error |
| cli | debug | SRSx CLI debugging |
| error |
| mgmt | debug | SRSx management interface debugging |
| error |
| service-point | info | SRSx service point debugging |
| trace |
| debug |
| warning |
| error |
| site-manager | info | SRSx site manager debugging |
| trace |
| debug |
| warning |
| error |
| srst-engine | info | E-SRST provisioning engine debugging |
| trace |
| debug |
| warning |
| error |
| all |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| log console monitor | Enables log monitor events for debugging. |