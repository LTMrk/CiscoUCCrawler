---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-multiple-outbound-dial-peer-html-3d06bb5dd0
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_multiple-outbound-dial-peer.html
retrieved_at: 2026-08-16T15:45:50.955916+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Outbound Dial Peer Group as an Inbound Dial-Peer Destination

## Chapter: Outbound Dial Peer Group as an Inbound Dial-Peer Destination

# Outbound Dial Peer Group as an Inbound Dial-Peer Destination

## Overview

This feature can
                           		group multiple outbound dial peers into a dial-peer group and configure this
                           		dial-peer group as the destination of an inbound dial peer.

You can group up to 20 outbound (SIP) dial peers into a dial-peer group and configure this dial-peer group as the destination
                           of an inbound dial peer. Once an incoming call is matched by an inbound dial peer with an active destination dial-peer group,
                           dial peers from this group are used to route the incoming call. No other outbound dial-peer provisioning to select outbound
                           dial peers is used.

A preference can be defined for each dial peer in a dial-peer group. This preference is used to decide the order of selection
                           of dial peers from the group for the setup of an outgoing call.

You can also specify various dial-peer hunt mechanism using the existing dial-peer hunt command.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Support for
                                          				  POTS dial-peer

Baseline Functionality

An outgoing
                                          				  POTS dial peer can be part of a dial-peer group. An inbound POTS dial peer can
                                          				  have a dial-peer group as the destination.

## Restrictions

If a dial-peer group is in the shutdown state, regular dial-peer search occurs.

If all dial-peers in an active dial-peer group are unavailable, call is disconnected.

Calls are statically routed to one of the dial-peers in the active dial-peer group.

The destination-pattern command is required on the outbound dial-peer even though matching is not done based on this command.

The outgoing
                                    				call setup is deferred until inter-digit timer expires or a terminator is
                                    				entered.

Dial-peer group works only with valid E.164 pattern.

### For POTS dial-peers:

Two-stage
                                    				dialing is not supported.

Overlapping
                                    				dialing is not supported.

TCL and VXML
                                    				routing changes are not supported.

Digit-stripping is not supported.

## Configure Outbound Dial-Peer Group as an Inbound Dial-Peer Destination

Perform this
                              		  task to configure a dial-peer group with multiple outbound peers and an inbound
                              		  dial peer referencing this dial-peer group as a destination.

### Before you begin

Configure SIP outbound dial peers to be associated with a dial-peer group.

For an
                                    				outbound POTS dial peer, ensure that destination-pattern
                                          					 .T and no
                                          					 digit-strip are configured to avoid unexpected dialed digit
                                    				strip.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice outbound-dial-peer-id [ voip | pots ]

- destination-pattern pattern

- no digit-strip for POTS dial peers.

- exit

- (Optional) dial-peer hunt hunt-order-number

- voice class dpg dial-peer-group-id

- dial-peer outbound-dial-peer-id [ preference preference-order ]

- (Optional) description string

- exit

- dial-peer voice inbound-dial-peer-id [ voip | pots ]

- destination dpg dial-peer-group-id

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enters
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

dial-peer voice outbound-dial-peer-id [ voip | pots ]

### Example:

```
Device(config)# dial-peer voice 123 voip
```

### Example:

```
Device(config)# dial-peer voice 345 pots
```

Defines a dial peer and enters dial peer configuration mode.

Step 4

destination-pattern pattern

### Example:

```
Device(config-dial-peer)# destination-pattern 1004
```

### Example:

```
Device(config-dial-peer)# destination-pattern .T
```

Configures a destination pattern. This step is required even
                                          				though the value is not used for dial-peer matching.

Step 5

no digit-strip for POTS dial peers.

### Example:

```
Device(config-dial-peer)# no digit-strip
```

Disable unexpected dialed digit strip.

Step 6

exit

### Example:

```
Device(config-dial-peer)# exit
```

Exits to global configuration mode.

Step 7

(Optional) dial-peer hunt hunt-order-number

### Example:

```
Device(config)# dial-peer hunt 0
```

Specifies a
                                          				hunt selection mechanism for dial peers.

The default mechanism is random selection.

Step 8

voice class dpg dial-peer-group-id

### Example:

```
Device(config)# voice class dpg 181
```

Creates a
                                          				dial-peer group for grouping multiple outbound dial peers and enters voice
                                          				class configuration mode.

You can use the shutdown command to resume regular outbound dial-peer provisioning in dial-peers with this dial-peer group as destination.

Step 9

dial-peer outbound-dial-peer-id [ preference preference-order ]

### Example:

```
Device(config-class)# dial-peer 123 preference 1
```

Associates a
                                          				configured outbound dial peer with this dial-peer group and configures a
                                          				preference value.

Repeat this step for all outbound dial-peers that need to be added to this dial-peer group.

If preference is not specified, the order of selection is random or as specified by the dial-peer hunt command.

Step 10

(Optional) description string

### Example:

```
Device(config-class)# description Boston Destination
```

Provides a
                                          				description for the dial-peer group.

Step 11

exit

### Example:

```
Device(config-class)# exit
```

Exits voice
                                          				class configuration mode and enters global configuration mode.

Step 12

dial-peer voice inbound-dial-peer-id [ voip | pots ]

### Example:

```
Device(config)# dial-peer voice 789 voip
```

### Example:

```
Device(config)# dial-peer voice 678 pots
```

Defines a dial
                                          				peer and enters dial peer configuration mode.

Step 13

destination dpg dial-peer-group-id

### Example:

```
Device(config-dial-peer)# destination dpg 181
```

Specifies a
                                          				dial peer group from which an outbound dial peer can be chosen.

Step 14

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer configuration mode and enters privileged EXEC mode.

## Verifying Outbound
                        	 Dial-Peer Groups as an Inbound Dial-Peer Destination

### SUMMARY STEPS

- show voice class
                                    				  dpg dial-peer-group-id

- show dial-peer voice inbound-dial-peer-id

### DETAILED STEPS

Step 1

show voice class
                                             				  dpg dial-peer-group-id

Displays the
                                          				configuration of an outbound dial-peer group.

### Example:

```
Device# show voice class dpg 200 Voice class dpg: 200     AdminStatus: Up
 Description: Boston Destination
 Total dial-peer entries: 4

 Peer Tag       Pref
 --------       ----
 1001           1
 1002           2
 1004           0
 1003           1
-------------------------------------
```

Step 2

show dial-peer voice inbound-dial-peer-id

Displays the
                                          				referencing of destination dial-peer group from an inbound dial peer.

### Example:

```
Device# show dial-peer voice 100 | include destination dpg destination dpg tag = 200 status = valid,
```

## Troubleshooting
                        	 Tips

### SUMMARY STEPS

- Enter the
                              			 following:

- debug voip dialpeer inout

- debug voip ccapi inout

### DETAILED STEPS

Enter the
                                       			 following:

- debug voip dialpeer inout

- debug voip ccapi inout

Displays the
                                          				configuration of an outbound dial-peer group.

### Example:

```
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchCore:
   Dial String=4001, Expanded String=4001, Calling Number=
   Timeout=TRUE, Is Incoming=TRUE, Peer Info Type=DIALPEER_INFO_SPEECH
*Jul 19 10:15:53.310 IST: //-1/xxxxxxxxxxxx/DPM/vepm_match_pattern_map:
   DEPM 1000 use caching dialstring 4001 status 0
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/MatchNextPeer:
```

Incoming dial
                                          				peer is first matched:

```
Result=Success(0); Incoming Dial-peer=600 Is Matched *Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeertype:exit@6602
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=600
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchSafModulePlugin:
   dialstring=NULL, saf_enabled=0, saf_dndb_lookup=0, dp_result=0
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpAssociateIncomingPeerSPI:exit@7181
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore:
   Calling Number=, Called Number=4001, Peer Info Type=DIALPEER_INFO_SPEECH
```

The dial-peer
                                          				group associated with a dial peer is selected:

```
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore: Outbound Destination DPG Group Request; Destination DPG=1 *Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchDestDPGroup:
   Result=0
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore:
   Result=SUCCESS(0) after DestDPGroup
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchSafModulePlugin:
   dialstring=4001, saf_enabled=0, saf_dndb_lookup=1, dp_result=0
```

List of active
                                          				Dial-peers configured within the DPG, sorted by preference:

