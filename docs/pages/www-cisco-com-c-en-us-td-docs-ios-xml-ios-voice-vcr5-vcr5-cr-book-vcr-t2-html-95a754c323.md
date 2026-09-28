---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-t2-html-95a754c323
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-t2.html
retrieved_at: 2026-08-16T23:16:04.923112+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: timeouts call-disconnect through timing clear-wait

## Chapter: timeouts call-disconnect through timing clear-wait

# timeouts call-disconnect through timing clear-wait

## timeouts call-disconnect

To configure the delay time for which a Foreign Exchange Office (FXO) voice port waits before disconnecting an incoming call
                              after disconnect tones are detected, use the timeouts call - disconnect command in voice-port configuration mode. To reset to the default, use the no form of this command.

timeouts call-disconnect { seconds | infinity }

no timeouts call-disconnect

### Syntax Description

seconds

Duration in seconds for which an FXO voice port stays in the connected state after the voice port detects a disconnect tone.
                                          Range is 1 to 120. The default is 60.

infinity

Disables disconnect supervision. The voice port does not disconnect when a disconnect tone is detected.

### Command Default

60 seconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(9)T

This command was introduced on Cisco 3600 series routers.

12.0(4)T

This command was introduced on Cisco 3600 series routers.

12.2(2)T

This command was implemented on Cisco 1750, Cisco 2600 series, and Cisco MC3810. The infinity keyword was added.

### Usage Guidelines

Use this command to change the time for which an FXO voice port remains connected after the calling party hangs up, when a
                              call is not answered. Use of the infinity keyword is not recommended for disabling the disconnect supervision feature.

## Examples

The following example configures voice port 0/0/1 to remain connected for 3 seconds while a disconnect tone is received by
                              the voice port:

```
voice-port 0/0/1
 timeouts call-disconnect 3
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a specified voice port.

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

timeouts wait-release

Specifies the delay time for releasing the calling voice port after a disconnect tone is received from the called voice port.

timing delay-duration

Configures the delay dial signal duration for a specified voice port.

## timeouts initial

To configure the initial digit timeout value for a specified voice port, use the timeouts initial command in voice-port configuration mode. To reset to the default, use the no form of this command.

timeouts initial seconds

no timeouts initial seconds

### Syntax Description

seconds

Initial timeout duration, in seconds. Range is 0 to 120. The default is 10.

### Command Default

10 seconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series routers.

### Usage Guidelines

Use the timeouts initial command to specify the number of seconds for which the system waits for the caller to input the first digit of the dialed
                              digits. The timeouts initial timer is activated when the call is accepted and is deactivated when the caller inputs the first
                              digit. If the configured timeout value is exceeded, the caller is notified through the appropriate tone and the call is terminated.

To disable the timeouts initial timer, set the seconds value to 0.

## Examples

The following example sets the initial digit timeout value to 10 seconds:

```
voice-port 1/0/0
 timeouts initial 10
```

### Related Commands

Command

Description

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

## timeouts interdigit (voice port)

To configure the interdigit timeout value for a specified voice port, use the timeouts interdigit command in voice-port configuration mode. To reset to the default, use the no form of this command.

timeouts interdigit seconds

no timeouts interdigit seconds

### Syntax Description

seconds

Interdigit timeout duration, in seconds. Range is 0 to 120. The default is 10.

### Command Default

10 seconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

### Usage Guidelines

Use this command to specify the number of seconds for which the system waits (after the caller inputs the initial digit) for
                              the caller to input a subsequent digit of the dialed digits. The timeouts interdigit timer is activated when the caller inputs
                              a digit and is restarted each time the caller inputs another digit until the destination address is identified. If the configured
                              timeout value is exceeded before the destination address is identified, the caller is notified through the appropriate tone
                              and the call is terminated.

To disable the timeouts interdigit timer, set the seconds value to 0.

## Examples

The following example sets the interdigit timeout value on the Cisco 3600 series for 10 seconds:

```
voice-port 1/0/0
 timeouts interdigit 10
```

The following example sets the interdigit timeout value on the Cisco MC3810 for 10 seconds:

```
voice-port 1/1
 timeouts interdigit 10
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a specified voice port.

## timeouts power-denial

To set the duration of the power denial timeout for the specified FXS voice port, use the timeouts power-denial command in voice-port configuration mode. To reset the timeout to the default, use the no form of this command.

timeouts power-denial ms

no timeouts power-denial

### Syntax Description

ms

Length of power denial, in milliseconds (ms). Range: 0 to 2500. Default: 750.

### Command Default

Default is 750 ms.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.2(13)T

This command was introduced.

12.4(2)T

The maximum value of the ms argument was increased from 1500 to 2500.

### Usage Guidelines

This command sets the duration of the power denial that the voice gateway applies to the FXS port when a call disconnects.
                              During the power denial duration the caller hears silence. To disable the power denial on a port, use the no supervisory disconnect lcfo command.

## Examples

The following example sets the power-denial duration to 500 ms:

```
voice-port 2/0
 timeouts power-denial 500
```

### Related Commands

Command

Description

supervisory disconnect lcfo

Signals a disconnect on an FXS loop-start port by applying a power denial using a LCFO.

## timeouts ringing

To configure the timeout value for ringing, use the timeouts ringing command in voice-port configuration mode. To reset to the default, use the no form of this command.

timeouts ringing { seconds | infinity }

no timeouts ringing

### Syntax Description

seconds

Duration, in seconds, for which a voice port allows ringing to continue if a call is not answered. Range is 5 to 60000. Default
                                          is 180 for nonSCCP-controlled ports.

infinity

Ringing continues until the caller goes on-hook. Default value for SCCP-controlled analog ports.

### Command Default

infinity for SCCP-controlled analog ports; 180 seconds for all other ports.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.0(7)XK

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.4(11)T

The command default value was increased from 180 seconds to infinity for SCCP-controlled analog ports.

### Usage Guidelines

This command allows you to limit the length of time for which a caller can continue ringing a telephone when there is no answer.

In Cisco IOS Release 12.4(11)T and later the default for this command is set to infinity for SCCP-controlled analog ports to prevent this timeout from expiring before the ringing no-answer timeout that is configured
                              on Cisco Unified CallManager Express with the timeouts ringing command in telephony-service mode.

## Examples

The following example configures voice port 0/0/1 to allow ringing for 600 seconds:

```
voice-port 0/0/1
 timeouts ringing 600
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a voice port.

timeouts interdigit

Configures the interdigit timeout value for a voice port.

timeouts ringing (telephony-service)

Sets the timeout value for ringing in a Cisco Unified CallManager Express system.

## timeouts wait-release

To configure the
                              		  delay timeout before the system starts the process for releasing voice ports,
                              		  use the timeouts wait - release command in voice-port configuration mode.
                              		  To reset to the default, use the no form of this
                              		  command.

timeouts wait-release { seconds | infinity }

no timeouts wait-release

### Syntax Description

seconds

Duration,
                                          						in seconds, for which a voice port stays in the call-failure state while the
                                          						Cisco router or concentrator sends a busy tone, reorder tone, or out-of-service
                                          						tone to the port. Range is 1 to 3600. Default is 30.

infinity

The voice
                                          						port is never released as long as the call-failure state remains.

### Command Default

30 seconds.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)
                                          						MA

This
                                          						command was introduced on Cisco MC3810.

12.0(7)XK

This
                                          						command was implemented on Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This
                                          						command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

Use this command to
                              		  limit the time a voice port can be held in a call failure state. After the
                              		  timeout, the release sequence is enabled.

You can also use
                              		  this command for voice ports with Foreign Exchange Station (FXS) loop-start
                              		  signaling to specify the time allowed for a caller to hang up before the voice
                              		  port goes into the parked state.

## Examples

The following
                              		  example configures voice port 0/0/1 to stay in the call-failure state for 180
                              		  seconds while a busy tone, reorder tone, or out-of-service tone is sent to the
                              		  voice port:

```
voice-port 0/0/1
 timeouts wait-release 180
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a voice port.

timeouts interdigit

Configures the interdigit timeout value for a voice port.

## timeouts teardown lmr

To configure the
                              		  time for which a Land Mobile Radio (LMR) voice port waits before tearing down
                              		  an LMR connection after detecting no voice activity, use the timeouts teardown lmr command in voice-port configuration mode. To
                              		  reset to the default, use the no form of this
                              		  command.

