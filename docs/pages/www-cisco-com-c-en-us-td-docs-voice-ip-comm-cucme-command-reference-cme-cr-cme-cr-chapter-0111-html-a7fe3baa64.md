---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-0111-html-a7fe3baa64
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_0111.html
retrieved_at: 2026-08-21T22:56:12.453009+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: H

## Chapter: Cisco Unified CME Commands: H

# Cisco Unified CME Commands: H

## headset auto-answer line

To enable auto-answer on the specified line when the headset key is
                              		  engaged, use the headset auto-answer command in ephone configuration mode.
                              		  To disable headset auto-answer for this line, use the no form of this command.

headset auto-answer line line-number

no headset auto-answer line line-number

### Syntax Description

line-number

Phone line that should be automatically answered.

### Command Default

Headset auto-answer is not enabled.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command enables headset auto-answer on a particular line. A
                              		  line, as used in this command, is not identical to a phone button. A line, as used in this
                              		  command, represents the ability for a call connection on this phone, and the
                              		  line numbers generally follow a top-to-bottom sequence starting with the number
                              		  1.

The following examples represent common situations pertaining to a
                              		  button:line relationship:

- button 1:1—A single ephone-dn is associated with a single ephone
                                 			 button. Counts as one line.

- button 1o1,2,3,4,5—Five ephone-dns are overlaid on a single ephone
                                 			 button. Counts as one line.

- button 2x1—An ephone button acts as an extension for an overlaid
                                 			 ephone button. Counts as one line.

- Button is unoccupied or programmed for speed-dial. Does not count
                                 			 as a line.

## Examples

The following example shows how to enable headset auto-answer for
                              		  line 1 (button 1) and line 4 (button 4), which has overlaid ephone-dns but
                              		  counts as a single line in this context. In this example, four (1, 2, 3, and 4)
                              		  buttons are defined for ephone 3.

```
ephone 3
 button 1:2 2:4 3:6 4o21,22,23,24,25
 headset auto-answer line 1
 headset auto-answer line 4
```

The following example shows how to enable headset auto-answer for
                              		  line 2 (button 2), which has overlaid ephone-dns, and line 3 (button 3), which
                              		  is an overlay rollover line. In this example, three (1, 2, and 3) buttons are
                              		  defined for ephone 17.

```
ephone 17
 button 1:2 2o21,22,23,24,25 3x2
 headset auto-answer line 2
 headset auto-answer line 3
```

The following example shows how to enable headset auto-answer for
                              		  line 2 (button 3) and line 3 (button 5). In this case, the button numbers do
                              		  not match the line numbers because buttons 2 and 4 are not used.

```
ephone 25
 button 1:2 3:4 5:6
 headset auto-answer line 2
 headset auto-answer line 3
```

## hfs enable

To enable the HTTP File-Fetch Server (HFS) download service on an IP
                              		  Phone in a Cisco Unified CME system, use the hfs enable command in telephony-service configuration
                              		  mode. To disable the HFS download service, use the no form of this command.

hfs enable [ port port-number ]

no hfs enable [ port port-number ]

### Syntax Description

port port-number

(Optional) Specifies the port where the HFS download
                                          						service is enabled. Range is from 1024 to 65535.

### Command Default

An IP Phone is unable to download configuration and firmware files
                              		  through the HFS infrastructure.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

Modification

15.2(1)T

This command was introduced.

### Usage Guidelines

To enable the HFS download service, the underlying HTTP server must
                              		  be enabled first using the ip http server command because the HFS infrastructure is
                              		  built on top of an existing IOS HTTP server.

This HFS infrastructure enables multiple HTTP services to co-exist.
                              		  The HFS download service runs on custom port 6970 but can also share default
                              		  port 80 with other services. Other HTTP services run on other non-standard
                              		  ports like 1234.

Use the hfs enable command without keyword or argument to
                              		  enable the HFS download service on the default HTTP server port.

## Examples

The following example shows how to enable the HFS download service
                              		  for Cisco Unified SIP IP Phone 7945 on port 65500:

```
Router(config)# ip http server Router(config)# ip http port 1234 Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# load 7945 SIP45.8.3.3S Router(config-register-global)# create profile Router(config-register-global)# exit Router (config)# telephony-service Router(config-telephony)# hfs enable port 65500
```

The following examples show how to enable the HFS service on default
                              		  and custom ports.

For the default port:

```
Router(config)# ip http server Router(config)# ip http port 1234 .
.
Router (config)# telephony-service Router(config-telephony)# hfs enable
```

For the custom port:

```
Router(config)# ip http server Router(config)# ip http port 1234 .
.
Router (config)# telephony-service Router(config-telephony)# hfs enable port 6970
```

The following example shows how an entered custom HFS port clashes
                              		  with the underlying ip http port. Port 6970 is configured as the IP HTTP port.
                              		  When the HFS port is configured with the same value, an error message is
                              		  displayed to show that the port is already in use.

```
Router(config)# ip http server Router (config)# ip http port 6970 .
.
Router (config)# telephony-service Router (config-telephony)# hfs enable port 6970 .
Invalid port number or port in use by other application
```

The HFS port number is already in use by the underlying IP HTTP
                              		  server so an HFS port that is different from the underlying IP HTTP port must
                              		  be used.

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profile files required for SIP
                                          						phones.

ip http port

Specifies the port where the HTTP service is run.

ip http server

Enables the underlying IOS HTTP server of the the HFS
                                          						infrastructure.

## hfs home-path

To set up a home-path for IP phone firmware files, use the hfs home-path command in telephony-service
                              		  configuration mode. To remove a directory as a home-path for phone files, use
                              		  the no form of this command.

hfs home-path path

no hfs home-path path

### Syntax Description

path

Directory path where only IP phone firmware and
                                          						configuration files are stored.

### Command Default

No directory path is specified for the storage of IP phone firmware
                              		  and configuration files.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

Modification

15.2(1)T

This command was introduced.

### Usage Guidelines

Use the hfs home-path command to specify a directory path as
                              		  the home-path to store IP phone firmware files.

## Examples

The following example shows how to set up a home-path for IP phone
                              		  firmware files in Cisco Unified CME:

```
Router(config)# telephony service Router(config-telephony)# hfs home-path flash:/cme/loads/
```

The following example shows how a new directory called phone-load can
                              		  be created under the root directory of the flash memory and set as the hfs
                              		  home-path:

```
cassini-c2801# mkdir flash:phone-loads Create directory filename [phone-loads]?
Created dir flash:phone-loads
cassini-c2801#sh flash:
-#- --length-- -----date/time------ path
1     13932728 Mar 22 2007 15:57:38 +00:00 c2801-ipbase-mz.124-1c.bin
2     33510140 Sep 18 2010 01:21:56 +00:00 rootfs9951.9-0-3.sebn
3       143604 Sep 18 2010 01:22:20 +00:00 sboot9951.111909R1-9-0-3.sebn
4         1249 Sep 18 2010 01:22:40 +00:00 sip9951.9-0-3.loads
5        66996 Sep 18 2010 01:23:00 +00:00 skern9951.022809R2-9-0-3.sebn
6        10724 Sep 18 2010 00:59:48 +00:00 dkern9951.100609R2-9-0-3.sebn
7      1507064 Sep 18 2010 01:00:24 +00:00 kern9951.9-0-3.sebn
8            0 Jan 5 2011 02:03:46 +00:00 phone-loads
14819328 bytes available (49192960 bytes used)
cassini-c2801#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
cassini-c2801(config)#tele
cassini-c2801(config)# telephony-service cassini-c2801(config-telephony)#hfs hom
cassini-c2801(config-telephony)#hfs home-path flash:?
WORD
cassini-c2801(config-telephony)# hfs home-path flash:phone-loads cassini-c2801(config-telephony)#
```

### Related Commands

Command

Description

hfs enable

Enables the HFS download service on an IP Phone in a Cisco
                                          						Unified CME system.

## hlog-block (voice
                        	 hunt-group)

To disable agent
                              		  status control (logout/login) for voice hunt group on SIP or SCCP phones using
                              		  Hlog softkey or by using FAC, use the hlog-block command in voice hunt-group configuration mode. To remove the
                              		  configuration, use the no form of
                              		  this command.

hlog-block

no hlog-block

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

15.4(3)M5

Cisco
                                          						Unified CME 10.5

This
                                          						command was introduced.

### Usage Guidelines

This command
                              		  disables the agent status control such that SIP or SCCP phones are not be able
                              		  to logout/login from the voice hunt group using Hlog/FAC.

## Examples

The following
                              		  example shows how the voice hunt group hlog-block option is enabled for a
                              		  phone:

```
Router(config)# voice hunt-group 1 parallel
Router(config-voice-hunt-group)# hlog-block
```

## hold-alert

To set a repeating audible alert notification when a call is on hold
                              		  on a Cisco Unified IP phone, use the hold - alert command in ephone-dn or ephone-dn-template configuration mode.
                              		  To disable this feature, use the no form of this command.

hold-alert timeout { idle | originator | shared | shared-idle } [ recurrence recurrence-timeout ] [ ring-silent-dn ]

no hold-alert timeout { idle | originator | shared | shared-idle } [ recurrence recurrence-timeout ] [ ring-silent-dn ]

timeout

Interval after which an audible alert notification is
                                       					 repeated, in seconds. Range is from 15 to 300. There is no default.

idle

Alerts only when the phone is idle.

originator

Alerts whether the phone is idle or busy.

shared

Alerts only when the extension is idle but alerts all phones
                                       					 that share the line.

shared-idle

Alerts all idle phones that share the line.

recurrence

Alerts recurrence after first timeout.

recurrence-timeout

Call on-hold recurrence timeout in seconds. Range is from 2
                                       					 to 300.

ring-silent-dn

Rings the silent DN.

### Command Default

Audible alert notification for on-hold calls is disabled. Only a
                              		  visual indication is provided.

### Command Modes

Ephone-dn configuration (config-ephone) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

The shared-idle option and ring-silent-dn parameter were
                                          						introduced.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

15.1(3)T2

Cisco Unified CME 8.5

The recurrence parameter was introduced.

15.1(4)M1

Cisco Unified CME 8.6

The recurrence parameter was introduced.

### Usage Guidelines

Use the hold - alert command
                              		  to set an audible alert notification on a Cisco Unified IP phone to remind the
                              		  phone user that a call is on hold. The timeout argument specifies the time interval
                              		  in seconds from the time the call is placed on hold to the time the on-hold
                              		  audible alert is generated. The alert is repeated every timeout seconds.

When the idle keyword is enabled, a one-second burst of
                              		  ringing on the phone is generated on the IP phone that placed the call in the
                              		  hold state, but only if the phone is in the idle state. If the phone is in
                              		  active use, no on-hold alert is generated.

When the originator keyword is enabled, a one-second
                              		  burst of ringing is generated on the phone that placed the call in the hold
                              		  state, but only if the phone is in the idle state. If the phone is in use on
                              		  another call, an audible beep (call-waiting tone) is generated.

When the shared keyword is enabled, a one-second ring
                              		  burst is generated for all the idle phones that share the extension with the
                              		  on-hold call. Phones that are in use do not receive an audio beep (call-waiting
                              		  tone) alert. Only the phone that placed the call on hold hears a call-waiting
                              		  beep if it is busy.

When the shared-idle keyword is enabled, a one-second ring burst is generated for
                              		  all the idle phones that share the line with the on-hold call.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example sets audible alert notification to idle on
                              		  extension 1111:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1111 Router(config-ephone-dn)# name phone1 Router(config-ephone-dn)# hold-alert 100 idle
```

The following example uses an ephone-dn template to set audible alert
                              		  notification for extension 1111 to only occur when the phone is idle:

```
Router(config)# ephone-dn-template 3 Router(config-ephone-dn-template)# hold-alert 100 idle Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1111 Router(config-ephone-dn)# name phone1 Router(config-ephone-dn)# ephone-dn-template 3 The following example uses an ephone-dn to set an additional timeout value between 2 and 300.
Router(config-ephone-dn)# hold-alert 
  <15-300> call on-hold timeout in seconds
Router(config-ephone-dn)# hold-alert 15
  idle         alert on-hold originator only if idle
  originator   alert on-hold originator always
  shared       alert all phones that share the line
  shared-idle  alert all idle phones that share the line
Router(config-ephone-dn)# hold-alert 15 idle 
  recurrence      alternate alert recurrence timeout after first
  ring-silent-dn  ring the silent DN
Router(config-ephone-dn)# hold-alert 15 idle recurrence 
  <2-300>  call on-hold recurrence timeout in seconds
Router(config-ephone-dn)# hold-alert 15 idle recurrence 3 
  ring-silent-dn  ring the silent DN
```

The following example uses an ephone-dn-template to set an additional
                              		  timeout value between 2 and 300.

```
Router(config-ephone-dn-template)# hold-alert 
  <15-300> call on-hold timeout in seconds
Router(config-ephone-dn-template)# hold-alert 15
  idle         alert on-hold originator only if idle
  originator   alert on-hold originator always
  shared       alert all phones that share the line
  shared-idle  alert all idle phones that share the line
Router(config-ephone-dn-template)# hold-alert 15 idle 
  recurrence      alternate alert recurrence timeout after first
  ring-silent-dn  ring the silent DN
Router(config-ephone-dn-template)# hold-alert 15 idle recurrence 
  <2-300>  call on-hold recurrence timeout in seconds
Router(config-ephone-dn-template)# hold-alert 15 idle recurrence 3 
  ring-silent-dn  ring the silent DN
```

### Related Commands

Command

Description

ephone-dn-template (ephone-dn)

Applies ephone-dn-template to the ephone-dn being
                                          						configured.

## hold-alert (voice
                        	 register global)

To enable a
                              		  one-time audible alert notification for a call still on hold after a subsequent
                              		  call has ended in Cisco Unified CME, use the command in voice register global
                              		  configuration mode. To disable this feature, use the no form of
                              		  this command.

hold-alert

no hold-alert

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Audible alert
                              		  notification for on-hold calls is disabled.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

### Usage Guidelines

This command
                              		  enables a one time audible alert notification on all supported SIP phones in a
                              		  Cisco Unified CME system to remind the phone user that a call is on hold after
                              		  a subsequent call has ended. The alert is not repeated and does not alert until
                              		  a subsequent call ends after the original call was placed on hold. This applies
                              		  globally to all SIP CME Phones.

## Examples

The following
                              		  example shows how to set audible alert notification on SIP phones for on-hold
                              		  calls:

```
Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# hold-alert Router(config-register-global)# create profile ! Restart phone(s) to update config file change
```

### Related Commands

Command

Description

call-waiting (voice register pool)

Enables
                                          						call waiting on a SIP phone.

mode (voice register global)

Enables
                                          						the mode for provisioning SIP phones in a Cisco CallManager Express (Cisco CME)
                                          						system.

## hops

To define the number of times that a call can proceed to the next
                              		  ephone-dn in a peer or longest-idle ephone hunt group before the call proceeds
                              		  to the final ephone-dn, use the hops command in ephone hunt configuration
                              		  mode. To return to the default number of hops, use the no form of this command.

hops number

no hops number

### Syntax Description

number

Number of hops before the call proceeds to the final
                                          						ephone-dn. Range is from 2 to 20, but the value must be less than or equal to
                                          						the number of extensions that are specified in the list command. Default automatically
                                          						adjusts to the number of hunt group members.

### Command Default

The number of hops automatically adjusts to the number of ephone hunt
                              		  group members.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

### Command Modes

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(7)T

Cisco CME 3.1

The maximum number of hops was restricted to the number of
                                          						extensions specified in the list command.

12.3(11)XL

Cisco CME 3.2.1

Increased maximum number of hops to 20.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco Unified CME 4.0

The default was changed from 2 hops to automatically adjust
                                          						the number of hops to the number of ephone hunt group members.

12.4(9)T

Cisco Unified CME 4.0

The modification to change the default was integrated into
                                          						Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command is valid only for peer and longest-idle ephone hunt
                              		  groups in Cisco Unified CallManager Express systems.

This command is required when you are configuring the auto logout command for peer and longest-idle hunt groups.

## Examples

The following example sets the number of hops to 6 for peer hunt
                              		  group 3:

```
Router(config)# ephone-hunt 3 peer Router(config-ephone-hunt)# hops 6
```

### Related Commands

Command

Description

auto logout

Enables the automatic change of an ephone hunt group
                                          						agent's ephone-dn to not-ready status.

final

Defines the last ephone-dn in an ephone hunt group.

list

Defines the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the current number of allowable redirects in a
                                          						Cisco Unified CME system.

no-reg (ephone-hunt)

Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper.

pilot

Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list.

## hops (voice hunt-group)

To define the number of times that a call can hop to the next number
                              		  in a peer hunt group before the call proceeds to the final number, use the hops command in voice hunt-group
                              		  configuration mode. To return to the default number of hops, use the no form of this command.

hops number

no hops

### Syntax Description

number

Number of hops before the call proceeds to the final
                                          						number. Range is 2 to 10, but the value must be less than or equal to the
                                          						number of extensions that are specified in the list command. The default is the
                                          						same number as there are destinations defined under the list command.

### Command Default

The default is the number of directory-number arguments configured in the list command.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Cisco IOS Release

Cisco product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command is valid only for peer or longest-idle voice hunt groups
                              		  in Cisco Unified CME systems.

## Examples

The following example shows how to set the number of hops to 6 for
                              		  peer voice hunt group 1:

```
Router(config)# voice hunt-group 1 peer Router(config-voice-hunt-group)# list 1000, 1001, 1002, 1003, 1004, 1005, 1006, 006, 1007, 1008, 1009 Router(config-voice-hunt-group)# hops 6
```

### Related Commands

Command

Description

final (voice hunt-group)

Defines the last extension in a voice hunt group.

list (voice hunt-group)

Defines the directory numbers that participate in a hunt
                                          						group.

timeout (voice hunt-group)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list and defines
                                          						the last directory number in the hunt group.

## host-id-check

To configure host-id-check option for a vpn-profile, use the host-id-check command in vpn-profile configuration mode. To disable the
                              		  host-id-check configuration, use the no form of this command.

host-id-check [ enable | disable ]

### Syntax Description

enable

Enables host-id-check option in a vpn-profile.

disable

Disables host-id-check option in a vpn-profile.

### Command Default

Host-id-check option is enabled.

### Command Modes

Vpn-profile configuration (conf-vpn-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to configure host-id-check option for a vpn-profile.
                              		  This host ID check enhances the security by parsing the host name or the IP
                              		  from latest URL of the VPN concentrator to check against the subjectAltNames
                              		  field within the certificate, if the subjectAltNames existed. This check is
                              		  performed by the phone.

## Examples

The following example shows the host-id-check option enabled in
                              		  vpn-profile 2 and disabled in vpn-profile 1:

```
Router# show run
!
voice service voip
 ip address trusted list
  ipv4 20.20.20.1
 vpn-group 1
  vpn-gateway 1 https://9.10.60.254/SSLVPNphone
  vpn-trustpoint 1 trustpoint cme_cert root
  vpn-hash-algorithm sha-1
 vpn-profile 1
  keepalive 50
  host-id-check disable
 vpn-profile 2
  mtu 1300
  password-persistent enable
  host-id-check enable
 sip
!
voice class media 10
 media flow-around
!
!
voice register global
 max-pool 10
```

### Related Commands

Command

Description

vpn-profile

Defines a VPN-profile.

## hunt-group report url

To set the filename parameters and the URL path where hunt group call
                              		  statistics are sent using TFTP, use the hunt - group report url command in telephony service mode. To disable this feature, use
                              		  the no form of this command.

hunt-group report url { prefix | suffix }

no hunt-group report url { prefix | suffix }

prefix

Provides the prefix of the filename to which the statistics
                                       					 are written. The prefix of the filename appears at the end of the URL.

suffix

Provides the suffix of the filename to which the statistics
                                       					 are written. Range is <0-1> to <1-200>.

### Command Default

This command is disabled by default.

### Command Modes

telephony-service (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T .

### Related Commands

Command

Description

hunt-group report delay hours

Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file.

hunt-group report every hours

Sets the hourly interval after which Cisco CME B-ACD call
                                          						statistics are automatically transferred to a file.

## hunt-group
                        	 statistics write-v2

To write all the
                              		  ephone hunt and voice hunt group statistics to a file along with total logged
                              		  in and logged out time for agents, use the hunt-group statistics write-v2 command in privileged EXEC mode.

hunt-group statistics write-v2 location

### Syntax Description

location

URL or
                                          						filename to which the statistics is written.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.3(2)T

Cisco
                                          						Unified CME 9.5

This
                                          						command was introduced.

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

This
                                          						command was enhanced to add statistics for total logged in and logged out time
                                          						for voice hunt group.

### Usage Guidelines

Use the hunt-group statistics write-v2 command to write out, in hourly
                              		  increments, all the ephone and voice hunt group statistics for the past seven
                              		  days, along with total logged in and logged out time for agents. This command
                              		  is intended to be used when normal hunt group statistics collection is
                              		  interrupted, perhaps due to TFTP server failure. If applicable, the TFTP
                              		  statistics report consists of both ephone and voice hunt statistics.

## Examples

The following
                              		  example shows how the hunt-group statistics write-v2 command writes a combination of ephone
                              		  and voice hunt group statistics to a file in TFTP server 202.153.144.25:

```
Router# hunt-group statistics write-v2 tftp://202.153.144.25/cmeteam/stats Writing out all hunt group statistics to tftp://202.153.144.25/cmeteam/stats
01:47:08 UTC Mon Mar 21 2016,
,
EPHONE HUNT GROUP STAT,
01, Sat 00:00 - 01:00, HuntGp, 02, 02, 00001, 00001, 00000, 0007, 0007, 000001, 000001, 0000, 00000, 000000, 000000,
01, Sat 00:00 - 01:00, Agent, 5012, 00001, 000001, 000001, 00000, 000000, 000000, 00001, 000008, 000008, 00001, 000003, 000003,
01, Sat 00:00 - 01:00, Queue, 00000, 00001, 00000, 00006, 00006, 00000, 00000, 00000, 00000, 00000, 
01, Sat 01:00 - 02:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 02:00 - 03:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 03:00 - 04:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 04:00 - 05:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 05:00 - 06:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 06:00 - 07:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 07:00 - 08:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 
.
.
.
06, Fri 19:00 - 20:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 20:00 - 21:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 21:00 - 22:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 22:00 - 23:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 23:00 - 00:00, HuntGp, 02, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
VOICE HUNT GROUP STAT,
01, Fri 01:00 - 02:00, HuntGp, 03, 02, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 01:00 - 02:00, Agent, 2001, 00000, 000000, 000000, 00000, 000000, 000000, 00001, 000067, 000067, 00000, 000000, 000000, 000000, 003600,
01, Fri 01:00 - 02:00, Agent, 2002, 00000, 000000, 000000, 00000, 000000, 000000, 00001, 000006, 000006, 00000, 000000, 000000, 000000, 003600,
01, Fri 01:00 - 02:00, Agent, 2005, 00000, 000000, 000000, 00000, 000000, 000000, 00001, 000004, 000004, 00000, 000000, 000000, 000000, 003600,
01, Fri 01:00 - 02:00, Queue, 00007, 00005, 00000, 00013, 00030, 00002, 00034, 00002, 00000, 00000, 00000, 00002, 00000, 00000, 00003, 00002, 00000, 00000, 00000, 00000,
01, Fri 02:00 - 03:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 03:00 - 04:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
.
.
.
02, Thu 20:00 - 21:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
02, Thu 21:00 - 22:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
02, Thu 22:00 - 23:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
02, Thu 23:00 - 00:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
02, Fri 00:00 - 01:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
```

### Related Commands

Command

Description

hunt-group report delay hours

Delays hunt group statistics collection for a specified number of hours.

hunt-group report every hours

Sets
                                          						the hourly interval at which Cisco Unified CME B-ACD call statistics are
                                          						automatically transferred to a file.

hunt-group report url

Sets
                                          						filename parameters and the URL path where Cisco Unified CME B-ACD call
                                          						statistics are to be sent using TFTP.

hunt-group statistics write-all

Writes all ephone and voice hunt group statistics to a
                                          						fille.

show voice hunt-group statistics

Displays voice hunt group statistics.

show ephone-hunt statistics

Displays ephone hunt group statistics.

## hunt-group logout

To set the hunt-group logout options, use the hunt-group logout command with DND , Hlog , notify , and threshold keywords in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

hunt-group logout [ DND | HLog | notify | threshold number ]

no hunt-group logout [ DND | HLog | notify | threshold number ]

### Syntax Description

DND

Agent phones do not answer the number of calls specified in
                                          						the auto logout command and are automatically
                                          						placed in both DND status and not-ready status. The HLog soft key is not
                                          						displayed on phones.

HLog

Agent phones do not answer the number of calls specified in
                                          						the auto logout command and are automatically
                                          						placed only in not-ready status. The HLog soft key is displayed on phones in
                                          						addition to the DND soft key.

notify

Enables logout call in queue notification on HLog PLK
                                          						button.

threshold number

Defines the boundary value by which how the Hlog PLK
                                          						indicates the number of calls in queue on the logout agent’s phone. Range is 1
                                          						to 65535.

### Command Default

DND and HLog functionality is not separate and the HLog soft key will
                              		  not be displayed on phones. The default is DND.

The default for threshold is disabled and the LED on the HLOG PLK
                              		  blinks slow in amber as long as there are calls in queue.

The default for notify is disabled and has no LED display.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

15.2(2)T2

Cisco Unified CME 9.1

The notify and threshold keywords were added.

### Usage Guidelines

When Do Not Disturb (DND) functionality is activated, no calls are
                              		  received at the phone, including ephone hunt group calls. DND is activated and
                              		  canceled using the DND soft key or the DND feature access code (FAC).

When HLog functionality is activated, hunt-group agents are placed in
                              		  not-ready status and hunt-group calls are blocked from the phone. Other calls
                              		  that directly dial the phone’s extension numbers are still received at the
                              		  phone. HLog is activated and canceled using the HLog soft key or an HLog FAC.

If the auto logout command is used, the Automatic Agent Status
                              		  Not-Ready feature is invoked for an ephone hunt group. This feature is
                              		  triggered when an ephone-dn member does not answer a specified number of ephone
                              		  hunt group calls. The following actions take place:

- If the hunt-group logout HLog command has been used, the agent is placed
                                 			 in not-ready status. The agent’s ephone-dn will not receive further hunt group
                                 			 calls but will receive calls that directly dial the ephone-dn’s extension
                                 			 numbers. An agent in not-ready status can return to ready status by pressing
                                 			 the HLog soft key or by using the HLog FAC.

- If the hunt-group logout HLog command has not been used or if the hunt-group logout DND command has been used, the phone on which
                                 			 the ephone-dn appears is placed into DND mode, in which the ephone-dn does not
                                 			 receive any calls at all, including hunt-group calls. The red lamp on the phone
                                 			 lights to indicate DND status. An agent in DND mode can return to ready status
                                 			 by pressing the DND soft key or by using the DND FAC.

The DND and Hlog keywords are exclusive and are used to
                              		  enable separate handling of DND and HLog functionality for hunt-group agents
                              		  and to display the HLog softkey on phones.

The notify and threshold keywords are used to enable the
                              		  indication of the calls in queue for logout agents using the Hlog Programmable
                              		  Line Key.

If the threshold number is enabled, the LED on the Hlog PLK blinks slow in amber for
                              		  the number of calls in queue less than the threshold and blinks fast in red for
                              		  those equal or beyond the threshold. This command will not take effect if hunt-group logout notify is disabled.

## Examples

The following example creates hunt group 3 with three agents
                              		  (extensions 1001, 1002, and 1003). It specifies that after one unanswered call,
                              		  an agent should be put into not-ready status but not into DND status.

```
Router(config)# telephony-service Router(config-telephony)# hunt-group logout HLog Router(config-telephony)# exit Router(config)# ephone-hunt 3 peer
Router(config-ephone-hunt)# pilot 4200
Router(config-ephone-hunt)# list 1001, 1002, 1003
Router(config-ephone-hunt)# timeout 10
Router(config-ephone-hunt)# auto logout
Router(config-ephone-hunt)# final 4500
```

The following example sets the value of threshold to 2:

```
Router(config)# telephony-service Router(config-telephony)# hunt-group logout ? DND        logout using DND softkey or PLK
  HLog       logout using HLog softkey or PLK
  notify     enable logout call in queue notification on HLog PLK button
  threshold  configure logout call in queue threshold
Router(config-telephony)# hunt-group logout threshold ? <1-65535>  number of calls in queue
Router(config-telephony)# no hunt-group logout notify Router(config-telephony)# no hunt-group logout threshold % Incomplete command.
```

```
Router(config-telephony)# no hunt-group logout threshold 2 Router(config-telephony)# no hunt-group logout ? DND        logout using DND softkey or PLK
```

HLog logout using HLog softkey or PLK

```
notify     enable logout call in queue notification on HLog PLK button
  threshold  configure logout call in queue threshold
