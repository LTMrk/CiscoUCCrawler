---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010001-html-b191aa6698
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010001.html
retrieved_at: 2026-08-21T20:40:31.789588+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 24, 2018

Chapter: Cisco Unified CME Commands: S2

## Chapter: Cisco Unified CME Commands: S2

# Cisco Unified CME Commands: S2

## shared-line

To create a directory number to be shared by multiple SIP phones, use
                              		  the shared-line command in voice register dn
                              		  configuration mode. To return to the default, use the no form of this command.

shared-line [ max-calls number-of-calls ]

no shared-line

### Syntax Description

max-calls number-of-calls

(Optional) Maximum number of active calls allowed on the
                                          						shared line. Range: 2 to 16. Default: 2.

### Command Default

Directory number is not a shared line. Maximum number of calls on a
                              		  shared line is 2.

### Command Modes

Voice register dn configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command enables a shared line on an individual SIP phone
                              		  directory number.

This command is supported only on the Cisco Unified IP Phone 7911G,
                              		  7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE.

## Examples

The following example shows that extension 5001 associated with
                              		  directory number 2 is defined as a shared line and can support up to four
                              		  calls:

```
Router(config)# voice register dn 2 Router(config-register-dn)# number 5001 Router(config-register-dn)# shared-line max-calls 4
```

### Related Commands

Command

Description

busy-trigger-per-button

Sets the maximum number of calls allowed on a SIP shared
                                          						line before activating Call Forward Busy or a busy tone.

debug shared-line

Displays debugging information about shared lines on SIP
                                          						phones.

huntstop

Disables call hunting behavior for a directory number on a
                                          						SIP phone.

number (voice register din)

Associates a telephone or extension number with a SIP
                                          						phone.

show shared-line

Displays information about shared lines on SIP phones.

show voice register dn

Displays all configuration information associated with a
                                          						specific voice register dn.

## shared-line sip

To add an ephone-dn as a member of a shared directory number in the
                              		  database of the Shared-Line Service Module for a mixed shared line between
                              		  Cisco Unified SIP and Cisco Unified SCCP IP phones, use the shared-line sip command in ephone-dn configuration mode. To
                              		  return to the default, use the no form of this command.

shared-line sip [ max calls number-of-calls ]

no shared-line sip

### Syntax Description

max calls number-of calls

(Optional) Maximum number of active calls allowed on the
                                          						shared line. Range: 2 to 16. Default: 2.

### Command Default

Directory number is not a mixed shared line.

Maximum number of calls on a mixed shared line is 2.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the shared-line sip command to add an ephone-dn as a member of a
                              		  shared directory number in the database of the Shared-Line Service Module for a
                              		  mixed shared line between Cisco Unified SIP IP phones and Cisco Unified SCCP IP
                              		  phones. However, a mixed shared line is not enabled when an ephone-dn nnnn is the only shared directory number nnnn in the database of the Shared-Line Service Module. It is
                              		  only enabled when a corresponding Cisco Unified SIP IP phone with a shared
                              		  directory number nnnn is subscribed.

Mixed shared lines can only be configured on one of several common
                              		  directory numbers. All attempts to add more are rejected.

Features are effectively supported on a mixed shared line when
                              		  dial-plan patterns have matching configurations in telephony-service and voice
                              		  register global configuration modes using the dialplan pattern command.

## Examples

The following example shows 1001 as the shared line between a Cisco
                              		  Unified SCCP IP phone and a Cisco Unified SIP IP phone. The maximum number of
                              		  active calls allowed on the mixed shared line is four.

```
voice register dn 1
 number 1001
 shared-line max-calls 4
ephone-dn 1 octo-line
 number 1001
 shared-line sip
```

The following example shows how configuring a mixed shared line on a
                              		  second common directory number is rejected:

```
Router(config)# ephone-dn 14 octo-line Router(config-ephone-dn)# number 2502 Router(config-ephone-dn)# shared-line sip Router(config)# ephone-dn 20 octo-line Router(config-ephone-dn)# number 2502 Router(config-ephone-dn)# shared-line sip DN number already exists in the shared line database
```

### Related Commands

Command

Description

dialplan pattern

Defines a pattern that is used to expand extension numbers
                                          						in Cisco Unified CME into fully qualified E.164 numbers, in telephony-service
                                          						configuration mode.

dialplan pattern (voice register)

Defines a pattern that is used to expand extension numbers
                                          						in Cisco Unified CME into fully qualified E.164 numbers, in voice register
                                          						global configuration mode.

shared-line

Creates a directory number to be shared by multiple Cisco
                                          						Unified SIP IP phones.

## show
                        	 capf-server

To display CAPF
                              		  server configuration and session information, use the show capf-server command in privileged EXEC
                              		  configuration mode.

show capf-server { auth-string | sessions | summary }

### Syntax Description

auth-string

Display
                                          						authentication strings for ephones.

sessions

Display
                                          						information about active CAPF sessions.

summary

Display
                                          						CAPF server configuration details.

### Command Modes

Privileged EXEC

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

### Usage Guidelines

This command is
                              		  used with Cisco Unified CME phone authentication.

## Examples

The following
                              		  example output displays CAPF server parameters:

```
Router# show capf-server summary CAPF Server Configuration Details
        Trustpoint for TLS With Phone: cmeserver
        Trustpoint for CA operation: iosra
        Source Address: 10.1.1.1
        Listening Port: 3804
        Phone Key Size: 1024
        Phone KeyGen Retries: 100
        Phone KeyGen Timeout: 120 minutes
        Device Authentication Mode: Auth-String
```

The following
                              		  example output displays the authentication strings that have been defined for
                              		  the phones with the listed MAC addresses:

```
Router# show capf-server auth-string Authentication Strings for configured Ephones
Mac-Addr        Auth-String
--------        -----------
000CCE3A817C    7012
001121116BDD    922
000D299D50DF    9182
000ED7B10DAC    3114
000F90485077    3328
0013C352E7F1    0678
```

The following
                              		  example output displays active sessions between phones (identified by their MAC
                              		  addresses) and the CAPF server. The phone ID field lists standard phone
                              		  identifications, which include the letters “SEP” plus the MAC addresses of the
                              		  phones. The below sample output defines the different session states that can
                              		  appear in the output.

```
Router# show capf-server sessions Active CAPF Sessions
Phone ID                State
SEP000CCE3A817C         AWAIT-KEYGEN-RES
```

State

Description

IDLE

Phone is
                                          					 idle.

AWAIT
                                          					 AUTH RES

A TLS
                                          					 connection was established on the TCP port that is specified in the
                                          					 configuration file. After a successful handshake verified the server
                                          					 certificate, a dialog was started between the CAPF server and the phone’s CAPF
                                          					 client. The server has challenged the phone by sending an authentication
                                          					 request and is waiting for a response.

AWAIT
                                          					 KEYGEN RESP

Phone
                                          					 authentication was successful. The CAPF server has sent a key generation
                                          					 request message to the phone and is waiting for a response.

AWAIT
                                          					 ENCRYPT MSG RESP

A key has
                                          					 been generated and the CAPF has used the phone’s public key to start the
                                          					 enrollment process with PKI. The CAPF sent an encrypt-message request to the
                                          					 phone and is waiting for a response.

AWAIT CA
                                          					 RESP

The
                                          					 phone has signed the received message using its private key and the CAPF has
                                          					 continued the enrollment process. PKI has forwarded the certificate request to
                                          					 the CA and is waiting for a response.

AWAIT
                                          					 STORE CERT RESP

Upon
                                          					 receiving an certificate issued from the CA, the CAPF has sent a
                                          					 store-certificate request message to the phone. The store-certificate request
                                          					 contains the certificate to be written to the phone’s flash memory. The CAPF is
                                          					 waiting for a store-certificate response message to confirm that the
                                          					 certificate has been stored.

## show
                        	 credentials

To display the
                              		  credentials settings that have been configured for use during Cisco Unified CME
                              		  phone authentication communications or secure Cisco Unified SRST fallback, use
                              		  the show credentials command in privileged EXEC mode.

show credentials

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(14)T

Cisco
                                          						SRST 3.3

This
                                          						command was introduced for Cisco SRST.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was introduced for Cisco Unified CME.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command for Cisco Unified CME was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Cisco Unified CME

This command
                              		  displays the credentials settings on a Cisco Unified CME router that has been
                              		  configured with a CTL provider to be used with Cisco Unified CME phone
                              		  authentication.

Cisco Unified SRST

This command
                              		  displays the credentials settings on the Cisco Unified SRST router that are
                              		  supplied to Cisco Unified CallManager for use during secure SRST fallback.

## Examples

The following is
                              		  sample output from the show credentials :

```
Router# show credentials Credentials IP: 10.1.1.22
Credentials PORT: 2445
Trustpoint: srstca
```

The below table
                              		  describes the fields in the sample output.

Field

Description

Credentials IP

Cisco
                                          					 Unified CME—IP address where the CTL provider is configured.

Cisco
                                          					 Unified SRST—The specified IP address where certificates from Cisco Unified
                                          					 CallManager to the SRST router are received.

Credentials PORT

Cisco
                                          					 Unified CME—TCP port for credentials service communication. Default is 2444.

Cisco
                                          					 Unified SRST—The port to which the SRST router connects to receive messages
                                          					 from the Cisco Unified IP phones. The port number is from 2000 to 9999. The
                                          					 default port number is 2445.

Trustpoint

Cisco
                                          					 Unified CME—CTL provider trustpoint label that will be used for TLS sessions
                                          					 with the CTL client.

Cisco
                                          					 Unified SRST—The name of the trustpoint that is associated with the credentials
                                          					 service between the Cisco Unified CallManager client and the SRST router.

### Related Commands

Description

credentials

Enters
                                          						credentials configuration mode to configure a Cisco Unified CME CTL provider
                                          						certificate or a Cisco Unified SRST router certificate.

ctl-service admin

Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol.

debug credentials

Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider and the CTL client or between a Cisco Unified SRST router and Cisco
                                          						Unified CallManager.

ip source-address (credentials)

Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with a Cisco Unified SRST router certificate.

## show cti

To display the status of the CTI subsystem, use the show cti command in privileged EXEC mode.

show cti { call | gcid | line node | session }

### Syntax Description

call

Details for active (ACT) calls only.

gcid

List of Global Call IDs for active calls only.

line node

List of line nodes.

session

Details for active CTI sessions.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

This commands displays status information for the CTI subsystem in
                              		  Cisco Unified CME.

## Examples

The following sample output is for each command when there are no
                              		  active calls.

```
Router# show cti gcid GCID                                 callIDs
===================================  =================
no active GCID
Router# show cti call DN         CallID GCID                                Calling    Called     State
=========  ====== =================================== ========== ========== =====
201       
204       
A line-node is the internal data structure of a directory number. Once a line-node is created, the structure remains until the CTI interface is shut down.
Router# show cti line-node line dn             number of call instance
================    =======================
1001                0
201                 0
202                 0
203                 0
204                 0
233                 0
6789                0
A0001               0
Router#
```

The following is sample output from the show cti gcid command for one call. This sample contains a single Gcid with
                              		  two callIDs, one for each call leg.

```
Router# show cti gcid GCID                                 callIDs
===================================  =================
1E2E3483-5ACB11DE-BA9EF925-DF2AFB55  59291, 59292,
```

The following is sample output from the show cti call command. This samples shows that a call was placed from (DN)
                              		  201 to (DN) 204 and both directory numbers are now Active (ACT). Note that the
                              		  Gcid and callIDs in this sample correspond to those in the output from the show cti gcid command.

```
Router# show cti call DN         CallID GCID                                Calling    Called     State
=========  ====== =================================== ========== ========== ======
201
           59291   1E2E3483-5ACB11DE-BA9EF925-DF2AFB55 201        204        ACT
204
           59292   1E2E3483-5ACB11DE-BA9EF925-DF2AFB55 201        204        ACT
```

The following is sample output from the show cti line-node command. In the following sample, there are eight line-nodes
                              		  and two (201 and 204) are in use.

```
Router# show cti line-node line dn             number of call instance
================    =======================
                    0
1001                0
201                 1
      callID 59291(C7C ),  *cg = 201, cd = 204
202                 0
203                 0
204                 1
      callID 59292(C7C ),  cg = 201, *cd = 204
233                 0
6789                0
A0001               0
```

<< Table number >> describes the significant fields shown
                              		  in the display.

Field

Description

GCID

Global Call ID (Gcid)—Unique identifier in for every call on
                                          					 an outbound leg of a VoIP dial peer for an endpoint. A single Gcid remains the
                                          					 same for the same call in the system, and is valid for redirect, transfer, and
                                          					 conference events.

CallID

Unique identifier for each call leg of a call.

### Related Commands

Command

Description

clear cti session

Clears the session between a CSTA client application and
                                          						Cisco Unified CME.

## show ctl-client

To display information about the certificate trust list (CTL) client,
                              		  use the show ctl-client command in privileged EXEC
                              		  configuration mode.

show ctl-client

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example displays trustpoints and IP addresses known to
                              		  the CTL client.

```
Router# show ctl-client CTL Client Information
-----------------------------
        SAST 1 Certificate Trustpoint: cmeserver
        SAST 1 Certificate Trustpoint: sast2
        List of Trusted Servers in the CTL
                CME     10.1.1.1        cmeserver
                TFTP    10.1.1.1        cmeserver
                CAPF    10.1.1.1        cmeserver
```

## show
                        	 ephone

To display
                              		  information about registered Cisco Unified IP phones, use the show ephone command in user EXEC or privileged EXEC
                              		  mode.

show ephone [ mac-address | phone-type ]

### Syntax Description

mac-address

(Optional) Displays information for the phone with the specified MAC address.

phone-type

(Optional) Displays information for phones of the specified phone type.
                                          						Supported phone types are version-specific. Type ? to display
                                          						a list of values.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						ITS 1.0 Cisco SRST 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						ITS 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

12.2(11)T

Cisco
                                          						ITS 2.01 Cisco SRST 2.01

The ata keyword
                                          						was added and this command was implemented on the Cisco 1760.

12.2(11)YT

Cisco
                                          						ITS 2.1 Cisco SRST 2.1

The 7914 keyword
                                          						was added.

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

The 7902 , 7905 , and 7912 keywords
                                          						were added.

12.3(7)T

Cisco
                                          						CME 3.1 Cisco SRST 3.1

The 7920 and 7936 keywords
                                          						were added.

12.3(11)XL

Cisco
                                          						CME 3.2.1 Cisco SRST 3.2.1

The 7970 keyword
                                          						was added.

12.3(14)T

Cisco
                                          						CME 3.3 Cisco SRST 3.3

The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T.

## Command History

12.4(4)XC

Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added.

12.4(9)T

Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were integrated into Cisco IOS Release 12.4(9)T.

12.4(6)XE

Cisco
                                          						Unified CME 4.0(2)

The 7931 keyword was added for Cisco Unified CME.

12.4(4)XC4

Cisco
                                          						Unified CME 4.0(3)

The 7931 keyword was added for Cisco Unified CME.

12.4(11)T

Cisco
                                          						Unified CME 4.0(3)

The 7931 keyword for Cisco Unified CME was integrated into Cisco IOS Release 12.4(11)T.

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1 Cisco Unified SRST 4.1

The 7921 and 7985 keywords were added.

12.4(15)T1

Cisco
                                          						Unified CME 4.1(1) Cisco Unified SRST 4.1(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were added and this command was integrated into Cisco IOS Release
                                          						12.4(15)T1.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1) Cisco Unified SRST 4.2(1)

Emergency response location (ERL) information displays in the output.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3

Support for user-defined phone types created with the ephone-type command was added.

12.4(15)XZ1

Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3

The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added.

12.4(20)T

Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0

The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added and this command was integrated into Cisco IOS Release
                                          						12.4(20)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The IP-STE keyword was added and logical partitioning
                                          						class of restriction (LPCOR) and Cancel Call Waiting information was added to
                                          						the output.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

## Examples

Significant
                              		  fields in the output from this command are described in the table.

The following
                              		  sample output shows general information for registered phones:

```
Router# show ephone ephone-8[7] Mac:000A.B7B1.444A TCP socket:[5] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 11/9 max_streams=1
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:8 privacy:0
IP:10.4.188.99 * 50007 Telecaster 7940  keepalive 8424 max_line 2 available_line 2
button 1: cw:1 ccw:(0 0) 
  dn 6  number 6006 CH1   IDLE         CH2   IDLE         overlay shared 
button 2: cw:1 ccw:(0 0 0 0 0 0 0 0) 
  dn 42 number 6042 CH1   IDLE         CH2   IDLE         CH3   IDLE         CH4   IDLE         CH5   IDLE         CH6   IDLE         CH7   IDLE         CH8   IDLE         shared 
overlay 1: 6(6006) 7(6007) 8(6008) 
Preferred Codec: g711ulaw 
Lpcor Type: local Incoming: ephone_group1 Outgoing: ephone_group1
```

The table
                              		  describes significant fields in the output.

Field

Description

Active
                                          					 Call

An
                                          					 active call is in progress.

activeLine

Line
                                          					 (button) on the phone that is in use. Zero indicates that no line is in use.

auto-dial number

Intercom extension that automatically dials number .

button number : dn number

Phone
                                          					 button number and the extension (ephone-dn) dn-tag number associated with that
                                          					 button.

bytes

Total
                                          					 number of voice data bytes sent or received by the phone.

Called
                                          					 Dn, Calling Dn

Ephone-dn tag numbers of the called and calling ephone-dn. Set to -1 if the
                                          					 call is not to or from an ephone-dn, or if there is no active call.

cfa number

Call-forward-all to number is
                                          					 enabled for this extension.

CH1 CH2

Status
                                          					 of channel 1 and, if this is a dual-line ephone-dn, the status of channel 2.

cw

1
                                          					 indicates that Call Waiting is enabled. 0 indicates that Call Waiting is
                                          					 disabled.

debug

1
                                          					 indicates that debug for the phone is enabled. 0 indicates that debug is
                                          					 disabled.

DnD

Do Not
                                          					 Disturb is set on this phone.

DP tag

Not
                                          					 used.

ephone- number

Unique
                                          					 sequence number used to identify this phone during configuration (phone-tag).

IP

Assigned IP address of the Cisco Unified IP phone.

Jitter

Amount
                                          					 of variation (in milliseconds) of the time interval between voice packets
                                          					 received by the Cisco Unified IP phone.

keepalive

Number
                                          					 of keepalive messages received from the Cisco Unified IP phone by the router.

Latency

Estimated playout delay for voice packets received by the Cisco Unified IP
                                          					 phone.

line number

Button
                                          					 number on an IP phone. Line 1 is the button nearest the top of the phone.

Lost

Number
                                          					 of voice packets lost, as calculated by the Cisco Unified IP phone, on the
                                          					 basis of examining voice packet time-stamp and sequence numbers during playout.

Lpcor
                                          					 Incoming

Setting
                                          					 of the lpcor incoming command.

Lpcor
                                          					 Outgoing

Setting
                                          					 of the lpcor outgoing command.

Lpcor
                                          					 Type

Setting
                                          					 of the lpcor type command.

Mac

MAC
                                          					 address.

Max
                                          					 Conferences

Maximum
                                          					 number of allowable conference calls and number of active conference calls.

max_line number

Maximum
                                          					 number of line buttons that can be configured on this phone.

mediaActive

1
                                          					 indicates that an active conversation is in progress. 0 indicates that no
                                          					 conversation is ongoing.

monitor-ring

This
                                          					 button is set up as a monitor button.

number

Telephone or extension number associated with the Cisco Unified IP phone button
                                          					 and its dn-tag.

offhook

1
                                          					 indicates that the phone is off-hook. 0 indicates that the phone is on-hook.

overlay

This
                                          					 button contains an overlay set. Use show ephone overlay to display the contents of overlay sets.

paging

1
                                          					 indicates that the phone has received an audio page. 0 indicates that the phone
                                          					 has not received an audio page.

paging-dn

Ephone-dn that is dedicated for receiving audio pages on this phone. The
                                          					 paging-dn number is the number of the paging set to which this phone belongs.

Password

Authentication string that the phone user types when logging in to the
                                          					 web-based Cisco Unified CME GUI.

Port

Port
                                          					 used for TAPI transmissions.

REGISTERED

The
                                          					 Cisco Unified IP phone is active and registered. Alternative states are
                                          					 UNREGISTERED (indicating that the connection to the Cisco Unified IP phone was
                                          					 closed in a normal manner) and DECEASED (indicating that the connection to the
                                          					 Cisco Unified IP phone was closed because of a keepalive timeout).

reset

Pending
                                          					 reset.

reset_sent

Request
                                          					 for reset has been sent to the Cisco Unified IP phone.

ringing

1
                                          					 indicates that the phone is ringing. 0 indicates that the phone is not ringing.

Rx Pkts

Number
                                          					 of received voice packets.

silent-ring

Silent
                                          					 ring has been set on this button and extension.

socket

TCP
                                          					 socket number used to connect to IP phone.

speed
                                          					 dial speed-tag:digit-string label-text

This
                                          					 button is a speed-dial button, assigned to the speed-dial sequence number speed-tag .
                                          					 It dials digit-string and displays the text label-text next to the button.

sub=3,
                                          					 sub=4

Subtype
                                          					 3 means that one Cisco Unified IP Phone 7914 Expansion Module is attached to
                                          					 the main Cisco Unified IP Phones 7960 and 7960G, and subtype 4 means that two
                                          					 are attached.

Tag number

Dn-tag
                                          					 number, the unique sequence number that identifies an ephone-dn during
                                          					 configuration, followed by the type of ephone-dn it is.

TAPI
                                          					 Client IP Address

IP
                                          					 address of the PC running the TAPI client.

TCP
                                          					 socket

TCP
                                          					 socket number used to communicate with the Cisco Unified IP phone. This can be
                                          					 correlated with the output of other debug and show commands.

Telecaster model-number

Type
                                          					 and model of the Cisco Unified IP phone. This information is received from the
                                          					 phone during its registration with the router.

Tx Pkts

Number
                                          					 of transmitted voice packets.

Username

Username that the phone user types when logging in to the web-based Cisco
                                          					 Unified CME GUI.

### Related Commands

Command

Description

show ephone-dn

Displays information about Cisco Unified IP phone extensions (ephone-dns).

show ephone login

Displays the login states of all local ephones.

show telephony-service all

Displays systemwide status and information for a Cisco Unified CME system.

## show ephone
                        	 attempted-registrations

To display the
                              		  log of ephones that unsuccessfully attempt to register with Cisco Unified CME,
                              		  use the show ephone attempted-registrations command in privileged EXEC mode.

show ephone attempted-registrations

### Syntax Description

This command has
                              		  no keywords or arguments.

### Command Modes

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

### Usage Guidelines

The no auto-reg-ephone blocks the automatic registration
                              		  of ephones whose MAC addresses are not explicitly listed in the configuration.
                              		  When automatic registration is blocked, Cisco Unified CME records the MAC
                              		  addresses of phones that attempt to register but cannot because they are
                              		  blocked.

Use the show ephone attempted-registrations to view the list of phones that have attempted to register but
                              		  have been blocked. The clear telephony-service ephone-attempted-registrations clears the list.

## Examples

The following
                              		  example displays ephones that unsuccessfully attempted to register with Cisco
                              		  Unified CME:

```
Router# show ephone attempted-registrations Attempting Mac address:
Num    Mac Address         DateTime                          DeviceType
-----------------------------------------------------------------------------
1      C863.8475.5417      22:52:05 UTC Thu Apr 28 2005      SCCP Gateway (AN) 
2      C863.8475.5408      22:52:05 UTC Thu Apr 28 2005      SCCP Gateway (AN) 
.....
25     000D.28D7.7222      22:26:32 UTC Thu Apr 28 2005      Telecaster 7960 
26     000D.BDB7.A9EA      22:25:59 UTC Thu Apr 28 2005      Telecaster 7960 
...
47     C863.94A8.D40F      22:52:17 UTC Thu Apr 28 2005      SCCP Gateway (AN) 
48     C863.94A8.D411      22:52:18 UTC Thu Apr 28 2005      SCCP Gateway (AN) 
49     C863.94A8.D400      22:52:15 UTC Thu Apr 28 2005      SCCP Gateway (AN)
```

The below table
                              		  describes the significant fields shown in the display.

Field

Description

Num

Index
                                          					 number.

Mac
                                          					 Address

MAC
                                          					 address of the ephone.

DateTime

Date and
                                          					 time that the attempt to register was made.

DeviceType

Type of
                                          					 ephone.

### Related Commands

Command

Description

auto-reg-ephone

Enables
                                          						automatic registration of ephones with the Cisco Unified CME system.

clear telephony-service ephone-attempted-registrations

Empties the log of ephones that unsuccessfully attempt to register with Cisco
                                          						Unified CME.

## show ephone cfa

To display status and information on the registered phones that have
                              		  call-forward-all set on one or more of their extensions (ephone-dns), use the show ephone cfa command in privileged EXEC mode.

show ephone cfa

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone cfa command:

```
Router# show ephone cfa ephone-1 Mac:0007.0EA6.353A TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:1.2.205.205 52491 Telecaster 7960  keepalive 14 max_line 6
button 1: dn 11 number 60011 cfa 60022 CH1 IDLE 
button 2: dn 17 number 60017 cfa 60021 CH1 IDLE
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone dn

To display phone information for specified dn-tag or for all dn-tags,
                              		  use the show ephone dn command in privileged EXEC mode.

show ephone dn [dn-tag]

### Syntax Description

dn-tag

(Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to identify the phone on which a particular dn-tag
                              		  has been assigned.

## Examples

The following is sample output for the two appearances of DN 5:

```
Router# show ephone dn 5 Tag 5, Normal or Intercom dn 
ephone 1, mac-address 0030.94C3.CAA2, line 2
ephone 2, mac-address 0030.94c2.9919, line 3
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone dnd

To display information on the registered phones that have “do not
                              		  disturb” set on one or more of their extensions (ephone-dns), use the show ephone dnd command in privileged EXEC mode.

show ephone dnd

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command does not apply to Cisco Unified SRST.

## Examples

The following is sample output from the show ephone dnd command:

```
Router# show ephone dnd ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:1.2.205.205 52486 Telecaster 7960  keepalive 2729 max_line 6 DnD
button 1: dn 11 number 60011 CH1 IDLE
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 login

To display the
                              		  login states of all local IP phones, use the show ephone login command in privileged EXEC mode.

show ephone login

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0

This
                                          						command was modified. LOCAL and GLOBAL replace TRUE in the output for “Pin
                                          						enabled.”

15.1(1)T

Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

The show ephone login command displays whether an ephone has a
                              		  personal identification number (PIN) and whether its owner is logged in.

In Cisco Unified
                              		  CME 7.1 and earlier versions, FALSE is displayed if there is no PIN configured
                              		  for the specified ephone. TRUE is displayed if there is a PIN configured for
                              		  the specified ephone.

In Cisco Unified
                              		  CME 8.0 and later versions, the show output is modified as follows:

- FALSE is
                                 			 displayed only if no PIN is defined, neither in an ephone configuration nor in
                                 			 the telephony-service configuration.

- LOCAL is
                                 			 displayed if an individual PIN is defined for the specific ephone.

- GLOBAL is
                                 			 displayed if a global PIN is defined.

## Examples

The following is
                              		  sample output from the show ephone login command. It shows that a PIN is defined for
                              		  ephone 1 and that its owner has not logged in. The other phones do not have
                              		  PINs associated with them.

```
Router# show ephone login ephone 1        Pin enabled:LOCAL       Logged-in:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE
```

The following is
                              		  sample output from the show ephone login command. It shows that a PIN is defined for
                              		  ephone 1 and that its owner has not logged in. A global PIN is defined also
                              		  defined for this system. If the pin command
                              		  is configured in ephone configuration mode and telephony-service configuration
                              		  mode, the command in ephone configuration mode takes precedence.

```
Router# show ephone login ephone 1        Pin enabled:LOCAL       Logged-in:FALSE
ephone 2        Pin enabled:GLOBAL      Logged-in:TRUE
ephone 3        Pin enabled:GLOBAL      Logged-in:TRUE
```

The following is
                              		  sample output from the show ephone login command. It shows that neither a local nor a
                              		  global PIN is enabled for ephones 1 to 3.

```
Router# show ephone login ephone 1        Pin enabled:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE
```

## Examples

The following is
                              		  sample output from the show ephone login command. It shows that a PIN is enabled for
                              		  ephone 1 and that its owner has not logged in. The other phones do not have
                              		  PINs associated with them.

```
Router# show ephone login ephone 1        Pin enabled:TRUE        Logged-in:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE
ephone 4        Pin enabled:FALSE
ephone 5        Pin enabled:FALSE
ephone 6        Pin enabled:FALSE
ephone 7        Pin enabled:FALSE
ephone 8        Pin enabled:FALSE
ephone 9        Pin enabled:FALSE
```

The below table
                              		  describes significant fields in this output.

Field

Description

ephone phone-tag

Phone
                                          					 identified with its unique phone-tag sequence number.

Pin
                                          					 enabled

In
                                          					 Cisco Unified CME 7.1 and earlier versions:

- TRUE—A PIN is defined for this phone.

- FALSE —No PIN is defined for this phone.

In
                                          					 Cisco Unified CME 8.0 and later versions:

- LOCAL—A PIN has been defined for this phone.

- GLOBAL—A global PIN is defined for this Cisco Unified CME system.

- FALSE—No PIN is defined.

Logged-in

- TRUE
                                             						indicates that a phone user is currently logged in on this phone.

- FALSE indicates that no phone user is currently logged in on this phone.

### Related Commands

Command

Description

login (telephony-service)

Defines when users of IP phones in a Cisco Unified CME system are logged out
                                          						automatically.

pin

Sets
                                          						set a personal identification number (PIN) for an IP phone in a Cisco Unified
                                          						CME system.

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone moh

To display information about moh files in use, use
                              		  the show ephone moh command in global configuration mode.

show ephone moh

### Syntax Description

This command has no arguments or keywords

### Command Modes

Global Configuration mode.

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use the show ephone moh to display information about the different
                              		  MOH group configured. The following examples displays different MOH group
                              		  configured.

## Examples

```
Router #show ephone moh
Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
Skinny Music On Hold Status (moh-group 2)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/audio/hello.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.6 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 3)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/bells.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.5 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 4)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/3003.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.7 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 5)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/4004.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.8 port 2000 via 0.0.0.0
```

### Related Commands

Command

Description

show ephone-dn

Displays MOH group information for a phone directory
                                          						number.

show ephone summary

Displays the information about the MOH files in use

show voice moh-group statistics

Displays the MOH subsystem statistics information

## show ephone offhook

To display information and packet counts for the phones that are
                              		  currently off hook, use the show ephone offhook command in privileged EXEC mode.

show ephone offhook

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command is introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command is integrated into Cisco IOS Release 12.3(4)T.

Cisco IOS XE Gibraltar 16.11.1a

Unified CME 12.6

This command is enhanced to display the keys that are in use per media stream, along with the sRTP Ciphers.

## Examples

The following sample output is displayed when no phone is off hook:

```
Router# show ephone offhook No ephone in specified type/condition.
```

The following sample output displays information for a phone that is
                              		  off hook:

```
Router# show ephone offhook ephone-5 Mac:000A.8A2C.8C6E TCP socket:[20] activeLine:1 REGISTERED
mediaActive:0 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.22.84.71 51228 Telecaster 7960  keepalive 43218 max_line 6
button 1:dn 9  number 59943 CH1 SIEZE     silent-ring
button 2:dn 10 number 59943 CH1 IDLE
button 3:dn 42 number A4400  auto dial A4500 CH1 IDLE
button 4:dn 96 number 69943  auto dial 95259943 CH1 IDLE
button 5:dn 75 number 49943  auto dial 49943 CH1 IDLE
speed dial 1:57514 marketing
Active Call on DN 9 chan 1 :59943 0.0.0.0 0 to 0.0.0.0 2000 via 172.30.151.1
G711Ulaw64k  160 bytes vad
Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1
Username:user1 Password:newuser
```

The following is a sample output for the show command, show ephone offhook . The lines that are added to the show command output as part of the Unified CME 12.6 enhancement are local key and remote
                              key.

```
ephone-1[0] Mac:549A.EBB5.8000 TCP socket:[1] activeLine:1 whisperLine:0 REGISTERED in SCCP ver 21/17 max_streams=1 + Authentication + Encryption with TLS connection
mediaActive:1 whisper_mediaActive:0 startMedia:1 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:8
IP:8.44.22.63 * 17872 SCCP Gateway (AN) keepalive 28 max_line 1 available_line 1
port 0/0/0
button 1: cw:1 ccw:(0 0)
 dn 1 number 6901 CM Fallback CH1 CONNECTED CH2 IDLE
Preferred Codec: g711ulaw
Lpcor Type: none Active Secure Call on DN 1 chan 1 :6901 8.44.22.63 18116
 to 8.39.25.11 8066 via 8.39.0.1
G711Ulaw64k 160 bytes no vad SRTP cipher: AES_CM_128_HMAC_SHA1_32
  local key: 0OPV0yxvcnRLPMzHfmYbwgHfdxcuS1uPbp5j/Tjk
  remote key: e8DQl3Kvk7LjZlipaCoMg9TMreBmiPsFmNiVHwIA Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1
```

The following sample output displays information for a phone that has
                              		  just completed a call:

```
Router# show ephone offhook ephone-5 Mac:000A.8A2C.8C6E TCP socket:[20] activeLine:1 REGISTERED
mediaActive:1 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.22.84.71 51228 Telecaster 7960  keepalive 43224 max_line 6
button 1:dn 9  number 59943 CH1 CONNECTED silent-ring
button 2:dn 10 number 59943 CH1 IDLE
button 3:dn 42 number A4400  auto dial A4500 CH1 IDLE
button 4:dn 96 number 69943  auto dial 95259943 CH1 IDLE
button 5:dn 75 number 49943  auto dial 49943 CH1 IDLE
speed dial 1:57514 marketing
Active Call on DN 9 chan 1 :59943 10.23.84.71 22926 to 172.30.131.129 2000 via 172.30.151.1
G711Ulaw64k  160 bytes no vad
Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1 (media path callID 19288 srcCallID 1
9289)
Username:user1 Password:newuser
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 overlay

To display
                              		  information for the registered phones that have overlay ephone-dns associated
                              		  with them, use the show ephone overlay in privileged EXEC mode.

show ephone overlay

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

This command does
                              		  not apply to Cisco Unified SRST.

## Examples

The following is
                              		  sample output from the show ephone overlay command:

```
Router# show ephone overlay ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.2.225.205 52486 Telecaster 7960  keepalive 2771 max_line 6
button 1: dn 11 number 60011 CH1 IDLE      overlay 
button 2: dn 17 number 60017 CH1 IDLE      overlay 
button 3: dn 24 number 60024 CH1 IDLE      overlay 
button 4: dn 30 number 60030 CH1 IDLE      overlay 
button 5: dn 36 number 60036 CH1 IDLE      CH2 IDLE      overlay 
button 6: dn 39 number 60039 CH1 IDLE      CH2 IDLE      overlay 
overlay 1: 11(60011) 12(60012) 13(60013) 14(60014) 15(60015) 16(60016) 
overlay 2: 17(60017) 18(60018) 19(60019) 20(60020) 21(60021) 22(60022) 
overlay 3: 23(60023) 24(60024) 25(60025) 26(60026) 27(60027) 28(60028) 
overlay 4: 29(60029) 30(60030) 31(60031) 32(60032) 33(60033) 34(60034) 
overlay 5: 35(60035) 36(60036) 37(60037) 
overlay 6: 38(60038) 39(60039) 40(60040)
```

The show ephone command describes significant fields in
                              		  this output. The below table describes a field that is not in that table.

Field

Description

overlay number

Displays
                                          					 the contents of an overlay set, including each dn-tag and its associated
                                          					 extension number.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone
                        	 phone-load

To display
                              		  information about the phone firmware that is loaded on registered phones, use
                              		  the show ephone phone-load command in privileged EXEC mode.

show ephone phone-load

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following is
                              		  sample output that displays the phone firmware versions for all phones in the
                              		  system:

```
Router# show ephone phone-load DeviceName        CurrentPhoneload       PreviousPhoneload      LastReset
=====================================================================
SEP0002B9AFC49F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C2D0B0   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000C30F03707   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C2999F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000A8A2C8C6E   3.2(2.14)              3.2(2.14)              Initialized
SEP0002B9AFBB4D   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP00075078627F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP0002FD659E59   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP00024BCCD626   3.2(2.14)                                     CM-closed-TCP
SEP0008215F88C1   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000C30F0390C   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C30143   3.2(2.14)              3.2(2.14)              TCP-timeout
```

The below table
                              		  describes significant fields in this output.

Field

Description

DeviceName

Device
                                          					 name.

CurrentPhoneLoad

Current
                                          					 phone firmware version.

PreviousPhoneLoad

Phone
                                          					 firmware version before last phone load.

LastReset

Reason
                                          					 for last reset of phone.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone
                        	 registered

To display the
                              		  status of registered phones, use the show ephone registered command in privileged EXEC mode.

show ephone registered

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The output was enhanced to include the setting of the
                                          						feature-button command.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

## Examples

The following is
                              		  sample output from the show ephone registered command:

```
Router# show ephone registered ephone-12[11] Mac:001A.A11B.7D6D TCP socket:[5] activeLine:0 whisperLine:0 REGIS
TERED in SCCP ver 15/12 max_streams=1
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 res
et_sent:0 paging 0 debug:0 caps:7
IP:10.10.1.17 * 35177 6941  keepalive 3593 max_line 4 available_line 3
button 1: cw:1 dn 11 number 1001 CH1   IDLE         CH2   IDLE
button 2: cw:1 dn 56 number 6971  auto dial 6970 CH1   IDLE
button 3: cw:1 dn 10 number 1000 CH1   IDLE         CH2   IDLE
1 feature buttons enabled: dnd
Preferred Codec: g711ulaw
Lpcor Type: none
```

The below table
                              		  describes significant fields in this output.

Field

Description

active

Number of
                                          					 active parties registered.

ephone

Cisco IP
                                          					 phone.

mac-address

MAC
                                          					 address of the Cisco IP phone.

keepalive

Defines
                                          					 keepalive timeout period to unregister IP phone.

feature-buttons

Displays
                                          					 the type of feature button on the ephone.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone
                        	 registered summary

To display the
                              		  details of all the registered Skinny Client Control Protocol (SCCP) phones that
                              		  are sorted based on ephone tags, use the show ephone registered summary command in privileged EXEC mode.

show ephone registered summary

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command has
                              		  no default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to view the details of the registered phones configured in the SCCP mode sorted
                              		  by ephone tags.

## Examples

The following is
                              		  sample output of the registered phones configured in the SCCP mode.

The * symbol
                                          			 adjacent to the Directory Number (DN) in the command output indicates that the
                                          			 Directory Number (DN) is an Overlay-dn.

```
router# show ephone registered summary ==================================================================================
PhoneType 	Ephone 	MacAddress 				 IpAddress 		Ln 		 Dn 		Number 		Status
==================================================================================
8941 								1 				7081.050C.0927  9.51.0.71 			1 			1 			3001 			Registered
 																												 																  2    2* 		3002				Registered
  																																														2 			5*		 3005				Registered
		                               												  	2				6*			3006 			Registered
7970 								2 				001B.D52C.DF27  9.51.0.72 			1				3 			3003 			Registered
  																																														2    4				3004				Registered
7970 								5 				001B.D52C.4AEE  9.51.0.75			 1 			9 			3009   	Registered
  																																														2 			10	 	3010				Registered
==================================================================================
Total ephones configured 			: 10
Total ephones registered 			: 3
Total ephones unregistered		: 5
Total ephones deceased 					: 0
Ephones in unknown state 			: 2
```

Field

Description

DN

Directory
                                       				  number of the phone.

Ephone

Total
                                       				  number of ephone tags configured.

IP
                                       				  Address

IP
                                       				  address of the phones.

LN

Line
                                       				  number of the phone.

MacAddress

Shows the
                                       				  MAC address of the SCCP phone.

Number

Number
                                       				  assigned to ephone.

PhoneType

Shows the
                                       				  type of Cisco IP phone.

Status

Shows the
                                       				  registration status.

### Related Commands

Command

Description

show ephone summary types

Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type.

show ephone unregistered summary

Displays the details of all the unregistered SCCP phones.

## show ephone remote

To display nonlocal phones (phones with no Address Resolution
                              		  Protocol [ARP] entry), use the show ephone remote command in privileged EXEC mode.

show ephone remote

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Phones without ARP entries are suspected not to be on the LAN. Use
                              		  the show ephone remote command to identify phones without ARP entries that might have
                              		  operational issues.

## Examples

The following is sample output that identifies ephone 2 as not having
                              		  an ARP entry:

```
Router# show ephone remote ephone-2 Mac:0185.047C.993E TCP socket:[4] activeLine:0 REGISTERED
mediaActive:1 offhook:0 ringing:0 reset:0 reset_sent:0 paging 1 debug:0
IP:10.50.50.20 49231 Telecaster 7910  keepalive 112 max_line 2 dual-line
button 1:dn 3  number 95021 CH1 IDLE
paging-dn 25
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone ringing

To display information on phones that are ringing, use the show ephone ringing command in privileged EXEC mode.

show ephone ringing

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone ringing command:

```
Router# show ephone ringing ephone-1 Mac:0005.5E37.8090 TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:1 reset:0 reset_sent:0 paging 0 debug:0
IP:10.50.50.10 49329 Telecaster 7960  keepalive 17602 max_line 6
button 1:dn 1  number 95011 CH1 RINGING   CH2 IDLE
button 2:dn 2  number 95012 CH1 IDLE
```

The show ephone describes significant fields in this
                              		  output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone rtp
                        	 connections

To display active
                              		  Real-Time Transport Protocol (RTP) call information on ephone call legs, use
                              		  the show ephone rtp connections command in privileged EXEC mode.

show ephone rtp connections

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

15.2(1)T

This
                                          						command was introduced.

### Usage Guidelines

The show ephone rtp connections command displays information on active
                              		  RTP calls, including the ephone tag number of the phone with an active call,
                              		  the channel of the ephone-dn, and the caller and called party's numbers for the
                              		  connection for both local and remote endpoints. The output from this command
                              		  provides an overview of all the connections in the system, narrowing the
                              		  criteria for debugging pulse code modulation and Cisco Unified CME packets
                              		  without a sniffer.

## Examples

The following
                              		  sample output shows all the connected ephones in the Cisco Unified CME system.
                              		  The sample output shows five active ephone connections with one of the phones
                              		  having the dspfarm-assist keyword configured to transcode the
                              		  code on the local leg to the indicated codec. The output also shows four ephone
                              		  to ephone calls, represented in the CallID columns of both the RTP connection
                              		  source and RTP connection destination by zero values.

Normally, a phone
                              		  can have only one active connection but in the presence of a whisper intercom
                              		  call, a phone can have two. In the sample output, ephone-40 has two active
                              		  calls: it is receiving both a normal call and a whisper intercom call. The
                              		  whisper intercom call is being sent by ephone-6, which has an invalid LocalIP
                              		  of 0.0.0.0. The invalid LocalIP indicates that it does not receive RTP audio
                              		  because it only has a one-way voice connection to the whisper intercom call
                              		  recipient.

```
Router# show ephone rtp connections Ephone RTP active connections :
Ephone    Line  DN Chan  SrcCallID  DstCallID             Codec (xcoded?)
    SrcNum DstNum  LocalIP               RemoteIP
ephone-5     1   5    1         15         14              G729 (Y)
    1005  1102  [192.168.1.100]:23192  [192.168.1.1]:2000
ephone-6     2  35    1          0          0       G711Ulaw64k (N) 
    1035  1036  [0.0.0.0]:0  [192.168.1.81]:21256
ephone-40    1 140    1          0          0       G711Ulaw64k (N)
    1140  1141  [192.168.1.81]:21244  [192.168.1.70]:20664
ephone-40    2  36    1          0          0       G711Ulaw64k (N)
    1035  1036  [192.168.1.81]:21256  [192.168.1.1]:2000
ephone-41    1 141    1          0          0       G711Ulaw64k (N)
    1140  1141  [192.168.1.70]:20664  [192.168.1.81]:21244 
Found 5 active ephone RTP connections
```

The below table
                              		  explains the fields in the show ephone rtp connections command output.

Field

Description

Ephone

Ephone
                                          					 tag number with an active call.

Line

Line
                                          					 appearance of the phone.

DN

Ephone-dn
                                          					 tag.

Chan

Channel
                                          					 of the ephone-dn.

SrcCallID

CCAPI
                                          					 CallID for the RTP connection source. For ephone to ephone calls, this will be
                                          					 0. SrcCallID compares to “CallId” in the show voip rtp connections command output.

DstCallID

CCAPI
                                          					 CallID for the RTP connection destination. For ephone to ephone calls, this
                                          					 will be 0. DstCallID compares to “dstCallId” in the show voip rtp connections command output.

Codec
                                          					 (xcoded)

Codec
                                          					 name used by the phone with the active call. If xcoded is ‘Y’, the phone has
                                          					 the dspfarm-assist keyword configured to transcode the
                                          					 code on the local leg to the indicated codec.

SrcNum

Caller’s number for the connection. This number is not necessarily the ephone’s
                                          					 DN.

DstNum

Called
                                          					 party’s number for the connection.

LocalIP

Call’s
                                          					 local IP address and port. This is usually the ephone’s IP address. The IP
                                          					 address in brackets is either in IPv4 or IPv6 format, followed by a colon and
                                          					 the port number. The port compares to the “LocalRTP” number in the show voip rtp connections command output.

RemoteIP

Call’s
                                          					 remote IP address and port. For flow-around ephone to ephone calls, this is
                                          					 usually the other ephone’s IP address. For flow-through trunk calls, this is
                                          					 usually the Cisco Unified CME’s IP address. The port compares to the “RmtRTP”
                                          					 number in the show voip rtp connections command output.

### Related Commands

Command

Description

show ephone registered

Displays the status of registered SCCP phones in Cisco Unified CME.

show voip rtp connections

Displays information about Real-Time Transport Protocol (RTP) named event
                                          						packets.

## show ephone socket

To display IP addresses (IPv4, IPv6, or dual-stack) being used by
                              		  ephone sockets, use the show ephone socket command in privileged EXEC mode.

show ephone socket

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use the show ephone socket command to verify if IPv4 only, IPv6 only, or dual-stack
                              		  (IPv4/IPv6) is configured on Cisco Unified CME. In the following example,
                              		  skinny_tcp_listen_socket fd = 0 and skinny_tcp_listen_socket fd = 1 verify that
                              		  dual-stack configuration. When IPv6 only is configured show ephone socket
                              		  command displays skinny_tcp_listen_socket fd = -1 and skinny_tcp_listen_socket
                              		  fd = 0 values. When IPv4 only is configured the show ephone socket command
                              		  displays skinny_tcp_listen_socket fd = 0 and skinny_tcp_listen_socket (ipv6) fd
                              		  = -1 values.

## Examples

The following is sample output from the show ephone socket command:

```
Router# show ephone ssocket skinny_tcp_listen_socket fd = 0
skinny_tcp_listen_socket (ipv6) fd = 1
 
skinny_secure_tcp_listen_socket fd = -1
skinny_secure_tcp_listen_socket (ipv6) fd = -1
 
skinny_open_sockets = 3:
Phone 3, 
skinny_sockets[0] fd = 1 
        read_buffer 0x480061E8, read_offset 0, read_header N, read_length 0                     
        resend_queue 0x47CE8178, resend_offset 0, resend_flag N, resend_Q_depth 0 
Phone 2, 
skinny_sockets[1] fd = 2 
        read_buffer 0x48006A24, read_offset 0, read_header N, read_length 0                     
        resend_queue 0x47CE8104, resend_offset 0, resend_flag N, resend_Q_depth 0 
Phone 1, 
skinny_sockets[2] fd = 3 
        read_buffer 0x48007260, read_offset 0, read_header N, read_length 0                     
        resend_queue 0x47CE8090, resend_offset 0, resend_flag N, resend_Q_depth 0
```

### Related Commands

Command

Description

show ephone summary

Displays information about Cisco IP phones.

## show ephone
                        	 summary brief

To display details
                              		  of all the SCCP phones sorted by ephone-tag, use the show ephone summary
                                    				brief command in privileged EXEC mode.

show ephone summary brief

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command had
                              		  no default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

The command output
                              		  displays the status, IP address, and MAC address of the phones.

## Examples

The following is
                              		  sample output of the show ephone summary
                                    				brief command.

The asterisk
                                          			 symbol (*) adjacent to the Directory Number (DN) in the command output
                                          			 indicates that the Directory Number (DN) is an Overlay-dn.

```
router# show ephone summary brief ============================================================================================================
PhoneType 	      Ephone 	      MacAddress 	      IpAddress 	      Ln 	    Dn 	     Number 	  Status
============================================================================================================
8941 						        1 						7081.050C.0927 							9.51.0.71 			     1 						1 							3001 				Registered
																																													           											2    			2* 						3002     Registered
																																													 																					2 						5* 						3005 				Registered
																																																																			2 						6* 						3006 				Registered
7970 						       	2 						001B.D52C.DF27 							9.51.0.72 								1 						3 							3003 				Registered
																																																																			2 						4 							3004 				Registered
7970 														3 						001B.54CA.43F7 																									1 						5 							3005 				Unregistered
																																																																			2 						6 							3006 				Unregistered
																																																																			3 						2* 						3002 				Unregistered
																																																																			3 						3* 						3003 				Unregistered
																																																																			3 						8* 						3008 				Unregistered
8945														 4 					 D48C.B5C9.D2E6 																									1 						7 							3007 				Unregistered
																																																																			2 						8 							3008 				Unregistered
7970 														5 						001B.D52C.4AEE 							9.51.0.75 								1 						9 							3009 				Registered
																																																																			2 						10 						3010 				Registered
8941														 6 						1111.2222.3333 																																																			Unregistered
8941 														10 					1111.2222.3334 																																																			Unregistered
6901 																						11 1111.2222.3332 																																																Unregistered
Unknown Ephone				 12 																																																																							Unknown
Unknown Ephone				 13 																																																																							Unknown
=========================================================================================================
Total ephones configured 	: 10
Total ephones registered 	: 3
Total ephones unregistered: 5
Total ephones deceased 			: 0
Ephones in unknown state 	: 2
```

Field

Description

DN

Directory
                                       				  number of the phone.

Ephone

ephone
                                       				  tag.

IP
                                       				  Address

IP
                                       				  address of the phone.

LN

Line
                                       				  number of the phone.

MacAddress

Shows the
                                       				  MAC address of the SCCP phone.

Number

Number
                                       				  assigned to ephone.

PhoneType

Shows the
                                       				  type of Cisco IP phone.

Status

Shows the
                                       				  registration status.

### Related Commands

Command

Description

show ephone summary types

Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type.

## show ephone summary

To display brief information about Cisco IP phones, use the show ephone summary command in privileged EXEC mode.

show ephone summary

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco CME 1.0 Cisco SRST 1.0

This command was introduced.

12.2(8)T

Cisco CME 2.0 Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						.

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was modified. The output was enhanced to show
                                          						IPv6 or IPv4 addresses configured on ephones.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was modified. The output was enhanced to show
                                          						voice-class stun-usage information.

## Examples

The following is sample output from the show ephone summary command:

```
Router# show ephone summary hairpin_block:
ephone-1[0] Mac:FCAC.3BAE.0000 TCP socket:[17] activeLine:0 whisperLine:0 REGISTERED
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0  primary_dn: 1*
IP:10.2.1.0 * SCCP Gateway (AN)  keepalive 2966   music 0  1:1
port 0/0/0
voice-class stun is enabled
ephone-2[1] Mac:FCAC.3BAE.0001 TCP socket:[18] activeLine:0 whisperLine:0 REGISTERED
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0  primary_dn: 2*
IP:10.2.1.5 * SCCP Gateway (AN)  keepalive 2966   music 0  1:2
port 0/0/1
voice-class stun is enabled
ephone-4 Mac:0030.94C3.F43A TCP socket:[-1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0
IP:10.2.1.1 Telecaster 7960  keepalive 59 
Max 48, Registered 1, Unregistered 0, Deceased 0, Sockets 1
Max Conferences 4 with 0 active (4 allowed)
Skinny Music On Hold Status
Active MOH clients 0 (max 72), Media Clients 0
No MOH file loaded
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 summary types

To display the
                              		  total count of registered and unregistered phones for each phone type operating
                              		  in the Skinny Client Control Protocol (SCCP ) mode, use the show ephone summary
                                    				types command in privileged EXEC mode.

show ephone summary types

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command has
                              		  no default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  displays the count of configured, registered, unregistered, and deceased
                              		  phones.

## Examples

The following is
                              		  an example of the show ephone summary
                                    				types command:

```
Router# show ephone summary types ===========================================================================
PhoneType										 Configured 	Registered 	Unregistered 	Deceased 	Other
===========================================================================
Unknown Ephone type 				2 										0 											0 										0 							2
6901 																			1 										0 											1 										0 							0
8945 																			1 										0 											1 										0 							0
7970 																			3 										2 											1 										0 							0
8941 																			3 										1 											2 										0 							0
===========================================================================
Total Phones 											10 									3 											5 										0 							2
===========================================================================
```

### Related Commands

Command

Description

show ephone summary brief

Displays the details of all the SCCP phones configured.

## show ephone tapiclients

To display status of ephone Telephony Application Programming
                              		  Interface (TAPI) clients, use the show ephone tapiclients command in
                              		  privileged EXEC mode.

show ephone tapiclients

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone tapiclients command:

```
Router# show ephone tapiclients ephone-4 Mac:0007.0EA6.39F8 TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:192.168.1.18 50291 Telecaster 7960  sub=3 keepalive 728 max_line 20
button 1:dn 6  number 1004 CH1 IDLE      CH2 IDLE
button 2:dn 1  number 1000 CH1 IDLE      shared
button 3:dn 2  number 1000 CH1 IDLE      shared
button 7:dn 3  number 1001 CH1 IDLE      CH2 IDLE      monitor-ring shared
button 8:dn 4  number 1002 CH1 IDLE      CH2 IDLE      monitor-ring shared
button 9:dn 5  number 1003 CH1 IDLE      CH2 IDLE      monitor-ring
button 10:dn 91 number A00  auto dial A01 CH1 IDLE
speed dial 1:2000 PAGE-STAFF
speed dial 2:2001 HUNT-STAFF
paging-dn 90
Username:userB Password:ge30qe
Tapi client information
Username:userB status:REGISTERED Socket :[5]
 Tapi Client IP address: 192.168.1.5  Port:2295
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone telephone-number

To display information for the phone associated with a specified
                              		  number, use the show ephone telephone-number command in
                              		  privileged EXEC mode.

show ephone telephone-number number

### Syntax Description

number

Telephone number that is associated with an ephone.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to find the phone on which a particular telephone
                              		  number appears.

## Examples

The following is sample output from the show ephone telephone-number :

```
Router# show ephone telephone-number 91400 DP tag: 0, primary
Tag 1, Normal or Intercom dn
  ephone 1, mac-address 000A.0E51.19F0, line 1
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone unregistered

To display information about unregistered phones, use the show ephone unregistered command in
                              		  privileged EXEC mode.

show ephone unregistered

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

There are two ways that an ephone can become unregistered. The first
                              		  way is when an ephone is listed in the running configuration but no physical
                              		  device has been registered for that ephone. The second way is when an unknown
                              		  device was registered at some time after the last router reboot but has since
                              		  unregistered.

## Examples

The following is sample output from the show ephone unregistered :

```
Router# show ephone unregistered ephone-1 Mac:0007.0E81.10F0 TCP socket:[-1] activeLine:0 UNREGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:0.0.0.0 0 Unknown 0  keepalive 0 max_line 0
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 unregistered summary

To display the
                              		  details of all the unregistered Skinny Call Control Protocol (SCCP) phones
                              		  sorted by ephone tag, use the show ephone unregistered
                                    				summary command in privileged EXEC mode.

show ephone unregistered summary

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command has
                              		  no default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to view the details of the unregistered phones configured in the SCCP mode.

## Examples

The following is a
                              		  sample output of the show ephone unregistered
                                    				summary command.

The * symbol
                                          			 adjacent to the Directory Number (DN) in the command output indicates that the
                                          			 Directory Number (DN) is an Overlay-dn.

```
router# show ephone unregistered summary ===============================================================================
PhoneType 			Ephone 			MacAddress 				IpAddress 		Ln 		Dn 		Number 		Status 
===============================================================================
7970 										3 						001B.54CA.43F7														1 			5 		3005 				Unregistered
																																																			2 			6 		3006 				Unregistered
																																																			3 			2* 	3002 				Unregistered
																																																			3 			3* 	3003 				Unregistered
																																																			3 			8* 	3008 				Unregistered
8945 										4 						D48C.B5C9.D2E6 													1 			7 		3007 				Unregistered
																																																			2 			8 		3008 				Unregistered
8941 										6 						1111.2222.3333 																															Unregistered
8941 										10 					1111.2222.3334 																															Unregistered
6901 																		11 1111.2222.3332 																												Unregistered
===============================================================================
Total ephones configured 	: 10
Total ephones registered 	: 3
Total ephones unregistered: 5
Total ephones deceased 			: 0
Ephones in unknown state 	: 2
```

Field

Description

DN

Directory number of the phone.

Ephone

Total number of ephone tags configured.

IP Address

IP address of the phones.

LN

Line number of the phone.

MacAddress

Shows the MAC address of the SCCP phone.

Number

Number assigned to ephone.

PhoneType

Shows the type of Cisco IP phone.

Status

Shows the registration status.

### Related Commands

Command

Description

show ephone registered summary

Displays the details of all the registered SCCP phones.

show ephone summary types pattern

Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type.

## show
                        	 ephone-dn

To display status
                              		  and information for a Cisco IP phone destination number or for extensions
                              		  (ephone-dns) in a Cisco Unified CallManager Express (Cisco Unified CME) or
                              		  Cisco Unified Survivable Remote Site Telephony (SRST) environment, use the show ephone-dn command in privileged EXEC mode.

show ephone-dn [dn-tag]

### Syntax Description

dn-tag

(Optional) For Cisco Unified CME, a unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

(Optional) For Cisco Unified SRST, a destination number tag. The destination
                                          						number can be from 1 to 288.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T command.

## Examples

## Examples

The following
                              		  Cisco Unified CME sample output displays status and information for all
                              		  ephone-dns:

```
Router# show ephone-dn 50/0/1 CH1 DOWN 
EFXS 50/0/1 Slot is 50, Sub-unit is 0, Port is 1
 Type of VoicePort is EFXS
 Operation State is UP
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
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
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
 Station name None, Station number 91400
 Caller ID Info Follows:
 Standard BELLCORE
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Digit Duration Timing is set to 100 ms
50/0/2 CH1 IDLE      CH2 IDLE        
EFXS 50/0/2 Slot is 50, Sub-unit is 0, Port is 2
 Type of VoicePort is EFXS
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
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
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
 Station name None, Station number 91450
 Caller ID Info Follows:
 Standard BELLCORE
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Digit Duration Timing is set to 100 ms
```

## Examples

The following
                              		  SRST sample output displays status and information for all ephone-dns:

```
Router# show ephone-dn 7 50/0/7 INVALID     
EFXS 50/0/7 Slot is 50, Sub-unit is 0, Port is 7
 Type of VoicePort is EFXS
 Operation State is UP
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
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to default
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
 Playout-delay Minimum mode is set to default, value 4 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 8 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Station name None, Station number None
 Caller ID Info Follows:
 Standard BELLCORE
 Voice card specific Info Follows:
 Digit Duration Timing is set to 100 ms
```

The following
                              		  table describes significant fields in the output from this command.

Field

Description

Administrative State

Administrative (configured) state of the voice port.

alert

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call alerting state (for example, because the far-end phone
                                          					 rang but was not answered and the far-end system decided to drop the call
                                          					 rather than let the phone ring for too long).

answered
                                          					 (incoming)

The
                                          					 number of incoming calls that were actually answered (the phone goes off hook
                                          					 when ringing).

answered
                                          					 (outgoing)

The
                                          					 number of outgoing call attempts that were answered by the far end.

busy

The
                                          					 number of outgoing call attempts that got a busy response.

Call
                                          					 Disconnect Time Out

Not
                                          					 applicable to the Cisco IP phone.

called,
                                          					 calling

Extension numbers of called and calling parties.

Caller
                                          					 ID Info Follows

Information about the caller ID.

Call
                                          					 Ref

A
                                          					 unique per-call identifier used by the SCCP protocol. The Call Ref values are
                                          					 assigned sequentially within the Cisco CME–SCCP interface, so this value also
                                          					 indicates the total number of SCCP calls since the router was last rebooted.

chan

Channel
                                          					 number of an ephone-dn.

CODEC

Codec
                                          					 type.

Companding Type

Not
                                          					 applicable to the Cisco IP phone.

connect

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call connected state.

Connection Mode

Not
                                          					 applicable to the Cisco IP phone.

Connection Number

Not
                                          					 applicable to the Cisco IP phone.

Description

Not
                                          					 applicable to the Cisco IP phone.

Digit
                                          					 Duration Timing

Not
                                          					 applicable to the Cisco IP phone.

DN
                                          					 STATE

Ephone-dn tag number and state of the phone line associated with an extension.

Echo
                                          					 Cancellation...

Not
                                          					 applicable to the Cisco IP phone.

Echo
                                          					 Cancel Coverage

Not
                                          					 applicable to the Cisco IP phone.

EFXS

Voice
                                          					 port type.

Far-end
                                          					 disconnect at...

See
                                          					 connect, alert, hold, and ring.

Final
                                          					 Jitter

The
                                          					 final voice packet receive jitter reported by the IP phone at the end of the
                                          					 call.

hold

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call hold state (for example, if the caller was left on hold
                                          					 for too long and got tired of waiting).

incoming

The
                                          					 number of incoming calls presented (the phone rings).

In Gain

Not
                                          					 applicable to the Cisco IP phone.

Initial
                                          					 Time Out

Amount
                                          					 of time the system waits for an initial input digit from the caller.

Interdigit Time Out

Amount
                                          					 of time the system waits for a subsequent input digit from the caller.

Last 64
                                          					 far-end disconnect cause codes

See the
                                          					 Mappings of PSTN Cause Codes to SIP Event table for a list of public switch
                                          					 telephone network (PSTN) cause codes that can be sent as an ISDN cause
                                          					 information element (IE) and the corresponding Session Interface Protocol (SIP)
                                          					 event.

Latency

The
                                          					 final voice packet receive latency reported by the IP phone at the end of the
                                          					 call.

Lost

Number
                                          					 of lost packets.

Music
                                          					 On Hold Threshold

Not
                                          					 applicable to the Cisco IP phone.

No
                                          					 Interface Down Failure

State
                                          					 of the interface.

Noise
                                          					 Regeneration

Not
                                          					 applicable to the Cisco IP phone.

Non
                                          					 Linear...

Not
                                          					 applicable to the Cisco IP phone.

Operation State

Operational state of the voice port.

Out
                                          					 Attenuation

Not
                                          					 applicable to the Cisco IP phone.

outgoing

The
                                          					 number of outgoing call attempts.

Playout-delay Maximum

Not
                                          					 applicable to the Cisco IP phone.

Playout-delay...

Not
                                          					 applicable to the Cisco IP phone.

Port

Port
                                          					 number for the interface associated with the voice interface card.

Region
                                          					 Tone

Not
                                          					 applicable to the Cisco IP phone.

ring

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the ringing state (for example, if the call was not answered and
                                          					 the caller hung up).

Ringing
                                          					 Time Out

Duration, in seconds, for which ringing is to continue if a call is not
                                          					 answered. Set with the timeouts ringing command.

Rx
                                          					 Pkts, bytes

Number
                                          					 of packets and bytes received during the current or last call.

Signal
                                          					 Level to phone, peak

For
                                          					 G.711 calls only, this parameter indicates the most recent voice signal level
                                          					 in the voice IP packets sent from the router to the IP phone. This parameter is
                                          					 valid only for VoIP or PSTN G.711 calls to the IP phones. This parameter is not
                                          					 valid for calls between local IP phones, or calls that use codecs other than
                                          					 G.711. The peak field indicates the peak signal level seen during the entire
                                          					 call.

Slot

Slot
                                          					 used in the voice interface card for this port.

Station
                                          					 name

Station
                                          					 name.

Station
                                          					 number

Station
                                          					 number.

Stream
                                          					 Port

RTP
                                          					 port allocated by the given DN/channel.

Sub-unit

Subunit
                                          					 used in the voice interface card for this port.

Tx
                                          					 Pkts, bytes

Number
                                          					 of packets and bytes transmitted during the current call or last call.

Type of
                                          					 VoicePort

Voice
                                          					 port type.

VAD

Voice
                                          					 activity detection.

Voice
                                          					 card specific info

Information specific to the voice card.

VPM
                                          					 STATE

State
                                          					 indication for the VPM software component.

VTSP
                                          					 STATE

State
                                          					 indication for the VTSP software component.

Wait
                                          					 Release Time Out

Time
                                          					 that a voice port stays in the call-failure state while the router sends a busy
                                          					 tone, reorder tone, or out-of-service tone to the port.

The following
                              		  table lists the PSTN cause codes that can be sent as an ISDN cause information
                              		  element (IE) and the corresponding SIP event for each. These are the far-end
                              		  disconnect cause codes listed in the output for the show ephone-dn statistics command.

PSTN
                                          					 Cause Code

Description

SIP
                                          					 Event

1

Unallocated number

410
                                          					 Gone

3

No
                                          					 route to destination

404 Not
                                          					 found

16

Normal
                                          					 call clearing

BYE

17

User
                                          					 busy

486
                                          					 Busy here

18

No user
                                          					 responding

480
                                          					 Temporarily unavailable

19

No
                                          					 answer from the user

21

Call
                                          					 rejected

603
                                          					 Decline

22

Number
                                          					 changed

302
                                          					 Moved temporarily

27

Destination out of order

404 Not
                                          					 found

28

Address
                                          					 incomplete

484
                                          					 Address incomplete

29

Facility rejected

501 Not
                                          					 implemented

31

Normal
                                          					 unspecified

404 Not
                                          					 found

34

No
                                          					 circuit available

503
                                          					 Service unavailable

38

Network
                                          					 out of order

41

Temporary failure

42

Switching equipment congestion

44

Requested channel not available

47

Resource unavailable

55

Incoming class barred within CUG

603
                                          					 Decline

57

Bearer
                                          					 capability not authorized

501 Not
                                          					 implemented

58

Bearer
                                          					 capability not presently available

63

Service
                                          					 or option unavailable

503
                                          					 Service unavailable

65

Bearer
                                          					 cap not implemented

501 Not
                                          					 implemented

79

Service
                                          					 or option not implemented

87

User
                                          					 not member of CUG

603
                                          					 Decline

88

Incompatible destination

400 Bad
                                          					 Request

95

Invalid
                                          					 message

102

Recover
                                          					 on timer expiry

408
                                          					 Request timeout

111

Protocol error

400 Bad
                                          					 request

127

Interworking unspecified

500
                                          					 Internal server error

Any
                                          					 code other than those listed above

500
                                          					 Internal server error

### Related Commands

Command

Description

show ephone-dn callback

Displays information about pending callbacks in a Cisco Unified CME or a Cisco
                                          						Unified SRST environment.

show ephone-dn loopback

Displays information about loopback ephone-dns that have been created in a
                                          						Cisco Unified CME or a Cisco Unified SRST environment.

show ephone-dn statistics

Displays display call statistics for a Cisco IP destination or for extensions
                                          						(ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST environment.

show ephone-dn summary

Displays brief information about Cisco IP phone destination numbers or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 callback

To display
                              		  information about pending callbacks in a Cisco Unified CallManager Express
                              		  (Cisco Unified CME) or a Cisco Unified Survivable Remote Site Telephony (Cisco
                              		  Unified SRST) environment, use the show ephone-dn callback command in privileged EXEC mode.

show ephone-dn callback

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following
                              		  sample output shows a callback placed by ephone-dn 1 against ephone-dn 3.
                              		  Ephone-dn 3 has its channel 1 on hold and has just seized dial tone on its
                              		  channel 2.

```
Router# show ephone-dn callback DN 3 (95021) CallBack pending to DN 1 (95021) for ephone-1 age 7 seconds
State for DN 3 is CH1 HOLD      CH2 SIEZE
```

The following
                              		  sample output shows a callback placed by ephone-dn 1 against ephone-dn 3.
                              		  Ephone-dn 3 has a call in progress on channel 1.

```
Router# show ephone-dn callback DN 3 (95021) CallBack pending to DN 1 (95021) for ephone-1 age 8 seconds
State for DN 3 is CH1 CONNECTED
```

Significant
                              		  fields in the output from this command are described in the following table.

Field

Description

DN 3
                                          					 (95021) CallBack pending to DN 1 (95021)

Callback
                                          					 originator is the extension with the dn-tag 1 (in this example), and the
                                          					 callback has been placed on the extension with the dn-tag 3 and the number
                                          					 95021.

age

Number of
                                          					 seconds since the callback was placed.

State for
                                          					 DN 3 is CH1... CH2...

Call
                                          					 states for channel 1 and channel 2, if any, of the extension that the callback
                                          					 is for.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 conference

To display
                              		  information about ad hoc and meet-me conferences in a Cisco Unified CallManager
                              		  Express (Cisco Unified CME) environment, use the show ephone-dn conference command in privileged EXEC mode.

show ephone-dn conference [ ad-hoc [ video ] | meetme [ video ] | number number ]

### Syntax Description

ad-hoc

(Optional) Displays adhoc conferences.

meetme

(Optional) Displays meet-me conferences.

video

(Optional) Displays video conferences.

number number

(Optional) Displays the conference telephone or extension number.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The command output was enhanced to display the unlocked
                                          						Meet-Me conference setting.

15.1(4)M

Cisco
                                          						CME 8.6

This
                                          						command was modified to display information on video conferences.

## Examples

The following
                              		  sample output displays information for the 1397 conference number. There are
                              		  three directory numbers and six inactive parties. The number of unlocked DN
                              		  tags are displayed at the end of each MeetMe conference.

```
Router# show ephone-dn conference number 1397 type   active inactive  numbers
==================================
Meetme    0       6      1397
DN tags: 10, 11, 12
Unlocked DN tags: 2/3
Meetme    0       4      2486
DN tags: 13, 14
All DN tags unlocked.
Meetme    0       4      1111
DN tags: 15, 16
Ad-hoc    0       4      7777
DN tags: 20, 21
Router# sh ephone-dn conference  ad-hoc video
type   		active 	inactive  	numbers
================================================
Ad-hoc-video    	3       	3      	2000  
DN tags: 20, 21, 22
Router# sh ephone-dn conference  meetme video
type   		active 	inactive  	numbers
================================================
Meetme-video    	0       	8      	3000  
1.	DN tags: 25
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

active

Number
                                          					 of active parties in the conference.

DN tags

Directory numbers (DNs) in the conference.

inactive

Number
                                          					 of inactive parties in the conference.

number

Conference telephone or extension number.

type

Type of
                                          					 conference: meet-me or ad hoc.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 loopback

To display
                              		  information about loopback ephone-dns that have been created in a Cisco Unified
                              		  CallManager Express (Cisco Unified CME) or a Cisco Unified Survivable Remote
                              		  Site Telephony (Cisco Unified SRST) environment, use the show ephone-dn loopback command in privileged EXEC mode.

show ephone-dn loopback

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

## Examples

The following
                              		  example displays information for a loopback using ephone-dn 21 and ephone-dn
                              		  22:

```
Router# show ephone-dn loopback LOOPBACK DN status (min 21, max 22):
DN 21 51...  Loopback to DN 22 CH1 IDLE
CallingDn -1 CalledDn -1 Called   Calling   G711Ulaw64k
Strip NONE, Forward 2, prefix 10 retry 10 Media 0.0.0.0 0
callID 0 srcCallID 0 ssrc 0 vector 0
DN 22 11...  Loopback to DN 21 CH1 IDLE
CallingDn -1 CalledDn -1 Called   Calling   G711Ulaw64k
Strip NONE, Forward 2, prefix 50 retry 10 Media 0.0.0.0 0
callID 0 srcCallID 0 ssrc 0 vector 0
```

Significant
                              		  fields in the output from this command are described in the following table.

Field

Description

Called,
                                          					 Calling

Called
                                          					 number and calling number when there is a call present.

CalledDn,
                                          					 CallingDn

Ephone-dn
                                          					 tag numbers of the called and calling ephone-dn. Set to -1 if the call is not
                                          					 to or from an ephone-dn, or if there is no active call.

callID

Internal
                                          					 call reference. This usage is the same as in other Cisco IOS voice gateway
                                          					 commands.

DN

Ephone-dn
                                          					 tag (sequence number).

Forward

Number of
                                          					 digits in the original called number to forward to the other ephone-dn in the
                                          					 loopback-dn pair.

G711...

G711Ulaw64k indicates G.711 codec, mu-law, 64000-bit stream. G711alaw64k
                                          					 indicates G.711 codec, A-law, 64000-bit stream.

Loopback
                                          					 to command...

Indicates
                                          					 the opposite ephone-dn in the loopback pair and the status of that ephone-dn.

Media

IP
                                          					 destination address, if any, for any voice packets that are passing through the
                                          					 loopback DN.

min, max

Lowest
                                          					 and highest dn-tag numbers of ephone-dns that are configured as loopback-dns.

prefix

Digit
                                          					 string to add to the beginning of forwarded called numbers.

retry

Number
                                          					 of seconds to wait before retrying the loopback target when is it busy.

srcCallID

Internal call reference for the destination.

ssrc

Real-time transport protocol (RTP) synchronization source (SSRC) of the most
                                          					 recent RTP packet.

Strip

Number
                                          					 of leading digits to strip before forwarding to the other extension in the
                                          					 loopback-dn pair.

vector

The
                                          					 following values describe the media path for voice packets that pass through
                                          					 the loopback-dn:

- 0—No
                                             						media path or not a loopback-dn path (inactive).

- 1—Normal path. Loopback-dn has identified the final media destination as a
                                             						local IP phone. The media IP address field shows a valid, non-zero value.

- 2—Hairpin. Media packets are routed back through paired loopback-dns. The final
                                             						destination is not known. For example, this can be a VoIP-to-VoIP call path by
                                             						a loopback-dn.

- 3—Hairpin. The final destination is an ephone-dn in a special mode such as
                                             						paging.

- 4—Loopback-dn chain has been detected, in which two loopback-dn pairs have been
                                             						connected together.

- 5—Loopback-dn chain has been detected in which more than two loopback-dn pairs
                                             						are connected in series.

### Related Commands

Command

Description

loopback-dn

Creates a virtual loopback voice port (loopback-dn) to establish a demarcation
                                          						point for VoIP voice calls and supplementary services.

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 paging

To display
                              		  configuration information on paging groups, use the show ephone-dn paging command in user EXEC or privileged EXEC
                              		  mode.

show ephone-dn paging

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

### Usage Guidelines

Use the show ephone-dn paging command to display which paging dn is
                              		  specified and which phone is being paged.

## Examples

The following is
                              		  a sample output from the show ephone-dn paging command before paging. The output shows two
                              		  parts: the static “Paging Configuration” part and the dynamic “Paging Control
                              		  Info” part. The output of the show ephone-dn paging command should be exactly the same before
                              		  and after paging.

```
Router# show ephone-dn paging Paging Configuration
ephone-dn 250 ( IDLE )
 number 7770
 paging ip 239.1.1.0 port 20480
   ephone-2[1]          paging-dn 250(OFF) 
   ephone-7[6]          paging-dn 250(OFF) 
 paging group 251,252
   voice reg pool 1     pagingGrp 251(OFF) 
   voice reg pool 2     pagingGrp 252(OFF) 
ephone-dn 251 ( IDLE )
 number 7771
 paging ip 239.1.1.1 port 20480
   voice reg pool 1     paging-dn 251(OFF) 
ephone-dn 252 ( IDLE )
 number 7772
 paging ip 239.1.1.2 port 20480
   voice reg pool 2     paging-dn 252(OFF) 
ephone-dn 253 ( IDLE )
 number 7773
 paging ip 239.1.1.3 port 20480
   ephone-8[7]          paging-dn 253(OFF) 
        Paging Control Info
skinnyPC[0] ephone-paging-dn 250        ( IDLE ) count 0
skinnyPC[1] ephone-paging-dn 251        ( IDLE ) count 0
skinnyPC[2] ephone-paging-dn 252        ( IDLE ) count 0
skinnyPC[4] ephone-paging-dn 253        ( IDLE ) count 0
```

The following is
                              		  a sample output from the show ephone-dn paging command during paging. In this output, the
                              		  “Paging Configuration” part remains the same expect for the changes in state
                              		  from IDLE to ACTIVE and OFF to ON. However, the “Paging Control Info” part
                              		  displays the changes in the paging control information.

```
Router# show ephone-dn paging Paging Configuration
ephone-dn 250 (ACTIVE)
 number 7770
 paging ip 239.1.1.0 port 20480
   ephone-2[1]          paging-dn 250(ON ) 
   ephone-7[6]          paging-dn 250(OFF) 
 paging group 251,252
   voice reg pool 1     pagingGrp 251(ON ) 
   voice reg pool 2     pagingGrp 252(ON ) 
ephone-dn 251 ( IDLE )
 number 7771
 paging ip 239.1.1.1 port 20480
   voice reg pool 1     paging-dn 251(ON ) 
ephone-dn 252 ( IDLE )
 number 7772
 paging ip 239.1.1.2 port 20480
   voice reg pool 2     paging-dn 252(ON ) 
ephone-dn 253 ( IDLE )
 number 7773
 paging ip 239.1.1.3 port 20480
   ephone-8[7]          paging-dn 253(OFF) 
        Paging Control Info
skinnyPC[0] ephone-paging-dn 250        (ACTIVE) count 1
				phone           ip address      port
ephone#[phone]  2[1]            239.1.1.0		 20480
sccp(ephone#[phone]): 2[1](mcast)
 group 251      (ephone#[phone]): None
 group 252      (ephone#[phone]): None
sip (pool[peer tag]): None
 group 251      (pool[peer tag]): 1[40001](mcast)
 group 252      (pool[peer tag]): 2[40003](mcast)
skinnyPC[1] ephone-paging-dn 251        ( IDLE ) count 0
skinnyPC[2] ephone-paging-dn 252        ( IDLE ) count 0
skinnyPC[4] ephone-paging-dn 253        ( IDLE ) count 0
```

The following is
                              		  another sample output from the show ephone-dn paging command during paging:

```
Paging Configuration
ephone-dn 250 ( IDLE )
 number 7770
 paging ip 239.1.1.0 port 20480
 paging group 251
   ephone-2[1]          pagingGrp 251(ON )
   voice reg pool 3     pagingGrp 251(ON )
ephone-dn 251 (ACTIVE)
 number 7771
 paging ip 239.1.1.1 port 20480
   ephone-2[1]          paging-dn 251(ON )
   voice reg pool 3     paging-dn 251(ON )
        Paging Control Info
skinnyPC[0] ephone-paging-dn 250        ( IDLE ) count 0
skinnyPC[1] ephone-paging-dn 251        (ACTIVE) count 1
                phone           ip address      port
ephone#[phone]  2[1]            239.1.1.1       20480
sccp(ephone#[phone]): 2[1](m)
sip (pool[peer tag]): 3[40007](m)
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

phone

Indicates
                                          					 the ephone-dn and the paging-dn tag.

ip
                                          					 address

Indicates
                                          					 the IP multicast address to multicast voice packets for audio paging.

port

Indicates
                                          					 the UDP port for multicast paging. Range is from 2000 to 65535.

### Related Commands

Command

Description

paging-dn

Creates
                                          						a paging extension (paging-dn) to receive audio pages on a Cisco Unified IP
                                          						phone in a Cisco Unified CME system.

paging-dn (voice register)

Registers a Cisco Unified SIP IP phone to an ephone-dn paging directory number.

paging group

Creates a combined paging group from two or more previously established paging
                                          						sets.

## show ephone-dn
                        	 park

To display
                              		  information about call-park slots in the system, use the show ephone-dn park command in privileged EXEC mode.

show ephone-dn park

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.3(7)T

This
                                          						command was introduced.

## Examples

The following
                              		  example shows information for a single call-park slot that uses an ephone-dn
                              		  identifier of 50 and an extension number of 1560.

```
Router
# show ephone-dn park DN 50 (1560) park-slot state IDLE
Notify to () timeout 15 limit 20
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

DN

Ephone-dn
                                          					 tag (identifier) number for the call-park slot.

(1560)

Extension
                                          					 number associated with the call-park slot.

park-slot
                                          					 state

Whether
                                          					 the call-park slot is in use or idle.

Notify to
                                          					 ( )

Extension
                                          					 that has been specified for notification. Empty parentheses indicate that no
                                          					 extension was specified in the configuration.

timeout

Number of
                                          					 seconds between reminder rings, in seconds.

limit

Number of
                                          					 reminder rings before a call parked at this slot is disconnected.

### Related Commands

Command

Description

park-slot

Creates
                                          						a floating extension (ephone-dn) at which calls can be temporarily held
                                          						(parked).

## show ephone-dn statistics

To display call statistics for a Cisco IP destination or for
                              		  extensions (ephone-dns) in a Cisco Unified CallManager Express (Cisco Unified
                              		  CME) or a Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST)
                              		  environment, use the show ephone-dn command in privileged EXEC mode.

show ephone-dn [dn-tag] statistics

### Syntax Description

dn-tag

(Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

statistics

Displays voice quality statistics on calls for a specified
                                          						extension or for all extensions.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ1

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following sample output displays statistics for all extensions
                              		  (ephone-dns) in a Cisco Unified CME system. There are two ephone-dns (DN1 and
                              		  DN3) in this example.

```
Router# show ephone-dn statistics Total Calls 103
Stats may appear to be inconsistent for conference or shared line cases
DN 1 chan 1 incoming 36 answered 21 outgoing 60 answered 30 busy 6
Far-end disconnect at:connect 29 alert 18 hold 7 ring 15
Last 64 far-end disconnect cause codes
17 17 17 17 17 17 16 16 16 16 16 16 16 16 16 16
16 16 16 16 65 16 65 65 65 65 16 65 65 65 16 16
16 16 16 16 16 16 16 16 16 16 16 16 16 65 47 65
47 47 16 16 16 16 16 16 16 16 16 16 16 16 16 16
local phone on-hook
DN 1 chan 1 (95011) voice quality statistics for last call
Call Ref 103 called 91500 calling 95011
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 30 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
DN 1 chan 2 incoming 0 answered 0 outgoing 1 answered 0 busy 0
Far-end disconnect at:connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
local phone on-hook
DN 1 chan 2 (95011) voice quality statistics for last call
Call Ref 86 called  calling
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 0 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
DN 3 chan 1 incoming 0 answered 0 outgoing 1 answered 1 busy 0
Far-end disconnect at:connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
DN 3 chan 1 (95021) voice quality statistics for current call
Call Ref 102 called 94011 calling 95021
Current Tx Pkts 241 bytes 3133 Rx Pkts 3304 bytes 515023 Lost 0
Jitter 30 Latency 0
Worst Jitter 30 Worst Latency 0
Signal Level to phone 201 (-39 dB) peak 5628 (-12 dB)
Packets counted by router 3305
```

The following sample output displays voice quality statistics for the
                              		  ephone-dn with dn-tag 2:

```
Router# show ephone-dn 2 statistics DN 2 chan 1 incoming 0 answered 0 outgoing 2 answered 0 busy 0
Far-end disconnect at: connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
28 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
local phone on-hook
DN 2 chan 1 (91450) voice quality statistics for last call
Call Ref 2 called  calling 
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 0 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
```

The show ephone-dn command describes significant fields in
                              		  the output from this command.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone
                                          						destination number or for extensions (ephone-dns) in a Cisco Unified CME or a
                                          						Cisco Unified SRST environment.

## show ephone-dn
                        	 summary

To display brief
                              		  information about Cisco IP phone destination numbers or for extensions
                              		  (ephone-dns) in a Cisco Unified CallManager Express (Cisco Unified CME) or a
                              		  Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST)
                              		  environment, use the show ephone-dn summary command in privileged EXEC mode.

show ephone-dn summary

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

## Examples

The following is
                              		  example output from the show ephone-dn summary :

```
Router# show ephone-dn summary PORT     DN STATE    CODEC    VAD VTSP STATE            VPM STATE
======== ==========  ======== === ===================== =========
50/0/1   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/2   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/3   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/4   INVALID     -         -  -                     EFXS_INIT               
 
50/0/5   INVALID     -         -  -                     EFXS_INIT               
 
50/0/6   INVALID     -         -  -                     EFXS_INIT
```

The following
                              		  table describes significant fields in the output from this command.

Field

Description

CODEC

Type of
                                          					 codec.

DN STATE

Status of
                                          					 the ephone-dn.

EFXS

Voice
                                          					 port type.

PORT

Port
                                          					 number (virtual) for this interface. The number that follows the last slash in
                                          					 the port number is the ephone-dn tag. For example, if the port number is
                                          					 50/0/1, the dn-tag is 1.

VAD

Voice
                                          					 activity detection status.

VPM STATE

State
                                          					 indication for the voice port module (VPM) software component.

VTSP
                                          					 STATE

State
                                          					 indication for the voice telephony service provider (VTSP) software component.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 whisper

To display
                              		  information about whisper intercom ephone-dns that have been created in Cisco
                              		  Unified CME, use the show ephone-dn whisper command in privileged EXEC mode.

show ephone-dn whisper

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(22)YB

Cisco
                                          						Unified CME 7.1

This
                                          						command was introduced.

12.4(24)T

Cisco
                                          						Unified CME 7.1

This
                                          						command was integrated into Cisco IOS Release 12.4(24)T.

## Examples

The following is
                              		  sample output from the show ephone-dn whisper command showing an active whisper intercom
                              		  call between extension 6001 and 6002:

```
Router# show ephone-dn whisper DN        DN NUMBER     LABEL         SPEED DIAL    DN STATE       PHONE         
==        =========     =====         ==========    ========       =====         
101       8881          wi_8881       -               IDLE         35 w36 
102       8882          -             -               IDLE         36 
103       8883          wi_8883       -               IDLE         m35 38 
104       8884          wi_8884       -               IDLE         38 
105       8885          wi_8885_sd_8888882            IDLE         
106       8886          wi_8886_sd_8888883            IDLE         36 
107       8887          -             8888            IDLE         35 
108       8888          Mary_sd_Peter 8887            IDLE         36 
109       8889          -             -               IDLE         
110       8890          wi_8890       -               IDLE         
111       4441          4441_wi_sd_4444442            IDLE         
112       4442          wi_4442       -               IDLE         
113       4443          -             -               IDLE         
114       4444          4444_sd-8882  8882            IDLE         
141       5551          -             -               IDLE         
142       5552          -             -               IDLE         
143       5553          -             -               IDLE         
144       5554          -             -               IDLE         
145       5555          -             -               IDLE         
161       6001          -             6002            WHISPER      1 
162       6002          -             6001            WHISPER      2 
163       6003          -             6001            IDLE         
164       6004          -             6002            IDLE         
166       6006          -             6003            IDLE         
167       6007          -             6003            IDLE         
168       6008          -             6002            IDLE         
169       6009          -             6006            IDLE
```

The following
                              		  table describes the significant fields in the output from this command in
                              		  alphabetical order.

Field

Description

DN

Directory
                                          					 number tag.

DN Number

Extension
                                          					 or telephone number assigned to directory number.

Label

Text
                                          					 string that identifies the whisper intercom line.

Speed
                                          					 Dial

Whisper
                                          					 intercom number to speed dial.

DN State

State of
                                          					 the directory number, either Idle or Busy.

Phone

Ephone
                                          					 that the directory number is assigned to.

### Related Commands

Command

Description

debug ephone whisper-intercom

Displays debugging messages for the Whisper Intercom feature.

show ephone-dn

Displays status and configuration information for phone extensions (ephone-dns)
                                          						in Cisco Unified CME.

whisper-intercom

Enables the Whisper Intercom feature on a directory number.

## show
                        	 ephone-hunt

To display
                              		  ephone-hunt configuration information and current status and statistics
                              		  information, use the show ephone-hunt command in privileged EXEC mode.

show ephone-hunt [ tag | summary ]

### Syntax Description

tag

(Optional) Hunt-group number that was used to identify a hunt group in the ephone-hunt command. Range is 1 to 100.

summary

(Optional) Displays hunt group configuration information.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

The show ephone-hunt and show ephone-hunt summary commands display information for peer, sequential, and
                              		  last-idle ephone hunt groups. Using the tag argument
                              		  outputs data for a specific ephone hunt group.

The output is
                              		  dependent on call activity. If there is no activity, no data is displayed.

## Examples

The following
                              		  examples are contained in this section:

## Examples

The following is
                              		  a sample output from the show ephone-hunt command when no argument or keyword
                              		  has been entered. The sample contains information for a peer hunt group, a
                              		  sequential hunt group, and a longest-idle hunt group. See the table for
                              		  descriptions of significant fields in the output.

```
Router# show ephone-hunt Group 1
    type: peer
    pilot number: 450, peer-tag 20123
    list of numbers:
        451, aux-number A450A0900, # peers 5, logout 0, down 1
            peer-tag  dn-tag  rna  login/logout  up/down
             [20122     42     0       login      up  ]
             [20121     41     0       login      up  ]
             [20120     40     0       login      up  ]
             [20119     30     0       login      up  ]
             [20118     29     0       login      down]
        452, aux-number A450A0901, # peers 4, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20127     45     0       login      up  ]
             [20126     44     0       login      up  ]
             [20125     43     0       login      up  ]
             [20124     31     0       login      up  ]
        453, aux-number A450A0902, # peers 4, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20131     48     0       login      up  ]
             [20130     47     0       login      up  ]
             [20129     46     0       login      up  ]
             [20128     32     0       login      up  ]
        477, aux-number A450A0903, # peers 1, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20132     499    0       login      up  ]
    preference: 0
    members initial state: logout
    preference (sec): 7
    timeout: 3, 3, 3, 3
    max timeout : 10
    hops: 4
    next-to-pick: 1
    E.164 register: yes
    auto logout: no
    stat collect: no
Group 2
    type: sequential
    pilot number: 601, peer-tag 20098
    list of numbers:
        123, aux-number A601A0200, # peers 1, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20097     56     0       login      up  ]
        622, aux-number A601A0201, # peers 3, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20101     112    0       login      up  ]
             [20100     111    0       login      up  ]
             [20099     110    0       login      up  ]
        623, aux-number A601A0202, # peers 3, logout 0, down 0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20104     122    0       login      up  ]
             [20103     121    0       login      up  ]
             [20102     120    0       login      up  ]
        *, aux-number A601A0203, # peers 1, logout 0, down 1
            peer-tag  dn-tag  rna  login/logout  up/down
             [20105     0      0       -          down]
        *, aux-number A601A0204, # peers 1, logout 0, down 1
            peer-tag  dn-tag  rna  login/logout  up/down
             [20106     0      0       -          down]
    final number: 5255348
    preference: 0
    members initial state: logout
    preference (sec): 9
    timeout: 5, 5, 5, 5, 5
    max timeout : 40
    fwd-final: orig-phone
    E.164 register: yes
    auto logout: no
    stat collect: no
Group 3
    type: longest-idle
    pilot number: 100, peer-tag 20142
    list of numbers:
        101, aux-number A100A9700, # peers 3, logout 0, down 3
            on-hook time stamp 7616, off-hook agents=0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20141     132    0       login      down]
             [20140     131    0       login      down]
             [20139     130    0       login      down]
        *, aux-number A100A9701, # peers 1, logout 0, down 1
            on-hook time stamp 7616, off-hook agents=0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20143     0      0       -          down]
        102, aux-number A100A9702, # peers 2, logout 0, down 2
            on-hook time stamp 7616, off-hook agents=0
            peer-tag  dn-tag  rna  login/logout  up/down
             [20145     142    0       login      down]
             [20144     141    0       login      down]
    all agents down!
    preference: 0
    members initial state: logout
    preference (sec): 7
    timeout: 100, 100, 100
    hops: 0
    E.164 register: yes
    auto logout: no
    stat collect: no
```

## Examples

The following
                              		  example shows a summary output. See the table for descriptions of significant
                              		  fields in the output.

```
Router# show ephone-hunt summary Group 1
    type: peer
    pilot number: 5000
    list of numbers:
       5001
       5002
       5003
       5004
       5005
    final number: 5006
    preference: 0
    members initial state: logout
    timeout: 180
    hops: 2
    E.164 register: yes
Group 2
    type: sequential
    pilot number: 6000
    list of numbers:
       5005
       5004
       5003
       5002
       5001
    final number: 5007
    preference: 5
    members initial state: logout
    timeout: 3
    E.164 register: no
```

## Examples

A portion of the show ephone-hunt command output displays the ready and
                              		  not-ready agent status of extensions in hunt groups. An extension that is ready
                              		  is available to receive hunt-group calls. An extension that is in not-ready
                              		  status blocks hunt-group calls. An agent toggles an extension from ready to not
                              		  ready and back to ready using the HLog soft key or a FAC.

The following
                              		  examples display some output that reports different agent status not-ready
                              		  conditions within a hunt group. In the hunt group used for these examples,
                              		  there are four users: agent1 and agent4 share extension 8001, agent2 is on
                              		  extension 8002, and agent3 is on extension 8003.

In the show ephone-hunt output, “logout 0” means that all
                              		  instances of the extension are in ready status. Any number greater than zero
                              		  next to “logout’ indicates that at least one ephone using the extension has
                              		  activated not-ready status.

If agent1 is in
                              		  not-ready status, the show ephone-hunt command will display the following
                              		  output. The logout value for extension 8001 is 1 because one phone is in
                              		  not-ready status.

```
Router# show ephone-hunt .
.
.
list of numbers:
 8001, aux-number A8000A100, # peers 2, logout 1 ...
 8002, aux-number A8000A101, # peers 1, logout 0...
 8003, aux-number A8000A102, # peers 1, logout 0...
.
```

If agent1 and
                              		  agent2 place their phones in not-ready status, the show ephone-hunt command will display the following output:

```
Router# show ephone-hunt .
.
.
list of numbers:
    8001, aux-number A8000A100, # peers 2, logout 1...
    8002, aux-number A8000A101, # peers 1, logout 1...
    8003, aux-number A8000A102, # peers 1, logout 0...
```

If all agents
                              		  place their phones in not-ready status, the show ephone-hunt command displays the following output.
                              		  Note that the logout value of 2 for extension 8001 indicates that both
                              		  ephone-dns with that extension number (agent1 and agent4) are in not-ready
                              		  status.

```
Router# show ephone-hunt .
.
.
list of numbers:
   8001, aux-number A8000A100, # peers 2, logout 2...
   8002, aux-number A8000A101, # peers 1, logout 1...
   8003, aux-number A8000A102, # peers 1, logout 1...
all agents logout!
```

## Examples

The show ephone-hunt command displays the parameters that
                              		  have been set using the auto logout command, which is used for the Automatic
                              		  Agent Status Not-Ready feature. The table shows the possible values of the auto
                              		  logout field. describes other fields in the output.

```
Router# show ephone-hunt 1 Group 1
   type:sequential
   pilot number:8888, peer-tag 20029
   list of numbers:
       8001, aux-number A8888A000, # peers 1, logout 0, down 0
           peer-tag:dn-tag [ 20028:1]
       8003, aux-number A8888A001, # peers 1, logout 0, down 0
           peer-tag:dn-tag [ 20030:3]
   preference:0
   members initial state: logout
   preference (sec):9
   timeout:5
   E.164 register:yes
   auto logout:no
   stat collect:yes
```

show
                                          					 ephone-hunt Output

Description

auto
                                          					 logout Command

```
auto logout: no
```

The
                                          					 Automatic Agent Status Not-Ready feature is disabled. This is also the default
                                          					 if this command is not used.

```
no auto logout
```

```
auto logout: 1 type: both
```

The
                                          					 Automatic Agent Status Not-Ready feature is enabled and no options have been
                                          					 used with the auto logout command. The number of unanswered calls is
                                          					 1 and the command applies to both static and dynamic hunt group members by
                                          					 default.

```
auto logout
```

```
auto logout: 2 type: both
```

Two
                                          					 unanswered calls will be sent to a hunt group agent before the agent’s status
                                          					 is automatically changed to not ready. The command applies to both static and
                                          					 dynamic hunt group members by default.

```
auto logout 2
```

```
auto logout: 3 type: static
```

Three
                                          					 unanswered calls will be sent to a hunt group agent before the agent’s status
                                          					 is automatically changed to not ready. The command applies to static hunt group
                                          					 members only.

```
auto logout 3 static
```

The table
                              		  describes significant fields shown in show ephone-hunt command displays.

Field

Description

auto
                                          					 logout

Indicates whether the Automatic Agent Status Not-Ready feature has been
                                          					 enabled. See the table.

aux-number

Auxiliary number used to generate dial peers for a hunt group. This number is
                                          					 generated by the list command.

description

Description string entered for the ephone hunt group. This value is set using
                                          					 the description (ephone-hunt) command.

dn-tag

Directory number (DN) sequence number.

E.164
                                          					 register

Displays whether a pilot number registers with an H.323 gatekeeper. This value
                                          					 is set by the no-reg command.

final
                                          					 number

Last
                                          					 number in the ephone-hunt group, after which a call is no longer redirected.
                                          					 This value is set by the final command.

fwd-final

Final
                                          					 destination of an unanswered call that has been transferred into a hunt group:
                                          					 orig-phone means calls are returned to the transferring phone, and final means
                                          					 calls are sent to the final number specified in the configuration. This value
                                          					 is set by the fwd-final command.

hops

Number
                                          					 of hops before a call proceeds to the final number. This value is set by the hops command.

list of
                                          					 numbers

Extension numbers that are group members of the specified ephone hunt group.
                                          					 This value is set by the list command.

login/logout

Ready
                                          					 status of the agent: login means ready and accepting calls, and logout means
                                          					 not-ready and blocking hunt-group calls.

logout

Number
                                          					 of agents in the not-ready state (not accepting hunt-group calls).

max
                                          					 timeout

Maximum
                                          					 combined timeout for the no-answer periods for all ephone-dns in the
                                          					 ephone-hunt list. This value is set by the max-timeout command.

members
                                          					 initial state: logout/login

Sets
                                          					 all static members initial state to logout.

next-to-pick

(Peer
                                          					 hunt groups only) List number of the agent whose phone will ring when the next
                                          					 call comes in to the hunt group. (For example, if the order of agents in the list command is 451, 452, 453, 454, the list number 2 represents extension 452.)

off-hook agents

Number
                                          					 of agents who are currently off-hook.

on-hook
                                          					 time stamp

(Longest-idle hunt groups only) The last on-hook time of the agent, which is
                                          					 used to determine which agent to ring next time.

peers

Displays the number of ephone-dn dial peers.

peer-tag

Dial-peer sequence number.

pilot
                                          					 number

Number
                                          					 that callers dial to reach the ephone hunt group.

preference

Preference order set by the preference (ephone-hunt) command for the primary pilot number.

preference (sec)

Preference order set by the preference (ephone-hunt) command for the secondary pilot number.

rna

Number
                                          					 of unanswered hunt group calls (ring-no-answer) by this agent, used for the
                                          					 Automatic Agent Status Not-Ready feature.

stat
                                          					 collect

Indicates whether statistic are being Cisco Unified CME B-ACD data is being
                                          					 collected. See the statistics collect command.

timeout

Number
                                          					 of seconds after which a call that is not answered at one number is redirected
                                          					 to the next number in the hunt-group list. Multiple values in this field refer
                                          					 to the timeouts for the hops between ephone-dns in a hunt group as they appear
                                          					 in the list command. This value is set by the timeout command.

type

Type of
                                          					 ephone hunt group: longest-idle, peer, or sequential.

up/down

Dial
                                          					 peer is up or down.

### Related Commands

Command

Description

auto logout

Enables automatic change of agent status to not-ready after a specified number
                                          						of hunt-group calls are not answered.

ephone-hunt

Enters ephone-hunt configuration mode to create a hunt group for use in a Cisco
                                          						Unified CME system.

hunt-group logout

Enables separate handling of DND and HLog functionality for hunt-group agents
                                          						and the display of an HLog soft key on phones.

members logout

Sets
                                          						all static members initial state to logout.

show
                                          						ephone-hunt statistics

Displays hunt group call statistics.

## show ephone-hunt
                        	 statistics

To display
                              		  ephone-hunt statistics information, use the show ephone-hunt statistics command in privileged EXEC mode.

show ephone-hunt tag statistics { last hours hours | start day time [ to day time ]}

### Syntax Description

tag

Hunt-tag number that was used to identify a hunt group in an ephone-hunt command. Range is 1 to 100.

last

Displays information for the previous number of specified hours, counting
                                          						backward from the current hour. Range is 1 to 167.

hours hours

Number
                                          						of hours for which to display call statistics.

start

Defines
                                          						the start of a period for which to display call statistics. Default duration is
                                          						one hour.

day

Day of
                                          						week. Use sun , mon , tue , wed , thu , fri , or sat .

time

Hour of
                                          						day. Range is 0 to 23.

to

(Optional) Defines the stop time for display of call statistics.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(11)T

Cisco
                                          						CME 3.2

This
                                          						command was introduced.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

Call
                                          						hold statistics were added.

12.4(9)T

Cisco
                                          						Unified CME 4.0

Call
                                          						hold statistics were integrated into Cisco IOS Release 12.4(9)T.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to add the following fields: Calls handoff to IOS, Average
                                          						time to handoff, Longest time to handoff, and Number of error calls.

### Usage Guidelines

The show ephone-hunt statistics last and show ephone-hunt statistics commands provide expanded information regarding
                              		  extension (list of numbers) and pilot numbers.

The output is
                              		  dependent on call activity. If there is no activity, no data is displayed.

If your Cisco
                              		  Unified CME system is configured with the basic automatic call distribution
                              		  (B-ACD) and auto-attendant service, you can enable the collection of call
                              		  statistics per ephone hunt group with the statistics collect command. Additional data is displayed for
                              		  all agents combined and for individual agents. The additional data includes
                              		  statistics such as: the number of calls received, the amount of time the calls
                              		  waited to be answered, and the amount of time the calls spent on hold or in a
                              		  queue.

The statistics collect command can be used to obtain other call
                              		  statistics, such as direct calls to hunt group pilot numbers. For more
                              		  information, see the “ Cisco Unified CME Basic
                                 			 Automatic Call Distribution and Auto-Attendant Service ” chapter in the Cisco Unified
                                 			 CME B-ACD and TCL Call-Handling Applications guide.

Once you have
                              		  enabled statistics collection, you can use the show ephone-hunt statistics command to display call statistics, or you can use the hunt-group report every hours and hunt-group report url commands to transfer the statistics to files
                              		  using TFTP.

## Examples

The following
                              		  is a sample output that displays call statistics for the past hour for hunt
                              		  group 2, which is associated with a Cisco Unified CME B-ACD service:

```
Router# show ephone-hunt 2 stat last 1 h Thu 02:00 - 03:00
    Max Agents: 3
    Min Agents: 3
    Total Calls: 9
    Answered Calls: 7
    Abandoned Calls: 2
    Average Time to Answer (secs): 6
    Longest Time to Answer (secs): 13
    Average Time in Call (secs): 75
    Longest Time in Call (secs): 161
    Average Time before Abandon (secs): 8
    Calls on Hold: 2
    Average Time in Hold (secs): 16
    Longest Time in Hold (secs): 21
    Per agent statistics:
      Agent: 8004
        From Direct Call:
          Total Calls Answered : 3:
          Average Time in Call (secs) : 70
          Longest Time in Call (secs) : 150
          Total Calls on Hold : 1:
          Average Hold Time (secs) : 21
          Longest Hold Time (secs) : 21
        From Queue:
          Total Calls Answered : 3
          Average Time in Call (secs) : 55
          Longest Time in Call (secs) : 78
          Total Calls on Hold : 2:
          Average Hold Time (secs) : 19
          Longest Hold Time (secs) : 26
      Agent: 8006
        From Direct Call:
          Total Calls Answered : 3:
          Average Time in Call (secs) : 51
          Longest Time in Call (secs) : 118
          Total Calls on Hold : 1:
          Average Hold Time (secs) : 11
          Longest Hold Time (secs) : 11
        From Queue:
          Total Calls Answered : 1
          Average Time in Call (secs) : 4
          Longest Time in Call (secs) : 4
      Agent: 8044
        From Direct Call:
          Total Calls Answered : 1:
          Average Time in Call (secs) : 161
          Longest Time in Call (secs) : 161
        From Queue:
          Total Calls Answered : 1
          Average Time in Call (secs) : 658
          Longest Time in Call (secs) : 658
Queue related statistics:
      Total calls presented to the queue:  5
      Calls handoff to IOS: 2
      Number of calls in the queue: 1
      Average time to handoff (secs):  2
      Longest time to handoff (secs):  3
      Number of abandoned calls:  0
      Average time before abandon (secs):  0
      Calls forwarded to voice mail:  0
      Calls answered by voice mail:  0
Number of error calls: 0
```

The following
                              		  is a sample output from the show ephone-hunt statistics command. The output focuses on
                              		  queue-related statistics.

```
Queue related statistics:
      Total calls presented to the queue: 8
      Calls handoff to IOS: 3
Number of calls in the queue: 1
      Average time to handoff (secs): 10
      Longest time to handoff (secs): 15
Number of abandoned calls: 4
      Average time before abandon (secs): 7
      Calls forwarded to voice mail: 0
      Calls answered by voice mail: 0
      Number of error calls: 0
```

The table
                              		  describes the significant fields shown in the output of the show ephone-hunt statistics command, in alphabetical order.

Field

Description

Abandoned calls

Total number of calls abandoned by hunt group agents. This
                                          					 does not include calls going to the final number.

Answered call

Total number of calls answered by hunt group agents.

Average
                                          					 time before abandon (secs)

Average
                                          					 length of time that unanswered calls waited before hanging up.

Average
                                          					 hold time (secs)

Average
                                          					 length of time that calls waited on hold for this agent.

Average
                                          					 time in call (secs)

Average
                                          					 length of time that unanswered calls waited before going to an agent.

Average
                                          					 time in hold (secs)

Average
                                          					 length of time that calls were kept on hold for all agents.

Average
                                          					 time to answer (secs)

Average
                                          					 length of time that all calls to Cisco Unified CME B-ACD waited before being
                                          					 answered.

Average
                                          					 time to handoff (secs)

Average
                                          					 length of time before a call was handed off to IOS.

Calls
                                          					 answered by voice mail

Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by voice mail.

Calls
                                          					 exited the queue

Total
                                          					 number of calls to Cisco Unified CME B-ACD that exited queues.

Calls
                                          					 forwarded to voice mail

Total
                                          					 number of calls to Cisco Unified CME B-ACD that were forwarded to voice mail.

Calls
                                          					 handoff to IOS

Total
                                          					 number of calls handed off to IOS.

Calls
                                          					 on hold

Total
                                          					 number of calls that were placed on hold.

Longest
                                          					 hold time (secs)

Longest
                                          					 length of time that a call to this agent spent between being placed on hold and
                                          					 being picked up.

Longest
                                          					 time in call (secs)

Longest
                                          					 length of time in which calls to Cisco Unified CME B-ACD went to an agent and
                                          					 waited in a call queue.

Longest
                                          					 time in hold (secs)

Longest
                                          					 length of time that a call spent between being placed on hold and being picked
                                          					 up by agents.

Longest
                                          					 time to answer (secs)

Longest
                                          					 length of time before calls to Cisco Unified CME B-ACD were answered.

Longest
                                          					 time to handoff (secs)

Longest
                                          					 length of time before a call was handed off to IOS.

Max
                                          					 agent

Maximum
                                          					 number of hunt group agents.

Min
                                          					 agent

Minimum
                                          					 number of hunt group agents.

Number
                                          					 of abandoned calls:

Total
                                          					 number of calls to Cisco Unified CME B-ACD that hung up before being answered.

Number
                                          					 of error calls

Total
                                          					 number of misdialed calls.

Total
                                          					 calls answered

Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by an agent.

Total
                                          					 calls on hold

Total
                                          					 number of calls that were on hold for this agent.

Total
                                          					 calls presented to the queue

Total
                                          					 number of calls made to Cisco Unified CME B-ACD.

Total calls

Total number of direct calls made to the hunt group.

From Cisco Unified CME Release 10.5 onwards, abandoned calls will
                                          			 not include the calls going to the final number. However, the total calls
                                          			 includes calls going to the final number. Use the formula " Final Calls= Total Calls - Answered Calls - Abandoned Calls " ,
                                          			 to calculate the calls going to the final number.

### Related Commands

Command

Description

ephone-hunt

Enters ephone-hunt configuration mode to create a hunt group for use in a Cisco
                                          						Unified CME system.

hunt-group report every hours

Sets
                                          						the hourly interval at which Cisco Unified CME B-ACD call statistics are
                                          						automatically transferred to a file.

hunt-group report url

Sets
                                          						filename parameters and the URL path where Cisco Unified CME B-ACD call
                                          						statistics are to be sent using TFTP.

statistics collect

Enables the collection of call statistics for an ephone hunt group.

## show
                        	 fb-its-log

To display
                              		  information about the Cisco CallManager Express (Cisco CME) eXtensible Markup
                              		  Language (XML) application program interface (API) configuration, statistics on
                              		  XML API queries, and the XML API event logs, use the show fb-its-log command in privileged EXEC mode.

show fb-its-log [ summary ]

### Syntax Description

summary

(Optional) Displays only the XML API configuration and the statistics for
                                          						queries and logs, and not the logs themselves.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.2(15)ZJ

3.0

This
                                          						command was introduced.

12.3(4)T

3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following is
                              		  sample output from the show fb-its-log summary command:

```
Router# show fb-its-log summary IP Keyswitch Logs:(21:11:30 UTC Wed Jul 1 2003)
  ---- Current Period ---
    extension events:4
    device events: 3
    overwrites:0
    missed:0
    deleted:0
 ---- History ------
    overwrites:0
    missed:0
    deleted:8
---- Threads ----
    max xml threads:2
    current thread:0
    read in process:FALSE
```

The following is
                              		  sample output from the show fb-its-log command:

```
Router# show fb-its-log IP Keyswitch Logs:(21:11:30 UTC Wed Jul 1 2003)
  ---- Current Period ---
    extension events:4
    device events: 3
    overwrites:0
    missed:0
    deleted:0
 ---- History ------
    overwrites:0
    missed:0
    deleted:8
---- Threads ----
    max xml threads:2
    cuttent thread:0
    read in process:FALSE
1  Time:21:11:06 UTC Wed Jul 1 2003
    Event:DN 1[2001] goes down
2  Time:21:11:06 UTC Wed Jul 1 2003
    Event:DN 2[2003] goes down
3  Time:21:11:06 UTC Wed Jul 1 2003
    Event:IP Phone 1[SEP003094C3F96A] unregistered
4  Time:21:11:06 UTC Wed Jul 1 2003
    Event:IP Phone 1[SEP003094C3F96A] unregistered
5  Time:21:11:54 UTC Wed Jul 2003
    Event:IP Phone 1[SEP003094C3F96A] registered
6  Time:21:11:57 UTC Wed Jul 2003
    Event:DN 1[2001] goes up
7  Time:21:11:57 UTC Wed Jul 2003
    Event:DN 2[2003] goes up
```

The following
                              		  table describes the significant fields in this output.

Field

Description

Current
                                          					 Period

The time
                                          					 between the last retain-timer-triggered cleanup to the next cleanup.

extension
                                          					 events

Events
                                          					 related to extensions that have been captured in the internal buffer.

device
                                          					 events

Events
                                          					 related to devices that have been captured in the internal buffer.

overwrites

Events
                                          					 that are written over previously recorded events in the buffer. Overwrites
                                          					 occur when the internal buffer size is too small; new events overwrite old
                                          					 ones. The internal buffer size is set using the max-size keyword in the log table command.

missed

Events
                                          					 that happen too quickly for the system to record.

deleted

Events
                                          					 removed from the internal buffer.

History

Information since the last system restart.

Threads

Current
                                          					 number of threads configured in the system.

max xml
                                          					 threads

Maximum
                                          					 number of concurrent XML threads allowed.

current
                                          					 thread

XML API
                                          					 query thread.

read in
                                          					 process

TRUE
                                          					 indicates that the xml-test.html file is being read now. FALSE indicates that
                                          					 the file is not being read.

UTC

Coordinated Universal Time, which is used by the system clock on the Cisco CME
                                          					 router.

### Related Commands

Command

Description

log table

Sets
                                          						the maximum size of the table used to capture phone events used for the Cisco
                                          						CME XML API.

## show ip address trusted list

To display a list of trusted ip addresses, use the show ip address trusted list command in privileged EXEC mode.

show ip address trusted list

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to display a list of trusted IP addresses.

## Examples

The following is a sample output from this command displaying all
                              		  statistical information:

```
Router #show ip address trusted list
IP Address Trusted Authentication
 Administration State: UP
 Operation State:      UP
IP Address Trusted Call Block Cause: call-reject (21)
VoIP Dial-peer IPv4 Session Targets:
Peer Tag        Oper State      Session Target
--------        ----------      --------------
11              DOWN            ipv4:1.3.45.1
1               UP              ipv4:1.3.45.1
IP Address Trusted List:
 ipv4 172.19.245.1
 ipv4 172.19.247.1
 ipv4 172.19.243.1
 ipv4 171.19.245.1
 ipv4 171.19.10.1
```

### Related Commands

Command

Description

ip address trusted list

Allows to add a list of trusted IP addresses.

## show presence
                        	 global

To display
                              		  configuration information about the presence service, use the show presence global command in user EXEC or privileged EXEC
                              		  mode.

show presence global

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(11)XJ

This
                                          						command was introduced.

12.4(15)T

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command
                              		  displays the configuration settings for presence.

## Examples

The following
                              		  example displays output from the show subscription global :

```
Router# show subscription global Presence Global Configuration Information:
=============================================
Presence feature enable            : TRUE
Presence allow external watchers   : FALSE
Presence max subscription allowed  : 100
Presence number of subscriptions   : 0
Presence allow external subscribe  : FALSE
Presence call list enable          : TRUE
Presence server IP address         : 0.0.0.0
Presence sccp blfsd retry interval : 60
Presence sccp blfsd retry limit    : 10
Presence router mode               : CME mode
```

The table
                              		  describes the significant fields shown in the display.

Field

Description

Presence
                                          					 feature enable

Indicates
                                          					 whether presence is enabled on the router with the presence command.

Presence
                                          					 allow external watchers

Indicates
                                          					 whether internal presentities can be watched by external watchers, as set by
                                          					 the watcher all

Presence
                                          					 max subscription allowed

Maximum
                                          					 number of presence subscriptions allowed by the max-subscription command.

Presence
                                          					 number of subscriptions

Current
                                          					 number of active presence subscriptions.

Presence
                                          					 allow external subscribe

Indicates
                                          					 whether internal watchers are allowed to subscribe to status notifications from
                                          					 external presentities, as set by the allow subscribe command.

Presence
                                          					 call list enable

Indicates
                                          					 whether the Busy Lamp Field (BLF) call-list feature is enabled with the presence call-list command.

Presence
                                          					 server IP address

Displays
                                          					 the IP address of an external presence server defined with the server command.

Presence
                                          					 sccp blfsd retry interval

Retry
                                          					 timeout, in seconds, for BLF speed-dial numbers on SCCP phones set by the sccp blf-speed-dial retry interval command.

Presence sccp blfsd retry limit

Maximum
                                          					 number of retries allowed for BLF speed-dial numbers on SCCP phones set by the sccp blf-speed-dial retry interval command.

Presence router mode

Indicates whether the configuration mode is set to Cisco Unified CME or Cisco
                                          					 Unified SRST by the mode command.

### Related Commands

Command

Description

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be
                                          						watched in a presence service.

allow subscribe

Allows internal watchers to monitor external presence entities (directory
                                          						numbers).

debug presence

Displays debugging information about the presence service.

presence enable

Allows the router to accept incoming presence requests.

server

Specifies the IP address of a presence server for sending presence requests
                                          						from internal watchers to external presence entities.

show presence subscription

Displays information about active presence subscriptions.

watcher all

Allows external watchers to monitor internal presence entities (directory
                                          						numbers).

## show presence
                        	 subscription

To display
                              		  information about active presence subscriptions, use the show presence subscription command in user EXEC or privileged
                              		  EXEC mode.

show presence subscription [ details | presentity telephone-number | subid subscription-id | summary ]

### Syntax Description

details

(Optional) Displays detailed information about presentities, watchers, and
                                          						presence subscriptions.

presentity telephone-number

(Optional) Displays information on the presentity specified by the destination
                                          						telephone number.

subid subscription-id

(Optional) Displays information for the specific subscription ID.

summary

(Optional) Displays summary information about active subscription requests.

### Command Default

Information for
                              		  all active presence subscriptions is displayed.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(11)XJ

This
                                          						command was introduced.

12.4(15)T

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

12.4(24)T

This
                                          						command was integrated into Cisco IOS Release 12.4(24)T.

### Usage Guidelines

This command
                              		  displays details about the currently active presence subscriptions

## Examples

The following is
                              		  sample output from the show presence subscription details command:

```
Presence Active Subscription Records Details:
=============================================
 
Subscription ID         : 1
  Watcher               : 6002@10.4.171.60
  Presentity            : 6005@10.4.171.34
  Expires               : 3600 seconds
  Subscription Duration : 1751 seconds
  line status           : idle 
  watcher type          : local 
  presentity type       : local 
  Watcher phone type    : SIP Phone
  subscription type     : Incoming Indication
  retry limit           : 0
  sibling subID         : 0
  sdb                   : 0
  dp                    : 6555346C
  watcher dial peer tag : 40001
  number of presentity  : 1
 
Subscription ID         : 2
  Watcher               : 6002@10.4.171.60
 
Presence Active Subscription Records:
=============================================
 
Subscription ID         : 30
  Watcher               : 4085550103@10.4.171.34
  Presentity            : 5001@10.4.171.20
  Expires               : 3600 seconds
  line status           : idle 
  watcher type          : local 
  presentity type       : remote 
  Watcher phone type    : SCCP [BLF Call List]
  subscription type     : Outgoing Request
  retry limit           : 0
  sibling subID         : 23
  sdb                   : 0
  dp                    : 0
  watcher dial peer tag : 0
```

The following is
                              		  sample output from the show presence subscription summary command:

```
Router# show presence subscription summary Presence Active Subscription Records Summary: 15 subscription
Watcher                  Presentity               SubID  Expires SibID  Status
======================== ======================== ====== ======= ====== ======
6002@10.4.171.60         6005@10.4.171.34          1     3600    0      idle
6005@10.4.171.81         6002@10.4.171.34          6     3600    0      idle
6005@10.4.171.81         6003@10.4.171.34          8     3600    0      idle
6005@10.4.171.81         6002@10.4.171.34          9     3600    0      idle
6005@10.4.171.81         6003@10.4.171.34          10    3600    0      idle
6005@10.4.171.81         6001@10.4.171.34          12    3600    0      idle
6001@10.4.171.61         6003@10.4.171.34          15    3600    0      idle 
6001@10.4.171.61         6002@10.4.171.34          17    3600    0      idle 
6003@10.4.171.59         6003@10.4.171.34          19    3600    0      idle 
6003@10.4.171.59         6002@10.4.171.34          21    3600    0      idle 
6003@10.4.171.59         5001@10.4.171.34          23    3600    24     idle 
6002@10.4.171.60         6003@10.4.171.34          121   3600    0      idle 
6002@10.4.171.60         5002@10.4.171.34          128   3600    129    idle 
6005@10.4.171.81         1001@10.4.171.34          130   3600    131    busy 
6005@10.4.171.81         7005@10.4.171.34          132   3600    133    idle
```

The following is
                              		  sample output from the show presence subscription summary command showing that device-based BLF
                              		  monitoring is enabled on two phones.

```
Watcher                    Presentity               SubID  Expires SibID  Status
========================== ======================== ====== ======= ====== ======
D 2036@10.6.2.6            2038@10.6.2.254          33     3600    0      idle                     
  2036@10.6.2.6            2038@10.6.2.254          35     3600    0      idle                     
D 2036@10.6.2.6            8883@10.6.2.254          37     3600    0      unknown
```

The following
                              		  is sample output from the show presence subscription subid command:

```
Router# show presence subscription subid 133 Presence Active Subscription Records:
=============================================
 
Subscription ID         : 133
  Watcher               : 6005@10.4.171.34
  Presentity            : 7005@10.4.171.20
  Expires               : 3600 seconds
  line status           : idle 
  watcher type          : local 
  presentity type       : remote 
  Watcher phone type    : SIP Phone
  subscription type     : Outgoing Request
  retry limit           : 0
  sibling subID         : 132
  sdb                   : 0
  dp                    : 0
  watcher dial peer tag : 0
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

Watcher

IP
                                          					 address of the watcher.

Presentity

IP
                                          					 address of the presentity.

Expires

Number
                                          					 of seconds until the subscription expires. Default is 3600.

line
                                          					 status

Status
                                          					 of the line:

- Idle—Line is not being used.

- In-use—User is on the line, whether or not this line can accept a new call.

- Unknown—Phone is unregistered or this line is not allowed to be watched.

watcher
                                          					 type

Whether
                                          					 the watcher is local or remote.

presentity type

Whether
                                          					 the presentity is local or remote.

Watcher
                                          					 phone type

Type of
                                          					 phone, either SCCP or SIP.

subscription type

The
                                          					 type of presence subscription, either incoming or outgoing.

retry
                                          					 limit

Maximum
                                          					 number of times the router attempts to subscribe for the line status of an
                                          					 external SCCP phone when either the presentity does not exist or the router
                                          					 receives a terminated NOTIFY from the external presence server. Set with the sccp blf-speed-dial retry-interval command.

sibling
                                          					 subID

Sibling
                                          					 subscription ID if presentity is remote. If value is 0, presentity is local.

sdb

Voice
                                          					 port of the presentity.

dp

Dial
                                          					 peer of the presentity.

watcher
                                          					 dial peer tag

Dial
                                          					 peer tag of the watcher device.

### Related Commands

Command

Description

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be
                                          						watched in a presence service.

blf-speed-dial

Enables BLF monitoring for a speed-dial number on a phone registered to Cisco
                                          						Unified CME.

debug ephone blf

Displays debugging information for BLF presence features.

debug presence

Displays debugging information about the presence service.

presence

Enables presence service and enters presence configuration mode.

presence enable

Allows the router to accept incoming presence requests.

show presence global

Displays configuration information about the presence service.

## show
                        	 sdspfarm

To display the
                              		  status of the configured digital signal processor (DSP) farms and transcoding
                              		  streams, use the show sdspfarm command in privileged EXEC mode.

show sdspfarm { units | sessions { active | callID number | statistics | summary }}

### Syntax Description

units

Displays the configured and registered DSP farms.

sessions

Displays the transcoding streams.

active

Displays all active sessions.

callID

Displays activities for a specific caller ID.

number

Displays caller ID number displayed by the show voip rtp connection command.

statistics

Displays session statistics.

summary

Displays summary information.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Products

Modification

12.3(11)T

Cisco
                                          						CME 3.2

This
                                          						command was introduced.

## Examples

The following is
                              		  sample output from the show sdspfarm units :

```
Router# show sdspfarm units mtp-1 Device:MTP123456782012 TCP socket:[-1]  UNREGISTERED
actual_stream:0 max_stream 0 IP:0.0.0.0  0  Unknown 0 keepalive 0  
mtp-2 Device:MTP000a8aeaca80 TCP socket:[5]  REGISTERED
actual_stream:40 max_stream 40 IP:10.5.49.160  11001  MTP YOKO keepalive 12074  
Supported codec:G711Ulaw
                 G711Alaw
                 G729
                 G729a
                 G729b
                 G729ab
 max-mtps:2, max-streams:240, alloc-streams:40, act-streams:0
The following is sample output from the show sdspfarm sessions active :
Router# show sdspfarm sessions active Stream-ID:3 mtp:2 1.5.49.160  20174  Local:2000 START  
 usage:MoH  (DN=3  , CH=1) FE=TRUE  
 codec:G729  duration:20 vad:0 peer Stream-ID:4 
Stream-ID:4 mtp:2 1.5.49.160  17072  Local:2000 START  
 usage:MoH  (DN=3  , CH=1) FE=FALSE 
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:3
```

The following is
                              		  sample output from the show sdspfarm sessions callID :

```
Router# show sdspfarm sessions callid 51M Stream-ID:6, srcCall-ID:51, codec:G729AnnexA , dur:20ms, vad:0, dstCall-ID:52, confID:5, mtp:2^
Peer Stream-ID:5, srcCall-ID:52, codec:G711Ulaw64k , dur:20ms, vad:0, dstCall-ID:51, confID:5, mtp:2^
Router-2015# show sdspfarm sessions callid 52
Stream-ID:5, srcCall-ID:52, codec:G711Ulaw64k , dur:20ms, vad:0, dstCall-ID:51, confID:5, mtp:2
Peer Stream-ID:6, srcCall-ID:51, codec:G729AnnexA , dur:20ms, vad:0, dstCall-ID:52, confID:5, mtp:2
```

The following
                              		  is sample output from the show sdspfarm sessions statistics :

```
Router# show sdspfarm sessions statistics Stream-ID:1 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:1014 in-pak:0 discard:0
Stream-ID:2 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:3 mtp:2 10.5.49.160  20174  Local:2000START  MoH  (DN=3  , CH=1) FE=TRUE  
 codec:G729  duration:20 vad:0 peer Stream-ID:4 
 recv-pak:0 xmit-pak:0 out-pak:4780 in-pak:0 discard:0
Stream-ID:4 mtp:2 10.5.49.160  17072  Local:2000START  MoH  (DN=3  , CH=1) FE=FALSE 
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:3 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:5 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:6 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:7 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:8 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:9 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:10 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:11 mtp:2 0.0.0.0  0  Local:0IDLE                               
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:12 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:13 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:14 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:15 mtp:2 0.0.0.0  0  Local:0IDLE         
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:16 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:17 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:18 mtp:2 0.0.0.0  0  Local:0IDLE         
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:19 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:20 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:21 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:22 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:23 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:24 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:25 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:26 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:27 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:28 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:29 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:30 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:31 mtp:2 0.0.0.0  0  Local:0IDLE                                
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:32 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:33 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:34 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:35 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:36 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:37 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:38 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:39 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
Stream-ID:40 mtp:2 0.0.0.0  0  Local:0IDLE        
 codec:G711Ulaw64k  duration:20 vad:0 peer Stream-ID:0 
 recv-pak:0 xmit-pak:0 out-pak:0 in-pak:0 discard:0
```

The following
                              		  is sample output from the show sdspfarm sessions summary :

```
Router# show sdspfarm sessions summary max-mtps:2, max-streams:240, alloc-streams:40, act-streams:2
  ID   MTP  State      CallID confID Usage                         Codec/Duration
==== ===== ====== =========== ====== ============================= ==============
1    2     IDLE   -1          0                                   G711Ulaw64k /20ms
2    2     IDLE   -1          0                                   G711Ulaw64k /20ms
3    2     START  -1          3      MoH  (DN=3  , CH=1) FE=TRUE  G729 /20ms
4    2     START  -1          3      MoH  (DN=3  , CH=1) FE=FALSE G711Ulaw64k /20ms
5    2     IDLE   -1          0                                   G711Ulaw64k /20ms
6    2     IDLE   -1          0                                   G711Ulaw64k /20ms
7    2     IDLE   -1          0                                   G711Ulaw64k /20ms
8    2     IDLE   -1          0                                   G711Ulaw64k /20ms
9    2     IDLE   -1          0                                   G711Ulaw64k /20ms
10   2     IDLE   -1          0                                   G711Ulaw64k /20ms
11   2     IDLE   -1          0                                   G711Ulaw64k /20ms
12   2     IDLE   -1          0                                   G711Ulaw64k /20ms
13   2     IDLE   -1          0                                   G711Ulaw64k /20ms
14   2     IDLE   -1          0                                   G711Ulaw64k /20ms
15   2     IDLE   -1          0                                   G711Ulaw64k /20ms
16   2     IDLE   -1          0                                   G711Ulaw64k /20ms
17   2     IDLE   -1          0                                   G711Ulaw64k /20ms
18   2     IDLE   -1          0                                   G711Ulaw64k /20ms
19   2     IDLE   -1          0                                   G711Ulaw64k /20ms
20   2     IDLE   -1          0                                   G711Ulaw64k /20ms
21   2     IDLE   -1          0                                   G711Ulaw64k /20ms
22   2     IDLE   -1          0                                   G711Ulaw64k /20ms
23   2     IDLE   -1          0                                   G711Ulaw64k /20ms
24   2     IDLE   -1          0                                   G711Ulaw64k /20ms
25   2     IDLE   -1          0                                   G711Ulaw64k /20ms
26   2     IDLE   -1          0                                   G711Ulaw64k /20ms
27   2     IDLE   -1          0                                   G711Ulaw64k /20ms
28   2     IDLE   -1          0                                   G711Ulaw64k /20ms
29   2     IDLE   -1          0                                   G711Ulaw64k /20ms
30   2     IDLE   -1          0                                   G711Ulaw64k /20ms
31   2     IDLE   -1          0                                   G711Ulaw64k /20ms
32   2     IDLE   -1          0                                   G711Ulaw64k /20ms
33   2     IDLE   -1          0                                   G711Ulaw64k /20ms
34   2     IDLE   -1          0                                   G711Ulaw64k /20ms
35   2     IDLE   -1          0                                   G711Ulaw64k /20ms
36   2     IDLE   -1          0                                   G711Ulaw64k /20ms
37   2     IDLE   -1          0                                   G711Ulaw64k /20ms
38   2     IDLE   -1          0                                   G711Ulaw64k /20ms
39   2     IDLE   -1          0                                   G711Ulaw64k /20ms
40   2     IDLE   -1          0                                   G711Ulaw64k /20ms
```

The following
                              		  table describes the fields shown in the show sdspfarm display.

Field

Description

act-streams

Active
                                          					 streams that are currently involved in calls.

alloc-streams

Number
                                          					 of transcoding streams that are actually allocated to all DSP farms that are
                                          					 registered to Cisco CME.

callID

Caller
                                          					 ID that the active stream is in.

Codec

Codec
                                          					 in use.

confID

ConfID
                                          					 that is used to communicate with DSP farms.

discard

Number
                                          					 of packets that are discarded.

dstCall-ID

Caller
                                          					 ID of the destination IP call leg.

Duration or dur

Packet
                                          					 rates, in milliseconds.

ID

Transcoding stream sequence number in Cisco CME.

in-pak

Number
                                          					 of incoming packets from the source call leg.

Local

Local
                                          					 port for voice packets.

max-mtps

Maximum
                                          					 number of Message Transfer Parts (MTPs) that are currently allowed to register
                                          					 in Cisco CME.

max-streams

Maximum
                                          					 number of transcoding streams that are currently allowed in Cisco CME.

mtp or
                                          					 MTP

MTP
                                          					 sequence number where the transcoding stream is located.

out-pak

Number
                                          					 of outgoing packets sending to source call leg.

peer
                                          					 Stream-ID

Stream
                                          					 sequence number of the other stream paired in the same transcoding session.
                                          					 (Two transcoding streams make up a transcoding session).

recv-pak

Number
                                          					 of voice packets received from DSP farm.

srcCall-ID

Source
                                          					 caller ID of the source IP call leg.

State

Current
                                          					 state of the transcoding stream, could be IDLE, SEIZE, START, STOP, or END.

Stream-ID

Transcoding stream sequence number in Cisco CME.

TCP-socket

Socket
                                          					 number for DSP farm (similar to TCP socket for show ephone output).

usage

Current
                                          					 usage of the stream; for example, Ip-Ip (IP to IP transcoding), MOH (for MOH
                                          					 transcoding) and Conf (conference).

vad

Voice-activity detection (VAD) flag for the transcoding stream. It should
                                          					 always be 0 (False).

xmit-pak

Number
                                          					 of packets that are sent to DSP farm.

### Related Commands

Command

Description

sdspfarm tag

Permits a DSP farm to be to registered to Cisco CME and be associated with an
                                          						SCCP client interface’s MAC address.

sdspfarm transcode sessions

Specifies the maximum number of transcoding sessions allowed per Cisco CME
                                          						router.

sdspfarm units

Specifies the maximum number of DSP farms that are allowed to be registered to
                                          						Cisco CME.

## show
                        	 shared-line

To display
                              		  information about the Session Initiation Protocol (SIP) shared lines, use the show shared-line command in user EXEC or privileged
                              		  EXEC mode.

show shared-line { call | details | subscription | summary }

### Syntax Description

call

Displays information about all active calls on shared lines.

details

Displays detailed information about each shared line.

subscription

Displays information for specific subscriptions to shared lines.

summary

Displays summary information about active subscriptions to shared lines.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(24)T

This
                                          						command was introduced.

## Examples

The following is
                              		  sample output from the show shared-line call command:

```
Router# show shared-line call Shared-Line active call info:
Shared-Line: '20141',  active calls: 3
Local User       Local Address                Remote User       Remote Address 	 CallID
==========       =====================        ===========       ===================== ====
20141            20141@10.6.0.2                20143             20143@10.10.0.1 	3168
 
20141            20141@10.6.0.1                Barge             20143@10.10.0.1 	3209
 
20141            20141@10.6.0.2                20141             20141@10.10.0.1 	3210
```

The following is
                              		  sample output from the show shared-line details command:

```
Router# show shared-line details Shared-Line info details:
 
Shared-Line: '20141',  subscribed users: 2,  max calls limit: 10
Index        Users                  sub_id         peer_tag        Status
=====        =====                  ======         ========        ======
  1          20141@10.6.0.1             5            40001           ACTIVE
  2          20141@10.6.0.2             6            40002           ACTIVE
Free call queue size: 7,   Active call queue size: 3
 
Message queue size: 20,   Event queue size: 64
```

The following is
                              		  sample output from the show shared-line subscription command:

```
Router# show shared-line subscription Shared-Line Subscription Info:
 
Subscriptions to: '20141',   total subscriptions: 2
SubID        Subscriber                   Expires         Sub-Status
=====        ==========                   =======         ==========
  5          20141@10.6.0.1                  3600          NOTIFY_ACKED
  6          20141@10.6.0.2                  3600          NOTIFY_ACKED
```

The following is
                              		  sample output from the show shared-line summary command:

```
Router# show shared-line summary Shared-Line info summary:
Shared-Line: '20141',  subscribed users: 2,  max calls limit: 10
```

The following
                              		  table describes the significant fields shown in the displays.

Field

Description

Expires

Number
                                          					 of seconds until the subscription expires.

Local
                                          					 Address

IP
                                          					 address of the local phone involved in the shared line call.

Local
                                          					 User

Extension number of the shared line.

Remote
                                          					 Address

IP
                                          					 address of the remote phone involved in the shared line call.

Remote
                                          					 User

Extension of the remote phone involved in the shared line call.

SubID

Subscription ID.

Subscriber

Extension number of the shared line and the IP address of the phone subscriber.

Sub-Status

Status
                                          					 of the subscription.

Users

IP
                                          					 addresses of the phones using the shared line.

### Related Commands

Command

Description

debug shared-line

Displays debugging information about SIP shared lines.

## show
                        	 telephony-service admin

To display
                              		  information about the Cisco CallManager Express (Cisco CME) system
                              		  administrator, use the show telephony-service admin command in user EXEC or privileged EXEC
                              		  mode.

show telephony-service admin

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.2(2)XT

2.0

This
                                          						command was introduced.

12.2(8)T

2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service admin admin_username Admin
admin_password word
edit DN through Web: enabled.
edit TIME through Web: enabled.
```

The following
                              		  table describes the significant fields in this output.

Field

Description

admin_username

Username
                                          					 of system administrator.

admin_password

Password
                                          					 of system administrator.

edit DN
                                          					 through Web

Whether
                                          					 editing of extensions through the GUI has been enabled using the dn-webedit command.

edit TIME
                                          					 through Web

Whether
                                          					 changing the router time through the GUI has been enabled using the time-webedit command.

### Related Commands

Command

Description

dn-webedit

Enables
                                          						adding of extensions (ephone-dns) through the web interface.

time-webedit

Enables
                                          						setting of time through the web interface.

## show
                        	 telephony-service all

To display
                              		  detailed configuration for phones, voice ports, and dial peers in a Cisco
                              		  Unified Communications Manager Express (Cisco Unified CME) system, use the show telephony-service all command in user EXEC or privileged EXEC mode.

show telephony-service all

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.1(5)YD

Cisco
                                          						Unified CME 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						Unified CME 2.0

This
                                          						command was integrated int Cisco IOS Release 12.2(8)T.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to display the total number of data collected from both
                                          						ephone and voice hunt groups.

### Usage Guidelines

Use the show telephony-service all command to display the total number of ephone and voice hunt
                              		  groups that have statistics collection turned on.

## Examples

The following is
                              		  a sample output from the show telephony-service all command:

```
Router# show telephony-service all CONFIG
======
ip source-address 10.0.0.1 port 2000
max-ephones 24
max-dn 24
dialplan-pattern 1 408734....
voicemail 11111
transfer-pattern 510734....
keepalive 30
ephone-dn 1
number 5001
huntstop
ephone-dn 2
number 5002
huntstop
call-forward noan 5001 timeout 8
ephone-dn 3
number 5003
huntstop
ephone 1
mac-address 0030.94C3.37CB
type 0
button  1:1
speed-dial 1 5002
speed-dial 2 5003
cos 0
!
ephone 2
mac-address 0030.94C3.F96A
type 0
button  1:2 2:3 3:4
speed-dial 1 5004
speed-dial 2 5001
cos 0
!
voice-port 50/0/1
 station-id number 5001
!
voice-port 50/0/2
 station-id number 5002
 timeout ringing 8
!
dial-peer voice 20025 pots
 destination-pattern 5001
 huntstop
 port 50/0/1
dial-peer voice 20026 pots
 destination-pattern 5002
 huntstop
 call-forward noan 5001
 port 50/0/2
dial-peer voice 20027 pots
 destination-pattern 5003
 huntstop
 port 50/0/3
```

The following is
                              		  a sample output from the show telephony-service all command. The output shows that call statistics
                              		  are collected for 14 hunt groups, including 6 ephone and 8 voice hunt groups.

```
Router# show telephony-service all CONFIG (Version=8.7)
=====================
Version 8.7
Max phoneload sccp version 17
Max dspfarm sccp version 18
Cisco Unified Communications Manager Express
For on-line documentation please see:
http://www.cisco.com/en/US/products/sw/voicesw/ps4625/tsd_products_support_series_home.html
protocol mode default
ip source-address 1.4.190.80 port 2000
ip qos dscp:
 ef (the MS 6 bits, 46, in ToS, 0xB8) for media
 cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
 af41 (the MS 6 bits, 34, in ToS, 0x88) for video
 default (the MS 6 bits, 0, in ToS, 0x0) for serviceservice directed-pickup
load 6921 SCCP69xx.9-0-3-0
load 6961 SCCP69xx.8-5-3-0
max-ephones 14
max-dn 56
max-conferences 4 gain -6
dspfarm units 0
dspfarm transcode sessions 0
conference software
privacy
no privacy-on-hold
hunt-group report url prefix tftp://223.255.254.254/ngm/huntgp/uc500/test
hunt-group report url suffix 0 to 20
hunt-group report every 1 hours
# of hunt-group collect data: 14
hunt-group report delay 0 hours
Number of ephone hunt-group configured: 6
hunt-group logout DND
max-redirect 20
cnf-file location: system:
cnf-file option: PER-PHONE-TYPE
```

The following is
                              		  another sample output from the show telephony-service all command. The output shows that call statistics
                              		  are collected for seven hunt groups, including three ephone and four voice hunt
                              		  groups.

```
Router# show telephony-service all .
.
.
.
.
hunt-group report url prefix tftp://223.255.254.254/ngm/huntgp/uc500/test
hunt-group report url suffix 0 to 20
hunt-group report every 1 hours
# of hunt-group collect data: 7
hunt-group report delay 0 hours
Number of ephone hunt-group configured: 3
.
.
.
.
.
```

The following
                              		  table describes significant fields in this output, in alphabetical order.

Field

Description

button

Button on
                                          					 the Cisco IP phone.

call-forward noan

Call
                                          					 forward no answer is set.

cnf-file
                                          					 location

Storage
                                          					 location for phone configuration files. System (default), flash or slot 0
                                          					 memory, and external TFTP server.

cnf-file option

Specifies the use of different phone configuration files by type of phone or by
                                          					 individual phone.

cos

Not
                                          					 applicable; unused.

destination-pattern

Destination pattern (telephone number) configured for this dial peer.

dial-peer voice

Voice
                                          					 dial peer.

dialplan-pattern

Dial-plan pattern is set to expand the abbreviated extension numbers to fully
                                          					 qualified E.164 numbers.

ephone

Cisco
                                          					 IP phone.

ephone-dn

Cisco
                                          					 IP phone directory number.

huntstop

Huntstop is set.

ip
                                          					 source-address

IP
                                          					 address used by Cisco IP phones to register with the router for service.

keepalive

IP
                                          					 phone keepalive period, in seconds.

mac-address

MAC
                                          					 address.

max-dn

Maximum
                                          					 directory numbers.

max-ephones

Maximum
                                          					 numbers of Cisco IP phones.

number

Cisco
                                          					 IP phone number.

port

TCP
                                          					 port number used by Cisco IP phones to communicate with the router.

pots

POTS
                                          					 dial peer set.

speed-dial

Speed-dial is set.

station-id number

Number
                                          					 used for caller ID purposes when calls are made using the line.

timeout

Timeout
                                          					 is set.

timeout
                                          					 ringing

Maximum
                                          					 amount of time that the phone is allowed to ring before the call is
                                          					 disconnected.

transfer-pattern

Transfer pattern is set to allow transfer of calls to a specified number.

type

Not
                                          					 applicable; unused.

voicemail

A
                                          					 voice-mail (speed-dial) number is set.

voice-port

(Virtual) voice port designator.

# of
                                          					 hunt-group collect data

Total
                                          					 number of data collected from both ephone and voice hunt groups.

### Related Commands

Command

Description

show telephony dial - peer

Displays dial peers for extensions in a Cisco Unified CME system.

show telephony voice - port

Displays virtual voice-port configuration for extensions in a Cisco Unified CME
                                          						system.

## show
                        	 telephony-service bulk-speed-dial

To display
                              		  information about bulk speed-dial lists, use the show telephony-service bulk-speed-dial command in privileged EXEC mode.

show telephony-service bulk-speed-dial { global list-id index-id [ all ] | local phone-tag list-id index-id [ all ] | summary }

### Syntax Description

global

Global
                                          						lists that can be accessed by all users.

local

Personal lists that can be accessed by users configured to use the lists.

list-id

Digit
                                          						that identifies the list. Range is from 0 to 9.

index-id

Identification number for an entry.

phone-tag

Ephone
                                          						identifier (phone-tag).

summary

List of
                                          						registered bulk speed-dial text files.

### Command Modes

Privileged EXEC

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

## Examples

The following
                              		  example displays the list of bulk speed-dial text files that have been
                              		  configured in the system:

```
Router# show telephony-service bulk-speed-dial summary List-id    Entries      Size    Reference  url
      0         40      3840    Global     tftp://192.168.254.254/phonedirs/uut.csv
      1         20      1920    Global     phoneBook.csv
      8         15      1440    Global     tftp://192.168.254.254/phonedirs/big.txt
      9         20      1920    Global     tftp://192.168.254.254/phonedirs/phoneBook.csv
      6      24879   2388384    ephone-2   tftp://192.168.254.254/phonedirs/big.txt1
      7         20      1920    ephone-2   phoneBook.csv
      6      24879   2388384    ephone-3   big.txt1
      7         20      1920    ephone-3   phoneBook.csv
4 Global List(s) 4 Local List(s)
```

The following
                              		  example displays the single entry 1234 from list 9:

```
Router# show telephony-service bulk-speed-dial global 9 1234 Number: 1800 200 1345 name: Jay Smith Private: yes Extension: No
```

The following
                              		  example displays all index entries starting with 1 for personal list number 7
                              		  for ephone 2:

```
Router# show telephony-service bulk-speed-dial local 2 7 1 all Index  Number                  Name                 Hide    Append
    1000   918005550164            ABC Co Front Desk      no     no 
    1003   919005550167            ABC Co File room       no     no 
    1100   918005550118                                   no     no 
    1200   918005550184            ABC Co President       no     no 
    1301   918005550152                                   no     no 
    1342   91800,5550185           ABC Co Sales           no     no 
    1682   91800555,,0115          ABC Co Service         no     no
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

List-id

Digit
                                          					 that identifies the list. Range is from 0 to 9.

Entries

Number
                                          					 of entries in the speed-dial file.

Size

Size of
                                          					 the file, in KB.

Reference

Assignment of the list: global if assigned to all ephones, or a specific ephone
                                          					 number.

url

Location of the text file, in URL format.

Index

Identification number for an entry.

Number

Number
                                          					 to be dialed and displayed on the phone.

Name

Name to
                                          					 be displayed on the phone.

Hide

Yes
                                          					 indicates that this number should not be displayed when it is dialed.

Append

Yes
                                          					 indicates that additional digits can be dialed by the user after this number
                                          					 has been speed-dialed before the call is completed.

### Related Commands

Command

Description

bulk-speed-dial list (ephone)

Enables a personal bulk speed-dial list for an ephone.

bulk-speed-dial list (telephony-service)

Enables a global bulk speed-dial list for all users of a Cisco Unified CME
                                          						system.

bulk-speed-dial prefix

Sets
                                          						the prefix code that phone users dial to access speed-dial numbers from a bulk
                                          						speed-dial list.

## show
                        	 telephony-service conference hardware

To display
                              		  information about hardware conferences in a Cisco Unified Communications
                              		  Manager Express (Cisco CME) system, use the show telephony-service conference hardware command in privileged EXEC mode.

show telephony-service conference hardware [ ad-hoc [ detail | video ] | detail [ video ] | meetme [ detail | video ] | number telephone-number ]

### Syntax Description

ad-hoc

(Optional) Ad-hoc hardware conferences.

detail

(Optional) Detailed information for all conferences.

video

(Optional) Video conferences.

meetme

(Optional) Meet-me hardware conferences.

number

(Optional) Conference number.

telephone-number

(Optional) Telephone or extension number.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

15.1(4)M

Cisco
                                          						Unified CME 8.6

This
                                          						command was modified to include the video option.

15.2(2)T

Cisco
                                          						Unified CME9.0

This
                                          						command was modified to add hardware conference information on Cisco Unified
                                          						SIP IP phones to the output display.

### Usage Guidelines

Use the show telephony-service conference hardware command to display ad-hoc and meet-me
                              		  hardware conferences information, including which parties are still in the
                              		  conference.

## Examples

The following
                              		  is a sample output that displays information for a four-party ad-hoc hardware
                              		  conference. Extension 8044 created the conference by calling extension 8012,
                              		  then adding extension 8004 to the conference. The conference administrator,
                              		  extension 8006, called into the conference after it was established.

```
Router# show telephony-service conference hardware detail
```

Conference Type Active Max Peak Host HostPhone Last

cur(initial)

=================================================================================

8893 Ad-hoc 4 8
                              		  4 8044 29 ( 29) 8006

Conference
                              		  parties:

8006 (admin)

8004

8012

```
8044
```

The following
                              		  is a sample output that displays information for a meet-me video conference:

```
Router# show telephony-service conference hardware detail video Conference   Type              Active  Max  Peak    Host         HostPhone   Last
                                                                   cur(initial) 
     
================================================================================
=============
9999         Meetme-Video          10    16    10   n/a            0     (  0)   9012        
Conference parties (number:phone)
    9012  :12 :Audio
    7001  :Video
    9003  :3 :Audio
    7047  :Audio
    7015  :Video
    3667  :Audio
    9024  :24 :Audio
    9023  :23 :Video
    3665  :Video
    9022  :22 :Video
```

The following
                              		  is another sample output from the show telephony-service conference hardware detail command. The output shows an ad-hoc video hardware conference among three
                              		  participants, two of which are Cisco Unified SIP IP phones.

```
Router# show telephony-service conference hardware detail Conference   Type Active  Max  Peak  Host                 HostPhone Last
                                                                                                     cur(initial)      
========================================================================
B000             Ad-hoc Video    3         4       3        3915 SIP3915     15(15)              5801 RM5801   
Conference parties (number:phone)
   5801 5801 :Video
   3916 SIPPHONE3916 :16 :Video
   3915 SIPPHONE3915 :15  (admin):Video
```

The following
                              		  is a sample output from the show telephony-service conference hardware ad-hoc command:

```
Router# show telephony-service conference hardware ad-hoc Conference   Type Active  Max  Peak  Host                 HostPhone   Last
                                                                                                     	cur(initial)      
========================================================================
B000             Ad-hoc Video    3         4       3        3915 SIP3915     15(15)              5801 RM5801
```

The following
                              		  is a sample output from the show telephony-service conference hardware meetme command:

```
Router# show telephony-service conference hardware meetme Conference   Type                Active  Max  Peak    Host                HostPhone   Last
                                                                                                          cur(initial)      
========================================================================
7788            Meetme Video     4        4       4         3916 SIP3916    16(16)              5802 RM5802
```

The following
                              		  is a sample output from the show telephony-service conference hardware number command:

```
Router# show telephony-service conference hardware number B000 Conference   Type                 Active  Max  Peak  Host                 HostPhone   Last
                                                                                                     cur(initial)      
========================================================================
B000             Ad-hoc Video    3         4       3        3915 SIP3915     15(15)              5801 RM5801
```

The following
                              		  is another sample output from the show telephony-service conference hardware number command:

```
Router# show telephony-service conference hardware number 7788 Conference   Type                Active   Max  Peak  Host                HostPhone   Last
                                                                                                        cur(initial)      
========================================================================
7788             Meetme Video   4         4        4       3917 SIP3917    17(17)               4801  SCCP4801
```

The following
                              		  table describes the significant fields shown in the display, listed in
                              		  alphabetical order.

Field

Description

Active

Number
                                          					 of active parties in the conference.

admin

Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can:

Dial in to any conference directly through the conference number.

Use the ConfList soft key to list conference parties.

Remove any party from any conference.

Conference

Conference directory number (DN).

Conference parties

DNs in
                                          					 the conference.

Last

Last
                                          					 participant to join the conference.

Host

Conference creator.

HostPhone cur(initial)

cur—Current host phone. The phone that currently hosts the conference creator.

(initial)—Initial host phone. The phone that hosted the conference creator when the conference was created.

Because you can transfer the conference creator, the current host phone may be different from the initial host phone.

Max

Maximum
                                          					 number of participants allowed in the conference.

Peak

Maximum
                                          					 number of participants in the conference at any time.

Type

Type of
                                          					 conference: meet-me or ad hoc.

## show
                        	 telephony-service directory-entry

To display the
                              		  entries made using the directory entry , use the show telephony-service directory-entry command in user EXEC or privileged
                              		  EXEC mode.

show telephony-service directory-entry

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.2(15)ZJ

3.0

This
                                          						command was introduced.

12.3(4)T

3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

This command
                              		  lists directory entries that are made using the directory entry but does not list entries that are made
                              		  using the name and number commands in ephone-dn configuration mode.

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service directory-entry directory entry 1 4085550123 name Smith, John
```

The following
                              		  table describes significant fields in this output, in alphabetical order.

Field

Description

directory directory-tag (shown as 1 in the example)

Sequence
                                          					 number or unique identifier for a directory entry.

name (shown as Smith, John)

Name that
                                          					 appears in the directory associated with the number.

number (shown as 4085550123 in the example)

Telephone
                                          					 number or extension for the directory entry.

### Related Commands

Command

Description

directory entry

Adds an
                                          						entry to a local phone directory that can be displayed on IP phones.

show telephony-service all

Displays detailed configuration of a Cisco CME system.

show telephony-service ephone - dn

Displays information for extensions (ephone-dns) in a Cisco CME system.

## show
                        	 telephony-service ephone

To display
                              		  configuration for the Cisco IP phones, use the show telephony-service ephone command in user EXEC or privileged EXEC mode.

show telephony-service ephone

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						CME 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

The
                                          						conference add-mode, conference drop-mode, and conference admin fields were
                                          						added.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The output was enhanced to include the setting of the feature-button command and information about
                                          						logical partitioning class of restriction (LPCOR).

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service ephone Number of Configured ephones 2 (Registered 2)
ephone 1
Device Security Mode: Non-Secure
mac-address 1234.4321.7000
type 7960
button  1:1
keepalive 30 auxiliary 30
multicast-moh
max-calls-per-button 8
busy-trigger-per-button 0
Always send media packets to this router: No
Preferred codec: g711ulaw
conference drop-mode never
conference add-mode all
conference admin: No
privacy: Yes
feature-button 1 Dnd
user-locale US
network-locale US
lpcor type: remote
lpcor (incoming): ephone_group2  (outgoing): ephone_group2
!
ephone 2
Device Security Mode: Non-Secure
mac-address 1234.4321.6000
type 7960
button  1:2
keepalive 30 auxiliary 30
multicast-moh
max-calls-per-button 8
busy-trigger-per-button 0
Always send media packets to this router: No
Preferred codec: g711ulaw
conference drop-mode never
conference add-mode all
conference admin: No
privacy: Yes
feature-button 1 Dnd
user-locale US
network-locale US
lpcor type: local
lpcor (incoming): ephone_group1  (outgoing): ephone_group1
!
```

The table
                              		  describes significant fields in this output, in alphabetical order.

Field

Description

button

Button
                                          					 number on IP phone, separator to denote ring characteristics and ephone-dn tag.
                                          					 A colon (:) separator denotes a normal ring.

conference add-mode

Who can
                                          					 add parties to a conference:

- creator—Only the creator can add parties.

- all—Any party can add other parties if the creator remains in the conference.

conference drop-mode

When
                                          					 conferences are dropped:

- creator—Conference terminates when the creator hangs up.

- local—Conference terminates when the last local party in the conference hangs
                                             						up or drops out of the conference.

- never—Conference is not dropped, even if the creator hangs up, as long as three
                                             						parties remain in the conference.

conference admin

Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can:

- Dial
                                             						in to any conference directly through the conference number

- Use
                                             						the ConfList soft key to list conference parties

- Remove any party from any conference

ephone

Cisco
                                          					 IP phone.

feature-button

Displays the type of feature button on the ephone. Feature type can be
                                          					 configured with privacy or DND.

lpcor
                                          					 (incoming)

Setting
                                          					 of the lpcor incoming command.

lpcor
                                          					 (outgoing)

Setting
                                          					 of the lpcor outgoing command.

lpcor
                                          					 type

Setting
                                          					 of the lpcor type command.

mac-address

MAC
                                          					 address of the Cisco IP phone.

speed-dial

Speed-tag (unique identifier) and the number that is programmed for that
                                          					 speed-tag.

type

Model
                                          					 type of phone.

### Related Commands

Command

Description

show telephony-service all

Displays detailed configuration for a Cisco Unified CME system.

show telephony-service dial - peer

Displays dial-peer information for extensions in Cisco Unified CME.

show telephony-service ephone - dn

Displays information for extensions in Cisco Unified CME.

show telephony-service voice - port

Displays configurations for virtual voice ports in Cisco Unified CME.

## show
                        	 telephony-service ephone-dn

To display
                              		  information about extensions (ephone-dns) in a Cisco CallManager Express (Cisco
                              		  CME) system, use the show telephony-service ephone - dn command in user EXEC or privileged EXEC mode.

show telephony-service ephone-dn

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.1(5)YD

1.0

This
                                          						command was introduced

12.2(8)T

2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service ephone-dn ephone-dn 1
 number 5001
 huntstop
ephone-dn 2
 number 5002
 huntstop
 call-forward noan 5001 timeout 8
ephone-dn 3
 number 5003
 huntstop
ephone-dn 4
 number 5004
 huntstop
```

The following
                              		  table describes significant fields in this output, in alphabetical order.

Field

Description

call-forward noan

Call
                                          					 forwarding is set to no answer. Other available options are call-forward busy
                                          					 and call-forward all.

ephone-dn

Cisco IP
                                          					 phone directory number.

huntstop

Huntstop
                                          					 is set.

number

Cisco IP
                                          					 phone number.

timeout

Timeout
                                          					 setting for call forwarding when an extension does not answer.

### Related Commands

Command

Description

show telephony-service all

Displays the detailed configuration of all the Cisco IP phones.

show telephony-service dial - peer

Displays dial peer information for extensions (ephone-dns) in a Cisco CME
                                          						system.

show telephony-service voice - port

Displays configurations for virtual voice ports in a Cisco CME system.

## show telephony-service ephone-dn-template

To display information about ephone-dn-template configurations, use
                              		  the show telephony-service ephone-dn - template command in user EXEC or privileged EXEC mode.

show telephony-service ephone-dn-template

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC Privileged EXEC

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

This command displays contents of ephone-dn templates. Use the show running-config to display the association of
                              		  templates to particular ephone-dns.

## Examples

The following is sample output from this command:

```
Router# show telephony-service ephone-dn-template ephone-template 1
 softkeys idle  Newcall Redial Cfwdall Dnd Pickup Gpickup Login
 codec g711ulaw
 User Locale: US
 Network Locale: US
ephone-template 2
 softkeys idle  Redial Newcall Dnd Cfwdall Pickup Gpickup Login
 codec g711ulaw
 User Locale: US
 Network Locale: US
```

### Related Commands

Command

Description

ephone-dn-template

Creates an ephone-dn template and enters ephone-dn-template
                                          						configuration mode.

## show
                        	 telephony-service ephone-template

To display the
                              		  contents of ephone-templates, use the show telephony-service ephone - template command in user EXEC or privileged EXEC mode.

show telephony-service ephone-template

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(11)T

Cisco
                                          						CME 3.2

This
                                          						command was introduced.

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

The
                                          						conference add-mode, conference drop-mode, and conference admin fields were
                                          						added.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1)

Emergency response location (ERL) information assigned to an ephone displays in
                                          						the output.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. Logical partitioning class of restriction (LPCOR)
                                          						information was added to the output.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

Use this command
                              		  to display the contents of each ephone template that is defined. Use the show running-config command to display the association
                              		  of templates to specific ephones.

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service ephone-template ephone-template 1
softkey idle  Cfwdall Dnd Gpickup Join Pickup RmLstC
softkey connected  Acct ConfList Confrn Endcall Hold Join Park
conference drop-mode never
conference add-mode all
conference admin: No
max-calls-per-button 8
busy-trigger-per-button 0
privacy default
MLPP max precedence level -1
MLPP indication Enabled
MLPP preemption Enabled
Always send media packets to this router: No
Preferred codec: g711ulaw
keepalive 30 auxiliary 30
User Locale: US
Network Locale: US
Emergency Response Location: 6
lpcor type: remote
lpcor (incoming): local_sccp_phone_1     (outgoing): local_sccp_phone_1
```

The following
                              		  table describes significant fields in this output.

Field

Description

ephone-template

Identifier for the ephone template.

softkey
                                          					 hold

Soft
                                          					 keys displayed during the hold call stage.

softkey
                                          					 idle

Soft
                                          					 keys displayed during the call-idle call stage.

softkey
                                          					 seized

Soft
                                          					 keys displayed during the call-seized call stage.

softkey
                                          					 alerting

Soft
                                          					 keys displayed during the call-alerting call stage.

softkey
                                          					 connected

Soft
                                          					 keys displayed during the call-connected call stage.

conference drop-mode

When
                                          					 conferences are dropped:

- creator: Conference terminates when the creator hangs up.

- local: Conference terminates when the last local party in the conference hangs
                                             						up or drops out of the conference.

- never: Conference is not dropped, even if the creator hangs up, if three
                                             						parties remain in the conference.

conference add-mode

Who can
                                          					 add parties to a conference:

- creator: Only the creator can add parties.

- all:
                                             						Any party can add other parties if the creator remains in the conference.

conference admin

Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can:

- Dial
                                             						in to any conference directly through the conference number.

- Use
                                             						the ConfList soft key to list conference parties.

- Remove any party from any conference.

Always
                                          					 send media packets to this router

Always
                                          					 send media packets to this Cisco Unified CME router, which acts as a proxy and
                                          					 forwards the packets to the destination, instead of sending them directly to
                                          					 the destination IP phone.

Preferred codec

Codec
                                          					 to use when initiating a call.

button-layout

Type of
                                          					 IP phone and number of fixed line or feature set.

- 1:
                                             						Button 24=Menu. Button 23=Headset.

- 2:
                                             						Button 24=Menu. Button 23=Headset. Button 22=Directories. Button 21=Messages.

User
                                          					 Locale

Locale
                                          					 that is associated with the phone user interface. The user locale identifies a
                                          					 set of detailed information, including language and font, to support users.

Network
                                          					 Locale

Locale
                                          					 that is associated with the phone. The network locale contains a definition of
                                          					 the tones and cadences that are used by the phones and gateways in the device
                                          					 pool in a specific geographic area.

Emergency response location

Identification of the ERL defined with the emergency response location command.

lpcor
                                          					 (incoming)

Setting
                                          					 of the lpcor incoming command.

lpcor
                                          					 (outgoing)

Setting
                                          					 of the lpcor outgoing command.

lpcor
                                          					 type

Setting
                                          					 of the lpcor type command.

### Related Commands

Command

Description

ephone-template

Creates an ephone template.

## show telephony-service fac

To display current feature access codes (FACs), use the show telephony-service fac command in privileged EXEC mode.

show telephony-service fac

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

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

Phone users dial FACs to access phone features. The set of standard
                              		  FACs must be enabled using the fac standard before phone users can use them.
                              		  Individual FACs can be changed using the fac custom command.

## Examples

The following example displays the set of standard FACs:

```
Router# show telephony-service fac telephony-service fac standard
 callfwd all **1
 callfwd cancel **2
 pickup local **3
 pickup group **4
 pickup direct **5
 park **6
 dnd **7
 redial **8
 voicemail **9
 ephone-hunt join *3
 ephone-hunt cancel #3
```

### Related Commands

Command

Description

fac

Enables standard FACs or creates a custom FAC.

## show telephony-service security-info

To display the security-related information that is configured under
                              		  telephony-service, use the show telephony-service security-info command in privileged EXEC
                              		  configuration mode.

show telephony-service security-info

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example displays security information that was
                              		  configured under telephony-service.

```
Router# show telephony-service security-info Skinny Server Trustpoint for TLS: cisco1
TFTP Credentials Trustpoint: cisco1
Server Security Mode: Secure
Global Device Security Mode: Authenticated
```

## show telephony-service tftp-bindings

To display the current configuration files accessible to IP phones,
                              		  use the show telephony-service tftp-bindings command in user EXEC or privileged
                              		  EXEC mode.

show telephony-service tftp-bindings

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC Privileged EXEC

## Command History

Cisco IOS Release

Cisco CME Version

Modification

12.2(11)YT

2.1

This command was introduced.

12.2(15)T

2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

Use this command with Cisco IOS Telephony Services V2.1, Cisco
                              		  CallManager Express 3.0, or a later version.

This command provides a list of configuration files that are
                              		  accessible to IP phones using TFTP, including the dictionary, language, and
                              		  tone configuration files that are associated with the ISO-3166 codes that have
                              		  been selected using the user-locale and network-locale commands.

## Examples

The following is sample output from the show telephony-service tftp-bindings when the ISO-3166 code for Germany has been selected for both
                              		  language and tones:

```
Router(config)# show telephony-service tftp-bindings tftp-server system:/its/SEPDEFAULT.cnf
tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml
tftp-server system:/its/ATADefault.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml
tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml
tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml
tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml
tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml
tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml
```

### Related Commands

Command

Description

network - locale

Sets the definition of the tones and cadences on the Cisco
                                          						IP Phones 7940 and 7940G and the Cisco IP Phones 7960 and 7960G for a specific
                                          						geographic area.

user - locale

Sets language for displays on the Cisco IP Phones 7940 and
                                          						7940G and the Cisco IP Phones 7960 and 7960G.

## show
                        	 telephony-service voice-port

To display
                              		  configurations of virtual voice ports in a Cisco CallManager Express (Cisco
                              		  CME) system, use the show telephony-service voice - port command in user EXEC or privileged EXEC mode.

show telephony-service voice-port

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						CME Version

Modification

12.1(5)YD

1.0

This
                                          						command was introduced.

12.2(8)T

2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

### Usage Guidelines

This command
                              		  displays virtual voice-port configurations for a Cisco CME system. Each
                              		  ephone-dn corresponds to a virtual voice port. For example, the ephone-dn with
                              		  dn-tag 7 corresponds to virtual voice port 50/0/7. The virtual voice port
                              		  provides the telephone line associated with the Cisco IP phone extension
                              		  (ephone-dn).

## Examples

The following is
                              		  sample output from this command:

```
Router# show telephony-service voice-port voice-port 50/0/1
 station-id number 5001
!
voice-port 50/0/2
 station-id number 5002
 timeout ringing 8
!
voice-port 50/0/3
 station-id number 5003
!
voice-port 50/0/4
 station-id number 5004
!
```

The following
                              		  table describes significant fields in this output, in alphabetical order.

Field

Description

station-id number

Phone
                                          					 number used for caller ID purposes for calls made from this voice port.

timeout
                                          					 ringing

Maximum
                                          					 amount of time that a phone is allowed to ring before the call is disconnected.

voice-port

Virtual
                                          					 voice port.

### Related Commands

Command

Description

show telephony-service all

Displays the detailed configuration of all the Cisco IP phones.

show telephony-service dial - peer

Displays dial-peer information for extensions in a Cisco CME system.

show telephony-service ephone - dn

Displays information for extensions (ephone-dns) in a Cisco CME system.

## show voice emergency

To display the IP address, subnet mask, and ELIN for each emergency
                              		  response location, use the show voice emergency command in user EXEC or privileged EXEC mode.

show voice emergency

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to display the IP address, subnet mask, and ELIN for
                              		  each emergency response location.

## Examples

The following example shows sample output which includes IP mask and
                              		  ELIN information for each ERL:

```
EEMERGENCY RESPONSE LOCATIONS
ERL               | ELIN 1     | ELIN2      | SUBNET 1        | SUBNET 2       
1                 | 6045550101 |            | 10.0.0.0        | 255.0.0.0 
2                 | 6045550102 | 6045550106 | 192.168.0.0     | 255.255.0.0 
3                 |            | 6045550107 | 172.16.0.0      | 255.255.0.0 
4                 | 6045550103 |            | 192.168.0.0     | 255.255.0.0 
5                 | 6045550105 |            | 209.165.200.224 | 255.0.0.0 
6 6045550198      |            | 6045550109 | 209.165.201.0   | 255.255.255.224
```

### Related Commands

Command

Description

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## show voice emergency addresses

To display address information for each emergency response location,
                              		  use the show emergency addresses command in user EXEC or privileged EXEC mode.

show voice emergency addresses

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays the physical address of each emergency response
                              		  location.

## Examples

The following example shows a sample output which includes physical
                              		  address information for the ERL:

```
Router# show voice emergency addresses 3850 Zanker Rd, San Jose,604,5550101
225 W Tasman Dr, San Jose,604,5550102
275 W Tasman Dr, San Jose,604,5550103
518 Bellew Dr,Milpitas,604,5550104
400 Tasman Dr,San Jose,604,5550105
    3675 Cisco Way,San Jose,604,5550106
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

show voice emergency all

Displays all emergency response location information.

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## show voice emergency all

To display all emergency response location information, use the show voice emergency all command in user EXEC or privileged EXEC mode.

show voice emergency all

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to display all information configured for each
                              		  emergency response location.

## Examples

The following example shows a sample output, displaying all
                              		  ERL-related information for ERL 1 and 3.

```
VOICE EMERGENCY RESPONSE SETTINGS
   Callback Number: 6045550103
   Emergency Line ID Number: 6045550155
   Expiry: 2 minutes
   Logging Enabled
EMERGENCY RESPONSE LOCATION 1
   Name: Cisco Systems 1
   Address: 3850 Zanker Rd, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.200.226 IP mask 1: 255.255.255.254
   IP Address 2: 209.165.202.129 IP mask 2: 255.255.0.0
   Emergency Line ID 1: 6045550180
   Emergency Line ID 2: 
   Last Caller:  6045550188 [Jan 30 2007 16:05.52 PM]
   Next ELIN For Emergency Call: 6045550166
EMERGENCY RESPONSE LOCATION 3
   Name: Cisco Systems 3
   Address: 225 W Tasman Dr, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.202.133 IP mask 1: 255.255.0.0
   IP Address 2: 209.165.202.130 IP mask 2: 255.0.0.0
   Emergency Line ID 1: 
   Emergency Line ID 2: 6045550150
   Last Caller:  
   Next ELIN For Emergency Call: 6045550151
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

name

Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

voice emergency response location

Creates a tag for identifying an ERL for the E911 services.

## show voice emergency callers

To display a list of 911 calls made over the last three hours, use
                              		  the show emergency callers command in privileged EXEC mode.

show voice emergency callers

### Syntax Description

This command has no arguments or keywords.

### Command Default

No list of 911 calls is displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added to Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to display a list of all 911 calls made in the past
                              		  three hours. The list shows the originating number, the ELIN used, and the time
                              		  the call was placed.

## Examples

The following example shows sample output, which includes the
                              		  originating number, the ELIN used, and the time the call was placed:

```
router# show voice emergency callers EMERGENCY CALLS CALL BACK TABLE
ELIN                      | CALLER                     | TIME                
6045550181                | 8155550151                | Oct 12 2006 04:05:21
6045550182                | 8155550152                | Oct 12 2006 04:05:21
```

### Related Commands

Command

Description

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

## show voice emergency zone

To display each emergency response zone’s list of locations in
                              		  priority order, use the show voice emergency zone command in user EXEC or privileged EXEC mode.

show voice emergency zone

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to display a list of the locations, in priority
                              		  order, of all configured emergency response zones.

## Examples

The following example shows a sample output which displays the ERL
                              		  locations for emergency response zones 90 and 100.

```
EMERGENCY RESPONSE ZONES
 zone 90
    location 4
    location 5
    location 6
    location 7
    location 2147483647
 zone 100
    location 1 priority 1
    location 2 priority 2
    location 3 priority 3
```

### Related Commands

Command

Description

location

Identifies locations within an emergency response zone.

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

voice emergency response zone

Creates an emergency response zone within which ERLs can be
                                          						grouped.

## show voice fac statistics

To display the FAC failure statistics collected by the system, use
                              		  the show voice fac statistics command in privileged EXEC mode.

show voice fac statistics

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to display the forced athentication code (FAC)
                              		  success or failure statistics collected by the system.

## Examples

The following is sample output from this command displaying all
                              		  statistical information:

```
Router# show voice fac statistics Voice FAC statistics for failure calls:
  Total basic calls:             5
  Total forward calls:           1
```

### Related Commands

Command

Description

show call active voice

Displays call information for voice calls that are in
                                          						progress.

show call history voice

Displays the call history table for voice calls.

## show voice
                        	 hunt-group

To display
                              		  configuration information associated with one or all voice hunt groups in a
                              		  Cisco Unified Communications Manager Express (Cisco Unified CME) system, use
                              		  the show voice hunt-group command in privileged EXEC mode.

show voice hunt-group hunt-group-tag [ brief ] { longest-idle | parallel | peer | sequential }

### Syntax Description

hunt-group-tag

(Optional) Unique sequence number that identifies the voice hunt group. Range
                                          						is 1 to 100.

brief

(Optional) Displays brief information on all voice hunt groups in a Cisco CME
                                          						system.

longest-idle

(Optional) Displays summary of longest-idle voice hunt groups.

parallel

(Optional) Displays summary of parallel voice hunt groups.

peer

(Optional) Displays summary of peer voice hunt groups.

sequential

(Optional) Displays summary of sequential voice hunt groups.

### Command Modes

Privileged EXEC (#	)

## Command History

Release

Modification

12.4(24)T

This
                                          						command was introduced in a release earlier than Cisco IOS Release 12.4(24)T.

15.2(2)T

This
                                          						command was modified to add stat collect as a field.

### Usage Guidelines

Use the show voice hunt-group command to get information about voice
                              		  hunt group configuration on the gateway as an alternative to the show running-confi g command.

Use the show voice hunt-group and show voice hunt-group brief commands to display hunt group configuration information for all voice hunt
                              		  groups in a Cisco Unified CME system. Use show voice hunt-group hunt-group-tag to display data on a specific
                              		  hunt-tag configuration created by the voice hunt-group command. Use the longest-idle , parallel , peer , or sequential keywords to display data on a specific type of voice hunt group configuration
                              		  created by the voice hunt-group command.

## Examples

The following
                              		  is a sample output from the show voice hunt-group command, displaying all voice hunt
                              		  groups configured on the router:

```
Router# show voice hunt-group Group 1
    type: longest-idle
    preference: 0
    preference (sec): 0
    timeout: 0
    final_number: 1
Group 34
    type: parallel
    pilot number: 3, peer-tag 2147483647
    secondary number: 4, peer-tag 2147483646
    preference: 0
    preference (sec): 0
    timeout: 0
    final_number:
```

The following
                              		  is a sample output from the show voice hunt-group command, displaying the configuration
                              		  for all the configured voice hunt groups:

```
Router# show voice hunt-group Group 5
 type: parallel
 pilot number: 1234, peer-tag 1234
 list of numbers: 
		MEMBER   					USED_BY    	 STATE     LOGIN/LOGOUT
		=======  					=======     	========  ============	
		9498889994				9498889994			DOWN						Logout
		9498889993				9498889994			UP								Login
		*													-												-									-
 secondary number: 5678, peer-tag 5678
 list preference: 5
 preference (sec): 8
 timeout: 180
 final_number: 4444
Group 8
 type: longest-idle
 pilot number: 6666, peer-tag 6666
 list of numbers: 
				MEMBER   					USED_BY    	 STATE     LOGIN/LOGOUT
				=======  					=======     	========  ============
				5106575902				5106575902			UP								Login
				4088531111				4088531111			UP								Login
				4083911375				4083911375			DOWN						Login
				4089306067				4089306067			DOWN						Logout
				8869395033				8869395033			DOWN						Logout
				88686619633			88686619633		DOWN						-
 preference: 0
 preference (sec): 0
 timeout: 180 
 final_number:
 hops: 6
	phone-display: Yes
Group 10
 type: longest-idle
 pilot number: 7777777, peer-tag 7777777
 secondary number: 88888888, peer-tag 88888888
 list of numbers: 
				MEMBER   			USED_BY     STATE     LOGIN/LOGOUT
				=======  			=======     ========  ============
				7654321					7654321					DOWN						Logout
				87654321				87654321				UP								Login
				987654321			987654321			UP								Logout
 preference: 0
 preference (sec): 0
 timeout: 180
 final_number:
 hops: 3
	phone-display: No
Group 15
 type: peer
 pilot number: 56789, peer-tag 56789
 list of numbers: 
				MEMBER   			USED_BY     STATE     LOGIN/LOGOUT
				=======  			=======     ========  ============
				87654321				87654321				DOWN						Login
				9876								9876				    UP						  Logout
				87654							87654							DOWN						-
 preference: 0
 preference (sec): 0
timeout: 180
 final_number:
 hops: 3
	phone-display: Yes
```

The following
                              		  is a sample output from the show voice hunt-group command, displaying information for a
                              		  particular voice hunt group as specified by the hunt-group-tag number:

```
Router# show voice hunt-group 5 Group 5
 type: parallel
 pilot number: 1234, peer-tag 1234
 secondary number: 5678, peer-tag 5678
 list of numbers: 
				MEMBER   						USED_BY     		STATE     LOGIN/LOGOUT
				=======  						=======     		========  ============
				9498889994					9498889994				UP								Logout
				9498889993					9498889993				DOWN						Login
				*														-													-									-
 preference: 5
 preference (sec): 8
 timeout: 20
 final_number: 4444
```

The following
                              		  is a sample output from the show voice hunt-group command, displaying information about
                              		  all the voice hunt groups of a particular type:

```
Router# show voice hunt-group longest-idle Group 8
 type: longest-idle
 pilot number: 6666, peer-tag 6666
 list of numbers: 
				MEMBER   						USED_BY     		STATE     LOGIN/LOGOUT
				=======  						=======     		========  ============
				5106575902					5106575902				UP								Logout
				4088531111					4088531111				UP								Login
				4083911375					4083911375				DOWN      -
				4089306067					4089306067				UP								Logout 
				8869395033     8869395033				-									-
				88686619633				88686619633			UP								Login
 preference: 0
 preference (sec): 0
 timeout: 180
 final_number:
 hops: 6
	phone-display: Yes
Group 10
 type: longest-idle
 pilot number: 7777777, peer-tag 7777777
 secondary number: 88888888, peer-tag 88888888
 list of numbers: 
				MEMBER   	USED_BY   	STATE     LOGIN/LOGOUT
				=======  	=======   	========  ============
				7654321			7654321				UP								Logout
				87654321		87654321			UP								Login
				987654321	987654321 	DOWN						Logout
 preference: 0
 preference (sec): 0
 timeout: 180
 final_number:
 hops: 3
	phone-display: No
```

The following
                              		  is a sample output from the show voice hunt-group command with the keyword brief :

```
Router# show voice hunt-group brief TAG TYPE PILOT     LIST
=== ==== ========  =====================================================
5   PAR  1234      9498889-, 9498889-
         5678      9498889-, 9498889-
8   LON  6666      5106575-, 4088531-, 4083911-, 4089306-, 8869395-,.....
10  LON  7777777   7654321, 8765432-, 9876543-
         8888888-  7654321, 8765432-, 9876543-
15  PER  56789     8765432-, 9876, 87654
```

The following
                              		  is a sample output from the show voice hunt-group command, indicating that call
                              		  statistics is being collected:

```
Router# show voice hunt-group 1 Group 1
    type: parallel
    pilot number: 5000, peer-tag 2147483647
    list of numbers: 
				MEMBER   USED_BY   STATE     LOGIN/LOGOUT
				=======  =======   ========  ============
				5001					5001						UP								Logout
				5002					5002						UP								Login
				5011					5011						DOWN      -
				5012					5012						UP								Logout
    preference: 0
    preference (sec): 0
    timeout: 12
    final_number: 5012
    stat collect: yes
				phone-display: Yes
```

The following
                              		  is a sample output from the show voice hunt-group command when there is no voice hunt
                              		  group configured:

```
Router# show voice hunt-group no voice hunt-groups configured
Router# show voice hunt-group brief no voice hunt-groups configured
Router# show voice hunt-group longest-idle no voice hunt-groups configured 
Router#
```

The following
                              		  table describes the significant fields shown in the output.

Field

Description

Group

Tag
                                          					 number of voice hunt group.

type

Type of
                                          					 voice hunt group. The available voice hunt group types are: longest-idle,
                                          					 parallel, peer and sequential.

pilot
                                          					 number

Number
                                          					 that callers dial to reach the specified voice hunt group.

secondary-number

Alternate number for the specified voice hunt group.

list of
                                          					 numbers

Numbers
                                          					 of the extensions configured in the voice hunt-group command‘s hunt-tag identifier.

preference

Preference order for the extension or telephone number associated with a dial
                                          					 peer. Range is 0 to 8. Default is 0.

preference (sec)

Preference order for the secondary pilot number. Range is from 0 to 10, where 0
                                          					 is the highest preference and 10 is the lowest preference. Default is 9.

timeout

Number
                                          					 of seconds after which a call that is not answered at one number is redirected
                                          					 to the next number in the hunt group list.

final_number

Last
                                          					 number in the voice hunt group, after which a call is no longer redirected.

hops

Number
                                          					 of hops before a call proceeds to the final number.

stat
                                          					 collect

Yes
                                          					 indicates that call statistics are being collected for a voice hunt group.

phone-display

Displays
                                          					 the hunt group information on My Phone Apps service button.

hlog-block

Blocks
                                          					 the hlog functionality of voice hunt group on the phone.

peer-tag

Peer
                                          					 hunting tag.

### Related Commands

Command

Description

final (voice hunt-group)

Defines the last extension in a voice hunt group.

hops (voice hunt-group)

Defines the number of times that a call is redirected to the next directory
                                          						number in a peer voice hunt group list before proceeding to the final directory
                                          						number.

list (voice hunt-group)

Defines the directory numbers that participate in a directory number hunt
                                          						group.

pilot (voice hunt-group)

Defines the voice dn that callers dial to reach a Cisco Unified Communications
                                          						Manager Express (Cisco Unified CME) voice hunt group.

timeout (voice hunt-group)

Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last directory number in
                                          						the hunt group.

voice hunt-group

Configures voice hunt groups and the associated parameters.

## show voice
                        	 hunt-group statistics

To display call
                              		  statistics from voice hunt groups, use the show voice hunt-group statistics command in privileged EXEC mode.

show voice hunt-group group-id statistics { last hours hours | start day time [ to day time ]}

### Syntax Description

group-id

Identifier for the voice hunt group. Range: 1 to 100.

last

Displays the latest call statistics for a voice hunt group for a specified
                                          						number of hours, counting backward from the current hour. Range: 1 to 167.

hours hours

Number
                                          						of hours that the call statistics are displayed.

start

Defines
                                          						the start of the period for which the call statistics are displayed. Default
                                          						duration is one hour.

day

Abbreviated day of the week. The following abbreviations are valid: sun, mon,
                                          						tue, wed, thu, fri, sat.

time

Hour of
                                          						the day. Range: 0 to 23.

to

(Optional) Defines the time the display of the call statistics ends.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

### Usage Guidelines

Use the show voice hunt-group statistics command to display the average and
                              		  longest times for a voice hunt group to answer a call, make a call, or put a
                              		  call on hold. The command can also display the number of answered and abandoned
                              		  calls, the number of calls forwarded to or answered by voice mail, and the
                              		  number of error calls.

The output is
                              		  dependent on call activity. If there is no activity, no data is displayed.

If your Cisco
                              		  Unified CME system is configured with the basic automatic call distribution
                              		  (B-ACD) and auto-attendant service, you can enable the collection of call
                              		  statistics for every voice hunt group with the voice hunt-group statistics collect command. Additional data is displayed for
                              		  all agents combined and for individual agents.

For remote
                              		  Cisco Unified SCCP IP phones in voice hunt groups, the hold and resume
                              		  statistics are not updated.

## Examples

The following
                              		  is a sample output from the show voice hunt-group statistics command. The output includes direct
                              		  calls to a voice hunt group number and calls from queue/B-ACD.

```
Router# show voice hunt-group 1 statistics last 1 h Wed 04:00 - 05:00
	Max Agents: 3
	Min Agents: 3
	Total Calls: 9
	Answered Calls: 7
	Abandoned Calls: 2
	Average Time to Answer (secs): 6
	Longest Time to Answer (secs): 13
	Average Time in Call (secs): 75
	Longest Time in Call (secs): 161
	Average Time before Abandon (secs): 8
	Calls on Hold: 2
	Average Time in Hold (secs): 16	
	Longest Time in Hold (secs): 21
	Per agent statistics:
		Agent: 5012
			From Direct Call:
				Total Calls Answered: 3
				Average Time in Call (secs): 70
				Longest Time in Call (secs): 150
				Totals Calls on Hold: 1
				Average Hold Time (secs): 21
				Longest Hold Time (secs): 21
			From Queue:
				Total Calls Answered: 3
				Average Time in Call (secs): 55
				Longest Time in Call (secs): 78
				Total Calls on Hold: 2
				Average Hold Time (secs): 19
				Longest Hold Time (secs): 26
		Agent: 5013
			From Direct Call:
				Total Calls Answered: 3
				Average Time in Call (secs): 51
				Longest Time in Call (secs): 118
				Totals Calls on Hold: 1
				Average Hold Time (secs): 11
				Longest Hold Time (secs): 11
			From Queue:
				Total Calls Answered: 1
				Average Time in Call (secs): 4
				Longest Time in Call (secs): 4
		Agent: 5014
			From Direct Call:
				Total Calls Answered: 1
				Average Time in Call (secs): 161
				Longest Time in Call (secs): 161
			From Queue:
				Total Calls Answered: 1
				Average Time in Call (secs): 658
				Longest Time in Call (secs): 658
	Queue related statistics:
		Total calls presented to the queue: 5
		Calls handoff to IOS: 5
		Number of calls in the queue: 0
		Average time to handoff (secs): 2
		Longest time to handoff (secs): 3
		Number of abandoned calls: 0
		Average time before abandon (secs): 0
		Calls forwarded to voice mail: 0
		Calls answered by voice mail: 0
		Number of error calls: 0
```

The following
                              		  is a sample output from the show voice hunt-group statistics command. The output focuses on
                              		  queue-related statistics.

```
Queue related statistics:
      Total calls presented to the queue: 8
      Calls handoff to IOS: 3
      Number of calls in the queue: 1
      Average time to handoff (secs): 10
      Longest time to handoff (secs): 15
      Number of abandoned calls: 4
      Average time before abandon (secs): 7
      Calls forwarded to voice mail: 0
      Calls answered by voice mail: 0
      Number of error calls: 0
```

The following
                              		  is a sample output from the show voice hunt-group statistics command. The output shows that no call
                              		  statistics were collected from voice hunt group 1 from 2:00 to 4:00 on a
                              		  Monday.

```
Router# show voice hunt-group 1 stat start Mon 2 to Mon 4 Mon 02:00 - 03:00
    No info
Mon 03:00 - 04:00
    No info
Mon 04:00 - 05:00
    No info
```

The following
                              		  table describes the significant fields shown in the display.

Field

Description

Abandoned calls

Total number of calls abandoned by hunt group agents. This
                                          					 does not include calls going to the final number.

Answered call

Total number of calls answered by hunt group agents.

Average time in call (secs)

Average length of time that unanswered calls waited before
                                          					 going to an agent.

Average time to answer (secs)

Average length of time that all calls to Cisco Unified CME
                                          					 B-ACD waited before being answered.

Average time in hold (secs)

Average length of time that calls were kept on hold for all
                                          					 agents.

Average hold time (secs)

Average length of time that calls waited on hold for this
                                          					 agent.

Average time to handoff (secs)

Average length of time before a call was handed off to IOS

Calls on hold

Total number of calls that were placed on hold.

Calls handoff to IOS

Total number of calls handed off to IOS.

Calls answered by voice mail

Total number of calls to Cisco Unified CME B-ACD that were
                                          					 answered by voice mail.

Calls forwarded to voice mail

Total number of calls to Cisco Unified CME B-ACD that were
                                          					 forwarded to voice mail.

Longest time to answer (secs)

Longest length of time before calls to Cisco Unified CME
                                          					 B-ACD were answered.

Longest time in call (secs)

Longest length of time that all calls to Cisco Unified CME
                                          					 B-ACD that went to an agent waited in a call queue.

Longest time in hold (secs)

Longest length of time that a call spent between being placed
                                          					 on hold and being picked up by agents.

Longest hold time (secs)

Longest length of time that a call to this agent was spent
                                          					 between being placed on hold and being picked up.

Longest time to handoff (secs)

Longest length of time before a call was handed off to IOS.

Max agent

Maximum number of hunt group agents.

Min
                                          					 agent

Minimum
                                          					 number of hunt group agents.

Number of abandoned calls

Total number of calls to Cisco Unified CME B-ACD that hung up
                                          					 before being answered.

Number of calls in the queue

Total number of calls in the queue.

Number of error calls

Total number of error calls.

Total calls

Total number of direct calls made to the hunt group.

Total
                                          					 calls answered

Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by an agent.

Total
                                          					 calls on hold

Total
                                          					 number of calls that were placed on hold for this agent.

Total calls presented to the queue

Total number of calls made to Cisco Unified CME B-ACD.

From Cisco Unified CME Release 10.5 onwards, abandoned calls will
                                          			 not include the calls going to the final number. However, the total calls
                                          			 includes calls going to the final number. Use the formula " Final Calls= Total Calls - Answered Calls - Abandoned Calls " ,
                                          			 to calculate the calls going to the final number.

### Related Commands

Command

Description

voice hunt-group statistics collect

Enables the collection of call statistics for voice hunt groups.

## show voice
                        	 register all

To display all
                              		  Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site
                              		  Telephony (SRST) or Cisco Unified Communications Manager Express (Cisco Unified
                              		  CME) configurations and register information, use the show voice register all command in privileged EXEC mode.

show voice register all

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

15.0(1)XA

Cisco
                                          						SIP SRST 8.0

This
                                          						command was modified to display the signaling transport protocol.

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1

The
                                          						output display of this command was modified.

15.2(4)M

Cisco
                                          						Unified CME 9.1

This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display.

### Usage Guidelines

KEM data are
                              		  displayed for Cisco Unified CME only. Cisco Unified SRST is unable to gather
                              		  all the configuration details about KEMs from Cisco Unified CM.

## Examples

## Examples

The following is
                              		  a sample output of the show voice register all command:

```
Router# show voice register all VOICE REGISTER GLOBAL
=====================
CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is srst
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
VOICE REGISTER DN
=================
Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Pool 2    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:   
  Pool 1    has this DN configured for line 3
VOICE REGISTER POOL
===================
 Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is disabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 2
Config:
  Mac address is 0015.C68E.6D13
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is disabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 3
Config:
  Mac address is 0021.5553.8998
  Number list 1 : DN 3
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is enabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

## Examples

The following is
                              		  a sample output of the show voice register all command:

```
Router# show voice register all 1) show voice register all
VOICE REGISTER GLOBAL
=====================
CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is cme
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  Source-address is 8.3.3.5 port 5060
  Time-format is 12
  Date-format is M/D/Y
  Time-zone is 5
  Hold-alert is disabled
  Mwi stutter is disabled
  Mwi registration for full E.164 is disabled
  Forwarding local is enabled
  Privacy is enabled
  Privacy-on-hold is disabled
  Dst auto adjust is enabled
    start at Apr week 1 day Sun time 02:00
    stop  at Oct week 8 day Sun time 02:00
  Max redirect number is 5
  IP QoS DSCP:
    ef (the MS 6 bits, 46, in ToS, 0xB8) for media
    cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
    af41 (the MS 6 bits, 34, in ToS, 0x88) for video
    default (the MS 6 bits, 0, in ToS, 0x0) for service
  Telnet Level: 0
  Tftp path is flash:
  Generate text file is disabled
  Tftp files are created, current syncinfo 0001140473454008
  OS79XX.TXT is not created
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
VOICE REGISTER DN
=================
Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua noan 999 timeout 8
  after-hour exempt
  Pool 2    has this DN configured for line 1
  Pool 7    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
  Auto answer is disabled
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  after-hour exempt
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:
  Auto answer is disabled
  call-forward b2bua all 678
  after-hour exempt
  Pool 1    has this DN configured for line 3
VOICE REGISTER TEMPLATE
=======================
Temp Tag 1
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  Dialplan Tag is 1
  softkey connected  Confrn
  Lpcor type none
  Pool 4 has this template configured
VOICE REGISTER DIALPLAN
=======================
Dialplan Tag 1
Config:
  Type is 7905-7912
  Template 1 has this dialplan configured
  Pool 4 has this dialplan configured
VOICE REGISTER POOL
===================
 Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Type is 7960
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone all is 4566
  call-forward b2bua all 4555
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 2
Config:
  Mac address is 0015.C68E.6D13
  Type is 7960
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone noan is 9886, timeout 98
  keep-conference is enabled
  username pool2 password lab
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
          
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 3
Config:
  Mac address is 0021.5553.8998
  Type is 7975
  Number list 1 : DN 3
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is enabled
  Busy trigger per button value is 0
  call-forward phone all is 45112
  call-forward b2bua all 45111
  after-hour exempt
  keep-conference is enabled
  kpml signal is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 4
Config:
  Mac address is 8989.9867.8769
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  template is 1
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 7
Config:
  Mac address is 0018.BAC8.D2B1
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

The following is
                              		  an example of a partial output of the show voice register all command, showing KEM data with the phone type
                              		  information:

```
Router# show voice register all Pool Tag 5
Config:
  Mac address is B4A4.E328.4698
  Type is 9971 addon 1 CKEM
  Number list 1 : DN 2
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Video is enabled
  Camera is enabled
  Busy trigger per button value is 0
  keep-conference is enabled
  registration expires timer max is 200 and min is 60
  kpml signal is enabled
  Lpcor Type is none
```

The following
                              		  is a sample output of the show voice register all command, showing the three KEMs configured
                              		  with phone type 9971:

```
Router# show voice register all Pool Tag 4
Config:
  Mac address is B4A4.E328.4698
  Type is 9971 addon 1 CKEM 2 CKEM 3 CKEM
  Number list 1 : DN 4
  Number list 2 : DN 5
  Number list 3 : DN 9
```

The following
                              		  table describes the significant fields shown in this output.

Field

Description

Pool
                                          					 Tag

Shows
                                          					 the assigned tag number of the current voice register pool.

Config

Shows
                                          					 the voice register pool.

Network
                                          					 address and Mask

Shows
                                          					 network address and mask information when the id command is configured.

Number
                                          					 list, Pattern, and Preference

Shows
                                          					 the number command configuration.

Proxy
                                          					 IP address

Shows
                                          					 the proxy command configuration.

Default
                                          					 preference

Shows
                                          					 the default preference value of this pool.

Incoming called number

Shows
                                          					 the incoming called-number command configuration.

Translate outgoing called tag

Shows
                                          					 the translate-outgoing command configuration.

Class
                                          					 of Restriction List Tag

Shows
                                          					 the COR tag.

Incoming corlist name

Shows
                                          					 the cor command
                                          					 configuration.

Application

Shows
                                          					 the application command configuration for this pool.

Dialpeers created

Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here.

Statistics

Shows
                                          					 the registration statistics for this pool.

Active
                                          					 registrations

Shows
                                          					 the current active registrations.

Total
                                          					 Registration Statistics

Shows
                                          					 the total registration statistics for this pool.

Registration requests

Shows
                                          					 the incoming registration requests.

Registration success

Shows
                                          					 the successful registrations.

Registration failed

Shows
                                          					 the failed registrations.

unRegister requests

Shows
                                          					 the incoming unregister/registration expire requests.

unRegister success

Reports
                                          					 the number of successful unregisters.

unRegister failed

Reports
                                          					 the number of failed unregisters.

### Related Commands

Command

Description

application (voice register pool)

Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment.

cor (voice register pool)

Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers.

id (voice register pool)

Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer.

number (voice register pool)

Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone.

proxy (voice register pool)

Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway.

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

translate-outgoing (voice register pool)

Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user.

## show voice
                        	 register credential

To display
                              		  configuration information associated with a credential file used for
                              		  authorization, use the show voice register credential command in privileged EXEC mode.

show voice register credential

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

## Examples

The following is
                              		  sample output from this command:

```
Router# show voice register credential username: Jsmith, password: 1234abc, service: PRESENCE , file index 3
username: Ksample, password: xyz1234, service: PRESENCE , file index 3
username: Mmore, password: updwssc, service: PRESENCE , file index 3
username: Sstove, password: 12bms, service: PRESENCE , file index 3
username: Yjones, password: 357llvrus, service: PRESENCE , file index 5
username: Yjones2, password: 55rrtuv, service: PRESENCE OOD_REFER , file index 5
username: vtemp, password: 1234567, service: PRESENCE , file index 5
```

The table contains
                              		  descriptions of fields shown in the output, listed in order of appearance.

Field

Description

username

Username
                                          					 that is authorized.

password

Password
                                          					 that is authorized.

service

Type of
                                          					 service for which the credential file is used; presence or Out-of-dialog REFER
                                          					 (OOD-R).

file
                                          					 index

Identification number of the credential file defined with the authenticate command.

### Related Commands

Command

Description

authenticate (voice register global)

Defines
                                          						the authenticate mode for SIP phones in a Cisco Unified CME system.

credential load

Reloads
                                          						a credential file into Flash memory.

show voice register all

Displays all Cisco Unified CME and Cisco Unified SIP SRST configurations and
                                          						register information.

## show voice register dial-peers

To display details of all dynamically created VoIP dial peers
                              		  associated with the Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) or Cisco Unified CallManager Express (Cisco
                              		  Unified CME) register event, use the show voice register dial-peers command in privileged EXEC mode.

show voice register dial-peers [ pool tag ]

### Syntax Description

pool tag

Number of entries in attempted registrations table. Size
                                          						range from 0 to 50.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1

This command was modified. Pool tag keyword- argument was
                                          						added. Command output display was also modified to display dial-peers specific
                                          						to a pool.

### Usage Guidelines

Use this command to display the dial-peers associated with a pool. To
                              		  display the dynamic dial-peers associated with a specific pool, use the pool
                              		  keyword followed by the pool tag. When using the pool keyword, you must specify
                              		  the pool tag.

## Examples

## Examples

The following is a sample output from this command displaying all
                              		  dial-peers:

```
Router#show voice register dial-peers
Dial-peers for Pool 1
dial-peer voice 40001 voip
 destination-pattern 45111
 session target ipv4:8.3.3.111:5060
 session protocol sipv2
 call-fwd-all         4555           
 after-hours-exempt   FALSE          
dial-peer voice 40002 voip
  destination-pattern 45113
  session target ipv4:8.33.33.111:5060
  session protocol sipv2
  after-hours-exempt   FALSE   
Dial-peers for Pool 2
 dial-peer voice 40003 voip
 destination-pattern 45112
 session target ipv4:8.33.33.112:5060
 session protocol sipv2
 call-fwd-noan-timeou 8              
 call-fwd-noan        999            
 after-hours-exempt   TRUE
```

## Examples

The following is a sample output from this command displaying all
                              		  statistical information related to pool 1:

```
Router# show voice register dial-peers pool 1 Dial-peers for Pool 1:
dial-peer voice 40004 voip
 destination-pattern 1000
 redirect ip2ip
 session target ipv4:9.13.18.40:19633
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40001 voip
 destination-pattern 2000
 redirect ip2ip
 session target ipv4:9.13.18.40:19634
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
```

## Examples

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with
                                          						the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register dialplan

To display all
                              		  configuration information for a specific SIP dial plan, use the show voice register dialplan command in privileged EXEC mode.

show voice register dialplan { tag | | all }

### Syntax Description

tag

Number
                                          						that identifies the SIP dialplan. Range: 1 to 24.

all

(Optional) Displays all the dialplans defined in a system.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was modified. All keyword was added. Pools and templates that have
                                          						dialplan configured are also displayed in the output.

### Usage Guidelines

Use this command
                              		  to verify the configuration of SIP dial plans. You define a dial plan with the voice register dialplan command and assign it to a SIP phone with
                              		  the dialplan command.

In Cisco Unified
                              		  CME 8.1 and later, show voice register dialplan command also displays the pools and templates that have the dialplan
                              		  configured. The pools which have the diaplan configured by virtue of inclusion
                              		  of a template is also displayed as part of the pool list display. If a dialplan
                              		  is configured under both template and pool, the dialplan under the pool takes
                              		  precedence and the pool is displayed.

When used with
                              		  the all keyword, the show voice register diaplan command displays configuration
                              		  information for all the dialplans defined in a system.

## Examples

The following is
                              		  sample output from this command displaying information for dialplan 1:

```
Router# show voice register dialplan 1 Dialplan Tag 1
Config:
  Type is 7905-7912
  Template 1 has this dialplan configured
  Pool 4 has this dialplan configured
```

The following is
                              		  a sample output from this command displaying information for all the dialplans
                              		  configured in a system:

```
Router# show voice register dialplan all Dialplan Tag 1
Config:
  Type is 7905-7912
  Pattern 1 is 9879, timeout is 0, user option is phone, button is default
  Pattern 24 is 908, timeout is 0, user option is phone, button is default
Dialplan Tag 2
Config:
  Type is 7940-7960-others
  Pattern 3 is 9845, timeout is 0, user option is phone, button is default
  Pattern 20 is 9098, timeout is 0, user option is phone, button is default
```

The table
                              		  contains descriptions of significant fields shown in this output, listed in
                              		  alphabetical order.

Field

Description

Config

List of
                                          					 configuration options defined for this SIP dial plan.

Dialplan Tag

Tag
                                          					 number of the requested SIP dial plan.

Pattern

Dial
                                          					 pattern defined for a SIP dial plan with the pattern command in voice register dialplan configuration mode.

Type

Phone
                                          					 type defined for a SIP dial plan with the type command.

### Related Commands

Command

Description

dialplan

Assigns a dial plan to a SIP phone.

pattern (voice register dialplan)

Defines a dial pattern for a SIP dial plan.

show voice register all

Displays all Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

type
                                          						(voice register dialplan)

Defines a phone type for a SIP dial plan.

voice register dialplan

Enters voice register dialplan configuration mode to define a dial plan for SIP
                                          						phones.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice
                        	 register dn

To display all
                              		  configuration information associated with a specific voice register dn, use the show voice register dn command in privileged EXEC mode.

show voice register dn { tag | all }

### Syntax Description

tag

Tag
                                          						number of the voice register dn for which to display information. Range is 1 to
                                          						750.

all

(Optional) Displays configuration information associated with all voice
                                          						register dns defined in a system.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4

This
                                          						command was introduced.

15.1(2)T

Cisco
                                          						CME 8.1 and Cisco SIP SRST 8.1

This
                                          						command was modified.The display output now shows pools that have DNs
                                          						configured under them. All keyword was added to show configuration information
                                          						for all voice register dns defined in system.

### Usage Guidelines

In Cisco Unified
                              		  CME 8.1 and Cisco Unified SIP SRST 8.1, the show voice register dn command
                              		  displays the pools that have the DNs configured under them. When used with all
                              		  keyword, the show voice register dn command displays configuration information
                              		  for all the DNs defined in a system.

## Examples

## Examples

The following is
                              		  a sample output from this command:

```
Router# show voice register dn 1
Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
```

## Examples

The following is
                              		  a sample output from this command:

```
Router# show voice register dn 2 Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
```

## Examples

The following is
                              		  a sample output from this command displaying information for all the dns:

```
Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 12
  Preference is 1
  Huntstop is enabled
  Allow watch is enabled
  Pool 2    has this DN configured for line 1, 2
```

## Examples

The following is
                              		  a sample output from this command displaying information for all the dns:

```
Router# show voice register dn all Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua noan 999 timeout 8
  after-hour exempt
  Pool 2    has this DN configured for line 1
  Pool 7    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687  
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687
  Pool 1    has this DN configured for line 1
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
  Auto answer is disabled
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  after-hour exempt
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:
  Auto answer is disabled
  call-forward b2bua all 678
  after-hour exempt
  Pool 1    has this DN configured for line 3
```

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

Auto
                                          					 answer

Status of
                                          					 auto-answer feature defined with the auto-answer command.

Config

List of
                                          					 configuration options defined for this voice register dn.

Dn Tag

Tag
                                          					 number of the requested voice register dn.

Huntstop

Status
                                          					 of huntstop behavior defined with the huntstop command.

Number

Telephone or extension number set with the number command in voice register dn configuration mode.

Preference

Preference order set with the preference command in voice register dn configuration mode.

### Related Commands

Command

Description

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show
                                          						voice register dn all

Displays information associated with all the dns configured in a system.

voice register dn

Enters voice register dn configuration mode to define an extension for a SIP
                                          						phone line.

## show voice
                        	 register global

To display all
                              		  global configuration parameters associated with Cisco Unified SIP IP phones,
                              		  use the show voice register global command in privileged EXEC mode.

show voice register global

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Privileged EXEC
                              		  (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was introduced.

15.0(1)XA

Cisco
                                          						SIP SRST 8.0

This
                                          						command was modified to display the signaling transport protocol.

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1

This
                                          						command was modified to include global statistics in the output display.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to include conference hardware in the output display.

## Examples

## Examples

The following is
                              		  a sample output from the show voice register global command used in Cisco Unified CME:

```
Router# show voice register global CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is cme
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  Source-address is 8.3.3.5 port 5060
  Time-format is 12
  Date-format is M/D/Y
  Time-zone is 5
  Hold-alert is disabled
  Mwi stutter is disabled
  Mwi registration for full E.164 is disabled
  Forwarding local is enabled
  Privacy is enabled
  Privacy-on-hold is disabled
  Dst auto adjust is enabled
    start at Apr week 1 day Sun time 02:00
    stop  at Oct week 8 day Sun time 02:00
  Max redirect number is 5
  IP QoS DSCP:
    ef (the MS 6 bits, 46, in ToS, 0xB8) for media
    cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
    af41 (the MS 6 bits, 34, in ToS, 0x88) for video
    default (the MS 6 bits, 0, in ToS, 0x0) for service
  Telnet Level: 0
  Tftp path is flash:
  Generate text file is disabled
  Tftp files are created, current syncinfo 0001140473454008
  OS79XX.TXT is not created
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

The following is
                              		  a sample output from the show voice register global command. The output shows that hardware
                              		  conferencing is enabled.

```
Router# show voice register global CONFIG [Version=8.7]
========================
  Version 8.7
  Mode is cme
  Max-pool is 50
  Max-dn is 100
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  Forced Authorization Code Refer is enabled
  Source-address is 1.5.40.20 port 5060
  Time-format is 12
  Date-format is M/D/Y
  Time-zone is 5
  Hold-alert is disabled
  Mwi stutter is disabled
  Mwi registration for full E.164 is disabled
  Forwarding local is enabled
  Video is enabled
  Camera is enabled
  Privacy is enabled
  Privacy-on-hold is disabled
  Conference hardware is enabled
  Dst auto adjust is enabled
start at Apr week 1 day Sun time 02:00
stop  at Oct week 8 day Sun time 02:00
```

## Examples

The following is
                              		  a sample output from the show voice register global command used in Cisco Unified SIP SRST:

```
Router# show voice register global CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is srst
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

Conference hardware

Shows
                                          					 whether the Cisco Unified SIP IP phone will perform local mixing on its own or
                                          					 request Cisco Unified CME to perform hardware conferencing using its DSP
                                          					 resource.

Date-format

Value
                                          					 of date-format command.

DST
                                          					 auto adjust

Setting
                                          					 of dst auto-adjust command.

Forwarding local

Setting
                                          					 of forwarding local command.

Generate text file

Setting
                                          					 of text file command.

Hold-alert

Setting
                                          					 of hold-alert command.

Load

Value
                                          					 of load command.

Max-dn

Reports
                                          					 the maximum number of SIP voice register directory numbers (DNs) supported by
                                          					 the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with
                                          					 the max-dn command. The maximum possible number is
                                          					 platform-dependent.

Max-pool

Reports
                                          					 the maximum number of SIP voice register pools supported by the Cisco Unified
                                          					 SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent.

Max
                                          					 redirect number

Maximum
                                          					 number of redirects set with the max-redirect command.

Mode

Reports
                                          					 the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST.

MWI
                                          					 registration

Setting
                                          					 of mwi command.

MWI
                                          					 stutter

Setting
                                          					 of mwi stutter command.

Time-format

Value
                                          					 of time-format command.

Time-zone

Number
                                          					 of the timezone selected with the timezone command.

TFTP
                                          					 path

Directory location of provisioning files for Cisco Unified SIP IP phones that
                                          					 is specified with the tftp-path command.

Version

Reports
                                          					 the Cisco Unified SIP SRST or Cisco Unified CME version number.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the Cisco Unified SIP IP phones currently registered with the
                                          						contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event.

voice register global

Enters voice register global configuration mode to set global parameters for
                                          						all supported Cisco Unified SIP IP phones in a Cisco Unified CME or Cisco
                                          						Unified SIP SRST environment.

## show voice register hfs

To display the HTTP File-Fetch Server (HFS) file bindings of firmware
                              		  files accessible to Cisco Unified SIP IP phones, use the show voice register hfs command in privileged EXEC mode.

show voice register hfs

### Syntax Description

This command has no arguments or keywords.

### Command Default

None

### Command Modes

Privileged EXEC

## Command History

Release

Modification

15.2(1)T

This command was introduced.

### Usage Guidelines

Use the show voice register hfs command with Cisco Unified CME 8.8 or a later
                              		  version.

This command displays the bindings of firmware files that are
                              		  accessible to Cisco Unified SIP IP phones using the HFS download service.

## Examples

The following is a sample output from the show voice register hfs command:

```
Router(config)# show voice register hfs Fetch Service Enabled = Y
   App enabled port = 6970
   Use default port = N
   Registered session-id = 19
 
Default home path = flash:/
   Ongoing fetches from home = 0
 
HTTP File Server Bindings
   No. of bindings = 11
   No. of url table entries = 9
   No. of alias table entries = 9
```

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profile files required for SIP
                                          						phones.

hfs enable

Enables the HFS download service on an IP Phone in a Cisco
                                          						Unified CME system.

## show voice
                        	 register pool

To display all
                              		  configuration information associated with a specific voice register pool, use
                              		  the show voice register pool command in privileged EXEC mode.

show voice register pool { pool-tag | all } [ brief ]

### Syntax Description

pool-tag

Tag
                                          						number of the voice register pool for which information is displayed. Range is
                                          						1 to 262.

all

Displays the information of all the voice register pools.

brief

(Optional) Displays brief information of all voice register pools.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1) Cisco Unified SIP SRST 4.2(1)

This
                                          						command was modified to include emergency response location information in the
                                          						output display.

12.4(20)T

Cisco
                                          						Unified CME 7.0 Cisco Unified SIP SRST 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the
                                          						output.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display.

15.2(4)M

Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1

This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display.

Cisco
                                          						IOS XE Everest 16.6.1

Unified SRST 12.0

This
                                          						command was modified to include the IPv6 address in the output display for
                                          						Unified SRST.

## Examples

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying information for voice
                              		  register pool 33 in Cisco Unified CME:

```
Router# show voice register pool 33 Pool Tag 33
Config:
 Mac address is 0009.B7F7.532E
 Type is 7960
 Number list 1 : DN 1
 Number list 2 : DN 2
 Number list 3 : DN 3
 Proxy Ip address is 0.0.0.0
 DTMF Relay is disabled
 Call Waiting is enabled
 DnD is disabled
 Busy trigger per button value is 0
 keep-conference is enabled
 template is 1
 Emergency response location 3
 Lpcor Type is local 
 Lpcor Incoming is sip_group
 Lpcor Outgoing is sip_group
 
 Transport type is udp 
 service-control mechanism is not supported 
 Privacy feature is not configured. 
 Privacy button is disabled 
 
Dialpeers created: 
 
Statistics: 
 Active registrations : 0 
 
 Total SIP phones registered: 0 
 Total Registration Statistics 
  Registration requests : 0 
  Registration success : 0 
  Registration failed : 0 
  unRegister requests : 0 
  unRegister success : 0 
  unRegister failed : 0
```

The following
                              		  is a sample output of the show voice register pool command. The output shows that a meet-me
                              		  hardware conference administrator has been assigned, the conference creator or
                              		  any of the participants can add a new participant, and the conference creator
                              		  can terminate the active video hardware conference by hanging up.

```
Router# show voice register pool 15 Pool Tag 15
Config:
  Mac address is 1C17.D340.81F0
  Type is 9951
  Number list 1 : DN 15
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-CP9951/9.0.1
  DTMF Relay is enabled, sip-notify
  Call Waiting is enabled
  DnD is disabled
  Video is enabled
  Camera is enabled
  Busy trigger per button value is 0
  feature-button 5 DnD
  feature-button 6 MeetMe
  keep-conference is enabled
  registration expires timer max is 86400 and min is 60
  template is 1
  kpml signal is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is supported
  registration Call ID is 1c17d340-81f00002-6c48fe8e-03013c10@1.5.40.105 
  Registration method: per line
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 3915
  contact IP address: 1.5.40.105 port 5060
  Phone SIS Version:  5.0.0
  GW SIS Version:  1.0.0
  conference admin: yes
  conference add mode: all
  conference drop mode: creator
  paging-dn: config 0 [multicast]  effective 0 [multicast]
...
```

The following
                              		  is an example of a partial output of the show voice register pool all command, showing KEM data with the phone type information:

```
Router# show voice register pool all Pool Tag 5
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM
Number list 1 : DN 2
Number list 2 : DN 3
Proxy Ip address is 0.0.0.0
DTMF Relay is disabled
Call Waiting is enabled
DnD is disabled
Video is enabled
Camera is enabled
Busy trigger per button value is 0
keep-conference is enabled
registration expires timer max is 200 and min is 60
kpml signal is enabled
Lpcor Type is none
```

The following
                              		  is a sample output of the show voice register pool all command, showing the three KEMs configured
                              		  with phone type 9971:

```
Router# show voice register pool all Pool Tag 4
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM 2 CKEM 3 CKEM
Number list 1 : DN 4
Number list 2 : DN 5
Number list 3 : DN 9
```

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying all information for voice register pool 1
                              		  in Cisco Unified SIP SRST:

```
Router# show voice register pool 1 Pool Tag 1
Config:
 Network address is 192.168.0.0, Mask is 255.255.0.0
 Number list 1 : Pattern is 50.., Preference is 2
 Proxy Ip address is 0.0.0.0
 Default preference is 2
 Incoming called number is 
 Translate outgoing called tag is 1
 Class of Restriction List Tag: default
 Incoming corlist name is allowall
 Application is default.new
 
Dialpeers created:
 
dial-peer voice 40007 voip
 application default.new
 corlist incoming allowall
 preference 2
 incoming called-number 5001
 destination-pattern 5001
 redirect ip2ip
 session target ipv4:192.168.0.3
 session protocol sipv2
 translate-outgoing called 1
 voice-class codec 1
 
Statistics:
 Active registrations : 2
 
 Total Registration Statistics
  Registration requests : 48
  Registration success : 48
  Registration failed : 0
  unRegister requests : 46
  unRegister success : 46
  unRegister failed : 0
 
Emergency response location 6
```

## Examples

The following is a sample output of the show voice register pool brief command, showing an IPv6 source address
                              		  configured on a Cisco SIP IP Phone:

```
Router# show voice register pool brief Pool ID                        IP Address                 Ln DN  Number     State
==== ========================  ========================== == === ========== ============
1    8.0.0.0                                                                UNREGISTERED
2    2001:420:54FF:13::312:0   2001:420:54FF:13::312:1           10001$     REGISTERED
```

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying voice-class stun-usage information for
                              		  voice register pool 51:

```
Router# show voice register pool 51 Pool Tag 51
Config:
  Mac address is 0011.209F.5D60
  Type is 7960
  Number list 1 : DN 51
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-SIPGateway/IOS-12.x
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  template is 10
  Lpcor Type is none
  
Transport type is udp
  service-control mechanism is not supported
  registration Call ID is 2BA38EE3-17D311DB-800BCD81-A9AD11F0
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 16263646
  contact IP address: 192.168.0.87 port 5060
  Reason for unregistered state:
         No registration request since last reboot/unregister
  voice-class stun-usage is enabled. tag is 1
Dialpeers created:
Dial-peers for Pool 51:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 2
    Registration success   : 2
    Registration failed    : 0
    unRegister requests    : 2
    unRegister success     : 2
    unRegister failed      : 0
    Attempts to register
           after last unregister : 0
    Last register request time   : 13:43:27.839 IST Tue Apr 20 2010
```

The following
                              		  table contains descriptions of significant fields shown in the Cisco Unified
                              		  CME and Cisco Unified SIP SRST output, listed in alphabetical order.

Field

Description

Active
                                          					 registrations

Shows
                                          					 the current active registrations.

Application

Shows
                                          					 the application command configuration for this pool.

Call
                                          					 Waiting

Shows
                                          					 the call-waiting command configuration.

Class
                                          					 of Restriction List Tag

Shows
                                          					 the COR tag.

Conference add mode

Shows
                                          					 the current setting of the hardware conference privilege for adding
                                          					 participants.

Conference admin

Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not.

Conference drop mode

Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up.

Config

Shows
                                          					 the voice register pool.

Default
                                          					 preference

Shows
                                          					 the default preference value of this pool.

Dialpeers created

Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here.

DnD

Shows
                                          					 the setting of the dnd-control command.

DTMF
                                          					 Relay

Shows
                                          					 the setting of the dtmf-relay command.

Emergency response location

Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made.

Incoming called number

Shows
                                          					 the incoming called-number command configuration.

Incoming corlist name

Shows
                                          					 the cor command
                                          					 configuration.

keep-conference

Shows
                                          					 the status of the keep-conference command.

Lpcor
                                          					 Incoming

Shows
                                          					 the setting of the lpcor incoming command.

Lpcor
                                          					 Outgoing

Shows
                                          					 the setting of the lpcor outgoing command.

Lpcor
                                          					 Type

Shows
                                          					 the setting of the lpcor type command.

Mac
                                          					 address

Shows
                                          					 the MAC address of the Cisco Unified SIP IP phone as defined by the id command.

Network
                                          					 address and Mask

Shows
                                          					 network address and mask information when the id command is configured.

Number
                                          					 list, Pattern, and Preference

Shows
                                          					 the number command configuration.

Pool
                                          					 Tag

Shows
                                          					 the assigned tag number of the current pool.

Proxy
                                          					 IP address

Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server.

Registration failed

Shows
                                          					 the failed registrations.

Registration requests

Shows
                                          					 the incoming registration requests.

Registration success

Shows
                                          					 the successful registrations.

Statistics

Shows
                                          					 the registration statistics for this pool.

Template

Shows
                                          					 the template-tag number for the template applied to the Cisco Unified SIP IP
                                          					 phone.

Total
                                          					 Registration Statistics

Shows
                                          					 the total registration statistics for this pool.

Translate outgoing called tag

Shows
                                          					 the translate-outgoing command configuration.

Type

Shows
                                          					 the phone type identified for the Cisco Unified SIP IP phone using the type command.

unRegister failed

Reports
                                          					 the number of failed unregisters.

unRegister requests

Shows
                                          					 the incoming unregister/registration expiry requests.

unRegister success

Reports
                                          					 the number of successful unregisters.

Username Password

Shows
                                          					 the values within the authentication credential.

### Related Commands

Command

Description

application (voice register pool)

Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment.

call-waiting (voice register pool)

Enables the call-waiting option on a SIP phone.

cor (voice register pool)

Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers.

dnd-control (voice register template)

Enables the Do-Not-Disturb (DND) soft key on SIP phones.

dtmf-relay (voice register pool)

Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints.

id (voice register pool)

Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer.

keep-conference (voice register pool)

Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected.

lpcor incoming

Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy.

lpcor outgoing

Associates an outgoing call with an LPCOR resource-group policy.

lpcor type

Specifies the LPCOR type for an IP phone.

number (voice register pool)

Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone.

proxy (voice register pool)

Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway.

show sip-ua status registrar

Displays all the Cisco Unified SIP IP phones registered with the contact
                                          						address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peer

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified CME or Cisco Unified SIP SRST register event.

translate-outgoing (voice register pool)

Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user.

type (voice register pool)

Defines a phone type for a SIP phone.

voice register pool

Enters voice register pool configuration mode for Cisco Unified SIP IP phones.

## show voice
                        	 register pool after-hour-exempt

To display the
                              		  details of a phone that has after-hour-exempt enabled on it, use the show voice register after-hour-exempt command in privileged EXEC mode.

show voice register after-hour-exempt

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Version

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of a phone that has after-hour-exempt enabled.
                              		  Individual phones can be exempted from call blocking using the after-hour
                              		  exempt.

## Examples

The following is
                              		  a sample output from this command displaying information for phones with after
                              		  after-hour-exempt:

```
Router# show voice register pool after-hour-exempt Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       3  8                        UNREGISTERED
                                     4  7   451110               UNREGISTERED
2    0015.C68E.6D13                  1  2   45112                UNREGISTERED
3    0021.5553.8998                  1  3   45113                UNREGISTERED
                                     2  3   45113                UNREGISTERED
7    0018.BAC8.D2B1                  1  2   45112                UNREGISTERED
```

## Examples

The following is
                              		  a sample output from this command displaying information for phones with after
                              		  after-hour-exempt:

```
Router# show voice register pool after-hour-exempt
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    9.13.18.40      9.13.18.40      1  1   1000                 REGISTERED  
                                     2  2   2000                 REGISTERED  
                                     3  3   3000                 REGISTERED  
                                     4  4   4000                 REGISTERED  
                                     5  5   5000                 UNREGISTERED
                                     6  6   6000                 UNREGISTERED
                                     7  7   7000                 UNREGISTERED
```

The table
                              		  contains descriptions of significant fields shown in this output, listed in
                              		  alphabetical order.

Field

Description

DN

Directory
                                          					 number of the phone.

IP
                                          					 Address/port

IP
                                          					 address and port number of the phones.

LN

Line
                                          					 number of the phone.

Number

Number of
                                          					 the phones that have after-hour exempt enabled.

Pool

Shows the
                                          					 current pool.

State

Registration state.

### Related Commands

Command

Description

after-hour exempt(voice register pool)

Specifies that an IP phone does not have any of its outgoing calls blocked
                                          						although call blocking is defined.

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register
                                          						information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool attempted-registrations

To display the details of phones that attempt to register with Cisco
                              		  Unified CME or Cisco Unified SRST and fail, use the show voice register pool attempted-registrations command in privileged EXEC mode.

show voice register pool attempted-registrations

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phones that attempt to
                              		  register with Cisco Unified CME or Cisco Unified SRST and fail. If the phone
                              		  registers successfully after some time, the attempted registration entry will
                              		  still show up in the attempted-registration table. Use the clear voice register
                              		  attempted-registrations command to remove the entry from the attempted
                              		  registration table.

## Examples

The following is a sample output from this command displaying
                              		  information for show voice register pool attempted-registrations:

```
Router# show voice register pool attempted-registrations Phones that have attempted registrations and have failed:
 MAC address: 001b.535c.d410 
 IP address : 8.3.3.111 
 Attempts   : 5
 Time of first attempt : *10:49:51.542 UTC Wed Oct 14 2009
 Time of latest attempt: *10:50:00.886 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
 MAC address: 0015.c68e.6d13 
 IP address : 8.33.33.112 
 Attempts   : 4
 Time of first attempt : *10:49:53.418 UTC Wed Oct 14 2009
 Time of latest attempt: *10:50:00.434 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
 MAC address: 0009.43E9.0B35 
 IP address : 9.13.40.83 
 Attempts   : 1
 Time of first attempt : *10:49:57.866 UTC Wed Oct 14 2009
 Time of latest attempt: *10:49:57.866 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
```

The following is a sample output from this command displaying
                              		  information for show voice register pool attempted-registrations when none of
                              		  the phones fail:

```
Router# show voice register pool attempted-registrations         
 Phones that have attempted registrations and have failed: NONE
```

### Related Commands

Command

Description

attempted-registrations size

Allows to set the size of the table that stores information
                                          						related to SIP phones that attempt to register and fail.

clear voice register attempted-registrations

Clears entries from the attempted-registration table.

## show voice
                        	 register pool cfa

show voice register pool cfa

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

15.1(2)T

Cisco
                                       					 Unified CME 8.1

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to display the voice register pool details of the phone with CFA feature
                              		  enabled. When Call Forward All feature is enabled on Cisco Unified SIP IP
                              		  phones such as 7940, 7941, 7941GE, 7942, 7945, 7960, 7961, 7961GE, 7962, 7965,
                              		  7970, 7971, 7975 through the CFA phone button. The show voice register pool
                                    				cfa command displays only the call forward all B2BUA details.

The show voice register pool cfa command also
                              		  displays the line number and DN number if available under the pool
                              		  configuration. If call-forward-all is configured under both pool and DN. the
                              		  configuration under DN takes precedence.

## Examples

The following is a
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool cfa
Pool 	Ln 	DN 	Number 	Call Forward All Number
==== 	== 	== 	====== 	========================
1 				2 		8 										678
						0			1 	45111 			4555
						4 		7 	451110 		4555
3 				1 		3 	45113 			87687
						2 		3 	45113 			87687
```

The table contains
                              		  descriptions of significant fields shown in this output, listed in alphabetical
                              		  order.

Call
                                       					 Forward All Number

Number to
                                       					 which the calls are forwarded.

DN

Voice
                                       					 register DN tag of the line.

LN

Line
                                       					 number of the telephone number.

Pool

Tag ID of
                                       					 the pool.

### Related Commands

Command

Description

call forward b2bua all

Enables
                                          						call forward all.

show voice register all

Displays
                                          						all Cisco Unified SIP SRST and Cisco Unified CME configurations and register
                                          						information.

show voice register pool

Displays
                                          						all configuration information associated with a particular voice register pool.

show voice register pool detail all

Displays
                                          						the details of all the pools defined in the system.

## show voice register pool connected

To display the details of SIP phones that are in connected state, use
                              		  the show voice register pool connected command in privileged EXEC mode.

show voice register pool connected [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are in
                                          						connected state.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently in connected state (in conversation). The output for show voice
                              		  register pool connected command shows details of both calls originating from
                              		  the SIP phones and calls made towards SIP phones. When used with brief keyword,
                              		  the show voice register pool connected command displays a brief detail of
                              		  phones in connected state.

Cisco Unified CME and Cisco Unified SRST

The following is sample output from this command displaying all
                              		  statistical information:

```
Router# show voice register pool connected Outbound calls from SIP line phones: 
Pool tag: 1
==============
 MAC Address    : 001B.535C.D410
 Contact IP     : 8.3.3.111
 Phone Number   : 45111
 Remote Number  : 45112
Call 2
SIP Call ID                : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC0401C 0x100 0x4
   CC Call ID              : 7
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.3.3.111]:5060
   Destn SIP Resp Addr:Port: [8.3.3.111]:50076
   Destination Name        : 8.3.3.111
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:17580
     Media Dest IP Addr:Port  : [8.3.3.111]:26298
Options-Ping    ENABLED:NO    ACTIVE:NO
Inbound calls to SIP line phones: 
          
Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
Call 3
SIP Call ID                : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC04018 0x100 0x80
   CC Call ID              : 8
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16384
     Media Dest IP Addr:Port  : [8.33.33.112]:30040
```

The following is sample output from this command displaying brief
                              		  statistical information:

```
Router# show voice register pool connected brief Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
1    8.3.3.111       45111                45112               
Inbound calls to SIP line phones: 
Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
2    8.33.33.112     45112                45111
```

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register pool ip

To display the
                              		  details of a SIP phone with a specific IP address, use the show voice register pool ip command in privileged EXEC mode.

show voice register pool ip ip-address

### Syntax Description

ip-address

IPv4
                                          						address of the SIP phone .

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of a phone with a specific IP-address. When the pool ID
                              		  is configured as a mac address or an IP address the registered pools contain
                              		  the IP address information. The pool information is displayed if the IP
                              		  addresses match.

When the pool ID
                              		  is IP and the pool is unregistered, IP address configured under pool is
                              		  compared with the input IP. When the pool ID is network contact, the IP address
                              		  of each phone that is registered is compared with the input IP address.

## Examples

The following is
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool ip 8.3.3.111 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       1  1   45111                REGISTERED  
                                     4  7   451110               UNREGISTERED
```

The table contains
                              		  descriptions of significant fields shown in this output, listed in alphabetical
                              		  order.

Field

Description

DN

Voice
                                          					 register DN tag of the line.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address of the SIP phone.

LN

Line
                                          					 number of the telephone number.

Number

Number of
                                          					 the phones that have a mac address.

Pool

Tag ID of
                                          					 the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice
                        	 register pool mac

To display the
                              		  details of voice register pool associated with a specific phone type, use the show voice register pool mac command in privileged EXEC mode.

show voice register pool mac H . H . H

### Syntax Description

H.H.H

MAC
                                          						address of the SIP phone attempting to register.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of the phone with the mac address H.H.H. The command
                              		  displays only the pools that are configured with an ID as mac.

## Examples

The following is
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool mac 001B.535C.D410 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       1  1   45111                REGISTERED  
                                     4  7   451110               UNREGISTERED
```

The table
                              		  contains descriptions of significant fields shown in this output, listed in
                              		  alphabetical order.

Field

Description

DN

Voice
                                          					 register DN tag of the line.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address of the SIP phone.

LN

Line
                                          					 number of the telephone number.

Number

Number of
                                          					 the phones that have a mac address.

Pool

Tag ID of
                                          					 the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice register pool on-hold

To display the details of phones that are currently on-hold, use the show voice register pool oh-hold command in privileged EXEC mode.

show voice register pool on-hold [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are
                                          						currently on-hold.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently on-hold. The show voice register pool on-hold command output also
                              		  displays a field to show if the hold was a locally initiated hold (initiated on
                              		  the phone) or if the hold was initiated on the remote end. When used with brief
                              		  keyword, the show voice register pool on-hold command displays a brief
                              		  information of the phones that are currently put on hold by the remote caller
                              		  or have put the remote caller on hold. The “Hold-Origin” field specifies the
                              		  type of the hold, which can be either remote or local. Local indicates that the
                              		  call is placed on hold by the local phone and remote indicates that call is
                              		  placed on hold by the remote phone. In case of double-hold, the hold origin
                              		  will display the value “Local and Remote”.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool on-hold brief Outbound calls from SIP line phones: 
Pool IP Address      Number               Remote Number        Hold Origin
==== =============== ==================== ==================== ==============
1    8.3.3.111       45111                45112                Remote & Local
Inbound calls to SIP line phones: 
Pool IP Address      Number               Remote Number        Hold Origin
==== =============== ==================== ==================== ==============
2    8.33.33.112     45112                45111                Remote & Local
```

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones on-hold:

```
Router# show voice register pool on-hold Outbound calls from SIP line phones: 
Pool tag: 1
==============
 MAC Address    : 001B.535C.D410
 Contact IP     : 8.3.3.111
 Phone Number   : 45111
 Remote Number  : 45112
 Local Hold     : CALL HOLD Pressed on SIP Phone
Call 4
SIP Call ID                : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC0401C 0x10100 0x4
   CC Call ID              : 7
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.3.3.111]:5060
   Destn SIP Resp Addr:Port: [8.3.3.111]:50076
   Destination Name        : 8.3.3.111
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:17580
     Media Dest IP Addr:Port  : [8.3.3.111]:26298
Options-Ping    ENABLED:NO    ACTIVE:NO
Inbound calls to SIP line phones: 
Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
 Remote Hold    : SIP Phone has received CALL HOLD
Call 5
SIP Call ID                : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC04018 0x4100 0x80
   CC Call ID              : 8
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16384
     Media Dest IP Addr:Port  : [8.33.33.112]:30040
Options-Ping    ENABLED:NO    ACTIVE:NO
```

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice register pool phone-load

To display the details of phone-loads associated with phones that are
                              		  registered to Cisco Unified CME, use the show voice register pool phone-load command
                              		  in privileged EXEC mode.

show voice register pool phone-load

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone-loads associated
                              		  with phones that are registered with Cisco Unified CME. The phone-load
                              		  information is taken from the REGISTER message sent by the phone.

## Examples

The following is a sample output from this command displaying
                              		  information for voice register pool phone-load:

```
Router# show voice register pool phone-load
Pool	 Device Name 				Current Version Previous Version
==== 	=========== 				================= ===================
1 				SEP001B535CD410 Cisco-CP7960G/8.0
```

### Related Commands

Command

Description

load(voice register global)

Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file.

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## show voice
                        	 register pool registered

To display the
                              		  details of phones that successfully register to Cisco Unified Communications
                              		  Manager Express (Cisco Unified CME), use the show voice register pool registered command in privileged EXEC mode.

show voice register pool registered

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Version

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

15.2(4)M

Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1

This
                                          						command was modified to display Key Expansion Module (KEM) details with the
                                          						phone type information.

### Usage Guidelines

Use the show voice register pool registered command to display the details of
                              		  phones that are successfully registered to Cisco Unified CME and Cisco Unified
                              		  Survivable Remote Site Telephony (Cisco Unified SRST).

## Examples

The following is
                              		  a sample output displaying information for a registered voice register pool in
                              		  Cisco Unified CME:

```
Router# show voice register pool registered Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Type is 7960
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-CP7960G/8.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone all is 4566
  call-forward b2bua all 4555
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is supported
  registration Call ID is 001b535c-d410790d-17a6877e-5d04bbc5@8.3.3.111 
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 45111
  contact IP address: 8.3.3.111 port 5060
Dialpeers created:
Dial-peers for Pool 1:
dial-peer voice 40001 voip
 destination-pattern 45111
 session target ipv4:8.3.3.111:5060
 session protocol sipv2
  call-fwd-all         4555           
  after-hours-exempt   FALSE          
Statistics:
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : *11:40:32.263 UTC Wed Oct 14 2009 
    Last unregister request time : 
    Register success time        : *11:40:32.267 UTC Wed Oct 14 2009 
    Unregister success time      :
```

The following is
                              		  a sample output displaying information for a registered voice register pool
                              		  with a Cisco Unified 9971 Session Initiation Protocol (SIP) IP phone attached
                              		  to a Cisco SIP IP Phone CKEM 36-Button Line Expansion Module:

```
Router# show voice register pool registered Pool Tag 5
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM
Number list 1 : DN 2
Number list 2 : DN 3
Proxy Ip address is 0.0.0.0
DTMF Relay is disabled
Call Waiting is enabled
DnD is disabled
Video is enabled
Camera is enabled
Busy trigger per button value is 0
keep-conference is enabled
registration expires timer max is 200 and min is 60
kpml signal is enabled
Lpcor Type is none
```

## Examples

```
The following is a sample output displaying information for a registered voice register pool in Cisco Unified SRST:
Router# show voice register pool registered Pool Tag 1
Config:
  Ip address is 9.13.18.40, Mask is 255.255.0.0
  Number list 1 : DN 1
  Number list 2 : DN 2
  Number list 3 : DN 3
  Number list 4 : DN 4
  Number list 5 : DN 5
  Number list 6 : DN 6
  Number list 7 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is enabled, rtp-nte, sip-notify
  kpml signal is enabled
  Lpcor Type is none
Dialpeers created:
Dial-peers for Pool 1:
dial-peer voice 40004 voip
 destination-pattern 1000
 redirect ip2ip
 session target ipv4:9.13.18.40:19633
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40001 voip
 destination-pattern 2000
 redirect ip2ip
 session target ipv4:9.13.18.40:19634
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40002 voip
 destination-pattern 3000
 redirect ip2ip
 session target ipv4:9.13.18.40:19635
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40003 voip
 destination-pattern 4000
 redirect ip2ip
 session target ipv4:9.13.18.40:19636
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
Statistics:
  Active registrations  : 4
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 4
    Registration success   : 4
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : .05:22:55.604 UTC Tue Oct 6 2009 
    Last unregister request time : 
    Register success time        : .05:22:55.604 UTC Tue Oct 6 2009 
    Unregister success time      :
```

The following
                              		  table contains descriptions of significant fields shown in the show voice register pool registered command output, listed in alphabetical
                              		  order.

Field

Description

Active
                                          					 registrations

Shows the
                                          					 current active registrations.

Application

Shows the application command configuration for this pool.

Call
                                          					 Waiting

Shows the
                                          					 setting of the call-waiting command.

Class
                                          					 of Restriction List Tag

Shows
                                          					 the COR tag.

Config

Shows
                                          					 the voice register pool.

Current
                                          					 phone-load

Shows
                                          					 the current version of the phone load.

Default
                                          					 preference

Shows
                                          					 the default preference value of this pool.

Dialpeers created

Results
                                          					 in a list of all dial peers created and their contents. Dial-peer contents
                                          					 differ for each application and are not described here.

DnD

Shows
                                          					 the setting of the dnd-control command.

DTMF
                                          					 Relay

Shows
                                          					 the setting of the dtmf-relay command.

Emergency response location

Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made.

Incoming called number

Shows
                                          					 the incoming called-number command configuration.

Incoming corlist name

Shows
                                          					 the cor command
                                          					 configuration.

keep-conference

Shows
                                          					 the status of the keep-conference command.

Lpcor
                                          					 Incoming

Shows
                                          					 the setting of the lpcor incoming command.

Lpcor
                                          					 Outgoing

Shows
                                          					 the setting of the lpcor outgoing command.

Lpcor
                                          					 Type

Shows
                                          					 the setting of the lpcor type command.

Mac
                                          					 address

Shows
                                          					 the MAC address of this SIP phone as defined by the id command.

Network
                                          					 address and Mask

Shows
                                          					 network address and mask information when the id command is configured.

Number
                                          					 list, Pattern, and Preference

Shows
                                          					 the number command configuration.

Pool
                                          					 Tag

Shows
                                          					 the assigned tag number of the current pool.

Previous phone-load

Shows
                                          					 the version of the previous phone load.

Proxy
                                          					 IP address

Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server.

Registration failed

Shows
                                          					 the failed registrations.

Registration requests

Shows
                                          					 the incoming registration requests.

Registration success

Shows
                                          					 the successful registrations.

Statistics

Shows
                                          					 the registration statistics for this pool.

statistics time-stamps

Shows
                                          					 the registration statistics for this pool with specific time stamps.

Template

Shows
                                          					 the template-tag number for the template applied to this SIP phone.

Total
                                          					 Registration Statistics

Shows
                                          					 the total registration statistics for this pool.

Translate outgoing called tag

Shows
                                          					 the translate-outgoing command configuration.

Type

Shows
                                          					 the phone type identified for this SIP phone using the type command.

unRegister failed

Reports
                                          					 the number of failed unregisters.

unRegister requests

Shows
                                          					 the incoming unregister/registration expiry requests.

unRegister success

Reports
                                          					 the number of successful unregisters.

Username Password

Shows
                                          					 the values within the authentication credential.

### Related Commands

Command

Description

application (voice register pool)

Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment.

call-waiting (voice register pool)

Enables the call-waiting option on a SIP phone.

cor (voice register pool)

Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers.

dnd-control (voice register template)

Enables the Do-Not-Disturb (DND) soft key on SIP phones.

dtmf-relay (voice register pool)

Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints.

id (voice register pool)

Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer.

keep-conference (voice register pool)

Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected.

lpcor incoming

Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy.

lpcor outgoing

Associates an outgoing call with an LPCOR resource-group policy.

lpcor type

Specifies the LPCOR type for an IP phone.

number (voice register pool)

Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone.

proxy (voice register pool)

Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show voice register pool unregistered

Displays the details of voice register pools that do not have any phones
                                          						registered.

translate-outgoing (voice register pool)

Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user.

type (voice register pool)

Defines a phone type for a SIP phone.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice
                        	 register pool remote

To display the
                              		  details of phones that are at a remote location, use the show voice register pool
                                    				remote command in privileged EXEC mode.

show voice register pool remote

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

15.1(2)T

Cisco
                                       					 Unified CME 8.1

Cisco
                                       					 Unified SRST 8.1

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of the phones that are at remote location and do not
                              		  have an address resolution protocol (ARP) entry. If the pool id is MAC or IP,
                              		  the entire pool detail is displayed in a brief format. If the pool id is
                              		  network, only the line details with remote contact IP address are displayed. In
                              		  Cisco Unified SRST, if the pool id is IP and if the pool is not registered, the
                              		  configured IP is checked to see if it is a remote IP.

## Examples

The following is a
                              		  sample output from this command displaying information for remote phones:

```
Router# show voice register pool remote Pool ID 	            IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410 8.3.3.111 	      1  1  45111      	 	        REGISTERED
																																					3  8                        UNREGISTERED
																																					4  7  451110                UNREGISTERED
2    8.3.3.112                       1  2  45112                 REGISTERED
3    8.3.0.0                         1  3  45113                 REGISTERED
```

## Examples

The following is a
                              		  sample output from this command displaying information for remote phones:

```
Router# show voice register pool remote Pool ID 	            IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1 			001B.535C.D410  8.33.33.111      1  1  45111                REGISTERED
																																						3  8 				                  UNREGISTERED
																																						4  7  451110               UNREGISTERED
2    8.33.33.112     8.33.33.112      1  2  45112                REGISTERED
3    8.3.0.0         8.3.44.116       1  3  45113                REGISTERED
```

The table contains
                              		  descriptions of significant fields shown in this output, listed in alphabetical
                              		  order.

### Related Commands

Command

Description

show voice register all voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register
                                          						information.

show voice register dial-peer

Displays
                                          						details of all dynamically created VoIP dial peers associated with the Cisco
                                          						SIP SRST or Cisco CME register event.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

voice register pool

Enters
                                          						voice register pool configuration mode for SIP phones.

## show voice register pool ringing

To display the details of phones that are currently in ringing state,
                              		  use the show voice register pool ringing command in privileged EXEC mode.

show voice register pool ringing [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are
                                          						currently in ringing state.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently in ringing state. When used with the brief keyword, the show voice
                              		  register pool ringing brief command only displays information related to calls
                              		  that are bound towards the SIP phones.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool ringing brief Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
2    8.33.33.112     45112                45111
```

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool ringing Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
Call 1
SIP Call ID                : C0B5DA7-ADA311DE-8011803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_RECD_PROCEEDING (4)
   Substate of the call    : SUBSTATE_PROCEEDING_PROCEEDING (2)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC00018 0x100 0x280
   CC Call ID              : 5
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 5
     Stream Type              : voice+dtmf (1)
     Stream Media Addr Type   : 1
     Negotiated Codec         : No Codec    (0 bytes)
     Codec Payload Type       : 255 (None)
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16882
```

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register pool telephone-number

To display the
                              		  details of a phone line with a specific telephone-number, use the show voice register pool telephone-number command in privileged EXEC mode.

show voice register pool telephone-number number

### Syntax Description

number

Number
                                          						identifying a specific phone.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of the phone line with the specified telephone-number.
                              		  If the line is registered, the contact ip address will be displayed. When the
                              		  phone line is not registered and the pool ID type is network IP, the IP address
                              		  is not displayed. When the phone line is not registered but some other line is
                              		  registered for the same pool with MAC or IP address, then the IP address is
                              		  displayed.

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register pool telephone number 45112 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
2    0015.C68E.6D13                  1  2   45112                UNREGISTERED
7    0018.BAC8.D2B1                  1  2   45112                UNREGISTERED
```

## Examples

```
Router# show voice register pool telephone-number 1000
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    9.13.18.40      9.13.18.40      1  1   1000                 REGISTERED
```

The table contains
                              		  descriptions of significant fields shown in this output, listed in alphabetical
                              		  order.

Field

Description

DN

Directory
                                          					 number of the phone.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address and port number of the phones

LN

Line
                                          					 number of the phone.

Number

Number of
                                          					 the phones.

Pool

Shows the
                                          					 current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show
                                          						voice register pool detail all

Displays the details of all the pools defined in the system.

## show voice
                        	 register pool type

To display the
                              		  details of voice register pools associated with a specific phone type, use the show voice register pool type command in privileged EXEC mode.

show voice register pool type type

### Syntax Description

type

3911, 3951, 7905, 7906, 7911, 7912, 7940, 7941, 7941GE, 7942, 7945, 7960, 7961, 7961GE, 7962, 7965, 7970, 7971, 7975, 7800
                                          Series, 8800 Series, ATA (Cisco SIP Phone ATA), ATA-191, CKEM (Cisco SIP Key Expansion Module), CP-8800-Audio (Cisco SIP Key
                                          Expansion Module), CP-8800-Video (Cisco SIP Key Expansion Module), P100 (PingTel Xpressa 100), P600 (Polycom SoundPoint 600).

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was introduced.

15.2(4)M

Cisco
                                          						Unified CME 9.1

This
                                          						command was modified to add CKEM as a value for the type argument
                                          						to display the details of voice register pools associated with all the phones
                                          						configured with KEMs.

15.3(3)M

Cisco Unified CME 10.0

This command was enhanced to display the properties for new
                                          						sip phone models configured using SIP fast track feature.

New keyword option all was added to display all the
                                          						phone models being used in the system along with the associated pools and
                                          						registration details.

Cisco IOS XE Gibraltar 16.10.1a

Unified CME 12.5

This command was modified to add CP-8800-Audio and CP-8800-Video as values for the type argument to display the details of voice register pools associated with A-KEMs and V-KEMs.

Cisco IOS XE Gibraltar 16.10.1a

Unified CME 12.5

This command was modified to add ATA-191 as the value for the type argument to display the details of voice register pools associated with Cisco ATA 191.

### Usage Guidelines

Use the show voice register pool type command to display the details of voice register pools
                              		  associated with a specific phone type.

The show voice register pool type command only takes the configured value of the phone type into
                              		  consideration.

The CKEM value is
                              		  available for Cisco Unified CME only and is not available for Cisco Unified
                              		  SRST.

## Examples

The following is
                              		  a sample output of the show voice register pool type command for a Cisco Unified 7960 SIP IP
                              		  phone, displaying all statistical information:

```
Router# show voice register pool type 7960 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       1  1   45111                REGISTERED  
                                     4  7   451110               UNREGISTERED
2    0015.C68E.6D13                  1  2   45112                UNREGISTERED
```

The following is a sample output of the show voice register pool type command, showing all the phones configured with CP-8800-Audio:

```
Router# show voice register pool type CP-8800-Audio Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
2    38ED.18AF.8993  8.55.0.199      1   2   7001$               REGISTERED
```

The following is a sample output of the show voice register pool type command, showing all the 8865 phones configured with CP-8800-Video:

```
Router# show voice register pool type CP-8800-Video Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
4    00CC.FC99.8973  8.55.0.88      1   1   5001$                REGISTERED
```

The following is a sample output of the show voice register pool type command, showing all the phones configured with CKEM:

```
Router# show voice register pool type CKEM Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
4    B4A4.E328.4698  9.45.31.111     1  4   5589$                REGISTERED
```

The following is a sample output of the show voice register pool type command for a Cisco Unified 7821 SIP IP phone
                              		  configured using SIP fast track feature, displaying all statistical
                              		  information:

```
Router# show voice register pool type 7821 FastTrack Phone Model : 7821
Pooltype(index) representing the phone model : 48
Reference pooltype to inherit the properties from : 6921
Number of lines supported : 2 (inherited from 6921)
Number of addon modules supported : 0 (inherited from 6921)
Default session transport : UDP (inherited from 6921)
Description(helpstring) : Cisco IP Phone 7821
Phone supports GSM : NO (inherited from 6921)
Phone supports Telnet acess : NO (inherited from 6921)
Phone supports firmware download from CME : YES (inherited from 6921)
Phone specific XML tags :
<maxNumCalls>12</maxNumCalls> (inherited from 6921)
<busyTrigger>12</busyTrigger> (inherited from 6921)
Phone family : RTL_PHONES
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
6    D824.BD27.9EAC  9.44.29.44      1  6   4080$                REGISTERED
```

The following is a sample output of the show voice register pool type all command, showing all the phone models
                              		  used in the system:

```
Router# show voice register pool type all Builtin Phone Model : 9971
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
3    A418.7529.93B0  9.44.29.41      1  3   4012$                REGISTERED  
9    001E.7A25.D4EE                  1  9   4006                 UNREGISTERED

Builtin KEM Module : CKEM
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
8    1234.1234.1234                                              UNREGISTERED  

Builtin Phone Model : Jabber-MAC
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    0021.5553.19D1                  1  1   4010                 UNREGISTERED

FastTrack Phone Model : 8900
Pooltype(index) representing the phone model : 52
Reference pooltype to inherit the properties from : 8945
Number of lines supported : 4
Number of addon modules supported : 0 (inherited from 8945)
Default session transport : UDP (inherited from 8945)
Description(helpstring) : Cisco SIP Phone 8945
Phone supports GSM : NO (inherited from 8945)
Phone supports Telnet acess : NO (inherited from 8945)
Phone supports firmware download from CME : YES
Phone spcific XML tags :
<maxNumCalls>24</maxNumCalls>
<busyTrigger>24</busyTrigger>
Phone family : GUMBO_PHONES
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
7    D824.BD27.9EBD  9.44.29.45      1  7   4022$                REGISTERED

Router#
```

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice
                        	 register pool type summary

To display the
                              		  total count of registered and unregistered phones for each Session Initiation
                              		  Protocol (SIP) phone type , use the show voice register pool type summary command in
                              		  privileged EXEC mode.

show voice register pool type summary

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command has
                              		  no default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to view the count of the phones configured, registered and unregistered in the
                              		  SIP mode.

## Examples

The following is a
                              		  sample output of the show voice register pool type summary command:

```
router# show voice register pool type summary =============================================================
PhoneType 													Configured			Registered 		Unregistered
=============================================================
7970 																						1 											1 												0
8941 																						4 									 	3 												1
Unknown Phone type 								4 											0 												4
=============================================================
Total Phones 														9 											4 												5
=============================================================
```

## show voice register pool unregistered

To display the details of the voice registration pools that do not
                              		  have any phones registered, use the show voice register pool unregistered command in privileged EXEC mode.

show voice register pool unregistered

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the pools that do not have
                              		  any active registrations. In Cisco Unified SRST, if multiple phones are trying
                              		  to register through the same pool and if one phone successfully registers and
                              		  the others do not, the pool is not considered as an unregistered pool, as it
                              		  does have an active registration of the registered phone.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for pools with no active registeration:

```
Router# show voice register pool unregistered Pool Tag: 2
 MAC Address                : 0015.C68E.6D13
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
 Pool Tag: 3
 MAC Address                : 0021.5553.8998
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
 Pool Tag: 4
 MAC Address                : 8989.9867.8769
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
```

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

show voice register pool registered

Displays details of phones that sucessfully register to
                                          						Cisco Unified CME or Cisco Unified SRST.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## show voice
                        	 register profile

To display the
                              		  content of configuration files that are in ASCII text format, use the show voice register profile command in privileged EXEC mode.

show voice register profile text tag

### Syntax Description

tag

Unique
                                          						identifier for voice register profile to be displayed. Range is 1–500.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display ASCII configuration files for the Cisco IP Phone 7905 and 7905G,
                              		  Cisco IP Phone 7912 and 7912G, Cisco ATA-186, or Cisco ATA-188. To generate
                              		  ASCII text files, use the file text command.

## Examples

The following is
                              		  sample output from this command displaying information in the configuration
                              		  profile for voice register pool 4:

```
Router# show voice register profile text 4 Pool Tag: 4
#txt
 AutoLookUp:0
 DirectoriesUrl:0
...
 CallWaiting:1
 CallForwardNumber:0
 Conference:1
 AttendedTransfer:1
 BlindTransfer:1
...
 SIPRegOn:1
 UseTftp:1
 UseLoginID:0
 UIPassword:0
 NTPIP:0.0.0.0
 UID:2468
...
```

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

Attended
                                          					 Transfer

Setting
                                          					 of soft key for attended transfer in a SIP phone template as defined by using
                                          					 the transfer-attended command. “1” indicates that the
                                          					 soft key is enabled; “0” indicates that the soft key is disabled.

Auto
                                          					 Lookup

1
                                          					 indicates that Auto Lookup is enabled. 0 indicates that it is disabled.

Blind
                                          					 Transfer

Setting
                                          					 of soft key for blind transfer in a SIP phone template as defined by using the transfer-blind command. “1” indicates that the
                                          					 soft key is enabled; “0” indicates that the soft key is disabled.

Call
                                          					 Waiting

Setting
                                          					 of the call-waiting option on a SIP phone as defined by using the call-waiting command. “1” indicates that the soft key is enabled; “0” indicates that the
                                          					 soft key is disabled.

Call
                                          					 Forward Number

Number to
                                          					 which incoming calls are forwarded

Conference

Setting
                                          					 of soft key for conference in a SIP phone template as defined by using the conference command. “1” indicates that the soft key is enabled; “0” indicates that the
                                          					 soft key is disabled.

Directories URL

1
                                          					 indicates that the Directories feature button for the phone is enabled. 0
                                          					 indicates that it is disabled.

NTPIP

IP
                                          					 address for the NTP source

Pool
                                          					 tag

Pool
                                          					 tag of the configuration file being requested.

SIP Reg
                                          					 On

1
                                          					 indicates that the registration with external proxy server for the phone is
                                          					 enabled. 0 indicates that it is disabled.

UI
                                          					 Password

1
                                          					 indicates that the UI password is enabled on the phone. 0 indicates that dit is
                                          					 disabled.

UID

Authenticatuion credential for SIP phone.

Use
                                          					 Login ID

1
                                          					 indicates that “use login id” for phone is enabled. 0 indicates that it is
                                          					 disabled.

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profiles required for SIP phone.

file text (voice register global)

Generates ASCII text files for the Cisco IP Phone 7905 and 7905G, Cisco IP
                                          						Phone 7912 and 79012G, Cisco ATA-186, or Cisco ATA-188.

reset (voice register global)

Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router.

voice register global

Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco CME or Cisco SIP SRST
                                          						environment.

## show voice
                        	 register session-server

To display the
                              		  call details of the registered session servers, use the show voice register session-server command in privileged EXEC mode.

show voice register session-server

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(22)T

This
                                          						command was introduced in a release earlier than Cisco IOS Release 12.4(22)T.

## Examples

The following is
                              		  sample output from the show voice register session-server command:

```
Router# show voice register session-server Feature server 2, keepalive 60, register-uri CISCO-80NVCGATW_1259887561000
Session reg_number 569, refID 9B2783C0
Route point voice_reg_pool 28 reg_number 570
Route point voice_reg_pool 9 reg_number 571
Route point voice_reg_pool 19 reg_number 572
Route point voice_reg_pool 22 reg_number 573
Subscription sub_id 1133, calledNumber 1242
Subscription sub_id 1135, calledNumber 1054
Subscription sub_id 1138, calledNumber 1155
Subscription sub_id 1140, calledNumber 1188
Subscription sub_id 1142, calledNumber 261
Subscription sub_id 1146, calledNumber 1055
Subscription sub_id 1147, calledNumber 1100
Subscription sub_id 1149, calledNumber 1025
Subscription sub_id 1152, calledNumber 264
Subscription sub_id 1154, calledNumber 267
Subscription sub_id 1156, calledNumber 1185
Subscription sub_id 1157, calledNumber 1218
Subscription sub_id 1160, calledNumber 1056
Subscription sub_id 1161, calledNumber 263
Subscription sub_id 1163, calledNumber 1186
Subscription sub_id 1165, calledNumber 1243
Subscription sub_id 1167, calledNumber 1053
Subscription sub_id 1169, calledNumber 1120
Subscription sub_id 1171, calledNumber 1154
Subscription sub_id 1173, calledNumber 265
```

The following
                              		  table describes the significant fields shown in this output.

Field

Definition

Feature
                                          					 server

The
                                          					 number of active feature servers.

keepalive

Interval,
                                          					 in seconds, at which the peer sends keepalive messages. The range is from 1 to
                                          					 60 seconds. The default is 60 seconds.

register-uri

The
                                          					 registered Uniform Resource Identifier (URI) for the server.

Session
                                          					 reg_number

The
                                          					 registered number of the session.

Route
                                          					 point voice_reg_pool

Denotes
                                          					 the registered virtual device for application redirection.

Subscription sub_id

The
                                          					 subidentification number of the subscription.

## show voice
                        	 register statistics

To display
                              		  statistics associated with the registration event, use the show voice register statistics command in privileged EXEC mode.

show voice register statistics [ global | pool tag ]

### Syntax Description

global

(Optional) Displays aggregate statistics associated with the SIP phone
                                          						registration event.

pool
                                          						tag

(Optional) Displays registration pool statistics associated with a specific
                                          						pool tag. The maximum number of pools is version and platform dependent. Type ? to display
                                          						a list of values.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

15.1(2)T

Cisco
                                          						CME 8.1 Cisco SIP SRST 8.1

This
                                          						command was modified. The global and pool keywords and tag argument were added.
                                          						The output display was also modified to show more information about pools in
                                          						unregistered state and time-stamps of registration event.

### Usage Guidelines

When using the show voice register statistics command, you can verify that the number of Registration and
                              		  unRegister successes for global statistics are the sum of the values in the
                              		  individual pools. Because some Registrations fail even before matching a voice
                              		  register pool, for Registration and unRegister failed statistics the value is
                              		  not the sum of the values in the individual pools. Immediate failures are
                              		  accounted in the global statistics.

In Cisco Unified
                              		  CME 8.1 and Cisco Unified SIP SRST 8.1, the time-stamps for the events is
                              		  displayed along with other registration related statistics. The command output
                              		  also displays the reason for pools in unregistered state. Use the show voice
                              		  register statistics command with pool tag keyword to display registration pool
                              		  statistics associated with a specific pool.

When using the
                              		  global keyword, the show voice register command output displays the aggregate
                              		  statistics associated with SIP phone registration. The output of this command
                              		  also displays the attempted-registrations table.

## Examples

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register statistics Sample Output:
Global statistics
  Active registrations  : 2
  Total SIP phones registered: 2
  Total Registration Statistics
    Registration requests  : 3
    Registration success   : 2
    Registration failed    : 1
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 1 
    Last Register Request Time   : *11:42:31.783 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009 
    Unregister Success Time      : 
Register pool 1 statistics
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 0 
    Last Register Request Time   : *11:11:54.615 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:54.623 UTC Wed Sep 16 2009 
    Unregister Success Time      : 
Register pool 2 statistics
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 0 
    Last Register Request Time   : *11:11:56.707 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009 
    Unregister Success Time      :
```

## Examples

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register statistics global Global Statistics: 
  Active registrations  : 1
  Total SIP phones registered: 2
  Total Registration Statistics
    R egistration requests  : 97715
    Registration success   : 3
    Registration failed    : 97712
    unRegister requests    : 1
    unRegister success     : 1
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 97712 
    Last register request time   : *06:45:11.127 UTC Wed Oct 14 2009 
    Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009 
    Register success time        : *12:10:37.263 UTC Tue Oct 13 2009 
    Unregister success time      : *11:56:22.182 UTC Tue Oct 13 2009 
 Phones that have attempted registrations and have failed:
 MAC address: 001b.535c.d410 
 IP address : 8.3.3.111 
 Attempts   : 97712
 Time of first attempt : *12:20:32.775 UTC Tue Oct 13 2009
 Time of latest attempt: *06:46:14.815 UTC Wed Oct 14 2009
 Reason for failure    : 
         Unauthorized registration request
```

## Examples

The following
                              		  is a sample output from this command displaying all statistical information
                              		  associated with pool 1:

```
Router# show voice register statistics pool 1 Pool 1 Statistics: 
  Active registrations  : 0
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 2
    Registration success   : 2
    Registration failed    : 0
    unRegister requests    : 1
    unRegister success     : 1
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : *12:10:37.259 UTC Tue Oct 13 2009 
    Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009 
    Register success time        : *12:10:37.263 UTC Tue Oct 13 2009 
    Unregister success time      : *11:56:22.182 UTC Tue Oct 13 2009 
  Reason for unregistered state: 
         No registration request since last reboot/unregister
```

The following
                              		  table describes the significant fields shown in this output.

Field

Description

Statistics:

Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool.

Active
                                          					 registrations

Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations.

Last
                                          					 Register Request Time

Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to register the last time.

Last
                                          					 unRegister Request Time

Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to unregister the last time.

Total
                                          					 Registration Statistics

Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool.

Registration requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests.

Registration success

Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations.

Registration failed

Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations.

unRegister requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests.

unRegister success

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters.

unRegister failed

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters.

Global
                                          					 statistics

Used
                                          					 with the statistics keyword. Details all active registrations.

Register pool number statistics

Used
                                          					 with the statistics keyword. Details specific pool statistics.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show
                                          						voice register pool attempted-registrations

Displays the details of phones that attempt to register with Cisco Unified CME
                                          						or Cisco Unified SRST and fail.

## show voice
                        	 register template

To display all
                              		  configuration information associated with a Cisco Unified SIP IP phone
                              		  template, use the show voice register template command in privileged EXEC mode.

show voice register template { template-tag | all }

### Syntax Description

template-tag

Number
                                          						of the template for which to display information. Range is 1 to 5.

all

Displays all configuration information associated with all the Cisco Unified
                                          						SIP IP phone templates.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1)

This
                                          						command was modified to include emergency response location (ERL) information
                                          						assigned to a Cisco Unified SIP IP phone in the output display.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was modified. All keyword was added. Pools that have the template
                                          						defined are also displayed in the output. Voice-class stun-usage information is
                                          						displayed in the output.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display.

### Usage Guidelines

Use the show voice register template command to display all configuration
                              		  information associated with a Cisco Unified SIP IP phone template defined in a
                              		  system. Use the all keyword
                              		  with the show voice register template command to display the details of all the
                              		  templates defined in the system. A maximum of 10 templates can be configured
                              		  and hence, the details of a maximum of 10 templates are displayed in the
                              		  output.

## Examples

The following
                              		  is a sample output from the show voice register template command displaying information for a
                              		  voice register template:

```
Router# show voice register template 1 Temp Tag 1
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  Voicemail is 56789, timeout 15
  softkey connected  Confrn Endcall Hold Trnsfer
  softkey hold  Newcall Resume
  softkey idle  Cfwdall Newcall Redial
  softkey seized  Cfwdall Endcall Redial
  Emergency response location 6
  Lpcor type local
  Lpcor incoming sccp_phone1
  Lpcor outgoing sccp_phone1
```

The following
                              		  is a sample output from the show voice register template command displaying voice-class stun-usage
                              		  information for voice register template 10:

```
Router# show voice register template 10 Temp Tag 10
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  softkey connected  Park Confrn Endcall Hold Trnsfer
  voice-class stun-usage is enabled. tag is 1
  Lpcor type none
  Pool 2 has this template configured
  Pool 3 has this template configured
  Pool 5 has this template configured
  Pool 6 has this template configured
  Pool 7 has this template configured
  Pool 8 has this template configured
  Pool 9 has this template configured
  Pool 10 has this template configured
  Pool 11 has this template configured
  Pool 50 has this template configured
```

The following
                              		  is a sample output from the show voice register template command. The output shows that a hardware
                              		  conference administrator has been assigned, only the conference creator can add
                              		  a new participant, and the conference creator can terminate the active video
                              		  hardware conference by hanging up.

```
Router# show voice register template 5 Temp Tag 5
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference softkey is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Video is disabled
  Camera is enabled
  Anonymous call block is disabled
  Lpcor type none
  paging-dn 0 [multicast]
  conference admin: yes
  conference add mode: creator
```

conference drop
                              		  mode: creator

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

Anonymous call block

Status
                                          					 of anonymous caller blocking defined with the anonymous block command.

Attended Transfer

Status
                                          					 of attended transfer soft key defined with the transfer-attended command.

Blind
                                          					 Transfer

Status
                                          					 of blind transfer soft key defined with the transfer-blind command.

Caller-ID block

Status
                                          					 of caller-id feature defined with the caller-id block command.

Conference

Status
                                          					 of conference soft key defined with the conference command.

Conference admin

Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not.

Conference add mode

Current
                                          					 setting of hardware conference privilege for adding participants.

Conference drop mode

Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up.

Config:

List of
                                          					 configuration options defined for this template.

Dnd
                                          					 controls

Status
                                          					 of Do-Not-Disturb soft key defined with the dnd-control command.

Emergency response location

The
                                          					 ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made.

Lpcor
                                          					 incoming

Setting
                                          					 of the lpcor incoming command.

Lpcor
                                          					 outgoing

Setting
                                          					 of the lpcor outgoing command.

Lpcor
                                          					 type

Setting
                                          					 of the lpcor type command.

Temp
                                          					 Tag

Tag
                                          					 number of the requested template.

VAD

Status
                                          					 of voice activity detection defined with the vad command.

Voicemail

Voice-mail extension and timeout value defined with the voice-mail command.

### Related Commands

Command

Description

show voice register all

Displays all voice register information, including statistics, pools, and dial
                                          						peers.

voice register template

Enters voice register template configuration mode and defines a template of
                                          						common parameters for Cisco Unified SIP IP phones.

## show voice
                        	 register tftp-bind

To display the
                              		  current configuration files accessible to SIP phones, use the show voice register tftp - bind command in privileged EXEC mode.

show voice register tftp-bind

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

### Usage Guidelines

This command
                              		  provides a list of configuration files that are accessible to SIP phones using
                              		  TFTP.

## Examples

The following is
                              		  sample output from this command:

```
Router(config)# show voice register tftp-bind tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf
 tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml
 tftp-server SIP0009B7F7532E.cnf url system:/cme/sipphone/SIP0009B7F7532E.cnf
 tftp-server SIP000ED7DF7932.cnf url system:/cme/sipphone/SIP000ED7DF7932.cnf
 tftp-server SIP0012D9EDE0AA.cnf url system:/cme/sipphone/SIP0012D9EDE0AA.cnf
 tftp-server gk123456789012 url system:/cme/sipphone/gk123456789012
 tftp-server gk123456789012.txt url system:/cme/sipphone/gk123456789012.txt
```

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

ata<mac-address>

Cisco SIP
                                          					 configuration profile for a particular Cisco ATA-186 or Cisco ATA-188 as
                                          					 indicated by the <mac-address>. This file is generated by using the create profile command.

ata<mac-address>.txt

ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco ATA-186
                                          					 or Cisco ATA-188 as indicated by the <mac-address>. This file is
                                          					 generated by using the file text command.

gk<mac-address>

Cisco SIP
                                          					 configuration profile for a particular Cisco IP Phone 7912 or Cisco IP Phone
                                          					 7912G as indicated by the <mac-address>. This file is generated by using
                                          					 the create profile command.

gk<mac>.txt

ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco IP Phone
                                          					 7912 or Cisco IP Phone 7912G as indicated by the <mac-address>. This file
                                          					 is generated by using the file text command.

Id<mac-address>

Cisco SIP
                                          					 configuration profile for a particular Cisco IP Phone 7905 or Cisco IP Phone
                                          					 7912G as indicated by the <mac-address>. This file is generated by using
                                          					 the create profile command.

Id<mac-address>.txt

ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco IP Phone
                                          					 7905 or Cisco IP Phone 7912G as indicated by the <mac-address>. This file
                                          					 is generated by using the file text command.

SIPDefault.cnf

Configuration file to be shared by all Cisco SIP IP Phone 7940s and Cisco SIP
                                          					 IP Phone 7960s. This file is automatically generated by the router through the source-address and is placed in router memory. The SIPDefault.cnf
                                          					 file contains the IP address that the phones use to register for service, using
                                          					 the Session Initiation Protocol (SIP).

SIP<mac-address>.cnf

Cisco
                                          					 SIP configuration profile for a particular Cisco IP Phone 7940 or Cisco IP
                                          					 Phone 7960 as indicated by the <mac-address>. This file is generated by
                                          					 using the create profile command.

syncinfo.xml

Configuration file to be shared by all Cisco SIP IP Phone 7940s and Cisco SIP
                                          					 IP Phone 7960s. This file is generated by using the create profile command.

### Related Commands

Description

create profile (voice register global)

Generates the configuration profiles required for SIP phones.

reset (voice register dn)

Performs a complete reboot of one phone associated with a Cisco CME router.

reset (voice register pool)

Performs a complete reboot of one or all phones associated with a Cisco CME
                                          						router.

text file (voice register global)

Generates an ASCII format text file of the Cisco SIP configuration profile for
                                          						Cisco IP Phone 7905s and 7905Gs, Cisco IP phone 7912s and 7912Gs, Cisco
                                          						ATA-186s, and Cisco ATA-188s.

tftp-path (voice register global)

Specifies the directory to which the provisioning file for SIP phones in a
                                          						Cisco CallManager Express (Cisco CME) system will be written.

voice register global

Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco CME or Cisco SIP SRST
                                          						environment.

## shutdown(telephony-service)

To shut down the Skinny Client Control Protocol (SCCP) server
                              		  listening socket, use the shutdown command in telephony-service configuration mode. To enable service, use
                              		  the no form of this command.

shutdown

no shutdown

### Syntax Description

This command has no arguments or keywords.

### Command Default

No shutdown is enabled

### Command Modes

Telephony-service configuration (config-telephony) Group configuration (conf-tele-group) Call-manager-fallback configuration (config-ccm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced

### Usage Guidelines

The shutdown command allows you to shut down the SCCP server
                              		  listening sockets when you want to change or remove the IP address set up on
                              		  your system. For example, If you have IPv6 address and you want to change the
                              		  IP address set up to dual stack (IPv4 and IPv6) you can use the shutdown
                              		  command.

## Examples

The following example shows SCCP server listening sockets being shut
                              		  down under telephony- service.

```
Router(config-telephony)#shut down 
shutdown
```

The following example shows SCCP server listening sockets being shut
                              		  down for group 2 (under group mode) in telephony service.

```
Router(config-telephony)#group 2
Router(conf-tele-group)#shutdown
```

The following example shows SCCP server listening sockets being shut
                              		  down under call-manager-fallback mode.

```
Router(config-telephony)#group 2
```

Router(conf-cm-fallback)#shutdown

### Related Commands

Command

Description

protocol -mode

Allows you to configure a preferred IP address mode for
                                          						SCCP IP phones.

ip source address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco Unified CME router.

## sip-prefix

To add "SIP_"
                              		  prefix in the locale names while populating the configuration files for this
                              		  phone type in fast track mode, use the sip-prefix command in global configuration mode. To disable, use the no form of
                              		  this command.

sip-prefix

no sip-prefix

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

sip-prefix is
                              		  enabled.

### Command Modes

Router (config-register-pooltype) #sip-prefix

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was introduced

### Usage Guidelines

The sip-prefix
                              		  command allows you to add “SIP_” prefix in the locale names of the
                              		  configuration files. For example, DX650 phones do not require “SIP_” prefix in
                              		  their locale names. However, other phone models require “SIP_” prefix in locale
                              		  names. Use this command while adding new phones in fast-track mode based on
                              		  their locale file format.

## Examples

The following
                              		  example shows how to configure “SIP_” prefix on the endpoint Cisco Unified IP
                              		  Phone 7811.

```
Router(config)#voice register pool-type 7811 
Router(config-register-pooltype)#sip-prefix
```

### Related Commands

Command

Description

num -lines

Defines
                                          						number of lines supported by the phone.

phoneload -support

Defines
                                          						the phone support for Phoneload.

reference -pooltype

Reference pooltype to inherit the properties used in fast-track
                                          						configuration.

## snr

To enable Single Number Reach (SNR) on an extension of an SCCP IP
                              		  phone, use the snr command in ephone-dn configuration mode. To disable SNR on the
                              		  extension, use the no form of this command.

snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

no snr

### Syntax Description

e164-number

E.164 telephone number to ring if IP phone extension does
                                          						not answer.

delay seconds

Sets the number of seconds that the call rings the IP phone
                                          						before ringing the remote phone. Range: 0 to 10. Default: disabled.

timeout seconds

Sets the number of seconds that the call rings after the
                                          						configured delay. Call continues to ring for this length of time on the IP
                                          						phone even if the remote phone answers the call. Range: 5 to 60. Default:
                                          						disabled.

cfwd-noan extension-number

(Optional) Forwards the call to this target number if the
                                          						phone does not answer after both the delay and timeout seconds have expired. This
                                          						is typically the voice mail number.

### Command Default

Single Number Reach is not enabled on the extension.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco UnifiedCME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command enables the SNR feature on the extension. The SNR
                              		  feature allows users to answer incoming calls on their desktop IP phone or at a
                              		  remote destination and to pick up in-progress calls on the desktop phone or the
                              		  remote destination without losing the connection. If an incoming call to this
                              		  extension is answered immediately, the call is treated as a normal call.

If the call is not answered within the number of seconds set with the delay keyword, Cisco Unified CME rings the
                              		  remote number while continuing to ring the SNR extension. If the call is
                              		  answered by the desktop IP phone within the number of seconds set with the timeout keyword, the call to the remote
                              		  number is disconnected. If the call is answered on the IP phone, the user can
                              		  send the call to the remote phone by pressing the Mobility soft key.

If the call is not answered by the IP phone within the number of
                              		  seconds set with the timeout keyword, the ringing call appearance
                              		  on the IP phone is deleted. This call is marked as hold state on the IP phone.
                              		  If the user answers the call on the remote phone, the user can pull back the
                              		  call to the IP phone by pressing the Resume soft-key.

## Examples

The following example shows extension 1001 is enabled for SNR. After
                              		  a call rings at this number for 5 seconds, the call also rings at the remote
                              		  number 4085550133. The call continues ringing on both phones for 15 seconds. If
                              		  the call is not answered after a total of 20 seconds, the call no longer rings
                              		  and is forwarded to the voice-mail number 2001.

```
ephone-dn 10
 number 1001
 mobility
 snr 4085550133 delay 5 timeout 15 cfwd-noan 2001
```

### Related Commands

Command

Description

mobility

Enables the Mobility feature on an extension of an SCCP IP
                                          						phone.

number

Associates a telephone or extension number with an
                                          						ephone-dn.

softkeys connected

Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state.

softkeys idle

Modifies the order and type of soft keys that display on an
                                          						IP phone during the idle call state.

## snr (voice register dn)

To enable the Single Number Reach (SNR) feature on an extension of a
                              		  Cisco Unified SIP IP phone, use the snr command in voice register dn
                              		  configuration mode. To disable the SNR feature on the extension, use the no form of the command.

snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

no snr

### Syntax Description

e164-number

E.164 telephone number to call when the Cisco Unified SIP
                                          						IP phone extension does not answer.

delay seconds

Sets the number of seconds that the Cisco Unified SIP IP
                                          						phone rings when called. When the time delay is reached, the call is tranferred
                                          						to the PSTN phone and the SNR directory number. Range: 0 to 30. Default: 5.

timeout seconds

Sets the number of seconds that the Cisco Unified SIP IP
                                          						phone rings after the configured time delay. When the timeout value is reached,
                                          						no call is displayed on the phone. You have to use the Resume soft key to pull
                                          						back or the Mobility soft key to send the call to a mobile phone. Range: 30 to
                                          						60. Default: 60.

cfwd-noan extension-number

(Optional) Forwards the call to the extension number when
                                          						the phone does not answer after both the time delay and timeout values are
                                          						reached. The extension number is typically the voice mail number.

### Command Default

The SNR feature is not enabled on the extension of a Cisco Unified
                              		  SIP IP phone.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the snr command to enable the SNR feature on an
                              		  extension of a Cisco Unified SIP IP phone.

The SNR feature allows you to answer incoming calls on your desktop
                              		  IP phones or at a remote destination. It also allows you to pick up in-progress
                              		  calls on a desktop phone or at a remote destination without losing the
                              		  connection. If an incoming call to the extension is answered immediately, the
                              		  call is treated as a normal call.

If the call is not answered within the number of seconds set with the delay keyword, Cisco Unified CME rings the
                              		  remote number while continuing to ring the SNR extension. If the call is
                              		  answered by the desktop IP phone within the number of seconds set with the timeout keyword, the call to the remote
                              		  number is disconnected. If the call is answered on the IP phone, you can send
                              		  the call to the remote phone by pressing the Mobility soft key.

If the call is not answered by the IP phone within the number of
                              		  seconds set with the timeout keyword, the call is dislayed on the
                              		  IP phone as being in the hold state. If the user answers the call on the remote
                              		  phone, the user can pull back the call to the IP phone by pressing the Resume
                              		  soft key.

## Examples

The following example shows that extension 1004 is enabled for SNR.
                              		  After a call rings at this number for one second, the call also rings at the
                              		  remote number 9900. The call continues ringing on both phones for 10 seconds.
                              		  If the call is not answered after a total of 11 seconds, the call no longer
                              		  rings and is forwarded to the voice-mail number 1007.

```
Router(config)# voice register dn  3 Router(config-register-dn)# number 1004 Router(config-register-dn)# name John Smith Router(config-register-dn)# mobility Router(config-register-dn)# snr calling-number local Router(config-register-dn)# snr 9900 delay 1 timeout 10 cfwd-noan 1007 Router(config-register-dn)# snr ring-stop Router(config-register-dn)# snr answer-too-soon 2
```

### Related Commands

Command

Description

mobility (voice register dn)

Enables the Mobility feature on an extension of a Cisco
                                          						Unified SIP IP phone.

snr answer-too-soon (voice register dn)

Sets the time in which SNR calls are prevented from being
                                          						diverted to the voice mailbox of a mobile phone.

snr calling-number local (voice register dn)

Replaces the calling party number displayed on the
                                          						configured mobile phone with the local SNR number.

snr ring-stop (voice register dn)

Ends the ringing on a Cisco Unified SIP IP phone after the
                                          						Single SNR call is answered on the configured mobile phone.

## snr answer-too-soon

To set the SNR answer to soon timer, use the snr answer-too-soon
                              		  command in ephone-dn mode. To reset the default, use the no form of the
                              		  command.

snr answer-too-soon time

no snr answer-too-soon

### Syntax Description

time

Time, in seconds. Range: 1 to 5.

### Command Default

No answer too soon timer is set.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to enable timer for answering the call on an SNR
                              		  mobile phone. You can set a timer from 1 to 5 seconds. If the call is answered
                              		  within the timer, the mobile leg is disconnected.

## Examples

```
Router(config)ephone-dn 10
Router(config-ephone-dn)#snr answer-too-soon 4
```

### Related Commands

Command

Description

snr

Enables SNR on the extension of an SCCP IP phone.

## snr answer-too-soon (voice register dn)

To set the time in which Single Number Reach (SNR) calls are
                              		  prevented from being diverted to the voice mailbox of a mobile phone, use the snr answer-too-soon command in voice register dn
                              		  configuration mode. To allow SNR calls to be diverted to the voice mailbox, use
                              		  the no form of the command.

snr answer-too-soon time

no snr answer-too-soon

### Syntax Description

time

Time, in seconds. Range: 1 to 5.

### Command Default

No answer-too-soon time is set. Calls may be diverted to the voice
                              		  mailbox when a user’s mobile phone is not answered or is turned off.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the snr answer-too-soon command to set the time in which
                              		  SNR calls are prevented from being diverted to the voice mailbox of a mobile
                              		  phone. When the call is diverted to the voice mailbox within the set time, the
                              		  mobile phone call leg is disconnected.

## Examples

The following example shows how SNR calls are prevented from being
                              		  diverted to the voice mailbox of a mobile phone for 2 seconds:

```
Router(config)# voice register dn  3 Router(config-register-dn)# number 1004 Router(config-register-dn)# name John Smith Router(config-register-dn)# mobility Router(config-register-dn)# snr calling-number local Router(config-register-dn)# snr 9900 delay 1 timeout 10 Router(config-register-dn)# snr ring-stop Router(config-register-dn)# snr answer-too-soon 2
```

### Related Commands

Command

Description

snr (voice register dn)

Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone.

## snr calling-number local

To replace the calling-party number with the single number reach
                              		  (SNR) extension number in calls forwarded to the remote phone, use the snr calling-number local command in ephone-dn configuration mode. To reset to the
                              		  default, use the no form of this command.

snr calling-number local

no snr calling-number local

### Syntax Description

This command has no arguments or keywords.

### Command Default

Calling-party number is not replaced.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command replaces the original calling party number with the SNR
                              		  extension number (local number) in the caller ID display for SNR calls
                              		  forwarded to the remote phone. When the call is forwarded to the remote phone,
                              		  such as a mobile phone, the caller ID shows the SNR number that the caller
                              		  dialed, not the number of the original calling party.

## Examples

The following example shows that the original calling party number is
                              		  replaced by the SNR extension number 1234 when the call is forwarded to the
                              		  mobile phone:

```
ephone-dn 1
 number 1234
 mobility
 snr 4085550123 delay 5 timeout 15 cfwd-noan 2001
 snr calling-number local
```

### Related Commands

Command

Description

calling-number local

Replaces a calling-party number and name with the
                                          						forwarding-party number and name for all calls.

mobility

Enables the Mobility feature on an extension of an SCCP IP
                                          						phone.

snr

Enables SNR on the extension of an SCCP IP phone.

## snr calling-number local (voice register dn)

To replace the calling party number displayed on the configured
                              		  mobile phone with the local Single Number Reach (SNR) number, use the snr calling-number local command in voice register dn configuration
                              		  mode. To return to the default, use the no form of this command.

snr calling-number local

no snr calling-number local

### Syntax Description

This command has no arguments or keywords.

### Command Default

The number of the calling party is displayed on the mobile phone
                              		  configured to receive SNR calls.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

## Examples

The following example shows how the snr calling-number local command is used to display the local SNR
                              		  number instead of the calling party’s number on the mobile phone:

```
Router(config)# voice register dn  3 Router(config-register-dn)# number 1004 Router(config-register-dn)# name John Smith Router(config-register-dn)# mobility Router(config-register-dn)# snr calling-number local Router(config-register-dn)# snr 9900 delay 1 timeout 10 Router(config-register-dn)# snr ring-stop Router(config-register-dn)# snr answer-too-soon 2
```

### Related Commands

Command

Description

snr (voice register dn)

Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone.

## snr mode

To set the mode for the Single Number Reach (SNR) directory number
                              		  (DN), use the snr mode command in ephone-dn configuration mode. To
                              		  return to the default, use the no form of this command.

snr mode [ virtual ]

no snr mode

### Syntax Description

virtual

Enables the virtual mode for an SNR DN when it is
                                          						unregistered or floating.

### Command Default

No DN mode is set for the SNR feature.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

A virtual SNR DN is a DN not associated with any registered phone but
                              		  is a number that can be called, have its calls forwarded to a preconfigured
                              		  mobile phone, or put on an Auto Hold state when the mobile phone answers the
                              		  call or the time delay is reached. In the Auto Hold state, the DN can either be
                              		  floating or unregistered. A floating DN is a DN not configured with any phone
                              		  while an unregistered DN is one associated with phones not registered to a
                              		  Cisco Unified CME system.

A ringback tone is heard when a call is made to a virtual DN.

To enable the SNR feature, the SNR DN must be in the up state, the
                              		  Mobility feature must be enabled, and the time delay or timeout value
                              		  configured with the snr command must be reached.

## Examples

The following example sets the virtual DN mode for SNR on ephone-dn
                              		  1:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# snr mode virtual
```

### Related Commands

Command

Description

ephone-dn

Enters ephone-dn configuration mode to configure a DN for
                                          						an IP phone line, intercom line, paging line, voice-mail port, or MWI.

snr

Enables SNR on an extension of a Cisco Unified SCCP IP
                                          						phone.

## snr ring-stop

To stop the IP phone from ringing after the SNR call is answered on a
                              		  mobile phone, use the snr ring-stop command in ephone-dn configuration mode. To
                              		  reset the default value, use the no form of the command.

snr ring-stop

no snr ring-stop

### Syntax Description

This command has no arguments or keywords.

### Command Default

Phone continues to ring after the SNR call is answered on a mobile
                              		  phone.

### Command Modes

Ephone-dn configuration (conf-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to stop the IP phone from ringing after the SNR call
                              		  is answered on a mobile phone.

## Examples

```
Router(config-ephone-dn)10 
Router(config-ephone-dn)#snr ring-stop
```

### Related Commands

Command

Description

snr

Enables SNR on the extension of an SCCP IP phone.

## snr ring-stop (voice register dn)

To end the ringing on a Cisco Unified SIP IP phone after the Single
                              		  Number Reach (SNR) call is answered on the configured mobile phone, use the snr ring-stop command in voice register dn
                              		  configuration mode. To allow the Cisco Unified SIP IP phone to continue ringing
                              		  even after the SNR call has been answered, use the no form of the command.

snr ring-stop

no snr ring-stop

### Syntax Description

This command has no arguments or keywords.

### Command Default

The Cisco Unified SIP IP phone continues to ring even after the SNR
                              		  call is answered on a mobile phone.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

## Examples

The following example shows how to end the ringing on a Cisco Unified
                              		  SIP IP phone:

```
Router(config)# voice register dn  3 Router(config-register-dn)# number 1004 Router(config-register-dn)# name John Smith Router(config-register-dn)# mobility Router(config-register-dn)# snr calling-number local Router(config-register-dn)# snr 9900 delay 1 timeout 10 Router(config-register-dn)# snr ring-stop Router(config-register-dn)# snr answer-too-soon 2
```

### Related Commands

Command

Description

snr (voice register dn)

Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone.

## softkeys alerting

To configure an ephone template for soft-key display during the
                              		  alerting call stage, use the softkeys alerting command in ephone-template configuration
                              		  mode. To remove a soft key alerting configuration, use the no form of this command.

softkeys alerting [ Acct ] [ Callback ] [ Endcall ]

no softkeys alerting

### Syntax Description

Acct

(Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Short for “account code.” Provides access to
                                          						configured accounts.

Callback

(Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Requests callback notification when a busy
                                          						called line becomes free.

Endcall

(Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Ends the current call.

### Command Default

The default soft keys for the alerting call stage and the order in
                              		  which they appear on IP phones are, from first to last, Acct, Callback, and
                              		  Endcall.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco CME Version

Modification

12.3(11)T

3.2

This command was introduced.

### Usage Guidelines

The alerting call stage is when the remote point is being notified of
                              		  an incoming call, and the status of the remote point is being relayed to the
                              		  caller as either ringback or busy.

The number and order of soft keys listed in the softkeys alerting correspond to the number and order of soft keys that will
                              		  appear on IP phones.

## Examples

In the following example, ephone template 1 is configured for the
                              		  alerting stage and for the seized and connected call stages:

```
Router(config)# telephony-service Router(config-telephony)# ephone-template 1 Router(config-ephone-template)# softkeys seized Redial Cfwdall Pickup Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an ephone.

softkeys connected

Configures an ephone template for soft-key display during
                                          						the connected call stage.

softkeys idle

Configures an ephone template for soft-key display during
                                          						the idle call stage.

softkeys seized

Configures an ephone template for soft-key display during
                                          						the seized call stage.

## softkeys connected
                        	 (voice register template)

To modify the
                              		  soft key display during the connected call state on Cisco Unified SIP IP
                              		  phones, use the softkeys connected command in voice register template configuration mode. To
                              		  return to the default, use the no form of
                              		  this command.

softkeys connected [ ConfList ] [ Confrn ] [ Endcall ] [ Hold ] [ Park ] [ RmLstC ] [ Trnsfer ] [ iDivert ] [ HLog ]

no softkeys connected

### Syntax Description

ConfList

(Optional) Lists all the participants in a conference.

Confrn

(Optional) Connects callers to a conference call. This soft key
                                          						also enables ad-hoc conference creators to initiate a conference.

Endcall

(Optional) Ends the current call.

Hold

(Optional) Places an active call on hold and resumes the call.

Park

(Optional) Places an active call on hold so it can be retrieved from another
                                          						phone in the system.

RmLstC

(Optional) Removes the last conference participant.

Trnsfer

(Optional) Transfers active calls to another extension.

iDivert

(Optional) Immediately diverts a call to a voice-messaging
                                          						system.

HLog

(Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this softkey to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls.

### Command Default

The default soft
                              		  keys for the connected call state and the order in which they appear on Cisco
                              		  Unified SIP IP phones are, from first to last: ConfList, Confrn, Endcall, Hold,
                              		  Park, RmLstC, Trnsfer, iDivert, and HLog.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

12.4(22)YB

Cisco
                                          						Unified CME 7.1

The Park keyword was added.

15.1(3)T

Cisco
                                          						Unified CME 8.5

The iDivert keword was added.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified. The syntax description for the Confrn soft key was
                                          						updated. The ConfList and RmLastC keywords were added.

Cisco IOS XE Everest 16.4.1

15.6(3)M1

Cisco Unified CME 11.6

HLog Softkey support was introduced.

### Usage Guidelines

The connected
                              		  call state is when the connection to a remote point is established.

The number and
                              		  order of soft keys used in this command correspond to the number and order of
                              		  soft keys that appear on Cisco Unified SIP IP phones. Any soft key that is not
                              		  explicitly specified with this command is disabled.

The ConfList
                              		  and RmLastC soft keys are added in the connected state when hardware conference
                              		  is enabled.

This command is
                              		  not supported on the Cisco Unified 7905, 7912, 7940, and 7960 SIP IP Phones.

## Examples

In the
                              		  following example, Cisco Unified SIP IP phone template 1 is configured for the
                              		  connected and seized call states:

```
Router(config)# voice register template 1 Router(config-register-temp)# softkeys seized Redial Cfwdall EndCall HLog Router(config-register-temp)# softkeys connected Confrn Hold Endcall HLog
```

The following
                              		  is a sample output from the show voice register template command. The output shows that the
                              		  iDivert soft key is in connected state.

```
Router# show voice register template 1 Temp Tag 1
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  softkeys seized Redial Cfwdall EndCall HLog
  softkeys connected Confrn Hold Endcall HLog
```

### Related Commands

Command

Description

softkeys hold (voice register template)

Modifies the soft key display on Cisco Unified SIP IP phones during the hold
                                          						call state.

softkeys idle (voice register template)

Modifies the soft key display on Cisco Unified SIP IP phones during the idle
                                          						call state.

softkeys seized (voice register template)

Modifies the soft key display on Cisco Unified SIP IP phones during the seized
                                          						call state.

template (voice register pool)

Applies a phone template to a Cisco Unified SIP IP phone.

## softkeys connected

To modify the order and type of soft keys that display on an IP phone
                              		  during the connected call state, use the softkeys connected command in ephone-template configuration mode. To reset to the
                              		  default, use the no form of this command.

softkeys connected [ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Mobility ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]

no softkeys connected

### Syntax Description

Acct

(Optional) Soft key that provides access to configured
                                          						accounts.

ConfList

(Optional) Soft key that lists all parties in a conference.

Confrn

(Optional) Soft key that connects callers to a conference
                                          						call.

Endcall

(Optional) Soft key that ends the current call.

Flash

(Optional) Soft key that provides hookflash functionality
                                          						for public switched telephony network (PSTN) services on calls connected to the
                                          						PSTN via a foreign exchange office (FXO) port. Also called “hookflash.”

HLog

(Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls.

Hold

(Optional) Soft key that places an active call on hold and
                                          						resumes the call.

Join

(Optional) Soft key that joins an established call to
                                          						conference.

LiveRcd

(Optional) Soft key that enables recording of a call.

Mobility

(Optional) Soft key that forwards the call to the PSTN
                                          						number defined by the Single Number Reach (SNR) feature.

Park

(Optional) Soft key that places an active call on hold, so
                                          						it can be retrieved from another phone in the system.

RmLstC

(Optional) Soft key that removes the last party added to
                                          						the conference. This soft key only works for the conference creator.

Select

(Optional) Soft key that selects a call or a conference on
                                          						which to take action.

TrnsfVM

(Optional) Soft key that transfers a call to a voice-mail
                                          						extension number.

Trnsfer

(Optional) Soft key that transfers active calls to another
                                          						extension.

### Command Default

The default soft keys for the connected call state and the order in
                              		  which they appear on IP phones are, from first to last:

- With HLog support: Hold, EndCall, Trnsfer, Confrn, Acct, Flash,
                                 			 Park, HLog

- Without HLog support: Hold, EndCall, Trnsfer, Confrn, Acct, Flash,
                                 			 Park

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The HLog keyword was added.

12.4(11)XJ

Cisco Unified CME 4.1

The ConfList , Join , RmLstC , and Select keywords were added.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

12.4(15)XZ

Cisco Unified CME 4.3

The LiveRcd and TrnsfVM keywords were added.

12.4(20)T

Cisco Unified CME 7.0

This command with the LiveRcd and TrnsfVM keywords was integrated
                                          						into Cisco IOS Release 12.4(20)T.

12.4(22)YB

Cisco Unified CME 7.1

The Mobility keyword was added.

12.4(24)T

Cisco UnifiedCME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

The connected call state is when the connection to a remote point has
                              		  been established.

Configure the ConfList, Join, and RmLstC soft keys for conferencing
                              		  functions. These soft keys are supported for hardware-based conferencing only
                              		  and require the appropriate DSP farm configuration.

## Examples

In the following example, ephone template 1 modifies the soft keys
                              		  displayed for the seized, alerting, and connected call states:

```
Router(config)# ephone-template 1 Router(config-ephone-template)# softkeys seized Redial Cfwdall Pickup Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode for an IP phone.

ephone-template (ephone)

Applies an ephone template to an ephone.

fxo-hook-flash

Enables display of the Flash soft key.

hunt-group logout

Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of the HLog soft key on phones.

softkeys alerting

Modifies the soft-key display for the alerting call state.

softkeys idle

Modifies the soft-key display for the idle call state.

softkeys ringing

Modifies the soft-key display for the ringing call state.

softkeys seized

Modifies the soft-key display for the seized call state.

## softkeys hold

To configure an ephone template to modify soft-key display during the
                              		  call-hold call stage, use the softkeys hold command in ephone-template configuration
                              		  mode. To remove a softkeys hold configuration, use the no form of this command.

softkeys hold [ Join ] [ Newcall ] [ Resume ] [ Select ]

no softkeys hold

### Syntax Description

Join

(Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Joins an established call to a conference.

Newcall

(Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Opens a line on a speaker phone to place a new call.

Resume

(Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Reconnects with the call on hold.

Select

(Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Selects a call or a conference on which to take action.

### Command Default

The default soft keys for the hold call stage and the order in which
                              		  they appear on IP phones are alphabetical, from first to last, Join, Newcall,
                              		  Resume, and Select.

### Command Modes

Ephone-template configuration (config-ephone-template)

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

12.4(11)XJ2

Cisco Unified CME 4.1

The Join and Select keywords were added.

12.4(15)T

Cisco Unified CME 4.1

This command with the Join and Select keywords was integrated into
                                          						Cisco IOS Release 12.4(15)T.

### Usage Guidelines

You reach the call-hold state by pressing the Hold soft key while you
                              		  are in the connected state. From the hold state, you can press Resume to return
                              		  to the connected state or NewCall to start another call, leaving the original
                              		  call in the call-hold state.

The number and order of soft keys listed in the softkeys hold correspond to the number and order of soft keys that will
                              		  appear on IP phones.

Configure the Join and Select soft keys for conferencing functions.
                              		  These soft keys are supported for hardware-based conferencing only and require
                              		  the appropriate DSP farm configuration..

## Examples

In the following example, ephone template 1 is configured for the
                              		  idle, alerting, connected, and hold call stages. It is applied to ephone 25.
                              		  When ephone 25 has a call on hold, the only soft key that will be available is
                              		  the Resume soft key.

```
Router(config)# telephony-service Router(config-telephony)# ephone-template 1 Router(config-ephone-template)# softkeys idle Redial Cfwdall Pickup Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall Router(config-ephone-template)# softkeys hold Resume Router(config-ephone-template)# exit Router(config)# ephone 25 Router(config-ephone)# button 1:39 Router(config-ephone)# ephone-template 1
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode for an IP phone.

ephone-template

Declares and names an ephone template to configure IP phone
                                          						soft-key display and enters ephone-template configuration mode

ephone-template (ephone)

Applies an ephone template to an ephone.

softkeys alerting

Configures an ephone template for soft-key display during
                                          						the alerting call stage.

softkeys connected

Configures an ephone template for soft-key display during
                                          						the connected call stage.

softkeys idle

Configures an ephone template for soft-key display during
                                          						the idle call stage.

softkeys seized

Configures an ephone template for soft-key display during
                                          						the seized call stage.

## softkeys idle

To modify the order and type of soft keys that display on an IP phone
                              		  during the idle call state, use the softkeys idle command in ephone template configuration mode. To reset to the
                              		  default, use the no form of this command.

softkeys idle [ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Mobility ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ]

no softkeys idle

### Syntax Description

Cfwdall

(Optional) Soft key that forwards all calls.

ConfList

(Optional) Soft key that lists all parties in a conference.

Dnd

(Optional) Soft key that enables the Do-Not-Disturb
                                          						features. This key is a toggle; pressing it a second time disables DND.

Gpickup

(Optional) Soft key that selectively picks up calls coming
                                          						into a phone number that is a member of a pickup group.

HLog

(Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls.

Join

(Optional) Soft key that joins an established call to a
                                          						conference.

Login

(Optional) Soft key that provides personal identification
                                          						number (PIN)-controlled access to restricted phone features.

Mobility

(Optional) Soft key that enables Single Number Reach (SNR)
                                          						feature. This key is a toggle; pressing it a second time disables SNR.

Newcall

(Optional) Soft key that opens a line on a speaker phone to
                                          						place a new call.

Pickup

(Optional) Soft key that selectively picks up calls coming
                                          						into another extension.

Redial

(Optional) Soft key that redials the last number dialed.

RmLstC

(Optional) Soft key that removes the last party added to
                                          						the conference. This soft key removes the last party only when the conference
                                          						creator presses it.

### Command Default

The default soft keys for the idle call stage and the order in which
                              		  they appear on IP phones are:

- FXO Trunk: Redial, NewCall, DoNotDisturb

- With HLog support: Redial, NewCall, CFwdAll, CallPickUp,
                                 			 GrpCallPickUp, DoNotDisturb, Login, HLog

- Without HLog support: Redial, NewCall, CFwdAll, CallPickUp,
                                 			 GrpCallPickUp, DoNotDisturb, Login

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The HLog keyword was added.

12.4(9)T

Cisco Unified CME 4.0

The HLog keyword was integrated into
                                          						Cisco IOS Release 12.4(9)T.

12.4(11)XJ2

Cisco Unified CME 4.1

The ConfList , Join , and RmLstC keywords were added.

12.4(15)T

Cisco Unified CME 4.1

This command with the ConfList , Join , and RmLstC keywords was integrated into
                                          						Cisco IOS Release 12.4(15)T.

12.4(22)YB

Cisco Unified CME 7.1

The Mobility keyword was added.

12.4(24)T

Cisco unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

The idle calling stage occurs before a call is made and after a call
                              		  is complete.

The number and order of soft keys listed in the softkeys idle command correspond to the number and order of soft keys on IP
                              		  phones.

Configure the ConfList, Join, and RmLstC soft keys for conferencing
                              		  functions. These soft keys are supported for hardware-based conferencing only
                              		  and require the appropriate DSP farm configuration.

## Examples

In the following example, ephone template 1 is configured for the
                              		  idle stage and for the alerting and connected call stages:

```
Router(config)# ephone-template 1 Router(config-ephone-template)# softkeys idle Redial Cfwdall Pickup Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode for an IP phone.

ephone-template

Creates an ephone template.

ephone-template (ephone)

Applies an ephone template to an ephone.

hunt-group logout

Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of an HLog soft key on phones.

softkeys alerting

Configures soft-key display during the alerting call state.

softkeys connected

Configures soft-key display during the connected call
                                          						state.

softkeys seized

Configures soft-key display during the seized call state.

## softkeys idle
                        	 (voice register template)

To modify the
                              		  soft-key display during the idle call state on SIP phones, use the softkeys idle command in voice register template configuration mode. To
                              		  remove a softkeys idle configuration, use the no form of
                              		  this command.

softkeys idle [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] [ HLog ]

no softkeys idle

### Syntax Description

Cfwdall

(Optional) Soft key for “call forward all.” Forwards all calls.

DND

(Optional) Soft key that enables the Do-Not-Disturb feature.

Gpickup

(Optional) Soft key that allows a user to pickup a call that is ringing on
                                          						another phone.

Newcall

(Optional) Soft key that opens a line on a speakerphone to place a new call.

Pickup

(Optional) Soft key that allows a user to pickup a call that is ringing on
                                          						another phone that is a member of the same pickup group.

Redial

(Optional) Soft key that redials the last number dialed.

HLog

(Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this softkey to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls.

### Command Default

The default soft
                              		  keys for the idle call state and the order in which they appear on SIP phones
                              		  are, from first to last, Redial, Newcall, Cfwdall, and HLog.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

12.4(22)YB

Cisco
                                          						Unified CME 7.1

The DND keyword
                                          						was added.

12.4(24)T

Cisco
                                          						Unified CME 7.1

This
                                          						command was integrated into Cisco IOS Release 12.4(24)T.

Cisco IOS XE Everest 16.4.1

15.6(3)M1

Cisco Unified CME 11.6

HLog Softkey support was introduced.

### Usage Guidelines

The idle
                              		  calling state occurs before a call is made and after a call is complete.

The number and
                              		  order of soft keys used in this command correspond to the number and order of
                              		  soft keys that appear on SIP phones. Any soft key that is not explicitly
                              		  specified with this command is disabled if this command is used to change the
                              		  default soft keys.

This command is
                              		  not supported on the Cisco Unified IP Phone 7905, 7912, 7940, or 7960.

## Examples

In the
                              		  following example, SIP phone template 1 is configured for the idle and
                              		  connected call states:

```
Router(config)# voice register template 1 Router(config-register-template)# softkeys idle Redial Cfwdall HLog Router(config-register-template)# softkeys connected Confrn Hold Endcall HLog
```

### Related Commands

Command

Description

softkeys connected (voice register template)

Modifies the soft-key display on SIP phones during the connected call state.

softkeys hold (voice register template)

Modifies the soft-key display on SIP phones during the hold call state.

softkeys idle (voice register template)

Modifies the soft-key display on SIP phones during the idle call state.

softkeys seized (voice register template)

Modifies the soft-key display on SIP phones during the seized call state.

template (voice register pool)

Applies a phone template to a SIP phone.

## softkeys
                        	 personal-conf-user (voice register template)

To enable a
                              		  personal user softkey template for Cisco IP Conference Phones 7832 and 8832,
                              		  use the softkeys personal-conf-user command in voice register template configuration mode. To
                              		  switch to a public user softkey template, use the no form of
                              		  this command.

softkeys personal-conf-user

no softkeys personal-conf-user

### Command Default

By default, the
                              		  CLI command softkeys personal-conf-user is disabled. Hence, the Cisco IP Conference Phones 7832 and
                              		  8832 support the public user softkey template if the command is not configured.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Fuji 16.9.1

Unified CME 12.3

A personal and public softkey template support was introduced for new Softkeys introduced as part of Unified CME 12.3 Release
                                          for Cisco IP Conference Phone 7832 and 8832.

### Usage Guidelines

The CLI command softkeys personal-conf-user is an optional configuration that is required only when the
                              		  phone template is applied to Cisco IP Conference Phones 7832 and 8832. If no
                              		  configuration is provided, then the default configuration of public user
                              		  softkey template is applied. When the CLI command is enabled, the personal
                              		  softkey template is applied to the conference phone (Only for Cisco IP
                              		  Conference Phone 7832 and 8832). When the command is not enabled, the public
                              		  softkey template is applied to the conference phone (Only for Cisco IP
                              		  Conference Phone 7832 and 8832).

As compared to public softkey user template, the following softkeys
                              		  are additionally supported in a personal user softkey template for various
                              		  phone states:

Messages

CfwdAll

DND

Redial

## Examples

In the following
                              		  example, Cisco IP Conference Phone 7832 is configured for the personal softkeys
                              		  template:

```
Router(config)# voice register template 7 Router(config-register-template)# softkeys personal-conf-user
```

### Related Commands

Command

Description

softkeys connected (voice register template)

Modifies the soft-key display on SIP phones during the connected call state.

softkeys hold (voice register template)

Modifies the soft-key display on SIP phones during the hold call state.

softkeys idle (voice register template)

Modifies the soft-key display on SIP phones during the idle call state.

softkeys seized (voice register template)

Modifies the soft-key display on SIP phones during the seized call state.

template (voice register pool)

Applies a phone template to a SIP phone.

## softkeys remote-in-use

To modify the order and type of soft keys that display on the IP
                              		  phone during the remote-in-use call state, use the softkeys remote-in-use command in ephone-template
                              		  configuration mode. To reset to the default, use the no form of this command.

softkeys remote-in-use [ CBarge ] [ Newcall ]

no softkeys remote-in-use

### Syntax Description

CBarge

(Optional) Soft key that allows a user to barge into a call
                                          						on a shared octo-line directory number.

Newcall

(Optional) Soft key that opens a line on a speakerphone to
                                          						place a new call.

### Command Default

The default soft keys for the remote-in-use call state and the order
                              		  in which they appear on IP phones are Newcall, CBarge.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was itegrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

The remote-in-use call state is when another phone is connected to a
                              		  call on an octo-line directory number shared by this phone.

## Examples

In the following example, ephone template 1 modifies the soft keys
                              		  displayed for the alerting, connected, and remote-in-use call states:

```
Router(config)# ephone-template 1 Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall Router(config-ephone-template)# softkeys remote-in-use CBarge Newcall
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an ephone.

softkeys alerting

Modifies the soft-key display for the alerting call stage.

softkeys idle

Modifies the soft-key display for the idle call stage.

softkeys seized

Modifies the soft-key display for the seized call stage.

## softkeys remote-in-use (voice register template)

To modify the soft-key display during the remote-in-use call state on
                              		  SIP shared-line phones, use the softkeys remote-in-use command in voice register template
                              		  configuration mode. To reset to the default, use the no form of this command.

softkeys remote-in-use [ Barge ] [ Newcall ] [ cBarge ]

no softkeys remote-in-use

### Syntax Description

Barge

(Optional) Soft key that allows a user to join a call on a
                                          						shared line.

Newcall

(Optional) Soft key that opens a line on a phone to place a
                                          						new call.

cBarge

(Optional) Soft key that allows a user to join a call on a
                                          						shared line and to turn the call into a conference call.

### Command Default

The default soft keys for the remote-in-use call state and the order
                              		  in which they appear on SIP phones are Barge, Newcall, cBarge.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

The remote-in-use call state is when another phone is connected to a
                              		  call on a directory number shared by this phone.

## Examples

In the following example, SIP phone template 1 modifies the soft keys
                              		  displayed for the alerting, connected, and remote-in-use call states:

```
Router(config)# voice register template 1 Router(config-register-temp)# softkeys alerting Callback Endcall Router(config-register-temp)# softkeys connected Confrn Hold Endcall Router(config-register-temp)# softkeys remote-in-use CBarge Newcall
```

### Related Commands

Command

Description

softkeys alerting (voice register template)

Modifies the soft-key display on SIP phones during the
                                          						alerting call state.

softkeys idle (voice register template)

Modifies the soft-key display on SIP phones during the idle
                                          						call state.

softkeys seized (voice register template)

Modifies the soft-key display on SIP phones during the
                                          						seized call state.

template (voice register pool)

Applies a phone template to a SIP phone.

## softkeys ringin
                        	 (voice register template)

To modify the
                              		  soft-key display during the ringing call state on SIP phones, use the softkeys ringIn command in voice register template configuration mode. To
                              		  remove the softkeys ringIn configuration, use the no form of
                              		  this command.

softkeys ringIn [ Answer ] [ DND ] [ iDivert ] [ HLog ]

no softkeys ringIn

### Syntax Description

Answer

(Optional) Soft key that picks up an incoming call.

DND

(Optional) Soft key that enables the Do Not Disturb feature.

HLog

(Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls.

iDivert

(Optional) Immediately diverts a call to a voice-messaging system.

### Command Default

The following
                              		  soft keys are displayed in alphabetical order, first to last, on IP phones
                              		  during the ringIn call state: Answer, Dnd, HLog, and iDivert.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(22)YB

Cisco
                                          						Unified CME 7.1

This
                                          						command was introduced.

12.4(24)T

Cisco
                                          						Unified CME 7.1

This
                                          						command was integrated into Cisco IOS Release 12.4(24)T.

Cisco IOS XE Everest 16.4.1

15.6(3)M1

Cisco Unified CME 11.6

HLog Softkey support was introduced.

### Usage Guidelines

Use this command
                              		  to create a template in which you specify which soft keys are displayed, and in
                              		  what order, on an IP phone during the ringing call state. The ringing calling
                              		  state is after a call is received and before the call is connected.

Any soft key that
                              		  is not explicitly specified with this command is disabled if this command is
                              		  used to change the default soft keys.

Configure the Answer keyword to enable a phone user to answer an incoming call on a line button that
                              		  is unavailable; for example, if a line button is configured with a dual-line
                              		  directory number and a call is holding on one channel of the directory number
                              		  and another call is ringing on the second channel, the phone user can press the
                              		  Answer soft key to pick up the incoming call on the second channel.

Configure the DND keyword
                              		  to enable the phone user to place the phone into Do-Not-Disturb mode. Configure
                              		  the Dnd soft key and the hunt-group logout DND command to enable the phone user to invoke DND
                              		  mode and log the phone out of hunt groups in which it is a member.

Configure the iDivert keyword to immediately divert a call to a voice-messaging system.

Configure the HLog keyword to place a phone into not-ready status, in which it does not accept
                              		  hunt-group calls.

To apply an voice
                              		  register template to a phone, configure the voice register
                                    				template command in voice register pool configuration mode.

## Examples

In the following
                              		  example, SIP phone template 1 is configured for the ringing state, and for the
                              		  alerting and connected call states:

```
Router(config)# voice register template 1 Router(config-register-template)# softkeys ringIn Answer Dnd Hlog iDivert Router(config-register-template)# softkeys idle Newcall Redial Pickup Cfwdall HLog Router(config-register-template)# softkeys connected Transfer Hold Endcall HLog
```

### Related Commands

Command

Description

softkeys connected (voice register template)

Modifies the soft-key display on SIP phones during the connected call state.

softkeys hold (voice register template)

Modifies the soft-key display on SIP phones during the hold call state.

softkeys idle (voice register template)

Modifies the soft-key display on SIP phones during the idle call state.

softkeys seized (voice register template)

Modifies the soft-key display on SIP phones during the seized call state.

## softkeys ringing

To configure an ephone template for soft-key display during the
                              		  ringing call state, use the softkeys ringing command in ephone-template configuration mode. To remove the softkeys ringing configuration, use the no form of this command.

softkeys ringing [ Answer ] [ Dnd ] [ HLog ]

no softkeys ringing

### Syntax Description

Answer

(Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state.

Dnd

(Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state.

HLog

(Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state.

### Command Default

The following soft keys are displayed in alphabetical order, first to
                              		  last, on IP phones during the ringing call state: Answer, Dnd, HLog

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command in ephone-template configuration mode to create a
                              		  template in which you can specify which soft keys are displayed, and in what
                              		  order, on an IP phone during the ringing call state. The ringing calling state
                              		  is when a call is received and before the call is connected.

Any soft key that is not explicitly configured is disabled.

You can enter any of the keywords in any order. The number and order
                              		  of soft keys listed in the softkeys ringing command corresponds to the number and
                              		  order of soft keys that will appear on IP phones during the ringing call state.

Configure the Answer keyword with this command to enable a
                              		  phone user to answer an incoming call on a line button that is unavailable; for
                              		  example, if a line button is configured with a dual-line directory number and a
                              		  call is holding on one channel of the directory number and another call is
                              		  ringing on the second channel, the phone user can use the Answer soft key to
                              		  pick up the incoming call on the second channel.

Configure the HLog keyword with this command to display the Hlog soft key during the ringing call state. To
                              		  enable HLog softkey functionality during the call ringing state, you must also
                              		  configure the hunt-group logout HLog command. If you configure the Hlog soft key
                              		  and do not configure the hunt-group logout HLog command, the Hlog soft key appears on the
                              		  phone screen but is not functional. The HLog softkey is a toggle for enabling
                              		  or disabling the not-ready status, in which the directory number does not
                              		  accept hunt-group calls.

Configure the Dnd keyword with this command to enable the
                              		  phone user to place the phone into Do-Not-Disturb mode. Configure the Dnd soft
                              		  key and the hunt-group logout DND command to enable the phone user to invoke DND
                              		  mode and log the phone out of hunt groups in which it is a member.

To apply an ephone template to phone, configure the ephone-template (ephone) command in the ephone configuration mode.

## Examples

In the following example, ephone template 1 is configured for the
                              		  ringing state, and for the alerting and connected call states:

```
Router(config)# telephony-service Router(config-telephony)# ephone-template 1 Router(config-ephone-template)# softkeys ringing Answer Dnd Hlog Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

dnd feature ring

Allows phone buttons configured with the feature-ring
                                          						option to not ring when their phones are in do-not-disturb (DND) mode.

ephone-template (ephone)

Applies an ephone template to an ephone.

hunt-group logout

Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents.

softkeys alerting

Configures an ephone template for soft-key display during
                                          						the alerting call state.

softkeys connected

Configures an ephone template for soft-key display during
                                          						the connected call state.

softkeys idle

Configures an ephone template for soft-key display during
                                          						the idle call state.

softkeys seized

Configures an ephone template for the soft-key display
                                          						during the seized call state.

## softkeys seized

To modify the order and type of soft keys that display on an IP phone
                              		  during the seized call state, use the softkeys seized command in ephone-template configuration mode. To remove a softkeys seized configuration, use the no form of this command.

softkeys seized [ CallBack ] [ Cfwdall ] [ CWOff ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ]

no softkeys seized

### Syntax Description

CallBack

(Optional) Soft key that requests callback notification
                                          						when a busy called line becomes free.

Cfwdall

(Optional) Soft key that forwards all calls.

CWOff

(Optional) Soft key that disables Call Waiting.

Endcall

(Optional) Soft key that ends the current call.

Gpickup

(Optional) Soft key that selectively picks up calls coming
                                          						into a phone number that is a member of a pickup group.

HLog

(Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls.

MeetMe

(Optional) Soft key that initiates a meet-me conference.

Pickup

(Optional) Soft key that selectively picks up calls to
                                          						another extension.

Redial

(Optional) Soft key that redials the last number dialed.

### Command Default

The default soft keys for the seized call stage and the order in
                              		  which they appear on IP phones are:

- With HLog support: Redial, EndCall, CFwdAll, CallPickUp,
                                 			 GrpCallPickUp, CallBack, HLog

- Without HLog support: Redial, EndCall, CFwdAll, CallPickUp,
                                 			 GrpCallPickUp, CallBack

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The HLog keyword was added.

12.4(9)T

Cisco Unified CME 4.0

The HLog keyword was integrated into
                                          						Cisco IOS Release 12.4(9)T.

12.4(11)XJ2

Cisco Unified CME 4.1

The MeetMe keyword was added.

12.4(15)T

Cisco Unified CME 4.1

The MeetMe keyword was integrated into
                                          						Cisco IOS Release 12.4(15)T.

15.0(1)XA

Cisco Unified CME 8.0

This command was modified. The CWOff keyword was added.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

The seized calling stage is when a caller is attempting a call and
                              		  has not yet been connected.

The number and order of soft keys listed in the softkeys seized command correspond to the number and order of soft keys on IP
                              		  phones.

You must configure the MeetMe soft key to initiate a meet-me
                              		  conference. Use this soft key for hardware conferencing only.

## Examples

In the following example, ephone template 1 modifies the soft keys in
                              		  the seized, alerting, and connected call states:

```
Router(config)# telephony-service Router(config-telephony)# ephone-template 1 Router(config-ephone-template)# softkeys seized Redial Cfwdall Pickup Router(config-ephone-template)# softkeys alerting Callback Endcall Router(config-ephone-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode for an IP phone.

ephone-template (ephone)

Applies an ephone template to an ephone.

hunt-group logout

Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of an HLog soft key on phones.

softkeys alerting

Modifies the soft keys that display during the alerting
                                          						call stage.

softkeys connected

Modifies the soft keys that display during the connected
                                          						call stage.

softkeys idle

Modifies the soft keys that display during the idle call
                                          						stage.

## softkeys seized (voice register template)

To modify the soft key display for the seized call state on Cisco
                              		  Unified SIP IP phones, use the softkeys seized command in voice register template
                              		  configuration mode. To return to the default, use the no form of this command.

softkeys seized [ Cfwdall ] [ Endcall ] [ Gpickup ] [ MeetMe ] [ Pickup ] [ Redial ]

no softkeys seized

### Syntax Description

Cfwdall

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Call forward all.” Forwards all calls.

Endcall

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Ends the current call.

Gpickup

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Group call pick up.” Selectively picks up
                                          						calls coming into a phone number that is a member of a pickup group.

MeetMe

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “MeetMe conference.” Initiates a meet-me
                                          						conference.

Pickup

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Call pick up.” Selectively picks up calls
                                          						coming into another extension.

Redial

(Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Redials the last number dialed.

### Command Default

The default soft keys for the seized call state and the order in
                              		  which they appear on Cisco Unified SIP IP phones are, from first to last:
                              		  Cfwdall, Endcall, Gpickup, MeetMe, Pickup, and Redial.

### Command Modes

Voice register template configuration (config-register-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

15.2(2)T

Cisco Unified CME 9.0

This command was modified. The MeetMe keyword was added.

### Usage Guidelines

The seized calling state is when a caller goes offhook before any
                              		  other action is taken.

The number and order of soft keys used in this command correspond to
                              		  the number and order of soft keys that appear on Cisco Unified SIP IP phones.
                              		  Any soft key that is not explicitly specified with this command is disabled.

The MeetMe soft key is added in the seized state when hardware
                              		  conference is enabled.

This command is not supported on the Cisco Unified 7905, 7912, 7940,
                              		  and 7960 SIP IP phones.

## Examples

In the following example, Cisco Unified SIP IP phone template 1 is
                              		  configured for the seized and connected call states:

```
Router(config)# voice register template 1 Router(config-register-template)# softkeys seized Redial Cfwdall Router(config-register-template)# softkeys connected Confrn Hold Endcall
```

### Related Commands

Command

Description

softkeys connected (voice register template)

Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the connected call state.

softkeys hold (voice register template)

Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the hold call state.

softkeys idle (voice register template)

Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the idle call state.

template (voice register pool)

Applies a template to a Cisco Unified SIP IP phone.

## source-addr

To specify the IP address of the certification authority proxy
                              		  function (CAPF) server on the Cisco Unified CME router, use the source-addr command in CAPF-server
                              		  configuration mode. To return to the default, use the no form of this command.

source-addr ip-address

no source-addr

### Syntax Description

ip-address

IP address of the Cisco Unified CME router.

### Command Default

No IP address is entered for the CAPF server in the router
                              		  configuration.

### Command Modes

CAPF-server configuration (config-capf-server)

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example identifies the IP address for the CAPF server
                              		  as 10.10.10.1:

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## source-address
                        	 (voice register global)

To identify the
                              		  IP address and port through which SIP phones communicate with a Cisco
                              		  CallManager Express (Cisco Unified CME) router, use the source-address command in voice register global
                              		  configuration mode. To disable the router from receiving messages from SIP
                              		  phones, use the no form of
                              		  this command.

source-address ip-address [ port port | secondary ip-address ]

no source-address ip-address

### Syntax Description

ip-address

Preexisting router IP address, typically one of the addresses of the Ethernet
                                          						port of the router.

port port

(Optional) TCP/IP port number to use for SIP. Range is 2000 to 9999. Default is
                                          						5060 for SIP phones.

secondary ip-address

Secondary router for Cisco Unified CME. TCP/IP port number is
                                          						same as the primary Cisco Unified CME router.

### Command Default

Port number for
                              		  SIP: 5060

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

Cisco
                                          						IOS XE Everest 16.4.1

Cisco
                                          						Unified CME 11.6

This
                                          						command was modified to add the keyword: secondary .

### Usage Guidelines

This command is a
                              		  mandatory command. The Cisco CallManager Express router cannot communicate with
                              		  the Cisco CME phones if the IP address is not provided. If the port number is
                              		  not provided, the SIP default port for is 5060. The IP address is usually the
                              		  IP address of the Ethernet port to which the phones are connected.

This command
                              		  enables a router to receive messages from Cisco IP phones through the specified
                              		  IP address and port.

For systems using
                              		  ITS V2.1, Cisco CME 3.0, or later versions, the IP phones receive their initial
                              		  configuration information and phone firmware from the TFTP server associated
                              		  with the router. The TFTP server address obtained by the Cisco IP phones points
                              		  to the router IP address. The Cisco IP phones transfer a configuration file
                              		  called SIPDefault.cnf. This file is automatically generated by the router
                              		  through the source-address and is placed in router memory. The
                              		  SIPDefault.cnf file contains the IP address that the phones, using the Session
                              		  Initiation Protocol (SIP), use to register for service. This IP address
                              		  corresponds to a valid Cisco Unified CME router IP address (and may be the same
                              		  as the router TFTP server address).

## Examples

The following
                              		  example shows how to set the IP source address and port:

```
Router(config)# voice register global Router(config-register-global)# source-address 10.6.21.4 port 6000 secondary 10.6.50.6
```

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profiles required for SIP phones.

file text (voice register global)

Generates ASCII text files for SIP phones.

tftp-path (voice register global)

Specifies the directory to which the provisioning file for SIP phones in a
                                          						Cisco CallManager Express (Cisco Unified CME) system will be written.

voice register global

Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco
                                          						SIP SRST environment.

## speed-dial

To create speed-dial definitions for a Cisco Unified IP phone or
                              		  analog phone that uses an analog telephone adaptor (ATA) in a Cisco Unified CME
                              		  system, use the speed-dial command in ephone or ephone-template
                              		  configuration mode. To disable a speed-dial definition, use the no form of this command.

speed-dial speed-tag digit-string [ label label-text ]

no speed-dial speed-tag

### Syntax Description

speed-tag

Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range is from 1 to 33.

digit-string

Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an ATA device.

For IP phones, if the first character of this string is the
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined.

label label-text

(Optional) String that contains identifying text to be
                                          						displayed next to the speed-dial button. Enclose the string in quotation marks
                                          						if the string contains a space.

### Command Default

No speed-dial definitions are created.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(15)ZJ

Cisco CME 3.0

The number of speed-dial definitions that can be created
                                          						was increased from 4 to 33. The ability to program speed-dial numbers at the
                                          						phone and the ability to lock speed-dial numbers were introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(11)XL

Cisco CME 3.2.1

This command was modified to allow IP phones to access more
                                          						speed-dial numbers than the number of available buttons on their phones and to
                                          						allow analog phones to access up to 33 speed-dial numbers.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

The speed-tag argument in this command is a
                              		  unique identifier for a speed-dial definition on the phone that is being
                              		  configured.

This command must be followed by a quick reboot of the phone using
                              		  the restart command.

If you use an ephone template to apply a to a phone and you also use
                              		  the same command in ephone configuration mode for the same phone, the value
                              		  that you set in ephone configuration mode has priority.

This command defines speed-dial numbers that are local to the ephone
                              		  that is being configured. The directory entry defines additional, systemwide speed-dial
                              		  numbers.

IP Phones

For IP phones, speed-dial numbers can be defined by administrators
                              		  using this command and the digit-string argument. The numbers are locked
                              		  if the digit-string argument begins with a plus sign
                              		  (+). Locked numbers cannot be changed at the phone. Speed-dial definitions
                              		  without speed-dial numbers (those defined with only a pound sign) and
                              		  speed-dial instances with unlocked digit-string arguments can be changed by
                              		  users at their IP phones. Changes made to speed-dial definitions are saved in
                              		  the router nonvolatile random-access memory (NVRAM) configuration after a
                              		  timer-based delay.

On Cisco Unified IP phones, speed-dial definitions are assigned to
                              		  available extension buttons that have not been assigned to extensions.
                              		  Speed-dial definitions are assigned in the order of their identifier (tag)
                              		  numbers. For example, if you define speed-dial 1, it is assigned to the first
                              		  phone button that is available after the buttons that have been assigned to
                              		  extensions. If you have used two buttons for extensions on a phone, speed-dial
                              		  1 is assigned to the third physical button on the phone. When you define
                              		  speed-dial 2, it is assigned to the fourth physical button on the phone, and so
                              		  on.

If more speed-dial definitions are created than are supported by the
                              		  IP phone setup, the extra speed-dial configurations can be dialed from IP
                              		  phones using this procedure:

- With the phone on-hook, an IP phone user presses a two-digit
                                 			 speed-dial code (that is, 05 for the entry with tag 5). A new soft key, Abbr,
                                 			 appears in the phone display.

- The phone user picks up the phone handset and presses the Abbr
                                 			 soft key. The full telephone number associated with the speed-dial tag is
                                 			 dialed.

Prior to Cisco IOS Releases 12.3(11)XL and 12.3(14)T, speed-dial
                              		  entries that were in excess of the number of physical phone buttons available
                              		  were ignored.

Analog Phones

Analog phone users who use a Cisco ATA-186, Cisco ATA-188, or Cisco
                              		  VG 224 to connect to a Cisco Unified CME system use a different method to
                              		  access speed-dial numbers. Analog phone users press the asterisk (*) key and
                              		  the speed-dial identifier (tag number) to dial a speed-dial number. For
                              		  instance, an analog phone user presses *1 to speed dial the number that has
                              		  been programmed as speed-dial 1 on that ephone. Analog phones can have up to 33
                              		  local speed-dial numbers programmed by the system administrator. The numbers
                              		  cannot be programmed from the phone.

Prior to Cisco IOS Releases 12.3(11)XL and 12.3(14)T, analog phones
                              		  were limited to nine speed-dial numbers.)

## Examples

The following example sets speed-dial button 2 to dial the phone
                              		  user’s assistant at extension 5001 and locks the setting so that the phone user
                              		  cannot change it at the phone:

```
Router(config)# ephone 23 Router(config-ephone)# speed-dial 2 +5001 label “Assistant”
```

### Related Commands

Description

directory entry

Adds a systemwide phone directory entry or speed-dial
                                          						entry.

restart (ephone)

Performs a fast reboot of a single IP phone in a Cisco
                                          						Unified CME system.

restart (telephony-service)

Performs a fast reboot of one or all phones in a Cisco
                                          						Unified CME system.

ephone-template (ephone)

Applies template to ephone configuration.

## speed-dial (voice logout-profile and voice user-profile)

To create speed-dial definitions in a user profile or logout profile
                              		  for Extension Mobility in Cisco Unified CME, use the speed-dial command in voice user-profile
                              		  configuration mode or voice logout-profile configuration mode. To disable a
                              		  speed-dial definition, use the no form of this command.

speed-dial speed-tag number [ label label ] [ blf ]

no speed-dial speed-tag

### Syntax Description

speed-tag

Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range: 1 to 36.

number

Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone, or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an analog telephone adapter (ATA) device.

For IP phones, if the first character of this string is the
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined.

label label

(Optional) String that contains identifying text to be
                                          						displayed next to the speed-dial button. Enclose the string in quotation marks
                                          						if the string contains a space.

blf

(Optional) Enables Busy Lamp Field (BLF) monitoring for a
                                          						speed-dial number.

### Command Default

No speed-dial definition is created.

### Command Modes

Voice logout-profile configuration (config-logout-profile) Voice user-profile configuration (config-user-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command in voice user-profile configuration mode to create a
                              		  speed-dial definition in a user profile for Extension Mobility. A user profile
                              		  is downloaded to the IP phone when a user is logged into an IP phone that is
                              		  registered in Cisco Unified CME and enabled for Extension Mobility.

Use this command in voice logout-profile configuration mode to create
                              		  a speed-dial definition in a logout profile for Extension Mobility. A logout
                              		  profile is downloaded to the IP phone when no user is logged into an IP phone
                              		  that is registered in Cisco Unified CME and enabled for Extension Mobility.

For button appearance, Extension Mobility will associate directory
                              		  numbers and then associates speed-dial definitions in the logout profile or
                              		  user profile to phone buttons in a sequential manner. If the profile contains
                              		  more directory and speed-dial numbers than there are buttons on the physical
                              		  phone to which the profile is downloaded, the remaining numbers in the profile
                              		  are ignored.

On Cisco Unified IP phones, speed-dial definitions are assigned to
                              		  available extension buttons that have not been assigned to extensions.
                              		  Speed-dial definitions are assigned in the order of their identifier (tag)
                              		  numbers, from 1 to 36.

## Examples

The following example shows the configuration for a user profile to
                              		  be downloaded when the a phone user logs into a Cisco Unified IP phone that is
                              		  enabled for Extension Mobility. The lines and speed-dial buttons in this
                              		  profile that are configured on an IP phone after the user logs in depend on the
                              		  phone type. For example, if the user logs into a Cisco Unified IP Phone 7970,
                              		  all buttons are configured according to voice-user profile1. However, if the
                              		  phone user logs into a Cisco Unified IP Phone 7960, all six lines are mapped to
                              		  phone buttons and the speed dial is ignored because there is no button
                              		  available for speed dial.

```
pin 12345
 user me password pass123
 number 2001 type silent-ring
 number 2002 type beep-ring
 number 2003 type feature-ring
 number 2004 type monitor-ring
 number 2005,2006 type overlay
 number 2007,2008 type cw-overly
 speed-dial 1 3001
 speed-dial 2 3002 blf
```

### Related Commands

Command

Description

logout-profile

Enables Cisco Unified IP phone for Extension Mobility and
                                          						assigns a logout profile to this phone.

reset (voice logout-profile and voice user-profile)

Performs complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded.

## speed-dial (voice register pool)

To create a speed-dial definition for a Cisco Unified SIP IP phone or
                              		  analog phone that uses an analog telephone adaptor (ATA) in a Cisco Unified
                              		  Communications Manager Express (Cisco Unified CME) system, use
                              		  the speed-dial command in voice register pool
                              		  configuration mode. To disable a speed-dial definition, use the no form of this command.

speed-dial speed-tag digit-string [ label label-text ]

no speed-dial speed-tag

### Syntax Description

speed-tag

Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range is 1 to 113.

digit-string

Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an ATA device.

For IP phones, if the first character of this string is a
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined.

label label-text

(Optional) Text string that appears next to the speed-dial
                                          						button. Enclose the string in quotation marks if the string contains a space.

### Command Default

No speed-dial definition is created.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

15.2(4)M

Cisco Unified CME 9.1

This command was modified to increase the number of
                                          						speed-dial configuration to 113.

### Usage Guidelines

The speed-dial command creates a speed-dial
                              		  definition for a Cisco Unified SIP IP phone being configured in Cisco Unified
                              		  CME.

The speed-tag argument is a unique identifier for
                              		  a speed-dial definition on the phone that is being configured. On Cisco Unified
                              		  IP phones, speed-dial definitions are assigned to available extension buttons
                              		  that have not been assigned to extensions. Speed-dial definitions are assigned
                              		  in the order of their identifier numbers.

For example, if you define speed-dial 1, it is assigned to the first
                              		  phone button that is available after the buttons that are assigned to
                              		  extensions. If you used two buttons for extensions on a phone, speed-dial 1 is
                              		  assigned to the third physical button on the phone. When you define speed-dial
                              		  2, it is assigned to the fourth physical button on the phone.

For Cisco Unified IP phones, speed-dial numbers can be assigned by
                              		  the administrator using the digit-string argument and can be locked if
                              		  the digit-string argument begins with a plus sign
                              		  (+). Locked numbers cannot be changed at the phone. Speed-dial instances
                              		  without speed-dial numbers (those defined with only a pound sign) and
                              		  speed-dial instances with unlocked digit-string arguments can be changed by
                              		  users at their Cisco Unified IP phones.

If more speed-dial definitions are created than are supported by the
                              		  IP phone setup, the extra speed-dial configurations are ignored.

Changes made to speed-dial buttons are saved in the router’s NVRAM
                              		  configuration after a timer-based delay.

Analog phone users who use a Cisco ATA-186 or Cisco ATA-188 to
                              		  connect to Cisco Unified CME systems use a different method to access
                              		  speed-dial numbers. Instead of pressing a speed-dial button, phone users with
                              		  ATA devices press the asterisk (*) key and a speed-tag number (speed-dial identifier) to
                              		  dial a speed-dial number. For instance, a phone user with a Cisco ATA-186
                              		  presses *1 to dial the number that has been programmed as speed-dial 1 on that
                              		  phone.

Phones with ATA devices are limited to a maximum of nine speed-dial
                              		  numbers that must be programmed by the system administrator. The numbers cannot
                              		  be programmed from the phone. With phones that use ATA devices, system
                              		  administrators must be sure to tell phone users when speed-dial numbers have
                              		  been programmed for their phones.

After you configure the speed-dial command, restart the phone using the reset command.

## Examples

The following example shows how to set speed-dial button 2 to dial
                              		  the head office at extension 5001 and lock the setting so that the phone user
                              		  cannot change it at the phone:

```
Router(config)# voice register pool 23 Router(config-register-pool)# speed-dial 2 +5001 label “Head Office”
```

The following example shows how to set speed-dial button 13 to dial
                              		  the sales office extension number (222):

```
Router(config)# voice register pool 3 Router(config-register-pool)# speed-dial 13 222 label “Sales Office”
```

### Related Commands

Command

Description

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router.

reset (voice register pool)

Performs a complete reboot of a specific SIP phone
                                          						associated with a Cisco Unified CME system.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## srst dn line-mode

To specify line mode for the ephone-dns that are automatically
                              		  created in Survivable Remote Site Telephony (SRST) mode on a Cisco Unified CME
                              		  router, use the srst dn line-mode command in telephony-service configuration mode. To return to
                              		  the default, use the no form of this command.

srst dn line-mode { dual | dual-octo | octo | single }

no srst dn line-mode

### Syntax Description

dual

SRST fallback ephone-dns are dual-line.

dual-octo

SRST fallback ephone-dns are dual-line or octo-line,
                                          						depending on the phone type.

octo

SRST fallback ephone-dns are octo-line.

single

SRST fallback ephone-dns are single-line.

### Command Default

Default is single-line mode.

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

12.4(15)XZ

Cisco Unified CME 4.3

The dual-octo and octo keywords were added.

12.4(20)T

Cisco Unified CME 7.0

This command with the dual-octo and octo keywords was integrated into
                                          						Cisco IOS Release 12.4(20)T.

### Usage Guidelines

This command specifies whether ephone-dns that are created during
                              		  fallback are dual-line, single-line, or octo-line ephone-dns. It applies only
                              		  to the ephone-dns that are “learned” automatically from ephone configuration
                              		  information, and not to ephone-dns that are manually configured in Cisco
                              		  Unified CME.

If you use the dual-octo keyword, the type of ephone-dn that
                              		  Cisco Unified CME in SRST mode creates depends on the phone type. It creates
                              		  dual-line ephone-dns if the phone type is a Cisco Unified IP Phone 7902 or
                              		  7920, or an analog phone connected to the Cisco VG224 or Cisco ATA. It creates
                              		  octo-line ephone-dns for all other phone types.

Use the show telephony-service ephone-dn command to display Cisco Unified CME parameters for ephone-dns.

## Examples

The following example specifies dual-line mode for all SRST fallback
                              		  ephone-dns.

```
telephony-service
 srst dn line-mode dual
```

### Related Commands

Command

Description

show telephony-service ephone-dn

Displays parameters for ephone-dns.

srst mode auto-provision

Enables SRST mode for a Cisco Unified CME router.

## srst dn template

To specify an ephone-dn template to be used in Survivable Remote Site
                              		  Telephony (SRST) mode on a Cisco Unified CallManager Express (Cisco Unified
                              		  CME) router, use the srst dn template command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

srst dn template template-tag

no srst dn template

### Syntax Description

template-tag

Identifying number of an existing ephone-dn template. Range
                                          						is from 1 to 15.

### Command Default

No ephone-dn template is specified.

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

### Usage Guidelines

This command applies the specified ephone-dn template to all SRST
                              		  fallback ephone-dns. Ephone-dn templates are created with the ephone-dn-template command.

Use the show telephony-service ephone-dn-template to display the contents of
                              		  ephone-dn templates.

## Examples

The following example applies ephone-dn template 2 to all SRST
                              		  fallback ephone-dns.

```
telephony-service
 srst dn template 2
```

### Related Commands

Command

Description

ephone-dn-template

Enters ephone-dn-template configuration mode to create an
                                          						ephone-dn template.

show telephony-service ephone-dn-template

Displays the contents of ephone-dn templates.

## srst ephone description

To specify a description to be associated with an ephone in
                              		  Survivable Remote Site Telephony (SRST) mode on a Cisco Unified CallManager
                              		  Express (Cisco Unified CME) router, use the srst ephone description command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

srst ephone description string

no srst ephone description

### Syntax Description

string

Description to be associated with an ephone. Maximum string
                                          						length is 100 characters.

### Command Default

No description is specified.

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

### Usage Guidelines

Use the show telephony-service ephone to display the ephone description to be associated with SRST
                              		  fallback phones.

## Examples

The following example applies a description to all SRST fallback
                              		  ephones.

```
telephony-service
 srst ephone description srst fallback auto-provision phone
```

The following excerpt displays a time-stamped SRST description for
                              		  ephone 1:

```
Router# show running-config ephone 1
 description srst fallback auto-provision phone : Jul 07 2005 17:45:08
 ephone-template 5
 mac-address 100A.7052.2AAE
 button 1:1 2:2
```

### Related Commands

Command

Description

show telephony-service ephone

Displays ephone settings.

## srst ephone template

To specify an ephone template to be used in Survivable Remote Site
                              		  Telephony (SRST) mode on a Cisco Unified CallManager Express (Cisco Unified
                              		  CME) router, use the srst ephone template command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

srst ephone template template-tag

no srst ephone template

### Syntax Description

template-tag

Identifying number of an existing ephone template. Range is
                                          						from 1 to 20.

### Command Default

No ephone template is specified.

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

### Usage Guidelines

Ephone templates are created with the ephone-template command. This command applies
                              		  the specified ephone template to all SRST fallback ephones.

Use the show telephony-service ephone-template to display the contents of ephone
                              		  templates.

## Examples

The following example applies ephone template 3 to all SRST fallback
                              		  ephones.

```
telephony-service
 srst ephone template 3
```

### Related Commands

Command

Description

ephone-template

Enters ephone-template configuration mode to create an
                                          						ephone template.

show telephony-service ephone-template

Displays the contents of ephone templates.

## srst mode auto-provision

To enable Survivable Remote Site Telephony (SRST) mode for a Cisco
                              		  Unified CallManager Express (Cisco Unified CME) router, use the srst mode auto-provision command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

srst mode auto-provision { all | dn | none }

no srst mode auto-provision

### Syntax Description

all

Includes information for learned ephones and ephone-dns in
                                          						the running configuration.

dn

Includes information for learned ephone-dns in the running
                                          						configuration.

none

Does not include information for learned ephones or learned
                                          						ephone-dns in the running configuration. Use this keyword when you want Cisco
                                          						Unified CME to provide SRST fallback services for Cisco Unified CallManager.

### Command Default

SRST mode is disabled.

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

### Usage Guidelines

This command puts a Cisco Unified CME router into SRST mode to
                              		  provide fallback call-processing services for IP phones that have lost
                              		  connection to their Cisco Unified CallManager. The phones can be preconfigured
                              		  manually or the Cisco Unified CME-SRST router can dynamically learn their
                              		  configuration. The keywords in this command allow you to specify how much of
                              		  the learned phone configurations you want to include in the running
                              		  configuration of the Cisco Unified CME-SRST router.

Use the none keyword to enable the Cisco Unified CME
                              		  router to provide SRST fallback services for Cisco Unified CallManager. Use the dn or all keyword to enable the Cisco Unified CME
                              		  router to learn the ephone-dn or ephone and ephone-dn configuration from Cisco
                              		  Unified CallManager and include the information in its running configuration.

## Examples

The following example shows how to enable the Cisco Unified CME
                              		  router to provide SRST fallback services for phones connected to Cisco Unified
                              		  CallManager. Information for learned ephone-dns and ephones is not included in
                              		  the running configuration.

```
telephony-service
 srst mode auto-provision none
```

### Related Commands

Command

Description

show telephony-service all

Displays detailed configuration for phones, voice ports,
                                          						and dial peers in a Cisco Unified CME system.

srst dn line-mode

Specifies line mode for the ephone-dns that are
                                          						automatically created in SRST mode on a Cisco Unified CME router.

## standby username password

To specify that the standby (secondary backup) router XML interface
                              		  is enabled, use the standby username password command in telephony-service configuration mode on the primary
                              		  router. To disable the XML interface on the secondary backup router, use the no form of this command.

standby username username password [0|6] password

no standby username username password [0|6] password

### Syntax Description

username

Specifies the username who is authorized to enable the XML
                                          						interface.

password

Specifies the password to use for access.

### Command Default

An authorized user is not named.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

Use this command to enable the XML interface on the secondary backup
                              		  router. The username and password must be the same as that used for access to
                              		  the primary router.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example enables the XML interface on the secondary
                              		  backup router:

```
Router(config)# telephony-service Router(config-telephony)# standby username admin password 1234
```

### Related Commands

Command

Description

username password

To assign a login account username and password to a phone
                                          						user so that the user can log in to the Cisco Unified CME router.

## statistics collect

To enable the collection of call statistics for an ephone hunt group,
                              		  use the statistics collect command in ephone-hunt configuration mode.
                              		  To stop statistics collection and to delete statistics that have been
                              		  collected, use the no form of this command.

statistics collect

no statistics collect

### Syntax Description

This command has no arguments or keywords.

### Command Default

The default is no call statistics data is collected.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

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

This command is used for the collection of call statistics, such as
                              		  direct calls to hunt group pilot numbers, or calls to the Basic Automatic Call
                              		  Distribution (B-ACD) and Auto Attendant service. For detailed information, see Cisco
                                 			 Unified CME B-ACD and Tcl Call-Handling Applications .

The statistics collect can be used to activate statistics
                              		  collection for any number of ephone hunt groups.

Statistics collection begins at the time that the statistics collect is entered. A maximum of one week (168
                              		  hours) of statistics can be stored at a time. You can display the statistics
                              		  with the show hunt-group or transfer statistics automatically to
                              		  files using TFTP. The no statistics collect deletes all statistics that have been
                              		  collected.

All or some of the statistics can be output with the show hunt-group or sent to files automatically using TFTP by using the hunt-group report url hunt-group report every hours commands.

## Examples

The following example enables the collection of call statistics for
                              		  ephone hunt group 1 and ephone hunt group 2:

```
Router(config)# ephone-hunt 1 Router(config-ephone-hunt)# statistics collect Router(config)# ephone-hunt 2 Router(config-ephone-hunt)# statistics collect
```

### Related Commands

Command

Description

hunt-group report delay hours

Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file.

hunt-group report every hours

Sets the hourly interval at which Cisco CME B-ACD call data
                                          						is automatically transferred to a file.

hunt-group report url

Sets filename parameters and the URL path where Cisco CME
                                          						B-ACD call statistics are to be sent using TFTP.

show ephone-hunt statistics

Displays ephone-hunt configuration information and current
                                          						status and statistics information.

## statistics collect (voice hunt-group)

To enable the collection of call statistics for a voice hunt group,
                              		  use the statistics collect command in voice hunt-group configuration
                              		  mode. To return to the default, use the no form of this command.

statistics collect

no statistics collect

### Syntax Description

This command has no arguments or keywords.

### Command Default

No configuration statistics can be collected for voice hunt groups.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

## Examples

The following example shows how to enable the collection of call
                              		  statistics for voice hunt group 60:

```
Router(config)# voice hunt-group 60 Router(config-voice-hunt-group)# statistics collect
```

### Related Commands

Command

Description

statistics collect

Enables the collection of call statistics for an ephone
                                          						hunt group.

## subnet

To define which IP phones are part of an emergency response location
                              		  (ERL) for the enhanced 911 service, use the subnet command in voice emergency response
                              		  location configuration mode. To remove the subnet definition, use the no form of this command.

subnet [ 1 | 2 ] IPaddress mask

no subnet [ 1 | 2 ]

### Syntax Description

IPaddress

IP address that identifies which IP phones are part of the
                                          						ERL.

mask

IP subnet mask for the network segment that is part of the
                                          						ERL.

### Command Default

No subnets are defined.

### Command Modes

Voice emergency response location configuration (cfg-emrgncy-resp-location)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added to Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to define the groups of IP phones that are part of
                              		  an ERL. You can create up to 2 different subnets. To include all phones on a
                              		  single ERL, you can set the subnet mask to 0.0.0.0 to indicate a “catch-all”
                              		  subnet.

## Examples

In the following example, all IP phones with the IP address of
                              		  10.X.X.X or 192.168.X.X are automatically associated with this ERL. If one of
                              		  the phones dials 911, its extension is replaced with 408 555-0100 before it
                              		  goes to the PSAP. The PSAP will see that the caller’s number is 408 555-0100.

```
voice emergency response location 1
 elin 1 4085550100
 subnet 10.0.0.0 255.0.0.0
 subnet 2 192.168.0.0 255.255.0.0
```

### Related Commands

Command

Description

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

## system message

To set a text message for display on idle Cisco IP Phones with
                              		  display, such as Cisco IP Phone 7940 and Cisco IP Phone 7960, in a Cisco
                              		  Unified Communications Manager Express (Cisco Unified CME) system, use the system message command in telephony-service configuration
                              		  mode. To return to the default, use the no form of this command.

system message text-message

no system message

### Syntax Description

text-message

Alphanumeric string of approximately 30 characters maximum
                                          						to display when the phone is idle.

### Command Default

The message “Cisco Unified Communications Manager Express” is
                              		  displayed.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco Unified CME 3.0

This command was introduced.

12.3(4)T

Cisco Unified CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The number of characters that can be displayed is not fixed because
                              		  IP phones typically use a proportional (as opposed to a fixed-width) font.
                              		  There is room for approximately 30 alphanumeric characters.

The display message is refreshed with a new message after any of the
                              		  following events occurs:

- A busy phone goes back on-hook.

- An idle phone receives a keepalive message.

- A phone is restarted.

## Examples

The following example sets the message “ABC Company” to display
                              		  instead of “Cisco Unified Communications Manager Express” on idle Cisco IP
                              		  Phones 7940 and 7940G and the Cisco IP Phones 7960 and 7960G:

```
Router(config)# telephony-service Router(config-telephony)# system message ABC Company
```

### Related Commands

Command

Description

telephony-service

Enters telephony-service configuration mode.

| max-calls number-of-calls | (Optional) Maximum number of active calls allowed on the
                                          						shared line. Range: 2 to 16. Default: 2. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| busy-trigger-per-button | Sets the maximum number of calls allowed on a SIP shared
                                          						line before activating Call Forward Busy or a busy tone. |
| debug shared-line | Displays debugging information about shared lines on SIP
                                          						phones. |
| huntstop | Disables call hunting behavior for a directory number on a
                                          						SIP phone. |
| number (voice register din) | Associates a telephone or extension number with a SIP
                                          						phone. |
| show shared-line | Displays information about shared lines on SIP phones. |
| show voice register dn | Displays all configuration information associated with a
                                          						specific voice register dn. |

| max calls number-of calls | (Optional) Maximum number of active calls allowed on the
                                          						shared line. Range: 2 to 16. Default: 2. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Note | The secondary number of an ephone-dn cannot be used as a search
                                       		  key in the Shared-Line Service Module. |
|---|---|

| Command | Description |
|---|---|
| dialplan pattern | Defines a pattern that is used to expand extension numbers
                                          						in Cisco Unified CME into fully qualified E.164 numbers, in telephony-service
                                          						configuration mode. |
| dialplan pattern (voice register) | Defines a pattern that is used to expand extension numbers
                                          						in Cisco Unified CME into fully qualified E.164 numbers, in voice register
                                          						global configuration mode. |
| shared-line | Creates a directory number to be shared by multiple Cisco
                                          						Unified SIP IP phones. |

| auth-string | Display
                                          						authentication strings for ephones. |
|---|---|
| sessions | Display
                                          						information about active CAPF sessions. |
| summary | Display
                                          						CAPF server configuration details. |

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

| State | Description |
|---|---|
| IDLE | Phone is
                                          					 idle. |
| AWAIT
                                          					 AUTH RES | A TLS
                                          					 connection was established on the TCP port that is specified in the
                                          					 configuration file. After a successful handshake verified the server
                                          					 certificate, a dialog was started between the CAPF server and the phone’s CAPF
                                          					 client. The server has challenged the phone by sending an authentication
                                          					 request and is waiting for a response. |
| AWAIT
                                          					 KEYGEN RESP | Phone
                                          					 authentication was successful. The CAPF server has sent a key generation
                                          					 request message to the phone and is waiting for a response. |
| AWAIT
                                          					 ENCRYPT MSG RESP | A key has
                                          					 been generated and the CAPF has used the phone’s public key to start the
                                          					 enrollment process with PKI. The CAPF sent an encrypt-message request to the
                                          					 phone and is waiting for a response. |
| AWAIT CA
                                          					 RESP | The
                                          					 phone has signed the received message using its private key and the CAPF has
                                          					 continued the enrollment process. PKI has forwarded the certificate request to
                                          					 the CA and is waiting for a response. |
| AWAIT
                                          					 STORE CERT RESP | Upon
                                          					 receiving an certificate issued from the CA, the CAPF has sent a
                                          					 store-certificate request message to the phone. The store-certificate request
                                          					 contains the certificate to be written to the phone’s flash memory. The CAPF is
                                          					 waiting for a store-certificate response message to confirm that the
                                          					 certificate has been stored. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco
                                          						SRST 3.3 | This
                                          						command was introduced for Cisco SRST. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was introduced for Cisco Unified CME. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command for Cisco Unified CME was integrated into Cisco IOS Release 12.4(9)T. |

| Field | Description |
|---|---|
| Credentials IP | Cisco
                                          					 Unified CME—IP address where the CTL provider is configured. Cisco
                                          					 Unified SRST—The specified IP address where certificates from Cisco Unified
                                          					 CallManager to the SRST router are received. |
| Credentials PORT | Cisco
                                          					 Unified CME—TCP port for credentials service communication. Default is 2444. Cisco
                                          					 Unified SRST—The port to which the SRST router connects to receive messages
                                          					 from the Cisco Unified IP phones. The port number is from 2000 to 9999. The
                                          					 default port number is 2445. |
| Trustpoint | Cisco
                                          					 Unified CME—CTL provider trustpoint label that will be used for TLS sessions
                                          					 with the CTL client. Cisco
                                          					 Unified SRST—The name of the trustpoint that is associated with the credentials
                                          					 service between the Cisco Unified CallManager client and the SRST router. |

|  | Description |
|---|---|
| credentials | Enters
                                          						credentials configuration mode to configure a Cisco Unified CME CTL provider
                                          						certificate or a Cisco Unified SRST router certificate. |
| ctl-service admin | Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol. |
| debug credentials | Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider and the CTL client or between a Cisco Unified SRST router and Cisco
                                          						Unified CallManager. |
| ip source-address (credentials) | Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with a Cisco Unified SRST router certificate. |

| call | Details for active (ACT) calls only. |
|---|---|
| gcid | List of Global Call IDs for active calls only. |
| line node | List of line nodes. |
| session | Details for active CTI sessions. |

| Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

| Field | Description |
|---|---|
| GCID | Global Call ID (Gcid)—Unique identifier in for every call on
                                          					 an outbound leg of a VoIP dial peer for an endpoint. A single Gcid remains the
                                          					 same for the same call in the system, and is valid for redirect, transfer, and
                                          					 conference events. |
| CallID | Unique identifier for each call leg of a call. |

| Command | Description |
|---|---|
| clear cti session | Clears the session between a CSTA client application and
                                          						Cisco Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| mac-address | (Optional) Displays information for the phone with the specified MAC address. |
|---|---|
| phone-type | (Optional) Displays information for phones of the specified phone type.
                                          						Supported phone types are version-specific. Type ? to display
                                          						a list of values. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						ITS 1.0 Cisco SRST 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						ITS 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(11)T | Cisco
                                          						ITS 2.01 Cisco SRST 2.01 | The ata keyword
                                          						was added and this command was implemented on the Cisco 1760. |
| 12.2(11)YT | Cisco
                                          						ITS 2.1 Cisco SRST 2.1 | The 7914 keyword
                                          						was added. |
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | The 7902 , 7905 , and 7912 keywords
                                          						were added. |
| 12.3(7)T | Cisco
                                          						CME 3.1 Cisco SRST 3.1 | The 7920 and 7936 keywords
                                          						were added. |
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 Cisco SRST 3.2.1 | The 7970 keyword
                                          						was added. |
| 12.3(14)T | Cisco
                                          						CME 3.3 Cisco SRST 3.3 | The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T. |

| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added. |
|---|---|---|
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(6)XE | Cisco
                                          						Unified CME 4.0(2) | The 7931 keyword was added for Cisco Unified CME. |
| 12.4(4)XC4 | Cisco
                                          						Unified CME 4.0(3) | The 7931 keyword was added for Cisco Unified CME. |
| 12.4(11)T | Cisco
                                          						Unified CME 4.0(3) | The 7931 keyword for Cisco Unified CME was integrated into Cisco IOS Release 12.4(11)T. |
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 Cisco Unified SRST 4.1 | The 7921 and 7985 keywords were added. |
| 12.4(15)T1 | Cisco
                                          						Unified CME 4.1(1) Cisco Unified SRST 4.1(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were added and this command was integrated into Cisco IOS Release
                                          						12.4(15)T1. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) Cisco Unified SRST 4.2(1) | Emergency response location (ERL) information displays in the output. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3 | Support for user-defined phone types created with the ephone-type command was added. |
| 12.4(15)XZ1 | Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3 | The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0 | The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added and this command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The IP-STE keyword was added and logical partitioning
                                          						class of restriction (LPCOR) and Cancel Call Waiting information was added to
                                          						the output. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Field | Description |
|---|---|
| Active
                                          					 Call | An
                                          					 active call is in progress. |
| activeLine | Line
                                          					 (button) on the phone that is in use. Zero indicates that no line is in use. |
| auto-dial number | Intercom extension that automatically dials number . |
| button number : dn number | Phone
                                          					 button number and the extension (ephone-dn) dn-tag number associated with that
                                          					 button. |
| bytes | Total
                                          					 number of voice data bytes sent or received by the phone. |
| Called
                                          					 Dn, Calling Dn | Ephone-dn tag numbers of the called and calling ephone-dn. Set to -1 if the
                                          					 call is not to or from an ephone-dn, or if there is no active call. |
| cfa number | Call-forward-all to number is
                                          					 enabled for this extension. |
| CH1 CH2 | Status
                                          					 of channel 1 and, if this is a dual-line ephone-dn, the status of channel 2. |
| cw | 1
                                          					 indicates that Call Waiting is enabled. 0 indicates that Call Waiting is
                                          					 disabled. |
| debug | 1
                                          					 indicates that debug for the phone is enabled. 0 indicates that debug is
                                          					 disabled. |
| DnD | Do Not
                                          					 Disturb is set on this phone. |
| DP tag | Not
                                          					 used. |
| ephone- number | Unique
                                          					 sequence number used to identify this phone during configuration (phone-tag). |
| IP | Assigned IP address of the Cisco Unified IP phone. |
| Jitter | Amount
                                          					 of variation (in milliseconds) of the time interval between voice packets
                                          					 received by the Cisco Unified IP phone. |
| keepalive | Number
                                          					 of keepalive messages received from the Cisco Unified IP phone by the router. |
| Latency | Estimated playout delay for voice packets received by the Cisco Unified IP
                                          					 phone. |
| line number | Button
                                          					 number on an IP phone. Line 1 is the button nearest the top of the phone. |
| Lost | Number
                                          					 of voice packets lost, as calculated by the Cisco Unified IP phone, on the
                                          					 basis of examining voice packet time-stamp and sequence numbers during playout. |
| Lpcor
                                          					 Incoming | Setting
                                          					 of the lpcor incoming command. |
| Lpcor
                                          					 Outgoing | Setting
                                          					 of the lpcor outgoing command. |
| Lpcor
                                          					 Type | Setting
                                          					 of the lpcor type command. |
| Mac | MAC
                                          					 address. |
| Max
                                          					 Conferences | Maximum
                                          					 number of allowable conference calls and number of active conference calls. |
| max_line number | Maximum
                                          					 number of line buttons that can be configured on this phone. |
| mediaActive | 1
                                          					 indicates that an active conversation is in progress. 0 indicates that no
                                          					 conversation is ongoing. |
| monitor-ring | This
                                          					 button is set up as a monitor button. |
| number | Telephone or extension number associated with the Cisco Unified IP phone button
                                          					 and its dn-tag. |
| offhook | 1
                                          					 indicates that the phone is off-hook. 0 indicates that the phone is on-hook. |
| overlay | This
                                          					 button contains an overlay set. Use show ephone overlay to display the contents of overlay sets. |
| paging | 1
                                          					 indicates that the phone has received an audio page. 0 indicates that the phone
                                          					 has not received an audio page. |
| paging-dn | Ephone-dn that is dedicated for receiving audio pages on this phone. The
                                          					 paging-dn number is the number of the paging set to which this phone belongs. |
| Password | Authentication string that the phone user types when logging in to the
                                          					 web-based Cisco Unified CME GUI. |
| Port | Port
                                          					 used for TAPI transmissions. |
| REGISTERED | The
                                          					 Cisco Unified IP phone is active and registered. Alternative states are
                                          					 UNREGISTERED (indicating that the connection to the Cisco Unified IP phone was
                                          					 closed in a normal manner) and DECEASED (indicating that the connection to the
                                          					 Cisco Unified IP phone was closed because of a keepalive timeout). |
| reset | Pending
                                          					 reset. |
| reset_sent | Request
                                          					 for reset has been sent to the Cisco Unified IP phone. |
| ringing | 1
                                          					 indicates that the phone is ringing. 0 indicates that the phone is not ringing. |
| Rx Pkts | Number
                                          					 of received voice packets. |
| silent-ring | Silent
                                          					 ring has been set on this button and extension. |
| socket | TCP
                                          					 socket number used to connect to IP phone. |
| speed
                                          					 dial speed-tag:digit-string label-text | This
                                          					 button is a speed-dial button, assigned to the speed-dial sequence number speed-tag .
                                          					 It dials digit-string and displays the text label-text next to the button. |
| sub=3,
                                          					 sub=4 | Subtype
                                          					 3 means that one Cisco Unified IP Phone 7914 Expansion Module is attached to
                                          					 the main Cisco Unified IP Phones 7960 and 7960G, and subtype 4 means that two
                                          					 are attached. |
| Tag number | Dn-tag
                                          					 number, the unique sequence number that identifies an ephone-dn during
                                          					 configuration, followed by the type of ephone-dn it is. |
| TAPI
                                          					 Client IP Address | IP
                                          					 address of the PC running the TAPI client. |
| TCP
                                          					 socket | TCP
                                          					 socket number used to communicate with the Cisco Unified IP phone. This can be
                                          					 correlated with the output of other debug and show commands. |
| Telecaster model-number | Type
                                          					 and model of the Cisco Unified IP phone. This information is received from the
                                          					 phone during its registration with the router. |
| Tx Pkts | Number
                                          					 of transmitted voice packets. |
| Username | Username that the phone user types when logging in to the web-based Cisco
                                          					 Unified CME GUI. |

| Command | Description |
|---|---|
| show ephone-dn | Displays information about Cisco Unified IP phone extensions (ephone-dns). |
| show ephone login | Displays the login states of all local ephones. |
| show telephony-service all | Displays systemwide status and information for a Cisco Unified CME system. |

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

| Field | Description |
|---|---|
| Num | Index
                                          					 number. |
| Mac
                                          					 Address | MAC
                                          					 address of the ephone. |
| DateTime | Date and
                                          					 time that the attempt to register was made. |
| DeviceType | Type of
                                          					 ephone. |

| Command | Description |
|---|---|
| auto-reg-ephone | Enables
                                          						automatic registration of ephones with the Cisco Unified CME system. |
| clear telephony-service ephone-attempted-registrations | Empties the log of ephones that unsuccessfully attempt to register with Cisco
                                          						Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| dn-tag | (Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0 | This
                                          						command was modified. LOCAL and GLOBAL replace TRUE in the output for “Pin
                                          						enabled.” |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Field | Description |
|---|---|
| ephone phone-tag | Phone
                                          					 identified with its unique phone-tag sequence number. |
| Pin
                                          					 enabled | In
                                          					 Cisco Unified CME 7.1 and earlier versions: TRUE—A PIN is defined for this phone. FALSE —No PIN is defined for this phone. In
                                          					 Cisco Unified CME 8.0 and later versions: LOCAL—A PIN has been defined for this phone. GLOBAL—A global PIN is defined for this Cisco Unified CME system. FALSE—No PIN is defined. |
| Logged-in | TRUE
                                             						indicates that a phone user is currently logged in on this phone. FALSE indicates that no phone user is currently logged in on this phone. |

| Command | Description |
|---|---|
| login (telephony-service) | Defines when users of IP phones in a Cisco Unified CME system are logged out
                                          						automatically. |
| pin | Sets
                                          						set a personal identification number (PIN) for an IP phone in a Cisco Unified
                                          						CME system. |
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show ephone-dn | Displays MOH group information for a phone directory
                                          						number. |
| show ephone summary | Displays the information about the MOH files in use |
| show voice moh-group statistics | Displays the MOH subsystem statistics information |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command is introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command is integrated into Cisco IOS Release 12.3(4)T. |
| Cisco IOS XE Gibraltar 16.11.1a | Unified CME 12.6 | This command is enhanced to display the keys that are in use per media stream, along with the sRTP Ciphers. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| overlay number | Displays
                                          					 the contents of an overlay set, including each dn-tag and its associated
                                          					 extension number. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| DeviceName | Device
                                          					 name. |
| CurrentPhoneLoad | Current
                                          					 phone firmware version. |
| PreviousPhoneLoad | Phone
                                          					 firmware version before last phone load. |
| LastReset | Reason
                                          					 for last reset of phone. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The output was enhanced to include the setting of the
                                          						feature-button command. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Field | Description |
|---|---|
| active | Number of
                                          					 active parties registered. |
| ephone | Cisco IP
                                          					 phone. |
| mac-address | MAC
                                          					 address of the Cisco IP phone. |
| keepalive | Defines
                                          					 keepalive timeout period to unregister IP phone. |
| feature-buttons | Displays
                                          					 the type of feature button on the ephone. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Note | The * symbol
                                          			 adjacent to the Directory Number (DN) in the command output indicates that the
                                          			 Directory Number (DN) is an Overlay-dn. |
|---|---|

| Field | Description |
|---|---|
| DN | Directory
                                       				  number of the phone. |
| Ephone | Total
                                       				  number of ephone tags configured. |
| IP
                                       				  Address | IP
                                       				  address of the phones. |
| LN | Line
                                       				  number of the phone. |
| MacAddress | Shows the
                                       				  MAC address of the SCCP phone. |
| Number | Number
                                       				  assigned to ephone. |
| PhoneType | Shows the
                                       				  type of Cisco IP phone. |
| Status | Shows the
                                       				  registration status. |

| Command | Description |
|---|---|
| show ephone summary types | Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type. |
| show ephone unregistered summary | Displays the details of all the unregistered SCCP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Release | Modification |
|---|---|
| 15.2(1)T | This
                                          						command was introduced. |

| Note | When an ephone
                                       		  to non-ephone call is made, information on the non-ephone does not appear in a show ephone rtp connections command output. To display the
                                       		  non-ephone call information, use the show voip rtp connections command. |
|---|---|

| Field | Description |
|---|---|
| Ephone | Ephone
                                          					 tag number with an active call. |
| Line | Line
                                          					 appearance of the phone. |
| DN | Ephone-dn
                                          					 tag. |
| Chan | Channel
                                          					 of the ephone-dn. |
| SrcCallID | CCAPI
                                          					 CallID for the RTP connection source. For ephone to ephone calls, this will be
                                          					 0. SrcCallID compares to “CallId” in the show voip rtp connections command output. |
| DstCallID | CCAPI
                                          					 CallID for the RTP connection destination. For ephone to ephone calls, this
                                          					 will be 0. DstCallID compares to “dstCallId” in the show voip rtp connections command output. |
| Codec
                                          					 (xcoded) | Codec
                                          					 name used by the phone with the active call. If xcoded is ‘Y’, the phone has
                                          					 the dspfarm-assist keyword configured to transcode the
                                          					 code on the local leg to the indicated codec. |
| SrcNum | Caller’s number for the connection. This number is not necessarily the ephone’s
                                          					 DN. |
| DstNum | Called
                                          					 party’s number for the connection. |
| LocalIP | Call’s
                                          					 local IP address and port. This is usually the ephone’s IP address. The IP
                                          					 address in brackets is either in IPv4 or IPv6 format, followed by a colon and
                                          					 the port number. The port compares to the “LocalRTP” number in the show voip rtp connections command output. |
| RemoteIP | Call’s
                                          					 remote IP address and port. For flow-around ephone to ephone calls, this is
                                          					 usually the other ephone’s IP address. For flow-through trunk calls, this is
                                          					 usually the Cisco Unified CME’s IP address. The port compares to the “RmtRTP”
                                          					 number in the show voip rtp connections command output. |

| Command | Description |
|---|---|
| show ephone registered | Displays the status of registered SCCP phones in Cisco Unified CME. |
| show voip rtp connections | Displays information about Real-Time Transport Protocol (RTP) named event
                                          						packets. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show ephone summary | Displays information about Cisco IP phones. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco SIP CME 10.5 | This
                                       					 command was introduced. |

| Note | The asterisk
                                          			 symbol (*) adjacent to the Directory Number (DN) in the command output
                                          			 indicates that the Directory Number (DN) is an Overlay-dn. |
|---|---|

| Field | Description |
|---|---|
| DN | Directory
                                       				  number of the phone. |
| Ephone | ephone
                                       				  tag. |
| IP
                                       				  Address | IP
                                       				  address of the phone. |
| LN | Line
                                       				  number of the phone. |
| MacAddress | Shows the
                                       				  MAC address of the SCCP phone. |
| Number | Number
                                       				  assigned to ephone. |
| PhoneType | Shows the
                                       				  type of Cisco IP phone. |
| Status | Shows the
                                       				  registration status. |

| Command | Description |
|---|---|
| show ephone summary types | Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco CME 1.0 Cisco SRST 1.0 | This command was introduced. |
| 12.2(8)T | Cisco CME 2.0 Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						. |
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was modified. The output was enhanced to show
                                          						IPv6 or IPv4 addresses configured on ephones. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was modified. The output was enhanced to show
                                          						voice-class stun-usage information. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| show ephone summary brief | Displays the details of all the SCCP phones configured. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| number | Telephone number that is associated with an ephone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco SIP CME 10.5 | This
                                       					 command was introduced. |

| Note | The * symbol
                                          			 adjacent to the Directory Number (DN) in the command output indicates that the
                                          			 Directory Number (DN) is an Overlay-dn. |
|---|---|

| Field | Description |
|---|---|
| DN | Directory number of the phone. |
| Ephone | Total number of ephone tags configured. |
| IP Address | IP address of the phones. |
| LN | Line number of the phone. |
| MacAddress | Shows the MAC address of the SCCP phone. |
| Number | Number assigned to ephone. |
| PhoneType | Shows the type of Cisco IP phone. |
| Status | Shows the registration status. |

| Command | Description |
|---|---|
| show ephone registered summary | Displays the details of all the registered SCCP phones. |
| show ephone summary types pattern | Displays the total number of registered and unregistered SCCP phones for each
                                          						phone type. |

| dn-tag | (Optional) For Cisco Unified CME, a unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). (Optional) For Cisco Unified SRST, a destination number tag. The destination
                                          						number can be from 1 to 288. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T command. |

| Field | Description |
|---|---|
| Administrative State | Administrative (configured) state of the voice port. |
| alert | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call alerting state (for example, because the far-end phone
                                          					 rang but was not answered and the far-end system decided to drop the call
                                          					 rather than let the phone ring for too long). |
| answered
                                          					 (incoming) | The
                                          					 number of incoming calls that were actually answered (the phone goes off hook
                                          					 when ringing). |
| answered
                                          					 (outgoing) | The
                                          					 number of outgoing call attempts that were answered by the far end. |
| busy | The
                                          					 number of outgoing call attempts that got a busy response. |
| Call
                                          					 Disconnect Time Out | Not
                                          					 applicable to the Cisco IP phone. |
| called,
                                          					 calling | Extension numbers of called and calling parties. |
| Caller
                                          					 ID Info Follows | Information about the caller ID. |
| Call
                                          					 Ref | A
                                          					 unique per-call identifier used by the SCCP protocol. The Call Ref values are
                                          					 assigned sequentially within the Cisco CME–SCCP interface, so this value also
                                          					 indicates the total number of SCCP calls since the router was last rebooted. |
| chan | Channel
                                          					 number of an ephone-dn. |
| CODEC | Codec
                                          					 type. |
| Companding Type | Not
                                          					 applicable to the Cisco IP phone. |
| connect | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call connected state. |
| Connection Mode | Not
                                          					 applicable to the Cisco IP phone. |
| Connection Number | Not
                                          					 applicable to the Cisco IP phone. |
| Description | Not
                                          					 applicable to the Cisco IP phone. |
| Digit
                                          					 Duration Timing | Not
                                          					 applicable to the Cisco IP phone. |
| DN
                                          					 STATE | Ephone-dn tag number and state of the phone line associated with an extension. |
| Echo
                                          					 Cancellation... | Not
                                          					 applicable to the Cisco IP phone. |
| Echo
                                          					 Cancel Coverage | Not
                                          					 applicable to the Cisco IP phone. |
| EFXS | Voice
                                          					 port type. |
| Far-end
                                          					 disconnect at... | See
                                          					 connect, alert, hold, and ring. |
| Final
                                          					 Jitter | The
                                          					 final voice packet receive jitter reported by the IP phone at the end of the
                                          					 call. |
| hold | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call hold state (for example, if the caller was left on hold
                                          					 for too long and got tired of waiting). |
| incoming | The
                                          					 number of incoming calls presented (the phone rings). |
| In Gain | Not
                                          					 applicable to the Cisco IP phone. |
| Initial
                                          					 Time Out | Amount
                                          					 of time the system waits for an initial input digit from the caller. |
| Interdigit Time Out | Amount
                                          					 of time the system waits for a subsequent input digit from the caller. |
| Last 64
                                          					 far-end disconnect cause codes | See the
                                          					 Mappings of PSTN Cause Codes to SIP Event table for a list of public switch
                                          					 telephone network (PSTN) cause codes that can be sent as an ISDN cause
                                          					 information element (IE) and the corresponding Session Interface Protocol (SIP)
                                          					 event. |
| Latency | The
                                          					 final voice packet receive latency reported by the IP phone at the end of the
                                          					 call. |
| Lost | Number
                                          					 of lost packets. |
| Music
                                          					 On Hold Threshold | Not
                                          					 applicable to the Cisco IP phone. |
| No
                                          					 Interface Down Failure | State
                                          					 of the interface. |
| Noise
                                          					 Regeneration | Not
                                          					 applicable to the Cisco IP phone. |
| Non
                                          					 Linear... | Not
                                          					 applicable to the Cisco IP phone. |
| Operation State | Operational state of the voice port. |
| Out
                                          					 Attenuation | Not
                                          					 applicable to the Cisco IP phone. |
| outgoing | The
                                          					 number of outgoing call attempts. |
| Playout-delay Maximum | Not
                                          					 applicable to the Cisco IP phone. |
| Playout-delay... | Not
                                          					 applicable to the Cisco IP phone. |
| Port | Port
                                          					 number for the interface associated with the voice interface card. |
| Region
                                          					 Tone | Not
                                          					 applicable to the Cisco IP phone. |
| ring | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the ringing state (for example, if the call was not answered and
                                          					 the caller hung up). |
| Ringing
                                          					 Time Out | Duration, in seconds, for which ringing is to continue if a call is not
                                          					 answered. Set with the timeouts ringing command. |
| Rx
                                          					 Pkts, bytes | Number
                                          					 of packets and bytes received during the current or last call. |
| Signal
                                          					 Level to phone, peak | For
                                          					 G.711 calls only, this parameter indicates the most recent voice signal level
                                          					 in the voice IP packets sent from the router to the IP phone. This parameter is
                                          					 valid only for VoIP or PSTN G.711 calls to the IP phones. This parameter is not
                                          					 valid for calls between local IP phones, or calls that use codecs other than
                                          					 G.711. The peak field indicates the peak signal level seen during the entire
                                          					 call. |
| Slot | Slot
                                          					 used in the voice interface card for this port. |
| Station
                                          					 name | Station
                                          					 name. |
| Station
                                          					 number | Station
                                          					 number. |
| Stream
                                          					 Port | RTP
                                          					 port allocated by the given DN/channel. |
| Sub-unit | Subunit
                                          					 used in the voice interface card for this port. |
| Tx
                                          					 Pkts, bytes | Number
                                          					 of packets and bytes transmitted during the current call or last call. |
| Type of
                                          					 VoicePort | Voice
                                          					 port type. |
| VAD | Voice
                                          					 activity detection. |
| Voice
                                          					 card specific info | Information specific to the voice card. |
| VPM
                                          					 STATE | State
                                          					 indication for the VPM software component. |
| VTSP
                                          					 STATE | State
                                          					 indication for the VTSP software component. |
| Wait
                                          					 Release Time Out | Time
                                          					 that a voice port stays in the call-failure state while the router sends a busy
                                          					 tone, reorder tone, or out-of-service tone to the port. |

| PSTN
                                          					 Cause Code | Description | SIP
                                          					 Event |
|---|---|---|
| 1 | Unallocated number | 410
                                          					 Gone |
| 3 | No
                                          					 route to destination | 404 Not
                                          					 found |
| 16 | Normal
                                          					 call clearing | BYE |
| 17 | User
                                          					 busy | 486
                                          					 Busy here |
| 18 | No user
                                          					 responding | 480
                                          					 Temporarily unavailable |
| 19 | No
                                          					 answer from the user |
| 21 | Call
                                          					 rejected | 603
                                          					 Decline |
| 22 | Number
                                          					 changed | 302
                                          					 Moved temporarily |
| 27 | Destination out of order | 404 Not
                                          					 found |
| 28 | Address
                                          					 incomplete | 484
                                          					 Address incomplete |
| 29 | Facility rejected | 501 Not
                                          					 implemented |
| 31 | Normal
                                          					 unspecified | 404 Not
                                          					 found |
| 34 | No
                                          					 circuit available | 503
                                          					 Service unavailable |
| 38 | Network
                                          					 out of order |
| 41 | Temporary failure |
| 42 | Switching equipment congestion |
| 44 | Requested channel not available |
| 47 | Resource unavailable |
| 55 | Incoming class barred within CUG | 603
                                          					 Decline |
| 57 | Bearer
                                          					 capability not authorized | 501 Not
                                          					 implemented |
| 58 | Bearer
                                          					 capability not presently available |
| 63 | Service
                                          					 or option unavailable | 503
                                          					 Service unavailable |
| 65 | Bearer
                                          					 cap not implemented | 501 Not
                                          					 implemented |
| 79 | Service
                                          					 or option not implemented |
| 87 | User
                                          					 not member of CUG | 603
                                          					 Decline |
| 88 | Incompatible destination | 400 Bad
                                          					 Request |
| 95 | Invalid
                                          					 message |
| 102 | Recover
                                          					 on timer expiry | 408
                                          					 Request timeout |
| 111 | Protocol error | 400 Bad
                                          					 request |
| 127 | Interworking unspecified | 500
                                          					 Internal server error |
| Any
                                          					 code other than those listed above | 500
                                          					 Internal server error |

| Command | Description |
|---|---|
| show ephone-dn callback | Displays information about pending callbacks in a Cisco Unified CME or a Cisco
                                          						Unified SRST environment. |
| show ephone-dn loopback | Displays information about loopback ephone-dns that have been created in a
                                          						Cisco Unified CME or a Cisco Unified SRST environment. |
| show ephone-dn statistics | Displays display call statistics for a Cisco IP destination or for extensions
                                          						(ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST environment. |
| show ephone-dn summary | Displays brief information about Cisco IP phone destination numbers or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| DN 3
                                          					 (95021) CallBack pending to DN 1 (95021) | Callback
                                          					 originator is the extension with the dn-tag 1 (in this example), and the
                                          					 callback has been placed on the extension with the dn-tag 3 and the number
                                          					 95021. |
| age | Number of
                                          					 seconds since the callback was placed. |
| State for
                                          					 DN 3 is CH1... CH2... | Call
                                          					 states for channel 1 and channel 2, if any, of the extension that the callback
                                          					 is for. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| ad-hoc | (Optional) Displays adhoc conferences. |
|---|---|
| meetme | (Optional) Displays meet-me conferences. |
| video | (Optional) Displays video conferences. |
| number number | (Optional) Displays the conference telephone or extension number. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The command output was enhanced to display the unlocked
                                          						Meet-Me conference setting. |
| 15.1(4)M | Cisco
                                          						CME 8.6 | This
                                          						command was modified to display information on video conferences. |

| Field | Description |
|---|---|
| active | Number
                                          					 of active parties in the conference. |
| DN tags | Directory numbers (DNs) in the conference. |
| inactive | Number
                                          					 of inactive parties in the conference. |
| number | Conference telephone or extension number. |
| type | Type of
                                          					 conference: meet-me or ad hoc. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |

| Field | Description |
|---|---|
| Called,
                                          					 Calling | Called
                                          					 number and calling number when there is a call present. |
| CalledDn,
                                          					 CallingDn | Ephone-dn
                                          					 tag numbers of the called and calling ephone-dn. Set to -1 if the call is not
                                          					 to or from an ephone-dn, or if there is no active call. |
| callID | Internal
                                          					 call reference. This usage is the same as in other Cisco IOS voice gateway
                                          					 commands. |
| DN | Ephone-dn
                                          					 tag (sequence number). |
| Forward | Number of
                                          					 digits in the original called number to forward to the other ephone-dn in the
                                          					 loopback-dn pair. |
| G711... | G711Ulaw64k indicates G.711 codec, mu-law, 64000-bit stream. G711alaw64k
                                          					 indicates G.711 codec, A-law, 64000-bit stream. |
| Loopback
                                          					 to command... | Indicates
                                          					 the opposite ephone-dn in the loopback pair and the status of that ephone-dn. |
| Media | IP
                                          					 destination address, if any, for any voice packets that are passing through the
                                          					 loopback DN. |
| min, max | Lowest
                                          					 and highest dn-tag numbers of ephone-dns that are configured as loopback-dns. |
| prefix | Digit
                                          					 string to add to the beginning of forwarded called numbers. |
| retry | Number
                                          					 of seconds to wait before retrying the loopback target when is it busy. |
| srcCallID | Internal call reference for the destination. |
| ssrc | Real-time transport protocol (RTP) synchronization source (SSRC) of the most
                                          					 recent RTP packet. |
| Strip | Number
                                          					 of leading digits to strip before forwarding to the other extension in the
                                          					 loopback-dn pair. |
| vector | The
                                          					 following values describe the media path for voice packets that pass through
                                          					 the loopback-dn: 0—No
                                             						media path or not a loopback-dn path (inactive). 1—Normal path. Loopback-dn has identified the final media destination as a
                                             						local IP phone. The media IP address field shows a valid, non-zero value. 2—Hairpin. Media packets are routed back through paired loopback-dns. The final
                                             						destination is not known. For example, this can be a VoIP-to-VoIP call path by
                                             						a loopback-dn. 3—Hairpin. The final destination is an ephone-dn in a special mode such as
                                             						paging. 4—Loopback-dn chain has been detected, in which two loopback-dn pairs have been
                                             						connected together. 5—Loopback-dn chain has been detected in which more than two loopback-dn pairs
                                             						are connected in series. |

| Command | Description |
|---|---|
| loopback-dn | Creates a virtual loopback voice port (loopback-dn) to establish a demarcation
                                          						point for VoIP voice calls and supplementary services. |
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| phone | Indicates
                                          					 the ephone-dn and the paging-dn tag. |
| ip
                                          					 address | Indicates
                                          					 the IP multicast address to multicast voice packets for audio paging. |
| port | Indicates
                                          					 the UDP port for multicast paging. Range is from 2000 to 65535. Note The
                                                   					 correct paging port for the paging-dn of Cisco Unified SIP IP phones is an even
                                                   					 number from 20480 to 32768 only. | Note | The
                                                   					 correct paging port for the paging-dn of Cisco Unified SIP IP phones is an even
                                                   					 number from 20480 to 32768 only. |
| Note | The
                                                   					 correct paging port for the paging-dn of Cisco Unified SIP IP phones is an even
                                                   					 number from 20480 to 32768 only. |

| Note | The
                                                   					 correct paging port for the paging-dn of Cisco Unified SIP IP phones is an even
                                                   					 number from 20480 to 32768 only. |
|---|---|

| Command | Description |
|---|---|
| paging-dn | Creates
                                          						a paging extension (paging-dn) to receive audio pages on a Cisco Unified IP
                                          						phone in a Cisco Unified CME system. |
| paging-dn (voice register) | Registers a Cisco Unified SIP IP phone to an ephone-dn paging directory number. |
| paging group | Creates a combined paging group from two or more previously established paging
                                          						sets. |

| Release | Modification |
|---|---|
| 12.3(7)T | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Ephone-dn
                                          					 tag (identifier) number for the call-park slot. |
| (1560) | Extension
                                          					 number associated with the call-park slot. |
| park-slot
                                          					 state | Whether
                                          					 the call-park slot is in use or idle. |
| Notify to
                                          					 ( ) | Extension
                                          					 that has been specified for notification. Empty parentheses indicate that no
                                          					 extension was specified in the configuration. |
| timeout | Number of
                                          					 seconds between reminder rings, in seconds. |
| limit | Number of
                                          					 reminder rings before a call parked at this slot is disconnected. |

| Command | Description |
|---|---|
| park-slot | Creates
                                          						a floating extension (ephone-dn) at which calls can be temporarily held
                                          						(parked). |

| dn-tag | (Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). |
|---|---|
| statistics | Displays voice quality statistics on calls for a specified
                                          						extension or for all extensions. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ1 | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone
                                          						destination number or for extensions (ephone-dns) in a Cisco Unified CME or a
                                          						Cisco Unified SRST environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |

| Field | Description |
|---|---|
| CODEC | Type of
                                          					 codec. |
| DN STATE | Status of
                                          					 the ephone-dn. |
| EFXS | Voice
                                          					 port type. |
| PORT | Port
                                          					 number (virtual) for this interface. The number that follows the last slash in
                                          					 the port number is the ephone-dn tag. For example, if the port number is
                                          					 50/0/1, the dn-tag is 1. |
| VAD | Voice
                                          					 activity detection status. |
| VPM STATE | State
                                          					 indication for the voice port module (VPM) software component. |
| VTSP
                                          					 STATE | State
                                          					 indication for the voice telephony service provider (VTSP) software component. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco
                                          						Unified CME 7.1 | This
                                          						command was introduced. |
| 12.4(24)T | Cisco
                                          						Unified CME 7.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(24)T. |

| Field | Description |
|---|---|
| DN | Directory
                                          					 number tag. |
| DN Number | Extension
                                          					 or telephone number assigned to directory number. |
| Label | Text
                                          					 string that identifies the whisper intercom line. |
| Speed
                                          					 Dial | Whisper
                                          					 intercom number to speed dial. |
| DN State | State of
                                          					 the directory number, either Idle or Busy. |
| Phone | Ephone
                                          					 that the directory number is assigned to. |

| Command | Description |
|---|---|
| debug ephone whisper-intercom | Displays debugging messages for the Whisper Intercom feature. |
| show ephone-dn | Displays status and configuration information for phone extensions (ephone-dns)
                                          						in Cisco Unified CME. |
| whisper-intercom | Enables the Whisper Intercom feature on a directory number. |

| tag | (Optional) Hunt-group number that was used to identify a hunt group in the ephone-hunt command. Range is 1 to 100. |
|---|---|
| summary | (Optional) Displays hunt group configuration information. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| show
                                          					 ephone-hunt Output | Description | auto
                                          					 logout Command |
|---|---|---|
| auto logout: no | The
                                          					 Automatic Agent Status Not-Ready feature is disabled. This is also the default
                                          					 if this command is not used. | no auto logout |
| auto logout: 1 type: both | The
                                          					 Automatic Agent Status Not-Ready feature is enabled and no options have been
                                          					 used with the auto logout command. The number of unanswered calls is
                                          					 1 and the command applies to both static and dynamic hunt group members by
                                          					 default. | auto logout |
| auto logout: 2 type: both | Two
                                          					 unanswered calls will be sent to a hunt group agent before the agent’s status
                                          					 is automatically changed to not ready. The command applies to both static and
                                          					 dynamic hunt group members by default. | auto logout 2 |
| auto logout: 3 type: static | Three
                                          					 unanswered calls will be sent to a hunt group agent before the agent’s status
                                          					 is automatically changed to not ready. The command applies to static hunt group
                                          					 members only. | auto logout 3 static |

| Field | Description |
|---|---|
| auto
                                          					 logout | Indicates whether the Automatic Agent Status Not-Ready feature has been
                                          					 enabled. See the table. |
| aux-number | Auxiliary number used to generate dial peers for a hunt group. This number is
                                          					 generated by the list command. |
| description | Description string entered for the ephone hunt group. This value is set using
                                          					 the description (ephone-hunt) command. |
| dn-tag | Directory number (DN) sequence number. |
| E.164
                                          					 register | Displays whether a pilot number registers with an H.323 gatekeeper. This value
                                          					 is set by the no-reg command. |
| final
                                          					 number | Last
                                          					 number in the ephone-hunt group, after which a call is no longer redirected.
                                          					 This value is set by the final command. |
| fwd-final | Final
                                          					 destination of an unanswered call that has been transferred into a hunt group:
                                          					 orig-phone means calls are returned to the transferring phone, and final means
                                          					 calls are sent to the final number specified in the configuration. This value
                                          					 is set by the fwd-final command. |
| hops | Number
                                          					 of hops before a call proceeds to the final number. This value is set by the hops command. |
| list of
                                          					 numbers | Extension numbers that are group members of the specified ephone hunt group.
                                          					 This value is set by the list command. |
| login/logout | Ready
                                          					 status of the agent: login means ready and accepting calls, and logout means
                                          					 not-ready and blocking hunt-group calls. |
| logout | Number
                                          					 of agents in the not-ready state (not accepting hunt-group calls). |
| max
                                          					 timeout | Maximum
                                          					 combined timeout for the no-answer periods for all ephone-dns in the
                                          					 ephone-hunt list. This value is set by the max-timeout command. |
| members
                                          					 initial state: logout/login | Sets
                                          					 all static members initial state to logout. |
| next-to-pick | (Peer
                                          					 hunt groups only) List number of the agent whose phone will ring when the next
                                          					 call comes in to the hunt group. (For example, if the order of agents in the list command is 451, 452, 453, 454, the list number 2 represents extension 452.) |
| off-hook agents | Number
                                          					 of agents who are currently off-hook. |
| on-hook
                                          					 time stamp | (Longest-idle hunt groups only) The last on-hook time of the agent, which is
                                          					 used to determine which agent to ring next time. |
| peers | Displays the number of ephone-dn dial peers. |
| peer-tag | Dial-peer sequence number. |
| pilot
                                          					 number | Number
                                          					 that callers dial to reach the ephone hunt group. |
| preference | Preference order set by the preference (ephone-hunt) command for the primary pilot number. |
| preference (sec) | Preference order set by the preference (ephone-hunt) command for the secondary pilot number. |
| rna | Number
                                          					 of unanswered hunt group calls (ring-no-answer) by this agent, used for the
                                          					 Automatic Agent Status Not-Ready feature. |
| stat
                                          					 collect | Indicates whether statistic are being Cisco Unified CME B-ACD data is being
                                          					 collected. See the statistics collect command. |
| timeout | Number
                                          					 of seconds after which a call that is not answered at one number is redirected
                                          					 to the next number in the hunt-group list. Multiple values in this field refer
                                          					 to the timeouts for the hops between ephone-dns in a hunt group as they appear
                                          					 in the list command. This value is set by the timeout command. |
| type | Type of
                                          					 ephone hunt group: longest-idle, peer, or sequential. |
| up/down | Dial
                                          					 peer is up or down. |

| Command | Description |
|---|---|
| auto logout | Enables automatic change of agent status to not-ready after a specified number
                                          						of hunt-group calls are not answered. |
| ephone-hunt | Enters ephone-hunt configuration mode to create a hunt group for use in a Cisco
                                          						Unified CME system. |
| hunt-group logout | Enables separate handling of DND and HLog functionality for hunt-group agents
                                          						and the display of an HLog soft key on phones. |
| members logout | Sets
                                          						all static members initial state to logout. |
| show
                                          						ephone-hunt statistics | Displays hunt group call statistics. |

| tag | Hunt-tag number that was used to identify a hunt group in an ephone-hunt command. Range is 1 to 100. |
|---|---|
| last | Displays information for the previous number of specified hours, counting
                                          						backward from the current hour. Range is 1 to 167. |
| hours hours | Number
                                          						of hours for which to display call statistics. |
| start | Defines
                                          						the start of a period for which to display call statistics. Default duration is
                                          						one hour. |
| day | Day of
                                          						week. Use sun , mon , tue , wed , thu , fri , or sat . |
| time | Hour of
                                          						day. Range is 0 to 23. |
| to | (Optional) Defines the stop time for display of call statistics. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco
                                          						CME 3.2 | This
                                          						command was introduced. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | Call
                                          						hold statistics were added. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | Call
                                          						hold statistics were integrated into Cisco IOS Release 12.4(9)T. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to add the following fields: Calls handoff to IOS, Average
                                          						time to handoff, Longest time to handoff, and Number of error calls. |

| Note | On the day
                                       		  that daylight saving time adjusts the time back by one hour at 2 a.m. each
                                       		  year, the original 1 a.m. to 2 a.m. statistics for that day are lost because
                                       		  they are overwritten by the new 1 a.m. to 2 a.m. statistics. |
|---|---|

| Field | Description |
|---|---|
| Abandoned calls | Total number of calls abandoned by hunt group agents. This
                                          					 does not include calls going to the final number. |
| Answered call | Total number of calls answered by hunt group agents. |
| Average
                                          					 time before abandon (secs) | Average
                                          					 length of time that unanswered calls waited before hanging up. |
| Average
                                          					 hold time (secs) | Average
                                          					 length of time that calls waited on hold for this agent. |
| Average
                                          					 time in call (secs) | Average
                                          					 length of time that unanswered calls waited before going to an agent. |
| Average
                                          					 time in hold (secs) | Average
                                          					 length of time that calls were kept on hold for all agents. |
| Average
                                          					 time to answer (secs) | Average
                                          					 length of time that all calls to Cisco Unified CME B-ACD waited before being
                                          					 answered. |
| Average
                                          					 time to handoff (secs) | Average
                                          					 length of time before a call was handed off to IOS. |
| Calls
                                          					 answered by voice mail | Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by voice mail. |
| Calls
                                          					 exited the queue | Total
                                          					 number of calls to Cisco Unified CME B-ACD that exited queues. |
| Calls
                                          					 forwarded to voice mail | Total
                                          					 number of calls to Cisco Unified CME B-ACD that were forwarded to voice mail. |
| Calls
                                          					 handoff to IOS | Total
                                          					 number of calls handed off to IOS. |
| Calls
                                          					 on hold | Total
                                          					 number of calls that were placed on hold. |
| Longest
                                          					 hold time (secs) | Longest
                                          					 length of time that a call to this agent spent between being placed on hold and
                                          					 being picked up. |
| Longest
                                          					 time in call (secs) | Longest
                                          					 length of time in which calls to Cisco Unified CME B-ACD went to an agent and
                                          					 waited in a call queue. |
| Longest
                                          					 time in hold (secs) | Longest
                                          					 length of time that a call spent between being placed on hold and being picked
                                          					 up by agents. |
| Longest
                                          					 time to answer (secs) | Longest
                                          					 length of time before calls to Cisco Unified CME B-ACD were answered. |
| Longest
                                          					 time to handoff (secs) | Longest
                                          					 length of time before a call was handed off to IOS. |
| Max
                                          					 agent | Maximum
                                          					 number of hunt group agents. |
| Min
                                          					 agent | Minimum
                                          					 number of hunt group agents. |
| Number
                                          					 of abandoned calls: | Total
                                          					 number of calls to Cisco Unified CME B-ACD that hung up before being answered. |
| Number
                                          					 of error calls | Total
                                          					 number of misdialed calls. |
| Total
                                          					 calls answered | Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by an agent. |
| Total
                                          					 calls on hold | Total
                                          					 number of calls that were on hold for this agent. |
| Total
                                          					 calls presented to the queue | Total
                                          					 number of calls made to Cisco Unified CME B-ACD. |
| Total calls | Total number of direct calls made to the hunt group. |

| Note | From Cisco Unified CME Release 10.5 onwards, abandoned calls will
                                          			 not include the calls going to the final number. However, the total calls
                                          			 includes calls going to the final number. Use the formula " Final Calls= Total Calls - Answered Calls - Abandoned Calls " ,
                                          			 to calculate the calls going to the final number. |
|---|---|

| Command | Description |
|---|---|
| ephone-hunt | Enters ephone-hunt configuration mode to create a hunt group for use in a Cisco
                                          						Unified CME system. |
| hunt-group report every hours | Sets
                                          						the hourly interval at which Cisco Unified CME B-ACD call statistics are
                                          						automatically transferred to a file. |
| hunt-group report url | Sets
                                          						filename parameters and the URL path where Cisco Unified CME B-ACD call
                                          						statistics are to be sent using TFTP. |
| statistics collect | Enables the collection of call statistics for an ephone hunt group. |

| summary | (Optional) Displays only the XML API configuration and the statistics for
                                          						queries and logs, and not the logs themselves. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.2(15)ZJ | 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| Current
                                          					 Period | The time
                                          					 between the last retain-timer-triggered cleanup to the next cleanup. |
| extension
                                          					 events | Events
                                          					 related to extensions that have been captured in the internal buffer. |
| device
                                          					 events | Events
                                          					 related to devices that have been captured in the internal buffer. |
| overwrites | Events
                                          					 that are written over previously recorded events in the buffer. Overwrites
                                          					 occur when the internal buffer size is too small; new events overwrite old
                                          					 ones. The internal buffer size is set using the max-size keyword in the log table command. |
| missed | Events
                                          					 that happen too quickly for the system to record. |
| deleted | Events
                                          					 removed from the internal buffer. |
| History | Information since the last system restart. |
| Threads | Current
                                          					 number of threads configured in the system. |
| max xml
                                          					 threads | Maximum
                                          					 number of concurrent XML threads allowed. |
| current
                                          					 thread | XML API
                                          					 query thread. |
| read in
                                          					 process | TRUE
                                          					 indicates that the xml-test.html file is being read now. FALSE indicates that
                                          					 the file is not being read. |
| UTC | Coordinated Universal Time, which is used by the system clock on the Cisco CME
                                          					 router. |

| Command | Description |
|---|---|
| log table | Sets
                                          						the maximum size of the table used to capture phone events used for the Cisco
                                          						CME XML API. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| ip address trusted list | Allows to add a list of trusted IP addresses. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This
                                          						command was introduced. |
| 12.4(15)T | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |

| Field | Description |
|---|---|
| Presence
                                          					 feature enable | Indicates
                                          					 whether presence is enabled on the router with the presence command. |
| Presence
                                          					 allow external watchers | Indicates
                                          					 whether internal presentities can be watched by external watchers, as set by
                                          					 the watcher all |
| Presence
                                          					 max subscription allowed | Maximum
                                          					 number of presence subscriptions allowed by the max-subscription command. |
| Presence
                                          					 number of subscriptions | Current
                                          					 number of active presence subscriptions. |
| Presence
                                          					 allow external subscribe | Indicates
                                          					 whether internal watchers are allowed to subscribe to status notifications from
                                          					 external presentities, as set by the allow subscribe command. |
| Presence
                                          					 call list enable | Indicates
                                          					 whether the Busy Lamp Field (BLF) call-list feature is enabled with the presence call-list command. |
| Presence
                                          					 server IP address | Displays
                                          					 the IP address of an external presence server defined with the server command. |
| Presence
                                          					 sccp blfsd retry interval | Retry
                                          					 timeout, in seconds, for BLF speed-dial numbers on SCCP phones set by the sccp blf-speed-dial retry interval command. |
| Presence sccp blfsd retry limit | Maximum
                                          					 number of retries allowed for BLF speed-dial numbers on SCCP phones set by the sccp blf-speed-dial retry interval command. |
| Presence router mode | Indicates whether the configuration mode is set to Cisco Unified CME or Cisco
                                          					 Unified SRST by the mode command. |

| Command | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be
                                          						watched in a presence service. |
| allow subscribe | Allows internal watchers to monitor external presence entities (directory
                                          						numbers). |
| debug presence | Displays debugging information about the presence service. |
| presence enable | Allows the router to accept incoming presence requests. |
| server | Specifies the IP address of a presence server for sending presence requests
                                          						from internal watchers to external presence entities. |
| show presence subscription | Displays information about active presence subscriptions. |
| watcher all | Allows external watchers to monitor internal presence entities (directory
                                          						numbers). |

| details | (Optional) Displays detailed information about presentities, watchers, and
                                          						presence subscriptions. |
|---|---|
| presentity telephone-number | (Optional) Displays information on the presentity specified by the destination
                                          						telephone number. |
| subid subscription-id | (Optional) Displays information for the specific subscription ID. |
| summary | (Optional) Displays summary information about active subscription requests. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This
                                          						command was introduced. |
| 12.4(15)T | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(24)T | This
                                          						command was integrated into Cisco IOS Release 12.4(24)T. |

| Field | Description |
|---|---|
| Watcher | IP
                                          					 address of the watcher. |
| Presentity | IP
                                          					 address of the presentity. |
| Expires | Number
                                          					 of seconds until the subscription expires. Default is 3600. |
| line
                                          					 status | Status
                                          					 of the line: Idle—Line is not being used. In-use—User is on the line, whether or not this line can accept a new call. Unknown—Phone is unregistered or this line is not allowed to be watched. |
| watcher
                                          					 type | Whether
                                          					 the watcher is local or remote. |
| presentity type | Whether
                                          					 the presentity is local or remote. |
| Watcher
                                          					 phone type | Type of
                                          					 phone, either SCCP or SIP. |
| subscription type | The
                                          					 type of presence subscription, either incoming or outgoing. |
| retry
                                          					 limit | Maximum
                                          					 number of times the router attempts to subscribe for the line status of an
                                          					 external SCCP phone when either the presentity does not exist or the router
                                          					 receives a terminated NOTIFY from the external presence server. Set with the sccp blf-speed-dial retry-interval command. |
| sibling
                                          					 subID | Sibling
                                          					 subscription ID if presentity is remote. If value is 0, presentity is local. |
| sdb | Voice
                                          					 port of the presentity. |
| dp | Dial
                                          					 peer of the presentity. |
| watcher
                                          					 dial peer tag | Dial
                                          					 peer tag of the watcher device. |

| Command | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be
                                          						watched in a presence service. |
| blf-speed-dial | Enables BLF monitoring for a speed-dial number on a phone registered to Cisco
                                          						Unified CME. |
| debug ephone blf | Displays debugging information for BLF presence features. |
| debug presence | Displays debugging information about the presence service. |
| presence | Enables presence service and enters presence configuration mode. |
| presence enable | Allows the router to accept incoming presence requests. |
| show presence global | Displays configuration information about the presence service. |

| units | Displays the configured and registered DSP farms. |
|---|---|
| sessions | Displays the transcoding streams. |
| active | Displays all active sessions. |
| callID | Displays activities for a specific caller ID. |
| number | Displays caller ID number displayed by the show voip rtp connection command. |
| statistics | Displays session statistics. |
| summary | Displays summary information. |

| Cisco
                                          						IOS Release | Cisco
                                          						Products | Modification |
|---|---|---|
| 12.3(11)T | Cisco
                                          						CME 3.2 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| act-streams | Active
                                          					 streams that are currently involved in calls. |
| alloc-streams | Number
                                          					 of transcoding streams that are actually allocated to all DSP farms that are
                                          					 registered to Cisco CME. |
| callID | Caller
                                          					 ID that the active stream is in. |
| Codec | Codec
                                          					 in use. |
| confID | ConfID
                                          					 that is used to communicate with DSP farms. |
| discard | Number
                                          					 of packets that are discarded. |
| dstCall-ID | Caller
                                          					 ID of the destination IP call leg. |
| Duration or dur | Packet
                                          					 rates, in milliseconds. |
| ID | Transcoding stream sequence number in Cisco CME. |
| in-pak | Number
                                          					 of incoming packets from the source call leg. |
| Local | Local
                                          					 port for voice packets. |
| max-mtps | Maximum
                                          					 number of Message Transfer Parts (MTPs) that are currently allowed to register
                                          					 in Cisco CME. |
| max-streams | Maximum
                                          					 number of transcoding streams that are currently allowed in Cisco CME. |
| mtp or
                                          					 MTP | MTP
                                          					 sequence number where the transcoding stream is located. |
| out-pak | Number
                                          					 of outgoing packets sending to source call leg. |
| peer
                                          					 Stream-ID | Stream
                                          					 sequence number of the other stream paired in the same transcoding session.
                                          					 (Two transcoding streams make up a transcoding session). |
| recv-pak | Number
                                          					 of voice packets received from DSP farm. |
| srcCall-ID | Source
                                          					 caller ID of the source IP call leg. |
| State | Current
                                          					 state of the transcoding stream, could be IDLE, SEIZE, START, STOP, or END. |
| Stream-ID | Transcoding stream sequence number in Cisco CME. |
| TCP-socket | Socket
                                          					 number for DSP farm (similar to TCP socket for show ephone output). |
| usage | Current
                                          					 usage of the stream; for example, Ip-Ip (IP to IP transcoding), MOH (for MOH
                                          					 transcoding) and Conf (conference). |
| vad | Voice-activity detection (VAD) flag for the transcoding stream. It should
                                          					 always be 0 (False). |
| xmit-pak | Number
                                          					 of packets that are sent to DSP farm. |

| Command | Description |
|---|---|
| sdspfarm tag | Permits a DSP farm to be to registered to Cisco CME and be associated with an
                                          						SCCP client interface’s MAC address. |
| sdspfarm transcode sessions | Specifies the maximum number of transcoding sessions allowed per Cisco CME
                                          						router. |
| sdspfarm units | Specifies the maximum number of DSP farms that are allowed to be registered to
                                          						Cisco CME. |

| call | Displays information about all active calls on shared lines. |
|---|---|
| details | Displays detailed information about each shared line. |
| subscription | Displays information for specific subscriptions to shared lines. |
| summary | Displays summary information about active subscriptions to shared lines. |

| Release | Modification |
|---|---|
| 12.4(24)T | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| Expires | Number
                                          					 of seconds until the subscription expires. |
| Local
                                          					 Address | IP
                                          					 address of the local phone involved in the shared line call. |
| Local
                                          					 User | Extension number of the shared line. |
| Remote
                                          					 Address | IP
                                          					 address of the remote phone involved in the shared line call. |
| Remote
                                          					 User | Extension of the remote phone involved in the shared line call. |
| SubID | Subscription ID. |
| Subscriber | Extension number of the shared line and the IP address of the phone subscriber. |
| Sub-Status | Status
                                          					 of the subscription. |
| Users | IP
                                          					 addresses of the phones using the shared line. |

| Command | Description |
|---|---|
| debug shared-line | Displays debugging information about SIP shared lines. |

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.2(2)XT | 2.0 | This
                                          						command was introduced. |
| 12.2(8)T | 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

| Field | Description |
|---|---|
| admin_username | Username
                                          					 of system administrator. |
| admin_password | Password
                                          					 of system administrator. |
| edit DN
                                          					 through Web | Whether
                                          					 editing of extensions through the GUI has been enabled using the dn-webedit command. |
| edit TIME
                                          					 through Web | Whether
                                          					 changing the router time through the GUI has been enabled using the time-webedit command. |

| Command | Description |
|---|---|
| dn-webedit | Enables
                                          						adding of extensions (ephone-dns) through the web interface. |
| time-webedit | Enables
                                          						setting of time through the web interface. |

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						Unified CME 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						Unified CME 2.0 | This
                                          						command was integrated int Cisco IOS Release 12.2(8)T. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to display the total number of data collected from both
                                          						ephone and voice hunt groups. |

| Field | Description |
|---|---|
| button | Button on
                                          					 the Cisco IP phone. |
| call-forward noan | Call
                                          					 forward no answer is set. |
| cnf-file
                                          					 location | Storage
                                          					 location for phone configuration files. System (default), flash or slot 0
                                          					 memory, and external TFTP server. |
| cnf-file option | Specifies the use of different phone configuration files by type of phone or by
                                          					 individual phone. |
| cos | Not
                                          					 applicable; unused. |
| destination-pattern | Destination pattern (telephone number) configured for this dial peer. |
| dial-peer voice | Voice
                                          					 dial peer. |
| dialplan-pattern | Dial-plan pattern is set to expand the abbreviated extension numbers to fully
                                          					 qualified E.164 numbers. |
| ephone | Cisco
                                          					 IP phone. |
| ephone-dn | Cisco
                                          					 IP phone directory number. |
| huntstop | Huntstop is set. |
| ip
                                          					 source-address | IP
                                          					 address used by Cisco IP phones to register with the router for service. |
| keepalive | IP
                                          					 phone keepalive period, in seconds. |
| mac-address | MAC
                                          					 address. |
| max-dn | Maximum
                                          					 directory numbers. |
| max-ephones | Maximum
                                          					 numbers of Cisco IP phones. |
| number | Cisco
                                          					 IP phone number. |
| port | TCP
                                          					 port number used by Cisco IP phones to communicate with the router. |
| pots | POTS
                                          					 dial peer set. |
| speed-dial | Speed-dial is set. |
| station-id number | Number
                                          					 used for caller ID purposes when calls are made using the line. |
| timeout | Timeout
                                          					 is set. |
| timeout
                                          					 ringing | Maximum
                                          					 amount of time that the phone is allowed to ring before the call is
                                          					 disconnected. |
| transfer-pattern | Transfer pattern is set to allow transfer of calls to a specified number. |
| type | Not
                                          					 applicable; unused. |
| voicemail | A
                                          					 voice-mail (speed-dial) number is set. |
| voice-port | (Virtual) voice port designator. |
| # of
                                          					 hunt-group collect data | Total
                                          					 number of data collected from both ephone and voice hunt groups. |

| Command | Description |
|---|---|
| show telephony dial - peer | Displays dial peers for extensions in a Cisco Unified CME system. |
| show telephony voice - port | Displays virtual voice-port configuration for extensions in a Cisco Unified CME
                                          						system. |

| global | Global
                                          						lists that can be accessed by all users. |
|---|---|
| local | Personal lists that can be accessed by users configured to use the lists. |
| list-id | Digit
                                          						that identifies the list. Range is from 0 to 9. |
| index-id | Identification number for an entry. |
| phone-tag | Ephone
                                          						identifier (phone-tag). |
| summary | List of
                                          						registered bulk speed-dial text files. |

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

| Field | Description |
|---|---|
| List-id | Digit
                                          					 that identifies the list. Range is from 0 to 9. |
| Entries | Number
                                          					 of entries in the speed-dial file. |
| Size | Size of
                                          					 the file, in KB. |
| Reference | Assignment of the list: global if assigned to all ephones, or a specific ephone
                                          					 number. |
| url | Location of the text file, in URL format. |
| Index | Identification number for an entry. |
| Number | Number
                                          					 to be dialed and displayed on the phone. |
| Name | Name to
                                          					 be displayed on the phone. |
| Hide | Yes
                                          					 indicates that this number should not be displayed when it is dialed. |
| Append | Yes
                                          					 indicates that additional digits can be dialed by the user after this number
                                          					 has been speed-dialed before the call is completed. |

| Command | Description |
|---|---|
| bulk-speed-dial list (ephone) | Enables a personal bulk speed-dial list for an ephone. |
| bulk-speed-dial list (telephony-service) | Enables a global bulk speed-dial list for all users of a Cisco Unified CME
                                          						system. |
| bulk-speed-dial prefix | Sets
                                          						the prefix code that phone users dial to access speed-dial numbers from a bulk
                                          						speed-dial list. |

| ad-hoc | (Optional) Ad-hoc hardware conferences. |
|---|---|
| detail | (Optional) Detailed information for all conferences. |
| video | (Optional) Video conferences. |
| meetme | (Optional) Meet-me hardware conferences. |
| number | (Optional) Conference number. |
| telephone-number | (Optional) Telephone or extension number. |

| Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 15.1(4)M | Cisco
                                          						Unified CME 8.6 | This
                                          						command was modified to include the video option. |
| 15.2(2)T | Cisco
                                          						Unified CME9.0 | This
                                          						command was modified to add hardware conference information on Cisco Unified
                                          						SIP IP phones to the output display. |

| Field | Description |
|---|---|
| Active | Number
                                          					 of active parties in the conference. |
| admin | Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can: Dial in to any conference directly through the conference number. Use the ConfList soft key to list conference parties. Remove any party from any conference. |
| Conference | Conference directory number (DN). |
| Conference parties | DNs in
                                          					 the conference. |
| Last | Last
                                          					 participant to join the conference. |
| Host | Conference creator. |
| HostPhone cur(initial) | cur—Current host phone. The phone that currently hosts the conference creator. (initial)—Initial host phone. The phone that hosted the conference creator when the conference was created. Because you can transfer the conference creator, the current host phone may be different from the initial host phone. |
| Max | Maximum
                                          					 number of participants allowed in the conference. |
| Peak | Maximum
                                          					 number of participants in the conference at any time. |
| Type | Type of
                                          					 conference: meet-me or ad hoc. |

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.2(15)ZJ | 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| directory directory-tag (shown as 1 in the example) | Sequence
                                          					 number or unique identifier for a directory entry. |
| name (shown as Smith, John) | Name that
                                          					 appears in the directory associated with the number. |
| number (shown as 4085550123 in the example) | Telephone
                                          					 number or extension for the directory entry. |

| Command | Description |
|---|---|
| directory entry | Adds an
                                          						entry to a local phone directory that can be displayed on IP phones. |
| show telephony-service all | Displays detailed configuration of a Cisco CME system. |
| show telephony-service ephone - dn | Displays information for extensions (ephone-dns) in a Cisco CME system. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						CME 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | The
                                          						conference add-mode, conference drop-mode, and conference admin fields were
                                          						added. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The output was enhanced to include the setting of the feature-button command and information about
                                          						logical partitioning class of restriction (LPCOR). |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Field | Description |
|---|---|
| button | Button
                                          					 number on IP phone, separator to denote ring characteristics and ephone-dn tag.
                                          					 A colon (:) separator denotes a normal ring. |
| conference add-mode | Who can
                                          					 add parties to a conference: creator—Only the creator can add parties. all—Any party can add other parties if the creator remains in the conference. |
| conference drop-mode | When
                                          					 conferences are dropped: creator—Conference terminates when the creator hangs up. local—Conference terminates when the last local party in the conference hangs
                                             						up or drops out of the conference. never—Conference is not dropped, even if the creator hangs up, as long as three
                                             						parties remain in the conference. |
| conference admin | Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can: Dial
                                             						in to any conference directly through the conference number Use
                                             						the ConfList soft key to list conference parties Remove any party from any conference |
| ephone | Cisco
                                          					 IP phone. |
| feature-button | Displays the type of feature button on the ephone. Feature type can be
                                          					 configured with privacy or DND. |
| lpcor
                                          					 (incoming) | Setting
                                          					 of the lpcor incoming command. |
| lpcor
                                          					 (outgoing) | Setting
                                          					 of the lpcor outgoing command. |
| lpcor
                                          					 type | Setting
                                          					 of the lpcor type command. |
| mac-address | MAC
                                          					 address of the Cisco IP phone. |
| speed-dial | Speed-tag (unique identifier) and the number that is programmed for that
                                          					 speed-tag. |
| type | Model
                                          					 type of phone. |

| Command | Description |
|---|---|
| show telephony-service all | Displays detailed configuration for a Cisco Unified CME system. |
| show telephony-service dial - peer | Displays dial-peer information for extensions in Cisco Unified CME. |
| show telephony-service ephone - dn | Displays information for extensions in Cisco Unified CME. |
| show telephony-service voice - port | Displays configurations for virtual voice ports in Cisco Unified CME. |

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.1(5)YD | 1.0 | This
                                          						command was introduced |
| 12.2(8)T | 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |

| Field | Description |
|---|---|
| call-forward noan | Call
                                          					 forwarding is set to no answer. Other available options are call-forward busy
                                          					 and call-forward all. |
| ephone-dn | Cisco IP
                                          					 phone directory number. |
| huntstop | Huntstop
                                          					 is set. |
| number | Cisco IP
                                          					 phone number. |
| timeout | Timeout
                                          					 setting for call forwarding when an extension does not answer. |

| Command | Description |
|---|---|
| show telephony-service all | Displays the detailed configuration of all the Cisco IP phones. |
| show telephony-service dial - peer | Displays dial peer information for extensions (ephone-dns) in a Cisco CME
                                          						system. |
| show telephony-service voice - port | Displays configurations for virtual voice ports in a Cisco CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-dn-template | Creates an ephone-dn template and enters ephone-dn-template
                                          						configuration mode. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco
                                          						CME 3.2 | This
                                          						command was introduced. |
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | The
                                          						conference add-mode, conference drop-mode, and conference admin fields were
                                          						added. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) | Emergency response location (ERL) information assigned to an ephone displays in
                                          						the output. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. Logical partitioning class of restriction (LPCOR)
                                          						information was added to the output. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Field | Description |
|---|---|
| ephone-template | Identifier for the ephone template. |
| softkey
                                          					 hold | Soft
                                          					 keys displayed during the hold call stage. |
| softkey
                                          					 idle | Soft
                                          					 keys displayed during the call-idle call stage. |
| softkey
                                          					 seized | Soft
                                          					 keys displayed during the call-seized call stage. |
| softkey
                                          					 alerting | Soft
                                          					 keys displayed during the call-alerting call stage. |
| softkey
                                          					 connected | Soft
                                          					 keys displayed during the call-connected call stage. |
| conference drop-mode | When
                                          					 conferences are dropped: creator: Conference terminates when the creator hangs up. local: Conference terminates when the last local party in the conference hangs
                                             						up or drops out of the conference. never: Conference is not dropped, even if the creator hangs up, if three
                                             						parties remain in the conference. |
| conference add-mode | Who can
                                          					 add parties to a conference: creator: Only the creator can add parties. all:
                                             						Any party can add other parties if the creator remains in the conference. |
| conference admin | Ad hoc
                                          					 and meet-me hardware conference administrator. The administrator can: Dial
                                             						in to any conference directly through the conference number. Use
                                             						the ConfList soft key to list conference parties. Remove any party from any conference. |
| Always
                                          					 send media packets to this router | Always
                                          					 send media packets to this Cisco Unified CME router, which acts as a proxy and
                                          					 forwards the packets to the destination, instead of sending them directly to
                                          					 the destination IP phone. |
| Preferred codec | Codec
                                          					 to use when initiating a call. |
| button-layout | Type of
                                          					 IP phone and number of fixed line or feature set. 1:
                                             						Button 24=Menu. Button 23=Headset. 2:
                                             						Button 24=Menu. Button 23=Headset. Button 22=Directories. Button 21=Messages. |
| User
                                          					 Locale | Locale
                                          					 that is associated with the phone user interface. The user locale identifies a
                                          					 set of detailed information, including language and font, to support users. |
| Network
                                          					 Locale | Locale
                                          					 that is associated with the phone. The network locale contains a definition of
                                          					 the tones and cadences that are used by the phones and gateways in the device
                                          					 pool in a specific geographic area. |
| Emergency response location | Identification of the ERL defined with the emergency response location command. |
| lpcor
                                          					 (incoming) | Setting
                                          					 of the lpcor incoming command. |
| lpcor
                                          					 (outgoing) | Setting
                                          					 of the lpcor outgoing command. |
| lpcor
                                          					 type | Setting
                                          					 of the lpcor type command. |

| Command | Description |
|---|---|
| ephone-template | Creates an ephone template. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| fac | Enables standard FACs or creates a custom FAC. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Cisco IOS Release | Cisco CME Version | Modification |
|---|---|---|
| 12.2(11)YT | 2.1 | This command was introduced. |
| 12.2(15)T | 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

| Command | Description |
|---|---|
| network - locale | Sets the definition of the tones and cadences on the Cisco
                                          						IP Phones 7940 and 7940G and the Cisco IP Phones 7960 and 7960G for a specific
                                          						geographic area. |
| user - locale | Sets language for displays on the Cisco IP Phones 7940 and
                                          						7940G and the Cisco IP Phones 7960 and 7960G. |

| Cisco
                                          						IOS Release | Cisco
                                          						CME Version | Modification |
|---|---|---|
| 12.1(5)YD | 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |

| Field | Description |
|---|---|
| station-id number | Phone
                                          					 number used for caller ID purposes for calls made from this voice port. |
| timeout
                                          					 ringing | Maximum
                                          					 amount of time that a phone is allowed to ring before the call is disconnected. |
| voice-port | Virtual
                                          					 voice port. |

| Command | Description |
|---|---|
| show telephony-service all | Displays the detailed configuration of all the Cisco IP phones. |
| show telephony-service dial - peer | Displays dial-peer information for extensions in a Cisco CME system. |
| show telephony-service ephone - dn | Displays information for extensions (ephone-dns) in a Cisco CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| show voice emergency all | Displays all emergency response location information. |
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| name | Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |
| voice emergency response location | Creates a tag for identifying an ERL for the E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added to Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| location | Identifies locations within an emergency response zone. |
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |
| voice emergency response zone | Creates an emergency response zone within which ERLs can be
                                          						grouped. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| show call active voice | Displays call information for voice calls that are in
                                          						progress. |
| show call history voice | Displays the call history table for voice calls. |

| hunt-group-tag | (Optional) Unique sequence number that identifies the voice hunt group. Range
                                          						is 1 to 100. |
|---|---|
| brief | (Optional) Displays brief information on all voice hunt groups in a Cisco CME
                                          						system. |
| longest-idle | (Optional) Displays summary of longest-idle voice hunt groups. |
| parallel | (Optional) Displays summary of parallel voice hunt groups. |
| peer | (Optional) Displays summary of peer voice hunt groups. |
| sequential | (Optional) Displays summary of sequential voice hunt groups. |

| Release | Modification |
|---|---|
| 12.4(24)T | This
                                          						command was introduced in a release earlier than Cisco IOS Release 12.4(24)T. |
| 15.2(2)T | This
                                          						command was modified to add stat collect as a field. |

| Field | Description |
|---|---|
| Group | Tag
                                          					 number of voice hunt group. |
| type | Type of
                                          					 voice hunt group. The available voice hunt group types are: longest-idle,
                                          					 parallel, peer and sequential. |
| pilot
                                          					 number | Number
                                          					 that callers dial to reach the specified voice hunt group. |
| secondary-number | Alternate number for the specified voice hunt group. |
| list of
                                          					 numbers | Numbers
                                          					 of the extensions configured in the voice hunt-group command‘s hunt-tag identifier. |
| preference | Preference order for the extension or telephone number associated with a dial
                                          					 peer. Range is 0 to 8. Default is 0. |
| preference (sec) | Preference order for the secondary pilot number. Range is from 0 to 10, where 0
                                          					 is the highest preference and 10 is the lowest preference. Default is 9. |
| timeout | Number
                                          					 of seconds after which a call that is not answered at one number is redirected
                                          					 to the next number in the hunt group list. |
| final_number | Last
                                          					 number in the voice hunt group, after which a call is no longer redirected. |
| hops | Number
                                          					 of hops before a call proceeds to the final number. |
| stat
                                          					 collect | Yes
                                          					 indicates that call statistics are being collected for a voice hunt group. |
| phone-display | Displays
                                          					 the hunt group information on My Phone Apps service button. |
| hlog-block | Blocks
                                          					 the hlog functionality of voice hunt group on the phone. |
| peer-tag | Peer
                                          					 hunting tag. |

| Command | Description |
|---|---|
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| hops (voice hunt-group) | Defines the number of times that a call is redirected to the next directory
                                          						number in a peer voice hunt group list before proceeding to the final directory
                                          						number. |
| list (voice hunt-group) | Defines the directory numbers that participate in a directory number hunt
                                          						group. |
| pilot (voice hunt-group) | Defines the voice dn that callers dial to reach a Cisco Unified Communications
                                          						Manager Express (Cisco Unified CME) voice hunt group. |
| timeout (voice hunt-group) | Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last directory number in
                                          						the hunt group. |
| voice hunt-group | Configures voice hunt groups and the associated parameters. |

| group-id | Identifier for the voice hunt group. Range: 1 to 100. |
|---|---|
| last | Displays the latest call statistics for a voice hunt group for a specified
                                          						number of hours, counting backward from the current hour. Range: 1 to 167. |
| hours hours | Number
                                          						of hours that the call statistics are displayed. |
| start | Defines
                                          						the start of the period for which the call statistics are displayed. Default
                                          						duration is one hour. |
| day | Abbreviated day of the week. The following abbreviations are valid: sun, mon,
                                          						tue, wed, thu, fri, sat. |
| time | Hour of
                                          						the day. Range: 0 to 23. |
| to | (Optional) Defines the time the display of the call statistics ends. |

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |

| Note | On the day
                                       		  that daylight saving time adjusts the time back by one hour at 2 a.m. each
                                       		  year, the original 1 a.m. to 2 a.m. statistics for that day are lost because
                                       		  they are overwritten by the new 1 a.m. to 2 a.m. statistics. |
|---|---|

| Field | Description |
|---|---|
| Abandoned calls | Total number of calls abandoned by hunt group agents. This
                                          					 does not include calls going to the final number. |
| Answered call | Total number of calls answered by hunt group agents. |
| Average time in call (secs) | Average length of time that unanswered calls waited before
                                          					 going to an agent. |
| Average time to answer (secs) | Average length of time that all calls to Cisco Unified CME
                                          					 B-ACD waited before being answered. |
| Average time in hold (secs) | Average length of time that calls were kept on hold for all
                                          					 agents. |
| Average hold time (secs) | Average length of time that calls waited on hold for this
                                          					 agent. |
| Average time to handoff (secs) | Average length of time before a call was handed off to IOS |
| Calls on hold | Total number of calls that were placed on hold. |
| Calls handoff to IOS | Total number of calls handed off to IOS. |
| Calls answered by voice mail | Total number of calls to Cisco Unified CME B-ACD that were
                                          					 answered by voice mail. |
| Calls forwarded to voice mail | Total number of calls to Cisco Unified CME B-ACD that were
                                          					 forwarded to voice mail. |
| Longest time to answer (secs) | Longest length of time before calls to Cisco Unified CME
                                          					 B-ACD were answered. |
| Longest time in call (secs) | Longest length of time that all calls to Cisco Unified CME
                                          					 B-ACD that went to an agent waited in a call queue. |
| Longest time in hold (secs) | Longest length of time that a call spent between being placed
                                          					 on hold and being picked up by agents. |
| Longest hold time (secs) | Longest length of time that a call to this agent was spent
                                          					 between being placed on hold and being picked up. |
| Longest time to handoff (secs) | Longest length of time before a call was handed off to IOS. |
| Max agent | Maximum number of hunt group agents. |
| Min
                                          					 agent | Minimum
                                          					 number of hunt group agents. |
| Number of abandoned calls | Total number of calls to Cisco Unified CME B-ACD that hung up
                                          					 before being answered. |
| Number of calls in the queue | Total number of calls in the queue. |
| Number of error calls | Total number of error calls. |
| Total calls | Total number of direct calls made to the hunt group. |
| Total
                                          					 calls answered | Total
                                          					 number of calls to Cisco Unified CME B-ACD that were answered by an agent. |
| Total
                                          					 calls on hold | Total
                                          					 number of calls that were placed on hold for this agent. |
| Total calls presented to the queue | Total number of calls made to Cisco Unified CME B-ACD. |

| Note | From Cisco Unified CME Release 10.5 onwards, abandoned calls will
                                          			 not include the calls going to the final number. However, the total calls
                                          			 includes calls going to the final number. Use the formula " Final Calls= Total Calls - Answered Calls - Abandoned Calls " ,
                                          			 to calculate the calls going to the final number. |
|---|---|

| Command | Description |
|---|---|
| voice hunt-group statistics collect | Enables the collection of call statistics for voice hunt groups. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 15.0(1)XA | Cisco
                                          						SIP SRST 8.0 | This
                                          						command was modified to display the signaling transport protocol. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1 | The
                                          						output display of this command was modified. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 | This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display. |

| Field | Description |
|---|---|
| Pool
                                          					 Tag | Shows
                                          					 the assigned tag number of the current voice register pool. |
| Config | Shows
                                          					 the voice register pool. |
| Network
                                          					 address and Mask | Shows
                                          					 network address and mask information when the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Shows
                                          					 the number command configuration. |
| Proxy
                                          					 IP address | Shows
                                          					 the proxy command configuration. |
| Default
                                          					 preference | Shows
                                          					 the default preference value of this pool. |
| Incoming called number | Shows
                                          					 the incoming called-number command configuration. |
| Translate outgoing called tag | Shows
                                          					 the translate-outgoing command configuration. |
| Class
                                          					 of Restriction List Tag | Shows
                                          					 the COR tag. |
| Incoming corlist name | Shows
                                          					 the cor command
                                          					 configuration. |
| Application | Shows
                                          					 the application command configuration for this pool. |
| Dialpeers created | Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here. |
| Statistics | Shows
                                          					 the registration statistics for this pool. |
| Active
                                          					 registrations | Shows
                                          					 the current active registrations. |
| Total
                                          					 Registration Statistics | Shows
                                          					 the total registration statistics for this pool. |
| Registration requests | Shows
                                          					 the incoming registration requests. |
| Registration success | Shows
                                          					 the successful registrations. |
| Registration failed | Shows
                                          					 the failed registrations. |
| unRegister requests | Shows
                                          					 the incoming unregister/registration expire requests. |
| unRegister success | Reports
                                          					 the number of successful unregisters. |
| unRegister failed | Reports
                                          					 the number of failed unregisters. |

| Command | Description |
|---|---|
| application (voice register pool) | Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment. |
| cor (voice register pool) | Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers. |
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer. |
| number (voice register pool) | Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone. |
| proxy (voice register pool) | Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway. |
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| translate-outgoing (voice register pool) | Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |

| Field | Description |
|---|---|
| username | Username
                                          					 that is authorized. |
| password | Password
                                          					 that is authorized. |
| service | Type of
                                          					 service for which the credential file is used; presence or Out-of-dialog REFER
                                          					 (OOD-R). |
| file
                                          					 index | Identification number of the credential file defined with the authenticate command. |

| Command | Description |
|---|---|
| authenticate (voice register global) | Defines
                                          						the authenticate mode for SIP phones in a Cisco Unified CME system. |
| credential load | Reloads
                                          						a credential file into Flash memory. |
| show voice register all | Displays all Cisco Unified CME and Cisco Unified SIP SRST configurations and
                                          						register information. |

| pool tag | Number of entries in attempted registrations table. Size
                                          						range from 0 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This command was modified. Pool tag keyword- argument was
                                          						added. Command output display was also modified to display dial-peers specific
                                          						to a pool. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with
                                          						the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| tag | Number
                                          						that identifies the SIP dialplan. Range: 1 to 24. |
|---|---|
| all | (Optional) Displays all the dialplans defined in a system. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was modified. All keyword was added. Pools and templates that have
                                          						dialplan configured are also displayed in the output. |

| Field | Description |
|---|---|
| Config | List of
                                          					 configuration options defined for this SIP dial plan. |
| Dialplan Tag | Tag
                                          					 number of the requested SIP dial plan. |
| Pattern | Dial
                                          					 pattern defined for a SIP dial plan with the pattern command in voice register dialplan configuration mode. |
| Type | Phone
                                          					 type defined for a SIP dial plan with the type command. |

| Command | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| pattern (voice register dialplan) | Defines a dial pattern for a SIP dial plan. |
| show voice register all | Displays all Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| type
                                          						(voice register dialplan) | Defines a phone type for a SIP dial plan. |
| voice register dialplan | Enters voice register dialplan configuration mode to define a dial plan for SIP
                                          						phones. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| tag | Tag
                                          						number of the voice register dn for which to display information. Range is 1 to
                                          						750. |
|---|---|
| all | (Optional) Displays configuration information associated with all voice
                                          						register dns defined in a system. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4 | This
                                          						command was introduced. |
| 15.1(2)T | Cisco
                                          						CME 8.1 and Cisco SIP SRST 8.1 | This
                                          						command was modified.The display output now shows pools that have DNs
                                          						configured under them. All keyword was added to show configuration information
                                          						for all voice register dns defined in system. |

| Field | Description |
|---|---|
| Auto
                                          					 answer | Status of
                                          					 auto-answer feature defined with the auto-answer command. |
| Config | List of
                                          					 configuration options defined for this voice register dn. |
| Dn Tag | Tag
                                          					 number of the requested voice register dn. |
| Huntstop | Status
                                          					 of huntstop behavior defined with the huntstop command. |
| Number | Telephone or extension number set with the number command in voice register dn configuration mode. |
| Preference | Preference order set with the preference command in voice register dn configuration mode. |

| Command | Description |
|---|---|
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show
                                          						voice register dn all | Displays information associated with all the dns configured in a system. |
| voice register dn | Enters voice register dn configuration mode to define an extension for a SIP
                                          						phone line. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was introduced. |
| 15.0(1)XA | Cisco
                                          						SIP SRST 8.0 | This
                                          						command was modified to display the signaling transport protocol. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This
                                          						command was modified to include global statistics in the output display. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to include conference hardware in the output display. |

| Field | Description |
|---|---|
| Conference hardware | Shows
                                          					 whether the Cisco Unified SIP IP phone will perform local mixing on its own or
                                          					 request Cisco Unified CME to perform hardware conferencing using its DSP
                                          					 resource. |
| Date-format | Value
                                          					 of date-format command. |
| DST
                                          					 auto adjust | Setting
                                          					 of dst auto-adjust command. |
| Forwarding local | Setting
                                          					 of forwarding local command. |
| Generate text file | Setting
                                          					 of text file command. |
| Hold-alert | Setting
                                          					 of hold-alert command. |
| Load | Value
                                          					 of load command. |
| Max-dn | Reports
                                          					 the maximum number of SIP voice register directory numbers (DNs) supported by
                                          					 the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with
                                          					 the max-dn command. The maximum possible number is
                                          					 platform-dependent. |
| Max-pool | Reports
                                          					 the maximum number of SIP voice register pools supported by the Cisco Unified
                                          					 SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent. |
| Max
                                          					 redirect number | Maximum
                                          					 number of redirects set with the max-redirect command. |
| Mode | Reports
                                          					 the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST. |
| MWI
                                          					 registration | Setting
                                          					 of mwi command. |
| MWI
                                          					 stutter | Setting
                                          					 of mwi stutter command. |
| Time-format | Value
                                          					 of time-format command. |
| Time-zone | Number
                                          					 of the timezone selected with the timezone command. |
| TFTP
                                          					 path | Directory location of provisioning files for Cisco Unified SIP IP phones that
                                          					 is specified with the tftp-path command. |
| Version | Reports
                                          					 the Cisco Unified SIP SRST or Cisco Unified CME version number. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the Cisco Unified SIP IP phones currently registered with the
                                          						contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event. |
| voice register global | Enters voice register global configuration mode to set global parameters for
                                          						all supported Cisco Unified SIP IP phones in a Cisco Unified CME or Cisco
                                          						Unified SIP SRST environment. |

| Release | Modification |
|---|---|
| 15.2(1)T | This command was introduced. |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profile files required for SIP
                                          						phones. |
| hfs enable | Enables the HFS download service on an IP Phone in a Cisco
                                          						Unified CME system. |

| pool-tag | Tag
                                          						number of the voice register pool for which information is displayed. Range is
                                          						1 to 262. Note The
                                                   						maximum number of pools is version and platform dependent. | Note | The
                                                   						maximum number of pools is version and platform dependent. |
|---|---|---|---|
| Note | The
                                                   						maximum number of pools is version and platform dependent. |
| all | Displays the information of all the voice register pools. |
| brief | (Optional) Displays brief information of all voice register pools. |

| Note | The
                                                   						maximum number of pools is version and platform dependent. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) Cisco Unified SIP SRST 4.2(1) | This
                                          						command was modified to include emergency response location information in the
                                          						output display. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 Cisco Unified SIP SRST 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the
                                          						output. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display. |
| Cisco
                                          						IOS XE Everest 16.6.1 | Unified SRST 12.0 | This
                                          						command was modified to include the IPv6 address in the output display for
                                          						Unified SRST. |

| Field | Description |
|---|---|
| Active
                                          					 registrations | Shows
                                          					 the current active registrations. |
| Application | Shows
                                          					 the application command configuration for this pool. |
| Call
                                          					 Waiting | Shows
                                          					 the call-waiting command configuration. |
| Class
                                          					 of Restriction List Tag | Shows
                                          					 the COR tag. |
| Conference add mode | Shows
                                          					 the current setting of the hardware conference privilege for adding
                                          					 participants. |
| Conference admin | Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not. |
| Conference drop mode | Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up. |
| Config | Shows
                                          					 the voice register pool. |
| Default
                                          					 preference | Shows
                                          					 the default preference value of this pool. |
| Dialpeers created | Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here. |
| DnD | Shows
                                          					 the setting of the dnd-control command. |
| DTMF
                                          					 Relay | Shows
                                          					 the setting of the dtmf-relay command. |
| Emergency response location | Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made. |
| Incoming called number | Shows
                                          					 the incoming called-number command configuration. |
| Incoming corlist name | Shows
                                          					 the cor command
                                          					 configuration. |
| keep-conference | Shows
                                          					 the status of the keep-conference command. |
| Lpcor
                                          					 Incoming | Shows
                                          					 the setting of the lpcor incoming command. |
| Lpcor
                                          					 Outgoing | Shows
                                          					 the setting of the lpcor outgoing command. |
| Lpcor
                                          					 Type | Shows
                                          					 the setting of the lpcor type command. |
| Mac
                                          					 address | Shows
                                          					 the MAC address of the Cisco Unified SIP IP phone as defined by the id command. |
| Network
                                          					 address and Mask | Shows
                                          					 network address and mask information when the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Shows
                                          					 the number command configuration. |
| Pool
                                          					 Tag | Shows
                                          					 the assigned tag number of the current pool. |
| Proxy
                                          					 IP address | Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server. |
| Registration failed | Shows
                                          					 the failed registrations. |
| Registration requests | Shows
                                          					 the incoming registration requests. |
| Registration success | Shows
                                          					 the successful registrations. |
| Statistics | Shows
                                          					 the registration statistics for this pool. |
| Template | Shows
                                          					 the template-tag number for the template applied to the Cisco Unified SIP IP
                                          					 phone. |
| Total
                                          					 Registration Statistics | Shows
                                          					 the total registration statistics for this pool. |
| Translate outgoing called tag | Shows
                                          					 the translate-outgoing command configuration. |
| Type | Shows
                                          					 the phone type identified for the Cisco Unified SIP IP phone using the type command. |
| unRegister failed | Reports
                                          					 the number of failed unregisters. |
| unRegister requests | Shows
                                          					 the incoming unregister/registration expiry requests. |
| unRegister success | Reports
                                          					 the number of successful unregisters. |
| Username Password | Shows
                                          					 the values within the authentication credential. |

| Command | Description |
|---|---|
| application (voice register pool) | Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment. |
| call-waiting (voice register pool) | Enables the call-waiting option on a SIP phone. |
| cor (voice register pool) | Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers. |
| dnd-control (voice register template) | Enables the Do-Not-Disturb (DND) soft key on SIP phones. |
| dtmf-relay (voice register pool) | Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints. |
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer. |
| keep-conference (voice register pool) | Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected. |
| lpcor incoming | Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy. |
| lpcor outgoing | Associates an outgoing call with an LPCOR resource-group policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| number (voice register pool) | Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone. |
| proxy (voice register pool) | Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway. |
| show sip-ua status registrar | Displays all the Cisco Unified SIP IP phones registered with the contact
                                          						address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peer | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified CME or Cisco Unified SIP SRST register event. |
| translate-outgoing (voice register pool) | Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user. |
| type (voice register pool) | Defines a phone type for a SIP phone. |
| voice register pool | Enters voice register pool configuration mode for Cisco Unified SIP IP phones. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Directory
                                          					 number of the phone. |
| IP
                                          					 Address/port | IP
                                          					 address and port number of the phones. |
| LN | Line
                                          					 number of the phone. |
| Number | Number of
                                          					 the phones that have after-hour exempt enabled. |
| Pool | Shows the
                                          					 current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| after-hour exempt(voice register pool) | Specifies that an IP phone does not have any of its outgoing calls blocked
                                          						although call blocking is defined. |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register
                                          						information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| attempted-registrations size | Allows to set the size of the table that stores information
                                          						related to SIP phones that attempt to register and fail. |
| clear voice register attempted-registrations | Clears entries from the attempted-registration table. |

| Cisco
                                    				  IOS Release | Cisco
                                    				  Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                       					 Unified CME 8.1 | This
                                       					 command was introduced. |

| Field | Description |
|---|---|
| Call
                                       					 Forward All Number | Number to
                                       					 which the calls are forwarded. |
| DN | Voice
                                       					 register DN tag of the line. |
| LN | Line
                                       					 number of the telephone number. |
| Pool | Tag ID of
                                       					 the pool. |

| Command | Description |
|---|---|
| call forward b2bua all | Enables
                                          						call forward all. |
| show voice register all | Displays
                                          						all Cisco Unified SIP SRST and Cisco Unified CME configurations and register
                                          						information. |
| show voice register pool | Displays
                                          						all configuration information associated with a particular voice register pool. |
| show voice register pool detail all | Displays
                                          						the details of all the pools defined in the system. |

| brief | (Optional) Displays brief details of SIP phones that are in
                                          						connected state. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| ip-address | IPv4
                                          						address of the SIP phone . |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Voice
                                          					 register DN tag of the line. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address of the SIP phone. |
| LN | Line
                                          					 number of the telephone number. |
| Number | Number of
                                          					 the phones that have a mac address. |
| Pool | Tag ID of
                                          					 the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| H.H.H | MAC
                                          						address of the SIP phone attempting to register. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Voice
                                          					 register DN tag of the line. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address of the SIP phone. |
| LN | Line
                                          					 number of the telephone number. |
| Number | Number of
                                          					 the phones that have a mac address. |
| Pool | Tag ID of
                                          					 the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| brief | (Optional) Displays brief details of SIP phones that are
                                          						currently on-hold. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| load(voice register global) | Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file. |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This
                                          						command was modified to display Key Expansion Module (KEM) details with the
                                          						phone type information. |

| Field | Description |
|---|---|
| Active
                                          					 registrations | Shows the
                                          					 current active registrations. |
| Application | Shows the application command configuration for this pool. |
| Call
                                          					 Waiting | Shows the
                                          					 setting of the call-waiting command. |
| Class
                                          					 of Restriction List Tag | Shows
                                          					 the COR tag. |
| Config | Shows
                                          					 the voice register pool. |
| Current
                                          					 phone-load | Shows
                                          					 the current version of the phone load. |
| Default
                                          					 preference | Shows
                                          					 the default preference value of this pool. |
| Dialpeers created | Results
                                          					 in a list of all dial peers created and their contents. Dial-peer contents
                                          					 differ for each application and are not described here. |
| DnD | Shows
                                          					 the setting of the dnd-control command. |
| DTMF
                                          					 Relay | Shows
                                          					 the setting of the dtmf-relay command. |
| Emergency response location | Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made. |
| Incoming called number | Shows
                                          					 the incoming called-number command configuration. |
| Incoming corlist name | Shows
                                          					 the cor command
                                          					 configuration. |
| keep-conference | Shows
                                          					 the status of the keep-conference command. |
| Lpcor
                                          					 Incoming | Shows
                                          					 the setting of the lpcor incoming command. |
| Lpcor
                                          					 Outgoing | Shows
                                          					 the setting of the lpcor outgoing command. |
| Lpcor
                                          					 Type | Shows
                                          					 the setting of the lpcor type command. |
| Mac
                                          					 address | Shows
                                          					 the MAC address of this SIP phone as defined by the id command. |
| Network
                                          					 address and Mask | Shows
                                          					 network address and mask information when the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Shows
                                          					 the number command configuration. |
| Pool
                                          					 Tag | Shows
                                          					 the assigned tag number of the current pool. |
| Previous phone-load | Shows
                                          					 the version of the previous phone load. |
| Proxy
                                          					 IP address | Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server. |
| Registration failed | Shows
                                          					 the failed registrations. |
| Registration requests | Shows
                                          					 the incoming registration requests. |
| Registration success | Shows
                                          					 the successful registrations. |
| Statistics | Shows
                                          					 the registration statistics for this pool. |
| statistics time-stamps | Shows
                                          					 the registration statistics for this pool with specific time stamps. |
| Template | Shows
                                          					 the template-tag number for the template applied to this SIP phone. |
| Total
                                          					 Registration Statistics | Shows
                                          					 the total registration statistics for this pool. |
| Translate outgoing called tag | Shows
                                          					 the translate-outgoing command configuration. |
| Type | Shows
                                          					 the phone type identified for this SIP phone using the type command. |
| unRegister failed | Reports
                                          					 the number of failed unregisters. |
| unRegister requests | Shows
                                          					 the incoming unregister/registration expiry requests. |
| unRegister success | Reports
                                          					 the number of successful unregisters. |
| Username Password | Shows
                                          					 the values within the authentication credential. |

| Command | Description |
|---|---|
| application (voice register pool) | Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment. |
| call-waiting (voice register pool) | Enables the call-waiting option on a SIP phone. |
| cor (voice register pool) | Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers. |
| dnd-control (voice register template) | Enables the Do-Not-Disturb (DND) soft key on SIP phones. |
| dtmf-relay (voice register pool) | Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints. |
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer. |
| keep-conference (voice register pool) | Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected. |
| lpcor incoming | Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy. |
| lpcor outgoing | Associates an outgoing call with an LPCOR resource-group policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| number (voice register pool) | Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone. |
| proxy (voice register pool) | Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show voice register pool unregistered | Displays the details of voice register pools that do not have any phones
                                          						registered. |
| translate-outgoing (voice register pool) | Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user. |
| type (voice register pool) | Defines a phone type for a SIP phone. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| Cisco
                                    				  IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                       					 Unified CME 8.1 Cisco
                                       					 Unified SRST 8.1 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| show voice register all voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register
                                          						information. |
| show voice register dial-peer | Displays
                                          						details of all dynamically created VoIP dial peers associated with the Cisco
                                          						SIP SRST or Cisco CME register event. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| voice register pool | Enters
                                          						voice register pool configuration mode for SIP phones. |

| brief | (Optional) Displays brief details of SIP phones that are
                                          						currently in ringing state. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| number | Number
                                          						identifying a specific phone. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Directory
                                          					 number of the phone. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address and port number of the phones |
| LN | Line
                                          					 number of the phone. |
| Number | Number of
                                          					 the phones. |
| Pool | Shows the
                                          					 current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show
                                          						voice register pool detail all | Displays the details of all the pools defined in the system. |

| type | 3911, 3951, 7905, 7906, 7911, 7912, 7940, 7941, 7941GE, 7942, 7945, 7960, 7961, 7961GE, 7962, 7965, 7970, 7971, 7975, 7800
                                          Series, 8800 Series, ATA (Cisco SIP Phone ATA), ATA-191, CKEM (Cisco SIP Key Expansion Module), CP-8800-Audio (Cisco SIP Key
                                          Expansion Module), CP-8800-Video (Cisco SIP Key Expansion Module), P100 (PingTel Xpressa 100), P600 (Polycom SoundPoint 600). |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was introduced. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 | This
                                          						command was modified to add CKEM as a value for the type argument
                                          						to display the details of voice register pools associated with all the phones
                                          						configured with KEMs. |
| 15.3(3)M | Cisco Unified CME 10.0 | This command was enhanced to display the properties for new
                                          						sip phone models configured using SIP fast track feature. New keyword option all was added to display all the
                                          						phone models being used in the system along with the associated pools and
                                          						registration details. |
| Cisco IOS XE Gibraltar 16.10.1a | Unified CME 12.5 | This command was modified to add CP-8800-Audio and CP-8800-Video as values for the type argument to display the details of voice register pools associated with A-KEMs and V-KEMs. |
| Cisco IOS XE Gibraltar 16.10.1a | Unified CME 12.5 | This command was modified to add ATA-191 as the value for the type argument to display the details of voice register pools associated with Cisco ATA 191. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)
                                    				  M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |
| show voice register pool registered | Displays details of phones that sucessfully register to
                                          						Cisco Unified CME or Cisco Unified SRST. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| tag | Unique
                                          						identifier for voice register profile to be displayed. Range is 1–500. |
|---|---|

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| Attended
                                          					 Transfer | Setting
                                          					 of soft key for attended transfer in a SIP phone template as defined by using
                                          					 the transfer-attended command. “1” indicates that the
                                          					 soft key is enabled; “0” indicates that the soft key is disabled. |
| Auto
                                          					 Lookup | 1
                                          					 indicates that Auto Lookup is enabled. 0 indicates that it is disabled. |
| Blind
                                          					 Transfer | Setting
                                          					 of soft key for blind transfer in a SIP phone template as defined by using the transfer-blind command. “1” indicates that the
                                          					 soft key is enabled; “0” indicates that the soft key is disabled. |
| Call
                                          					 Waiting | Setting
                                          					 of the call-waiting option on a SIP phone as defined by using the call-waiting command. “1” indicates that the soft key is enabled; “0” indicates that the
                                          					 soft key is disabled. |
| Call
                                          					 Forward Number | Number to
                                          					 which incoming calls are forwarded |
| Conference | Setting
                                          					 of soft key for conference in a SIP phone template as defined by using the conference command. “1” indicates that the soft key is enabled; “0” indicates that the
                                          					 soft key is disabled. |
| Directories URL | 1
                                          					 indicates that the Directories feature button for the phone is enabled. 0
                                          					 indicates that it is disabled. |
| NTPIP | IP
                                          					 address for the NTP source |
| Pool
                                          					 tag | Pool
                                          					 tag of the configuration file being requested. |
| SIP Reg
                                          					 On | 1
                                          					 indicates that the registration with external proxy server for the phone is
                                          					 enabled. 0 indicates that it is disabled. |
| UI
                                          					 Password | 1
                                          					 indicates that the UI password is enabled on the phone. 0 indicates that dit is
                                          					 disabled. |
| UID | Authenticatuion credential for SIP phone. |
| Use
                                          					 Login ID | 1
                                          					 indicates that “use login id” for phone is enabled. 0 indicates that it is
                                          					 disabled. |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profiles required for SIP phone. |
| file text (voice register global) | Generates ASCII text files for the Cisco IP Phone 7905 and 7905G, Cisco IP
                                          						Phone 7912 and 79012G, Cisco ATA-186, or Cisco ATA-188. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router. |
| voice register global | Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco CME or Cisco SIP SRST
                                          						environment. |

| Release | Modification |
|---|---|
| 12.4(22)T | This
                                          						command was introduced in a release earlier than Cisco IOS Release 12.4(22)T. |

| Field | Definition |
|---|---|
| Feature
                                          					 server | The
                                          					 number of active feature servers. |
| keepalive | Interval,
                                          					 in seconds, at which the peer sends keepalive messages. The range is from 1 to
                                          					 60 seconds. The default is 60 seconds. |
| register-uri | The
                                          					 registered Uniform Resource Identifier (URI) for the server. |
| Session
                                          					 reg_number | The
                                          					 registered number of the session. |
| Route
                                          					 point voice_reg_pool | Denotes
                                          					 the registered virtual device for application redirection. |
| Subscription sub_id | The
                                          					 subidentification number of the subscription. |

| global | (Optional) Displays aggregate statistics associated with the SIP phone
                                          						registration event. |
|---|---|
| pool
                                          						tag | (Optional) Displays registration pool statistics associated with a specific
                                          						pool tag. The maximum number of pools is version and platform dependent. Type ? to display
                                          						a list of values. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 15.1(2)T | Cisco
                                          						CME 8.1 Cisco SIP SRST 8.1 | This
                                          						command was modified. The global and pool keywords and tag argument were added.
                                          						The output display was also modified to show more information about pools in
                                          						unregistered state and time-stamps of registration event. |

| Field | Description |
|---|---|
| Statistics: | Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool. |
| Active
                                          					 registrations | Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations. |
| Last
                                          					 Register Request Time | Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to register the last time. |
| Last
                                          					 unRegister Request Time | Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to unregister the last time. |
| Total
                                          					 Registration Statistics | Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool. |
| Registration requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests. |
| Registration success | Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations. |
| Registration failed | Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations. |
| unRegister requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests. |
| unRegister success | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters. |
| unRegister failed | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters. |
| Global
                                          					 statistics | Used
                                          					 with the statistics keyword. Details all active registrations. |
| Register pool number statistics | Used
                                          					 with the statistics keyword. Details specific pool statistics. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show
                                          						voice register pool attempted-registrations | Displays the details of phones that attempt to register with Cisco Unified CME
                                          						or Cisco Unified SRST and fail. |

| template-tag | Number
                                          						of the template for which to display information. Range is 1 to 5. |
|---|---|
| all | Displays all configuration information associated with all the Cisco Unified
                                          						SIP IP phone templates. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) | This
                                          						command was modified to include emergency response location (ERL) information
                                          						assigned to a Cisco Unified SIP IP phone in the output display. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was modified. All keyword was added. Pools that have the template
                                          						defined are also displayed in the output. Voice-class stun-usage information is
                                          						displayed in the output. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display. |

| Field | Description |
|---|---|
| Anonymous call block | Status
                                          					 of anonymous caller blocking defined with the anonymous block command. |
| Attended Transfer | Status
                                          					 of attended transfer soft key defined with the transfer-attended command. |
| Blind
                                          					 Transfer | Status
                                          					 of blind transfer soft key defined with the transfer-blind command. |
| Caller-ID block | Status
                                          					 of caller-id feature defined with the caller-id block command. |
| Conference | Status
                                          					 of conference soft key defined with the conference command. |
| Conference admin | Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not. |
| Conference add mode | Current
                                          					 setting of hardware conference privilege for adding participants. |
| Conference drop mode | Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up. |
| Config: | List of
                                          					 configuration options defined for this template. |
| Dnd
                                          					 controls | Status
                                          					 of Do-Not-Disturb soft key defined with the dnd-control command. |
| Emergency response location | The
                                          					 ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made. |
| Lpcor
                                          					 incoming | Setting
                                          					 of the lpcor incoming command. |
| Lpcor
                                          					 outgoing | Setting
                                          					 of the lpcor outgoing command. |
| Lpcor
                                          					 type | Setting
                                          					 of the lpcor type command. |
| Temp
                                          					 Tag | Tag
                                          					 number of the requested template. |
| VAD | Status
                                          					 of voice activity detection defined with the vad command. |
| Voicemail | Voice-mail extension and timeout value defined with the voice-mail command. |

| Command | Description |
|---|---|
| show voice register all | Displays all voice register information, including statistics, pools, and dial
                                          						peers. |
| voice register template | Enters voice register template configuration mode and defines a template of
                                          						common parameters for Cisco Unified SIP IP phones. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| ata<mac-address> | Cisco SIP
                                          					 configuration profile for a particular Cisco ATA-186 or Cisco ATA-188 as
                                          					 indicated by the <mac-address>. This file is generated by using the create profile command. |
| ata<mac-address>.txt | ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco ATA-186
                                          					 or Cisco ATA-188 as indicated by the <mac-address>. This file is
                                          					 generated by using the file text command. |
| gk<mac-address> | Cisco SIP
                                          					 configuration profile for a particular Cisco IP Phone 7912 or Cisco IP Phone
                                          					 7912G as indicated by the <mac-address>. This file is generated by using
                                          					 the create profile command. |
| gk<mac>.txt | ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco IP Phone
                                          					 7912 or Cisco IP Phone 7912G as indicated by the <mac-address>. This file
                                          					 is generated by using the file text command. |
| Id<mac-address> | Cisco SIP
                                          					 configuration profile for a particular Cisco IP Phone 7905 or Cisco IP Phone
                                          					 7912G as indicated by the <mac-address>. This file is generated by using
                                          					 the create profile command. |
| Id<mac-address>.txt | ASCII
                                          					 text file of a Cisco SIP configuration profile for a particular Cisco IP Phone
                                          					 7905 or Cisco IP Phone 7912G as indicated by the <mac-address>. This file
                                          					 is generated by using the file text command. |
| SIPDefault.cnf | Configuration file to be shared by all Cisco SIP IP Phone 7940s and Cisco SIP
                                          					 IP Phone 7960s. This file is automatically generated by the router through the source-address and is placed in router memory. The SIPDefault.cnf
                                          					 file contains the IP address that the phones use to register for service, using
                                          					 the Session Initiation Protocol (SIP). |
| SIP<mac-address>.cnf | Cisco
                                          					 SIP configuration profile for a particular Cisco IP Phone 7940 or Cisco IP
                                          					 Phone 7960 as indicated by the <mac-address>. This file is generated by
                                          					 using the create profile command. |
| syncinfo.xml | Configuration file to be shared by all Cisco SIP IP Phone 7940s and Cisco SIP
                                          					 IP Phone 7960s. This file is generated by using the create profile command. |

|  | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profiles required for SIP phones. |
| reset (voice register dn) | Performs a complete reboot of one phone associated with a Cisco CME router. |
| reset (voice register pool) | Performs a complete reboot of one or all phones associated with a Cisco CME
                                          						router. |
| text file (voice register global) | Generates an ASCII format text file of the Cisco SIP configuration profile for
                                          						Cisco IP Phone 7905s and 7905Gs, Cisco IP phone 7912s and 7912Gs, Cisco
                                          						ATA-186s, and Cisco ATA-188s. |
| tftp-path (voice register global) | Specifies the directory to which the provisioning file for SIP phones in a
                                          						Cisco CallManager Express (Cisco CME) system will be written. |
| voice register global | Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco CME or Cisco SIP SRST
                                          						environment. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced |

| Command | Description |
|---|---|
| protocol -mode | Allows you to configure a preferred IP address mode for
                                          						SCCP IP phones. |
| ip source address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco Unified CME router. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was introduced |

| Command | Description |
|---|---|
| num -lines | Defines
                                          						number of lines supported by the phone. |
| phoneload -support | Defines
                                          						the phone support for Phoneload. |
| reference -pooltype | Reference pooltype to inherit the properties used in fast-track
                                          						configuration. |

| e164-number | E.164 telephone number to ring if IP phone extension does
                                          						not answer. |
|---|---|
| delay seconds | Sets the number of seconds that the call rings the IP phone
                                          						before ringing the remote phone. Range: 0 to 10. Default: disabled. |
| timeout seconds | Sets the number of seconds that the call rings after the
                                          						configured delay. Call continues to ring for this length of time on the IP
                                          						phone even if the remote phone answers the call. Range: 5 to 60. Default:
                                          						disabled. |
| cfwd-noan extension-number | (Optional) Forwards the call to this target number if the
                                          						phone does not answer after both the delay and timeout seconds have expired. This
                                          						is typically the voice mail number. Note This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. | Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |
| Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |

| Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco UnifiedCME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| mobility | Enables the Mobility feature on an extension of an SCCP IP
                                          						phone. |
| number | Associates a telephone or extension number with an
                                          						ephone-dn. |
| softkeys connected | Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state. |
| softkeys idle | Modifies the order and type of soft keys that display on an
                                          						IP phone during the idle call state. |

| e164-number | E.164 telephone number to call when the Cisco Unified SIP
                                          						IP phone extension does not answer. |
|---|---|
| delay seconds | Sets the number of seconds that the Cisco Unified SIP IP
                                          						phone rings when called. When the time delay is reached, the call is tranferred
                                          						to the PSTN phone and the SNR directory number. Range: 0 to 30. Default: 5. |
| timeout seconds | Sets the number of seconds that the Cisco Unified SIP IP
                                          						phone rings after the configured time delay. When the timeout value is reached,
                                          						no call is displayed on the phone. You have to use the Resume soft key to pull
                                          						back or the Mobility soft key to send the call to a mobile phone. Range: 30 to
                                          						60. Default: 60. Note When the default is enabled, the Cisco Unified SIP IP
                                                   						phone continues to ring for 60 seconds even if the remote phone answers the
                                                   						call. | Note | When the default is enabled, the Cisco Unified SIP IP
                                                   						phone continues to ring for 60 seconds even if the remote phone answers the
                                                   						call. |
| Note | When the default is enabled, the Cisco Unified SIP IP
                                                   						phone continues to ring for 60 seconds even if the remote phone answers the
                                                   						call. |
| cfwd-noan extension-number | (Optional) Forwards the call to the extension number when
                                          						the phone does not answer after both the time delay and timeout values are
                                          						reached. The extension number is typically the voice mail number. Note This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. | Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |
| Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |

| Note | When the default is enabled, the Cisco Unified SIP IP
                                                   						phone continues to ring for 60 seconds even if the remote phone answers the
                                                   						call. |
|---|---|

| Note | This option is not supported for calls from FXO trunks
                                                   						because the calls connect immediately. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| mobility (voice register dn) | Enables the Mobility feature on an extension of a Cisco
                                          						Unified SIP IP phone. |
| snr answer-too-soon (voice register dn) | Sets the time in which SNR calls are prevented from being
                                          						diverted to the voice mailbox of a mobile phone. |
| snr calling-number local (voice register dn) | Replaces the calling party number displayed on the
                                          						configured mobile phone with the local SNR number. |
| snr ring-stop (voice register dn) | Ends the ringing on a Cisco Unified SIP IP phone after the
                                          						Single SNR call is answered on the configured mobile phone. |

| time | Time, in seconds. Range: 1 to 5. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| snr | Enables SNR on the extension of an SCCP IP phone. |

| time | Time, in seconds. Range: 1 to 5. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| snr (voice register dn) | Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| calling-number local | Replaces a calling-party number and name with the
                                          						forwarding-party number and name for all calls. |
| mobility | Enables the Mobility feature on an extension of an SCCP IP
                                          						phone. |
| snr | Enables SNR on the extension of an SCCP IP phone. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| snr (voice register dn) | Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone. |

| virtual | Enables the virtual mode for an SNR DN when it is
                                          						unregistered or floating. Note Virtual mode is activated when the DN state remains up
                                                   						when it should be in the down state. | Note | Virtual mode is activated when the DN state remains up
                                                   						when it should be in the down state. |
|---|---|---|---|
| Note | Virtual mode is activated when the DN state remains up
                                                   						when it should be in the down state. |

| Note | Virtual mode is activated when the DN state remains up
                                                   						when it should be in the down state. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode to configure a DN for
                                          						an IP phone line, intercom line, paging line, voice-mail port, or MWI. |
| snr | Enables SNR on an extension of a Cisco Unified SCCP IP
                                          						phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| snr | Enables SNR on the extension of an SCCP IP phone. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| snr (voice register dn) | Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone. |

| Acct | (Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Short for “account code.” Provides access to
                                          						configured accounts. |
|---|---|
| Callback | (Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Requests callback notification when a busy
                                          						called line becomes free. |
| Endcall | (Optional) Soft-key name that appears on the IP phone
                                          						during the alerting call stage. Ends the current call. |

| Cisco IOS Release | Cisco CME Version | Modification |
|---|---|---|
| 12.3(11)T | 3.2 | This command was introduced. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| softkeys connected | Configures an ephone template for soft-key display during
                                          						the connected call stage. |
| softkeys idle | Configures an ephone template for soft-key display during
                                          						the idle call stage. |
| softkeys seized | Configures an ephone template for soft-key display during
                                          						the seized call stage. |

| ConfList | (Optional) Lists all the participants in a conference. |
|---|---|
| Confrn | (Optional) Connects callers to a conference call. This soft key
                                          						also enables ad-hoc conference creators to initiate a conference. |
| Endcall | (Optional) Ends the current call. |
| Hold | (Optional) Places an active call on hold and resumes the call. |
| Park | (Optional) Places an active call on hold so it can be retrieved from another
                                          						phone in the system. |
| RmLstC | (Optional) Removes the last conference participant. |
| Trnsfer | (Optional) Transfers active calls to another extension. |
| iDivert | (Optional) Immediately diverts a call to a voice-messaging
                                          						system. |
| HLog | (Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this softkey to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(22)YB | Cisco
                                          						Unified CME 7.1 | The Park keyword was added. |
| 15.1(3)T | Cisco
                                          						Unified CME 8.5 | The iDivert keword was added. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified. The syntax description for the Confrn soft key was
                                          						updated. The ConfList and RmLastC keywords were added. |
| Cisco IOS XE Everest 16.4.1 15.6(3)M1 | Cisco Unified CME 11.6 | HLog Softkey support was introduced. |

| Command | Description |
|---|---|
| softkeys hold (voice register template) | Modifies the soft key display on Cisco Unified SIP IP phones during the hold
                                          						call state. |
| softkeys idle (voice register template) | Modifies the soft key display on Cisco Unified SIP IP phones during the idle
                                          						call state. |
| softkeys seized (voice register template) | Modifies the soft key display on Cisco Unified SIP IP phones during the seized
                                          						call state. |
| template (voice register pool) | Applies a phone template to a Cisco Unified SIP IP phone. |

| Acct | (Optional) Soft key that provides access to configured
                                          						accounts. |
|---|---|
| ConfList | (Optional) Soft key that lists all parties in a conference. |
| Confrn | (Optional) Soft key that connects callers to a conference
                                          						call. |
| Endcall | (Optional) Soft key that ends the current call. |
| Flash | (Optional) Soft key that provides hookflash functionality
                                          						for public switched telephony network (PSTN) services on calls connected to the
                                          						PSTN via a foreign exchange office (FXO) port. Also called “hookflash.” |
| HLog | (Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls. |
| Hold | (Optional) Soft key that places an active call on hold and
                                          						resumes the call. |
| Join | (Optional) Soft key that joins an established call to
                                          						conference. |
| LiveRcd | (Optional) Soft key that enables recording of a call. |
| Mobility | (Optional) Soft key that forwards the call to the PSTN
                                          						number defined by the Single Number Reach (SNR) feature. |
| Park | (Optional) Soft key that places an active call on hold, so
                                          						it can be retrieved from another phone in the system. |
| RmLstC | (Optional) Soft key that removes the last party added to
                                          						the conference. This soft key only works for the conference creator. |
| Select | (Optional) Soft key that selects a call or a conference on
                                          						which to take action. |
| TrnsfVM | (Optional) Soft key that transfers a call to a voice-mail
                                          						extension number. |
| Trnsfer | (Optional) Soft key that transfers active calls to another
                                          						extension. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The HLog keyword was added. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | The ConfList , Join , RmLstC , and Select keywords were added. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The LiveRcd and TrnsfVM keywords were added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command with the LiveRcd and TrnsfVM keywords was integrated
                                          						into Cisco IOS Release 12.4(20)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The Mobility keyword was added. |
| 12.4(24)T | Cisco UnifiedCME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Note | The ConfList (including the Remove, Update, and Exit soft keys
                                       		  within the ConfList function) and RmLstC soft keys do not work on the Cisco
                                       		  Unified IP Phone 7902, 7935, and 7936. |
|---|---|

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode for an IP phone. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| fxo-hook-flash | Enables display of the Flash soft key. |
| hunt-group logout | Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of the HLog soft key on phones. |
| softkeys alerting | Modifies the soft-key display for the alerting call state. |
| softkeys idle | Modifies the soft-key display for the idle call state. |
| softkeys ringing | Modifies the soft-key display for the ringing call state. |
| softkeys seized | Modifies the soft-key display for the seized call state. |

| Join | (Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Joins an established call to a conference. |
|---|---|
| Newcall | (Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Opens a line on a speaker phone to place a new call. |
| Resume | (Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Reconnects with the call on hold. |
| Select | (Optional) Soft-key name that appears on an IP phone during
                                          						the hold call stage. Selects a call or a conference on which to take action. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | The Join and Select keywords were added. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with the Join and Select keywords was integrated into
                                          						Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode for an IP phone. |
| ephone-template | Declares and names an ephone template to configure IP phone
                                          						soft-key display and enters ephone-template configuration mode |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| softkeys alerting | Configures an ephone template for soft-key display during
                                          						the alerting call stage. |
| softkeys connected | Configures an ephone template for soft-key display during
                                          						the connected call stage. |
| softkeys idle | Configures an ephone template for soft-key display during
                                          						the idle call stage. |
| softkeys seized | Configures an ephone template for soft-key display during
                                          						the seized call stage. |

| Cfwdall | (Optional) Soft key that forwards all calls. |
|---|---|
| ConfList | (Optional) Soft key that lists all parties in a conference. |
| Dnd | (Optional) Soft key that enables the Do-Not-Disturb
                                          						features. This key is a toggle; pressing it a second time disables DND. |
| Gpickup | (Optional) Soft key that selectively picks up calls coming
                                          						into a phone number that is a member of a pickup group. |
| HLog | (Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls. |
| Join | (Optional) Soft key that joins an established call to a
                                          						conference. |
| Login | (Optional) Soft key that provides personal identification
                                          						number (PIN)-controlled access to restricted phone features. |
| Mobility | (Optional) Soft key that enables Single Number Reach (SNR)
                                          						feature. This key is a toggle; pressing it a second time disables SNR. |
| Newcall | (Optional) Soft key that opens a line on a speaker phone to
                                          						place a new call. |
| Pickup | (Optional) Soft key that selectively picks up calls coming
                                          						into another extension. |
| Redial | (Optional) Soft key that redials the last number dialed. |
| RmLstC | (Optional) Soft key that removes the last party added to
                                          						the conference. This soft key removes the last party only when the conference
                                          						creator presses it. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The HLog keyword was added. |
| 12.4(9)T | Cisco Unified CME 4.0 | The HLog keyword was integrated into
                                          						Cisco IOS Release 12.4(9)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | The ConfList , Join , and RmLstC keywords were added. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with the ConfList , Join , and RmLstC keywords was integrated into
                                          						Cisco IOS Release 12.4(15)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The Mobility keyword was added. |
| 12.4(24)T | Cisco unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Note | The ConfList (including the Remove, Update, and Exit soft keys
                                       		  within the ConfList function) and RmLstC soft keys do not work on the Cisco
                                       		  Unified IP Phone 7902 and Cisco Unified IP Phone 7935 and 7936. |
|---|---|

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode for an IP phone. |
| ephone-template | Creates an ephone template. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| hunt-group logout | Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of an HLog soft key on phones. |
| softkeys alerting | Configures soft-key display during the alerting call state. |
| softkeys connected | Configures soft-key display during the connected call
                                          						state. |
| softkeys seized | Configures soft-key display during the seized call state. |

| Cfwdall | (Optional) Soft key for “call forward all.” Forwards all calls. |
|---|---|
| DND | (Optional) Soft key that enables the Do-Not-Disturb feature. |
| Gpickup | (Optional) Soft key that allows a user to pickup a call that is ringing on
                                          						another phone. |
| Newcall | (Optional) Soft key that opens a line on a speakerphone to place a new call. |
| Pickup | (Optional) Soft key that allows a user to pickup a call that is ringing on
                                          						another phone that is a member of the same pickup group. |
| Redial | (Optional) Soft key that redials the last number dialed. |
| HLog | (Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this softkey to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(22)YB | Cisco
                                          						Unified CME 7.1 | The DND keyword
                                          						was added. |
| 12.4(24)T | Cisco
                                          						Unified CME 7.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(24)T. |
| Cisco IOS XE Everest 16.4.1 15.6(3)M1 | Cisco Unified CME 11.6 | HLog Softkey support was introduced. |

| Command | Description |
|---|---|
| softkeys connected (voice register template) | Modifies the soft-key display on SIP phones during the connected call state. |
| softkeys hold (voice register template) | Modifies the soft-key display on SIP phones during the hold call state. |
| softkeys idle (voice register template) | Modifies the soft-key display on SIP phones during the idle call state. |
| softkeys seized (voice register template) | Modifies the soft-key display on SIP phones during the seized call state. |
| template (voice register pool) | Applies a phone template to a SIP phone. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Fuji 16.9.1 | Unified CME 12.3 | A personal and public softkey template support was introduced for new Softkeys introduced as part of Unified CME 12.3 Release
                                          for Cisco IP Conference Phone 7832 and 8832. |

| Command | Description |
|---|---|
| softkeys connected (voice register template) | Modifies the soft-key display on SIP phones during the connected call state. |
| softkeys hold (voice register template) | Modifies the soft-key display on SIP phones during the hold call state. |
| softkeys idle (voice register template) | Modifies the soft-key display on SIP phones during the idle call state. |
| softkeys seized (voice register template) | Modifies the soft-key display on SIP phones during the seized call state. |
| template (voice register pool) | Applies a phone template to a SIP phone. |

| CBarge | (Optional) Soft key that allows a user to barge into a call
                                          						on a shared octo-line directory number. |
|---|---|
| Newcall | (Optional) Soft key that opens a line on a speakerphone to
                                          						place a new call. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was itegrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| softkeys alerting | Modifies the soft-key display for the alerting call stage. |
| softkeys idle | Modifies the soft-key display for the idle call stage. |
| softkeys seized | Modifies the soft-key display for the seized call stage. |

| Barge | (Optional) Soft key that allows a user to join a call on a
                                          						shared line. |
|---|---|
| Newcall | (Optional) Soft key that opens a line on a phone to place a
                                          						new call. |
| cBarge | (Optional) Soft key that allows a user to join a call on a
                                          						shared line and to turn the call into a conference call. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| softkeys alerting (voice register template) | Modifies the soft-key display on SIP phones during the
                                          						alerting call state. |
| softkeys idle (voice register template) | Modifies the soft-key display on SIP phones during the idle
                                          						call state. |
| softkeys seized (voice register template) | Modifies the soft-key display on SIP phones during the
                                          						seized call state. |
| template (voice register pool) | Applies a phone template to a SIP phone. |

| Answer | (Optional) Soft key that picks up an incoming call. |
|---|---|
| DND | (Optional) Soft key that enables the Do Not Disturb feature. |
| HLog | (Optional) Soft key that places a phone into not-ready status, in which it does
                                          						not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key to be
                                          						functional. This key is a toggle; pressing it a second time returns the phone
                                          						to ready status, in which it is available to receive calls. |
| iDivert | (Optional) Immediately diverts a call to a voice-messaging system. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco
                                          						Unified CME 7.1 | This
                                          						command was introduced. |
| 12.4(24)T | Cisco
                                          						Unified CME 7.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(24)T. |
| Cisco IOS XE Everest 16.4.1 15.6(3)M1 | Cisco Unified CME 11.6 | HLog Softkey support was introduced. |

| Command | Description |
|---|---|
| softkeys connected (voice register template) | Modifies the soft-key display on SIP phones during the connected call state. |
| softkeys hold (voice register template) | Modifies the soft-key display on SIP phones during the hold call state. |
| softkeys idle (voice register template) | Modifies the soft-key display on SIP phones during the idle call state. |
| softkeys seized (voice register template) | Modifies the soft-key display on SIP phones during the seized call state. |

| Answer | (Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state. |
|---|---|
| Dnd | (Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state. |
| HLog | (Optional) Soft-key name that appears on the IP phone
                                          						during the ringing call state. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| dnd feature ring | Allows phone buttons configured with the feature-ring
                                          						option to not ring when their phones are in do-not-disturb (DND) mode. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| hunt-group logout | Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents. |
| softkeys alerting | Configures an ephone template for soft-key display during
                                          						the alerting call state. |
| softkeys connected | Configures an ephone template for soft-key display during
                                          						the connected call state. |
| softkeys idle | Configures an ephone template for soft-key display during
                                          						the idle call state. |
| softkeys seized | Configures an ephone template for the soft-key display
                                          						during the seized call state. |

| CallBack | (Optional) Soft key that requests callback notification
                                          						when a busy called line becomes free. |
|---|---|
| Cfwdall | (Optional) Soft key that forwards all calls. |
| CWOff | (Optional) Soft key that disables Call Waiting. |
| Endcall | (Optional) Soft key that ends the current call. |
| Gpickup | (Optional) Soft key that selectively picks up calls coming
                                          						into a phone number that is a member of a pickup group. |
| HLog | (Optional) Soft key that places a phone into not-ready
                                          						status, in which it does not accept hunt-group calls. You must set the hunt-group logout command to HLog for this soft key
                                          						to be visible. This key is a toggle; pressing it a second time returns the
                                          						phone to ready status, in which it is available to receive calls. |
| MeetMe | (Optional) Soft key that initiates a meet-me conference. |
| Pickup | (Optional) Soft key that selectively picks up calls to
                                          						another extension. |
| Redial | (Optional) Soft key that redials the last number dialed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The HLog keyword was added. |
| 12.4(9)T | Cisco Unified CME 4.0 | The HLog keyword was integrated into
                                          						Cisco IOS Release 12.4(9)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | The MeetMe keyword was added. |
| 12.4(15)T | Cisco Unified CME 4.1 | The MeetMe keyword was integrated into
                                          						Cisco IOS Release 12.4(15)T. |
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was modified. The CWOff keyword was added. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode for an IP phone. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| hunt-group logout | Enables separate handling of DND and HLog functionality for
                                          						hunt-group agents and the display of an HLog soft key on phones. |
| softkeys alerting | Modifies the soft keys that display during the alerting
                                          						call stage. |
| softkeys connected | Modifies the soft keys that display during the connected
                                          						call stage. |
| softkeys idle | Modifies the soft keys that display during the idle call
                                          						stage. |

| Cfwdall | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Call forward all.” Forwards all calls. |
|---|---|
| Endcall | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Ends the current call. |
| Gpickup | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Group call pick up.” Selectively picks up
                                          						calls coming into a phone number that is a member of a pickup group. |
| MeetMe | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “MeetMe conference.” Initiates a meet-me
                                          						conference. |
| Pickup | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Short for “Call pick up.” Selectively picks up calls
                                          						coming into another extension. |
| Redial | (Optional) Appears on the Cisco Unified SIP IP phone during
                                          						the seized call state. Redials the last number dialed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 15.2(2)T | Cisco Unified CME 9.0 | This command was modified. The MeetMe keyword was added. |

| Command | Description |
|---|---|
| softkeys connected (voice register template) | Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the connected call state. |
| softkeys hold (voice register template) | Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the hold call state. |
| softkeys idle (voice register template) | Configures a Cisco Unified SIP IP phone template for soft
                                          						key display during the idle call state. |
| template (voice register pool) | Applies a template to a Cisco Unified SIP IP phone. |

| ip-address | IP address of the Cisco Unified CME router. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| ip-address | Preexisting router IP address, typically one of the addresses of the Ethernet
                                          						port of the router. |
|---|---|
| port port | (Optional) TCP/IP port number to use for SIP. Range is 2000 to 9999. Default is
                                          						5060 for SIP phones. |
| secondary ip-address | Secondary router for Cisco Unified CME. TCP/IP port number is
                                          						same as the primary Cisco Unified CME router. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| Cisco
                                          						IOS XE Everest 16.4.1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was modified to add the keyword: secondary . |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profiles required for SIP phones. |
| file text (voice register global) | Generates ASCII text files for SIP phones. |
| tftp-path (voice register global) | Specifies the directory to which the provisioning file for SIP phones in a
                                          						Cisco CallManager Express (Cisco Unified CME) system will be written. |
| voice register global | Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco
                                          						SIP SRST environment. |

| speed-tag | Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range is from 1 to 33. |
|---|---|
| digit-string | Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an ATA device. For IP phones, if the first character of this string is the
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined. |
| label label-text | (Optional) String that contains identifying text to be
                                          						displayed next to the speed-dial button. Enclose the string in quotation marks
                                          						if the string contains a space. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The number of speed-dial definitions that can be created
                                          						was increased from 4 to 33. The ability to program speed-dial numbers at the
                                          						phone and the ability to lock speed-dial numbers were introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)XL | Cisco CME 3.2.1 | This command was modified to allow IP phones to access more
                                          						speed-dial numbers than the number of available buttons on their phones and to
                                          						allow analog phones to access up to 33 speed-dial numbers. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| directory entry | Adds a systemwide phone directory entry or speed-dial
                                          						entry. |
| restart (ephone) | Performs a fast reboot of a single IP phone in a Cisco
                                          						Unified CME system. |
| restart (telephony-service) | Performs a fast reboot of one or all phones in a Cisco
                                          						Unified CME system. |
| ephone-template (ephone) | Applies template to ephone configuration. |

| speed-tag | Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range: 1 to 36. |
|---|---|
| number | Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone, or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an analog telephone adapter (ATA) device. For IP phones, if the first character of this string is the
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined. |
| label label | (Optional) String that contains identifying text to be
                                          						displayed next to the speed-dial button. Enclose the string in quotation marks
                                          						if the string contains a space. |
| blf | (Optional) Enables Busy Lamp Field (BLF) monitoring for a
                                          						speed-dial number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| logout-profile | Enables Cisco Unified IP phone for Extension Mobility and
                                          						assigns a logout profile to this phone. |
| reset (voice logout-profile and voice user-profile) | Performs complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded. |

| speed-tag | Unique sequence number that identifies a speed-dial
                                          						definition during configuration tasks. Range is 1 to 113. |
|---|---|
| digit-string | Digits to be dialed when the speed-dial button is pressed
                                          						on an IP phone or the digits to be dialed when the associated code is entered
                                          						from an analog phone with an ATA device. For IP phones, if the first character of this string is a
                                          						plus sign (+), this speed-dial number is locked and cannot be changed at the
                                          						phone. If the only character in this string is a pound sign (#), a
                                          						user-programmable speed-dial button with no speed-dial number attached is
                                          						defined. |
| label label-text | (Optional) Text string that appears next to the speed-dial
                                          						button. Enclose the string in quotation marks if the string contains a space. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 15.2(4)M | Cisco Unified CME 9.1 | This command was modified to increase the number of
                                          						speed-dial configuration to 113. |

| Command | Description |
|---|---|
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router. |
| reset (voice register pool) | Performs a complete reboot of a specific SIP phone
                                          						associated with a Cisco Unified CME system. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| dual | SRST fallback ephone-dns are dual-line. |
|---|---|
| dual-octo | SRST fallback ephone-dns are dual-line or octo-line,
                                          						depending on the phone type. |
| octo | SRST fallback ephone-dns are octo-line. |
| single | SRST fallback ephone-dns are single-line. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The dual-octo and octo keywords were added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command with the dual-octo and octo keywords was integrated into
                                          						Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| show telephony-service ephone-dn | Displays parameters for ephone-dns. |
| srst mode auto-provision | Enables SRST mode for a Cisco Unified CME router. |

| template-tag | Identifying number of an existing ephone-dn template. Range
                                          						is from 1 to 15. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-dn-template | Enters ephone-dn-template configuration mode to create an
                                          						ephone-dn template. |
| show telephony-service ephone-dn-template | Displays the contents of ephone-dn templates. |

| string | Description to be associated with an ephone. Maximum string
                                          						length is 100 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| show telephony-service ephone | Displays ephone settings. |

| template-tag | Identifying number of an existing ephone template. Range is
                                          						from 1 to 20. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-template | Enters ephone-template configuration mode to create an
                                          						ephone template. |
| show telephony-service ephone-template | Displays the contents of ephone templates. |

| all | Includes information for learned ephones and ephone-dns in
                                          						the running configuration. |
|---|---|
| dn | Includes information for learned ephone-dns in the running
                                          						configuration. |
| none | Does not include information for learned ephones or learned
                                          						ephone-dns in the running configuration. Use this keyword when you want Cisco
                                          						Unified CME to provide SRST fallback services for Cisco Unified CallManager. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Note | We do not recommend that you use the dn or all keyword if you want Cisco Unified CME to
                                       		  provide SRST fallback services. After the Cisco Unified CME-SRST router learns
                                       		  the phone configuration from Cisco Unified CallManager and you save the
                                       		  configuration, the fallback phones are treated as locally configured phones on
                                       		  the Cisco Unified CME-SRST router which can adversely impact the fallback
                                       		  behavior of those phones. |
|---|---|

| Command | Description |
|---|---|
| show telephony-service all | Displays detailed configuration for phones, voice ports,
                                          						and dial peers in a Cisco Unified CME system. |
| srst dn line-mode | Specifies line mode for the ephone-dns that are
                                          						automatically created in SRST mode on a Cisco Unified CME router. |

| username | Specifies the username who is authorized to enable the XML
                                          						interface. |
|---|---|
| password | Specifies the password to use for access. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Command | Description |
|---|---|
| username password | To assign a login account username and password to a phone
                                          						user so that the user can log in to the Cisco Unified CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays the automatic transfer of Cisco CME B-ACD call
                                          						statistics to a file. |
| hunt-group report every hours | Sets the hourly interval at which Cisco CME B-ACD call data
                                          						is automatically transferred to a file. |
| hunt-group report url | Sets filename parameters and the URL path where Cisco CME
                                          						B-ACD call statistics are to be sent using TFTP. |
| show ephone-hunt statistics | Displays ephone-hunt configuration information and current
                                          						status and statistics information. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| statistics collect | Enables the collection of call statistics for an ephone
                                          						hunt group. |

| IPaddress | IP address that identifies which IP phones are part of the
                                          						ERL. |
|---|---|
| mask | IP subnet mask for the network segment that is part of the
                                          						ERL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added to Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |

| text-message | Alphanumeric string of approximately 30 characters maximum
                                          						to display when the phone is idle. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |