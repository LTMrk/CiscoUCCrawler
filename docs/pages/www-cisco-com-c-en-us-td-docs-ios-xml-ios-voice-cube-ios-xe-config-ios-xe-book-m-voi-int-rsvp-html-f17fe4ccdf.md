---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-int-rsvp-html-f17fe4ccdf
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-int-rsvp.html
retrieved_at: 2026-08-16T15:48:52.919798+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Interworking Between RSVP Capable and RSVP Incapable Networks

## Chapter: Interworking Between RSVP Capable and RSVP Incapable Networks

# Interworking Between RSVP Capable and RSVP Incapable Networks

The Interworking Between RSVP Capable and RSVP Incapable Networks feature provides precondition-based Resource Reservation
                        Protocol (RSVP) support for basic audio call and supplementary services on Cisco Unified Border Element (UBE). This feature
                        improves the interoperability between RSVP and non-RSVP networks. RSVP functionality added to Cisco UBE helps you to reserve
                        the required bandwidth before making a call.

This feature extends RSVP support to delayed-offer to delayed-offer and delayed-offer to early-offer calls, along with the
                        early-offer to early-offer calls.

## Feature Information for Interworking Between RSVP Capable and RSVP Incapable Networks

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Interworking Between RSVP Capable and RSVP Incapable Networks

Baseline Functionality

The Interworking between RSVP Capable and RSVP Incapable Networks feature provides precondition-based RSVP support for basic
                                          audio call and supplementary services on the Cisco UBE.

The following commands were introduced or modified: acc-qos , ip qos defending-priority , ip qos dscp , ip qos policy-locator , ip qos preemption-priority , req-qos , voice-class sip rsvp-fail-policy

## Prerequisites for Interworking Between RSVP Capable and RSVP Incapable Networks

RSVP policies allow you to configure separate bandwidth pools with varying limits so that any one application, such as video,
                                 can consume all the RSVP bandwidth on a specified interface at the expense of other applications, such as voice, which would
                                 be dropped.

To limit bandwidth per application, you must configure a bandwidth limit before configuring Support for the Interworking Between
                                 RSVP Capable and RSVP Incapable Networks feature. See Configure RSVP on an Interface .

## Restrictions for Interworking Between RSVP Capable and RSVP Incapable Networks

The Support for Interworking Between RSVP Capable and RSVP Incapable Networks feature has the following restrictions:

Segmented RSVP is not supported.

Interoperability between Cisco UBE and Cisco Unified Communications Manager is not available.

RSVP-enabled video calls are not supported.

## How to Configure Interworking Between RSVP Capable and RSVP Incapable Networks

### Configure RSVP on an Interface

You must allocate some bandwidth for the interface before enabling RSVP. Perform this task to configure RSVP on an interface.

### SUMMARY STEPS

- enable

- configure terminal

- interface type slot / port

- ip rsvp bandwidth [ reservable-bw [ max-reservable-bw ] [ sub-pool reservable-bw ]]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

interface type slot / port

#### Example:

```
Device(config)# interface FastEthernet 0/1
```

Configures an interface type and enters interface configuration mode.

Step 4

ip rsvp bandwidth [ reservable-bw [ max-reservable-bw ] [ sub-pool reservable-bw ]]

#### Example:

```
Device(config-if)# ip rsvp bandwidth 10000 100000
```

Enables RSVP for IP on an interface.

Step 5

end

#### Example:

```
Device(config-if)# end
```

(Optional) Exits interface configuration mode and returns to privileged EXEC mode.

### Configuring Optional RSVP on the Dial Peer

Perform this task to configure optional RSVP at the dial peer level. This configuration allows you to have uninterrupted
                                 call even if there is a failure in bandwidth reservation.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- no acc-qos { controlled-load | guaranteed-delay } [ audio | video ]

