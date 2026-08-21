---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-s-cmds-html-ee13c90a7d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/s_cmds.html
retrieved_at: 2026-08-21T23:40:25.875705+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: S

## Chapter: S

## s how clock

To display clock statistics, use the show clock command in EXEC mode.

show clock

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

Cisco Unified SRST Manager uses the Network Time Protocol (NTP) server for clocking functions. Use the show clock command to display the Cisco Unified SRST Manager clock status.

### Examples

The following is sample output for the show clock command:

Table 16 describes the significant fields shown in the display.

Table 16 show clock Field Descriptions

time zone

Current time zone setting.

clock state

Synchronization state of the clock.

delta from reference (ms)

Difference between the module clock and the NTP reference clock.

time of day (sec)

Current time of day in seconds.

time of day (ms)

Current time of day in microseconds.

### Related Commands

ntp server

Specifies the NTP server for Cisco Unified SRST Manager.

show ntp

Displays the time source for an NTP server.

## sh ow configuration

To display the contents of the non-volatile memory, use the show configuration command in EXEC mode.

show configuration

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

Use this command for troubleshooting.

### Examples

The following is sample output for the show configuration command:

### Related Commands

backup category

Specifies the type of data to be backed up and initiates the backup process.

hostname

Specifies the hostname of the current messaging gateway.

ip domain-name

Specifies the local messaging gateway’s domain name and/or domain name server.

restore factory default

Restores factory default settings.

## s how interfaces

To display the IP configuration and statistics for the Ethernet interface, use the show interfaces command in privileged EXEC mode.

show interfaces

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Examples

The following is sample output for the show interfaces command:

### Related Commands

ip name-server

Specifies the domain name server.

## s how ip dns cache

To display the DNS cache, use the show ip dns cache command in EXEC mode.

show ip dns cache

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Examples

The following is sample output for the show ip dns cache command:

### Related Commands

hostname

Specifies the hostname for the current configuring Cisco Unified SRST Manager.

ip name-server

Specifies the domain name server.

ntp server

Specifies the NTP clocking server.

show hosts

Displays all configured hosts.

## s how license status

To display the license agreement, use the show license status command in EXEC mode.

show license status

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Examples

The following is sample output for the show license status command:

## sh ow log name

To display logging data, use the show log name command in EXEC mode.

show log name word [ containing expression | paged | tail ]

### Syntax Description

word

The name of the log file to display. Use the show logs command to display a list of available log files.

containing expression

Only displays events that match a search expression.

paged

Displays in paged mode.

tail

Displays the latest events as they occur.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

This command has the following filtering options:

- show begin : Begins the output of any show command from a specified string.

- show exclude : Filters show command output so that it excludes lines that contain a particular regular expression.

- show include : Filters show command output so that it displays only lines that contain a particular regular expression.

### Examples

The following partial output for the show log name command displays the dmesg log:

The following sample output for the show log command displays the dmesg log using a search string:

The following partial output for the show log command displays the dmesg log in paged mode:

The following output for the show log name command displays the current dmesg log as events are being entered:

The following partial output for the show log name command displays the dmesg log beginning with the first line starting with ide0:

### Related Commands.

log console

Configures the types of messages to be displayed on the console.

log console monitor

Displays system messages on the console.

log server address

Specifies an external server for saving log messages.

log trace boot

Saves the trace configuration on rebooting.

log trace buffer save

Saves the current trace information.

show logging

Shows the types of messages that are displayed on the console.

show logs

Displays the list of available logs.

## sh ow ntp

To display the time source for a Network Time Protocol (NTP) server, use the show ntp command in EXEC mode.

show ntp [ detail ]

### Syntax Description

detail

Displays detailed information about the NTP servers.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

This command displays the chain of NTP servers back to their primary time source, starting from the local host.

### Examples

The following is sample output for the show ntp command:

Table 17 describes the significant fields shown in the display.

Table 17 show ntp Field Descriptions

(first field)

IP address of the host.

stratum

Server hop count to the primary clock source. Valid values are:

- 0—Unspecified

- 1—Primary clock reference

- 2–255—Secondary reference via NTP

offset

Time offset between the host and the local host, in seconds.

synch distance

Host synchronization distance, which is the estimated error relative to the primary source.

The following is sample output for the show ntp detail command:

Table 18 describes the significant fields shown in the display.

Table 18 show ntp detail Field Descriptions

server

IP address of the host server.

port

Port number of the host server.

stratum

Server hop count to the primary clock source. Valid values are:

- 0—Unspecified

- 1—Primary clock reference

- 2–255—Secondary reference via NTP

precision

Precision of the clock, in seconds to the power of two.

leap

Two-bit code warning of an impending leap second to be inserted in the NTP time scale. Valid values are:

- 00—No warning

- 01—Last minute was 61 seconds

- 10—Last minute was 59 seconds

- 11—Alarm condition (clock not synchronized)

refid

IP address of the peer selected for synchronization.

delay