timeouts teardown lmr { seconds | infinity }

no timeouts teardown lmr { seconds | infinity }

### Syntax Description

seconds

Duration
                                          						in seconds for which an LMR voice port waits before tearing down an LMR
                                          						connection after detecting no voice activity. Valid values are 5 to 60000. The
                                          						default is 1800 seconds.

infinity

Disables
                                          						disconnect supervision. The voice port does not disconnect when no voice
                                          						activity is detected.

### Command Default

1800 seconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This
                                          						command was introduced.

12.3(7)T

This
                                          						command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The timeouts teardown lmr command has an effect on an ear and mouth
                              		  (E&M) voice port only if the signal type for that port is LMR.

## Examples

The following
                              		  example configures voice port 1/0/1 on a Cisco 3745 to remain connected for 6
                              		  seconds after no voice activity is detected by the voice port:

```
voice-port 1/0/1
 timeouts teardown lmr 6
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a specified voice port.

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

timeouts wait-release

Specifies the delay time for releasing the calling voice port after a
                                          						disconnect tone is received from the called voice port.

timeouts delay-duration

Configures the delay dial signal duration for a specified voice port.

## timer accessrequest sequential delay

To configure the intermessage delay used when a border element (BE) is trying to determine a route from a list of neighboring
                              BEs, use the timer accessrequest sequential delay command in Annex G configuration mode. To reset the default value, use the no form of this
                              command.

timer accessrequest sequential delay value

no timer

### Syntax Description

value

Amount of allowed intermessage delay (in increments of 100 ms). Range is from 0 to 10. The default is 1 (100 ms).

### Command Default

1 (100 ms)

### Command Modes

Annex G configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Setting the value of the delay to 0 causes the BE to broadcast or "blast" the AccessRequest messages to all eligible neighbors.

## Examples

The following example shows a timer delay of 1000 ms.

```
Router(config)# call-router h323-annexg be20 Router(config-annexg)# timer accessrequest sequential delay 10
```

### Related Commands

Command

Description

call - router

Enables the Annex G border element configuration commands.

## timer cluster-element

To configure the length of time between dynamic capacity messages to the local gatekeeper, use the timer cluster-element command in gatekeeper configuration mode. To stop sending dynamic updates, use the no form of this command.

timer cluster-element { announce | resource-update } seconds

no timer cluster-element

### Syntax Description

announce

Configures the lengh of time between announcement messages to the gatekeepers in the local cluster.

resource - update

Configures the lengh of time between resource update messages to gatekeepers in the local cluster.

seconds

Number of seconds between resource updates sent to the gatekeeper. The valid range is 1 to 60. There is no default value.

### Command Default

Disabled by default.

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on Cisco AS5850.

12.4(11)T

The resource - update keyword was introduced.

### Usage Guidelines

Use the timer cluster-element command to manage the length of time between resource updates and time between announcement messages sent to the gatekeeper.
                              The announcement indication is exchanged at a set interval of time and carries information about the call and endpoint capacity
                              for the zone. This allows the alternate gatekeepers to manage the bandwidth for a single zone even though the gatekeepers
                              are in separate physical devices.

The gatekeeper assumes that the alternate gatekeeper has failed (and assumes that any previously allocated bandwidth is now
                              available) if the gatekeeper does not receive an announcement message within six announcement periods or if the TCP connection
                              with the gatekeeper is detected to be broken.

Lower this interval for closer tracking between elements. Raise it to lower messaging overhead.

## Examples

The following command sets the announcement period to 20 seconds:

```
Router(config-gk)# timer cluster-element announce 20
```

The following command resets the announcement period to the default value:

```
Router(config-gk)# no timer cluster-element announce
```

The following example shows the time between resource update messages to gatekeepers in local cluster being set to 20 seconds:

```
Router(config-gk)# timer cluster-element resource-update 20
```

### Related Commands

Command

Description

call-routing hunt-scheme

Enables capacity-based load-balancing.

zone cluster local

Defines a local grouping of gatekeepers.

zone remote

Statically specifies a remote zone if DNS is unavailable or undesirable.

## timer irr period

To configure the information request response (IRR) timer, or the periodic interval of IRR messages sent by the gatekeeper,
                              use the timer irr period command in gatekeeper configuration mode. To disable, use the no form of this command.

timer irr period minutes

no timer irr period

### Syntax Description

minutes

Length, in minutes, of the interval between IRR messages. Range is from 1 to 60. The default is 4.

### Command Default

4 minutes

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use this command to configure IRR frequency that is included in the admission confirm (ACF) message. The IRR frequency is
                              set to 240 seconds (4 minutes), based on an average 4-minute call hold time. The IRR allows the gatekeepers to terminate calls
                              for which a disengage request (DRQ) has not been received. If missing DRQs are not a problem, the IRR frequency can be set
                              to a larger value than 4 minutes, minimizing the number of unnecessary IRRs sent by a gateway.

## Examples

The following example shows that the IRR timer has been configured with a value of 45, meaning that IRR messages are sent
                              by the gatekeeper every 45 minutes:

```
gatekeeper
.
.
.
lrq reject-resource-low
 no irq global-request
 timer lrq seq delay 10
 timer lrq window 6
 timer irr period 45
 no shutdown
