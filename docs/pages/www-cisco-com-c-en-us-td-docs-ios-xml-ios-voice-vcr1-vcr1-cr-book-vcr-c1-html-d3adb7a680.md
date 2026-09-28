---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr1-vcr1-cr-book-vcr-c1-html-d3adb7a680
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr1/vcr1-cr-book/vcr-c1.html
retrieved_at: 2026-08-16T23:15:19.946757+00:00
---

Cisco IOS Voice Command Reference - A through C

# Cisco IOS Voice Command Reference - A through C

Updated: April 25, 2026

Chapter: cable detect through call application stats

## Chapter: cable detect through call application stats

# cable detect through call application stats

## cable-detect

To enable cable polling on an analog Foreign Exchange Office (FXO) voice port, use the cable-detect command in voice port configuration mode. To disable cable polling, use the no form of this command.

cable-detect

no cable-detect

### Syntax Description

This command has no arguments or keywords.

### Command Default

Cable polling on an analog FXO voice port is disabled.

### Command Modes

Voice port configuration (config-voiceport)

## Command History

Release

Modification

15.1(1)T

This command was introduced.

15.2(4)M

This command was modified. Cable polling was extended to analog Foreign Exchange Office End Ground Start (FXOGS), Foreign
                                          Exchange Office End Loop Start (FXOLS), Foreign Exchange Station End Ground Start (FXSGS), and Foreign Exchange Station End
                                          Loop Start (FXSLS) voice ports.

### Usage Guidelines

The FXOLS voice port is in the busyout state if the Digital Signal Processor (DSP) detects that no cable is connected between
                              the analog FXSLS and FXOLS ports. If you have configured the no cable-detect command and the analog FXOLS voice port is in busyout state because no cable is connected, the Cisco software stops polling
                              the cable connection. The analog FXOLS voice port remains in the busyout state until you use the shutdown and no shutdown commands to switch the analog FXOLS voice port to the idle state. The cable-detect command supports loop start and Central Automatic Message Accounting (CAMA) signaling.

Unlike FXOLS, for analog FXOGS, FXSLS, and FXSGS voice ports, the voice port state does not change when the cable status
                              changes from connected to disconnected or disconnected to connected; only a syslog message is printed to indicate the new
                              cable status. The cable-detect command will not show up under the voice port if the analog voice interface does not support cable polling.

For analog FXOGS, the cable-detect command can be configured on all FXO voice interface cards.

This command can be configured on the following analog FXOLS voice interface cards (VICs):

VIC2-2FXS

VIC2-4FXS

EM-HDA-6FXO

EM-HDA-3FXS-4FXO

EM-HDA-4FXO

For analog FXSLS and FXSGS, this command can be configured on the following FXS voice interface cards:

VIC3-2FXS/DID

VIC3-4FXS/DID

VIC3-2FXS-E/DID

EM3-HDA-8FXS/DID

SM-D-72FXS

SM-D-48FXS-E

Onboard analog FXS on Cisco 8xx platforms

Onboard analog FXS on Cisco VG20x and VG2435 platforms

## Examples

The following example shows how to enable cable polling on an FXOLS voice port:

```
Device> enable Device# configure terminal Device(config)# voice-port 1/2/3 Device(config-voiceport)# cable-detect
```

### Related Commands

Command

Description

shutdown

Changes the state of the voice ports for a specific voice interface card to offline.

## cable-detect-poll-timer

To configure the cable polling timer value for background polling processes on an analog voice port, use the cable-detect-poll-timer command in voice service configuration mode. To disable the polling timer, use the no form of this command.

cable-detect-poll-timer timer-value

no cable-detect-poll-timer

### Syntax Description

timer-value

Cable polling timer value in minutes. The range is from 0 to 1440.

### Command Default

The cable polling on analog voice ports is disabled.

### Command Modes

Voice service configuration (conf-voi-serv)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

Use the cable-detect-poll-timer command to configure the cable polling timer value on analog Foreign Exchange Office End Ground Start (FXOGS), Foreign Exchange
                              Office End Loop Start (FXOLS), Foreign Exchange Station End Ground Start (FXSGS), and Foreign Exchange Station End Loop Start
                              (FXSLS) voice ports.

## Examples

The following example shows how to enable cable polling on an FXOLS voice port:

```
Device> enable Device# configure terminal Device(config)# voice service pots Device(conf-voi-serv)# cable-detect-poll-timer 100
```

### Related Commands

Command

Description

cable-detect

Enables cable polling on analog FXOGS, FXOLS, FXSGS, and FXSLS voice ports.

## cac_off

To disable connection admission control (CAC), use the cac_off command in interface-ATM-VC configuration mode. To enable CAC, use the no form of this command.

cac_off

no cac_off

### Syntax Description

This command has no keywords or arguments.

### Command Default

Call admission control is enabled.

### Command Modes

Interface-ATM-VC configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

Connection admission control (CAC) is a set of actions taken by each ATM switch during connection setup to determine whether
                              the requested quality of service (QoS) will violate the QoS guarantees for established connections. CAC reserves bandwidth
                              for voice calls, however, the bandwidth required when the lossless compression codec (LLCC) is used is dynamic and usually
                              less than what is generally reserved by CAC. Disabling CAC can help in better utilization of bandwidth when LLCC is used.

## Examples

The following example disables call admission control on a PVC:

```
interface ATM0/IMA1.1 point-to-point
 pvc test1 15/135
  cac_off
```

## cache (neighbor BE)

To configure the local border element (BE) to cache the descriptors received from its neighbors, use the cache command in neighbor BE configuration mode. To disable caching, use the no form of this command.

cache

no cache

### Syntax Description

This command has no arguments or keywords.

### Command Default

Caching is not enabled

### Command Modes

Neighbor BE configuration (config-annexg-neigh)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300 universal access server, Cisco AS5350,
                                          Cisco AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Use this command to configure the local BE to cache the descriptors received from its neighbor. If caching is enabled, the
                              neighbors are queried at the specified interval for their descriptors.

## Examples

The following example shows the border element enabled to cache the descriptors from its neighbors.

```
Router(config-annexg-neigh)# id neighbor-id Router(config-annexg-neigh)# cache
```

### Related Commands

Command

Description

id

Configures the local ID of the neighboring BE.

port

Configures the neighbor’s port number that is used for exchanging Annex G messages.

query-interval

Configures the interval at which the local BE queries the neighboring BE.

## cache reload time (global application configuration mode)

To configure the router to reload scripts from cache on a regular interval, use the cache reload time command in global application configuration mode. To set the value to the default, use the no form of this command.

cache reload time bg-minutes

no cache reload time

### Syntax Description

bg - minutes

Number of minutes after which the background process is awakened. This background process checks the time elapsed since the
                                          script was last used and whether the script is current:

If the script has not been used in the last "unload time," it unloads the script and quits. The unload time is not configurable.

If the script has been used, the background process loads the script from the URL. It compares the scripts, and if they do
                                                not match, it begins using the new script for new calls.

### Command Default

30 minutes

### Command Modes

Global application configuration

## Command History

Release

Modification

12.3(14)T

The call application cache reload time command was moved to global application configuration mode and changed to cache reload time .

## Examples

The following example displays the cache reload time command configured to specify 15 minutes before a background process is awakened:

Enter application configuration mode to configure applications and services:

```
application
```

Enter global application configuration mode:

```
global
```

Configure the cache reload time:

```
cache reload time 15
```

### Related Commands

Command

Description

call application cache reload time

Configures the router to reload the MGCP scripts from cache on a regular interval.

show call application voice

Displays all Tcl or MGCP scripts that are loaded.

## cadence

To define the tone-on and tone-off durations for a call-progress tone, use the cadence command in call-progress 
                              dualtone 
                              configuration mode. To restore the default cadence, use the no form of this command.

{ cadence cycle-1-on-time cycle-1-off-time [ cycle-2-on-time cycle-2-off-time ] [ cycle-3-on-time cycle-3-off-time ] [ cycle-4-on-time cycle-4-off-time ] | continuous }

no cadence

### Syntax Description

cycle-1-on-time

Tone-on duration for the first cycle of the cadence pattern, in milliseconds (ms). Range is from 0 to 1000. The default is
                                          0.

cycle-1-off-time

Tone-off duration for the first cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default is 0.

cycle-2-on-time

(Optional) Tone-on duration for the second cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

cycle-2-off-time

(Optional) Tone-off duration for the second cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

cycle-3-on-time

(Optional) Tone-on duration for the third cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

cycle-3-off-time

(Optional) Tone-off duration for the third cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

cycle-4-on-time

(Optional) Tone-on duration for the fourth cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

cycle-4-off-time

(Optional) Tone-off duration for the fourth cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0.

continuous

Continuous call-progress tone is detected.

### Command Default

Continuous

### Command Modes

Call-progress dualtone configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810.

12.2(2)T

This command was implemented on the Cisco 1750 and integrated into Cisco IOS Release 12.2(2)T.

### Usage Guidelines

This command specifies the cadence for a class of custom call-progress tones.

You must define each cadence that you want a voice port to detect. Reenter the command for each additional cadence to be detected.

You must associate the class of custom call-progress tones with a voice port for this command to affect tone detection.

## Examples

The following example defines a cadence for a busy tone in the custom-cptone voice class with the name "country-x." This example
                              defines 500 ms tone on and 500 ms tone off.

```
voice class custom-cptone country-x
 dualtone busy
 cadence 500 500
```

The following example configures detection of the default frequency and cadence values for the busy tone in the custom-cptone
                              voice class with the name "country-x". The default frequency is a 300 Hz tone, and the default cadence is continuous.

```
voice class custom-cptone country-x
 dualtone busy
 no cadence
 no frequency
```

### Related Commands

Command

Description

supervisory custom-cptone

Associates a class of custom call-progress tones with a voice port.

voice class custom-cptone

Creates a voice class for defining custom call-progress tones.

voice class dualtone-detect-params

Modifies the boundaries and limits for custom call-progress tones defined by the voice class custom-cptone command.

## cadence-list

