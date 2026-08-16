---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr3-vcr3-cr-book-vcr-q1-html-3c344cdbf4
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr3/vcr3-cr-book/vcr-q1.html
retrieved_at: 2026-08-16T23:18:48.811844+00:00
---

Cisco IOS Voice Command Reference - K through R

# Cisco IOS Voice Command Reference - K through R

Updated: December 21, 2024

Chapter: Q

## Chapter: Q

# Q

## q850-cause

To map a Q.850 call-disconnect cause code to a different Q.850 call-disconnect cause code, use the q850-cause command in application-map configuration mode. To disable the code-to-code mapping, use the no form of this command.

q850-cause code-id q850-cause code-id

no q850-cause code-id q850-cause code-id

### Syntax Description

code-id

Q.850 call-disconnect cause code to be mapped. Range: 1 to 127.

### Command Default

No mapping occurs.

### Command Modes

Application-map

## Command History

Release

Modification

12.4(9)T

This command was introduced.

### Usage Guidelines

Use this command to map a Q.850 call-disconnect cause code to any different Q.850 call-disconnect cause code.

Use this command in conjunction with the application and map commands.

This command operates only on incoming H.323 call legs that are disconnected by a call-control application.

## Examples

The following example maps cause code 34 to cause code 17:

```
Router(config)# application Router(config-app)# map Router(config-app-map)# q850-cause 34 q850-cause 17
```

### Related Commands

Command

Description

application

Enables a specific application on a dial peer.

map

Enables mapping.

map q850-cause

Maps a Q.850 call-disconnect cause code to a tone.

progress_ind

Sets a specific progress indicator in Call Setup, Progress, or Connect messages from an H.323 VoIP gateway.

## qsig decode

To enable decoding for QSIG supplementary services, use the qsig decode command in voice service configuration mode. To reset to the default, use the no form of this command.

qsig decode

no qsig decode

### Syntax Description

This command has no keywords or arguments.

### Command Default

QSIG decoding is disabled.

### Command Modes

Voice service configuration

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command decodes application protocol data units (APDUs) for supplementary services. If this command is not enabled, data
                              units are not interpreted and are tunneled through the router.

## Examples

The following example enables QSIG decoding:

```
Router(config)# voice service voip Router(conf-voi-serv)# qsig decode
```

### Related Commands

Command

Description

supplementary-service h450.7

Globally enables H.450.7 supplementary services capabilities exchange.

## query-interval

To configure the interval at which the local border element (BE) queries the neighboring BE, use the query - interval command in Annex G Neighbor BE Configuration mode. To remove the interval, use the no form of this command.

query-interval query-interval

no query-interval

### Syntax Description

query - interval

Frequency, in minutes, at which this BE should query the specified neighbor BE for descriptors. Default is 30. A value of
                                          0 disables periodic querying.

### Command Default

30 minutes

### Command Modes

Annex G Neighbor BE configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Use this command to configure the interval at which the local BE queries the neighboring BE. Use this command only if you
                              want a query interval other than 30 minutes.

## Examples

The following example sets the query interval to 45 minutes:

```
Router(config-annexg-neigh)# query-interval 45
```

### Related Commands

Command

Description

emulate

Configures the local BE to cache the descriptors received from its neighbors. If caching is enabled, the neighbors are queried
                                          at the specified interval for their descriptors.

local

Configures the identifier for the neighbor BE.

session transport

Configures the neighbor’s port number that is used for exchanging Annex G messages.

| code-id | Q.850 call-disconnect cause code to be mapped. Range: 1 to 127. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(9)T | This command was introduced. |

| Command | Description |
|---|---|
| application | Enables a specific application on a dial peer. |
| map | Enables mapping. |
| map q850-cause | Maps a Q.850 call-disconnect cause code to a tone. |
| progress_ind | Sets a specific progress indicator in Call Setup, Progress, or Connect messages from an H.323 VoIP gateway. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| supplementary-service h450.7 | Globally enables H.450.7 supplementary services capabilities exchange. |

| query - interval | Frequency, in minutes, at which this BE should query the specified neighbor BE for descriptors. Default is 30. A value of
                                          0 disables periodic querying. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| emulate | Configures the local BE to cache the descriptors received from its neighbors. If caching is enabled, the neighbors are queried
                                          at the specified interval for their descriptors. |
| local | Configures the identifier for the neighbor BE. |
| session transport | Configures the neighbor’s port number that is used for exchanging Annex G messages. |