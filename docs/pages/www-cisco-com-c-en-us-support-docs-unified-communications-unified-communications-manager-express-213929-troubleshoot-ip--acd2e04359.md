---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-express-213929-troubleshoot-ip--acd2e04359
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-express/213929-troubleshoot-ip-phone-registration-issue.html
retrieved_at: 2026-08-21T09:47:00.840011+00:00
---

Troubleshoot IP Phone Registration Issues with CUCME

# Troubleshoot IP Phone Registration Issues with CUCME

### Download Options

Updated: November 23, 2018

Document ID: 213929

Contents

## Contents

## Introduction

This document describes how to troubleshoot Skinny Client Control Protocol (SCCP) and Session Initiation Protocol (SIP) Phone registrations issues on Cisco Unified Communications Manager Express (CUCME).

## SCCP Phone Registration Issues

Use the show ephone registered command to display the status of registered Skinny Client Control Protocol phones.

```
Router# show ephone registeredephone-12[11] Mac:001A.A11B.7D6D TCP socket:[5] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 15/12 max_streams=1mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:7IP:10.10.1.17 * 35177 6941  keepalive 3593 max_line 4 available_line 3button 1: cw:1 dn 11 number 1001 CH1   IDLE         CH2   IDLEbutton 2: cw:1 dn 56 number 6971  auto dial 6970 CH1   IDLEbutton 3: cw:1 dn 10 number 1000 CH1   IDLE         CH2   IDLE1 feature buttons enabled: dndPreferred Codec: g711ulawLpcor Type: none
```

Use the show ephone command to display the status of Skinny Client Control Protocol phones that are not registered or are trying to register.

```
Router# show ephone

ephone-8[7] Mac:000A.B7B1.444A TCP socket:[5] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 11/9 max_streams=1

mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:8 privacy:0

IP:10.4.188.99 * 50007 Telecaster 7940  keepalive 8424 max_line 2 available_line 2

button 1: cw:1 ccw:(0 0)

  dn 6  number 6006 CH1   IDLE         CH2   IDLE         overlay shared

button 2: cw:1 ccw:(0 0 0 0 0 0 0 0)

  dn 42 number 6042 CH1   IDLE         CH2   IDLE         CH3   IDLE         CH4   IDLE         CH5   IDLE         CH6   IDLE         CH7   IDLE         CH8   IDLE         shared

overlay 1: 6(6006) 7(6007) 8(6008)

Preferred Codec: g711ulaw

Lpcor Type: local Incoming: ephone_group1 Outgoing: ephone_group1
```

To display the log of ephones that unsuccessfully attempt to register with Cisco Unified CUCME, use the show ephone attempted-registrations command in privileged EXEC mode.

```
Router# show ephone attempted-registrationsAttempting Mac address:Num    Mac Address         DateTime                          DeviceType-----------------------------------------------------------------------------1      C863.8475.5417      22:52:05 UTC Thu Apr 28 2005      SCCP Gateway (AN) 2      C863.8475.5408      22:52:05 UTC Thu Apr 28 2005      SCCP Gateway (AN) .....25     000D.28D7.7222      22:26:32 UTC Thu Apr 28 2005      Telecaster 7960 26     000D.BDB7.A9EA      22:25:59 UTC Thu Apr 28 2005      Telecaster 7960 ...47     C863.94A8.D40F      22:52:17 UTC Thu Apr 28 2005      SCCP Gateway (AN) 48     C863.94A8.D411      22:52:18 UTC Thu Apr 28 2005      SCCP Gateway (AN) 49     C863.94A8.D400      22:52:15 UTC Thu Apr 28 2005      SCCP Gateway (AN)
```

In case this is a phone replacement be apprised auto-registration is disabled to make sure we have done the ephone and ephone-dn configuration as per The Home Depot standard.

### Different Type of Issues with SCCP Phones

Step 1. Not booting up/nothing in the display: Verify the switch port PoE configuration and compare it with a working port.

Step 2. Not getting IP address (stuck in configuring IP/getting wrong IP address/not getting TFTP Server IP).

- Verify if DHCP is enabled on the phone from the settings menu

- Check the switch port is configured with correct voice VLAN (check on the switch port the phone is connected to)

show run interface fast/gig x/x

show cdp neighbor detail

Step 3. Not registering even if the IP address is updated:

- Verify network connectivity between the CUCME and IP Phone.

- debug ip tcp transaction.

- The configuration of the CUCME, the Phone MAC address, phone type etc.

- Are the Cisco phone firmware files required for each phone type installed in flash memory “show flash”

- Verify if the phone requests/downloads correct configuration files using the following debugs.

- debug tftp event/packet.

- debug ephone register mac-address <MAC of the Phone>.

Step 4. Not registering with CUCME even after downloading configuration file:

- Verify if the TCP session to port 2000 is open from Skinny Client Control Protocol Phone.

- Useful debugs

- debug ip tcp transaction

- debug tftp event/packet