To specify a tone cadence pattern to be detected, use the cadence-list command in voice-class configuration mode. To delete a cadence pattern, use the no form of this command.

cadence-list cadence-id cycle-1-on-time cycle-1-off-time [ cycle-2-on-time cycle-2-off-time ] [ cycle-3-on-time cycle-3-off-time ] [ cycle-4-on-time cycle-4-off-time ]

no cadence-list cadence-id

### Syntax Description

cadence-id

A tag to identify this cadence list. The range is from 1 to 10.

cycle-1-on-time

The tone duration for the first cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds). The
                                          default is 0.

cycle-1-off-time

The silence duration for the first cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0.

cycle-2-on-time

(Optional) The tone duration for the second cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0.

cycle-2-off-time

(Optional) The silence duration for the second cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0.

cycle-3-on-time

(Optional) The tone duration for the third cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0.

cycle-3-off-time

(Optional) The silence duration for the third cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0.

cycle-4-on-time

(Optional) The tone duration for the fourth cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0.

cycle-4-off-time

(Optional) The silence duration for the fourth cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0.

### Command Default

No cadence pattern is configured.

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, the Cisco MC3810.

### Usage Guidelines

A cadence list enables the router to match a complex tone pattern from a PBX or public switched telephone network (PSTN).
                              A tone is detected if it matches any configured cadence list. You can create up to ten cadence lists, enabling the router
                              to detect up to ten different tone patterns. If the tone to be detected consists of only one on-off cycle, you can configure
                              this in either of two ways:

Create a cadence list using only the cycle-1-on-time and cycle-1-off-time variables .

Use the cadence-max-off-time and cadence-min-on-time commands.

You must also configure the times of the cadence-max-off-time and cadence-min-on-time commands to be compatible with the on and off times specified by the cadence-list command. The time of the cadence-max-off-time must be equal to or greater than the longest off-time in the cadence list; the cadence-min-on-time must be equal to or less than the shortest on-time in the cadence list.

## Examples

The following example shows configuration of cadence list 1 with three on/off cycles and cadence list 2 with two on/off cycles
                              for voice class 100:

```
voice class dualtone 100
 cadence-list 1 100 100 300 300 100 200
 cadence-list 2 100 200 100 400
```

### Related Commands

Command

Description

cadence-max-off-time

Specifies the maximum off duration for detection of a tone.

cadence-min-on-time

Specifies the minimum on duration for detection of a tone.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## cadence-max-off-time

To specify the maximum time that a tone can be off and still detected
                              		  as part of a cadence, use the cadence-max-off-time command in voice-class
                              		  configuration mode. To restore the default, use the no form of this command.

cadence-max-off-time time

no cadence-max-off-time

### Syntax Description

time

The maximum off time of a tone that can be detected, in
                                          						10-millisecond increments. Range is from 0 to 5000 (0 milliseconds to 50
                                          						seconds). The default is 0.

### Command Default

0 (no off time)

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco
                                          						3600 series and the Cisco MC3810.

### Usage Guidelines

Specify a time value greater than the off time of the tone to be
                              		  detected, and use a time value greater than 0 to enable detection of a cadenced
                              		  tone. With the default (0), the router detects only a continuous tone.

## Examples

The following example shows configuration of a maximum off duration
                              		  of 20 seconds for voice class 100:

```
voice class dualtone 100
 cadence-max-off-time 2000
```

### Related Commands

Command

Description

cadence-min-on-time

Specifies the minimum on duration for detection of a tone.

cadence-variation

Specifies the cadence variation time allowed for detection
                                          						of a tone.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## cadence-min-on-time

To specify the minimum time that a tone can be on and still detected as part of a cadence, use the cadence-min-on-time command in voice-class configuration mode. To restore the default, use the no form of this command.

cadence-min-on-time time

no cadence-min-on-time

### Syntax Description

time

The minimum on time of a tone that can be detected, in 10-millisecond increments. Range is from 0 to 100 (0 milliseconds to 1 seconds). The
                                          default is 0.

### Command Default

0 (no minimum on time)

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series and the Cisco MC3810.

### Usage Guidelines

Specify a time value shorter than the on time of the tone to be detected. With the default (0), a tone of any length is detected.

## Examples

The following example shows configuration of a minimum on duration of 30 milliseconds (three 10-ms time intervals) for voice
                              class 100:

```
voice class dualtone 100
 cadence-min-on-time 3
```

### Related Commands

Command

Description

cadence-max-off-time

Specifies the maximum off duration for detection of a tone.

cadence-variation

Specifies the cadence variation time allowed for detection of a tone.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## cadence-variation

To specify the cadence variation time allowed for detection of a tone, use the cadence-variation command in voice-class configuration mode. To restore the default cadence variation time, use the no form of this command.

cadence-variation time

no cadence-variation

### Syntax Description

time

The maximum time by which the tone onset can vary from the specified onset time and still be detected, in 10-millisecond
                                          increments. Range is from 0 to 200 (0 milliseconds to 2 seconds). The default is 10.

### Command Default

10 milliseconds

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810.

12.1(5)XM

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750 router.

### Usage Guidelines

Specify a time value greater than the cadence variation of the tone to be detected. With the default of 0, only those tones
                              that match the configured cadence are detected.

This command creates a detection limit for one parameter within a voice class. You can apply the detection limit to any voice
                              port.

## Examples

The following example specifies a cadence variation time of 30 milliseconds for voice class 100:

```
voice class dualtone 100
 cadence-variation 3
```

The following example specifies 80 ms (eight 10-ms time intervals) as the maximum allowable cadence variation in voice class
                              70:

```
voice class dualtone-detect-params 70
 cadence-variation 8
```

### Related Commands

Command

Description

cadence-max-off-time

Specifies the maximum off duration for detection of a tone.

cadence-min-on-time

Specifies the minimum on duration for detection of a tone.

supervisory answer dualtone

Enables answer supervision on a voice port.

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port.

## call accounting-template

To select an accounting template at a specific location, use the call accounting-template command in global configuration or application configuration mode. To deselect a specific accounting template, use the no form of this command.

call accounting-template acctTempName url

no call accounting-template acctTempName url

### Syntax Description

acctTempName

Template name.

url

Location of the template.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config) Application configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850.

12.3(14)T

This command was added to the application configuration mode to replace the call application voice accounting-template command.

### Usage Guidelines

For call detail records, the template name must have a .cdr extension. To select call records based on your accounting needs
                              and to specify the location of an accounting template that defines the applicable vendor-specific attributes (VSAs) for generating
                              those selected call records, use the call accounting-template command in global configuration mode.

The acctTempName argument refers to a specific accounting template file that you want to send to the RADIUS server. This template file defines
                              only specific VSAs selected by you to control your call records based on your accounting needs.

## Examples

The example below shows the accounting template cdr1 selected from a specific TFTP address.

```
call accounting-template temp-ivr tftp://kyer/sample/cdr/cdr1.cdr
```

### Related Commands

Command

Description

call application voice accounting-template

Configures T.37 fax accounting with VoIP AAA nonblocking API.

show call accounting-template voice

Selects an accounting template at a specific location.

## call accounting-template voice

To select an accounting template at a specific location, use the call accounting-template voice command in global configuration mode. To remove a specific accounting template, use the no form of this command.

call accounting-template voice acctTempName url

no call accounting-template voice acctTempName url

### Syntax Description

acctTempName

Template name.

url

Location of the template.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850.

12.3(14)T

The call accounting-template voice command is replaced by the call accounting-template command in application configuration mode. See the call accounting-template command for more information.

### Usage Guidelines

The template name must have a .cdr extension.

To select call records based on your accounting needs and to specify the location of an accounting template that defines the
                              applicable vendor-specific attributes (VSAs) for generating those selected call records, use the call accounting-template voice command in global configuration mode.

The acctTempName argument refers to a specific accounting template file that you want to send to the RADIUS server. This template file defines
                              only specific VSAs selected by you to control your call records based on your accounting needs.

## Examples

The example below shows the accounting template cdr1 selected from a specific TFTP address.

```
call accounting-template voice temp-ivr tftp://kyer/sample/cdr/cdr1.cdr
```

### Related Commands

Command

Description

call accounting-template voice reload

Reloads the accounting template.

show call accounting-template voice

Selects an accounting template at a specific location.

## call accounting-template voice reload

To reload the accounting template, use the call accounting-template voice reload command in privileged EXEC mode.

call accounting-template voice reload acctTempName

### Syntax Description

reload

Reloads the accounting template from the address (for example, a tftp address) where the template is stored.

acctTempName

Name of the accounting template.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850.

### Usage Guidelines

Use the call accounting-template voice reload command to reload the template from the URL defined in the call accounting-template voice command. After bootup, if the template file fails to load from the TFTP server, the system tries to automatically reload
                              the file at 5-minute intervals.

## Examples

The example below shows how to reload accounting template cdr2:

```
call accounting-template voice reload cdr2
```

### Related Commands

Command

Description

call accounting-template voice

Selects an accounting template at a specific location

gw-accounting aaa

Defines and loads the template file at the location defined by the URL.

show call accounting-template voice

Displays the VSAs that are contained in the accounting template.

## call-agent

To define the call agent for a Media Gateway Control Protocol (MGCP) profile, use the call-agent command in MGCP profile configuration mode. To return to the default values, use the no form of this command.

call-agent { dns-name | ip-address } [port] [ service-type type ] [ version protocol-version ]

no call-agent

### Syntax Description

dns-name

Fully qualified domain name (including host portion) for the call agent. For example, "ca123.example.net".

ip-address

IP address of the call agent.

port

(Optional) User Datagram Protocol (UDP) port number over which the gateway sends messages to the call agent. Range is from
                                          1025 to 65535.

The default call-agent UDP port is 2727 for MGCP 1.0, Network-based Call Signaling (NCS) 1.0, and Trunking Gateway Control
                                                Protocol (TGCP) 1.0.

The default call-agent UDP port is 2427 for MGCP 0.1 and Simple Gateway Control Protocol (SGCP).

service-type type