Router(config-telephony)# no hunt-group logout dnd Router(config-telephony)# no hunt-group logout hlog
```

### Related Commands

Command

Description

auto logout

Enables the automatic change of an agent’s ephone-dn to
                                          						not-ready status after a specified number of hunt-group calls are not answered.

feature-button index < feature identifier >
                                          						[ label label ]

Enables the feature button configuration on a line key.

## hunt-group report
                        	 delay hours

To delay the
                              		  automatic transfer of Cisco CallManager Express (Cisco CME) basic automatic
                              		  call distribution (B-ACD) call statistics to a file, use the hunt-group report delay hours command in telephony-service configuration mode. To remove to
                              		  the delay setting, use the no form of
                              		  this command.

hunt-group report delay number hours

no hunt-group report delay number hours

### Syntax Description

number

Number
                                          						of hours by which the collection of statistics can be extended for the
                                          						statistics collection periods configured with the hunt-group report every hours command. The range is from 1 to 10.

### Command Default

Hunt-group report
                              		  is delayed for one hour.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						product

Modification

12.3(11)XL

Cisco
                                          						CME 3.2.1

This
                                          						command was introduced.

12.3(14)T

Cisco
                                          						CME 3.3

This
                                          						command was integrated into Cisco IOS Release 12.3(14)T.

### Usage Guidelines

This command is
                              		  used for Cisco CME basic automatic call distribution (B-ACD) and auto-attendant
                              		  (AA) service only.

The hunt-group report delay hours command is used as part of a statistics reporting configuration
                              		  that allows Cisco CME B-ACD call statistics to be sent automatically to files
                              		  using TFTP. For detailed information, see Cisco CME B-ACD and Tcl
                                 			 Call-Handling Applications .

Statistics are
                              		  collected and stored ( statistics collect command and hunt-group report url command) in specified intervals ( hunt-group report every hours command). The default is for the statistics to be collected one
                              		  hour after the specified interval. Because calls are counted when they end,
                              		  some of the longer calls may not be counted. For example, if there is a call
                              		  from 1:35 p.m. to 3:30 p.m., the interval is 1 hour, and there is no delay,
                              		  TFTP will write the 1 p.m. to 2 p.m. statistics at 3 p.m. However, at 3 p.m.,
                              		  the 1:35 p.m. call is still active, so the call will not be counted at that
                              		  time as occurring in the 1 p.m. to 2 p.m. time slot. When the call finishes at
                              		  3:30 p.m., it will be counted as occurring from 1 p.m. to 2 p.m. The show hunt-group command will report it, but TFTP will
                              		  have already sent out its report. To include the 1:35 p.m. call, you could use
                              		  the hunt-group report delay hours command to delay TFTP statistics reporting
                              		  for an extra hour so the 1 p.m. to 2 p.m. report will be written at 4 p.m.
                              		  instead of 3 p.m.

## Examples

The following
                              		  example shows a configuration in which statistics are reported for B-ACD calls
                              		  that occur within three-hour time frames, but the collection of the statistic
                              		  collection is extended for an extra hour to include calls that did not end
                              		  within the three-hour time period:

```
Router(config)# telephony-service Router(config-telephony)# hunt-group report every 3 hours Router(config-telephony)# hunt-group report delay 1 hours
```

The following
                              		  is an example of a report that the previous configuration might send to a file
                              		  if the statistics collect command was entered at 18:20:

```
23:00:00 UTC Tue Dec 20 2004,
,
01, Tue 18:00 - 19:00, HuntGp, 02, 01, 00005, 00002, 0003, 0006, 000001, 000001, 0011,
01, Tue 19:00 - 20:00, HuntGp, 02, 02, 00000, 00000, 0000, 0000, 000000, 000000, 0000,
01, Tue 20:00 - 21:00, HuntGp, 02, 02, 00006, 00003, 0003, 0009, 000001, 000003, 0012,
```

Statistics
                              		  collection has to take place for at least three hours for the statistics to be
                              		  written to a file. The following is a chronology of events:

- At 19:00,
                                 			 the statistics collection was active for 40 minutes, so no statistics were
                                 			 written to file.

- At 20:00,
                                 			 the statistics collection was active for 1 hour and 40 minutes, so no
                                 			 statistics were written to file.

- At 21:00,
                                 			 the statistics collection was active for 2 hours and 40 minutes, so no
                                 			 statistics were written to file.

- At 22:00,
                                 			 the statistics collection was active for 3 hours and 40 minutes but there is a
                                 			 one-hour delay, so no statistics were written to file.

- At 23:00 the
                                 			 statistics were written to a file using TFTP.

### Related Commands

Command

Description

hunt-group report every hours

Sets
                                          						the hourly interval after which Cisco CME B-ACD call statistics are
                                          						automatically transferred to a file.

hunt-group report url

Sets
                                          						filename parameters and the URL path where Cisco CME B-ACD call statistics are
                                          						to be sent using TFTP.

statistics collect

Enables the collection of Cisco CME B-ACD call data for an ephone hunt group.

## hunt-group report every hours

To set the hourly interval at which Cisco CallManager Express (Cisco
                              		  CME) basic automatic call distribution (B-ACD) call statistics are
                              		  automatically transferred to a file, use the hunt-group report every hours command in telephony-service configuration mode. To remove the
                              		  interval setting, use the no form of this command.

hunt-group report every number hours

no hunt-group report every number hours

### Syntax Description

number

Number of hours after which auto-attendant (AA) call
                                          						statistics are collected and reported. The range is from 1 to 84.

### Command Default

No hourly interval is configured.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

### Usage Guidelines

This command is used for Cisco CME basic automatic call distribution
                              		  (B-ACD) and auto-attendant (AA) service only.

The hunt-group report every hours command is used as part of a statistics reporting configuration
                              		  that allows Cisco CME B-ACD call statistics to be sent automatically to files
                              		  by means of TFTP. For detailed information, see Cisco
                                 			 CME B-ACD and Tcl Call-Handling Applications .

Because calls are counted when they end, some of the longer calls may
                              		  not be counted in the report. To delay the time in which statistics are
                              		  collected and transferred you may configure a delay time with the hunt-group report delay hours command.

## Examples

The following example sets the statistics collection to occur every
                              		  three hours. There is no delay.

```
Router(config)# telephony-service Router(config-telephony)# hunt-group report every 3 hours
```

The following is an example of a report that the previous
                              		  configuration might send to a file if the statistics collect command was entered at 18:20:

```
22:00:00 UTC Tue Dec 20 2005,
,
01, Tue 18:00 - 19:00, HuntGp, 02, 01, 00005, 00002, 0003, 0006, 000001, 000001, 0011,
01, Tue 19:00 - 20:00, HuntGp, 02, 02, 00000, 00000, 0000, 0000, 000000, 000000, 0000,
01, Tue 20:00 - 21:00, HuntGp, 02, 02, 00006, 00003, 0003, 0009, 000001, 000003, 0012,
```

Statistics collection has to take place for at least three hours for
                              		  the statistics to be written to a file. The following is a chronology of
                              		  events:

- At 19:00, the statistics collection was active for 40 minutes, so
                                 			 no statistics were written to file.

- At 20:00, the statistics collection was active for 1 hour and 40
                                 			 minutes, so no statistics were written to file.

- At 21:00, the statistics collection was active for 2 hours and 40
                                 			 minutes, so no statistics were written to file.

- At 22:00, the statistics collection was active for 3 hours and 40
                                 			 minutes, so statistics were written to a file using TFTP.

If the previous example were configured for a delay of one hour using
                              		  the hunt-group report delay 1 hours command, the statistics would be written one hour later at
                              		  23:00.

### Related Commands

Command

Description

hunt-group report delay hours

Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file.

hunt-group report url

Sets filename parameters and the URL path where Cisco CME
                                          						B-ACD call statistics are to be sent using TFTP.

statistics collect

Enables the collection of Cisco CME B-ACD call statistics
                                          						for an ephone hunt group.

## hunt-group statistics write-all

To write all the ephone and voice hunt group statistics to a file,
                              		  use the hunt-group statistics write-all command in privileged EXEC mode.

hunt-group statistics write-all location

### Syntax Description

location

URL or filename to which the statistics should be written.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

15.2(2)T

Cisco Unified CME 9.0

This command was introduced to replace the ephone-hunt statistics write-all command.

### Usage Guidelines

Use the hunt-group statistics write-all command to write out, in hourly
                              		  increments, all the ephone and voice hunt group statistics for the past seven
                              		  days. This command is intended to be used when normal hunt group statistics
                              		  collection is interrupted, perhaps due to TFTP server failure. If applicable,
                              		  the TFTP statistics report consists of both ephone and voice hunt statistics.

The commands that are normally used to provide hunt group statistics
                              		  are hunt-group report delay hours , hunt-group report every hours , hunt-group report url , and statistics collect . These commands allow you to specify
                              		  shorter, more precise reporting periods and file naming conventions.

## Examples

The following example shows how the hunt-group statistics write-all command writes a combination of ephone
                              		  and voice hunt group statistics to a file in TFTP server 223.255.254.254:

```
Router# hunt-group statistics write-all tftp://223.255.254.254/ngm/huntgp/uc500/statall Writing out all hunt group statistics to tftp://223.255.254.254/ngm/huntgp/uc500/statall
00:08:34 UTC Sat Feb 19 2011,
,
EPHONE HUNT GROUP STAT,
01, Sat 00:00 - 01:00, HuntGp, 02, 02, 00001, 00001, 00000, 0007, 0007, 000001, 000001, 0000, 00000, 000000, 000000,
01, Sat 00:00 - 01:00, Agent, 5012, 00001, 000001, 000001, 00000, 000000, 000000, 00001, 000008, 000008, 00001, 000003, 000003,
01, Sat 00:00 - 01:00, Queue, 00000, 00001, 00000, 00006, 00006, 00000, 00000, 00000, 00000, 00000, 
01, Sat 01:00 - 02:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 02:00 - 03:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 03:00 - 04:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 04:00 - 05:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 05:00 - 06:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 06:00 - 07:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 07:00 - 08:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 
.
.
.
06, Fri 19:00 - 20:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 20:00 - 21:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 21:00 - 22:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 22:00 - 23:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
06, Fri 23:00 - 00:00, HuntGp, 02, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
VOICE HUNT GROUP STAT,
01, Sat 00:00 - 01:00, HuntGp, 08, 08, 00002, 00002, 00000, 0002, 0003, 000004, 000005, 0000, 00001, 000003, 000003,
01, Sat 00:00 - 01:00, Agent, 5022, 00001, 000005, 000005, 00000, 000000, 000000, 00000, 000000, 000000, 00000, 000000, 000000,
01, Sat 00:00 - 01:00, Agent, 5012, 00001, 000004, 000004, 00001, 000003, 000003, 00001, 000005, 000005, 00001, 000003, 000003,
01, Sat 00:00 - 01:00, Queue, 00001, 00001, 00000, 00003, 00003, 00000, 00000, 00000, 00000, 00000, 
01, Sat 01:00 - 02:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 02:00 - 03:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 03:00 - 04:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 04:00 - 05:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Sat 05:00 - 06:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
.
.
.
08, Fri 19:00 - 20:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
08, Fri 20:00 - 21:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
08, Fri 21:00 - 22:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
08, Fri 22:00 - 23:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
08, Fri 23:00 - 00:00, HuntGp, 08, 08, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
```

### Related Commands

Command

Description

hunt-group report delay hours

Delays hunt group statistics collection for a specified
                                          						number of hours.

hunt-group report every hours

Sets the hourly interval at which Cisco Unified CME B-ACD
                                          						call statistics are automatically transferred to a file.

hunt-group report url

Sets filename parameters and the URL path where Cisco
                                          						Unified CME B-ACD call statistics are to be sent using TFTP.

show ephone-hunt

Displays ephone hunt group information.

show ephone-hunt statistics

Displays ephone hunt group statistics.

statistics collection

Enables the collection of call statistics for an ephone
                                          						hunt group.

statistics collection (voice hunt-group)

Enables the collection of call statistics for a voice hunt
                                          						group.

## huntstop (ephone-dn and ephone-dn-template)

To disable call hunting for directory numbers or channels, use the huntstop command in ephone-dn or
                              		  ephone-dn-template configuration mode. To reset to the default, use the no form of this command.

huntstop [ channel number-of-channels ]

no huntstop [ channel number-of-channels ]

### Syntax Description

channel

(Optional) For dual-line and octo-line directory numbers.
                                          						Prevents incoming calls from hunting to the next channel if the first channel
                                          						is busy or does not answer.

number-of-channels

Supported for octo-line directory numbers only. Number of
                                          						channels available to accept incoming calls. Remaining channels are reserved
                                          						for outgoing calls or features such as call transfer, call waiting, and
                                          						conferencing. Range: 1 to 8. Default: 8.

### Command Default

Ephone-dn huntstop is enabled. Channel huntstop is disabled for
                              		  dual-line directory numbers. Channel huntstop is set to 8 for octo-line
                              		  directory numbers.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced.

12.2(2)XT

Cisco ITS 2.0

This command was implemented on the Cisco 1750 and Cisco
                                          						1751.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(15)ZJ

Cisco CME 3.0

The channel keyword was introduced.

12.3(4)T

Cisco CME 3.0

This channel keyword was integrated into
                                          						Cisco IOS Release 12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was added to ephone-dn-template configuration
                                          						mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

12.4(15)XZ

Cisco Unified CME 4.3

The number-of-channels argument was
                                          						added for octo-lines.

12.4(20)T

Cisco Unified CME 7.0

This command with the number-of-channels argument for
                                          						octo-lines was integrated into Release 12.4(20)T.

### Usage Guidelines

Use this command without the channel keyword to disable call hunting for
                              		  ephone-dns. An incoming call does not roll over (hunt) to another ephone-dn if
                              		  the called number is busy or does not answer and a call hunt strategy has been
                              		  established that includes this ephone-dn. A huntstop prevents hunt-on-busy from
                              		  redirecting a call from a busy phone into a dial-peer with a catch-all default
                              		  destination. Use the no huntstop command to disable huntstop and allow
                              		  hunting for ephone-dns.

Channel huntstop works in a similar way, but it affects call hunting
                              		  behavior for the two channels of a dual-line ephone-dn. Use the channel keyword to prevent incoming calls
                              		  from hunting to the second channel of an ephone-dn if the first channel is busy
                              		  or does not answer. Incoming calls hunt forward to the next ephone-dn in the
                              		  hunt sequence instead of to the next channel on the same ephone-dn.

For example, an incoming call might search through the following
                              		  ephone-dns and channels:

ephone-dn 10 (channel 1) ephone-dn 10 (channel 2)

ephone-dn 11 (channel 1) ephone-dn 11 (channel 2) ephone-dn 12
                              		  (channel 1) ephone-dn 12 (channel 2)

If the huntstop channel command is not enabled (the default), a
                              		  call might ring for 30 seconds on ephone-dn 10 (channel 1) and then after 30
                              		  seconds move to ephone-dn 10 (channel 2), which is usually not the desired
                              		  behavior. It is useful to reserve the second channel of a dual-line ephone-dn
                              		  for call transfer, call waiting, or conferencing.

The number argument is required for an octo-line
                              		  directory number when using the channel keyword. This argument limits the
                              		  number of channels for incoming calls on an octo-line directory number and
                              		  reserves the other channels for outgoing calls or features such as call
                              		  transfer or conferencing. The router selects idle channels from the lowest
                              		  number to the highest. This argument is supported only for an octo-line
                              		  directory number.

In an ephone-dn template, you can apply separate huntstop channel commands for dual-line directory numbers
                              		  and octo-line directory numbers.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example shows huntstop is disabled for ephone-dn 1. The
                              		  huntstop attribute is set to OFF and allows calls to extension 5001 to hunt to
                              		  another directory number when directory number 1 is busy.

```
ephone-dn 1
 number 5001
 no huntstop