- debug ephone register mac-address <MAC of the Phone>

Note :Post any configuration change make sure you create a new configuration file using the command “create cnf-files” and do a write-memory.

## SIP Phone Registration Issues

Use the show voice register statistics command to display statistics associated with the registration event.

```
Router# show voice register statisticsSample Output:Global statistics  Active registrations  : 2  Total SIP phones registered: 2  Total Registration Statistics    Registration requests  : 3    Registration success   : 2    Registration failed    : 1    unRegister requests    : 0    unRegister success     : 0    unRegister failed      : 0    Attempts to register     after last unregister        : 1     Last Register Request Time   : *11:42:31.783 UTC Wed Sep 16 2009     Last Unregister Request Time :     Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009     Unregister Success Time      : Register pool 1 statistics  Active registrations  : 1  Total SIP phones registered: 1  Total Registration Statistics    Registration requests  : 1    Registration success   : 1    Registration failed    : 0    unRegister requests    : 0    unRegister success     : 0    unRegister failed      : 0    Attempts to register     after last unregister        : 0     Last Register Request Time   : *11:11:54.615 UTC Wed Sep 16 2009     Last Unregister Request Time :     Register Success Time        : *11:11:54.623 UTC Wed Sep 16 2009     Unregister Success Time      : Register pool 2 statistics  Active registrations  : 1  Total SIP phones registered: 1  Total Registration Statistics    Registration requests  : 1    Registration success   : 1    Registration failed    : 0    unRegister requests    : 0    unRegister success     : 0    unRegister failed      : 0    Attempts to register     after last unregister        : 0     Last Register Request Time   : *11:11:56.707 UTC Wed Sep 16 2009     Last Unregister Request Time :     Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009     Unregister Success Time
```

Use the show voice register all command to display configuration and registration information for Session Initiation Protocol phones in Cisco Unified CUCME.

```
Router# show voice register pool allPool Tag 5Config:Mac address is B4A4.E328.4698Type is 9971 addon 1 CKEMNumber list 1 : DN 2Number list 2 : DN 3Proxy Ip address is 0.0.0.0DTMF Relay is disabledCall Waiting is enabledDnD is disabledVideo is enabledCamera is enabledBusy trigger per button value is 0keep-conference is enabledregistration expires timer max is 200 and min is 60kpml signal is enabledLpcor Type is none
```

To display the details of phones that attempt to register with CUCME or Cisco Unified SRST and fail, use the show voice register pool attempted-registrations command in privileged EXEC mode.

```
Router# show voice register pool attempted-registrationsPhones that have attempted registrations and have failed: MAC address: 001b.535c.d410  IP address : 8.3.3.111  Attempts   : 5 Time of first attempt : *10:49:51.542 UTC Wed Oct 14 2009 Time of latest attempt: *10:50:00.886 UTC Wed Oct 14 2009 Reason for failure    :          No pool match for the registration request MAC address: 0015.c68e.6d13  IP address : 8.33.33.112  Attempts   : 4 Time of first attempt : *10:49:53.418 UTC Wed Oct 14 2009 Time of latest attempt: *10:50:00.434 UTC Wed Oct 14 2009 Reason for failure    :          No pool match for the registration request MAC address: 0009.43E9.0B35  IP address : 9.13.40.83  Attempts   : 1 Time of first attempt : *10:49:57.866 UTC Wed Oct 14 2009 Time of latest attempt: *10:49:57.866 UTC Wed Oct 14 2009 Reason for failure    :          No pool match for the registration request
```

For Session Initiation Protocol Phone, verify if the registrar server is enabled in the CUCME

In case this is a phone replacement be apprised auto-registration is disabled to make sure we have done the pool and dn configuration as per The Home Depot standard.

### Different Type of Issues with SIP Phones

Step 1. Not booting up/nothing in the display:

Verify the switch port PoE configuration and compare it with a working port.

Step 2. Not getting IP address (stuck in configuring IP)/getting wrong IP address/not getting TFTP Server IP:

- Verify if DHCP is enabled on the phone from the settings menu.

- Check the switch port is configured with correct voice VLAN (check on the switch port the phone is connected to).

show run interface fast/gig x/x

show cdp neighbor detail

Step 3. Not registering even if the IP address is updated:

- Verify network connectivity between the CUCME and IP Phone.

- debug ip tcp transaction.

- The configuration of the CUCME, the Phone MAC address, phone type etc.

- Are the Cisco phone firmware files required for each phone type installed in flash memory show flash.

- Verify if the phone requests/downloads correct configuration files using the following debugs.

- debug tftp event/packet.

Step 4. Do not register with CUCME even after the configuration file is downloaded:

- Verify if the TCP session to port 5060 is open from Session Initiation Protocol Phone.

- The Register SIP messages are coming in from the Phone.

- debug ccsip message.

- debug voice register error.

- debug voice register event.

Note : Post any configuration change make sure you create a new configuration file using the command create profile and do a write-memory.