- req-qos { controlled-load | guaranteed-delay } [ audio | video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer 77 voip
```

Enters dial peer voice configuration mode.

Step 4

no acc-qos { controlled-load | guaranteed-delay } [ audio | video ]

#### Example:

```
Device(config-dial-peer)# no acc-qos controlled-load
```

Removes any value configured for the acc-qos command.

- controlled-load --Indicates that RSVP guarantees a single level of preferential service, presumed to correlate to a delay boundary. The controlled
                                                         load service uses admission (or capacity) control to ensure that preferential service is received even when the bandwidth
                                                         is overloaded.

- guaranteed-delay --Indicates that RSVP reserves bandwidth and guarantees a minimum bit rate and preferential queueing if the bandwidth reserved
                                                         is not exceeded.

Step 5

req-qos { controlled-load | guaranteed-delay } [ audio | video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]]

#### Example:

```
Device(config-dial-peer)# req-qos controlled-load
```

Configures the desired quality of service (QoS) to be used.

Calls continue even if there is a failure in bandwidth reservation.

Configure the req-qos command using the same keyword that you used to configure the acc-qos command, either controlled-load or guaranteed-delay . That is, if you configured acc-qos controlled-load command in the previous step, then use the req-qos controlled-load command here.

Step 6

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode.

### Configure Mandatory RSVP on the Dial Peer

Perform this task to configure Mandatory RSVP on the dial peer. This configuration ensures that the call does not connect
                                 if sufficient bandwidth is not allocated.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- acc-qos { best-effort | controlled-load | guaranteed-delay } [ audio | video ]

- req-qos { best-effort [ audio | video ] | { controlled-load | guaranteed-delay } [ audio | video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]]}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer 77 voip
```

Enters dial peer voice configuration mode.

Step 4

acc-qos { best-effort | controlled-load | guaranteed-delay } [ audio | video ]

#### Example:

```
Device(config-dial-peer)# acc-qos best-effort
```

Configures mandatory RSVP on the dial-peer.

Keywords are as follows:

best-effort –Indicates that Resource Reservation Protocol (RSVP) makes no bandwidth reservation. This is the default.

controlled-load –Indicates that RSVP guarantees a single level of preferential service, presumed to correlate to a delay boundary. The controlled
                                                   load service uses admission (or capacity) control to ensure that preferential service is received even when the bandwidth
                                                   is overloaded.

guaranteed-delay –Indicates that RSVP reserves bandwidth and guarantees a minimum bit rate and preferential queuing if the bandwidth reserved
                                                   is not exceeded.

Step 5

req-qos { best-effort [ audio | video ] | { controlled-load | guaranteed-delay } [ audio | video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]]}

#### Example:

```
Device(config-dial-peer)# req-qos controlled-load
```

Configures mandatory RSVP on the dial-peer.

Calls continue even if there is a drop in the bandwidth reservation.

Step 6

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode.

### Configure Midcall RSVP Failure Policies

Perform this task to enable call handling policies for a midcall RSVP failure.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip rsvp-fail-policy { video | voice } post-alert { optional keep-alive | mandatory { keep-alive | disconnect retry retry-attempts }} interval seconds

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 66 voip
```

Enters dial peer voice configuration mode.

Step 4

voice-class sip rsvp-fail-policy { video | voice } post-alert { optional keep-alive | mandatory { keep-alive | disconnect retry retry-attempts }} interval seconds

#### Example:

```
Device(config-dial-peer)# voice-class sip rsvp-fail-policy voice post-alert mandatory keep-alive interval 50
```

Enables call handling policies for a midcall RSVP failure.

Keywords are as follows:

optional keep-alive –The keepalive messages are sent when RSVP fails only if RSVP negotiation is optional.

mandatory keep-alive –The keepalive messages are sent when RSVP fails only if RSVP negotiation is mandatory.

Keepalive messages are sent at 30-second intervals when a postalert call fails to negotiate RSVP regardless of the RSVP negotiation
                                                         setting (mandatory or optional).

Step 5

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode.

### Configure DSCP Values

Perform this task to configure different Differentiated Services Code Point (DSCP) values based on RSVP status.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- ip qos dscp { dscp-value | set-af | set-cs | default | ef } { signaling | media [ rsvp-pass | rsvp-fail ] | video [ rsvp-none | rsvp-pass | rsvp-fail ]}

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 66 voip
```

Enters dial peer voice configuration mode.

Step 4

ip qos dscp { dscp-value | set-af | set-cs | default | ef } { signaling | media [ rsvp-pass | rsvp-fail ] | video [ rsvp-none | rsvp-pass | rsvp-fail ]}

#### Example:

```
Device(config-dial-peer)# ip qos dscp af11 media rsvp-pass
```

Configures DSCP values based on RSVP status.

Keywords are as follows:

media rsvp-pass –Specifies that the DSCP value applies to media packets with successful RSVP reservations.

media rsvp-fail –Specifies that the DSCP value applies to packets (media or video) with failed RSVP reservations.

The default DSCP value for all media (voice and fax) packets is ef .

You must configure the DSCP values for all cases: media rsvp-pass , and media rsvp-fail .

Step 5

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode.

### Configure an Application ID

Perform this task to configure a specific application ID for RSVP establishment.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- ip qos policy-locator { video | voice } [ app app-string ] [ guid guid-string ] [ sapp subapp-string ] [ ver version-string ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 66 voip
```

Enters dial peer voice configuration mode.

Step 4

ip qos policy-locator { video | voice } [ app app-string ] [ guid guid-string ] [ sapp subapp-string ] [ ver version-string ]

#### Example:

```
Device(config-dial-peer)# ip qos policy-locator voice
```

Configures a QoS policy locator (application ID) used to deploy RSVP policies for specifying bandwidth reservations on Cisco
                                             IOS Session Initiation Protocol (SIP) devices.

Step 5

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode.

### Configure Priority

Perform this task to configure priorities for call preemption.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- ip qos defending-priority defending-pri-value

- ip qos preemption-priority preemption-pri-value

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 66 voip
```

Enters dial peer voice configuration mode.

Step 4

ip qos defending-priority defending-pri-value

#### Example:

```
Device(config-dial-peer)# ip qos defending-priority 66
```

Configures the RSVP defending priority value for determining QoS.

Step 5

ip qos preemption-priority preemption-pri-value

#### Example:

```
Device(config-dial-peer)# ip qos preemption-priority 75
```

Configures the RSVP preemption priority value for determining QoS.

Step 6

end

#### Example:

```
Device(config-dial-peer)# end
```

(Optional) Exits dial peer configuration mode and returns to privileged EXEC mode.

## Troubleshooting for Interworking Between RSVP Capable and RSVP Incapable Networks Feature

Use the following commands to debug any errors that you may encounter when you configure the Support for Interworking Between
                           RSVP Capable and RSVP Incapable Networks feature.

debug call rsvp-sync events

debug call rsvp-sync func-trace

debug ccsip all

debug ccsip messages

debug ip rsvp messages

debug sccp all

## Verify Interworking Between RSVP Capable and RSVP Incapable Networks

This task explains how to display information to verify the configuration for the Support for Interworking Between RSVP Capable
                              and RSVP Incapable Networks feature. These commands need not be entered in any specific order.

### SUMMARY STEPS

- enable

- show sip-ua calls

- show ip rsvp installed

- show ip rsvp reservation

- show ip rsvp interface detail [ interface-type number ]

- show sccp connections details

- show sccp connections rsvp

- show sccp connections internal

- show sccp [ all | connections | statistics ]

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

show sip-ua calls

### Example:

```
Device# show sip-ua calls
```

(Optional) Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls.

Step 3

show ip rsvp installed

### Example:

```
Device# show ip rsvp installed
```

(Optional) Displays RSVP-related installed filters and corresponding bandwidth information.

Step 4

show ip rsvp reservation

### Example:

```
Device# show ip rsvp reservation
```

(Optional) Displays RSVP-related receiver information currently in the database.

Step 5

show ip rsvp interface detail [ interface-type number ]

### Example:

```
Device# show ip rsvp interface detail GigabitEthernet 0/0
```

(Optional) Displays the interface configuration for hello.

Step 6

show sccp connections details

### Example:

```
Device# show sccp connections details
```

(Optional) Displays SCCP connection details, such as call-leg details.

Step 7

show sccp connections rsvp

### Example:

```
Device# show sccp connections rsvp
```

(Optional) Displays information about active SCCP connections that are using RSVP.

Step 8

show sccp connections internal

### Example:

```
Device# show sccp connections internal
```

(Optional) Displays the internal SCCP details, such as time-stamp values.

Step 9

show sccp [ all | connections | statistics ]

### Example:

```
Device# show sccp statistics
```

(Optional) Displays SCCP information, such as administrative and operational status.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Interworking Between RSVP Capable and RSVP Incapable Networks | Baseline Functionality | The Interworking between RSVP Capable and RSVP Incapable Networks feature provides precondition-based RSVP support for basic
                                          audio call and supplementary services on the Cisco UBE. The following commands were introduced or modified: acc-qos , ip qos defending-priority , ip qos dscp , ip qos policy-locator , ip qos preemption-priority , req-qos , voice-class sip rsvp-fail-policy |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | interface type slot / port Example: Device(config)# interface FastEthernet 0/1 | Configures an interface type and enters interface configuration mode. |
| Step 4 | ip rsvp bandwidth [ reservable-bw [ max-reservable-bw ] [ sub-pool reservable-bw ]] Example: Device(config-if)# ip rsvp bandwidth 10000 100000 | Enables RSVP for IP on an interface. |
| Step 5 | end Example: Device(config-if)# end | (Optional) Exits interface configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer 77 voip | Enters dial peer voice configuration mode. |
| Step 4 | no acc-qos { controlled-load \| guaranteed-delay } [ audio \| video ] Example: Device(config-dial-peer)# no acc-qos controlled-load | Removes any value configured for the acc-qos command. Keywords are as follows: controlled-load --Indicates that RSVP guarantees a single level of preferential service, presumed to correlate to a delay boundary. The controlled
                                                         load service uses admission (or capacity) control to ensure that preferential service is received even when the bandwidth
                                                         is overloaded. guaranteed-delay --Indicates that RSVP reserves bandwidth and guarantees a minimum bit rate and preferential queueing if the bandwidth reserved
                                                         is not exceeded. |
| Step 5 | req-qos { controlled-load \| guaranteed-delay } [ audio \| video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]] Example: Device(config-dial-peer)# req-qos controlled-load | Configures the desired quality of service (QoS) to be used. Calls continue even if there is a failure in bandwidth reservation. Note Configure the req-qos command using the same keyword that you used to configure the acc-qos command, either controlled-load or guaranteed-delay . That is, if you configured acc-qos controlled-load command in the previous step, then use the req-qos controlled-load command here. | Note | Configure the req-qos command using the same keyword that you used to configure the acc-qos command, either controlled-load or guaranteed-delay . That is, if you configured acc-qos controlled-load command in the previous step, then use the req-qos controlled-load command here. |
| Note | Configure the req-qos command using the same keyword that you used to configure the acc-qos command, either controlled-load or guaranteed-delay . That is, if you configured acc-qos controlled-load command in the previous step, then use the req-qos controlled-load command here. |
| Step 6 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

| Note | Configure the req-qos command using the same keyword that you used to configure the acc-qos command, either controlled-load or guaranteed-delay . That is, if you configured acc-qos controlled-load command in the previous step, then use the req-qos controlled-load command here. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer 77 voip | Enters dial peer voice configuration mode. |
| Step 4 | acc-qos { best-effort \| controlled-load \| guaranteed-delay } [ audio \| video ] Example: Device(config-dial-peer)# acc-qos best-effort | Configures mandatory RSVP on the dial-peer. Keywords are as follows: best-effort –Indicates that Resource Reservation Protocol (RSVP) makes no bandwidth reservation. This is the default. controlled-load –Indicates that RSVP guarantees a single level of preferential service, presumed to correlate to a delay boundary. The controlled
                                                   load service uses admission (or capacity) control to ensure that preferential service is received even when the bandwidth
                                                   is overloaded. guaranteed-delay –Indicates that RSVP reserves bandwidth and guarantees a minimum bit rate and preferential queuing if the bandwidth reserved
                                                   is not exceeded. |
| Step 5 | req-qos { best-effort [ audio \| video ] \| { controlled-load \| guaranteed-delay } [ audio \| video ] [ bandwidth [ default bandwidth-value ] [ max bandwidth-value ]]} Example: Device(config-dial-peer)# req-qos controlled-load | Configures mandatory RSVP on the dial-peer. Calls continue even if there is a drop in the bandwidth reservation. |
| Step 6 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 66 voip | Enters dial peer voice configuration mode. |
| Step 4 | voice-class sip rsvp-fail-policy { video \| voice } post-alert { optional keep-alive \| mandatory { keep-alive \| disconnect retry retry-attempts }} interval seconds Example: Device(config-dial-peer)# voice-class sip rsvp-fail-policy voice post-alert mandatory keep-alive interval 50 | Enables call handling policies for a midcall RSVP failure. Keywords are as follows: optional keep-alive –The keepalive messages are sent when RSVP fails only if RSVP negotiation is optional. mandatory keep-alive –The keepalive messages are sent when RSVP fails only if RSVP negotiation is mandatory. Note Keepalive messages are sent at 30-second intervals when a postalert call fails to negotiate RSVP regardless of the RSVP negotiation
                                                         setting (mandatory or optional). | Note | Keepalive messages are sent at 30-second intervals when a postalert call fails to negotiate RSVP regardless of the RSVP negotiation
                                                         setting (mandatory or optional). |
| Note | Keepalive messages are sent at 30-second intervals when a postalert call fails to negotiate RSVP regardless of the RSVP negotiation
                                                         setting (mandatory or optional). |
| Step 5 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

| Note | Keepalive messages are sent at 30-second intervals when a postalert call fails to negotiate RSVP regardless of the RSVP negotiation
                                                         setting (mandatory or optional). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 66 voip | Enters dial peer voice configuration mode. |
| Step 4 | ip qos dscp { dscp-value \| set-af \| set-cs \| default \| ef } { signaling \| media [ rsvp-pass \| rsvp-fail ] \| video [ rsvp-none \| rsvp-pass \| rsvp-fail ]} Example: Device(config-dial-peer)# ip qos dscp af11 media rsvp-pass | Configures DSCP values based on RSVP status. Keywords are as follows: media rsvp-pass –Specifies that the DSCP value applies to media packets with successful RSVP reservations. media rsvp-fail –Specifies that the DSCP value applies to packets (media or video) with failed RSVP reservations. The default DSCP value for all media (voice and fax) packets is ef . Note You must configure the DSCP values for all cases: media rsvp-pass , and media rsvp-fail . | Note | You must configure the DSCP values for all cases: media rsvp-pass , and media rsvp-fail . |
| Note | You must configure the DSCP values for all cases: media rsvp-pass , and media rsvp-fail . |
| Step 5 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

| Note | You must configure the DSCP values for all cases: media rsvp-pass , and media rsvp-fail . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 66 voip | Enters dial peer voice configuration mode. |
| Step 4 | ip qos policy-locator { video \| voice } [ app app-string ] [ guid guid-string ] [ sapp subapp-string ] [ ver version-string ] Example: Device(config-dial-peer)# ip qos policy-locator voice | Configures a QoS policy locator (application ID) used to deploy RSVP policies for specifying bandwidth reservations on Cisco
                                             IOS Session Initiation Protocol (SIP) devices. |
| Step 5 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 66 voip | Enters dial peer voice configuration mode. |
| Step 4 | ip qos defending-priority defending-pri-value Example: Device(config-dial-peer)# ip qos defending-priority 66 | Configures the RSVP defending priority value for determining QoS. |
| Step 5 | ip qos preemption-priority preemption-pri-value Example: Device(config-dial-peer)# ip qos preemption-priority 75 | Configures the RSVP preemption priority value for determining QoS. |
| Step 6 | end Example: Device(config-dial-peer)# end | (Optional) Exits dial peer configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | show sip-ua calls Example: Device# show sip-ua calls | (Optional) Displays active user agent client (UAC) and user agent server (UAS) information on SIP calls. |
| Step 3 | show ip rsvp installed Example: Device# show ip rsvp installed | (Optional) Displays RSVP-related installed filters and corresponding bandwidth information. |
| Step 4 | show ip rsvp reservation Example: Device# show ip rsvp reservation | (Optional) Displays RSVP-related receiver information currently in the database. |
| Step 5 | show ip rsvp interface detail [ interface-type number ] Example: Device# show ip rsvp interface detail GigabitEthernet 0/0 | (Optional) Displays the interface configuration for hello. |
| Step 6 | show sccp connections details Example: Device# show sccp connections details | (Optional) Displays SCCP connection details, such as call-leg details. |
| Step 7 | show sccp connections rsvp Example: Device# show sccp connections rsvp | (Optional) Displays information about active SCCP connections that are using RSVP. |
| Step 8 | show sccp connections internal Example: Device# show sccp connections internal | (Optional) Displays the internal SCCP details, such as time-stamp values. |
| Step 9 | show sccp [ all \| connections \| statistics ] Example: Device# show sccp statistics | (Optional) Displays SCCP information, such as administrative and operational status. |