Round-trip delay of the packet, in milliseconds.

dispersion

Measure, in milliseconds, of how scattered the time offsets have been from a given time server.

offset

Time offset between the host and the local host, in seconds.

rootdelay

Total round-trip delay, in seconds, to the primary reference source at the root of the synchronization subnet.

rootdispersion

Maximum error, in seconds, relative to the primary reference source at the root of the synchronization subnet.

synch dist

Host synchronization distance, which is the estimated error relative to the primary source.

reference time

Local time, in time-stamp format, when the local clock was last updated. If the local clock has never been synchronized, the value is zero.

originate timestamp

Local time, in time-stamp format, at the peer when its latest NTP message was sent. If the peer becomes unreachable, the value is zero.

transmit timestamp

Local time, in time-stamp format, when the latest NTP message from the peer arrived. If the peer becomes unreachable, the value is zero.

### Related Commands

ntp server

Configures the Network Time Protocol (NTP) server to keep the system time synchronized with the NTP server.

show clock

Displays clock statistics.

## show srsx central-call-agent

To display the list of configured Cisco Unified Communications Manager systems or details for the specified Cisco Unified Communications Manager system, use the show srsx central-call-agent command.

show srsx central-call-agent [ hostname [ srst-references | nodes ]]

### Syntax Description

hostname

Hostname of a specific Cisco Unified Communications Manager system.

srst-references

Displays the Cisco Unified SRST references for the specified Cisco Unified Communications Manager system.

nodes

Displays all the nodes discovered for the Cisco Unified Communications Manager system.

## Command Modes

EXEC mode

### Command History

9.0

This command was introduced.

### Usage Guidelines

This information is also available in the Cisco Unified SRST Manager graphical user interface, which we recommend that you use as the primary administrative interface.

### Examples

The following is an example of the show srsx central-call-agent command:

The following is an example of the show srsx central-call-agent command with a central call agent specified:

The following is an example of the show srsx central-call-agent command with a central call agent specified and asking for a list of the Cisco Unified SRST references:

The following is an example of the show srsx central-call-agent command with a central call agent specified and asking for a list of the nodes discovered for the central call agent:

### Related Commands

show srsx site

Displays the sites on the Cisco Unified SRST system.

## show srsx provisioning-history

To display the provisioning history for all sites, use the show srsx provisioning-history command.

show srsx provisioning-history

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC mode

### Command History

9.0

This command was introduced.

### Usage Guidelines

This information is also available in the Cisco Unified SRST Manager graphical user interface, which we recommend that you use as the primary administrative interface.

### Examples

The following is an example of the show srsx provisioning-history command in Cisco Unified SRST Manager 9.0:

The following is an example of the show srsx provisioning-history command in Cisco Unified SRST Manager 9.0:

### Related Commands

show srsx central-call-agent

Displays the central call agents available on the Cisco Unified SRST system.

show srsx site

Displays the sites on the Cisco Unified SRST system.

## show srsx site

To display the list of sites managed by the Cisco Unified SRST Manager or to see details for the specified site, use the show srsx site command.

show srsx site [ sitename ]

### Syntax Description

sitename

Name of a specific site.

## Command Modes

EXEC mode

### Command History

9.0

This command was introduced.

### Usage Guidelines

This information is also available in the Cisco Unified SRST Manager graphical user interface, which we recommend that you use as the primary administrative interface.

### Examples

The following is an example of the show srsx site command:

The following is an example of the show srsx site command with a site specified:

### Related Commands

show srsx central-call-agent

Displays the central call agents available on the Cisco Unified SRST system.

## show srsx site-template

To display the site provisioning templates used when provisioning Cisco Unified SRST Manager devices, use the show srsx site-template command.

show srsx site-template [ default ] | [ name ] | [ auto-learned ]

### Syntax Description

default

Displays default site provisioning templates.

name

Displays details for the selected template.

auto-learned

Displays site provisioning templates for auto-learned sites.

## Command Modes

EXEC mode

### Command History

9.0

This command was introduced.

### Usage Guidelines

This information is also available in the Cisco Unified SRST Manager graphical user interface, which we recommend that you use as the primary administrative interface.

### Examples

The following is an example of the show srsx site-template command in which the voicemail pilot has been auto-learned:

### Related Commands

show srsx central-call-agent

Displays the central call agents available on the Cisco Unified SRST system.

show srsx site

Displays the sites on the Cisco Unified SRST system.

## show srsx system-settings

To display the global Cisco Unified survivable remote system configuration values, use the show srsx system-settings command.

show srsx system-settings

### Syntax Description

This command has no arguments or keywords.

## Command Modes

EXEC mode

### Command History

9.0

This command was introduced.

### Usage Guidelines

This information is also available in the Cisco Unified SRST Manager GUI, which we recommend that you use as the primary administrative interface.

### Examples

The following is an example of the show srsx system-settings command:

### Related Commands

show srsx central-call-agent

Displays the central call agents available on the Cisco Unified SRST Manager system.

show srsx site

