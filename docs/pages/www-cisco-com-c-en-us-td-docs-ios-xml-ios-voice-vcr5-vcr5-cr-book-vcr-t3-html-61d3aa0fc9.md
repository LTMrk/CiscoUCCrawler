---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-t3-html-61d3aa0fc9
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-t3.html
retrieved_at: 2026-08-16T23:16:12.151595+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: timing delay-duration through type (voice)

## Chapter: timing delay-duration through type (voice)

# timing delay-duration through type (voice)

## timing delay-duration

To specify the delay signal duration for a specified voice port, use the timing delay - duration command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing delay-duration time

no timing delay-duration time

### Syntax Description

time

Delay signal duration for delay dial signaling, in milliseconds. Range is from 100 to 5000. The default is 2000.

### Command Default

2000 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

### Usage Guidelines

The call direction for the timing delay - duration command is out. This command is supported on E&M ports only.

## Examples

The following example sets the delay signal duration on a voice port to 3000 milliseconds:

```
voice-port 1/0/0
 timing delay-duration 3000
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

## timing delay-start

To specify the minimum delay time from outgoing seizure to out-dial address for a specified voice port, use the timing delay - start command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing delay-start time

no timing delay-start

### Syntax Description

time

Minimum delay time, in milliseconds, from outgoing seizure to outdial address. Range is from 20 to 2000. The default on the Cisco 3600 series is 300.

### Command Default

Cisco 3600 series: 300 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series routers.

### Usage Guidelines

The call direction for the timing delay - start command is out. It is supported on E&M ports only.

## Examples

The following example sets the delay-start duration on a voice port to 250 milliseconds:

```
voice-port 1/0/0
 timing delay-start 250
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

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

## timing delay-voice tdm

To specify the delay after which voice packets are played out, use the timing delay-voice tdm command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing delay-voice tdm milliseconds

no timing delay-voice tdm milliseconds

### Syntax Description

milliseconds

Duration, in milliseconds, of the timing delay. Range is integers from 1 to 1500. Default is 0.

### Command Default

milliseconds : 0 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.3(14)T

This command was implemented on the Cisco 2800 series and Cisco 3800 series.

12.4(2)T

This command was integrated into Cisco IOS Release 12.4(2)T.

### Usage Guidelines

The timing delay-voice tdm command has an effect on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                              To avoid voice loss at the receiving end of an LMR system, use this command to configure a delay for the voice packet equal
                              to the sum of the durations of all the injected tones and pauses configured with the inject tone command and the inject pause command.

## Examples

The following example configures a timing delay of 470 milliseconds before the voice packet is played out:

```
voice class tone-signal mytones
 inject tone 1 1950 3 150
 inject tone 2 2000 0 60
 inject pause 3 60
 inject tone 4 2175 3 150
 inject tone 5 1000 0 50
voice-port 1/0/0
 voice-class tone-signal mytones
 timing delay-voice tdm 470
```

Note that the delay of 470 milliseconds is equal to the sum of the durations of the injected tones and pauses in the tone-signal
                              voice class.

### Related Commands

Command

Description

inject pause

Specifies a pause between injected tones.

inject tone

Specifies a wakeup or frequency selection tone to be played out before the voice packet.

## timing delay-with-integrity

To specify the duration of the wink pulse for the delay dial for a specified voice port, use the timing delay - with - integrity command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing delay-with-integrity time

no timing delay-with-integrity

### Syntax Description

time

Duration of the wink pulse for the delay dial, in milliseconds. Range is from 0 to 5000. The default is 0.

### Command Default

0 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

### Usage Guidelines

This command is supported on E&M ports only.

## Examples

The following example sets the duration of the wink pulse for the delay dial to 10 milliseconds:

```
voice-port 1/0/0
 timing delay-with-integrity 10
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

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

## timing dialout-delay

To specify the dial-out delay for the sending digit on a specified voice port, use the timing dialout - delay command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing dialout-delay time

no timing dialout-delay time

### Syntax Description

time

Dial-out delay, in milliseconds, for the sending digit or cut-through on a Foreign Exchange Office (FXO) trunk or an E&M immediate
                                          trunk. Range is from 100 to 5000. The default is 300.

### Command Default

300 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on Cisco MC3810.

## Examples

The following example sets the dial-out delay to 350 milliseconds:

```
voice-port 1/0/0
 timing dialout-delay 350
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

timing delay-with-integrity

Specifies the duration of the wink pulse for the delay dial for a specified voice port.

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

## timing dial-pulse min-delay

To specify the time between wink-like pulses for a specified voice port, use the timing dial - pulse min - delay command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing dial-pulse min-delay time

no timing dial-pulse min-delay

### Syntax Description

time

Time between wink-like pulses, in milliseconds. Range is from 0 to 5000. The default is 300.

### Command Default

300 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

### Usage Guidelines

Use the timing dial - pulse min - delay command with PBXs that require a wink-like pulse, even though they have been configured for delay-dial signaling. If the
                              value for this argument is set to 0, the router does not generate this wink-like pulse. The call signal direction for this
                              command is in.

## Examples

The following example sets the time between the generation of wink-like pulses on a voice port to 350 milliseconds:

```
voice-port 1/0/0
 timing dial-pulse min-delay 350
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

timing delay-with-integrity

Specifies the duration of the wink pulse for the delay dial for a specified voice port.

timing dialout-delay

Specifies the dialout delay for the sending digit on a specified voice port.

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

## timing digit

To specify the dual tone multifrequency (DTMF) digit signal duration for a specified voice port, use the timing digit command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing digit time

no timing digit

### Syntax Description

time

The DTMF digit signal duration, in milliseconds. Range is 5 from 0 to 100. The default is 100.

### Command Default

100 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

### Usage Guidelines

The call signal direction for the timing digit command is out. This command is supported on Foreign Exchange Office (FXO), Foreign Exchange Station (FXS), and E&M ports.

## Examples

The following example sets the DTMF digit signal duration on a voice port to 50 milliseconds:

```
voice-port 1/0/0
 timing digit 50
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

## timing guard-out

To specify the guard-out duration of a Foreign Exchange Office (FXO) voice port, use the timing guard - out command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing guard-out time

no timing guard-out

### Syntax Description

time

Duration of the guard-out period, in milliseconds. The range is from 300 to 3000. The default is 2000.

### Command Default

The default is 2000 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on Cisco MC3810.

12.0(7)XK

This command was implemented on Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

This command is supported on FXO voice ports only.

For Caller ID to work for FXO ports registered to a Cisco Unified CM, the range in milliseconds must be between 1000 to 2000.

## Examples

The following example sets the timing guard-out duration on a voice port to 1000 milliseconds:

```
voice-port 1/0/0
 timing guard-out 1000
```

## timing hangover

To specify the number of milliseconds of delay before the digital signal processor (DSP) tells Cisco IOS software to turn
                              off the E-lead after the DSP detects that the voice stream has stopped, use the timing hangover command in voice-port configuration mode. To return to the default value, use the no form of this command.

timing hangover milliseconds

no timing hangover milliseconds

### Syntax Description

milliseconds

The number of milliseconds for which the E-lead stays active after VAD determines that the voice stream has stopped. Valid
                                          values are 0 to 10000. The default is 250 milliseconds.

### Command Default

milliseconds : 250 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The timing hangover command has an effect on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                              If the voice port has been configured with the lmr e-lead voice command, use the timing hangover command to adjust the timing if the E-lead is being turned on and off too frequently.

## Examples

The following example configures E-lead on voice port 1/0/1 on a Cisco 3745 to stay active for 300 milliseconds after VAD
                              determines that the voice stream has stopped:

```
voice-port 1/0/1
 timing hangover 300
```

## timing hookflash-in

To specify the maximum duration of an on-hook condition that will be interpreted as a hookflash by the Cisco IOS software,
                              use the timing hookflash-in command in voice-port configuration mode. To restore the default duration for hookflash timing, use the no form of this command.

timing hookflash-in milliseconds

no timing hookflash-in

### Syntax Description

milliseconds

Upper limit of the hookflash duration range, in milliseconds.

E&M voice ports--Range is 0 to 1550 milliseconds. Default is 480 milliseconds.

FXS voice ports--Range is 50 to 1550 milliseconds. Default is 1000 milliseconds.

### Command Default

milliseconds : 480 milliseconds for E&M voice ports, 1000 milliseconds for FXS voice ports.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco 3600 series.

12.3(7)T

Lower limit of the range for E&M voice ports was extended to 0 milliseconds.

12.3(14)T

This command was implemented on the Cisco 2800 series and Cisco 3800 series.

12.4(2)T

This command was integrated into Cisco IOS Release 12.4(2)T.

### Usage Guidelines

This command is applied to E&M or Foreign Exchange Station (FXS) interfaces.

For Land Mobile Radio E&M voice ports, the timing hookflash-in command configures the delay between when the M-lead is raised and when voice is transmitted. Setting the hookflash duration
                              to 0 milliseconds specifies no delay in the audio input and eliminates front-end clipping.

Analog phones connected to FXS ports use hookflash to access a second dial tone to initiate some phone features, such as transfer
                              and conference. Hookflash is an on-hook condition of short duration that is usually generated when a phone user presses the
                              Flash button on a phone. Cisco voice gateways measure the duration of detected on-hook conditions to determine whether they
                              should be interpreted as hookflash or not. The duration for the on-hook conditions generated by Flash buttons on phones varies
                              for different phone types and is interpreted by Cisco IOS software as follows:

An on-hook condition that lasts for a time period that falls inside the hookflash duration range is considered a hookflash.

An on-hook condition that lasts for a shorter period than the lower limit of the range is ignored.

An on-hook condition that lasts for a longer period than the higher limit of the range is considered a disconnect.

The hookflash duration range for FXS voice ports is defined as follows:

The lower limit of the range is set in software at 150 ms, although there is also a hardware-imposed lower limit that is typically
                                    about 20 ms, depending on platform type. An on-hook condition that lasts for a shorter time than this hardware-imposed lower
                                    limit is simply not reported to the Cisco IOS software.

The upper limit of the range is set in software at 1000 ms by default, although this value can be changed using the timing hookflash-in command in voice-port configuration mode on the voice gateway. The upper limit can be set to any value from 50 to 1550 ms.
                                    For more information, see the explanations in the "Examples" section.

This command does not affect whether hookflash relay is enabled; hookflash relay is enabled only when the dtmf-relay h245-signal command is configured on the applicable VoIP dial peers. When the dtmf-relay h245-signal command is configured, the H.323 gateway relays hookflash by using an H.245 "signal" User Input Indication method. Hookflash
                              is sent only when an H.245 signal is available.

## Examples

The following example sets an upper limit of 200 milliseconds for the hookflash duration range:

```
voice-port 1/0/0
 timing hookflash-in 200
```

If the timing hookflash-in command is set to X, a value greater than 150, then any on-hook duration between 150 and X is interpreted as a hookflash.
                              For example, if X is 1550, the hookflash duration range is 150 to 1550 ms. An on-hook signal that lasts for 1250 ms is interpreted
                              as a hookflash, but an on-hook signal of 55 ms is ignored.

```
voice-port 1/0/0
 timing hookflash-in 1550
```

If the timing hookflash-in command is set to X, a value less than 150, then any on-hook duration between Y, the hardware lower limit, and X is interpreted
                              as a hookflash. For example, if X is 65, the hookflash duration range is Y to 65 ms. An on-hook signal that lasts for 1250
                              ms is interpreted as a disconnect, but an on-hook signal of 55 ms is interpreted as a hookflash. (This example assumes that
                              Y for the voice gateway is lower than 55 ms.)

```
voice-port 1/0/0
 timing hookflash-in 65
```

### Related Commands

Command

Description

dtmf-relay (Voice over IP)

Specifies how an H.323 gateway relays DTMF tones between telephony interfaces and an IP network.

## timing hookflash-out

To specify the duration of hookflash indications that the gateway generates on a Foreign Exchange Office (FXO) interface,
                              use the timing hookflash - out command in voice-port configuration mode. To restore the default duration for hookflash timing, use the no form of this command.

timing hookflash-out time

no timing hookflash-out

### Syntax Description

time

Duration of the hookflash, in milliseconds. Range is from 50 to 1550. The default is 400 milliseconds.

### Command Default

400 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.1(1)T

This command was introduced on Cisco 2500, Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco MC3810.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on Cisco AS5850.

### Usage Guidelines

This command does not affect whether hookflash relay is enabled; hookflash relay is enabled only when the dtmf - relay h245 - signal command is configured on the applicable VoIP dial peers. Hookflash is relayed by using an H.245-signal indication and can
                              be sent only when an H.245 signal is available.

Use the timing hookflash - out command on FXO interfaces to specify the duration (in milliseconds) of a hookflash indication. To set hookflash timing parameters
                              for analog voice interfaces, use the timing command.

## Examples

The following example implements timing for the hookflash with a duration of 200 milliseconds.

```
voice-port 1/0/0 timing hookflash-out 200
```

### Related Commands

Command

Description

dtmf-relay (Voice over IP)

Specifies how an H.323 gateway relays DTMF tones between telephony interfaces and an IP network.

voice-port

Enters voice-port configuration mode.

## timing ignore m-lead

To ignore M-lead or voice activity detection (VAD) changes for a specified amount of time after sending the E-lead off signal,
                              use the timing ignore m-lead command in voice-port configuration mode. To return to the default value, use the no form of this command.

timing ignore m-lead milliseconds

no timing ignore m-lead milliseconds

### Syntax Description

milliseconds

The number of milliseconds following the sending of the E-lead off signal for which the M-lead and VAD changes are ignored.
                                          Valid values are 0 to 10000. The default is 0 milliseconds.

### Command Default

milliseconds : 0 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The timing ignore m-lead command has an effect on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                                    Use this command to reduce echo feedback on an LMR voice port. This command has an effect only if the voice port is configured
                                    for half duplex mode.

## Examples

