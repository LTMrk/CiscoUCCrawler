---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01101-html-34b3dda1f6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01101.html
retrieved_at: 2026-08-21T22:56:42.149488+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: O

## Chapter: Cisco Unified CME Commands: O

# Cisco Unified CME Commands: O

## olsontimezone

To set the Olson Timezone so that the correct local time is displayed
                              		  on Cisco Unified SCCP IP phones or Cisco Unified SIP IP phones, use the olsontimezone command in telephony-service or
                              		  voice register global configuration mode, respectively. To return to the
                              		  default, use the no form of this command.

olsontimezone timezone version number

no olsontimezone

### Syntax Description

timezone

Olson Timezone names, which include the area (name of
                                          						continent or ocean) and location (name of a specific location within that
                                          						region, usually cities or small islands).

version number

Version of the tzupdater.jar or TzDataCSV.csv file. The
                                          						version indicates whether the file needs to be updated or not.

### Command Default

No Olson Timezone is set.

### Command Modes

Telephony-service configuration (config-telephony)

Voice register global configuration (config-register-global)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the olsontimezone command in either
                              		  telephony-service or voice register global configuration mode, with the current
                              		  version of Oracle’s Olson Timezone updater tool, tzupdater.jar, to set the
                              		  correct Olson Timezone.

For Cisco Unified 3911 and 3951 SIP IP phones and Cisco Unified 6921,
                              		  6941, 6961, and 6945 SCCP and SIP IP phones, the correct Olson Timezone updater
                              		  file is TzDataCSV.csv. The TzDataCSV.csv file is created based on the
                              		  tzupdater.jar file.

To set the correct time zone, you must determine the Olson Timezone
                              		  area/location where the Cisco Unified CME is located and download the latest
                              		  tzupdater.jar or TzDataCSV.csv to a TFTP server (such as flash or slot 0) that
                              		  is accessible to the Cisco Unified CME.

After a complete reboot, the phone checks if the version of its
                              		  configuration file is earlier or later than 2010o. If it is earlier, the phone
                              		  loads the latest tzupdater.jar and uses that updater file to calculate the
                              		  Olson Timezone.

To make the Olson Timezone feature backward compatible, both the time-zone and timezone commands are retained as legacy time
                              		  zones. Because the olsontimezone command covers approximately
                              		  500 time zones (Version 2010o of the tzupdater.jar file supports approximately
                              		  453 Olson Timezone IDs.), this command takes precedence when either the time-zone or the timezone command (that covers a total of 90
                              		  to100 time zones only) is present at the same time as the olsontimezone command.

## Examples

The following example shows 7:29 p.m. as the time set on a Cisco
                              		  Unified 7961 SCCP IP phone in Buenos Aires on May 13, 2011:

```
Router(config)# tftp-server flash:tzupdater.jar Router(config)# tftp-server flash:TzDataCSV.csv Router(config)# telephony-service Router(config-telephony)# olsontimezone America/Argentina/Buenos Aires version 2010o Router(config-telephony)# create cnf-files Router(config-telephony)# time-zone 21 Router(config-telephony)# exit Router(config)# clock timezone CST -6 Router(config)# clock summer-time date 12 October 2010 2:00 26 April 2011 2:00 Router(config)# exit Router# clock set 19:29:00 13 May 2011 Router# configure terminal Router(config)# telephony-service Router(config-telephony)# reset
```

The following example shows 3:25 p.m. as the time set on a Cisco
                              		  Unified 6921 SIP IP phone in Buenos Aires on November 17, 2011:

```
Router(config)# tftp-server slot0:tzupdater.jar Router(config)# tftp-server slot0:TzDataCSV.csv Router(config)# voice register global Router(config-register-global)# olsontimezone America/Argentina/Buenos Aires version 2010o Router(config-register-global)# create profile Router(config-register-global)# timezone 21 Router(config-register-global)# exit Router(config)# clock timezone CST -6 Router(config)# clock summer-time date 12 October 2010 2:00 26 April 2011 2:00 Router(config)# exit Router# clock set 15:25:00 17 November 2011 Router# configure terminal Router(config)# voice register global Router(config-register-global)# reset
```

### Related Commands

Command

Description

time-zone

Sets the time zone so that the correct local time is
                                          						displayed on Cisco Unified SCCP IP phones in a Cisco Unified CME system.

timezone

Sets the time zone used for Cisco Unified SIP IP phones in
                                          						a Cisco Unified CME system.

## olsontimezone

To set the Olson Timezone so that the correct local time is displayed
                              		  on Cisco Unified SCCP IP phones or Cisco Unified SIP IP phones, use the olsontimezone command in telephony-service or
                              		  voice register global configuration mode, respectively. To return to the
                              		  default, use the no form of this command.

olsontimezone timezone version number

no olsontimezone

### Syntax Description

timezone

Olson Timezone names, which include the area (name of
                                          						continent or ocean) and location (name of a specific location within that
                                          						region, usually cities or small islands).

version number

Version of the tzupdater.jar or TzDataCSV.csv file. The
                                          						version indicates whether the file needs to be updated or not.