```
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersMoreArg:
   Result=SUCCESS(0) List of Matched Outgoing Dial-peer(s):
     1: Dial-peer Tag=1004
     2: Dial-peer Tag=1001
     3: Dial-peer Tag=1003 
     4: Dial-peer Tag=1002
```

## Configuration
                        	 Examples for Outbound Dial Peer Group as an Inbound Dial-Peer
                        	 Destination

```
Device> enable Device# configure terminal ! Configuring outbound dial peers that are to be grouped.
Device(config)# dial-peer voice 1001 voip Device(config-dial-peer)# destination-pattern 1001 Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# session target ipv4:10.1.1.1 Device(config-dial-peer)# exit Device(config)# dial-peer voice 1002 voip Device(config-dial-peer)# destination-pattern 1002 Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# session target ipv4:10.1.1.2 Device(config-dial-peer)# exit Device(config)# dial-peer voice 1003 voip Device(config-dial-peer)# destination-pattern 1003 Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# session target ipv4:10.1.1.3 Device(config-dial-peer)# exit Device(config)# dial-peer voice 1004 pots Device(config-dial-peer)# destination-pattern 5... Device(config-dial-peer)# no digit-strip Device(config-dial-peer)# direct-inward-dial Device(config-dial-peer)# port 1/0/0:23 Device(config-dial-peer)# forward-digits all Device(config-dial-peer)# exit !Grouping outbound dial peers and configuring preferences if needed.
Device(config)# voice class dpg 200 Device(config-class)# dial-peer 1001 preference 1 Device(config-class)# dial-peer 1002 preference 2 Device(config-class)# dial-peer 1003 preference 3 Device(config-class)# dial-peer 1004 preference 4 Device(config-class)# description Boston Destination Device(config-class)# exit !Associating outbound dial peer group with an inbound dial peer group.
Device(config)# dial-peer voice 100 voip Device(config-dial-peer)# incoming called-number 13411 Device(config-dial-peer)# destination dpg 200 Device(config-dial-peer)# end !Associating outbound dial peer group with an inbound POTS dial peer group.
Device(config)# dial-peer voice 600 pots Device(config-dial-peer)# incoming called-number 4T Device(config-dial-peer)# destination dpg 200 Device(config-dial-peer)# end
```

### Verifying
                              		  Outbound Dial-Peer Group Configuration

```
Device# show voice class dpg 200 Voice class dpg: 200     AdminStatus: Up
 Description: Boston Destination
 Total dial-peer entries: 4

 Peer Tag       Pref
 --------       ----
 1001           1
 1002           2
 1004           0
 1003           1
-------------------------------------
```

### Verifying
                              		  Inbound Dial-Peer Referencing Outbound Dial-Peer Group

```
Device# show dial-peer voice 100 | include destination dpg destination dpg tag = 200 status = valid,
```

```
Device# show dial-peer voice 600 | include destination dpg destination dpg tag = 200 status = valid,
```

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Support for
                                          				  POTS dial-peer | Baseline Functionality | An outgoing
                                          				  POTS dial peer can be part of a dial-peer group. An inbound POTS dial peer can
                                          				  have a dial-peer group as the destination. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | dial-peer voice outbound-dial-peer-id [ voip \| pots ] Example: For VoIP dial peer: Device(config)# dial-peer voice 123 voip Example: For POTS dial peer: Device(config)# dial-peer voice 345 pots | Defines a dial peer and enters dial peer configuration mode. |
| Step 4 | destination-pattern pattern Example: For VoIP Dial Peers Device(config-dial-peer)# destination-pattern 1004 Example: For POTS Dial Peers Device(config-dial-peer)# destination-pattern .T | Configures a destination pattern. This step is required even
                                          				though the value is not used for dial-peer matching. |
| Step 5 | no digit-strip for POTS dial peers. Example: Device(config-dial-peer)# no digit-strip | Disable unexpected dialed digit strip. |
| Step 6 | exit Example: Device(config-dial-peer)# exit | Exits to global configuration mode. |
| Step 7 | (Optional) dial-peer hunt hunt-order-number Example: Device(config)# dial-peer hunt 0 | (Optional) Specifies a
                                          				hunt selection mechanism for dial peers. The default mechanism is random selection. |
| Step 8 | voice class dpg dial-peer-group-id Example: Device(config)# voice class dpg 181 | Creates a
                                          				dial-peer group for grouping multiple outbound dial peers and enters voice
                                          				class configuration mode. You can use the shutdown command to resume regular outbound dial-peer provisioning in dial-peers with this dial-peer group as destination. |
| Step 9 | dial-peer outbound-dial-peer-id [ preference preference-order ] Example: Device(config-class)# dial-peer 123 preference 1 | Associates a
                                          				configured outbound dial peer with this dial-peer group and configures a
                                          				preference value. Repeat this step for all outbound dial-peers that need to be added to this dial-peer group. If preference is not specified, the order of selection is random or as specified by the dial-peer hunt command. |
| Step 10 | (Optional) description string Example: Device(config-class)# description Boston Destination | (Optional) Provides a
                                          				description for the dial-peer group. |
| Step 11 | exit Example: Device(config-class)# exit | Exits voice
                                          				class configuration mode and enters global configuration mode. |
| Step 12 | dial-peer voice inbound-dial-peer-id [ voip \| pots ] Example: For VoIP dial
                                          				peer: Device(config)# dial-peer voice 789 voip Example: For POTS
                                          				dial peer: Device(config)# dial-peer voice 678 pots | Defines a dial
                                          				peer and enters dial peer configuration mode. |
| Step 13 | destination dpg dial-peer-group-id Example: Device(config-dial-peer)# destination dpg 181 | Specifies a
                                          				dial peer group from which an outbound dial peer can be chosen. |
| Step 14 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer configuration mode and enters privileged EXEC mode. |

| Step 1 | show voice class
                                             				  dpg dial-peer-group-id Displays the
                                          				configuration of an outbound dial-peer group. Example: Device# show voice class dpg 200 Voice class dpg: 200     AdminStatus: Up
 Description: Boston Destination
 Total dial-peer entries: 4

 Peer Tag       Pref
 --------       ----
 1001           1
 1002           2
 1004           0
 1003           1
------------------------------------- |
|---|---|
| Step 2 | show dial-peer voice inbound-dial-peer-id Displays the
                                          				referencing of destination dial-peer group from an inbound dial peer. Example: Device# show dial-peer voice 100 \| include destination dpg destination dpg tag = 200 status = valid, |

| Enter the
                                       			 following: debug voip dialpeer inout debug voip ccapi inout Displays the
                                          				configuration of an outbound dial-peer group. Example: *Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchCore:
   Dial String=4001, Expanded String=4001, Calling Number=
   Timeout=TRUE, Is Incoming=TRUE, Peer Info Type=DIALPEER_INFO_SPEECH
*Jul 19 10:15:53.310 IST: //-1/xxxxxxxxxxxx/DPM/vepm_match_pattern_map:
   DEPM 1000 use caching dialstring 4001 status 0
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/MatchNextPeer: Incoming dial
                                          				peer is first matched: Result=Success(0); Incoming Dial-peer=600 Is Matched *Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeertype:exit@6602
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpAssociateIncomingPeerCore:
   Result=Success(0) after DP_MATCH_INCOMING_DNIS; Incoming Dial-peer=600
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpMatchSafModulePlugin:
   dialstring=NULL, saf_enabled=0, saf_dndb_lookup=0, dp_result=0
*Jul 19 10:15:53.310 IST: //-1/ED647BD1B0F9/DPM/dpAssociateIncomingPeerSPI:exit@7181
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore:
   Calling Number=, Called Number=4001, Peer Info Type=DIALPEER_INFO_SPEECH The dial-peer
                                          				group associated with a dial peer is selected: *Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore: Outbound Destination DPG Group Request; Destination DPG=1 *Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchDestDPGroup:
   Result=0
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersCore:
   Result=SUCCESS(0) after DestDPGroup
*Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchSafModulePlugin:
   dialstring=4001, saf_enabled=0, saf_dndb_lookup=1, dp_result=0 List of active
                                          				Dial-peers configured within the DPG, sorted by preference: *Jul 19 10:15:53.311 IST: //-1/ED647BD1B0F9/DPM/dpMatchPeersMoreArg:
   Result=SUCCESS(0) List of Matched Outgoing Dial-peer(s):
     1: Dial-peer Tag=1004
     2: Dial-peer Tag=1001
     3: Dial-peer Tag=1003 
     4: Dial-peer Tag=1002 |
|---|