The following example configures voice port 1/0/1 on a Cisco 3745 to ignore M-lead or VAD changes for 500 milliseconds after
                              sending the E-lead off signal:

```
voice-port 1/0/1
 timing ignore m-lead 500
```

## timing interdigit

To specify the dual-tone multifrequency (DTMF) interdigit duration for a specified voice port, use the timing interdigit command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing interdigit time

no timing interdigit time

### Syntax Description

time

DTMF interdigit duration, in milliseconds. Range is from 50 to 500. The default is 100.

### Command Default

100 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

11.3(1)MA

This command was supported on Cisco MC3810.

### Usage Guidelines

The call signal direction for the timing interdigit command is out. This command is supported on Foreign Exchange Office (FXO), Foreign Exchange Station (FXS), and E&M ports.

## Examples

The following example sets the DTMF interdigit duration on a voice port to 150 milliseconds:

```
voice-port 1/0/0
 timing interdigit 150
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

## timing opx-ringwait

To set the maximum wait time for detecting the next ring on FXO ports, use the timing opx-ringwait command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing opx-ringwait msecs

no timing opx-ringwait

### Syntax Description

msecs

Maximum duration, in milliseconds, to wait for the next ring. Range is 2000 to 10000. Default is 6000.

### Command Default

Timeout for detecting ring tones is 6000 ms (6 sec).

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.4(4)T

This command was introduced.

### Usage Guidelines

This command prevents the voice gateway from prematurely disconnecting private line automatic ring-down (PLAR) off-premises
                              extension (OPX) calls when the duration between ring tones from the switch is more than 6 sec. The absence of a ring tone
                              from the switch indicates that the originating party has disconnected the call. Because some analog switches take longer than
                              6 sec to generate the ring tone, the voice gateway could clear the call leg while it is still ringing for a PLAR OPX call,
                              unless the 6-sec default is changed with this command.

## Examples

The following example sets the timeout for the next ring to 8 sec:

```
voice-port 2/0/10
 timing opx-ringwait 8000
```

### Related Commands

Command

Description

voice-port

Enters voice-port configuration mode.

show voice port

Displays configuration information about a specific voice port.

## timing percentbreak

To specify the percentage of the break period for dialing pulses for a voice port, use the timing percentbreak command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing percentbreak percent

no timing percentbreak

### Syntax Description

percent

Percentage of the break period for dialing pulses. Range is from 20 to 80. The default is 50.

### Command Default

50 percent

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA4

This command was introduced on Cisco MC3810.

12.0(7)XK

This command was implemented on Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

The timing percentbreak command is supported on Foreign Exchange Office (FXO) and E&M voice ports only.

## Examples

The following example sets the break period percentage on a voice port to 30 percent:

```
voice-port 0/0/1
 timing percentbreak 30
```

### Related Commands

Command

Description

timing pulse

Configures the pulse dialing rate for a voice port.

timing pulse - interdigit

Configures the pulse interdigit timing for a voice port.

## timing pulse

To specify the pulse dialing rate for a specified voice port, use the timing pulse command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing pulse pulses-per-second

no timing pulse pulses-per-second

### Syntax Description

pulses - per - second

Pulse dialing rate, in pulses per second. Range is from 10 to 20. The default is 20.

### Command Default

20 pulses per seconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA

This command was supported on the Cisco MC3810.

### Usage Guidelines

The call signal direction for the timing pulse command is out. This command is supported on Foreign Exchange Office (FXO) and E&M ports only.

## Examples

The following example sets the pulse dialing rate on a voice port to 15 pulses per second:

```
voice-port 1/0/0
 timing pulse 15
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

timing pulse-interdigit

Specifies the pulse interdigit timing for a specified voice port.

timing wink-duration

Specifies the maximum wink signal duration for a specified voice port.

timing wink-wait

Specifies the maximum wink-wait duration for a specified voice port.

## timing pulse-interdigit

To specify the pulse interdigit timing for a specified voice port, use the timing pulse - interdigit command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing pulse-interdigit time

no timing pulse-interdigit time

### Syntax Description

time

Pulse dialing interdigit timing, in milliseconds. Range is from 100 to 1000. The default is 500.

### Command Default

500 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

11.3(1)MA

This command was supported on Cisco MC3810.

### Usage Guidelines

The call signal direction for the timing pulse - interdigit command is out. This command is supported on Foreign Exchange Office (FXO) and E&M ports only.

## Examples

The following example sets the pulse-dialing interdigit timing on a voice port to 300 milliseconds:

```
voice-port 1/0/0
 timing pulse-interdigit 300
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

timing wink-duration

Specifies the maximum wink signal duration for a specified voice port.

timing wink-wait

Specifies the maximum wink-wait duration for a specified voice port.

## timing sup-disconnect

To define the minimum time to ensure that an on-hook indication is intentional and not an electrical transient on the line
                              before a supervisory disconnect occurs (based on power denial signaled by the PSTN or PBX), use the timing sup-disconnect command in voice-port configuration mode. To restore the default value, use the no form of this command.

timing sup-disconnect milliseconds

no timing sup-disconnect milliseconds

### Syntax Description

milliseconds

Minimum time, in milliseconds, after detection of an on-hook indication to determine that the on-hook condition is intentional
                                          and then to hang up the POTS call leg. The range is from 50 to 1500. The default is 350.

### Command Default

The default minimum time is 350 milliseconds before a supervisory disconnect occurs.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(12)

This command was introduced.

12.3(11)T6

This command was integrated into Cisco IOS Release 12.3(11)T6.

12.3(14)T

This command was integrated into Cisco IOS Release 12.3(14)T.

12.4(12)

This command was integrated into Cisco IOS Release 12.4(12).

### Usage Guidelines

Prior to the implementation of the timing sup-disconnect command, analog Foreign Exchange Office (FXO) ports could not detect short disconnect signals lasting fewer than 350 ms in
                              duration. Using this command, you can specify a wait period from 50 to 1500 ms to ensure that when an on-hook indication persists
                              for a time that is longer than the configured value, the on-hook condition is considered intentional and a hang-up is signaled
                              on the POTS call leg.

This timer affects only analog loop-start FXO voice ports.

Even though the timing sup-disconnect command can be entered under the voice port in FXO ground-start signaling, the changes in the timer setting take effect only
                              in FXO loop-start signaling.

## Examples

The following example sets the timer to wait 500 ms after detecting an on-hook signal before a supervisory disconnect occurs
                              on the POTS call leg:

```
voice-port 1/0/0
 timing sup-disconnect 500
```

### Related Commands

Command

Description

show voice port

Displays configuration information about a specific voice port.

voice-port

Enters voice-port configuration mode.

## timing wait-wink

To set the maximum time to wait for wink signal after an outgoing seizure is sent, use the timing wait - wink command in voice port configuration mode. To restore the default value, use the no form of this command.

timing wait-wink milliseconds

no timing wait-wink milliseconds

### Syntax Description

milliseconds

Maximum time to wait for wink signal after an outgoing seizure is sent. Valid entries are from 100 to 6500 milliseconds (ms). Supported on ear and mouth (E&M) ports only.

### Command Default

milliseconds : 550 milliseconds

### Command Modes

Voice port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series routers.

11.3(1)MA

This command was implemented on Cisco MC3810 multiservice concentrators.

12.4(12)

The millisecond range was extended from 5000 to 6500.

## Examples

The following example configures the maximum time to wait for wink signaling after an outgoing seizure is sent on a voice
                              port for 300 milliseconds:

```
voice-port 1/0/0
 timing wait-wink 300
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

timing delay-with-integrity

Specifies the duration of the wink pulse for the delay dial for a specified voice port.

timing dialout-delay

Specifies the dial-out delay for the sending digit on a specified voice port.

timing delay-with-integrity

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

timing wink-wait

Specifies the maximum wink-wait duration for a specified voice port.

## timing wink-duration

To specify the timing for transmit and receive wink-signal duration for a voice port, use the timing wink - duration command in voice-port configuration mode. To reset to the default values, use the no form of this command.

timing wink-duration { time | receive minimum maximum }

no timing wink-duration

### Syntax Description

time

Maximum transmit duration, in milliseconds (ms), for a wink-start signal. The range is from 50 to 3000. The default is 200.

receive

Indicates that a range is to be specified for a received wink-start signal.

minimum

Received minimum wink length, in milliseconds. The range is from 40 to 2950. The default is 140.

maximum

Received maximum wink length, in milliseconds. The range is from 150 to 3150. The default is 290.

### Command Default

Transmit wink-duration timing is set to 200 ms. The received wink-duration timing minimum is set to 140 ms and the maximum
                              is set to 290 ms.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

11.3(1)MA

This command was integrated into Cisco IOS Release 11.3(1)MA and support was added for the Cisco MC3810.

12.4(13)

This command was integrated into Cisco IOS Release 12.4(13) and the receive keyword and minimum and maximum arguments were added.

### Usage Guidelines

The call signal direction for the timing wink - duration command is out. This command is supported on ear and mouth (E&M) ports only.

When wink-start signaling is used, the originating side seizes the line by going off-hook and then waits for an acknowledgment
                              from the other end before initiating a call. The acknowledgment is a reversal of polarity (off-hook) for a timing period referred
                              to as a wink. A wink should occur no earlier than 100 ms after the receipt of the incoming seizure signal. In addition to
                              the signaling function, the wink start serves as an integrity check that identifies a malfunctioning trunk and allows the
                              network to send a reorder tone to the calling party.

When you set the receive range, the minimum and maximum values of acceptable wink must provide an acceptable range of at least
                              50 ms. For example, entering the command timing wink-duration receive 160 200 results in an error message.

## Examples

The following example shows how to set the transmit wink-signal duration on voice port 1/0/0 to 300 ms:

```
voice-port 1/0/0
 timing wink-duration 300
```

The following example shows how to set the range for the receive wink-signal duration on voice port 1/0/0 to 160 to 210 ms:

```
voice-port 1/0/0
 timing wink-duration receive 160 210
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

timing delay-duration

Specifies the delay signal duration for a specified voice port.

timing delay-start

Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port.

timing delay-with-integrity

Specifies the duration of the wink pulse for the delay dial for a specified voice port.

timing dialout-delay

Specifies the dialout delay for the sending digit on a specified voice port.

timing delay-with-integrity

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

timing wink-wait

Specifies the maximum wink-wait duration for a specified voice port.

## timing wink-wait

To specify the maximum wink-wait duration for a specified voice port, use the timing wink - wait command in voice-port configuration mode. To reset to the default, use the no form of this command.

timing wink-wait time

no timing wink-wait

### Syntax Description

time

Maximum wink-wait duration, in milliseconds, for a wink start signal. Range is from 100 to 6500. The default is 200.

### Command Default

200 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series.

11.3(1)MA

This command was supported on Cisco MC3810.

12.4(12)

The millisecond range was extended from 5000 to 6500.

### Usage Guidelines

The call signal direction for the timing wink - wait command is out. This command is supported on ear and mouth (E&M) ports only.

## Examples

The following example sets the wink-wait duration on a voice port to 300 milliseconds:

```
voice-port 1/0/0
 timing wink-wait 300
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

timing clear-wait

Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port.

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

## tls

To enable Transport Layer Security (TLS) for the Skinny Client Control Protocol (SCCP) connection between the SCCP server
                              and the SCCP client, use the tls command in DSP farm profile configuration mode. To disable secure SCCP signaling, use the no form of this command.

tls

no tls

### Syntax Description

This command has no arguments or keywords.

### Command Default

Secure SCCP signaling exchange is enabled by default.

### Command Modes