### Command Default

No Olson Timezone is set.

### Command Modes

Telephony-service configuration (config-telephony)

Voice register global configuration (config-register-global)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the olsontimezone command in either
                              		  telephony-service or voice register global configuration mode, with the current
                              		  version of Oracle’s Olson Timezone updater tool, tzupdater.jar, to set the
                              		  correct Olson Timezone.

For Cisco Unified 3911 and 3951 SIP IP phones and Cisco Unified 6921,
                              		  6941, 6961, and 6945 SCCP and SIP IP phones, the correct Olson Timezone updater
                              		  file is TzDataCSV.csv. The TzDataCSV.csv file is created based on the
                              		  tzupdater.jar file.

To set the correct time zone, you must determine the Olson Timezone
                              		  area/location where the Cisco Unified CME is located and download the latest
                              		  tzupdater.jar or TzDataCSV.csv to a TFTP server (such as flash or slot 0) that
                              		  is accessible to the Cisco Unified CME.

After a complete reboot, the phone checks if the version of its
                              		  configuration file is earlier or later than 2010o. If it is earlier, the phone
                              		  loads the latest tzupdater.jar and uses that updater file to calculate the
                              		  Olson Timezone.

To make the Olson Timezone feature backward compatible, both the time-zone and timezone commands are retained as legacy time
                              		  zones. Because the olsontimezone command covers approximately
                              		  500 time zones (Version 2010o of the tzupdater.jar file supports approximately
                              		  453 Olson Timezone IDs.), this command takes precedence when either the time-zone or the timezone command (that covers a total of 90
                              		  to100 time zones only) is present at the same time as the olsontimezone command.

## Examples

The following example shows 7:29 p.m. as the time set on a Cisco
                              		  Unified 7961 SCCP IP phone in Buenos Aires on May 13, 2011:

```
Router(config)# tftp-server flash:tzupdater.jar Router(config)# tftp-server flash:TzDataCSV.csv Router(config)# telephony-service Router(config-telephony)# olsontimezone America/Argentina/Buenos Aires version 2010o Router(config-telephony)# create cnf-files Router(config-telephony)# time-zone 21 Router(config-telephony)# exit Router(config)# clock timezone CST -6 Router(config)# clock summer-time date 12 October 2010 2:00 26 April 2011 2:00 Router(config)# exit Router# clock set 19:29:00 13 May 2011 Router# configure terminal Router(config)# telephony-service Router(config-telephony)# reset
```

The following example shows 3:25 p.m. as the time set on a Cisco
                              		  Unified 6921 SIP IP phone in Buenos Aires on November 17, 2011:

```
Router(config)# tftp-server slot0:tzupdater.jar Router(config)# tftp-server slot0:TzDataCSV.csv Router(config)# voice register global Router(config-register-global)# olsontimezone America/Argentina/Buenos Aires version 2010o Router(config-register-global)# create profile Router(config-register-global)# timezone 21 Router(config-register-global)# exit Router(config)# clock timezone CST -6 Router(config)# clock summer-time date 12 October 2010 2:00 26 April 2011 2:00 Router(config)# exit Router# clock set 15:25:00 17 November 2011 Router# configure terminal Router(config)# voice register global Router(config-register-global)# reset
```

### Related Commands

Command

Description

time-zone

Sets the time zone so that the correct local time is
                                          						displayed on Cisco Unified SCCP IP phones in a Cisco Unified CME system.

timezone

Sets the time zone used for Cisco Unified SIP IP phones in
                                          						a Cisco Unified CME system.

## overlap-signal

To configure overlap dialing in SCCP or SIP IP phones, use the
                              		  overlap-signal command in ephone, ephone-template, telephony-service, voice
                              		  register pool, voice register global, or voice register template configuration
                              		  mode.

overlap-signal

### Syntax Description

This command has no arguments or keywords.

### Command Default

Overlap-signal is disabled.

### Command Modes

