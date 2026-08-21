---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-feature-guide-srst8-1-html-68eb2dbb5f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/feature/guide/srst8_1.html
retrieved_at: 2026-08-21T21:29:54.485255+00:00
---

Cisco Unified Survivable Remote Site Telephony 8.1 New Features

# Cisco Unified Survivable Remote Site Telephony 8.1 New Features

### Download Options

Updated: July 26, 2010

## Table Of Contents

Cisco Unified Survivable Remote Site Telephony 8.1 New Features

Finding Feature Information

Contents

Prerequisites for Cisco Unified SRST 8.1

Information About Cisco Unified SRST 8.1

Toll Fraud Prevention Enhancement

IP Address Trusted Authentication

Direct Inward Dial for Incoming ISDN Calls

Disconnecting ISDN Calls With no Matching Dial-peer

Blocking Two-stage Dialing Service on Analog and Digital FXO Ports

Enhancements to SIP Phone Configuration

Removing Global Registration Parameters for SIP Phones

Verifying SIP Phone Registration

How to Configure Cisco Unified SRST 8.1 New Features

Configuring IP Address Trusted Authentication for Incoming VoIP Calls

Prerequisites

Restrictions

Examples

Adding Valid IP Addresses For Incoming VoIP Calls

Prerequisites

Examples

Configuring Direct Inward Dial for Incoming ISDN Calls

Restrictions

Examples

Blocking Secondary Dialtone on Analog and Digital FXO Ports

Examples

Troubleshooting Tips for Toll Fraud Prevention

Additional References

Related Documents

Standards

MIBs

RFCs

Technical Assistance

Command Reference

attempted-registrations size

clear voice register attempted-registrations

dial-peer no-match isdn disconnect-cause

direct-inward-dial isdn

ip address trusted call-block cause

ip address trusted authenticate

ip address trusted list

secondary dialtone (voice port)

show voice register all

show voice register dial-peers

show voice register dn

show voice register global

show voice register pool

show voice register pool mac

show voice register pool ip

show voice register pool network

show voice register pool telephone-number

show voice register pool after-hour-exempt

show voice register pool attempted-registrations

show voice register pool connected

show voice register pool on-hold

show voice register pool phone-load

show voice register pool registered

show voice register pool remote

show voice register pool ringing

show voice register pool unregistered

show voice register statistics

voice register global

Feature Information for Cisco Unified SRST 8.1

## Cisco Unified Survivable Remote Site Telephony 8.1 New Features

Last Updated: November 04, 2009

This document describes the following new and enhanced features in Cisco Unified Survivable Remote Site Telephony 8.1 (Cisco Unified SRST):

• Toll Fraud Prevention Enhancement

• Enhancements to SIP Phone Configuration

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest feature information and caveats, see the release notes for your platform and software release. To find information about the features documented in this module, and to see a list of the releases in which each feature is supported, see the "Feature Information for Cisco Unified SRST 8.1" section .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS, Catalyst OS, and Cisco IOS XE software image support. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Contents

• Prerequisites for Cisco Unified SRST 8.1

• Information About Cisco Unified SRST 8.1

• How to Configure Cisco Unified SRST 8.1 New Features

• Configuration Examples for Cisco Unified CME 8.1, page 17

• Additional References

• Command Reference

• Feature Information for Cisco Unified SRST 8.1

## Prerequisites for Cisco Unified SRST 8.1

• Cisco Unified SRST 8.1

• Cisco IOS Release 15.1(2)T

## Information About Cisco Unified SRST 8.1

To configure Cisco Unified SRST features, you should understand the following concepts:

• Toll Fraud Prevention Enhancement

• Enhancements to SIP Phone Configuration

### Toll Fraud Prevention Enhancement

Cisco Unified SRST8.1 enhances the Toll Fraud Prevention feature to secure the Cisco Unified SRST system against potential toll fraud exploitation by unauthorized users. The following are the enhancements to Toll Fraud Prevention in Cisco Unified SRST:

• IP Address Trusted Authentication

• Direct Inward Dial for Incoming ISDN Calls

• Disconnecting ISDN Calls With no Matching Dial-peer

• Blocking Two-stage Dialing Service on Analog and Digital FXO Ports

### IP Address Trusted Authentication

IP address trusted authentication process blocks unauthorized calls and helps secure the Cisco Unified SRST system against potential toll fraud exploitation by unauthorized users. In Cisco Unified SRST, IP address trusted authentication is enabled by default. When IP address trusted authenticate is enabled, Cisco Unified CME accepts incoming VoIP (SIP/H.323) calls only if the remote IP address of an incoming VoIP call is successfully validated from the system IP address trusted list . If the IP address trusted authentication fails, an incoming VoIP call is then disconnected by the application with a user- defined cause code and a new application internal error code 31 message (TOLL_FRAUD_CALL_BLOCK) is logged. For more information, see the, "Configuring IP Address Trusted Authentication for Incoming VoIP Calls" section .

Cisco Unified SRST maintains an IP address trusted list to validate the remote IP addresses of incoming VOIP calls. Cisco Unified SRST saves an IPv4 session target of VoIP dial-peer to add the trusted IP addresses to IP address trusted list automatically.The IPv4 session target is identified as a trusted IP address only if the status of VoIP dial-peer in operation is "UP". Up to 10050 IPv4 addresses can be defined in the trusted IP address list. No duplicate IP addresses are allowed in the trusted IP address list. You can manually add up to 100 trusted IP addresses for incoming VOIP calls. For more information on manually adding trusted IP addresses, see the, "Adding Valid IP Addresses For Incoming VoIP Calls" section .

A call detail record (CDR) history record is generated when the call is blocked as a result of IP address trusted authentication failure. A new voice Internal Error Code (IEC) is saved to the CDR history record. The voice IEC error messages are logged to syslog if "voice iec syslog" option is enabled. The following is an IEC toll fraud call rejected syslog display:

```
*Aug 14 19:54:32.507: %VOICE_IEC-3-GW: Application Framework Core: Internal Error (Toll 
fraud call rejected): IEC=1.1.228.3.31.0 on callID 3 GUID=AE5066C5883E11DE8026A96657501A09
```

The IP address trusted list authentication must be suspended when Cisco Unified SRST is defined with "gateway" and a VoIP dial-peer with "session-target ras" is in operational UP status. The incoming VOIP call routing is then controlled by the gatekeeper. Table 1 shows administration state and operational state in different trigger conditions.

Table 1 Administration and Operation States of IP Address Trusted Authentication

Trigger Condition

Administration State

Operation State

When ip address trusted authenticate is enabled.

Down

Down

When "gateway" is defined and a VoIP dial-peer with "ras" as a session target is in "UP" operational state

Up

Down

When ip address trusted authenticate is enabled and either "gateway" is not defined or no voip dial-peer with "ras" as session target is in "UP" operational state

Up

Up

Note We recommend enabling SIP authentication before enabling Out-of-dialog REFER (OOD-R) to avoid any potential toll fraud threats.

### Direct Inward Dial for Incoming ISDN Calls

In Cisco Unified SRST 8.1 and later versions the direct-inward-dial isdn feature in enabled to prevent the toll fraud for incoming ISDN calls. The called number of an incoming ISDN enbloc dialing call is used to match the outbound dial-peers even if the direct-inward-dial option is disabled from a selected inbound plain old telephone service (POTS) dial-peer. If no outbound dial-peer is selected for the outgoing call set up, the incoming ISDN call is disconnected with cause-code "unassigned-number (1)". For more information on direct-inward dial for incoming ISDN calls, see the, "Configuring Direct Inward Dial for Incoming ISDN Calls" section .

### Disconnecting ISDN Calls With no Matching Dial-peer

Cisco Unified SRST 8.1 and later versions disconnect unauthorized ISDN calls when no matching inbound voice dial-peer is selected. Cisco Unified SRST and voice gateways use the dial-peer no-match disconnect-cause command to disconnect an incoming ISDN call when no inbound dial-peer is selected to avoid default POTS dial-peer behavior including two-stage dialing service to handle the incoming ISDN call.

### Blocking Two-stage Dialing Service on Analog and Digital FXO Ports

Cisco Unified SRST 8.1 and later versions block the two-stage dialing service which is initiated when an Analog or Digital FXO port goes offhook and the private line automatic ringdown (PLAR) connection is not setup from the voice-port. As a result, no outbound dial-peer is selected for an incoming analog or digital FXO call and no dialed digits are collected from an FXO call. Cisco Unified SRST and voice gateways disconnect the FXO call with cause-code "unassigned-number (1)". Cisco Unified SRST uses the no secondary dialtone command by default from FXO voice-port to block the two-stage dialing service on Analog or digital FXO ports. For more information on blocking two-stage dialing service on Analog and Digital FXO port, see Blocking Secondary Dialtone on Analog and Digital FXO Ports .

### Enhancements to SIP Phone Configuration

Cisco Unified SRST 8.1 and later versions, allows you to verify SIP phone registration process, remove global registration parameters, and display details on phones that attempted to register with Cisco Unified SRST and fail. Following are the enhancements to SIP Phone configuration:

• Removing Global Registration Parameters for SIP Phones

• Verifying SIP Phone Registration

### Removing Global Registration Parameters for SIP Phones

In Cisco Unified SRST 8.1 and later versions, you can use the no voice register global command to automatically remove existing DNs and pools. The no voice register global command also removes the voice register dialplan, template, and session-server configurations when the system is in Cisco Unified CME mode. For more information, see the "Command Reference" section

### Verifying SIP Phone Registration

In Cisco Unified CME 8.1 and later versions, you can verify SIP phone registration details and other information - related to SIP phones. Table 2 shows a list of new show commands and the information that these commands provide. For detailed information on these show commands, see the "Command Reference" section .

Table 2 New commands and display information

Commands

Display Information

attempted-registrations size

Allows you to set the size of the table that stores information related to SIP phones that attempted to register and failed.

clear voice register attempted-registrations

Allows you to clear all the entries in attempted-registration table.

show voice register dn all

Displays the details of all the DNs defined in the system.

show voice register dial-peers pool

Displays the dialpeers a pool with a specific tag.

show voice register dialplan all

Displays the details of all the Dialplans that are defined in the system.

show voice register pool after-hour-exempt

Displays the details of the phones with "after-hour exempt" set.

show voice register pool attempted-registrations

Displays the details of the phones that have attempted to register and failed.

show voice register pool connected

Displays detailed information of phones that are in connected state (in conversation).

show voice register pool connected brief

Displays a brief information of phones that are in connected state (in conversation).

show voice register pool ip

Displays the details of a phone with a specific IPv4 address.

show voice register pool mac

Displays the details of a phone with a specific mac address.

show voice register pool network

Displays the information of the pools with a specific network address configured.

show voice register pool on-hold

Displays detailed information of phones that are currently on-hold.

show voice register pool on-hold brief

Displays brief information of phones that are currently on-hold.

show voice register pool phone-load

Displays the phone-load details of registered phones.

show voice register pool registered

Displays the details of the phones that are successfully registered.

show voice register pool remote

Displays remote phones (phones with no Address Resolution Protocol (ARP) entry.

show voice register pool ringing

Displays the detailed information of the phones that are currently ringing.

show voice register pool ringing brief

Displays brief information of phones that are currently ringing.

show voice register pool telephone-number

Displays the details of the phone with a specified telephone-number.

show voice register pool unregistered

Displays the details of the pools that do not have any registered phones.

show voice register statistics global

Displays the global statistics of registered SIP phones.

show voice register statistics pool

Displays the pool statistics associated with a specific pool.

## How to Configure Cisco Unified SRST 8.1 New Features

This section contains the following tasks.

• Configuring IP Address Trusted Authentication for Incoming VoIP Calls

• Adding Valid IP Addresses For Incoming VoIP Calls

• Configuring Direct Inward Dial for Incoming ISDN Calls

• Blocking Secondary Dialtone on Analog and Digital FXO Ports

• Troubleshooting Tips for Toll Fraud Prevention

### Configuring IP Address Trusted Authentication for Incoming VoIP Calls

### Prerequisites

• Cisco Unified SRST 8.1 or a later version.

### Restrictions

• IP address trusted authentication is skipped if an incoming SIP call is originated from a SIP phone.

• IP address trusted authentication is skipped if an incoming call is an IPv6 call.

• For an incoming VoIP call, IP trusted authentication must be invoked when the IP address trusted authentication is in "UP" operational state.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice service voip

4. ip address trusted authenticate

5. ip-address trusted call-block cause < code >

6. end

7. show ip address trusted list

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

voice service voip

Example:

Router(config)# voice service voip

Enters voice service voip configuration mode.

Step 4

ip address trusted authenticate

Example:

Router(conf-voi-serv)# ip address trusted authenticate

Enables IP address authentication on incoming H.323 or SIP trunk calls for toll fraud prevention support.

IP address trusted list authenticate is enabled by default. Use the " no ip address trusted list authenticate " command to disable the IP address trusted list authentication.

Step 5

ip-address trusted call-block cause code

Example:

Router(conf-voi-serv)#ip address trusted call-block cause call-reject

Issues a cause-code when the incoming call is rejected to the IP address trusted authentication.

Note If the IP address trusted authentication fails, a call-reject (21) cause-code is issued to disconnect the incoming VoIP call.

Step 6

end

Example:

Router()# end

Returns to privileged EXEC mode.

Step 7

show ip address trusted list

Example:

Router# # show ip address trusted list

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

Verifies a list of valid IP addresses for incoming H.323 or SIP trunk calls, Call Block cause for rejected incoming calls.

### Examples

Router # show ip address trusted list

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

VoIP Dial-peer IPv4 Session Targets:

Peer Tag Oper State Session Target

-------- ---------- --------------

11 DOWN ipv4:1.3.45.1

1 UP ipv4:1.3.45.1

IP Address Trusted List:

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 172.19.245.0 255.255.255.0''

### Adding Valid IP Addresses For Incoming VoIP Calls

### Prerequisites

• Cisco Unified SRST 8.1 or a later version.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice service voip

4. ip address trusted list

5. ipv4 ipv4 address network mask

6. end

7. show ip address trusted list

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

voice service voip

Example:

Router(config)# voice service voip

Enters voice service voip configuration mode.

Step 4

ip address trusted list

Example:

Router(conf-voi-serv)# ip address trusted list

Router(cfg-iptrust-list)#

Enters ip address trusted list mode and allows to manually add additional valid IP addresses.

Step 5

ipv4 {< ipv4 address > [< network mask >]}

Example:

Router(config)#voice service voip

Router(conf-voi-serv)#ip taddress trusted list

Router(cfg-iptrust-list)#ipv4 172.19.245.1

Router(cfg-iptrust-list)#ipv4 172.19.243.1

Allows you to add up to 100 IPv4 addresses in ip address trusted list . Duplicate IP addresses are not allowed in the ip address trusted list.

• (Optional) network mask — allows to define a subnet IP address.

Step 6

end

Example:

Router(config-register-pool)# end

Returns to privileged EXEC mode.

Step 7

show ip address trusted list

Example:

Router# show shared-line

Displays a list of valid IP addresses for incoming H.323 or SIP trunk calls.

### Examples

The following example shows 4 IP addresses configured as trusted IP addresses:

Router#show ip address trusted list

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

VoIP Dial-peer IPv4 Session Targets:

Peer Tag Oper State Session Target

-------- ---------- --------------

11 DOWN ipv4:1.3.45.1

1 UP ipv4:1.3.45.1

IP Address Trusted List:

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 171.19.10.1

### Configuring Direct Inward Dial for Incoming ISDN Calls

To configure Direct Inward Dial for incoming ISDN calls, perform the following steps:

### Restrictions

• Direct-inward-dial isdn is not supported for incoming ISDN overlap dialing call.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice service pots

4. direct-inward-dial isdn

5. end

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

voice service pots

Example:

Router(config)# voice service pots

Router(conf-voi-serv)#

Enters voice service configuration mode with voice telephone-service encapsulation type (pots).

Step 4

direct-inward-dial isdn

Example:

Router(conf-voi-serv)#direct-inward-dial isdn

Enables direct-inward-dial (DID) for incoming ISDN number. The incoming ISDN (enbloc dialing) call is treated as if the digits were received from the DID trunk. The called number is used to select the outgoing dial peer. No dial tone is presented to the caller.

Step 5

exit

Example:

Router(conf-voi-serv)# exit

Exits voice service pots configuration mode.

### Examples

!

voice service voip

ip address trusted list

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 171.19.10.1

allow-connections h323 to h323

allow-connections h323 to sip

allow-connections sip to h323

allow-connections sip to sip

supplementary-service media-renegotiate

sip

registrar server expires max 120 min 120

!

!

dial-peer voice 1 voip

destination-pattern 5511...

session protocol sipv2

session target ipv4:1.3.45.1

incoming called-number 5522...

direct-inward-dial

dtmf-relay sip-notify

codec g711ulaw

!

dial-peer voice 100 pots

destination-pattern 91...

incoming called-number 2...

forward-digits 4

!

### Blocking Secondary Dialtone on Analog and Digital FXO Ports

To block secondary dialtone on Analog and Digital FXO port, perform the following steps:

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice-port

4. no secondary dialtone

5. exit

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

voice-port

Example:

Router(config)#voice-p 2/0/0

Enters voice-port configuration mode.

• Type your Analog or Digital FXO port number.

Step 4

no secondary dialtone

Example:

Router((config-voiceport)# no secondary dialtone

Blocks the secondary dialtone on Analong and Digital FXO port.

Step 5

end

Example:

Router(conf-voiceport)# exit

Returns to privileged EXEC mode.

Step 6

show run

Example:

Router# show run | sec voice-port 2/0/0

Verifies that the secondary dialtone is disabled on the specific voice-port.

### Examples

```
Router# conf t
```

```
Router(config)#voice-p 2/0/0
```

```
Router(config-voiceport)# no secondary dialtone
```

!

end

Router# show run | sec voice-port 2/0/0

Foreign Exchange Office 2/0/0 Slot is 2, Sub-unit is 0, Port is 0

Type of VoicePort is FXO

Operation State is DORMANT

Administrative State is UP

...

Secondary dialtone is disabled

### Troubleshooting Tips for Toll Fraud Prevention

When incoming VOIP call is rejected by IP address trusted authentication, a specific internal error code (IEC) 1.1.228.3.31.0 is saved to the call history record. You can monitor the failed or rejected calls using the IEC support. Follow these steps to monitor any rejected calls:

Step 1 Use the show voice iec description command to find the text description of an IEC code.

Router# show voice iec description 1.1.228.3.31.0

IEC Version: 1

Entity: 1 (Gateway)

Category: 228 (User is denied access to this service)

Subsystem: 3 (Application Framework Core)

Error: 31 (Toll fraud call rejected)

Diagnostic Code: 0

Step 2 View the IEC statistics information using the Enable iec statistics command. The example below shows that 2 calls were rejected due to toll fraud call reject error code.

Example:

Router# Enable iec statistics

Router(config)#voice statistics type iec

Router#show voice statistics iec since-reboot

Internal Error Code counters

----------------------------

Counters since reboot:

SUBSYSTEM Application Framework Core [subsystem code 3]

[errcode 31] Toll fraud call rejected 2

Step 3 Use the enable IEC syslog command to verify the syslog message logged when a call with IEC error is released.

Example:

Router# Enable iec syslog

Router (config)#voice iec syslog

Feb 11 01:42:57.371: %VOICE_IEC-3-GW: Application Framework Core:

Internal Error (Toll fraud call rejected): IEC=1.1.228.3.31.0 on

callID 288 GUID=DB3F10AC619711DCA7618593A790099E

Step 4 Verify the source address of an incoming VOIP call using the show call history voice last command.

Example:

Router# show call history voice last 1

GENERIC:

SetupTime=3306550 ms

Index=6

...

InternalErrorCode=1.1.228.3.31.0

...

RemoteMediaIPAddress=1.5.14.13

...

Step 5 IEC is saved to VSA of Radius Accounting Stop records. Monitor the rejected calls using the external RADIUS server.

Example:

Feb 11 01:44:06.527: RADIUS: Cisco AVpair [1] 36 "internal-error-code=1.1.228.3.31.0"

Step 6 Retrieve the IEC details from cCallHistoryIec MIB object. More information on IEC is available at: ttp://www.cisco.com/en/US/docs/ios/voice/monitor/configuration/guide/vt_voip_err_cds_ps6350_TSD_Products_Configuration_Guide_Chapter.html

Example:

getmany 1.5.14.10 cCallHistoryIec

cCallHistoryIec.6.1 = 1.1.228.3.31.0

>getmany 172.19.156.132 cCallHistory

cCallHistorySetupTime.6 = 815385

cCallHistoryPeerAddress.6 = 1300

cCallHistoryPeerSubAddress.6 =

cCallHistoryPeerId.6 = 8000

cCallHistoryPeerIfIndex.6 = 76

cCallHistoryLogicalIfIndex.6 = 0

cCallHistoryDisconnectCause.6 = 15

cCallHistoryDisconnectText.6 = call rejected (21)

cCallHistoryConnectTime.6 = 0

cCallHistoryDisconnectTime.6 = 815387

cCallHistoryCallOrigin.6 = answer(2)

cCallHistoryChargedUnits.6 = 0

cCallHistoryInfoType.6 = speech(2)

cCallHistoryTransmitPackets.6 = 0

cCallHistoryTransmitBytes.6 = 0

cCallHistoryReceivePackets.6 = 0

cCallHistoryReceiveBytes.6 = 0

cCallHistoryReleaseSrc.6 = internalCallControlApp(7)

cCallHistoryIec.6.1 = 1.1.228.3.31.0

>getone 172.19.156.132 cvVoIPCallHistoryRemMediaIPAddr.6

cvVoIPCallHistoryRemMediaIPAddr.6 = 1.5.14.13

## Additional References

The following sections provide references related to Cisco Unified SRST.

### Related Documents

Related Topic

Document Title

Cisco Unified CME configuration

• Cisco Unified Communications Manager Express System Administrator Guide

• Cisco Unified Communications Manager Express Command Reference

Cisco Unified CME network design

• Cisco Unified CallManager Express Solution Reference Network Design Guide

Cisco IOS voice configuration

• Cisco IOS Voice Configuration Library

• Cisco IOS Voice Command Reference

Phone documentation for Cisco Unified CME

• User Documentation for Cisco Unified IP Phones

### Standards

Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature.

—

### MIBs

MIB

MIBs Link

No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature.

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL:

http://www.cisco.com/go/mibs

### RFCs

RFC

Title

No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature.

—

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/techsupport

## Command Reference

The following commands are introduced or modified in the features documented in this module.

New and Modified Commands

• attempted-registrations size

• clear voice register attempted-registrations

• dial-peer no-match isdn disconnect-cause

• direct-inward-dial isdn

• ip address trusted call-block cause

• ip address trusted authenticate

• ip address trusted list

• secondary dialtone (voice port)

• show voice register all

• show voice register dial-peers

• show voice register dn

• show voice register global

• show voice register pool

• show voice register pool mac

• show voice register pool ip

• show voice register pool network

• show voice register pool telephone-number

• show voice register pool after-hour-exempt

• show voice register pool attempted-registrations

• show voice register pool connected

• show voice register pool on-hold

• show voice register pool phone-load

• show voice register pool registered

• show voice register pool remote

• show voice register pool ringing

• show voice register pool unregistered

• show voice register statistics

• voice register global

## attempted-registrations size

To set the size of the table that shows a number of attempted-registrations, use the attempted- registrations command in voice register global mode. To set the size of attempted-registrations table to its default value, use the no form of this command.

attempted-registrations size size

no attempted-registrations size

### Syntax Description

size

Number of entries in attempted registrations table. Size range from 0 to 50.

### Command Default

The default size for attempted registration table is 10.

## Command Modes

voice register global

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST  8.1

This command was introduced.

### Usage Guidelines

Use this command to define the size of the table that stores information related to SIP phones that attempt to register with Cisco Unified CME or Cisco Unified SRST and fail. The default size of an attempted registration table is 10. The minimum size of attempted registration table is 0. Use the attempted-registration size 0 when you do not wish to store any information about phones attempting to register with the Cisco Unified CME or Cisco Unified SRST and fail. The maximum size of attempted registration table is 50.

When the current number of entries in the table is more than the new size that is being configured, system prompts the user for the following confirmation, "This will remove x old entries from the table. Proceed? Yes/No ?". The default user confirmation is "No". Where "x" represents the number of entries that will be deleted. The old entries are classified on basis of the time-stamp of the latest register attempt made by the phone.

During rollback, the user confirmation is not sought and the target configuration is applied. If the current number of entries in the table is more than the default value of the table size, then entries in excess of the default table size are cleared before reverting to the target table size.

For example, if the configured table size is 40 and there are currently 35 entries in the table, any change in the size of the attempted registration table during rollback removes 25 oldest entries leaving only the default (10) entries before making the table size equal to the size in target configuration.

### Examples

The following example shows attempted-registrations size:

Router# conf t

Router(config)#voice register global

Router(config-register-global)#attempted-registrations size 15

!

### Related Commands

Command

Description

clear voice register attempted- registrations

Allows to delete entries in attempted-registration table.

show voice register attempted-registrations

Displays details of phones that attempted to register and failed.

## clear voice register attempted-registrations

To clear the attempted-registrations, use the clear voice register attempted-registrations command in voice register global mode.

clear voice register attempted registrations [ip ip-address | mac H.H.H ]

### Syntax Description

ip ip-address

(Optional) IP address of the SIP phone attempting to register.

mac H.H.H

(Optional) MAC address of the SIP phone attempting to register.

### Command Default

The attempted-registration entries are not cleared.

## Command Modes

Privileged EXEC.

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to delete the entries in the attempted-registration table. The clear voice register attempted-registrations command does not alter the table size, but clears the existing entries. A user confirmation is sought before the cleanup is done.

The primary key to recognize the SIP phones that fail to register is through their MAC address (hardware address) and the secondary key is the IP address. You can clear the attempted registration entry for a specific phone that failed to register by providing its IP address or MAC address and create more space for new attempted registration entries in the attempted-registrations table. When no options (IP or MAC) are selected, all the entries are removed. A user confirmation is sought in such a case, before clearing the attempted-registrations table.

The ip keyword allows you to delete entries corresponding to a specific IP address. Similarly, the mac keyword allows you to clear the entries related to a specific MAC address. User confirmation is not sought if ip or mac option is used.

### Examples

Router # clear voice regis attempted-registrations

This will clear all the entries. Proceed? Yes/No? [no]: Yes

Router# clear voice register attempted-registrations ?

ip IP Address of the phone

mac MAC Address of the phone

### Related Commands

Command

Description

attempted-registrations size

Allows to set the size of the attempted-registrations table.

show voice register attempted-registration

Displays details of phones that attempted to register and failed.

## dial-peer no-match isdn disconnect-cause

To disconnect the incoming ISDN call when no inbound voice dial peer is matched, use the dial-peer no-match disconnect-cause command in global configuration mode. To restore the default incoming call handling behavior, use the no form of this command.

dial-peer no-match isdn disconnect-cause cause-code

no dial-peer no-match isdn disconnect-cause cause-code

### Syntax Description

cause-code

An ISDN cause code number. Range is from 1 to 188.

### Command Default

Dial-peer no-match isdn disconnect-cause command is disabled. Incoming ISDN calls are not forced to disconnect if no inbound dial-peer is matched.

## Command Modes

Global configuration

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to disconnect unathorized ISDN calls when no inbound voice or modem dial peer is matched.

Refer to the ISDN Cause Values table in the Cisco IOS Debug Command Reference , for a list of ISDN cause codes.

### Examples

The following example shows that ISDN cause code 28 has been specified to match inbound voice or modem dial peers:

Router# dial-peer no-match disconnect-cause 28

### Related Commands

Command

Description

show dial-peer voice

Displays configuration information for dial peers.

## direct-inward-dial isdn

To enable incoming ISDN enbloc dialing calls, use the direct-inward-dial isdn command in voice service voip mode. To disable incoming ISDN enbloc dialing calls use the no form of the command.

direct-inward-dial isdn

no direct-inward-dial isdn

### Syntax Description

This command has no arguments or keywords.

### Command Default

The direct inward dial isdn is command is enabled.

## Command Modes

voice service pots

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use the direct-inward-dial-isdn command to enable the direct-inward-dial (DID) call treatment for an incoming ISDN call. When this feature is enabled, the incoming ISDN call is treated as if the digits were received from the DID trunk. The called number is used to select the outgoing dial peer. No dial tone is presented to the caller to collect dialed digits even if "no direct-inward-dial" of the selected inbound dial-peer is defined for an incoming ISDN call.

Use the no form of this command to turn off the global direct-inward-dial setting for incoming ISDN calls. When this command line is disabled, the "direct-inward-dial" setting of a selected inbound dial-peer is used to handle the incoming ISDN calls.'

### Examples

The following is a sample output from this command displaying DID enabled for ISDN:

!

voice service voip

ip address trusted list

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 171.19.10.1

allow-connections h323 to h323

allow-connections h323 to sip

allow-connections sip to h323

allow-connections sip to sip

supplementary-service media-renegotiate

sip

registrar server expires max 120 min 120

!

!

dial-peer voice 1 voip

destination-pattern 5511...

session protocol sipv2

session target ipv4:1.3.45.1

incoming called-number 5522...

direct-inward-dial

...

!

### Related Commands

Command

Description

voice service

Enters voice service configuration mode.

## ip address trusted call-block cause

To issues a cause-code when the incoming call is rejected by the IP address trusted authentication, use the ip address trusted call-block cause command in voice service voip mode. To stop the IP address trusted authentication process from sending a call-block cause, use the no form of this command.

ip-address trusted call-block cause code-id

no ip-address trusted call-block cause code-id

### Syntax Description

code-id

Q.850 call-disconnect cause code. Range is from 1 to 127.

### Command Default

A call-reject (21) cause-code is issued to disconnect the incoming VoIP calls.

## Command Modes

Voice Service voip.

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to issue a cause-code when the incoming call is rejected by the IP address trusted authentication. You can issue a specific call-block cause code using any one of the Q.850 call reject cause codes.

### Examples

The following is a sample output from this command displaying the default call block cause code:

Router # show ip address trusted list

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

VoIP Dial-peer IPv4 Session Targets:

Peer Tag Oper State Session Target

-------- ---------- --------------

11 DOWN ipv4:1.3.45.1

1 UP ipv4:1.3.45.1

### Related Commands

Command

Description

ip address trusted list

Allows to manually add additional valid IP addresses.

ip address trusted authenticate

Enables IP address trusted authentication for incoming VoIP calls.

## ip address trusted authenticate

To enable ip address trusted authentication for incoming VoIP (H.323/SIP) calls, use the ip address trusted authenticate command in voice service voip mode. To disable ip address trusted authentication, use the no form of this command.

ip address trusted authenticate

no ip address trusted authenticate

### Syntax Description

This command has no arguments or keywords.

### Command Default

IP address trusted list authenticate is enabled.

## Command Modes

Voice Service Voip

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to enable the ip address trusted authentication for incoming H.323 or SIP trunk calls for toll fraud prevention on Cisco Unified CME.

### Examples

The following is a sample output from this command displaying IP address trusted authentication enabled for incoming calls:

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

VoIP Dial-peer IPv4 Session Targets:

Peer Tag Oper State Session Target

-------- ---------- --------------

11 DOWN ipv4:1.3.45.1

1 UP ipv4:1.3.45.1

IP Address Trusted List:

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 171.19.10.1

### Related Commands

Command

Description

ip address trusted list

Allows to manually add additional valid IP addresses.

ip address trusted call- block cause

Allows to issues a cause-code when the incoming call is rejected by the IP address trusted authentication.

## ip address trusted list

To manually add multiple IP addresses for incoming VoIP (H.323/SIP) calls, use the ip address trusted list command in voice service voip mode. To turn off the list, use the no form of this command.

ip address trusted list { ipv4 ipv4 address network mask }

no ip address trusted list { ipv4 ipv4 address network mask }

### Syntax Description

ipv4-address

IPv4 address of the incoming H.323 or SIP calls.

network mask

Subnet IP address.

### Command Default

IP address trusted list is disabled.

## Command Modes

Voice Service Voip.

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to manually add unique and multiple IP addresses to a list of trusted IP addresses. You can add up to 100 IPv4 addresses in the ip address trusted list . No duplicate IP addresses are allowed.

### Examples

The following is a sample output from this command displaying a list of trusted IP addresses:

Router # show ip address trusted list

IP Address Trusted Authentication

Administration State: UP

Operation State: UP

IP Address Trusted Call Block Cause: call-reject (21)

VoIP Dial-peer IPv4 Session Targets:

Peer Tag Oper State Session Target

-------- ---------- --------------

11 DOWN ipv4:1.3.45.1

1 UP ipv4:1.3.45.1

IP Address Trusted List:

ipv4 172.19.245.1

ipv4 172.19.247.1

ipv4 172.19.243.1

ipv4 171.19.245.1

ipv4 171.19.10.1

### Related Commands

Command

Description

IP address trusted authenticate

Enables IP address trusted authentication for incoming VoIP calls.

IP address trusted code-block cause

Allows to issues a cause-code when the incoming call is rejected by the IP address trusted authentication.

## secondary dialtone (voice port)

To allow dialed digits to be collected from the remote switch when "connection plar" is not defined from the analog FXO voice-port, use the secondary dialtone command in global configuration mode. To disable the secondary dialtone, use the no form of the command.

secondary dialtone

no secondary dialtone

### Syntax Description

This command has no arguments or keywords.

### Command Default

The secondary dialtone command is disabled.

## Command Modes

Global configuration

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use the secondary dialtone command to allow dialed digits to be collected from the remote switch when "connection plar" is not defined from the analog FXO voice-port.

The following is a sample output from this command:

Router(config)# voice-port 2/0/0

Router (config-voiceport)# no secondary ?

dialtone Secondary dialtone option for FXO port

Router (config-voiceport)#no secondary dialtone

"secondary dialtone" is used to enable 2-stage dialing for an

incoming call

!

### Related Commands

Command

Description

voice service

Enters voice service configuration mode.

## show voice register all

To display all Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) or Cisco Unified Communications Manager Express (Cisco Unified CME) configurations and register information, use the show voice register all command in privileged EXEC mode.

show voice register all

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was added to Cisco CME.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1

This command was modified. The output display was modified.

### Examples

Cisco Unified SIP SRST

The following is an example of show voice register all command:

```
Router# show voice register all
```

```
VOICE REGISTER GLOBAL
```

```
=====================
```

```
CONFIG [Version=8.1]
```

```
========================
```

```
Version 8.1
```

```
Mode is srst
```

```
Max-pool is 10
```

```
Max-dn is 10
```

```
Outbound-proxy is enabled and will use global configured value
```

```
Security Policy: DEVICE-DEFAULT
```

```
timeout interdigit 10
```

```
network-locale[0] US    (This is the default network locale for this box)
```

```
network-locale[1] US
```

```
network-locale[2] US
```

```
network-locale[3] US
```

```
network-locale[4] US
```

```
user-locale[0] US    (This is the default user locale for this box)
```

```
user-locale[1] US
```

```
user-locale[2] US
```

```
user-locale[3] US
```

```
user-locale[4] US   Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
VOICE REGISTER DN
```

```
=================
```

```
Dn Tag 1
```

```
Config:
```

```
Number is 45111
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Pool 1    has this DN configured for line 1
```

```
Dn Tag 2
```

```
Config:
```

```
Number is 45112
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Pool 2    has this DN configured for line 1
```

```
Dn Tag 3
```

```
Config:
```

```
Number is 45113
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Pool 3    has this DN configured for line 1, 2
```

```
Dn Tag 4
```

```
Config:
```

```
Dn Tag 7
```

```
Config:
```

```
Number is 451110
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Pool 1    has this DN configured for line 4
```

```
Dn Tag 8
```

```
Config:
```

```
Pool 1    has this DN configured for line 3
```

```
VOICE REGISTER POOL
```

```
===================
```

```
Pool Tag 1
```

```
Config:
```

```
Mac address is 001B.535C.D410
```

```
Number list 1 : DN 1
```

```
Number list 3 : DN 8
```

```
Number list 4 : DN 7
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
kpml signal is disabled
```

```
Lpcor Type is none
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 2
```

```
Config:
```

```
Mac address is 0015.C68E.6D13
```

```
Number list 1 : DN 2
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
kpml signal is disabled
```

```
Lpcor Type is none
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 3
```

```
Config:
```

```
Mac address is 0021.5553.8998
```

```
Number list 1 : DN 3
```

```
Number list 2 : DN 3
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
kpml signal is enabled
```

```
Lpcor Type is none
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

Cisco Unified CME

The following is an example of show voice register all command :

```
Router# show voice register all
```

```
1) show voice register all
```

```
VOICE REGISTER GLOBAL
```

```
=====================
```

```
CONFIG [Version=8.1]
```

```
========================
```

```
Version 8.1
```

```
Mode is cme
```

```
Max-pool is 10
```

```
Max-dn is 10
```

```
Outbound-proxy is enabled and will use global configured value
```

```
Security Policy: DEVICE-DEFAULT
```

```
Source-address is 8.3.3.5 port 5060
```

```
Time-format is 12
```

```
Date-format is M/D/Y
```

```
Time-zone is 5
```

```
Hold-alert is disabled
```

```
Mwi stutter is disabled
```

```
Mwi registration for full E.164 is disabled
```

```
Forwarding local is enabled
```

```
Privacy is enabled
```

```
Privacy-on-hold is disabled
```

```
Dst auto adjust is enabled
```

```
start at Apr week 1 day Sun time 02:00
```

```
stop  at Oct week 8 day Sun time 02:00
```

```
Max redirect number is 5
```

```
IP QoS DSCP:
```

```
ef (the MS 6 bits, 46, in ToS, 0xB8) for media
```

```
cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
```

```
af41 (the MS 6 bits, 34, in ToS, 0x88) for video
```

```
default (the MS 6 bits, 0, in ToS, 0x0) for service
```

```
Telnet Level: 0
```

```
Tftp path is flash:
```

```
Generate text file is disabled
```

```
Tftp files are created, current syncinfo 0001140473454008
```

```
OS79XX.TXT is not created
```

```
timeout interdigit 10
```

```
network-locale[0] US    (This is the default network locale for this box)
```

```
network-locale[1] US
```

```
network-locale[2] US
```

```
network-locale[3] US
```

```
network-locale[4] US
```

```
user-locale[0] US    (This is the default user locale for this box)
```

```
user-locale[1] US
```

```
user-locale[2] US
```

```
user-locale[3] US
```

```
user-locale[4] US   Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
VOICE REGISTER DN
```

```
=================
```

```
Dn Tag 1
```

```
Config:
```

```
Number is 45111
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
Pool 1    has this DN configured for line 1
```

```
Dn Tag 2
```

```
Config:
```

```
Number is 45112
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
call-forward b2bua noan 999 timeout 8
```

```
after-hour exempt
```

```
Pool 2    has this DN configured for line 1
```

```
Pool 7    has this DN configured for line 1
```

```
Dn Tag 3
```

```
Config:
```

```
Number is 45113
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
call-forward b2bua all 87687
```

```
Pool 3    has this DN configured for line 1, 2
```

```
Dn Tag 4
```

```
Config:
```

```
Auto answer is disabled
```

```
Dn Tag 7
```

```
Config:
```

```
Number is 451110
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
after-hour exempt
```

```
Pool 1    has this DN configured for line 4
```

```
Dn Tag 8
```

```
Config:
```

```
Auto answer is disabled
```

```
call-forward b2bua all 678
```

```
after-hour exempt
```

```
Pool 1    has this DN configured for line 3
```

```
VOICE REGISTER TEMPLATE
```

```
=======================
```

```
Temp Tag 1
```

```
Config:
```

```
Attended Transfer is enabled
```

```
Blind Transfer is enabled
```

```
Semi-attended Transfer is enabled
```

```
Conference is enabled
```

```
Caller-ID block is disabled
```

```
DnD control is enabled
```

```
Anonymous call block is disabled
```

```
Dialplan Tag is 1
```

```
softkey connected  Confrn
```

```
Lpcor type none
```

```
Pool 4 has this template configured
```

```
VOICE REGISTER DIALPLAN
```

```
=======================
```

```
Dialplan Tag 1
```

```
Config:
```

```
Type is 7905-7912
```

```
Template 1 has this dialplan configured
```

```
Pool 4 has this dialplan configured
```

```
VOICE REGISTER POOL
```

```
===================
```

```
Pool Tag 1
```

```
Config:
```

```
Mac address is 001B.535C.D410
```

```
Type is 7960
```

```
Number list 1 : DN 1
```

```
Number list 3 : DN 8
```

```
Number list 4 : DN 7
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
Call Waiting is enabled
```

```
DnD is disabled
```

```
Busy trigger per button value is 0
```

```
call-forward phone all is 4566
```

```
call-forward b2bua all 4555
```

```
keep-conference is enabled
```

```
Lpcor Type is none
```

```
Transport type is udp
```

```
service-control mechanism is not supported
```

```
Privacy feature is not configured.
```

```
Privacy button is disabled
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 2
```

```
Config:
```

```
Mac address is 0015.C68E.6D13
```

```
Type is 7960
```

```
Number list 1 : DN 2
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
Call Waiting is enabled
```

```
DnD is disabled
```

```
Busy trigger per button value is 0
```

```
call-forward phone noan is 9886, timeout 98
```

```
keep-conference is enabled
```

```
username pool2 password lab
```

```
Lpcor Type is none
```

```
Transport type is udp
```

```
service-control mechanism is not supported
```

```
Privacy feature is not configured.
```

```
Privacy button is disabled
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 3
```

```
Config:
```

```
Mac address is 0021.5553.8998
```

```
Type is 7975
```

```
Number list 1 : DN 3
```

```
Number list 2 : DN 3
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
Call Waiting is enabled
```

```
DnD is enabled
```

```
Busy trigger per button value is 0
```

```
call-forward phone all is 45112
```

```
call-forward b2bua all 45111
```

```
after-hour exempt
```

```
keep-conference is enabled
```

```
kpml signal is enabled
```

```
Lpcor Type is none
```

```
Transport type is udp
```

```
service-control mechanism is not supported
```

```
Privacy feature is not configured.
```

```
Privacy button is disabled
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 4
```

```
Config:
```

```
Mac address is 8989.9867.8769
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
Call Waiting is enabled
```

```
DnD is disabled
```

```
Busy trigger per button value is 0
```

```
keep-conference is enabled
```

```
template is 1
```

```
Lpcor Type is none
```

```
Transport type is udp
```

```
service-control mechanism is not supported
```

```
Privacy feature is not configured.
```

```
Privacy button is disabled
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

```
Pool Tag 7
```

```
Config:
```

```
Mac address is 0018.BAC8.D2B1
```

```
Number list 1 : DN 2
```

```
Proxy Ip address is 0.0.0.0
```

```
DTMF Relay is disabled
```

```
Call Waiting is enabled
```

```
DnD is disabled
```

```
Busy trigger per button value is 0
```

```
keep-conference is enabled
```

```
Lpcor Type is none
```

```
Transport type is udp
```

```
service-control mechanism is not supported
```

```
Privacy feature is not configured.
```

```
Privacy button is disabled
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

```
Dialpeers created:
```

```
Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

Table 3 describes the significant fields shown in this output.

Table 3 show voice register all Field Descriptions

Field

Description

Pool Tag

Used with the all and pool keywords. Shows the assigned tag number of the current pool.

Config

Used with the all and pool keywords. Shows the voice register pool.

Network address and Mask

Used with the all and pool keywords. Shows network address and mask information if the id command is configured.

Number list, Pattern, and Preference

Used with the all and pool keywords. Shows the number command configuration.

Proxy IP address

Used with the all and pool keywords. Shows the proxy command configuration.

Default preference

Used with the all and pool keywords. Shows the default preference value of this pool.

Incoming called number

Used with the all and pool keywords. Shows the incoming called-number command configuration.

Translate outgoing called tag

Used with the all and pool keywords. Shows the translate-outgoing command configuration.

Class of Restriction List Tag

Used with the all and pool keywords. Shows the COR tag.

Incoming corlist name

Used with the all and pool keywords. Shows the cor command configuration.

Application

Used with the all and pool keywords. Shows the application command configuration for this pool.

Dialpeers created:

Used with the all and pool keywords. What follows is a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here.

Statistics

Used with the all , pool , and statistics keywords. Shows the registration statistics for this pool.

Active registrations

Used with the all , pool , and statistics keywords. Shows the current active registrations.

Total Registration Statistics

Used with the all , pool , and statistics keywords. Shows the total registration statistics for this pool.

Registration requests

Used with the all , pool , and statistics keywords. Shows the incoming registration requests.

Registration success

Used with the all , pool , and statistics keywords. Shows the successful registrations.

Registration failed

Used with the all , pool , and statistics keywords. Shows the failed registrations.

unRegister requests

Used with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests.

unRegister success

Used with the all , pool , and statistics keywords. Reports the number of successful unregisters.

unRegister failed

Used with the all , pool , and statistics keywords. Reports the number of failed unregisters.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register dial-peers

To display details of all dynamically created VoIP dial peers associated with the Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) or Cisco Unified CallManager Express (Cisco Unified CME) register event, use the show voice register dial-peers command in privileged EXEC mode.

show voice register dial-peers [pool tag ]

### Syntax Description

pool tag

Number of entries in attempted registrations table. Size range from 0 to 50.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1

This command was modified. Pool tag keyword- argument was added. Command output display was also modified to display dial-peers specific to a pool.

### Usage Guidelines

Use this command to display the dial-peers associated with a pool. To display the dynamic dial-peers associated with a specific pool, use the pool keyword followed by the pool tag. When using the pool keyword, you must specify the pool tag.

### Examples

Cisco Unified CME adn Cisco Unified SIP SRST

The following is a sample output from this command displaying all dial-peers:

Router# show voice register dial-peers

Dial-peers for Pool 1

dial-peer voice 40001 voip

destination-pattern 45111

session target ipv4:8.3.3.111:5060

session protocol sipv2

call-fwd-all 4555

after-hours-exempt FALSE

dial-peer voice 40002 voip

destination-pattern 45113

session target ipv4:8.33.33.111:5060

session protocol sipv2

after-hours-exempt FALSE

Dial-peers for Pool 2

dial-peer voice 40003 voip

destination-pattern 45112

session target ipv4:8.33.33.112:5060

session protocol sipv2

call-fwd-noan-timeou 8

call-fwd-noan 999

after-hours-exempt TRUE

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying all statistical information related to pool 1:

```
Router# show voice register dial-peers pool 1
```

Dial-peers for Pool 1:

dial-peer voice 40004 voip

destination-pattern 1000

redirect ip2ip

session target ipv4:9.13.18.40:19633

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

dial-peer voice 40001 voip

destination-pattern 2000

redirect ip2ip

session target ipv4:9.13.18.40:19634

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register dn

To display all configuration information associated with a specific voice register dn, use the show voice register dn command in privileged EXEC mode.

show voice register dn { tag | all}

### Syntax Description

tag

Tag number of the voice register dn for which to display information. Range is 1 to 750.

all

(Optional) Displays configuration information associated with all voice register dns defined in a system.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was introduced.

15.1(2)T

Cisco CME 8.1 and Cisco SIP SRST 8.1

This command was modified.The display output now shows pools that have DNs configured under them. All keyword was added to show configuration information for all voice register dns defined in system.

### Usage Guidelines

In Cisco Unified CME 8.1 and Cisco Unified SIP SRST 8.1, the show voice register dn command displays the pools that have the DNs configured under them. When used with all keyword, the show voice register dn command displays configuration information for all the DNs defined in a system.

### Examples

Cisco Unified SIP CME

The following is a sample output from this command:

Router# show voice register dn 1

Dn Tag 1

Config:

Number is 11

Preference is 10

Huntstop is enabled

Translation-profile incoming saaa

Allow watch is enabled

Pool 1 has this DN configured for line 1

Cisco Unified SIP SRST

The following is a sample output from this command:

Router# show voice register dn 2

Dn Tag 1

Config:

Number is 11

Preference is 10

Huntstop is enabled

Translation-profile incoming saaa

Allow watch is enabled

Pool 1 has this DN configured for line 1

Cisco Unified SIP SRST

The following is a sample output from this command displaying information for all the dns:

```
Dn Tag 1
```

```
Config:
```

```
Number is 11
```

```
Preference is 10
```

```
Huntstop is enabled
```

```
Translation-profile incoming saaa
```

```
Allow watch is enabled
```

```
Pool 1    has this DN configured for line 1
```

```
Dn Tag 2
```

```
Config:
```

```
Number is 12
```

```
Preference is 1
```

```
Huntstop is enabled
```

```
Allow watch is enabled
```

```
Pool 2    has this DN configured for line 1, 2
```

Cisco Unified SIP CME

The following is a sample output from this command displaying information for all the dns:

```
Router# show voice register dn all
```

```
Dn Tag 1
```

```
Config:
```

```
Number is 45111
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
Dn Tag 2
```

```
Config:
```

```
Number is 45112
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
call-forward b2bua noan 999 timeout 8
```

```
after-hour exempt
```

```
Pool 2    has this DN configured for line 1
```

```
Pool 7    has this DN configured for line 1
```

```
Dn Tag 3
```

```
Config:
```

```
Number is 45113
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
call-forward b2bua all 87687
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
call-forward b2bua all 87687
```

```
Pool 1    has this DN configured for line 1
```

```
Pool 3    has this DN configured for line 1, 2
```

```
Dn Tag 4
```

```
Config:
```

```
Auto answer is disabled
```

```
Dn Tag 7
```

```
Config:
```

```
Number is 451110
```

```
Preference is 0
```

```
Huntstop is disabled
```

```
Auto answer is disabled
```

```
after-hour exempt
```

```
Pool 1    has this DN configured for line 4
```

```
Dn Tag 8
```

```
Config:
```

```
Auto answer is disabled
```

```
call-forward b2bua all 678
```

```
after-hour exempt
```

```
Pool 1    has this DN configured for line 3
```

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 4 show voice register dn Field Descriptions

Field

Description

Auto answer

Status of auto-answer feature defined with the auto-answer command.

Config

List of configuration options defined for this voice register dn.

Dn Tag

Tag number of the requested voice register dn.

Huntstop

Status of huntstop behavior defined with the huntstop command.

Number

Telephone or extension number set with the number command in voice register dn configuration mode.

Preference

Preference order set with the preference command in voice register dn configuration mode.

### Related Commands

Command

Description

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register dn all

Displays information associated with all the dns configured in a system.

voice register dn

Enters voice register dn configuration mode to define an extension for a SIP phone line.

## show voice register global

To display all global configuration parameters associated with SIP phones, use the show voice register global command in privileged EXEC mode.

show voice register global

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

15.0(1)XA

Cisco SIP SRST 8.0

This command was updated to display the signaling transport protocol.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1

This command was modified.The output display now includes global statistics.

### Examples

Cisco Unified CME

The following is sample output from this command:

```
Router# show voice register global
```

```
CONFIG [Version=8.1]
```

```
========================
```

```
Version 8.1
```

```
Mode is cme
```

```
Max-pool is 10
```

```
Max-dn is 10
```

```
Outbound-proxy is enabled and will use global configured value
```

```
Security Policy: DEVICE-DEFAULT
```

```
Source-address is 8.3.3.5 port 5060
```

```
Time-format is 12
```

```
Date-format is M/D/Y
```

```
Time-zone is 5
```

```
Hold-alert is disabled
```

```
Mwi stutter is disabled
```

```
Mwi registration for full E.164 is disabled
```

```
Forwarding local is enabled
```

```
Privacy is enabled
```

```
Privacy-on-hold is disabled
```

```
Dst auto adjust is enabled
```

```
start at Apr week 1 day Sun time 02:00
```

```
stop  at Oct week 8 day Sun time 02:00
```

```
Max redirect number is 5
```

```
IP QoS DSCP:
```

```
ef (the MS 6 bits, 46, in ToS, 0xB8) for media
```

```
cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
```

```
af41 (the MS 6 bits, 34, in ToS, 0x88) for video
```

```
default (the MS 6 bits, 0, in ToS, 0x0) for service
```

```
Telnet Level: 0
```

```
Tftp path is flash:
```

```
Generate text file is disabled
```

```
Tftp files are created, current syncinfo 0001140473454008
```

```
OS79XX.TXT is not created
```

```
timeout interdigit 10
```

```
network-locale[0] US    (This is the default network locale for this box)
```

```
network-locale[1] US
```

```
network-locale[2] US
```

```
network-locale[3] US
```

```
network-locale[4] US
```

```
user-locale[0] US    (This is the default user locale for this box)
```

```
user-locale[1] US
```

```
user-locale[2] US
```

```
user-locale[3] US
```

```
user-locale[4] US   Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

Cisco Unified SIP SRST

```
Router# show voice register global
```

```
CONFIG [Version=8.1]
```

```
========================
```

```
Version 8.1
```

```
Mode is srst
```

```
Max-pool is 10
```

```
Max-dn is 10
```

```
Outbound-proxy is enabled and will use global configured value
```

```
Security Policy: DEVICE-DEFAULT
```

```
timeout interdigit 10
```

```
network-locale[0] US    (This is the default network locale for this box)
```

```
network-locale[1] US
```

```
network-locale[2] US
```

```
network-locale[3] US
```

```
network-locale[4] US
```

```
user-locale[0] US    (This is the default user locale for this box)
```

```
user-locale[1] US
```

```
user-locale[2] US
```

```
user-locale[3] US
```

```
user-locale[4] US   Active registrations  : 0
```

```
Total SIP phones registered: 0
```

```
Total Registration Statistics
```

```
Registration requests  : 0
```

```
Registration success   : 0
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   :
```

```
Last unregister request time :
```

```
Register success time        :
```

```
Unregister success time      :
```

Table 5 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 5 show voice register global Field Descriptions

Field

Description

Date-format

Value of date-format command.

DST auto adjust

Setting of dst auto-adjust command.

Forwarding local

Setting of forwarding local command.

Generate text file

Setting of text file command.

Hold-alert

Setting of hold-alert command.

Load

Value of load command.

Max-dn

Reports the maximum number of SIP voice register directory numbers (dns) supported by the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with the max-dn command. The maximum possible number is platform-dependent.

Max-pool

Reports the maximum number of SIP voice register pools supported by the Cisco Unified SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent.

Max redirect number

Maximum number of redirects set with the max-redirect command.

Mode

Reports the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST.

MWI registration

Setting of mwi command.

MWI stutter

Setting of mwi stutter command.

Time-format

Value of time-format command.

Time-zone

Number of the timezone selected with the timezone command.

TFTP path

Directory location of provisioning files for SIP phones that is specified with the tftp-path command.

Version

Reports the Cisco Unified SIP SRST or Cisco Unified CME version number.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event.

voice register global

Enters voice register global configuration mode in order to set global parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco Unified SIP SRST environment.

## show voice register pool

To display all configuration information associated with a specific voice register pool, use the show voice register pool command in privileged EXEC mode.

show voice register pool { tag | all} [brief]

### Syntax Description

tag

Tag number of the voice register pool for which to display information. The maximum number of pools is version and platform dependent. Type ? to display a list of values.

all

Displays information for all pools configured in a system.

brief

(Optional) Displays brief information for a specific voice register pool.

## Command Modes

Privileged EXEC (#)

### Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST

This command was introduced.

12.3(4)T

Cisco SIP SRST

This command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco Unified CME.

12.4(15)XY

Cisco Unified CME  4.2(1) Cisco Unified SIP SRST 4.2(1)

Emergency response location (ERL) information displays in the output.

12.4(20)T

Cisco Unified CME  7.0 Cisco Unified SIP SRST 7.0

This command was integrated into Cisco IOS Release 12.4(20)T.

15.0(1)XA

Cisco Unified CME 8.0

This command was modified. Logical partitioning class of restriction (LPCOR) information was added to the output.

15.1(2)T

Cisco Unified CME 8.1

This command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the output.

### Examples

Cisco Unified CME Example 1:

The following is a sample output from this command displaying information for voice register pool 1:

F

Router# show voice register pool 1

Pool Tag 1

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

call-fwd-all 4555

after-hours-exempt FALSE

Statistics:

Active registrations : 1

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 1

Registration success : 1

Registration failed : 0

unRegister requests : 0

unRegister success : 0

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : *11:40:32.263 UTC Wed Oct 14 2009

Last unregister request time :

Register success time : *11:40:32.267 UTC Wed Oct 14 2009

Unregister success time :

Cisco Unified CME Example 2 :

The following is a sample output from this command displaying information for all the voice register pools:

Router# show voice register pool all

Pool Tag 1

Config:

Mac address is 001B.535C.D410

Type is 7960

Number list 1 : DN 3

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

template is 3

Lpcor Type is none

Transport type is udp

service-control mechanism is supported

registration Call ID is 001b535c-d4100002-6d241f50-0fac9bc9@8.3.3.111

Privacy feature is not configured.

Privacy button is disabled

active primary line is: 45111

contact IP address: 8.3.3.111 port 5060

Reason for unregistered state:

No registration request since last reboot/unregister

Dialpeers created:

Dial-peers for Pool 1:

Statistics:

Active registrations : 0

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 2

Registration success : 2

Registration failed : 0

unRegister requests : 1

unRegister success : 1

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : *12:10:37.259 UTC Tue Oct 13 2009

Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009

Register success time : *12:10:37.263 UTC Tue Oct 13 2009

Unregister success time : *11:56:22.182 UTC Tue Oct 13 2009

Pool Tag 2

Config:

Mac address is 0015.C68E.6D13

Type is 7960

Number list 1 : DN 2

Proxy Ip address is 0.0.0.0

Current Phone load version is Cisco-CP7960G/8.0

DTMF Relay is disabled

Call Waiting is enabled

DnD is disabled

Busy trigger per button value is 0

call-forward phone noan is 9886, timeout 98

keep-conference is enabled

username pool2 password lab

Lpcor Type is none

Transport type is udp

service-control mechanism is supported

registration Call ID is 0015c68e-6d130002-24aebd5d-43d8d548@8.33.33.112

Privacy feature is not configured.

Privacy button is disabled

active primary line is: 45112

contact IP address: 8.33.33.112 port 5060

Dialpeers created:

Dial-peers for Pool 2:

dial-peer voice 40002 voip

destination-pattern 45112

session target ipv4:8.33.33.112:5060

session protocol sipv2

call-fwd-noan-timeou 8

call-fwd-noan 999

after-hours-exempt TRUE

Statistics:

Active registrations : 1

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 1

Registration success : 1

Registration failed : 0

unRegister requests : 0

unRegister success : 0

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : *11:56:21.407 UTC Tue Oct 13 2009

Last unregister request time :

Register success time : *11:56:21.411 UTC Tue Oct 13 2009

Unregister success time :

Cisco Unified CME Example 3:

The following is a sample output from this command displaying brief information for the voice register pools:

Router# show voice register pool 1 brief

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

4 7 451110 UNREGISTERED

Cisco Unified CME Example 4:

The following is a sample output from this command displaying brief information for all the voice register pools:

Router# show voice register pool all brief

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

4 7 451110 UNREGISTERED

2 0015.C68E.6D13 1 2 45112 UNREGISTERED

3 0021.5553.8998 1 3 45113 UNREGISTERED

2 3 45113 UNREGISTERED

4 8989.9867.8769 UNREGISTERED

7 0018.BAC8.D2B1 1 2 45112 UNREGISTERED

10 9.13.18.40 9.13.18.40 1 1 1000 REGISTERED

Cisco Unified SIP SRST Example 1:

The following is a sample output from this command displaying all information for voice register pool 1:

Router# show voice register pool 1

Pool Tag 1

Config:

Mac address is 0019.06FC.A377

Number list 1 : DN 1

Number list 2 : DN 2

Proxy Ip address is 0.0.0.0

DTMF Relay is disabled

kpml signal is enabled

Lpcor Type is none

Reason for unregistered state:

No registration request since last reboot/unregister

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

Attempts to register

after last unregister : 0

Last register request time :

Last unregister request time :

Register success time :

Unregister success time :

Cisco Unified SIP SRST Example 2:

The following is a sample output from this command displaying all information for voice register pool all:

Router# show voice register pool all

Pool Tag 1

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

codec g711ulaw bytes 160

after-hours-exempt FALSE

dial-peer voice 40001 voip

destination-pattern 2000

redirect ip2ip

session target ipv4:9.13.18.40:19634

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

Statistics:

Active registrations : 4

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 4

Registration success : 4

Registration failed : 0

unRegister requests : 0

unRegister success : 0

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : .05:22:55.604 UTC Tue Oct 6 2009

Last unregister request time :

Register success time : .05:22:55.604 UTC Tue Oct 6 2009

Unregister success time :

Pool Tag 2

Config:

Mac address is 0019.06FC.A377

Number list 1 : DN 1

Number list 2 : DN 2

Proxy Ip address is 0.0.0.0

DTMF Relay is disabled

kpml signal is enabled

Lpcor Type is none

Reason for unregistered state:

No registration request since last reboot/unregister

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

Attempts to register

after last unregister : 0

Last register request time :

Last unregister request time :

Register success time :

Unregister success time :

Cisco Unified SIP SRST Example 3:

The following is a sample output from this command displaying all information for voice register pool all brief:

Router# show voice register pool all brief

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

3 8 UNREGISTERED

4 7 451110 UNREGISTERED

2 8.33.33.112 8.3.3.112 1 2 45112 REGISTERED

3 8.3.0.0 8.3.3.116 1 3 45113 REGISTERED

Cisco Unified SIP SRST Example 4:

The following is a sample output from this command displaying all information for voice register pool brief:

Router# show voice register pool 2 brief

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

2 9.13.18.40 9.13.18.40 1 1 1000 REGISTERED

2 2 2000 REGISTERED

3 3 3000 REGISTERED

Voice class stun usage Example 5:

The following is sample output from this command displaying voice-class stun-usage information for voice register pool 51:

Router# show voice register pool 51

Pool Tag 51

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

Active registrations : 0

Total SIP phones registered: 0

Total Registration Statistics

Registration requests : 2

Registration success : 2

Registration failed : 0

unRegister requests : 2

unRegister success : 2

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : 13:43:27.839 IST Tue Apr 20 2010

Table 6 contains descriptions of significant fields shown in the Cisco Unified CME and Cisco Unified SIP SRST output, listed in alphabetical order.

Table 6 show voice register pool Field Descriptions

Field

Description

Active registrations

Shows the current active registrations. Used with the all , pool , and statistics keywords.

Application

Shows the application command configuration for this pool. Used with the all and pool keywords.

Current phone-load

Shows the current version of the phone load.

Call Waiting

Setting of call-waiting command.

Config:

Shows the voice register pool. Used with the all and pool keywords.

Class of Restriction List Tag

Shows the COR tag. Used with the all and pool keywords.

Default preference

Shows the default preference value of this pool. Used with the all and pool keywords.

Dialpeers created:

Results in a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here. Used with the all and pool keywords.

DnD

Setting of dnd-control command.

DTMF Relay

Setting of dtmf-relay command.

Emergency response location

The ephone's emergency response location to which an emergency response team is dispatched when an emergency call is made.

Incoming called number

Shows the incoming called-number command configuration. Used with the all and pool keywords.

Incoming corlist name

Shows the cor command configuration. Used with the all and pool keywords.

keep-conference

Status of keep-conference command.

Lpcor Incoming

Setting of the lpcor incoming command.

Lpcor Outgoing

Setting of the lpcor outgoing command.

Lpcor Type

Setting of the lpcor type command.

Mac address

MAC address of this SIP phone as defined by using the id command.

Network address and Mask

Shows network address and mask information if the id command is configured. Used with the all and pool keywords.

Number list, Pattern, and Preference

Shows the number (voice register pool) command configuration. Used with the all and pool keywords.

Pool Tag

Shows the assigned tag number of the current pool. Used with the all and pool keywords.

Previous phone-load

Shows the version of the previous phone-load.

Proxy IP address

Shows the proxy command configuration; that is, the IP address of the external SIP server. Used with the all and pool keywords.

Registration failed

Shows the failed registrations. Used with the all , pool , and statistics keywords.

Registration requests

Shows the incoming registration requests. Used with the all , pool , and statistics keywords.

Registration success

Shows the successful registrations. Used with the all , pool , and statistics keywords.

Statistics:

Shows the registration statistics for this pool. Used with the all , pool , and statistics keywords.

statistics time-stamps

Shows the registration statistics for this pool with specific time-stamps.

Template

Template-tag number for template that is applied to this SIP phone.

Translate outgoing called tag

Shows the translate-outgoing command configuration. Used with the all and pool keywords.

Total Registration Statistics

Shows the total registration statistics for this pool. Used with the all , pool , and statistics keywords.

Type

Phone type identified for this SIP phone using the type command.

unRegister requests

Shows the incoming unregister/registration expiry requests. Used with the all , pool , and statistics keywords.

unRegister success

Reports the number of successful unregisters. Used with the all , pool , and statistics keywords.

unRegister failed

Reports the number of failed unregisters. Used with the all , pool , and statistics keywords.

Username Password

Values within the authentication credential.

Voice class stun usage

Displays the configured voice-class stun-usage information.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints registered with the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register dial-peer

Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified CME or Cisco Unified SIP SRST register event.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool mac

To display the details of voice register pool associated with a specific phone type, use the show voice register pool mac command in privileged EXEC mode.

show voice register pool mac H.H.H

### Syntax Description

H.H.H

MAC address of the SIP phone attempting to register.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone with the mac address H.H.H. The command displays only the pools that are configured with an ID as mac.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is sample output from this command displaying all statistical information:

Router# show voice register pool mac 001B.535C.D410

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

4 7 451110 UNREGISTERED

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 7 show voice register pool mac field descriptions

Field

Description

DN

Voice register DN tag of the line.

ID

Phone identification (ID) address.

IP Address

IP address of the SIP phone.

LN

Line number of the telephone number.

Number

Number of the phones that have a mac address.

Pool

Tag ID of the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register pool ip

To display the details of a SIP phone with a specific IP address, use the show voice register pool ip command in privileged EXEC mode.

show voice register pool ip ip-address

### Syntax Description

ip-address

IPv4 address of the SIP phone .

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of a phone with a specific IP-address. When the pool ID is configured as a mac address or an IP address the registered pools contain the IP address information. The pool information is displayed if the IP addresses match.

When the pool ID is IP and the pool is unregistered, IP address configured under pool is compared with the input IP. When the pool ID is network contact, the IP address of each phone that is registered is compared with the input IP address.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is sample output from this command displaying all statistical information:

```
Router# show voice register pool ip 8.3.3.111
```

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

4 7 451110 UNREGISTERED

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 8 show voice register pool ip field descriptions

Field

Description

DN

Voice register DN tag of the line.

ID

Phone identification (ID) address.

IP Address

IP address of the SIP phone.

LN

Line number of the telephone number.

Number

Number of the phones that have a mac address.

Pool

Tag ID of the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register pool network

To display the details of a phone with a specific network address, use the show voice register pool network command in privileged EXEC mode.

show voice register pool network network-address

### Syntax Description

network-address

Network address of the SIP phone.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of pools that have network ID configured and whose network address matches the specific network address provided by the user.

### Examples

The following is sample output from this command displaying all statistical information:

```
Router# show voice register pool network 78.89.0.0
```

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

7 78.89.0.0 1 1 6576 UNREGISTERED

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 9 show voice register pool network field descriptions

Field

Description

DN

Directory number of the phone.

ID

Phone identification (ID) address.

IP Address

IP address and port number of the phones

LN

Line number of the phone.

Number

Number of the phone that have network address.

Pool

Shows the current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register pool ip

Displays the voice register pool details of a phone with a specific IP address.

## show voice register pool telephone-number

To display the details of a phone line with a specific telephone-number, use the show voice register pool telephone-number command in privileged EXEC mode.

show voice register pool telephone-number number

### Syntax Description

number

Number identifying a specific phone.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone line with the specified telephone-number. If the line is registered, the contact ip address will be displayed. When the phone line is not registered and the pool ID type is network IP, the IP address is not displayed. When the phone line is not registered but some other line is registered for the same pool with MAC or IP address, then the IP address is displayed.

### Examples

Cisco Unified CME

The following is a sample output from this command displaying all statistical information:

```
Router# show voice register pool telephone number 45112
```

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

2 0015.C68E.6D13 1 2 45112 UNREGISTERED

7 0018.BAC8.D2B1 1 2 45112 UNREGISTERED

Cisco Unified SRST

Router# show voice register pool telephone-number 1000

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 9.13.18.40 9.13.18.40 1 1 1000 REGISTERED

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 10 show voice register pool telephone number field descriptions

Field

Description

DN

Directory number of the phone.

ID

Phone identification (ID) address.

IP Address

IP address and port number of the phones

LN

Line number of the phone.

Number

Number of the phones.

Pool

Shows the current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register pool detail all

Displays the details of all the pools defined in the system.

## show voice register pool after-hour-exempt

To display the details of a phone that has after-hour-exempt enabled on it, use the show voice register after-hour-exempt command in privileged EXEC mode.

show voice register after-hour-exempt

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of a phone that has after-hour-exempt enabled. Individual phones can be exempted from call blocking using the after-hour exempt.

### Examples

Cisco Unified CME

The following is a sample output from this command displaying information for phones with after after-hour-exempt:

```
Router# show voice register pool after-hour-exempt
```

```
Pool ID              IP Address      Ln DN  Number               State
```

```
==== =============== =============== == === ==================== ============
```

```
1    001B.535C.D410  8.3.3.111       3  8                        UNREGISTERED
```

```
4  7   451110               UNREGISTERED
```

```
2    0015.C68E.6D13                  1  2   45112                UNREGISTERED
```

```
3    0021.5553.8998                  1  3   45113                UNREGISTERED
```

```
2  3   45113                UNREGISTERED
```

```
7    0018.BAC8.D2B1                  1  2   45112                UNREGISTERED
```

Cisco Unified SRST

The following is a sample output from this command displaying information for phones with after after-hour-exempt:

```
Router# show voice register pool after-hour-exempt
```

```
Pool ID              IP Address      Ln DN  Number               State
```

```
==== =============== =============== == === ==================== ============
```

```
1    9.13.18.40      9.13.18.40      1  1   1000                 REGISTERED
```

```
2  2   2000                 REGISTERED
```

```
3  3   3000                 REGISTERED
```

```
4  4   4000                 REGISTERED
```

```
5  5   5000                 UNREGISTERED
```

```
6  6   6000                 UNREGISTERED
```

```
7  7   7000                 UNREGISTERED
```

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 11 show voice register pool after-hour exempt field descriptions

Field

Description

DN

Directory number of the phone.

IP Address/port

IP address and port number of the phones.

LN

Line number of the phone.

Number

Number of the phones that have after-hour exempt enabled.

Pool

Shows the current pool.

State

Registration state.

### Related Commands

Command

Description

after-hour exempt(voice register pool)

Specifies that an IP phone does not have any of its outgoing calls blocked although call blocking is defined.

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool attempted-registrations

To display the details of phones that attempt to register with Cisco Unified CME or Cisco Unified SRST and fail, use the show voice register pool attempted-registrations command in privileged EXEC mode.

show voice register pool attempted-registrations

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phones that attempt to register with Cisco Unified CME or Cisco Unified SRST and fail. If the phone registers successfully after some time, the attempted registration entry will still show up in the attempted-registration table. Use the clear voice register attempted-registrations command to remove the entry from the attempted registration table.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for show voice register pool attempted-registrations:

Router# show voice register pool attempted-registrations

Phones that have attempted registrations and have failed:

MAC address: 001b.535c.d410

IP address : 8.3.3.111

Attempts : 5

Time of first attempt : *10:49:51.542 UTC Wed Oct 14 2009

Time of latest attempt: *10:50:00.886 UTC Wed Oct 14 2009

Reason for failure :

No pool match for the registration request

MAC address: 0015.c68e.6d13

IP address : 8.33.33.112

Attempts : 4

Time of first attempt : *10:49:53.418 UTC Wed Oct 14 2009

Time of latest attempt: *10:50:00.434 UTC Wed Oct 14 2009

Reason for failure :

No pool match for the registration request

MAC address: 0009.43E9.0B35

IP address : 9.13.40.83

Attempts : 1

Time of first attempt : *10:49:57.866 UTC Wed Oct 14 2009

Time of latest attempt: *10:49:57.866 UTC Wed Oct 14 2009

Reason for failure :

No pool match for the registration request

The following is a sample output from this command displaying information for show voice register pool attempted-registrations when none of the phones fail:

Router# show voice register pool attempted-registrations

Phones that have attempted registrations and have failed: NONE

### Related Commands

Command

Description

attempted-registrations size

Allows to set the size of the table that stores information related to SIP phones that attempt to register and fail.

clear voice register attempted-registrations

Clears entries from the attempted-registration table.

## show voice register pool connected

To display the details of SIP phones that are in connected state, use the show voice register pool connected command in privileged EXEC mode.

show voice register pool connected [brief]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are in connected state.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are currently in connected state (in conversation). The output for show voice register pool connected command shows details of both calls originating from the SIP phones and calls made towards SIP phones. When used with brief keyword, the show voice register pool connected command displays a brief detail of phones in connected state.

Cisco Unified CME and Cisco Unified SRST

The following is sample output from this command displaying all statistical information:

Router# show voice register pool connected

Outbound calls from SIP line phones:

Pool tag: 1

==============

MAC Address : 001B.535C.D410

Contact IP : 8.3.3.111

Phone Number : 45111

Remote Number : 45112

Call 2

SIP Call ID : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111

State of the call : STATE_ACTIVE (7)

Substate of the call : SUBSTATE_NONE (0)

Calling Number : 45111

Called Number : 45112

Bit Flags : 0xC0401C 0x100 0x4

CC Call ID : 7

Source IP Address (Sig ): 8.3.3.5

Destn SIP Req Addr:Port : [8.3.3.111]:5060

Destn SIP Resp Addr:Port: [8.3.3.111]:50076

Destination Name : 8.3.3.111

Number of Media Streams : 1

Number of Active Streams: 1

RTP Fork Object : 0x0

Media Mode : flow-through

Media Stream 1

State of the stream : STREAM_ACTIVE

Stream Call ID : 7

Stream Type : voice-only (0)

Stream Media Addr Type : 1

Negotiated Codec : g729r8 (20 bytes)

Codec Payload Type : 18

Negotiated Dtmf-relay : inband-voice

Dtmf-relay Payload Type : 0

QoS ID : -1

Local QoS Strength : BestEffort

Negotiated QoS Strength : BestEffort

Negotiated QoS Direction : None

Local QoS Status : None

Media Source IP Addr:Port: [8.3.3.5]:17580

Media Dest IP Addr:Port : [8.3.3.111]:26298

Options-Ping ENABLED:NO ACTIVE:NO

Inbound calls to SIP line phones:

Pool tag: 2

==============

MAC Address : 0015.C68E.6D13

Contact IP : 8.33.33.112

Phone Number : 45112

Remote Number : 45111

Call 3

SIP Call ID : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5

State of the call : STATE_ACTIVE (7)

Substate of the call : SUBSTATE_NONE (0)

Calling Number : 45111

Called Number : 45112

Bit Flags : 0xC04018 0x100 0x80

CC Call ID : 8

Source IP Address (Sig ): 8.3.3.5

Destn SIP Req Addr:Port : [8.33.33.112]:5060

Destn SIP Resp Addr:Port: [8.33.33.112]:5060

Destination Name : 8.33.33.112

Number of Media Streams : 1

Number of Active Streams: 1

RTP Fork Object : 0x0

Media Mode : flow-through

Media Stream 1

State of the stream : STREAM_ACTIVE

Stream Call ID : 8

Stream Type : voice-only (0)

Stream Media Addr Type : 1

Negotiated Codec : g729r8 (20 bytes)

Codec Payload Type : 18

Negotiated Dtmf-relay : inband-voice

Dtmf-relay Payload Type : 0

QoS ID : -1

Local QoS Strength : BestEffort

Negotiated QoS Strength : BestEffort

Negotiated QoS Direction : None

Local QoS Status : None

Media Source IP Addr:Port: [8.3.3.5]:16384

Media Dest IP Addr:Port : [8.33.33.112]:30040

The following is sample output from this command displaying brief statistical information:

Router# show voice register pool connected brief

Pool IP Address Number Remote Number

==== =============== ==================== ====================

1 8.3.3.111 45111 45112

Inbound calls to SIP line phones:

Pool IP Address Number Remote Number

==== =============== ==================== ====================

2 8.33.33.112 45112 45111

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register pool on-hold

To display the details of phones that are currently on-hold, use the show voice register pool oh-hold command in privileged EXEC mode.

show voice register pool on-hold [brief]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are currently on-hold.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are currently on-hold. The show voice register pool on-hold command output also displays a field to show if the hold was a locally initiated hold (initiated on the phone) or if the hold was initiated on the remote end. When used with brief keyword, the show voice register pool on-hold command displays a brief information of the phones that are currently put on hold by the remote caller or have put the remote caller on hold. The "Hold-Origin" field specifies the type of the hold, which can be either remote or local. Local indicates that the call is placed on hold by the local phone and remote indicates that call is placed on hold by the remote phone. In case of double-hold, the hold origin will display the value "Local and Remote".

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for phones ringing in a voice register pool:

```
Router# show voice register pool on-hold brief
```

Outbound calls from SIP line phones:

Pool IP Address Number Remote Number Hold Origin

==== =============== ==================== ==================== ==============

1 8.3.3.111 45111 45112 Remote & Local

Inbound calls to SIP line phones:

Pool IP Address Number Remote Number Hold Origin

==== =============== ==================== ==================== ==============

2 8.33.33.112 45112 45111 Remote & Local

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for phones on-hold:

Router# show voice register pool on-hold

Outbound calls from SIP line phones:

Pool tag: 1

==============

MAC Address : 001B.535C.D410

Contact IP : 8.3.3.111

Phone Number : 45111

Remote Number : 45112

Local Hold : CALL HOLD Pressed on SIP Phone

Call 4

SIP Call ID : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111

State of the call : STATE_ACTIVE (7)

Substate of the call : SUBSTATE_NONE (0)

Calling Number : 45111

Called Number : 45112

Bit Flags : 0xC0401C 0x10100 0x4

CC Call ID : 7

Source IP Address (Sig ): 8.3.3.5

Destn SIP Req Addr:Port : [8.3.3.111]:5060

Destn SIP Resp Addr:Port: [8.3.3.111]:50076

Destination Name : 8.3.3.111

Number of Media Streams : 1

Number of Active Streams: 1

RTP Fork Object : 0x0

Media Mode : flow-through

Media Stream 1

State of the stream : STREAM_ACTIVE

Stream Call ID : 7

Stream Type : voice-only (0)

Stream Media Addr Type : 1

Negotiated Codec : g729r8 (20 bytes)

Codec Payload Type : 18

Negotiated Dtmf-relay : inband-voice

Dtmf-relay Payload Type : 0

QoS ID : -1

Local QoS Strength : BestEffort

Negotiated QoS Strength : BestEffort

Negotiated QoS Direction : None

Local QoS Status : None

Media Source IP Addr:Port: [8.3.3.5]:17580

Media Dest IP Addr:Port : [8.3.3.111]:26298

Options-Ping ENABLED:NO ACTIVE:NO

Inbound calls to SIP line phones:

Pool tag: 2

==============

MAC Address : 0015.C68E.6D13

Contact IP : 8.33.33.112

Phone Number : 45112

Remote Number : 45111

Remote Hold : SIP Phone has received CALL HOLD

Call 5

SIP Call ID : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5

State of the call : STATE_ACTIVE (7)

Substate of the call : SUBSTATE_NONE (0)

Calling Number : 45111

Called Number : 45112

Bit Flags : 0xC04018 0x4100 0x80

CC Call ID : 8

Source IP Address (Sig ): 8.3.3.5

Destn SIP Req Addr:Port : [8.33.33.112]:5060

Destn SIP Resp Addr:Port: [8.33.33.112]:5060

Destination Name : 8.33.33.112

Number of Media Streams : 1

Number of Active Streams: 1

RTP Fork Object : 0x0

Media Mode : flow-through

Media Stream 1

State of the stream : STREAM_ACTIVE

Stream Call ID : 8

Stream Type : voice-only (0)

Stream Media Addr Type : 1

Negotiated Codec : g729r8 (20 bytes)

Codec Payload Type : 18

Negotiated Dtmf-relay : inband-voice

Dtmf-relay Payload Type : 0

QoS ID : -1

Local QoS Strength : BestEffort

Negotiated QoS Strength : BestEffort

Negotiated QoS Direction : None

Local QoS Status : None

Media Source IP Addr:Port: [8.3.3.5]:16384

Media Dest IP Addr:Port : [8.33.33.112]:30040

Options-Ping ENABLED:NO ACTIVE:NO

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register pool phone-load

To display the details of phone-loads associated with phones that are registered to Cisco Unified CME, use the show voice register pool phone-load command in privileged EXEC mode.

show voice register pool phone-load

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone-loads associated with phones that are registered with Cisco Unified CME. The phone-load information is taken from the REGISTER message sent by the phone.

### Examples

The following is a sample output from this command displaying information for voice register pool phone-load:

```
Router# show voice register pool phone-load
```

Pool Device Name Current Version Previous Version

==== =========== ================= ===================

1 SEP001B535CD410 Cisco-CP7960G/8.0

### Related Commands

Command

Description

load(voice register global)

Associates a type of Cisco Unified IP phone with a phone firmware file.

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool registered

To display the details of phones that successfully register to Cisco Unified CME, use the show voice register pool registered command in privileged EXEC mode.

show voice register pool registered

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of phones that are successfully registered to Cisco Unified CME and Cisco Unified SRST.

### Examples

Cisco Unified CME

The following is a example displaying information for registered voice register pool:

Router# show voice register pool registered

Pool Tag 1

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

call-fwd-all 4555

after-hours-exempt FALSE

Statistics:

Active registrations : 1

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 1

Registration success : 1

Registration failed : 0

unRegister requests : 0

unRegister success : 0

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : *11:40:32.263 UTC Wed Oct 14 2009

Last unregister request time :

Register success time : *11:40:32.267 UTC Wed Oct 14 2009

Unregister success time :

Cisco Unified SRST

The following is and example displaying information for registered voice register pool:

Router# show voice register pool registered

Pool Tag 1

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

codec g711ulaw bytes 160

after-hours-exempt FALSE

dial-peer voice 40001 voip

destination-pattern 2000

redirect ip2ip

session target ipv4:9.13.18.40:19634

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

dial-peer voice 40002 voip

destination-pattern 3000

redirect ip2ip

session target ipv4:9.13.18.40:19635

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

dial-peer voice 40003 voip

destination-pattern 4000

redirect ip2ip

session target ipv4:9.13.18.40:19636

session protocol sipv2

dtmf-relay rtp-nte sip-notify

digit collect kpml

codec g711ulaw bytes 160

after-hours-exempt FALSE

Statistics:

Active registrations : 4

Total SIP phones registered: 1

Total Registration Statistics

Registration requests : 4

Registration success : 4

Registration failed : 0

unRegister requests : 0

unRegister success : 0

unRegister failed : 0

Attempts to register

after last unregister : 0

Last register request time : .05:22:55.604 UTC Tue Oct 6 2009

Last unregister request time :

Register success time : .05:22:55.604 UTC Tue Oct 6 2009

Unregister success time :

Table 6 contains descriptions of significant fields shown in the Cisco Unified CME and Cisco Unified SIP SRST output, listed in alphabetical order.

Table 12 show voice register pool registered Field Descriptions

Field

Description

Active registrations

Shows the current active registrations. Used with the all , pool , and statistics keywords.

Application

Shows the application command configuration for this pool. Used with the all and pool keywords.

Current phone-load

Shows the current version of the phone load.

Call Waiting

Setting of call-waiting command.

Config:

Shows the voice register pool. Used with the all and pool keywords.

Class of Restriction List Tag

Shows the COR tag. Used with the all and pool keywords.

Default preference

Shows the default preference value of this pool. Used with the all and pool keywords.

Dialpeers created:

Results in a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here. Used with the all and pool keywords.

DnD

Setting of dnd-control command.

DTMF Relay

Setting of dtmf-relay command.

Emergency response location

The ephone's emergency response location to which an emergency response team is dispatched when an emergency call is made.

Incoming called number

Shows the incoming called-number command configuration. Used with the all and pool keywords.

Incoming corlist name

Shows the cor command configuration. Used with the all and pool keywords.

keep-conference

Status of keep-conference command.

Lpcor Incoming

Setting of the lpcor incoming command.

Lpcor Outgoing

Setting of the lpcor outgoing command.

Lpcor Type

Setting of the lpcor type command.

Mac address

MAC address of this SIP phone as defined by using the id command.

Network address and Mask

Shows network address and mask information if the id command is configured. Used with the all and pool keywords.

Number list, Pattern, and Preference

Shows the number (voice register pool) command configuration. Used with the all and pool keywords.

Pool Tag

Shows the assigned tag number of the current pool. Used with the all and pool keywords.

Previous phone-load

Shows the version of the previous phone-load.

Proxy IP address

Shows the proxy command configuration; that is, the IP address of the external SIP server. Used with the all and pool keywords.

Registration failed

Shows the failed registrations. Used with the all , pool , and statistics keywords.

Registration requests

Shows the incoming registration requests. Used with the all , pool , and statistics keywords.

Registration success

Shows the successful registrations. Used with the all , pool , and statistics keywords.

Statistics:

Shows the registration statistics for this pool. Used with the all , pool , and statistics keywords.

statistics time-stamps

Shows the registration statistics for this pool with specific time-stamps.

Template

Template-tag number for template that is applied to this SIP phone.

Translate outgoing called tag

Shows the translate-outgoing command configuration. Used with the all and pool keywords.

Total Registration Statistics

Shows the total registration statistics for this pool. Used with the all , pool , and statistics keywords.

Type

Phone type identified for this SIP phone using the type command.

unRegister requests

Shows the incoming unregister/registration expiry requests. Used with the all , pool , and statistics keywords.

unRegister success

Reports the number of successful unregisters. Used with the all , pool , and statistics keywords.

unRegister failed

Reports the number of failed unregisters. Used with the all , pool , and statistics keywords.

Username Password

Values within the authentication credential.

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register pool unregistered

Displays the details of voice register pools that do not have any phones registered.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool remote

To display the details of phones that are at a remote location, use the show voice register pool remote command in privileged EXEC mode.

show voice register pool remote

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified  SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phones that are at remote location and do not have an address resolution protocol (ARP) entry.If the pool id is MAC or IP, the entire pool detail is displayed in a brief format. If the pool id is network, only the line details with remote contact IP address are displayed. In Cisco Unified  SRST, if the pool id is IP and if the pool is not registered, the configured IP is checked to see if it is a remote IP.

### Examples

Cisco Unified CME

The following is a sample output from this command displaying information for remote phones:

```
Router# show voice register pool remote
```

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.3.3.111 1 1 45111 REGISTERED

3 8 UNREGISTERED

4 7 451110 UNREGISTERED

2 8.3.3.112 1 2 45112 REGISTERED

3 8.3.0.0 1 3 45113 REGISTERED

Cisco Unified SRST

The following is a sample output from this command displaying information for remote phones:

Router# show voice register pool remote

Pool ID IP Address Ln DN Number State

==== =============== =============== == === ==================== ============

1 001B.535C.D410 8.33.33.111 1 1 45111 REGISTERED

3 8 UNREGISTERED

4 7 451110 UNREGISTERED

2 8.33.33.112 8.33.33.112 1 2 45112 REGISTERED

3 8.3.0.0 8.3.44.116 1 3 45113 REGISTERED

Table 7 contains descriptions of significant fields shown in this output, listed in alphabetical order.

Table 13 show voice register pool telephone number field descriptions

Field

Description

DN

Directory number of the phone.

ID

Phone identification (ID) address.

IP Address

IP address and port number of the phones

LN

Line number of the phone.

Number

Number of the phones.

Pool

Shows the current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register dial-peer

Displays details of all dynamically created VoIP dial peers associated with the Cisco SIP SRST or Cisco CME register event.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool ringing

To display the details of phones that are currently in ringing state, use the show voice register pool ringing command in privileged EXEC mode.

show voice register pool ringing [brief]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are currently in ringing state.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are currently in ringing state. When used with the brief keyword, the show voice register pool ringing brief command only displays information related to calls that are bound towards the SIP phones.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for phones ringing in a voice register pool:

```
Router# show voice register pool ringing brief
```

Pool IP Address Number Remote Number

==== =============== ==================== ====================

2 8.33.33.112 45112 45111

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for phones ringing in a voice register pool:

Router# show voice register pool ringing

Pool tag: 2

==============

MAC Address : 0015.C68E.6D13

Contact IP : 8.33.33.112

Phone Number : 45112

Remote Number : 45111

Call 1

SIP Call ID : C0B5DA7-ADA311DE-8011803A-FF3E4CBC@8.3.3.5

State of the call : STATE_RECD_PROCEEDING (4)

Substate of the call : SUBSTATE_PROCEEDING_PROCEEDING (2)

Calling Number : 45111

Called Number : 45112

Bit Flags : 0xC00018 0x100 0x280

CC Call ID : 5

Source IP Address (Sig ): 8.3.3.5

Destn SIP Req Addr:Port : [8.33.33.112]:5060

Destn SIP Resp Addr:Port: [8.33.33.112]:5060

Destination Name : 8.33.33.112

Number of Media Streams : 1

Number of Active Streams: 1

RTP Fork Object : 0x0

Media Mode : flow-through

Media Stream 1

State of the stream : STREAM_ACTIVE

Stream Call ID : 5

Stream Type : voice+dtmf (1)

Stream Media Addr Type : 1

Negotiated Codec : No Codec (0 bytes)

Codec Payload Type : 255 (None)

Negotiated Dtmf-relay : inband-voice

Dtmf-relay Payload Type : 0

QoS ID : -1

Local QoS Strength : BestEffort

Negotiated QoS Strength : BestEffort

Negotiated QoS Direction : None

Local QoS Status : None

Media Source IP Addr:Port: [8.3.3.5]:16882

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

## show voice register pool unregistered

To display the details of the voice registration pools that do not have any phones registered, use the show voice register pool unregistered command in privileged EXEC mode.

show voice register pool unregistered

### Syntax Description

This command has no arguments or keywords.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the pools that do not have any active registrations. In Cisco Unified SRST, if multiple phones are trying to register through the same pool and if one phone successfully registers and the others do not, the pool is not considered as an unregistered pool, as it does have an active registration of the registered phone.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying information for pools with no active registeration:

Router# show voice register pool unregistered

Pool Tag: 2

MAC Address : 0015.C68E.6D13

No. of attempts to register: 0

Unregister time :

Last register request time :

Reason for state unregister:

No registration request since last reboot/unregister

Pool Tag: 3

MAC Address : 0021.5553.8998

No. of attempts to register: 0

Unregister time :

Last register request time :

Reason for state unregister:

No registration request since last reboot/unregister

Pool Tag: 4

MAC Address : 8989.9867.8769

No. of attempts to register: 0

Unregister time :

Last register request time :

Reason for state unregister:

No registration request since last reboot/unregister

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register pool registered

Displays details of phones that sucessfully register to Cisco Unified CME or Cisco Unified SRST.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register statistics

To display statistics associated with the registration event, use the show voice register statistics command in privileged EXEC mode.

show voice register statistics [global | poo l tag ]

### Syntax Description

global

(Optional) Displays aggregate statistics associated with the SIP phone registration event.

pool tag

(Optional) Displays registration pool statistics associated with a specific pool tag. The maximum number of pools is version and platform dependent. Type ? to display a list of values.

## Command Modes

Privileged EXEC

### Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

15.1(2)T

Cisco CME 8.1 Cisco SIP SRST 8.1

This command was modified. The global and pool keywords and tag argument were added. The output display was also modified to show more information about pools in unregistered state and time-stamps of registration event.

### Usage Guidelines

When using the show voice register statistics command, you can verify that the number of Registration and unRegister successes for global statistics are the sum of the values in the individual pools. Because some Registrations fail even before matching a voice register pool, for Registration and unRegister failed statistics the value is not the sum of the values in the individual pools. Immediate failures are accounted in the global statistics.

In Cisco Unified CME 8.1 and Cisco Unified SIP SRST 8.1, the time-stamps for the events is displayed along with other registration related statistics. The command output also displays the reason for pools in unregistered state. Use the show voice register statistics command with pool tag keyword to display registration pool statistics associated with a specific pool.

When using the global keyword, the show voice register command output displays the aggregate statistics associated with SIP phone registration. The output of this command also displays the attempted-registrations table.

### Examples

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying all statistical information:

```
Router# show voice register statistics
```

```
Sample Output:
```

```
Global statistics
```

```
Active registrations  : 2
```

```
Total SIP phones registered: 2
```

```
Total Registration Statistics
```

```
Registration requests  : 3
```

```
Registration success   : 2
```

```
Registration failed    : 1
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister        : 1
```

```
Last Register Request Time   : *11:42:31.783 UTC Wed Sep 16 2009
```

```
Last Unregister Request Time :
```

```
Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009
```

```
Unregister Success Time      :
```

```
Register pool 1 statistics
```

```
Active registrations  : 1
```

```
Total SIP phones registered: 1
```

```
Total Registration Statistics
```

```
Registration requests  : 1
```

```
Registration success   : 1
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister        : 0
```

```
Last Register Request Time   : *11:11:54.615 UTC Wed Sep 16 2009
```

```
Last Unregister Request Time :
```

```
Register Success Time        : *11:11:54.623 UTC Wed Sep 16 2009
```

```
Unregister Success Time      :
```

```
Register pool 2 statistics
```

```
Active registrations  : 1
```

```
Total SIP phones registered: 1
```

```
Total Registration Statistics
```

```
Registration requests  : 1
```

```
Registration success   : 1
```

```
Registration failed    : 0
```

```
unRegister requests    : 0
```

```
unRegister success     : 0
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister        : 0
```

```
Last Register Request Time   : *11:11:56.707 UTC Wed Sep 16 2009
```

```
Last Unregister Request Time :
```

```
Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009
```

```
Unregister Success Time      :
```

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying all statistical information:

```
Router# show voice register statistics global
```

Global Statistics:

Active registrations : 1

Total SIP phones registered: 2

Total Registration Statistics

R egistration requests : 97715

Registration success : 3

Registration failed : 97712

unRegister requests : 1

unRegister success : 1

unRegister failed : 0

Attempts to register

after last unregister : 97712

Last register request time : *06:45:11.127 UTC Wed Oct 14 2009

Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009

Register success time : *12:10:37.263 UTC Tue Oct 13 2009

Unregister success time : *11:56:22.182 UTC Tue Oct 13 2009

Phones that have attempted registrations and have failed:

MAC address: 001b.535c.d410

IP address : 8.3.3.111

Attempts : 97712

Time of first attempt : *12:20:32.775 UTC Tue Oct 13 2009

Time of latest attempt: *06:46:14.815 UTC Wed Oct 14 2009

Reason for failure :

Unauthorized registration request

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from this command displaying all statistical information associated with pool 1:

```
Router# show voice register statistics pool 1
```

```
Pool 1 Statistics:
```

```
Active registrations  : 0
```

```
Total SIP phones registered: 1
```

```
Total Registration Statistics
```

```
Registration requests  : 2
```

```
Registration success   : 2
```

```
Registration failed    : 0
```

```
unRegister requests    : 1
```

```
unRegister success     : 1
```

```
unRegister failed      : 0
```

```
Attempts to register
```

```
after last unregister : 0
```

```
Last register request time   : *12:10:37.259 UTC Tue Oct 13 2009
```

```
Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009
```

```
Register success time        : *12:10:37.263 UTC Tue Oct 13 2009
```

```
Unregister success time      : *11:56:22.182 UTC Tue Oct 13 2009
```

```
Reason for unregistered state:
```

```
No registration request since last reboot/unregister
```

Table 14 describes the significant fields shown in this output.

Table 14 show voice register statistics Field Descriptions

Field

Description

Statistics:

Used with the all , pool , and statistics keywords. Shows the registration statistics for this pool.

Active registrations

Used with the all , pool , and statistics keywords. Shows the current active registrations.

Last Register Request Time

Used with all , pool , and statistics keywords. Shows details such as day, date, and time when the phones requested to register the last time.

Last unRegister Request Time

Used with all, pool, and statistics keywords. Shows details such as day, date, and time when the phones requested to unregister the last time.

Total Registration Statistics

Used with the all , pool , and statistics keywords. Shows the total registration statistics for this pool.

Registration requests

Used with the all , pool , and statistics keywords. Shows the incoming registration requests.

Registration success

Used with the all , pool , and statistics keywords. Shows the successful registrations.

Registration failed

Used with the all , pool , and statistics keywords. Shows the failed registrations.

unRegister requests

Used with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests.

unRegister success

Used with the all , pool , and statistics keywords. Reports the number of successful unregisters.

unRegister failed

Used with the all , pool , and statistics keywords. Reports the number of failed unregisters.

Global statistics

Used with the statistics keyword. Details all active registrations.

Register pool number statistics

Used with the statistics keyword. Details specific pool statistics.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information.

show voice register pool

Displays all configuration information associated with a particular voice register pool.

show voice register pool attempted-registrations

Displays the details of phones that attempt to register with Cisco Unified CME or Cisco Unified SRST and fail.

## voice register global

To enter voice register global configuration mode in order to set global parameters for all supported Cisco SIP IP phones in a Cisco Unified CME or Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) environment, use the voice register global command in global configuration mode. To automatically remove the existing DNs, pools, and global dialplan patterns, use the no form of this command.

voice register global

no voice register global

### Syntax Description

This command has no arguments or keywords.

### Command Default

There are no system-level parameters configured for SIP IP phones.

## Command Modes

Global configuration (config)

### Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

15.0(1)XA

Cisco SIP SRST 8.0

This command was updated to display the signaling transport protocol.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

The no form of the command was modified.

### Usage Guidelines

Cisco Unified CME

Use this command to set provisioning parameters for all supported SIP phones in a Cisco Unified CME system.

Cisco Unified SIP SRST

Use this command to set provisioning parameters for multiple pools; that is, all supported Cisco SIP IP phones in a SIP SRST environment.

Cisco Unified CME 8.1 enhances the no form of voice register global command. The no voice register global command clears global configuration along with pools and DN configuration and also removes the configurations for voice register template, voice register dialplan, and voice register session-server. A confirmation is sought before the cleanup is made.

In Cisco Unified SRST 8.1 and later versions, the no voice register global command removes pools and DNs along with the global configuration.

### Examples1

Cisco Unified CME

The following is a partial sample output from the show voice register global command. All of the parameters listed were set under voice register global configuration mode:

Router# show voice register global

CONFIG [Version=4.0(0)]

========================

Version 4.0(0)

Mode is cme

Max-pool is 48

Max-dn is 48

Source-address is 10.0.2.4 port 5060

Load 7960-40 is P0S3-07-4-07

Time-format is 12

Date-format is M/D/Y

Time-zone is 5

Hold-alert is disabled

Mwi stutter is disabled

Mwi registration for full E.164 is disabled

Dst auto adjust is enabled

start at Apr week 1 day Sun time 02:00

stop at Oct week 8 day Sun time 02:00

### Examples2

Cisco Unified CME and Cisco Unified SRST

The following is a sample output from no voice register global command:

Router(config)# no voice register global

This will remove all the existing DNs, Pools, Templates,

Dialplan-Patterns, Dialplans and Feature Servers on the system.

Are you sure you want to proceed? Yes/No? [no]:

### Related Commands

Command

Description

allow connections sip to sip

Allows connections between SIP endpoints in a Cisco multiservice IP-to-IP gateway.

application (voice register global)

Selects the session-level application for all dial peers associated with SIP phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco Unified system.

## Feature Information for Cisco Unified SRST 8.1

Table 15 lists the release history for this feature.

Not all commands may be available in your Cisco IOS software release. For release information about a specific command, see the command reference documentation.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator enables you to determine which Cisco IOS software images support a specific software release, feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Note Table 15 lists only the Cisco IOS software release that introduced support for a given feature in a given Cisco IOS software release train. Unless noted otherwise, subsequent releases of that Cisco IOS software release train also support that feature.

Table 15 Feature Information for Cisco Unified SRST 8.1

Feature Name

Releases

Feature Information

Cisco Unified SRST 8.1

15.1(2)T

• Toll Fraud Prevention Enhancement

• Enhancements to SIP Phone Configuration

### Cisco and the Cisco Logo are trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and other countries. A listing of Cisco's trademarks can be found at www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1005R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. © 2010 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

| Trigger Condition | Administration State | Operation State |
|---|---|---|
| When ip address trusted authenticate is enabled. | Down | Down |
| When "gateway" is defined and a VoIP dial-peer with "ras" as a session target is in "UP" operational state | Up | Down |
| When ip address trusted authenticate is enabled and either "gateway" is not defined or no voip dial-peer with "ras" as session target is in "UP" operational state | Up | Up |

| Commands | Display Information |
|---|---|
| attempted-registrations size | Allows you to set the size of the table that stores information related to SIP phones that attempted to register and failed. |
| clear voice register attempted-registrations | Allows you to clear all the entries in attempted-registration table. |
| show voice register dn all | Displays the details of all the DNs defined in the system. |
| show voice register dial-peers pool | Displays the dialpeers a pool with a specific tag. |
| show voice register dialplan all | Displays the details of all the Dialplans that are defined in the system. |
| show voice register pool after-hour-exempt | Displays the details of the phones with "after-hour exempt" set. |
| show voice register pool attempted-registrations | Displays the details of the phones that have attempted to register and failed. |
| show voice register pool connected | Displays detailed information of phones that are in connected state (in conversation). |
| show voice register pool connected brief | Displays a brief information of phones that are in connected state (in conversation). |
| show voice register pool ip | Displays the details of a phone with a specific IPv4 address. |
| show voice register pool mac | Displays the details of a phone with a specific mac address. |
| show voice register pool network | Displays the information of the pools with a specific network address configured. |
| show voice register pool on-hold | Displays detailed information of phones that are currently on-hold. |
| show voice register pool on-hold brief | Displays brief information of phones that are currently on-hold. |
| show voice register pool phone-load | Displays the phone-load details of registered phones. |
| show voice register pool registered | Displays the details of the phones that are successfully registered. |
| show voice register pool remote | Displays remote phones (phones with no Address Resolution Protocol (ARP) entry. |
| show voice register pool ringing | Displays the detailed information of the phones that are currently ringing. |
| show voice register pool ringing brief | Displays brief information of phones that are currently ringing. |
| show voice register pool telephone-number | Displays the details of the phone with a specified telephone-number. |
| show voice register pool unregistered | Displays the details of the pools that do not have any registered phones. |
| show voice register statistics global | Displays the global statistics of registered SIP phones. |
| show voice register statistics pool | Displays the pool statistics associated with a specific pool. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service voip configuration mode. |
| Step 4 | ip address trusted authenticate Example: Router(conf-voi-serv)# ip address trusted authenticate | Enables IP address authentication on incoming H.323 or SIP trunk calls for toll fraud prevention support. IP address trusted list authenticate is enabled by default. Use the " no ip address trusted list authenticate " command to disable the IP address trusted list authentication. |
| Step 5 | ip-address trusted call-block cause code Example: Router(conf-voi-serv)#ip address trusted call-block cause call-reject | Issues a cause-code when the incoming call is rejected to the IP address trusted authentication. Note If the IP address trusted authentication fails, a call-reject (21) cause-code is issued to disconnect the incoming VoIP call. |
| Step 6 | end Example: Router()# end | Returns to privileged EXEC mode. |
| Step 7 | show ip address trusted list Example: Router# # show ip address trusted list IP Address Trusted Authentication Administration State: UP Operation State: UP IP Address Trusted Call Block Cause: call-reject (21) | Verifies a list of valid IP addresses for incoming H.323 or SIP trunk calls, Call Block cause for rejected incoming calls. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service voip configuration mode. |
| Step 4 | ip address trusted list Example: Router(conf-voi-serv)# ip address trusted list Router(cfg-iptrust-list)# | Enters ip address trusted list mode and allows to manually add additional valid IP addresses. |
| Step 5 | ipv4 {< ipv4 address > [< network mask >]} Example: Router(config)#voice service voip Router(conf-voi-serv)#ip taddress trusted list Router(cfg-iptrust-list)#ipv4 172.19.245.1 Router(cfg-iptrust-list)#ipv4 172.19.243.1 | Allows you to add up to 100 IPv4 addresses in ip address trusted list . Duplicate IP addresses are not allowed in the ip address trusted list. • (Optional) network mask — allows to define a subnet IP address. |
| Step 6 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |
| Step 7 | show ip address trusted list Example: Router# show shared-line | Displays a list of valid IP addresses for incoming H.323 or SIP trunk calls. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service pots Example: Router(config)# voice service pots Router(conf-voi-serv)# | Enters voice service configuration mode with voice telephone-service encapsulation type (pots). |
| Step 4 | direct-inward-dial isdn Example: Router(conf-voi-serv)#direct-inward-dial isdn | Enables direct-inward-dial (DID) for incoming ISDN number. The incoming ISDN (enbloc dialing) call is treated as if the digits were received from the DID trunk. The called number is used to select the outgoing dial peer. No dial tone is presented to the caller. |
| Step 5 | exit Example: Router(conf-voi-serv)# exit | Exits voice service pots configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice-port Example: Router(config)#voice-p 2/0/0 | Enters voice-port configuration mode. • Type your Analog or Digital FXO port number. |
| Step 4 | no secondary dialtone Example: Router((config-voiceport)# no secondary dialtone | Blocks the secondary dialtone on Analong and Digital FXO port. |
| Step 5 | end Example: Router(conf-voiceport)# exit | Returns to privileged EXEC mode. |
| Step 6 | show run Example: Router# show run \| sec voice-port 2/0/0 | Verifies that the secondary dialtone is disabled on the specific voice-port. |

| Related Topic | Document Title |
|---|---|
| Cisco Unified CME configuration | • Cisco Unified Communications Manager Express System Administrator Guide • Cisco Unified Communications Manager Express Command Reference |
| Cisco Unified CME network design | • Cisco Unified CallManager Express Solution Reference Network Design Guide |
| Cisco IOS voice configuration | • Cisco IOS Voice Configuration Library • Cisco IOS Voice Command Reference |
| Phone documentation for Cisco Unified CME | • User Documentation for Cisco Unified IP Phones |

| Standard | Title |
|---|---|
| No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature. | — |

| MIB | MIBs Link |
|---|---|
| No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature. | To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL: http://www.cisco.com/go/mibs |

| RFC | Title |
|---|---|
| No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature. | — |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/techsupport |

| size | Number of entries in attempted registrations table. Size range from 0 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST  8.1 | This command was introduced. |

| Command | Description |
|---|---|
| clear voice register attempted- registrations | Allows to delete entries in attempted-registration table. |
| show voice register attempted-registrations | Displays details of phones that attempted to register and failed. |

| ip ip-address | (Optional) IP address of the SIP phone attempting to register. |
|---|---|
| mac H.H.H | (Optional) MAC address of the SIP phone attempting to register. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| attempted-registrations size | Allows to set the size of the attempted-registrations table. |
| show voice register attempted-registration | Displays details of phones that attempted to register and failed. |

| cause-code | An ISDN cause code number. Range is from 1 to 188. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show dial-peer voice | Displays configuration information for dial peers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| voice service | Enters voice service configuration mode. |

| code-id | Q.850 call-disconnect cause code. Range is from 1 to 127. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| ip address trusted list | Allows to manually add additional valid IP addresses. |
| ip address trusted authenticate | Enables IP address trusted authentication for incoming VoIP calls. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| ip address trusted list | Allows to manually add additional valid IP addresses. |
| ip address trusted call- block cause | Allows to issues a cause-code when the incoming call is rejected by the IP address trusted authentication. |

| ipv4-address | IPv4 address of the incoming H.323 or SIP calls. |
|---|---|
| network mask | Subnet IP address. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| IP address trusted authenticate | Enables IP address trusted authentication for incoming VoIP calls. |
| IP address trusted code-block cause | Allows to issues a cause-code when the incoming call is rejected by the IP address trusted authentication. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| voice service | Enters voice service configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This command was modified. The output display was modified. |

| Field | Description |
|---|---|
| Pool Tag | Used with the all and pool keywords. Shows the assigned tag number of the current pool. |
| Config | Used with the all and pool keywords. Shows the voice register pool. |
| Network address and Mask | Used with the all and pool keywords. Shows network address and mask information if the id command is configured. |
| Number list, Pattern, and Preference | Used with the all and pool keywords. Shows the number command configuration. |
| Proxy IP address | Used with the all and pool keywords. Shows the proxy command configuration. |
| Default preference | Used with the all and pool keywords. Shows the default preference value of this pool. |
| Incoming called number | Used with the all and pool keywords. Shows the incoming called-number command configuration. |
| Translate outgoing called tag | Used with the all and pool keywords. Shows the translate-outgoing command configuration. |
| Class of Restriction List Tag | Used with the all and pool keywords. Shows the COR tag. |
| Incoming corlist name | Used with the all and pool keywords. Shows the cor command configuration. |
| Application | Used with the all and pool keywords. Shows the application command configuration for this pool. |
| Dialpeers created: | Used with the all and pool keywords. What follows is a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here. |
| Statistics | Used with the all , pool , and statistics keywords. Shows the registration statistics for this pool. |
| Active registrations | Used with the all , pool , and statistics keywords. Shows the current active registrations. |
| Total Registration Statistics | Used with the all , pool , and statistics keywords. Shows the total registration statistics for this pool. |
| Registration requests | Used with the all , pool , and statistics keywords. Shows the incoming registration requests. |
| Registration success | Used with the all , pool , and statistics keywords. Shows the successful registrations. |
| Registration failed | Used with the all , pool , and statistics keywords. Shows the failed registrations. |
| unRegister requests | Used with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests. |
| unRegister success | Used with the all , pool , and statistics keywords. Reports the number of successful unregisters. |
| unRegister failed | Used with the all , pool , and statistics keywords. Reports the number of failed unregisters. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| pool tag | Number of entries in attempted registrations table. Size range from 0 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This command was modified. Pool tag keyword- argument was added. Command output display was also modified to display dial-peers specific to a pool. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| tag | Tag number of the voice register dn for which to display information. Range is 1 to 750. |
|---|---|
| all | (Optional) Displays configuration information associated with all voice register dns defined in a system. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was introduced. |
| 15.1(2)T | Cisco CME 8.1 and Cisco SIP SRST 8.1 | This command was modified.The display output now shows pools that have DNs configured under them. All keyword was added to show configuration information for all voice register dns defined in system. |

| Field | Description |
|---|---|
| Auto answer | Status of auto-answer feature defined with the auto-answer command. |
| Config | List of configuration options defined for this voice register dn. |
| Dn Tag | Tag number of the requested voice register dn. |
| Huntstop | Status of huntstop behavior defined with the huntstop command. |
| Number | Telephone or extension number set with the number command in voice register dn configuration mode. |
| Preference | Preference order set with the preference command in voice register dn configuration mode. |

| Command | Description |
|---|---|
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register dn all | Displays information associated with all the dns configured in a system. |
| voice register dn | Enters voice register dn configuration mode to define an extension for a SIP phone line. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 15.0(1)XA | Cisco SIP SRST 8.0 | This command was updated to display the signaling transport protocol. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This command was modified.The output display now includes global statistics. |

| Field | Description |
|---|---|
| Date-format | Value of date-format command. |
| DST auto adjust | Setting of dst auto-adjust command. |
| Forwarding local | Setting of forwarding local command. |
| Generate text file | Setting of text file command. |
| Hold-alert | Setting of hold-alert command. |
| Load | Value of load command. |
| Max-dn | Reports the maximum number of SIP voice register directory numbers (dns) supported by the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with the max-dn command. The maximum possible number is platform-dependent. |
| Max-pool | Reports the maximum number of SIP voice register pools supported by the Cisco Unified SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent. |
| Max redirect number | Maximum number of redirects set with the max-redirect command. |
| Mode | Reports the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST. |
| MWI registration | Setting of mwi command. |
| MWI stutter | Setting of mwi stutter command. |
| Time-format | Value of time-format command. |
| Time-zone | Number of the timezone selected with the timezone command. |
| TFTP path | Directory location of provisioning files for SIP phones that is specified with the tftp-path command. |
| Version | Reports the Cisco Unified SIP SRST or Cisco Unified CME version number. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event. |
| voice register global | Enters voice register global configuration mode in order to set global parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco Unified SIP SRST environment. |

| tag | Tag number of the voice register pool for which to display information. The maximum number of pools is version and platform dependent. Type ? to display a list of values. |
|---|---|
| all | Displays information for all pools configured in a system. |
| brief | (Optional) Displays brief information for a specific voice register pool. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco Unified CME. |
| 12.4(15)XY | Cisco Unified CME  4.2(1) Cisco Unified SIP SRST 4.2(1) | Emergency response location (ERL) information displays in the output. |
| 12.4(20)T | Cisco Unified CME  7.0 Cisco Unified SIP SRST 7.0 | This command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was modified. Logical partitioning class of restriction (LPCOR) information was added to the output. |
| 15.1(2)T | Cisco Unified CME 8.1 | This command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the output. |

| Field | Description |
|---|---|
| Active registrations | Shows the current active registrations. Used with the all , pool , and statistics keywords. |
| Application | Shows the application command configuration for this pool. Used with the all and pool keywords. |
| Current phone-load | Shows the current version of the phone load. |
| Call Waiting | Setting of call-waiting command. |
| Config: | Shows the voice register pool. Used with the all and pool keywords. |
| Class of Restriction List Tag | Shows the COR tag. Used with the all and pool keywords. |
| Default preference | Shows the default preference value of this pool. Used with the all and pool keywords. |
| Dialpeers created: | Results in a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here. Used with the all and pool keywords. |
| DnD | Setting of dnd-control command. |
| DTMF Relay | Setting of dtmf-relay command. |
| Emergency response location | The ephone's emergency response location to which an emergency response team is dispatched when an emergency call is made. |
| Incoming called number | Shows the incoming called-number command configuration. Used with the all and pool keywords. |
| Incoming corlist name | Shows the cor command configuration. Used with the all and pool keywords. |
| keep-conference | Status of keep-conference command. |
| Lpcor Incoming | Setting of the lpcor incoming command. |
| Lpcor Outgoing | Setting of the lpcor outgoing command. |
| Lpcor Type | Setting of the lpcor type command. |
| Mac address | MAC address of this SIP phone as defined by using the id command. |
| Network address and Mask | Shows network address and mask information if the id command is configured. Used with the all and pool keywords. |
| Number list, Pattern, and Preference | Shows the number (voice register pool) command configuration. Used with the all and pool keywords. |
| Pool Tag | Shows the assigned tag number of the current pool. Used with the all and pool keywords. |
| Previous phone-load | Shows the version of the previous phone-load. |
| Proxy IP address | Shows the proxy command configuration; that is, the IP address of the external SIP server. Used with the all and pool keywords. |
| Registration failed | Shows the failed registrations. Used with the all , pool , and statistics keywords. |
| Registration requests | Shows the incoming registration requests. Used with the all , pool , and statistics keywords. |
| Registration success | Shows the successful registrations. Used with the all , pool , and statistics keywords. |
| Statistics: | Shows the registration statistics for this pool. Used with the all , pool , and statistics keywords. |
| statistics time-stamps | Shows the registration statistics for this pool with specific time-stamps. |
| Template | Template-tag number for template that is applied to this SIP phone. |
| Translate outgoing called tag | Shows the translate-outgoing command configuration. Used with the all and pool keywords. |
| Total Registration Statistics | Shows the total registration statistics for this pool. Used with the all , pool , and statistics keywords. |
| Type | Phone type identified for this SIP phone using the type command. |
| unRegister requests | Shows the incoming unregister/registration expiry requests. Used with the all , pool , and statistics keywords. |
| unRegister success | Reports the number of successful unregisters. Used with the all , pool , and statistics keywords. |
| unRegister failed | Reports the number of failed unregisters. Used with the all , pool , and statistics keywords. |
| Username Password | Values within the authentication credential. |
| Voice class stun usage | Displays the configured voice-class stun-usage information. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints registered with the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register dial-peer | Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified CME or Cisco Unified SIP SRST register event. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| H.H.H | MAC address of the SIP phone attempting to register. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Voice register DN tag of the line. |
| ID | Phone identification (ID) address. |
| IP Address | IP address of the SIP phone. |
| LN | Line number of the telephone number. |
| Number | Number of the phones that have a mac address. |
| Pool | Tag ID of the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| ip-address | IPv4 address of the SIP phone . |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Voice register DN tag of the line. |
| ID | Phone identification (ID) address. |
| IP Address | IP address of the SIP phone. |
| LN | Line number of the telephone number. |
| Number | Number of the phones that have a mac address. |
| Pool | Tag ID of the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| network-address | Network address of the SIP phone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Directory number of the phone. |
| ID | Phone identification (ID) address. |
| IP Address | IP address and port number of the phones |
| LN | Line number of the phone. |
| Number | Number of the phone that have network address. |
| Pool | Shows the current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register pool ip | Displays the voice register pool details of a phone with a specific IP address. |

| number | Number identifying a specific phone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Directory number of the phone. |
| ID | Phone identification (ID) address. |
| IP Address | IP address and port number of the phones |
| LN | Line number of the phone. |
| Number | Number of the phones. |
| Pool | Shows the current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register pool detail all | Displays the details of all the pools defined in the system. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Directory number of the phone. |
| IP Address/port | IP address and port number of the phones. |
| LN | Line number of the phone. |
| Number | Number of the phones that have after-hour exempt enabled. |
| Pool | Shows the current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| after-hour exempt(voice register pool) | Specifies that an IP phone does not have any of its outgoing calls blocked although call blocking is defined. |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| attempted-registrations size | Allows to set the size of the table that stores information related to SIP phones that attempt to register and fail. |
| clear voice register attempted-registrations | Clears entries from the attempted-registration table. |

| brief | (Optional) Displays brief details of SIP phones that are in connected state. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| brief | (Optional) Displays brief details of SIP phones that are currently on-hold. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| load(voice register global) | Associates a type of Cisco Unified IP phone with a phone firmware file. |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| Active registrations | Shows the current active registrations. Used with the all , pool , and statistics keywords. |
| Application | Shows the application command configuration for this pool. Used with the all and pool keywords. |
| Current phone-load | Shows the current version of the phone load. |
| Call Waiting | Setting of call-waiting command. |
| Config: | Shows the voice register pool. Used with the all and pool keywords. |
| Class of Restriction List Tag | Shows the COR tag. Used with the all and pool keywords. |
| Default preference | Shows the default preference value of this pool. Used with the all and pool keywords. |
| Dialpeers created: | Results in a list of all dial peers created and their contents. Dial-peer contents differ per application and are not described here. Used with the all and pool keywords. |
| DnD | Setting of dnd-control command. |
| DTMF Relay | Setting of dtmf-relay command. |
| Emergency response location | The ephone's emergency response location to which an emergency response team is dispatched when an emergency call is made. |
| Incoming called number | Shows the incoming called-number command configuration. Used with the all and pool keywords. |
| Incoming corlist name | Shows the cor command configuration. Used with the all and pool keywords. |
| keep-conference | Status of keep-conference command. |
| Lpcor Incoming | Setting of the lpcor incoming command. |
| Lpcor Outgoing | Setting of the lpcor outgoing command. |
| Lpcor Type | Setting of the lpcor type command. |
| Mac address | MAC address of this SIP phone as defined by using the id command. |
| Network address and Mask | Shows network address and mask information if the id command is configured. Used with the all and pool keywords. |
| Number list, Pattern, and Preference | Shows the number (voice register pool) command configuration. Used with the all and pool keywords. |
| Pool Tag | Shows the assigned tag number of the current pool. Used with the all and pool keywords. |
| Previous phone-load | Shows the version of the previous phone-load. |
| Proxy IP address | Shows the proxy command configuration; that is, the IP address of the external SIP server. Used with the all and pool keywords. |
| Registration failed | Shows the failed registrations. Used with the all , pool , and statistics keywords. |
| Registration requests | Shows the incoming registration requests. Used with the all , pool , and statistics keywords. |
| Registration success | Shows the successful registrations. Used with the all , pool , and statistics keywords. |
| Statistics: | Shows the registration statistics for this pool. Used with the all , pool , and statistics keywords. |
| statistics time-stamps | Shows the registration statistics for this pool with specific time-stamps. |
| Template | Template-tag number for template that is applied to this SIP phone. |
| Translate outgoing called tag | Shows the translate-outgoing command configuration. Used with the all and pool keywords. |
| Total Registration Statistics | Shows the total registration statistics for this pool. Used with the all , pool , and statistics keywords. |
| Type | Phone type identified for this SIP phone using the type command. |
| unRegister requests | Shows the incoming unregister/registration expiry requests. Used with the all , pool , and statistics keywords. |
| unRegister success | Reports the number of successful unregisters. Used with the all , pool , and statistics keywords. |
| unRegister failed | Reports the number of failed unregisters. Used with the all , pool , and statistics keywords. |
| Username Password | Values within the authentication credential. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register pool unregistered | Displays the details of voice register pools that do not have any phones registered. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified SIP SRST or Cisco Unified CME register event. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified  SRST 8.1 | This command was introduced. |

| Field | Description |
|---|---|
| DN | Directory number of the phone. |
| ID | Phone identification (ID) address. |
| IP Address | IP address and port number of the phones |
| LN | Line number of the phone. |
| Number | Number of the phones. |
| Pool | Shows the current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register dial-peer | Displays details of all dynamically created VoIP dial peers associated with the Cisco SIP SRST or Cisco CME register event. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| brief | (Optional) Displays brief details of SIP phones that are currently in ringing state. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register pool registered | Displays details of phones that sucessfully register to Cisco Unified CME or Cisco Unified SRST. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| global | (Optional) Displays aggregate statistics associated with the SIP phone registration event. |
|---|---|
| pool tag | (Optional) Displays registration pool statistics associated with a specific pool tag. The maximum number of pools is version and platform dependent. Type ? to display a list of values. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.1(2)T | Cisco CME 8.1 Cisco SIP SRST 8.1 | This command was modified. The global and pool keywords and tag argument were added. The output display was also modified to show more information about pools in unregistered state and time-stamps of registration event. |

| Field | Description |
|---|---|
| Statistics: | Used with the all , pool , and statistics keywords. Shows the registration statistics for this pool. |
| Active registrations | Used with the all , pool , and statistics keywords. Shows the current active registrations. |
| Last Register Request Time | Used with all , pool , and statistics keywords. Shows details such as day, date, and time when the phones requested to register the last time. |
| Last unRegister Request Time | Used with all, pool, and statistics keywords. Shows details such as day, date, and time when the phones requested to unregister the last time. |
| Total Registration Statistics | Used with the all , pool , and statistics keywords. Shows the total registration statistics for this pool. |
| Registration requests | Used with the all , pool , and statistics keywords. Shows the incoming registration requests. |
| Registration success | Used with the all , pool , and statistics keywords. Shows the successful registrations. |
| Registration failed | Used with the all , pool , and statistics keywords. Shows the failed registrations. |
| unRegister requests | Used with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests. |
| unRegister success | Used with the all , pool , and statistics keywords. Reports the number of successful unregisters. |
| unRegister failed | Used with the all , pool , and statistics keywords. Reports the number of failed unregisters. |
| Global statistics | Used with the statistics keyword. Details all active registrations. |
| Register pool number statistics | Used with the statistics keyword. Details specific pool statistics. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and register information. |
| show voice register pool | Displays all configuration information associated with a particular voice register pool. |
| show voice register pool attempted-registrations | Displays the details of phones that attempt to register with Cisco Unified CME or Cisco Unified SRST and fail. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 15.0(1)XA | Cisco SIP SRST 8.0 | This command was updated to display the signaling transport protocol. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | The no form of the command was modified. |

| Command | Description |
|---|---|
| allow connections sip to sip | Allows connections between SIP endpoints in a Cisco multiservice IP-to-IP gateway. |
| application (voice register global) | Selects the session-level application for all dial peers associated with SIP phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco Unified system. |

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified SRST 8.1 | 15.1(2)T | • Toll Fraud Prevention Enhancement • Enhancements to SIP Phone Configuration |