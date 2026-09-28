---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr4-vcr4-cr-book-vcr-s3-html-005cce1a7e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr4/vcr4-cr-book/vcr-s3.html
retrieved_at: 2026-08-16T23:17:35.430673+00:00
---

Cisco IOS Voice Command Reference - S commands

# Cisco IOS Voice Command Reference - S commands

Updated: December 20, 2025

Chapter: show aal2 profile through show call filter match-list

## Chapter: show aal2 profile through show call filter match-list

# show aal2 profile through show call filter match-list

## show aal2 profile

To display the ATM adaptation layer 2 (AAL2) profiles configured on the system, use the show aal2 profile command in privileged EXEC mode.

show aal2 profile all { itut profile-number | atmf profile-number | custom profile-number }

### Syntax Description

all

Displays ITU-T, ATMF, and custom AAL2 profiles configured on the system.

itut

Displays ITU-T profiles configured on the system.

atmf

Displays ATMF profiles configured on the system.

custom

Displays custom profiles configured on the system.

profile - number

AAL2 profile number to display. Choices are as follows:

For ITU-T:

1 = G.711 u-law

2 = G.711 u-law with silence insertion descriptor (SID)

7 = G.711 u-law and G.729ar8

For ATMF: None. ATMF is not supported.

For custom:

100 = G.711 u-law and G.726r32

110 = G.711 u-law, G.726r32, and G.729ar8

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)XA

This command was introduced on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(2)T

This command was implemented on the Cisco 7200 series.

### Usage Guidelines

This command applies to AAL2 VoATM applications on the Cisco 7200 series routers.

## Examples

The following command displays all of the configured profiles in the system:

```
Router# show aal2 profile all Printing all the Profiles in the system
Profile Type: ITUT Profile Number: 1 SID Support: 0
Red enable: 1 Num entries: 1
Coding type: g711ulaw Packet length: 40 UUI min: 0 UUI max: 15
Profile Type: ITUT Profile Number: 2 SID Support: 1
Red enable: 1 Num entries: 1
Coding type: g711ulaw Packet length: 40 UUI min: 0 UUI max: 15
Profile Type: custom Profile Number: 100 SID Support: 1
Red enable: 1 Num entries: 2
Coding type: g711ulaw Packet length: 40 UUI min: 0 UUI max: 7
Coding type: g726r32 Packet length: 40 UUI min: 8 UUI max: 15
Profile Type: ITUT Profile Number: 7 SID Support: 1
Red enable: 1 Num entries: 2
Coding type: g711ulaw Packet length: 40 UUI min: 0 UUI max: 15
Coding type: g729ar8 Packet length: 10 UUI min: 0 UUI max: 15
Profile Type: custom Profile Number: 110 SID Support: 1
Red enable: 1 Num entries: 3
Coding type: g711ulaw Packet length: 40 UUI min: 0 UUI max: 7
Coding type: g726r32 Packet length: 40 UUI min: 8 UUI max: 15
Coding type: g729ar8 Packet length: 30 UUI min: 8 UUI max: 15
```

The table below describes significant fields shown in this output.

Field

Description

Coding type

Voice compression algorithm.

ITUT Profile Number

Predefined combination of one or more codec types configured for a digital signal processor (DSP).

Num entries

Number of profile elements.

Packet length

Sample size.

Profile Type

Category of codec types configured on DSP. Possible types are ITU-T, ATMF, and custom.

Red enable

Redundancy for type 3 packets.

SID Support

Silence insertion descriptor.

UUI max

Maximum sequence number on the voice packets.

UUI min

Minimum sequence number on the voice packets.

### Related Commands

Command

Description

codec aal2-profile

Sets the codec profile for a DSP on a per-call basis.

## show app-hosting detail

To view detailed information about a specific hosted application (container or virtualized application) on a Cisco IOS XE
                              device, use the show app-hosting detail command in privileged EXEC mode.

show app-hosting detail appid application_id

## Syntax Description

This specifies the unique identifier (App ID) of the application for which you want to see the details.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS XE Fuji 16.12.1

This command was introduced.

### Usage Guidelines

Output of the show app-hosting detail command typically includes Application State, Application Type, Resource Reservations, Network Configuration, File Locations,
                              and Version Information.

## Examples

The following is an example for show app-hosting detail appid vdsp command. Observe that the vDSP container is in RUNNING state:

```
router# show app-hosting detail appid vdsp App id : vdsp
Owner : iox
State : RUNNING
Application
Type : docker
Name : vDSP-DSPFARM-Feature
Version : 1.0.827
Description : Built on 2024-08-27 21:58:36
Author : Cisco Systems, Inc.
Path : bootflash:vDSP_1.0.827.aarch64.tar
URL Path :
Activated profile name : vDSP-500
Resource reservation
Memory : 1010 MB
Disk : 256 MB
CPU : 11495 units
CPU-percent : 34 %
VCPU : 1
Platform resource profiles
Profile Name CPU(unit) CPU(percent) Memory(MB) Disk(MB)
---------------------------------------------------------------------------
vDSP-50         17         --        1001       256
vDSP-100        17         --        1002       256
...
Docker
------
Run-time information
Command :
Entry-point : /root/vdsp_start.sh
Run options in use :
Package run options :
Application health information
Status : 0
Last probe error :
Last probe output : 6.2 0.0 0.0 0.0 0.0 6.2 41
```

## show atm video-voice address

To display the network service access point (NSAP) address for the ATM interface, enter the show atm video - voice address command in privileged EXEC mode.

show atm video-voice address

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

### Usage Guidelines

Use this command to review ATM interface NSAP addresses that have been assigned with the atm video aesa command and to ensure
                              that ATM management is confirmed for those addresses.

## Examples

The following example displays ATM interface NSAP addresses:

```
Router# show atm video-voice address nsap address                                  type         ilmi status
47.0091810000000002F26D4901.00107B4832E1.FE   VOICE_AAL5   Confirmed
47.0091810000000002F26D4901.00107B4832E1.C8   VIDEO_AAL1   Confirmed
```

The table below describes the significant fields shown in the output.

Field

Description

NSAP address

NSAP address for the ATM interface.

Type

Type of ATM interface.

ILMI status

Integrated Local management Interface (ILMI) protocol status for the ATM interface.

### Related Commands

Command

Description

codec aal2-profile

Sets the codec profile for a DSP on a per-call basis.

## show auto-config

To display the current status of auto-configuration applications, use the show auto-config command in privileged EXEC mode.

show auto-config [ application sccp ]

### Syntax Description

application sccp

Displays the current status of only the Skinny Client Control Protocol (SCCP) application.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)XY

This command was introduced on the Communication Media Module.

12.3(14)T

This command was integrated into Cisco IOS Release 12.3(14)T.

## Examples

The following is sample output from show auto-config command:

```
Router# show auto-config application sccp auto-config application: sccp
 auto-config admin state: ENABLED & ACTIVE 
 download retries: (3)
 download timeout: no timeout, continuous retry
 server(s):  172.19.240.41 172.19.240.40 172.19.240.42
Configuration Download statistics:
        Download Attempted             : 2
          Download Successful          : 2
          Download Failed              : 0
        Configuration Attempted        : 2
          Configuration Successful     : 2
          Configuration Failed(parsing): 0
          Configuration Failed(config) : 0
Configuration Error History:
```

The table below describes the significant fields shown in the display.

Field

Description

ENABLED

Shows auto-config application: SCCP is enabled.

ACTIVE

Shows the SCCP application has registered to use auto-configuration.

timeout

Shows timeout is set to 0, continuous retry without timeout.

### Related Commands

Command

Description

auto-config

Enables auto-configuration or enters auto-config application configuration mode for the SCCP application.

debug auto-config

Enables debugging for auto-configuration applications.

debug sccp config

Enables SCCP event debugging.

## show backhaul-session-manager group

To display the status, statistics, or configuration for a particular session group or all available session groups, use the show backhaul - session - manager group command in privileged EXEC mode.

show backhaul-session-manager group { status | stats | cfg } { all | name group-name }

### Syntax Description

status

Status for available session groups.

stats

Statistics for available session groups.

cfg

Configuration for available session groups.

all

Specified parameters for all session groups.

name group - name

A particular session group.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco AS5300.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for
                                          the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

## Examples

The following example displays statistics for all session groups:

```
Router# s how backhaul-session-manager group stats all Session-Group grp1 statistics
   Successful Fail-Overs      :0
   Un-Successful Fail-Over attempts:0
   Active Pkts receive count  :0
   Standby Pkts receive count :0
   Total PDUs dispatch err    :0
```

The following example displays the current configuration for all session groups:

```
Router# show backhaul-session-manager group cfg all Session-Group
   Group Name :grp1
   Set Name   :set1
   Sessions   :3
    Dest:10.5.0.3 8304  Local:10.1.2.15 8304  Priority:0
    Dest:10.5.0.3 8300  Local:10.1.2.15 8300  Priority:2
    Dest:10.5.0.3 8303  Local:10.1.2.15 8303  Priority:2
    RUDP Options
      timer cumulative ack :100
      timer keepalive      :1000
      timer retransmit     :300
      timer transfer state :2000
      receive max          :32
      cumulative ack max   :3
      retrans max          :2
      out-of-sequence max  :3
      auto-reset max       :5
```

The following example displays the current state of all session groups. The group named "grp1" belongs to the set named "set1".

```
Router# show backhaul-session-manager group status all Session-Group
Group Name   :grp1
   Set Name     :set1
   Status       :Group-OutOfService
   Status (use) :Group-None
```

The table below describes the significant fields shown in the output.

Field

Descrption

RUDP Options

Reliable User datagram Protocol (RUDP) options.

Status

One of the following:

Group-OutOfService--No session in the group has been established.

Group-Inservice--At least one session in the group has been established.

Status (use)

One of the following:

Group-Standby--The virtual switch controller (VSC) connected to the other end of this group goes into standby mode.

Group-Active--The VSC connected to the other end of this group is the active VSC.

Group-None--The VSC has not yet declared its intent.

### Related Commands

Command

Description

show backhaul-session-manager session

Displays status, statistics, or configuration of sessions.

show backhaul-session-manager set

Displays session groups associated with a specific session set or all session sets.

## show backhaul-session-manager session

To display various information about a session or sessions, use the show backhaul - session - manager session command in privileged EXEC mode.

show backhaul-session-manager session { all | ip ip-address }

### Syntax Description

all

Information is displayed about all available sessions.

ip

Information is displayed about the session associated with this IP address only.

ip - address

IP address of the local or remote session.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco AS5300.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for
                                          the Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850.

## Examples

The following command displays information for all available sessions:

```
Router# show backhaul-session-manager session all Session information --
Session-id:35
  Group:grp1  /*this session belongs to the group named 'grp1' */
Configuration:
     Local:10.1.2.15      , port:8303
    Remote:10.5.0.3       , port:8303
  Priority:2
  RUDP Option:Client, Conn Id:0x2
State:
  Status:OPEN_WAIT, Use-status:OOS,  /*see explanation below */
Statistics:
  # of resets:0
  # of auto_resets 0
  # of unexpected RUDP transitions (total) 0
  # of unexpected RUDP transitions (since last reset) 0
  Receive pkts -  Total:0 , Since Last Reset:0
  Recieve failures -  Total:0 ,Since Last Reset:0
  Transmit pkts - Total:0, Since Last Reset:0
  Transmit Failures (PDU Only)
         Due to Blocking (Not an Error) - Total:0, Since Last Reset:0
         Due to causes other than Blocking - Total:0, Since Last
Reset:0
  Transmit Failures (NON-PDU Only)
         Due to Blocking(Not an Error) - Total:0, Since Last Reset:0
         Due to causes other than Blocking - Total:0, Since Last
Reset:0
  RUDP statistics
         Open failures:0
         Not ready failures:0
         Conn Not Open failures:0
         Send window full  failures:0
         Resource unavailble failures:0
         Enqueue failures:0
```

The table below describes significant fields shown in this output.

Field

Description

State

Can be any of the following:

OPEN--The connection is established.

OPEN_WAIT--The connection is awaiting establishment.

OPEN_XFER--Session failover is in progress for this session, which is a transient state.

CLOSE--The session is down, also a transient state.

The session waits a fixed amount of time and then moves to OPEN_WAIT.

Use-status

Indicates whether PRI signaling traffic is currently being transported over this session. Can be either of the following:

OOS--The session is not being used to transport signaling traffic. Out of service (OOS) does not indicate if the connection
                                                is established.

IS--The session is being used currently to transport all PRI signaling traffic. In service (IS) indicates that the connection
                                                is established.

### Related Commands

Command

Description

show backhaul-session-manager group

Displays status, statistics, or configuration of a specific session group or all session groups.

show backhaul-session-manager set

Displays session groups associated with a specific session set or all session sets.

## show backhaul-session-manager set

To display session groups associated with a specified session set or all session sets, use the show backhaul - session - manager set command in privileged EXEC mode.

show backhaul-session-manager set { all | name session-set-name }

### Syntax Description

all

All available session sets.

name session - set - name

A specified session set.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco AS5300.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for the
                                          Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command is supported on the Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

## Examples

The following command displays session groups associated with all session sets:

```
Router# show backhaul-session-manager set all
```

### Related Commands

Command

Description

show backhaul - session - manager group

Displays status, statistics, or configuration of a specific session group or all session groups.

show backhaul - session - manager session

Displays status, statistics, or configuration of a session or all sessions.

## show call accounting-template voice

To display accounting template activity, use the show call accounting - template voice command in privileged EXEC mode.

show call accounting-template voice [ WORD | attrList | qdump | summary ]

### Syntax Description

WORD

(Optional) Name of the accounting template.

attrList

(Optional) Displays all vendor-specific attributes (VSAs) that are filtered by accounting templates.

qdump

(Optional) Displays template activity in the service and free queues.

summary

(Optional) Lists names of all the accounting templates and the number of attributes in each template currently being used.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

### Usage Guidelines

The show call accounting - template voice command displays the status and attributes defined in each template after it is configured.

The show call accounting - template voice WORD command displays the status of a specific template and the attributes (VSAs) that are defined for that template.

The show call accounting - template voice attrList command displays all VSAs that can be filtered by accounting templates.

The show call accounting - template voice qdump command displays template activity in the service (svc) and free queues. It displays the template URL, the number of legs
                                    on which a template is active, and the state of a template.

After an accounting template is defined, it is put in the svc queue to serve new incoming calls. When a running accounting
                                          template is undefined or reloaded during an active call, the template is moved from the svc queue to the free queue and can
                                          be reused after all the active calls stop referencing it. Templates that are reloaded or undefined and that are referenced
                                          during an active call are considered to be in a "dirty" state and are called dirty templates.

To ensure that start and stop records correspond on an active call that is referencing a dirty template, all dirty templates
                                          must be kept alive until all active calls referencing that dirty template are released. After all active calls are released,
                                          the reloaded templates are applied to the next call.

The show call accounting - template voice summary command displays the current status of all the accounting templates that are configured. It shows if the template was loaded
                                    and if it is running successfully.

## Examples

The following example displays details about two templates named "cdr1" and "cdr2".

```
Router# show call accounting-template voice CDR template cdr1 is running
url: tftp://sanjoe/santa/abc/Templates/cdr1.cdr
The last load was successful.
attr:  h323-call-origin (56)
attr:  h323-call-type (57)
attr:  h323-gw-id (65)
attr:  subscriber (79)
attr:  in-portgrp-id (80)
attr:  out-portgrp-id (81)
Totally 6 attrs defined.
CDR template cdr2 is running
url: tftp://sanjoe/santa/abc/Templates/cdr2.cdr
The last load was successful.
attr:  h323-call-origin (56)
attr:  h323-call-type (57)
attr:  h323-connect-time (59)
attr:  h323-disconnect-time (64)
attr:  h323-gw-id (65)
attr:  h323-setup-time (76)
attr:  h323-voice-quality (78)
Totally 7 attrs defined.
```

The following example displays details about the template named "cdr1" only.

```
Router# show call accounting-template voice cdr1 CDR template cdr1 is running
url: tftp://sanjoe/santa/abc/Templates/cdr1.cdr
The last load was successful.
attr:  h323-call-origin (56)
attr:  h323-call-type (57)
attr:  h323-gw-id (65)
attr:  subscriber (79)
attr:  in-portgrp-id (80)
attr:  out-portgrp-id (81)
Totally 6 attrs defined.
```

The following example displays all 64 attributes that can be filtered by a template.

```
Router# show call accounting-template voice attrList h323-call-origin      
h323-call-type     
h323-gw-id     
h323-setup-time   
h323-connect-time      
h323-disconnect-time     
h323-disconnect-cause
.
.
.
calling-party-category   
originating-line-info      
charge-number      
transmission-medium-req     
redirecting-number      
backward-call-indicators
Totally 64 attributes are filterable.
```

The following example displays template activity in the service queue. Initially, no templates are in the dirty state.

```
Router# show call accounting-template voice qdump name         url                              is_dirty   no_of_legs
=========================================================================
cdr1         tftp://sanjoe/santa/abc                        0
cdr2         tftp://sanjoe/santa/abc                        0
cdr3         tftp://sanjoe/santa/abc                        0
```

After the templates are reloaded during active calls, the display below shows the templates named "cdr1" and "cdr2" to be
                              in a dirty state.

```
.
.
.
Templates in freeq
cdr1         tftp://sanjoe/santa/abc            dirty       1
cdr2         tftp://sanjoe/santa/abc            dirty       1
```

The following example displays a summary of all configured accounting templates. The template named "cdr3" is not in running
                              mode, either because it has been rejected or because it does not exist at the given URL.

```
Router# show call accounting-template voice summary name         url                                    last_load  is_running
=========================================================================
cdr1         tftp://sanjoe/santa/abc                success    is running
cdr2         tftp://sanjoe/santa/abc                success    is running
cdr3         tftp://sanjoe/santa/abc                fail       is not running
```

The table below describes the fields shown in the show call accounting - template voice display.

Field

Description

name

Name of the accounting template.

url

Location of the accounting template.

last_load

Describes if the accounting template was successfully or unsuccessfully loaded from its location.

is_running

Describes if the accounting template was activated after it was successfully loaded from its location.

is_dirty

Shows that the accounting template was reloaded during an active call.

no_of_legs

Number of call legs.

attr

Vendor-specific attributes (VSAs) defined in an accounting template.

### Related Commands

Command

Description

gw-accounting aaa

Configures a new accounting template.

## show call active fax

To display call information for T.37 store-and-forward fax transmissions in progress, use the show call active fax command in user EXEC or privileged EXEC mode.

show call active fax [ brief [ id identifier ] | compact [ duration { less seconds | more seconds }] | id identifier ]

### Syntax Description

brief

(Optional) Displays a truncated version of fax call information.

id identifier

(Optional) Displays only the call with the specified identifier . Range is a hex value from 1 to FFFF.

compact

(Optional) Displays a compact version of the fax call information.

duration

(Optional) Displays active calls that are longer or shorter than a specified seconds value. The arguments and keywords are as follows:

less --Displays calls shorter than the seconds value.

more --Displays calls longer than the seconds value.

seconds --Elapsed time, in seconds. Range is from 1 to 2147483647. There is no default value.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 2600 series and Cisco 3600 series.

12.0(3)XG

This command was modified. Support for Voice over Frame Relay (VoFR) was added.

12.0(4)XJ

This command was implemented for store-and-forward fax on the Cisco AS5300.

12.0(4)T

This command was implemented on the Cisco 7200 series.

12.0(7)XK

This command was implemented on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(3)T

This command was modified. This command was implemented for modem pass-through over VoIP on the Cisco AS5300.

12.1(5)XM

This command was implemented on the Cisco AS5800.

12.1(5)XM2

The command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support was not included for the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, and Cisco AS5850.

12.2(11)T

Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850.

12.3(14)T

This command was modified. T.38 fax relay call statistics were made available to Call Detail Records (CDRs) through vendor-specific
                                          attributes (VSAs) and added to the call log.

12.4(2)T

This command was modified. The LocalHostname display field was added to the VoIP call leg record.

12.4(15)T

This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output.

12.4(16)

This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output.

12.4(22)T

This command was modified. Command output was updated to show IPv6 information.

### Usage Guidelines

Use this command to display the contents of the active call table. This command displays information about call times, dial
                              peers, connections, quality of service, and other status and statistical information for T.37 store-and-forward fax calls
                              currently connected through the router. This command works with both on-ramp and off-ramp store-and-forward fax functions.

To display information about fax relay calls in progress, use the show call active voice command.

## Examples

The following is sample output from the show call active fax command:

```
Router# show call active fax GENERIC:
SetupTime=22021 ms
Index=1
PeerAddress=peer one
PeerSubAddress=
PeerId=0
PeerIfIndex=0
LogicalIfIndex=0
ConnectTime=24284
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=10
TransmitPackets=0
TransmitBytes=0
ReceivePackets=0
ReceiveBytes=41190
MMOIP:
ConnectionId[0x37EC7F41 0xB0110001 0x0 0x35C34]
CallID=1
RemoteIPAddress=10.0.0.0
SessionProtocol=SMTP
SessionTarget=
MessageId=
AccountId=
ImgEncodingType=MH
ImgResolution=fine
AcceptedMimeTypes=2
DiscardedMimeTypes=1
Notification=None
GENERIC:
SetupTime=23193 ms
Index=1
PeerAddress=527....
PeerSubAddress=
PeerId=3469
PeerIfIndex=157
LogicalIfIndex=30
ConnectTime=24284
CallState=4
CallOrigin=1
ChargedUnits=0
InfoType=10
TransmitPackets=5
TransmitBytes=6513
ReceivePackets=0
ReceiveBytes=0
TELE:    
ConnectionId=[0x37EC7F41 0xB0110001 0x0 0x35C34]
CallID=2
Port=3/0/0 (2)
BearerChannel=3/0/0.1
TxDuration=24010 ms
FaxTxDuration=10910 ms
FaxRate=14400
NoiseLevel=-1
ACOMLevel=-1
OutSignalLevel=0
InSignalLevel=0
InfoActivity=0
ERLLevel=-1
SessionTarget=
ImgPages=0
```

The table below provides an alphabetical listing of the fields displayed in the output of the show call active fax command and a description of each field.

Field

Description

ACOM Level

Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceler, which is the sum of the Echo Return
                                          Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call.

BearerChannel

Identification of the bearer channel carrying the call.

Buffer Drain Events

Total number of jitter buffer drain events.

Buffer Fill Events

Total number of jitter buffer fill events.

CallDuration

Length of the call, in hours, minutes, and seconds, hh:mm:ss.

CallOrigin

Call origin: answer or originate.

CallState

Current state of the call.

ChargedUnits

Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second.

CodecBytes

Payload size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

ConnectionId

Global call identifier for this gateway call.

ConnectTime

Time, in milliseconds, at which the call was connected.

Consecutive-packets-lost Events

Total number of consecutive (two or more) packet-loss events.

Corrected packet-loss Events

Total number of packet-loss events that were corrected using the RFC 2198 method.

Dial-Peer

Tag of the dial peer sending this call.

EchoCancellerMaxReflector=64

The location of the largest reflector, in milliseconds (ms). The reflector size does not exceed the configured echo path
                                          capacity. For example, if 32 ms is configured, the reflector does not report beyond 32 ms.

ERLLevel

Current echo return loss (ERL) level for this call.

FaxTxDuration

Duration of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization Rate by
                                          dividing the FaxTxDuration value by the TxDuration value.

GapFillWithInterpolation

Duration of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and following
                                          in time because voice data was lost or not received in time from the voice gateway for this call.

GapFillWithPrediction

Duration of the voice signal played out with signal synthesized from parameters, or samples of data preceding in time, because
                                          voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are frame-eraser
                                          and frame-concealment strategies in G.729 and G.723.1 compression algorithms.

GapFillWithRedundancy

Duration of a voice signal played out with a signal synthesized from available redundancy parameters because voice data was
                                          lost or not received in time from the voice gateway for this call.

GapFillWithSilence

Duration of a voice signal replaced with silence because voice data was lost or not received in time for this call.

GENERIC

Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs.

H323 call-legs

Total H.323 call legs for which call records are available.

HiWaterPlayoutDelay

High-water-mark Voice Playout FIFO Delay during this call, in ms.

Index

Dial peer identification number.

InfoActivity

Active information transfer activity state for this call.

InfoType

Information type for this call; for example, voice or fax.

InSignalLevel

Active input signal level from the telephony interface used by this call.

Last Buffer Drain/Fill Event

Elapsed time since the last jitter buffer drain or fill event, in seconds.

LocalHostname

Local hostnames used for locally generated gateway URLs.

LogicalIfIndex

Index number of the logical interface for this call.

LoWaterPlayoutDelay

Low-water-mark Voice Playout FIFO Delay during this call, in ms.

LowerIFName

Physical lower interface information. Appears only if the medium is ATM, Frame Relay (FR), or High-Level Data Link Control
                                          (HDLC).

Media

Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR, or HDLC.

Modem passthrough signaling method in use

Indicates that this is a modem pass-through call and that named signaling events (NSEs)--a Cisco-proprietary version of named
                                          telephone events in RFC 2833--are used for signaling codec upspeed. The upspeed method is the method used to dynamically change
                                          the codec type and speed to meet network conditions. This means that you might move to a faster codec when you have both voice
                                          and data calls and then slow down when there is only voice traffic.

NoiseLevel

Active noise level for this call.

OnTimeRvPlayout

Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values.

OutSignalLevel

Active output signal level to the telephony interface used by this call.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value of the peer table entry to which this call was made.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

PeerSubAddress

Subaddress when this call is connected.

Percent Packet Loss

Total percent packet loss.

Port

Identification of the time-division multiplexing (TDM) voice port carrying the call.

ReceiveBytes

Number of bytes received by the peer during this call.

ReceiveDelay

Average Playout FIFO Delay plus the Decoder Delay during this voice call, in ms.

ReceivePackets

Number of packets received by this peer during this call.

ReleaseSource

Number value of the release source.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

RoundTripDelay

Voice packet round-trip delay between the local and remote systems on the IP backbone for this call.

SelectedQoS

Selected Resourse Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

SessionTarget

Session target of the peer used for this call.

SetupTime

Value of the system UpTime, in milliseconds, when the call associated with this entry was started.

SignalingType

Signaling type for this call; for example, channel-associated signaling (CAS) or common channel signaling (CCS).

SIP call-legs

Total Session Initiation Protocol (SIP) call legs for which call records are available.

Telephony call-legs

Total telephony call legs for which call records are available.

Time between Buffer Drain/Fills

Minimum and maximum durations between jitter buffer drain or fill events, in seconds.

TransmitBytes

Number of bytes sent by this peer during this call.

TransmitPackets

Number of packets sent by this peer during this call.

TxDuration

The length of the call. Appears only if the medium is TELE.

VAD

Whether voice activation detection (VAD) was enabled for this call.

VoiceTxDuration

Duration of voice transmission from this peer to the voice gateway for this call, in ms. Derive the Voice Utilization Rate
                                          by dividing the VoiceTxDuration value by the TxDuration value.

The following is sample output from the show call active fax brief command:

```
Router# show call active fax brief <ID>: <start>hs.<index> +<connect> pid:<peer_id> <dir> <addr> <state> \
  tx:<packets>/<bytes> rx:<packets>/<bytes> <state>
IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec>
FR <protocol> [int dlci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
  sig:<on/off> <codec> (payload size)
Tele <int>: tx:<tot>/<v>/<fax>ms <codec> noise:<l> acom:<l> i/o:<l>/<l> dBm
 
1    : 22021hs.1 +2263 pid:0 Answer wook song active
tx:0/0 rx:0/41190
IP 0.0.0.0 AcceptedMime:2 DiscardedMime:1
 
1    : 23193hs.1 +1091 pid:3469 Originate 527.... active
tx:10/13838 rx:0/0
Tele : tx:31200/10910/20290ms  noise:-1 acom:-1  i/0:0/0 dBm
```

The following is sample output from the show call active fax command displaying T.38 fax relay statistics:

```
Router# show call active fax Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 0
MGCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
 GENERIC:
SetupTime=1874690 ms
Index=1
PeerAddress=5551234
PeerSubAddress=
PeerId=3
PeerIfIndex=244
LogicalIfIndex=118
ConnectTime=187875
CallDuration=00:00:44 sec
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=fax
TransmitPackets=309
TransmitBytes=5661
ReceivePackets=1124
ReceiveBytes=49189
TELE:
ConnectionId=[0x6B241E98 0xA78111D8 0x8002000A 0xF4107CA0]
IncomingConnectionId=[0x6B241E98 0xA78111D8 0x8002000A 0xF4107CA0]
CallID=1
Port=3/0/0 (1)
BearerChannel=3/0/0.1
TxDuration=2840 ms
VoiceTxDuration=0 ms
FaxTxDuration=0 ms
FaxRate=disable bps
FaxRelayMaxJitBufDepth 346
FaxRelayJitterBufOverflow 0
Initial HS Modulation is V.17/long/14400
Recent HS modulation is V.17/short/14400
Number of pages 1
Direction of transmission is Transmit
Num of Packets TX'ed/RX'ed 932/52
Packet loss conceal is 0
Encapsulation protocol is T.38 (UDPTL)
ECM is DISABLED
NoiseLevel=0
ACOMLevel=0
OutSignalLevel=0
InSignalLevel=0
InfoActivity=0
ERLLevel=0
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=5551234
OriginalCallingOctet=0x80
OriginalCalledNumber=5555678
OriginalCalledOctet=0x80
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=5551234
TranslatedCallingOctet=0x80
TranslatedCalledNumber=5555678
TranslatedCalledOctet=0x80
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=5555678
GwReceivedCalledOctet3=0x80
GwReceivedCallingNumber=5551234
GwReceivedCallingOctet3=0x80
GwReceivedCallingOctet3a=0x0
DSPIdentifier=1/0:0
Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 0
MGCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
```

The table below provides an alphabetical listing of the fields displayed in the output of the show call active fax command for T.38 fax relay statistics and a description of each field.

Field

Description

ACOMLevel

Current ACOM level estimate in 0.1 dB increments. The term ACOM is used in G.165, General Characteristics of International Telephone Connections and International Telephone Circuits: Echo Cancellers . ACOM is the combined loss achieved by the echo canceller, which is the sum of the ERL, ERL enhancement, and nonlinear processing
                                          loss for the call.

BearerChannel

Identification of the bearer channel carrying the call.

ERLLevel

Current ERL level estimate in 0.1 dB increments.

FaxRate

Fax transmission rate from this peer to the specified dial peer, in bits per second (bps).

FaxRelayJitterBufOverflow

Fax relay jitter buffer overflow, in ms.

FaxRelayMaxJitBufDepth

Fax relay maximum jitter buffer depth, in ms.

FaxTxDuration

Duration of fax transmission from this peer to the voice gateway for this call, in ms.

GwReceivedCalledNumber, GwReceivedCalledOctet3

Call information received at the gateway.

H323 call-legs

Type of call: H.323.

Initial HS Modulation

Initial high speed modulation used.

LogicalIfIndex

Index number of the logical interface for this call.

MGCP call-legs

Type of call: Media Gateway Control Protocol (MGCP).

Multicast call-legs

Type of call: Multicast.

OriginalCallingNumber, OriginalCalling Octet, OriginalCalledNumber, OriginalCalledOctet, OriginalRedirectCalledNumber, OriginalRedirectCalledOctet

Original call information regarding calling, called, and redirect numbers, and octet-3s. Octet-3s are information elements
                                          (IEs) of Q.931 that include type of number, numbering plan indicator, presentation indicator, and redirect reason information.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

Port

Identification of the TDM voice port carrying the call.

Recent HS Modulation

Most recent high-speed modulation used.

SIP call-legs

Type of call: SIP.

Telephony call-legs

Type of call: Telephony.

Total call-legs

Total calls.

TranslatedCallingNumber, TranslatedCallingOctet, TranslatedCalledNumber, TranslatedCalledOctet, TranslatedRedirectCalledNumber,
                                          TranslatedRedirectCalledOctet

Translated call information.

TxDuration

Duration of transmit path open from this peer to the voice gateway for this call, in ms.

VoiceTxDuration

Duration of voice transmission from this peer to the voice gateway for this call, in ms.

### Related Commands

Command

Description

show call active voice

Displays call information for voice calls that are in progress.

show call history

Displays the call history table.

show call-router routes

Displays the dynamic routes in the cache of the BE.

show call-router status

Displays the Annex G BE status.

show voice port

Displays configuration information about a specific voice port.

## show call active media

To display call information for media calls in progress, use the show call active media command in user EXEC or privileged EXEC mode.

show call active media [ [ brief ] [ id identifier ] | compact [ duration { less seconds | more seconds }]]

### Syntax Description

brief

(Optional) Displays a truncated version of call information.

id identifier

(Optional) Displays only the call with the specified identifier . The range is a hexadecimal value from 1 to FFFF.

compact

(Optional) Displays a compact version of call information.

duration

(Optional) Displays the call history for the specified time duration.

less seconds

(Optional) Displays the call history for shorter duration calls, in seconds. The range is from 1 to 2147483647.

more seconds

(Optional) Displays the call history for longer duration calls, in seconds. The range is from 1 to 2147483647.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

12.4(18)M

This command was modified. The less keyword, more keyword, and seconds argument were added.

### Usage Guidelines

Use this command to display the contents of the active call table. This command displays information about call times, dial
                              peers, connections, quality of service, and other status and statistical information for media calls currently connected through
                              the router.

When a media call is no longer active, its record is stored. You can display the record by using the show call history media command.

## Examples

The following is sample output from the show call active media command:

```
Router# show call active media Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Media call-legs: 2
Total call-legs: 2
 GENERIC:
SetupTime=408040 ms
Index=1
PeerAddress=sip:mrcpv2TTSServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2235
PeerIfIndex=185
LogicalIfIndex=0
ConnectTime=408130 ms
CallDuration=00:00:01 sec
CallState=4
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=0
TransmitBytes=0
ReceivePackets=57
ReceiveBytes=9120
VOIP-MEDIA:
ConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
IncomingConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
CallID=18
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10000
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10000
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=6B0CC055-C3511DB-801BC48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=0
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=0 ms
LoWaterPlayoutDelay=0 ms
TxPakNumber=0 
TxSignalPak=0 
TxComfortNoisePak=0 
TxDuration=0 
TxVoiceDuration=0 
RxPakNumber=0 
RxSignalPak=0 
RxComfortNoisePak=0 
RxDuration=0 
RxVoiceDuration=0 
RxOutOfSeq=0 
RxLatePak=0 
RxEarlyPak=0 
RxBadProtocol=0 
PlayDelayCurrent=0 
PlayDelayMin=0 
PlayDelayMax=0 
PlayDelayClockOffset=0 
PlayDelayJitter=0 
PlayErrPredictive=0 
PlayErrInterpolative=0 
PlayErrSilence=0 
PlayErrBufferOverFlow=0 
PlayErrRetroactive=0 
PlayErrTalkspurt=0 
OutSignalLevel=0 
InSignalLevel=0 
LevelTxPowerMean=0 
LevelRxPowerMean=0 
LevelBgNoise=0 
ERLLevel=0 
ACOMLevel=0 
ErrRxDrop=0 
ErrTxDrop=0 
ErrTxControl=0 
ErrRxControl=0 
Source tg label=test5
ReceiveDelay=0 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
SRTP = off
TextRelay = off
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
Media Setting=flow-through
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=4085254655
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=4085254655
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurCallTimestamp=
LongDurcallDuration=
Username=
 GENERIC:
SetupTime=408050 ms
Index=1
PeerAddress=sip:mrcpv2ASRServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2234
PeerIfIndex=184
LogicalIfIndex=0
ConnectTime=408160 ms
CallDuration=00:00:03 sec
CallState=4
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=188
TransmitBytes=30080
ReceivePackets=0
ReceiveBytes=0
VOIP-MEDIA:
ConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
IncomingConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
CallID=19
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10002
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10002
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=6B0E94CD-C3511DB-801DC48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=1000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=1495 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=100 ms
LoWaterPlayoutDelay=95 ms
TxPakNumber=0 
TxSignalPak=0 
TxComfortNoisePak=0 
TxDuration=0 
TxVoiceDuration=0 
RxPakNumber=0 
RxSignalPak=0 
RxComfortNoisePak=0 
RxDuration=0 
RxVoiceDuration=0 
RxOutOfSeq=0 
RxLatePak=0 
RxEarlyPak=0 
RxBadProtocol=0 
PlayDelayCurrent=0 
PlayDelayMin=0 
PlayDelayMax=0 
PlayDelayClockOffset=0 
PlayDelayJitter=0 
PlayErrPredictive=0 
PlayErrInterpolative=0 
PlayErrSilence=0 
PlayErrBufferOverFlow=0 
PlayErrRetroactive=0 
PlayErrTalkspurt=0 
OutSignalLevel=0 
InSignalLevel=0 
LevelTxPowerMean=0 
LevelRxPowerMean=0 
LevelBgNoise=0 
ERLLevel=0 
ACOMLevel=0 
ErrRxDrop=0 
ErrTxDrop=0 
ErrTxControl=0 
ErrRxControl=0 
Source tg label=test5
ReceiveDelay=100 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
SRTP = off
TextRelay = off
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
Media Setting=flow-through
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=4085254655
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=4085254655
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurCallTimestamp=
LongDurcallDuration=
Username=
Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Media call-legs: 2
Total call-legs: 2
```

The table below describes the significant fields shown in the display.

Field

Description

Telephony call-legs

Total telephony call legs for which call records are available.

SIP call-legs

Total session initiation protocol (SIP) call legs for which call records are available.

H323 call-legs

Total H.323 call legs for which call records are available.

Media

Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR (for Frame Relay), or HDLC (for High-Level Data Link
                                          Control).

GENERIC

Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs.

SetupTime

Value of the system UpTime, in milliseconds, when the call associated with this entry was started.

Index

Dial peer identification number.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value of the peer table entry to which this call was made.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

LogicalIfIndex

Index number of the logical interface for this call.

ConnectTime

Time, in milliseconds, at which the call was connected.

CallDuration

Length of the call, in hours, minutes, and seconds, hh:mm:ss.

CallOrigin

Call origin: answer or originate.

CallState

Current state of the call.

ChargedUnits

Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second.

InfoType

Information type for this call; for example, voice or fax.

TransmitBytes

Number of bytes sent by this peer during this call.

TransmitPackets

Number of packets sent by this peer during this call.

ReceivePackets

Number of packets received by this peer during this call.

ReceiveBytes

Number of bytes received by the peer during this call.

ReceiveDelay

Average Playout FIFO Delay plus the Decoder Delay during this voice call, in ms.

ConnectionId

Global call identifier for this gateway call.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

SelectedQoS

Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionTarget

Session target of the peer used for this call.

OnTimeRvPlayout

Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values.

GapFillWithInterpolation

Duration of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and following
                                          in time because voice data was lost or not received in time from the voice gateway for this call.

GapFillWithRedundancy

Duration of a voice signal played out with a signal synthesized from available redundancy parameters because voice data was
                                          lost or not received in time from the voice gateway for this call.

GapFillWithPrediction

Duration of the voice signal played out with signal synthesized from parameters, or samples of data preceding in time, because
                                          voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are frame-eraser
                                          and frame-concealment strategies in G.729 and G.723.1 compression algorithms.

GapFillWithSilence

Duration of a voice signal replaced with silence because voice data was lost or not received in time for this call.

HiWaterPlayoutDelay

High-water-mark Voice Playout FIFO Delay during this call, in ms.

LoWaterPlayoutDelay

Low-water-mark Voice Playout FIFO Delay during this call, in ms.

CodecBytes

Payload size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

InSignalLevel

Active input signal level from the telephony interface used by this call.

OutSignalLevel

Active output signal level to the telephony interface used by this call.

ERLLevel

Current echo return loss (ERL) level for this call.

ACOMLevel

Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceler, which is the sum of the Echo Return
                                          Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call.

PeerSubAddress

Subaddress when this call is connected.

RoundTripDelay

Voice packet round-trip delay between the local and remote systems on the IP backbone for this call.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

TxDuration

The length of the call. Appears only if the medium is TELE.

VAD

Whether voice activation detection (VAD) was enabled for this call.

### Related Commands

Command

Description

show call history media

Displays the call history table.

## show call active total-calls

To display the total number of calls in progress, use the show call active total-calls command in user EXEC or privileged EXEC mode.

show call active total-calls

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

15.3(3)M

This command was introduced.

## Examples

The following example shows how to view the total number of active calls:

```
Device# show call active total-calls Total Number of Active Calls : 110
```

## show call active
                        	 video

To display call
                              		  information for Signaling Connection Control Protocol (SCCP), Session
                              		  Initiation Protocol (SIP), and H.323 video calls in progress, use the show call active video command in user EXEC or privileged EXEC
                              		  mode.

show call active video [ [ brief ] [ id call-identifier ] | compact [ duration { less | more } seconds ] | echo-canceller call-id | session-id WORD | stats ]

### Syntax Description

brief

(Optional) Displays a truncated version of active video call information.

id call-identifier

(Optional) Displays only the video calls with the specified identifier. The
                                          						range is from 1 to FFFF.

compact

(Optional) Displays a compact version of active video call information.

duration

(Optional) Displays call history for the specified time duration.

less

Displays
                                          						call history for shorter duration calls.

more

Displays
                                          						call history for longer duration calls.

seconds

Time, in
                                          						seconds. The range is from 1 to 2147483647.

echo-canceller call-id

(Optional) Displays information about the state of the extended echo canceller
                                          						(EC). The range is from 0 to FFFFFFFF.

(Optional) Displays session identifier details for a specific
                                          						session-id. WORD specifies a wildcard pattern which is
                                          						matched against the localUUID, RemoteUUID or complete Session-Id header string.
                                          						A valid wildcard pattern can comprise one or more combination of any of these
                                          						characters *, [0-9], [a-f], [A-F].

stats

(Optional) Displays information about DSP statistics and video quality metrics.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was introduced.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command was integrated into Cisco IOS Release 12.4(9)T.

12.4(11)T

--

This
                                          						command was modified. Support was added for SIP and H.323 calls.

12.4(16); 12.4(15)T

--

This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output.

15.1(4)M

Cisco
                                          						Unified CME 8.6

This
                                          						command was modified. The stats keyword
                                          						was added.

Cisco
                                          						IOS 15.6(2)T

Cisco IOS XE Denali 16.3.1

--

This
                                          						command was modified.

The session-id keyword was added.

show call active video brief command output was enhanced to show VRF details
                                                							 and session-id details.

show call active video compact command output was enhanced to show VRF details.

Cisco IOS XE 17.16.1a

--

This command was modified to display SCIP video codec information.

This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies.

### Usage Guidelines

Use the show call active video command to display the contents of the active video call table.

Before you can
                              		  query the echo state, you need to know the hexadecimal ID. Use the show call active video brief command to find the hexadecimal ID.

## Examples

The following is a sample compact output for SCIP video codec traffic:

```
Router # show call active video compact <callID>  A/O FAX  T<sec>  Codec  type        Peer Address   IP R<ip>:<udp>     VRF
Total call-legs: 2
  11        ANS      T6      scip   VOIP-VIDEO   P1234         10.64.86.70:6011    NA                  
  13        ORG      T6      scip   VOIP-VIDEO   P1111         10.64.86.70:6007    NA
```

## Examples

The following is a sample brief output for SCIP video codec traffic:

```
Router # show call active video brief Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
1215 : 15 2673580ms.1 (*11:49:40.800 UTC Tue Jul 23 2024) +1010 pid:666 Answer 1234 active
 dur 00:00:27 tx:12/10266 rx:12/10266 dscp:0 media:0 audio tos:0xB8 video tos:0x88
 IP 10.64.86.70:6007 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:a97cadb85d17540b97f11e5f891a4425
 RemoteUUID:8a790915375e57d59d825b012bc9d145
 VRF: NA
1215 : 17 2673580ms.2 (*11:49:40.800 UTC Tue Jul 23 2024) +1010 pid:777 Originate 1111 active
 dur 00:00:27 tx:12/10266 rx:12/10266 dscp:0 media:0 audio tos:0xB8 video tos:0x88
 IP 10.64.86.70:6003 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:8a790915375e57d59d825b012bc9d145
 RemoteUUID:a97cadb85d17540b97f11e5f891a4425
 VRF: NA  

Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
```

## Examples

The following is sample output from the show call active video brief command:

```
Router # show call active video brief <ID>: <CallID> <start>ms.<index> (<start>) +<connect> pid:<peer_id> <dir> <addr> <state> 
  dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> dscp:<packets violation> media:<packets violation> audio tos:<audio tos value> video tos:<video tos value>
 IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec> <textrelay> <transcoded
  
 media inactive detected:<y/n> media cntrl rcvd:<y/n> timestamp:<time>
  
 long duration call detected:<y/n> long duration call duration :<sec> timestamp:<time>
 LostPacketRate:<%> OutOfOrderRate:<%>
LocalUUID: <%> RemoteUUID: <%>
 VRF:<%>
  MODEMPASS <method> buf:<fills>/<drains> loss <overall%> <multipkt>/<corrected>
   last <buf event time>s dur:<Min>/<Max>s
 FR <protocol> [int dlci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
  <codec> (payload size)
 ATM <protocol> [int vpi/vci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
  <codec> (payload size)
 Tele <int> (callID) [channel_id] tx:<tot>/<v>/<fax>ms <codec> noise:<l> acom:<l> i/o:<l>/<l> dBm
  MODEMRELAY info:<rcvd>/<sent>/<resent> xid:<rcvd>/<sent> total:<rcvd>/<sent>/<drops>
         speeds(bps): local <rx>/<tx> remote <rx>/<tx>
 Proxy <ip>:<audio udp>,<video udp>,<tcp0>,<tcp1>,<tcp2>,<tcp3> endpt: <type>/<manf>
 bw: <req>/<act> codec: <audio>/<video>
  tx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>
 rx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>

Telephony call-legs: 0
SIP call-legs: 1
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
11EC : 2 798700ms.1 (*12:49:45.019 IST Tue Jan 12 2016) +2010 pid:441 Answer sipp connected
 dur 00:00:50 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6005 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
LocalUUID : ab30317f1a784dc48ff824d0d3715d86
RemoteUUID : 47755a9de7794ba387653f2099600ef2
 VRF: VRF1

Telephony call-legs: 0
SIP call-legs: 1
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
```

The following is sample output from the show call active video command:

```
Router# show call active video Telephony call-legs: 4
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 2
Multicast call-legs: 0
Total call-legs: 6
 GENERIC:
SetupTime=169281770 ms
Index=2
PeerAddress=
PeerSubAddress=
PeerId=0
PeerIfIndex=0
LogicalIfIndex=0
ConnectTime=169281770 ms
CallDuration=01:20:44 sec
CallState=2
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=819728
TransmitBytes=571031017
ReceivePackets=796308
ReceiveBytes=566120602
VOIP:
ConnectionId[0x0 0x0 0x0 0x0]
IncomingConnectionId[0x0 0x0 0x0 0x0]
CallID=85 
GlobalCallId=[0x0 0x0 0x0 0x0]
CallReferenceId=25666520
CallServiceType=Video Conference
RTP Loopback Call=FALSE 
sessionIDLocaluuid=6f0a93a3a79451aebeb6d83f79a3359f
sessionIDRemoteuuid=a55b0f45861551b88f57d1fb5bb23f89
RemoteIPAddress=0.0.0.0 RemoteUDPPort=2000
RemoteSignallingIPAddress=0.0.0.0 
RemoteSignallingPort=0
RemoteMediaIPAddress=1.4.211.39 
RemoteMediaPort=2000 
RoundTripDelay=0 ms
SelectedQoS=best-effort 
tx_DtmfRelay=inband-voice 
FastConnect=FALSE
AnnexE=FALSE 
Separate H245 Connection=FALSE 
H245 Tunneling=FALSE
SessionProtocol=other 
ProtocolCallId= sipv2
SessionTarget= 1.4.211.39
SafEnabled=FALSE
OnTimeRvPlayout=0 
GapFillWithSilence=0 ms 
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms 
GapFillWithRedundancy=0 ms 
HiWaterPlayoutDelay=0ms 
LoWaterPlayoutDelay=0 ms 
Video Conferee Statistics ConfereeActualFrameRate=0
ConfereeActualBitrate=934600 
ConfereeTotalRxPackets=129853
ConfereeTotalRxBytes=125825024 
ConfereeTotalTxPackets=129853
ConfereeTotalTxBytes=125825085 
ConfereeTotalPacketsDropped=313
ConfereeCurrentPacketsDropped=0 
ConfereeTotalPacketsOutOfOrder=296
ConfereeCurrentPacketsOutOfOrder=0 
ConfereeMaxJitter=0 ConfereeCurJitter=0
ConfereeMaxDelay=0 
ConfereeCurDelay=0 
ConfereeMaxOutOfSyncDelay=0
ConfereeCurrentOutOfSyncDelay=0 
ConfereeFastVideoUpdateRate=0
ConfereeVideoDuration=1076 
Video Quality Scores RxVideoMOSInstant=78/100 (Good)
RxVideoMOSAverage=70/100 (Good) 
VIDEO: VideoTransmitCodec=H264
VideoTransmitPictureWidth=640 
VideoTransmitPictureHeight=480
VideoTransmitFrameRate=30 
VideoTransmitBitrate=934600 bps 
VideoTransmitLevel=2
VideoTransmitProfile=Baseline 
VideoTransmitPayloadFormat=RFC3984
VideoTransmitPackets=129853 
VideoTransmitBytes=125825085
VideoTransmitDuration=1076 seconds 
VideoReceiveCodec=H264
VideoReceivePictureWidth=640 
VideoReceivePictureHeight=480
VideoReceiveFrameRate=30 
VideoReceiveBitrate=934600 bps 
VideoReceiveLevel=2
VideoReceiveProfile=Baseline 
VideoReceivePayloadFormat=RFC3984
VideoReceivePackets=129853 
VideoReceiveBytes=125825024
VideoReceiveDuration=1076 seconds 
VideoCap_Codec=H264 
VideoCap_Format=CUSTOM
VideoCap_PictureWidth=640 
VideoCap_PictureHeight=480 
VideoCap_FrameRate=30
VideoCap_Bitrate=960000 bps 
VideoCap_Level=2 
VideoCap_Profile=Baseline
VideoCap_PayloadFormat=RFC3984 
VideoLostPackets=0 
VideoEarlyPackets=0
VideoLatePackets=0 
VideoUsedBandwidth=934600 
VideoNumberOfChannels=0
PlayoutMode = undefined 
PlayoutInitialDelay=0 ms 
ReceiveDelay=0 ms
LostPackets=0 
EarlyPackets=0 
LatePackets=0 
SRTP = off 
TextRelay = off 
VAD =disabled 
CoderTypeRate=h264 
CodecBytes=0 
Media Setting=flow-around 
CallerName=
CallerIDBlocked=False 
OriginalCallingNumber= 
OriginalCallingOctet=0x0
OriginalCalledNumber= 
OriginalCalledOctet=0x0 
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0 
TranslatedCallingNumber=
TranslatedCallingOctet=0x0 
TranslatedCalledNumber= 
TranslatedCalledOctet=0x0
TranslatedRedirectCalledNumber= 
TranslatedRedirectCalledOctet=0x0
MediaInactiveDetected=no 
MediaInactiveTimestamp= 
MediaControlReceived=
LongDurationCallDetected=no 
LongDurCallTimestamp= 
LongDurcallDuration=
Username= MlppServiceDomainNW=0 (none) 
MlppServiceDomainID= 
PrecedenceLevel=0
(PRECEDENCE_LEVEL_NONE)
```

