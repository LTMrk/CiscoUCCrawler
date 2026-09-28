---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr4-vcr4-cr-book-vcr-s9-html-11a89fc396
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr4/vcr4-cr-book/vcr-s9.html
retrieved_at: 2026-08-16T23:18:03.231968+00:00
---

Cisco IOS Voice Command Reference - S commands

# Cisco IOS Voice Command Reference - S commands

Updated: December 20, 2025

Chapter: show vdev through show voice statistics memory-usage

## Chapter: show vdev through show voice statistics memory-usage

# show vdev through show voice statistics memory-usage

## show vdev

To display information about the digital signal processors (DSPs) on a specific card, use the show vdev command in privileged
                              EXEC mode.

show vdev { slot / port }

### Syntax Description

slot

Slot in which the voice card resides.

port

Port on the voice card.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(2)T

This command was introduced on the Cisco AS5850.

### Usage Guidelines

This command can be used on the standby and active route switch controller (RSC) to verify that dynamic and bulk synchronization
                              have been performed correctly on a specified port.

## Examples

The following example shows the output for the last port on a 324 universal port card.

```
Router# show vdev 2/323 flags = 0x0000
dev_status = 0x0000
service = 0x0000
service_type = 0x0
min_speed = 0, max_speed = 0
modulation = 0, err_correction = 0, compression = 0
csm_call_info = 0x0, csm_session = Invalid
vdev_p set to modem_info
DSPLIB information:
dsplib_state = 0x0
dsplib_next_action = 0x0
HDLC information:
call_id = 0x0
called_number = 
speed = 0
ces = 0x0
spc = FALSE
d_idb = 0x0
Bulk sync reference = 2, Global bulk syncs = 2
```

The table below displays significant fields shown in the output.

Field

Description

flags

Internal vdev flags

dev_status

Additional flags giving status of the resource

service

Service currently running on this DSP

service_type

Service type as passed in by RPM

min_speed

Minimum configured modem speed

max_speed

Maximum configured modem speed

modulation

Maximum modulation to be negotiated

err_correction

Error correction to be negotiated

compression

Compression to be negotiated

csm_call_info

Address of the associated csm_call_info structure

csm_session

Session ID as maintained by CSM

vdev_p

Address of the associated resource structure

dsplib_state

State of the resource as seen by the DSPLIB

dsplib_next_action

Next DSPLIB action that should be taken on this resource

call_id

Call identifier if this resource has a HDLC call

called_number

Called number if this resource has a HDLC call

speed

Speed of the connection if this resource has a HDLC call

ces

Circuit emulation service information

spc

True if semi permanent call link

d_idb

Address of the associated D channel idb, if this resource has a HDLC call

Bulk sync reference

Number of times that this resource has been bulk synchronized

Global bulk syncs

Number of bulk synchronizations that the VDEV High Availability client has performed

### Related Commands

Command

Description

debug vdev

Turns on debugging for voice devices.

show redundancy

Displays current or historical status and related information on a redundant RSC.

## show vfc

To see the entries in the host-name-and-address cache, use the show vfc command in privileged EXEC mode.

show vfc slot-number [ technology ]

### Syntax Description

slot - number

VFC slot number.

technology

(Optional) Displays the technology type of the VFC.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3 NA

This command was introduced on the Cisco AS5300.

12.0(2)XH

The technology keyword was added.

## Examples

The following is sample output from this command showing that the card in slot 1 is a C549 DSPM:

```
Router# show vfc 1 technology Technology in VFC slot 1 is C549
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

voice-card

Configures a voice card and enters voice-card configuration mode.

## show vfc cap-list

To show the current list of files on the capability list for this voice feature card (VFC), use the show vfc cap - list command in user EXEC mode.

show vfc slot cap-list

### Syntax Description

slot

Slot where the VFC is installed. Range is from 0 to 2.

### Command Modes

User EXEC (>)

## Command History

Release

Modification

11.3 NA

This command was introduced on the Cisco AS5300.

## Examples

The following is sample output from this command:

```
Router# show vfc 1 cap-list Capability List for VFC in slot 1:
1. fax-vfc-l.0.1.bin
2. bas-vfc-l.0.1.bin
3. cdc-g729-l.0.1.bin
4. cdc-g711-l.0.1.bin
5. cdc-g726-l.0.1.bin
6. cdc-g728-l.0.1.bin
7. cdc-gsmfr-l.0.1.bin
```

The first line in this output is a general description, stating that this is the capability list for the VFC residing in slot
                              1. Below this is a numbered list, each line of which identifies one currently installed in-service file.

### Related Commands

Command

Description

show vfc default - file

Displays the default files included in the default file list for this VFC.

show vfc directory

Displays the list of all files residing on this VFC.

show vfc version

Displays the version of the software residing on this VFC.

## show vfc default-file

To show the default files included in the default file list for a voice feature card (VFC), use the show vfc default - file command in user EXEC mode.

show vfc slot default-file

### Syntax Description

slot

Slot where the VFC is installed. Range is from 0 to 2.

### Command Modes

User EXEC (>)

## Command History

Release

Modification

11.3 NA

This command was introduced on the Cisco AS5300.

## Examples

The following is sample output from this command:

```
Router# show vfc 1 default-file Default List for VFC in slot 1:
1. btl-vfc-l.0.13.0.bin
2. cor-vfc-l.0.1.bin
3. bas-vfc-l.0.1.bin
4. cdc-g729-l.0.1.bin
5. fax-vfc-l.0.1.bin
6. jbc-vfc-l.0.13.0.bin
```

The first line in this output is a general description, stating that this is the default list for the VFC residing in slot
                              1. Below this is a numbered list, each line of which identifies one default file.

### Related Commands

Command

Description

show vfc cap - list

Displays the current list of files on the capability list for this VFC.

show vfc directory

Displays the list of all files residing on this VFC.

show vfc version

Displays the version of the software residing on this VFC.

## show vfc directory

To show the list of all files residing on a voice feature card (VFC), use the show vfc directory command in user EXEC mode.

show vfc slot directory

### Syntax Description

slot

Slot where the VFC is installed. Range is from 0 to 2.

### Command Modes

User EXEC (>)

## Command History

Release

Modification

11.3 NA

This command was introduced on the Cisco AS5300.

### Usage Guidelines

Use this command to display a list of all of the files currently stored in Flash memory for a particular VFC.

## Examples

The following is sample output from this command:

```
Router# show vfc 1 directory Files in slot 1  VFC flash:
     File Name                        Size (Bytes)
1 .  vcw-vfc-mz.gsm.VCW               292628
2 .  btl-vfc-l.0.13.0.bin             4174
3 .  cor-vfc-l.0.1.bin                54560
4 .  jbc-vfc-l.0.13.0.bin             16760
5 .  fax-vfc-l.0.1.bin                64290
6 .  bas-vfc-l.0.1.bin                54452
7 .  cdc-g711-l.0.1.bin               190
8 .  cdc-g729-l.0.1.bin               21002
9 .  cdc-g726-l.0.1.bin               190
10.  cdc-g728-l.0.1.bin               22270
11.  cdc-gsmfr-l.0.1.bin              190
```

The table below describes significant fields in this output.

Field

Description

File Name

Name of the file stored in Flash memory.

Size (Bytes)

Size of the file in bytes.

### Related Commands

Command

Description

show vfc cap - list

Displays the current list of files on the capability list for this VFC.

show vfc default - file

Displays the default files included in the default file list for this VFC.

show vfc version

Displays the version of the software residing on this VFC.

## show vfc version

To show the version of the software residing on a voice feature card (VFC), use the show vfc version command in user EXEC mode.

show vfc slot version { dspware | vcware }

### Syntax Description

slot

Slot where the VFC is installed. Range is from 0 to 2.

dspware

Which DSPWare software to display.

vcware

Which VCWare software to display.

### Command Modes

Privileged EXEC (#) User EXEC (>)

## Command History

Release

Modification

11.3 NA

This command was introduced on the Cisco AS5300.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T with changes to the command output.

### Usage Guidelines

Use this command to display the version of the software currently installed in Flash memory on a VFC.

## Examples

The following is sample output from this command:

```
Router# show vfc 0 version dspware Version of Dspware in VFC slot 0 is 0.10
```

The output from this command is a simple declarative sentence stating the version number for the selected type of software
                              (in this example, DSPWare) for the VFC residing in the selected slot number (in this example, slot 0).

Cisco IOS Release 12.2(13)T adds new information to the output of the show vfc slot version vcware and show vfc slot version
                              dspware commands. Messages are output if the Cisco VCWare or DSPWare is not compatible with the Cisco IOS image. The new information
                              is advisory only, so there is no action taken if the software is compatible or incompatible.

If the versions detected fall within the defined criteria and are compatible, nothing is output at bootup time. A confirmation
                              line is output when the show vfc version vcware and show vfc version dspware commands are used:

```
Router# show vfc 1 version vcware Voice Feature Card in Slot 1:
VCWare Version     : 7.35
ROM Monitor Version: 1.3
     DSPWare Version    : 3.4.46L
     Technology         : C549
VCWare/DSPWare version compatibility OK
```

The table below shows output field descriptions for the show vfc version vcware command with compatible firmware.

Field

Description

Voice Feature Card in Slot

Slot in which the VFC is installed.

VCWare Version

Cisco VCWare version. Version 7.35 is the required minimum for Cisco IOS Release 12.2(11)T and higher.

ROM

ROM monitor version shows 1.3 .

DSPWare Version

The DSPWare version shows 3.4.46L, which is the required minimum for Cisco IOS Release 12.2(11)T and higher .

Technology

The technology shows C549. C549 technology is available to support either medium-complexity codecs or high-complexity codecs.

VCWare/DSPWare version compatibility

The Cisco VCWare and DSPWare versions are compatible with Cisco IOS software . Cisco VCWare/DSPWare version compatibility
                                          is either OK or shows a mismatch.

This option is available only with Cisco IOS Release 12.2(10) mainline and later release or Cisco IOS Release 12.2(11)T and
                                                      later.

The following is sample outpou from this command.

```
Router# show vfc 1 version dspware
DSPWare version in VFC slot 1 is 3.4.46L
VCWare/DSPWare version compatibility OK
```

The table below shows output field descriptions for the show vfc version dspware command with compatible firmware.

Field

Description

Voice Feature Card in Slot

Slot in which the VFC is installed .

DSPWare Version

The DSPWare version shows 3.4.46L, which is the required minimum for Cisco IOS Release 12.2(10)T and higher .

VCWare/DSPWare version compatibility

The Cisco VCWare and DSPWare versions are compatible with Cisco IOS software. Cisco VCWare/DSPWare version compatibility
                                          is either OK or shows a mismatch.

This option is available only with Cisco IOS Release 12.2(10) mainline and later or 12.2(11)T and later.

If the found versions are out of range or otherwise mismatched, a representative message is output when you boot up the router
                              or is appended to the output of the show vfc version vcware and show vfc version dspware commands. Other than the output of
                              these messages, the version check has no other effect, and the software functions normally. The following is an example of
                              when a found version is out of range or mismatched at bootup :

```
... 
Firmware version mismatch for bundle AS5300 VCWare 
  - 	version found (6.04) is lower than minimum required (7.35)
Firmware version mismatch for bundle AS5300 C549 
  - version found (3.3.10L) is lower than minimum required (3.4.46L)
```

If you were to enter an explicit request, and the software were incompatible, the following output would be displayed :

```
Router# show vfc 1 version vcware Voice Feature Card in Slot 1:
VCWare Version     : 6.04
ROM Monitor Version: 1.3
     DSPWare Version    : 3.3.10L
     Technology         : C549
Firmware version mismatch for bundle AS5300 VCWare 
  - version found (6.04) is lower than minimum required (7.14) 
Firmware version mismatch for bundle AS5300 C549 
  - version found (3.3.10L) is lower than minimum required (3.4.26L)
Router# show vfc 1 version dspware DSPWare version in VFC slot 1 is 3.3.10L
Firmware version mismatch for bundle AS5300 VCWare 
  - version found (6.04) is lower than minimum required (7.14)
Firmware version mismatch for bundle AS5300 C549 
  - version found (3.3.10L) is lower than minimum required (3.4.26L)
```

### Related Commands

Command

Description

show vfc cap - list

Displays the current list of files on the capability list for this VFC.

show vfc default - file

Displays the default files included in the default file list for this VFC.

show vfc directory

Displays the list of all files residing on this VFC.

## show video call summary

To display summary information about video calls and the current status of the Video CallManager (ViCM), use the show video call summary command in privileged EXEC mode.

show video call summary

### Syntax Description

There are no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco MC3810.

12.0(7)T

The command was integrated into Cisco IOS Release 12.0(7)T.

### Usage Guidelines

Use this command to quickly examine the status of current video calls. In Cisco IOS Release 12.0(5)XK and Release 12.0(7)T,
                              there can be only one video call in progress.

## Examples

The following example displays information about the ViCM when no call is in progress on the serial interface that connects
                              to the local video codec:

```
Router# show video call summary Serial0:ViCM = Idle, Codec Ready
```

The following output shows a call starting:

```
Router# show video call summary Serial0:ViCM = Call Connected
```

The following output shows a call disconnecting:

```
Router# show video call summary Serial0:ViCM = Idle
```

### Related Commands

Command

Description

show call history video record

Displays information about video calls.

## show voice accounting method

To display connectivity status information for accounting method lists, use the show voice accounting method command in privileged EXEC mode.

show voice accounting method [method-list-name]

### Syntax Description

method-list-name

(Optional) Name of a specific method list. This option displays connectivity status information for a single method list
                                          identified by this argument.

### Command Default

If no argument is specified, connectivity status information for all accounting method lists is displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use the show voice accounting method command to display the history of status (reachable or unreachable), status transition time, and statistics of the accounting
                              status for a specified accounting method list or all the accounting method lists. A maximum of ten status histories are displayed.

## Examples

The following is sample output from the show voice accounting method command for a specific method list:

```
Router# show voice accounting method ml1 Accounting Method List [ml1]
====================== 
Current Status:
---------------
unreachable                [21:52:39 gmt Dec 4 2002]
last record sent time      [23:14:59 gmt Dec 4 2002]
total probe sent out       [84]
Status History:
---------------
(2) unreachable            [21:52:39 gmt Dec 4 2002]
(1) reachable              [21:46:19 gmt Dec 4 2002]
                 SUCCESS                        FAILURE
Record  [Received   | Notified ] [Received   |  Notified  | Reported ]
Type    [from server| to client] [from server|  to client | to call  ]
------  [-----------|----------] [-----------|------------|----------]
START   [     0     |     0    ] [     0     |      0     |     0    ]
UPDATE  [     0     |     0    ] [     0     |      0     |     0    ]
STOP    [     0     |     0    ] [     84    |      84    |     0    ]
ACCT_ON [     0     |     0    ] [     0     |      0     |     0    ]
------  [-----------|----------] [-----------|------------|----------]
TOTAL   [     0     |     0    ] [     84    |      84    |     0    ]
```

If there is no status history, as in the following example, no status history is displayed.

```
Router# show voice accounting method Accounting Method List [ml1]
====================== 
Current Status:
---------------
reachable                  [21:52:39 gmt Dec 4 2002]
last record sent time      [23:14:59 gmt Dec 4 2002]
total probe sent out       [2]
                 SUCCESS                        FAILURE
Record  [Received   | Notified ] [Received   |  Notified  | Reported ]
Type    [from server| to client] [from server|  to client | to call  ]
------  [-----------|----------] [-----------|------------|----------]
START   [     0     |     0    ] [     0     |      0     |     0    ]
UPDATE  [     0     |     0    ] [     0     |      0     |     0    ]
STOP    [     0     |     0    ] [     2     |      2     |     0    ]
ACCT_ON [     0     |     0    ] [     0     |      0     |     0    ]
------  [-----------|----------] [-----------|------------|----------]
TOTAL   [     0     |     0    ] [     2     |      2     |     0    ]
```

The table below describes the significant fields shown in the display.

Field

Description

Current Status: reachable or unreachable

Current status of the method list: reachable or unreachable and the time (in hh:mm:ss) and date the method list reached this
                                          status.

last record sent time

Time (in hh:mm:ss) and date the last accounting record was sent to the method list.

total probe sent out

Number of probe records sent up to the time of the show command.

SUCCESS: Received from server

Number of success status of the accounting records of this type received from the method list.

SUCCESS: Notified to client

Number of success status of the accounting records of this type for which notifications were sent to the GAS.

FAILURE: Received from server

Number of failure status of the accounting records of this type received from the method list.

FAILURE: Notified to client

Number of failure status of the accounting records of this type for which notifications were sent to the GAS.

FAILURE: Reported to call

Number of failure status of the accounting records of this type that were reported to the call application.

### Related Commands

Command

Description

clear voice accounting method

Clears accounting status statistics for a particular accounting method list or all accounting method lists.

## show voice accounting response pending

To display information regarding pending VoIP AAA accounting responses, use the show voice accounting response pending command in privileged EXEC mode.

show voice accounting response pending

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example displays information regarding pending VoIP AAA accounting responses:

```
Router# show voice accounting response pending Total num of acct sessions waiting for acct responses: 0
Total num of acct start responses pending:             0
Total num of acct interim update responses pending:     0
Total num of acct stop responses pending:              0
```

The table below lists and describes the significant output fields.

Field

Description

Total num of acct sessions waiting for acct responses

Number of accounting sessions that are waiting for accounting responses.

Total num of acct start responses pending

Number of accounting start responses that are pending.

Total num of acct interim update responses pending

Number of accounting interim update responses that are pending.

Total num of acct stop responses pending

Number of accounting stop responses that are pending.

## show voice busyout

To display information about the voice-busyout state, use the show voice busyout command in privileged EXEC mode.

show voice busyout

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

This command displays the following information:

Interfaces that are being monitored for busyout events

Voice ports currently in the busyout state and the reasons

## Examples

The following is sample output from this command:

```
Router# show voice busyout If following network interfaces are down, voice port will be put into busyout state
ATM0
Serial0
The following voice ports are in busyout state
1/1     	is forced into busyout state
1/2     	is in busyout state caused by network interfaces
1/3     	is in busyout state caused by ATM0
1/4     	is in busyout state caused by network interfaces
1/5     	is in busyout state caused by Serial0
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

busyout forced

Forces a voice port into the busyout state.

busyout monitor

Places a voice port in the busyout monitor state.

busyout seize

Changes the busyout seize procedure from a voice port.

voice-port busyout

Places all voice ports associated with a serial or ATM interface in a busyout state.

## show voice cable-status

To display the current or last cable status of a specific analog voice port or all idle analog voice ports, use the show voice cable-status command in privileged EXEC mode.

show voice cable-status { all | summary | x/y/z | x/y/z-z1 }

### Syntax Description

all

Specifies the current cable status of all analog voice ports that have cable polling enabled.

summary

Specifies the last cable status of all analog voice ports that have cable polling enabled.

x/y/z

Voice port number.

x/y/z-z1

Voice port number range. The range is from 0 to 71. Example: 2/0/0-71.

### Command Modes

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

Before using the show voice cable-status command, you must disable the cable-detect-poll-timer command.

## Examples

The following is sample output from the show voice cable-status all command:

```
Device# show voice cable-status all Warning:This may take time to perform and cause call disruption!

PORT         cable-status
========== ================
0/2/0        cable-detect not configured
0/2/1        connected
0/2/2        connected
0/2/3        busy out
0/3/0        administrative down
0/3/1        in busy state
0/3/2        connected
0/3/3        connected
1/0/16       not connected
```

### Related Commands

Command

Description

cable-detect

Enables cable polling on analog FXOGS, FXOLS, FXSGS, and FXSLS voice ports.

cable-detect-poll-timer

Configures the cable polling timer value for background polling processes on an analog voice port.

## show voice call

To display the call status for voice ports on the Cisco router, use the show voice call command in user EXEC or privileged EXEC mode.

### Cisco 827, Cisco 1700 Series, and Cisco 7750 with Analog Voice Ports

show voice call [ slot / port | status [call-id] [ sample seconds ] | summary ]

### Cisco 2600, Cisco 3600, Cisco 3700 Series with Analog Voice Ports

show voice call [ slot / stubunit / port | status [call-id] [ sample seconds ] | summary ]

### Cisco 2600, Cisco 3600, and Cisco 3700 Series with Digital Voice Ports (with T1 Packet Voice Trunk Network Modules)

show voice call [ slot / port : ds0-group | status [call-id] [ sample seconds ] | summary ]

### Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850, Cisco 7200 Series, and Cisco 7500 Series with Digital Voice Ports

show voice call [ slot / port : ds0-group | status [call-id] [ sample seconds ] | summary ]

### Syntax Description

Cisco 827, Cisco 1700 Series, and Cisco 7750 with Analog Voice Ports

slot / port

(Optional) A specific analog voice port:

slot-- Physical slot in which the analog voice module (AVM) is installed.

/ port --Analog voice port number. Range is from 1 to 6. The slash mark is required.

status [ call-id ]

(Optional) Displays status of active calls. If call-id is specified, this command displays the status of a specific call .

sample seconds

(Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10.

summary

(Optional) Displays current settings and state of the voice port, regardless of port activity.

Cisco 2600 Series, Cisco 3600 Series, Cisco 3700 Series with Analog Voice Ports

slot / subunit / port

(Optional) A specific analog voice port:

slot --Router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform.

/ subunit -- Voice interface card (VIC) in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network
                                                module.) The slash mark is required.

/ port -- Analog voice port number. Valid entries are 0 and 1. The slash mark is required.

status [ call-id ]

(Optional) Displays status of active calls. If call-id is specified, this command displays the status of a specific call .

sample seconds

(Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10.

summary

(Optional) Displays current settings and state of the voice port, regardless of port activity.

Cisco 2600, Cisco 3600, and Cisco 3700 Series with Digital Voice Ports (with T1 Packet Voice Trunk Network Modules)

slot / port : ds0 - group

(Optional) A specific digital voice port:

slot -- Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for the
                                                particular platform.

/ port --T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1. (One VWIC fits in an NM.) The
                                                slash mark is required.

: ds0 - group-- T1 or E1 logical port number. Range is from 0 to 23 for T1 and from 0 to 30 for E1. The colon is required.

status [ call-id ]

(Optional) Displays status of active calls. If call-id is specified, this command shows the status of a specific call .

sample seconds

(Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10.

summary

(Optional) Displays current settings and state of the DSP port regardless of port activity.

Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850, Cisco 7200 Series, and Cisco 7500 Series with Digital Voice Ports

slot / port : ds0 - group

(Optional) A specific digital voice port:

slot --Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for
                                                the particular platform.

/ port-- T1 or E1 physical port in the VWIC. Valid entries are 0 and 1. (One VWIC fits in an NM.) The slash mark is required.

: ds0 - group-- T1 or E1 logical port number. Range is from 0 to 23 for T1 and from 0 to 30 for E1. The colon is required.

status [ call-id ]

(Optional) Displays status of active calls. If call-id is specified, this command shows the status of a specific call .

sample seconds

(Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10.

summary

(Optional) Displays current settings and state of the voice port regardless of port activity.

### Command Modes

User EXEC (#) privileged EXEC (>)

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(13)T

This command was modified with the status , call-id , and sample seconds command options. This command is available on all voice platforms.

12.4(3d)

This command was modified to support the Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms for Non-Facility Associated
                                          Signaling (NFAS) configuration. Output was modified to provide accurate port information for NFAS configuration on these platforms.

15.1(3)T

This command was modified. The output of this command was enhanced to display the connection status of foreign exchange office
                                          (FXO) ports.

### Usage Guidelines

This command works on Voice over Frame Relay, Voice over ATM, and Voice over IP by providing the status at the following
                              levels of the call-handling module:

Call-processing state machine

End-to-end call manager

Protocol state machine

Tandem switch

This command is not supported in Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms for NFAS configuration before Cisco
                                          IOS Release 12.4(3d).

This command displays call-processing and protocol state-machine information for a voice port if the information is available.
                              This command also shows information on the DSP channel associated with the voice port if the information is available. All
                              real-time information in the DSP channel, such as jitter and buffer overrun, is queried to the DSP channel, and asynchronous
                              responses are returned to the host side.

If no call is active on a voice port, the show voice call summary command displays only the VPM (shutdown) state. If a call is active on a voice port, the show voice call summary command displays voice telephony service provider (VTSP) state. For an on-net call or a local call without local bypass (not
                              cross-connected), the codec and voice activity detection (VAD) fields are displayed. For an off-net call or a local call with
                              local bypass, the codec and VAD fields are not displayed.

When a call is active on a voice port, the show voice call summary command displays the VTSP state. The VTSP state always shows the VTSP signaling state irrespective of the type of call: voice
                              call or a fax call. A fax call does not display S_Fax. The following output is displayed:

```
PORT           CODEC    VAD VTSP STATE            VPM STATE
============== ======== === ==================== ======================
1/0:1.1         1         y  S_CONNECT             EM_CONNECT
```

Use the show voice dsmp stream command to display the current session of the voice Distributed Stream Media Processor (DSMP) media stream and its related
                                          applications.

The show voice call command does not display the codec and VAD fields because this information is in the summary display. If you use the show voice call status command by itself, an immediate list of all the active calls is shown. You can use the call-id argument to request that the DSP associated with the call-id be queried for run-time statistics twice, once immediately, and a second time after sample seconds .

The sample seconds is the number of seconds over which the status is to be determined. The results of the run-time statistic queries are then
                              analyzed and presented in a one-line summary format.

When a call terminates during the specified sample period , the following output message is returned:

```
CallID call id cannot be queried 
CallID call id second sample responses unavailable
```

The Voice Call Tuning feature is not supported on the Cisco AS5300.

## Examples

The following is sample output from the show voice call summary command showing two local calls connected without local bypass:

```
Router# show voice call summary PORT    CODEC    VAD VTSP STATE            VPM STATE
======= ======== === ===================== ========================
0:17.18                                     *shutdown*
0:18.19 g729ar8   n  S_CONNECT             FXOLS_OFFHOOK
0:19.20                                    FXOLS_ONHOOK
0:20.21                                    FXOLS_ONHOOK
0:21.22                                    FXOLS_ONHOOK
0:22.23                                    FXOLS_ONHOOK
0:23.24                                    EM_ONHOOK
1/1                                        FXSLS_ONHOOK
1/2                                        FXSLS_ONHOOK
1/3                                        EM_ONHOOK
1/4                                        EM_ONHOOK
1/5                                        FXOLS_ONHOOK
1/6     g729ar8   n  S_CONNECT             FXOLS_CONNECT
```

The following is sample output from the show voice call summary command showing two local calls connected with local bypass:

```
Router# show voice call summary PORT    CODEC    VAD VTSP STATE            VPM STATE
======= ======== === ===================== ========================
0:17.18                                     *shutdown*
0:18.19              S_CONNECT             FXOLS_OFFHOOK
0:19.20                                    FXOLS_ONHOOK
0:20.21                                    FXOLS_ONHOOK
0:21.22                                    FXOLS_ONHOOK
0:22.23                                    FXOLS_ONHOOK
0:23.24                                    EM_ONHOOK
1/1                                        FXSLS_ONHOOK
1/2                                        FXSLS_ONHOOK
1/3                                        EM_ONHOOK
1/4                                        EM_ONHOOK
1/5                                        FXOLS_ONHOOK
1/6                  S_CONNECT             FXOLS_CONNECT
```

The following is sample output from the show voice call summary command in which the connected FXO port 0/2/0 shows status of "FXOLS_ONHOOK" whereas the FXO port 0/2/1, which is disconnected,
                              shows a status of "FXOLS_BUSYOUT":

```
Router# show voice call summary PORT           CODEC     VAD VTSP STATE            VPM STATE
============== ========= === ==================== ======================
0/0/0         -          -  -                     FXSLS_ONHOOK             
0/0/1         -          -  -                     FXSLS_ONHOOK             
0/3/0:23.1      -          -  -                     
0/3/0:23.2      -          -  -                     
.
.
.
0/3/0:23.23     -          -  -                     
0/1/0         -          -  -                     DID_ONHOOK               
0/1/1         -          -  -                     DID_ONHOOK               
0/2/0         -          -  -                     FXOLS_ONHOOK             
0/2/1         -          -  -                     FXOLS_BUSYOUT            
2/0/0         -          -  -                     FXSLS_ONHOOK             
2/0/1         -          -  -                     FXSLS_ONHOOK             
2/0/2         -          -  -                     FXSLS_ONHOOK             
2/0/3         -          -  -                     FXSLS_ONHOOK             
2/0/4         -          -  -                     FXSLS_ONHOOK             
2/0/5         -          -  -                     FXSLS_ONHOOK             
2/0/6         -          -  -                     FXSLS_ONHOOK             
2/0/7         -          -  -                     FXSLS_ONHOOK
```

Beginning in Cisco IOS Release 15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected
                                          or disconnected, a message is displayed to indicate the status change. For example, the following message is displayed to
                                          report that a cable has been connected, and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122
                                          EST: %LINK-3-UPDOWN: Interface Foreign Exchange Office 0/2/0, changed state to operational status up due to cable reconnection

The following is sample output from the show voice call summary command showing one regular PRI port and one NFAS PRI port on a Cisco AS5350, Cisco AS5400, or Cisco AS5850 platform. Port
                              3/2:D belongs to a regular PRI voice port with time slots 0 and 22. Port Se3/1 belongs to an NFAS PRI voice port with time
                              slots 0,1, and 2 on T1 controller 3/1, which is a member of an NFAS group.

In the case of NFAS on Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms, the port is reported in terms of the serial
                              interface associated with the T1 controller, and the time slot is counted from 0 (for example, 0, 1, 2, 3).

```
Router# show voice call summary PORT           CODEC    VAD VTSP STATE            VPM STATE
============== ======== === ==================== ======================
3/2:D.0        None      y  S_ALERTING            S_TSP_INCALL
3/2:D.22       None      y  S_ALERTING            S_TSP_INCALL
Se3/1:0        None      y  S_CONNECT             S_TSP_CONNECT
Se3/1:1        None      y  S_CONNECT             S_TSP_CONNECT
Se3/1:2        None      y  S_CONNECT             S_TSP_CONNECT
```

The output from the show voice call summary command is slightly different in the PORT field on platforms other than the Cisco AS5350, Cisco AS5400, and Cisco AS5850.
                                          The contrast between platform types is as follows: Platform Regular PRI (T1) NFAS PRI (T1)* --------------------------------------------------------------
                                          non-AS5xxx 3/0:23.TS 3/1:23.TS AS5xxx 3/0:D.TS Ser3/1:(TS-1) * Assumes T1 3/1 is a member of an NFAS group with T1 3/0 as
                                          the primary NFAS member, and TS is the time slot counted from a base of 1 (for example 1, 2, 3).

The following is sample output from the show voice call command for analog voice ports:

```
Router# show voice call 1/1 vpm level 1 state = FXSLS_ONHOOK
vpm level 0 state = S_UP
1/2 vpm level 1 state = FXSLS_ONHOOK
vpm level 0 state = S_UP
1/3 is shutdown
1/4 vtsp level 0 state = S_CONNECT
vpm level 1 state = S_TRUNKED
vpm level 0 state = S_UP
1/5 vpm level 1 state = EM_ONHOOK
vpm level 0 state = S_UP
1/6 vpm level 1 state = EM_ONHOOK
vpm level 0 state = S_UP
Router# show voice call 1/4 1/4 vtsp level 0 state = S_CONNECT
vpm level 1 state = S_TRUNKED
vpm level 0 state = S_UP
router#			***DSP VOICE VP_DELAY STATISTICS***
Clk Offset(ms): 1445779863, Rx Delay Est(ms): 95
Rx Delay Lo Water Mark(ms): 95, Rx Delay Hi Water Mark(ms): 125
		***DSP VOICE VP_ERROR STATISTICS***
Predict Conceal(ms): 10, Interpolate Conceal(ms): 0
Silence Conceal(ms): 0, Retroact Mem Update(ms): 0
Buf Overflow Discard(ms): 20, Talkspurt Endpoint Detect Err: 0
		***DSP VOICE RX STATISTICS***
Rx Vox/Fax Pkts: 537, Rx Signal Pkts: 0, Rx Comfort Pkts: 0
Rx Dur(ms): 50304730, Rx Vox Dur(ms): 16090, Rx Fax Dur(ms): 0
Rx Non-seq Pkts: 0, Rx Bad Hdr Pkts: 0
Rx Early Pkts: 0, Rx Late Pkts: 0
		***DSP VOICE TX STATISTICS***
Tx Vox/Fax Pkts: 567, Tx Sig Pkts: 0, Tx Comfort Pkts: 0
Tx Dur(ms): 50304730, Tx Vox Dur(ms): 17010, Tx Fax Dur(ms): 0
		***DSP VOICE ERROR STATISTICS***
Rx Pkt Drops(Invalid Header): 0, Tx Pkt Drops(HPI SAM Overflow): 0
		***DSP LEVELS***
TDM Bus Levels(dBm0): Rx -70.3 from PBX/Phone, Tx -68.0 to PBX/Phone
TDM ACOM Levels(dBm0): +2.0, TDM ERL Level(dBm0): +5.6
TDM Bgd Levels(dBm0): -71.4, with activity being voice
```

The following is sample output from the show voice call command for analog voice ports on a Cisco 7200 series. The output includes the DSPfarm, T1 interface, and DS0 or TLM slot
                              configuration:

```
Router# show voice call 6/0:0 6/0:0 1 -         -  -                     vpm level 1 state = FXOGS_ONHOOK 
vpm level 0 state = S_UP
6/0:0 2 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 3 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 4 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 5 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 6 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 7 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 8 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 9 -         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 10-         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 11-         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
6/0:0 12-         -  -                     vpm level 1 state = FXOGS_ONHOOK
vpm level 0 state = S_UP
```

The following is sample output from the show voice call status command on the Cisco 2600 series. You can use this command rather than the show call active brief command to obtain the caller ID; the caller ID output of the show voice call status command is already in hexadecimal form.

```
Router# show voice call status CallID     CID  ccVdb      Port      DSP/Ch  Called #   Codec    Dial-peers
0x1        11CE 0x02407B20 1:0.1     1/1     1000       g711ulaw 2000/1000
1 active call found
```

Using the call-id argument is a generic means to identify active calls. If the call-id is omitted, the query shows all active voice calls. In the following example, a list of all active calls with relevant identifying
                              information is shown:

```
Router# show voice call status CallID    CID    ccVdb       Port     DSP/Ch  Called #   Codec    Dial-peers
0x3       11D4   0x62972834  1/0/0    1/1     10001      g711ulaw 1/2
0x4       11D4   0x62973AD0  1/0/1    2/1    *10001      g711ulaw 2/1
0xA       11DB   0x62FE9D68  1/1/0    3/1    *2692       g729r8   0/2692
2 active calls found
```

You can query only one call at a time. If you attempt queries from different ports (console and Telnet ), and if a query
                                          is in progress on another port, the system asks you to wait for completion of that query. You can query any call from anywhere,
                                          at anytime, except during the sample interval for an enquiry that is already in progress. This simplifies the implementation
                                          significantly and does not reduce the usefulness of the command.

The following example shows echo-return-loss (ERL) reflector information where the call ID is 3 and the sample period is
                              10 seconds:

```
Router# show voice call status 3 sample 10 Gathering information (10 seconds)...
CallID    Port     DSP/Ch  Codec    Rx/Tx     ERL         Jitter
0x3       1/0/0    1/1     g711ulaw 742/154   5.6         50/15
```

In this example, ERL is the echo return loss (in dB) as reported by the DSP. Jitter values are the current delay and the
                              jitter of the packets around that delay.

If the router is running the extended echo canceller, output looks similar to the following if you enter the same command.
                              The output shows a new value under ERL/Reflctr: the time difference, in ms, between the original signal and the loudest echo
                              (peak reflector) as detected by the echo canceller:

```
Router# show voice call status 3 sample 10 Gathering information (10 seconds)...
CallID    Port     DSP/Ch  Codec    Rx/Tx     ERL/Reflctr Jitter
0x3       1/0/0    1/1     g711ulaw 742/154   5.6/12      50/15
```

The following examples show output using the NextPort version of the standard echo canceller. ( Time-slot information is
                              also in the output for digital ports.)

```
Router# show voice call status CallID     CID  ccVdb      Port      DSP/Ch  Called #   Codec    Dial-peers
0x97       12BB 0x641B0F68 3/0:D.1   1012/2  31001      g711ulaw 3/31000
0x99       12BE 0x641B0F68 3/0:D.2   1012/3  31002      g711ulaw 3/31000
2 active calls found
Router# show voice call status CallID     CID  ccVdb       Port     DSP/Ch  Called #   Codec    Dial-peers
0x2        11D1 0x62FE6478 1/0/0     1/1     10001      g711ulaw 1/2
0x3        11D1 0x62FE80F0 1/0/1     2/1    *10001      g711ulaw 2/1
1 active call found
```

When using the test call id command, you must specify a call ID, which you can obtain by using the show voice call status command. The following is an example of how to obtain the call ID for use as the call-id argument. The first parameter displayed in the output is the call ID.

Do not use the 0x prefix in the call-id argument when you enter the resulting call ID in the test call status command .

The following shows keyword choices when using the show voice call command with the | (pipe) option:

```
Router# show voice call | ? append    Append redirected output to URL (URLs supporting append operation
            only)
  begin     Begin with the line that matches
  exclude   Exclude lines that match
  include   Include lines that match
  redirect  Redirect output to a URL
  tee       Copy output to a URL
```

The table below describes significant fields shown in the previous displays.

Field (listed alphabetically)

Description

Called #

Called number.

No "*" before the number denotes an originating call leg. Two of the call legs in the example constitute one locally switched
                                                call and one network call, so the call legs refer to two active calls.

A "*" before the number denotes a destination call leg (for example, this number was called with Called #).

CallID

This hexadecimal number used for further query is the monotonically increasing number that call control maintains for each
                                          call leg (ccCallID_t).

ccVdb

Value that is displayed in many other debugs to identify these call legs.

CID

Conglomerate value derived from the GUID that appears in the show call active brief command.

Codec

Codec.

Dial-peers

Dial peer .

DSP/Ch

DSP and channel allocated to this call leg. The format of these values is platform dependent (particularly the Cisco AS5300,
                                          which shows the DSP number as a 3-digit number, <VFC#><DSPM#><DSP#>).

Time-slot information is also in the output for digital ports. For example, if you are using a digital port, the time slot
                                          is also returned: dsp/ch/ time slot .

ERL

Echo return loss (in dB).

ERL/Reflctr

Time difference, in ms, between the original signal and the loudest echo (peak reflector) as detected by the echo canceller.

Jitter

Current values of the delay and the jitter of the packets around that delay.

Port

V oice port.

Rx/Tx

Transmit and receive rates for the connection.

VAD

Voice-activity detection: y or n.

VPM STATE

Voice-port-module (VPM) state.

VTSP STATE

Voice-telephony-service-provider (VTSP) state.

For more information about the extended echo canceller, see Extended ITU-T G.168 Echo Cancellation .

### Related Commands

Command

Description

show call active brief

Displays a summary of active call information.

show dial-peer voice

Displays the configuration for all VoIP and POTS dial peers configured on the router.

show voice dsmp stream

Displays the current session of the voice DSPM media stream.

show voice dsp

Displays the current status of all DSP voice channels.

show voice port

Displays configuration information about a specific voice port.

test call id

Manipulates the echo canceller and jitter buffer parameters in real time.

## show voice call rate

To display the voice call rate information, use the show voice call rate command in privileged EXEC mode.

show voice call rate [ table ]

### Syntax Description

table

(Optional) Displays the voice call rate information in a tabular format.

### Command Default

Displays the voice call rate information in a histogram format.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

15.3(2)T

This command was replaced by the show call history stats cps command.

Cisco IOS XE Release 3.9S

This command was replaced by the show call history stats cps command.

### Usage Guidelines

You can use the show voice call rate command to display the voice call rate information in the histogram format. Use the show voice call rate table command to display the voice call rate information in a tabular format.

## Examples

The following is sample output from the show voice call rate command. In the output, x-axis measures time in seconds (1 unit = 1 second) and y-axis measures call legs per second (cps)
                              (1 unit = 1 cps):

```
Router# show voice call rate 3845-1   04:35:57 AM Wednesday Sep 7 2011 UTC
          122                    11
          5009          2        40      42    64
  100
   90
   80
   70
   60
   50
   40
   30
   20    ***
   10    ****                      **              *
     0....5....1....1....2....2....3....3....4....4....5....5....6
                  0    5    0    5    0    5    0    5    0    5    0
          VoIP Call switching rate per second (last 60 seconds)
          # = calls entering the module per second
```

The following is sample output from the show voice call rate table command:

```
Router# show voice call rate table 3845-1   04:35:57 AM Wednesday Sep 7 2011 UTC
          Voice Call switching rate per second (last 60 seconds)
Period     Actual     Average
--------------------------------------
 1-5            0          0
 6-10         64         13
11-15          0          0
16-20          0          0
21-25          2          0
26-30          0          0
31-35         24          5
36-40          0          0
41-45          6          1
46-50         10          2
51-55          0          0
56-60          0          0
```

The following table describes the significant fields shown in the display.

Field

Description

Period

Duration of 5 seconds.

Actual

Number of call legs created in 5 seconds.

Average

The average call legs created in 5 seconds.

### Related Commands

Command

Description

voice call rate monitoring

Enables voice call rate monitoring.

## show voice cause-code

To display error category to Q.850 cause code mapping, use the show voice cause-code command in user EXEC mode.

show voice cause-code category-q850

### Syntax Description

category q850

Displays error category to Q.850 cause code mapping.

### Command Default

No default behavior or values.

### Command Modes

User EXEC (>)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command to display the internal error category to Q.850 cause code mapping table, and configured and default values,
                              with category descriptions.

## Examples

The following example displays Q.850 cause code mapping:

```
Router# show voice cause-code category-q850 The Internal Error Category to Q850 cause code mapping table:-
 Error Configured Default    Description
Category  Q850     Q850
   128     27        3  Destination address resolution failure                 
   129     38      102  Call setup timeout                                     
   178     41       41  Internal Communication Error                           
   179     41       41  External communication Error                           
   180     47       47  Software Error                                         
   181     47       47  Software Resources Unavailable                         
   182     47       47  Hardware Resources Unavailable                         
   183     41       41  Capability Exchange Failure                            
   184     49       49  QoS Error                                              
   185     41       41  RTP/RTCP receive timer expired or bearer layer failure 
   186     38       38  Signaling socket failure                               
   187     38       38  Gateway or signaling interface taken out of service   
   228     50       50  User is denied access to this service                  
   278     65       65  Media Negotiation Failure due to non-existing Codec
```

The table below describes the significant fields shown in the display.

Field

Description

128

Destination address resolution failure

129

Call setup timeout

178

Internal communication error

179

External communication Error

180

Software error

181

Software resources unavailable

182

Hardware resources unavailable

183

Capability exchange failure

184

QoS error

185

RTP/RTCP receive timer expired or bearer layer failure

186

Signaling socket failure

187

Gateway or signaling interface taken out of service

228

User denied access to this service

278

Media negotiation failure due to non existing codec

### Related Commands

Command

Description

error-category q850-cause

Specifies Q.850 cause code mapping

## show voice class called-number

To display a specific voice class called-number, use the show voice class called-number command in privileged EXEC mode.

show voice class called-number [ inbound | outbound ] tag

### Syntax Description

inbound

Displays the specified inbound voice class called-number.

outbound

Displays the specified outbound voice class called-number.

tag

Digits that identify this voice class called-number.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to display a specific inbound or outbound voice class called-number.

## Examples

The following is sample output from this command:

```
Router# show voice class called-number outbound 200 Called Number Outbound: 200
           index 1      4085550100
           index 2      4085550102
           index 3      4085550103
           index 4      4085550104
```

The table below describes significant fields shown in the display.

Field

Description

Called Number Inbound/Outbound

The tag for the specified inbound or outbound voice class called-number.

index number

The number or range of numbers for this voice class called number.

### Related Commands

Command

Description

show voice class called-number-pool

Displays voice class called number pool configuration information.

## show voice class called-number-pool

To display a voice class called-number pool, use the show voice class called-number-pool command in privileged EXEC mode.

show voice class called-number-pool tag [ detail ]

### Syntax Description

tag

Digits that identify this voice class called-number-pool. Range is 1 to 10000.

detail

Displays idle called number and allocated called number information.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to display the voice class called number pool configuration information. The detail keyword displays up to 16 idle called numbers, and up to 4 allocated called numbers for each allocated request.

## Examples

The following sample output displays configuration information for voice class called-number-pool 100, including idle called
                              numbers and allocated called numbers:

```
Router(config)# show voice class called-number-pool 100 detail Called Number Pool: 100
index 1 100A11 - 100A20
index 2 200#55 - 200#77
index 3 5551111 - 6662333
index 99 123C11 - 123C99
All called numbers are generated from table: FALSE
No of idle called numbers: 16
List of idle called numbers:
100A11 100A12 .. Display up to 16 idle called number from the pool
100A13 100A14
100A15 100A16
100A17 100A18
100A19 100A20
200#55 200#56
200#57 200#58
200#59 200#60
No of alloc requests : 1
Ref Id Alloc PC Size
2 41F84190 16
List of alloc called numbers: .. Display the first 4 allocated called number for RefId 2
200#61 200#62
200#63 200#64
```

The table below describes significant fields shown in the display.

Field

Description

Called Number Pool

Tag that identifies the called number pool.

index

Number or range of numbers for this called number pool.

All called numbers are generated from table

FALSE--Numbers are not generated from called number table.

TRUE--Numbers are generated from called number table.

No. of idle called numbers

Number of idle called numbers in the called number pool.

List of idle called numbers

List of idle numbers in the called number pool.

No. of alloc requests

Number of requests for numbers from the called number pool.

Ref Id Alloc PC Size

Reference ID for a specific list of allocated numbers.

List of alloc called numbers

List of first four allocated numbers from the called number pool.

### Related Commands

Command

Description

show voice class called-number

Displays a specific voice class called-number.

## show voice class e164-pattern-map

To display the configuration of a voice class E.164 pattern map, use the show voice class e164-pattern-map command in user EXEC or privileged EXEC mode.

### Syntax Description

summary

(Optional) Displays the summary information of the configuration.

tag

(Optional) Displays the status and content of E.164 pattern maps.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

You can use the show voice class e164-pattern-map command to display the status of a map and all E.164 patterns in the map. This command is used not only to display E.164
                              patterns in a text file, but E.164 patterns configured through the CLI. But for parsing error, the command applies only to
                              a text file.

## Examples

The following is sample output from the show voice class e164-pattern map command:

```
Device# show voice class e164-pattern-map summary e164-pattern-map 1
-----------------------------------------
It has 100 entries
It is populated from url http://http-host/config-files/destination-pattern-map.cfg

e164-pattern-map 2
-----------------------------------------
It has 23 entries

e164-pattern-map 3
-----------------------------------------
Loading failed on url http://http-host/config-files/destination-pattern-map-1.cfg

e164-pattern-map 4
-----------------------------------------
Parsing error on patterns: “123gh” “1*g”
It is populated from url http://http-host/config-files/destination-pattern-map-2.cfg
```

### Related Commands

Command

Description

destination e164-pattern-map

Links a destination E.164 pattern map to a dial peer.

url

Specifies the URL of a text file that has E.164 patterns configured on an E.164 pattern map.

## show voice class e164-translation

To display the configuration of a voice class E.164 translation table, use the show voice class e164-translation command in privileged EXEC mode.

show voice class e164-translation tag

### Syntax Description

tag

Displays the status and content of the voice class E.164 translation table. The range is from 1 to 10000.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

## Examples

The following example displays the E.164 translation table. The incoming call numbers +41993000000 and  +41993000001 are
                              translated, and replaced by +418893000000 and +418893000001 respectively.

```
Router# show voice class e164-translation Voice class e164-translation: 1         AdminStat: Up
 Description:
 URL: ftp://test:test123@8.0.0.200/test_e164.cfg
      (Loaded:TRUE Valid: TRUE)

 Duplicate error count:    0
 Syntax error count:    0
 Error count:    0

 Total Translation Rules: 2

 Rule#  Match Call Number                 Replace Call Number
 -----  -----------------                 -------------------
 1      +41993000000                      +418893000000
 2      +41993000001                      +418893000001

 Total Rules from Internal Sorted list: 2

 Match Reverse Call Number         Match Call Number
 -------------------------         -----------------
 00000039914+                      +41993000000
 10000039914+                      +41993000001

 Lookup Array Setup:

 Offset  Match Reverse Number              Match Call Number
 ------  -------------------               -----------------
 12      00000039914+                      +41993000000
```

### Related Commands

Command

Description

show voice class e164-pattern-map

## show voice class phone-proxy

To display the details of the sessions and file buffer function being conducted through the all the phone proxies, use the show voice class phone-proxy command in privileged EXEC mode.

show voice class phone-proxy [ file-buffer [detail] | sessions ]

## Syntax Description

file-buffer

(Optional) Shows the summary of phone proxy file buffer function working status.

detail

(Optional) Shows the details of phone proxy file buffer.

sessions

(Optional) Shows the phone proxy instance mapping status between phone and dial peer signal-address and protocol status.

### Command Modes

Privileged EXEC mode

## Command History

15.3(3)M

This command was introduced.

IOS XE Fuji Release 16.8.1

This command was modified. The command was enhanced to display phone proxy file buffer details.

## Examples

The following example shows sample output from the show voice class phone-proxy command:

```
Device# show voice class phone-proxy Phone-Proxy 'mypp':
 Description: mycluster
   Access Secure: secure 
   Tftp-client address: 198.51.100.2
   Tftp-server address: 198.51.100.101
   Capf server address: 198.51.100.101
   CUCM service settings: preserve(default)
   Ctl file name: myctl
   Session-timeout: 180 seconds
   Max-concurrent-sessions: 300
   Current sessions: 10
   Configuration status: complete
   Dialpeers associated: 
      Name                      State
      ---------------------------------
      dialpeer1                     inactive
      dialpeer2                     active
      dialpeer3                     active
Phone-Proxy 'test': 
Description: test-cluster
   Access secure: nonsecure (default)
   Tftp-client address: 10.0.0.2
   Tftp-server address: 10.0.0.1
   Local capf server address: 104.0.0.3
   CUCM service settings: disable
   Ctl file name: ctl_test
   Session-timeout: 180 seconds
   Max-concurrent-sessions: 300
   Current sessions: 20
   Configuration status: not complete
   Dialpeers associated: 
      Name                      State
      ---------------------------------
      dialpeer 4                     inactive
      dialpeer 5                     inactive
```

The following shows details of the sessions being conducted through the phone proxy:

```
Device# show voice class phone-proxy sessions Phone-Proxy 'mypp':
               srcaddr:port         dstaddr:port     vrf 
            ------------         -------------    ----
-------------Sessions of Dialpeer dialpeer1-------
 |Access:   10.0.100.11:2000    10.0.100.15:69    test1     |
 |Core  :   192.168.0.2:10002   192.169.0.101:69   global   |
  ------------------------------------------------------------------------
 ------------------------------------------------------------------------
 |Access:   10.0.100.35:2004    10.0.100.15:69    test1     |
 |Core  :   192.168.0.2:10008   192.169.0.101:69   global   |
  ------------------------------------------------------------------------
                                              
 |Access:   10.0.100.21:4000    10.0.100.15:69    test1     |
 |Core  :                                                   |
  ------------------------------------------------------------------------

Phone-Proxy 'test':
               srcaddr:port         dstaddr:port     vrf 
            ------------         -------------    ----
-------------Sessions of Dialpeer dialpeer1----------------
 |Access:   10.2.100.9:2000      10.2.100.15:69    test1     |
 |Core  :   20.21.21.101:10002   20.21.21.2:69     global   |
  ------------------------------------------------------------------------
                                               
 |Access:   10.2.100.21:4000    10.2.100.15:69    test1     |
 |Core  :                                                   |
  ------------------------------------------------------------------------
```

## show voice class resource-group

To display the resource group configuration information for a specific resource group or all resource groups, use the show voice class resource-group command in privileged EXEC mode.

show voice class resource-group { tag | all }

### Syntax Description

tag

Unique tag for the resource group.

all

Displays information for all voice resource groups.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.1(2)T

This command was introduced.

### Usage Guidelines

You can use the show voice class resource-group command to display the parameters configured to monitor resources.

## Examples

The following is sample output from the show voice class resource-group command:

```
Router> enable Router# show voice class resource-group 2 Resource Availability Indicator status 
Resource Index 2
Resource Type:SYSTEM
         Status: Low threshold
Resource Type: MEM Subtype: io-mem Low/High watermark: 2/5
         Status: Low threshold
Report Interval 34
------------------------------------------------------------
```

The table below describes the significant fields shown in the display.

Field

Description

Resource Index

Unique index value to identify the resource group.

Resource Type

Type of the resource being monitored.

Status

Status of the resource.

Subtype

Subtype of the resource being monitored.

Report Interval

Periodic reporting interval for the resource being monitored. The status of the resource being monitored is reported based
                                          on the preconfigured timer value.

### Related Commands

Command

Description

debug rai

Enables debugging for Resource Allocation Indication (RAI).

rai target

Configures the SIP RAI mechanism.

resource (voice)

Configures parameters for monitoring resources, use the resource command in voice-class configuration mode.

periodic-report interval

Configures periodic reporting parameters for gateway resource entities.

voice class resource-group

Enters voice-class configuration mode and assigns an identification tag number for a resource group.

## show voice class server-group

To display the configurations for all configured server groups or a specified server group, use the show voice class server-group command in privileged EXEC mode.

show voice class server-group [ server-group-id | dialpeer dialpeer-tag ]

server-group-id

Unique server group ID to identify the server group.

dialpeer dialpeer-tag

Unique number of a dialpeer that is associated with a server group.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Release 3.11S

15.4(1)T

The following commands were introduced or modified: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) .

The following command is introduced under voice class server-group . huntstop rule-tag resp-code from_resp_code to to_resp_code .

### Usage Guidelines

You can use the show voice class server-group command to display the configurations for all configured server groups or a specified server group.

## Examples

The following is sample output from the show voice class server-group command:

```
Router> enable Router# show voice class server-group 1 AdminStatus: Up              OperStatus: Up
            Hunt-Scheme: preference      Last returned server:
            Description: server-group for huntstop feature testing
            Total Huntstop tags: 1
            Tag ID From Response code       To Response code         
            ------ -------------------      ------------------       
             1     404                      404
             2     410                      599
            -------------------------------------
            Total server entries: 3  
            Pref     Type    IP Address      IP Port
            --------------------------------------------------------
            1         ipv4     10.1.1.1                                 
            2         ipv4     10.1.1.2                 34515         
            3         ipv4     10.1.1.3
```

The table below describes the significant fields shown in the display.

Field

Description

description

Description of the server group.

ipv4 port preference

A server IPv4 address as a part of this server group along with an optional port number and preference order.

ipv6 port preference

A server IPv6 address as a part of this server group along with an optional port number and preference order.

hunt-scheme

A hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this server
                                          group) for the setting up of outgoing calls.

hunt-stop

Stops hunting based on (configurable) response codes in the Server Group along with dial-peer.

### Related Commands

Command

Description

voice class server-group

Enters voice-class configuration mode and configures server groups (groups of IPv4 and IPv6 addresses), description, hunt-scheme,
                                          huntstop, and shutdown (Server Group).

## show voice class sip-options-keepalive

To display the details of connectivity between CUBE VoIP dial peers and SIP servers, use show voice class sip-options-keepalive command in privileged EXEC mode.

show voice class sip-options-keepalive [ global | profile-tag ]

global

Displays information on voice class sip-options-keepalive global.

profile-tag

The unique tag for SIP options keepalive profile. Range: 1–10000.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

Use show voice class sip-options-keepalive global command to view the global and the instant status information of the out-of-dialog (OOD) ping mechanism that is configured
                              between the dial peers and SIP servers.

## Examples

The following sample output displays the details of the server group and the OOD Keepalive Profiles defined on the server
                              group.

```
Router# show voice class sip-options-keepalive global Server Group: 1
  List of OOD Keepalive Profile(s):
        171
----------------------------------------------------
```

### Related Commands

voice-class sip options-keepalive

Monitors connectivity between CUBE VoIP dial-peers and SIP servers. This command also configures OOD ping mechanism between
                                          any number of destinations.

## show voice class sip-predefined-profiles

To display the SIP profiles defined on a CUBE router, use show voice class sip-predefined-profiles command in privileged EXEC mode.

show voice class sip-predefined-profiles

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

The SIP profiles enable SIP messaging between incompatible devices on the network. Use this command to display the SIP profiles
                              defined on all CUBE routers in a network.

## Examples

The following sample output displays detailed information about all predefined SIP profiles:

```
Router# show voice class sip-predefined-profiles voice class sip-hdr-passthrulist 20001
passthru-hdr Call-Info
passthru-hdr Content-ID
passthru-hdr Allow-Events
passthru-hdr Supported
passthru-hdr Remote-Party-I
passthru-hdr Require
passthru-hdr Referred-By
      
voice class sip-profiles 20001
  request INVITE sip-header Cisco-Guid remove
```

## show voice class uri

To display summary or detailed information about configured uniform resource identifier (URI) voice classes, use the show voice class uri command in user EXEC or privileged EXEC mode.

show voice class uri [ tag | summary ]

### Syntax Description

tag

(Optional) Specific URI voice class for which to display detailed information.

summary

(Optional) Displays a short summary of all URI voice classes.

### Command Default

Detailed information about the configured URI voice classes is displayed.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

15.1(2)T

This command was modified. The command was enhanced to display the mutiple hosts in the configured URI classes.

### Usage Guidelines

If both the tag argument and summary keyword are omitted, the output displays detailed information about all URI voice classes.

## Examples

The following is sample output from this command:

```
Router# show voice class uri Voice URI class: 100
     SNMP status = Active
     Schema = sip
     pattern = 12345
Voice URI class: 101
     SNMP status = Active
     Schema = sip
     pattern = 555....
Voice URI class: 102
     SNMP status = Active
     Schema = sip
     user-id = demo
     host = cisco
     phone context = 
Voice URI class: 103
    SNMP status = Active
    Schema = tel
    phone number = 555....
    phone context = 
Voice URI class: 700
     SNMP status = Active
     Schema = sip
     pattern = elmo@sip.tgw.com*
Voice URI class: 104
     SNMP status = Active
     Schema = tel
     pattern = 5550134
Voice URI class: 700
     SNMP status = Active
     Schema = sip
     user-id = 
     host = exmp.example.com
     phone context = 
     
     host instances:
      ipv4:192.168.0.1
      ipv6:[2001:0DB8:0:1:FFFF:1234::5]
      dns:ogw.example.com
```

The following is sample output from this command with the summary keyword:

```
Router# show voice class uri summary _____________________________________________________________
Class Name                       Schema     SNMP
-------------------------------------------------------------
100                              sip       Active
101                              sip       Active
102                              sip       Active
103                              tel       Active
700                              sip       Active
104                              tel       Active
_____________________________________________________________
```

The table below describes the significant fields in the displays.

Field

Description

Class Name

Tag that identifies the URI voice class.

Schema

Whether the voice class is used for SIP or TEL URIs.

pattern

Pattern used to match the entire SIP or TEL URI as configured with the pattern command.

user-id

Pattern used to match the user-id field in the SIP URI as configured with the user-id command.

host

Pattern used to match the host field in the SIP URI with the host command.

phone number

Pattern used to match the phone number field in a TEL URI as configured with the phone number command.

phone context

Pattern used to match the phone context field in a SIP or TEL URI as configured with the phone context command.

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

show dialplan incall uri

Displays which dial peer is matched for a specific URI in an incoming call.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

## show voice connectivity summary

To display the results of the last connectivity checks performed on all analog Foreign Exchange Station (FXS) ports on a router,
                              use the show voice connectivity summary command in privileged EXEC mode.

show voice connectivity summary

### Syntax Description

This command has no arguments or keywords.

### Command Default

A summary of the last connectivity checks performed on all analog FXS ports on a router is displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.1(3)T

This command was introduced.

## Examples

The following example shows how the show voice connectivity summary command is used:

```
Router> enable Router# show voice connectivity summary .
.
.
! The summary results include information such as the port address, type of connectivity
! check performed, result of connectivity check for each port
```

## show voice data

To display the call control application programming interface (CCAPI) and Telephony Service Provider (VTSP) data structures,
                              use the show voice data command in user EXEC or privileged EXEC mode.

show voice data { ccapi { ccCallEntry { call-id | all } | ccCallInfo } | vtsp { ccCallInfo | vtsp_cdb { call-id | all }} | vtsp_sdb { call-id | all }}

### Syntax Description

ccapi

Displays all the CCAPI calls.

ccCallEntry

Displays the call entry.

call-id

Call identifier (ID) in the range 1 to 4294967295.

all

Displays all the call entries.

ccCallInfo

Displays the call information.

vtsp

Displays all the VTSP calls.

vtsp_cdb

Displays all the VTSP call control back calls.

vtsp_sdb

Displays all the VTSP signalling data block calls.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(22)T

This command was introduced in a release earlier than Cisco IOS Release 12.4(22)T.

## Examples

The following is sample output from the show voice data command:

```
Router# show voice data ccapi ccCallEntry all CallEntry=0x6B8051B0; CallID=7(0x7)::
element:{ 0x6B8051B0; 0x6B8051B4; 0x6B8051B8; } 7; <appReturnStack>; 1735408; 1; 0x6B8051D8; 7; 8; callInfo:{ 0; 112233; <NULL>; 889988; <NULL>; <NULL>; <NULL>; <NULL>; <NULL>; <NULL>; <NULL>; FALSE; FALSE; TRUE; <NULL>; 0; 0; 0; <NULL>; RegularLine; Unknown; D356CC33-E54B-11D7-8005-00169D6EE1AE; D356CC33-E54B-11D7-8005-00169D6EE1AE; 0; 0; 0; 0; 0; 998877; 0x6B80547C; 0; TRUE; FALSE; 0.0.0.0; 0.0.0.0; 0x6B8054A0; 0x6B8054A4; 0x6B8054A8; 0x6B8054AC; 0; FALSE; FALSE; 0x6B8054BC; 0; call_decode:{ redirect_info:{ 0xFF; 0xFF; 0xFF; 0xFF; 0xFF; 0xFF; 0x00; 0xFF; 255; <NULL>; <NULL>; 0x00; FALSE; FALSE; } 0x00; 0x80; 0x00; 0x80; 0; 0x00; <NULL>; 0; 0x00; <NULL>; FALSE; FALSE; FALSE; FALSE; -1; <NULL>; TRUE; <transfer_info>; FALSE; 129; 40; 104; 0xFF; TRUE; } FALSE; D357685B-E54B-11D7-8016-CB962D72A90A; 0; 0; 0; 0; 0; 0; 0x6B805634; FALSE; <NULL>; FALSE; FALSE; FALSE; 0; 0; 0; <NULL>; ISDN 7/0:1:D; FALSE; FALSE; FALSE; 0x00; <NULL>; <NULL>; 0x6B80585C; 0; 0x6B805864; } 0x6B805914; 0x6B805918; 0x6B80591C; 0x6B805920; <altAssocList>; FALSE; 0x6B80593C; 0x6B805940; 0x6B805944; FALSE; 0; 65535; TRUE; 0; FALSE; 1; <disconnect_timer>; <inter_digit_timer>; 10000; <initial_timer_timestamp>; 10000; FALSE; 0; 0; -1; <NULL>; 0x6B8059F8; <evCategoryMask>; <evDetailMask>; 4294967295; 0x6B805C48; FALSE; 0; 0; TRUE; TRUE; TRUE; 0; 0; 0x6B805C6C; FALSE; 0; 4; 0; -1; FALSE;
CallEntry=0x6B805C90; CallID=8(0x8)::
element:{ 0x6B805C90; 0x6B805C94; 0x6B805C98; } 8; <appReturnStack>; 1735408; 2; 0x6B805CB8; 8; 7; callInfo:{ 0; 112233; <NULL>; 889988; <NULL>; 112233; 112233; <NULL>; <NULL>; <NULL>; <NULL>; FALSE; FALSE; TRUE; <NULL>; 0; 0; 0; <NULL>; RegularLine; Unknown; D356CC33-E54B-11D7-8005-00169D6EE1AE; D356CC33-E54B-11D7-8005-00169D6EE1AE; 7; 0; 0; 0; 2; 112233; 0x6B805F5C; 0; FALSE; FALSE; 0.0.0.0; 0.0.0.0; 0x6B805F80; 0x6B805F84; 0x6B805F88; 0x6B805F8C; 0; FALSE; FALSE; 0x6B805F9C; 0; call_decode:{ redirect_info:{ 0xFF; 0xFF; 0xFF; 0xFF; 0xFF; 0xFF; 0x00; 0xFF; 255; <NULL>; <NULL>; 0x00; FALSE; FALSE; } 0x00; 0x80; 0x00; 0x00; 0; 0x00; <NULL>; 0; 0x00; <NULL>; FALSE; FALSE; FALSE; FALSE; -1; <NULL>; TRUE; <transfer_info>; FALSE; 129; 40; 104; 0xFF; TRUE; } FALSE; D357685B-E54B-11D7-8016-CB962D72A90A; 0; 0; -1; 0; 0; 0; 0x6B806114; FALSE; <NULL>; FALSE; FALSE; FALSE; 0; 0; 0; <NULL>; ISDN 7/0:1:D; TRUE; FALSE; FALSE; 0x00; <NULL>; <NULL>; 0x6B80633C; 0; 0x6B806344; } 0x6B8063F4; 0x6B8063F8; 0x6B8063FC; 0x6B806400; <altAssocList>; FALSE; 0x6B80641C; 0x6B806420; 0x6B806424; FALSE; 0; 65535; FALSE; 0; FALSE; 1; <disconnect_timer>; <inter_digit_timer>; 10000; <initial_timer_timestamp>; 10000; FALSE; 0; 0; -1; <NULL>; 0x6B8064D8; <evCategoryMask>; <evDetailMask>; 4294967295; 0x6B806728; FALSE; 0; 0; TRUE; TRUE; TRUE; 0; 0; 0x6B80674C; FALSE; 0; 4; 0; -1; FALSE;
```

The table below describes the significant fields shown in the display.

Field

Description

CallEntry

Displays the call entry identification number used for the incoming call leg.

CallID

Displays the specified call identifier value.

element

Indicates the various configuration values for the service element.

callInfo

Displays the call informaton.

call_decode

Displays the status of the audio decoder.

redirect_info

Displays the forwarding request information when a call is being forwarded.

transfer_info

Displays the call transfer request information.

disconnect_timer

Displays the timeout value, in seconds, specified to disconnect the call.

inter_digit_timer

Displays the maximum allowable time, in seconds, between digits dialed by the user.

### Related Commands

Command

Description

debug voip ccapi error

Traces error logs in the call control API.

## show voice dnis-map

To display current dialed-number identification service (DNIS) map information, use the show voice dnis-map command in privileged
                              EXEC mode.

show voice dnis-map [ dnis-map-name | summary ]

### Syntax Description

dnis - map - name

(Optional) Name of a specific DNIS map.

summary

(Optional) Displays a short summary of each DNIS map.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660.

### Usage Guidelines

This command displays a detailed description of each configured DNIS map.

If the name of a specific DNIS map is entered, the command displays detailed information about only that DNIS map.

If the summary keyword is used, the command displays a one-line summary about each DNIS map.

If an asterisk is displayed next to a DNIS map name when the summary keyword is used, it means that the DNIS map is configured, but not running. Normally this is because the external text file
                              was not successfully loaded, for example:

```
dnis-map            Entries    URL
--------            -------    ---
dmap1               1
*dmap4              0          http://dnismaps/dnismap4.txt
```

To create a DNIS map, use the voice dnis - map command. You can link to an external DNIS map text file or use the dnis command to add numbers to a DNIS map in Cisco IOS software.

To associate a DNIS map with a dial peer, use the dnis - map command.

## Examples

The following is sample output from the show voice dnis-map command:

```
Router# show voice dnis-map
There are 2 dnis-maps configured
Dnis-map dmap1
-----------------------------------------
  It has 3 entries
  It is not populated from a file.
DNIS                  URL
----                  ---
 4085551212           tftp://global/tickets/movies.vxml
 4085551234           tftp://global/tickets/plays.vxml
 4085554321           tftp://global/tickets/games.vxml
Dnis-map dmap4
-----------------------------------------
  It has 0 entries
  It is populated from url http://dnismaps/dnismap4.txt
DNIS                URL
----                ---
```

The table below describes the fields shown in this output.

Field

Description

Dnis-map

Name of a DNIS map that is configured on the gateway.

DNIS

Destination telephone number specified in this DNIS map.

URL

Location of the VoiceXML document to invoke for this DNIS number.

The following is sample output from the show voice dnis-map summary command:

```
Router# show voice dnis-map summary
There are 3 dnis-maps configured
dnis-map            Entries    URL
--------            -------    ---
dmap1               3
dmap4               0        http://dnismaps/dnismap4.txt
dmap6               8
```

describes the fields shown in this output.

Field

Description

dnis-map

Names of the DNIS maps that are configured on the gateway.

Entries

Number of entries in DNIS maps that reside on the gateway. This field displays 0 if the DNIS map is a text file stored on
                                          an external server.

URL

Location of externally stored DNIS maps.

### Related Commands

Command

Description

dnis

Adds a DNIS number to a DNIS map.

dnis - map

Associates a DNIS map to a dial peer.

voice dnis - map

Enters DNIS map configuration mode to create a DNIS map.

voice dnis - map load

Reloads a DNIS map that has changed since the previous load.

## show voice dsmp stream

To display the current session of voice Distributed Stream Media Processor (DSPM) media stream, the recent state transitions,
                              and stream connection, use the show voice dsmp stream command in privileged EXEC mode.

show voice dsmp stream { stream ID | leg }

### Syntax Description

stream ID

DSMP media stream identifier. Range: 1 to 4294967295.

leg

Call leg corresponding to a caller ID.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

When the calls hang, use this command to get the current sessions of the DSMP media stream. You can look at the DSMP state
                              transitions corresponding to the calls and find out the problems.

## Examples

The following example shows an output of a typical DSMP session in a VoIP call. This call consists of four streams, two input
                              streams and two output streams:

```
Router# show voice dsmp stream Total number of streams in use is: 4
 
Stream information:: stream=1
Type: TDM, Direction: OUTPUT
Fax/Modem Type: voice
Xmit Function: 0x00000000
Xmit function is Enabled
Call ID: 4, Conference ID: -1
 
Session information:: session=0x658CA948 dsp_intf=0x642DDD8C dsp_name=1/9:3
 
connections=2 streams=4 (5 1 4 3 )
current state S_DSMP_VC_RUNNING current container simple_voice_container
State Transitions: timestamp (container, state) -- event -> (container, state)
367121.596 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367121.796 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367122.712 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367122.732 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367122.920 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367122.940 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367123.112 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367123.152 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367124.432 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367124.632 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367124.732 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367124.932 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367125.032 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367125.232 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.140 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.160 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.340 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.380 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.548 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367126.568 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
 
Session log information::
Regular Timer:
    Timer start operations:
             Timestamp    Duration(ms)        Caller
            367122.652            4000    0x6113397C
            367119.388            4000    0x6113397C
            367117.624           10000    0x6112ED88
 
    Timer stop operations:
             Timestamp    Duration(ms)        Caller
            367122.656               0    0x61133A98
            367119.392               0    0x61133A98
            367117.624               0    0x6112F060
            367117.624               0    0x6112EE24
    Number of overwritten entries: 2
          
Periodic Timer:
    Timer start operations:
    None
    Timer stop operations:
    None
Packet suppression is disabled
 
Stream information:: stream=3
Type: PACKET, Direction: OUTPUT
Fax/Modem Type: voice
Xmit Function: 0x6111D324
Xmit function is Enabled
Call ID: 3, Conference ID: 2
DSP Encap: 0x1
Codec Mask: 0x4; Codec Bytes: 20
Fax Rate Mask: 0x2; Fax Bytes: 20; T38 Disabled
VAD Mask: 0x2
 
Session information:: session=0x658CA948 dsp_intf=0x642DDD8C dsp_name=1/9:3
 
connections=2 streams=4 (5 1 4 3 )
current state S_DSMP_VC_RUNNING current container simple_voice_container
State Transitions: timestamp (container, state) -- event -> (container, state)
367128.452 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367128.652 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.556 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.588 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.756 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.796 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.968 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367129.988 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367131.276 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367131.472 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367131.572 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367131.772 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367131.872 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367132.072 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367132.980 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.000 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.180 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.220 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.400 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.420 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
 
Session log information::
Regular Timer:
    Timer start operations:
             Timestamp    Duration(ms)        Caller
            367131.020            4000    0x6113397C
            367128.316            4000    0x6113397C
            367122.652            4000    0x6113397C
            367119.388            4000    0x6113397C
    Number of overwritten entries: 1
 
    Timer stop operations:
             Timestamp    Duration(ms)        Caller
            367131.024               0    0x61133A98
            367128.320               0    0x61133A98
            367122.656               0    0x61133A98
            367119.392               0    0x61133A98
    Number of overwritten entries: 4
 
Periodic Timer:
    Timer start operations:
    None
    Timer stop operations:
    None
Packet suppression is disabled
 
Stream information:: stream=4
Type: PACKET, Direction: INPUT
Fax/Modem Type: voice
Xmit Function: 0x61F2CA34
Xmit function is Enabled
Call ID: 3, Conference ID: 2
DSP Encap: 0x1
Codec Mask: 0x4; Codec Bytes: 20
Fax Rate Mask: 0x2; Fax Bytes: 20; T38 Disabled
VAD Mask: 0x2
 
Session information:: session=0x658CA948 dsp_intf=0x642DDD8C dsp_name=1/9:3
 
connections=2 streams=4 (5 1 4 3 )
current state S_DSMP_VC_RUNNING current container simple_voice_container
State Transitions: timestamp (container, state) -- event -> (container, state)
367133.400 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367133.420 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367134.692 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367134.892 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367134.992 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367135.192 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367135.292 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367135.492 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.400 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.432 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.600 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.640 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.812 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367136.840 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.112 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.312 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.412 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.612 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.712 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.912 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
 
Session log information::
Regular Timer:
    Timer start operations:
             Timestamp    Duration(ms)        Caller
            367137.648            4000    0x6113397C
            367134.440            4000    0x6113397C
            367131.020            4000    0x6113397C
            367128.316            4000    0x6113397C
    Number of overwritten entries: 3
 
    Timer stop operations:
             Timestamp    Duration(ms)        Caller
            367137.648               0    0x61133A98
            367134.440               0    0x61133A98
            367131.024               0    0x61133A98
            367128.320               0    0x61133A98
    Number of overwritten entries: 6
          
Periodic Timer:
    Timer start operations:
    None
    Timer stop operations:
    None
Packet suppression is disabled
 
Stream information:: stream=5
Type: TDM, Direction: INPUT
Fax/Modem Type: voice
Xmit Function: 0x00000000
Xmit function is Enabled
Call ID: 4, Conference ID: -1
 
Session information:: session=0x658CA948 dsp_intf=0x642DDD8C dsp_name=1/9:3
 
connections=2 streams=4 (5 1 4 3 )
current state S_DSMP_VC_RUNNING current container simple_voice_container
State Transitions: timestamp (container, state) -- event -> (container, state)
367138.712 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367138.912 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367139.824 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367139.844 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367140.024 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367140.064 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367140.244 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367140.252 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367141.536 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367141.736 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367141.836 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367142.036 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367142.136 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367142.336 (simple_voice_container, S_DSMP_VC_RUNNING) -- E_DSMP_CC_PLAY_REQ -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.244 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.264 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.444 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.484 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.652 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_BEGIN -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
367143.672 (simple_voice_container, CNFSM_CONTAINER_STATE) -- E_DSMP_DSP_DTMF_DIGIT_END -> (simple_voice_container, CNFSM_NO_STATE_CHANGE)
 
Session log information::
Regular Timer:
    Timer start operations:
             Timestamp    Duration(ms)        Caller
            367137.648            4000    0x6113397C
            367134.440            4000    0x6113397C
            367131.020            4000    0x6113397C
            367128.316            4000    0x6113397C
    Number of overwritten entries: 3
          
    Timer stop operations:
             Timestamp    Duration(ms)        Caller
            367137.648               0    0x61133A98
            367134.440               0    0x61133A98
            367131.024               0    0x61133A98
            367128.320               0    0x61133A98
    Number of overwritten entries: 6
 
Periodic Timer:
    Timer start operations:
    None
    Timer stop operations:
    None
Packet suppression is disabled
```

The table below describes the significant fields shown in the display.

Field

Description

Stream information

Shows stream ID.

Type

Type of stream.

Direction

Direction of stream.

Fax/Modem Type

Type of fax or modem.

Xmit Function

Transmit function in use.

Call ID

Caller ID of call leg.

Conference ID

Conference ID.

Session information

Information about the associated session.

connections

Number of stream connections.

streams

Number of streams.

current state

Current state and container of the session.

State Transitions

State transitions of the associated session.

DSP Encap

Encapsulation associated with the session.

Codec Mask

Codec mask associated with the session.

Fax Rate Mask

Fax rates associated with the session.

Fax Bytes

Fax bytes associated with the session.

VAD Mask

VAD mask associated with the session.

### Related Commands

Command

Description

show call active voice

Displays call information for voice calls in progress.

show voice call

Displays the call status for voice ports on the Cisco router.

## show voice dsp

To display either the current status or the selective statistics pertaining to the digital signal processor (DSP) voice channels,
                              use the show voice dsp command in User EXEC mode or Privileged EXEC mode.

show voice dsp [ active [ slot slot-number [slot-number] ]
                              							
                              							 | capabilities slot slot-number dsp dsp-number | cpu-load slot slot-number dsp dsp-number [ reset ]
                              							
                              							 | detailed | error | 
                              								 [ group all | sorted-list ] slot slot-number | signalling | voice | version [ slot | slot / dsp ] [ slot | slot / dsp ]
                              							
                              						]

### Cisco ASR 1000 Series Routers

show voice dsp [ active [ slot slot-number ]
                              							
                              							 | capabilities slot slot-number dsp dsp-number | cpu-load slot slot-number dsp dsp-number [ reset ]
                              							
                              							 | crash-dump | detailed | error | group { all | slot slot-number }
                              							
                              							 | signalling | sorted-list slot slot-number | voice ]

### Syntax Description

active

(Optional) Displays the active channels.

slot slot-number [ slot-number ]

(Optional) Specifies either a single slot or the first slot in a range. To specify a range of slots, enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All the slots in the range are affected by the command.

capabilities

(Optional)  Displays DSP capabilities.

dsp dsp-number

(Optional) Specifies the DSP on the slot.

cpu-load

(Optional)  Displays DSP CPU load.

reset

(Optional) Resets DSP CPU statistics.

crash-dump

(Optional) Displays the DSP crash dump status.

To enable a DSP crash dump, set the file limit to a non-zero number, and set the destination to a valid file name.

detailed

(Optional)  Displays detailed information about DSP status.

error

(Optional)  Displays DSP errors.

group

(Optional)  Displays DSP group information.

all

(Optional) Displays all the DSP group details.

sorted-list

(Optional)  Displays a DSP-sorted list.

signaling

(Optional)  Displays DSP signaling channel usage.

voice

(Optional)  Displays DSP voice channel usage.

version

(Optional)  Displays the DSP firmware version.

slot

(Optional) The first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument.
                                          The second slot specifies the end of the range. All the slots in the range are affected by the command.

/ dsp

(Optional) The first DSP in a range. To specify a range of DSPs, you can enter a  second DSP in the syntax of this argument.
                                          The second DSP specifies the end of the range. All the DSPs in the range are affected by the command. The slash mark is required.

### Command Default

No default behavior or values.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE 17.18.2

This command was implemented on the C8375-E-G2 secure router.

Cisco IOS XE Release 3.3.0S

The show voice dsp group all command output was modified for SPA-DSP on the Cisco ASR 1000 Series Router.

Cisco IOS XE Release 3.2S

This command was implemented on the Cisco ASR 1000 Series Router.

Cisco IOS XE Release 2.5

This command was integrated into Cisco IOS XE Release 2.5.

12.4(11)T

The command was modified. Command output was enhanced to display information about the DSP H.320 channels.

12.4(4)XC

The command was modified. The version keyword was added and the command was implemented on the Cisco AS5350XM and Cisco AS5400XM platforms.

12.4(4)T

The command was modified. The command output was enhanced to display the codec setting for modem relay operation.

12.3(14)T

The command was modified. The command output was enhanced to display status information pertaining to the NM-HDV network
                                          module TI-549 DSPs.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.0(7)XK

This command was implemented on the Cisco 2600 Series and Cisco 3600 Series, and the display format was modified.

11.3(1)MA

This command was introduced on the Cisco MC3810.

### Usage Guidelines

Use this command when abnormal behavior occurs in the DSP voice channels. The channel or channels should have an active voice
                              call at the time the command is executed.

Cisco ASR 1000 Series Routers

In Cisco IOS XE Release 3.3.0s, the show voice dsp group all command output that is displayed when a SPA-DSP undergoes call recovery is enhanced. The command output is seen only during
                              the call recovery process, which lasts for a few milliseconds. The additional information that is included in the command
                              output pertains to: HA State : DSP_HA_STATE_PENDING1. The additional information is displayed when a SPA-DSP undergoes call
                              recovery.

## Examples

The following sample output shows how HA State : DSP_HA_STATE_PENDING1 is added. The additional command output is seen only
                              in Cisco IOS XE Release 3.3.0S and later releases:

```
Router# show voice dsp group all Show DSP group all
 
DSP groups on slot 0 bay 0:
dsp 1:
  State: UP
  HA State : DSP_HA_STATE_PENDING1
  Max signal/voice channel: 43/43
  Max credits: 645
  num_of_sig_chnls_allocated: 43
  Transcoding channels allocated: 43
  Group: FLEX_GROUP_XCODE, complexity: LOW
    Shared credits: 0, reserved credits: 645
    Transcoding channels allocated: 24
    Credits used (rounded-up): 360
```

## Examples

The following sample output shows the current status of the codec, set for modem relay, on channel 1:

```
Router# show voice dsp ----------------------------FLEX VOICE CARD 1 ------------------------------
                           *DSP VOICE CHANNELS*
DSP   DSP             DSPWARE CURR  BOOT                         PAK   TX/RX
TYPE  NUM CH CODEC    VERSION STATE STATE   RST AI VOICEPORT TS ABRT PACK COUNT
===== === == ======== ======= ===== ======= === == ========= == ==== ============
C5510 001 01 modem-re 4.5.909 busy  idle      0  0 1/1/0     05    0      298/353
                           *DSP SIGNALING CHANNELS*
DSP   DSP             DSPWARE CURR  BOOT                         PAK   TX/RX
TYPE  NUM CH CODEC    VERSION STATE STATE   RST AI VOICEPORT TS ABRT PACK COUNT
===== === == ======== ======= ===== ======= === == ========= == ==== ============
C5510 001 05 {flex}   4.5.909 alloc idle      0  0 1/1/3     02    0         15/0
C5510 001 06 {flex}   4.5.909 alloc idle      0  0 1/1/2     02    0         17/0
C5510 001 07 {flex}   4.5.909 alloc idle      0  0 1/1/1     06    0         31/0
C5510 001 08 {flex}   4.5.909 alloc idle      0  0 1/1/0     06    0        321/0
------------------------END OF FLEX VOICE CARD 1 ----------------------------
```

## Examples

The following sample output shows the current status of all the DSP voice channels:

```
Router# show voice dsp DSP# 0, channel# 0 G729A BUSY
DSP# 0, channel# 1 G729A BUSY
DSP# 1, channel# 2 FAX IDLE
DSP# 1, channel# 3 FAX IDLE
DSP# 2, channel# 4 NONE BAD
DSP# 2, channel# 5 NONE BAD
DSP# 3, channel# 6 NONE BAD
DSP# 3, channel# 7 NONE BAD
DSP# 4, channel# 8 NONE BAD
DSP# 4, channel# 9 NONE BAD
DSP# 5, channel# 10 NONE BAD
DSP# 5, channel# 11 NONE BAD
```

## Examples

The following is a sample output of this command on a Cisco 1750 router:

```
Router# show voice dsp DSP#0: state IN SERVICE, 2 channels allocated
channel#0: voice port 1/0, codec G711 ulaw, state UP
channel#1: voice port 1/1, codec G711 ulaw, state UP
DSP#1: state IN SERVICE, 2 channels allocated
channel#0: voice port 2/0, codec G711 ulaw, state UP
channel#1: voice port 2/1, codec G711 ulaw, state UP
DSP#2: state RESET, 0 channels allocated
```

## Examples

The following is a sample output command on a secure Survivable Remote Site Telephony (SRST) router with the NM-HDV network
                              module and the TI-549 (C549) DSP installed:

```
Router# show voice dsp DSP  DSP    DSPWARE  CURR     BOOT                              PAK   TX/RX
TYPE NUM CH CODEC    VERSION  STATE STATE  RST AI VOICEPORT TS ABORT PACK COUNT
==== === == ======== ======= ===== ======= === == ======== === ==== ===========
C549  1  01 {medium} 4.4.3    IDLE  idle     0  0   1/0:0   1   0    9357/9775
C549  1  02 {medium} 4.4.3    IDLE  idle     0      1/0:0   2   0    0/0
C549  2  01 {medium} 4.4.3    IDLE  idle     0  0   1/0:0   3   0    0/0
C549  2  02 {medium} 4.4.3    IDLE  idle     0      1/0:0   4   0    0/0
C549  3  01 {medium} 4.4.3    IDLE  idle     0  0   1/0:0   5   0    0/13
C549  3  02 {medium} 4.4.3    IDLE  idle     0      1/0:0   6   0    0/13
```

## Examples

The following is a sample output of this command on an H.320 network configured for video support:

```
Router# show voice dsp DSP  DSP             DSPWARE CURR  BOOT                         PAK     TX/RX
TYPE NUM CH CODEC    VERSION STATE STATE   RST AI VOICEPORT TS ABORT  PACK COUNT
==== === == ======== ======= ===== ======= === == ========= == ===== ============ edsp 001 01 g711ulaw  0.1 IDLE  50/0/1.1 edsp 002 02 g711ulaw  0.1 IDLE  50/0/1.2 edsp 003 01 g729r8 p  0.1 IDLE  50/0/2.1 ----------------------------FLEX VOICE CARD 1 ------------------------------
                           *DSP VOICE CHANNELS*
DSP   DSP             DSPWARE CURR  BOOT                         PAK   TX/RX
TYPE  NUM CH CODEC    VERSION STATE STATE   RST AI VOICEPORT TS ABRT PACK COUNT
===== === == ======== ======= ===== ======= === == ========= == ==== ============
C5510 001 05 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 06 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 07 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 08 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 09 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 10 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 11 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 12 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 13 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 14 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 15 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 001 16 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 01 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 02 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 03 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 04 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 05 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 06 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 07 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 08 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 09 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 10 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 11 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 12 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 13 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 14 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 15 None     9.0.105 idle  idle      0  0                 0          0/0
C5510 003 16 None     9.0.105 idle  idle      0  0                 0          0/0
*DSP H.320 CHANNELS*
DSP   DSP     TX/RX       DSPWARE CURR               PAK   TX/RX
TYPE  NUM CH  CODEC       VERSION STATE VOICEPORT TS ABRT PACK COUNT
===== === === =========== ======= ===== ========= == ==== ============
C5510 001 01  h320p(01)   9.0.105 busy  1/0/0:15  06 
      001 02  h320s(02)   9.0.105 busy  1/0/0:15  07 
      001 03  h320s(03)   9.0.105 busy  1/0/0:15  08 
      001 04  h320s(04)   9.0.105 busy  1/0/0:15  09 
      001 01a g711ulaw    9.0.105 busy                 0 1013663/5083
                                                                     00          
      001 01v h263 /h263  9.0.105 busy                 0 104908/30911
                                                                     4           
------------------------END OF FLEX VOICE CARD 1 ----------------------------
```

The table below describes the significant fields shown in the displays.

Field

Description

DSP

Number of the DSP.

channel

Number of the channel and its status.

DSP TYPE

TI-549 (C549) DSP.

DSP NUM

Number of the DSP.

CH

Channel number.

CODEC

Complexity setting.

DSPWARE VERSION

Version of DSPware.

CURR STATE

Current status of the channel: alloc (allocated), busy, or idle.

BOOT STATE

DSP readiness, either idle or in service.

RST

Number of times the DSP has been reset or restarted.

AI

Alarm indication count on the channel.

VOICEPORT

Voice card number and slot.

TS

Time slot.

PAK ABORT

Number of dropped packets.

TX/RX PACK COUNT

Number of transmitted and received packets.

## Examples

The following output shows the active DSP group information of the C8375-E-G2 router platform:

```
Router# show voice dsp group DSP groups on vdsp
         DSP default version: 0.1.717
 
         dsp 1:
             State: UP, firmware version: 1.0.827
             Max voice channel: 400
             Max credits: 6000, Voice credits: 6000  Transcoding channels allocated: 10  ** 
             Group: FLEX_GROUP_VOICE, complexity: FLEX
         dsp 2:
             State: UP, firmware version: 1.0.827
             Max voice channel: 400
```

## Examples

The following example shows the channel capabilities of the DSP profiles on C8375-E-G2 router platform:

```
router# show voice dsp capabilities Supported vDSP profiles are:
vDSP-32 (Max credits 3360)
vDSP-64 (Max credits 6720)
vDSP-256 (Max credits 26880)
vDSP-512 (Max credits 53760)
vDSP-1024 (Max credits 107520)
vDSP-2048 (Max credits 215040)

Current active vDSP profile is vDSP-500

Credit Information:

Transcode Credit:
LC (G711) Credits: 105
MC (G722/G729a) Credits: 240
HC (iLBC/G729) Credits: 420
VHC (iSAC/Opus) Credits: 420

Universal Transcode Credit:
LC (G711) Credits: 105
MC (G722/G729a) Credits: 336
HC (iLBC/G729) Credits: 672
VHC (iSAC/Opus) Credits: 840

Conference 8-party credits:
LC (G711) Credits: 420
MC (G722) Credits: 672
HC (G729/G729a) Credits: 1120
VHC (iLBC) Credits: 1120

Add-on advanced service:
NR/Ext-NR : 82
ASP : 82

Total of 2 DSPs, each with 26250 credits.
```

## Examples

The following sample output shows the DSP Type, DSP number, channel number, codecs running, DSP firmware version, and current
                              state of the channels running on the SPA-DSP inside the Cisco ASR 1000 Series Router:

```
Router# show voice dsp ----------------------------- SPA-DSP 1/1 ---------------------------
*DSP INFORMATION*
DSP    DSP               DSPWARE CURR
TYPE   NUM CH CODEC      VERSION STATE RST AI
====== === == ========= ======== ===== === ==
SP2600 001    None      26.07.00 up    4   0
SP2600 002    None      26.07.00 up    3   0
SP2600 003    None      26.07.00 up    3   0
SP2600 004    None      26.07.00 up    1   0
SP2600 005    None      26.07.00 up    1   0
SP2600 006    None      26.07.00 up    1   0
SP2600 007    None      26.07.00 up    1   0
SP2600 008    None      26.07.00 up    1   0
SP2600 009    None      26.07.00 up    1   0
SP2600 010    None      26.07.00 up    1   0
SP2600 011    None      26.07.00 up    1   0
SP2600 012    None      26.07.00 up    1   0
SP2600 013    None      26.07.00 up    1   0
SP2600 014    None      26.07.00 up    1   0
SP2600 015    None      26.07.00 up    1   0
SP2600 016    None      26.07.00 up    1   0
SP2600 017    None      26.07.00 up    1   0
SP2600 018    None      26.07.00 up    1   0
SP2600 019    None      26.07.00 up    1   0
SP2600 020    None      26.07.00 up    1   0
SP2600 021    None      26.07.00 up    1   0
------------------------- END OF SPA-DSP 1/1 -------------------------------------
```

## Examples

The following output shows the active channels on SPA-DSP located in slot 1 of the Cisco ASR 1000 Series Router:

```
Router# show voice dsp active slot 1 ------------------ SPA-DSP 1/1 ---------------------------
*DSP VOICE CHANNELS*
DSP    DSP               DSPWARE CURR
TYPE   NUM CH CODEC      VERSION STATE RST AI
====== === == ========= ======== ===== === ==
SP2600 001 01 g711ulaw  26.07.00 busy  4   0
SP2600 002 01 g711ulaw  26.07.00 busy  3   0
------------------------- END OF SPA-DSP 1/1 ------------
```

## Examples

The following example shows the channel capabilities of the different types of codecs on the Cisco ASR 1000 Series Router:

```
Router# show voice dsp capabilities slot 1 Card 1/1 DSP 1 Capabilities:
DSP Type: SP2600 - 43
    Credits   645 ,  G711Credits 15,  HC Credits  37,  MC Credits  23,
    FC Channel  43,  HC Channel  17,  MC Channel  28,
    Conference 8-party credits:
     G711  58 ,  G729  107,  G722  129,  ILBC  215
  Secure Credits:
    Sec LC Xcode  24,      Sec HC Xcode  64,
    Sec MC Xcode  35,      Sec G729 conf 161,
    Sec G722 conf 215,     Sec ILBC conf 322,
    Sec G711 conf 92 ,
  Max Conference Parties per DSP:
    G711 88,  G729 48,  G722 40,  ILBC 24,
    Sec G711 56,  Sec G729 32,
    Sec G722 24  Sec ILBC 16,
  Voice Channels:
    g711perdsp = 43,  g726perdsp = 28, g729perdsp = 17, g729aperdsp = 28,
    g723perdsp = 17,  g728perdsp = 17, g723perdsp = 17, gsmperdsp   = 28,
    gsmefrperdsp = 17, gsmamrnbperdsp = 17,
    ilbcperdsp = 17, isacperdsp = 8  modemrelayperdsp = 17,
    g72264Perdsp = 28, h324perdsp = 17,
    m_f_thruperdsp = 43, faxrelayperdsp = 28,
    maxchperdsp = 43, minchperdsp = 17,
    srtp_maxchperdsp = 27, srtp_minchperdsp = 14, faxrelay_srtp_perdsp = 
4,
    g711_srtp_perdsp = 27, g729_srtp_perdsp = 14, g729a_srtp_perdsp = 24,----------
```

## Examples

The following example shows the details of the DSP errors on the Cisco ASR 1000 Series Router.

The crash dump details must be enabled to display the crash dump for a SPA-DSP. To enable a crash dump, set the destination
                                          of the crash dump file to a valid file name, and set the file limit to a non-zero number.

```
Router# show voice dsp crash-dump Voice DSP Crash-dump status:
    Destination file url is <none>
    File limit is 0
DSP crash dump is currently disabled
To enable DSP crash dump, set file-limit to a non-zero number and set
destination to a valid file name
```

### Related Commands

Command

Description

dsp services dspfarm

Enables the DSP farm services.

dspfarm profile

Enters the DSP farm profile configuration mode and defines a profile for DSP farm services.

show dspfarm

Displays DSP farm service information, such as operational status, and DSP resource allocation for transcoding.

## show voice dsp channel

To display the voice digital signal processor (DSP) channels, use the show voice dsp channel command in user EXEC or privileged EXEC mode.

show voice dsp channel { operational-status { slot | / dsp | / channel } [ slot | / dsp | / channel ] | statistics slot-number [slot-number] | traffic slot-number [slot-number] }

### Syntax Description

operational-status

Displays the operational state for active sessions on a specific channel or range of channels.

slot

A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command.

/ dsp

A single DSP on the slot or the first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected by the command. The slash mark is required.

/ channel

A single DSP channel or the first DSP channel in a range. The second occurrence of this argument specifies either a single DSP channel or the last DSP channel in a range. The slash mark is required.

statistics

Displays DSP statistics for a specific channel or range of channels.

slot-number

A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command.

traffic

Displays traffic on a specific channel or range of channels.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(4)XC

The command was introduced on the Cisco AS5350XM and Cisco AS5400XM platforms.

12.4(11)T

The command was modified. Command output was enhanced to display information about DSP H.320 channels.

### Usage Guidelines

Use this command when abnormal behavior occurs in the DSP voice channels. The channel or channels should have an active voice
                              call at the time the command is executed.

## Examples

The following is sample output from the show voice dsp channel operational-status command on slot 3/13/1:

```
Router# show voice dsp channel operational-status 3/13/1 Operational status of Slot/DSP/Channel : 3/13/1
 Servicetype  : VOICE
 Codec Type  : gsmamr-nb
 Encapsulation : RTP            
 Transmitted Packets : 346
 Transmitted Bytes : 11740
 Received Packets : 411
 Received Bytes : 11142
 Playout de-jitter mode :  None
 Playout de-jitter buffer minimum delay : 0 msec
 Playout de-jitter buffer initial delay : 0 msec
 Playout de-jitter buffer maximum delay : 0 msec
 Noise level : -5.0 
 ERLLevel : 6 
 ACOMLevel : 6 
CodecPktPeriod=20 Milliseconds
CodecFrameFormat=bandwidth-efficient
CodecCrc=Disabled
CodecModes=3,6
CodecEncodeRate=6
CodecDecodeRate=6
CodecEncodeChanges=1
CodecDecodeChanges=0
CodecCrcFails=0
CodecBadFrameQuality=0
CodecInvalidCMRs=0
CodecInvalidFrameType=0
 Voice activity detection : Enabled    
 Dtmf Relay : inband-voice
 ComfortNoisePak : 52 
 TxVoiceDuration : 11560 
 VoiceRxDuration : 3380 
 Rx OutOfSeq Paks : 0 
 Rx Late Paks : 0 
 Rx Early Paks : 0 
 Lost Packets : 0
 Playout Delay Current : 50 
 Playout Delay Min : 50 
 Playout Delay Max : 50 
 Playout Delay ClockOffset : 80 
 Playout Delay Jitter : 0 
 Error Rx Drop : 0 
 Error Tx Drop : 0 
 Error Tx Control : 0 
 Error Rx Control : 0 
 Playout Error Predictive : 0 
 Playout Error Interpolative : 0 
 Playout Error Silence : 0 
 Playout Error BufferOverFlow : 0 
 Playout Error Retroactive : 0 
 Playout Error Talkspurt : 0
```

The table below describes the significant fields shown in the display.

Field

Description

DSP

Number of the DSP.

Channel

Number of the channel and its status.

Codec Type

Complexity setting.

TxVoiceDuration

Transmitted voice duration.

### Related Commands

Command

Description

show voice dsp

Displays the current status or selective statistics of DSP voice channels,.

## show voice dsp crash-dump

To display voice digital signal processor (DSP) crash dump information, use the show voice dsp crash-dump command in privileged EXEC configuration mode.

show voice dsp crash-dump

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example checks your configuration:

```
Router# show voice dsp crash-dump Voice DSP Crash-dump status:
    Destination file url is slot0:banjo-152-s 
    File limit is 20 
    Last DSP dump file written was 
          tftp://112.29.248.12/tester/26-152-t2 
    Next DSP dump file written will be slot0:banjo-152-s1
```

The following example shows that the crash dump feature is enabled:

```
Router# show voice dsp crash-dump Voice DSP Crash-dump status:
    Destination file url is
          tftp://172.29.248.12/xxtir/dspdump6.bin
    File limit is 10
    Last DSP dump file written was
          tftp://172.29.248.12/xxtir/dspdump6.bin1
    Next DSP dump file written will be
          tftp://172.29.248.12/xxtir/dspdump6.bin2
```

The following example shows that the crash dump feature is disabled:

```
Router# show voice dsp crash-dump Voice DSP Crash-dump status:
    Destination file url is
          tftp://172.29.248.12/xxtir/dspdump6.bin
    File limit is 0
    Last DSP dump file written was
          tftp://172.29.248.12/xxtir/dspdump6.bin1
DSP crash dump is currently disabled
To enable DSP crash dump, set file-limit to a non-zero number
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

debug voice dsp crash-dump

Displays crash dump debug information.

voice dsp crash-dump

Enables the crash dump feature and specifies the destination file and the file limit.

## show voice dsp summary

To display the digital signal processor (DSP) summary, use the show voice dsp summary command in user EXEC or privileged EXEC mode.

show voice dsp summary [ slot | slot / dsp ] [ slot | slot / dsp ]

### Syntax Description

slot

(Optional) A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command.

/ dsp

(Optional) A single DSP on the slot or the first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected by the command. The slash mark is required.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(4)XC

This command was introduced. The command was implemented on the Cisco AS5350XM and Cisco AS5400XM platforms.

12.4(11)T

The command was modified. Command output was enhanced to display information about DSP H.320 channels.

12.4(19)

The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls.

12.4(18a)

The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls.

12.4(13f)

The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls.

12.4(15)T5

The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls.

## Examples

The following sample output from the show voice dsp summary command shows summary information about DSPs:

```
Router# show voice dsp summary Total number of DSPs = 48
 
Codectype       Calls    Codectype       Calls    Codectype       Calls
g729r8 pre-ietf     0    g729ar8             0    g726r16             0
g726r24             0    g726r32             0    g711ulaw            0
g711alaw            1    g728                0    g723r63             0
g723r53             0    gsmfr               0    gsmefr              0
g729br8             0    g729abr8            0    g723ar63            0
g723ar53            0    g729r8              0    t38                 0
clear-channel       0    vofr cisco          0    llcc                0
g726r40             0    transparent         0    modem-relay         0
cisco               0                        0                        0
pass-through        0    gsmamr-nb           0    
 
Legend       :
======
Channel state: (s)shutdown   (a)active call (d)download pending
               (b)busiedout  (B)bad         (p)busyout pending
Call type    : (v)voice      (f)fax-relay   (_)not in use
 
Summary      :
=======
Channels     :  Total 768  In-Use    001  
Calls        :  Total 001  Voice     001  Fax  000
             :  Free  713  Disabled  000 
 
      DSP      DSP        DSP    Channel            Call            
DSP#  State    Complexity Resets State              Type
2/1   ACTIVE   FLEXI      0      ________ ________  ________ ________
2/2   ACTIVE   FLEXI      0      ________ ________  ________ ________
2/3   ACTIVE   FLEXI      0      ________ ________  ________ ________
2/4   ACTIVE   FLEXI      0      ________ ________  ________ ________
2/5   ACTIVE   FLEXI      0      ________ ________  ________ ________
2/6   ACTIVE   FLEXI      0      ________ ________  ________ _________
```

The table below describes the significant fields shown in the display.

Field

Description

DSP

Number of the DSP.

Codectype

Complexity setting.

Channels

Number of the channel and its status.

State

Status of the calls.

### Related Commands

Command

Description

show voice dsp

Displays the current status or selective statistics of DSP voice channels,.

## show voice eddri prefix

To show applicable prefixes for the event dispatcher and data repository interface (EDDRI), use the show voice eddri prefix
                              command in privileged EXEC mode.

show voice eddri prefix [ prefix_number ]

### Syntax Description

all

All neighbors

prefix_number

(Optional) Specified EDDRI prefix.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

If no prefix is specified, all configured prefixes appear.

The EDDRI notifies threaded grep (TGREP) when an attribute changes on some subsystems. EDDRI interacts with the dial-peer
                              subsystem, trunk-group subsystems, call-control API (CCAPI) subsystem, and customer-relationship-management (CRM) subsystem
                              to notify changes in particular attributes. EDDRI is responsible for creating the prefix database.

## Examples

The following example shows output for the show voice eddri prefix command:

```
prefix 4 address family decimal
advertise flag 0x27 ac 24 tc 24 capacity timer 25 sec
AC_avg 24, FD_avg 0, SD_avg 0
succ_curr 0 tot_curr 0
succ_report 0 tot_report 0
changed 0 replacement position 0
trunk group castg2 
dial peer tag 1001
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

debug voip eddri

Turns on debugging for the EDDRI.

## show voice emergency locations

To display the emergency response locations (ERL) for E911 services, use show voice emergency locations command in privileged EXEC mode.

show voice emergency locations

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

Use this command to display an ERL that identifies an area where emergency teams can quickly locate a 911 caller. This command
                              displays ERL assignment by zone, device, and interfaces.

## Examples

The following example displays ERL assignment by zone, device, and interfaces.

```
Router# show voice emergency locations ERL ASSIGNMENT BY ZONE
DIAL-PEER   ZONE
=================
911         10

ERL ASSIGNMENT BY DEVICE AND INTERFACES
ERL         DEVICE
======================
12          dial-peer 100
```

### Related Commands

voice emergency response

Configures emergency response location, zone, and settings for E911 services.

## show voice enum-match-table

To display the rules of an ENUM match table, use the show voice enum - match - table command in privileged EXEC mode.

show voice enum-match-table [ table-number [ sort ]]

### Syntax Description

table - number

(Optional) ENUM match table to display, by number. Range is from 1 to 15.

sort

(Optional) Sorts the output by ascending table number.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

This command displays the ENUM match table rules in the order in which they were defined. The sort keyword changes the display
                              to list the rules from lowest to highest preference.

## Examples

The following sample output displays the rules of ENUM match table number 3:

```
Router# show voice enum-match-table 3 voice enum_match_table 3
rule 1 5 /^9\(1.*\)/ /+\1/ cisco
rule 2 4 /^9011\(.*\)/ /+1408\1/ arpa
rule 10 1 /^(.*)/ /\1/ e164.cisco.com
```

The following sample output displays the ENUM match tables in ascending order by table number:

```
Router# show voice enum-match-table voice enum-match-table 3
rule 1 5 /^9\(1.*\)/ /+\1/ cisco
rule 2 4 /^9011\(.*\)/ /+1408\1/ arpa
rule 10 1 /^(.*)/ /\1/ e164.cisco.com
voice enum-match-table 5
rule 2 4 /^9011\(.*\)/ /+1408\1/ arpa
rule 10 1 /^(.*)/ /\1/ e164.cisco.com
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

rule (ENUM configuration)

Defines the ENUM rule.

test enum

Tests the ENUM rule.

voice enum-match-table

Initiates the voice ENUM match table definition.

## show voice hpi capture

To display capture status and statistics, use the show voice hpi capture command in privileged EXEC mode.

show voice hpi capture

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(10)

This command was introduced.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

This command displays the capture status and statistics. Use this command to confirm logger status and to examine the logger
                              status output when the logger is running.

Caution

Using the message logger feature in a production network environment increases CPU and memory usage on the gateway.

If you are experiencing problems with certain voice calls, the engineering team at Cisco might ask you to capture the control
                                          messages using the voice DSP logger. You can capture these messages by turning on the logger, repeating the problematic calls,
                                          and capturing the logs. Only Cisco engineers can determine if you should send the logs in for further review.

## Examples

The following sample output shows capture statistics (HPI capture and logging) and status:

```
Router# show voice hpi capture HPI Capture is on and is logging to URL ftp://172.23.184.216/d:\test_data.dat1 messages sent to URL, 0 messages droppedMessage Buffer (total:inuse:free)  2134:0000:2134Buffer Memory:699952 bytes, Message size:328 bytes
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

debug hpi

Enables debugging for HPI message events.

voice hpi capture

Allocates the Host Port Interface (HPI) capture buffer (size in bytes) and sets up or changes the destination URL for captured
                                          data.

## show voice iec description

To display Internal Error Code (IEC) descriptions, use the show voice iec description command in user EXEC mode.

show voice iec description string

### Syntax Description

string

Six-part dotted decimal string that displays the definition of an internal error code.

### Command Default

No default behavior or values.

### Command Modes

User EXEC

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example displays IEC descriptions:

```
Router# show voice iec description 1.1.180.2.21.4 IEC Version: 1
Entity: 1 (Gateway)
Category: 180 (Software error)
Subsystem: 2 (TCL IVR)
Error: 21 (Script syntax)
Diagnostic Code: 4
```

The table below describes significant fields shown in the display.

Field

Description

IEC version

IEC version. A value of 1 indicates the Cisco IOS Release 12.3(4)T version.

Entity

Network physical entity (hardware system) that generated the IEC. The value 1 is assigned to the gateway.

Category

Error category, defined in terms of ITU-based Q.850 cause codes and VoIP network errors.

Subsystem

Specific subsystem within the physical entity where the IEC was generated.

Error Code

Error code within the subsystem.

Diagnostic Code

Cisco internal diagnostic value. Report this value to Cisco Technical Support.

### Related Commands

Command

Description

show voice statistics iec

Displays IEC statistics.

## show voice lmr

To display the Land Mobile Radio (LMR) related dynamic information and static information for LMR ports or a DS0 group, use
                              the show voice lmr command in privileged EXEC mode.

show voice lmr [ slot / subunit / port | slot / port : ds0-group ] [ details | timing [ warnings ]]

### Syntax Description

slot/subunit/port

(Optional) Voice port that you specify with the slot / subunit / port designation.

slot specifies a router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform.

subunit specifies a voice interface card (VIC) in which the voice port is located. Valid entries are 0 and 1.

port specifies an analog voice port number. Valid entries are 0 and 1.

The slash marks are required.

slot/port : ds0 - group

(Optional) Voice port that you specify with the slot / port : ds0 - group designation.

slot specifies a router slot in which the packet voice NM is installed. Valid entries are router slot numbers for the particular
                                                platform.

port specifies a T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1.

ds0 - group specifies a T1 or E1 logical port number. T1 range is from 0 to 23. E1 range is from 0 to 30.

The colon is required.

details

(Optional) Displays more information. If this keyword is omitted, less information is displayed.

timing

(Optional) Displays the timing configuration for all LMR ports.

warnings

(Optional) Displays all LMR ports that are having suspicious timing configuration.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.4(24)T

This command was modified in a release earlier than Cisco IOS Release 12.4(24)T. The timing and warnings keywords were added.

### Usage Guidelines

This command displays information for LMR voice ports only. If no voice port is specified, the command displays information
                              for all ear and mouth (E&M) LMR voice ports.

When the details keyword is used, this command displays information about timeouts, timers, and injected tones and pauses, in addition to detailed voice port and
                              active call information found in the show voice port and show call active voice commands.

## Examples

The following is sample output from the show voice lmr command for an E&M LMR analog voice port on a Cisco 3745 router:

```
Router# show voice lmr 2/0/0 2/0/0
=========
 Connection type: n/a
 Out Attenuation = 0 db, In Gain = 0 dB
 E-lead capability is inactive, polarity = normal
 M-lead capability is inactive, polarity = normal
 voice-class tone-signal test
 state = LMR_CONNECT, e-lead = off, m-lead = off
 full duplex, voice path = rx
 Terminating side of the connection
 TransmitPackets=113, TransmitBytes=2241
 ReceivePackets=113, ReceiveBytes=2241
 CoderTypeRate=g729r8
 NoiseLevel=-65, ACOMLevel=22
 OutSignalLevel=-68, InSignalLevel=-79
 RemoteIPAddress=10.5.25.40, RemoteUDPPort=17272
 Remote SignallingIPAddress=10.5.25.40, Port=15418
 Remote MediaIPAddress=10.5.25.40, Port=17272
 RoundTripDelay=2 ms
 SessionProtocol=cisco
 VAD =enabled
```

The following is sample output from the show voice lmr details command for an E&M LMR analog voice port on a Cisco 3745 router:

```
Router# show voice lmr 2/0/0 details 2/0/0
=========
 Description:
 Connection type: n/a
 Out Attenuation = 0 db, In Gain = 0 dB
 Timing hangover: 500 ms
 E-lead capability is inactive, polarity = normal
 M-lead capability is inactive, polarity = normal
 Timing hookflash-in: 480
 Timing delay-voice: 470 ms
 Music On Hold Threshold: -38 dB, Noise Threshold: -62 dB
 E&M type: 1, Operation:  2-wire
 Impedance is set to 600r Ohm
 lmr tear down timeout is set to 1800 second
 lmr PTT transmit timeout is not set
 lmr PTT receive timeout is not set
 voice-class tone-signal test
         inject tone 1 1950 3 150
         inject tone 2 2000 0 60
         inject pause 3 60
         inject tone 4 2175 3 150
         inject tone 5 1000 0 50
         inject guard-tone 6 1950 -10 
 state = LMR_CONNECT, e-lead = off, m-lead = off
 full duplex, voice path = rx
 Terminating side of the connection
 TransmitPackets=113, TransmitBytes=2241
 ReceivePackets=113, ReceiveBytes=2241
 CoderTypeRate=g729r8
 NoiseLevel=-66, ACOMLevel=22
 OutSignalLevel=-68, InSignalLevel=-79
 PeerAddress=37200
 PeerSubAddress=
 PeerId=200
 SessionTarget=
 RemoteIPAddress=10.5.25.40, RemoteUDPPort=17272
 Remote SignallingIPAddress=10.5.25.40, Port=15418
 Remote MediaIPAddress=10.5.25.40, Port=17272
 RoundTripDelay=0 ms
 SessionProtocol=cisco
 VAD =enabled
 SelectedQoS=best-effort
 ProtocolCallId=
 SessionTarget=
```

The table below describes the significant fields shown in the output, in the order in which they appear.

Field

Description

Connection type

Type of connection between LMR routers: private line, automatic ringdown (PLAR), trunk, or n/a

Out Attenuation

Output attenuation.

In Gain

Input gain.

E-lead capability

Active or inactive.

polarity

Polarity of the E&M voice port: normal or reverse.

M-lead capability

Active or inactive.

voice class tone-signal

Name of the tone-signal voice class.

state=

Signaling state.

e-lead =

On or off.

m-lead =

On or off.

full duplex

Voice path for the voice port is operating in full duplex mode.

half duplex

Voice path for the voice port is operating in half duplex mode.

voice path

Transmit or receive.

TransmitPackets

Number of packets sent by this peer during this call.

TransmitBytes

Number of bytes sent by this peer during this call.

ReceivePackets

Number of packets received by this peer during this call.

ReceiveBytes

Number of bytes received by the peer during this call.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

NoiseLevel

Active noise level for this call.

ACOMLevel

Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceller, which is the sum of the Echo
                                          Return Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call.

OutSignalLevel

Active output signal level to the telephony interface used by this call.

InSignalLevel

Active input signal level from the telephony interface used by this call.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

Remote SignallingIPAddress, Port

Call control server IP address and signaling port number.

Remote MediaIPAddress, Port

Remote side media server IP address and RTP port number.

RoundTripDelay

Voice packet round trip delay between the local and remote systems on the IP backbone for this call.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

VAD

Whether voice activation detection (VAD) is enabled.

Description

Description of what the port is connected to.

Timing hangover

Number of milliseconds of delay before the digital signal processor (DSP) tells Cisco IOS software to turn off the E-lead
                                          after the DSP detects that the voice stream has stopped.

Timing hookflash-in

Maximum duration of a hookflash for a Foreign Exchange Station (FXS) interface.

Timing delay-voice

Delay before a voice packet is played out.

Music On Hold Threshold

Decibel level of music played when calls are put on hold.

Noise Threshold

Noise threshold for incoming calls.

E&M type

E&M signaling type.

Operation

2-wire or 4-wire operation.

Impedance

Terminating impedance of the interface.

lmr tear down timeout

Time for which the voice port waits before tearing down an LMR connection after detecting no voice activity.

lmr PTT transmit timeout

Maximum time for transmitting a voice packet.

lmr PTT receive timeout

Maximum time for receiving a voice packet.

inject pause

Pause injected before the voice packet is played out.

inject tone

Tone injected before the voice packet is played out.

inject guard-tone

Guard tone played out with the voice packet.

PeerAddress

Destination pattern or number associated with this peer.

PeerSubAddress

Subaddress when this call is connected.

PeerId

ID value of the peer table entry to which this call was made.

SessionTarget

Network-specific address to receive calls from the dial peer.

SelectedQoS

Selected RSVP quality of service (QoS) for this call.

ProtocolCallId

Voice signaling specific call ID.

### Related Commands

Command

Description

show call active voice

Displays call information for voice calls in progress.

show voice port

Displays configuration information about a specific voice port.

## show voice pcm capture

To display PCM capture status and statistics, use the show voice pcm capture command in privileged EXEC mode.

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

This command displays the PCM capture status and statistics. Use this command to confirm logger status and to examine the
                              logger status output when the logger is running.

## Examples

The following is sample output from the show voice pcm capture command :

```
Router# show voice pcm capture PCM Capture is on and is logging to URL tftp://10.10.1.2/acphan/
50198 messages sent to URL, 0 messages dropped
Message Buffer (total:inuse:free) 200000:0:200000
Buffer Memory: 68000000 bytes, Message size: 340 bytes
```

### Related Commands

Command

Description

voice pcm capture

Allocates the number of Pulse Code Modulation (PCM) capture buffers, sets up or changes the destination URL for captured
                                          data, enables PCM capture on-demand, and changes the PCM capture trigger string by the user.

## show voice port

To display configuration information about a specific voice port, use the show voice port command in privileged EXEC mode.

### Cisco 1750 Router

show voice port slot / port

### Cisco 2600 and Cisco 3600 Series Router with Analog Voice Ports

show voice port [ slot / subunit / port | summary ]

### Cisco 2600 and Cisco 3600 Series Router with Digital Voice Ports (with T1 Packet Voice Trunk Network Modules)

show voice port [ slot / port : ds0-group | summary ]

### Cisco AS5300 Universal Access Server

show voice port controller-number :D

### Cisco 7200 Series Router

show voice port { slot / port : ds0-group-number | slot / subunit / port }

### Syntax Description

Cisco 1750 Router

slot

Slot number in the router in which the VIC is installed. Valid entries are 0, 1, and 2, depending on the slot in which it
                                          is installed.

/ port

Voice port. Valid entries are 0 and 1. The slash mark is required.

Cisco 2600 and Cisco 3600 Series Router with Analog Voice Ports

slot / subunit / port

(Optional) The analog voice port designation:

slot -- Router slot in which a voice network module (VNM) is installed. Valid entries are router slot numbers for the particular platform.

subunit --Voice Interface Card (VIC) in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network
                                                module.) The slash mark is required.

port-- Analog voice port number. Valid entries are 0 and 1. The slash mark is required.

summary

(Optional) Displays a summary of all voice ports.

Cisco 2600 and Cisco 3600 Series Router with Digital Voice Ports

slot / port : ds0 - group

(Optional) Specifies the digital voice port designation:

slot-- Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for the
                                                particular platform.

/ port-- T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1. (One VWIC fits in an NM.) The slash
                                                mark is required.

: ds0 - group-- T1 or E1 logical port number. T1 range is 0 to 23. E1 range is 0 to 30. The colon is required.

summary

(Optional) Displays a summary of all voice ports.

Cisco AS5300 Universal Access Server

controller - number

T1 or E1 controller.

:D

D channel that is associated with the ISDN PRI. The colon is required.

Cisco 7200 Series Router

slot

Router location where the voice port adapter is installed. Range is 0 to 3.

/ port

Voice interface card location. Valid entries are 0 and 1. The slash mark is required.

: ds0-group-number

Defined DS0 group number. Because each defined DS0 group number is represented on a separate voice port, you can define individual
                                          DS0s on the digital T1/E1 card. The colon is required.

slot

Slot number in the Cisco router where the VIC is installed. Range is 0 to 3, depending on the slot where it is installed.

/ subunit

Subunit on the VIC where the voice port is located. Valid entries are 0 and 1. The slash mark is required.

/ port

Voice port number. Valid entries are 0 and 1. The slash mark is required.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA

This command was modified. Port-specific values for the Cisco MC3810 were added.

12.0(3)T

This command was modified. Port-specific values for the Cisco MC3810 were added.

12.0(5)XK

This command was modified. The ds0-group argument was added for the Cisco 2600 series and Cisco 3600 series.

12.0(5)XE

This command was modified. Additional syntax was created for digital voice to allow specification of the DS0 group. This
                                          command applies to VoIP on the Cisco 7200 series.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

12.0(7)XK

This command was modified. The summary keyword was added for the Cisco 2600 series and Cisco 3600 series. The ds0-group argument was added for the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(8)T

This command was modified. This command was implemented for direct inward dial (DID) on the Cisco IAD2420 series.

12.2(2)XN

This command was modified. Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was
                                          added to Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco Gateway 200 (Cisco VG200).

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. It was implemented on the
                                          Cisco IAD2420 series.

12.4(11)T

This command was modified. This command was enhanced to display voice class called-number-pool configuration information
                                          for the voice port.

12.4(12)

This command was modified. This command was integrated into Cisco IOS Release 12.4(12) and output was modified to display
                                          the parameter set by the timing sup-disconnect command.

15.0(1)XA

This command was modified. The output was enhanced to display the logical partitioning class of restriction (LPCOR) policy
                                          for incoming and outgoing calls.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

15.1(3)T

This command was modified. The output of this command was enhanced to display the connection status of foreign exchange office
                                          (FXO) ports.

### Usage Guidelines

Use this command to display configuration and VIC-specific information about a specific port.

This command works on Voice over IP, Voice over Frame Relay, and Voice over ATM.

The ds0-group command automatically creates a logical voice port that is numbered as follows on Cisco 2600, Cisco 3600 series, and Cisco
                              7200 series routers: slot / port : ds0-group - number . Although only one voice port is created for each group, applicable calls are routed to any channel in the group.

This command is not supported on Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 platforms for Non-Facility Associated
                                          Signaling (NFAS) configuration.

## Examples

The following is sample output from the show voice port command for an E&M analog voice port:

```
Router# show voice port 1/0/0 E&M Slot is 1, Sub-unit is 0, Port is 0
 Type of VoicePort is E&M
 Operation State is unknown
 Administrative State is unknown
 The Interface Down Failure Cause is 0
 Alias is NULL
 Noise Regeneration is disabled
 Non Linear Processing is disabled
 Music On Hold Threshold is Set to 0 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is disabled
 Echo Cancel Coverage is set to 16ms
 Connection Mode is Normal
 Connection Number is not set
 Initial Time Out is set to 0 s
 Interdigit Time Out is set to 0 s
 Analog Info Follows:
 Region Tone is set for northamerica
 Currently processing none
 Maintenance Mode Set to None (not in mtc mode)
 Number of signaling protocol errors are 0
 Voice card specific Info Follows:
 Signal Type is wink-start
 Operation Type is 2-wire
 Impedance is set to 600r Ohm
 E&M Type is unknown
 Dial Type is dtmf
 In Seizure is inactive
 Out Seizure is inactive
 Digit Duration Timing is set to 0 ms
 InterDigit Duration Timing is set to 0 ms
 Pulse Rate Timing is set to 0 pulses/second
 InterDigit Pulse Duration Timing is set to 0 ms
 Clear Wait Duration Timing is set to 0 ms
 Wink Wait Duration Timing is set to 0 ms
 Wink Duration Timing is set to 0 ms
 Delay Start Timing is set to 0 ms
 Delay Duration Timing is set to 0 ms
```

The following is sample output from the show voice port command for an E&M digital voice port:

```
Router# show voice port 1/0/1 receEive and transMit Slot is 1, Sub-unit is 0, Port is 1
 Type of VoicePort is E&M
 Operation State is DORMANT
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancel Coverage is set to 8 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Region Tone is set for US
```

The following is sample output from the show voice port command for a foreign exchange station (FXS) analog voice port:

```
Router# show voice port 1/1/1 Foreign Exchange Station 1/1/1 Slot is 1, Sub-unit is 1, Port is 1
 Type of VoicePort is FXS  VIC2-2FXS
 Operation State is DORMANT
 Administrative State is UP
 The Last Interface Down Failure Cause is Administrative Shutdown
 Description is I am a FXS LoopStart port
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 3 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 64 ms
 Echo Cancel worst case ERL is set to 6 dB
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 250 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Supervisory Disconnect Time Out is set to 750 ms
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Analog Info Follows:
 Currently processing none
 Maintenance Mode Set to None (not in mtc mode)
 Number of signaling protocol errors are 0
 Impedance is set to 600r Ohm
 Station name None, Station number None
 Translation profile (Incoming): 
 Translation profile (Outgoing):
 lpcor (Incoming): local_group
 lpcor (Outgoing): local_group
 Voice card specific Info Follows:
 Signal Type is loopStart
 Ring Frequency is 25 Hz
 Hook Status is On Hook
 Ring Active Status is inactive
 Ring Ground Status is inactive
 Tip Ground Status is active
 Digit Duration Timing is set to 100 ms
 InterDigit Duration Timing is set to 100 ms
 Hookflash-in Timing is set to max=1000 ms, min=150 ms
 Hookflash-out Timing is set to 400 ms
 No disconnect acknowledge
 Ring Cadence is defined by CPTone Selection
 Ring Cadence are [20 40] * 100 msec
 Ringer Equivalence Number is set to 1
```

The following is sample output from the show voice port command for an FXO analog voice port:

```
Router# show voice port 1/0/1 Foreign Exchange Office 1/0/1 Slot is 1, Sub-unit is 0, Port is 1
 Type of VoicePort is FXO
 Operation State is DORMANT
 Administrative State is UP
 The Last Interface Down Failure Cause is Administrative Shutdown
 Description is I am an FXO LoopStart port
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 3 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 64 ms
 Echo Cancel worst case ERL is set to 6 dB
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 250 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Analog Info Follows:
 Currently processing none
 Maintenance Mode Set to None (not in mtc mode)
 Number of signaling protocol errors are 0
 Impedance is set to 600r Ohm
 Station name None, Station number None
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Voice card specific Info Follows:
 Signal Type is loopStart 
 Battery-Reversal is enabled
 Number Of Rings is set to 1
 Supervisory Disconnect is signal
 Answer Supervision is inactive
 Hook Status is On Hook
 Ring Detect Status is inactive
 Ring Ground Status is inactive
 Tip Ground Status is inactive
 Dial Out Type is dtmf
 Digit Duration Timing is set to 100 ms
 InterDigit Duration Timing is set to 100 ms
 Pulse Rate Timing is set to 10 pulses/second
 InterDigit Pulse Duration Timing is set to 750 ms
 Percent Break of Pulse is 60 percent
 GuardOut timer is 2000 ms
 Minimum ring duration timer is 125 ms
 Hookflash-in Timing is set to 600 ms
 Hookflash-out Timing is set to 400 ms
 Supervisory Disconnect Timing (loopStart only) is set to 750 ms
 OPX Ring Wait Timing is set to 6000 ms
```

The following is sample output from the show voice port summary command. Note that for the connected FXO analog voice port 0/2/0, which has the ADMIN state of "up" and the OPER state of
                              "dorm," this output shows that the IN STATUS is "idle" and the OUT STATUS is "on-hook":

```
Router# show voice port summary IN       OUT
PORT            CH   SIG-TYPE   ADMIN OPER STATUS   STATUS   EC
=============== == ============ ===== ==== ======== ======== ==
0/0/0           --  fxs-ls      up    dorm on-hook  idle     y 
0/0/1           --  fxs-ls      up    dorm on-hook  idle     y 
0/3/0:23        01  isdn-voice  up    dorm none     none     y 
0/3/0:23        02  isdn-voice  up    dorm none     none     y 
.
.
.
0/1/0           --  did-in-wnk  up    dorm idle     idle     y 
0/1/1           --  did-in-wnk  up    dorm idle     idle     y 
0/2/0           --  fxo-ls      up    dorm idle     on-hook  y 
0/2/1           --  fxo-ls      up    down idle     off-hook y 
2/0/0           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/1           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/2           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/3           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/4           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/5           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/6           --  fxs-ls      up    dorm on-hook  idle     y 
2/0/7           --  fxs-ls      up    dorm on-hook  idle     y
```

If the FXO port 0/2/0 is disconnected, the output of the show voice port summary command changes so that the OUT STATUS is reported as "off-hook," and the OPER state changes to "down."

The following is sample output from the show voice port command for an ISDN voice port:

```
Router# show voice port ISDN 2/0:23 Slot is 2, Sub-unit is 0, Port is 23
 Type of VoicePort is ISDN-VOICE
 Operation State is DORMANT
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 64 ms
 Echo Cancel worst case ERL is set to 6 dB
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 250 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Station name None, Station number None
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Voice class called number pool: 
DS0 channel specific status info:
                                      IN      OUT
    PORT       CH  SIG-TYPE    OPER STATUS   STATUS    TIP     RING
    2/0:23     01  isdn-voice  up   none     none                       
    2/0:23     02  isdn-voice  up   none     none                       
    2/0:23     03  isdn-voice  up   none     none                       
    2/0:23     04  isdn-voice  up   none     none                       
    2/0:23     05  isdn-voice  up   none     none                       
    2/0:23     06  isdn-voice  up   none     none                       
    2/0:23     07  isdn-voice  dorm none     none                       
    2/0:23     08  isdn-voice  dorm none     none                       
    2/0:23     09  isdn-voice  dorm none     none                       
    2/0:23     10  isdn-voice  dorm none     none                       
    2/0:23     11  isdn-voice  dorm none     none                       
    2/0:23     12  isdn-voice  dorm none     none                       
    2/0:23     13  isdn-voice  dorm none     none                       
    2/0:23     14  isdn-voice  dorm none     none                       
    2/0:23     15  isdn-voice  dorm none     none                       
    2/0:23     16  isdn-voice  dorm none     none                       
    2/0:23     17  isdn-voice  dorm none     none                       
    2/0:23     18  isdn-voice  dorm none     none                       
    2/0:23     19  isdn-voice  dorm none     none                       
    2/0:23     20  isdn-voice  dorm none     none                       
    2/0:23     21  isdn-voice  dorm none     none                       
    2/0:23     22  isdn-voice  dorm none     none                       
    2/0:23     23  isdn-voice  dorm none     none
```

The following is sample output from the show voice port command for the connected FXO analog voice port 0/2/0, which has the Administrative State of "UP" and the Operation State
                              of "DORMANT":

```
Router# show voice port 0/2/0 Foreign Exchange Office 0/2/0 Slot is 0, Sub-unit is 2, Port is 0
 Type of VoicePort is FXO
 Operation State is DORMANT
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 3 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 128 ms
 Echo Cancel worst case ERL is set to 6 dB
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 1000 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 15 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Power Denial Disconnect Time Out is set to 1000 ms
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Analog Info Follows:
 Currently processing none
 Maintenance Mode Set to None (not in mtc mode)
 Number of signaling protocol errors are 0
 Impedance is set to 600r Ohm
 Station name None, Station number None
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 lpcor (Incoming): 
 lpcor (Outgoing): 
 Voice card specific Info Follows:
 Signal Type is loopStart 
 Battery-Reversal is enabled
 Number Of Rings is set to 1
 Supervisory Disconnect is signal
 Answer Supervision is inactive
 Hook Status is On Hook
 Ring Detect Status is inactive
 Ring Ground Status is inactive
 Tip Ground Status is inactive
 Dial Out Type is dtmf
 Digit Duration Timing is set to 100 ms
 InterDigit Duration Timing is set to 100 ms
 Pulse Rate Timing is set to 10 pulses/second
 InterDigit Pulse Duration Timing is set to 750 ms
 Percent Break of Pulse is 60 percent
 GuardOut timer is 2000 ms
 Minimum ring duration timer is 125 ms
 Hookflash-in Timing is set to 600 ms
 Hookflash-out Timing is set to 400 ms
 Supervisory Disconnect Timing (loopStart only) is set to 350 ms
 OPX Ring Wait Timing is set to 6000 ms
 Secondary dialtone is disabled
```

If the FXO port 0/2/0 is disconnected, the output of the show voice port command changes so that the Administrative State remains "UP" but the Operation State is "DOWN." Beginning in Cisco IOS Release
                                          15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected or disconnected, a message is
                                          displayed to indicate the status change. For example, the following message is displayed to report that a cable has been connected,
                                          and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122 EST: %LINK-3-UPDOWN: Interface Foreign Exchange
                                          Office 0/2/0, changed state to operational status up due to cable reconnection

The table below describes significant fields shown in these outputs, in alphabetical order.

Field

Description

Administrative State

Administrative state of the voice port.

Alias

User-supplied alias for the voice port.

Clear Wait Duration Timing

Time (in milliseconds [ms]) of inactive seizure signal to declare call cleared.

Companding Type

Companding standard used to convert between analog and digital signals in pulse code modulation (PCM) systems.

Connection Mode

Connection mode of the interface.

Connection Number

Full E.164 telephone number used to establish a connection with the trunk or private line automatic ringdown (PLAR) mode.

Currently Processing

Type of call currently being processed: none, voice, or fax.

Delay Duration Timing

Maximum delay signal duration (in ms) for delay dial signaling.

Delay Start Timing

Timing (in ms) of generation of delayed start signal from detection of incoming seizure.

Dial Type

Out-dialing type of the voice port.

Digit Duration Timing

Dual-tone multifrequency (DTMF) digit duration (in ms).

E&M Type

Type of E&M interface.

Echo Cancel Coverage

Echo cancel coverage for this port.

Echo Cancellation

Whether echo cancellation is enabled for this port.

Impedance

Configured terminating impedance for the E&M interface.

In Gain

Amount of gain (in decibels [dB]) inserted at the receiver side of the interface.

In Seizure

Incoming seizure state of the E&M interface.

Initial Time Out

Amount of time (in seconds) the system waits for an initial input digit from the caller.

Interdigit Duration Timing

DTMF interdigit duration (in seconds).

InterDigit Pulse Duration Timing

Pulse dialing interdigit timing (in ms).

Interdigit Time Out

Amount of time (in seconds) the system waits for a subsequent input digit from the caller.

Lpcor (Incoming)

Setting of the lpcor incoming command.

Lpcor (Outgoing)

Setting of the lpcor outgoing command.

Maintenance Mode

Maintenance mode of the voice port.

Music On Hold Threshold

Configured music-on-hold threshold value for this interface.

Noise Regeneration

Whether background noise should be played to fill silent gaps if voice activity detection (VAD) is activated.

Non Linear Processing

Whether nonlinear processing is enabled for this port.

Number of signaling protocol errors

Number of signaling protocol errors.

Operation State

Operational state of the voice port.

Operation Type

Operation type of the E&M signal: 2-wire or 4-wire.

Out Attenuation

Amount of attenuation (in dB) inserted at the transmit side of the interface.

Out Seizure

Outgoing seizure state of the E&M interface.

Port

Port number for the interface associated with the voice interface card.

Pulse Rate Timing

Pulse dialing rate, in pulses per second (pps).

Region Tone

Configured regional tone for this interface.

Ring Active Status

Ring active indication.

Ring Cadence

Configured ring cadence for this interface.

Ring Frequency

Configured ring frequency (in hertz) for this interface.

Ring Ground Status

Ring ground indication.

Ringing Time Out

Ringing timeout duration (in seconds).

Signal Type

Type of signaling for a voice port: delay-dial, ground-start, immediate, loop-start, and wink-start.

Slot

Slot used in the voice interface card for this port.

Sub-unit

Subunit used in the voice interface card for this port.

Tip Ground Status

Tip ground indication.

Type of VoicePort

Type of voice port: FXO, FXS, or E&M.

The Interface Down Failure Cause

Text string describing why the interface is down,

Wait Release Time Out

Length of time (in seconds) that a voice port stays in call-failure state while a busy tone, reorder tone, or out-of-service
                                          tone is sent to the port.

Wink Duration Timing

Maximum wink duration (in ms) for wink-start signaling.

Wink Wait Duration Timing

Maximum wink wait duration (in ms) for wink-start signaling.

### Related Commands

Command

Description

ds0 group

Specifies the DS0 time slots that make up a logical voice port on a T1 or E1 controller and specifies the signaling type
                                          by which the router communicates with the PBX or PSTN.

timing sup-disconnect

Defines the minimum time to ensure that an on-hook indication is intentional and not an electrical transient on the line
                                          before a supervisory disconnect occurs (based on power denial signaled by the PSTN or PBX).

## show voice sip license

To display SIP trunk license information, use show voice sip license command in privileged EXEC mode.

show voice sip license [ stats { table } | status ]

### Syntax Description

stats

Displays license usage over time.

table

(Optional) Displays license usage over time in tabular format.

status

Displays license status.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Amsterdam 17.2.1r

This command was introduced.

Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a

This command was modified to support Cisco Smart Licensing Using Policy.

Cisco IOS XE Bengaluru 17.6.1a

This command was modified to display licensing information for WebSockets in CUBE.

### Usage Guidelines

Use show voice sip license stats command to display license usage in graphical format. The output includes eight graphs. Four graphs display "CUBE Standard
                              Trunk License Usage" and four graphs display "TDM-SIP Trunk Sessions" details. The following describes how to interpret the
                              graphical data:

License usage for the last 60 seconds —The graph displays the licenses that are used in the last 60 seconds. X-axis represents the time in seconds and Y-axis represents
                                    the licenses that are used. # represents the licenses that are used.

For example, in the following graph, 15 licenses were used at the second second.

```
1                  
       1122334455667788990998877665544332211                        
       5050505050505061505050505050505050505                       
  100                   ###                                         
   90                 #######                                       
   80               ###########                                     
   70             ###############                                   
   60           ###################                                 
   50         #######################                               
   40       ###########################                             
   30     ###############################                           
   20    ##################################                         
   10  #####################################                       
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
        CUBE Standard Trunk License Usage (last 60 seconds)
```

License usage for the last 60 minutes —The graph displays the licenses that are used in the last 60 minutes. X-axis represents the time in minutes and Y-axis represents
                                    the licenses that are used. The values on the Y-axis vary based on the licenses used. # represents the average licenses used. * represents the maximum licenses used. The maximum licenses that are used over a minute are calculated by taking the average
                                    of top three values of licenses that are used over the 60 seconds in that minute.

For example, in the following graph, on the 48th minute,
                                    a maximum of 383 licenses were used.

```
369863146641 
                                                    8880900440044 
                                                    3330922440011 
  910                                                  **         
  820                                                  #*         
  730                                                  ##         
  640                                                 *##*   **   
  550                                                 ###*   ##   
  460                                                 ####  *##*  
  370                                                *####  *##*  
  280                                                #####* ####  
  190                                                ###### ####  
  100                                               *######*####* 
   10                                               ############# 
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum     # = average
```

License usage for the last 72 hours —The graph displays the licenses that are used in the last 72 hours. X-axis represents the time in hours and Y-axis represents
                                    the licenses that are used. The values on the Y-axis vary based on the licenses used. # represents the average licenses used. * represents the maximum licenses used. The maximum licenses that are used over each hour are the same as the maximum licenses
                                    used over the minutes in that hour. While computing license consumption over a period, the maximum value during that period
                                    is considered.

For example, in the following graph, during the first
                                    hour, a maximum of 900 licenses were used.

```
9                                                                       
      0                                                                       
      0                                                                       
  970                                                                         
  890 *                                                                       
  810 *                                                                       
  730 *                                                                       
  650 *                                                                       
  570 *                                                                       
  490 *                                                                       
  410 *                                                                       
  330 *                                                                       
  250 *                                                                       
  170 #                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum     # = average
```

License usage for the last 72 days —The graph displays the licenses that are used for the last 72 days. X-axis represents the time in hours and Y-axis represents
                                    the licenses that are used. The values on the Y-axis vary based on the licenses used. # represents the average licenses used. * represents the maximum licenses used. The maximum licenses used each day is the same as the maximum licenses used over the
                                    hours in that day. While computing license consumption over a period, the maximum value during that period is considered.

For example, in the following graph, on day 1, a maximum of 950 licenses were used.

```
9 2                                                                     
      5 0                                                                     
      0 0                                                                     
 1000 *                                                                       
  900 *                                                                       
  800 *                                                                       
  700 *                                                                       
  600 *                                                                       
  500 *                                                                       
  400 *                                                                       
  300 *                                                                       
  200 * *                                                                     
  100 * *                                                                     
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum     # = average
```

The following is a sample TDM-SIP Trunk Sessions graph. # represents the average licenses used. * represents the maximum licenses used. In the below graph, a maximum of 1 TDM-SIP trunk session was used during the first
                              hour.

```
11                                                                      
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1 **                                                                      
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 hours)
          * = maximum   # = average
```

Use the table keyword to display the licenses used over time in tabular format. The output includes the following tables for "CUBE Standard
                              Trunk License Usage" and "TDM-SIP Trunk Sessions":

License usage for the last 60 seconds

License usage for the last 60 minutes

License usage for the last 72 hours

License usage for the last 72 days

The license usage for WebSockets in CUBE is displayed in graphical format using show voice sip license stats . For display of the licensing usage information in tabular format, use show voice sip license stats table . License usage is displayed for Enhanced, Standard, and Aggregate call counts for WebSockets. TDM calls are not counted for
                              WebSockets in CUBE.

## Examples

The following are sample outputs for show voice sip license stats command:

```
cube#show voice sip license stats 

          11:01:01 AM Thursday Aug 29 2019 IST

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 seconds)         
          

                                                                  
                                                                  
                                                     369863146641 
                                                    8880900440044 
                                                    3330922440011 
  910                                                  **         
  820                                                  #*         
  730                                                  ##         
  640                                                 *##*   **   
  550                                                 ###*   ##   
  460                                                 ####  *##*  
  370                                                *####  *##*  
  280                                                #####* ####  
  190                                                ###### ####  
  100                                               *######*####* 
   10                                               ############# 
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum     # = average 

                                                                              
                                                                              
      9                                                                       
      0                                                                       
      0                                                                       
  970                                                                         
  890 *                                                                       
  810 *                                                                       
  730 *                                                                       
  650 *                                                                       
  570 *                                                                       
  490 *                                                                       
  410 *                                                                       
  330 *                                                                       
  250 *                                                                       
  170 #                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum     # = average 
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum     # = average 

                                                                    
                                                                  
                                                                  
                                                                  
                11                                                
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1           ##                                                
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 seconds)
                                                                  
                                                                  
                                                                  
                                                                  
                                                    1             
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                               *             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 minutes)
          * = maximum   # = average

                                                                                
                                                                              
                                                                              
                                                                              
      11                                                                      
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1 **                                                                      
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 hours)
          * = maximum   # = average

                                                                             
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 days)
          * = maximum   # = average
```

The following are sample outputs for show voice sip license stats table command:

```
cube#show voice sip license stats table 

        02:50:16 PM Wednesday Nov 13 2019 UTC

CUBE Standard Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Standard Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50        324        900
51-55        343        899
56-60        292        600

          
CUBE Standard Trunk License Usage  (last 72 hours)
Period     Average       Max
----------------------------
 1-5          35        900
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

CUBE Standard Trunk License Usage  (last 72 days)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

TDM-SIP Trunk Sessions (last 60 seconds)
Period        Average        Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

TDM-SIP Trunk Sessions (last 60 minutes)
Period        Average        Max
----------------------------
 1-5           0          2
 6-10          0          1
11-15          0          1
16-20          0          1
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

TDM-SIP Trunk Sessions (last 72 hours)
Period        Average         Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

TDM-SIP Trunk Sessions (last 72 days)
Period        Average         Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

The following example shows output of show voice sip license status command when SIP service is enabled:

```
cube#show voice sip license status

Host Name: cube
Current Time: Nov 25 2019 14:46:41 IST
SIP service: Up
License request interval: 5 Minute(s)
Next request at: Nov 25 2019 14:50:44 IST
Recent request(s) for CUBE Standard Trunk
-----------------------------------------------------------
Timestamp                   Count        Result              
-----------------------------------------------------------
Nov 25 2019 14:45:44 IST    10           Out of compliance   
Nov 25 2019 14:40:44 IST    4            Authorized          
Nov 25 2019 14:35:44 IST    2            Authorized
```

After the entitlement request is sent and before receiving the response, the "Result" column in the output shows the same
                              value as that of the previous and appends it with "(Response Pending)". For example, in the following output, the response
                              is awaited for the entitlement request that is sent at "Dec 5 2019 16:17:46 IST". Hence, the "Result" column shows "Authorized(Response
                              Pending)". If the entitlement request is sent for the first time, then the "Result" is shown as "Unknown(Response Pending)".

```
cube#show voice sip license status

Host Name: cube
Current Time: Dec 5 2019 16:18:22 IST
SIP service: Up
License request interval: 1 Minute(s)
Next request at: Dec 5 2019 16:18:46 IST
Recent request(s) for CUBE Standard Trunk
---------------------------------------------------------------------
Timestamp                   Count        Result              
---------------------------------------------------------------------          
Dec 5 2019 16:17:46 IST     2            Authorized(Response Pending)
Dec 5 2019 15:59:46 IST     0            Authorized          
Dec 5 2019 15:58:46 IST     1            Authorized
```

After receiving the response, the output is updated accordingly. Considering the above example, the result for the entitlement
                              request that is sent at "Dec 5 2019 16:17:46 IST" will be updated as "Authorized" as shown below.

```
cube#show voice sip license status

Host Name: cube
Current Time: Dec 5 2019 16:18:32 IST
SIP service: Up
License request interval: 1 Minute(s)
Next request at: Dec 5 2019 16:18:46 IST
Recent request(s) for CUBE Standard Trunk
---------------------------------------------------------------------
Timestamp                   Count        Result              
---------------------------------------------------------------------          
Dec 5 2019 16:17:46 IST     2            Authorized
Dec 5 2019 15:59:46 IST     0            Authorized          
Dec 5 2019 15:58:46 IST     1            Authorized
```

The entitlement request is sent only when there is a change in the license request count. For example, in the following output,
                              license request interval is 5 minutes and a request was sent for a count of 3 at Nov 21 2019 14:29:50 IST. There was no change
                              in the license usage during the 5-minute interval and therefore a request is not sent at Nov 21 2019 14:34:50 IST. The license
                              usage got changed in the next 5-minute interval and therefore a request was sent at Nov 21 2019 14:39:50 IST.

```
cube#show voice sip license status

Host Name: cube
Current Time: Nov 22 2019 04:02:53 IST 
SIP service: Up
License request interval: 5 Minute(s)
Next request at: Nov 22 2019 04:04:50 IST
Recent request(s) for CUBE Standard Trunk
-----------------------------------------------------------
Time                        Count        Result                
-----------------------------------------------------------
Nov 21 2019 14:39:50 IST    0            Authorized              
Nov 21 2019 14:29:50 IST    3            Authorized
```

The following example shows output of the show voice sip license status command when the evaluation period has expired and the SIP service is blocked. Although the SIP service is blocked, information
                              about previous requests sent (when the SIP service was up) is available in the output. In the following example, a licenses
                              request was sent for a count of 15 at Nov 26 2019 04:59:53 IST when the SIP service was up. After that, the SIP service was
                              blocked due to expiry of evaluation period.

```
cube#show voice sip license status

Host Name: cube
Current Time: Nov 26 2019 05:03:08 IST
SIP service: blocked due to eval expiry
License request interval: 5 Minute(s)
Next request at: Nov 26 2019 05:04:53 IST
Recent request(s) for CUBE Standard Trunk
-----------------------------------------------------------
Timestamp                   Count        Result              
-----------------------------------------------------------
Nov 26 2019 04:59:53 IST    15           Eval period
```

## Examples

The following is a sample output for license usage in tabular and graphical format for Standard CUBE trunk calls:

```
Router#show voice sip license stats table
CUBE Standard Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           1          1
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Standard Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Standard Trunk License Usage  (last 72 hours)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          2         99
21-25          0         40
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0         43
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

CUBE Standard Trunk License Usage  (last 72 days)
Period     Average       Max
----------------------------
 1-5           0         99
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

```
Router#show voice sip license stats

                                                                  
                                                                  
                                                                  
                                                                  
      111111111111                                                
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1 ############                                                
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                      9 99 4 2                  4                             
                      9 99 0 1                  3                             
  100                 * **                                                    
   90                 * **                                                    
   80                 * **                                                    
   70                 * **                                                    
   60                 * **                                                    
   50                 * **                                                    
   40                 * ** *                    *                             
   30                 * ** *                    *                             
   20                 * ** * *                  *                             
   10                 * *# * *                  *                             
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      9                                                                       
      9                                                                       
  100                                                                         
   99 *                                                                       
   98 *                                                                       
   97 *                                                                       
   96 *                                                                       
   95 *                                                                       
   94 *                                                                       
   93 *                                                                       
   92 *                                                                       
   91 *                                                                       
   90 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum   # = average
```

The following is a sample output for license usage in tabular and graphical format for Enhanced CUBE calls:

```
Router#show voice sip license stats table
CUBE Enhanced Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Enhanced Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Enhanced Trunk License Usage  (last 72 hours)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0         50
21-25          0         20
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0         41
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

CUBE Enhanced Trunk License Usage  (last 72 days)
Period     Average       Max
----------------------------
 1-5           0         41
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

```
Router#show voice sip license stats
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                      5 53 221                  4                             
                      0 00 004                  1                             
  100                                                                         
   90                                                                         
   80                                                                         
   70                                                                         
   60                                                                         
   50                 * *                                                     
   40                 * *                       *                             
   30                 * **                      *                             
   20                 * ** **                   *                             
   10                 * ** ***                  *                             
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      4                                                                       
      1                                                                       
   50                                                                         
   49                                                                         
   48                                                                         
   47                                                                         
   46                                                                         
   45                                                                         
   44                                                                         
   43                                                                         
   42                                                                         
   41 *                                                                       
   40 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 days)
          * = maximum   # = average
```

The following is a sample output for license usage in tabular and graphical format for Aggregate trunk CUBE calls:

```
Router#show voice sip license stats table
CUBE Aggregate Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Aggregate Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Aggregate Trunk License Usage  (last 72 hours)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0         50
21-25          0         20
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0         41
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0

CUBE Aggregate Trunk License Usage  (last 72 days)
Period     Average       Max
----------------------------
 1-5           0         41
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

```
Router#show voice sip license stats
       
                                                                  
                                                                  
                                                                  
                                                                  
      11111111111111111                                           
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1 #################                                           
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                      9 99 422                  8                             
                      9 99 001                  0                             
  100                 * **                                                    
   90                 * **                                                    
   80                 * **                      *                             
   70                 * **                      *                             
   60                 * **                      *                             
   50                 * **                      *                             
   40                 * ** *                    *                             
   30                 * ** *                    *                             
   20                 * ** ***                  *                             
   10                 * *# ***                  *                             
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      9                                                                       
      9                                                                       
  100                                                                         
   99 *                                                                       
   98 *                                                                       
   97 *                                                                       
   96 *                                                                       
   95 *                                                                       
   94 *                                                                       
   93 *                                                                       
   92 *                                                                       
   91 *                                                                       
   90 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 days)
          * = maximum   # = average
```

The license usage reporting for WebSockets in CUBE includes the summary of last 10 usage reports. The following is a sample
                              output of show voice sip license for a CUBE router in B2BHA mode:

```
Router#show voice sip license status 
Host Name: Router
Current Time: Apr 30 2021 07:37:12 UTC
SIP service: Up
License use recorded every: 7 Day(s)
Next record at: May 7 2021 07:00:00 UTC
Recent use of license(s) for CUBE Enhanced Trunk
----------------------------------------------------------------------------
Timestamp                   Count       
----------------------------------------------------------------------------
Apr 30 2021 07:00:00 UTC    10          
Apr 30 2021 05:55:11 UTC    1           
Apr 30 2021 05:54:52 UTC    1           
Router#sh log | sec LICENSE_INFO
*Apr 30 07:00:00.751: %CUBE-5-LICENSE_INFO: Requesting for 0 CUBE Enhanced trunk licenses
Router#sh voice sip license stats  

Router   07:37:47 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                 
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:37:50 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 seconds)

          
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      1                                                                       
      0                                                                       
   20                                                                         
   19                                                                         
   18                                                                         
   17                                                                         
   16                                                                         
   15                                                                         
   14                                                                         
   13                                                                         
   12                                                                         
   11                                                                         
   10 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:37:54 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                            
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 seconds)

          
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      1                                                                       
      0                                                                       
   20                                                                         
   19                                                                         
   18                                                                         
   17                                                                         
   16                                                                         
   15                                                                         
   14                                                                         
   13                                                                         
   12                                                                         
   11                                                                         
   10 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                        
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:37:56 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 seconds)

          
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                             
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 days)
          * = maximum   # = average

===========================================================================

STANDBY:

Router#sh voice sip license status 
Host Name: Router
Current Time: Apr 30 2021 07:37:26 UTC
SIP service: Up
License use recorded every: 7 Day(s)
Next record at: Timer not started
Recent use of license(s) for CUBE Enhanced Trunk
----------------------------------------------------------------------------
Timestamp                   Count       
----------------------------------------------------------------------------
Apr 30 2021 05:55:11 UTC    1           
Router#sh log | sec LICENSE_INFO
Router#
Router#
Router#sh voice sip license stats  

Router   07:38:52 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                             
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                        
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:38:52 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      1                                                                       
      0                                                                       
   20                                                                         
   19                                                                         
   18                                                                         
   17                                                                         
   16                                                                         
   15                                                                         
   14                                                                         
   13                                                                         
   12                                                                         
   11                                                                         
   10 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 hours)
          * = maximum   # = average\

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:38:57 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 seconds)

          
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
      1                                                                       
      0                                                                       
   20                                                                         
   19                                                                         
   18                                                                         
   17                                                                         
   16                                                                         
   15                                                                         
   14                                                                         
   13                                                                         
   12                                                                         
   11                                                                         
   10 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   07:38:58 AM Friday Apr 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 seconds)

          
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                            
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                             
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                        
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 days)
          * = maximum   # = average
```

The license usage reporting for WebSockets in CUBE includes the summary of last 10 usage reports. The following is a sample
                              output of show voice sip license for a CUBE router in Standalone mode:

```
Router#show voice sip license status 
Host Name: Router
Current Time: Mar 30 2021 00:32:35 UTC
SIP service: Up
License use recorded every: 8 Hour(s)
Next record at: Mar 30 2021 07:00:00 UTC
Recent use of license(s) for CUBE Standard Trunk
----------------------------------------------------------------------------
Timestamp                   Count       
----------------------------------------------------------------------------
Mar 29 2021 23:00:00 UTC    0           
Mar 29 2021 22:00:00 UTC    9           
Mar 29 2021 21:00:00 UTC    24          
Mar 29 2021 20:00:00 UTC    13          
Mar 29 2021 11:00:00 UTC    0           
Mar 29 2021 09:00:00 UTC    2           
Recent use of license(s) for CUBE Enhanced Trunk
----------------------------------------------------------------------------
Timestamp                   Count       
----------------------------------------------------------------------------
Mar 29 2021 21:00:00 UTC    0           
Mar 29 2021 20:00:00 UTC    2           
Mar 29 2021 11:00:00 UTC    0           
Mar 29 2021 09:00:00 UTC    8      

==========================================

Router#sh voice sip license stats                                                         

Router   12:34:22 AM Tuesday Mar 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Standard Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
          21         1                                                        
         943         0                                                        
  100                                                                         
   90                                                                         
   80                                                                         
   70                                                                         
   60                                                                         
   50                                                                         
   40                                                                         
   30                                                                         
   20     *                                                                   
   10    ***         *                                                        
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Standard Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   12:34:23 AM Tuesday Mar 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Enhanced Trunk License Usage (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
           2         8                                                        
   10                                                                         
    9                                                                         
    8                *                                                        
    7                *                                                        
    6                *                                                        
    5                *                                                        
    4                *                                                        
    3                *                                                        
    2      *         *                                                        
    1      *         *                                                        
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Enhanced Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   12:34:25 AM Tuesday Mar 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Aggregate Trunk License Usage (last 60 minutes)
          * = maximum   # = average\

                                                                              
                                                                              
                                                                              
          21         1                                                        
         945         0                                                        
  100                                                                         
   90                                                                         
   80                                                                         
   70                                                                         
   60                                                                         
   50                                                                         
   40                                                                         
   30                                                                         
   20     **                                                                  
   10    ***         *                                                        
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0 
          CUBE Aggregate Trunk License Usage (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          CUBE Aggregate Trunk License Usage (last 72 days)
          * = maximum   # = average

Router   12:34:25 AM Tuesday Mar 30 2021 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 seconds)

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                            
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          TDM-SIP Trunk Sessions (last 60 minutes)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 hours)
          * = maximum   # = average

                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                        
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1                                                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          TDM-SIP Trunk Sessions (last 72 days)
          * = maximum   # = average
```

## show voice source-group

To display the details of one or more voice source IP groups, use the show voice source - group command in privileged EXEC mode.

show voice source-group [ name | sort [ ascending | descending ]]

### Syntax Description

name

(Optional) Name of the source IP group to display.

sort [ ascending | descending

(Optional) Displays the source IP groups in either ascending or descending alphanumerical order.

### Command Default

Ascending order

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

## Examples

The following sample output shows an invalid configuration.

```
Router# show voice source-group abc Source Group: abc
    description="",
    carrier-id source="sj_area",
    carrier-id target="",
    trunk-group-label source="",
    trunk-group-label target="ny_main",
    h323zone-id="",
    access-list=,
    disconnect-cause="no-service",
    translation-profile="",
```

The following sample output shows a valid configuration for carrier-ID routing:

```
Router# show voice source-group abc Source Group: abc
    description="",
    carrier-id source="",
    carrier-id target="",
    trunk-group-label source="texas_backup",
    trunk-group-label target="ny_main",
    h323zone-id="",
    access-list=,
    disconnect-cause="no-service",
    translation-profile="",
```

If you are using carrier-ID routing, both carrier-ID fields are filled in and the "trunk-group-label" fields are blank.

The following sample output displays the source groups in ascending order. Both source IP groups use carrier-ID routing.

```
Router# show voice source-group sort ascending Source Group:1
        description="routec calls from 1311 to 1411",
        carrier-id source="1311",
        carrier-id target="1411",
        trunk-group-label source="",
        trunk-group-label target="",
        h323zone-id="fr1311",
        access-list= ,
        disconnect-cause="user-busy",
        destination-pattern="",
        incoming called-number="",
        translation-profile="10",
Source Group:2
        description="",
        carrier-id source="abcd",
        carrier-id target="xyz",
        trunk-group-label source="",
        trunk-group-label target="",
        h323zone-id="",
        access-list= ,
        disconnect-cause="no-service",
        destination-pattern="",
        incoming called-number="",
        translation-profile="",
```

The table below describes significant fields shown in this output.

Field

Description

Source Group

Name of the voice source IP group.

description

Description of the voice source IP group.

carrier-id source

Name of the source carrier ID used by the terminating gateway to select a target carrier.

carrier-id target

Name of the target carrier ID used by the terminating gateway to select a dial peer for routing the call over a POTS line.

trunk-group-label source

Name of the source trunk group used by the originating gateway to route the call over an inbound dial peer.

trunk-group-label target

Name of the target trunk group used by the terminating gateway to select a dial peer for routing an outbound call over a
                                          POTS line.

h323zone-id

Name of the zone associated with incoming H.323 calls to the voice source IP group.

access-list

Number of the access list used by the voice source IP group to block calls.

disconnect-cause

Phrase returned by the voice source IP group when a call is blocked.

translation-profile

Name of the translation profile used by the voice source IP group to translate calls.

### Related Commands

Command

Description

voice source-group

Initiates a voice source IP group definition.

## show voice statistics csr interval accounting

To display accounting statistics by configured intervals, use the show voice statistics csr interval accounting command in privileged EXEC mode.

show voice statistics csr interval tag-number accounting { all | method-list method-list-name } [ push { all | ftp | syslog }]

### Syntax Description

tag-number

Interval that represents a specified time range. The valid range is from 1 to 36655.

You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command.

all

Displays all voice accounting statistics.

method-list-name method-list-name

Displays accounting statistics by method list. You must specify a method-list name.

push

(Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows:

all--Pushes statistics to both the FTP and syslog servers.

ftp--Pushes statistics to the FTP server.

syslog--Pushes statistics to the syslog server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following sample output shows all of the statistics that were collected for interval tag 102 for method list h323-1:

```
Router# show voice statistics csr interval 102 accounting method-list h323-1 Client Type: Voice ACCT Stats 
        Start Time: 2002-05-01T19:35:17Z        End Time: 2002-05-01T19:36:29Z
methodlist=h323-1,acc_pass_criteria=1,pstn_in_pass=0,pstn_in_fail=0,pstn_out_pass=0,
pstn_out_fail=0,ip_in_pass=0,ip_in_fail=0,ip_out_pass=0,ip_out_fail=0
```

The table below lists and describes the significant output fields.

Field

Description

Client Type

The type of statistics collected.

Start Time

The start time of the statistics collection.

End Time

The ending time of the statistics collection.

method-list

The method list name.

acc_pass_criteria

Accounting pass criteria:

1: all start/interim/stop messages passed.

2: all start/stop messages passed.

3: stop-only message passed.

pstn_in_pass

Number of incoming calls on the PSTN leg that meet acc_pass_criteria.

pstn_in_fail

Number of incoming calls on the PSTN leg that fail acc_pass_criteria.

pstn_out_pass

Number of outgoing calls on the PSTN leg that meet acc_pass_criteria.

pstn_out_fail

Number of outgoing calls on the PSTN leg that fail acc_pass_criteria.

ip_in_pass

Number of incoming calls on the IP leg that meet acc_pass_criteria.

ip_in_fail

Number of incoming calls on the IP leg that fail acc_pass_criteria.

ip_out_pass

Number of outgoing calls on the IP leg that meet acc_pass_criteria.

ip_out_fail

Number of outgoing calls on the IP leg that fail acc_pass_criteria.

### Related Commands

Command

Description

show event-manager consumers

Displays event-manager statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics csr since-reset all

Displays all CSRs since the last reset.

show voice statistics interval-tag

Displays the configured interval numbers.

show voice statistics memory-usage

Displays current memory usage.

## show voice statistics csr interval aggregation

To display signaling statistics by configured intervals, use the show voice statistics csr interval aggregation command in privileged EXEC mode.

show voice statistics csr interval tag-number aggregation { all | gateway | ip | pstn | trunk-group { trunk-group-labe l | all } | voice-port { voice-port-label | all }} [ mode { concise | verbose }] [ push { all | ftp | syslog }]

### Syntax Description

tag-number

Interval that represents a specified time range. The valid range is from 1 to 36655.

You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command.

all

Displays all levels of signaling statistics.

gateway

Displays gateway-wide level statistics.

ip

Displays VoIP interface level statistics.

pstn

Displays telephone interface level statistics.

trunk-group

Displays trunk-group level statistics.

trunk-group-label --displays statistics for a specific trunk group

all --Displays statistics for all trunk groups.

voice-port

Displays voice-port level statistics:

voice-port-label --displays statistics for a specific voice port

all --Displays statistics for all voice ports.

mode

(Optional) Statistics are displayed in a specified mode. The keywords are as follows:

concise--Displays output that contains total calls, answered calls, and answered call duration.

verbose--Displays all fields contained in call statistic records (CSRs). This is the default setting.

push

(Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows:

all--Pushes statistics to both the FTP and syslog servers.

ftp--Pushes statistics to the FTP server.

syslog--Pushes statistics to the syslog server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command is valid only if the voice statistics time-range command is configured to either the periodic or start-stop value. If you enter the show voice statistics csr interval aggregation command but the gateway has been configured to collect statistics only since the last reset, the gateway displays an error
                              message.

You must first enter the show voice statistics interval-tag to obtain the valid tag numbers that you can enter for this command.

## Examples

The following sample output shows signaling statistics for all aggregation levels for interval tag 200:

```
Router# show voice statistics csr interval 200 aggregation all Client Type: VCSR
        Start Time: 2002-04-28T01:48:24Z        End Time: 2002-04-28T01:50:01Z
record_type=gw,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=ip,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=pstn,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/0:23,in_call=0,in_ans=0,in_fail=0
,out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/1:23,in_call=0,in_ans=0,in_fail=0
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
```

The table below lists and describes the significant output fields.

Field

Description

Client Type

The type of statistics collected.

Start Time

The start time of the statistics collection.

End Time

The ending time of the statistics collection.

record_type

Call statistics record type. Symbols are gw, ip, pstn, tg, and vp.

trunk_group_id

Trunk group ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

voice_port_id

Voice port ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

in_call

Number of incoming calls.

in_ans

Number of incoming calls answered by the gateway.

in_fail

Number of incoming calls that failed.

out_call

Number of outgoing calls attempted.

out_ans

Number of outgoing calls that received answers.

out_fail

Number of outgoing calls that failed.

in_szre_d

Incoming seizure duration (in seconds).

out_szre_d

Outgoing seizure duration (in seconds).

in_conn_d

Incoming connected duration (in seconds).

out_conn_d

Outgoing connected duration (in seconds).

orig_disconn

Number of calls encountering the originating side having been disconnected before the outgoing calls were connected.

in_ans_abnorm

Number of incoming answered calls terminated with any cause code other than "normal".

out_ans_abnorm

Number of outgoing answered calls terminated with any cause code other than "normal".

in_mcd

Number of incoming calls lasting less than the configured minimum call duration (MCD).

out_mcd

Number of outgoing calls lasting less than the configured MCD.

in_pdd

Total post dial delay duration on incoming calls (in ms).

out_pdd

Total post dial delay duration on outgoing calls (in ms).

in_setup_delay

Total inbound setup delay duration (in ms).

out_setup_delay

Total outbound setup delay duration (in ms).

lost_pkt

Number of calls losing more than the configured number of packets.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

latency

Number of calls encountering more than the configured amount of latency.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

jitter

Number of calls encountering more than configured amount of jitter.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

in_cc_no

Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5).

in_disc_cc

Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal).

out_disc_cc

Outgoing disconnect cause code.

out_cc_no

Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5).

in_cc_id

Disconnect cause code ID for the following field for incoming calls.

in_cc_cntr

Disconnect cause code counter for incoming calls (any incoming cause code counter pairs).

out_cc_id

Disconnect cause code ID for the following field for outgoing calls.

out_cc_cntr

Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs).

### Related Commands

Command

Description

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics csr since-reset all

Displays all CSRs since the last reset.

show voice statistics interval-tag

Displays the configured interval numbers.

show voice statistics memory-usage

Displays current memory usage.

voice statistics time-range

Specifies the time range to collect CSRs.

## show voice statistics csr since-reset accounting

To display VoIP AAA accounting statistics since the last reset, use the show voice statistics csr since-reset accounting command in privileged EXEC mode.

show voice statistics csr since-reset accounting { all | method-list method-list-name } [ push { all | ftp | syslog }]

### Syntax Description

all

All collected statistics since the last reset are displayed.

method-list method-list-name

Collected statistics by method list since the last reset are displayed. The method-list-name argument specifies the name
                                          of the method list.

push

(Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows:

all--Pushes statistics to both the FTP and syslog servers.

ftp--Pushes statistics to the FTP server.

syslog--Pushes statistics to the syslog server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command only applies if the voice statistics time-range command is configured to the since-reset value. Voice statistics collection on the gateway is reset using the clear voice statistics csr command.

If you enter the show voice statistics csr since-reset accounting command but the gateway has been configured for periodic collection or to a specific interval, the gateway will display an
                              error message.

## Examples

The following sample output shows the accounting statistics for method list h323-1 since the last reset:

```
Router# show voice statistics csr since-reset accounting method-list h323-1
Client Type: Voice ACCT Stats 
        Start Time: 2002-05-05T17:39:17Z        End Time: 2002-05-09T19:00:16Z
methodlist=h323-1,acc_pass_criteria=1,pstn_in_pass=0,pstn_in_fail=1,pstn_out_pass=0,
pstn_out_fail=0,ip_in_pass=0,ip_in_fail=0,ip_out_pass=0,ip_out_fail=1
```

The table below lists and describes the significant output fields.

Field

Description

Client Type

The type of statistics collected.

Start Time

The start time of the statistics collection.

End Time

The ending time of the statistics collection.

method-list

The method list name.

acc_pass_criteria

Accounting pass criteria:

1: all start/interim/stop messages passed.

2: all start/stop messages passed.

3: stop-only message passed.

pstn_in_pass

Number of incoming calls on the PSTN leg that meet acc_pass_criteria.

pstn_in_fail

Number of incoming calls on the PSTN leg that fail acc_pass_criteria.

pstn_out_pass

Number of outgoing calls on the PSTN leg that meet acc_pass_criteria.

pstn_out_fail

Number of outgoing calls on the PSTN leg that fail acc_pass_criteria.

ip_in_pass

Number of incoming calls on the IP leg that meet acc_pass_criteria.

ip_in_fail

Number of incoming calls on the IP leg that fail acc_pass_criteria.

ip_out_pass

Number of outgoing calls on the IP leg that meet acc_pass_criteria.

ip_out_fail

Number of outgoing calls on the IP leg that fail acc_pass_criteria.

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics interval-tag

Displays the configured interval numbers

show voice statistics memory-usage

Displays current memory usage.

voice statistics time-range

Specifies a time range to collect statistics from the gateway on a periodic basis, since the last reset, or for a specific
                                          time duration.

## show voice statistics csr since-reset aggregation-level

To display signaling statistics since the last reset, use the show voice statistics csr since-reset aggregation-level command in privileged EXEC mode.

show voice statistics csr since-reset aggregation-level { all | gateway | ip | pstn | trunk-group { all | trunk-group-label } | voice-port { all | voice-port-label }} [ mode { concise | verbose }] [ push { all | ftp | syslog }]

### Syntax Description

all

All signaling statistics.

gateway

Gateway-wide level statistics.

ip

VoIP-interface-level statistics.

pstn

PSTN-level statistics.

trunk-group

Trunk-group-level statistics. Keywords and arguments are as follows.

all --Statistics for all trunk groups.

trunk-group-label --Statistics for a specific trunk group.

voice-port

Voice-port-level statistics. Keywords and arguments are as follows:

all --Statistics for all voice ports.

voice-port-label --Statistics for a specific voice port.

mode

(Optional) Statistics in a specified mode. Keywords are as follows:

concise--Output contains total calls, answered calls, and answered call duration.

verbose--All fields contained in call statistic records (CSRs). This is the default.

push

(Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. Keywords are as follows:

all--Pushes statistics to both the FTP and syslog servers.

ftp--Pushes statistics to the FTP server.

syslog--Pushes statistics to the syslog server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command applies only if the voice statistics time-range command is configured to the since-reset value. Voice statistics collection on the gateway is reset using the clear voice statistics csr command.

If you enter the show voice statistics csr since-reset aggregation-level command but the gateway has been configured for periodic collection or to a specific interval, the gateway will display an
                              error message.

## Examples

The following sample output shows signaling statistics for all aggregation levels since the last reset:

```
Router# show voice statistics csr since-reset aggregation-level all Client Type: VCSR
        Start Time: 2002-04-25T01:48:12Z        End Time: 2002-04-25T01:50:01Z
record_type=gw,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=ip,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=pstn,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/0:23,in_call=0,in_ans=0,in_fail=0
,out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/1:23,in_call=0,in_ans=0,in_fail=0
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
```

The following sample output shows signaling statistics for the IP aggregation level since the last reset:

```
Router# show voice statistics csr since-reset aggregation-level ip Client Type: VCSR
        Start Time: 2002-04-25T01:48:12Z        End Time: 2002-05-02T21:21:27Z
record_type=ip,trunk_group_id=10,voice_port_id=2,in_call=15,in_ans=15,in_fail=0,out_call=0out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
```

The following sample output shows signaling statistics for the PSTN aggregation level since the last reset:

```
Router# show voice statistics csr since-reset aggregation-level pstn Client Type: VCSR
        Start Time: 2002-04-25T01:48:12Z        End Time: 2002-05-02T21:21:42Z
record_type=pstn,trunk_group_id=25,voice_port_id=2,in_call=100,in_ans=10,in_fail=90,
out_call=0,out_ans=0,out_fail=0,in_szre_d=100,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
```

The table below lists and describes the significant output fields.

Field

Description

Client Type

The type of statistics collected.

Start Time

The start time of the statistics collection.

End Time

The ending time of the statistics collection.

record_type

Call statistics record type. Symbols are gw, ip, pstn, tg, and vp.

trunk_group_id

Trunk group ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

voice_port_id

Voice port ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

in_call

Number of incoming calls.

in_ans

Number of incoming calls answered by the gateway.

in_fail

Number of incoming calls that failed.

out_call

Number of outgoing calls attempted.

out_ans

Number of outgoing calls that received answers.

out_fail

Number of outgoing calls that failed.

in_szre_d

Incoming seizure duration (in seconds).

out_szre_d

Outgoing seizure duration (in seconds).

in_conn_d

Incoming connected duration (in seconds).

out_conn_d

Outgoing connected duration (in seconds).

orig_disconn

Number of calls encountering the originating side having been disconnected before the outgoing calls were connected.

in_ans_abnorm

Number of incoming answered calls terminated with any cause code other than "normal".

out_ans_abnorm

Number of outgoing answered calls terminated with any cause code other than "normal".

in_mcd

Number of incoming calls lasting less than the configured minimum call duration (MCD).

out_mcd

Number of outgoing calls lasting less than the configured MCD.

in_pdd

Total post dial delay duration on incoming calls (in ms).

out_pdd

Total post dial delay duration on outgoing calls (in ms).

in_setup_delay

Total inbound setup delay duration (in ms).

out_setup_delay

Total outbound setup delay duration (in ms).

lost_pkt

Number of calls losing more than the configured number of packets.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

latency

Number of calls encountering more than the configured amount of latency.

This field will exist only in "IP" records. In other types of records, this field will be empty and extra commas are expected.

jitter

Number of calls encountering more than configured amount of jitter.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

in_disc_cc

Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal).

out_disc_cc

Outgoing disconnect cause code.

in_cc_no

Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5).

out_cc_no

Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5).