```

The following example shows a typical configuration in which enabling
                              		  huntstop (default) is required:

```
ephone-dn 1
 number 5001
 
ephone 4
 button 1:1
 mac-address 0030.94c3.8724
 
dial-peer voice 5000 voip
 destination-pattern 5...
 session target ipv4:192.168.17.225
```

In the previous example, the huntstop attribute for the dial peer is
                              		  set to ON by default and prevents calls to extension 5001 from being rerouted
                              		  to the on-net H.323 dial peer for 5... when extension 5001 is busy (the three
                              		  periods are used as wildcards).

The following example shows another configuration in which huntstop
                              		  is not desired and is explicitly disabled. In this example, ephone 4 is
                              		  configured with two lines, each with the same extension number 5001. This
                              		  allows the second line to provide call-waiting notification for extension
                              		  number 5001 when the first line is in use. Setting no huntstop on the first line (ephone-dn 1) allows
                              		  incoming calls to hunt to the second line (ephone-dn 2) when the first line is
                              		  busy.

Ephone-dn 2 has call forwarding set to extension 6000, which
                              		  corresponds to a locally attached answering machine connected to a foreign
                              		  exchange station (FXS) voice port. In this example, the plain old telephone
                              		  system (POTS) dial peer for extension 6000 also has the dial-peer huntstop
                              		  attribute explicitly set to prevent further hunting.

```
ephone-dn 1
 number 5001
 no huntstop
 preference 1
 call-forward noan 6000
 
ephone-dn 2
 number 5001
 preference 2
 call-forward busy 6000
 call-forward noan 6000
 
ephone 4
 button 1:1 2:2
 mac-address 0030.94c3.8724
 
dial-peer voice 6000 pots
 destination-pattern 6000
 huntstop
 port 1/0/0
 description answering-machine
```

The following example shows a dual-line configuration in which an
                              		  ephone-dn template is used to prevent calls from hunting to the second channel
                              		  of any ephone-dn. The calls hunt through the first channels for each ephone-dn
                              		  in the order 10, 11, 12.

```
ephone-dn-template 2
 huntstop channel
 
ephone-dn 10 dual-line
 number 1001
 no huntstop
 ephone-dn-template 2
 
ephone-dn 11 dual-line
 number 1001
 no huntstop
 ephone-dn-template 2
 preference 1
 
ephone-dn 12 dual-line
 number 1001
 no huntstop
 ephone-dn-template 2
 preference 2
```

The following example shows a configuration in which incoming calls
                              		  to octo-line directory number 7 are limited to four, freeing the other four
                              		  channels for outgoing calls or features such as call transfer or conferencing.

```
ephone-dn  7  octo-line
 number 2001
 name Smith, John
 huntstop channel 4
```

The following example shows an ephone-dn template configuration in
                              		  which the huntstop is set for both dual-line and octo-line directory numbers.

```
ephone-dn-template  1
 huntstop channel
 huntstop channel 4
```

### Related Commands

Command

Description

huntstop (dial-peer)

Disables further dial-peer hunting if a call fails using
                                          						hunt groups.

number

Associates a telephone or extension number with a directory
                                          						number (ephone-dn).

## huntstop (voice register dn)

To disable call hunting behavior for a directory number on a SIP
                              		  phone, use the huntstop command in voice register dn
                              		  configuration mode. To reset to the default, use the no form of this command.

huntstop [ channel number ]

no huntstop [ channel number ]

### Syntax Description

channel number

(Optional) Number of channels available to accept incoming
                                          						calls. Remaining channels are reserved for outgoing calls or features such as
                                          						call transfer, call waiting, and conferencing. Range: 1 to 50. Default: 0
                                          						(disabled).

### Command Default

Call hunting is enabled for the directory number. Channel huntstop is
                              		  disabled (0) for the directory number.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(22)YB

Cisco Unified CME 7.1

The channel keyword and number argument were added.

12.4(24)T

Cisco Unified CME 7.1

This command has been integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command disables call hunting behavior for a directory number on
                              		  a SIP IP phone so that an incoming call does not roll over (hunt) to another
                              		  directory number if the called directory number is busy or does not answer and
                              		  if a hunting strategy has been established that includes this directory number.
                              		  A huntstop allows you to prevent hunt-on-busy from redirecting a call from a
                              		  busy phone into a dial-peer setup with a catch-all default destination. Use the no huntstop command to disable huntstop and allow
                              		  hunting for directory numbers (default).

The channel keyword and number argument limits the number of channels
                              		  for incoming calls to a directory number and reserves the other channels for
                              		  outgoing calls or features such as call transfer or conferencing. The router
                              		  selects idle channels from the lowest number to the highest.

## Examples

The following example shows a typical configuration in which huntstop
                              		  is required. The huntstop command is enabled and prevents
                              		  calls to extension 5001 from being rerouted to the on-net H.323 dial peer for
                              		  5... when extension 5001 is busy (three periods are used as wild cards).

```
voice register dn 1
 number 5001
 huntstop
 
voice register pool 4
 button 1:1
 mac-address 0030.94c3.8724
 
dial-peer voice 5000 voip
 destination-pattern 5...
 session target ipv4:192.168.17.225
```

The following example shows a configuration in which huntstop is not
                              		  desired (default). In this example, directory number 4 is configured with two
                              		  lines, each with the same extension number 5001. This is done to allow the
                              		  second line to provide call-waiting notification for extension number 5001 when
                              		  the first line is in use. Not enabling huntstop on the first line (directory
                              		  number 1) allows incoming calls to hunt to the second line (directory number 2)
                              		  on phone 4 when the directory number 1 line is busy.

Directory number 2 has call forwarding set to extension 6000, which
                              		  corresponds to a locally attached answering machine connected to a foreign
                              		  exchange station (FXS) voice port. In this example, the plain old telephone
                              		  system (POTS) dial peer for extension 6000 has the dial-peer huntstop attribute
                              		  explicitly set to prevent further hunting.

```
voice register dn 1
 number 5001
 preference 1
 call-forward noan 6000
 
voice register dn 2
 number 5001
 preference 2
 call-forward busy 6000
 call-forward noan 6000
 
voice register pool 4
 button 1:1 2:2
 mac-address 0030.94c3.8724
 
dial-peer voice 6000 pots
 destination-pattern 6000
 huntstop
 port 1/0/0
 description answering-machine
```

The following example shows a configuration in which incoming calls
                              		  to directory number 23 are blocked if the total number of calls to extension
                              		  8123 exceeds 4. This frees the other channels for outgoing calls or features
                              		  such as call transfer or conferencing.

```
voice register dn  23
 number 8123
 shared-line max-calls 4
 huntstop channel 4
```

### Related Commands

Command

Description

huntstop (dial-peer)

Disables all further dial-peer hunting if a call fails on
                                          						the dial peer.

shared-line

Creates a directory number to be shared by multiple SIP
                                          						phones.

| line-number | Phone line that should be automatically answered. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| port port-number | (Optional) Specifies the port where the HFS download
                                          						service is enabled. Range is from 1024 to 65535. Note If the entered custom HFS port clashes with the
                                                   						underlying IP HTTP port, an error message is displayed and the command is
                                                   						disallowed. | Note | If the entered custom HFS port clashes with the
                                                   						underlying IP HTTP port, an error message is displayed and the command is
                                                   						disallowed. |
|---|---|---|---|
| Note | If the entered custom HFS port clashes with the
                                                   						underlying IP HTTP port, an error message is displayed and the command is
                                                   						disallowed. |

| Note | If the entered custom HFS port clashes with the
                                                   						underlying IP HTTP port, an error message is displayed and the command is
                                                   						disallowed. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(1)T | This command was introduced. |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profile files required for SIP
                                          						phones. |
| ip http port | Specifies the port where the HTTP service is run. |
| ip http server | Enables the underlying IOS HTTP server of the the HFS
                                          						infrastructure. |

| path | Directory path where only IP phone firmware and
                                          						configuration files are stored. Note The administrator must store the phone firmware files at
                                                   						the location set as the home path directory | Note | The administrator must store the phone firmware files at
                                                   						the location set as the home path directory |
|---|---|---|---|
| Note | The administrator must store the phone firmware files at
                                                   						the location set as the home path directory |

| Note | The administrator must store the phone firmware files at
                                                   						the location set as the home path directory |
|---|---|

| Release | Modification |
|---|---|
| 15.2(1)T | This command was introduced. |

| Command | Description |
|---|---|
| hfs enable | Enables the HFS download service on an IP Phone in a Cisco
                                          						Unified CME system. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.4(3)M5 | Cisco
                                          						Unified CME 10.5 | This
                                          						command was introduced. |

| timeout | Interval after which an audible alert notification is
                                       					 repeated, in seconds. Range is from 15 to 300. There is no default. |
|---|---|
| idle | Alerts only when the phone is idle. |
| originator | Alerts whether the phone is idle or busy. |
| shared | Alerts only when the extension is idle but alerts all phones
                                       					 that share the line. |
| shared-idle | Alerts all idle phones that share the line. |
| recurrence | Alerts recurrence after first timeout. |
| recurrence-timeout | Call on-hold recurrence timeout in seconds. Range is from 2
                                       					 to 300. |
| ring-silent-dn | Rings the silent DN. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. The shared-idle option and ring-silent-dn parameter were
                                          						introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |
| 15.1(3)T2 | Cisco Unified CME 8.5 | The recurrence parameter was introduced. |
| 15.1(4)M1 | Cisco Unified CME 8.6 | The recurrence parameter was introduced. |

| Command | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies ephone-dn-template to the ephone-dn being
                                          						configured. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |

| Note | This command
                                       		  does not apply to Cisco ATAs that have been configured for SIP in Cisco Unified
                                       		  CME. |
|---|---|

| Command | Description |
|---|---|
| call-waiting (voice register pool) | Enables
                                          						call waiting on a SIP phone. |
| mode (voice register global) | Enables
                                          						the mode for provisioning SIP phones in a Cisco CallManager Express (Cisco CME)
                                          						system. |

| number | Number of hops before the call proceeds to the final
                                          						ephone-dn. Range is from 2 to 20, but the value must be less than or equal to
                                          						the number of extensions that are specified in the list command. Default automatically
                                          						adjusts to the number of hunt group members. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The maximum number of hops was restricted to the number of
                                          						extensions specified in the list command. |
| 12.3(11)XL | Cisco CME 3.2.1 | Increased maximum number of hops to 20. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The default was changed from 2 hops to automatically adjust
                                          						the number of hops to the number of ephone hunt group members. |
| 12.4(9)T | Cisco Unified CME 4.0 | The modification to change the default was integrated into
                                          						Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| auto logout | Enables the automatic change of an ephone hunt group
                                          						agent's ephone-dn to not-ready status. |
| final | Defines the last ephone-dn in an ephone hunt group. |
| list | Defines the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco Unified CME system. |
| no-reg (ephone-hunt) | Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| pilot | Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list. |

| number | Number of hops before the call proceeds to the final
                                          						number. Range is 2 to 10, but the value must be less than or equal to the
                                          						number of extensions that are specified in the list command. The default is the
                                          						same number as there are destinations defined under the list command. |
|---|---|

| Cisco IOS Release | Cisco product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| list (voice hunt-group) | Defines the directory numbers that participate in a hunt
                                          						group. |
| timeout (voice hunt-group) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list and defines
                                          						the last directory number in the hunt group. |

| enable | Enables host-id-check option in a vpn-profile. |
|---|---|
| disable | Disables host-id-check option in a vpn-profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| prefix | Provides the prefix of the filename to which the statistics
                                       					 are written. The prefix of the filename appears at the end of the URL. |
|---|---|
| suffix | Provides the suffix of the filename to which the statistics
                                       					 are written. Range is <0-1> to <1-200>. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T . |

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file. |
| hunt-group report every hours | Sets the hourly interval after which Cisco CME B-ACD call
                                          						statistics are automatically transferred to a file. |

| location | URL or
                                          						filename to which the statistics is written. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.3(2)T | Cisco
                                          						Unified CME 9.5 | This
                                          						command was introduced. |
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was enhanced to add statistics for total logged in and logged out time
                                          						for voice hunt group. |

| Note | On the day
                                       		  that daylight saving time adjusts the time back by one hour at 2 a.m. each
                                       		  year, the original 1 a.m. to 2 a.m. statistics for that day are lost because
                                       		  they are overwritten by the new 1 a.m. to 2 a.m. statistics. |
|---|---|

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays hunt group statistics collection for a specified number of hours. |
| hunt-group report every hours | Sets
                                          						the hourly interval at which Cisco Unified CME B-ACD call statistics are
                                          						automatically transferred to a file. |
| hunt-group report url | Sets
                                          						filename parameters and the URL path where Cisco Unified CME B-ACD call
                                          						statistics are to be sent using TFTP. |
| hunt-group statistics write-all | Writes all ephone and voice hunt group statistics to a
                                          						fille. |
| show voice hunt-group statistics | Displays voice hunt group statistics. |
| show ephone-hunt statistics | Displays ephone hunt group statistics. |

| DND | Agent phones do not answer the number of calls specified in
                                          						the auto logout command and are automatically
                                          						placed in both DND status and not-ready status. The HLog soft key is not
                                          						displayed on phones. |
|---|---|
| HLog | Agent phones do not answer the number of calls specified in
                                          						the auto logout command and are automatically
                                          						placed only in not-ready status. The HLog soft key is displayed on phones in
                                          						addition to the DND soft key. |
| notify | Enables logout call in queue notification on HLog PLK
                                          						button. |
| threshold number | Defines the boundary value by which how the Hlog PLK
                                          						indicates the number of calls in queue on the logout agent’s phone. Range is 1
                                          						to 65535. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 15.2(2)T2 | Cisco Unified CME 9.1 | The notify and threshold keywords were added. |

| Note | When an agent who is a dynamic member of a hunt group is in
                                       		  not-ready status, the agent’s slot in the ephone hunt group is not
                                       		  relinquished. It remains reserved by the agent until the agent leaves the
                                       		  group. |
|---|---|

| Command | Description |
|---|---|
| auto logout | Enables the automatic change of an agent’s ephone-dn to
                                          						not-ready status after a specified number of hunt-group calls are not answered. |
| feature-button index < feature identifier >
                                          						[ label label ] | Enables the feature button configuration on a line key. |

| number | Number
                                          						of hours by which the collection of statistics can be extended for the
                                          						statistics collection periods configured with the hunt-group report every hours command. The range is from 1 to 10. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 | This
                                          						command was introduced. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | This
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |

| Command | Description |
|---|---|
| hunt-group report every hours | Sets
                                          						the hourly interval after which Cisco CME B-ACD call statistics are
                                          						automatically transferred to a file. |
| hunt-group report url | Sets
                                          						filename parameters and the URL path where Cisco CME B-ACD call statistics are
                                          						to be sent using TFTP. |
| statistics collect | Enables the collection of Cisco CME B-ACD call data for an ephone hunt group. |

| number | Number of hours after which auto-attendant (AA) call
                                          						statistics are collected and reported. The range is from 1 to 84. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file. |
| hunt-group report url | Sets filename parameters and the URL path where Cisco CME
                                          						B-ACD call statistics are to be sent using TFTP. |
| statistics collect | Enables the collection of Cisco CME B-ACD call statistics
                                          						for an ephone hunt group. |

| location | URL or filename to which the statistics should be written. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 15.2(2)T | Cisco Unified CME 9.0 | This command was introduced to replace the ephone-hunt statistics write-all command. |

| Note | On the day that daylight saving time adjusts the time back by one
                                       		  hour at 2 a.m. each year, the original 1 a.m. to 2 a.m. statistics for that day
                                       		  are lost because they are overwritten by the new 1 a.m. to 2 a.m. statistics. |
|---|---|

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays hunt group statistics collection for a specified
                                          						number of hours. |
| hunt-group report every hours | Sets the hourly interval at which Cisco Unified CME B-ACD
                                          						call statistics are automatically transferred to a file. |
| hunt-group report url | Sets filename parameters and the URL path where Cisco
                                          						Unified CME B-ACD call statistics are to be sent using TFTP. |
| show ephone-hunt | Displays ephone hunt group information. |
| show ephone-hunt statistics | Displays ephone hunt group statistics. |
| statistics collection | Enables the collection of call statistics for an ephone
                                          						hunt group. |
| statistics collection (voice hunt-group) | Enables the collection of call statistics for a voice hunt
                                          						group. |

| channel | (Optional) For dual-line and octo-line directory numbers.
                                          						Prevents incoming calls from hunting to the next channel if the first channel
                                          						is busy or does not answer. |
|---|---|
| number-of-channels | Supported for octo-line directory numbers only. Number of
                                          						channels available to accept incoming calls. Remaining channels are reserved
                                          						for outgoing calls or features such as call transfer, call waiting, and
                                          						conferencing. Range: 1 to 8. Default: 8. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(2)XT | Cisco ITS 2.0 | This command was implemented on the Cisco 1750 and Cisco
                                          						1751. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The channel keyword was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This channel keyword was integrated into
                                          						Cisco IOS Release 12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was added to ephone-dn-template configuration
                                          						mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The number-of-channels argument was
                                          						added for octo-lines. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command with the number-of-channels argument for
                                          						octo-lines was integrated into Release 12.4(20)T. |

| Command | Description |
|---|---|
| huntstop (dial-peer) | Disables further dial-peer hunting if a call fails using
                                          						hunt groups. |
| number | Associates a telephone or extension number with a directory
                                          						number (ephone-dn). |

| channel number | (Optional) Number of channels available to accept incoming
                                          						calls. Remaining channels are reserved for outgoing calls or features such as
                                          						call transfer, call waiting, and conferencing. Range: 1 to 50. Default: 0
                                          						(disabled). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The channel keyword and number argument were added. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command has been integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| huntstop (dial-peer) | Disables all further dial-peer hunting if a call fails on
                                          						the dial peer. |
| shared-line | Creates a directory number to be shared by multiple SIP
                                          						phones. |