```

### Related Commands

Command

Description

timer lrq seq delay

Defines the time interval between successive LRQ messages.

timer lrq window

Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs.

timer server timeout

Specifies the timeout value for a response from a back-end GKTMP server.

## timer lrq seq delay

To define the time interval between successive sequential location requests (LRQs), use the timer lrq seq delay command in gatekeeper configuration mode. To reset to the default, use the no form of this command.

timer lrq seq delay time

no timer lrq seq delay

### Syntax Description

time

Time interval, in 100-millisecond units. Range is 1 to 10 (0.1 to 1 second). The default is 5 (500 milliseconds).

### Command Default

5 units (500 milliseconds)

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on Cisco AS5850.

### Usage Guidelines

The LRQ sequential timing source (SEQ) delay is used to set the time between sending LRQs to remote gatekeepers for address
                              resolution. To resolve an address, the gatekeeper might have several remote zones configured, and it can send the LRQs simultaneously
                              (blast) or sequentially (seq). The gatekeeper chooses the best route based on availability and cost. Using LRQs sequentially
                              results in lower network traffic, but it can increase latency of calls when the most preferred route is unavailable.

Lowering the time increases traffic on the network but might reduce the call setup time.

## Examples

The following command sets the LRQ delay timer to 100 milliseconds:

```
timer lrq seq delay 1
```

The following command resets the LRQ delay timer to the default value:

```
no timer lrq seq delay
```

### Related Commands

Command

Description

timer lrq window

Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs.

## timer lrq seq delay centisec

To define the time interval between successive sequential location requests (LRQs), use the timer lrq seq delay centices command in gatekeeper configuration mode. To reset to the default, use the no form of this command.

timer lrq seq delay centisec time

no timer lrq seq delay centisec

### Syntax Description

time

Time interval, in 100-millisecond units. Range is 1 to 10 (0.1 to 1 second). The default is 1(100 milliseconds).

### Command Default

Timers are set to their default value.

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.4(4)T

This command was introduced.

### Usage Guidelines

The LRQ sequential timing source (SEQ) delay is used to set the time between sending LRQs to remote gatekeepers for address
                              resolution. To resolve an address, the gatekeeper might have several remote zones configured, and it can send the LRQs simultaneously
                              (blast) or sequentially (seq). The gatekeeper chooses the best route based on availability and cost. Using LRQs sequentially
                              results in lower network traffic, but it can increase latency of calls when the most preferred route is unavailable.

Lowering the time increases traffic on the network but might reduce the call setup time.

This command cannot be configured at the same time as the timer lrq seq delay command.

## Examples

The following command sets the LRQ delay timer to 100 milliseconds:

```
timer lrq seq delay centisec 1
```

The following command resets the LRQ delay timer to the default value:

```
no timer lrq seq delay centisec
```

### Related Commands

Command

Description

timer lrq window decisec

Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs.

## timer lrq window

To define the time window during which the gatekeeper collects responses to one or more outstanding LRQs, use the timer lrq window command in gatekeeper configuration mode. To reset to the default, use the no form of this command.

timer lrq window seconds

no timer lrq window

### Syntax Description

seconds

Time window, in seconds. Range is 1 to 15. The default is 3.

### Command Default

3 seconds

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on Cisco AS5850.

### Usage Guidelines

Increasing the time can increase the call success rate but might reduce the overall time for call setup.

## Examples

The following command sets the timer to 5 seconds:

```
timer lrq window 5
```

The following command sets the timer to the default value:

```
no timer lrq window
```

### Related Commands

Command

Description

timer lrq seq delay

Defines the time interval between successive sequential LRQs.

## timer lrq window decisec

To define the time window during which the gatekeeper collects responses to one or more outstanding LRQs, use the timer lrq window decisec command in gatekeeper configuration mode. To reset to the default, use the no form of this command.

timer lrq window decisec time

no timer lrq window decisec

### Syntax Description

time

Time window, in seconds. Range is 1 to 15. The default is 2.

### Command Default

Timers are set to their default value.

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.4(4)T

This command was introduced.

### Usage Guidelines

Increasing the time can increase the call success rate but might reduce the overall time for call setup.

This command cannot be in effect at the same time as the timer lrq window command.

## Examples

The following command sets the timer to 5 seconds:

```
timer lrq window decisec 2
```

The following command sets the timer to the default value:

```
no timer lrq window decisec
```

### Related Commands

Command

Description

timer lrq seq delay centsec

Defines the time interval between successive sequential LRQs.

## timer media-inactive

To enable the timer for media inactivity detection using the digital signal processor (DSP) (based on RTP as the only criterion)
                              and to configure a multiplication factor based on the real-time control protocol (RTCP) timer interval, use the timer media-inactive command in gateway configuration mode. To reset to the default, use the no form of this command.

timer media-inactive multiple

no timer media-inactive multiple

### Syntax Description

multiple

Multiples of the RTCP report transmission interval. Range is 4 to 1000. The default is 5, and the recommended value is 5.

### Command Default

A call is considered inactive if no RTP packet activity is detected for a period of time calculated as five times the interval
                              set by the ip rtcp report interval command.

### Command Modes

Gateway configuration

## Command History

Release

Modification

12.4(4)T

This command was introduced.

### Usage Guidelines

When the timer media-inactive command is used, the gateway uses the inactivity timer as a combination of the timer media-inactive command and the ip rtcp report interval command. The timer media-inactive command uses DSP statistics. This capability is based on the configuration of callfeature parameters using application command-line
                              interface (CLI) to enable control.

The media are considered inactive only if there is no transfer of RTP packets in the send direction and no RTP packets in
                              the receive direction. If RTP is present in either the send or receive direction, it is considered active. In this mode, DSP
                              filters out any comfort noise packets, and the presence of any comfort noise packet is considered inactivity in either direction.

The multiple argument (or multiplication factor) is multiplied by the interval that is set using the ip rtcp report interval command. This command configures the average interval between successive RTCP report transmissions for a given voice session.
                              For example, if the value argument is set to 25,000 milliseconds, an RTCP report is sent every 25 seconds, on average. If no RTP packets are received
                              during the calculated interval, the call is disconnected. The gateway signals the disconnect to the VoIP network and the time-division
                              multiplexing (TDM) network so that upstream and downstream devices can clear their resources.

## Examples

The following example uses the ip rtcp report interval command to set the reporting interval to 5000 milliseconds, and then the timer media-inactive command to set the multiplication factor to 10. The result is that calls detected as inactive for 50 seconds (5,000 milliseconds
                              times 10) will be disconnected.

```
Router(config)# ip rtcp report interval 5000 Router(config)# gateway Router(config-gateway)# timer media-inactive 10 Router(config-gateway)# exit
```

### Related Commands

Command

Description

ip rtcp report interval

Configures the minimum interval of RTCP report transmissions.

## timer receive-rtcp

To enable the Real-Time Control Protocol (RTCP) timer and to configure a multiplication factor for the RTCP timer interval
                              for Session Initiation Protocol (SIP) or H.323, use the timer receive-rtcp command in gateway configuration mode. To reset to the default, use the no form of this command.

timer receive-rtcp timer

no timer receive-rtcp timer

### Syntax Description

timer

Multiples of the RTCP report transmission interval. Range is 0 to 1000. Default is 0. Recommended value is 5.

### Command Default

The default value for the timer argument is 0 multiples, which disables the timer so that no silence detection is in effect.

### Command Modes

Gateway configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

### Usage Guidelines

The timer receive-rtcp command uses library-based detection and the receipt of either Real-Time Protocol (RTP) or RTCP packets is considered activity
                              on a call. Silence detection occurs only if there are no packets received for both RTP and RTCP.

When the ip rtcp report interval and timer receive-rtcp commands are used, the gateway uses RTCP report detection, rather than RTP packet detection, to determine whether calls on
                              the gateway are still active or should be disconnected. RTCP report detection is therefore more reliable than RTP packet detection
                              because there can be periods during voice calls when one or both parties are not sending RTP packets.

One common example of a voice session in which no RTP is sent is when a caller dials into a conference call and mutes that
                              endpoint. If voice activity detection (VAD, also known as silence suppression) is enabled, no RTP packets are sent while the
                              endpoint is muted. However, the muted endpoint continues to send RTCP reports at the interval specified by the ip rtcp report interval command.

The timer receive-rtcp timer argument (or m factor for multiplication factor) is multiplied by the interval that is set using the ip rtcp report interval command. If no RTP or RTCP packets are received during the calculated interval, the call is disconnected. The gateway signals
                              the disconnect to the VoIP network and the time-division multiplex (TDM) network so that upstream and downstream devices can
                              clear their resources. The gateway sends a Q.931 DISCONNECT message to the TDM network and a SIP BYE or H.323 ReleaseComplete
                              message to the VoIP network to clear the call when the timer expires. The Q.931 DISCONNECT message is sent with a cause code
                              value of 3 (no route) for SIP calls and a cause code value of 41 (temporary failure) for H.323 calls. No Q.931 Progress Indicator
                              (PI) value is included in the DISCONNECT message.

To show timer-related output for SIP calls, use the debug ccsip events command. To show timer-related output for H.323 calls, use the debug cch323 h225 command.

## Examples

The following example sets the multiplication factor to 10 (or x * 10, where x is the interval that is set with the ip rtcp report interval command):

```
Router(config)# gateway Router(config-gateway)# timer receive-rtcp 10 Router(config-gateway)# exit
```

### Related Commands

Command

Description

debug cch323 h225

Traces the state transition of the gateway H.225 state machine based on the processed events.

debug ccsip events

Displays all SIP SPI events tracing and traces the events posted to SIP SPI from all interfaces.

ip rtcp report interval

Configures the minimum interval of RTCP report transmissions.

## timer receive-rtp

To configure the Real-Time Transport Protocol (RTP) timeout interval to clear connections that pause indefinitely, use the timer receive-rtp command in gateway configuration mode. To reset the timer to the default value, use the no form of this command.

timer receive-rtp seconds

no timer receive-rtp

### Syntax Description

seconds

Timer value, in seconds. Range: 180 to 86400. Default: 1200.

### Command Default

1200 seconds (20 minutes)

### Command Modes

Gateway configuration (config-gateway)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.4(20)T

This command was modified. The recommended timer range is defined as 1200 seconds.

### Usage Guidelines

This command is used to configure the RTP timeout interval in seconds. The timeout value is used to clear connections that
                              pause indefinitely. The recommended value is 1200 seconds, or 20 minutes.

## Examples

The following example shows the RTP timeout interval set to the recommended 1200 seconds (20 minutes).

```
Router(config-gateway)# timer receive-rtp 600
```

### Related Commands

Command

Description

codec (dspfarm-profile)

Specifies the codecs supported by a DSP farm profile.

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for DSP farm services.

maximum sessions (dspfarm-profile)

Specifies the maximum number of sessions that need to be supported by the profile.

## timer server retry

To set the gatekeeper’s retry timer for failed Gatekeeper Transaction Message Protocol (GKTMP) connections, use the timer server retry command in gatekeeper configuration mode. To reset the timer to its default, use the no form of this command or the default server timer retry command.

server timer retry seconds

no server timer retry

default server timer retry

### Syntax Description

seconds

Number of seconds for which the gatekeeper should wait before retrying the GKTMP server. Range is from 1 through 300. The
                                          default is 30.

### Command Default

30 seconds

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

After the gatekeeper detects that its GKTMP server TCP connection has failed, the gatekeeper retries the server after an interval
                              based on the setting of this timer, and keeps retrying until the connection is established.

This timer applies only to deployments where static triggers are used between the gatekeeper and the GKTMP server. If dynamic
                              triggers are used, the server must determine and implement a retry mechanism if the TCP connection to the gatekeeper fails.

## Examples

The following example shows that the retry timer has been set to 45 seconds:

```
Router# show gatekeeper configuration
.
.
.
h323id tet
 gw-type-prefix 1#* default-technology
 gw-type-prefix 9#* gw ipaddr 1.1.1.1 1720
 timer server retry 45
 no shutdown
