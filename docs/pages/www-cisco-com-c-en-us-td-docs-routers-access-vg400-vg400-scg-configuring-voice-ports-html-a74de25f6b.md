---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg400-vg400-scg-configuring-voice-ports-html-a74de25f6b
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg400/vg400-scg/configuring-voice-ports.html
retrieved_at: 2026-08-22T01:18:51.399711+00:00
---

Cisco VG400 Voice Gateway Software Configuration Guide

# Cisco VG400 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring Voice Ports

## Chapter: Configuring Voice Ports

# Configuring Voice Ports

This chapter explains how to configure voice ports using the commands specific for Cisco VG400 Analog Voice Gateways and associated
                        service modules.

This chapter contains the following topics:

## Prerequisite

Before you configure voice ports on Cisco Voice Gateway VG400, you must establish a working IP network.

To configure sipline support on a device that runs on Cisco IOS XE 17.8.1 or later, ensure that the CUCM version is 14.0 SU1
                                 or later.

## Configuring the Voice Port

This section discuss the changes and modifications on the following commands:

### loop-length

The loop-length CLI is created to configure the analog FXS voice port. It has the following format:

voice-port x/y/z

[no] loop-length [long | short]

The loop-length CLI has the following characteristics:

For the Cisco VG400 platform, the default is short loop-length. This command is not applicable to analog FXS on motherboard
                                    slot.

This command is applicable to all 48 FXS voice ports on SM-D-48FXS-E and the first 4 (0-3) FXS voice ports on SM-D-72FX like
                                    the Cisco VG400 platform.

The default FXS is short loop-length and long loop-length FXS needs to be configured.

The first eight voice ports 0/0/0-7 can be configured as long loop (OPX-lite).

FXS voice ports on VIC 1 (0/1/0 - 0/1/23) will not support long loop. By default, they are short-loop FXS.

Shutdown and no shutdown are required on the voice port after loop-length is configured for it totake effect.

Because up to 2 ren is supported on long-loop (OPX-lite) FXS, when loop-length long is configured on the FXS voice port, if
                                    its existing ren configuration is greater than 2, it will be changed automatically to 2, a message “The existing ren configuration
                                    is changed to 2" is displayed on the console.

When loop-length short is configured on the FXS voice port, if the voice port has ring dc-offset configured, the ring dc-offset
                                    configuration will be removed. A message “The existing ring dc-offset configuration is removed” is displayed on the console.

### ren

The existing ren CLI under FXS voice port will accept value 1-2 for FXS voice port with loop-length long configured. For short
                              loop-length analog FXS voice port, ren CLI will accept value 1-5.

### ren dc-offset

The existing ring dc-offset CLI is configurable on the long loop-length FXS voice port.

### cm-current-enhance

The existing cm-current-enhance CLI is configurable on the long loop-length FXS voice port.

### vmwi

The existing vmwi [fsk | dc-voltage] is configurable on all on-board FXS voice ports.

For configuration examples, see Cisco VG400 Configuration Examples .

## Cisco IOS Bulk Configuration

An optional bulk-configuration mechanism for voice-port and voice dial peer is available to save on time.

### group

The group option is added to dial-peer CLI for dial peer bulk configuration. It has the following formats:

dial-peer group <tag> pots

dial-peer group <tag> pots all stcapp

The second command from the above list will create dial peers on all analog voice ports as stcapp ports by expanding it to
                              the following three commands:

```
dial-peer group <tag> pots
service stcapp
port all
```

The group command is specific for stcapp-controlled analog ports. Therefore, only a subset of dial peer commands are supported,
                              which are as follows:

port

description

service

shutdown

preference

The port subcommand specifies what ports to configure for a specific group command.  It has the following formats:

```
port <voice port#> [ans | called | dest] <E164 address> [desc <description>]
port <voice port#> [desc <description>]
port <voice port#>
port <start voice port#>-<end port#> [ans | called | dest] <E164 address> <interval>
[desc <description>]
port <start voice port#>-<end port#> [ans | called | dest] <E164 address> [desc
<description>]
port <start voice port#>-<end port#> [desc <description>]
port <start voice port#>-<end port#>
port all [ans | called | dest] <E164 address> <interval> [desc <description>]
port all [ans | called | dest] <E164 address> [desc <description>]
port all [desc <description>]
port all
```

The voice port# is composed of slot#/subunit#/port# or slot#/port# .

The ans is the abbreviation for answer-address , which has the same meaning as the subcommand under dial-peer voice <tag> pots .

The called is the abbreviation for incoming called-number , which has the same meaning as the subcommand under dial-peer voice <tag> pots .

The dest is the abbreviation for description , which has the same meaning as the subcommand under dial-peer voice <tag> pots .

The <interval> denotes the interval value of the E164 number for each adjacent port. The default is zero and the allowable value is from
                                    1 to 100, inclusively.

Multiple port commands are allowed and can be removed one by one with exact port specification or all at once using no port all .

No overlay port commands are allowed. As a result, no other port commands are allowed if port all is configured.