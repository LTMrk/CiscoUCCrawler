---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bcs-installation-guide-bcsvd-in-socccfig-html-8daaa36b1d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bcs/installation/guide/bcsvd_in/SOCCcfig.html
retrieved_at: 2026-08-21T22:59:04.511970+00:00
---

Installing Cisco Business Communications Solution Verified Designs

# Installing Cisco Business Communications Solution Verified Designs

Updated: November 2, 2007

Chapter: Appendix C: Cisco BCS Verified Designs Configuration Example

## Chapter: Appendix C: Cisco BCS Verified Designs Configuration Example

## Appendix C: Cisco BCS Verified Designs Configuration Example

This appendix shows an example of a Cisco BCS Verified Designs configuration file. Descriptive statements are included for each subsection in the configuration file.

```
Building configuration...
```

```
Current configuration : 11927 bytes
```

```
!
```

```
version 12.3
```

```
service timestamps debug datetime msec
```

```
service timestamps log datetime msec
```

```
no service password-encryption
```

```
!
```

```
hostname Cisco_2801a
```

```
!
```

```
boot-start-marker
```

```
boot system flash:c2801-ipvoice-mz.123_11_T6.bin
```

```
boot system flash:
```

```
boot system flash:c2801-spservicek9-mz.2005-05-16.ESE_20050516_123_11_T6.bin
```

```
boot system flash:
```

```
boot-end-marker
```

```
!
```

```
enable password cisco
```

```
!
```

```
mmi polling-interval 60
```

```
no mmi auto-configure
```

```
no mmi pvc
```

```
mmisnmp-timeout 180
```

```
no aaa new-model
```

```
ip subnet-zero
```

```
ip cef
```

```
!
```

```
!
```

```
ip dhcp excluded-address 10.1.31.1 10.1.31.20
```

```
ip dhcp excluded-address 10.1.51.1 10.1.51.20
```

```
ip dhcp excluded-address 10.1.71.1 10.1.71.20
```

```
!
```

```
! The commands below define DHCP for data, voice, and wireless LAN. Option 150 should point to voice mail.
```

```
!
```

```
ip dhcp pool Data
```

```
network 10.1.31.0 255.255.255.0
```

```
default-router 10.1.31.1
```

```
!
```

```
ip dhcp pool Voice
```

```
network 10.1.51.0 255.255.255.0
```

```
default-router 10.1.51.1
```

```
option 150 ip 10.1.51.1
```

```
!
```

```
ip dhcp pool WLAN
```

```
network 10.1.71.0 255.255.255.0
```

```
default-router 10.1.71.1
```

```
!
```

```
!
```

```
no ip domain lookup
```

```
no ftp-server write-enable
```

```
!
```

```
!
```

```
!
```

```
! The statements below enable H.323 to H.323, H.323 to SIP, in Cisco IOS software so that 
H.323 calls to IP phones at this site can roll over to voice mail.
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
supplementary-service h450.12
```

```
h323
```

```
! Translation rules manipulate digits of calling- or called-numbers (depending on how they 
are referred to in the subsequent "voice translation-profile" command).
```

```
! Translation rules use regular expressions to state what numbers, or patterns, should be 
substituted for what other numbers and can be much more sophisticated than the basic ones 
used below.
```

```
voice translation-rule 101
```

```
rule 1 /^101/ /1/
```

```
rule 2 /^202/ /2/
```

```
rule 3 /^252/ /2/
```

```
rule 4 /^303/ /3/
```

```
rule 5 /^353/ /3/
```

```
rule 6 /^404/ /4/
```

```
rule 7 /^454/ /4/
```

```
rule 8 /^505/ /5/
```

```
rule 9 /^555/ /5/
```

```
!
```

```
!
```

```
voice translation-profile 101
```

```
translate called 101
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
interface Loopback0
```

```
ip address 10.1.10.2 255.255.255.255
```

```
h323-gateway voip interface
```

```
h323-gateway voip bind srcaddr 10.1.10.1
```

```
!
```

```
interface FastEthernet0/0
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
!
```

```
interface FastEthernet0/0.31
```

```
encapsulation dot1Q 31
```

```
ip address 10.1.31.1 255.255.255.0
```

```
!
```

```
interface FastEthernet0/0.51
```

```
encapsulation dot1Q 51
```

```
ip address 10.1.51.1 255.255.255.0
```

```
!
```

```
interface FastEthernet0/0.71
```

```
encapsulation dot1Q 71
```

```
ip address 10.1.71.1 255.255.255.0
```

```
!
```

```
interface Service-Engine0/0
```

```
ip unnumbered FastEthernet0/0.31
```

```
service-module ip address 10.1.31.2 255.255.255.0
```

```
service-module ip default-gateway 10.1.31.1
```

```
!
```

```
interface FastEthernet0/1
```

```
no ip address
```

```
shutdown
```

```
duplex auto
```

```
speed auto
```

```
!
```

```
interface Serial0/3/0
```

```
bandwidth 512
```

```
ip address 192.168.1.2 255.255.255.252
```

```
encapsulation frame-relay
```

```
!
```

```
router eigrp 100
```

```
network 10.0.0.0
```

```
network 192.168.1.0
```

```
no auto-summary
```

```
!
```

```
ip classless
```

```
!
```

```
!
```

```
ip http server
```

```
no ip http secure-server
```

```
ip http path flash:
```

```
!
```

```
! The statements below define the TFTP server for the IP phone loads.
```

```
!
```

```
tftp-server flash:ATA030100SCCP040211A.zup
```

```
tftp-server flash:CP7902040000SCCP040701A.sbin
```

```
tftp-server flash:CP7905040000SCCP040701A.sbin
```

```
tftp-server flash:P00403020214.bin
```

```
tftp-server flash:CP7912040000SCCP040701A.sbin
```

```
tftp-server flash:S00103020002.bin
```

```
tftp-server flash:P00503010100.bin
```

```
tftp-server flash:cmterm_7936.3-3-5-0.bin
```

```
tftp-server flash:P00303020214.bin
```

```
tftp-server flash:P00305000301.sbn
```

```
tftp-server flash:cmterm_7920.3.3-01-08.bin
```

```
!
```

```
control-plane
```

```
!
```

```
!
```

```
!
```

```
voice-port 0/3/0
```

```
!
```

```
voice-port 0/3/1
```

```
!
```

```
sccp local FastEthernet0/0.31
```

```
sccp ccm 10.1.31.1 identifier 1
```

```
sccp
```

```
!
```

```
sccp ccm group 1
```

```
associate ccm 1 priority 1
```

```
associate profile 1 register mtp001121fb0366
```

```
!
```

```
dspfarm profile 1 transcode
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec gsmfr
```

```
maximum sessions 5
```

```
associate application SCCP
```

```
!
```

```
! 1 is the Cisco Unity Express pilot number and 1980 is the voice-mail pilot number. Calls 
to these numbers are directed via SIP to Cisco Unity Express at its IP address. The 
translation rule defined earlier is used here to translate DID numbers to the extensions 
before the call is routed to Cisco Unity Express. DTMF relay to Cisco Unity Express must 
be via SIP-Notify, and G.711 "no vad" must be configured on this dial-peer.
```

```
!
```

```
dial-peer voice 1 voip
```

```
description ** cue voicemail pilot number **
```

```
destination-pattern 1480
```

```
session protocol sipv2
```

```
session target ipv4:10.1.31.2
```

```
dtmf-relay sip-notify
```

```
codec g711ulaw
```

```
no vad
```

```
!
```

```
dial-peer voice 2 voip
```

```
description ** cue auto attendant number **
```

```
destination-pattern 1490
```

```
session protocol sipv2
```

```
session target ipv4:10.1.31.2
```

```
dtmf-relay sip-notify
```

```
codec g711ulaw
```

```
no vad
```

```
!
```

```
dial-peer voice 102 voip
```

```
description Call to Cisco_2811a
```

```
translation-profile outgoing 101
```

```
destination-pattern 15....
```

```
session target ipv4:10.1.32.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 103 voip
```

```
description Call to Cisco_2821a
```

```
translation-profile outgoing 101
```

```
destination-pattern 20....
```

```
session target ipv4:10.1.33.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 106 voip
```

```
description Call to Cisco_2851a
```

```
translation-profile outgoing 101
```

```
destination-pattern 35....
```

```
session target ipv4:10.1.36.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 108 voip
```

```
description Call to Cisco_3825a
```

```
translation-profile outgoing 101
```

```
destination-pattern 45....
```

```
session target ipv4:10.1.38.1
```

```
dtmf-relay h245-alphanumeric
```

```
codec g771ulaw
```

```
!
```

```
dial-peer voice 104 voip
```

```
description Call to Callmanager
```

```
translation-profile outgoing 101
```

```
destination-pattern 25....
```

```
session target ipv4:10.1.33.97
```

```
dtmf-relay h245-alphanumeric
```

```
no vad
```

```
!
```

```
dial-peer voice 4980 voip
```

```
description Unity Voice Mail
```

```
destination-pattern 4980
```

```
session target ipv4:10.1.38.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
! The commands below following the "telephony-service" keyword is the main Cisco CME 
configuration for this router. Key considerations include the following:
```

```
! - The "load" command associates a type of Cisco IP phone with a phone firmware file.
```

```
! - The "max-ephones" and "max-dn" commands specify the maximum number of phones and 
extensions supported on this system.
```

```
! - The "source-address" provides the IP address and port through which IP phones 
communicate with the Cisco CME router.
```

```
! - The "system message" ??.
```

```
! - The "sdspfarm" commands ??.
```

```
! - The "create cnf-files" command generates the XML configuration files required for IP 
phones.
```

```
! - The "voicemail" command defines the voice mail pilot number as 1480.
```

```
! - The "max-conferences" command specifies that the maximum number of three-party 
conferences simultaneously supported by this Cisco CME system is eight.
```

```
! - The "web admin" commands define the Cisco CME system administrator and customer 
administrator accounts.
```

```
! - The "dn-webedit" and "time-webedit" commands enable the ability to add extensions 
(ephone-dns) and allow
```

```
! - The "transfer-system" command defines the types of transfer (blind and consult) 
supported by the Cisco CME system.
```

```
! - The "secondary dialtone" command defines the ?? by the Cisco CME system.
```

```
telephony-service
```

```
load 7960-7940 P00303020214
```

```
load 7920 cmterm_7920.3.3-01-08.bin
```

```
load 7912 CP7912040000SCCP040701A.sbin
```

```
max-ephones 24
```

```
max-dn 72
```

```
ip source-address 10.1.31.1 port 2000
```

```
system message CME on 2801
```

```
sdspfarm units 5
```

```
sdspfarm transcode sessions 10
```

```
sdspfarm tag 1 mtp001121fb0366
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
voicemail 1480
```

```
max-conferences 8
```

```
web admin system name cmeadmin password cmeadmin
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult
```

```
secondary-dialtone 9
```

```
!
```

```
!
```

```
! The definitions of the Cisco CME IP phone extensions (ephone-dn) start below. Key 
considerations include the following:
```

```
! - The "dual-line" designation ensures that transfers and conferences can be done on the 
phone.
```

```
! - The "number" keyword provides the extension digits, and the "secondary" field ensures 
that DID numbers for this extension are also matched to this ephone-dn.
```

```
! - The "name" keyword provides the name that will be used on the phone display.
```

```
! - The "call-forward busy and noan" keywords provide the voice-mail pilot number (1480) 
where calls must be forwarded when the user is busy on the phone or when the call is not 
answered (after a timeout of the given number of seconds).
```

```
ephone-dn  1  dual-line
```

```
number 1000
```

```
label 1000
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  2  dual-line
```

```
number 1001
```

```
label 1001
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  3  dual-line
```

```
number 1002
```

```
label 1002
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  4  dual-line
```

```
number 1003
```

```
label 1003
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  5  dual-line
```

```
number 1004
```

```
label 1004
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  6  dual-line
```

```
number 1005
```

```
label 1005
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  7  dual-line
```

```
number 1006
```

```
label 1006
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  8  dual-line
```

```
number 1007
```

```
label 1007
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  9  dual-line
```

```
number 1008
```

```
label 1008
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  10 dual-line
```

```
number 1009
```

```
label 1009
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  11  dual-line
```

```
number 1010
```

```
label 1010
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  12  dual-line
```

```
number 1011
```

```
label 1011
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  13  dual-line
```

```
number 1012
```

```
label 1012
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  14  dual-line
```

```
number 1013
```

```
label 1013
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  15  dual-line
```

```
number 1014
```

```
label 1014
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  16  dual-line
```

```
number 1015
```

```
label 1015
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  17  dual-line
```

```
number 1016
```

```
label 1016
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  18  dual-line
```

```
number 1017
```

```
label 1017
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  19  dual-line
```

```
number 1018
```

```
label 1018
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  20  dual-line
```

```
number 1019
```

```
label 1019
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  21  dual-line
```

```
number 1020
```

```
label 1020
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  22  dual-line
```

```
number 1021
```

```
label 1021
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  23  dual-line
```

```
number 1022
```

```
label 1022
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  24  dual-line
```

```
number 1023
```

```
label 1023
```

```
description First Last Name
```

```
name First Last Name
```

```
call-forward busy 1480
```

```
call-forward noan 1480 timeout 10
```

```
!
```

```
!
```

```
ephone-dn  25
```

```
number 1488....
```

```
mwi on
```

```
!
```

```
!
```

```
ephone-dn  26
```

```
number 1489....
```

```
mwi off
```

```
!
```

```
!
```

```
! The following block of commands provides all the "ephone" definitions on the system. 
These represent the physical phone parameters such as their MAC addresses, the user ID 
(called username) associated with the phone, the button layouts, and the phone type. Key 
considerations include the following:
```

```
! - The "username" is used by the end users to log in to Cisco CME to get a web display of 
their phone settings.
```

```
! - The "type" command specifies the IP phone type (in this case a Cisco 7960 IP Phone).
```

```
! - The "button" command provides the button layout on the phone. Button 1 has ??, etc.
```

```
ephone  1
```

```
username "user1" password null
```

```
mac-address 0030.94C2.5DF0
```

```
type 7960
```

```
button  1:1
```

```
!
```

```
!
```

```
!
```

```
ephone  2
```

```
username "user2" password null
```

```
mac-address 0012.D984.B03E
```

```
type 7912
```

```
button  1:2
```

```
!
```

```
!
```

```
!
```

```
ephone  3
```

```
username "user3" password null
```

```
mac-address 0000.0000.0001
```

```
type 7960
```

```
button  1:3
```

```
!
```

```
!
```

```
!
```

```
ephone  4
```

```
username "user4" password null
```

```
mac-address 0000.0000.0002
```

```
type 7960
```

```
button  1:4
```

```
!
```

```
!
```

```
!
```

```
ephone  5
```

```
username "user5" password null
```

```
mac-address 0000.0000.0003
```

```
type 7960
```

```
button  1:5
```

```
!
```

```
!
```

```
!
```

```
ephone  6
```

```
username "user6" password null
```

```
mac-address 0000.0000.0004
```

```
type 7960
```

```
button  1:6
```

```
!
```

```
!
```

```
!
```

```
ephone  7
```

```
username "user7" password null
```

```
mac-address 0000.0000.0005
```

```
type 7960
```

```
button  1:7
```

```
!
```

```
!
```

```
!
```

```
ephone  8
```

```
username "user8" password null
```

```
mac-address 0000.0000.0006
```

```
type 7960
```

```
button  1:8
```

```
!
```

```
!
```

```
!
```

```
ephone  9
```

```
username "user9" password null
```

```
mac-address 0000.0000.0007
```

```
type 7960
```

```
button  1:9
```

```
!
```

```
!
```

```
!
```

```
ephone  10
```

```
username "user10" password null
```

```
mac-address 0000.0000.0008
```

```
type 7960
```

```
button  1:10
```

```
!
```

```
!
```

```
!
```

```
ephone  11
```

```
username "user11" password null
```

```
mac-address 0000.0000.0009
```

```
type 7960
```

```
button  1:11
```

```
!
```

```
!
```

```
!
```

```
ephone  12
```

```
username "user12" password null
```

```
mac-address 0000.0000.000A
```

```
type 7960
```

```
button  1:12
```

```
!
```

```
!
```

```
!
```

```
ephone  13
```

```
username "user13" password null
```

```
mac-address 0000.0000.000B
```

```
type 7960
```

```
button  1:13
```

```
!
```

```
!
```

```
!
```

```
ephone  14
```

```
username "user14" password null
```

```
mac-address 0000.0000.000C
```

```
type 7960
```

```
button  1:14
```

```
!
```

```
!
```

```
!
```

```
ephone  15
```

```
username "user15" password null
```

```
mac-address 0000.0000.000D
```

```
type 7960
```

```
button  1:15
```

```
!
```

```
!
```

```
!
```

```
ephone  16
```

```
username "user16" password null
```

```
mac-address 0000.0000.000E
```

```
type 7960
```

```
button  1:16
```

```
!
```

```
!
```

```
!
```

```
ephone  17
```

```
username "user17" password null
```

```
mac-address 0000.0000.000F
```

```
type 7960
```

```
button  1:17
```

```
!
```

```
!
```

```
!
```

```
ephone  18
```

```
username "user18" password null
```

```
mac-address 0000.0000.0010
```

```
type 7960
```

```
button  1:18
```

```
!
```

```
!
```

```
!
```

```
ephone  19
```

```
username "user19" password null
```

```
mac-address 0000.0000.0011
```

```
type 7960
```

```
button  1:19
```

```
!
```

```
!
```

```
!
```

```
ephone  20
```

```
username "user20" password null
```

```
mac-address 0000.0000.0012
```

```
type 7960
```

```
button  1:20
```

```
!
```

```
!
```

```
!
```

```
ephone  21
```

```
username "user21" password null
```

```
mac-address 0000.0000.0013
```

```
type 7960
```

```
button  1:21
```

```
!
```

```
!
```

```
!
```

```
ephone  22
```

```
username "user22" password null
```

```
mac-address 0000.0000.0014
```

```
type 7960
```

```
button  1:22
```

```
!
```

```
!
```

```
!
```

```
ephone  23
```

```
username "user23" password null
```

```
mac-address 0000.0000.0015
```

```
type 7960
```

```
button  1:23
```

```
!
```

```
!
```

```
!
```

```
ephone  24
```

```
username "user24" password null
```

```
mac-address 0000.0000.0016
```

```
type 7960
```

```
button  1:24
```

```
!
```

```
!
```

```
!
```

```
line con 0
```

```
exec-timeout 0 0
```

```
line aux 0
```

```
line 2
```

```
no activation-character
```

```
no exec
```

```
transport preferred none
```

```
transort input all
```

```
transport output all
```

```
line vty 0 4 password cisco
```

```
login
```

```
!
```

```
end
```