Call-manager-fallback Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Telephony-service configuration (config-telephony) Voice register pool (config-register-pool) Voice register global configuration (config-register-global) Voice register template (config-register-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5 Cisco Unified SRST 8.5

This command was introduced.

### Usage Guidelines

SCCP IP phones

In SCCP IP phones, overlap dialing is enabled when the overlap signal
                              		  command is configured in ephone, ephone-template, and telephony-service
                              		  configurations modes.

SIP IP phones

In SIP IP Phones, overlap dialing is enabled when the overlap signal
                              		  command is configured in voice register pool, voice register global, and voice
                              		  register template configuration modes.

Cisco Unified SRST

In Cisco Unified SRST, overlap dialing is enabled on SCCP IP phones
                              		  when overlap signal command is configured in call-manager-fallback
                              		  configuration mode.

## Examples

The following example shows overlap-signal enabled on SCCP phones:

```
Router# show running config
!
!
telephony-service
 max-ephones 25
 max-dn 15
 load 7906 SCCP11.8-5-3S.loads
 load 7911 SCCP11.8-5-3S.loads
 load 7921 CP7921G-1.3.3.LOADS
 load 7941 SCCP41.8-5-3S.loads
 load 7942 SCCP42.8-5-3S.loads
 load 7961 SCCP41.8-5-3S.loads
 load 7962 SCCP42.8-5-3S.loads
 max-conferences 12 gain -6
 web admin system name cisco password cisco
 transfer-system full-consult
 create cnf-files version-stamp Jan 01 2002 00:00:00
 overlap-signal
!
ephone-template  1
 button-layout 1 line
 button-layout 3-6 blf-speed-dial
!
ephone-template  9
 feature-button 1 Endcall
 feature-button 3 Mobility
!
!
ephone-template  10
 feature-button 1 Park
 feature-button 2 MeetMe
 feature-button 3 CallBack
 button-layout 1 line
 button-layout 2-4 speed-dial
 button-layout 5-6 blf-speed-dial
 overlap-signal
!
ephone  10
 device-security-mode none
 mac-address 02EA.EAEA.0010
 overlap-signal
```

!

The following example shows overlap-signal configured in voice
                              		  register global and voice register pool 10:

```
Router#show running config
!
!
!
voice service voip
 ip address trusted list
  ipv4 20.20.20.1
 media flow-around
 allow-connections sip to sip
!
voice class media 10
 media flow-around
!
!
voice register global
 max-pool 10
 overlap-signal
!
voice register pool  5
 overlap-signal
!
!
!
```

The following example shows overlap-signal configured in
                              		  call-manager-fallback mode:

```
Router# show run | sec call-manager
call-manager-fallback
 max-conferences 12 gain -6
 transfer-system full-consult
 overlap-signal
```

## overwrite-dyn-stats (voice hunt-group)

To overwrite
                              		  statistics of previously joined dynamic agent with statistics of newly joined
                              		  dynamic agents for voice hunt group, use the overwrite-dyn-stats command in voice hunt-group configuration mode. To remove the
                              		  configuration, use the no form of
                              		  this command.

overwrite-dyn-stats

no overwrite-dyn-stats

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

voice hunt group configuration (config-voice-hunt-group)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

This
                                          						command was introduced.

### Usage Guidelines

This command is
                              		  configured to overwrite statistics of previously joined dynamic agent with
                              		  statistics of newly joined dynamic agents for voice hunt group. To remove the
                              		  configuration, use the no form of this command. The statistics for the first 32
                              		  members (both dynamic and static members) joining in an hour are collected in
                              		  the 32 statistic slots allotted. If any of the static members logout and login
                              		  during the hour, that member is allotted the same slot as previous. In
                              		  scenarios where free slots are available, free slots are used to write
                              		  statistics of the newly joined dynamic agent. Once all the 32 slots are
                              		  exhausted and a new dynamic member tries to join within the same hour, the overwrite-dyn-stats CLI takes effect. Using the CLI, the
                              		  hunt statistic slot for the first dynamic member that joined the hunt-group is
                              		  overwritten with the statistics of the newly joined dynamic member. The
                              		  overwriting for statistics will continue at the same slot.

## Examples

The following
                              		  example shows how the voice hunt group overwrite-dyn-stats option is enabled:

```
Router(config)# voice hunt-group 1 parallel
Router(config-voice-hunt-group)# overwrite-dyn-stats
```

| timezone | Olson Timezone names, which include the area (name of
                                          						continent or ocean) and location (name of a specific location within that
                                          						region, usually cities or small islands). |
|---|---|
| version number | Version of the tzupdater.jar or TzDataCSV.csv file. The
                                          						version indicates whether the file needs to be updated or not. Note In Cisco Unified CME 9.0, the latest version is 2010o. | Note | In Cisco Unified CME 9.0, the latest version is 2010o. |
| Note | In Cisco Unified CME 9.0, the latest version is 2010o. |

| Note | In Cisco Unified CME 9.0, the latest version is 2010o. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| time-zone | Sets the time zone so that the correct local time is
                                          						displayed on Cisco Unified SCCP IP phones in a Cisco Unified CME system. |
| timezone | Sets the time zone used for Cisco Unified SIP IP phones in
                                          						a Cisco Unified CME system. |

| timezone | Olson Timezone names, which include the area (name of
                                          						continent or ocean) and location (name of a specific location within that
                                          						region, usually cities or small islands). |
|---|---|
| version number | Version of the tzupdater.jar or TzDataCSV.csv file. The
                                          						version indicates whether the file needs to be updated or not. Note In Cisco Unified CME 9.0, the latest version is 2010o. | Note | In Cisco Unified CME 9.0, the latest version is 2010o. |
| Note | In Cisco Unified CME 9.0, the latest version is 2010o. |

| Note | In Cisco Unified CME 9.0, the latest version is 2010o. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| time-zone | Sets the time zone so that the correct local time is
                                          						displayed on Cisco Unified SCCP IP phones in a Cisco Unified CME system. |
| timezone | Sets the time zone used for Cisco Unified SIP IP phones in
                                          						a Cisco Unified CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 Cisco Unified SRST 8.5 | This command was introduced. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |