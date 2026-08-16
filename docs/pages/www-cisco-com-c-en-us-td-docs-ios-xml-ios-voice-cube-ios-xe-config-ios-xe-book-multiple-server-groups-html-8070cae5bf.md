---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-multiple-server-groups-html-8070cae5bf
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/multiple-server-groups.html
retrieved_at: 2026-08-16T15:45:59.457628+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Server Groups

## Chapter: Server Groups

# Server Groups

## Overview

This feature
                           		configures a server group (group of server addresses) that can be referenced
                           		from an outbound dial peer.

Server groups allow you to create simpler configurations by specifying a list of destination
                           			SIP servers for a single dial peer. When a call matches a dial peer that is configured
                           			with a server group, the destination is selected from the list of candidates based on a
                           			configured preference in the server group. If it is not possible to complete that call,
                           			the next candidate is selected. Alternatively, you can also choose to stop hunting
                           			through the group if a specified response code is received. If the call cannot be placed
                           			to any of the servers in the group, or hunting is stopped, call processing continues to
                           			the next preferred dial-peer.

You can configure server groups for SIP dial peers to include up to five IPv4 or IPv6 target
                           			server addresses listed in strict order of preference, or with equal weight for round
                           			robin or random selection. If a server-group is in the shutdown mode, all dial-peers
                           			using this destination are out of service.

Whenever destination server group is used, and multiple interfaces are involved, ensure that
                                       				all servers in a group are reachable through the network to which the associated
                                       				dial-peer is bound.

If there are session targets of different network, then different dial-peers must be created with appropriate grouping of
                                       the targets with respective binding of the interfaces.

You can use Server Groups only with SIP dial peers.

If a destination IP on the server group responds with codes 404, 500, or 503, the server
                                             						group hunts for the next destination. But if the server group receives codes
                                             						480, 486, or 600, hunting is not supported and hence the server group does
                                             						not hunt to the next destination. Further, the call fails.

Caution

Huntstop is not allowed for the following set of cause codes 401, 407, 415, 417, 422, 480, 485, 486, and 488.

If you attempt to configure one of the listed cause codes specifically, the following CLI error message appears.

Example, huntstop 1 resp-code 401

```
Error: The specified response code cannot be used with Huntstop.
```

If you attempt to configure a range of codes that includes one of those listed, the command will be accepted with the following
                                             warning message.

Example, huntstop 1 resp-code 420 to 430

```
Warning: Range includes code(s) that will not stop hunting.
```

Load Balancing for DNS SRV Hosts can be used as an alternative to Server Groups.

### Feature Information for
                           	 Configuring Server Groups in Outbound Dial Peers

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Server Groups in Outbound Dial Peers

Cisco IOS
                                          				  XE Release 3.11S

15.4(1)T

This
                                          				  feature configures server groups (groups of IPv4 and IPv6 addresses) which can
                                          				  be referenced from an outbound SIP dial peer.

The following command is  introduced under: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) .

Hunt Stop for Server Groups

This feature allows you to configure hunt-stop based on (configurable) response codes in the Server Group.

The following command is introduced under voice class server-group. huntstop rule-tag resp-code from_resp_code to to_resp_code

### Configure Server Groups in Outbound Dial Peers

## Configure Server Groups in Outbound Dial Peers

### SUMMARY STEPS

- enable

- configure terminal

- voice class server-group server-group-id

- { ipv4 | ipv6 } address [ port port ] [ preference preference-order ]

- (Optional) hunt-scheme round-robin

- (Optional) description string

- (Optional) huntstop rule-tag resp-code from_resp_code to to_resp_code

- dial-peer voice dial-peer-id voip

- session protocol sipv2

- destination-pattern [+] string [T]

- session server-group server-group-id

- end

- show voice class server-group server-group-id

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enters privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice class server-group server-group-id

### Example:

```
Device(config)# voice class server-group 171
```

Configures a voice class server group and enters voice class configuration mode.

You can use the shutdown command to make the server group inactive.

Step 4

{ ipv4 | ipv6 } address [ port port ] [ preference preference-order ]

### Example:

```
Device(config-class)# ipv4 10.1.1.1 preference 3
```

Configures a server IP address as a part of this server group along with an optional port number and preference order.

Repeat this step to add up to five servers to the server group.

The servers are not selected by the preference value if round robin is configured in the next step.

Default and highest value of preference is zero.

Step 5

(Optional) hunt-scheme round-robin

### Example:

```
Device(config-class)# hunt-scheme round-robin
```

Defines a hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this
                                          server group) for the setting up of outgoing calls.

If a hunt scheme is not defined, an available IP address of highest preference value is selected. If neither a round-robin
                                                hunt scheme nor a preference value is configured, the selection of servers is random.

Step 6

(Optional) description string

### Example:

```
Device(config-class)# description It has 3 entries
```