DSP farm profile configuration (config-dspfarm-profile #)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

12.4(24)T

This command was integrated into Cisco IOS Release 12.4(24)T.

### Usage Guidelines

Use the tls command to enable secure SCCP signaling exchange. The configuration can be modified only when the dspfarm profile is shut
                              down. To shut down the dsp farm profile, configure the no shutdown command.

## Examples

The following example shows how to configure the tls command to enable TLS support for digital signal processor (DSP) farm services profile 1:

```
Router(config)# dspfarm profile 1 transcode security Router(config-dspfarm-profile)# tls
```

### Related Commands

Command

Description

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for DSP farm services.

## toggle-between-two-calls

To define a Feature Access Code (FAC) to access the Toggle Between Two Calls feature in feature mode on analog phones connected
                              to FXS ports, use the toggle-between-two-calls command in STC application feature-mode call-control configuration mode. To return the code to its default, use the no form of this command.

toggle-between-two-calls keypad-character

no toggle-between-two-calls

### Syntax Description

keypad-character

Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #5.

### Command Default

The default value is #5.

### Command Modes

STC application feature-mode call-control configuration (config-stcapp-fmcode)

## Command History

Release

Modification

15.0(1)M

This command was introduced.

### Usage Guidelines

This command changes the value of the FAC for Toggle Between Two Calls from the default (#5) to the specified value.

If you attempt to configure this command with a value that is already configured for another FAC in feature mode, you receive
                              a message. This message will not prevent you from configuring the feature code. If you configure a duplicate FAC, the system
                              implements the first feature it matches in the order of precedence as determined by the value for each FAC (#1 to #5).

If you attempt to configure this command with a value that precludes or is precluded by another FAC in feature mode, you receive
                              a message. If you configure a FAC to a value that precludes or is precluded by another FAC in feature mode, the system always
                              executes the call feature with the shortest code and ignores the longer code. For example, 1 will always preclude 12 and 123.
                              These messages will not prevent you from configuring the feature code. You must configure a new value for the precluded code
                              in order to enable phone user access to that feature.

## Examples

The following example shows how to change the value of the feature code for the Toggle Between Two Calls feature from the
                              default (#5). With this configuration, a phone user in basic call mode presses hook flash to get the first dial tone, then
                              dials an extension number to connect to a second call. During the second call, the user presses a hook flash to get a feature
                              tone and then dials 55 to toggle back to the previous call party.

```
Router(config)# stcapp call-control mode feature Router(config-stcapp-fmcode)# toggle-between-two-calls 55 Router(config-stcapp-fmcode)# exit
```

### Related Commands

Command

Description

conference

Defines FAC in Feature Mode to initiate a three-party conference.

drop-last-conferee

Defines FAC in feature mode to use to drop last active call during a three-party conference.

hangup-last-active-call

Defines FAC in feature mode to drop last active call during a three-party conferencee.

transfer

Defines FAC in feature mode to connect a call to a third party that the phone user dials.

## token-root-name

To specify which root or Certificate Authority (CA) certificate the router uses to validate the settlement token in the incoming
                              setup message, use the token - root - name command in settlement configuration mode. To reset to the default, use the no form of this command.

token-root-name name

no token-root-name

### Syntax Description

name

Certificate identification name as configured with the crypto ca identity name command or the crypto ca trusted-root name command.

### Command Default

The terminating gateway uses the CA certificate to validate the settlement token.

### Command Modes

Settlement configuration

## Command History

Release

Modification

12.1(1)T

This command was introduced on Cisco 2600 series, Cisco 3600 series, Cisco AS5300, and Cisco AS5800.

## Examples

The following example defines the token - root - name as "sample":

```
token-root-name sample
```

The following example shows new output for the show settlement command to display the value of the token - root - name command:

```
Settlement Provider 0
        Operation Status = UP
        Type = osp
        Address url = https://1.14.115.100:8444/
        Encryption = all                (default)
        Token Root Name = sample
        Max Concurrent Connections = 20 (default)
        Connection Timeout = 3600 (s)   (default)
        Response Timeout = 1 (s)        (default)
        Retry Delay = 2 (s)             (default)
        Retry Limit = 1                 (default)
        Session Timeout = 86400 (s)     (default)
        Customer Id = 1000
        Device Id = 2000
        Roaming = Disabled              (default)
        Signed Token = On
        Number of Connections = 1
        Number of Transactions = 0
```

### Related Commands

Command

Description

crypto ca identity

Declares the Certificate Authority that your router should use.

crypto ca trusted - root

Configures the root certificate that the server uses to sign the settlement tokens.

show settlement

Displays the configuration for all settlement server transactions.

## tone busytone

To enable automatic busytone generation in a basic call scenario, use the tone busytone command in dial peer voice configuration mode. To disable automatic busytone generation, use the no form of this command.

tone busytone remote-onhook

no tone busytone remote-onhook

### Syntax Description

remote-onhook

Generates busy tone after remote onhook in basic call mode.

### Command Default

Automatic busytone generation after remote disconnect is disabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(20)T

This command was introduced.

### Usage Guidelines

The automatic busytone generation after remote disconnect in basic call mode feature is enabled and disabled per dial peer
                              with the tone busytone remote-onhook command. The tone busytone command is available to all dial peer services. Each service determines whether to utilize or enable it. For STCAPP, only
                              the Foreign eXchange Subscriber (FXS) loop-start port will enable this service.

The tone busytone command cannot coexist with the dialtone generation after remote-onhook feature. Because the tone dialtone is a default configuration, you must disable the feature using the no tone dialtone command before connfiguring the tone busytone command.

Use the show dial-peer voice command or the show stcapp device voice command to verify the feature is enabled.

## Examples

The following example shows busytone generation after remote disconnect being configured:

```
Router(config-dial-peer)# tone busytone remote-onhook
```

### Related Commands

Command

Description

show dial-peer voice

Displays information for voice dial peers.

tone dialtone

Enable automatic dial tone generation.

show stcapp device voice

Displays configuration information about STCAPP analog voice ports.

## tone dialtone

To enable automatic dial-tone generation in basic call mode, use the tone dialtone command in dial peer configuration mode. To disable automatic dial-tone generation, use the no form of this command.

tone dialtone remote-onhook

no tone dialtone remote-onhook

### Syntax Description

remote-onhook

Generates dial tone after remote onhook in basic call mode.

### Command Default

Automatic dial-tone generation after remote disconnect is enabled.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(6)XE

This command was introduced.

12.4(11)T

This command was integrated into Cisco IOS Release 12.4(11)T.

### Usage Guidelines

Use this command to generate immediate dial tone once a remote party disconnects, similar to what the user experiences in
                              a PBX environment. If you disable this feature using the no form of this command, the user is required to go on hook or perform a hookflash to generate dial tone after the remote party
                              disconnects in a basic two-part call scenario. This feature is supported on Skinny Client Control Protocol (SCCP) gateway
                              controlled loop-start FXS ports only.

## Examples

The following examples show that the automatic Dial Tone Generation After Remote Onhook feature is enabled. Because the dial
                              tone generation after remote onhook feature is enabled by default, it does not display in the show running-config output.

```
Router# show running-config service stcapp
 dial-peer voice 3001 pots
 port 1/1/1
 
Router# show dial-peer voice 3001 VoiceEncapPeer3001
 peer type = voice, system default peer = FALSE, information type = voice,
!
!
!
 in bound application associated: 'stcapp'
 dial tone generation after remote-onhook = enabled
 
Router# show stcapp device voice-port 1/1/1 Port Identifier:  1/1/1
!
Dialtone after remote-onhook feature: activated
```

The following examples show the dial tone generation after remote onhook feature disabled.

```
Router# show running-config no tone dialtone remote-onhook
dial-peer voice 3002 pots
 service stcapp
 port 1/1/0
```

### Related Commands

Command

Description

sccp

Enables SCCP and related applications.

show dial-peer voice

Displays information for voice dial peers.

show stcapp device

Displays configuration information about SCCP Telephony Control Application (STCAPP) analog voice ports.

## tone incoming

To activate 2100-Hz answer (ANS) tone detection on either the IP or the PSTN side of the network and to disable the echo
                              suppressor, use the tone incoming command in voice-service VoIP configuration mode or VoIP dial-peer configuration mode. To deactivate tone detection and disable
                              the echo suppressor, use the no form of this command.

tone incoming [ ip | pstn ] { ans-all auto-control | ans disable echo suppressor | anspr disable echo suppressor }

no tone incoming

### Syntax Description

ip

(Optional) Specifies tone detection on the IP side of the network.

pstn

(Optional) Specifies tone detection on the PSTN side of the network.

ans auto-control

Detects ANS tone and enables standard actions for modem tones.

ans-all disable echo suppressor

Detects modem answer tones and disables echo suppressor.

anspr disable echo suppressor

Detects /ANS tone and disables echo suppressor.

### Command Default

Tone incoming detection is not enabled.

### Command Modes

Voice-service VoIP configuration VoIP dial-peer configuration

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

Use this command in voice-service VoIP or VoIP dial-peer configuration mode to activate detection of all ANS, ANSam, and
                              ANSpr tones and enable or disable echo canceller control. When this command is issued in voice-service VoIP configuration
                              mode , all dial peers are globally configured unless a specific dial peer is configured for no tone incoming.

To deactivate all 2100-Hz ANS, ANSam, and ANSpr tone detection on either the IP or the PSTN side of the network, and enable
                              the echo canceller, use the no tone incoming command in voice-service VoIP configuration or VoIP dial-peer configuration mode.

If neither IP nor PSTN is specified, all ANS, ANSam, and ANSpr tones are detected on both sides of the network, and the echo
                              suppressor is disabled in all cases.

The tone incoming ip ans-all auto-control command is equivalent to these two commands together:

tone incoming ip ans disable echo suppressor

tone incoming ip anspr disable echo suppressor

The tone incoming pstn ans-all auto-control command is equivalent to these two commands together:

tone incoming pstn ans disable echo suppressor

tone incoming pstn anspr disable echo suppressor

The tone incoming ans-all auto-control command is equivalent to these four commands together:

tone incoming ip ans disable echo suppressor

tone incoming ip anspr disable echo suppressor

tone incoming pstn ans disable echo suppressor

tone incoming pstn anspr disable echo suppressor

When modem tones from either the IP or PSTN direction are received, the echo canceller can be dynamically disabled to allow
                              modem calls to pass through.

The IP tone detector feature applies only on the following NextPort platforms: Cisco AS5350, Cisco AS5400, and Cisco AS5850--and
                              only with SIP and H.323 voice signaling. It does not apply to MGCP in VoIP dial-peer configuration mode.

The gateway must be configured for G.711 codecs for the IP tone detector feature to work (see the "Examples" section).

To display the status of the echo canceller, use the show port operational status command.

## Examples

The following example configures tone detection of ANS tones in voice-service VoIP configuration mode:

```
Router(conf-voi-serv)# tone incoming ip ans disable echo supressor
```

The following example configures tone detection of all incoming ANS, ANSam, and ANSpr tones on a dial peer:

```
Router(config-dial-peer)# tone incoming ip ans-all auto-control
```

### Related Commands

Command

Description

tone incoming system

Sets a dial peer for tone incoming or no tone incoming detection.

show port operational status

Displays the status of the echo canceller.

## tone incoming system

To set a dial peer for tone incoming or no tone incoming, use the tone incoming system command in VoIP dial-peer configuration mode. To block the voice service VoIP settings for a dial peer, use the no form of this command.

tone incoming system

no tone incoming system

### Syntax Description

This command has no arguments or keywords.

### Command Default

The dial peer is set for tone incoming.

### Command Modes

VoIP dial-peer configuration

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

Use this command in VoIP dial-peer configuration mode to activate or deactivate tone detection and to enable echo canceller
                              control. When modem tones from either the IP or PSTN directions are received. The echo canceller can be dynamically disabled
                              to allow modem calls through. This command is used primarily to allow or to block global voice service VoIP configuration
                              settings.

To block the voice service VoIP settings for a dial peer, use the no tone incoming system command.

## Examples

The following example shows activating tone detection for a dial peer.

```
Router(config-dial-peer)# tone incoming system
```

The following example shows deactivating tone detection for a dial peer.

```
Router(config-dial-peer)# no tone incoming system
```

### Related Commands

Command

Description

tone incoming ans disable echo suppressor

Activates ANS tone detection.

tone incoming anspr disable echo canceller

Activates ANSpr tone detection.

tone incoming ans-all auto-control

Activates ANS, ANSam, and ANSpr tone detection.

show port operational status

Displays the status of the echo canceller.

## tone ringback alert-no-PI

To generate automatic ringback for the caller when no Progress Indicator (PI) alert has been received over the H.323 network,
                              use the tone ringback alert - no - PI command in dial-peer configuration mode. To disable automatic ringback, use the no form of this command.

tone ringback alert-no-PI

no tone ringback alert-no-PI

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 1700 series, Cisco 2600 series, Cisco 3600 series, Cisco 3700 series, Cisco 7200
                                          series, Cisco AS5300, and Cisco AS5800.

### Usage Guidelines

Use this command to generate ringback in an H.323 network when the attached device (for example, an ISDN device) cannot.

## Examples

The following example activates ringback for a VoIP dial peer numbered 322:

```
Router(config)# dial-peer voice 322 voip
Router(config-dial-peer)# tone ringback alert-no-PI
```

### Related Commands

Command

Description

progress_ind

Sets a specific PI in call Setup, Progress, or Connect messages from an H.323 VoIP gateway.

## trace (voice service voip)

To configure the VoIP Trace framework in CUBE, use the trace command in voice service voip configuration mode. To disable VoIP tracing, use the no form of this command.

[no] trace

### Command Default

Trace is enabled by default.

### Command Modes

Voice Service VoIP configuration mode (conf-voi-serv)

## Command History

Release

Modification

Cisco IOS XE Amsterdam 17.3.2

Cisco IOS XE Bengaluru 17.4.1a

This command was introduced on Cisco Unified Border Element.

### Usage Guidelines

Use the trace command to configure the VoIP Trace framework to persistently monitor and troubleshoot SIP calls on CUBE. With trace enabled, event logging and debugging of VoIP parameters such as SIP messages, FSM, and Unified Communication flows processed
                              by CUBE are logged.

VoIP tracing is disabled using the command shutdown under the trace configuration mode. To re-enable VoIP Trace, configure [no] shutdown . The shutdown command retains the custom memory-limit whereas [no] trace resets the memory-limit to default.

To define a custom limit for the memory allotted for storage of VoIP Trace information in CUBE, configure memory-limit memory under trace configuration mode. Range is 10–1000 MB. If memory-limit isn’t configured, the default configuration of memory-limit platform is applied. By default, 10% of the total memory available to the IOS processor at the time of configuring the command will
                              be reserved for VoIP Trace data storage.

## Examples

The following is a sample configuration for enabling trace on Unified Border Element:

```
router#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
router(config)#voice service voip
router(conf-voi-serv)#?
VOICE SERVICE configuration commands:
address-hiding Address hiding (SIP-SIP)
allow-connections Allow call connection types
call-quality Global call quality of service setup
callmonitor Call Monitoring
cause-code Sets the internal cause code for SIP and H323
clid Caller ID option
cpa Enable Call Progress Analysis for voip calls
default Set a command to its defaults
dtmf-interworking Dtmf Interworking
emergency List of Emergency Numbers
exit Exit from voice service configuration mode
fax Global fax commands
fax-relay Global fax relay commands
gcid Enable Global Call Identifcation for voip
h323 Global H.323 configuration commands
ip Voice service voip ip setup
lpcor Voice service voip lpcor setup
media Global media setting for voip calls
media-address Voice Media IP Address Range
mode Global mode setting for voip calls
modem Global modem commands
no Negate a command or set its defaults
notify send facility indication to application
qsig QSIG
redirect voip call redirect
redundancy-group Associate redundancy-group with voice HA
redundancy-reload Reload control when RG fail
rtcp Configure RTCP report generation
rtp-media-loop Global setting for rtp media loop count
rtp-port Global setting for rtp port range
shutdown Stop VoIP services gracefully without dropping active calls
signaling Global setting for signaling payload handling
sip SIP configuration commands
srtp Allow Secure calls
stun STUN configuration commands
supplementary-service Config supplementary service features trace Voip Trace configuration voice enable voice parameters
vpn-group Enter vpn-group mode
vpn-profile Enter vpn-profile mode

router(conf-voi-serv)# trace
```

### Related Commands

Command

Description

memory-limit (trace)

Defines the memory limit for storing VoIP Trace information.

Disable the VoIP Trace serviceability framework in CUBE.

show voip trace

Displays the VoIP Trace information for SIP legs on a call received on CUBE

## transfer

To define a Feature Access Code (FAC) to access the Call Transfer feature in feature mode on analog phones connected to FXS
                              ports, use the transfer command in STC application feature-mode call-control configuration mode. To return the code to its default, use the no form of this command.

transfer keypad-character

no transfer

### Syntax Description

keypad-character

Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #2.

### Command Default

The default value is #2.

### Command Modes

STC application feature-mode call-control configuration (config-stcapp-fmcode)

## Command History

Release

Modification

15.0(1)M

This command was introduced.

### Usage Guidelines

This command changes the value of the FAC for Call Transfer from the default (#2) to the specified value.

If you attempt to configure this command with a value that is already configured for another FAC in feature mode, you receive
                              a message. This message will not prevent you from configuring the feature code. If you configure a duplicate FAC, the system
                              implements the first feature it matches in the order of precedence as determined by the value for each FAC (#1 to #5).

If you attempt to configure this command with a value that precludes or is precluded by another FAC in feature mode, you receive
                              a message. If you configure a FAC to a value that precludes or is precluded by another FAC in feature mode, the system always
                              executes the call feature with the shortest code and ignores the longer code. For example, 1 will always preclude 12 and 123.
                              These messages will not prevent you from configuring the feature code. You must configure a new value for the precluded code
                              in order to enable phone user access to that feature.

## Examples

The following example shows how to change the value of the feature code for the Call Transfer feature from the default (#2).
                              With this configuration, a phone user presses hook flash to get the first dial tone, then dials an extension number to connect
                              to a second call. When the second call is established, the user presses hook flash to get a feature tone and then dials 22
                              to transfer the call; the user hears silence after the call is transferred.

```
Router(config)# stcapp call-control mode feature Router(config-stcapp-fmcode)# transfer 22 Router(config-stcapp-fmcode)# exit
```

### Related Commands

Command

Description

conference

Defines FAC in Feature Mode to initiate a three-party conference.

drop-last-conferee

Defines FAC in feature mode to use to drop last active call during a three-party conference.

hangup-last-active-call

Defines FAC in feature mode to drop last active call during a three-party conferencee.

toggle-between-two-calls

Defines FAC in feature mode to toggle between two active calls.

## translate

To apply a translation rule to manipulate dialed digits on an inbound POTS call leg, use the translate command in voice-port configuration mode. To remove the translation rule, use the no form of this command.

translate { calling-number | called-number } name-tag

no translate { calling-number | called-number } name-tag

### Syntax Description

calling - number

Translation rule applies to the inbound calling party number.

called - number

Translation rule applies to the inbound called party number.

name - tag

Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value.

### Command Default

No default behavior or values

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.0(7)XR1

This command was introduced for VoIP on Cisco AS5300.

12.0(7)XK

This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T and implemented for VoIP Cisco AS5300, Cisco 7200, and Cisco 7500.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

A translation rule is a general-purpose digit-manipulation mechanism that performs operations such as automatically adding
                              telephone area and prefix codes to dialed numbers.

## Examples

The following example applies translation rule 21 to the POTS inbound calling-party number:

```
translation-rule 21
 rule 1 555.% 1408555 subscriber international
 rule 2 7.% 1408555 abbreviated international
voice-port 0:1
 translate calling-number 21
```

The following example applies translation rule 20 to the POTS inbound called-party number:

```
translation-rule 20
 rule 1 .%555.% 7 any abbreviated
voice-port 0:1
 translate called-number 20
```

### Related Commands

Command

Description

numbering-type

Specifies number type for the VoIP or POTS dial peer.

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

show translation-rule

Displays the contents of all the rules that have been configured for a specific translation name.

translate-outgoing

Applies a translation rule to a calling party number or a called party number for outgoing calls.

translation-rule

Creates a translation name and enters translation-rule configuration mode.

voip-incoming translation-rule

Captures calls that originate from H.323-compatible clients.

## translate (translation profiles)

To associate a translation rule with a voice translation profile, use the translate command in voice translation-profile configuration mode. To delete the translation rule from the profile, use the no form of this command.

translate { called | calling | redirect-called | redirect-target } translation-rule-number

no translate { called | calling | redirect-called | redirect-target } translation-rule-number

### Syntax Description

called

Associates the translation rule with called numbers.

calling

Associates the translation rule with calling numbers.

redirect - called

Associates the translation rule with redirected called numbers.

redirect-target

Associates the translation rule with transfer-to numbers and call-forwarding final destination numbers.

translation - rule - number

Number of the translation rule to use for the call translation. Valid range is from 1 to 2147483647. There is no default value.

### Command Default

No translation rule is associated with the translation profile.

### Command Modes

Voice translation-profile configuration (cfg-translation-profile)

## Command History

Release

Modification

12.0(7)XR1

This command was introduced on the Cisco AS5300.

12.0(7)XK

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T and implemented on the following platforms: Cisco 1750, Cisco
                                          AS5300, Cisco 7200 series, and Cisco 7500 series.

12.1(2)T

This command was implemented on the Cisco MC3810.

12.2(11)T

This command was reconfigured for voice translation-profile configuration mode. The redirect - called keyword and translation-rule-number argument were added.

12.4(11)XJ

The redirect-target keyword was added.

12.4(15)T

The redirect-target keyword was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

Use this command as part of a voice translation-profile definition. Enter this command for each translation rule that is part
                              of the profile definition.

## Examples

The following example defines voice translation profile "sjmorning" with two translation rules: translation rule 15 for called
                              numbers and translation rule 36 for calling numbers.

```
Router(config)# voice translation-profile sjmorning Router(cfg-translation-profile)# translate called 15 Router(cfg-translation-profile)# translate calling 36
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation-rule.

show voice translation-profile

Displays the configuration of the translation-profile.

translation-profile (dial-peer)

Assigns a translation profile to a dial peer.

translation-profile (source group)

Assigns a translation profile to a source IP group.

translation-profile (trunk group)

Assigns a translation profile to a trunk group.

translation-profile (voice port)

Assigns a translation profile to a voice port.

translation-profile (voice service POTS)

Assigns a translation profile to an NFAS interface.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translate-outgoing

To apply a translation rule to manipulate dialed digits on an outbound POTS or VoIP call leg, use the translate - outgoing command in dial-peer configuration mode. To disable the translation rule, use the no form of this command.

translate-outgoing { calling-number | called-number } name-tag

no translate-outgoing { calling-number | called-number } name-tag

### Syntax Description

calling - number

Apply to the outbound calling party number.

called - number

Apply to the outbound called party number.

name - tag

Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is 1 to 2147483647. There is no
                                          default value.

### Command Default

No default behavior or values

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.0(7)XR1

This command was introduced for VoIP on Cisco AS5300.

12.0(7)XK

This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(1)T

This command was integrated into Cisco IOS Release 12.2(1)T and implemented for VoIP on the Cisco 1750, Cisco AS5300, Cisco
                                          7200, and Cisco 7500. support for the Cisco MC3810 is not included in this release.

12.1(2)T

This command is supported on the Cisco MC3810 in this release.

## Examples

The following example applies translation rule 21 to the VoIP outbound calling number:

```
translation-rule 21
 rule 1 555.% 1408555 subscriber international
 rule 2 7.% 1408555 abbreviated international
 dial-peer voice 100 voip
 translate-outgoing calling-number 21
```

The following example applies translation rule 20 to the VoIP called number:

```
translation-rule 20
 rule 1 .%555.% 7 any abbreviated
dial-peer voice 100 voip
 translate-outgoing called-number 20
```

### Related Commands

Command

Description

numbering-type

Specifies number type for the VoIP or POTS dial peer.

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

show translation-rule

Displays the contents of all the rules that have been configured for a specific translation name.

translate

Applies a translation rule to a calling party number or a called party number for incoming calls.

translation-rule

Creates a translation name and enters translation-rule configuration mode.

voip-incoming translation-rule

Captures calls that originate from H.323-compatible clients.

## translation-profile (dial peer)

To assign a translation profile to a dial peer, use the translation - profile command in dial peer configuration mode. To delete the translation profile from the dial peer, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing } name

### Syntax Description

incoming

Specifies that this translation profile handles incoming calls.

outgoing

Specifies that this translation profile handles outgoing calls.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

12.4(22)T

Support for IPv6 was added.

### Usage Guidelines

Use the translation - profile command to assign a predefined translation profile to a dial peer.

## Examples

The following example assigns the translation profile named "profile1" to handle translation of outgoing calls for a dial
                              peer:

```
Router(config)# dial-peer voice 111 pots Router(config-dial-peer)# translation-profile outgoing profile1
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation rule.

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translation-profile (source group)

To assign a translation profile to a source IP group, use the translation - profile command in source group configuration mode. To delete the translation profile from the source IP group, use the no form of this command.

translation-profile incoming name

no translation-profile incoming name

### Syntax Description

incoming

Specifies that this translation profile handles incoming calls.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Source group configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the translation - profile command to assign a predefined translation profile to a source IP group.

## Examples

The following example assigns the translation profile named "chicago" to handle translation of incoming calls for a voice
                              source group:

```
Router(config)# voice source-group alpha Router(cfg-source-grp)# translation-profile incoming chicago
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation rule.

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translation-profile (trunk group)

To assign a translation profile to a trunk group, use the translation - profile command in trunk group configuration mode. To delete the translation profile from the trunk group, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing } name

### Syntax Description

incoming

Specifies that this translation profile handles incoming calls.

outgoing

Specifies that this translation profile handles outgoing calls.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Trunk group configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the translation - profile command to assign a predefined translation profile to a trunk group.

## Examples

The following example assigns the translation profile named "newyork" to handle translation of incoming calls for a trunk
                              group:

```
Router(config)# trunk group 10
Router(config-trunk-group)# translation-profile incoming newyork
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation rule.

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translation-profile (voice port)

To assign a translation profile to a voice port, use the translation - profile command in voice port configuration mode. To delete the translation profile from the voice port, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing } name

### Syntax Description

incoming

Specifies that this translation profile handles incoming calls.

outgoing

Specifies that this translation profile handles outgoing calls.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Voice port configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the translation - profile command to assign a predefined translation profile to a voice port.

## Examples

The following example assigns the translation profile named "chicago" to handle translation of incoming calls and a translation
                              profile named "sanjose" to handle outgoing calls for a voice port:

```
Router(config)# voice-port 1/0/0
Router(config-voiceport)# translation-profile incoming chicago Router(config-voiceport)# translation-profile outgoing sanjose
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation rule.

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translation-profile (voice service POTS)

To assign a translation profile to a non-facility associated signaling (NFAS) interface, use the translation - profile command in voice service POTS configuration mode. To delete the translation profile from the interface, use the no form of this command.

translation-profile [ incoming | outgoing ] controller [ T1 | E1 ] unit-number name

no translation-profile [ incoming | outgoing ] controller [ T1 | E1 ] unit-number name

### Syntax Description

incoming

Specifies that this translation profile handles incoming calls.

outgoing

Specifies that this translation profile handles outgoing calls.

T1

T1 controller.

E1

E1 controller.

unit-number

Number of the controller unit.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Voice service POTS configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the translation - profile command to assign a predefined translation profile to an NFAS interface.

## Examples

The following example assigns to an NFAS interface the translation profile named "delta1" to outgoing T1 calls on controller
                              slot 3 and translation profile "alpha" to incoming T1 calls on controller slot 2:

```
Router(config)# voice service pots Router(conf-voi-serv)# translation-profile outgoing controller T1 3 delta1 Router(conf-voi-serv)# translation-profile incoming controller T1 2 alpha
```

### Related Commands

Command

Description

rule (voice translation-rule)

Sets the criteria for the translation rule.

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Initiates the translation-profile definition.

voice translation-rule

Initiates the translation-rule definition.

## translation-rule

To create a translation name and enter translation-rule configuration mode to apply rules to the translation name, use the translation - rule command in global configuration mode. To disable the translation rule, use the no form of this command.

translation-rule name-tag

no translation-rule name-tag

### Syntax Description

name - tag

Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(7)XR1

This command was introduced for VoIP on Cisco AS5300.

12.0(7)XK

This command was implemented for the following voice technologies on the following platforms:

VoIP Cisco 2600 series, Cisco 3600 series, and Cisco MC3810

VoFR Cisco 2600 series, Cisco 3600 series, and Cisco MC3810

VoATM Cisco 3600 series and Cisco MC3810

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T and implemented for the following voice technology on the following
                                          platforms: VoIP (Cisco 1750, Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco 7200 series, and Cisco 7500 series)

12.1(2)T

This command was integrated ino Cisco IOS Release 12.1(2)T for the following voice technologies on the following platforms:

VoIP Cisco MC3810

VoFR Cisco 2600 series, Cisco 3600 series, and Cisco MC3810

VoATM Cisco 3600 series and Cisco MC3810

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

This command applies to all translation rules.

## Examples

The following example creates translation rule 21 and applies a rule to it:

```
translation-rule 21 rule 1 555.% 1408555 subscriber international
```

### Related Commands

Command

Description

numbering-type

Specifies number type for the VoIP or POTS dial peer.

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

test translation-rule

Tests the execution of the translation rules on a specific name tag.

translate

Applies a translation rule to a calling party number or a called party number for incoming calls.

translate-outgoing

Applies a translation rule to a calling party number or a called party number for outgoing calls.

voip-incoming translation-rule

Captures calls that originate from H.323-compatible clients.

## transport (sip-ua)

To configure the Session Initiation Protocol (SIP) user agent (gateway) for SIP signaling messages on inbound calls through
                              the SIP TCP, Transport Layer Security (TLS) over TCP, or User Datagram Protocol (UDP) socket, use the transport command in SIP user agent configuration mode. To block reception of SIP signaling messages on a particular socket, use the no form of this command.

transport { tcp [ tls [ v1.0 | v1.1 | v1.2 [ minimum ]
                              										
                              										 | v1.3 ]
                              								]
                              							
                              							 | udp }

no transport { tcp [ tls [ v1.0 | v1.1 | v1.2 [ minimum ]
                              										
                              										 | v1.3 ]
                              								]
                              							
                              							 | udp }

default transport { tcp [ tls ]
                              							
                              							 | udp }

### Syntax Description

SIP user agent receives SIP messages on TCP port 5060.

(Optional) SIP user agent receives SIP messages on TLS over TCP port 5061. You can configure TLS version 1.0, 1.1, 1.2, or
                                          1.3.

Starting from Cisco IOS XE 26.1.1 release, insecure TLS versions and ciphers are not supported in default configurations. However, these insecure configurations
                                          are supported in "system mode insecure" operation-mode.

(Optional) Specifies minimum configured TLS version. The minimum keyword can be configured only with TLS version 1.2. This configuration enables TLS versions 1.2 and 1.3.

SIP user agent receives SIP messages on UDP port 5060.

### Command Default

TCP, TLS over TCP, and UDP transport protocols are enabled.

### Command Modes

SIP user-agent configuration (config-sip-ua)

## Command History

Release

Modification

Cisco IOS XE 26.1.1

This command is modified with the removal of insecure TLS versions (1.0, 1.1) and associated ciphers from default configurations.
                                          Support for insecure configurations in "system mode insecure" operation-mode.

Cisco IOS XE 17.18.2

Security warnings for usage of legacy TLS and associated weaker ciphers.

This command is modified to include the TLS version 1.3 support. In addition, minimum keyword configuration support is introduced with TLS version 1.2.

Introduced support for the following YANG models:

transport tcp tls v1.3

transport tcp tls v1.2 minimum

Introduced support for YANG models.

15.6(1)T and 3.17S

This command was modified to include the TLS version 1.2.

12.4(6)T

The optional TLS keyword was added to the command.

12.2(11)T

Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms in this release.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco 7200 series routers. Support for the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms were not included in this release.

12.2(2)XB1

This command was implemented on Cisco AS5850 platforms.

12.2(2)XA

This command was implemented on Cisco AS5400 and Cisco AS5350 platforms.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

12.1(1)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300 platforms.

### Usage Guidelines

This command controls whether messages reach the SIP service provider interface (SPI). Setting tcp , or tls over tcp , or udp as the protocol for the SIP user agents to listen on port 5060.

To block reception of SIP signaling messages on a specific socket, use the no form of this command.

To reset this command to the default value, use the default form of this command.

In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                          For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher.

Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                          insecure configurations are allowed in "system mode insecure" operation-mode. The following are the insecure ciphers associated
                                          with TLS versions (1.0, 1.1):

DHE_RSA_WITH_AES_128_CBC_SHA

RSA_WITH_AES_128_CBC_SHA

RSA_WITH_AES_256_CBC_SHA

## Examples

The following example sets the SIP user agent to allow the reception of SIP signaling messages on the UDP socket:

```
sip-ua transport udp
```

## Examples

The following example sets the SIP user agent to allow the reception of SIP signaling messages on the TCP socket:

```
sip-ua transport tcp
```

## Examples

The following example sets the SIP user agent to allow the reception of SIP signaling messages on the TLS over TCP socket:

```
sip-ua transport tcp tls v1.0  Enable TLS Version 1.0 v1.1  Enable TLS Version 1.1 v1.2  Enable TLS Version 1.2 v1.3  Enable TLS Version 1.3
```

## Examples

The following example sets the SIP user agent to TLS version 1.2  as minimum, enabling both TLS versions 1.2 and 1.3:

```
sip-ua transport tcp tls v1.2 minimum
```

## Examples

The following example illustrates a security warning message display in Cisco IOS XE 17.18.2 release for configurations using TLS versions below 1.2:

```
Device(config-sip-ua)# transport tcp tls v1.0 SECURITY WARNING - Module: SIPUA, Command: transport tcp tls v1.0, Reason: Weak tls version, 
Remediation: Use stronger tls version to enhance security

Device(config-sip-ua)# do sh run | sec sip-ua sip-ua 
 no remote-party-id
 timers connect 501
 timers dns registrar-cache 60
 transport tcp tls v1.0
 registration spike 100
 connection-reuse
  crypto signaling remote-addr 10.10.10.70 255.255.255.255  trustpoint CUBE-TLS strict-cipher  
alias exec tcp show sip-ua connections tcp tls detail
```

## Examples

The following example illustrates weaker TLS versions (1.0, 1.1) configuration in insecure mode with warning message display,
                              starting from Cisco IOS XE 26.1.1 release:

```
Device# configure terminal Device(config)# system mode insecure Device(config)# sip-ua Device(config-sip-ua)# transport tcp tls v1.1 SECURITY WARNING - Module: SIPUA, Command: transport tcp tls v1.0, Reason: Weak tls version, 
Remediation: Use stronger tls version to enhance security
```

## Examples

The following example illustrates weaker TLS versions (1.0, 1.1) configuration in secure mode with error message display,
                              starting from Cisco IOS XE 26.1.1 release:

```
Device(config-sip-ua)# transport tcp tls v1.1 %Error:Insecure configurations are not permitted in secure mode. To proceed, set the system mode to insecure 
using the command system mode insecure, and then try again.
Module: SIPUA, Command: transport tcp tls v1.1 , Reason: Weak tls version, Remediation: Use stronger tls version
to enhance security
%ERROR: Security policy check failed, configuration can't be applied
```

### Related Commands

Command

Description

sip-ua

Enables the SIP user agent configuration commands.

## transport switch

To enable switching between UDP and TCP transport mechanisms globally for large Session Initiation Protocol (SIP) messages,
                              use the transport switch command in SIP configuration mode. To disable switching between UDP and TCP transport mechanisms globally for large SIP messages,
                              use the no form of this command.

transport switch udp tcp

no transport switch udp tcp

### Syntax Description

udp

Enables switching the transport mechanism from UDP on the basis of the size of the SIP request being greater than the MTU
                                          size.

tcp

Enables switching transport to TCP.

### Command Default

Disabled.

### Command Modes

SIP configuration

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

Switching between transports is provided globally on the router and also on an individual VoIP dial peer.

Dial-peer mode. You can configure transport for a specific dial peer by using the voice - class sip transport switch command. The voice - class sip transport switch command in dial-peer configuration mode takes precedence over the transport switch command in global configuration mode.

SIP mode. You can configure transport globally by using the transport switch command. The transport switch command is considered only when there is no matching VoIP dial peer.

In a call forking scenario, if this command is configured, the configuration applies to all forks.

## Examples

The following example enables switching of the transport from UDP to TCP:

```
Router(config)# voice service voip Router(config-voi-srv)# sip Router(conf-serv-sip)# transport switch udp tcp
```

### Related Commands

Command

Description

debug ccsip transport

Enables tracing of the SIP transport handler and the TCP or UDP process.

sip

Enters SIP configuration mode from voice-service VoIP configuration mode.

voice - class sip transport switch

Enables switching between transport mechanisms if the SIP message is larger than 1300 bytes for a specific dial peer.

## trunk group (global)

To define or modify the definition of a trunk group and to enter trunk group configuration mode, use the trunk group command in global configuration mode. To delete the trunk group, use the no form of this command.

trunk group name

no trunk group name

### Syntax Description

name

Name of the trunk group. Valid names contain a maximum of 63 alphanumeric characters.

### Command Default

No trunk group is defined.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced.

### Usage Guidelines

Use the trunk group command to assign a number or a name to a set of trunk characteristics. The set of characteristics, or profile , is assigned to specific trunks as part of the usual trunk configuration steps.

The trunk group command initiates the profile definition and switches from global configuration to trunk group configuration mode. Additional
                              commands are available to construct the characteristics of the profile.

Up to 1000 trunk groups can be configured on the gateway provided that the gateway has sufficient memory to store the profiles.
                              If you see the message "Trunk group name could not be added as the threshold has been reached", enter the debug tgrm command and check the number of trunk groups or check for insufficient memory.

To associate a trunk group with an interface, use the trunk-group (interface) command. A trunk group that was created using the trunk group (global) command can be associated with an interface. However, a trunk group need not be defined globally before being associated
                              with an interface. If a trunk group has not been defined globally, it will be created by issuing the trunk-group (interface) command.

## Examples

The following example creates trunk group 5 and configures the trunk group profile:

```
Router(config)# trunk group 5 Router(config-trunk-group)# carrier-id allcalls Router(config-trunk-group)# max-calls voice 500 in Router(config-trunk-group)# hunt-scheme round-robin even up Router(config-trunk-group)# translation-profile incoming 3 Router(config-trunk-group)# translation-profile outgoing 2 Router(config-trunk-group)# exit
```

The following example creates a trunk group named "mytrunk" and configures the trunk group profile:

```
Router(config)# trunk group mytrunk Router(config-trunk-group)# carrier-id local Router(config-trunk-group)# max-calls voice 500 Router(config-trunk-group)# hunt-scheme least-idle Router(config-trunk-group)# translation-profile incoming 1 Router(config-trunk-group)# translation-profile outgoing 12 Router(config-trunk-group)# exit
```

### Related Commands

Command

Description

carrier-id (trunk group)

Identifies the carrier that owns the trunk group.

description (trunk group)

Permits a description to be associated with a trunk group.

hunt-scheme least-idle

Specifies the least-idle channel search method for incoming and outgoing calls.

hunt-scheme least-used

Specifies the least-used channel search method for incoming and outgoing calls.

hunt-scheme longest-idle

Specifies the longest-idle channel search method for incoming and outgoing calls.

hunt-scheme random

Specifies the random channel search method for incoming and outgoing calls.

hunt-scheme round-robin

Specifies the round-robin channel search method for incoming and outgoing calls.

hunt-scheme sequential

Specifies the sequential channel search method for incoming and outgoing calls.

max-calls

Specifies the number of incoming and outgoing voice and data calls that a trunk group can handle.

show trunk group

Displays the configuration of trunk groups.

translation-profile (trunk group)

Defines call number translation profiles for incoming and outgoing calls.

trunk-group (interface)

Assigns an ISDN PRI or NFAS interface to a trunk group.

## trunk-group (CAS custom)

To assign a channel-associated signaling (CAS) trunk to a trunk group, use the trunk - group command in CAS custom configuration mode. To delete the CAS trunk from the trunk group, use the no form of this command.

trunk-group name [preference-num]

no trunk-group name [preference-num]

### Syntax Description

name

Name of the trunk group. Maximum length of the trunk group name is 63 alphanumeric characters.

preference - num

(Optional) Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority).

### Command Default

Preference-num is set lower than 64 (internally set to 65)

### Command Modes

CAS custom configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the trunk - group command to assign a CAS trunk as a member of a trunk group. This assignment provides the CAS trunk with carrier information,
                              a hunt scheme for finding an available channel for the outgoing call, and translation profiles for number translation.

If more than one CAS trunk is assigned to the same trunk group, the preference - num value determines the order in which the trunk group uses the interfaces. A preference - num value of 1 is the highest preference so that the trunk is used first; a value of 64 is the lowest preference so that the
                              trunk is used last. If no value is entered for preference - num , the software assigns the trunk a preference of 65, which causes that trunk to be used after all other trunks are used.

If two CAS trunks have the same preference - num , the trunk that was configured first is used before the other trunk.

A CAS trunk can belong to only one trunk group.

If an interface is removed from the CAS trunk, the interface is removed automatically from the trunk group. A new nonprimary
                              CAS interface is automatically a member of the same trunk group as its primary CAS interface.

## Examples

The following example assigns two CAS interfaces to trunk group "westcoast". The preference value for DS0 group 2 is lower
                              than for DS0 group 1; hence DS0 group 2 has a higher priority. Trunk group "westcoast" uses DS0 group 2 first.

```
Router(config)# controller T1 1/0 Router(config-controller)# ds0-group 1 timeslots 1-10 type e&m-fgd Router(config-controller)# cas-custom 1 Router(config-controller)# trunk-group westcoast 5 Router(config-controller)# exit Router(config)# controller T1 1/0 Router(config-controller)# ds0-group 2 timeslots 15-20 type e&m-fgd Router(config-controller)# cas-custom 2 Router(config-controller)# trunk-group westcoast 3 Router(config-controller)# exit
```

### Related Commands

Command

Description

show trunk group

Displays the configuration of a trunk group.

## trunkgroup (dial peer)

To assign a dial peer to a trunk group for trunk group label routing, use the trunkgroup command in dial-peer configuration mode. To delete the dial peer from the trunk group, use the no form of this command.

trunkgroup name preference-num

no trunkgroup name

### Syntax Description

name

Label of the trunk group to use for the call. Valid trunk group names contain a maximum of 63 alphanumeric characters.

preference - num

Preference or priority of the trunk group. Range is from 1 (highest priority) to 64 (lowest priority).

### Command Default

Preference-num is set lower than 64 (internally set to 65)

### Command Modes

Dial peer configuration (config dial-peer)

## Command History

Release

Modification

12.1(3)T

This command was introduced.

12.2

This command was integrated into the Cisco IOS Release 12.2.

12.2(11)T

The preference - num argument was added.

### Usage Guidelines

Use the trunkgroup command to assign an outgoing dial peer as a member of one or more trunk groups. This assignment provides the dial peer with
                              carrier information, a hunt scheme for finding an available channel for the outgoing call, and translation profiles for number
                              translation.

If the dial peer is a member of more than one trunk group, use the preference - num value to set the order in which the trunk groups will be used for the dial peer. A preference - num value of 1 is the highest preference so that the trunk group is used first; a value of 64 is the lowest preference so that
                              the trunk group is used last. If no value is entered for preference - num , the software assigns the trunk group a preference of 65, which causes that trunk group to be selected after all other trunks
                              are used.

If two trunk groups have the same preference - num , the trunk group that was configured first is used before the other trunk group.

## Examples

In the following example, dial peer 112 should use the trunk group "east17" and trunk group "north5" for outbound dial peer
                              matching. When selecting a trunk group, "north5" is used first because it has a higher preference than "east17":

```
Router(config)# dial-peer voice 112 pots Router(config-dial-peer)# trunkgroup east17 3 Router(config-dial-peer)# trunkgroup north5 1
```

### Related Commands

Command

Description

debug dialpeer

Initiates dial peer debugging.

show dial-peer voice

Displays the dial peer configuration.

translation-profile (dial peer)

Defines call number translation profiles for incoming and outgoing calls.

## trunk-group (interface)

To assign an ISDN PRI or Non-Facility Associated Signaling (NFAS) interface to a trunk group, use the trunk - group command in interface configuration mode. To delete the interface from the trunk group, use the no form of this command.

trunk-group name [preference-num]

no trunk-group name [preference-num]

### Syntax Description

name

Name of the trunk group. Valid trunk group names contain a maximum of 63 alphanumeric characters.

preference - num

Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority).

### Command Default

Preference-num is set lower than 64 (internally set to 65)

### Command Modes

Interface configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced.

12.2

This command was integrated into Cisco IOS Release 12.2.

12.2(11)T

The trunk-group identification was expanded to include alphanumeric characters using the name argument, and the preference-num argument was added.

### Usage Guidelines

Use the trunk - group command to configure an ISDN PRI or Non-Facility Associated Signaling (NFAS) interface as a member of a trunk group. This
                              assignment provides the interface with carrier information, a hunt scheme for finding an available channel for the outgoing
                              call, and translation profiles for number translation.

If more than one interface is assigned to the same trunk group, the preference_num value determines the order in which the trunk group uses the interfaces. A preference - num value of 1 is the highest preference so that the interface is used first; a value of 64 is the lowest preference so that
                              the interface is used last. If no value is entered for preference - num , the software assigns the interface a preference of 65, which causes that interface to be selected after all other interfaces
                              are used.

If two interfaces have the same preference - num , the interface that was configured first is used before the other interface.

An interface can belong to only one trunk group. Multiple interfaces can belong to the same trunk group.

If an NFAS interface group is assigned as a member of a trunk group, all the subinterfaces belong to that trunk group.

If a subinterface is removed from the NFAS group, the subinterface is removed automatically from the trunk group.

If a new nonprimary NFAS interface is added to the NFAS group, that interface automatically becomes a member of the same trunk
                              group as its primary NFAS interface.

## Examples

The following example assigns an ISDN interface to trunk group "eastern" with a preference of 3.

```
Router(config)# interface Serial2:23 Router(config-if)# no ip address Router(config-if)# isdn switch-type primary-ni Router(config-if)# isdn T306 30000 Router(config-if)# isdn T310 10000 Router(config-if)# no cdp enable Router(config-if)# trunk-group eastern 3 Router(config-if)# exit
```

If another interface were assigned to trunk group "eastern" with preference of 1 or 2, the trunk group would use that interface
                              before the one shown above.

### Related Commands

Command

Description

show trunk group

Displays the configuration of the trunk group.

## trunk-group (voice port)

To assign an analog voice port to a trunk group, use the trunk - group command in voice port configuration mode. To delete the trunk group, use the no form of this command.

trunk-group name [preference-num]

no trunk-group name [preference-num]

### Syntax Description

name

Name of the trunk group. Maximum length of the trunk group name is 63 alphanumeric characters.

preference - num

Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority).

### Command Default

Preference-num is set lower than 64 (internally set to 65)

### Command Modes

Voice port configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the trunk - group command to configure an analog voice port as a member of a trunk group. This assignment provides the voice port with carrier
                              information, a hunt scheme for finding an available channel for the outgoing call, and translation profiles for number translation.

If more than one voice port is assigned to the same trunk group, the preference - num value determines the order by which the trunk group uses the voice ports. A preference - num value of 1 is the highest preference so that the voice port is used first; a value of 64 is the lowest preference so that
                              the voice port is used last. If no value is entered for preference - num , the software assigns the voice port a preference of 65, which causes that voice port to be selected after all other voice
                              ports are used.

If two voice ports have the same preference - num , the voice port that was configured first is used before the other voice port.

A voice port can belong to only one trunk group. Multiple voice ports can belong to the same trunk group.

## Examples

The following example assigns voice port 1/0/0 and voice port 1/0/1 to trunk group "north5". Trunk group "north5" uses voice
                              port 1/0/1 before using voice port 1/0/0 because voice port 1/0/1 has preference 1, which is a higher priority than voice
                              port 1/0/0, with preference 2.

```
Router(config)# voice port 1/0/0 Router(config-voiceport)# translation-profile incoming 7 Router(config-voiceport)# translation-profile outgoing 4 Router(config-voiceport)# trunk-group north5 2 Router(config-voiceport)# exit Router(config)# voice port 1/0/1 Router(config-voiceport)# translation-profile incoming 3 Router(config-voiceport)# translation-profile outgoing 8 Router(config-voiceport)# trunk-group north5 1 Router(config-voiceport)# exit
```

### Related Commands

Command

Description

show trunk group

Displays the configuration of a trunk group.

## trunk-group-label (dial peer)

To specify a trunk group as the source or target of a call, use the trunk - group - label command in dial peer configuration mode. To delete the trunk group label, use the no form of this command.

trunk-group-label { source | target } name

no trunk-group-label { source | target } name

### Syntax Description

source

Indicates the trunk group as the source of the incoming call.

target

Indicates the trunk group as the target of the outbound call.

name

Trunk group label. Maximum length of the trunk group label is 127 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration (config dial-peer)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

An originating gateway uses the source trunk group label as a matching key to route the call over an inbound dial peer. The
                              terminating gateway uses the target trunk group label to select a dial peer for routing the outbound call over a POTS line.

If a dial peer has a source (or target) carrier ID already defined, then assigning a source (or target) trunk group label
                              to that same dial peer overrides the source (or target) carrier ID. The same is true for the reverse: if a dial peer has a
                              source (or target) trunk group label defined, then assigning a source (or target) carrier ID for that same dial peer overrides
                              the source (or target) trunk group label.

The name of a trunk group label and carrier ID cannot be the same in dial peers.

## Examples

The following example shows that dial peer 112 should use trunk group label "north3" for inbound dial peer matching and trunk
                              group label "east17" for outbound dial peer matching:

```
Router(config)# dial-peer voice 112 pots Router(config-dial-peer)# trunk-group-label source north3 Router(config-dial-peer)# trunk-group-label target east17
```

### Related Commands

Command

Description

carrier-id (dial peer)

Specifies the carrier associated with a VoIP call.

show dial-peer voice

Displays configuration information for dial peers.

## trunk-group-label (voice source group)

To define a trunk group label in a source IP group, use the trunk - group - label command in voice source group configuration mode. To delete the trunk group label, use the no form of this command.

trunk-group-label { source | target } name

no trunk-group-label { source | target } name

### Syntax Description

source

Indicates the trunk group as the source of the incoming call.

target

Indicates the trunk group as the target of the outbound call.

name

Trunk group label. Maximum length of the trunk group label is 127 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Voice source group configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

A terminating gateway uses the source trunk group label as a search key to find a source IP group for the incoming VoIP call.
                              The gateway uses the target trunk group label to select an outbound dial peer to route the call over a POTS line.

If a source IP group has a source (or target) carrier ID already defined, then assigning a source (or target) trunk group
                              label to that same source IP group overrides the source (or target) carrier ID. The same is true for the reverse: if a source
                              IP group has a source (or target) trunk group label defined, then assigning a source (or target) carrier ID for that same
                              source IP group overrides the source (or target) trunk group label.

The name of a trunk group label and carrier ID of the same type (source or target) cannot be the same in the source IP group.

## Examples

The following example shows that source IP group "alpha" uses trunk group "north3" to search for a source IP group for incoming
                              VoIP calls and trunk group "east17" for outbound dial peer matching:

```
Router(config)# voice source-group alpha Router(cfg-source-grp)# trunk-group-label source north3 Router(cfg-source-grp)# trunk-group-label target east17
```

### Related Commands

Command

Description

carrier-id (dial-peer)

Specifies the carrier associated with a VoIP call.

show voice source-group

Displays the configuration for voice source IP groups.

## trustpoint (DSP farm profile)

To associate a trustpoint with a DSP farm profile, use the trustpoint command in DSP farm profile configuration configuration mode. To remove the association, use the no form of this command.

trustpoint trustpoint-label

no trustpoint trustpoint-label

### Syntax Description

trustpoint-label

Label of the trustpoint to be associated with the digital signal processor (DSP) farm profile.

### Command Default

No trustpoints are associated with the DSP farm profile

### Command Modes

DSP farm profile configuration (config-dspfarm-profile)

## Command History

Release

Modification

12.4(11)XW1

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

Use this command to associate trustpoints with secure DSP farm profiles only. Use the security keyword of the dspfarm profile command to configure a secure DSP farm profile. If the trustpoint is not already configured, you are prompted to configure
                              the trustpoint.

## Examples

The following example associates the trustpoint dspfarm with the DSP farm profile 101:

```
Router(config)# dspfarm profile 101 conference security Router(config-dspfarm-profile)# trustpoint dspfarm
```

### Related Commands

Command

Description

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for digital signal processor (DSP) farm services.

## trustpoint (voice class)

To configure a trustpoint, and associate it to a TLS profile, use the trustpoint command in voice class configuration mode. To delete the trustpoint, use the no form of this command.

trustpoint trustpoint-name [ client client-trustpoint-name ]

no trustpoint

### Syntax Description

trustpoint-name

trustpoint trustpoint-name —creates a trustpoint to store the devices certificate
                                          generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands.

client client-trustpoint-name

(Optional) Associate a client trustpoint​. Specify the client trustpoint label​.

### Command Default

No default behavior or values

### Command Modes

Voice class configuration (config-class)

## Command History

Release

Modification

Cisco IOS XE Amsterdam 17.3.1a

This command was introduced under voice class configuration
                                          mode.

Introduced support for Yang Model.

Cisco IOS XE 26.1.1

This command was modified to allow provisioning and assigning separate certificates for client and server roles on each SIP
                                          trunk in CUBE.

### Usage Guidelines

The trustpoint is associated to a TLS profile through the command voice class tls-profile tag . The tag associates the trustpoint configuration to the command crypto signaling .

Starting from Cisco IOS XE 26.1.1 release, you can configure client trustpoint along with existing trustpoint configuration under voice class tls profile . The client trustpoint is used for TLS client authentication. If client trustpoint is not configured then it'll fallback
                              to common trustpoint .

## Examples

The following example illustrates how to create a voice class tls-profile and
                              associate a trustpoint to be used by Cisco UBE to establish a connection with a
                              remote device:

```
Router(config)#voice class tls-profile 2
Router(config-class)#trustpoint CUBETP
```

## Examples

The following is a sub option to configure client trustpoint along with existing trustpoint config under voice class tls profile :

```
Router(config)#voice class tls-profile 1 ​
Router(config-class)#trustpoint  CUBE_TP client Client_TP
```

### Related Commands

Command

Description

voice class tls-profile

Provides sub-options to configure the commands that are required for a TLS session.

crypto signaling

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process.

## ttl

To set the expiration timer for advertisements, enter the ttl command in Annex G configuration mode. To reset to the default, use the no form of this command.

ttl ttl-value

no ttl

### Syntax Description

ttl - value

Amount of time (in seconds) for which a route from a neighbor is considered valid. Range is from 1 to 2147483647. The default
                                          is 1800 (or 30 minutes).

### Command Default

1800 seconds (30 minutes)

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

This command was implemented on Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

The address templates or routes that are static to this Annex G border element (BE) can be advertised to its neighbors. A
                              time-to-live (TTL) value is associated with each of the advertised routes. The TTL value indicates how long the neighbor should
                              consider the routes valid. On expiration of the ttl, the neighbor must query the addressing information again.

## Examples

The following example shows a BE with a time-to-live value of 20 seconds.

```
Router(config)# call-router h323-annexg be20 Router(config-annexg)# ttl 20
```

### Related Commands

Command

Description

call - router

Enables the Annex G BE configuration commands.

show call - router status

Displays the Annex G BE status.

## type (settlement)

To point to the provider type and the specific settlement server, use the type command in settlement configuration mode. To disable this command, use the no form of this command.

type { osp | uni-osp }

no type

### Syntax Description

osp

Enables the Open Settlement Protocol (OSP) server type.

uni - osp

Enables authentication of VoIP calls to the Public Switched Telephone Network (PSTN) using a single settlement server.

### Command Default

osp

### Command Modes

Settlement configuration

## Command History

Release

Modification

12.0(4)XH1

This command was introduced on Cisco 2600 series and Cisco 3600 series, and Cisco AS5300.

12.1(2)T

The uni-osp keyword was introduced.

### Usage Guidelines

This command defines the settlement server that is doing the accounting and enables the server to do the accounting.

## Examples

The following example enables authentication of VoIP calls to the PSTN using a single settlement server:

```
settlement 0
 type uni-osp
```

### Related Commands

Command

Description

connection - timeout

Sets the connection timeout.

customer - id

Sets the customer identification.

device - id

Sets the device identification.

encryption

Specifies the encryption method.

max - connection

Sets the maximum simultaneous connections.

response - timeout

Sets the response timeout.

retry - delay

Sets the retry delay.

retry - limit

Sets the connection retry limit.

session - timeout

Sets the session timeout.

settlement

Enters settlement configuration mode.

show settlement

Displays the configuration for all settlement server transactions.

shutdown/no shutdown

Brings up the settlement provider and then shuts it down.

url

Specifies the Internet service provider (ISP) address.

## type (voice)

To specify the E&M interface type, use the type command in voice-port configuration mode. To reset to the default, use the no form of this command.

type { 1 | 2 | 3 | 5 }

no type { 1 | 2 | 3 | 5 }

### Syntax Description

1

Indicates the following lead configuration:

E--Output, relay to ground.

M--Input, referenced to ground.

2

Indicates the following lead configuration:

E--Output, relay to SG.

M--Input, referenced to ground.

SB--Feed for M, connected to -48V.

SG--Return for E, galvanically isolated from ground.

3

Indicates the following lead configuration:

E--Output, relay to ground.

M--Input, referenced to ground.

SB--Connected to -48V.

SG--Connected to ground.

5

Indicates the following lead configuration:

E--Output, relay to ground.

M--Input, referenced to -48V.

### Command Default

Type 1

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on Cisco 3600 series routers.

11.3(1)MA

This command was implemented on Cisco MC3810.

### Usage Guidelines

Use the type command to specify the E&M interface for a particular voice port. With 1 , the tie-line equipment generates the E-signal to the PBX type grounding the E-lead. The tie-line equipment detects the M-signal
                              by detecting current flow to ground. If you select 1 , a common ground must exist between the line equipment and the PBX.

With 2 , the interface requires no common ground between the equipment, thereby avoiding ground loop noise problems. The E-signal
                              is generated toward the PBX by connecting it to SG. The M-signal is indicated by the PBX connecting it to SB. While Type 2
                              interfaces do not require a common ground, they do have the tendency to inject noise into the audio paths because they are
                              asymmetrical with respect to the current flow between devices.

E&M Type 4 is not a supported option. However, Type 4 operates similarly to Type 2 except for the M-lead operation. On Type
                                          4, the M-lead states are open/ground, compared to Type 2, which is open/battery. Type 4 can interface with Type 2. To use
                                          Type 4 you can set the E&M voice port to Type 2 and perform the necessary M-lead rewiring.

With 3 , the interface operates the same as Type 1 interfaces with respect to the E-signal. The M-signal, however, is indicated by
                              the PBX connecting it to SB on assertion and alternately connecting it to SG during inactivity. If you select 3 , a common ground must be shared between equipment.

With 5 , the Type 5 line equipment indicates E-signal to the PBX by grounding the E-lead. The PBX indicates M-signal by grounding
                              the M-lead. A Type 5 interface is quasi-symmetrical in that while the line is up, current flow is more or less equal between
                              the PBX and the line equipment, but noise injection is a problem.

## Examples

The following example selects Type 3 as the interface type for the voice port:

```
voice-port 1/0/0
 type 3
```

| time | Delay signal duration for delay dial signaling, in milliseconds. Range is from 100 to 5000. The default is 2000. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
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

| time | Minimum delay time, in milliseconds, from outgoing seizure to outdial address. Range is from 20 to 2000. The default on the Cisco 3600 series is 300. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series routers. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
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

| milliseconds | Duration, in milliseconds, of the timing delay. Range is integers from 1 to 1500. Default is 0. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.3(14)T | This command was implemented on the Cisco 2800 series and Cisco 3800 series. |
| 12.4(2)T | This command was integrated into Cisco IOS Release 12.4(2)T. |

| Command | Description |
|---|---|
| inject pause | Specifies a pause between injected tones. |
| inject tone | Specifies a wakeup or frequency selection tone to be played out before the voice packet. |

| time | Duration of the wink pulse for the delay dial, in milliseconds. Range is from 0 to 5000. The default is 0. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Dial-out delay, in milliseconds, for the sending digit or cut-through on a Foreign Exchange Office (FXO) trunk or an E&M immediate
                                          trunk. Range is from 100 to 5000. The default is 300. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on Cisco MC3810. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Time between wink-like pulses, in milliseconds. Range is from 0 to 5000. The default is 300. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | The DTMF digit signal duration, in milliseconds. Range is 5 from 0 to 100. The default is 100. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Duration of the guard-out period, in milliseconds. The range is from 300 to 3000. The default is 2000. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on Cisco MC3810. |
| 12.0(7)XK | This command was implemented on Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| milliseconds | The number of milliseconds for which the E-lead stays active after VAD determines that the voice stream has stopped. Valid
                                          values are 0 to 10000. The default is 250 milliseconds. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| milliseconds | Upper limit of the hookflash duration range, in milliseconds. E&M voice ports--Range is 0 to 1550 milliseconds. Default is 480 milliseconds. FXS voice ports--Range is 50 to 1550 milliseconds. Default is 1000 milliseconds. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco 3600 series. |
| 12.3(7)T | Lower limit of the range for E&M voice ports was extended to 0 milliseconds. |
| 12.3(14)T | This command was implemented on the Cisco 2800 series and Cisco 3800 series. |
| 12.4(2)T | This command was integrated into Cisco IOS Release 12.4(2)T. |

| Command | Description |
|---|---|
| dtmf-relay (Voice over IP) | Specifies how an H.323 gateway relays DTMF tones between telephony interfaces and an IP network. |

| time | Duration of the hookflash, in milliseconds. Range is from 50 to 1550. The default is 400 milliseconds. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on Cisco 2500, Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco MC3810. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |

| Command | Description |
|---|---|
| dtmf-relay (Voice over IP) | Specifies how an H.323 gateway relays DTMF tones between telephony interfaces and an IP network. |
| voice-port | Enters voice-port configuration mode. |

| milliseconds | The number of milliseconds following the sending of the E-lead off signal for which the M-lead and VAD changes are ignored.
                                          Valid values are 0 to 10000. The default is 0 milliseconds. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| time | DTMF interdigit duration, in milliseconds. Range is from 50 to 500. The default is 100. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |
| 11.3(1)MA | This command was supported on Cisco MC3810. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| msecs | Maximum duration, in milliseconds, to wait for the next ring. Range is 2000 to 10000. Default is 6000. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice-port | Enters voice-port configuration mode. |
| show voice port | Displays configuration information about a specific voice port. |

| percent | Percentage of the break period for dialing pulses. Range is from 20 to 80. The default is 50. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA4 | This command was introduced on Cisco MC3810. |
| 12.0(7)XK | This command was implemented on Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| timing pulse | Configures the pulse dialing rate for a voice port. |
| timing pulse - interdigit | Configures the pulse interdigit timing for a voice port. |

| pulses - per - second | Pulse dialing rate, in pulses per second. Range is from 10 to 20. The default is 20. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This command was supported on the Cisco MC3810. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Pulse dialing interdigit timing, in milliseconds. Range is from 100 to 1000. The default is 500. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |
| 11.3(1)MA | This command was supported on Cisco MC3810. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing dial-pulse min-delay | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing wink-duration | Specifies the maximum wink signal duration for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| milliseconds | Minimum time, in milliseconds, after detection of an on-hook indication to determine that the on-hook condition is intentional
                                          and then to hang up the POTS call leg. The range is from 50 to 1500. The default is 350. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(12) | This command was introduced. |
| 12.3(11)T6 | This command was integrated into Cisco IOS Release 12.3(11)T6. |
| 12.3(14)T | This command was integrated into Cisco IOS Release 12.3(14)T. |
| 12.4(12) | This command was integrated into Cisco IOS Release 12.4(12). |

| Command | Description |
|---|---|
| show voice port | Displays configuration information about a specific voice port. |
| voice-port | Enters voice-port configuration mode. |

| milliseconds | Maximum time to wait for wink signal after an outgoing seizure is sent. Valid entries are from 100 to 6500 milliseconds (ms). Supported on ear and mouth (E&M) ports only. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series routers. |
| 11.3(1)MA | This command was implemented on Cisco MC3810 multiservice concentrators. |
| 12.4(12) | The millisecond range was extended from 5000 to 6500. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dial-out delay for the sending digit on a specified voice port. |
| timing delay-with-integrity | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Maximum transmit duration, in milliseconds (ms), for a wink-start signal. The range is from 50 to 3000. The default is 200. |
|---|---|
| receive | Indicates that a range is to be specified for a received wink-start signal. |
| minimum | Received minimum wink length, in milliseconds. The range is from 40 to 2950. The default is 140. |
| maximum | Received maximum wink length, in milliseconds. The range is from 150 to 3150. The default is 290. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |
| 11.3(1)MA | This command was integrated into Cisco IOS Release 11.3(1)MA and support was added for the Cisco MC3810. |
| 12.4(13) | This command was integrated into Cisco IOS Release 12.4(13) and the receive keyword and minimum and maximum arguments were added. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
| timing delay-duration | Specifies the delay signal duration for a specified voice port. |
| timing delay-start | Specifies the minimum delay time from outgoing seizure to out-dial address for a specified voice port. |
| timing delay-with-integrity | Specifies the duration of the wink pulse for the delay dial for a specified voice port. |
| timing dialout-delay | Specifies the dialout delay for the sending digit on a specified voice port. |
| timing delay-with-integrity | Specifies the time between wink-like pulses for a specified voice port. |
| timing digit | Specifies the DTMF digit signal duration for a specified voice port. |
| timing interdigit | Specifies the DTMF interdigit duration for a specified voice port. |
| timing percentbreak | Specifies the percentage of a break period for a dialing pulse for a specified voice port. |
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |
| timing pulse-interdigit | Specifies the pulse interdigit timing for a specified voice port. |
| timing wink-wait | Specifies the maximum wink-wait duration for a specified voice port. |

| time | Maximum wink-wait duration, in milliseconds, for a wink start signal. Range is from 100 to 6500. The default is 200. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series. |
| 11.3(1)MA | This command was supported on Cisco MC3810. |
| 12.4(12) | The millisecond range was extended from 5000 to 6500. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| timeouts wait-release | Configures the timeout value for releasing voice ports. |
| timing clear-wait | Indicates the minimum amount of time between the inactive seizure signal and the call being cleared for a specified voice
                                          port. |
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

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 12.4(24)T | This command was integrated into Cisco IOS Release 12.4(24)T. |

| Command | Description |
|---|---|
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for DSP farm services. |

| keypad-character | Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #5. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced. |

| Command | Description |
|---|---|
| conference | Defines FAC in Feature Mode to initiate a three-party conference. |
| drop-last-conferee | Defines FAC in feature mode to use to drop last active call during a three-party conference. |
| hangup-last-active-call | Defines FAC in feature mode to drop last active call during a three-party conferencee. |
| transfer | Defines FAC in feature mode to connect a call to a third party that the phone user dials. |

| name | Certificate identification name as configured with the crypto ca identity name command or the crypto ca trusted-root name command. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on Cisco 2600 series, Cisco 3600 series, Cisco AS5300, and Cisco AS5800. |

| Command | Description |
|---|---|
| crypto ca identity | Declares the Certificate Authority that your router should use. |
| crypto ca trusted - root | Configures the root certificate that the server uses to sign the settlement tokens. |
| show settlement | Displays the configuration for all settlement server transactions. |

| remote-onhook | Generates busy tone after remote onhook in basic call mode. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(20)T | This command was introduced. |

| Note | The tone busytone command cannot coexist with the dialtone generation after remote-onhook feature. Because the tone dialtone is a default configuration, you must disable the feature using the no tone dialtone command before connfiguring the tone busytone command. |
|---|---|

| Command | Description |
|---|---|
| show dial-peer voice | Displays information for voice dial peers. |
| tone dialtone | Enable automatic dial tone generation. |
| show stcapp device voice | Displays configuration information about STCAPP analog voice ports. |

| remote-onhook | Generates dial tone after remote onhook in basic call mode. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(6)XE | This command was introduced. |
| 12.4(11)T | This command was integrated into Cisco IOS Release 12.4(11)T. |

| Command | Description |
|---|---|
| sccp | Enables SCCP and related applications. |
| show dial-peer voice | Displays information for voice dial peers. |
| show stcapp device | Displays configuration information about SCCP Telephony Control Application (STCAPP) analog voice ports. |

| ip | (Optional) Specifies tone detection on the IP side of the network. |
|---|---|
| pstn | (Optional) Specifies tone detection on the PSTN side of the network. |
| ans auto-control | Detects ANS tone and enables standard actions for modem tones. |
| ans-all disable echo suppressor | Detects modem answer tones and disables echo suppressor. |
| anspr disable echo suppressor | Detects /ANS tone and disables echo suppressor. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Command | Description |
|---|---|
| tone incoming system | Sets a dial peer for tone incoming or no tone incoming detection. |
| show port operational status | Displays the status of the echo canceller. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Command | Description |
|---|---|
| tone incoming ans disable echo suppressor | Activates ANS tone detection. |
| tone incoming anspr disable echo canceller | Activates ANSpr tone detection. |
| tone incoming ans-all auto-control | Activates ANS, ANSam, and ANSpr tone detection. |
| show port operational status | Displays the status of the echo canceller. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 1700 series, Cisco 2600 series, Cisco 3600 series, Cisco 3700 series, Cisco 7200
                                          series, Cisco AS5300, and Cisco AS5800. |

| Command | Description |
|---|---|
| progress_ind | Sets a specific PI in call Setup, Progress, or Connect messages from an H.323 VoIP gateway. |

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.3.2 Cisco IOS XE Bengaluru 17.4.1a | This command was introduced on Cisco Unified Border Element. |

| Command | Description |
|---|---|
| memory-limit (trace) | Defines the memory limit for storing VoIP Trace information. |
| shutdown (trace) | Disable the VoIP Trace serviceability framework in CUBE. |
| show voip trace | Displays the VoIP Trace information for SIP legs on a call received on CUBE |

| keypad-character | Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #2. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced. |

| Command | Description |
|---|---|
| conference | Defines FAC in Feature Mode to initiate a three-party conference. |
| drop-last-conferee | Defines FAC in feature mode to use to drop last active call during a three-party conference. |
| hangup-last-active-call | Defines FAC in feature mode to drop last active call during a three-party conferencee. |
| toggle-between-two-calls | Defines FAC in feature mode to toggle between two active calls. |

| calling - number | Translation rule applies to the inbound calling party number. |
|---|---|
| called - number | Translation rule applies to the inbound called party number. |
| name - tag | Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced for VoIP on Cisco AS5300. |
| 12.0(7)XK | This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T and implemented for VoIP Cisco AS5300, Cisco 7200, and Cisco 7500. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| numbering-type | Specifies number type for the VoIP or POTS dial peer. |
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| show translation-rule | Displays the contents of all the rules that have been configured for a specific translation name. |
| translate-outgoing | Applies a translation rule to a calling party number or a called party number for outgoing calls. |
| translation-rule | Creates a translation name and enters translation-rule configuration mode. |
| voip-incoming translation-rule | Captures calls that originate from H.323-compatible clients. |

| called | Associates the translation rule with called numbers. |
|---|---|
| calling | Associates the translation rule with calling numbers. |
| redirect - called | Associates the translation rule with redirected called numbers. |
| redirect-target | Associates the translation rule with transfer-to numbers and call-forwarding final destination numbers. |
| translation - rule - number | Number of the translation rule to use for the call translation. Valid range is from 1 to 2147483647. There is no default value. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced on the Cisco AS5300. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T and implemented on the following platforms: Cisco 1750, Cisco
                                          AS5300, Cisco 7200 series, and Cisco 7500 series. |
| 12.1(2)T | This command was implemented on the Cisco MC3810. |
| 12.2(11)T | This command was reconfigured for voice translation-profile configuration mode. The redirect - called keyword and translation-rule-number argument were added. |
| 12.4(11)XJ | The redirect-target keyword was added. |
| 12.4(15)T | The redirect-target keyword was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation-rule. |
| show voice translation-profile | Displays the configuration of the translation-profile. |
| translation-profile (dial-peer) | Assigns a translation profile to a dial peer. |
| translation-profile (source group) | Assigns a translation profile to a source IP group. |
| translation-profile (trunk group) | Assigns a translation profile to a trunk group. |
| translation-profile (voice port) | Assigns a translation profile to a voice port. |
| translation-profile (voice service POTS) | Assigns a translation profile to an NFAS interface. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| calling - number | Apply to the outbound calling party number. |
|---|---|
| called - number | Apply to the outbound called party number. |
| name - tag | Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is 1 to 2147483647. There is no
                                          default value. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced for VoIP on Cisco AS5300. |
| 12.0(7)XK | This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.2(1)T and implemented for VoIP on the Cisco 1750, Cisco AS5300, Cisco
                                          7200, and Cisco 7500. support for the Cisco MC3810 is not included in this release. |
| 12.1(2)T | This command is supported on the Cisco MC3810 in this release. |

| Command | Description |
|---|---|
| numbering-type | Specifies number type for the VoIP or POTS dial peer. |
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| show translation-rule | Displays the contents of all the rules that have been configured for a specific translation name. |
| translate | Applies a translation rule to a calling party number or a called party number for incoming calls. |
| translation-rule | Creates a translation name and enters translation-rule configuration mode. |
| voip-incoming translation-rule | Captures calls that originate from H.323-compatible clients. |

| incoming | Specifies that this translation profile handles incoming calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing calls. |
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| 12.4(22)T | Support for IPv6 was added. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation rule. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| incoming | Specifies that this translation profile handles incoming calls. |
|---|---|
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation rule. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| incoming | Specifies that this translation profile handles incoming calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing calls. |
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation rule. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| incoming | Specifies that this translation profile handles incoming calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing calls. |
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation rule. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| incoming | Specifies that this translation profile handles incoming calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing calls. |
| T1 | T1 controller. |
| E1 | E1 controller. |
| unit-number | Number of the controller unit. |
| name | Name of the translation profile. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Sets the criteria for the translation rule. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Initiates the translation-profile definition. |
| voice translation-rule | Initiates the translation-rule definition. |

| name - tag | Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced for VoIP on Cisco AS5300. |
| 12.0(7)XK | This command was implemented for the following voice technologies on the following platforms: VoIP Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 VoFR Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 VoATM Cisco 3600 series and Cisco MC3810 |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T and implemented for the following voice technology on the following
                                          platforms: VoIP (Cisco 1750, Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco 7200 series, and Cisco 7500 series) |
| 12.1(2)T | This command was integrated ino Cisco IOS Release 12.1(2)T for the following voice technologies on the following platforms: VoIP Cisco MC3810 VoFR Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 VoATM Cisco 3600 series and Cisco MC3810 |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| numbering-type | Specifies number type for the VoIP or POTS dial peer. |
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| test translation-rule | Tests the execution of the translation rules on a specific name tag. |
| translate | Applies a translation rule to a calling party number or a called party number for incoming calls. |
| translate-outgoing | Applies a translation rule to a calling party number or a called party number for outgoing calls. |
| voip-incoming translation-rule | Captures calls that originate from H.323-compatible clients. |

| tcp | SIP user agent receives SIP messages on TCP port 5060. |
|---|---|
| tls | (Optional) SIP user agent receives SIP messages on TLS over TCP port 5061. You can configure TLS version 1.0, 1.1, 1.2, or
                                          1.3. Starting from Cisco IOS XE 26.1.1 release, insecure TLS versions and ciphers are not supported in default configurations. However, these insecure configurations
                                          are supported in "system mode insecure" operation-mode. |
| minimum | (Optional) Specifies minimum configured TLS version. The minimum keyword can be configured only with TLS version 1.2. This configuration enables TLS versions 1.2 and 1.3. |
| udp | SIP user agent receives SIP messages on UDP port 5060. |

| Release | Modification |
|---|---|
| Cisco IOS XE 26.1.1 | This command is modified with the removal of insecure TLS versions (1.0, 1.1) and associated ciphers from default configurations.
                                          Support for insecure configurations in "system mode insecure" operation-mode. |
| Cisco IOS XE 17.18.2 | Security warnings for usage of legacy TLS and associated weaker ciphers. |
| Cisco IOS XE 17.14.1a | This command is modified to include the TLS version 1.3 support. In addition, minimum keyword configuration support is introduced with TLS version 1.2. Introduced support for the following YANG models: transport tcp tls v1.3 transport tcp tls v1.2 minimum |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |
| 15.6(1)T and 3.17S | This command was modified to include the TLS version 1.2. |
| 12.4(6)T | The optional TLS keyword was added to the command. |
| 12.2(11)T | Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms in this release. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on Cisco 7200 series routers. Support for the
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms were not included in this release. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850 platforms. |
| 12.2(2)XA | This command was implemented on Cisco AS5400 and Cisco AS5350 platforms. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |
| 12.1(1)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300 platforms. |

| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                          For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
|---|---|

| Note | Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                          insecure configurations are allowed in "system mode insecure" operation-mode. The following are the insecure ciphers associated
                                          with TLS versions (1.0, 1.1): DHE_RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Command | Description |
|---|---|
| sip-ua | Enables the SIP user agent configuration commands. |

| udp | Enables switching the transport mechanism from UDP on the basis of the size of the SIP request being greater than the MTU
                                          size. |
|---|---|
| tcp | Enables switching transport to TCP. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| debug ccsip transport | Enables tracing of the SIP transport handler and the TCP or UDP process. |
| sip | Enters SIP configuration mode from voice-service VoIP configuration mode. |
| voice - class sip transport switch | Enables switching between transport mechanisms if the SIP message is larger than 1300 bytes for a specific dial peer. |

| name | Name of the trunk group. Valid names contain a maximum of 63 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |

| Command | Description |
|---|---|
| carrier-id (trunk group) | Identifies the carrier that owns the trunk group. |
| description (trunk group) | Permits a description to be associated with a trunk group. |
| hunt-scheme least-idle | Specifies the least-idle channel search method for incoming and outgoing calls. |
| hunt-scheme least-used | Specifies the least-used channel search method for incoming and outgoing calls. |
| hunt-scheme longest-idle | Specifies the longest-idle channel search method for incoming and outgoing calls. |
| hunt-scheme random | Specifies the random channel search method for incoming and outgoing calls. |
| hunt-scheme round-robin | Specifies the round-robin channel search method for incoming and outgoing calls. |
| hunt-scheme sequential | Specifies the sequential channel search method for incoming and outgoing calls. |
| max-calls | Specifies the number of incoming and outgoing voice and data calls that a trunk group can handle. |
| show trunk group | Displays the configuration of trunk groups. |
| translation-profile (trunk group) | Defines call number translation profiles for incoming and outgoing calls. |
| trunk-group (interface) | Assigns an ISDN PRI or NFAS interface to a trunk group. |

| name | Name of the trunk group. Maximum length of the trunk group name is 63 alphanumeric characters. |
|---|---|
| preference - num | (Optional) Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority). |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show trunk group | Displays the configuration of a trunk group. |

| name | Label of the trunk group to use for the call. Valid trunk group names contain a maximum of 63 alphanumeric characters. |
|---|---|
| preference - num | Preference or priority of the trunk group. Range is from 1 (highest priority) to 64 (lowest priority). |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |
| 12.2 | This command was integrated into the Cisco IOS Release 12.2. |
| 12.2(11)T | The preference - num argument was added. |

| Command | Description |
|---|---|
| debug dialpeer | Initiates dial peer debugging. |
| show dial-peer voice | Displays the dial peer configuration. |
| translation-profile (dial peer) | Defines call number translation profiles for incoming and outgoing calls. |

| name | Name of the trunk group. Valid trunk group names contain a maximum of 63 alphanumeric characters. |
|---|---|
| preference - num | Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority). |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |
| 12.2 | This command was integrated into Cisco IOS Release 12.2. |
| 12.2(11)T | The trunk-group identification was expanded to include alphanumeric characters using the name argument, and the preference-num argument was added. |

| Command | Description |
|---|---|
| show trunk group | Displays the configuration of the trunk group. |

| name | Name of the trunk group. Maximum length of the trunk group name is 63 alphanumeric characters. |
|---|---|
| preference - num | Priority of the trunk group member in a trunk group. Range is from 1 (highest priority) to 64 (lowest priority). |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show trunk group | Displays the configuration of a trunk group. |

| source | Indicates the trunk group as the source of the incoming call. |
|---|---|
| target | Indicates the trunk group as the target of the outbound call. |
| name | Trunk group label. Maximum length of the trunk group label is 127 alphanumeric characters. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| carrier-id (dial peer) | Specifies the carrier associated with a VoIP call. |
| show dial-peer voice | Displays configuration information for dial peers. |

| source | Indicates the trunk group as the source of the incoming call. |
|---|---|
| target | Indicates the trunk group as the target of the outbound call. |
| name | Trunk group label. Maximum length of the trunk group label is 127 alphanumeric characters. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| carrier-id (dial-peer) | Specifies the carrier associated with a VoIP call. |
| show voice source-group | Displays the configuration for voice source IP groups. |

| trustpoint-label | Label of the trustpoint to be associated with the digital signal processor (DSP) farm profile. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(11)XW1 | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for digital signal processor (DSP) farm services. |

| trustpoint-name | trustpoint trustpoint-name —creates a trustpoint to store the devices certificate
                                          generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands. |
|---|---|
| client client-trustpoint-name | (Optional) Associate a client trustpoint​. Specify the client trustpoint label​. |

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.3.1a | This command was introduced under voice class configuration
                                          mode. Introduced support for Yang Model. |
| Cisco IOS XE 26.1.1 | This command was modified to allow provisioning and assigning separate certificates for client and server roles on each SIP
                                          trunk in CUBE. |

| Command | Description |
|---|---|
| voice class tls-profile | Provides sub-options to configure the commands that are required for a TLS session. |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process. |

| ttl - value | Amount of time (in seconds) for which a route from a neighbor is considered valid. Range is from 1 to 2147483647. The default
                                          is 1800 (or 30 minutes). |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| call - router | Enables the Annex G BE configuration commands. |
| show call - router status | Displays the Annex G BE status. |

| osp | Enables the Open Settlement Protocol (OSP) server type. |
|---|---|
| uni - osp | Enables authentication of VoIP calls to the Public Switched Telephone Network (PSTN) using a single settlement server. |

| Release | Modification |
|---|---|
| 12.0(4)XH1 | This command was introduced on Cisco 2600 series and Cisco 3600 series, and Cisco AS5300. |
| 12.1(2)T | The uni-osp keyword was introduced. |

| Command | Description |
|---|---|
| connection - timeout | Sets the connection timeout. |
| customer - id | Sets the customer identification. |
| device - id | Sets the device identification. |
| encryption | Specifies the encryption method. |
| max - connection | Sets the maximum simultaneous connections. |
| response - timeout | Sets the response timeout. |
| retry - delay | Sets the retry delay. |
| retry - limit | Sets the connection retry limit. |
| session - timeout | Sets the session timeout. |
| settlement | Enters settlement configuration mode. |
| show settlement | Displays the configuration for all settlement server transactions. |
| shutdown/no shutdown | Brings up the settlement provider and then shuts it down. |
| url | Specifies the Internet service provider (ISP) address. |

| 1 | Indicates the following lead configuration: E--Output, relay to ground. M--Input, referenced to ground. |
|---|---|
| 2 | Indicates the following lead configuration: E--Output, relay to SG. M--Input, referenced to ground. SB--Feed for M, connected to -48V. SG--Return for E, galvanically isolated from ground. |
| 3 | Indicates the following lead configuration: E--Output, relay to ground. M--Input, referenced to ground. SB--Connected to -48V. SG--Connected to ground. |
| 5 | Indicates the following lead configuration: E--Output, relay to ground. M--Input, referenced to -48V. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on Cisco 3600 series routers. |
| 11.3(1)MA | This command was implemented on Cisco MC3810. |

| Note | E&M Type 4 is not a supported option. However, Type 4 operates similarly to Type 2 except for the M-lead operation. On Type
                                          4, the M-lead states are open/ground, compared to Type 2, which is open/battery. Type 4 can interface with Type 2. To use
                                          Type 4 you can set the E&M voice port to Type 2 and perform the necessary M-lead rewiring. |
|---|---|