(Optional) Protocol service type valid values for the type argument are mgcp , ncs , sgcp , and tgcp . The default service type is mgcp .

version protocol-version

(Optional) Version number of the protocol. Valid values follow:

Service-type MGCP-- 0.1 , 1.0

Service-type NCS-- 1.0

Service-type SGCP-- 1.1 , 1.5

Service-type TGCP-- 1.0

The default service type and version are mgcp and 0.1 .

### Command Default

The default call-agent UDP port is 2727 for MGCP 1.0, Network-based Call Signaling (NCS) 1.0, and Trunking Gateway Control
                              Protocol (TGCP) 1.0.
                              The default call-agent UDP port is 2427 for MGCP 0.1 and Simple Gateway Control Protocol (SGCP).
                              The default service type and version are MGCP 0.1.

### Command Modes

MGCP profile configuration (config-mgcp-profile)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when values for a MGCP profile are configured.

Call-agent configuration for an MGCP profile (with this command) and global call-agent configuration (with the mgcp call-agent command) are mutually exclusive; the first to be configured on an endpoint blocks configuration of the other on the same
                              endpoint.

Identifying call agents by Domain Name System (DNS) name rather than by IP address in the call-agent command provides call-agent redundancy, because a DNS name can have more than one IP address associated with it. If a call
                              agent is identified by a DNS name and a message from the gateway fails to reach the call agent, the max1 lookup and max2 lookup commands enable a search from the DNS lookup table for a backup call agent at a different IP address.

The port argument configures the call agent port number (the UDP port over which the gateway sends messages to the call agent). The
                              reverse, or the gateway port number (the UDP port over which the gateway receives messages from the call agent), is configured
                              by specifying a port number in the mgcp command.

The service type mgcp supports the Restart In Progress (RSIP) error messages sent by the gateway if the mgcp sgcp restart notify command is enabled. The service type sgcp ignores the RSIP messages.

## Examples

The following example defines a call agent for the MGCP profile named "tgcp_trunk":

```
Router(config)# mgcp profile tgcp_trunk Router(config-mgcp-profile)# call-agent 10.13.93.3 2500 service-type tgcp version 1.0
```

### Related Commands

Command

Description

max1 lookup

Enables DNS lookup of the MGCP call agent address when the suspicion threshold value is reached.

max2 lookup

Enables DNS lookup of the MGCP call agent address when the disconnect threshold value is reached.

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp call-agent

Configures the address of the call agent (media gateway controller).

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## call application alternate

Effective with Cisco IOS Release 12.3(14)T, the call application alternate command is replaced by the service command in global application configuration mode. See the service command for more information.

To specify an alternate application to use if the application that is configured in the dial peer fails, use the call application alternate command in global configuration mode. To return to the default behavior, use the no form of this command.

call application alternate [application-name]

no call application alternate

### Syntax Description

application-name

(Optional) Name of the specific voice application to use if the application in the dial peer fails. If a specific application
                                          name is not entered, the gateway uses the DEFAULT application.

### Command Default

The call is rejected if the application in the dial peer fails.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

12.3(14)T

This command was replaced by the service command in global application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

If this command is not configured, calls are rejected when the dial peer that matches the call does not specify a valid voice
                              application.

In releases before Cisco IOS Release 12.2(11)T, the default application (DEFAULT) was automatically triggered if no application
                              was configured in the dial peer or if the configured application failed. The default application is no longer automatically
                              executed unless the call application alternate command is configured.

The application named DEFAULT is a simple application that outputs dial tone, collects digits, and places a call to the dialed
                              number. This application is included in Cisco IOS software; you do not have to download it or configure it by using the call application voice command.

The call application alternate command specifies that if the application that is configured in the dial peer fails, the default voice application is executed.
                              If the name of a specific application is entered, that application is triggered if the application configured in the dial
                              peer fails. If the alternate application also fails, the call is rejected.

If an application name is entered, that application must first be configured on the gateway by using the call application voice command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application alternate 
	Warning: This command has been deprecated. Please use the following:
		service
```

The following example configures the DEFAULT application as the alternate:

```
call application alternate
```

The following example configures the application session as the alternate:

```
call application alternate session
```

### Related Commands

Command

Description

application

Enables a voice application on a dial peer.

call application voice

Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application.

service

Loads and configures a specific, standalone application on a dial peer.

show call application voice

Displays information about voice applications.

## call application cache reload time

Effective with Cisco IOS Release 12.3(14)T, the call application cache reload time command is replaced by the cache reload time command in application configuration global mode. See the cache reload time command for more information.

To configure the router to reload the Media Gateway Control Protocol (MGCP) scripts from cache on a regular interval, use
                              the call application cache reload time command in global configuration mode. To set the value to the default, use the no form of this command.

call application cache reload time bg-minutes

no call application cache reload time

### Syntax Description

bg-minutes

Specifies the number of minutes after which the background process is awakened. This background process checks the time elapsed
                                          since the script was last used and whether the script is current:

If the script has not been used in the last "unload time," it unloads the script and quits. The unload time is not configurable.

If the script has been used, the background process loads the script from the URL. It compares the scripts, and if they do
                                                not match, it begins using the new script for new calls.

### Command Default

30 minutes

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco AS5300.

12.3(14)T

This command was replaced by the cache reload time command in application configuration global mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application cache reload 20 Warning: This command has been deprecated. Please use the following:
		cache reload time
```

The following example displays the call application cache reload time command configured to specify 30 minutes before a background process is awakened:

```
call application cache reload time 30
```

### Related Commands

Command

Description

cache reload time

Configures the router to reload scripts from cache on a regular interval.

call application voice load

Allows reload of an application that was loaded via the MGCP scripting package.

show call application voice

Displays all Tcl or MGCP scripts that are loaded.

## call application dump event-log

To flush the event log buffer for application instances to an external file, use the call application dump event-log command in privileged EXEC mode.

call application dump event-log

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

This command immediately writes the event log buffer to the external file whose location is defined with the call application event-log dump ftp command in global configuration mode.

The call application dump event-log command and the call application event-log dump ftp command are two different commands.

## Examples

The following example flushes the application event log buffer:

```
Router# call application dump event-log
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application event-log dump ftp

Enables the gateway to write the contents of the application event log buffer to an external file.

call application event-log max-buffer-size

Sets the maximum size of the event log buffer for each application instance.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application event-log

Effective with Cisco IOS Release 12.3(14)T, the call application event-log command is replaced by the event-log command in application configuration monitor mode. See the event-log command for more information.

To enable event logging for all voice application instances, use the call application event-log command in global configuration mode. To reset to the default, use the no form of this command.

call application event-log

no call application event-log

### Syntax Description

This command has no arguments or keywords.

### Command Default

Event logging for voice applications is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the event-log command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables event logging globally for all voice application instances. To enable or disable event logging for a
                              specific application, use the call application voice event-log command.

To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20%, the gateway automatically disables all event logging. It resumes event logging
                                          when free memory rises above 30%. While throttling is occurring, the gateway does not capture any new event logs even if event
                                          logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating faults.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application event-log Warning: This command has been deprecated. Please use the following:
             event-log
```

The following example enables event logging for all application instances:

```
call application event-log
```

### Related Commands

Command

Description

call application event-log error-only

Restricts event logging to error events only for application instances.

call application event-log max-buffer-size

Sets the maximum size of the event log buffer for each application instance.

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application stats

Enables statistics collection for voice applications.

call application voice event-log

Enables event logging for a specific voice application.

call leg event-log

Enables event logging for voice, fax, and modem call legs.

event-log

Enables event logging for applications.

monitor call application event-log

Displays the event log for an active application instance in real-time.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application event-log dump ftp

Effective with Cisco IOS Release 12.3(14)T, the call application event-log dump ftp command is replaced by the event-log dump ftp command in application configuration monitor mode. See the event-log dump ftp command for more information.

To enable the gateway to write the contents of the application event
                              		  log buffer to an external file, use the call application event-log dump ftp command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

call application event-log dump ftp server [ :port ] /file username username password [ [encryption-type] ] password

no call application event-log dump ftp

### Syntax Description

server

Name or IP address of FTP server where file is located.

: port

(Optional) Specific port number on server.

/ file

Name and path of file.

username

Username required to access file.

encryption-type

(Optional) The Cisco proprietary algorithm used to encrypt
                                          						the password. Values are 0 or 7. To disable encryption enter 0; to enable
                                          						encryption enter 7. If you specify 7, you must enter an encrypted password (a
                                          						password already encrypted by a Cisco router).

password

Password required to access file.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the event-log dump ftp command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables the gateway to automatically write the event log
                              		  buffer to the named file either after an active application instance terminates
                              		  or when the event log buffer becomes full. The default buffer size is 4 KB. To
                              		  modify the size of the buffer, use the call application event-log max-buffer-size command. To manually flush the
                              		  event log buffer, use the call application dump event-log command in privileged EXEC mode.

The call application dump event-log command and the call application event-log dump ftp command are two different commands.

Enabling the gateway to write event logs to FTP could adversely
                              		  impact gateway memory resources in some scenarios, for example, when:

The gateway is consuming
                                    			 high processor resources and FTP does not have enough processor resources to
                                    			 flush the logged buffers to the FTP server.

The designated FTP server
                                    			 is not powerful enough to perform FTP transfers quickly

Bandwidth on the link
                                    			 between the gateway and the FTP server is not large enough

The gateway is receiving
                                    			 a high volume of short-duration calls or calls that are failing

You should enable FTP dumping only when necessary and not enable it
                              		  in situations where it might adversely impact system performance.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning
                              		  message is displayed to direct users to the replacement command options:

```
Router(config)# call application event-log dump ftp Warning: This command has been deprecated. Please use the following:
		event-log dump ftp
```

The following example enables the gateway to write application event
                              		  logs to an external file named app_elogs.log on a server named ftp-server:

```
call application event-log dump ftp ftp-server/:elogs/app-elogs.log username myname password 0 mypass
```

The following example specifies that application event logs are
                              		  written to an external file named app_elogs.log on a server with the IP address
                              		  of 10.10.10.101:

```
call application event-log dump ftp 10.10.10.101/:elogs/app-elogs.log username myname password 0 mypass
```

### Related Commands

Command

Description

call application dump event-log

Flushes the event log buffer for application instances to
                                          						an external file.

call application event-log

Enables event logging for voice application instances.

call application event-log max-buffer-size

Sets the maximum size of the event log buffer for each
                                          						application instance.

event-log dump ftp

Enables the gateway to write the contents of the
                                          						application event log buffer to an external file.

show call application session-level

Displays event logs and statistics for voice application
                                          						instances.

## call application event-log error-only

Effective with Cisco IOS Release 12.3(14)T, the call application event-log error-only command is replaced by the event-log error-only command in application configuration monitor mode. See the event-log error-only command for more information.

To restrict event logging to error events only for application instances, use the call application event-log error-only command in global configuration mode. To reset to the default, use the no form of this command.

call application event-log error-only

no call application event-log error-only

### Syntax Description

This command has no arguments or keywords.

### Command Default

All application events are logged.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the event-log error-only command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command limits new event logging to error events only; it does not enable logging. You must use this command with either
                              the call application event-log command, which enables event logging for all voice applications, or with the call application voice event-log command, which enables event logging for a specific application. Any events logged before this command is issued are not
                              affected.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application event-log error-only Warning: This command has been deprecated. Please use the following:
		event-log error-only
```

The following example enables event logging for error events only:

```
call application event-log
call application event-log error-only
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application history session event-log save-exception-only

Saves in history only the event logs for application instances that have at least one error.

call application voice event-log

Enables event logging for a specific voice application.

event-log error-only

Restricts event logging to error events only for application instances.

show call application app-level

Displays application-level statistics for voice applications.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application event-log max-buffer-size

Effective with Cisco IOS Release 12.3(14)T, the call application event-log max-buffer-size command is replaced by the event-log max-buffer-size command in application configuration monitor mode. See the event-log max-buffer-size command for more information.

To set the maximum size of the event log buffer for each application instance, use the call application event-log max-buffer-size command in global configuration mode. To reset to the default, use the no form of this command.

call application event-log max-buffer-size kilobytes

no call application event-log max-buffer-size

### Syntax Description

kilobytes

Maximum buffer size, in kilobytes. Range is 1 to 50. Default is 4.

### Command Default

4 kilobytes

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the event-log max-buffer-size command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

If the event log buffer reaches the limit set by this command, the gateway allocates a second buffer of equal size. The contents
                              of both buffers is displayed when you use the show call application session-level command. When the first event log buffer becomes full, the gateway automatically appends its contents to an external FTP
                              location if the call application event-log dump ftp command is used.

A maximum of two buffers are allocated for an event log. If both buffers are filled, the first buffer is deleted and another
                              buffer is allocated for new events (buffer wraps around). If the call application event-log dump ftp command is configured and the second buffer becomes full before the first buffer is dumped, event messages are dropped and
                              are not recorded in the buffer.

Do not set the maximum buffer size to more than you need for a typical application session. After an active session terminates,
                              the amount of memory used by the buffer is allocated to the history table and is maintained for the length of time set by
                              the call application history session retain-timer command. Also consider that most fatal errors are captured at the end of an event log.

To conserve memory resources, write the event log buffer to FTP by using the call application event-log dump ftp command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application event-log max-buffer-size Warning: This command has been deprecated. Please use the following:
		event-log max-buffer-size
```

The following example sets the application event log buffer to 8 kilobytes:

```
call application event-log
call application event-log max-buffer-size 8
```

### Related Commands

Command

Description

call application dump event-log

Flushes the event log buffer for application instances to an external file.

call application event-log

Enables event logging for voice application instances.

call application event-log dump ftp

Enables the gateway to write the contents of the application event log buffer to an external file.

event-log max-buffer-size

Sets the maximum size of the event log buffer for each application instance.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application global

Effective with Cisco IOS Release 12.3(14)T, the call application global command is replaced by the global command in application configuration mode. See the global command for more information.

To configure an application to use for incoming calls whose incoming dial peer does not have an explicit application configured,
                              use the call application global command in global configuration mode. To remove the application, use the no form of this command.

call application global application-name

no call application global application-name

### Syntax Description

application-name

Character string that defines the name of the application.

### Command Default

The default application is default for all dial peers.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(15)ZJ

This command was introduced.

12.3(4)T

This command was integrated into Cisco IOS Release 12.3(4)T.

12.3(14)T

This command was replaced by the global command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

The application defined in the dial peer always takes precedence over the global application configured with the call application global command. The application configured with this command executes only when a dial peer has no application configured.

The application you configure with this command can be an application other than the default session application, but it
                              must be included with the Cisco IOS software or be loaded onto the gateway with the call application voice command before using this command. If the application does not exist in Cisco IOS software or has not been loaded onto the
                              gateway, this command will have no effect.

In Cisco IOS Release 12.3(4)T and later releases, the application-name default refers to the application that supports Open
                                          Settlement Protocol (OSP), call transfer, and call forwarding. The default session application in Cisco IOS Release 12.2(13)T
                                          and earlier releases has been renamed default.old.c and can still be configured for specific dial peers through the application command or globally configured for all inbound dial peers through the call application global command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application global Warning: This command has been deprecated. Please use the following:
		global
```

In the following example, the clid_authen_collect application is configured as the global application for all inbound dial
                              peers that do not have a specific application configured:

```
call application global clid_authen_collect
```

### Related Commands

Command

Description

application

Enables a specific IVR application on a dial peer.

call application voice

Defines the name to be used for an application and indicates the location of the appropriate IVR script to be used with this
                                          application.

global

Enters application configuration mode.

## call application history session event-log save-exception-only

Effective with Cisco IOS Release 12.3(14)T, the call application history session event-log save-exception-only command is replaced by the history session event-log save-exception-only command in application configuration monitor mode. See the history session event-log save-exception-only command for more information.

To save in history only the event logs for application sessions that have at least one error, use the call application history session event-log save-exception-only command in global configuration mode. To reset to the default, use the no form of this command.

call application history session event-log save-exception-only

no call application history session event-log save-exception-only

### Syntax Description

This command has no arguments or keywords.

### Command Default

All event logs for sessions are saved to history.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the history session event-log save-exception-only command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Application event logs move from active to history after an instance terminates. If you use this command, the voice gateway
                              saves event logs only for instances that had one or more errors. Event logs for normal instances that do not contain any errors
                              are not saved to history.

This command does not affect records saved to an FTP server by using the call application dump event-log command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application history session event-log save-exception-only Warning: This command has been deprecated. Please use the following:
		history session event-log save-exception-only
```

The following example saves an event log in history only if the instance had an error:

```
call application history session event-log save-exception-only
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application event-log error-only

Restricts event logging to error events only for application instances.

call application event-log max-buffer-size

Sets the maximum size of the event log buffer for each application instance.

call application history session max-records

Sets the maximum number of application instance records saved in history.

call application history session retain-timer

Sets the maximum number of minutes for which application instance records are saved in history.

history session event-log save-exception-only

Saves in history only the event logs for application sessions that have at least one error.

## call application history session max-records

Effective with Cisco IOS Release 12.3(14)T, the call application history session max-records command is replaced by the history session max-records command in application configuration monitor mode. See the history session max-records command for more information.

To set the maximum number of application instance records saved in history, use the call application history session max-records command in global configuration mode. To reset to the default, use the no form of this command.

call application history session max-records number

no call application history session max-records

### Syntax Description

number

Maximum number of records to save in history. Range is 0 to 2000. Default is 360.

### Command Default

360

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the history session max-records command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command affects the number of records that display when you use the show call application history session-level command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application history session max-records Warning: This command has been deprecated. Please use the following:
		history session max-records
```

The following example sets the maximum record limit to 500:

```
call application history session max-records 500
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application history session event-log save-exception-only

Saves in history only the event logs for application instances that have at least one error.

call application history session retain-timer

Sets the maximum number of minutes that application instance records are saved in history.

history session max-records

Sets the maximum number of application instance records saved in history.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application history session retain-timer

Effective with Cisco IOS Release 12.3(14)T, the call application history session retain-timer command is replaced by the history session retain-timer command in application configuration monitor mode. See the history session retain-timer command for more information.

To set the maximum number of minutes for which application instance records are saved in history, use the call application history session retain-timer command in global configuration mode. To reset to the default, use the no form of this command.

call application history session retain-timer minutes

no call application history session retain-timer

### Syntax Description

minutes

Maximum time, in minutes, for which history records are saved. Range is 0 to 4294,967,295. Default is 15.

### Command Default

15

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the history session retain-timer command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command affects the number of records that display when you use the show call application history session-level command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application history session retain-timer Warning: This command has been deprecated. Please use the following:
		history session retain-timer
```

The following example sets the maximum time to save history records to 1 hour:

```
call application history session retain-timer 60
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application history session event-log save-exception-only

Saves in history only the event logs for application instances that have at least one error.

call application history session max-records

Sets the maximum number of application instance records saved in history.

history session retain-timer

Sets the maximum number of minutes for which application instance records are saved in history.

show call application session-level

Displays event logs and statistics for voice application instances.

## call application interface dump event-log

To flush the event log buffer for application interfaces to an external file, use the call application interface dump event-log command in privileged EXEC mode.

call application interface dump event-log

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

This command immediately writes the event log buffer to the external file whose location is defined with the call application interface event-log dump ftp command in global configuration mode.

The call application interface dump event-log command and the call application interface event-log dump ftp command are two different commands.

## Examples

The following example writes the event log buffer to the external file named int_elogs:

```
Router(config)# call application interface event-log dump ftp ftp-server/int_elogs.log username myname password 0 mypass Router(config)# exit Router# call application interface dump event-log
```

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application interface event-log dump ftp

Enables the voice gateway to write the contents of the interface event log buffer to an external file.

call application interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each application interface.

show call application interface

Displays event logs and statistics for application interfaces.

## call application interface event-log

Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log command is replaced by the interface event-log command in application configuration monitor mode. See the interface event-log command for more information.

To enable event logging for interfaces that provide services to voice applications, use the call application interface event-log command in global configuration mode. To reset to the default, use the no form of this command.

call application interface event-log [ { aaa | asr | flash | http | ram | rtsp | smtp | tftp | tts } [ server server ] [ disable ]]

no call application interface event-log [ { aaa | asr | flash | http | ram | rtsp | smtp | tftp | tts } [ server server ] [ disable ]]

### Syntax Description

aaa

Authentication, authorization, and accounting (AAA) interface type.

asr

Automatic speech recognition (ASR) interface type.

flash

Flash memory of the Cisco gateway.

http

Hypertext Transfer Protocol (HTTP) interface type.

ram

Memory of the Cisco gateway.

rtsp

Real Time Streaming Protocol (RTSP) interface type.

smtp

Simple Mail Transfer Protocol (SMTP) interface type.

tftp

Trivial File Transfer Protocol (TFTP) interface type.

tts

Text-to-speech (TTS) interface type.

server server

(Optional) Server name or IP address.

disable

(Optional) Disables event logging for the specified interface type or server.

### Command Default

Event logging for application interfaces is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface event-log command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables event logging globally for all interface types and servers unless you select a specific interface type
                              or server. Specifying an interface type takes precedence over the global command for a specific interface type. Specifying
                              an individual server takes precedence over the interface type.

To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20%, the gateway automatically disables all event logging. It resumes event logging
                                          when free memory rises above 30%. While throttling is occurring, the gateway does not capture any new event logs even if event
                                          logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating faults.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application interface event-log Warning: This command has been deprecated. Please use the following:
		interface event-log
```

The following example enables event logging for all interfaces:

```
call application interface event-log
```

The following example enables event logging for HTTP interfaces only:

```
call application interface event-log http
```

The following example enables event logging for all interfaces except HTTP:

```
call application interface event-log
call application interface event-log http disable
```

The following example enables event logging for all HTTP servers except the server with the IP address of 10.10.1.1:

```
call application interface event-log http
call application interface event-log http server http://10.10.1.1 disable
```

### Related Commands

Command

Description

call application interface event-log dump ftp

Enables the gateway to write the contents of the interface event log buffer to an external file.

call application interface event-log error-only

Restricts event logging to error events only for application interfaces.

call application interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each application interface.

call application interface max-server-records

Sets the maximum number of application interface records that are saved.

call application interface stats

Enables statistics collection for application interfaces.

interface event-log

Enables event logging for interfaces providing services to voice applications.

show call application interface

Displays event logs and statistics for application interfaces.

## call application interface event-log dump ftp

Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log dump ftp command is replaced by the interface event-log dump ftp command in application configuration monitor
                                          		  mode. See the interface event-log dump ftp command for more information.

To enable the gateway to write the contents of the interface event
                              		  log buffer to an external file, use the call application interface event-log dump ftp command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

call application interface event-log dump ftp server [ :port ] /file username username password [ [encryption-type] ] password

no call application interface event-log dump ftp

### Syntax Description

server

Name or IP address of FTP server where the file is located.

: port

(Optional) Specific port number on server.

/ file

Name and path of file.

username username

Username required to access file.

encryption-type

(Optional) Cisco proprietary algorithm used to encrypt the
                                          						password. Values are 0 or 7. To disable encryption enter 0; to enable
                                          						encryption enter 7. If you specify 7, you must enter an encrypted password (a
                                          						password already encrypted by a Cisco router).

password password

Password required to access file.

### Command Default

Interface event log buffer is not written to an external file.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface event-log dump ftp command in application configuration
                                          						monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message.

### Usage Guidelines

This command enables the gateway to automatically write the interface
                              		  event log buffer to the named file when the buffer becomes full. The default
                              		  buffer size is 4 KB. To modify the size of the buffer, use the call application interface event-log max-buffer-size command. To manually flush the
                              		  event log buffer, use the call application interface dump event-log command in privileged EXEC mode.

The call application interface dump event-log command and the call application interface event-log dump ftp command are two different commands.

- The gateway is
                                          				  consuming high processor resources and FTP does not have enough processor
                                          				  resources to flush the logged buffers to the FTP server.

- The designated FTP
                                          				  server is not powerful enough to perform FTP transfers quickly

- Bandwidth on the link
                                          				  between the gateway and the FTP server is not large enough

- The gateway is
                                          				  receiving a high volume of short-duration calls or calls that are failing

You should enable FTP dumping only when necessary and not enable it
                              		  in situations where it might adversely impact system performance.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning
                              		  message is displayed to direct users to the replacement command options:

```
Router(config)# call application interface event-log dump ftp Warning: This command has been deprecated. Please use the following:
		interface event-log dump ftp
```

The following example specifies that interface event log are written
                              		  to an external file named int_elogs.log on a server named ftp-server:

```
call application interface event-log dump ftp ftp-server/elogs/int_elogs.log username myname password 0 mypass
```

The following example specifies that application event logs are
                              		  written to an external file named int_elogs.log on a server with the IP address
                              		  of 10.10.10.101:

```
call application interface event-log dump ftp 10.10.10.101/elogs/int_elogs.log username myname password 0 mypass
```

### Related Commands

Command

Description

call application interface dump event-log

Flushes the event log buffer for application interfaces to
                                          						an external file.

call application interface event-log

Enables event logging for external interfaces used by voice
                                          						applications.

call application interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each
                                          						application interface.

call application interface max-server-records

Sets the maximum number of application interface records
                                          						that are saved.

interface event-log dump ftp

Enables the gateway to write the contents of the interface
                                          						event log buffer to an external file.

show call application interface

Displays event logs and statistics for application
                                          						interfaces.

## call application interface event-log error-only

Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log error-only command is replaced by the interface event-log error only command in application configuration monitor mode. See the interface event-log error only command for more information.

To restrict event logging to error events only for application interfaces, use the call application interface event-log error-only command in global configuration mode. To reset to the default, use the no form of this command.

call application interface event-log error-only

no call application interface event-log error-only

### Syntax Description

This command has no arguments or keywords.

### Command Default

All events are logged.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface event-log error only command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command limits the severity level of the events that are logged; it does not enable logging. You must use this command
                              with the call application interface event-log command, which enables event logging for all application interfaces.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application interface event-log error-only Warning: This command has been deprecated. Please use the following:
             interface event-log error only
```

The following example enables event logging for error events only:

```
call application interface event-log error-only
```

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each application interface.

call application interface max-server-records

Sets the maximum number of application interface records that are saved.

interface event-log error-only

Restricts event logging to error events only for application interfaces.

show call application interface

Displays event logs and statistics for application interfaces.

## call application interface event-log max-buffer-size

Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log max-buffer-size command is replaced by the interface event-log max-buffer-size command in application configuration monitor mode. See the interface event-log max-buffer-size command for more information.

To set the maximum size of the event log buffer for each application interface, use the call application interface event-log max-buffer-size command in global configuration mode. To reset to the default, use the no form of this command.

call application interface event-log max-buffer-size kilobytes

no call application interface event-log max-buffer-size

### Syntax Description

kilobytes

Maximum buffer size, in kilobytes. Range is 1 to 10. Default is 4.

### Command Default

4 kilobytes

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface event-log max-buffer-size command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

If the event log buffer reaches the limit set by this command, the gateway allocates a second buffer of equal size. The contents
                              of both buffers is displayed when you use the show call application interface command. When the first event log buffer becomes full, the gateway automatically appends its contents to an external FTP
                              location if the call application interface event-log dump ftp command is used.

A maximum of two buffers are allocated for an event log. If both buffers are filled, the first buffer is deleted and another
                              buffer is allocated for new events (buffer wraps around). If the call application interface event-log dump ftp command is configured and the second buffer becomes full before the first buffer is dumped, event messages are dropped and
                              are not recorded in the buffer.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application interface event-log max-buffer-size Warning: This command has been deprecated. Please use the following:
			interface event-log max-buffer-size
```

The following example sets the maximum buffer size to 8 kilobytes:

```
call application interface event-log max-buffer-size 8
```

### Related Commands

Command

Description

call application interface dump event-log

Flushes the event log buffer for application interfaces to an external file.

call application interface event-log dump ftp

Enables the gateway to write the contents of the interface event log buffer to an external file.

call application interface max-server-records

Sets the maximum number of application interface records that are saved.

interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each application interface.

show call application interface

Displays event logs and statistics for application interfaces.

## call application interface max-server-records

Effective with Cisco IOS Release 12.3(14)T, the call application interface max-server-records command is replaced by the interface max-server-records command in application configuration monitor mode. See the interface max-server-records command for more information.

To set the maximum number of application interface records that are saved, use the call application interface max-server-records command in global configuration mode. To reset to the default, use the no form of this command.

call application interface max-server-records number

no call application interface max-server-records

### Syntax Description

number

Maximum number of records to save. Range is 1 to 100. Default is 10.

### Command Default

10

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface max-server-records command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

Only the specified number of records from the most recently accessed servers are kept.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application interface max-server-records Warning: This command has been deprecated. Please use the following:
             interface max-server-records
```

The following example sets the maximum saved records to 50:

```
call application interface max-server-records 50
```

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application interface event-log max-buffer-size

Sets the maximum size of the event log buffer for each application interface.

interface max-server-records

Sets the maximum number of application interface records that are saved.

show call application interface

Displays event logs and statistics for application interfaces.

## call application interface stats

Effective with Cisco IOS Release 12.3(14)T, the call application interface stats command is replaced by the interface stats command in application configuration monitor mode. See the interface stats command for more information.

To enable statistics collection for application interfaces, use the call application interface stats command in global configuration mode. To reset to the default, use the no form of this command.

call application interface stats

no call application interface stats

### Syntax Description

This command has no arguments or keywords.

### Command Default

Statistics collection is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the interface stats command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