Provides a description for the server group.

Step 7

(Optional) huntstop rule-tag resp-code from_resp_code to to_resp_code

### Example:

You can configure hunting in 2 ways, providing the following cause codes -

Range

```
Device(config-class)# huntstop 1 resp-code 400 to 410
```

Standalone

```
Device(config-class)# huntstop 2 resp-code 414
```

Stops hunting for servers in the Server Group based on configurable response codes.

Huntstop rule identifier tags range: 1-1000.

Configurable SIP error response codes range: 400 to 599. The range must be in between 400 and 599 and must be entered in minimum
                                                to maximum order (Example: 450 to 460). You can enter multiple ranges using additional instances of this command. Response
                                                codes do not need to be ordered between instances (Example: huntstop 1 500 to 510 and huntstop 2 400 to 450).

The following error message appears if there is an invalid input for SIP Response codes.

```
Error: Invalid SIP response code range configured for hunt-stop.
```

Overlapping of SIP error response codes configuration is not permitted. For example, huntstop 1 resp-code 400 to 510.

The following error message appears if you try to configure the overlapping SIP error response codes.

```
Error: Overlap of response codes.
```

When one of the cause codes is in the configured range, the following warning message appears.

Example, huntstop 1 resp-code 400 to 405

```
Warning: Range includes codes that will not stop hunting.
```

Step 8

dial-peer voice dial-peer-id voip

### Example:

```
Device(config)# dial-peer voice 123 voip
```

Defines a VoIP dial peer and enters dial peer configuration mode.

Step 9

session protocol sipv2

### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies SIP version 2 as the session protocol for calls between local and remote routers using the packet network.

Step 10

destination-pattern [+] string [T]

### Example:

```
Device(config-dial-peer)# destination-pattern +5550179
```

Specifies either the prefix or the full E.164 telephone number to be used for a dial peer.

Step 11

session server-group server-group-id

### Example:

```
Device(config-dial-peer)# session server-group 171
```

Configures the specified server group as the destination of the dial peer.

This command is available for SIP dial peers only.

If the specified server group is in shutdown mode, the dial peer is not selected to route outgoing calls.

Step 12

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial peer configuration mode and enters privileged EXEC mode.

Step 13

show voice class server-group server-group-id

### Example:

```
Device# show voice class server-group 171
```

Displays information about the voice class server group.

## Verify Server Groups in Outbound Dial Peers

### SUMMARY STEPS

- show voice class server-group [ server-group-id ]

- show running-config | section server-group

### DETAILED STEPS

Step 1

show voice class server-group [ server-group-id ]

The following example displays the configurations for all configured server groups or a specified server group.

### Example:

```
Device# show voice class server-group 1 Voice class server-group: 1
 AdminStatus: Up                 OperStatus: Up
 Hunt-Scheme: preference         Last returned server: 
 Description: It has 3 entries
 Total server entries: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2                                 
 3      ipv4   10.1.1.3
-------------------------------------

 Total Huntstop tags: 2
 Tag ID From Response code       To Response code         
 ------ -------------------      ------------------       
  1     404                      404           
  2     410                      599
 -------------------------------------
```

The following example displays the configurations for dial peers that are associated with server groups.

### Example:

```
Device# show voice class server-group dialpeer 1 Voice class server-group: 1    AdminStatus: Up
 Hunt-Scheme: preference
 Total Remote Targets: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2
 3      ipv4   10.1.1.3
```

Step 2

show running-config | section server-group

The following example displays the running configuration for server groups.

### Example:

```
Device#show running-config | section server-group
voice class server-group 1
ipv4 10.1.1.1 preference 1
ipv4 10.1.1.2 preference 2
ipv4 10.1.1.3 preference 3
description It has 3 entries
huntstop 1 resp-code 404 to 404
huntstop 2 resp-code 410 to 599
voice class server-group 2
ipv4 10.1.1.1
ipv4 10.1.1.2
ipv4 10.1.1.3
description It has 3 entries
hunt-scheme round-robin
huntstop 1 resp-code 401 to 599
```

## Configuration
                        	 Examples for Server Groups in Outbound Dial Peers

### Server Groups in Outbound Dial Peers (Preference-Based Selection)

```
! Configuring the Server Group
Device(config)# voice class server-group 1 Device(config-class)# ipv4 10.1.1.1 preference 1 Device(config-class)# ipv4 10.1.1.2 preference 2 Device(config-class)# ipv4 10.1.1.3 preference 3 Device(config-class)# description It has 3 entries Device (config-class)# huntstop 1 resp-code 404 Device(config-class)# huntstop 2 resp-code 410 to 599 Device(config-class)# exit ! Configuring an outbound SIP dial peer.   
Device(config)# dial-peer voice 1 voip !Associate a destination pattern 
Device(config-dial-peer)# destination-pattern 3001 Device(config-dial-peer)# session protocol sipv2 !Associate a server group with the dial peer
Device(config-dial-peer)# session server-group 1 Device(config-dial-peer)# end ! Displays the configurations made for the outbound dial peer 181 associated with a server group
Device# show voice class server-group dialpeer 1 Voice class server-group: 1    AdminStatus: Up
 Hunt-Scheme: preference
 Total Remote Targets: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2
 3      ipv4   10.1.1.3

! Displays the configurations made for the server group.

Device# show voice class server-group 1 Voice class server-group: 1
 AdminStatus: Up                 OperStatus: Up
 Hunt-Scheme: preference         Last returned server: 
 Description: It has 3 entries
 Total server entries: 3
 
 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2
 3      ipv4   10.1.1.3

-------------------------------------

 Total Huntstop tags: 2
 Tag ID From Response code       To Response code         
 ------ -------------------      ------------------       
  1     404                      404           
  2     410                      599
 -------------------------------------
```

### Server Groups in Outbound Dial Peers (Round-Robin-Based Selection)

```
! Configuring the Server Group
Device(config)# voice class server-group 2 Device(config-class)# ipv4 10.1.1.1 Device(config-class)# ipv4 10.1.1.2 Device(config-class)# ipv4 10.1.1.3 Device(config-class)# hunt-scheme round-robin Device(config-class)# huntstop 1 resp-code 401 to 599 Device(config-class)# description It has 3 entries Device(config-class)# exit ! Configuring an outbound SIP dial peer.   
Device(config)# dial-peer voice 2 voip ! Associate a destination pattern 
Device(config-dial-peer)# destination-pattern 3001 Device(config-dial-peer)# session protocol sipv2 ! Associate a server group with the dial peer
Device(config-dial-peer)# session server-group 2 Device(config-dial-peer)# end ! Displays the configurations made for the outbound dial peer 181 associated with a server group
Device# show voice class server-group dialpeer 2 Voice class server-group: 2    AdminStatus: Up
 Hunt-Scheme: round-robin
 Total Remote Targets: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 0      ipv4   10.1.1.3
 0      ipv4   10.1.1.1
 0      ipv4   10.1.1.2

! Displays the configurations made for the server group.
Device# show voice class server-group 2 Voice class server-group: 2
 AdminStatus: Up                 OperStatus: Up
 Hunt-Scheme: round-robin        Last returned server: 10.1.1.2
 Description: It has 3 entries
 Total server entries: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 0      ipv4   10.1.1.1
 0      ipv4   10.1.1.2
 0      ipv4   10.1.1.3

-------------------------------------

 Total Huntstop tags: 1
 Tag ID From Response code       To Response code         
 ------ -------------------      ------------------       
  1     401                      599           
 -------------------------------------
```

| Note | Whenever destination server group is used, and multiple interfaces are involved, ensure that
                                       				all servers in a group are reachable through the network to which the associated
                                       				dial-peer is bound. If there are session targets of different network, then different dial-peers must be created with appropriate grouping of
                                       the targets with respective binding of the interfaces. |
|---|---|

| Note | You can use Server Groups only with SIP dial peers. If a destination IP on the server group responds with codes 404, 500, or 503, the server
                                             						group hunts for the next destination. But if the server group receives codes
                                             						480, 486, or 600, hunting is not supported and hence the server group does
                                             						not hunt to the next destination. Further, the call fails. |
|---|---|

| Caution | Huntstop is not allowed for the following set of cause codes 401, 407, 415, 417, 422, 480, 485, 486, and 488. If you attempt to configure one of the listed cause codes specifically, the following CLI error message appears. Example, huntstop 1 resp-code 401 Error: The specified response code cannot be used with Huntstop. If you attempt to configure a range of codes that includes one of those listed, the command will be accepted with the following
                                             warning message. Example, huntstop 1 resp-code 420 to 430 Warning: Range includes code(s) that will not stop hunting. |
|---|---|

| Note | Load Balancing for DNS SRV Hosts can be used as an alternative to Server Groups. |
|---|---|

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Server Groups in Outbound Dial Peers | Cisco IOS
                                          				  XE Release 3.11S 15.4(1)T | This
                                          				  feature configures server groups (groups of IPv4 and IPv6 addresses) which can
                                          				  be referenced from an outbound SIP dial peer. The following command is  introduced under: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) . |
| Hunt Stop for Server Groups | Cisco IOS XE Bengaluru 17.4.1a | This feature allows you to configure hunt-stop based on (configurable) response codes in the Server Group. The following command is introduced under voice class server-group. huntstop rule-tag resp-code from_resp_code to to_resp_code |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice class server-group server-group-id Example: Device(config)# voice class server-group 171 | Configures a voice class server group and enters voice class configuration mode. You can use the shutdown command to make the server group inactive. |
| Step 4 | { ipv4 \| ipv6 } address [ port port ] [ preference preference-order ] Example: Device(config-class)# ipv4 10.1.1.1 preference 3 | Configures a server IP address as a part of this server group along with an optional port number and preference order. Repeat this step to add up to five servers to the server group. The servers are not selected by the preference value if round robin is configured in the next step. Default and highest value of preference is zero. |
| Step 5 | (Optional) hunt-scheme round-robin Example: Device(config-class)# hunt-scheme round-robin | (Optional) Defines a hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this
                                          server group) for the setting up of outgoing calls. If a hunt scheme is not defined, an available IP address of highest preference value is selected. If neither a round-robin
                                                hunt scheme nor a preference value is configured, the selection of servers is random. |
| Step 6 | (Optional) description string Example: Device(config-class)# description It has 3 entries | (Optional) Provides a description for the server group. |
| Step 7 | (Optional) huntstop rule-tag resp-code from_resp_code to to_resp_code Example: You can configure hunting in 2 ways, providing the following cause codes - Range Device(config-class)# huntstop 1 resp-code 400 to 410 Standalone Device(config-class)# huntstop 2 resp-code 414 | (Optional) Stops hunting for servers in the Server Group based on configurable response codes. Huntstop rule identifier tags range: 1-1000. Configurable SIP error response codes range: 400 to 599. The range must be in between 400 and 599 and must be entered in minimum
                                                to maximum order (Example: 450 to 460). You can enter multiple ranges using additional instances of this command. Response
                                                codes do not need to be ordered between instances (Example: huntstop 1 500 to 510 and huntstop 2 400 to 450). The following error message appears if there is an invalid input for SIP Response codes. Error: Invalid SIP response code range configured for hunt-stop. Overlapping of SIP error response codes configuration is not permitted. For example, huntstop 1 resp-code 400 to 510. The following error message appears if you try to configure the overlapping SIP error response codes. Error: Overlap of response codes. When one of the cause codes is in the configured range, the following warning message appears. Example, huntstop 1 resp-code 400 to 405 Warning: Range includes codes that will not stop hunting. |
| Step 8 | dial-peer voice dial-peer-id voip Example: Device(config)# dial-peer voice 123 voip | Defines a VoIP dial peer and enters dial peer configuration mode. |
| Step 9 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies SIP version 2 as the session protocol for calls between local and remote routers using the packet network. |
| Step 10 | destination-pattern [+] string [T] Example: Device(config-dial-peer)# destination-pattern +5550179 | Specifies either the prefix or the full E.164 telephone number to be used for a dial peer. |
| Step 11 | session server-group server-group-id Example: Device(config-dial-peer)# session server-group 171 | Configures the specified server group as the destination of the dial peer. This command is available for SIP dial peers only. If the specified server group is in shutdown mode, the dial peer is not selected to route outgoing calls. |
| Step 12 | end Example: Device(config-dial-peer)# end | Exits dial peer configuration mode and enters privileged EXEC mode. |
| Step 13 | show voice class server-group server-group-id Example: Device# show voice class server-group 171 | Displays information about the voice class server group. |

| Step 1 | show voice class server-group [ server-group-id ] The following example displays the configurations for all configured server groups or a specified server group. Example: Device# show voice class server-group 1 Voice class server-group: 1
 AdminStatus: Up                 OperStatus: Up
 Hunt-Scheme: preference         Last returned server: 
 Description: It has 3 entries
 Total server entries: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2                                 
 3      ipv4   10.1.1.3
-------------------------------------

 Total Huntstop tags: 2
 Tag ID From Response code       To Response code         
 ------ -------------------      ------------------       
  1     404                      404           
  2     410                      599
 ------------------------------------- The following example displays the configurations for dial peers that are associated with server groups. Example: Device# show voice class server-group dialpeer 1 Voice class server-group: 1    AdminStatus: Up
 Hunt-Scheme: preference
 Total Remote Targets: 3

 Pref   Type   IP Address                               IP Port
 ----   ----   ----------                               -------
 1      ipv4   10.1.1.1
 2      ipv4   10.1.1.2
 3      ipv4   10.1.1.3 |
|---|---|
| Step 2 | show running-config \| section server-group The following example displays the running configuration for server groups. Example: Device#show running-config \| section server-group
voice class server-group 1
ipv4 10.1.1.1 preference 1
ipv4 10.1.1.2 preference 2
ipv4 10.1.1.3 preference 3
description It has 3 entries
huntstop 1 resp-code 404 to 404
huntstop 2 resp-code 410 to 599
voice class server-group 2
ipv4 10.1.1.1
ipv4 10.1.1.2
ipv4 10.1.1.3
description It has 3 entries
hunt-scheme round-robin
huntstop 1 resp-code 401 to 599 |