Displays the sites on the Cisco Unified SRST Manager system.

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Field | Description |
|---|---|
| time zone | Current time zone setting. |
| clock state | Synchronization state of the clock. |
| delta from reference (ms) | Difference between the module clock and the NTP reference clock. |
| time of day (sec) | Current time of day in seconds. |
| time of day (ms) | Current time of day in microseconds. |

| Command | Description |
|---|---|
| ntp server | Specifies the NTP server for Cisco Unified SRST Manager. |
| show ntp | Displays the time source for an NTP server. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| backup category | Specifies the type of data to be backed up and initiates the backup process. |
| hostname | Specifies the hostname of the current messaging gateway. |
| ip domain-name | Specifies the local messaging gateway’s domain name and/or domain name server. |
| restore factory default | Restores factory default settings. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| ip name-server | Specifies the domain name server. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| hostname | Specifies the hostname for the current configuring Cisco Unified SRST Manager. |
| ip name-server | Specifies the domain name server. |
| ntp server | Specifies the NTP clocking server. |
| show hosts | Displays all configured hosts. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| word | The name of the log file to display. Use the show logs command to display a list of available log files. |
|---|---|
| containing expression | Only displays events that match a search expression. |
| paged | Displays in paged mode. |
| tail | Displays the latest events as they occur. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| log console | Configures the types of messages to be displayed on the console. |
| log console monitor | Displays system messages on the console. |
| log server address | Specifies an external server for saving log messages. |
| log trace boot | Saves the trace configuration on rebooting. |
| log trace buffer save | Saves the current trace information. |
| show logging | Shows the types of messages that are displayed on the console. |
| show logs | Displays the list of available logs. |

| detail | Displays detailed information about the NTP servers. |
|---|---|

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Field | Description |
|---|---|
| (first field) | IP address of the host. |
| stratum | Server hop count to the primary clock source. Valid values are: 0—Unspecified 1—Primary clock reference 2–255—Secondary reference via NTP |
| offset | Time offset between the host and the local host, in seconds. |
| synch distance | Host synchronization distance, which is the estimated error relative to the primary source. |

| Field | Description |
|---|---|
| server | IP address of the host server. |
| port | Port number of the host server. |
| stratum | Server hop count to the primary clock source. Valid values are: 0—Unspecified 1—Primary clock reference 2–255—Secondary reference via NTP |
| precision | Precision of the clock, in seconds to the power of two. |
| leap | Two-bit code warning of an impending leap second to be inserted in the NTP time scale. Valid values are: 00—No warning 01—Last minute was 61 seconds 10—Last minute was 59 seconds 11—Alarm condition (clock not synchronized) |
| refid | IP address of the peer selected for synchronization. |
| delay | Round-trip delay of the packet, in milliseconds. |
| dispersion | Measure, in milliseconds, of how scattered the time offsets have been from a given time server. |
| offset | Time offset between the host and the local host, in seconds. |
| rootdelay | Total round-trip delay, in seconds, to the primary reference source at the root of the synchronization subnet. |
| rootdispersion | Maximum error, in seconds, relative to the primary reference source at the root of the synchronization subnet. |
| synch dist | Host synchronization distance, which is the estimated error relative to the primary source. |
| reference time | Local time, in time-stamp format, when the local clock was last updated. If the local clock has never been synchronized, the value is zero. |
| originate timestamp | Local time, in time-stamp format, at the peer when its latest NTP message was sent. If the peer becomes unreachable, the value is zero. |
| transmit timestamp | Local time, in time-stamp format, when the latest NTP message from the peer arrived. If the peer becomes unreachable, the value is zero. |

| Command | Description |
|---|---|
| ntp server | Configures the Network Time Protocol (NTP) server to keep the system time synchronized with the NTP server. |
| show clock | Displays clock statistics. |

| hostname | Hostname of a specific Cisco Unified Communications Manager system. |
|---|---|
| srst-references | Displays the Cisco Unified SRST references for the specified Cisco Unified Communications Manager system. |
| nodes | Displays all the nodes discovered for the Cisco Unified Communications Manager system. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| show srsx site | Displays the sites on the Cisco Unified SRST system. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| show srsx central-call-agent | Displays the central call agents available on the Cisco Unified SRST system. |
| show srsx site | Displays the sites on the Cisco Unified SRST system. |

| sitename | Name of a specific site. |
|---|---|

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| show srsx central-call-agent | Displays the central call agents available on the Cisco Unified SRST system. |

| default | Displays default site provisioning templates. |
|---|---|
| name | Displays details for the selected template. |
| auto-learned | Displays site provisioning templates for auto-learned sites. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| show srsx central-call-agent | Displays the central call agents available on the Cisco Unified SRST system. |
| show srsx site | Displays the sites on the Cisco Unified SRST system. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| show srsx central-call-agent | Displays the central call agents available on the Cisco Unified SRST Manager system. |
| show srsx site | Displays the sites on the Cisco Unified SRST Manager system. |