To display the interface statistics enabled by this command, use the show call application interface command. To reset the interface counters to zero, use the clear call application interface command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application interface stats Warning: This command has been deprecated. Please use the following:
		interface stats
```

The following example enables statistics collection for application interfaces:

```
call application interface stats
```

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

clear call application interface

Clears application interface statistics or event logs.

interface stats

Enables statistics collection for application interfaces.

show call application interface

Displays event logs and statistics for application interfaces.

stats

Enables statistics collection for voice applications.

## call application session start (global)

Effective with Cisco IOS Release 12.3(14)T, the call application session start (global) command is replaced by the the session start command in application configuration mode. See the session start command for more information.

To start a new instance (session) of a Tcl IVR 2.0 application, use the call application session start command in global configuration mode. To stop the session and remove the configuration, use the no form of this command.

call application session start instance-name application-name

no call application session start instance-name

### Syntax Description

instance-name

Alphanumeric label that uniquely identifies this application instance.

application-name

Name of the Tcl application. This is the name of the application that was assigned with the call application voice command.

### Command Default

This command has no default behavior or values.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

12.3(14)T

The call application session start (global configuration) command was replaced by the session start command in application configuration mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

This command starts a new session, or instance, of a Tcl IVR 2.0 application. It cannot start a session for a VoiceXML application
                              because Cisco IOS software cannot start a VoiceXML application without an active call leg.

You can start an application instance only after the Tcl application is loaded onto the gateway with the call application voice command.

If this command is used, the session restarts if the gateway reboots.

The no call application session start command stops the Tcl session and removes the configuration from the gateway. You can stop an application session without
                              removing the configuration by using the call application session stop command.

VoiceXML sessions cannot be stopped with the no call application session start command because VoiceXML sessions cannot be started with Cisco IOS commands.

If the application session stops running, it does not restart unless the gateway reboots. A Tcl script might intentionally
                              stop running by executing a "call close" command for example, or it might fail because of a script error.

You can start multiple instances of the same application by using different instance names.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application session start Warning: This command has been deprecated. Please use the following:
		session start
```

The following example starts a session named my_instance for the application named demo:

```
call application session start my_instance demo
```

The following example starts another session for the application named demo:

```
call application session start my_instance2 demo
```

### Related Commands

Command

Description

call application session start (privileged EXEC)

Starts a new instance (session) of a Tcl application from privileged EXEC mode.

call application session stop

Stops a voice application session that is running.

debug voip ivr

Displays debug messages for VoIP IVR interactions.

session start

Starts a new instance (session) of a Tcl IVR 2.0 application.

show call application services registry

Displays a one-line summary of all registered services.

show call application sessions

Displays summary or detailed information about voice application sessions.

## call application session start (privileged EXEC)

To start a new instance (session) of a Tcl IVR 2.0 application, use the call application session start command in privileged EXEC mode.

call application session start instance-name [application-name]

### Syntax Description

instance-name

Alphanumeric label that uniquely identifies this application instance.

application-name

(Optional) Name of the Tcl application. This is the name of the application that was assigned with the call application voice command.

This argument is optional if the application instance was previously started and stopped.

### Command Default

None

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command starts a new session, or instance, of a Tcl IVR 2.0 application. It cannot start a session for a VoiceXML application
                              because Cisco IOS software cannot start a VoiceXML application without an active call leg.

You can start an application instance only after the Tcl application is loaded onto the gateway with the call application voice command.

Using this command does not restart the session if the gateway reboots. To automatically restart the session if the gateway
                              reboots, use the call application session start command in global configuration mode.

To stop an application session once it starts running, use the call application session stop command.

If the application session stops running, it does not restart unless the gateway reboots and the call application session start command is used in global configuration mode. A Tcl script might intentionally stop running by executing a "call close" command
                              for example, or it might fail due to a script error.

You can start multiple instances of the same application by using different instance names.

## Examples

The following example restarts an application session called my_instance:

```
call application session start my_instance
```

### Related Commands

Command

Description

call application session start (global configuration)

Starts a new instance (session) of a Tcl application in global configuration mode.

call application session stop

Stops a voice application session that is running.

show call application services registry

Displays a one-line summary of all registered services.

show call application sessions

Displays summary or detailed information about voice application sessions.

## call application session stop

To stop a voice application session that is running, use the call application session stop command in privileged EXEC mode.

call application session stop { callid call-id | handle handle | id session-id | name instance-name }

### Syntax Description

callid call-id

Call-leg ID that can be displayed in the output from the debug voip ivr script command if the Tcl script uses puts commands.

handle handle

Handle of a session from the Tcl mod_handle infotag.

id session-id

Session ID that can be displayed with the show call application sessions command.

name instance-name

Instance name that was configured with the call application session start command.

### Command Default

None

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

This command stops a Tcl IVR 2.0 or VoiceXML application session that is identified by one of four different methods: call
                              ID, handle, session ID, or instance name. To see a list of currently running applications, use the show call application sessions command.

A Tcl session that is stopped with this command receives a session terminate event. The session is expected to close all call
                              legs and stop. If a session does not close itself after a 10-second timer, it is forcibly stopped and all call legs that it
                              controls disconnect.

Using this command to stop a VoiceXML session immediately stops the document interpretation and disconnects the call leg.
                              No VoiceXML events are thrown.

If you stop a Tcl session that is configured to start with the call application session start command in global configuration mode, you must remove the session by using the no call application session start command before you can restart it.

To see a list of stopped sessions, use the show call application sessions command. Only stopped sessions that are configured to start with the call application session start command in global configuration mode are displayed. If a session was started with the call application session start command in privileged EXEC mode, it is not tracked by the system and it is not shown as stopped in the output of the show call application sessions command.

## Examples

The following example stops an application session called my_instance:

```
call application session stop name my_instance
```

### Related Commands

Command

Description

call application session start (global configuration)

Starts a new instance (session) of a Tcl application from global configuration mode.

show call application services registry

Displays a one-line summary of all registered services.

show call application sessions

Displays summary or detailed information about voice application sessions.

## call application stats

Effective with Cisco IOS Release 12.3(14)T, the call application stats command is replaced by the stats command in application configuration monitor mode. See the stats command for more information.

To enable statistics collection for voice applications, use the call application stats command in global configuration mode. To reset to the default, use the no form of this command.

call application stats

no call application stats

### Syntax Description

This command has no arguments or keywords.

### Command Default

Statistics collection is disabled.

### Command Modes

Global configuration (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.3(14)T

This command was replaced by the stats command in application configuration monitor mode.

12.4(24)T

This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message.

### Usage Guidelines

To display the application statistics, use the show call application session-level , show call application app-level , or show call application gateway-level command. To reset the application counters in history to zero, use the clear call application stats command.

## Examples

Effective with Cisco IOS Release 12.4(24)T, the following warning message is displayed to direct users to the replacement
                              command options:

```
Router(config)# call application stats 
        Warning: This command has been deprecated. Please use the following:
             stats
```

The following example enables statistics collection for voice applications:

```
call application stats
```

### Related Commands

Command

Description

call application event-log

Enables event logging for voice application instances.

call application interface stats

Enables statistics collection for application interfaces.

clear call application stats

Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics.

show call application app-level

Displays application-level statistics for voice applications.

show call application gateway-level

Displays gateway-level statistics for voice application instances.

show call application session-level

Displays event logs and statistics for voice application instances.

stats

Enables statistics collection for voice applications.

| Release | Modification |
|---|---|
| 15.1(1)T | This command was introduced. |
| 15.2(4)M | This command was modified. Cable polling was extended to analog Foreign Exchange Office End Ground Start (FXOGS), Foreign
                                          Exchange Office End Loop Start (FXOLS), Foreign Exchange Station End Ground Start (FXSGS), and Foreign Exchange Station End
                                          Loop Start (FXSLS) voice ports. |

| Command | Description |
|---|---|
| shutdown | Changes the state of the voice ports for a specific voice interface card to offline. |

| timer-value | Cable polling timer value in minutes. The range is from 0 to 1440. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| cable-detect | Enables cable polling on analog FXOGS, FXOLS, FXSGS, and FXSLS voice ports. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300 universal access server, Cisco AS5350,
                                          Cisco AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| id | Configures the local ID of the neighboring BE. |
| port | Configures the neighbor’s port number that is used for exchanging Annex G messages. |
| query-interval | Configures the interval at which the local BE queries the neighboring BE. |

| bg - minutes | Number of minutes after which the background process is awakened. This background process checks the time elapsed since the
                                          script was last used and whether the script is current: If the script has not been used in the last "unload time," it unloads the script and quits. The unload time is not configurable. If the script has been used, the background process loads the script from the URL. It compares the scripts, and if they do
                                                not match, it begins using the new script for new calls. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(14)T | The call application cache reload time command was moved to global application configuration mode and changed to cache reload time . |

| Command | Description |
|---|---|
| call application cache reload time | Configures the router to reload the MGCP scripts from cache on a regular interval. |
| show call application voice | Displays all Tcl or MGCP scripts that are loaded. |

| cycle-1-on-time | Tone-on duration for the first cycle of the cadence pattern, in milliseconds (ms). Range is from 0 to 1000. The default is
                                          0. |
|---|---|
| cycle-1-off-time | Tone-off duration for the first cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default is 0. |
| cycle-2-on-time | (Optional) Tone-on duration for the second cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| cycle-2-off-time | (Optional) Tone-off duration for the second cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| cycle-3-on-time | (Optional) Tone-on duration for the third cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| cycle-3-off-time | (Optional) Tone-off duration for the third cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| cycle-4-on-time | (Optional) Tone-on duration for the fourth cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| cycle-4-off-time | (Optional) Tone-off duration for the fourth cycle of the cadence pattern, in milliseconds. Range is from 0 to 1000. The default
                                          is 0. |
| continuous | Continuous call-progress tone is detected. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810. |
| 12.2(2)T | This command was implemented on the Cisco 1750 and integrated into Cisco IOS Release 12.2(2)T. |

| Command | Description |
|---|---|
| supervisory custom-cptone | Associates a class of custom call-progress tones with a voice port. |
| voice class custom-cptone | Creates a voice class for defining custom call-progress tones. |
| voice class dualtone-detect-params | Modifies the boundaries and limits for custom call-progress tones defined by the voice class custom-cptone command. |

| cadence-id | A tag to identify this cadence list. The range is from 1 to 10. |
|---|---|
| cycle-1-on-time | The tone duration for the first cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds). The
                                          default is 0. |