.
.
.
```

### Related Commands

Command

Description

timer server timeout

Specifies the timeout value for a response from a back-end GKTMP server.

## timer server timeout

To specify the timeout interval for a response from a back-end Gatekeeper Transaction Message Protocol (GKTMP) application
                              server, use the timer server timeout command in gatekeeper configuration mode. To reset to the default, use the no form of this command.

timer server timeout time

no timer server timeout

### Syntax Description

time

Timeout interval, in 100-ms units. Range is 1 to 50 (0.1 to 5 seconds). Default is 3 (300 ms).

### Command Default

3 units

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.1(2)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

### Usage Guidelines

Use this command to specify the timeout interval for a response from a back-end GKTMP application server.

## Examples

The following command sets the timeout interval to 400 ms:

```
timer server timeout 4
```

The following command resets the timeout interval to the default value:

```
no timer server timeout
```

### Related Commands

Command

Description

server registration - port

Configures the listener port for the server to establish a connection with the gatekeeper.

server trigger

Configures a static server trigger for external applications.

## timers

To configure the Session Initiation Protocol (SIP) signaling timers, use the timers command in SIP user-agent configuration mode. To restore the default value, use the no form of this command.

timers { trying number | connect number | disconnect number | expires number }

no timers

### Syntax Description

trying number

Time (in ms) to wait for a 100 response to an INVITE request. Range is from 100 to 1000. Default is 500.

connect number

Time (in ms) to wait for a 200 response to an ACK request. Range is from 100 to 1000. Default is 500.

disconnect number

Time (in ms) to wait for a 200 response to a BYE request. Range is from 100 to 1000. Default is 500.

expires number

Time (in ms) for which an INVITE request is valid. Range is from 60000 to 300000. Default is 180000.

### Command Default

trying , connect , and disconnect --500 ms expires --180000 ms

### Command Modes

SIP user-agent configuration (config-sip-ua)

Voice class tenant configuration

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.1(3)T

This command was modified to change the names of the parameters. Two of the parameters ( invite - wait - 180 and invite - wait - 200 ) were combined into one ( trying ).

12.2(2)XA

This command was implemented on the Cisco AS5400 and AS5350.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco 7200 series routers. Support for the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

Introduced support for YANG models under SIP user agent configuration mode.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models under voice class tenant configuration
                                          mode.

### Usage Guidelines

If you used an earlier version of this command to configure timers, the timer settings are maintained. The output of the show
                              running-config command reflects both previous and current timers.

To reset this command to the default value, you can also use the default command.

## Examples

The following example sets the trying timers to the default of 500 ms.

```
Router(config)# sip-ua
Router(config-sip-ua)# timers trying 500
```

### Related Commands

Command

Description

default

Sets a command to its default.

inband
                                          -
                                          alerting

Specifies an inband-alerting SIP header.

max
                                          -
                                          forwards

Specifies the maximum number of hops for a request.

retry 
                                          (
                                          SIP user
                                          -
                                          agent
                                          )

Configures the SIP signaling timers for retry attempts.

transport

Enables SIP UA transport for TCP/UDP.

## timers buffer-invite

To enable the
                              		  Session Initiation Protocol (SIP) buffer-invite timer and to configure the
                              		  timer interval, use the timers buffer-invite command in SIP user-agent
                              		  configuration mode or voice class tenant configuration mode. To restore the
                              		  default value, use the no form of this
                              		  command.

timers buffer-invite timer system

no timers buffer-invite

### Syntax Description

timer

Buffer-invite timer value, in ms. Range is 50 to 5000.

system

Specifies
                                          						that the buffer-invite timer use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations.

### Command Default

Disabled

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.3(8)T

This
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

Use this command to enable the SIP buffer-invite timer and to configure the timer interval. Configure the command isdn supp-service name calling under the serial interface before configuring the command timers buffer-invite . Without configuring isdn supp-service name calling command, the timer to buffer the outgoing invite is not triggered.

For more details on the command isdn supp-service name calling , see isdn supp-service name calling .

## Examples

The following
                              		  example sets retransmission time to 500 milliseconds:

```
Router(config-class)# timers buffer-invite system
```

The following
                              		  example sets retransmission time in the voice class tenant configuration mode:

### Related Commands

Command

Description

sip-ua

Enables
                                          						SIP user-agent configuration commands.

## timers comet

To set how long the Session Initiation Protocol (SIP) user agent (UA) waits before retransmitting conditions-met (COMET) requests,
                              use the timers comet command in SIP user-agent configuration mode. To reset to the default, use the no form of this command.

timers comet time

no timers comet

### Syntax Description

time

Waiting time, in milliseconds. Range is 100 to 1000. The default is 500.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(2)XB1

This command was implemented on Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release.

12.2(11)T

This command was inplemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

### Usage Guidelines

COMET, or conditions met, indicates whether preconditions for a given call or session have been met. This command is applicable
                              only with calls involving quality of service (QoS) (calls other than best-effort).

## Examples

The following example sets retransmission time to 500 milliseconds:

```
Router(config)# sip-ua Router(config-sip-ua)# timers comet 500
```

### Related Commands

Command

Description

show sip - ua statistics

Displays response, traffic, timer, and retry statistics.

show sip - ua timers

Displays the current settings for SIP UA timers.

timers prack

Sets how long the UA waits before retransmitting a PRACK request.

## timers connect

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits for a 200 response to
                              		  an ACK request, use the timers connect command in SIP user-agent configuration
                              		  mode or voice class tenant configuration mode. To reset to the default, use the
                              		  no form of this command.

timers connect number system

no timers connect number

### Syntax Description

number

Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.1(1)T

This
                                          						command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300.

12.1(3)T

This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying).

12.2(2)XA

This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This
                                          						command was implemented on the Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          						Cisco AS5850 is not included in this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

If you used the
                              		  previous more generic timers command
                              		  to configure timers, your previous timer settings are maintained. The output of
                              		  the show running-config command reflects both timers.

To reset this
                              		  command to the default value, you can also use the default command.

## Examples

The following
                              		  example sets connect time to 200 milliseconds:

```
sip-ua
 timers connect 200
```

The following
                              		  example sets connect time in the voice class tenant configuration mode:

```
Router(config-class)# timers connect system
```

### Related Commands

Command

Description

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

## timers connection
                        	 aging

To globally set the
                              		  time before the Session Initiation Protocol (SIP) user agent (UA) ages out a
                              		  TCP or UDP connection because of inactivity, use the timers connection aging command in SIP user-agent configuration mode
                              		  or voice class tenant configuration mode. To reset this time to the default
                              		  value, use the no form of this command.

timers connection aging timer-value system

no timers connection aging

### Syntax Description

timer-value

Time to
                                          						wait, in minutes, before aging out a TCP or UDP connection because of
                                          						inactivity. Range is from 5 to 30. Default is 5.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

5 minutes

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.3(8)T

This
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

The minimum value
                              		  of this connection is 5 minutes.

## Examples

The following
                              		  example ages out a connection in 10 minutes:

```
sip-ua
 timers connection aging 10
