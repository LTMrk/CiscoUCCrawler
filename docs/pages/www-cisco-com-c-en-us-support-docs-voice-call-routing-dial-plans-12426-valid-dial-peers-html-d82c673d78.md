---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-12426-valid-dial-peers-html-d82c673d78
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/12426-valid-dial-peers.html
retrieved_at: 2026-08-20T23:24:31.963788+00:00
---

Understand the Operational Status of Dial Peers on Cisco IOS Platforms

# Understand the Operational Status of Dial Peers on Cisco IOS Platforms

### Download Options

Updated: February 2, 2006

Document ID: 12426

Contents

## Contents

## Introduction

This document describes how to understand the operational status of dial peers on Cisco IOS® platforms.

## Prerequisites

### Requirements

Readers of this document should have knowledge of these topics:

Understanding Dial Peers and Call Legs on Cisco IOS Platforms

Understanding Inbound and Outbound Dial Peers on Cisco IOS Platforms

If Voice-Network (VoIP, VoFR, VoATM) and POTS dial-peers are not valid and in the "operational status", they are not considered for the Cisco IOS router/gateway inbound and outbound dial-peer matching process. In order to be considered valid/operational, dial-peers must meet one of these criteria:

Destination-pattern and a voice-port or session target is configured.

Incoming called-number is configured.

Answer-address is configured.

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command. This document is not restricted to specific software and hardware versions.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Invalid Dial-Peer Configurations

Based on the previous three rule criteria, this table displays examples of dial-peer configurations that are in the down operational status.

```
dial-peer voice 1 pots 
  port 1/0:23 !--- Invalid dial-peer (rule 1): Has voice-port configured only. !
 dial-peer voice 2 pots
  destination-pattern 1T !--- Invalid dial-peer (rule 1): Has destination-pattern configured only. !
 dial-peer voice 6 voip
  session target ipv4:172.16.13.111 !--- Invalid dial-peer (rule 1): Has session target configured only. !
 dial-peer voice 7 voip
  destination-pattern 83... !--- Invalid dial-peer (rule 1): Has destination-pattern configured only. !
```

Note: A dial-peer configuration statement without any subcommands is considered invalid by violation of 1, 2, and 3.

## Valid Dial-Peer Configurations

Based on the previous three rule criteria, this table displays examples of dial-peer configurations that are in up operational status.

```
dial-peer voice 3 pots
  destination-pattern 1T          
  port 1/0:23
  prefix 1 !--- Valid dial-peer (rule 1): Has voice-port and destination-pattern configured. !
 dial-peer voice 4 pots
  incoming called-number 83. !--- Valid dial-peer (rule 2): Has incoming called-number configured. !
 dial-peer voice 5 pots
  answer-address 408 !--- Valid dial-peer (rule 2): Has answer-address configured. ss configured. 
 !
 dial-peer voice 8 voip
  destination-pattern 83...
  session target ipv4:172.16.13.111 !--- Valid dial-peer (rule 1): Has session target and destination-pattern configured. !
 dial-peer voice 9 voip
  incoming called-number . !--- Valid dial-peer (rule 2): Has incoming called-number configured. !
 dial-peer voice 10 voip    
  answer-address 6666 !--- Valid dial-peer (rule 2): Has answer-address configured. !
```

Note: Assume a dial-peer intended for inbound matching has an incoming called-number or an answer-address configured and a destination-pattern command is added. After you add the command destination-pattern string , the dial-peer goes operationally down. This is because the router maps a destination-pattern to an address ( session target ) or a voice-port ( port ) for outbound dial-peer matching purposes. In this scenario there is nothing to map to. For example, if you add a destination-pattern on dial-peer 4, 5, 9 and 10, they change their operational status to down.

Note: On dial-peer 4 and 5, if you remove the destination-pattern and add a port command, the dial-peers remain valid. Similarly if we remove the destination-pattern and add the session-target command on 9 and 10, they also remain operational.

## Check the Dial-Peer Configuration

In order to check the validity of the dial peer configuration, use the Cisco IOS command show dial-peer voice summary .

```
2600# show dial-peer voice summary dial-peer hunt 0
                                                       PASS
   TAG TYPE   ADMIN OPER PREFIX   DEST-PATTERN    PREF THRU SESS-TARGET    PORT
     1 pots   up    down                           0                       1/0:23
     2 pots   up    down          1T               0                       
     3 pots   up    up   1        1T               0                       1/0:23
     4 pots   up    up                             0                       
     5 pots   up    up                             0                       
     6 voip   up    down                           0   syst ipv4:172.16.13.111  
     7 voip   up    down          83...            0   syst                     
     8 voip   up    up            83...            0   syst ipv4:172.16.13.111  
     9 voip   up    up                             0   syst                     
    10 voip   up    up                             0   syst
```

### Revision History

1.0

06-Dec-2001

Initial Release

### Contributed by Cisco Engineers

ccastano

| Dial Peer Examples |
|---|
| dial-peer voice 1 pots 
  port 1/0:23 !--- Invalid dial-peer (rule 1): Has voice-port configured only. !
 dial-peer voice 2 pots
  destination-pattern 1T !--- Invalid dial-peer (rule 1): Has destination-pattern configured only. !
 dial-peer voice 6 voip
  session target ipv4:172.16.13.111 !--- Invalid dial-peer (rule 1): Has session target configured only. !
 dial-peer voice 7 voip
  destination-pattern 83... !--- Invalid dial-peer (rule 1): Has destination-pattern configured only. ! |

| Valid Peer Examples |
|---|
| dial-peer voice 3 pots
  destination-pattern 1T          
  port 1/0:23
  prefix 1 !--- Valid dial-peer (rule 1): Has voice-port and destination-pattern configured. !
 dial-peer voice 4 pots
  incoming called-number 83. !--- Valid dial-peer (rule 2): Has incoming called-number configured. !
 dial-peer voice 5 pots
  answer-address 408 !--- Valid dial-peer (rule 2): Has answer-address configured. ss configured. 
 !
 dial-peer voice 8 voip
  destination-pattern 83...
  session target ipv4:172.16.13.111 !--- Valid dial-peer (rule 1): Has session target and destination-pattern configured. !
 dial-peer voice 9 voip
  incoming called-number . !--- Valid dial-peer (rule 2): Has incoming called-number configured. !
 dial-peer voice 10 voip    
  answer-address 6666 !--- Valid dial-peer (rule 2): Has answer-address configured. ! |

| Check the Dial-Peer Configuration |
|---|
| 2600# show dial-peer voice summary dial-peer hunt 0
                                                       PASS
   TAG TYPE   ADMIN OPER PREFIX   DEST-PATTERN    PREF THRU SESS-TARGET    PORT
     1 pots   up    down                           0                       1/0:23
     2 pots   up    down          1T               0                       
     3 pots   up    up   1        1T               0                       1/0:23
     4 pots   up    up                             0                       
     5 pots   up    up                             0                       
     6 voip   up    down                           0   syst ipv4:172.16.13.111  
     7 voip   up    down          83...            0   syst                     
     8 voip   up    up            83...            0   syst ipv4:172.16.13.111  
     9 voip   up    up                             0   syst                     
    10 voip   up    up                             0   syst |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Dec-2001 | Initial Release |