in_cc_id

Disconnect cause code ID for the following field for incoming calls.

in_cc_cntr

Disconnect cause code counter for incoming calls (any incoming cause code counter pairs).

out_cc_id

Disconnect cause code ID for the following field for outgoing calls.

out_cc_cntr

Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs).

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

clear voice statistics csr

Clears voice-statistic collection settings on the gateway.

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics interval-tag

Displays voice statistics within a specified interval.

show voice statistics memory-usage

Displays current memory usage.

voice statistics time-range

Specifies the time range to collect CSRs.

## show voice statistics csr since-reset all

To display all voice call statistical information since a reset occurred, use the show voice statistics csr since-reset all command in privileged EXEC mode.

show voice statistics csr since-reset all [ mode { concise | verbose }] [ push { all | ftp | syslog }]

### Syntax Description

mode

(Optional) Statistics are displayed in a specified mode. The keywords are as follows:

concise--Displays output that contains total calls, answered calls, and answered call duration.

verbose--Displays all fields contained in call statistic records (CSRs). This is the default setting.

push

(Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows:

all--Pushes statistics to both the FTP and syslog servers.

ftp--Pushes statistics to the FTP server.

syslog--Pushes statistics to the syslog server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command can also be used to display and push VoIP internal error codes (IECs).

## Examples

The following example shows all of the statistics that were collected since the last reset:

```
Router# show voice statistics csr since-reset all Client Type: VCSR
        Start Time: 2002-05-01T19:35:17Z        End Time: 2002-05-01T19:36:26Z
record_type=gw,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=ip,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,lost_pkt=0,latency=0,jitter=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=pstn,trunk_group_id=,voice_port_id=,in_call=0,in_ans=0,in_fail=0,out_call=0,
out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,orig_disconn=0,
in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,in_setup_delay=0,
out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/0/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/0,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=4/1/1,in_call=0,in_ans=0,in_fail=0,
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/0:23,in_call=0,in_ans=0,in_fail=0
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
!
record_type=vp,trunk_group_id=,voice_port_id=2/1:23,in_call=0,in_ans=0,in_fail=0
out_call=0,out_ans=0,out_fail=0,in_szre_d=0,out_szre_d=0,in_conn_d=0,out_conn_d=0,
orig_disconn=0,in_ans_abnorm=0,out_ans_abnorm=0,in_mcd=0,out_mcd=0,in_pdd=0,out_pdd=0,
in_setup_delay=0,out_setup_delay=0,in_disc_cc_16=0,out_disc_cc_16=0
Client Type: Voice ACCT Stats 
        Start Time: 2002-05-01T19:35:17Z        End Time: 2002-05-01T19:36:29Z
methodlist=h323-1,acc_pass_criteria=1,pstn_in_pass=0,pstn_in_fail=0,pstn_out_pass=0,
pstn_out_fail=0,ip_in_pass=0,ip_in_fail=0,ip_out_pass=0,ip_out_fail=0
```

The table below lists and describes the significant output fields.

Field

Description

Client Type

The type of statistics collected.

Start Time

The start time of the statistics collection.

End Time

The ending time of the statistics collection.

record_type

Call statistics record type. Symbols are gw, ip, pstn, tg, and vp.

trunk_group_id

Trunk group ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

voice_port_id

Voice port ID.

For the symbols gw, ip, pstn, and some vp records, this field is empty.

in_call

Number of incoming calls.

in_ans

Number of incoming calls answered by the gateway.

in_fail

Number of incoming calls that failed.

out_call

Number of outgoing calls attempted.

out_ans

Number of outgoing calls that received answers.

out_fail

Number of outgoing calls that failed.

in_szre_d

Incoming seizure duration (in seconds).

out_szre_d

Outgoing seizure duration (in seconds).

in_conn_d

Incoming connected duration (in seconds).

out_conn_d

Outgoing connected duration (in seconds).

orig_disconn

Number of calls encountering the originating side having been disconnected before the outgoing calls were connected.

in_ans_abnorm

Number of incoming answered calls terminated with any cause code other than "normal".

out_ans_abnorm

Number of outgoing answered calls terminated with any cause code other than "normal".

in_mcd

Number of incoming calls lasting less than the configured minimum call duration (MCD).

out_mcd

Number of outgoing calls lasting less than the configured MCD.

in_pdd

Total post dial delay duration on incoming calls (in ms).

out_pdd

Total post dial delay duration on outgoing calls (in ms).

in_setup_delay

Total inbound setup delay duration (in ms).

out_setup_delay

Total outbound setup delay duration (in ms).

lost_pkt

Number of calls losing more than the configured number of packets.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

latency

Number of calls encountering more than the configured amount of latency.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

jitter

Number of calls encountering more than the configured amount of jitter.

This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected.

in_disc_cc

Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal).

out_disc_cc

Outgoing disconnect cause code.

in_cc_no

Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5).

out_cc_no

Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5).

in_cc_id

Disconnect cause code ID for the following field for incoming calls.

in_cc_cntr

Disconnect cause code counter for incoming calls (any incoming cause code counter pairs).

out_cc_id

Disconnect cause code ID for the following field for outgoing calls.

out_cc_cntr

Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs).

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics interval-tag

Displays voice statistics within a specified interval.

show voice statistics memory-usage

Displays current memory usage.

## show voice statistics iec

To display Internal Error Code (IEC) statistics, use the show voice statistics iec command in user EXEC or privileged EXEC mode.

show voice statistics iec { interval number | since-reboot | since-reset } [ push [ all | ftp | syslog ]]

### Syntax Description

interval

Displays statistics for the specified interval.

number

The interval tag number. The range is from 1 to 36655.

since-reboot

Displays IEC statistics since the last reboot.

since-reset

Displays IEC statistics since the last reset.

push

Specifies the off-load pushing interface.

all

Indicates that IEC statistics will be off-loaded to all push interfaces.

ftp

Indicates that IEC statistics will be off-loaded to the FTP server.

syslog

Indicates that IEC statistics will be off-loaded to the syslog server.

### Command Modes

User EXEC (#) Privileged EXEC(#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

12.4(24)T

This command was modified in a release earlier than Cisco IOS Release 12.4(24)T. The push all , ftp and syslog keywords were added.

### Usage Guidelines

Before you can display IEC statistics for a specific interval, use the show voice statistics interval-tag command to display available interval options. Before you display view IEC statistics since reboot, you must configure the voice statistics type iec command. Before you can display IEC statistics since the last reset, you must configure the voice statistics type iec command and the voice statistics time-range since-reset command.

## Examples

The following is sample output from the show voice statistics iec since-reset command, which displays statistics since the last instance when IEC counters were cleared:

```
Router# show voice statistics iec since-reset Internal Error Code counters
----------------------------
Counters since last reset (2002-11-28T01:55:31Z):
  SUBSYSTEM CCAPI [subsystem code 1]
      [errcode   6] No DSP resource                            5
  SUBSYSTEM SSAPP [subsystem code 4]
      [errcode   5] No dial peer match                          2
      [errcode   3] CPU high                                  96
  SUBSYSTEM H323 [subsystem code 5]
      [errcode  22] No Usr Responding, H225 timeout            1
      [errcode 27] H225 invalid msg                           1
      [errcode 79] H225 chn, sock fail                       27
  SUBSYSTEM VTSP [subsystem code 9]
      [errcode   6] No DSP resource                           83
```

The table below describes the significant fields shown in the display.

Field

Description

SUBSYSTEM

Indicates the specific subsystem within the physical entity where the IEC was generated.

errcode

Identifies the error code within the subsystem.

The following is sample output from the show voice statistics iec since-reset push all command, which displays statistics since the last instance when IEC counters were cleared and off-loaded to all push interfaces.

```
Router# show voice statistics iec since-reset push all Internal Error Code counters
----------------------------
Counters since last reset (2009-07-16T01:40:59Z):
No errors.
Router#
*Jul 16 01:43:39.530: %VSTATS-6-IEC: SEQ=1:
stats_type,version,entity_id,start_time,end_time,record_count
IEC,1,7206-2,2009-07-16T01:40:59Z,2009-07-16T01:43:39Z,0
```

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

show voice statistics

Displays voice statistics.

show voice statistics interval-tag

Displays interval options available for IEC statistics.

voice statistics time-range since-reset

Enables collection of call statistics accumulated since the last resetting of IEC counters.

voice statistics type iec

Enables collection of IEC statistics.

## show voice statistics interval-tag

To display the interval numbers assigned by the gateway, use the show voice statistics interval-tag command in privileged EXEC mode.

show voice statistics interval-tag

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This is used to obtain the interval tag number required for the show voice statistics csr interval accounting and show voice statistics csr interval aggregation commands.

## Examples

The following example shows the start and end times for specific interval tags:

```
Router# show voice statistics interval-tag Current System Time is: 2002-4-1T010:10:00Z
	Interval-Tag				Intervals Start Time							End Time
	101				2002-3-31T010:00:00Z							2002-3-31T010:55:00Z
	105				2002-3-31T012:15:00Z							2002-3-31T012:30:00Z
```

The table below lists and describes the significant output fields.

Field

Description

Current System Time

Current system time of the gateway.

Interval-Tag

Interval number.

Intervals Start Time

Interval start time.

End Time

Interval end time.

### Related Commands

Command

Description

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics csr since-reset all

Displays all CSRs since the last reset.

show voice statistics memory-usage

Displays current memory usage.

## show voice statistics memory-usage

To display the memory used for collecting call statistics and to estimate the future use of memory, use the show voice statistics memory-usage command in privileged EXEC mode.

show voice statistics memory-usage { all | csr | iec }

### Syntax Description

all

Memory used to collect both signaling and accounting call statistics records (CSRs).

csr

Memory used to collect signaling CSRs only.

iec

Memory used to collect Cisco internal error codes (IECs) only.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows all of the memory used at a fixed interval and since the last reset for signaling and accounting;
                              it also shows the estimated future memory to be used.

```
Router# show voice statistics memory-usage all *** Voice Call Statistics Record Memory Usage ***
        Fixed Interval Option -
                CSR size: 136 bytes
                Number of CSR per interval: 9
                Used memory size (proximate): 0
                Estimated future claimed memory size (proximate): 0
        Since Reset Option -
                CSR size: 136 bytes
                Total count of CSR: 9
                Used memory size (proximate): 1224
*** Voice Call Statistics Accounting Record Memory Usage ***
        Fixed Interval Option -
                ACCT REC size: 80 bytes
                Number of ACCT REC per interval: 1
                Used memory size (proximate): 0
                Estimated future claimed memory size (proximate): 0
        Since Reset Option -
                ACCT REC size: 80 bytes
                Total count of ACCT REC: 1
                Used memory size (proximate): 80
```

The table below lists and describes the significant output fields.

Field

Description

Voice Call Statistics Record Memory Usage

Fixed Interval Option:

Statistics gathered for a fixed interval.

CSR size

Size of the CSR for the fixed interval.

Number of CSR per interval

Number of CSRs collected for the fixed interval.

Used memory size (proximate)

Amount of memory currently being used to store statistics.

Estimated future claimed memory size (proximate)

Amount of remaining memory available to store statistics.

Since Reset Option:

Statistics gathered since the last reset or reboot of the gateway.

CSR size

Size of the CSR since the last reset.

Total count of CSR

Total number of CSRs gathered since the last reset.

Used memory size (proximate)

Amount of memory currently being used to store statistics.

Voice Call Statistics Accounting Record Memory Usage

Fixed Interval Option:

Statistics gathered for a fixed interval.

ACCT REC size

Accounting record size.

Number of ACCT REC per interval

Number of accounting records per interval.

Used memory size (proximate)

Amount of memory currently being used to store statistics.

Estimated future claimed memory size (proximate)

Amount of remaining memory available to store statistics.

Since Reset Option:

Statistics gathered since the last reset or reboot of the gateway.

ACCT REC size

Accounting record size.

Total count of ACCT REC

Total number of accounting records since the last reset or reboot of the gateway.

Used memory size (proximate)

Amount of memory currently being used to store statistics.

### Related Commands

Command

Description

show event-manager consumers

Displays event statistics.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr interval aggregation

Displays statistical information by configured intervals for signaling statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

show voice statistics csr since-reset aggregation-level

Displays all signaling CSRs since the last reset.

show voice statistics csr since-reset all

Displays all CSRs since the last reset.

show voice statistics interval-tag

Displays the configured interval numbers.

| slot | Slot in which the voice card resides. |
|---|---|
| port | Port on the voice card. |

| Release | Modification |
|---|---|
| 12.3(2)T | This command was introduced on the Cisco AS5850. |

| Field | Description |
|---|---|
| flags | Internal vdev flags |
| dev_status | Additional flags giving status of the resource |
| service | Service currently running on this DSP |
| service_type | Service type as passed in by RPM |
| min_speed | Minimum configured modem speed |
| max_speed | Maximum configured modem speed |
| modulation | Maximum modulation to be negotiated |
| err_correction | Error correction to be negotiated |
| compression | Compression to be negotiated |
| csm_call_info | Address of the associated csm_call_info structure |
| csm_session | Session ID as maintained by CSM |
| vdev_p | Address of the associated resource structure |
| dsplib_state | State of the resource as seen by the DSPLIB |
| dsplib_next_action | Next DSPLIB action that should be taken on this resource |
| call_id | Call identifier if this resource has a HDLC call |
| called_number | Called number if this resource has a HDLC call |
| speed | Speed of the connection if this resource has a HDLC call |
| ces | Circuit emulation service information |
| spc | True if semi permanent call link |
| d_idb | Address of the associated D channel idb, if this resource has a HDLC call |
| Bulk sync reference | Number of times that this resource has been bulk synchronized |
| Global bulk syncs | Number of bulk synchronizations that the VDEV High Availability client has performed |

| Command | Description |
|---|---|
| debug vdev | Turns on debugging for voice devices. |
| show redundancy | Displays current or historical status and related information on a redundant RSC. |

| slot - number | VFC slot number. |
|---|---|
| technology | (Optional) Displays the technology type of the VFC. |

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced on the Cisco AS5300. |
| 12.0(2)XH | The technology keyword was added. |

| Command | Description |
|---|---|
| voice-card | Configures a voice card and enters voice-card configuration mode. |

| slot | Slot where the VFC is installed. Range is from 0 to 2. |
|---|---|

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced on the Cisco AS5300. |

| Command | Description |
|---|---|
| show vfc default - file | Displays the default files included in the default file list for this VFC. |
| show vfc directory | Displays the list of all files residing on this VFC. |
| show vfc version | Displays the version of the software residing on this VFC. |

| slot | Slot where the VFC is installed. Range is from 0 to 2. |
|---|---|

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced on the Cisco AS5300. |

| Command | Description |
|---|---|
| show vfc cap - list | Displays the current list of files on the capability list for this VFC. |
| show vfc directory | Displays the list of all files residing on this VFC. |
| show vfc version | Displays the version of the software residing on this VFC. |

| slot | Slot where the VFC is installed. Range is from 0 to 2. |
|---|---|

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced on the Cisco AS5300. |

| Field | Description |
|---|---|
| File Name | Name of the file stored in Flash memory. |
| Size (Bytes) | Size of the file in bytes. |

| Command | Description |
|---|---|
| show vfc cap - list | Displays the current list of files on the capability list for this VFC. |
| show vfc default - file | Displays the default files included in the default file list for this VFC. |
| show vfc version | Displays the version of the software residing on this VFC. |

| slot | Slot where the VFC is installed. Range is from 0 to 2. |
|---|---|
| dspware | Which DSPWare software to display. |
| vcware | Which VCWare software to display. |

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced on the Cisco AS5300. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T with changes to the command output. |

| Field | Description |
|---|---|
| Voice Feature Card in Slot | Slot in which the VFC is installed. |
| VCWare Version | Cisco VCWare version. Version 7.35 is the required minimum for Cisco IOS Release 12.2(11)T and higher. |
| ROM | ROM monitor version shows 1.3 . |
| DSPWare Version | The DSPWare version shows 3.4.46L, which is the required minimum for Cisco IOS Release 12.2(11)T and higher . |
| Technology | The technology shows C549. C549 technology is available to support either medium-complexity codecs or high-complexity codecs. |
| VCWare/DSPWare version compatibility | The Cisco VCWare and DSPWare versions are compatible with Cisco IOS software . Cisco VCWare/DSPWare version compatibility
                                          is either OK or shows a mismatch. Note This option is available only with Cisco IOS Release 12.2(10) mainline and later release or Cisco IOS Release 12.2(11)T and
                                                      later. | Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later release or Cisco IOS Release 12.2(11)T and
                                                      later. |
| Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later release or Cisco IOS Release 12.2(11)T and
                                                      later. |

| Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later release or Cisco IOS Release 12.2(11)T and
                                                      later. |
|---|---|

| Field | Description |
|---|---|
| Voice Feature Card in Slot | Slot in which the VFC is installed . |
| DSPWare Version | The DSPWare version shows 3.4.46L, which is the required minimum for Cisco IOS Release 12.2(10)T and higher . |
| VCWare/DSPWare version compatibility | The Cisco VCWare and DSPWare versions are compatible with Cisco IOS software. Cisco VCWare/DSPWare version compatibility
                                          is either OK or shows a mismatch. Note This option is available only with Cisco IOS Release 12.2(10) mainline and later or 12.2(11)T and later. | Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later or 12.2(11)T and later. |
| Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later or 12.2(11)T and later. |

| Note | This option is available only with Cisco IOS Release 12.2(10) mainline and later or 12.2(11)T and later. |
|---|---|

| Command | Description |
|---|---|
| show vfc cap - list | Displays the current list of files on the capability list for this VFC. |
| show vfc default - file | Displays the default files included in the default file list for this VFC. |
| show vfc directory | Displays the list of all files residing on this VFC. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco MC3810. |
| 12.0(7)T | The command was integrated into Cisco IOS Release 12.0(7)T. |

| Command | Description |
|---|---|
| show call history video record | Displays information about video calls. |

| method-list-name | (Optional) Name of a specific method list. This option displays connectivity status information for a single method list
                                          identified by this argument. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Current Status: reachable or unreachable | Current status of the method list: reachable or unreachable and the time (in hh:mm:ss) and date the method list reached this
                                          status. |
| last record sent time | Time (in hh:mm:ss) and date the last accounting record was sent to the method list. |
| total probe sent out | Number of probe records sent up to the time of the show command. |
| SUCCESS: Received from server | Number of success status of the accounting records of this type received from the method list. |
| SUCCESS: Notified to client | Number of success status of the accounting records of this type for which notifications were sent to the GAS. |
| FAILURE: Received from server | Number of failure status of the accounting records of this type received from the method list. |
| FAILURE: Notified to client | Number of failure status of the accounting records of this type for which notifications were sent to the GAS. |
| FAILURE: Reported to call | Number of failure status of the accounting records of this type that were reported to the call application. |

| Command | Description |
|---|---|
| clear voice accounting method | Clears accounting status statistics for a particular accounting method list or all accounting method lists. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Total num of acct sessions waiting for acct responses | Number of accounting sessions that are waiting for accounting responses. |
| Total num of acct start responses pending | Number of accounting start responses that are pending. |
| Total num of acct interim update responses pending | Number of accounting interim update responses that are pending. |
| Total num of acct stop responses pending | Number of accounting stop responses that are pending. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| busyout forced | Forces a voice port into the busyout state. |
| busyout monitor | Places a voice port in the busyout monitor state. |
| busyout seize | Changes the busyout seize procedure from a voice port. |
| voice-port busyout | Places all voice ports associated with a serial or ATM interface in a busyout state. |

| all | Specifies the current cable status of all analog voice ports that have cable polling enabled. |
|---|---|
| summary | Specifies the last cable status of all analog voice ports that have cable polling enabled. |
| x/y/z | Voice port number. |
| x/y/z-z1 | Voice port number range. The range is from 0 to 71. Example: 2/0/0-71. |

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| cable-detect | Enables cable polling on analog FXOGS, FXOLS, FXSGS, and FXSLS voice ports. |
| cable-detect-poll-timer | Configures the cable polling timer value for background polling processes on an analog voice port. |

| Cisco 827, Cisco 1700 Series, and Cisco 7750 with Analog Voice Ports |
|---|
| slot / port | (Optional) A specific analog voice port: slot-- Physical slot in which the analog voice module (AVM) is installed. / port --Analog voice port number. Range is from 1 to 6. The slash mark is required. |
| status [ call-id ] | (Optional) Displays status of active calls. If call-id is specified, this command displays the status of a specific call . |
| sample seconds | (Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10. |
| summary | (Optional) Displays current settings and state of the voice port, regardless of port activity. |

| Cisco 2600 Series, Cisco 3600 Series, Cisco 3700 Series with Analog Voice Ports |
|---|
| slot / subunit / port | (Optional) A specific analog voice port: slot --Router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform. / subunit -- Voice interface card (VIC) in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network
                                                module.) The slash mark is required. / port -- Analog voice port number. Valid entries are 0 and 1. The slash mark is required. |
| status [ call-id ] | (Optional) Displays status of active calls. If call-id is specified, this command displays the status of a specific call . |
| sample seconds | (Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10. |
| summary | (Optional) Displays current settings and state of the voice port, regardless of port activity. |

| Cisco 2600, Cisco 3600, and Cisco 3700 Series with Digital Voice Ports (with T1 Packet Voice Trunk Network Modules) |
|---|
| slot / port : ds0 - group | (Optional) A specific digital voice port: slot -- Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for the
                                                particular platform. / port --T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1. (One VWIC fits in an NM.) The
                                                slash mark is required. : ds0 - group-- T1 or E1 logical port number. Range is from 0 to 23 for T1 and from 0 to 30 for E1. The colon is required. |
| status [ call-id ] | (Optional) Displays status of active calls. If call-id is specified, this command shows the status of a specific call . |
| sample seconds | (Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10. |
| summary | (Optional) Displays current settings and state of the DSP port regardless of port activity. |

| Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850, Cisco 7200 Series, and Cisco 7500 Series with Digital Voice Ports |
|---|
| slot / port : ds0 - group | (Optional) A specific digital voice port: slot --Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for
                                                the particular platform. / port-- T1 or E1 physical port in the VWIC. Valid entries are 0 and 1. (One VWIC fits in an NM.) The slash mark is required. : ds0 - group-- T1 or E1 logical port number. Range is from 0 to 23 for T1 and from 0 to 30 for E1. The colon is required. |
| status [ call-id ] | (Optional) Displays status of active calls. If call-id is specified, this command shows the status of a specific call . |
| sample seconds | (Optional) Displays status over a specified sampling interval, in seconds. Range is from 1 to 30. Default is 10. |
| summary | (Optional) Displays current settings and state of the voice port regardless of port activity. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(13)T | This command was modified with the status , call-id , and sample seconds command options. This command is available on all voice platforms. |
| 12.4(3d) | This command was modified to support the Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms for Non-Facility Associated
                                          Signaling (NFAS) configuration. Output was modified to provide accurate port information for NFAS configuration on these platforms. |
| 15.1(3)T | This command was modified. The output of this command was enhanced to display the connection status of foreign exchange office
                                          (FXO) ports. |

| Note | This command is not supported in Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms for NFAS configuration before Cisco
                                          IOS Release 12.4(3d). |
|---|---|

| Note | Use the show voice dsmp stream command to display the current session of the voice Distributed Stream Media Processor (DSMP) media stream and its related
                                          applications. |
|---|---|

| Note | The Voice Call Tuning feature is not supported on the Cisco AS5300. |
|---|---|

| Note | Beginning in Cisco IOS Release 15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected
                                          or disconnected, a message is displayed to indicate the status change. For example, the following message is displayed to
                                          report that a cable has been connected, and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122
                                          EST: %LINK-3-UPDOWN: Interface Foreign Exchange Office 0/2/0, changed state to operational status up due to cable reconnection |
|---|---|

| Note | The output from the show voice call summary command is slightly different in the PORT field on platforms other than the Cisco AS5350, Cisco AS5400, and Cisco AS5850.
                                          The contrast between platform types is as follows: Platform Regular PRI (T1) NFAS PRI (T1)* --------------------------------------------------------------
                                          non-AS5xxx 3/0:23.TS 3/1:23.TS AS5xxx 3/0:D.TS Ser3/1:(TS-1) * Assumes T1 3/1 is a member of an NFAS group with T1 3/0 as
                                          the primary NFAS member, and TS is the time slot counted from a base of 1 (for example 1, 2, 3). |
|---|---|

| Note | You can query only one call at a time. If you attempt queries from different ports (console and Telnet ), and if a query
                                          is in progress on another port, the system asks you to wait for completion of that query. You can query any call from anywhere,
                                          at anytime, except during the sample interval for an enquiry that is already in progress. This simplifies the implementation
                                          significantly and does not reduce the usefulness of the command. |
|---|---|

| Note | Do not use the 0x prefix in the call-id argument when you enter the resulting call ID in the test call status command . |
|---|---|

| Field (listed alphabetically) | Description |
|---|---|
| Called # | Called number. No "*" before the number denotes an originating call leg. Two of the call legs in the example constitute one locally switched
                                                call and one network call, so the call legs refer to two active calls. A "*" before the number denotes a destination call leg (for example, this number was called with Called #). |
| CallID | This hexadecimal number used for further query is the monotonically increasing number that call control maintains for each
                                          call leg (ccCallID_t). |
| ccVdb | Value that is displayed in many other debugs to identify these call legs. |
| CID | Conglomerate value derived from the GUID that appears in the show call active brief command. |
| Codec | Codec. |
| Dial-peers | Dial peer . |
| DSP/Ch | DSP and channel allocated to this call leg. The format of these values is platform dependent (particularly the Cisco AS5300,
                                          which shows the DSP number as a 3-digit number, <VFC#><DSPM#><DSP#>). Time-slot information is also in the output for digital ports. For example, if you are using a digital port, the time slot
                                          is also returned: dsp/ch/ time slot . |
| ERL | Echo return loss (in dB). |
| ERL/Reflctr | Time difference, in ms, between the original signal and the loudest echo (peak reflector) as detected by the echo canceller. |
| Jitter | Current values of the delay and the jitter of the packets around that delay. |
| Port | V oice port. |
| Rx/Tx | Transmit and receive rates for the connection. |
| VAD | Voice-activity detection: y or n. |
| VPM STATE | Voice-port-module (VPM) state. |
| VTSP STATE | Voice-telephony-service-provider (VTSP) state. |

| Command | Description |
|---|---|
| show call active brief | Displays a summary of active call information. |
| show dial-peer voice | Displays the configuration for all VoIP and POTS dial peers configured on the router. |
| show voice dsmp stream | Displays the current session of the voice DSPM media stream. |
| show voice dsp | Displays the current status of all DSP voice channels. |
| show voice port | Displays configuration information about a specific voice port. |
| test call id | Manipulates the echo canceller and jitter buffer parameters in real time. |

| Note | With CSCuc53349, the show voice call rate command is replaced by the show call history stats cps command. See the show call history stats cps command for more information. |
|---|---|

| table | (Optional) Displays the voice call rate information in a tabular format. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |
| 15.3(2)T | This command was replaced by the show call history stats cps command. |
| Cisco IOS XE Release 3.9S | This command was replaced by the show call history stats cps command. |

| Field | Description |
|---|---|
| Period | Duration of 5 seconds. |
| Actual | Number of call legs created in 5 seconds. |
| Average | The average call legs created in 5 seconds. |

| Command | Description |
|---|---|
| voice call rate monitoring | Enables voice call rate monitoring. |

| category q850 | Displays error category to Q.850 cause code mapping. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| 128 | Destination address resolution failure |
| 129 | Call setup timeout |
| 178 | Internal communication error |
| 179 | External communication Error |
| 180 | Software error |
| 181 | Software resources unavailable |
| 182 | Hardware resources unavailable |
| 183 | Capability exchange failure |
| 184 | QoS error |
| 185 | RTP/RTCP receive timer expired or bearer layer failure |
| 186 | Signaling socket failure |
| 187 | Gateway or signaling interface taken out of service |
| 228 | User denied access to this service |
| 278 | Media negotiation failure due to non existing codec |

| Command | Description |
|---|---|
| error-category q850-cause | Specifies Q.850 cause code mapping |

| inbound | Displays the specified inbound voice class called-number. |
|---|---|
| outbound | Displays the specified outbound voice class called-number. |
| tag | Digits that identify this voice class called-number. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Field | Description |
|---|---|
| Called Number Inbound/Outbound | The tag for the specified inbound or outbound voice class called-number. |
| index number | The number or range of numbers for this voice class called number. |

| Command | Description |
|---|---|
| show voice class called-number-pool | Displays voice class called number pool configuration information. |

| tag | Digits that identify this voice class called-number-pool. Range is 1 to 10000. |
|---|---|
| detail | Displays idle called number and allocated called number information. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Field | Description |
|---|---|
| Called Number Pool | Tag that identifies the called number pool. |
| index | Number or range of numbers for this called number pool. |
| All called numbers are generated from table | FALSE--Numbers are not generated from called number table. TRUE--Numbers are generated from called number table. |
| No. of idle called numbers | Number of idle called numbers in the called number pool. |
| List of idle called numbers | List of idle numbers in the called number pool. |
| No. of alloc requests | Number of requests for numbers from the called number pool. |
| Ref Id Alloc PC Size | Reference ID for a specific list of allocated numbers. |
| List of alloc called numbers | List of first four allocated numbers from the called number pool. |

| Command | Description |
|---|---|
| show voice class called-number | Displays a specific voice class called-number. |

| summary | (Optional) Displays the summary information of the configuration. |
|---|---|
| tag | (Optional) Displays the status and content of E.164 pattern maps. |

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| destination e164-pattern-map | Links a destination E.164 pattern map to a dial peer. |
| url | Specifies the URL of a text file that has E.164 patterns configured on an E.164 pattern map. |

| tag | Displays the status and content of the voice class E.164 translation table. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice class e164-pattern-map | Displays status of a map and all E.164 patterns in the map. |

| file-buffer | (Optional) Shows the summary of phone proxy file buffer function working status. |
|---|---|
| detail | (Optional) Shows the details of phone proxy file buffer. |
| sessions | (Optional) Shows the phone proxy instance mapping status between phone and dial peer signal-address and protocol status. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |
| IOS XE Fuji Release 16.8.1 | This command was modified. The command was enhanced to display phone proxy file buffer details. |

| tag | Unique tag for the resource group. |
|---|---|
| all | Displays information for all voice resource groups. |

| Release | Modification |
|---|---|
| 15.1(2)T | This command was introduced. |

| Field | Description |
|---|---|
| Resource Index | Unique index value to identify the resource group. |
| Resource Type | Type of the resource being monitored. |
| Status | Status of the resource. |
| Subtype | Subtype of the resource being monitored. |
| Report Interval | Periodic reporting interval for the resource being monitored. The status of the resource being monitored is reported based
                                          on the preconfigured timer value. |

| Command | Description |
|---|---|
| debug rai | Enables debugging for Resource Allocation Indication (RAI). |
| rai target | Configures the SIP RAI mechanism. |
| resource (voice) | Configures parameters for monitoring resources, use the resource command in voice-class configuration mode. |
| periodic-report interval | Configures periodic reporting parameters for gateway resource entities. |
| voice class resource-group | Enters voice-class configuration mode and assigns an identification tag number for a resource group. |

| server-group-id | Unique server group ID to identify the server group. |
|---|---|
| dialpeer dialpeer-tag | Unique number of a dialpeer that is associated with a server group. |

| Release | Modification |
|---|---|
| Cisco IOS XE Release 3.11S 15.4(1)T | The following commands were introduced or modified: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) . |
| Cisco IOS XE Bengaluru 17.4.1a | The following command is introduced under voice class server-group . huntstop rule-tag resp-code from_resp_code to to_resp_code . |

| Field | Description |
|---|---|
| description | Description of the server group. |
| ipv4 port preference | A server IPv4 address as a part of this server group along with an optional port number and preference order. |
| ipv6 port preference | A server IPv6 address as a part of this server group along with an optional port number and preference order. |
| hunt-scheme | A hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this server
                                          group) for the setting up of outgoing calls. |
| hunt-stop | Stops hunting based on (configurable) response codes in the Server Group along with dial-peer. |

| Command | Description |
|---|---|
| voice class server-group | Enters voice-class configuration mode and configures server groups (groups of IPv4 and IPv6 addresses), description, hunt-scheme,
                                          huntstop, and shutdown (Server Group). |

| global | Displays information on voice class sip-options-keepalive global. |
|---|---|
| profile-tag | The unique tag for SIP options keepalive profile. Range: 1–10000. |

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| voice-class sip options-keepalive | Monitors connectivity between CUBE VoIP dial-peers and SIP servers. This command also configures OOD ping mechanism between
                                          any number of destinations. |
|---|---|

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| tag | (Optional) Specific URI voice class for which to display detailed information. |
|---|---|
| summary | (Optional) Displays a short summary of all URI voice classes. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| 15.1(2)T | This command was modified. The command was enhanced to display the mutiple hosts in the configured URI classes. |

| Field | Description |
|---|---|
| Class Name | Tag that identifies the URI voice class. |
| Schema | Whether the voice class is used for SIP or TEL URIs. |
| pattern | Pattern used to match the entire SIP or TEL URI as configured with the pattern command. |
| user-id | Pattern used to match the user-id field in the SIP URI as configured with the user-id command. |
| host | Pattern used to match the host field in the SIP URI with the host command. |
| phone number | Pattern used to match the phone number field in a TEL URI as configured with the phone number command. |
| phone context | Pattern used to match the phone context field in a SIP or TEL URI as configured with the phone context command. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| show dialplan incall uri | Displays which dial peer is matched for a specific URI in an incoming call. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |

| ccapi | Displays all the CCAPI calls. |
|---|---|
| ccCallEntry | Displays the call entry. |
| call-id | Call identifier (ID) in the range 1 to 4294967295. |
| all | Displays all the call entries. |
| ccCallInfo | Displays the call information. |
| vtsp | Displays all the VTSP calls. |
| vtsp_cdb | Displays all the VTSP call control back calls. |
| vtsp_sdb | Displays all the VTSP signalling data block calls. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced in a release earlier than Cisco IOS Release 12.4(22)T. |

| Field | Description |
|---|---|
| CallEntry | Displays the call entry identification number used for the incoming call leg. |
| CallID | Displays the specified call identifier value. |
| element | Indicates the various configuration values for the service element. |
| callInfo | Displays the call informaton. |
| call_decode | Displays the status of the audio decoder. |
| redirect_info | Displays the forwarding request information when a call is being forwarded. |
| transfer_info | Displays the call transfer request information. |
| disconnect_timer | Displays the timeout value, in seconds, specified to disconnect the call. |
| inter_digit_timer | Displays the maximum allowable time, in seconds, between digits dialed by the user. |

| Command | Description |
|---|---|
| debug voip ccapi error | Traces error logs in the call control API. |

| dnis - map - name | (Optional) Name of a specific DNIS map. |
|---|---|
| summary | (Optional) Displays a short summary of each DNIS map. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660. |

| Field | Description |
|---|---|
| Dnis-map | Name of a DNIS map that is configured on the gateway. |
| DNIS | Destination telephone number specified in this DNIS map. |
| URL | Location of the VoiceXML document to invoke for this DNIS number. |

| Field | Description |
|---|---|
| dnis-map | Names of the DNIS maps that are configured on the gateway. |
| Entries | Number of entries in DNIS maps that reside on the gateway. This field displays 0 if the DNIS map is a text file stored on
                                          an external server. |
| URL | Location of externally stored DNIS maps. |

| Command | Description |
|---|---|
| dnis | Adds a DNIS number to a DNIS map. |
| dnis - map | Associates a DNIS map to a dial peer. |
| voice dnis - map | Enters DNIS map configuration mode to create a DNIS map. |
| voice dnis - map load | Reloads a DNIS map that has changed since the previous load. |

| stream ID | DSMP media stream identifier. Range: 1 to 4294967295. |
|---|---|
| leg | Call leg corresponding to a caller ID. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Field | Description |
|---|---|
| Stream information | Shows stream ID. |
| Type | Type of stream. |
| Direction | Direction of stream. |
| Fax/Modem Type | Type of fax or modem. |
| Xmit Function | Transmit function in use. |
| Call ID | Caller ID of call leg. |
| Conference ID | Conference ID. |
| Session information | Information about the associated session. |
| connections | Number of stream connections. |
| streams | Number of streams. |
| current state | Current state and container of the session. |
| State Transitions | State transitions of the associated session. |
| DSP Encap | Encapsulation associated with the session. |
| Codec Mask | Codec mask associated with the session. |
| Fax Rate Mask | Fax rates associated with the session. |
| Fax Bytes | Fax bytes associated with the session. |
| VAD Mask | VAD mask associated with the session. |

| Command | Description |
|---|---|
| show call active voice | Displays call information for voice calls in progress. |
| show voice call | Displays the call status for voice ports on the Cisco router. |

| active | (Optional) Displays the active channels. |
|---|---|
| slot slot-number [ slot-number ] | (Optional) Specifies either a single slot or the first slot in a range. To specify a range of slots, enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All the slots in the range are affected by the command. |
| capabilities | (Optional)  Displays DSP capabilities. |
| dsp dsp-number | (Optional) Specifies the DSP on the slot. |
| cpu-load | (Optional)  Displays DSP CPU load. |
| reset | (Optional) Resets DSP CPU statistics. |
| crash-dump | (Optional) Displays the DSP crash dump status. Note To enable a DSP crash dump, set the file limit to a non-zero number, and set the destination to a valid file name. | Note | To enable a DSP crash dump, set the file limit to a non-zero number, and set the destination to a valid file name. |
| Note | To enable a DSP crash dump, set the file limit to a non-zero number, and set the destination to a valid file name. |
| detailed | (Optional)  Displays detailed information about DSP status. |
| error | (Optional)  Displays DSP errors. |
| group | (Optional)  Displays DSP group information. |
| all | (Optional) Displays all the DSP group details. |
| sorted-list | (Optional)  Displays a DSP-sorted list. |
| signaling | (Optional)  Displays DSP signaling channel usage. |
| voice | (Optional)  Displays DSP voice channel usage. |
| version | (Optional)  Displays the DSP firmware version. |
| slot | (Optional) The first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument.
                                          The second slot specifies the end of the range. All the slots in the range are affected by the command. |
| / dsp | (Optional) The first DSP in a range. To specify a range of DSPs, you can enter a  second DSP in the syntax of this argument.
                                          The second DSP specifies the end of the range. All the DSPs in the range are affected by the command. The slash mark is required. |

| Note | To enable a DSP crash dump, set the file limit to a non-zero number, and set the destination to a valid file name. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE 17.18.2 | This command was implemented on the C8375-E-G2 secure router. |
| Cisco IOS XE Release 3.3.0S | The show voice dsp group all command output was modified for SPA-DSP on the Cisco ASR 1000 Series Router. |
| Cisco IOS XE Release 3.2S | This command was implemented on the Cisco ASR 1000 Series Router. |
| Cisco IOS XE Release 2.5 | This command was integrated into Cisco IOS XE Release 2.5. |
| 12.4(11)T | The command was modified. Command output was enhanced to display information about the DSP H.320 channels. |
| 12.4(4)XC | The command was modified. The version keyword was added and the command was implemented on the Cisco AS5350XM and Cisco AS5400XM platforms. |
| 12.4(4)T | The command was modified. The command output was enhanced to display the codec setting for modem relay operation. |
| 12.3(14)T | The command was modified. The command output was enhanced to display status information pertaining to the NM-HDV network
                                          module TI-549 DSPs. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 Series and Cisco 3600 Series, and the display format was modified. |
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |

| Field | Description |
|---|---|
| DSP | Number of the DSP. |
| channel | Number of the channel and its status. |
| DSP TYPE | TI-549 (C549) DSP. |
| DSP NUM | Number of the DSP. |
| CH | Channel number. |
| CODEC | Complexity setting. |
| DSPWARE VERSION | Version of DSPware. |
| CURR STATE | Current status of the channel: alloc (allocated), busy, or idle. |
| BOOT STATE | DSP readiness, either idle or in service. |
| RST | Number of times the DSP has been reset or restarted. |
| AI | Alarm indication count on the channel. |
| VOICEPORT | Voice card number and slot. |
| TS | Time slot. |
| PAK ABORT | Number of dropped packets. |
| TX/RX PACK COUNT | Number of transmitted and received packets. |

| Note | The crash dump details must be enabled to display the crash dump for a SPA-DSP. To enable a crash dump, set the destination
                                          of the crash dump file to a valid file name, and set the file limit to a non-zero number. |
|---|---|

| Command | Description |
|---|---|
| dsp services dspfarm | Enables the DSP farm services. |
| dspfarm profile | Enters the DSP farm profile configuration mode and defines a profile for DSP farm services. |
| show dspfarm | Displays DSP farm service information, such as operational status, and DSP resource allocation for transcoding. |

| operational-status | Displays the operational state for active sessions on a specific channel or range of channels. |
|---|---|
| slot | A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command. |
| / dsp | A single DSP on the slot or the first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected by the command. The slash mark is required. |
| / channel | A single DSP channel or the first DSP channel in a range. The second occurrence of this argument specifies either a single DSP channel or the last DSP channel in a range. The slash mark is required. |
| statistics | Displays DSP statistics for a specific channel or range of channels. |
| slot-number | A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command. |
| traffic | Displays traffic on a specific channel or range of channels. |

| Release | Modification |
|---|---|
| 12.4(4)XC | The command was introduced on the Cisco AS5350XM and Cisco AS5400XM platforms. |
| 12.4(11)T | The command was modified. Command output was enhanced to display information about DSP H.320 channels. |

| Field | Description |
|---|---|
| DSP | Number of the DSP. |
| Channel | Number of the channel and its status. |
| Codec Type | Complexity setting. |
| TxVoiceDuration | Transmitted voice duration. |

| Command | Description |
|---|---|
| show voice dsp | Displays the current status or selective statistics of DSP voice channels,. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| debug voice dsp crash-dump | Displays crash dump debug information. |
| voice dsp crash-dump | Enables the crash dump feature and specifies the destination file and the file limit. |

| slot | (Optional) A single slot or the first slot in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected by the command. |
|---|---|
| / dsp | (Optional) A single DSP on the slot or the first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected by the command. The slash mark is required. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. The command was implemented on the Cisco AS5350XM and Cisco AS5400XM platforms. |
| 12.4(11)T | The command was modified. Command output was enhanced to display information about DSP H.320 channels. |
| 12.4(19) | The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls. |
| 12.4(18a) | The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls. |
| 12.4(13f) | The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls. |
| 12.4(15)T5 | The command was modified. Command output was modified to accurately show the "Codectype" as "voice" rather than "fax" for
                                          T.38 calls. |

| Field | Description |
|---|---|
| DSP | Number of the DSP. |
| Codectype | Complexity setting. |
| Channels | Number of the channel and its status. |
| State | Status of the calls. |

| Command | Description |
|---|---|
| show voice dsp | Displays the current status or selective statistics of DSP voice channels,. |

| all | All neighbors |
|---|---|
| prefix_number | (Optional) Specified EDDRI prefix. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| debug voip eddri | Turns on debugging for the EDDRI. |

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| voice emergency response | Configures emergency response location, zone, and settings for E911 services. |
|---|---|

| table - number | (Optional) ENUM match table to display, by number. Range is from 1 to 15. |
|---|---|
| sort | (Optional) Sorts the output by ascending table number. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (ENUM configuration) | Defines the ENUM rule. |
| test enum | Tests the ENUM rule. |
| voice enum-match-table | Initiates the voice ENUM match table definition. |

| Release | Modification |
|---|---|
| 12.2(10) | This command was introduced. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Caution | Using the message logger feature in a production network environment increases CPU and memory usage on the gateway. |
|---|---|

| Note | If you are experiencing problems with certain voice calls, the engineering team at Cisco might ask you to capture the control
                                          messages using the voice DSP logger. You can capture these messages by turning on the logger, repeating the problematic calls,
                                          and capturing the logs. Only Cisco engineers can determine if you should send the logs in for further review. |
|---|---|

| Command | Description |
|---|---|
| debug hpi | Enables debugging for HPI message events. |
| voice hpi capture | Allocates the Host Port Interface (HPI) capture buffer (size in bytes) and sets up or changes the destination URL for captured
                                          data. |

| string | Six-part dotted decimal string that displays the definition of an internal error code. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| IEC version | IEC version. A value of 1 indicates the Cisco IOS Release 12.3(4)T version. |
| Entity | Network physical entity (hardware system) that generated the IEC. The value 1 is assigned to the gateway. |
| Category | Error category, defined in terms of ITU-based Q.850 cause codes and VoIP network errors. |
| Subsystem | Specific subsystem within the physical entity where the IEC was generated. |
| Error Code | Error code within the subsystem. |
| Diagnostic Code | Cisco internal diagnostic value. Report this value to Cisco Technical Support. |

| Command | Description |
|---|---|
| show voice statistics iec | Displays IEC statistics. |

| slot/subunit/port | (Optional) Voice port that you specify with the slot / subunit / port designation. slot specifies a router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform. subunit specifies a voice interface card (VIC) in which the voice port is located. Valid entries are 0 and 1. port specifies an analog voice port number. Valid entries are 0 and 1. The slash marks are required. |
|---|---|
| slot/port : ds0 - group | (Optional) Voice port that you specify with the slot / port : ds0 - group designation. slot specifies a router slot in which the packet voice NM is installed. Valid entries are router slot numbers for the particular
                                                platform. port specifies a T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1. ds0 - group specifies a T1 or E1 logical port number. T1 range is from 0 to 23. E1 range is from 0 to 30. The colon is required. |
| details | (Optional) Displays more information. If this keyword is omitted, less information is displayed. |
| timing | (Optional) Displays the timing configuration for all LMR ports. |
| warnings | (Optional) Displays all LMR ports that are having suspicious timing configuration. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.4(24)T | This command was modified in a release earlier than Cisco IOS Release 12.4(24)T. The timing and warnings keywords were added. |

| Field | Description |
|---|---|
| Connection type | Type of connection between LMR routers: private line, automatic ringdown (PLAR), trunk, or n/a |
| Out Attenuation | Output attenuation. |
| In Gain | Input gain. |
| E-lead capability | Active or inactive. |
| polarity | Polarity of the E&M voice port: normal or reverse. |
| M-lead capability | Active or inactive. |
| voice class tone-signal | Name of the tone-signal voice class. |
| state= | Signaling state. |
| e-lead = | On or off. |
| m-lead = | On or off. |
| full duplex | Voice path for the voice port is operating in full duplex mode. |
| half duplex | Voice path for the voice port is operating in half duplex mode. |
| voice path | Transmit or receive. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| ReceivePackets | Number of packets received by this peer during this call. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| NoiseLevel | Active noise level for this call. |
| ACOMLevel | Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceller, which is the sum of the Echo
                                          Return Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call. |
| OutSignalLevel | Active output signal level to the telephony interface used by this call. |
| InSignalLevel | Active input signal level from the telephony interface used by this call. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| Remote SignallingIPAddress, Port | Call control server IP address and signaling port number. |
| Remote MediaIPAddress, Port | Remote side media server IP address and RTP port number. |
| RoundTripDelay | Voice packet round trip delay between the local and remote systems on the IP backbone for this call. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| VAD | Whether voice activation detection (VAD) is enabled. |
| Description | Description of what the port is connected to. |
| Timing hangover | Number of milliseconds of delay before the digital signal processor (DSP) tells Cisco IOS software to turn off the E-lead
                                          after the DSP detects that the voice stream has stopped. |
| Timing hookflash-in | Maximum duration of a hookflash for a Foreign Exchange Station (FXS) interface. |
| Timing delay-voice | Delay before a voice packet is played out. |
| Music On Hold Threshold | Decibel level of music played when calls are put on hold. |
| Noise Threshold | Noise threshold for incoming calls. |
| E&M type | E&M signaling type. |
| Operation | 2-wire or 4-wire operation. |
| Impedance | Terminating impedance of the interface. |
| lmr tear down timeout | Time for which the voice port waits before tearing down an LMR connection after detecting no voice activity. |
| lmr PTT transmit timeout | Maximum time for transmitting a voice packet. |
| lmr PTT receive timeout | Maximum time for receiving a voice packet. |
| inject pause | Pause injected before the voice packet is played out. |
| inject tone | Tone injected before the voice packet is played out. |
| inject guard-tone | Guard tone played out with the voice packet. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerSubAddress | Subaddress when this call is connected. |
| PeerId | ID value of the peer table entry to which this call was made. |
| SessionTarget | Network-specific address to receive calls from the dial peer. |
| SelectedQoS | Selected RSVP quality of service (QoS) for this call. |
| ProtocolCallId | Voice signaling specific call ID. |

| Command | Description |
|---|---|
| show call active voice | Displays call information for voice calls in progress. |
| show voice port | Displays configuration information about a specific voice port. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice pcm capture | Allocates the number of Pulse Code Modulation (PCM) capture buffers, sets up or changes the destination URL for captured
                                          data, enables PCM capture on-demand, and changes the PCM capture trigger string by the user. |

| Cisco 1750 Router |
|---|
| slot | Slot number in the router in which the VIC is installed. Valid entries are 0, 1, and 2, depending on the slot in which it
                                          is installed. |
| / port | Voice port. Valid entries are 0 and 1. The slash mark is required. |
| Cisco 2600 and Cisco 3600 Series Router with Analog Voice Ports |
| slot / subunit / port | (Optional) The analog voice port designation: slot -- Router slot in which a voice network module (VNM) is installed. Valid entries are router slot numbers for the particular platform. subunit --Voice Interface Card (VIC) in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network
                                                module.) The slash mark is required. port-- Analog voice port number. Valid entries are 0 and 1. The slash mark is required. |
| summary | (Optional) Displays a summary of all voice ports. |
| Cisco 2600 and Cisco 3600 Series Router with Digital Voice Ports |
| slot / port : ds0 - group | (Optional) Specifies the digital voice port designation: slot-- Router slot in which the packet voice trunk network module (NM) is installed. Valid entries are router slot numbers for the
                                                particular platform. / port-- T1 or E1 physical port in the voice WAN interface card (VWIC). Valid entries are 0 and 1. (One VWIC fits in an NM.) The slash
                                                mark is required. : ds0 - group-- T1 or E1 logical port number. T1 range is 0 to 23. E1 range is 0 to 30. The colon is required. |
| summary | (Optional) Displays a summary of all voice ports. |
| Cisco AS5300 Universal Access Server |
| controller - number | T1 or E1 controller. |
| :D | D channel that is associated with the ISDN PRI. The colon is required. |
| Cisco 7200 Series Router |
| slot | Router location where the voice port adapter is installed. Range is 0 to 3. |
| / port | Voice interface card location. Valid entries are 0 and 1. The slash mark is required. |
| : ds0-group-number | Defined DS0 group number. Because each defined DS0 group number is represented on a separate voice port, you can define individual
                                          DS0s on the digital T1/E1 card. The colon is required. |
| slot | Slot number in the Cisco router where the VIC is installed. Range is 0 to 3, depending on the slot where it is installed. |
| / subunit | Subunit on the VIC where the voice port is located. Valid entries are 0 and 1. The slash mark is required. |
| / port | Voice port number. Valid entries are 0 and 1. The slash mark is required. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This command was modified. Port-specific values for the Cisco MC3810 were added. |
| 12.0(3)T | This command was modified. Port-specific values for the Cisco MC3810 were added. |
| 12.0(5)XK | This command was modified. The ds0-group argument was added for the Cisco 2600 series and Cisco 3600 series. |
| 12.0(5)XE | This command was modified. Additional syntax was created for digital voice to allow specification of the DS0 group. This
                                          command applies to VoIP on the Cisco 7200 series. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |
| 12.0(7)XK | This command was modified. The summary keyword was added for the Cisco 2600 series and Cisco 3600 series. The ds0-group argument was added for the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(8)T | This command was modified. This command was implemented for direct inward dial (DID) on the Cisco IAD2420 series. |
| 12.2(2)XN | This command was modified. Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was
                                          added to Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco Gateway 200 (Cisco VG200). |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. It was implemented on the
                                          Cisco IAD2420 series. |
| 12.4(11)T | This command was modified. This command was enhanced to display voice class called-number-pool configuration information
                                          for the voice port. |
| 12.4(12) | This command was modified. This command was integrated into Cisco IOS Release 12.4(12) and output was modified to display
                                          the parameter set by the timing sup-disconnect command. |
| 15.0(1)XA | This command was modified. The output was enhanced to display the logical partitioning class of restriction (LPCOR) policy
                                          for incoming and outgoing calls. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(3)T | This command was modified. The output of this command was enhanced to display the connection status of foreign exchange office
                                          (FXO) ports. |

| Note | This command is not supported on Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 platforms for Non-Facility Associated
                                          Signaling (NFAS) configuration. |
|---|---|

| Note | If the FXO port 0/2/0 is disconnected, the output of the show voice port summary command changes so that the OUT STATUS is reported as "off-hook," and the OPER state changes to "down." |
|---|---|

| Note | If the FXO port 0/2/0 is disconnected, the output of the show voice port command changes so that the Administrative State remains "UP" but the Operation State is "DOWN." Beginning in Cisco IOS Release
                                          15.1(3)T, there is improved status monitoring of FXO ports--any time an FXO port is connected or disconnected, a message is
                                          displayed to indicate the status change. For example, the following message is displayed to report that a cable has been connected,
                                          and the status is changed to "up" for FXO port 0/2/0: 000118: Jul 14 18:06:05.122 EST: %LINK-3-UPDOWN: Interface Foreign Exchange
                                          Office 0/2/0, changed state to operational status up due to cable reconnection |
|---|---|

| Field | Description |
|---|---|
| Administrative State | Administrative state of the voice port. |
| Alias | User-supplied alias for the voice port. |
| Clear Wait Duration Timing | Time (in milliseconds [ms]) of inactive seizure signal to declare call cleared. |
| Companding Type | Companding standard used to convert between analog and digital signals in pulse code modulation (PCM) systems. |
| Connection Mode | Connection mode of the interface. |
| Connection Number | Full E.164 telephone number used to establish a connection with the trunk or private line automatic ringdown (PLAR) mode. |
| Currently Processing | Type of call currently being processed: none, voice, or fax. |
| Delay Duration Timing | Maximum delay signal duration (in ms) for delay dial signaling. |
| Delay Start Timing | Timing (in ms) of generation of delayed start signal from detection of incoming seizure. |
| Dial Type | Out-dialing type of the voice port. |
| Digit Duration Timing | Dual-tone multifrequency (DTMF) digit duration (in ms). |
| E&M Type | Type of E&M interface. |
| Echo Cancel Coverage | Echo cancel coverage for this port. |
| Echo Cancellation | Whether echo cancellation is enabled for this port. |
| Impedance | Configured terminating impedance for the E&M interface. |
| In Gain | Amount of gain (in decibels [dB]) inserted at the receiver side of the interface. |
| In Seizure | Incoming seizure state of the E&M interface. |
| Initial Time Out | Amount of time (in seconds) the system waits for an initial input digit from the caller. |
| Interdigit Duration Timing | DTMF interdigit duration (in seconds). |
| InterDigit Pulse Duration Timing | Pulse dialing interdigit timing (in ms). |
| Interdigit Time Out | Amount of time (in seconds) the system waits for a subsequent input digit from the caller. |
| Lpcor (Incoming) | Setting of the lpcor incoming command. |
| Lpcor (Outgoing) | Setting of the lpcor outgoing command. |
| Maintenance Mode | Maintenance mode of the voice port. |
| Music On Hold Threshold | Configured music-on-hold threshold value for this interface. |
| Noise Regeneration | Whether background noise should be played to fill silent gaps if voice activity detection (VAD) is activated. |
| Non Linear Processing | Whether nonlinear processing is enabled for this port. |
| Number of signaling protocol errors | Number of signaling protocol errors. |
| Operation State | Operational state of the voice port. |
| Operation Type | Operation type of the E&M signal: 2-wire or 4-wire. |
| Out Attenuation | Amount of attenuation (in dB) inserted at the transmit side of the interface. |
| Out Seizure | Outgoing seizure state of the E&M interface. |
| Port | Port number for the interface associated with the voice interface card. |
| Pulse Rate Timing | Pulse dialing rate, in pulses per second (pps). |
| Region Tone | Configured regional tone for this interface. |
| Ring Active Status | Ring active indication. |
| Ring Cadence | Configured ring cadence for this interface. |
| Ring Frequency | Configured ring frequency (in hertz) for this interface. |
| Ring Ground Status | Ring ground indication. |
| Ringing Time Out | Ringing timeout duration (in seconds). |
| Signal Type | Type of signaling for a voice port: delay-dial, ground-start, immediate, loop-start, and wink-start. |
| Slot | Slot used in the voice interface card for this port. |
| Sub-unit | Subunit used in the voice interface card for this port. |
| Tip Ground Status | Tip ground indication. |
| Type of VoicePort | Type of voice port: FXO, FXS, or E&M. |
| The Interface Down Failure Cause | Text string describing why the interface is down, |
| Wait Release Time Out | Length of time (in seconds) that a voice port stays in call-failure state while a busy tone, reorder tone, or out-of-service
                                          tone is sent to the port. |
| Wink Duration Timing | Maximum wink duration (in ms) for wink-start signaling. |
| Wink Wait Duration Timing | Maximum wink wait duration (in ms) for wink-start signaling. |

| Command | Description |
|---|---|
| ds0 group | Specifies the DS0 time slots that make up a logical voice port on a T1 or E1 controller and specifies the signaling type
                                          by which the router communicates with the PBX or PSTN. |
| timing sup-disconnect | Defines the minimum time to ensure that an on-hook indication is intentional and not an electrical transient on the line
                                          before a supervisory disconnect occurs (based on power denial signaled by the PSTN or PBX). |

| stats | Displays license usage over time. |
|---|---|
| table | (Optional) Displays license usage over time in tabular format. |
| status | Displays license status. |

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.2.1r | This command was introduced. |
| Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a | This command was modified to support Cisco Smart Licensing Using Policy. |
| Cisco IOS XE Bengaluru 17.6.1a | This command was modified to display licensing information for WebSockets in CUBE. |

| name | (Optional) Name of the source IP group to display. |
|---|---|
| sort [ ascending \| descending | (Optional) Displays the source IP groups in either ascending or descending alphanumerical order. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Field | Description |
|---|---|
| Source Group | Name of the voice source IP group. |
| description | Description of the voice source IP group. |
| carrier-id source | Name of the source carrier ID used by the terminating gateway to select a target carrier. |
| carrier-id target | Name of the target carrier ID used by the terminating gateway to select a dial peer for routing the call over a POTS line. |
| trunk-group-label source | Name of the source trunk group used by the originating gateway to route the call over an inbound dial peer. |
| trunk-group-label target | Name of the target trunk group used by the terminating gateway to select a dial peer for routing an outbound call over a
                                          POTS line. |
| h323zone-id | Name of the zone associated with incoming H.323 calls to the voice source IP group. |
| access-list | Number of the access list used by the voice source IP group to block calls. |
| disconnect-cause | Phrase returned by the voice source IP group when a call is blocked. |
| translation-profile | Name of the translation profile used by the voice source IP group to translate calls. |

| Command | Description |
|---|---|
| voice source-group | Initiates a voice source IP group definition. |

| tag-number | Interval that represents a specified time range. The valid range is from 1 to 36655. Note You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. | Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
|---|---|---|---|
| Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
| all | Displays all voice accounting statistics. |
| method-list-name method-list-name | Displays accounting statistics by method list. You must specify a method-list name. |
| push | (Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows: all--Pushes statistics to both the FTP and syslog servers. ftp--Pushes statistics to the FTP server. syslog--Pushes statistics to the syslog server. |

| Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Client Type | The type of statistics collected. |
| Start Time | The start time of the statistics collection. |
| End Time | The ending time of the statistics collection. |
| method-list | The method list name. |
| acc_pass_criteria | Accounting pass criteria: 1: all start/interim/stop messages passed. 2: all start/stop messages passed. 3: stop-only message passed. |
| pstn_in_pass | Number of incoming calls on the PSTN leg that meet acc_pass_criteria. |
| pstn_in_fail | Number of incoming calls on the PSTN leg that fail acc_pass_criteria. |
| pstn_out_pass | Number of outgoing calls on the PSTN leg that meet acc_pass_criteria. |
| pstn_out_fail | Number of outgoing calls on the PSTN leg that fail acc_pass_criteria. |
| ip_in_pass | Number of incoming calls on the IP leg that meet acc_pass_criteria. |
| ip_in_fail | Number of incoming calls on the IP leg that fail acc_pass_criteria. |
| ip_out_pass | Number of outgoing calls on the IP leg that meet acc_pass_criteria. |
| ip_out_fail | Number of outgoing calls on the IP leg that fail acc_pass_criteria. |

| Command | Description |
|---|---|
| show event-manager consumers | Displays event-manager statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics csr since-reset all | Displays all CSRs since the last reset. |
| show voice statistics interval-tag | Displays the configured interval numbers. |
| show voice statistics memory-usage | Displays current memory usage. |

| tag-number | Interval that represents a specified time range. The valid range is from 1 to 36655. Note You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. | Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
|---|---|---|---|
| Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
| all | Displays all levels of signaling statistics. |
| gateway | Displays gateway-wide level statistics. |
| ip | Displays VoIP interface level statistics. |
| pstn | Displays telephone interface level statistics. |
| trunk-group | Displays trunk-group level statistics. trunk-group-label --displays statistics for a specific trunk group all --Displays statistics for all trunk groups. |
| voice-port | Displays voice-port level statistics: voice-port-label --displays statistics for a specific voice port all --Displays statistics for all voice ports. |
| mode | (Optional) Statistics are displayed in a specified mode. The keywords are as follows: concise--Displays output that contains total calls, answered calls, and answered call duration. verbose--Displays all fields contained in call statistic records (CSRs). This is the default setting. |
| push | (Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows: all--Pushes statistics to both the FTP and syslog servers. ftp--Pushes statistics to the FTP server. syslog--Pushes statistics to the syslog server. |

| Note | You must first enter the show voice statistics interval-tag command to obtain the valid tag numbers that you can enter for this command. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Client Type | The type of statistics collected. |
| Start Time | The start time of the statistics collection. |
| End Time | The ending time of the statistics collection. |
| record_type | Call statistics record type. Symbols are gw, ip, pstn, tg, and vp. |
| trunk_group_id | Trunk group ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| voice_port_id | Voice port ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| in_call | Number of incoming calls. |
| in_ans | Number of incoming calls answered by the gateway. |
| in_fail | Number of incoming calls that failed. |
| out_call | Number of outgoing calls attempted. |
| out_ans | Number of outgoing calls that received answers. |
| out_fail | Number of outgoing calls that failed. |
| in_szre_d | Incoming seizure duration (in seconds). |
| out_szre_d | Outgoing seizure duration (in seconds). |
| in_conn_d | Incoming connected duration (in seconds). |
| out_conn_d | Outgoing connected duration (in seconds). |
| orig_disconn | Number of calls encountering the originating side having been disconnected before the outgoing calls were connected. |
| in_ans_abnorm | Number of incoming answered calls terminated with any cause code other than "normal". |
| out_ans_abnorm | Number of outgoing answered calls terminated with any cause code other than "normal". |
| in_mcd | Number of incoming calls lasting less than the configured minimum call duration (MCD). |
| out_mcd | Number of outgoing calls lasting less than the configured MCD. |
| in_pdd | Total post dial delay duration on incoming calls (in ms). |
| out_pdd | Total post dial delay duration on outgoing calls (in ms). |
| in_setup_delay | Total inbound setup delay duration (in ms). |
| out_setup_delay | Total outbound setup delay duration (in ms). |
| lost_pkt | Number of calls losing more than the configured number of packets. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| latency | Number of calls encountering more than the configured amount of latency. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| jitter | Number of calls encountering more than configured amount of jitter. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| in_cc_no | Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5). |
| in_disc_cc | Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal). |
| out_disc_cc | Outgoing disconnect cause code. |
| out_cc_no | Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5). |
| in_cc_id | Disconnect cause code ID for the following field for incoming calls. |
| in_cc_cntr | Disconnect cause code counter for incoming calls (any incoming cause code counter pairs). |
| out_cc_id | Disconnect cause code ID for the following field for outgoing calls. |
| out_cc_cntr | Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs). |

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Command | Description |
|---|---|
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics csr since-reset all | Displays all CSRs since the last reset. |
| show voice statistics interval-tag | Displays the configured interval numbers. |
| show voice statistics memory-usage | Displays current memory usage. |
| voice statistics time-range | Specifies the time range to collect CSRs. |

| all | All collected statistics since the last reset are displayed. |
|---|---|
| method-list method-list-name | Collected statistics by method list since the last reset are displayed. The method-list-name argument specifies the name
                                          of the method list. |
| push | (Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows: all--Pushes statistics to both the FTP and syslog servers. ftp--Pushes statistics to the FTP server. syslog--Pushes statistics to the syslog server. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Client Type | The type of statistics collected. |
| Start Time | The start time of the statistics collection. |
| End Time | The ending time of the statistics collection. |
| method-list | The method list name. |
| acc_pass_criteria | Accounting pass criteria: 1: all start/interim/stop messages passed. 2: all start/stop messages passed. 3: stop-only message passed. |
| pstn_in_pass | Number of incoming calls on the PSTN leg that meet acc_pass_criteria. |
| pstn_in_fail | Number of incoming calls on the PSTN leg that fail acc_pass_criteria. |
| pstn_out_pass | Number of outgoing calls on the PSTN leg that meet acc_pass_criteria. |
| pstn_out_fail | Number of outgoing calls on the PSTN leg that fail acc_pass_criteria. |
| ip_in_pass | Number of incoming calls on the IP leg that meet acc_pass_criteria. |
| ip_in_fail | Number of incoming calls on the IP leg that fail acc_pass_criteria. |
| ip_out_pass | Number of outgoing calls on the IP leg that meet acc_pass_criteria. |
| ip_out_fail | Number of outgoing calls on the IP leg that fail acc_pass_criteria. |

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics interval-tag | Displays the configured interval numbers |
| show voice statistics memory-usage | Displays current memory usage. |
| voice statistics time-range | Specifies a time range to collect statistics from the gateway on a periodic basis, since the last reset, or for a specific
                                          time duration. |

| all | All signaling statistics. |
|---|---|
| gateway | Gateway-wide level statistics. |
| ip | VoIP-interface-level statistics. |
| pstn | PSTN-level statistics. |
| trunk-group | Trunk-group-level statistics. Keywords and arguments are as follows. all --Statistics for all trunk groups. trunk-group-label --Statistics for a specific trunk group. |
| voice-port | Voice-port-level statistics. Keywords and arguments are as follows: all --Statistics for all voice ports. voice-port-label --Statistics for a specific voice port. |
| mode | (Optional) Statistics in a specified mode. Keywords are as follows: concise--Output contains total calls, answered calls, and answered call duration. verbose--All fields contained in call statistic records (CSRs). This is the default. |
| push | (Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. Keywords are as follows: all--Pushes statistics to both the FTP and syslog servers. ftp--Pushes statistics to the FTP server. syslog--Pushes statistics to the syslog server. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Client Type | The type of statistics collected. |
| Start Time | The start time of the statistics collection. |
| End Time | The ending time of the statistics collection. |
| record_type | Call statistics record type. Symbols are gw, ip, pstn, tg, and vp. |
| trunk_group_id | Trunk group ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| voice_port_id | Voice port ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| in_call | Number of incoming calls. |
| in_ans | Number of incoming calls answered by the gateway. |
| in_fail | Number of incoming calls that failed. |
| out_call | Number of outgoing calls attempted. |
| out_ans | Number of outgoing calls that received answers. |
| out_fail | Number of outgoing calls that failed. |
| in_szre_d | Incoming seizure duration (in seconds). |
| out_szre_d | Outgoing seizure duration (in seconds). |
| in_conn_d | Incoming connected duration (in seconds). |
| out_conn_d | Outgoing connected duration (in seconds). |
| orig_disconn | Number of calls encountering the originating side having been disconnected before the outgoing calls were connected. |
| in_ans_abnorm | Number of incoming answered calls terminated with any cause code other than "normal". |
| out_ans_abnorm | Number of outgoing answered calls terminated with any cause code other than "normal". |
| in_mcd | Number of incoming calls lasting less than the configured minimum call duration (MCD). |
| out_mcd | Number of outgoing calls lasting less than the configured MCD. |
| in_pdd | Total post dial delay duration on incoming calls (in ms). |
| out_pdd | Total post dial delay duration on outgoing calls (in ms). |
| in_setup_delay | Total inbound setup delay duration (in ms). |
| out_setup_delay | Total outbound setup delay duration (in ms). |
| lost_pkt | Number of calls losing more than the configured number of packets. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| latency | Number of calls encountering more than the configured amount of latency. Note This field will exist only in "IP" records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in "IP" records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in "IP" records. In other types of records, this field will be empty and extra commas are expected. |
| jitter | Number of calls encountering more than configured amount of jitter. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| in_disc_cc | Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal). |
| out_disc_cc | Outgoing disconnect cause code. |
| in_cc_no | Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5). |
| out_cc_no | Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5). |
| in_cc_id | Disconnect cause code ID for the following field for incoming calls. |
| in_cc_cntr | Disconnect cause code counter for incoming calls (any incoming cause code counter pairs). |
| out_cc_id | Disconnect cause code ID for the following field for outgoing calls. |
| out_cc_cntr | Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs). |

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in "IP" records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| clear voice statistics csr | Clears voice-statistic collection settings on the gateway. |
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics interval-tag | Displays voice statistics within a specified interval. |
| show voice statistics memory-usage | Displays current memory usage. |
| voice statistics time-range | Specifies the time range to collect CSRs. |

| mode | (Optional) Statistics are displayed in a specified mode. The keywords are as follows: concise--Displays output that contains total calls, answered calls, and answered call duration. verbose--Displays all fields contained in call statistic records (CSRs). This is the default setting. |
|---|---|
| push | (Optional) Statistics are downloaded to an FTP or syslog server, or to both servers. The keywords are as follows: all--Pushes statistics to both the FTP and syslog servers. ftp--Pushes statistics to the FTP server. syslog--Pushes statistics to the syslog server. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Client Type | The type of statistics collected. |
| Start Time | The start time of the statistics collection. |
| End Time | The ending time of the statistics collection. |
| record_type | Call statistics record type. Symbols are gw, ip, pstn, tg, and vp. |
| trunk_group_id | Trunk group ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| voice_port_id | Voice port ID. Note For the symbols gw, ip, pstn, and some vp records, this field is empty. | Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
| in_call | Number of incoming calls. |
| in_ans | Number of incoming calls answered by the gateway. |
| in_fail | Number of incoming calls that failed. |
| out_call | Number of outgoing calls attempted. |
| out_ans | Number of outgoing calls that received answers. |
| out_fail | Number of outgoing calls that failed. |
| in_szre_d | Incoming seizure duration (in seconds). |
| out_szre_d | Outgoing seizure duration (in seconds). |
| in_conn_d | Incoming connected duration (in seconds). |
| out_conn_d | Outgoing connected duration (in seconds). |
| orig_disconn | Number of calls encountering the originating side having been disconnected before the outgoing calls were connected. |
| in_ans_abnorm | Number of incoming answered calls terminated with any cause code other than "normal". |
| out_ans_abnorm | Number of outgoing answered calls terminated with any cause code other than "normal". |
| in_mcd | Number of incoming calls lasting less than the configured minimum call duration (MCD). |
| out_mcd | Number of outgoing calls lasting less than the configured MCD. |
| in_pdd | Total post dial delay duration on incoming calls (in ms). |
| out_pdd | Total post dial delay duration on outgoing calls (in ms). |
| in_setup_delay | Total inbound setup delay duration (in ms). |
| out_setup_delay | Total outbound setup delay duration (in ms). |
| lost_pkt | Number of calls losing more than the configured number of packets. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| latency | Number of calls encountering more than the configured amount of latency. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| jitter | Number of calls encountering more than the configured amount of jitter. Note This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. | Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
| in_disc_cc | Incoming disconnect cause code. For example, in_disc_cc_16=3 indicates that 3 calls were disconnected or finished with a
                                          disconnect cause code of 16 (normal). |
| out_disc_cc | Outgoing disconnect cause code. |
| in_cc_no | Number of the following disconnect cause code counters as per incoming calls (expected to be fewer than 5). |
| out_cc_no | Number of the following disconnect cause code counters as per outgoing calls (expected to be fewer than 5). |
| in_cc_id | Disconnect cause code ID for the following field for incoming calls. |
| in_cc_cntr | Disconnect cause code counter for incoming calls (any incoming cause code counter pairs). |
| out_cc_id | Disconnect cause code ID for the following field for outgoing calls. |
| out_cc_cntr | Disconnect cause code counter for outgoing calls (any outgoing cause code counter pairs). |

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | For the symbols gw, ip, pstn, and some vp records, this field is empty. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Note | This field will exist only in IP records. In other types of records, this field will be empty and extra commas are expected. |
|---|---|

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics interval-tag | Displays voice statistics within a specified interval. |
| show voice statistics memory-usage | Displays current memory usage. |

| interval | Displays statistics for the specified interval. |
|---|---|
| number | The interval tag number. The range is from 1 to 36655. |
| since-reboot | Displays IEC statistics since the last reboot. |
| since-reset | Displays IEC statistics since the last reset. |
| push | Specifies the off-load pushing interface. |
| all | Indicates that IEC statistics will be off-loaded to all push interfaces. |
| ftp | Indicates that IEC statistics will be off-loaded to the FTP server. |
| syslog | Indicates that IEC statistics will be off-loaded to the syslog server. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| 12.4(24)T | This command was modified in a release earlier than Cisco IOS Release 12.4(24)T. The push all , ftp and syslog keywords were added. |