```

The following
                              		  example ages out a connection in the voice class tenant configuration mode:

```
Router(config-class)# timers connection aging system
```

### Related Commands

Command

Description

show sip-ua timers

Displays
                                          						the current settings for the SIP UA timers.

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

timers expires

Sets how
                                          						long a SIP INVITE request is valid.

## timers connection establish

To set the time to wait for establishing TLS connection with the  remote server, use the timers connection establish tls command in SIP user-agent configuration mode. To reset this time to the default value, use the no form of this command.

timers connection establish tls timer-value

no timers connection establish tls

### Syntax Description

timer-value

Time to wait, in seconds, for successfully establishing a TLS connection with the remote server. Range is from 5 to 20. Default
                                          is 20.

### Command Default

20 seconds

### Command Modes

SIP user-agent configuration

## Command History

Release

Modification

This
                                          						command was introduced.

### Usage Guidelines

Use this command to set the time to wait for establishing a TLS connection with the remote server. The minimum value is 5
                              seconds and maximum value is 20 seconds. The default value is 20 seconds.

## Examples

The following example sets the time to wait before establishing a TLS connection:

```
router(config-sip-ua)#timer connection establish tls 10
```

### Related Commands

Command

Description

show sip-ua timers

Displays
                                          						the current settings for the SIP UA timers.

## timers disconnect

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits for a 200 response to a
                              		  BYE request, use the timers command
                              		  in SIP user-agent configuration mode or voice class tenant configuration modeTo
                              		  reset to the default, use the no form of this command.

timers disconnect time system

no timers disconnect time

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.1(1)T

This
                                          						command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300.

12.1(3)T

This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying).

12.2(2)XA

This
                                          						command was implemented on the Cisco AS5350 and Cisco AS400.

12.2(2)XB1

This
                                          						command was implemented on Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series. Supported for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          						Cisco AS5850 platforms is not included in this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

If you used the
                              		  previous more generic timers command
                              		  to configure timers, your previous timer settings are maintained. The output of
                              		  the show running-config command reflects both timers.

To reset this
                              		  command to the default value, you can also use the default command.

## Examples

The following
                              		  example sets disconnect time to 200 milliseconds:

```
sip-ua
 timers disconnect 200
```

The following
                              		  example sets disconnect time in the voice class tenant configuration mode:

```
Router(config-class)# timers disconnect system
```

### Related Commands

Command

Description

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

## timers dns

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits for the DNS resolved
                              		  address cache, use the timers dns command in SIP user-agent configuration mode
                              		  or voice class tenant configuration mode. To reset to the default, use the no
                              		  form of this command.

timers dns system

no timers dns

### Syntax Description

registrar-cache

DNS cache
                                          						refresh time for registrar.

time

Waiting
                                          						time, in seconds. Range is 60 to 65535. The default is 65535.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

65535 seconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

15.1(4)T

This
                                          						command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

If you used the
                              		  previous more generic timers command
                              		  to configure timers, your previous timer settings are maintained. The output of
                              		  the show running-config command reflects both timers.

To reset this
                              		  command to the default value, you can also use the default command.

## Examples

The following
                              		  example sets DNS cache refresh time to 200 seconds:

```
sip-ua
 timers dns registrar-cache 200
```

The following
                              		  example sets DNS cache refresh time in the voice class tenant configuration
                              		  mode:

```
Router(config-class)# timers dns registrar-cache system
```

### Related Commands

Command

Description

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

## timers expires

To set how long a
                              		  Session Initiation Protocol (SIP) INVITE request is valid, use the timers command
                              		  in SIP user-agent configuration mode or voice class tenant configuration mode.
                              		  To reset to the default, use the no form of this command.

timers expires time system

no timers expires

### Syntax Description

time

Expiration time, in ms. Range is 60,000 to 300,000. Default is 180000.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

180000 ms

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.1(1)T

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300.

12.1(3)T

This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying).

12.2(2)XA

This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This
                                          						command was implemented on the Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

If you used the
                              		  previous more generic timers command
                              		  to configure timers, your previous timer settings are maintained. The output of
                              		  the show running-config command reflects both timers.

To reset this
                              		  command to the default value, you can also use the default command.

## Examples

The following
                              		  example sets the expiration time to 180,000 ms:

```
sip-ua
 timers expires 180000
```

The following
                              		  example sets the expiration time in the voice class tenant configuration mode:

```
Router(config-class)# timers expires system
```

### Related Commands

Command

Description

default

Enables a
                                          						default aggregation cache.

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

timers

Configures the SIP signaling timers.

## timers hold

To enable the
                              		  Session Initiation Protocol (SIP) hold timer and configure the timer interval
                              		  before disconnecting a held call, use the timers hold command in SIP user-agent configuration mode
                              		  or voice class tenant configuration mode. To restore the default value, use the no form of this
                              		  command.

timers hold time system

no timers hold

### Syntax Description

time

Time (in
                                          						minutes) to wait before sending a BYE request. Range is 15 to 2880. Default is
                                          						2880.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

Enabled

time: 2880 minutes

### Command Modes

SIP user-agent configuration mode

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.3(1)

This
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

### Usage Guidelines

The hold timer is
                              		  typically activated when a gateway receives a call hold request from the other
                              		  endpoint, for example, a SIP phone.

## Examples

The following
                              		  example sets the hold timer to expire after 75 minutes:

```
Router(config-sip-ua)# t imers hold 75
```

The following
                              		  example sets the hold timer in the voice class tenant configuration mode:

```
Router(config-class)# timers hold system
```

### Related Commands

Command

Description

show
                                          						sip-ua timers

Displays
                                          						the current settings for SIP user agent timers.

suspend -
                                          						resume

Enables
                                          						SIP Suspend and Resume (call-hold) functionality.

timer
                                          						receive-rtcp

Enables
                                          						media inactivity Real-Time Control Protocol (RTCP) timer.

## timers info

To specify the wait time before INFO retransmission, use the timers info timers command in SIP user-agent configuration mode or voice class tenant configuration mode. To reset this value to the
                              default, use the no form of this command.

timers info milliseconds

no timers info

## Syntax Description

Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

voice class tenant configuration (config-class)

## Command History

Cisco IOS 15.6(2)T

This command was introduced.

Cisco IOS XE Dublin
                                             17.10.1a

Introduced support for YANG models.

## Examples

In sip-ua mode:

```
Device> enable Device# configure terminal Device(config)# sip-ua Device(config-sip-ua)# timers info 300
```

In voice class tenant mode:

```
Device> enable Device# configure terminal Device(config)# voice class tenant 1 Device(config-class)# timers info 300
```

## timers keepalive

To set the keepalive timers interval between sending Options message requests when the session initiation protocol (SIP) servers
                              are in the down state, use the timers keepalive command in SIP user agent configuration mode. To restore the keepalive timers to the default value of 120 seconds when active
                              or 30 seconds when down, use the no form of this command.

timers keepalive { active | down } seconds

no timers keepalive { active | down } seconds

### Syntax Description

active

SIP servers are in the active state.

down

SIP servers are in the down state.

seconds

Time in seconds between keepalive messages when the SIP servers are either active or down, as follows:

If active is specified, the range is from 10 to 600 seconds; the default value is 120 seconds.

If down is specified, the range is from 1 to 120 seconds; the default value is 30 seconds.

### Command Default

The default value for the active state is 120 seconds and the default value for the down state is 30 seconds.

### Command Modes

SIP user agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(6)T

This command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

Use this command to change the keepalive message time interval in seconds between the sending Options message requests when
                              the SIP server or servers are either in the active or down state.

## Examples

The following example sets the keepalive message time interval to 20 seconds when the SIP server is in the active state:

```
sip-ua
 timers keepalive active 20
```

The following example sets the keepalive message time interval to 10 seconds when the SIP server is in the down state:

```
sip-ua
 timers keepalive down 10