The following shows sample output from the show call active video stats command:

```
Router# show call active video stats <ID>: <CallID> <start>ms.<index> +<connect> +<disc> pid:<peer_id> <direction> <addr>
  dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> 
Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 1
Multicast call-legs: 0
Total call-legs: 1
0    : 5 *10:54:50.661 PDT Tue Jan 11 2011.2 +0 pid:0 Originate  connecting
 dur 00:17:27 tx:126342/122451295 rx:126640/122453063
Video Conferee Statistics
ConfereeActualFrameRate=0  ConfereeActualBitrate=934300
ConfereeTotalRxPackets=126166  ConfereeTotalRxBytes=122282402
ConfereeTotalTxPackets=126166  ConfereeTotalTxBytes=122282463
ConfereeTotalPacketsDropped=295  ConfereeCurrentPacketsDropped=0
ConfereeTotalPacketsOutOfOrder=278  ConfereeCurrentPacketsOutOfOrder=0
ConfereeMaxJitter=0  ConfereeCurJitter=0
ConfereeMaxDelay=0  ConfereeCurDelay=0
ConfereeMaxOutOfSyncDelay=0  ConfereeCurrentOutOfSyncDelay=0
ConfereeFastVideoUpdateRate=0  ConfereeVideoDuration=1046
Video Quality Scores
RxVideoMOSInstant=78/100 (Good)
  (Compression Degradation: 86%, Network Degradation: 13%, Transcoding Degradation: 0%)
RxVideoMOSAverage=70/100 (Good)
  (Compression Degradation: 93%, Network Degradation: 6%, Transcoding Degradation: 0%)
```

The following is sample output from the show call active video command using the compact keyword:

```
Router# show call active video compact <callID>  A/O  FAX T<sec>   Codec   type     Peer    Address IP R<ip>:<udp>  VRF
Total call-legs: 2
10193925 ANS   T22          H.264 VOIP-VIDEO P2005    10.0.0.1:18070         VRF1
10193927 ORG   T22          H.264 VOIP-VIDEO P3001    11.0.0.1:27008         VRF2
```

The table below describes the significant fields shown in the display, in alphabetical order.

Field

Description

CallDuration

Length of the call, in hours, minutes, and seconds, hh:mm:ss.

CallState

Current state of the call.

Call agent controlled call-legs

Displays call legs for devices that are not telephony endpoints; for example, transcoding and conferencing

ChargedUnits

Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of a second.

CodecBytes

Payload size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

ConnectionId

Global call identifier for this gateway call.

ConnectTime

Time, in milliseconds (ms), during which the call was connected.

EchoCancellerMaxReflector

Size of the largest reflector, in ms. The reflector size cannot exceed the configured echo path capacity. For example, if
                                          32 ms is configured, the reflector does not report capacity beyond 32 ms.

ERLLevel

Current echo return loss (ERL) level for this call.

FaxTxDuration

Duration, in ms, of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization
                                          Rate by dividing the FaxTxDuration value by the TxDuration value.

GapFillWithInterpolation

Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call.

GapFillWithRedundancy

Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call.

GapFillWithPrediction

Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms.

GapFillWithSilence

Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call.

GENERIC

Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs.

H320CallType

Total H320 call types available.

H323 call-legs

Total H.323 call legs for which call records are available.

HiWaterPlayoutDelay

High-water-mark voice playout first in first out (FIFO) delay during this call, in ms.

Index

Dial peer identification number.

InfoActivity

Active information transfer activity state for this call.

InfoType

Information type for this call; for example, voice, speech, or fax.

InSignalLevel

Active input signal level from the telephony interface used by this call.

Last Buffer Drain/Fill Event

Elapsed time since the last jitter buffer drain or fill event, in seconds.

LocalHostname

Local hostnames used for locally generated gateway URLs.

LogicalIfIndex

Index number of the logical interface for this call.

LoWaterPlayoutDelay

Low-water-mark voice playout FIFO delay during this call, in ms.

LowerIFName

Physical lower interface information. Appears only if the medium is ATM, Frame Relay (FR), or High-Level Data Link Control
                                          (HDLC).

Media

Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR, or HDLC.

Multicast call-legs

Total multicast call legs for which call records are available.

NoiseLevel

Active noise level for this call.

OnTimeRvPlayout

Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values.

OutSignalLevel

Active output signal level to the telephony interface used by this call.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value of the peer table entry to which this call was made.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

PeerSubAddress

Subaddress when this call is connected.

ReceiveBytes

Number of bytes received by the peer during this call.

ReceiveDelay

Average playout FIFO delay plus the decoder delay during this voice call, in ms.

ReceivePackets

Number of packets received by this peer during this call.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

RoundTripDelay

Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call.

SCCP call-legs

Call legs for SCCP telephony endpoints.

SelectedQoS

Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionIDLocaluuid

UUID generated from originating user agent.

SessionIDRemoteuuid

UUID generated from terminating user agent.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

SessionTarget

Session target of the peer used for this call.

SetupTime

Value of the system UpTime, in milliseconds, when the call associated with this entry was started.

SIP call-legs

Total SIP call legs for which call records are available.

Telephony call-legs

Total telephony call legs for which call records are available.

Total call-legs

Total number of call legs for the call.

TransmitBytes

Number of bytes sent by this peer during this call.

TransmitPackets

Number of packets sent by this peer during this call.

TxDuration

The length of the call. Appears only if the medium is TELE.

VAD

Whether voice activation detection (VAD) was enabled for this call.

VideoCap_Annex

Extension of the video stream; for example, annex D1 and E.

VideoCap_Bitrate

Negotiated bitrate of the video stream; for example, 128000 b/s.

VideoCap_Codec

Codec for the active video call.

VideoCap_Format

Video format for the active video call.

VideoCap_FrameRate

Negotiated frame rate of the video stream; for example, 15 or 30 f/s.

VideoCap_PictureHeight

Height of the video resolution.

VideoCap_PictureWidth

Width of the video resolution.

VideoEarlyPackets

Number of early packets for a video call.

VideoLatePackets

Number of late packets in a video call.

VideoLostPackets

Number of lost packets in a video call.

VideoNumberOfChannels

Number of channels used for a video call.

Video Quality Score

Instantaneous and average Mean Opinion Score (MOS) for each active call leg. The MOS score is based on the amount of video
                                          quality degradation caused by compression distortion and the amount of video quality degradation caused by packet loss. The
                                          scale for the MOS score is as follows:

Excellent--(80--100)

Good--(60--80)

Fair--(40--60)

Poor--(20--40)

Bad--(0--20)

VideoReceiveBytes

Number of bytes received in the video call.

VideoReceiveCodec

Type of video codec used in the receiving stream.

VideoReceivePackets

Number of packets received in the video call.

VideoTransmitBytes

Number of bytes transmitted in the video call.

VideoTransmitCodec

Type of video codec used in the transmission stream.

VideoTransmitPackets

Number of packets transmitted in the video call.

VideoUsedBandwidth

Bandwidth, in kbps, used for a video call.

VoiceTxDuration

Duration of voice transmission from this peer to the voice gateway for this call, in milliseconds. Derive the Voice Utilization
                                          Rate by dividing the VoiceTxDuration value by the TxDuration value.

### Related Commands

Command

Description

show call history video

Displays call history information for SCCP video calls.

## show call active
                        	 voice

To display call information for voice calls in progress, use the show call active voice command in user EXEC or privileged EXEC mode.

show call active voice [ [ brief ] [ long-dur-call-inactive | media-inactive ] [ called-number number | calling-number number ] [ id call-identifier ] | compact [ duration { less | more } seconds ] | dest-route-string tag | echo-canceller { hexadecimal-id | port slot-number | summary } | long-dur-call [ called-number number | calling-number number ] | redirect tbct | session-id word | stats ]

### Syntax in Cisco IOS Release
                              			 12.2(33)SXH and Subsequent 12.2SX Releases

show call active [ brief ]

### Syntax Description

brief

(Optional) Displays a truncated version of call information.

long-dur-call-inactive

(Optional) Displays long duration calls that are detected and notified.

media-inactive

(Optional) Displays information about inactive media that have been detected.

called-number number

(Optional) Displays a specific called number pattern.

calling-number number

(Optional) Displays a specific calling number pattern.

id call-identifier

(Optional) Displays only the call with the specified call-identifier value. The range is from 1 to
                                          						FFFF.

compact

(Optional) Displays a compact version of call information.

duration

(Optional) Displays the call history for the specified time duration.

less seconds

Displays the call history for shorter duration calls, in seconds. The range is
                                          						from 1 to 2147483647.

more seconds

Displays the call history for longer duration calls, in seconds. The range is
                                          						from 1 to 2147483647.

dest-route-string tag

(Optional) Displays only the call with the specified destination
                                          						route tag value.
                                          						The range is from 1 to 10000.

echo-canceller

(Optional) Displays information about the state of the extended echo canceller
                                          						(EC).

hexadecimal-id

The
                                          						hexadecimal ID of an active voice call. The range is from 0x0 to 0xFFFFFFFF.

port slot-number

Displays EC details for a specified active voice port. The range varies
                                          						depending on the voice ports available on the router.

summary

Displays an EC summary for all active voice calls.

long-dur-call

(Optional) Displays long duration calls that are detected and notified.

redirect

(Optional) Displays information about active calls that are being redirected
                                          						using Release-to-Pivot (RTPvt) or Two B-Channel Transfer (TBCT).

tbct

Displays information about TBCT calls.

(Optional) Displays session identifier details for a specific
                                          						session-id. WORD specifies a wildcard pattern which is
                                          						matched against the localUUID, RemoteUUID or complete Session-Id header string.
                                          						A valid wildcard pattern can comprise one or more combination of any of these
                                          						characters *, [0-9], [a-f], [A-F].

stats

(Optional) Displays information about digital signal processing (DSP) voice
                                          						quality metrics.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This
                                          						command was introduced.

12.0(3)XG

This
                                          						command was modified. Support for Voice over Frame Relay (VoFR) was added.

12.0(4)XJ

This
                                          						command was implemented for store-and-forward fax on the Cisco AS5300.

12.0(4)T

This
                                          						command was implemented on the Cisco 7200 series.

12.0(7)XK

This
                                          						command was implemented on the Cisco MC3810.

12.1(3)T

This
                                          						command was implemented for modem pass-through over VoIP on the Cisco AS5300.

12.1(5)XM

This
                                          						command was implemented on the Cisco AS5800.

12.1(5)XM2

The
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This
                                          						command was implemented on the Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support was not
                                          						included for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850.

12.2(11)T

Support
                                          						was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850.

12.2(13)T

This
                                          						command was modified. The echo-canceller keyword was added. The command
                                          						output was modified with an extra reflector location when the extended EC is
                                          						present; the largest reflector location is shown.

12.3(1)

This
                                          						command was modified. The redirect keyword was added.

12.3(4)T

This
                                          						command was modified. The called-number , calling-number , and media-inactive keywords were added.

12.3(14)T

This
                                          						command was modified. New output relating to Skinny Client Control Protocol
                                          						(SCCP), SCCP Telephony Control Application (STCAPP), and modem pass-through
                                          						traffic was added.

12.4(2)T

This
                                          						command was modified. The LocalHostname display field was added to the VoIP
                                          						call leg record and command output was enhanced to display modem relay physical
                                          						layer and error correction protocols.

12.4(4)T

This
                                          						command was modified. The long-dur-call keyword was added.

12.4(11)XW

This
                                          						command was modified. The stats keyword
                                          						was added.

12.4(15)T

This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output.

12.2(33)SXH

This
                                          						command was integrated into Cisco IOS Release 12.2(33)SXH.

12.4(16)

This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output.

12.4(22)T

This
                                          						command was modified. Command output was updated to show IPv6 information.

15.3(3)M

This
                                          						command was modified. The dest-route-string keyword was added.

Cisco
                                          						IOS XE Release 3.10S

This
                                          						command was integrated into Cisco IOS XE Release 3.10S.

Cisco
                                          						IOS 15.6(2)T

Cisco IOS XE Denali 16.3.1

This
                                          						command was modified.

The session-id keyword was added.

show call active voice brief command output was enhanced to show VRF details and session-id details.

show call active voice compact command output was enhanced to show VRF details.

Cisco IOS XE 17.16.1a

This command was modified to display SCIP audio codec information.

This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies.

### Usage Guidelines

Use this command to display the contents of the active voice call table. This command displays information about call times,
                              dial peers, connections, and quality of service, and other status and statistical information for voice calls currently connected
                              through the router.

Before you can query the echo state, you need to know the hexadecimal ID. To find the hexadecimal ID, enter the show call active voice brief command or use the show voice call status command.

When the extended EC is present, the show call active voice command displays the contents of the Ditech EC_CHAN_CTRL structure. The table below contains names and descriptions of the
                              fields in the EC_CHAN_CTRL structure. The table also provides a listing of the information types associated with this command.

Use the show call active
                                    				voice dest-route-string command to display only the
                              		  active voice calls with call routing configured using specified
                              		  destination-route-string globally and in dial-peer level.

Symbol

Field

Description

BYP0

Channel
                                          					 bypass

1 = Transparent bypass; EC is disabled.

0 = Cancel; EC is enabled.

TAIL3

Max tail

0 = 24 milliseconds.

1 = 32 milliseconds.

2 = 48 milliseconds.

3 = 64 milliseconds.

This field should be set just greater than the anticipated worst round-trip tail delay.

REC3

Residual
                                          					 echo control

0 = Cancel only; echo is the result of linear processing; no nonlinear processing is applied.

1 = Suppress residual; residual echo is zeroed; simple nonlinear processing is applied (you might experience "dead air" when
                                                talking).

2 = Reserved.

3 = Generate comfort noise (default).

FRZ0

h-register hold

1 =
                                          					 Freezes h-register; used for testing.

HZ0

h-register clear

Sending
                                          					 the channel command with this bit set clears the h-register.

TD3

Modem
                                          					 tone disable

0 = Ignore 2100 Hz modem answer tone.

1 = G.164 mode (bypass canceller if 2100 Hz tone).

2 = R.

3 = G.165 mode (bypass canceller for phase reversing tone only).

ERL0

Echo
                                          					 return loss

0 = 6 decibel (dB).

1 = 3 dB.

2 = 0 dB.

3 = R. Worst echo return loss (ERL) situation in which canceller still works.

HLC1

High
                                          					 level compensation

0 = No attenuation.

1 = 6 dB if clipped. On loud circuits, the received direction can be attenuated 6 dB if clipping is observed.

R0

Reserved

Must be
                                          					 set to 0 to ensure compatibility with future releases.

Use the show call active voice redirect tbct command to monitor any active calls that implement RTPvt or TBCT.

When a call is no longer active, its record is stored. You can display the record by using the show call history voice command.

## Examples

The following is a sample compact output for SCIP audio codec traffic:

```
Router # show call active voice compact <callID>  A/O FAX  T<sec>  Codec  type  Peer Address  IP R<ip>:<udp>    VRF
Total call-legs: 2
  350      ANS      T6      scip   VOIP   Psipp        10.43.33.45:6006   NA                  
  351      ORG      T6      scip   VOIP   P8888        10.43.33.45:6002   NA
```

## Examples

The following is a sample brief output for SCIP audio codec traffic:

```
Router # show call active voice brief Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2

121C : 19 2737820ms.1 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:666 Answer 1234 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6008 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:37110991b54051679f675479a6e93de7
 RemoteUUID:e74b1bf0678e5209915c03a9660cb00f
 VRF: NA
121C : 20 2737820ms.2 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:777 Originate 1111 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6004 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:e74b1bf0678e5209915c03a9660cb00f
 RemoteUUID:37110991b54051679f675479a6e93de7
 VRF: NA

Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
```

## Examples

The following is sample output from the show call active voice command for modem relay traffic:

```
Router# show call active voice Modem Relay Local Rx Speed=0 bps
Modem Relay Local Tx Speed=0 bps
Modem Relay Remote Rx Speed=0 bps
Modem Relay Remote Tx Speed=0 bps
Modem Relay Phy Layer Protocol=v34
Modem Relay Ec Layer Protocol=v14
SPRTInfoFramesReceived=0
SPRTInfoTFramesSent=0
SPRTInfoTFramesResent=0
SPRTXidFramesReceived=0
SPRTXidFramesSent=0
SPRTTotalInfoBytesReceived=0
SPRTTotalInfoBytesSent=0
SPRTPacketDrops=0
```

The table below describes the significant fields shown in the display.

Field

Description

Modem Relay Local Rx Speed

Download speed, in bits per second, of the local modem relay.

Modem Relay Local Tx Speed

Upload speed of the local modem relay.

Modem Relay Remote Rx Speed

Download speed of the remote modem relay.

Modem Relay Remote Tx Speed

Upload speed of the remote modem relay.

Modem Relay Phy Layer Protocol

Physical protocol of the modem relay.

Modem Relay Ec Layer Protocol

EC layer protocol of the modem relay.

SPRTInfoFramesReceived

Total number of simple packet relay transport (SPRT) protocol frames received.

SPRTInfoTFramesSent

Total number of SPRT frames sent.

SPRTInfoTFramesResent

Total number of SPRT frames sent again.

SPRTXidFramesReceived

Total number of SPRTS ID frames received.

SPRTXidFramesSent

Total number of SPRTS ID frames sent.

SPRTTotalInfoBytesReceived

Total number of SPRT bytes received.

SPRTTotalInfoBytesSent

Total number of SPRT bytes sent.

SPRTPacketDrops

Total number of SPRT packets dropped.

The following is sample output from the show call active voice command:

```
Router# show call active voice Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 1
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
 GENERIC:
SetupTime=1072620 ms
Index=1
PeerAddress=9193927582
PeerSubAddress=
PeerId=8
PeerIfIndex=19
LogicalIfIndex=0
ConnectTime=1078940 ms
CallDuration=00:00:51 sec
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=speech
TransmitPackets=1490
TransmitBytes=0
ReceivePackets=2839
ReceiveBytes=56780
VOIP:
ConnectionId[0xE28B6D1D 0x3D9011D6 0x800400D0 0xBA0D97A1]
IncomingConnectionId[0xE28B6D1D 0x3D9011D6 0x800400D0 0xBA0D97A1]
CallID=1
sessionIDLocaluuid=4fd24d9121935531a7f8d750ad16e19 
sessionIDRemoteuuid=db248b6cbdc547bbc6c6fdfb6916eeb
RemoteIPAddress=10.44.44.44 RemoteUDPPort=17096
RemoteSignallingIPAddress=10.44.44.44 
RemoteSignallingPort=56434
RemoteMediaIPAddress=10.44.44.44 
RemoteMediaPort=17096 
RoundTripDelay=6 ms
SelectedQoS=best-effort 
tx_DtmfRelay=h245-signal 
FastConnect=TRUE AnnexE=FALSE
Separate H245 Connection=FALSE 
H245 Tunneling=TRUE SessionProtocol=cisco
ProtocolCallId= sipv2
SessionTarget= 10.44.44.44
OnTimeRvPlayout=54160 
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms 
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms 
HiWaterPlayoutDelay=70 ms 
LoWaterPlayoutDelay=60 ms
TxPakNumber=1490 
TxSignalPak=0 
TxComfortNoisePak=1 
TxDuration=54240
TxVoiceDuration=29790 
RxPakNumber=2711 
RxSignalPak=0 
RxDuration=0
TxVoiceDuration=54210 
VoiceRxDuration=54160 
RxOutOfSeq=0 
RxLatePak=0
RxEarlyPak=0 
PlayDelayCurrent=60 
PlayDelayMin=60 
PlayDelayMax=70
PlayDelayClockOffset=212491899 
PlayDelayJitter=0 ms 
PlayErrPredictive=0
PlayErrInterpolative=0 
PlayErrSilence=0 
PlayErrBufferOverFlow=10
PlayErrRetroactive=0 
PlayErrTalkspurt=0 
OutSignalLevel=-57 
InSignalLevel=-51
LevelTxPowerMean=0 
LevelRxPowerMean=-510 
LevelBgNoise=0 
ERLLevel=16
ACOMLevel=16 
ErrRxDrop=0 
ErrTxDrop=0 
ErrTxControl=0 
ErrRxControl=0
ReceiveDelay=60 ms 
LostPackets=0 
EarlyPackets=0 
LatePackets=0 
SRTP = off 
VAD =enabled 
CoderTypeRate=g729r8 
CodecBytes=20 
Media Setting=flow-through
CallerName= 
CallerIDBlocked=False 
OriginalCallingNumber=9193927582
OriginalCallingOctet=0x21 
OriginalCalledNumber=93615494
OriginalCalledOctet=0xC1 
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF 
TranslatedCallingNumber=9193927582
TranslatedCallingOctet=0x21 
TranslatedCalledNumber=93615494
TranslatedCalledOctet=0xC1 
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF 
GwReceivedCalledNumber=93615494
GwReceivedCalledOctet3=0xC1 
GwReceivedCallingNumber=9193927582
GwReceivedCallingOctet3=0x21 
GwReceivedCallingOctet3a=0x81
MediaInactiveDetected=no 
MediaInactiveTimestamp= 
MediaControlReceived=
Username= GENERIC: 
SetupTime=1072760 ms 
Index=1 PeerAddress=93615494
PeerSubAddress= 
PeerId=9 
PeerIfIndex=18 
LogicalIfIndex=4 
ConnectTime=1078940 ms
CallDuration=00:00:53 sec 
CallState=4 
CallOrigin=1 
ChargedUnits=0
InfoType=speech 
TransmitPackets=2953 
TransmitBytes=82684 
ReceivePackets=1490
ReceiveBytes=29781 TELE: 
ConnectionId=[0xE28B6D1D 0x3D9011D6 0x800400D00xBA0D97A1] 
IncomingConnectionId=[0xE28B6D1D 0x3D9011D6 0x800400D0 0xBA0D97A1]
CallID=2 
Port=3/0/0 (1) 
BearerChannel=3/0/0.2 
TxDuration=59080 ms
VoiceTxDuration=29790 ms 
FaxTxDuration=0 ms 
CoderTypeRate=g729r8 
NoiseLevel=-54
ACOMLevel=16 
OutSignalLevel=-57 
InSignalLevel=-51 
InfoActivity=1 
ERLLevel=16
EchoCancellerMaxReflector=8 
SessionTarget= ImgPages=0 CallerName=
CallerIDBlocked=False 
AlertTimepoint=1073340 ms
OriginalCallingNumber=9193927582 
OriginalCallingOctet=0x21
OriginalCalledNumber=93615494 
OriginalCalledOctet=0xC1
OriginalRedirectCalledNumber= 
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=9193927582 
TranslatedCallingOctet=0x21
TranslatedCalledNumber=93615494 
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber= 
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=93615494 
GwReceivedCalledOctet3=0xC1
GwOutpulsedCalledNumber=93615494 
GwOutpulsedCalledOctet3=0xC1
GwReceivedCallingNumber=9193927582 
GwReceivedCallingOctet3=0x21
GwReceivedCallingOctet3a=0x81 
GwOutpulsedCallingNumber=9193927582
GwOutpulsedCallingOctet3=0x21 
GwOutpulsedCallingOctet3a=0x81
DSPIdentifier=3/1:1 
Telephony call-legs: 1 
SIP call-legs: 0 
H323 call-legs: 1
Call agent controlled call-legs: 0 
SCCP call-legs: 0 
Multicast call-legs: 0
Total call-legs: 2
```

The first table above and the table below describe the significant fields shown in the display, in alphabetical order.

Field

Description

CallDuration

Length of the call, in hours, minutes, and seconds, hh:mm:ss.

CallState

Current state of the call.

Call agent controlled call-legs

Displays call legs for devices that are not telephony endpoints; for example, transcoding and conferencing

ChargedUnits

Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second.

CodecBytes

Payload size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

ConnectionId

Global call identifier for this gateway call.

ConnectTime

Time, in ms, during which the call was connected.

EchoCancellerMaxReflector

Size of the largest reflector, in ms. The reflector size cannot exceed the configured echo path capacity. For example, if
                                          32 ms is configured, the reflector does not report capacity beyond 32 ms.

ERLLevel

Current echo return loss (ERL) level for this call.

FaxTxDuration

Duration, in ms, of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization
                                          Rate by dividing the FaxTxDuration value by the TxDuration value.

GapFillWithInterpolation

Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call.

GapFillWithRedundancy

Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call.

GapFillWithPrediction

Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms.

GapFillWithSilence

Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call.

GENERIC

Generic or common parameters; that is, parameters that are common for VoIP and telephony call legs.

H320CallType

Total H320 call types available.

H323 call-legs

Total H.323 call legs for which call records are available.

HiWaterPlayoutDelay

High-water-mark voice playout first in first out (FIFO) delay during this call, in ms.

Index

Dial peer identification number.

InfoActivity

Active information transfer activity state for this call.

InfoType

Information type for this call; for example, voice, speech, or fax.

InSignalLevel

Active input signal level from the telephony interface used by this call.

LogicalIfIndex

Index number of the logical interface for this call.

LoWaterPlayoutDelay

Low-water-mark voice playout FIFO delay during this call, in ms.

Media

Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, Frame Relay (FR), or High-Level Data Link Control (HDLC).

Multicast call-legs

Total multicast call legs for which call records are available.

NoiseLevel

Active noise level for this call.

OnTimeRvPlayout

Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values.

OutSignalLevel

Active output signal level to the telephony interface used by this call.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value of the peer table entry to which this call was made.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

PeerSubAddress

Subaddress when this call is connected.

ReceiveBytes

Number of bytes received by the peer during this call.

ReceiveDelay

Average playout FIFO delay plus the decoder delay during this voice call, in ms.

ReceivePackets

Number of packets received by this peer during this call.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

RoundTripDelay

Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call.

SCCP call-legs

Call legs for SCCP telephony endpoints.

SelectedQoS

Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionIDLocaluuid

UUID generated from the originating user agent.

SessionIDRemoteuuid

UUID generated from the terminating user agent.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

SessionTarget

Session target of the peer used for this call.

SetupTime

Value of the system UpTime, in ms, when the call associated with this entry was started.

SIP call-legs

Total SIP call legs for which call records are available.

Telephony call-legs

Total telephony call legs for which call records are available.

Total call-legs

Total number of call legs for the call.

TransmitBytes

Number of bytes sent by this peer during this call.

TransmitPackets

Number of packets sent by this peer during this call.

TxDuration

The length of the call. Appears only if the medium is TELE.

VAD

Whether voice activation detection (VAD) was enabled for this call.

VoiceTxDuration

Duration of voice transmission from this peer to the voice gateway for this call, in ms. Derive the Voice Utilization Rate
                                          by dividing the VoiceTxDuration value by the TxDuration value.

The following is sample output from the show call active voice command for voice traffic over call-agent controlled call legs. Note that call legs for SCCP telephony endpoints, that is,
                              phones controlled by STCAPP, are displayed under the "Call agent controlled call-legs" field ("SCCP call-legs" displays call
                              legs for devices that are not telephony endpoints; for example, transcoding and conferencing).

```
Router# show call active voice Telephony call-legs: 2
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 2
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 4
 GENERIC:
SetupTime=1557650 ms
Index=1
PeerAddress=
PeerSubAddress=
PeerId=999100
PeerIfIndex=14
LogicalIfIndex=10
ConnectTime=1562040 ms
CallDuration=00:01:01 sec
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=speech
TransmitPackets=3101
TransmitBytes=519564
ReceivePackets=3094
ReceiveBytes=494572
TELE:
ConnectionId=[0x11B1860C 0x22D711D7 0x8014E4D4 0x8FD15327]
IncomingConnectionId=[0x11B1860C 0x22D711D7 0x8014E4D4 0x8FD15327]
CallID=25
Port=3/0/0 (25)
BearerChannel=3/0/0.1
TxDuration=59670 ms
VoiceTxDuration=59670 ms
FaxTxDuration=0 ms
CoderTypeRate=g711ulaw
NoiseLevel=-12
ACOMLevel=22
OutSignalLevel=-12
InSignalLevel=-11
InfoActivity=1
ERLLevel=22
EchoCancellerMaxReflector=2
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x80
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=
TranslatedCallingOctet=0x0
TranslatedCalledNumber=
TranslatedCalledOctet=0x80
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0x0
DSPIdentifier=1/1:1
 GENERIC:
SetupTime=1559430 ms
Index=1
PeerAddress=7702
PeerSubAddress=
PeerId=999100
PeerIfIndex=14
LogicalIfIndex=11
ConnectTime=1562020 ms
CallDuration=00:01:03 sec
CallState=4
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=3151
TransmitBytes=528900
ReceivePackets=3158
ReceiveBytes=503876
TELE:
ConnectionId=[0x0 0x0 0x0 0x0]
IncomingConnectionId=[0x0 0x0 0x0 0x0]
CallID=26
Port=3/0/0 (26)
BearerChannel=3/0/0.2
TxDuration=60815 ms
VoiceTxDuration=60815 ms
FaxTxDuration=0 ms
CoderTypeRate=g711ulaw
NoiseLevel=-12
ACOMLevel=28
OutSignalLevel=-12
InSignalLevel=-11
InfoActivity=1
ERLLevel=28
EchoCancellerMaxReflector=2
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
AlertTimepoint=1559430 ms
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=7701
TranslatedCallingOctet=0x0
TranslatedCalledNumber=7702
TranslatedCalledOctet=0x0
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0x0
GwOutpulsedCalledNumber=7702
GwOutpulsedCalledOctet3=0x0
GwOutpulsedCallingNumber=7701
GwOutpulsedCallingOctet3=0x0
GwOutpulsedCallingOctet3a=0x0
DSPIdentifier=1/1:2
 GENERIC:
SetupTime=1562040 ms
Index=1
PeerAddress=
PeerSubAddress=
PeerId=0
PeerIfIndex=0
LogicalIfIndex=0
ConnectTime=0 ms
CallDuration=00:00:00 sec
CallState=2
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=3215
TransmitBytes=512996
ReceivePackets=3208
ReceiveBytes=512812
VOIP:
ConnectionId[0x0 0x0 0x0 0x0]
IncomingConnectionId[0x0 0x0 0x0 0x0]
CallID=27
RemoteIPAddress=10.10.0.0
RemoteUDPPort=17718
RemoteSignallingIPAddress=10.10.0.0
RemoteSignallingPort=0
RemoteMediaIPAddress=10.2.6.10
RemoteMediaPort=17718
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=inband-voice
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=other
ProtocolCallId=
SessionTarget=
OnTimeRvPlayout=60640
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=105 ms
LoWaterPlayoutDelay=105 ms
TxPakNumber=3040 
TxSignalPak=0 
TxComfortNoisePak=0 
TxDuration=60815 
TxVoiceDuration=60815 
RxPakNumber=3035 
RxSignalPak=0 
RxDuration=0 
TxVoiceDuration=60690 
VoiceRxDuration=60640 
RxOutOfSeq=0 
RxLatePak=0 
RxEarlyPak=0 
PlayDelayCurrent=105 
PlayDelayMin=105 
PlayDelayMax=105 
PlayDelayClockOffset=-1662143961 
PlayDelayJitter=0 
PlayErrPredictive=0 
PlayErrInterpolative=0 
PlayErrSilence=0 
PlayErrBufferOverFlow=0 
PlayErrRetroactive=0 
PlayErrTalkspurt=0 
OutSignalLevel=-12 
InSignalLevel=-11 
LevelTxPowerMean=0 
LevelRxPowerMean=-115 
LevelBgNoise=0 
ERLLevel=28 
ACOMLevel=28 
ErrRxDrop=0 
ErrTxDrop=0 
ErrTxControl=0 
ErrRxControl=0 
PlayoutMode = undefined
PlayoutInitialDelay=0 ms
ReceiveDelay=105 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
SRTP = off
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
Media Setting=flow-around
Modem passthrough signaling method is nse:
Buffer Fill Events = 0
Buffer Drain Events = 0
Percent Packet Loss = 0
Consecutive-packets-lost Events = 0
Corrected packet-loss Events = 0
Last Buffer Drain/Fill Event = 0sec
Time between Buffer Drain/Fills = Min 0sec Max 0sec
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=
TranslatedCallingOctet=0x0
TranslatedCalledNumber=
TranslatedCalledOctet=0x0
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0x0
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
Username=
 GENERIC:
SetupTime=1562040 ms
Index=2
PeerAddress=
PeerSubAddress=
PeerId=0
PeerIfIndex=0
LogicalIfIndex=0
ConnectTime=0 ms
CallDuration=00:00:00 sec
CallState=2
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=3380
TransmitBytes=540332
ReceivePackets=3386
ReceiveBytes=540356
VOIP:
ConnectionId[0x0 0x0 0x0 0x0]
IncomingConnectionId[0x0 0x0 0x0 0x0]
CallID=28
RemoteIPAddress=10.0.0.0
RemoteUDPPort=18630
RemoteSignallingIPAddress=10.10.0.0
RemoteSignallingPort=0
RemoteMediaIPAddress=10.2.6.10
RemoteMediaPort=18630
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=inband-voice
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=other
ProtocolCallId=
SessionTarget=
OnTimeRvPlayout=63120
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=105 ms
LoWaterPlayoutDelay=105 ms
TxPakNumber=3158 
TxSignalPak=0 
TxComfortNoisePak=0 
TxDuration=63165 
TxVoiceDuration=63165 
RxPakNumber=3164 
RxSignalPak=0 
RxDuration=0 
TxVoiceDuration=63165 
VoiceRxDuration=63120 
RxOutOfSeq=0 
RxLatePak=0 
RxEarlyPak=0 
PlayDelayCurrent=105 
PlayDelayMin=105 
PlayDelayMax=105 
PlayDelayClockOffset=957554296 
PlayDelayJitter=0 
PlayErrPredictive=0 
PlayErrInterpolative=0 
PlayErrSilence=0 
PlayErrBufferOverFlow=0 
PlayErrRetroactive=0 
PlayErrTalkspurt=0 
OutSignalLevel=-12 
InSignalLevel=-11 
LevelTxPowerMean=0 
LevelRxPowerMean=-114 
LevelBgNoise=0 
ERLLevel=22 
ACOMLevel=22 
ErrRxDrop=0 
ErrTxDrop=0 
ErrTxControl=0 
ErrRxControl=0 
PlayoutMode = undefined
PlayoutInitialDelay=0 ms
ReceiveDelay=105 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
SRTP = off
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
Media Setting=flow-around
Modem passthrough signaling method is nse:
Buffer Fill Events = 0
Buffer Drain Events = 0
Percent Packet Loss = 0
Consecutive-packets-lost Events = 0
Corrected packet-loss Events = 0
Last Buffer Drain/Fill Event = 0sec
Time between Buffer Drain/Fills = Min 0sec Max 0sec
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=
TranslatedCallingOctet=0x0
TranslatedCalledNumber=
TranslatedCalledOctet=0x0
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0x0
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
Username=
Telephony call-legs: 2
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 2
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 4
```

The tables above describe the significant fields shown in the display, in alphabetical order.

The following is sample output from the show call active voice command to indicate if Service Advertisement Framework (SAF) is being used:

```
Router# show call active voice Total call-legs: 2
GENERIC:
SetupTime=1971780 ms
Index=1
PeerAddress=6046692010
PeerSubAddress=
PeerId=20003
PeerIfIndex=17
.
.
.
VOIP:
SessionProtocol=sipv2
ProtocolCallId=7A9E7D9A-EAD311DC-8036BCC4-6EEE85D6@1.5.6.12
SessionTarget=1.5.6.10
SafEnabled=TRUE
SafTrunkRouteId=1
SafPluginDialpeerTag=8
```

The tables above describe the significant fields shown in the display.

The following is sample output from the show call active voice command for fax-relay traffic:

```
Router# show call active voice Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 1
MGCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
 GENERIC:
SetupTime=1049400 ms
Index=2
PeerAddress=52930
PeerSubAddress=
PeerId=82
PeerIfIndex=222
LogicalIfIndex=0
ConnectTime=105105
CallDuration=00:00:59
CallState=4
CallOrigin=1
ChargedUnits=0
InfoType=10
TransmitPackets=1837
TransmitBytes=29764
ReceivePackets=261
ReceiveBytes=4079
VOIP:
ConnectionId[0xEB630F4B 0x9F5E11D7 0x8008CF18 0xB9C3632]
IncomingConnectionId[0xEB630F4B 0x9F5E11D7 0x8008CF18 0xB9C3632]
RemoteIPAddress=10.7.95.3
RemoteUDPPort=16610
RemoteSignallingIPAddress=10.7.95.3
RemoteSignallingPort=1720
RemoteMediaIPAddress=10.7.95.3
RemoteMediaPort=16610
RoundTripDelay=13 ms
SelectedQoS=best-effort
tx_DtmfRelay=inband-voice
FastConnect=TRUE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=TRUE
SessionProtocol=cisco
ProtocolCallId=
SessionTarget=ipv4:10.7.95.3
OnTimeRvPlayout=1000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=110 ms
LoWaterPlayoutDelay=70 ms
ReceiveDelay=70 ms
LostPackets=0
EarlyPackets=1
LatePackets=0
VAD = enabled
CoderTypeRate=t38
CodecBytes=40
Media Setting=flow-through
AlertTimepoint=104972
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=4085550130
OriginalCallingOctet=0x0
OriginalCalledNumber=52930
OriginalCalledOctet=0xE9
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x7F
TranslatedCallingNumber=4085550130
TranslatedCallingOctet=0x0
TranslatedCalledNumber=52930
TranslatedCalledOctet=0xE9
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=52930
GwReceivedCalledOctet3=0xE9
GwOutpulsedCalledNumber=52930
GwOutpulsedCalledOctet3=0xE9
GwReceivedCallingNumber=555-0100
GwReceivedCallingOctet3=0x0
GwReceivedCallingOctet3a=0x80
GwOutpulsedCallingNumber=555-0101
GwOutpulsedCallingOctet3=0x0
GwOutpulsedCallingOctet3a=0x80
Username=
FaxRelayMaxJitterBufDepth  = 0 ms
FaxRelayJitterBufOverFlow = 0
FaxRelayHSmodulation = 0
FaxRelayNumberOfPages = 0
Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 1
MGCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 1
```

The tables above describe the significant fields shown in the display.

The following is sample output from the show call active voice brief command:

```
Router# show call active voice brief <ID>: <CallID> <start>ms.<index> (<start>) +<connect> pid:<peer_id> <dir> <addr> <state> 
  dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> dscp:<packets violation> media:<packets 
violation> audio tos:<audio tos value> video tos:<video tos value>
 IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec> <textrelay> <transcoded
  
 media inactive detected:<y/n> media cntrl rcvd:<y/n> timestamp:<time>
  
 long duration call detected:<y/n> long duration call duration :<sec> timestamp:<time>
 LostPacketRate:<%> OutOfOrderRate:<%>
 LocalUUID:<%> RemoteUUID:<%>
 VRF:<%>
  MODEMPASS <method> buf:<fills>/<drains> loss <overall%> <multipkt>/<corrected>
   last <buf event time>s dur:<Min>/<Max>s
 FR <protocol> [int dlci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
  <codec> (payload size)
 ATM <protocol> [int vpi/vci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
  <codec> (payload size)
 Tele <int> (callID) [channel_id] tx:<tot>/<v>/<fax>ms <codec> noise:<l> acom:<l> i/o:<l>/<l> dBm
  MODEMRELAY info:<rcvd>/<sent>/<resent> xid:<rcvd>/<sent> total:<rcvd>/<sent>/<drops>
         speeds(bps): local <rx>/<tx> remote <rx>/<tx>
 Proxy <ip>:<audio udp>,<video udp>,<tcp0>,<tcp1>,<tcp2>,<tcp3> endpt: <type>/<manf>
 bw: <req>/<act> codec: <audio>/<video>
  tx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>
 rx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>

Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
1218 : 15 2442930ms.1 (*13:22:20.797 UTC Thu Feb 18 2016) +2010 pid:880 Answer sipp active
 dur 00:00:02 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 1.4.186.60:6005 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off 
Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
LocalUUID:ab30317f1a784dc48ff824d0d3715d86
RemoteUUID:47755a9de7794ba387653f2099600ef2
 VRF: VRF1
1218 : 16 2442940ms.1 (*13:22:20.807 UTC Thu Feb 18 2016) +2000 pid:770 Originate 7777 active
 dur 00:00:02 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 9.45.33.11:16384 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms g711ulaw TextRelay: off 
Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
LocalUUID:47755a9de7794ba387653f2099600ef2
RemoteUUID:ab30317f1a784dc48ff824d0d3715d86
 VRF: NA

Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
```

The following is an example of the show call active voice command using the echo-canceller keyword. The number 9 represents the hexadecimal ID of an active voice call.

```
Router# show call active voice echo-canceller 9 ACOM=-65  ERL=45
Echo canceller control words=6C 0
Bypass=OFF  Tail=64  Residual ecan=Comfort noise
Freeze=OFF  Modem tone disable=Ignore 2100Hz tone
Worst ERL=6  High level compensation=OFF
Max amplitude reflector (in msec)=5
Ecan version = 8180
```

The following is sample output from the show call active voice echo-canceller command for a call with a hexadecimal ID of 10:

```
Router# show call active voice echo-canceller 10 ACOM=-15  ERL=7 
Echo canceller control words=6C 0 
Bypass=OFF  Tail=64  Residual ecan=Comfort noise 
Freeze=OFF  Modem tone disable=Ignore 2100Hz tone 
Worst ERL=6  High level compensation=OFF 
Max amplitude reflector (in msec)=64
```

The call ID number (which is 10 in the preceding example) changes with every new active call. When an active call is up, you
                              must enter the show call active voice brief command to obtain the call ID number. The call ID must be converted to hexadecimal value if you want to use the show call active voice echo-canceller x command ( x = call ID converted to hexadecimal value).

The table below shows call ID examples converted to hexadecimal values (generally incremented by 2):

Decimal

Hex

2

2

4

4

6

6

8

8

10

A

12

C

Alternatively, you can use the show voice call status command to obtain the call ID. The call ID output is already in hexadecimal values form when you use this command:

```
Router# show voice call status CallID     CID  ccVdb      Port      DSP/Ch  Called #   Codec    Dial-peers
0x1        11CE 0x02407B20 1:0.1     1/1     1000       g711ulaw 2000/1000
```

The following is sample output from the show call active voice command using the compact keyword:

```
Router# show call active voice compact <callID>  A/O  FAX T<sec>   Codec      type    Peer        Address IP R<ip>:<udp>  VRF
Total call-legs: 2
8565722  ANS    T12         g711ulaw   VOIP   P777412373   10.0.0.1:30804          VRF1
8565723  ORG    T12         g711ulaw   VOIP   P777512373   11.0.0.1:30804          VRF2
```

The following is sample output from the show call active voice redirect command using the tbct keyword:

```
Router# show call active voice redirect tbct TBCT:
        Maximum no. of TBCT calls allowed:No limit
        Maximum TBCT call duration:No limit
Total number TBCT calls currently being monitored = 1
ctrl name=T1-2/0, tag=13, call-ids=(7, 8), start_time=*00:12:25.985 UTC Mon Mar 1 1993
```

The table below describes the significant fields shown in the display.

Field

Description

Maximum no. of TBCT calls allowed

Maximum number of calls that can use TBCT as defined by the tbct max calls command.

Maximum TBCT call duration

Maximum length allowed for a TBCT call as defined by the tbct max call-duration command.

Total number TBCT calls currently being monitored

Total number of active TBCT calls.

ctrl name

Name of the T1 controller where the call originated.

tag

Call tag number that identifies the call.

call-ids

Numbers that uniquely identify the call legs.

start_time

Time, in hours, minutes, and seconds, when the redirected call began.

### Related Commands

Command

Description

show call active fax

Displays call information for fax transmissions that are in progress.

show call history

Displays the call history table.

show call-router routes

Displays the dynamic routes in the cache of the BE.

show call-router status

Displays the Annex G BE status.

show dial-peer voice

Displays configuration information for dial peers.

show num-exp

Displays how the number expansions are configured in VoIP.

show voice call status

Displays the call status for voice ports on the Cisco router or concentrator.

show voice port

Displays configuration information about a specific voice port.

## show call application app-level

To display application-level statistics for voice applications, use the show call application app-level command in privileged EXEC mode.

show call application { active | history } app-level [ app-tag application-name | summary ]

### Syntax Description

active

Displays statistics for active application instances.

history

Displays statistics for terminated application instances.

app-tag application-name

Name of a specific voice application. Output displays statistics for that voice application.

summary

Displays a summary for each application.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

To display statistics with this command, you must enable statistics collection with the call application stats command.

This command displays gauges and counters that are aggregated per application. The values represent all instances of a particular
                                    voice application running on the gateway while statistics collection is enabled.

To reset application-level counters to zero and subtract the counters from the gateway-level statistics in history, use the clear call application stats command. Statistic counters continue accumulating in history until you use the clear call application stats command or the gateway reloads.

Statistics for an application are automatically cleared if the application is deleted with the no call application voice command or its script is reloaded with the call application voice load command.

## Examples

The following is sample output from the show call application app-level command using different keywords:

```
Router# show call application active app-level summary Application level active Info:
                             Sessions       
App Name                 w/ Stats   Total     
session                  0          0         
fax_hop_on               0          0         
clid_authen              0          0         
clid_authen_collect      0          0         
clid_authen_npw          0          0         
clid_authen_col_npw      0          0         
clid_col_npw_3           0          0         
clid_col_npw_npw         0          0         
Default                  0          0         
lib_off_app              0          0         
fax_on_vfc_onramp_app    0          0         
asr                      0          0         
offramp                  0          0         
generic                  1          1         
smtp_record              0          0         
authen                   0          0         
authorize                0          0         
ram_record_replay        0          0         
Router# show call application active app-level app-tag generic Application level active Info:
Application Name:              generic
url:                           tftp://10.10.10.113/tftplocal/generic.vxml
Total sessions:                                 1
Sessions w/ stats:                              1
Currently connected incoming PSTN legs:         1
Currently connected outgoing PSTN legs:         0
Currently connected incoming VoIP legs:         0
Currently connected outgoing VoIP legs:         0
Placecalls in transit:                          0
Handouts in transit:                            0
Pending ASNL subscriptions:                     0
Pending ASNL unsubscriptions:                   0
Prompts playing (non-TTS):                      0
Recordings:                                     0
TTS prompts playing:                            0
```

For a description of the fields shown in the display above, see Table 38 on page 1363.

```
Router# show call application history app-level summary Application level history Info:
                                   Sessions                     Last Reset          
App Name                 Stats w/ Stats   Total      Errors     Time                
session                  N     0          0          0         
fax_hop_on               N     0          0          0         
clid_authen              N     0          0          0         
clid_authen_collect      N     0          0          0         
clid_authen_npw          N     0          0          0         
clid_authen_col_npw      N     0          0          0         
clid_col_npw_3           N     0          0          0         
clid_col_npw_npw         N     0          0          0         
Default                  N     0          0          0         
lib_off_app              N     0          0          0         
fax_on_vfc_onramp_app    N     0          0          0         
ram_record_replay        N     0          0          0         
authorize                N     0          0          0         
authen                   N     0          0          0         
smtp_record              N     0          0          0         
generic                  Y     2          2          4          *Jul  3 15:49:28
offramp                  N     0          0          0         
asr                      N     0          0          0
```

The table below describes the fields shown in the display.

Field

Description

App Name

Name of the voice application.

Stats

Whether statistics is enabled for this application.

If statistics is enabled, this field displays N until there is at least one active instance of the application.

Sessions w/ stats

Number of terminated application instances that the gauges represent.

Total

Total number of instances of the application.

Errors

Total number of errors for all instances of the application.

Last Reset Time

Time at which the statistics were last cleared with the clear call application stats command, or the gateway was restarted.

```
Router# show call application history app-level app-tag generic Application level history Info:
Application name:              generic
URL:                           tftp://10.10.10.113/tftplocal/generic.vxml
Total sessions:                2
Sessions w/ stats:             2
Last reset time:               *Jul  3 15:49:28 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                2        0         0        0       
Total legs connected:                      2        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                2        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            3          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            3          0          0         
Total media duration (in seconds):         3          0          0         
 Application Internal Service - Handoff
                                           Incoming   Outgoing  
Bridged handoffs:                          0          0         
Bridged handoffs returned:                 0          0         
Blind handoffs:                            0          0         
Handoffs failed:                           x          0         
 Application Internal Service - Placecall/transfer 
Placecall requests:                        0
Placecall successes:                       0
Placecall failures:                        0
 Application Internal Service - Document Read-Write 
                                           Read       Write     
Doc requests:                              0          0         
Doc successes:                             0          0         
Doc failures:                              0          0         
 Application Internal Service - Downloaded Script 
Script parse errors:                       0
 Application Internal Service - ASNL 
ASNL notifications:                        0             
                                           Subscription   Unsubscription
ASNL requests:                             0              0             
ASNL successes:                            0              0             
ASNL failures:                             0              0             
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            1
DTMFs long pound:                          0
Subscriber Interaction - ASR
ASRs not matched:                          0
ASRs matched:                              0
ASRs no input:                             0
 Subscriber Interaction - AAA
                                           Authentication Authorization 
AAA successes:                             0              1             
AAA failures:                              0              0
```

For a description of the fields shown in this display, see Table 41 on page 1379.

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application stats

Enables statistics collection for voice applications.

call application voice event-log

Enables event logging for a specific voice application.

clear call application stats

Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics.

show call application gateway-level

Displays gateway-level statistics for voice application instances.

show call application session-level

Displays event logs and statistics for voice application instances.

## show call application gateway-level

To display gateway-level statistics for voice application instances, use the show call application gateway-level command in privileged EXEC mode.

show call application { active | history } gateway-level

### Syntax Description

active

Displays statistics for active application instances.

history

Displays statistics for terminated application instances.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

To display statistics with this command, you must enable statistics collection with the call application stats command.

This command displays gauges and counters that are aggregated per gateway. The values represent all instances of all voice
                                    applications running on the gateway while statistics collection is enabled.

To reset application-level counters to zero and subtract the counters from the gateway-level statistics in history, use the clear call application stats command. Statistic counters continue accumulating in history until you use the clear call application stats command or the gateway reloads.

Statistics for an application are automatically cleared if the application is deleted with the no call application voice command or its script is reloaded with the call application voice load command.

## Examples

The following is sample output from the show call application gateway-level command using different keywords:

```
Router# show call application active gateway-level Gateway level statistics for active application sessions:
Sessions w/ stats:                              1
Currently connected incoming PSTN legs:         1
Currently connected outgoing PSTN legs:         0
Currently connected incoming VoIP legs:         0
Currently connected outgoing VoIP legs:         0
Placecalls in transit:                          0
Handouts in transit:                            0
Pending ASNL subscriptions:                     0
Pending ASNL unsubscriptions:                   0
Prompts playing (non-TTS):                      0
Recordings:                                     0
TTS prompts playing:                            0
```

The table below describes the fields shown in the display.

Field

Description

Sessions w/ stats

Number of active application instances that the gauges represent.

Currently connected incoming PSTN legs

Number of active call legs that are incoming from the PSTN.

Currently connected outgoing PSTN legs

Number of active call legs that are outgoing to the PSTN.

Currently connected incoming VoIP legs

Number of active call legs that are incoming from the IP network.

Currently connected outgoing VoIP legs

Number of active call legs that are outgoing to the IP network.

Placecalls in transit

Number of outgoing calls in progress for all active application instances. The value is decremented by one after the call
                                          is either set up or the setup fails.

Handouts in transit

Number of handoffs in progress for all active application instances. The value is decremented by one after the receiving
                                          application either hands back the application or rejects the handoff.

Pending ASNL subscriptions

Number of Application Subscribe Notify Layer (ASNL) subscription requests that are in progress for all active application
                                          instances.

Pending ASNL unsubscriptions

Number of ASNL unsubscription requests that are in progress for all active application instances.

Prompts playing (non-TTS)

Number of recorded prompts being played in all active application instances.

Recordings

Number of recordings being made in all active application instances.

TTS prompts playing

Number of text-to-speech (TTS) prompts playing in all active application instances.

```
Router# show call application history gateway-level Gateway level statistics for history application sessions:
Sessions w/ stats:             2
Last reset time:               *Jul  3 15:49:28 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                2        0         0        0       
Total legs connected:                      2        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                2        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            3          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            3          0          0         
Total media duration (in seconds):         3          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            1
DTMFs long pound:                          0
```

For a description of the fields shown with the history keyword, see the table above.

### Related Commands

Command

Description

call application stats

Enables statistics collection for voice applications.

clear call application stats

Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics.

show call application app-level

Displays application-level statistics for voice applications.

show call application session-level

Displays event logs and statistics for voice application instances.

## show call application interface

To display event logs and statistics for application interfaces, use the show call application interface command in privileged EXEC mode.

show call application interface [ summary |  { aaa | asr | flash | http | ram | rtsp | smtp | tftp | tts } [ server server ] [ event-log | info | summary ]]

### Syntax Description

summary

(Optional) Displays a short summary of all interface types or the selected interface.

aaa

Authentication, authorization, and accounting (AAA) interface type.

asr

Automatic speech recognition (ASR) interface type.

flash

Flash memory of the Cisco gateway.

http

Hypertext Transfer Protocol (HTTP) interface type.

ram

Memory of the Cisco gateway.

rtsp

Real Time Streaming Protocol (RTSP) interface type.

smtp

Simple Mail Transfer Protocol (SMTP) interface type.

tftp

Trivial File Transfer Protocol (TFTP) interface type.

tts

Text-to-speech (TTS) interface type.

server server

(Optional) Displays event logs or statistics for the specified server.

event-log

(Optional) Displays event logs for the selected interface type or server.

info

(Optional) Displays statistics for the selected interface type or server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

If you use the server keyword, only statistics or event logs for that server display. To display event logs or statistics with this command, you
                              must enable statistics and event logging with the call application interface event-log and call application interface stats command, respectively. To reset statistic counters to zero and clear the event logs in history, use the clear call application interface command.

## Examples

The following is sample output from the show call application interface command using different keywords:

```
Router# show call application interface summary Aggregated statistics for http service:
Stats last reset time *Jul  3 15:24:48 PST
Read requests:                   3
Read successes:                  0
Read failures:                   3
Read aborts:                     0
Total bytes read:                0
Write requests:                  0
Write successes:                 0
Write failures:                  0
Write aborts:                    0
Total bytes written:             0
Aggregated statistics for tts service:
Stats last reset time *Jul  3 15:24:48 PST
Read requests:                   0
Read successes:                  0
Read failures:                   0
Read aborts:                     0
Aggregated statistics for asr service:
Stats last reset time *Jul  3 15:24:48 PST
Read requests:                   0
Read successes:                  0
Read failures:                   0
Read aborts:                     0
Aggregated statistics for tftp service:
Stats last reset time *Jul  3 15:24:48 PST
Read requests:                   3
Read successes:                  2
Read failures:                   0
Read aborts:                     1
Total bytes read:                145888
Router# show call application interface tftp summary Aggregated statistics for tftp service:
Stats last reset time *Jul  3 15:24:48 PST
Read requests:                   3
Read successes:                  2
Read failures:                   0
Read aborts:                     1
Total bytes read:                145888
Server Name          Stats Error Count            Event Log
172.19.139.145       Y     0                      Y 
speech-serv          Y     0                      N 
Router# show call application interface tftp Server name:         172.19.139.145
Statistics:
Last reset time *Jul  3 16:08:13 PST
Read requests:                   1
Read successes:                  2
Read failures:                   0
Read aborts:                     1
Total bytes read:                145888
Event log: 
Last reset time *Jul  3 16:08:13 PST
buf_size=50K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
172.19.139.145:1057277293:53:INFO: ID = 6549D9E0: Read requested for URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277295:54:INFO: ID = 6549D9E0: Streamed read transaction Successful URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277306:59:INFO: ID = 649A0320: Streamed read transaction Successful URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277317:65:INFO: ID = 650922A8: Read request aborted for URL = tftp://172.19.139.145/audio/ch_welcome.au
--------------------------------------------------------------------------------
Router# show call application interface tftp event-log Server name:         172.19.139.145
Event log: 
Last reset time *Jul  3 16:08:13 PST
buf_size=50K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
172.19.139.145:1057277293:53:INFO: ID = 6549D9E0: Read requested for URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277295:54:INFO: ID = 6549D9E0: Streamed read transaction Successful URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277306:59:INFO: ID = 649A0320: Streamed read transaction Successful URL = tftp://172.19.139.145/audio/ch_welcome.au
172.19.139.145:1057277317:65:INFO: ID = 650922A8: Read request aborted for URL = tftp://172.19.139.145/audio/ch_welcome.au
--------------------------------------------------------------------------------
Router# show call application interface tftp info Server name:         172.19.139.145
Statistics:
Last reset time *Jul  3 16:08:13 PST
Read requests:             3
Read successes:            2
Read failures:             0
Read aborts:               1
Total bytes read:                145888
--------------------------------------------------------------------------------
```

The table below describes the significant fields shown in the display.

Field

Description

Last reset time

Time at which the statistics were last cleared with the clear call application interface command, or the gateway was restarted.

Read requests

Total number of read requests from applications to this interface type.

Read successes

Number of successful read requests from applications to this interface type.

Read failures

Number of failed read requests from applications to this interface type.

Read aborts

Number of aborted read requests from applications to this interface type.

Total bytes read

Total number of bytes that the application read from this interface type.

Server name

Name of the specific server.

Stats

Whether statistics are enabled for this server.

Error Count

Total number of errors for this server.

Event Log

Whether event logging is enabled for this server.

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application interface stats

Enables statistics collection for application interfaces.

clear call application interface

Clears application interface statistics and event logs.

## show call application services registry

To display a one-line summary of all TCL IVR 2.0 application sessions that have registered as a service, use the show call application services registry command in user EXEC or privileged EXEC mode.

show call application services registry

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The services registry is a database that keeps track of every TCL IVR 2.0 application instance that registers as a service.
                                    Other TCL applications can then find and communicate with any registered application.

A TCL session is not registered as a service through a Cisco IOS command. A running instance of a TCL IVR 2.0 application
                                    registers itself as a service with the TCL service register command. For information about the service register command, refer
                                    to the TCL IVR API Version 2.0 Programmer’s Guide .

## Examples

The following is sample output for this command:

```
Router# show call application services registry There are 1 Registered Services
  Service Name         Session ID  Session Name
  data_service                  4  s1
```

The table below describes significant fields in the display.

Field

Description

Service Name

Name specified by the TCL service register command.

Session ID

ID of the session that registered as this service. You can use this ID in the show call application sessions id command to view details about this session.

Session Name

Name configured by the call application session start command, if the session was started on the gateway rather than by an incoming call.

### Related Commands

Command

Description

call application session start (global configuration)

Starts a new instance (session) of a TCL application from global configuration mode.

call application session start (privileged EXEC)

Starts a new instance (session) of a TCL application from privileged EXEC mode.

call application session stop

Stops a voice application session that is running.

show call application sessions

Displays summary or detailed information about voice application sessions.

## show call application session-level

To display event logs and statistics for individual voice application instances, use the show call application session-level command in privileged EXEC mode.

show call application { active | history } session-level [ summary |  [ app-tag application-name | last [number] | session-id session-id ] [ event-log | info ]]

### Syntax Description

active

Displays event logs or statistics for active application instances.

history

Displays event logs or statistics for inactive application instances in the history table.

summary

Displays a summary of each application instance.

app-tag application-name

Name of a specific voice application. Output displays event logs or statistics for that voice application.

last

(Optional) Displays event logs or statistics for the most recent instance.

number

(Optional) Displays event logs or statistics for this number of most recent previous instances.

session-id session-id

Identifies a specific application instance. Output displays event logs or statistics for that instance.

event-log

(Optional) Displays event logs for application instances.

info

(Optional) Displays statistics for application instances.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

To display event logs or statistics with this command, you must enable event logging and statistics with the call application event-log and call application stats command, respectively.

This command displays gauges and counters that are aggregated per application instance. The values represent an individual
                                    instance running on the gateway while statistics collection is enabled.

The number of records that are included when using the history keyword depends on the settings of the call application history session max-records and call application history session retain-timer commands.

## Examples

The following is sample output from the show call application session-level command using different keywords and arguments:

```
Router# show call application active session-level summary SID  Application Name       Stat Err Cnt    Log Start Time                     
5    generic                Y    6          Y   *Jul  3 15:19:4
6    generic                Y    3          Y   *Jul  3 15:19:5
Router# show call application active session-level last Session Info:
Session id:          6
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:19:53 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs currently connected:                  1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                0        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            4          0          0         
Media actives:                             0          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            4          0          0         
Total media duration (in seconds):         0          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            3
DTMFs long pound:                          0
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
6:1057274393:472:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
6:1057274393:473:INFO: Incoming Telephony call received, LegID = 10
6:1057274393:474:INFO: LegID = 10: Calling = 4084644753, called = 52927, dial peer = 1 
6:1057274393:475:INFO: LegID = 10: Leg State = LEG_INCCONNECTED 
6:1057274393:478:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
6:1057274408:517:INFO: Script received event = "error.badfetch"
Router# show call application active session-level info Session Info:
Session id:          5
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:19:44 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs currently connected:                  1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                0        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            9          0          0         
Media actives:                             0          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            9          0          0         
Total media duration (in seconds):         0          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            8
DTMFs long pound:                          0
Session Info:
Session id:          6
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:19:53 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP     
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                3        0         0        0      
Total legs connected:                      3        0         0        0      
Legs currently connected:                  1        0         0        0      
Legs handed in:                            0        0         0        0      
Legs handed in returned back:              0        0         0        0      
Legs handed out:                           0        0         0        0      
Legs handed out came back:                 0        0         0        0      
Legs disconnected normally:                0        0         0        0      
Legs disconnected for user error:          0        0         0        0      
Legs disconnected for system error:        0        0         0        0      
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            7          0          0         
Media actives:                             0          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            7          0          0         
Media duration (in seconds):               0          0          0         
 Application Internal Service - Handoff
                                           Incoming   Outgoing 
Bridged handoffs:                          0          0        
Bridged handoffs returned:                 0          0        
Blind handoffs:                            0          0        
Handoffs in transit:                       x          0        
Handoffs failed:                           x          0        
 Application Internal Service - Placecall/transfer
Placecall requests:                        0
Placecall successes:                       0
Placecall failures:                        0
Placecalls in transit:                     0
 Application Internal Service - Document Read-Write
                                           Read       Write    
Doc requests:                              0          0        
Doc successes:                             0          0        
Doc failures:                              0          0        
 Application Internal Service - Downloaded Script
Script parse errors:                       0
 Application Internal Service - ASNL
ASNL notifications:                        0            
                                           Subscription   Unsubscription
ASNL requests:                             0              0            
ASNL successes:                            0              0            
ASNL pendings:                             0              0            
ASNL failures:                             0              0            
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            6
DTMFs long pound:                          0
 Subscriber Interaction - ASR
ASRs not matched:                          0
ASRs matched:                              0
ASRs no input:                             0
 Subscriber Interaction - AAA
                                           Authentication Authorization
AAA successes:                             0              0            
AAA failures:                              0              0            
Router# show call application active session-level event-log Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
5:1057274384:454:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
5:1057274384:455:INFO: Incoming Telephony call received, LegID = D
5:1057274384:456:INFO: LegID = D: Calling = 4085550198, called = 52927, dial peer = 1 
5:1057274384:457:INFO: LegID = D: Leg State = LEG_INCCONNECTED 
5:1057274384:460:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
5:1057274384:462:ERR : Prompt play setup failure.
5:1057274384:463:INFO: Script received event = "error.badfetch"
5:1057274389:464:INFO: Timed out waiting for user DTMF digits, no user input.
5:1057274389:465:INFO: Script received event = "noinput"
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
6:1057274393:472:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
6:1057274393:473:INFO: Incoming Telephony call received, LegID = 10
6:1057274393:474:INFO: LegID = 10: Calling = 4084644753, called = 52927, dial peer = 1 
6:1057274393:475:INFO: LegID = 10: Leg State = LEG_INCCONNECTED 
6:1057274393:478:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
6:1057274393:480:ERR : Prompt play setup failure.
6:1057274393:481:INFO: Script received event = "error.badfetch"
6:1057274398:488:INFO: Timed out waiting for user DTMF digits, no user input.
6:1057274398:489:INFO: Script received event = "noinput"
6:1057274398:490:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
Router# show call application active session-level app-tag generic Session Info:
Session id:          5
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:19:44 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs currently connected:                  1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                0        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            16         0          0         
Media actives:                             0          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            17         0          0         
Total media duration (in seconds):         0          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            16
DTMFs long pound:                          0
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
5:1057274384:454:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
5:1057274384:455:INFO: Incoming Telephony call received, LegID = D
5:1057274384:456:INFO: LegID = D: Calling = 4085550198, called = 52927, dial peer = 1 
5:1057274384:457:INFO: LegID = D: Leg State = LEG_INCCONNECTED 
5:1057274384:460:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
5:1057274384:462:ERR : Prompt play setup failure.
5:1057274384:463:INFO: Script received event = "error.badfetch"
5:1057274389:464:INFO: Timed out waiting for user DTMF digits, no user input.
5:1057274389:465:INFO: Script received event = "noinput"
5:1057274389:466:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
Router# show call application active session-level session-id 7 Session Info:
Session id:          7
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:21:26 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs currently connected:                  1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                0        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            3          0          0         
Media actives:                             0          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            3          0          0         
Total media duration (in seconds):         0          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            2
DTMFs long pound:                          0
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
7:1057274486:662:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
7:1057274486:663:INFO: Incoming Telephony call received, LegID = 13
7:1057274486:664:INFO: LegID = 13: Calling = 4085550198, called = 52927, dial peer = 1 
7:1057274486:665:INFO: LegID = 13: Leg State = LEG_INCCONNECTED 
7:1057274486:668:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
Router# show call application history session-level summary SID  Application Name       Stat Err Cnt    Log Stop Time       Duration       
1    generic                Y    3          Y   *Jul  3 15:49:2 00:00:11
2    generic                Y    1          Y   *Jul  3 15:49:3 00:00:03
Router# show call application history session-level last Session Info:
Session id:          2
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:49:29 PST
Stop time:           *Jul  3 15:49:33 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                1        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            1          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            1          0          0         
Total media duration (in seconds):         0          0          0         
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
2:1057276169:28:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
2:1057276169:29:INFO: Incoming Telephony call received, LegID = 4
2:1057276169:30:INFO: LegID = 4: Calling = 4085550198, called = 52927, dial peer = 1 
2:1057276169:31:INFO: LegID = 4: Leg State = LEG_INCCONNECTED 
2:1057276169:34:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
2:1057276169:36:ERR : Prompt play setup failure.
2:1057276169:37:INFO: Script received event = "error.badfetch"
2:1057276173:39:INFO: Script received event = "telephone.disconnect.hangup"
2:1057276173:40:INFO: LegID = 4: Call disconnected, cause = normal call clearing (16)
2:1057276173:43:INFO: Session done, terminating cause = 
Router# show call application history session-level event-log Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
1:1057276157:3:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
1:1057276157:4:INFO: Incoming Telephony call received, LegID = 1
1:1057276157:5:INFO: LegID = 1: Calling = 4085550198, called = 52927, dial peer = 1 
1:1057276157:6:INFO: LegID = 1: Leg State = LEG_INCCONNECTED 
1:1057276157:9:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
1:1057276160:12:ERR : Prompt play setup failure.
1:1057276160:13:INFO: Script received event = "error.badfetch"
1:1057276165:14:INFO: Timed out waiting for user DTMF digits, no user input.
1:1057276165:15:INFO: Script received event = "noinput"
1:1057276165:16:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
1:1057276165:18:ERR : Prompt play setup failure.
1:1057276165:19:INFO: Script received event = "error.badfetch"
1:1057276168:21:INFO: Script received event = "telephone.disconnect.hangup"
1:1057276168:22:INFO: LegID = 1: Call disconnected, cause = normal call clearing (16)
1:1057276168:25:INFO: Session done, terminating cause = 
Event log:
buf_size=25K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
2:1057276169:28:INFO: Session started for App-type = generic, URL = tftp://demo/scripts/primary/generic.vxml
2:1057276169:29:INFO: Incoming Telephony call received, LegID = 4
2:1057276169:30:INFO: LegID = 4: Calling = 4085550198, called = 52927, dial peer = 1 
2:1057276169:31:INFO: LegID = 4: Leg State = LEG_INCCONNECTED 
2:1057276169:34:INFO: Playing prompt #1: http://172.19.139.145/audio/ch_welcome.au
2:1057276169:36:ERR : Prompt play setup failure.
2:1057276169:37:INFO: Script received event = "error.badfetch"
2:1057276173:39:INFO: Script received event = "telephone.disconnect.hangup"
2:1057276173:40:INFO: LegID = 4: Call disconnected, cause = normal call clearing (16)
2:1057276173:43:INFO: Session done, terminating cause = 
Router# show call application history session-level info Session Info:
Session id:          1
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:49:17 PST
Stop time:           *Jul  3 15:49:28 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                1        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            2          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            2          0          0         
Total media duration (in seconds):         3          0          0         
 Subscriber Interaction - DTMF
DTMFs not matched:                         0
DTMFs matched:                             0
DTMFs no input:                            1
DTMFs long pound:                          0
Session Info:
Session id:          2
Session name:        
Application name:    generic
Application URL:     tftp://demo/scripts/primary/generic.vxml
Start time:          *Jul  3 15:49:29 PST
Stop time:           *Jul  3 15:49:33 PST
Statistics:
 Subscriber Service - Call
                                                  PSTN               VOIP      
                                           Incoming Outgoing  Incoming Outgoing
Legs setup:                                1        0         0        0       
Total legs connected:                      1        0         0        0       
Legs handed in:                            0        0         0        0       
Legs handed in returned back:              0        0         0        0       
Legs handed out:                           0        0         0        0       
Legs handed out came back:                 0        0         0        0       
Legs disconnected normally:                1        0         0        0       
Legs disconnected for user error:          0        0         0        0       
Legs disconnected for system error:        0        0         0        0       
 Subscriber Service - Media
                                           Play       Record     TTS       
Media attempts:                            1          0          0         
Media successes:                           0          0          0         
Media aborts:                              0          0          0         
Media failures:                            1          0          0         
Total media duration (in seconds):         0          0          0
```

The table below describes significant fields in the displays.

These fields display for the show call application session-level , show call application app-level , and show call application gateway-level commands. At the session level, the fields apply to a single application instance. At the application level, the fields apply
                                          to all instances of an application. At the gateway level, the fields apply to all instances of all applications.

Field

Description

Session id

Session ID assigned to the instance when it became active.

Session name

Name of the session defined with the call application session start command.

Application name

Name of the application defined with the call application voice command.

Application URL

Location of the application script defined with the call application voice command.

Start time

Time at which the session started.

Subscriber Service -- Call

Legs setup

Number of calls setup (indications and requests) by an application instance.

Total legs connected

Number of calls connected by an application instance.

Legs currently connected

Number of calls currently connected by an application instance at any moment.

Legs handed in

Number of call legs received as an incoming handoff from another application.

Legs handed in returned back

Number of call legs received as an incoming handoff from another application that were returned to the other application.

Legs handed out

Number of call legs handed off to another application.

Legs handed out came back

Number of call legs handed off to another application that were returned by the other application.

Legs disconnected normally

Number of incoming and outgoing calls disconnected for normal causes.

Legs disconnected for user error

Number of incoming calls disconnected for call failure reasons, such as no answer or busy.

Legs disconnected for system error

Number of incoming calls disconnected for system failure reasons, such as no resources.

Subscriber Service -- Media

Media attempts

Number of prompt playouts, recordings, and text-to-speech (TTS) attempts on call legs in this application instance.

Media actives,

Number of prompt playouts, recordings, and TTS prompts currently active on call legs in an application instance.

Media successes

Number of prompt playouts, recordings, and TTS prompts that were successful on call legs in an application instance.

Media aborts

Number of prompt playouts, recordings, and TTS prompts that were aborted by the caller on call legs in an application instance.

Media failures

Number of prompt playouts, recording, and TTS attempts that failed on call legs in an application instance.

Total media duration

Total duration, in seconds, of prompt playing, recording, or TTS.

Application Internal Service -- Handoff

Bridged handoffs, incoming

Number of handoffs received with callback (bridged transfers) in an application instance.

Bridged handoffs, outgoing

Number of handoffs placed with callback (bridged transfers) by an application instance.

Bridged handoffs returned, incoming

Number of incoming bridged handoffs that were returned by an application instance.

Bridged handoffs returned, outgoing

Number of outgoing bridged handoffs that were returned to an application instance.

Blind handoffs, incoming

Number of handoffs received with no callback (blind transfers) in an application instance.

Blind handoffs, outgoing

Number of handoffs placed with no callback (blind transfers) by an application instance.

Handoffs in transit 1

Number of handoffs in progress for an application instance. The value is decremented by one after the receiving application
                                          either hands back the application or rejects the handoff.

Handoffs failed

Number of handoffs that failed (bridged and blind) in an application instance.

Application Internal Service -- Placecall/transfer

Placecall requests

Number of outgoing call setup requests made by an application instance.

Placecall successes

Number of outgoing calls placed by an application instance.

Placecall failures

Number of outgoing call setup requests that failed for an application instance.

Place calls in transit

Number of outgoing calls in progress for an application. The value is decremented by one after the call is either set up
                                          or the setup fails.

Application Internal Service -- Document Read-Write

Doc requests

Number of document fetch and submit requests.

Doc successes

Number of successful document fetches and submits.

Doc failures

Number of document fetch and submit failures.

Application Internal Service -- Downloaded Script

Script parse errors

Number of semantic errors seen by an application instance.

Application Internal Service -- ASNL

ASNL notifications

Number of Application Subscribe Notify Layer (ASNL) notifications received from servers.

ASNL requests

Number of subscribe or unsubscribe requests made by an application instance.

ASNL successes

Number of subscribe or unsubscribe requests that succeeded for an application instance.

ANSL failures

Number of subscribe or unsubscribe requests that failed for an application instance.

Subscriber Interaction --- DTMF

DTMFs not matched

Number of DTMF patterns input by a caller that were not matched in an application instance.

DTMFs matched

Number of DTMF patterns input by a caller that were matched in an application instance.

DTMFs no input

Number of "no input" notifications received (includes DTMF timeouts).

DTMFs long pound

Number of long-pound interrupts from a caller seen by an application instance.

Subscriber Interaction -- ASR

ASR not matched

Number of automatic speech recognition (ASR) phrases from a caller that were not matched in an application instance.

ASR matched

Number of automatic speech recognition (ASR) phrases from a caller that were matched in an application instance.

ASR no inputs

Number of "no input" notifications received from ASR servers.

Subscriber Interaction -- AAA Authentication

AAA authentication successes

Number of AAA authentication successes.

AAA authentication failures

Number of AAA authentication failures because of invalid passwords.

Subscriber Interaction -- AAA Authorizations

AAA authorization successes

Number of AAA authorization successes.

AAA authorization failures

Number of AAA authorization failures.

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application history session max-records

Sets the maximum number of application instance records saved in history.

call application history session retain-timer

Sets the maximum number of minutes for which application instance records are saved in history.

call application stats

Enables statistics collection for voice applications.

call application voice event-log

Enables event logging for a specific voice application.

show call application app-level

Displays application-level statistics for voice applications.

show call application gateway-level

Displays gateway-level statistics for voice application instances.

## show call application sessions

To display summary or detailed information about all running or stopped voice application sessions, use the show call application sessions command in user EXEC or privileged EXEC mode.

show call application sessions [ callid call-id | id session-id | name instance-name ]

### Syntax Description

callid call-id

(Optional) Call-leg ID of an active call that is being controlled by the session.

id session-id

(Optional) Session ID for the specific application instance.

name instance-name

(Optional) Name assigned to the instance with the call application session start command.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

A specific application session is identified by one of three different methods: call ID, session ID, or instance name.

If a specific session is identified by a callid , id , or name keyword, this command displays information about that specific session only. If you do not use a keyword, this command displays
                                    a one-line summary of all sessions, not just those sessions that are started by the call application session start command.

This command lists all running TCL IVR 2.0 and VoiceXML application sessions and TCL sessions that are stopped. A session
                                    displays a state of "stopped" if you intentionally stop it with the call application session stop or no call application session start command, or because there is a syntax error that prevents the script from running. This is the case only if the session is
                                    started with the call application session start command through global configuration mode.

If a session is started with the call application session start command in privileged EXEC mode, it is not tracked by the system and is therefore not shown as stopped in the output of the show call application sessions command.

## Examples

The following is sample output from this command:

```
Router# show call application sessions TCL Sessions
    There are 1 active TCL sessions
     SID  Name        Called     Calling                App Name               Legs
       5  serv1                                         sample_service        
VXML Sessions
    No running VXML sessions
Stopped Sessions
  Instance Name        App Name             State               
  my_instance1         sample               stopped
```

The table below describes significant fields in the display.

Field

Description

SID

Session identifier for active sessions.

Name

Session name that was configured with the call application session start command.

Called

Called number for active calls that are using the session.

Calling

Calling number for active calls that are using the session.

App Name

Name of the application for which the instance was created.

Legs

Any active call legs that are controlled by the session.

State

Shows "stopped" for any session that is no longer running, provided that the session is started with the call application session start command in global configuration mode.

The following is sample output for a session named serv1:

```
Router# show call aplication sessions name serv1 Session named serv1 is in the start list in state running
  It is configured to start on GW reboot
  The application it runs is sample_service
  Handle is TCL_HAND*1653710732*0*3193204
TCL Session ID B
                 App: sample_service
                 URL: tftp://dev/demo/scripts/sample_service.tcl
        Session name: serv1
      Session handle: TCL_HAND*1653710732*0*3193204
           FSM State: start_state
    ID for 'show call active voice id' display: 0
                Legs:
            Services: data_service
```

The table below describes significant fields in the display.

Field

Description

App

Name of the application for which the instance was created.

URL

Location of the script used for the application as specified with the call application voice command.

Session name

Session name that was configured with the call application session start command.

Session handle

Handle that is returned from the TCL mod_handle infotag. A session handle is used in a TCL script on a Cisco gateway to send
                                          messages to other sessions.

FSM State

Current state in the TCL IVR 2.0 finite-state machine, as specified with the TCL fsm setstate command in the script.

ID for ‘show call active voice id’ display:

Call identifier.

Legs

Any active call legs that are controlled by this session.

Services

Service name for the session if it registered as a service with the TCL service register command in the script. You can display
                                          a list of all registered services with the show call application services registry command.

### Related Commands

Command

Description

call application session start (global configuration)

Starts a new instance (session) of a TCL application from global configuration mode.

call application session start (privileged EXEC)

Starts a new instance of a TCL application from privileged EXEC mode.

call application session stop

Stops a voice application session that is running.

show call application services registry

Displays a one-line summary of all registered services.

## show call application voice

To display information about voice applications, use the show call application voice command in EXEC mode.

show call application voice [ name | summary ]

### Syntax Description

name

(Optional) Name of the desired voice application. Output displays information about that application.

summary

(Optional) Output displays a one-line summary of each voice application.

### Command Default

If both the name argument and summary keyword are omitted, command output displays detailed information about all interactive voice response (IVR) applications.

### Command Modes

EXEC (#)

## Command History

Release

Modification

11.3(6)NA2

This command was introduced.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

12.1(5)T

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB

This command was modified to support VoiceXML applications.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, Cisco 3745, and Cisco 7200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

12.3(14)T

New output was added relating to the SCCP Telephony Control Application (STCAPP).

### Usage Guidelines

The show call application voice command displays a detailed description of each configured application.

If the name of a specific application is entered, the command displays detailed information about only that application.

If the summary keyword is entered, the command displays a one-line summary about each application.

If STCAPP is enabled, the summary command displays STCAPP as an available call application.

If an asterisk is displayed next to the application name when the summary keyword is used, the application is configured, but not running. Normally this is because the application was not successfully
                              loaded, for example:

```
name                 description
*vapptest2           flash:helloworld.vxml
```

TCL scripts and VoiceXML documents can be stored in any of the following locations: TFTP, FTP, or HTTP servers; Flash memory
                              of the gateway; or the removable disks of the Cisco 3600 series. The audio files that they use can be stored in any of these
                              locations and on RTSP servers.

## Examples

The following example shows the output for the session Toolkit Command Language (TCL) script:

```
Router# show call application voice session Application session
    The script is compiled into the image
    It has 0 calls active.
    Interpreted by infrastructure version 2.0
The TCL Script is:
------------------
# app_session.tcl
#----------------------------------
# August 1999, Saravanan Shanmugham
#
# Copyright (c) 1998, 1999, 2000, 2001 by cisco Systems, Inc.
# All rights reserved.
#----------------------------------
#
# This tcl script mimics the default SESSION app
#
# If DID is configured, just place the call to the dnis
# Otherwise, output dial-tone and collect digits from the
# caller against the dial-plan.
#
# Then place the call. If successful, connect it up, otherwise
# the caller should hear a busy or congested signal.
# The main routine just establishes the statemachine and then exits.
# From then on the system drives the statemachine depending on the
# events it recieves and calls the appropriate tcl procedure
#---------------------------------
#   Example Script
#---------------------------------
proc init { } {
    global param
    set param(interruptPrompt) true
    set param(abortKey) *
    set param(terminationKey) #
}
proc act_Setup { } {
    global dest
    global beep
    set beep 0
    if { [infotag get leg_isdid] } {
        set dest [infotag get leg_dnis]
        leg proceeding leg_incoming
        leg setup $dest callInfo leg_incoming
        fsm setstate PLACECALL
    } else {
        leg setupack leg_incoming
        playtone leg_incoming tn_dial
        set param(dialPlan) true
        leg collectdigits leg_incoming param
    }
}
proc act_GotDest { } {
    global dest
    set status [infotag get evt_status]
    if {  $status == "cd_004" } {
        set dest [infotag get evt_dcdigits]
        leg proceeding leg_incoming
        leg setup $dest callInfo leg_incoming
    } else {
        puts "\nCall [infotag get con_all] got event $status collecting destina"
        call close
    }
}
proc act_CallSetupDone { } {
    global beep
    set status [infotag get evt_status]
    if { $status == "ls_000"} {
        set  creditTimeLeft [infotag get leg_settlement_time leg_all]
        if { ($creditTimeLeft == "unlimited") ||
             ($creditTimeLeft == "uninitialized") } {
            puts "\n Unlimited Time"
        } else {
            # start the timer for ...
            if { $creditTimeLeft < 10 } {
                set beep 1
                set delay $creditTimeLeft
            } else {
                set delay [expr $creditTimeLeft - 10]
            }
            timer start leg_timer $delay leg_incoming
        }
    } else {
        puts "Call [infotag get con_all] got event $status collecting destinati"
        call close
    }
}
proc act_Timer { } {
    global beep
    global incoming
    global outgoing
    set incoming [infotag get leg_incoming]
    set outgoing [infotag get leg_outgoing]
    if { $beep == 0 } {
        #insert a beep ...to the caller
        connection destroy con_all
        set beep 1
    } else {
        connection destroy con_all
        fsm setstate LASTWARN
    }
}
proc act_LastWarn { } {
    media play leg_incoming flash:out_of_time.au
}
proc act_Destroy { } {
    media play leg_incoming flash:beep.au
}
proc act_Beeped { } {
    global incoming
    global outgoing
    connection create $incoming $outgoing
}
proc act_ConnectedAgain { } {
    timer start leg_timer 10 leg_incoming
}
proc act_Ignore { } {
# Dummy
    puts "Event Capture"
}
proc act_Cleanup { } {
    call close
}
init
#----------------------------------
#   State Machine
#------------------
  set fsm(any_state,ev_disconnected)  "act_Cleanup              same_state"
  set fsm(CALL_INIT,ev_setup_indication) "act_Setup            GETDEST"
  set fsm(GETDEST,ev_collectdigits_done)  "act_GotDest          PLACECALL"
  set fsm(PLACECALL,ev_setup_done)    "act_CallSetupDone    CALLACTIVE"
  set fsm(CALLACTIVE,ev_leg_timer)    "act_Timer            INSERTBEEP"
  set fsm(INSERTBEEP,ev_destroy_done) "act_Destroy          same_state"
  set fsm(INSERTBEEP,ev_media_done)   "act_Beeped           same_state"
  set fsm(INSERTBEEP,ev_create_done)    "act_ConnectedAgain   CALLACTIVE"
  set fsm(LASTWARN,ev_destroy_done)     "act_LastWarn        CALLDISCONNECT"
  set fsm(CALLACTIVE,ev_disconnected)   "act_Cleanup         CALLDISCONNECT"
  set fsm(CALLDISCONNECT,ev_disconnected)   "act_Cleanup         same_state"
  set fsm(CALLDISCONNECT,ev_media_done)     "act_Cleanup         same_state"
  set fsm(CALLDISCONNECT,ev_disconnect_done) "act_Cleanup         same_state"
  set fsm(CALLDISCONNECT,ev_leg_timer)      "act_Cleanup         same_state"
  fsm define fsm CALL_INIT
```

The following is sample output for the summary keyword:

```
Router# show call application voice summary name                 description
session              Basic app to do DID, or supply dialtone.
fax_hop_on           Script to talk to a fax redialer
clid_authen          Authenticate with (ani, dnis)
clid_authen_collect  Authenticate with (ani, dnis), collect if that fails
clid_authen_npw      Authenticate with (ani, NULL)
clid_authen_col_npw  Authenticate with (ani, NULL), collect if that fails
clid_col_npw_3       Authenticate with (ani, NULL), and 3 tries collecting
clid_col_npw_npw     Authenticate with (ani, NULL) and 3 tries without pw
DEFAULT              Default system session application
lib_off_app          Libretto Offramp
TCL Script Version 2.0 supported.
TCL Script Version 1.1 supported.
Voice Browser Version 2.0 for VoiceXML 1.0 & 2.0 supported.
```

The following is sample output for the summary keyword when STCAPP is enabled:

```
Router# show call application voice summary SERVICES (standalone applications):
  name                      type            description
  ipsla-responder           Tcl Script      builtin:app_test_rcvr_script.tcl  
  clid_authen               Tcl Script      builtin:app_clid_authen_script.tcl  
  clid_col_npw_npw          Tcl Script      builtin:app_clid_col_npw_npw_script.tcl  
  DEFAULT                   C Script        builtin:Session_Service.C  
  CTAPP                     C Script        builtin:CallTreatment_Service.C  
  clid_authen_col_npw       Tcl Script      builtin:app_clid_authen_col_npw_script.tcl  
  fax_hop_on                Tcl Script      builtin:app_fax_hop_on_script.tcl  
  ipsla-testcall            Tcl Script      builtin:app_test_place_script.tcl  
  clid_authen_npw           Tcl Script      builtin:app_clid_authen_npw_script.tcl  
  session                   Tcl Script      builtin:app_session_script.tcl  
  clid_authen_collect       Tcl Script      builtin:app_clid_authen_collect_script.tcl  
  clid_col_npw_3            Tcl Script      builtin:app_clid_col_npw_3_script.tcl  
  lib_off_app               CCAPI           Libretto Offramp
  DEFAULT.C.OLD             CCAPI           Obsolete system session application
  stcapp                    CCAPI           SCCP Call Control Application
  MGCPAPP                   CCAPI           MGCP Application
```

The following is sample output for the stcapp keyword when the STCAPP is enabled:

```
Router# show call application voice stcapp App Status:              Active
CCM Status:              UP
CCM Group:               2
Registration Mode:   	   CCM
Total Devices:           5
Total Calls in Progress: 0
Total Call Legs in Use:  0
```

The following is sample output from the show call application voice command for a VoiceXML application named vapptest1:

```
Router# show call application voice vapptest1 VXML Application vapptest1
    URL=flash:demo0.vxml
    Security not trusted
    No languages configured
    It has: 0 calls active.
          0 incoming calls
          0 calls handed off to it
          0 call transfers initiated
          0 pages loaded,  0 successful
          0 prompts played
          0 recorded messages
    Interpreted by Voice Browser Version 2.0 for VoiceXML 1.0 & 2.0.
The VXML Script is:
------------------
<?xml version="1.0"?>
<vxml version="1.0">
  <form>
	    <block>
      <audio src="flash:demo0.au"/>
    </block>
  </form>
</vxml>
```

The table below describes the fields shown in the show call application voice display:

Field

Description

URL

Location of the document used by the application.

It has: n calls active.

Number of calls that are using this application.

incoming calls

Number of incoming public switched telephone network (PSTN) or IP calls that invoked this application.

calls handed off to it

Number of calls that were handed off to this application by another TCL or VoiceXML application.

call transfers initiated

Number of call transfers that were initiated by this application.

pages loaded

Number of VoiceXML pages that were loaded by the application.

successful

Number of VoiceXML pages that were completed.

prompts played

Number of audio prompts that were played by the application.

recorded messages

Number of audio recordings made by the VoiceXML application.

Interpreted by

Programming language used by the application.

The TCL or VoiceXML Script is

Content of the VoiceXML document or TCL script.

### Related Commands

Command

Description

call application voice

Defines the name to be used for an application and indicates the location of the appropriate IVR script to be used with the
                                          application.

call application voice load

Reloads the designated TCL script or VoiceXML document.

## show call fallback cache

To display the current Calculated Planning Impairment Factor (ICPIF) estimates for all IP addresses in cache, use the show call fallback cache command in EXEC mode.

show call fallback cache [ip-address]

### Syntax Description

ip - address

(Optional) Specific IP address.

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Use this command to clear all entries in the cache.

## Examples

The following example displays output from this command:

```
Router# show call fallback cache Probe   IP Address      Codec   Delay   Loss    ICPIF   Reject  Accept
-----   ----------      -----   -----   ----    -----   ------  ------
1       1.1.1.4         g729r8  40      0					0       0       9
2       122.24.56.25    g729r8  148					10      5       1       4
2 active probes
Field                      Description
-------                    ------------
Probe                      Probe number
IP Address                 IP Address to which the probe is sent
Codec                      Codec Type of the probe
Delay                      Delay in milliseconds that the probe incurred
Loss                       Loss in % that the probe incurred
ICPIF                      Computed ICPIF value for the probe
Reject                     Number of times that calls of Codec Type <Codec>
                           were rejected to the IP Address
Accept                     Number of times that calls of Codec Type <Codec>
                           were accepted to the IP Address
active probes              Number of destinations being probed
Router# show call fallback cache 10.14.115.53 Probe   IP Address      Codec           ICPIF   Reject  Accept
-----   ----------      -----           -----   ------  ------
1       10.14.115.53     g729r8          0       0       2
1 active probes
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

show call fallback stats

Displays call fallback statistics.

## show call fallback config

To display the call fallback configuration, use the show call fallback config command in EXEC mode.

show call fallback config

### Syntax Description

This command has no arguments or keywords.

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following example displays output from the show call fallback config command:

```
Router# show call fallback config VoIP fallback config:
Fallback is ON
Using ICPIF threshold:
        ICPIF value timeout:20 seconds
        ICPIF threshold:20
Number of packets in a probe:20
IP precedence of probe packets:2
Fallback cache size:2 entries
Fallback cache timeout:240 seconds
Instantaneous value weight:65
MD5 Keychain:secret
```

The table below describes the fields shown in the show call fallback config display.

Field

Description

Fallback is

Lists enabled/disabled state of call fallback.

Using ICPIF threshold

ICPIF is configured to determine network traffic.

ICPIF value timeout

Lists probe timeout for collecting ICPIF information.

ICPIF threshold

Lists configured ICPIF threshold.

Number of packets in a probe

Lists number of configured packets per probe.

IP precedence of probe packets

Lists configured IP precedence for probes.

Fallback cache size

Number of allowed entries in call fallback cache.

Fallback cache timeout

Length of cache timeout, in seconds.

Instantaneous value weight

Lists weight configured for calculating cache entry based on new probe and last entry.

MD5 Keychain

MD5 authentication has been configured with a keychain of secret.

### Related Commands

Command

Description

call fallback monitor

Enables the monitoring of destinations without fallback to alternate dial peers.

show voice trunk-conditioning signaling

Enables fallback to alternate dial peers in case of network congestion.

## show call fallback stats

To display the call fallback statistics, use the show call fallback stats command in EXEC mode.

show call fallback stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600, Cisco 3600, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

To remove all values, use the clear call fallback stats command.

## Examples

The following example displays output from the show call fallback stats command:

```
Router# show call fallback stats VOIP Fallback Stats:
Total accepted calls:3
Total rejected calls:1
Total cache overflows:1
Field                      Description
-------                    ------------
Total accepted calls       Number of times that calls were successful over IP.
Total rejected calls       Number of times that calls were rejected over IP.
Total cache overflows      Number of times that the fallback cache overflowed and required pruning.
The table below describes the fields shown in the show call fallback stats display
```

Field

Description

Total accepted calls

Number of times that calls were successful over IP.

Total rejected calls

Number of times that calls were rejected over IP.

Total cache overflows

Number of times that the fallback cache overflowed and required pruning.

### Related Commands

Command

Description

clear call fallback stats

Clears the call fallback statistics.

show call fallback cache

Displays the current ICPIF estimates for all IP addresses in the cache.

## show call filter
                        	 components

To display the
                              		  components used for filtering calls, use the show call filter components
                              		  command in privileged EXEC mode.

show call filter components

### Command Default

No default behavior
                              		  or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This
                                          						command was introduced.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release
                                          						3.10S.

## Examples

The following
                              		  example shows the output from running the show call filter components command.
                              		  The GCFM is the generic call filter module, which is the internal module that
                              		  controls which components are filtered:

```
Router# show call filter components The following components registered in GCFM:
     ISDN
     VTSP
     CCAPI
     TGRM
     DIAL-PEER
     NUMBER-TRANSLATION
     SSAPP
     VOICE-IVR-V2
     H323
     SIP
     CRM
					TSP
     FAX-FOIP
     FAX-FMSP
     FAX-DMSP
     FAX-MSPI
     FAX-MTA
     DSPAPI
     MGCP
     DSMP
     H221
```

The table below
                              		  describes the significant fields shown in the display.

Field

Description

The
                                          					 following components registered in GCFM:

Shows which
                                          					 components are filtered in the generic call filter module.

### Related Commands

Command

Description

call filter match-list voice

Create a
                                          						call filter match list for debugging voice calls.

debug call filter inout

Display
                                          						the debug trace inside the GCFM.

debug condition match-list

Run a
                                          						filtered debug on a voice call.

outgoing port

Configure
                                          						debug filtering for the outgoing port.

show call filter match-list

Display
                                          						call filter match lists.

## show call filter
                        	 match-list

To display call
                              		  filter match lists, use the show call filter match-list command in privileged
                              		  EXEC mode.

show call filter match-list tag

### Syntax Description

tag

Numeric
                                          						label that uniquely identifies the match list.

### Command Default

No default behavior
                              		  or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This
                                          						command was introduced.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release
                                          						3.10S.

## Examples

The following
                              		  example shows an output from the show call filter match-list command:

```
Router# show call filter match-list ********************************************* 
call filter match-list 9 voice 
*********************************************
  incoming calling-number 50200
  incoming called-number 50201
  incoming signal local ipv4 10.0.101.22
  incoming signal remote ipv4  10.0.101.21
  incoming media local ipv4  10.0.101.22
  incoming media remote ipv4  10.0.101.21
  incoming dialpeer 502
  outgoing calling-number 50200
  outgoing called-number 50201
  outgoing port 6/0:D
  outgoing dialpeer 501
 debug condition match-list is set to EXACT_MATCH 
********************************************* 
call filter match-list 10 voice 
*********************************************
  incoming calling-number 50300
  incoming called-number 50301
  incoming signal local ipv4 10.0.101.22
  incoming signal remote ipv4  10.0.101.21
  incoming media local ipv4  10.0.101.22
  incoming media remote ipv4  10.0.101.21
  incoming dialpeer 504
  outgoing calling-number 50300
  outgoing called-number 50301
  outgoing port 6/1:D
  outgoing dialpeer 503
 debug condition match-list is set to EXACT_MATCH
```

The table below
                              		  describes the significant fields shown in the display.

Field

Description

call filter
                                          					 match-list 9 voice

Shows which
                                          					 match list is being displayed.

debug
                                          					 condition match-list is set to EXACT_MATCH

Shows
                                          					 whether the debug condition is set for exact match or partial match.

### Related Commands

Command

Description

call filter match-list voice

Create a
                                          						call filter match list for debugging voice calls.

debug call filter inout

Display
                                          						the debug trace inside the GCFM.

debug condition match-list

Run a
                                          						filtered debug on a voice call.

show call filter components

Display
                                          						the components used for filtering calls.

| all | Displays ITU-T, ATMF, and custom AAL2 profiles configured on the system. |
|---|---|
| itut | Displays ITU-T profiles configured on the system. |
| atmf | Displays ATMF profiles configured on the system. |
| custom | Displays custom profiles configured on the system. |
| profile - number | AAL2 profile number to display. Choices are as follows: For ITU-T: 1 = G.711 u-law 2 = G.711 u-law with silence insertion descriptor (SID) 7 = G.711 u-law and G.729ar8 For ATMF: None. ATMF is not supported. For custom: 100 = G.711 u-law and G.726r32 110 = G.711 u-law, G.726r32, and G.729ar8 |

| Release | Modification |
|---|---|
| 12.1(1)XA | This command was introduced on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |

| Field | Description |
|---|---|
| Coding type | Voice compression algorithm. |
| ITUT Profile Number | Predefined combination of one or more codec types configured for a digital signal processor (DSP). |
| Num entries | Number of profile elements. |
| Packet length | Sample size. |
| Profile Type | Category of codec types configured on DSP. Possible types are ITU-T, ATMF, and custom. |
| Red enable | Redundancy for type 3 packets. |
| SID Support | Silence insertion descriptor. |
| UUI max | Maximum sequence number on the voice packets. |
| UUI min | Minimum sequence number on the voice packets. |

| Command | Description |
|---|---|
| codec aal2-profile | Sets the codec profile for a DSP on a per-call basis. |

| appid application_id | This specifies the unique identifier (App ID) of the application for which you want to see the details. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Fuji 16.12.1 | This command was introduced. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| Field | Description |
|---|---|
| NSAP address | NSAP address for the ATM interface. |
| Type | Type of ATM interface. |
| ILMI status | Integrated Local management Interface (ILMI) protocol status for the ATM interface. |

| Command | Description |
|---|---|
| codec aal2-profile | Sets the codec profile for a DSP on a per-call basis. |

| application sccp | Displays the current status of only the Skinny Client Control Protocol (SCCP) application. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)XY | This command was introduced on the Communication Media Module. |
| 12.3(14)T | This command was integrated into Cisco IOS Release 12.3(14)T. |

| Field | Description |
|---|---|
| ENABLED | Shows auto-config application: SCCP is enabled. |
| ACTIVE | Shows the SCCP application has registered to use auto-configuration. |
| timeout | Shows timeout is set to 0, continuous retry without timeout. |

| Command | Description |
|---|---|
| auto-config | Enables auto-configuration or enters auto-config application configuration mode for the SCCP application. |
| debug auto-config | Enables debugging for auto-configuration applications. |
| debug sccp config | Enables SCCP event debugging. |

| status | Status for available session groups. |
|---|---|
| stats | Statistics for available session groups. |
| cfg | Configuration for available session groups. |
| all | Specified parameters for all session groups. |
| name group - name | A particular session group. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco AS5300. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for
                                          the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |

| Field | Descrption |
|---|---|
| RUDP Options | Reliable User datagram Protocol (RUDP) options. |
| Status | One of the following: Group-OutOfService--No session in the group has been established. Group-Inservice--At least one session in the group has been established. |
| Status (use) | One of the following: Group-Standby--The virtual switch controller (VSC) connected to the other end of this group goes into standby mode. Group-Active--The VSC connected to the other end of this group is the active VSC. Group-None--The VSC has not yet declared its intent. |

| Command | Description |
|---|---|
| show backhaul-session-manager session | Displays status, statistics, or configuration of sessions. |
| show backhaul-session-manager set | Displays session groups associated with a specific session set or all session sets. |

| all | Information is displayed about all available sessions. |
|---|---|
| ip | Information is displayed about the session associated with this IP address only. |
| ip - address | IP address of the local or remote session. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco AS5300. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for
                                          the Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Field | Description |
|---|---|
| State | Can be any of the following: OPEN--The connection is established. OPEN_WAIT--The connection is awaiting establishment. OPEN_XFER--Session failover is in progress for this session, which is a transient state. CLOSE--The session is down, also a transient state. The session waits a fixed amount of time and then moves to OPEN_WAIT. |
| Use-status | Indicates whether PRI signaling traffic is currently being transported over this session. Can be either of the following: OOS--The session is not being used to transport signaling traffic. Out of service (OOS) does not indicate if the connection
                                                is established. IS--The session is being used currently to transport all PRI signaling traffic. In service (IS) indicates that the connection
                                                is established. |

| Command | Description |
|---|---|
| show backhaul-session-manager group | Displays status, statistics, or configuration of a specific session group or all session groups. |
| show backhaul-session-manager set | Displays session groups associated with a specific session set or all session sets. |

| all | All available session sets. |
|---|---|
| name session - set - name | A specified session set. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco AS5300. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. Support for the
                                          Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |

| Command | Description |
|---|---|
| show backhaul - session - manager group | Displays status, statistics, or configuration of a specific session group or all session groups. |
| show backhaul - session - manager session | Displays status, statistics, or configuration of a session or all sessions. |

| WORD | (Optional) Name of the accounting template. |
|---|---|
| attrList | (Optional) Displays all vendor-specific attributes (VSAs) that are filtered by accounting templates. |
| qdump | (Optional) Displays template activity in the service and free queues. |
| summary | (Optional) Lists names of all the accounting templates and the number of attributes in each template currently being used. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| Field | Description |
|---|---|
| name | Name of the accounting template. |
| url | Location of the accounting template. |
| last_load | Describes if the accounting template was successfully or unsuccessfully loaded from its location. |
| is_running | Describes if the accounting template was activated after it was successfully loaded from its location. |
| is_dirty | Shows that the accounting template was reloaded during an active call. |
| no_of_legs | Number of call legs. |
| attr | Vendor-specific attributes (VSAs) defined in an accounting template. |

| Command | Description |
|---|---|
| gw-accounting aaa | Configures a new accounting template. |

| brief | (Optional) Displays a truncated version of fax call information. |
|---|---|
| id identifier | (Optional) Displays only the call with the specified identifier . Range is a hex value from 1 to FFFF. |
| compact | (Optional) Displays a compact version of the fax call information. |
| duration | (Optional) Displays active calls that are longer or shorter than a specified seconds value. The arguments and keywords are as follows: less --Displays calls shorter than the seconds value. more --Displays calls longer than the seconds value. seconds --Elapsed time, in seconds. Range is from 1 to 2147483647. There is no default value. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(3)XG | This command was modified. Support for Voice over Frame Relay (VoFR) was added. |
| 12.0(4)XJ | This command was implemented for store-and-forward fax on the Cisco AS5300. |
| 12.0(4)T | This command was implemented on the Cisco 7200 series. |
| 12.0(7)XK | This command was implemented on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(3)T | This command was modified. This command was implemented for modem pass-through over VoIP on the Cisco AS5300. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | The command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support was not included for the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5400, and Cisco AS5850. |
| 12.2(11)T | Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850. |
| 12.3(14)T | This command was modified. T.38 fax relay call statistics were made available to Call Detail Records (CDRs) through vendor-specific
                                          attributes (VSAs) and added to the call log. |
| 12.4(2)T | This command was modified. The LocalHostname display field was added to the VoIP call leg record. |
| 12.4(15)T | This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output. |
| 12.4(16) | This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output. |
| 12.4(22)T | This command was modified. Command output was updated to show IPv6 information. |

| Field | Description |
|---|---|
| ACOM Level | Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceler, which is the sum of the Echo Return
                                          Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call. |
| BearerChannel | Identification of the bearer channel carrying the call. |
| Buffer Drain Events | Total number of jitter buffer drain events. |
| Buffer Fill Events | Total number of jitter buffer fill events. |
| CallDuration | Length of the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallOrigin | Call origin: answer or originate. |
| CallState | Current state of the call. |
| ChargedUnits | Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second. |
| CodecBytes | Payload size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| ConnectionId | Global call identifier for this gateway call. |
| ConnectTime | Time, in milliseconds, at which the call was connected. |
| Consecutive-packets-lost Events | Total number of consecutive (two or more) packet-loss events. |
| Corrected packet-loss Events | Total number of packet-loss events that were corrected using the RFC 2198 method. |
| Dial-Peer | Tag of the dial peer sending this call. |
| EchoCancellerMaxReflector=64 | The location of the largest reflector, in milliseconds (ms). The reflector size does not exceed the configured echo path
                                          capacity. For example, if 32 ms is configured, the reflector does not report beyond 32 ms. |
| ERLLevel | Current echo return loss (ERL) level for this call. |
| FaxTxDuration | Duration of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization Rate by
                                          dividing the FaxTxDuration value by the TxDuration value. |
| GapFillWithInterpolation | Duration of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and following
                                          in time because voice data was lost or not received in time from the voice gateway for this call. |
| GapFillWithPrediction | Duration of the voice signal played out with signal synthesized from parameters, or samples of data preceding in time, because
                                          voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are frame-eraser
                                          and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithRedundancy | Duration of a voice signal played out with a signal synthesized from available redundancy parameters because voice data was
                                          lost or not received in time from the voice gateway for this call. |
| GapFillWithSilence | Duration of a voice signal replaced with silence because voice data was lost or not received in time for this call. |
| GENERIC | Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs. |
| H323 call-legs | Total H.323 call legs for which call records are available. |
| HiWaterPlayoutDelay | High-water-mark Voice Playout FIFO Delay during this call, in ms. |
| Index | Dial peer identification number. |
| InfoActivity | Active information transfer activity state for this call. |
| InfoType | Information type for this call; for example, voice or fax. |
| InSignalLevel | Active input signal level from the telephony interface used by this call. |
| Last Buffer Drain/Fill Event | Elapsed time since the last jitter buffer drain or fill event, in seconds. |
| LocalHostname | Local hostnames used for locally generated gateway URLs. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| LoWaterPlayoutDelay | Low-water-mark Voice Playout FIFO Delay during this call, in ms. |
| LowerIFName | Physical lower interface information. Appears only if the medium is ATM, Frame Relay (FR), or High-Level Data Link Control
                                          (HDLC). |
| Media | Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR, or HDLC. |
| Modem passthrough signaling method in use | Indicates that this is a modem pass-through call and that named signaling events (NSEs)--a Cisco-proprietary version of named
                                          telephone events in RFC 2833--are used for signaling codec upspeed. The upspeed method is the method used to dynamically change
                                          the codec type and speed to meet network conditions. This means that you might move to a faster codec when you have both voice
                                          and data calls and then slow down when there is only voice traffic. |
| NoiseLevel | Active noise level for this call. |
| OnTimeRvPlayout | Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values. |
| OutSignalLevel | Active output signal level to the telephony interface used by this call. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value of the peer table entry to which this call was made. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| PeerSubAddress | Subaddress when this call is connected. |
| Percent Packet Loss | Total percent packet loss. |
| Port | Identification of the time-division multiplexing (TDM) voice port carrying the call. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| ReceiveDelay | Average Playout FIFO Delay plus the Decoder Delay during this voice call, in ms. |
| ReceivePackets | Number of packets received by this peer during this call. |
| ReleaseSource | Number value of the release source. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| RoundTripDelay | Voice packet round-trip delay between the local and remote systems on the IP backbone for this call. |
| SelectedQoS | Selected Resourse Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| SessionTarget | Session target of the peer used for this call. |
| SetupTime | Value of the system UpTime, in milliseconds, when the call associated with this entry was started. |
| SignalingType | Signaling type for this call; for example, channel-associated signaling (CAS) or common channel signaling (CCS). |
| SIP call-legs | Total Session Initiation Protocol (SIP) call legs for which call records are available. |
| Telephony call-legs | Total telephony call legs for which call records are available. |
| Time between Buffer Drain/Fills | Minimum and maximum durations between jitter buffer drain or fill events, in seconds. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| TxDuration | The length of the call. Appears only if the medium is TELE. |
| VAD | Whether voice activation detection (VAD) was enabled for this call. |
| VoiceTxDuration | Duration of voice transmission from this peer to the voice gateway for this call, in ms. Derive the Voice Utilization Rate
                                          by dividing the VoiceTxDuration value by the TxDuration value. |

| Field | Description |
|---|---|
| ACOMLevel | Current ACOM level estimate in 0.1 dB increments. The term ACOM is used in G.165, General Characteristics of International Telephone Connections and International Telephone Circuits: Echo Cancellers . ACOM is the combined loss achieved by the echo canceller, which is the sum of the ERL, ERL enhancement, and nonlinear processing
                                          loss for the call. |
| BearerChannel | Identification of the bearer channel carrying the call. |
| ERLLevel | Current ERL level estimate in 0.1 dB increments. |
| FaxRate | Fax transmission rate from this peer to the specified dial peer, in bits per second (bps). |
| FaxRelayJitterBufOverflow | Fax relay jitter buffer overflow, in ms. |
| FaxRelayMaxJitBufDepth | Fax relay maximum jitter buffer depth, in ms. |
| FaxTxDuration | Duration of fax transmission from this peer to the voice gateway for this call, in ms. |
| GwReceivedCalledNumber, GwReceivedCalledOctet3 | Call information received at the gateway. |
| H323 call-legs | Type of call: H.323. |
| Initial HS Modulation | Initial high speed modulation used. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| MGCP call-legs | Type of call: Media Gateway Control Protocol (MGCP). |
| Multicast call-legs | Type of call: Multicast. |
| OriginalCallingNumber, OriginalCalling Octet, OriginalCalledNumber, OriginalCalledOctet, OriginalRedirectCalledNumber, OriginalRedirectCalledOctet | Original call information regarding calling, called, and redirect numbers, and octet-3s. Octet-3s are information elements
                                          (IEs) of Q.931 that include type of number, numbering plan indicator, presentation indicator, and redirect reason information. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| Port | Identification of the TDM voice port carrying the call. |
| Recent HS Modulation | Most recent high-speed modulation used. |
| SIP call-legs | Type of call: SIP. |
| Telephony call-legs | Type of call: Telephony. |
| Total call-legs | Total calls. |
| TranslatedCallingNumber, TranslatedCallingOctet, TranslatedCalledNumber, TranslatedCalledOctet, TranslatedRedirectCalledNumber,
                                          TranslatedRedirectCalledOctet | Translated call information. |
| TxDuration | Duration of transmit path open from this peer to the voice gateway for this call, in ms. |
| VoiceTxDuration | Duration of voice transmission from this peer to the voice gateway for this call, in ms. |

| Command | Description |
|---|---|
| show call active voice | Displays call information for voice calls that are in progress. |
| show call history | Displays the call history table. |
| show call-router routes | Displays the dynamic routes in the cache of the BE. |
| show call-router status | Displays the Annex G BE status. |
| show voice port | Displays configuration information about a specific voice port. |

| brief | (Optional) Displays a truncated version of call information. |
|---|---|
| id identifier | (Optional) Displays only the call with the specified identifier . The range is a hexadecimal value from 1 to FFFF. |
| compact | (Optional) Displays a compact version of call information. |
| duration | (Optional) Displays the call history for the specified time duration. |
| less seconds | (Optional) Displays the call history for shorter duration calls, in seconds. The range is from 1 to 2147483647. |
| more seconds | (Optional) Displays the call history for longer duration calls, in seconds. The range is from 1 to 2147483647. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| 12.4(18)M | This command was modified. The less keyword, more keyword, and seconds argument were added. |

| Field | Description |
|---|---|
| Telephony call-legs | Total telephony call legs for which call records are available. |
| SIP call-legs | Total session initiation protocol (SIP) call legs for which call records are available. |
| H323 call-legs | Total H.323 call legs for which call records are available. |
| Media | Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR (for Frame Relay), or HDLC (for High-Level Data Link
                                          Control). |
| GENERIC | Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs. |
| SetupTime | Value of the system UpTime, in milliseconds, when the call associated with this entry was started. |
| Index | Dial peer identification number. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value of the peer table entry to which this call was made. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| ConnectTime | Time, in milliseconds, at which the call was connected. |
| CallDuration | Length of the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallOrigin | Call origin: answer or originate. |
| CallState | Current state of the call. |
| ChargedUnits | Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second. |
| InfoType | Information type for this call; for example, voice or fax. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| ReceivePackets | Number of packets received by this peer during this call. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| ReceiveDelay | Average Playout FIFO Delay plus the Decoder Delay during this voice call, in ms. |
| ConnectionId | Global call identifier for this gateway call. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| SelectedQoS | Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionTarget | Session target of the peer used for this call. |
| OnTimeRvPlayout | Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values. |
| GapFillWithInterpolation | Duration of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and following
                                          in time because voice data was lost or not received in time from the voice gateway for this call. |
| GapFillWithRedundancy | Duration of a voice signal played out with a signal synthesized from available redundancy parameters because voice data was
                                          lost or not received in time from the voice gateway for this call. |
| GapFillWithPrediction | Duration of the voice signal played out with signal synthesized from parameters, or samples of data preceding in time, because
                                          voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are frame-eraser
                                          and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithSilence | Duration of a voice signal replaced with silence because voice data was lost or not received in time for this call. |
| HiWaterPlayoutDelay | High-water-mark Voice Playout FIFO Delay during this call, in ms. |
| LoWaterPlayoutDelay | Low-water-mark Voice Playout FIFO Delay during this call, in ms. |
| CodecBytes | Payload size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| InSignalLevel | Active input signal level from the telephony interface used by this call. |
| OutSignalLevel | Active output signal level to the telephony interface used by this call. |
| ERLLevel | Current echo return loss (ERL) level for this call. |
| ACOMLevel | Current ACOM level for this call. ACOM is the combined loss achieved by the echo canceler, which is the sum of the Echo Return
                                          Loss, Echo Return Loss Enhancement, and nonlinear processing loss for the call. |
| PeerSubAddress | Subaddress when this call is connected. |
| RoundTripDelay | Voice packet round-trip delay between the local and remote systems on the IP backbone for this call. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| TxDuration | The length of the call. Appears only if the medium is TELE. |
| VAD | Whether voice activation detection (VAD) was enabled for this call. |

| Command | Description |
|---|---|
| show call history media | Displays the call history table. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| brief | (Optional) Displays a truncated version of active video call information. |
|---|---|
| id call-identifier | (Optional) Displays only the video calls with the specified identifier. The
                                          						range is from 1 to FFFF. |
| compact | (Optional) Displays a compact version of active video call information. |
| duration | (Optional) Displays call history for the specified time duration. |
| less | Displays
                                          						call history for shorter duration calls. |
| more | Displays
                                          						call history for longer duration calls. |
| seconds | Time, in
                                          						seconds. The range is from 1 to 2147483647. |
| echo-canceller call-id | (Optional) Displays information about the state of the extended echo canceller
                                          						(EC). The range is from 0 to FFFFFFFF. |
| session-id WORD | (Optional) Displays session identifier details for a specific
                                          						session-id. WORD specifies a wildcard pattern which is
                                          						matched against the localUUID, RemoteUUID or complete Session-Id header string.
                                          						A valid wildcard pattern can comprise one or more combination of any of these
                                          						characters *, [0-9], [a-f], [A-F]. |
| stats | (Optional) Displays information about DSP statistics and video quality metrics. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was introduced. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(11)T | -- | This
                                          						command was modified. Support was added for SIP and H.323 calls. |
| 12.4(16); 12.4(15)T | -- | This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output. |
| 15.1(4)M | Cisco
                                          						Unified CME 8.6 | This
                                          						command was modified. The stats keyword
                                          						was added. |
| Cisco
                                          						IOS 15.6(2)T Cisco IOS XE Denali 16.3.1 | -- | This
                                          						command was modified. The session-id keyword was added. show call active video brief command output was enhanced to show VRF details
                                                							 and session-id details. show call active video compact command output was enhanced to show VRF details. |
| Cisco IOS XE 17.16.1a | -- | This command was modified to display SCIP video codec information. Note This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. | Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |

| Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

| Field | Description |
|---|---|
| CallDuration | Length of the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallState | Current state of the call. |
| Call agent controlled call-legs | Displays call legs for devices that are not telephony endpoints; for example, transcoding and conferencing |
| ChargedUnits | Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of a second. |
| CodecBytes | Payload size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| ConnectionId | Global call identifier for this gateway call. |
| ConnectTime | Time, in milliseconds (ms), during which the call was connected. |
| EchoCancellerMaxReflector | Size of the largest reflector, in ms. The reflector size cannot exceed the configured echo path capacity. For example, if
                                          32 ms is configured, the reflector does not report capacity beyond 32 ms. |
| ERLLevel | Current echo return loss (ERL) level for this call. |
| FaxTxDuration | Duration, in ms, of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization
                                          Rate by dividing the FaxTxDuration value by the TxDuration value. |
| GapFillWithInterpolation | Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call. |
| GapFillWithRedundancy | Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call. |
| GapFillWithPrediction | Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithSilence | Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call. |
| GENERIC | Generic or common parameters, that is, parameters that are common for VoIP and telephony call legs. |
| H320CallType | Total H320 call types available. |
| H323 call-legs | Total H.323 call legs for which call records are available. |
| HiWaterPlayoutDelay | High-water-mark voice playout first in first out (FIFO) delay during this call, in ms. |
| Index | Dial peer identification number. |
| InfoActivity | Active information transfer activity state for this call. |
| InfoType | Information type for this call; for example, voice, speech, or fax. |
| InSignalLevel | Active input signal level from the telephony interface used by this call. |
| Last Buffer Drain/Fill Event | Elapsed time since the last jitter buffer drain or fill event, in seconds. |
| LocalHostname | Local hostnames used for locally generated gateway URLs. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| LoWaterPlayoutDelay | Low-water-mark voice playout FIFO delay during this call, in ms. |
| LowerIFName | Physical lower interface information. Appears only if the medium is ATM, Frame Relay (FR), or High-Level Data Link Control
                                          (HDLC). |
| Media | Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, FR, or HDLC. |
| Multicast call-legs | Total multicast call legs for which call records are available. |
| NoiseLevel | Active noise level for this call. |
| OnTimeRvPlayout | Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values. |
| OutSignalLevel | Active output signal level to the telephony interface used by this call. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value of the peer table entry to which this call was made. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| PeerSubAddress | Subaddress when this call is connected. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| ReceiveDelay | Average playout FIFO delay plus the decoder delay during this voice call, in ms. |
| ReceivePackets | Number of packets received by this peer during this call. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| RoundTripDelay | Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call. |
| SCCP call-legs | Call legs for SCCP telephony endpoints. |
| SelectedQoS | Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionIDLocaluuid | UUID generated from originating user agent. |
| SessionIDRemoteuuid | UUID generated from terminating user agent. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| SessionTarget | Session target of the peer used for this call. |
| SetupTime | Value of the system UpTime, in milliseconds, when the call associated with this entry was started. |
| SIP call-legs | Total SIP call legs for which call records are available. |
| Telephony call-legs | Total telephony call legs for which call records are available. |
| Total call-legs | Total number of call legs for the call. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| TxDuration | The length of the call. Appears only if the medium is TELE. |
| VAD | Whether voice activation detection (VAD) was enabled for this call. |
| VideoCap_Annex | Extension of the video stream; for example, annex D1 and E. |
| VideoCap_Bitrate | Negotiated bitrate of the video stream; for example, 128000 b/s. |
| VideoCap_Codec | Codec for the active video call. |
| VideoCap_Format | Video format for the active video call. |
| VideoCap_FrameRate | Negotiated frame rate of the video stream; for example, 15 or 30 f/s. |
| VideoCap_PictureHeight | Height of the video resolution. |
| VideoCap_PictureWidth | Width of the video resolution. |
| VideoEarlyPackets | Number of early packets for a video call. |
| VideoLatePackets | Number of late packets in a video call. |
| VideoLostPackets | Number of lost packets in a video call. |
| VideoNumberOfChannels | Number of channels used for a video call. |
| Video Quality Score | Instantaneous and average Mean Opinion Score (MOS) for each active call leg. The MOS score is based on the amount of video
                                          quality degradation caused by compression distortion and the amount of video quality degradation caused by packet loss. The
                                          scale for the MOS score is as follows: Excellent--(80--100) Good--(60--80) Fair--(40--60) Poor--(20--40) Bad--(0--20) |
| VideoReceiveBytes | Number of bytes received in the video call. |
| VideoReceiveCodec | Type of video codec used in the receiving stream. |
| VideoReceivePackets | Number of packets received in the video call. |
| VideoTransmitBytes | Number of bytes transmitted in the video call. |
| VideoTransmitCodec | Type of video codec used in the transmission stream. |
| VideoTransmitPackets | Number of packets transmitted in the video call. |
| VideoUsedBandwidth | Bandwidth, in kbps, used for a video call. |
| VoiceTxDuration | Duration of voice transmission from this peer to the voice gateway for this call, in milliseconds. Derive the Voice Utilization
                                          Rate by dividing the VoiceTxDuration value by the TxDuration value. |

| Command | Description |
|---|---|
| show call history video | Displays call history information for SCCP video calls. |

| brief | (Optional) Displays a truncated version of call information. |
|---|---|
| long-dur-call-inactive | (Optional) Displays long duration calls that are detected and notified. |
| media-inactive | (Optional) Displays information about inactive media that have been detected. |
| called-number number | (Optional) Displays a specific called number pattern. |
| calling-number number | (Optional) Displays a specific calling number pattern. |
| id call-identifier | (Optional) Displays only the call with the specified call-identifier value. The range is from 1 to
                                          						FFFF. |
| compact | (Optional) Displays a compact version of call information. |
| duration | (Optional) Displays the call history for the specified time duration. |
| less seconds | Displays the call history for shorter duration calls, in seconds. The range is
                                          						from 1 to 2147483647. |
| more seconds | Displays the call history for longer duration calls, in seconds. The range is
                                          						from 1 to 2147483647. |
| dest-route-string tag | (Optional) Displays only the call with the specified destination
                                          						route tag value.
                                          						The range is from 1 to 10000. |
| echo-canceller | (Optional) Displays information about the state of the extended echo canceller
                                          						(EC). |
| hexadecimal-id | The
                                          						hexadecimal ID of an active voice call. The range is from 0x0 to 0xFFFFFFFF. |
| port slot-number | Displays EC details for a specified active voice port. The range varies
                                          						depending on the voice ports available on the router. |
| summary | Displays an EC summary for all active voice calls. |
| long-dur-call | (Optional) Displays long duration calls that are detected and notified. |
| redirect | (Optional) Displays information about active calls that are being redirected
                                          						using Release-to-Pivot (RTPvt) or Two B-Channel Transfer (TBCT). |
| tbct | Displays information about TBCT calls. |
| session-id WORD | (Optional) Displays session identifier details for a specific
                                          						session-id. WORD specifies a wildcard pattern which is
                                          						matched against the localUUID, RemoteUUID or complete Session-Id header string.
                                          						A valid wildcard pattern can comprise one or more combination of any of these
                                          						characters *, [0-9], [a-f], [A-F]. |
| stats | (Optional) Displays information about digital signal processing (DSP) voice
                                          						quality metrics. |

| Release | Modification |
|---|---|
| 11.3(1)T | This
                                          						command was introduced. |
| 12.0(3)XG | This
                                          						command was modified. Support for Voice over Frame Relay (VoFR) was added. |
| 12.0(4)XJ | This
                                          						command was implemented for store-and-forward fax on the Cisco AS5300. |
| 12.0(4)T | This
                                          						command was implemented on the Cisco 7200 series. |
| 12.0(7)XK | This
                                          						command was implemented on the Cisco MC3810. |
| 12.1(3)T | This
                                          						command was implemented for modem pass-through over VoIP on the Cisco AS5300. |
| 12.1(5)XM | This
                                          						command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | The
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This
                                          						command was implemented on the Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support was not
                                          						included for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850. |
| 12.2(11)T | Support
                                          						was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850. |
| 12.2(13)T | This
                                          						command was modified. The echo-canceller keyword was added. The command
                                          						output was modified with an extra reflector location when the extended EC is
                                          						present; the largest reflector location is shown. |
| 12.3(1) | This
                                          						command was modified. The redirect keyword was added. |
| 12.3(4)T | This
                                          						command was modified. The called-number , calling-number , and media-inactive keywords were added. |
| 12.3(14)T | This
                                          						command was modified. New output relating to Skinny Client Control Protocol
                                          						(SCCP), SCCP Telephony Control Application (STCAPP), and modem pass-through
                                          						traffic was added. |
| 12.4(2)T | This
                                          						command was modified. The LocalHostname display field was added to the VoIP
                                          						call leg record and command output was enhanced to display modem relay physical
                                          						layer and error correction protocols. |
| 12.4(4)T | This
                                          						command was modified. The long-dur-call keyword was added. |
| 12.4(11)XW | This
                                          						command was modified. The stats keyword
                                          						was added. |
| 12.4(15)T | This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output. |
| 12.2(33)SXH | This
                                          						command was integrated into Cisco IOS Release 12.2(33)SXH. |
| 12.4(16) | This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output. |
| 12.4(22)T | This
                                          						command was modified. Command output was updated to show IPv6 information. |
| 15.3(3)M | This
                                          						command was modified. The dest-route-string keyword was added. |
| Cisco
                                          						IOS XE Release 3.10S | This
                                          						command was integrated into Cisco IOS XE Release 3.10S. |
| Cisco
                                          						IOS 15.6(2)T Cisco IOS XE Denali 16.3.1 | This
                                          						command was modified. The session-id keyword was added. show call active voice brief command output was enhanced to show VRF details and session-id details. show call active voice compact command output was enhanced to show VRF details. |
| Cisco IOS XE 17.16.1a | This command was modified to display SCIP audio codec information. Note This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. | Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |

| Note | This feature is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

| Symbol | Field | Description |
|---|---|---|
| BYP0 | Channel
                                          					 bypass | 1 = Transparent bypass; EC is disabled. 0 = Cancel; EC is enabled. |
| TAIL3 | Max tail | 0 = 24 milliseconds. 1 = 32 milliseconds. 2 = 48 milliseconds. 3 = 64 milliseconds. Note This field should be set just greater than the anticipated worst round-trip tail delay. | Note | This field should be set just greater than the anticipated worst round-trip tail delay. |
| Note | This field should be set just greater than the anticipated worst round-trip tail delay. |
| REC3 | Residual
                                          					 echo control | 0 = Cancel only; echo is the result of linear processing; no nonlinear processing is applied. 1 = Suppress residual; residual echo is zeroed; simple nonlinear processing is applied (you might experience "dead air" when
                                                talking). 2 = Reserved. 3 = Generate comfort noise (default). |
| FRZ0 | h-register hold | 1 =
                                          					 Freezes h-register; used for testing. |
| HZ0 | h-register clear | Sending
                                          					 the channel command with this bit set clears the h-register. |
| TD3 | Modem
                                          					 tone disable | 0 = Ignore 2100 Hz modem answer tone. 1 = G.164 mode (bypass canceller if 2100 Hz tone). 2 = R. 3 = G.165 mode (bypass canceller for phase reversing tone only). |
| ERL0 | Echo
                                          					 return loss | 0 = 6 decibel (dB). 1 = 3 dB. 2 = 0 dB. 3 = R. Worst echo return loss (ERL) situation in which canceller still works. |
| HLC1 | High
                                          					 level compensation | 0 = No attenuation. 1 = 6 dB if clipped. On loud circuits, the received direction can be attenuated 6 dB if clipping is observed. |
| R0 | Reserved | Must be
                                          					 set to 0 to ensure compatibility with future releases. |

| Note | This field should be set just greater than the anticipated worst round-trip tail delay. |
|---|---|

| Field | Description |
|---|---|
| Modem Relay Local Rx Speed | Download speed, in bits per second, of the local modem relay. |
| Modem Relay Local Tx Speed | Upload speed of the local modem relay. |
| Modem Relay Remote Rx Speed | Download speed of the remote modem relay. |
| Modem Relay Remote Tx Speed | Upload speed of the remote modem relay. |
| Modem Relay Phy Layer Protocol | Physical protocol of the modem relay. |
| Modem Relay Ec Layer Protocol | EC layer protocol of the modem relay. |
| SPRTInfoFramesReceived | Total number of simple packet relay transport (SPRT) protocol frames received. |
| SPRTInfoTFramesSent | Total number of SPRT frames sent. |
| SPRTInfoTFramesResent | Total number of SPRT frames sent again. |
| SPRTXidFramesReceived | Total number of SPRTS ID frames received. |
| SPRTXidFramesSent | Total number of SPRTS ID frames sent. |
| SPRTTotalInfoBytesReceived | Total number of SPRT bytes received. |
| SPRTTotalInfoBytesSent | Total number of SPRT bytes sent. |
| SPRTPacketDrops | Total number of SPRT packets dropped. |

| Field | Description |
|---|---|
| CallDuration | Length of the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallState | Current state of the call. |
| Call agent controlled call-legs | Displays call legs for devices that are not telephony endpoints; for example, transcoding and conferencing |
| ChargedUnits | Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second. |
| CodecBytes | Payload size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| ConnectionId | Global call identifier for this gateway call. |
| ConnectTime | Time, in ms, during which the call was connected. |
| EchoCancellerMaxReflector | Size of the largest reflector, in ms. The reflector size cannot exceed the configured echo path capacity. For example, if
                                          32 ms is configured, the reflector does not report capacity beyond 32 ms. |
| ERLLevel | Current echo return loss (ERL) level for this call. |
| FaxTxDuration | Duration, in ms, of fax transmission from this peer to the voice gateway for this call. You can derive the Fax Utilization
                                          Rate by dividing the FaxTxDuration value by the TxDuration value. |
| GapFillWithInterpolation | Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call. |
| GapFillWithRedundancy | Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call. |
| GapFillWithPrediction | Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithSilence | Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call. |
| GENERIC | Generic or common parameters; that is, parameters that are common for VoIP and telephony call legs. |
| H320CallType | Total H320 call types available. |
| H323 call-legs | Total H.323 call legs for which call records are available. |
| HiWaterPlayoutDelay | High-water-mark voice playout first in first out (FIFO) delay during this call, in ms. |
| Index | Dial peer identification number. |
| InfoActivity | Active information transfer activity state for this call. |
| InfoType | Information type for this call; for example, voice, speech, or fax. |
| InSignalLevel | Active input signal level from the telephony interface used by this call. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| LoWaterPlayoutDelay | Low-water-mark voice playout FIFO delay during this call, in ms. |
| Media | Medium over which the call is carried. If the call is carried over the (telephone) access side, the entry is TELE. If the
                                          call is carried over the voice network side, the entry is either ATM, Frame Relay (FR), or High-Level Data Link Control (HDLC). |
| Multicast call-legs | Total multicast call legs for which call records are available. |
| NoiseLevel | Active noise level for this call. |
| OnTimeRvPlayout | Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values. |
| OutSignalLevel | Active output signal level to the telephony interface used by this call. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value of the peer table entry to which this call was made. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| PeerSubAddress | Subaddress when this call is connected. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| ReceiveDelay | Average playout FIFO delay plus the decoder delay during this voice call, in ms. |
| ReceivePackets | Number of packets received by this peer during this call. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| RoundTripDelay | Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call. |
| SCCP call-legs | Call legs for SCCP telephony endpoints. |
| SelectedQoS | Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionIDLocaluuid | UUID generated from the originating user agent. |
| SessionIDRemoteuuid | UUID generated from the terminating user agent. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| SessionTarget | Session target of the peer used for this call. |
| SetupTime | Value of the system UpTime, in ms, when the call associated with this entry was started. |
| SIP call-legs | Total SIP call legs for which call records are available. |
| Telephony call-legs | Total telephony call legs for which call records are available. |
| Total call-legs | Total number of call legs for the call. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| TxDuration | The length of the call. Appears only if the medium is TELE. |
| VAD | Whether voice activation detection (VAD) was enabled for this call. |
| VoiceTxDuration | Duration of voice transmission from this peer to the voice gateway for this call, in ms. Derive the Voice Utilization Rate
                                          by dividing the VoiceTxDuration value by the TxDuration value. |

| Decimal | Hex |
|---|---|
| 2 | 2 |
| 4 | 4 |
| 6 | 6 |
| 8 | 8 |
| 10 | A |
| 12 | C |

| Field | Description |
|---|---|
| Maximum no. of TBCT calls allowed | Maximum number of calls that can use TBCT as defined by the tbct max calls command. |
| Maximum TBCT call duration | Maximum length allowed for a TBCT call as defined by the tbct max call-duration command. |
| Total number TBCT calls currently being monitored | Total number of active TBCT calls. |
| ctrl name | Name of the T1 controller where the call originated. |
| tag | Call tag number that identifies the call. |
| call-ids | Numbers that uniquely identify the call legs. |
| start_time | Time, in hours, minutes, and seconds, when the redirected call began. |

| Command | Description |
|---|---|
| show call active fax | Displays call information for fax transmissions that are in progress. |
| show call history | Displays the call history table. |
| show call-router routes | Displays the dynamic routes in the cache of the BE. |
| show call-router status | Displays the Annex G BE status. |
| show dial-peer voice | Displays configuration information for dial peers. |
| show num-exp | Displays how the number expansions are configured in VoIP. |
| show voice call status | Displays the call status for voice ports on the Cisco router or concentrator. |
| show voice port | Displays configuration information about a specific voice port. |

| active | Displays statistics for active application instances. |
|---|---|
| history | Displays statistics for terminated application instances. |
| app-tag application-name | Name of a specific voice application. Output displays statistics for that voice application. |
| summary | Displays a summary for each application. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | Statistics for an application are automatically cleared if the application is deleted with the no call application voice command or its script is reloaded with the call application voice load command. |
|---|---|

| Field | Description |
|---|---|
| App Name | Name of the voice application. |
| Stats | Whether statistics is enabled for this application. Note If statistics is enabled, this field displays N until there is at least one active instance of the application. | Note | If statistics is enabled, this field displays N until there is at least one active instance of the application. |
| Note | If statistics is enabled, this field displays N until there is at least one active instance of the application. |
| Sessions w/ stats | Number of terminated application instances that the gauges represent. |
| Total | Total number of instances of the application. |
| Errors | Total number of errors for all instances of the application. |
| Last Reset Time | Time at which the statistics were last cleared with the clear call application stats command, or the gateway was restarted. |

| Note | If statistics is enabled, this field displays N until there is at least one active instance of the application. |
|---|---|

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application stats | Enables statistics collection for voice applications. |
| call application voice event-log | Enables event logging for a specific voice application. |
| clear call application stats | Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics. |
| show call application gateway-level | Displays gateway-level statistics for voice application instances. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| active | Displays statistics for active application instances. |
|---|---|
| history | Displays statistics for terminated application instances. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | Statistics for an application are automatically cleared if the application is deleted with the no call application voice command or its script is reloaded with the call application voice load command. |
|---|---|

| Field | Description |
|---|---|
| Sessions w/ stats | Number of active application instances that the gauges represent. |
| Currently connected incoming PSTN legs | Number of active call legs that are incoming from the PSTN. |
| Currently connected outgoing PSTN legs | Number of active call legs that are outgoing to the PSTN. |
| Currently connected incoming VoIP legs | Number of active call legs that are incoming from the IP network. |
| Currently connected outgoing VoIP legs | Number of active call legs that are outgoing to the IP network. |
| Placecalls in transit | Number of outgoing calls in progress for all active application instances. The value is decremented by one after the call
                                          is either set up or the setup fails. |
| Handouts in transit | Number of handoffs in progress for all active application instances. The value is decremented by one after the receiving
                                          application either hands back the application or rejects the handoff. |
| Pending ASNL subscriptions | Number of Application Subscribe Notify Layer (ASNL) subscription requests that are in progress for all active application
                                          instances. |
| Pending ASNL unsubscriptions | Number of ASNL unsubscription requests that are in progress for all active application instances. |
| Prompts playing (non-TTS) | Number of recorded prompts being played in all active application instances. |
| Recordings | Number of recordings being made in all active application instances. |
| TTS prompts playing | Number of text-to-speech (TTS) prompts playing in all active application instances. |

| Command | Description |
|---|---|
| call application stats | Enables statistics collection for voice applications. |
| clear call application stats | Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics. |
| show call application app-level | Displays application-level statistics for voice applications. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| summary | (Optional) Displays a short summary of all interface types or the selected interface. |
|---|---|
| aaa | Authentication, authorization, and accounting (AAA) interface type. |
| asr | Automatic speech recognition (ASR) interface type. |
| flash | Flash memory of the Cisco gateway. |
| http | Hypertext Transfer Protocol (HTTP) interface type. |
| ram | Memory of the Cisco gateway. |
| rtsp | Real Time Streaming Protocol (RTSP) interface type. |
| smtp | Simple Mail Transfer Protocol (SMTP) interface type. |
| tftp | Trivial File Transfer Protocol (TFTP) interface type. |
| tts | Text-to-speech (TTS) interface type. |
| server server | (Optional) Displays event logs or statistics for the specified server. |
| event-log | (Optional) Displays event logs for the selected interface type or server. |
| info | (Optional) Displays statistics for the selected interface type or server. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Field | Description |
|---|---|
| Last reset time | Time at which the statistics were last cleared with the clear call application interface command, or the gateway was restarted. |
| Read requests | Total number of read requests from applications to this interface type. |
| Read successes | Number of successful read requests from applications to this interface type. |
| Read failures | Number of failed read requests from applications to this interface type. |
| Read aborts | Number of aborted read requests from applications to this interface type. |
| Total bytes read | Total number of bytes that the application read from this interface type. |
| Server name | Name of the specific server. |
| Stats | Whether statistics are enabled for this server. |
| Error Count | Total number of errors for this server. |
| Event Log | Whether event logging is enabled for this server. |

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application interface stats | Enables statistics collection for application interfaces. |
| clear call application interface | Clears application interface statistics and event logs. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Field | Description |
|---|---|
| Service Name | Name specified by the TCL service register command. |
| Session ID | ID of the session that registered as this service. You can use this ID in the show call application sessions id command to view details about this session. |
| Session Name | Name configured by the call application session start command, if the session was started on the gateway rather than by an incoming call. |

| Command | Description |
|---|---|
| call application session start (global configuration) | Starts a new instance (session) of a TCL application from global configuration mode. |
| call application session start (privileged EXEC) | Starts a new instance (session) of a TCL application from privileged EXEC mode. |
| call application session stop | Stops a voice application session that is running. |
| show call application sessions | Displays summary or detailed information about voice application sessions. |

| active | Displays event logs or statistics for active application instances. |
|---|---|
| history | Displays event logs or statistics for inactive application instances in the history table. |
| summary | Displays a summary of each application instance. |
| app-tag application-name | Name of a specific voice application. Output displays event logs or statistics for that voice application. |
| last | (Optional) Displays event logs or statistics for the most recent instance. |
| number | (Optional) Displays event logs or statistics for this number of most recent previous instances. |
| session-id session-id | Identifies a specific application instance. Output displays event logs or statistics for that instance. |
| event-log | (Optional) Displays event logs for application instances. |
| info | (Optional) Displays statistics for application instances. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | These fields display for the show call application session-level , show call application app-level , and show call application gateway-level commands. At the session level, the fields apply to a single application instance. At the application level, the fields apply
                                          to all instances of an application. At the gateway level, the fields apply to all instances of all applications. |
|---|---|

| Field | Description |
|---|---|
| Session id | Session ID assigned to the instance when it became active. |
| Session name | Name of the session defined with the call application session start command. |
| Application name | Name of the application defined with the call application voice command. |
| Application URL | Location of the application script defined with the call application voice command. |
| Start time | Time at which the session started. |
| Subscriber Service -- Call |
| Legs setup | Number of calls setup (indications and requests) by an application instance. |
| Total legs connected | Number of calls connected by an application instance. |
| Legs currently connected | Number of calls currently connected by an application instance at any moment. |
| Legs handed in | Number of call legs received as an incoming handoff from another application. |
| Legs handed in returned back | Number of call legs received as an incoming handoff from another application that were returned to the other application. |
| Legs handed out | Number of call legs handed off to another application. |
| Legs handed out came back | Number of call legs handed off to another application that were returned by the other application. |
| Legs disconnected normally | Number of incoming and outgoing calls disconnected for normal causes. |
| Legs disconnected for user error | Number of incoming calls disconnected for call failure reasons, such as no answer or busy. |
| Legs disconnected for system error | Number of incoming calls disconnected for system failure reasons, such as no resources. |
| Subscriber Service -- Media |
| Media attempts | Number of prompt playouts, recordings, and text-to-speech (TTS) attempts on call legs in this application instance. |
| Media actives, | Number of prompt playouts, recordings, and TTS prompts currently active on call legs in an application instance. |
| Media successes | Number of prompt playouts, recordings, and TTS prompts that were successful on call legs in an application instance. |
| Media aborts | Number of prompt playouts, recordings, and TTS prompts that were aborted by the caller on call legs in an application instance. |
| Media failures | Number of prompt playouts, recording, and TTS attempts that failed on call legs in an application instance. |
| Total media duration | Total duration, in seconds, of prompt playing, recording, or TTS. |
| Application Internal Service -- Handoff |
| Bridged handoffs, incoming | Number of handoffs received with callback (bridged transfers) in an application instance. |
| Bridged handoffs, outgoing | Number of handoffs placed with callback (bridged transfers) by an application instance. |
| Bridged handoffs returned, incoming | Number of incoming bridged handoffs that were returned by an application instance. |
| Bridged handoffs returned, outgoing | Number of outgoing bridged handoffs that were returned to an application instance. |
| Blind handoffs, incoming | Number of handoffs received with no callback (blind transfers) in an application instance. |
| Blind handoffs, outgoing | Number of handoffs placed with no callback (blind transfers) by an application instance. |
| Handoffs in transit 1 | Number of handoffs in progress for an application instance. The value is decremented by one after the receiving application
                                          either hands back the application or rejects the handoff. |
| Handoffs failed | Number of handoffs that failed (bridged and blind) in an application instance. |
| Application Internal Service -- Placecall/transfer |
| Placecall requests | Number of outgoing call setup requests made by an application instance. |
| Placecall successes | Number of outgoing calls placed by an application instance. |
| Placecall failures | Number of outgoing call setup requests that failed for an application instance. |
| Place calls in transit | Number of outgoing calls in progress for an application. The value is decremented by one after the call is either set up
                                          or the setup fails. |
| Application Internal Service -- Document Read-Write |
| Doc requests | Number of document fetch and submit requests. |
| Doc successes | Number of successful document fetches and submits. |
| Doc failures | Number of document fetch and submit failures. |
| Application Internal Service -- Downloaded Script |
| Script parse errors | Number of semantic errors seen by an application instance. |
| Application Internal Service -- ASNL |
| ASNL notifications | Number of Application Subscribe Notify Layer (ASNL) notifications received from servers. |
| ASNL requests | Number of subscribe or unsubscribe requests made by an application instance. |
| ASNL successes | Number of subscribe or unsubscribe requests that succeeded for an application instance. |
| ANSL failures | Number of subscribe or unsubscribe requests that failed for an application instance. |
| Subscriber Interaction --- DTMF |
| DTMFs not matched | Number of DTMF patterns input by a caller that were not matched in an application instance. |
| DTMFs matched | Number of DTMF patterns input by a caller that were matched in an application instance. |
| DTMFs no input | Number of "no input" notifications received (includes DTMF timeouts). |
| DTMFs long pound | Number of long-pound interrupts from a caller seen by an application instance. |
| Subscriber Interaction -- ASR |
| ASR not matched | Number of automatic speech recognition (ASR) phrases from a caller that were not matched in an application instance. |
| ASR matched | Number of automatic speech recognition (ASR) phrases from a caller that were matched in an application instance. |
| ASR no inputs | Number of "no input" notifications received from ASR servers. |
| Subscriber Interaction -- AAA Authentication |
| AAA authentication successes | Number of AAA authentication successes. |
| AAA authentication failures | Number of AAA authentication failures because of invalid passwords. |
| Subscriber Interaction -- AAA Authorizations |
| AAA authorization successes | Number of AAA authorization successes. |
| AAA authorization failures | Number of AAA authorization failures. |

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application history session max-records | Sets the maximum number of application instance records saved in history. |
| call application history session retain-timer | Sets the maximum number of minutes for which application instance records are saved in history. |
| call application stats | Enables statistics collection for voice applications. |
| call application voice event-log | Enables event logging for a specific voice application. |
| show call application app-level | Displays application-level statistics for voice applications. |
| show call application gateway-level | Displays gateway-level statistics for voice application instances. |

| callid call-id | (Optional) Call-leg ID of an active call that is being controlled by the session. |
|---|---|
| id session-id | (Optional) Session ID for the specific application instance. |
| name instance-name | (Optional) Name assigned to the instance with the call application session start command. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Note | If a session is started with the call application session start command in privileged EXEC mode, it is not tracked by the system and is therefore not shown as stopped in the output of the show call application sessions command. |
|---|---|

| Field | Description |
|---|---|
| SID | Session identifier for active sessions. |
| Name | Session name that was configured with the call application session start command. |
| Called | Called number for active calls that are using the session. |
| Calling | Calling number for active calls that are using the session. |
| App Name | Name of the application for which the instance was created. |
| Legs | Any active call legs that are controlled by the session. |
| State | Shows "stopped" for any session that is no longer running, provided that the session is started with the call application session start command in global configuration mode. |

| Field | Description |
|---|---|
| App | Name of the application for which the instance was created. |
| URL | Location of the script used for the application as specified with the call application voice command. |
| Session name | Session name that was configured with the call application session start command. |
| Session handle | Handle that is returned from the TCL mod_handle infotag. A session handle is used in a TCL script on a Cisco gateway to send
                                          messages to other sessions. |
| FSM State | Current state in the TCL IVR 2.0 finite-state machine, as specified with the TCL fsm setstate command in the script. |
| ID for ‘show call active voice id’ display: | Call identifier. |
| Legs | Any active call legs that are controlled by this session. |
| Services | Service name for the session if it registered as a service with the TCL service register command in the script. You can display
                                          a list of all registered services with the show call application services registry command. |

| Command | Description |
|---|---|
| call application session start (global configuration) | Starts a new instance (session) of a TCL application from global configuration mode. |
| call application session start (privileged EXEC) | Starts a new instance of a TCL application from privileged EXEC mode. |
| call application session stop | Stops a voice application session that is running. |
| show call application services registry | Displays a one-line summary of all registered services. |

| name | (Optional) Name of the desired voice application. Output displays information about that application. |
|---|---|
| summary | (Optional) Output displays a one-line summary of each voice application. |

| Release | Modification |
|---|---|
| 11.3(6)NA2 | This command was introduced. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |
| 12.1(5)T | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB | This command was modified to support VoiceXML applications. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, Cisco 3745, and Cisco 7200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T for VoiceXML applications. This command is supported on the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |
| 12.3(14)T | New output was added relating to the SCCP Telephony Control Application (STCAPP). |

| Field | Description |
|---|---|
| URL | Location of the document used by the application. |
| It has: n calls active. | Number of calls that are using this application. |
| incoming calls | Number of incoming public switched telephone network (PSTN) or IP calls that invoked this application. |
| calls handed off to it | Number of calls that were handed off to this application by another TCL or VoiceXML application. |
| call transfers initiated | Number of call transfers that were initiated by this application. |
| pages loaded | Number of VoiceXML pages that were loaded by the application. |
| successful | Number of VoiceXML pages that were completed. |
| prompts played | Number of audio prompts that were played by the application. |
| recorded messages | Number of audio recordings made by the VoiceXML application. |
| Interpreted by | Programming language used by the application. |
| The TCL or VoiceXML Script is | Content of the VoiceXML document or TCL script. |

| Command | Description |
|---|---|
| call application voice | Defines the name to be used for an application and indicates the location of the appropriate IVR script to be used with the
                                          application. |
| call application voice load | Reloads the designated TCL script or VoiceXML document. |

| ip - address | (Optional) Specific IP address. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| show call fallback stats | Displays call fallback statistics. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Field | Description |
|---|---|
| Fallback is | Lists enabled/disabled state of call fallback. |
| Using ICPIF threshold | ICPIF is configured to determine network traffic. |
| ICPIF value timeout | Lists probe timeout for collecting ICPIF information. |
| ICPIF threshold | Lists configured ICPIF threshold. |
| Number of packets in a probe | Lists number of configured packets per probe. |
| IP precedence of probe packets | Lists configured IP precedence for probes. |
| Fallback cache size | Number of allowed entries in call fallback cache. |
| Fallback cache timeout | Length of cache timeout, in seconds. |
| Instantaneous value weight | Lists weight configured for calculating cache entry based on new probe and last entry. |
| MD5 Keychain | MD5 authentication has been configured with a keychain of secret. |

| Command | Description |
|---|---|
| call fallback monitor | Enables the monitoring of destinations without fallback to alternate dial peers. |
| show voice trunk-conditioning signaling | Enables fallback to alternate dial peers in case of network congestion. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600, Cisco 3600, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Field | Description |
|---|---|
| Total accepted calls | Number of times that calls were successful over IP. |
| Total rejected calls | Number of times that calls were rejected over IP. |
| Total cache overflows | Number of times that the fallback cache overflowed and required pruning. |

| Command | Description |
|---|---|
| clear call fallback stats | Clears the call fallback statistics. |
| show call fallback cache | Displays the current ICPIF estimates for all IP addresses in the cache. |

| Release | Modification |
|---|---|
| 12.3(4)T | This
                                          						command was introduced. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release
                                          						3.10S. |

| Field | Description |
|---|---|
| The
                                          					 following components registered in GCFM: | Shows which
                                          					 components are filtered in the generic call filter module. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a
                                          						call filter match list for debugging voice calls. |
| debug call filter inout | Display
                                          						the debug trace inside the GCFM. |
| debug condition match-list | Run a
                                          						filtered debug on a voice call. |
| outgoing port | Configure
                                          						debug filtering for the outgoing port. |
| show call filter match-list | Display
                                          						call filter match lists. |

| tag | Numeric
                                          						label that uniquely identifies the match list. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This
                                          						command was introduced. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release
                                          						3.10S. |

| Field | Description |
|---|---|
| call filter
                                          					 match-list 9 voice | Shows which
                                          					 match list is being displayed. |
| debug
                                          					 condition match-list is set to EXACT_MATCH | Shows
                                          					 whether the debug condition is set for exact match or partial match. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a
                                          						call filter match list for debugging voice calls. |
| debug call filter inout | Display
                                          						the debug trace inside the GCFM. |
| debug condition match-list | Run a
                                          						filtered debug on a voice call. |
| show call filter components | Display
                                          						the components used for filtering calls. |