| Field | Description |
|---|---|
| SUBSYSTEM | Indicates the specific subsystem within the physical entity where the IEC was generated. |
| errcode | Identifies the error code within the subsystem. |

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| show voice statistics | Displays voice statistics. |
| show voice statistics interval-tag | Displays interval options available for IEC statistics. |
| voice statistics time-range since-reset | Enables collection of call statistics accumulated since the last resetting of IEC counters. |
| voice statistics type iec | Enables collection of IEC statistics. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Current System Time | Current system time of the gateway. |
| Interval-Tag | Interval number. |
| Intervals Start Time | Interval start time. |
| End Time | Interval end time. |

| Command | Description |
|---|---|
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics csr since-reset all | Displays all CSRs since the last reset. |
| show voice statistics memory-usage | Displays current memory usage. |

| all | Memory used to collect both signaling and accounting call statistics records (CSRs). |
|---|---|
| csr | Memory used to collect signaling CSRs only. |
| iec | Memory used to collect Cisco internal error codes (IECs) only. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Voice Call Statistics Record Memory Usage |
| Fixed Interval Option: | Statistics gathered for a fixed interval. |
| CSR size | Size of the CSR for the fixed interval. |
| Number of CSR per interval | Number of CSRs collected for the fixed interval. |
| Used memory size (proximate) | Amount of memory currently being used to store statistics. |
| Estimated future claimed memory size (proximate) | Amount of remaining memory available to store statistics. |
| Since Reset Option: | Statistics gathered since the last reset or reboot of the gateway. |
| CSR size | Size of the CSR since the last reset. |
| Total count of CSR | Total number of CSRs gathered since the last reset. |
| Used memory size (proximate) | Amount of memory currently being used to store statistics. |
| Voice Call Statistics Accounting Record Memory Usage |
| Fixed Interval Option: | Statistics gathered for a fixed interval. |
| ACCT REC size | Accounting record size. |
| Number of ACCT REC per interval | Number of accounting records per interval. |
| Used memory size (proximate) | Amount of memory currently being used to store statistics. |
| Estimated future claimed memory size (proximate) | Amount of remaining memory available to store statistics. |
| Since Reset Option: | Statistics gathered since the last reset or reboot of the gateway. |
| ACCT REC size | Accounting record size. |
| Total count of ACCT REC | Total number of accounting records since the last reset or reboot of the gateway. |
| Used memory size (proximate) | Amount of memory currently being used to store statistics. |

| Command | Description |
|---|---|
| show event-manager consumers | Displays event statistics. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr interval aggregation | Displays statistical information by configured intervals for signaling statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| show voice statistics csr since-reset aggregation-level | Displays all signaling CSRs since the last reset. |
| show voice statistics csr since-reset all | Displays all CSRs since the last reset. |
| show voice statistics interval-tag | Displays the configured interval numbers. |