```

### Related Commands

Command

Description

busyout monitor keepalive

Selects a voice port or ports to be busied out in cases of a keepalive failure.

keepalive target

Identifies a SIP server that will receive keepalive packets from the SIP gateway.

keepalive trigger

Sets number of Options message requests that must consecutively receive responses from the SIP servers in order to unbusy
                                          the voice ports when in the down state.

retry keepalive

Sets the retry keepalive count for retransmissions.

## timers notify

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits before retransmitting a
                              		  Notify message, use the timers notify command in SIP user-agent configuration
                              		  mode or voice class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

timers notify time system

no timers notify

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(2)XB

This
                                          						command was introduced.

12.2(2)XB2

This
                                          						command was implemented on Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release.

Cisco IOS
                                          						XE Release 2.5

This
                                          						command was integrated into Cisco IOS XE Release 2.5.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

A Notify message
                              		  informs the user agent that initiated the transfer or Refer request about the
                              		  outcome of the SIP transaction.

## Examples

The following
                              		  example sets retransmission time to 500 milliseconds:

```
Router(config)# sip-ua Router(config-sip-ua)# timers notify 500
```

The following
                              		  example sets retransmission time in the voice class tenant configuration mode:

```
Router(config-class)# timers notify system
```

### Related Commands

Command

Description

show sip - ua statistics

Displays
                                          						response, traffic, timer, and retry statistics

show sip - ua timers

Displays
                                          						the current settings for SIP UA timers

## timers options

To specify the wait time before OPTIONS retransmission, use the timers options timers command in SIP user-agent configuration mode or voice class tenant configuration mode. To reset this value to the
                              default, use the no form of this command.

timers options milliseconds

no timers options

## Syntax Description

Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

voice class tenant configuration (config-class)

## Command History

Cisco IOS 15.6(2)T

This command was introduced.

Cisco IOS XE Dublin
                                             17.10.1a

Introduced support for YANG models.

## Examples

In sip-ua mode:

```
Device> enable Device# configure terminal Device(config)# sip-ua Device(config-sip-ua)# timers options 300
```

In voice class tenant mode:

```
Device> enable Device# configure terminal Device(config)# voice class tenant 1 Device(config-class)# timers options 300
```

## timers prack

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) wait s before retransmitting
                              		  a provisional response acknowledgement (PRACK) request, use the timers prack command in SIP user-agent configuration mode
                              		  or voice class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

timers prack time system

no timers prack

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(2)XB

This
                                          						command was introduced.

12.2(2)XB1

This
                                          						command was implemented on Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release.

12.2(11)T

This
                                          						command was applicable to the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in
                                          						this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

PRACK allows
                              		  reliable exchanges of SIP provisional responses between SIP endpoints. When the
                              		  retransmission value is set, retransmissions are sent with an exponential
                              		  backoff of up to 4 seconds. That is, the retransmission interval for each
                              		  packet increases exponentially until 4 seconds is reached.

## Examples

The following
                              		  example sets retransmission time to 500 milliseconds:

```
Router(config)# sip-ua Router(config-sip-ua)# timers prack 500
```

The following
                              		  example sets retransmission time in the voice class tenant configuration mode:

```
Router(config-class)# timers prack system
```

### Related Commands

Command

Description

show sip - ua statistics

Displays
                                          						response, traffic, timer, and retry statistics.

show sip - ua timers

Displays
                                          						the current settings for SIP UA timers.

timers comet

Sets
                                          						how long the UA waits before retransmitting a COMET request.

## timers refer

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits before retransmitting a
                              		  Refer request, use the timers refer command in SIP user-agent configuration mode
                              		  or voice class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

timers refer time system

no timers refer

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. Default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(11)YT

This
                                          						command was introduced.

12.2(15)T

This
                                          						command is supported on the Cisco 1700 series, Cisco 2600 series, Cisco 3600
                                          						series, and the Cisco 7200 series routers in this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

A SIP Refer request
                              		  is sent by the originating gateway to the receiving gateway and initiates call
                              		  forward and call transfer capabilities.

## Examples

The following
                              		  example sets retransmission time to 500 milliseconds:

```
Router(config)# sip-ua Router(config-sip-ua)# timers refer 500
```

The following
                              		  example sets retransmission time in the voice class tenant configuration mode:

```
Router(config-class)# timers refer system
```

### Related Commands

Command

Description

show sip - ua statistics

Displays
                                          						response, traffic, timer, and retry statistics.

show sip - ua timers

Displays
                                          						the current settings for SIP UA timers.

## timers register

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits before sending register
                              		  requests, use the timers register command in SIP user-agent configuration
                              		  mode or voice class tenant configuration mode. To reset this value to the
                              		  default, use the no form of this
                              		  command.

timers register milliseconds system

no timers register

### Syntax Description

milliseconds

Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. Default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(15)ZJ

This
                                          						command was introduced.

12.3(4)T

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(22)T

Support
                                          						for IPv6 was added.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

## Examples

The following
                              		  example sends register requests every 500 milliseconds:

```
sip-ua 
 retry invite 9
 retry register 9
 timers register 500
```

The following
                              		  example sends register requests in the voice class tenant configuration mode:

```
Router(config-class)# timers register system
```

### Related Commands

Command

Description

retry register

Sets the
                                          						total number of SIP registers to send.

## timers rel1xx

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) waits before retransmitting a
                              		  reliable1xx response, use the timers rel1xx command in SIP user-agent configuration
                              		  mode or voice class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

timers rel1xx time system

no timers rel1xx

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(2)XB

This
                                          						command was introduced.

12.2(2)XB1

This
                                          						command was implemented on Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release.

12.2(11)T

This
                                          						command is supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in
                                          						this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

## Examples

The following
                              		  example sets retransmission time to 400 milliseconds:

```
Router(config)# sip-ua Router(config-sip-ua)# timers rel1xx 400
```

The following
                              		  example sets retransmission time in the voice class tenant configuration mode:

```
Router(config-class)# timers rel1xx system
```

### Related Commands

Command

Description

retry rel1xx

Configures how many times the reliable1xx response is retransmitted.

show sip - ua statistics

Displays
                                          						response, traffic, timer, and retry statistics.

show sip - ua timers

Displays the current settings for SIP UA timers.

## timers trying

To set how long the
                              		  Session Initiation Protocol (SIP) user agent (UA) wait s for a 100 response to
                              		  a SIP INVITE request, use the timers command
                              		  in SIP user-agent configuration mode or voice class tenant configuration mode.
                              		  To reset to the default, use the no form of this command.

timers trying time system

no timers trying

### Syntax Description

time

Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500.

system

Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.1(1)T

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300.

12.1(3)T

This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying).

12.2(2)XA

This
                                          						command was implemented on Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This
                                          						command was implemented on Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series routers. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

If you used the
                              		  previous more generic timers command
                              		  to configure timers, your previous timer settings are maintained. The output of
                              		  the show running-config command reflects both timers.

To reset this
                              		  command to the default value, you can also use the default command.

## Examples

The following
                              		  example sets trying time to 500 milliseconds.

```
sip-ua
 timers trying 500
```

The following
                              		  example sets trying time in the voice class tenant configuration mode:

```
Router(config-class)# timers trying system
```

### Related Commands

Command

Description

sip-ua

Enables
                                          						the SIP user-agent configuration commands.

## timers update

To set how long the Session Initiation Protocol (SIP) user agent (UA) waits before sending update requests, use the timers update timers command in SIP user-agent configuration mode or voice class tenant configuration mode. To reset this value to the
                              default, use the no form of this command.

timers update milliseconds [system]

no timers update

## Syntax Description

Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500.

Uses the global sip-ua value. This keyword is available only for the tenant mode to allow it to fallback to the global configurations.

### Command Default

500 milliseconds

### Command Modes

SIP user-agent configuration

voice class tenant configuration (config-class)

## Command History

Cisco IOS 15.6(2)T and Cisco IOS XE Denali 16.3.1

This command was modified to include the keyword: system . This command is now available under voice class tenants.

Cisco IOS XE Dublin
                                             17.10.1a

Introduced support for YANG models.

### Usage Guidelines

Executing this command sets the wait time before sending update requests.

## Examples

In sip-ua mode:

```
Device> enable Device# configure terminal Device(config)# sip-ua Device(config-sip-ua)# timers update 300
```

In voice class tenant mode:

```
Device> enable Device# configure terminal Device(config)# voice class tenant 1 Device(config-class)# timers update 300
```

## timing answer-winkwidth

To specify the minimum duration delay between start of incoming seizure and wink in signal. Use the timing answer-winkwidth
                              command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing answer-winkwidth time

no timing answer-winkwidth time

### Syntax Description

time

Duration of the answer winkwidth delay in milliseconds. Range is from 110 to 290.

The default is 210

### Command Default

no timing answer-winkwidth

or

timing answer-winkwidth 210

### Command Modes

Voice-port configuration

## timing clear-wait

To set the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice port,
                              use the timing clear - wait command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing clear-wait time

no timing clear-wait time

### Syntax Description

time

Minimum time, in milliseconds, between an inactive seizure signal and the call being cleared. Cisco 3600 series range is from
                                          200 to 2000. The default for both is 400.

### Command Default

400 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 2600 and Cisco 3600 series routers.

### Usage Guidelines

This command is supported on E&M ports only.

## Examples

The following example sets the clear-wait duration on a voice port to 300 milliseconds:

```
voice-port 1/0/0
 timing clear-wait 300
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a specified voice port.

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