| cycle-1-off-time | The silence duration for the first cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0. |
| cycle-2-on-time | (Optional) The tone duration for the second cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0. |
| cycle-2-off-time | (Optional) The silence duration for the second cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0. |
| cycle-3-on-time | (Optional) The tone duration for the third cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0. |
| cycle-3-off-time | (Optional) The silence duration for the third cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0. |
| cycle-4-on-time | (Optional) The tone duration for the fourth cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100 seconds).
                                          The default is 0. |
| cycle-4-off-time | (Optional) The silence duration for the fourth cycle of the cadence pattern. Range is from 0 to 1000 (0 milliseconds to 100
                                          seconds). The default is 0. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, the Cisco MC3810. |

| Command | Description |
|---|---|
| cadence-max-off-time | Specifies the maximum off duration for detection of a tone. |
| cadence-min-on-time | Specifies the minimum on duration for detection of a tone. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| time | The maximum off time of a tone that can be detected, in
                                          						10-millisecond increments. Range is from 0 to 5000 (0 milliseconds to 50
                                          						seconds). The default is 0. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco
                                          						3600 series and the Cisco MC3810. |

| Command | Description |
|---|---|
| cadence-min-on-time | Specifies the minimum on duration for detection of a tone. |
| cadence-variation | Specifies the cadence variation time allowed for detection
                                          						of a tone. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| time | The minimum on time of a tone that can be detected, in 10-millisecond increments. Range is from 0 to 100 (0 milliseconds to 1 seconds). The
                                          default is 0. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series and the Cisco MC3810. |

| Command | Description |
|---|---|
| cadence-max-off-time | Specifies the maximum off duration for detection of a tone. |
| cadence-variation | Specifies the cadence variation time allowed for detection of a tone. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| time | The maximum time by which the tone onset can vary from the specified onset time and still be detected, in 10-millisecond
                                          increments. Range is from 0 to 200 (0 milliseconds to 2 seconds). The default is 10. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810. |
| 12.1(5)XM | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750 router. |

| Command | Description |
|---|---|
| cadence-max-off-time | Specifies the maximum off duration for detection of a tone. |
| cadence-min-on-time | Specifies the minimum on duration for detection of a tone. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port. |

| acctTempName | Template name. |
|---|---|
| url | Location of the template. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850. |
| 12.3(14)T | This command was added to the application configuration mode to replace the call application voice accounting-template command. |

| Command | Description |
|---|---|
| call application voice accounting-template | Configures T.37 fax accounting with VoIP AAA nonblocking API. |
| show call accounting-template voice | Selects an accounting template at a specific location. |

| acctTempName | Template name. |
|---|---|
| url | Location of the template. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850. |
| 12.3(14)T | The call accounting-template voice command is replaced by the call accounting-template command in application configuration mode. See the call accounting-template command for more information. |

| Command | Description |
|---|---|
| call accounting-template voice reload | Reloads the accounting template. |
| show call accounting-template voice | Selects an accounting template at a specific location. |

| reload | Reloads the accounting template from the address (for example, a tftp address) where the template is stored. |
|---|---|
| acctTempName | Name of the accounting template. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the following platforms: Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800,
                                          and Cisco AS5850. |

| Command | Description |
|---|---|
| call accounting-template voice | Selects an accounting template at a specific location |
| gw-accounting aaa | Defines and loads the template file at the location defined by the URL. |
| show call accounting-template voice | Displays the VSAs that are contained in the accounting template. |

| dns-name | Fully qualified domain name (including host portion) for the call agent. For example, "ca123.example.net". |
|---|---|
| ip-address | IP address of the call agent. |
| port | (Optional) User Datagram Protocol (UDP) port number over which the gateway sends messages to the call agent. Range is from
                                          1025 to 65535. The default call-agent UDP port is 2727 for MGCP 1.0, Network-based Call Signaling (NCS) 1.0, and Trunking Gateway Control
                                                Protocol (TGCP) 1.0. The default call-agent UDP port is 2427 for MGCP 0.1 and Simple Gateway Control Protocol (SGCP). |
| service-type type | (Optional) Protocol service type valid values for the type argument are mgcp , ncs , sgcp , and tgcp . The default service type is mgcp . |
| version protocol-version | (Optional) Version number of the protocol. Valid values follow: Service-type MGCP-- 0.1 , 1.0 Service-type NCS-- 1.0 Service-type SGCP-- 1.1 , 1.5 Service-type TGCP-- 1.0 The default service type and version are mgcp and 0.1 . |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| max1 lookup | Enables DNS lookup of the MGCP call agent address when the suspicion threshold value is reached. |
| max2 lookup | Enables DNS lookup of the MGCP call agent address when the disconnect threshold value is reached. |
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp call-agent | Configures the address of the call agent (media gateway controller). |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application alternate command is replaced by the service command in global application configuration mode. See the service command for more information. |
|---|---|

| application-name | (Optional) Name of the specific voice application to use if the application in the dial peer fails. If a specific application
                                          name is not entered, the gateway uses the DEFAULT application. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the service command in global application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| application | Enables a voice application on a dial peer. |
| call application voice | Defines the name of a voice application and specifies the location of the Tcl or VoiceXML document to load for this application. |
| service | Loads and configures a specific, standalone application on a dial peer. |
| show call application voice | Displays information about voice applications. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application cache reload time command is replaced by the cache reload time command in application configuration global mode. See the cache reload time command for more information. |
|---|---|

| bg-minutes | Specifies the number of minutes after which the background process is awakened. This background process checks the time elapsed
                                          since the script was last used and whether the script is current: If the script has not been used in the last "unload time," it unloads the script and quits. The unload time is not configurable. If the script has been used, the background process loads the script from the URL. It compares the scripts, and if they do
                                                not match, it begins using the new script for new calls. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco AS5300. |
| 12.3(14)T | This command was replaced by the cache reload time command in application configuration global mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| cache reload time | Configures the router to reload scripts from cache on a regular interval. |
| call application voice load | Allows reload of an application that was loaded via the MGCP scripting package. |
| show call application voice | Displays all Tcl or MGCP scripts that are loaded. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | The call application dump event-log command and the call application event-log dump ftp command are two different commands. |
|---|---|

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application event-log dump ftp | Enables the gateway to write the contents of the application event log buffer to an external file. |
| call application event-log max-buffer-size | Sets the maximum size of the event log buffer for each application instance. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application event-log command is replaced by the event-log command in application configuration monitor mode. See the event-log command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the event-log command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20%, the gateway automatically disables all event logging. It resumes event logging
                                          when free memory rises above 30%. While throttling is occurring, the gateway does not capture any new event logs even if event
                                          logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating faults. |
|---|---|

| Command | Description |
|---|---|
| call application event-log error-only | Restricts event logging to error events only for application instances. |
| call application event-log max-buffer-size | Sets the maximum size of the event log buffer for each application instance. |
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application stats | Enables statistics collection for voice applications. |
| call application voice event-log | Enables event logging for a specific voice application. |
| call leg event-log | Enables event logging for voice, fax, and modem call legs. |
| event-log | Enables event logging for applications. |
| monitor call application event-log | Displays the event log for an active application instance in real-time. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application event-log dump ftp command is replaced by the event-log dump ftp command in application configuration monitor mode. See the event-log dump ftp command for more information. |
|---|---|

| server | Name or IP address of FTP server where file is located. |
|---|---|
| : port | (Optional) Specific port number on server. |
| / file | Name and path of file. |
| username | Username required to access file. |
| encryption-type | (Optional) The Cisco proprietary algorithm used to encrypt
                                          						the password. Values are 0 or 7. To disable encryption enter 0; to enable
                                          						encryption enter 7. If you specify 7, you must enter an encrypted password (a
                                          						password already encrypted by a Cisco router). |
| password | Password required to access file. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the event-log dump ftp command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message. |

| Note | The call application dump event-log command and the call application event-log dump ftp command are two different commands. |
|---|---|

| Command | Description |
|---|---|
| call application dump event-log | Flushes the event log buffer for application instances to
                                          						an external file. |
| call application event-log | Enables event logging for voice application instances. |
| call application event-log max-buffer-size | Sets the maximum size of the event log buffer for each
                                          						application instance. |
| event-log dump ftp | Enables the gateway to write the contents of the
                                          						application event log buffer to an external file. |
| show call application session-level | Displays event logs and statistics for voice application
                                          						instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application event-log error-only command is replaced by the event-log error-only command in application configuration monitor mode. See the event-log error-only command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the event-log error-only command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application history session event-log save-exception-only | Saves in history only the event logs for application instances that have at least one error. |
| call application voice event-log | Enables event logging for a specific voice application. |
| event-log error-only | Restricts event logging to error events only for application instances. |
| show call application app-level | Displays application-level statistics for voice applications. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application event-log max-buffer-size command is replaced by the event-log max-buffer-size command in application configuration monitor mode. See the event-log max-buffer-size command for more information. |
|---|---|

| kilobytes | Maximum buffer size, in kilobytes. Range is 1 to 50. Default is 4. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the event-log max-buffer-size command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application dump event-log | Flushes the event log buffer for application instances to an external file. |
| call application event-log | Enables event logging for voice application instances. |
| call application event-log dump ftp | Enables the gateway to write the contents of the application event log buffer to an external file. |
| event-log max-buffer-size | Sets the maximum size of the event log buffer for each application instance. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application global command is replaced by the global command in application configuration mode. See the global command for more information. |
|---|---|

| application-name | Character string that defines the name of the application. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(14)T | This command was replaced by the global command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | In Cisco IOS Release 12.3(4)T and later releases, the application-name default refers to the application that supports Open
                                          Settlement Protocol (OSP), call transfer, and call forwarding. The default session application in Cisco IOS Release 12.2(13)T
                                          and earlier releases has been renamed default.old.c and can still be configured for specific dial peers through the application command or globally configured for all inbound dial peers through the call application global command. |
|---|---|

| Command | Description |
|---|---|
| application | Enables a specific IVR application on a dial peer. |
| call application voice | Defines the name to be used for an application and indicates the location of the appropriate IVR script to be used with this
                                          application. |
| global | Enters application configuration mode. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application history session event-log save-exception-only command is replaced by the history session event-log save-exception-only command in application configuration monitor mode. See the history session event-log save-exception-only command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the history session event-log save-exception-only command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | This command does not affect records saved to an FTP server by using the call application dump event-log command. |
|---|---|

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application event-log error-only | Restricts event logging to error events only for application instances. |
| call application event-log max-buffer-size | Sets the maximum size of the event log buffer for each application instance. |
| call application history session max-records | Sets the maximum number of application instance records saved in history. |
| call application history session retain-timer | Sets the maximum number of minutes for which application instance records are saved in history. |
| history session event-log save-exception-only | Saves in history only the event logs for application sessions that have at least one error. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application history session max-records command is replaced by the history session max-records command in application configuration monitor mode. See the history session max-records command for more information. |
|---|---|

| number | Maximum number of records to save in history. Range is 0 to 2000. Default is 360. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the history session max-records command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application history session event-log save-exception-only | Saves in history only the event logs for application instances that have at least one error. |
| call application history session retain-timer | Sets the maximum number of minutes that application instance records are saved in history. |
| history session max-records | Sets the maximum number of application instance records saved in history. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application history session retain-timer command is replaced by the history session retain-timer command in application configuration monitor mode. See the history session retain-timer command for more information. |
|---|---|

| minutes | Maximum time, in minutes, for which history records are saved. Range is 0 to 4294,967,295. Default is 15. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the history session retain-timer command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application history session event-log save-exception-only | Saves in history only the event logs for application instances that have at least one error. |
| call application history session max-records | Sets the maximum number of application instance records saved in history. |
| history session retain-timer | Sets the maximum number of minutes for which application instance records are saved in history. |
| show call application session-level | Displays event logs and statistics for voice application instances. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | The call application interface dump event-log command and the call application interface event-log dump ftp command are two different commands. |
|---|---|

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application interface event-log dump ftp | Enables the voice gateway to write the contents of the interface event log buffer to an external file. |
| call application interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each application interface. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log command is replaced by the interface event-log command in application configuration monitor mode. See the interface event-log command for more information. |
|---|---|

| aaa | Authentication, authorization, and accounting (AAA) interface type. |
|---|---|
| asr | Automatic speech recognition (ASR) interface type. |
| flash | Flash memory of the Cisco gateway. |
| http | Hypertext Transfer Protocol (HTTP) interface type. |
| ram | Memory of the Cisco gateway. |
| rtsp | Real Time Streaming Protocol (RTSP) interface type. |
| smtp | Simple Mail Transfer Protocol (SMTP) interface type. |
| tftp | Trivial File Transfer Protocol (TFTP) interface type. |
| tts | Text-to-speech (TTS) interface type. |
| server server | (Optional) Server name or IP address. |
| disable | (Optional) Disables event logging for the specified interface type or server. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface event-log command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Note | To prevent event logging from adversely impacting system resources for production traffic, the gateway uses a throttling mechanism.
                                          When free processor memory drops below 20%, the gateway automatically disables all event logging. It resumes event logging
                                          when free memory rises above 30%. While throttling is occurring, the gateway does not capture any new event logs even if event
                                          logging is enabled. You should monitor free memory and enable event logging only when necessary for isolating faults. |
|---|---|

| Command | Description |
|---|---|
| call application interface event-log dump ftp | Enables the gateway to write the contents of the interface event log buffer to an external file. |
| call application interface event-log error-only | Restricts event logging to error events only for application interfaces. |
| call application interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each application interface. |
| call application interface max-server-records | Sets the maximum number of application interface records that are saved. |
| call application interface stats | Enables statistics collection for application interfaces. |
| interface event-log | Enables event logging for interfaces providing services to voice applications. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log dump ftp command is replaced by the interface event-log dump ftp command in application configuration monitor
                                          		  mode. See the interface event-log dump ftp command for more information. |
|---|---|

| server | Name or IP address of FTP server where the file is located. |
|---|---|
| : port | (Optional) Specific port number on server. |
| / file | Name and path of file. |
| username username | Username required to access file. |
| encryption-type | (Optional) Cisco proprietary algorithm used to encrypt the
                                          						password. Values are 0 or 7. To disable encryption enter 0; to enable
                                          						encryption enter 7. If you specify 7, you must enter an encrypted password (a
                                          						password already encrypted by a Cisco router). |
| password password | Password required to access file. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface event-log dump ftp command in application configuration
                                          						monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the
                                          						new CLI is replaced with an explicit error message. |

| Note | The call application interface dump event-log command and the call application interface event-log dump ftp command are two different commands. |
|---|---|

| Command | Description |
|---|---|
| call application interface dump event-log | Flushes the event log buffer for application interfaces to
                                          						an external file. |
| call application interface event-log | Enables event logging for external interfaces used by voice
                                          						applications. |
| call application interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each
                                          						application interface. |
| call application interface max-server-records | Sets the maximum number of application interface records
                                          						that are saved. |
| interface event-log dump ftp | Enables the gateway to write the contents of the interface
                                          						event log buffer to an external file. |
| show call application interface | Displays event logs and statistics for application
                                          						interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log error-only command is replaced by the interface event-log error only command in application configuration monitor mode. See the interface event-log error only command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface event-log error only command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each application interface. |
| call application interface max-server-records | Sets the maximum number of application interface records that are saved. |
| interface event-log error-only | Restricts event logging to error events only for application interfaces. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface event-log max-buffer-size command is replaced by the interface event-log max-buffer-size command in application configuration monitor mode. See the interface event-log max-buffer-size command for more information. |
|---|---|

| kilobytes | Maximum buffer size, in kilobytes. Range is 1 to 10. Default is 4. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface event-log max-buffer-size command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application interface dump event-log | Flushes the event log buffer for application interfaces to an external file. |
| call application interface event-log dump ftp | Enables the gateway to write the contents of the interface event log buffer to an external file. |
| call application interface max-server-records | Sets the maximum number of application interface records that are saved. |
| interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each application interface. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface max-server-records command is replaced by the interface max-server-records command in application configuration monitor mode. See the interface max-server-records command for more information. |
|---|---|

| number | Maximum number of records to save. Range is 1 to 100. Default is 10. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface max-server-records command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application interface event-log max-buffer-size | Sets the maximum size of the event log buffer for each application interface. |
| interface max-server-records | Sets the maximum number of application interface records that are saved. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application interface stats command is replaced by the interface stats command in application configuration monitor mode. See the interface stats command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the interface stats command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| clear call application interface | Clears application interface statistics or event logs. |
| interface stats | Enables statistics collection for application interfaces. |
| show call application interface | Displays event logs and statistics for application interfaces. |
| stats | Enables statistics collection for voice applications. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application session start (global) command is replaced by the the session start command in application configuration mode. See the session start command for more information. |
|---|---|

| instance-name | Alphanumeric label that uniquely identifies this application instance. |
|---|---|
| application-name | Name of the Tcl application. This is the name of the application that was assigned with the call application voice command. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| 12.3(14)T | The call application session start (global configuration) command was replaced by the session start command in application configuration mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application session start (privileged EXEC) | Starts a new instance (session) of a Tcl application from privileged EXEC mode. |
| call application session stop | Stops a voice application session that is running. |
| debug voip ivr | Displays debug messages for VoIP IVR interactions. |
| session start | Starts a new instance (session) of a Tcl IVR 2.0 application. |
| show call application services registry | Displays a one-line summary of all registered services. |
| show call application sessions | Displays summary or detailed information about voice application sessions. |

| instance-name | Alphanumeric label that uniquely identifies this application instance. |
|---|---|
| application-name | (Optional) Name of the Tcl application. This is the name of the application that was assigned with the call application voice command. Note This argument is optional if the application instance was previously started and stopped. | Note | This argument is optional if the application instance was previously started and stopped. |
| Note | This argument is optional if the application instance was previously started and stopped. |

| Note | This argument is optional if the application instance was previously started and stopped. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call application session start (global configuration) | Starts a new instance (session) of a Tcl application in global configuration mode. |
| call application session stop | Stops a voice application session that is running. |
| show call application services registry | Displays a one-line summary of all registered services. |
| show call application sessions | Displays summary or detailed information about voice application sessions. |

| callid call-id | Call-leg ID that can be displayed in the output from the debug voip ivr script command if the Tcl script uses puts commands. |
|---|---|
| handle handle | Handle of a session from the Tcl mod_handle infotag. |
| id session-id | Session ID that can be displayed with the show call application sessions command. |
| name instance-name | Instance name that was configured with the call application session start command. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call application session start (global configuration) | Starts a new instance (session) of a Tcl application from global configuration mode. |
| show call application services registry | Displays a one-line summary of all registered services. |
| show call application sessions | Displays summary or detailed information about voice application sessions. |

| Note | Effective with Cisco IOS Release 12.3(14)T, the call application stats command is replaced by the stats command in application configuration monitor mode. See the stats command for more information. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.3(14)T | This command was replaced by the stats command in application configuration monitor mode. |
| 12.4(24)T | This command was modified. The automatic conversion to the new CLI is replaced with an explicit error message. |

| Command | Description |
|---|---|
| call application event-log | Enables event logging for voice application instances. |
| call application interface stats | Enables statistics collection for application interfaces. |
| clear call application stats | Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics. |
| show call application app-level | Displays application-level statistics for voice applications. |
| show call application gateway-level | Displays gateway-level statistics for voice application instances. |
| show call application session-level | Displays event logs and statistics for voice application instances. |
| stats | Enables statistics collection for voice applications. |