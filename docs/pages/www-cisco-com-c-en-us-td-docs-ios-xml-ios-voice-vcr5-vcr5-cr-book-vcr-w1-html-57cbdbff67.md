---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-w1-html-57cbdbff67
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-w1.html
retrieved_at: 2026-08-16T23:14:33.464115+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: W

## Chapter: W

- W

- watcher all

- xsvc

# W

## watcher all

To allow an external watcher to monitor an internal presentity, use the watcher all command in presence configuration mode. To disable monitoring by external watchers, use the no form of this command.

watcher all

no watcher all

### Syntax Description

This command has no arguments or keywords.

### Command Default

Only internal watchers are allowed when presence is enabled.

### Command Modes

Presence configuration (config-presence)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command allows external watchers on a remote router connected through a SIP trunk to monitor internal directory numbers.
                              You must enable the allow watch command on the internal directory numbers that are watched. To allow external watching from the remote router, you must enable
                              the allow subscribe command on the remote router.

## Examples

The following example shows how to enable external watching of an internal presentity:

```
Router(config)# presence Router(config-presence)# watcher all
```

### Related Commands

Command

Description

allow subscribe

Allows internal watchers to monitor external presentities.

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service.

presence

Enables presence service on the router and enters presence configuration mode.

presence enable

Allows incoming presence requests from SIP trunks.

server

Specifies the IP address of a presence server for sending presence requests from internal watchers to external presence entities.

show presence global

Displays configuration information about the presence service.

show presence subscription

Displays information about active presence subscriptions.

## xsvc

To add support for extended serviceability (xsvc) on TDM, (ISDN-PRI/BRI, DS0-group, analog voice-port) voice interfaces,
                              which are defined as a trunk group, use the xsvc command. To disable support for extended serviceability, use the no form of this command.

no xsvc

### Syntax Description

This command has no arguments or keywords.

### Command Default

Extended serviceability is disabled on trunk groups.

### Command Modes

Trunk group configuration

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use this command to add support for extended serviceability on voice interfaces which are defined as a trunk group.

## Examples

The following example enables monitoring on a trunk group.

```
Router(config)# trunk group tdm-tg1 Router(config-trunk-group)# xsvc
```

### Related Commands

Command

Description

provider

Enables a provider service.

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| allow subscribe | Allows internal watchers to monitor external presentities. |
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service. |
| presence | Enables presence service on the router and enters presence configuration mode. |
| presence enable | Allows incoming presence requests from SIP trunks. |
| server | Specifies the IP address of a presence server for sending presence requests from internal watchers to external presence entities. |
| show presence global | Displays configuration information about the presence service. |
| show presence subscription | Displays information about active presence subscriptions. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| provider | Enables a provider service. |