timeouts wait-release

Configures the timeout value for releasing voice ports.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

timing delay-with-integrity

Specifies the duration of the wink pulse for the delay dial for a specified voice port.

timing dialout-delay

Specifies the dialout delay for the sending digit on a specified voice port.

timing dial-pulse min-delay

Specifies the time between wink-like pulses for a specified voice port.

timing digit

Specifies the DTMF digit signal duration for a specified voice port.

timing interdigit

Specifies the DTMF interdigit duration for a specified voice port.

timing percentbreak

Specifies the percentage of a break period for a dialing pulse for a specified voice port.

timing pulse

Specifies the pulse dialing rate for a specified voice port.

timing pulse-interdigit

Specifies the pulse interdigit timing for a specified voice port.

timing wink-duration

Specifies the maximum wink signal duration for a specified voice port.

timing wink-wait

Specifies the maximum wink-wait duration for a specified voice port.

| seconds | Duration in seconds for which an FXO voice port stays in the connected state after the voice port detects a disconnect tone.
                                          Range is 1 to 120. The default is 60. |
|---|---|
| infinity | Disables disconnect supervision. The voice port does not disconnect when a disconnect tone is detected. |

| Release | Modification |
|---|---|
| 11.3(9)T | This command was introduced on Cisco 3600 series routers. |
| 12.0(4)T | This command was introduced on Cisco 3600 series routers. |
| 12.2(2)T | This command was implemented on Cisco 1750, Cisco 2600 series, and Cisco MC3810. The infinity keyword was added. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Specifies the delay time for releasing the calling voice port after a disconnect tone is received from the called voice port. |
| timing delay-duration | Configures the delay dial signal duration for a specified voice port. |

| seconds | Initial timeout duration, in seconds. Range is 0 to 120. The default is 10. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series routers. |

| Command | Description |
|---|---|
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |

| seconds | Interdigit timeout duration, in seconds. Range is 0 to 120. The default is 10. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |

| ms | Length of power denial, in milliseconds (ms). Range: 0 to 2500. Default: 750. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 12.4(2)T | The maximum value of the ms argument was increased from 1500 to 2500. |

| Command | Description |
|---|---|
| supervisory disconnect lcfo | Signals a disconnect on an FXS loop-start port by applying a power denial using a LCFO. |

| seconds | Duration, in seconds, for which a voice port allows ringing to continue if a call is not answered. Range is 5 to 60000. Default
                                          is 180 for nonSCCP-controlled ports. |
|---|---|
| infinity | Ringing continues until the caller goes on-hook. Default value for SCCP-controlled analog ports. |

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.4(11)T | The command default value was increased from 180 seconds to infinity for SCCP-controlled analog ports. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a voice port. |
| timeouts ringing (telephony-service) | Sets the timeout value for ringing in a Cisco Unified CallManager Express system. |

| seconds | Duration,
                                          						in seconds, for which a voice port stays in the call-failure state while the
                                          						Cisco router or concentrator sends a busy tone, reorder tone, or out-of-service
                                          						tone to the port. Range is 1 to 3600. Default is 30. |
|---|---|
| infinity | The voice
                                          						port is never released as long as the call-failure state remains. |

| Release | Modification |
|---|---|
| 11.3(1)
                                          						MA | This
                                          						command was introduced on Cisco MC3810. |
| 12.0(7)XK | This
                                          						command was implemented on Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This
                                          						command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a voice port. |

| seconds | Duration
                                          						in seconds for which an LMR voice port waits before tearing down an LMR
                                          						connection after detecting no voice activity. Valid values are 5 to 60000. The
                                          						default is 1800 seconds. |
|---|---|
| infinity | Disables
                                          						disconnect supervision. The voice port does not disconnect when no voice
                                          						activity is detected. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This
                                          						command was introduced. |
| 12.3(7)T | This
                                          						command was integrated into Cisco IOS Release 12.3(7)T. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Specifies the delay time for releasing the calling voice port after a
                                          						disconnect tone is received from the called voice port. |
| timeouts delay-duration | Configures the delay dial signal duration for a specified voice port. |

| value | Amount of allowed intermessage delay (in increments of 100 ms). Range is from 0 to 10. The default is 1 (100 ms). |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| call - router | Enables the Annex G border element configuration commands. |

| announce | Configures the lengh of time between announcement messages to the gatekeepers in the local cluster. |
|---|---|
| resource - update | Configures the lengh of time between resource update messages to gatekeepers in the local cluster. |
| seconds | Number of seconds between resource updates sent to the gatekeeper. The valid range is 1 to 60. There is no default value. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |
| 12.4(11)T | The resource - update keyword was introduced. |

| Command | Description |
|---|---|
| call-routing hunt-scheme | Enables capacity-based load-balancing. |
| zone cluster local | Defines a local grouping of gatekeepers. |
| zone remote | Statically specifies a remote zone if DNS is unavailable or undesirable. |

| minutes | Length, in minutes, of the interval between IRR messages. Range is from 1 to 60. The default is 4. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| timer lrq seq delay | Defines the time interval between successive LRQ messages. |
| timer lrq window | Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs. |
| timer server timeout | Specifies the timeout value for a response from a back-end GKTMP server. |

| time | Time interval, in 100-millisecond units. Range is 1 to 10 (0.1 to 1 second). The default is 5 (500 milliseconds). |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |

| Command | Description |
|---|---|
| timer lrq window | Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs. |

| time | Time interval, in 100-millisecond units. Range is 1 to 10 (0.1 to 1 second). The default is 1(100 milliseconds). |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |

| Note | This command cannot be configured at the same time as the timer lrq seq delay command. |
|---|---|

| Command | Description |
|---|---|
| timer lrq window decisec | Defines the time window during which the gatekeeper collects responses to one or more outstanding LRQs. |

| seconds | Time window, in seconds. Range is 1 to 15. The default is 3. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |

| Command | Description |
|---|---|
| timer lrq seq delay | Defines the time interval between successive sequential LRQs. |

| time | Time window, in seconds. Range is 1 to 15. The default is 2. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |

| Note | This command cannot be in effect at the same time as the timer lrq window command. |
|---|---|

| Command | Description |
|---|---|
| timer lrq seq delay centsec | Defines the time interval between successive sequential LRQs. |

| multiple | Multiples of the RTCP report transmission interval. Range is 4 to 1000. The default is 5, and the recommended value is 5. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |

| Command | Description |
|---|---|
| ip rtcp report interval | Configures the minimum interval of RTCP report transmissions. |

| timer | Multiples of the RTCP report transmission interval. Range is 0 to 1000. Default is 0. Recommended value is 5. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |

| Command | Description |
|---|---|
| debug cch323 h225 | Traces the state transition of the gateway H.225 state machine based on the processed events. |
| debug ccsip events | Displays all SIP SPI events tracing and traces the events posted to SIP SPI from all interfaces. |
| ip rtcp report interval | Configures the minimum interval of RTCP report transmissions. |

| seconds | Timer value, in seconds. Range: 180 to 86400. Default: 1200. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.4(20)T | This command was modified. The recommended timer range is defined as 1200 seconds. |

| Command | Description |
|---|---|
| codec (dspfarm-profile) | Specifies the codecs supported by a DSP farm profile. |
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for DSP farm services. |
| maximum sessions (dspfarm-profile) | Specifies the maximum number of sessions that need to be supported by the profile. |

| seconds | Number of seconds for which the gatekeeper should wait before retrying the GKTMP server. Range is from 1 through 300. The
                                          default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| timer server timeout | Specifies the timeout value for a response from a back-end GKTMP server. |

| time | Timeout interval, in 100-ms units. Range is 1 to 50 (0.1 to 5 seconds). Default is 3 (300 ms). |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| server registration - port | Configures the listener port for the server to establish a connection with the gatekeeper. |
| server trigger | Configures a static server trigger for external applications. |

| trying number | Time (in ms) to wait for a 100 response to an INVITE request. Range is from 100 to 1000. Default is 500. |
|---|---|
| connect number | Time (in ms) to wait for a 200 response to an ACK request. Range is from 100 to 1000. Default is 500. |
| disconnect number | Time (in ms) to wait for a 200 response to a BYE request. Range is from 100 to 1000. Default is 500. |
| expires number | Time (in ms) for which an INVITE request is valid. Range is from 60000 to 300000. Default is 180000. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.1(3)T | This command was modified to change the names of the parameters. Two of the parameters ( invite - wait - 180 and invite - wait - 200 ) were combined into one ( trying ). |
| 12.2(2)XA | This command was implemented on the Cisco AS5400 and AS5350. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco 7200 series routers. Support for the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models under SIP user agent configuration mode. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models under voice class tenant configuration
                                          mode. |

| Command | Description |
|---|---|
| default | Sets a command to its default. |
| inband
                                          -
                                          alerting | Specifies an inband-alerting SIP header. |
| max
                                          -
                                          forwards | Specifies the maximum number of hops for a request. |
| retry 
                                          (
                                          SIP user
                                          -
                                          agent
                                          ) | Configures the SIP signaling timers for retry attempts. |
| transport | Enables SIP UA transport for TCP/UDP. |

| timer | Buffer-invite timer value, in ms. Range is 50 to 5000. |
|---|---|
| system | Specifies
                                          						that the buffer-invite timer use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations. |

| Release | Modification |
|---|---|
| 12.3(8)T | This
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Note | For more details on the command isdn supp-service name calling , see isdn supp-service name calling . |
|---|---|

| Command | Description |
|---|---|
| sip-ua | Enables
                                          						SIP user-agent configuration commands. |

| time | Waiting time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was inplemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |

| Command | Description |
|---|---|
| show sip - ua statistics | Displays response, traffic, timer, and retry statistics. |
| show sip - ua timers | Displays the current settings for SIP UA timers. |
| timers prack | Sets how long the UA waits before retransmitting a PRACK request. |

| number | Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.1(1)T | This
                                          						command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300. |
| 12.1(3)T | This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying). |
| 12.2(2)XA | This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This
                                          						command was implemented on the Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          						Cisco AS5850 is not included in this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |

| timer-value | Time to
                                          						wait, in minutes, before aging out a TCP or UDP connection because of
                                          						inactivity. Range is from 5 to 30. Default is 5. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.3(8)T | This
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show sip-ua timers | Displays
                                          						the current settings for the SIP UA timers. |
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |
| timers expires | Sets how
                                          						long a SIP INVITE request is valid. |

| timer-value | Time to wait, in seconds, for successfully establishing a TLS connection with the remote server. Range is from 5 to 20. Default
                                          is 20. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.4.1a | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| show sip-ua timers | Displays
                                          						the current settings for the SIP UA timers. |

| time | Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.1(1)T | This
                                          						command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300. |
| 12.1(3)T | This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying). |
| 12.2(2)XA | This
                                          						command was implemented on the Cisco AS5350 and Cisco AS400. |
| 12.2(2)XB1 | This
                                          						command was implemented on Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series. Supported for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          						Cisco AS5850 platforms is not included in this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |

| registrar-cache | DNS cache
                                          						refresh time for registrar. |
|---|---|
| time | Waiting
                                          						time, in seconds. Range is 60 to 65535. The default is 65535. |
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 15.1(4)T | This
                                          						command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |

| time | Expiration time, in ms. Range is 60,000 to 300,000. Default is 180000. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.1(1)T | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300. |
| 12.1(3)T | This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying). |
| 12.2(2)XA | This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This
                                          						command was implemented on the Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| default | Enables a
                                          						default aggregation cache. |
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |
| timers | Configures the SIP signaling timers. |

| time | Time (in
                                          						minutes) to wait before sending a BYE request. Range is 15 to 2880. Default is
                                          						2880. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.3(1) | This
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |

| Command | Description |
|---|---|
| show
                                          						sip-ua timers | Displays
                                          						the current settings for SIP user agent timers. |
| suspend -
                                          						resume | Enables
                                          						SIP Suspend and Resume (call-hold) functionality. |
| timer
                                          						receive-rtcp | Enables
                                          						media inactivity Real-Time Control Protocol (RTCP) timer. |

| milliseconds | Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS 15.6(2)T | This command was introduced. |
| Cisco IOS XE Dublin
                                             17.10.1a | Introduced support for YANG models. |

| active | SIP servers are in the active state. |
|---|---|
| down | SIP servers are in the down state. |
| seconds | Time in seconds between keepalive messages when the SIP servers are either active or down, as follows: If active is specified, the range is from 10 to 600 seconds; the default value is 120 seconds. If down is specified, the range is from 1 to 120 seconds; the default value is 30 seconds. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| busyout monitor keepalive | Selects a voice port or ports to be busied out in cases of a keepalive failure. |
| keepalive target | Identifies a SIP server that will receive keepalive packets from the SIP gateway. |
| keepalive trigger | Sets number of Options message requests that must consecutively receive responses from the SIP servers in order to unbusy
                                          the voice ports when in the down state. |
| retry keepalive | Sets the retry keepalive count for retransmissions. |

| time | Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This
                                          						command was introduced. |
| 12.2(2)XB2 | This
                                          						command was implemented on Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release. |
| Cisco IOS
                                          						XE Release 2.5 | This
                                          						command was integrated into Cisco IOS XE Release 2.5. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show sip - ua statistics | Displays
                                          						response, traffic, timer, and retry statistics |
| show sip - ua timers | Displays
                                          						the current settings for SIP UA timers |

| milliseconds | Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS 15.6(2)T | This command was introduced. |
| Cisco IOS XE Dublin
                                             17.10.1a | Introduced support for YANG models. |

| time | Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This
                                          						command was introduced. |
| 12.2(2)XB1 | This
                                          						command was implemented on Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release. |
| 12.2(11)T | This
                                          						command was applicable to the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in
                                          						this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show sip - ua statistics | Displays
                                          						response, traffic, timer, and retry statistics. |
| show sip - ua timers | Displays
                                          						the current settings for SIP UA timers. |
| timers comet | Sets
                                          						how long the UA waits before retransmitting a COMET request. |

| time | Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. Default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.2(11)YT | This
                                          						command was introduced. |
| 12.2(15)T | This
                                          						command is supported on the Cisco 1700 series, Cisco 2600 series, Cisco 3600
                                          						series, and the Cisco 7200 series routers in this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show sip - ua statistics | Displays
                                          						response, traffic, timer, and retry statistics. |
| show sip - ua timers | Displays
                                          						the current settings for SIP UA timers. |

| milliseconds | Waiting
                                          						time, in milliseconds. Range is from 100 to 1000. Default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This
                                          						command was introduced. |
| 12.3(4)T | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(22)T | Support
                                          						for IPv6 was added. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| retry register | Sets the
                                          						total number of SIP registers to send. |

| time | Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This
                                          						command was introduced. |
| 12.2(2)XB1 | This
                                          						command was implemented on Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this
                                          						release. |
| 12.2(11)T | This
                                          						command is supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in
                                          						this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . This
                                          									command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| retry rel1xx | Configures how many times the reliable1xx response is retransmitted. |
| show sip - ua statistics | Displays
                                          						response, traffic, timer, and retry statistics. |
| show sip - ua timers | Displays the current settings for SIP UA timers. |

| time | Waiting
                                          						time, in milliseconds. Range is 100 to 1000. The default is 500. |
|---|---|
| system | Use the
                                          						global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.1(1)T | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						AS5300. |
| 12.1(3)T | This
                                          						command was modified to change the names of the parameters. Two of the
                                          						parameters (invite-wait-180 and invite-wait-200) were combined into one
                                          						(trying). |
| 12.2(2)XA | This
                                          						command was implemented on Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This
                                          						command was implemented on Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco
                                          						7200 series routers. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip-ua | Enables
                                          						the SIP user-agent configuration commands. |

| milliseconds | Waiting time, in milliseconds. Range is from 100 to 1000. Default is 500. |
|---|---|
| system | Uses the global sip-ua value. This keyword is available only for the tenant mode to allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| Cisco IOS 15.6(2)T and Cisco IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . This command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                             17.10.1a | Introduced support for YANG models. |

| time | Duration of the answer winkwidth delay in milliseconds. Range is from 110 to 290. The default is 210 |
|---|---|

| time | Minimum time, in milliseconds, between an inactive seizure signal and the call being cleared. Cisco 3600 series range is from
                                          200 to 2000. The default for both is 400. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 2600 and Cisco 3600 series routers. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |