---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-express-213925-troubleshoot-hun-cd93fd78cd
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-express/213925-troubleshoot-hunt-groups-on-cucme.html
retrieved_at: 2026-08-21T09:47:04.898351+00:00
---

Troubleshoot Hunt Groups on CUCME

# Troubleshoot Hunt Groups on CUCME

### Download Options

Updated: November 21, 2018

Document ID: 213925

Contents

## Contents

## Introduction

This document describes how to troubleshoot hunt-groups on Cisco Unified Communications Manager Express (CUCME).

## Background Information

Hunt groups allow incoming calls to a specific number (pilot number) to be directed to a defined group of extension numbers.

Incoming calls are redirected from the pilot number to the first extension number as defined by the configuration. If the first number is busy or does not answer, the call is redirected to the next phone on the list. A call continues to be redirected on busy or no answer from number to number in the list until it is answered or until the call reaches the number that is defined as the final number.

## Add or Remove Extension From a Hunt-Group

In order to add or remove an extension from the hunt-group use these configuration set:

```
Router#voice hunt-group 35 parallel

Router#final 097

Router#list 885,886, <add new DN/ remove DN >

Router#timeout 30

Router#statistics collect

Router#pilot 035

Router#preference 2 secondary 2
```

## Extension Unable To Logout From Hunt Group

If an extension is unable to logout of the hunt-group, go ahead, redo the configuration of the ephone or the voice register pool, and reset the phone. Ensure that you recreate the configuration files as well.

## Extension Is Logged Out Of The Hunt Group

- Gather the affected extension number and the hunt-group information from the end user.

- Login to the Call Manager Express router and get these outputs:

### For SCCP Phones

Step 1. Collect the following show outputs show ephone-hunt or show ephone-hunt summary or show ephone-hunt <hunt group tag> to identify the ephone-dn’s which are part of that hunt-group.

```
Router#show ephone-hunt

Group 1

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
```

```
Router# show ephone-hunt summary

Group 1

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
```

Gather ephone details :

```
Router#show ephone | b <Directory Number/ Extension Number>

ephone-461[460] Mac:203A.0722.54F3 TCP socket:[67] activeLine:1 whisperLine:0 REGISTERED in SCCP ver 22/17 max_streams=5
mediaActive:1 whisper_mediaActive:0 startMedia:1 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:9
IP:10.128.182.90 * 51189 7965 keepalive 106099 max_line 6 available_line 3 HuntGroupLogout
button 1: cw:1 ccw:(0 0)
dn 203 number 461 CH1 CONNECTED CH2 IDLE huntGroupLogout
button 2: cw:1 ccw:(0 0)
dn 204 number 461 CH1 IDLE CH2 IDLE
button 3: cw:1 ccw:(0 0)
dn 205 number 461 CH1 IDLE CH2 IDLE
speed dial 1:2548876
speed dial 2:6567710
speed dial 3:6528989
Preferred Codec: g711ulaw
Lpcor Type: none Active Call on DN 203 chan 1 :461 10.128.182.90 22082
to 10.121.128.90 2000 via 10.128.182.90
G729 30 bytes no vad
Tx Pkts 10663 bytes 447846 Rx Pkts 10663 bytes 447846 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1 (media path callID 2799007 srcCallID 2799009)
```

Gather hunt-group details:

```
Router#sh ephone-hunt 1

Group 1
type: longest-idle
pilot number: 001, peer-tag 20682
list of numbers:
A482, aux-number A001A0000, # peers 1, logout 0, down 0
on-hook time stamp 3334171983, off-hook agents=1
peer-tag dn-tag rna login/logout up/down
[20681 252 0 login up ]
A454, aux-number A001A0001, # peers 1, logout 1, down 1
on-hook time stamp 3334166112, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20683 223 0 logout down]
*, aux-number A001A0002, # peers 1, logout 0, down 1
on-hook time stamp 3327356688, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20684 0 0 - down]
only one agent available!
preference: 8
preference (sec): 7
members initial state: logout
timeout: 300, 300, 300
max timeout : 10000
description: (Phone Center)
display-logout: Night Service Active
present-call: onhook-phone
hops: 1
E.164 register: yes
auto logout: no
stat collect: no
number of calls in queue: 0
callqueue display: continuously
debug: no
```

Step 2. Redo the Hunt group configuration, or if there is a complain that only one phone is logged-out of the hunt group, then re-configure the Directory Number (DN) and try to reset the phone.

```
Router#config)#no ephone-dn XYZ //Remove the ephone-dn configuration//
Router#config)#ephone-dn XYZ//Add the ephone-dn back again//  Router#(config)#no ephone ABC //Remove the ephone configuration//

Router#(config)#ephone ABC //Add the ephone back again, one command at a time//
Router#(config-ephone)# device-security-mode none
Router#(config-ephone)# mac-address AAAA.BBBB.CCCC
Router#(config-ephone)# ephone-template 1
Cannot update the CNF file for phone-ABC with type (0)

The ephone template tag has been changed under this ephone,
please execute create cnf-files under telephony-services
and restart or reset ephone to take effect.
Router#(config-ephone)# speed-dial 1 YYYYYYY
Router#(config-ephone)# speed-dial 2 XXXXXXX
Router#(config-ephone)# speed-dial 3 NNNNNNN
Router#(config-ephone)# no auto-hold newline
Router#(config-ephone)# type 7965
Router#(config-ephone)# button 1:203 2:204 3:205
Router#(config-ephone)#telephony-service
Router#(config-telephony)#create cnf-files
Creating CNF files
Router#(config-telephony)#end
Router##wr

 

Router##show ephone | b -461 //Verify the ephone configuration with the pre-check//
ephone-461[460] Mac:203A.0722.54F3 TCP socket:[67] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 22/17 max_streams=5
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:9
IP:10.128.182.90 * 50357 7965 keepalive 0 max_line 6 available_line 3
button 1: cw:1 ccw:(0 0)
dn 203 number 461 CH1 IDLE CH2 IDLE
button 2: cw:1 ccw:(0 0)
dn 204 number 461 CH1 IDLE CH2 IDLE
button 3: cw:1 ccw:(0 0)
dn 205 number 461 CH1 IDLE CH2 IDLE
speed dial 1:2548876
speed dial 2:6567710
speed dial 3:6528989
Preferred Codec: g711ulaw
Lpcor Type: none
```

### For SIP Phones

- Collect the following show outputs show voice hunt-group or show voice hunt-group brief or show voice hunt-group <hunt group tag> to identify the ephone-dn which are part of hunt-group.

```
Router# show voice hunt-groupGroup 1    type: longest-idle    preference: 0    preference (sec): 0    timeout: 0    final_number: 1Group 34    type: parallel    pilot number: 3, peer-tag 2147483647    secondary number: 4, peer-tag 2147483646    preference: 0    preference (sec): 0    timeout: 0    final_number: 

 

 

Router##show voice hunt-group 42
Group 42
type: parallel
pilot number: 042, peer-tag 2147483618
secondary number: 642, peer-tag 2147483617
list of numbers:
Member Used-by State Login/Logout====== ======= ===== ============461 461 up logout
462 462 up login
386 386 up login
885 885 up login
886 886 up login
preference: 2
preference (sec): 2
timeout: 30
final_number: 097
stat collect: yes
phone-display: no
```

```
Router#(config)#no voice hunt-group 42 parallel //Remove the hunt-group config//

Router#(config)#voice hunt-group 42 parallel //Redo the hunt-group config//
Router#(config-voice-hunt-group)# final 097
Router#(config-voice-hunt-group)# list 461,462,386,885,886
Router#(config-voice-hunt-group)# timeout 30
Router#(config-voice-hunt-group)# statistics collect
Router#(config-voice-hunt-group)# pilot 042 secondary 642
Router#(config-voice-hunt-group)# preference 2 secondary 2
Router#(config-voice-hunt-group)#end
Router##wr
Building configuration...

Router#show voice hunt-group 42 //Verify the hunt-group config//
Group 42
type: parallel
pilot number: 042, peer-tag 2147483618
secondary number: 642, peer-tag 2147483617
list of numbers:
Member Used-by State Login/Logout

====== ======= ===== ============

461 461 up login
462 462 up login
386 386 up login
885 885 up login
886 886 up login
preference: 2
preference (sec): 2
timeout: 30
final_number: 097
stat collect: yes
phone-display: no
```

- Place a few test calls and check for the resolution.

Router#show ephone ringing

Or

Router#show voice register pool ringing

### Contributed by Cisco Engineers

Nikhil P C

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager Express