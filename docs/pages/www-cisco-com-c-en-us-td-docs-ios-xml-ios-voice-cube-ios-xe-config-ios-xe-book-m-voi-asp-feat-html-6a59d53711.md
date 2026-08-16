---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-asp-feat-html-6a59d53711
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-asp-feat.html
retrieved_at: 2026-08-16T15:51:41.084313+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Acoustic Shock Protection

## Chapter: Acoustic Shock Protection

# Acoustic Shock Protection

Acoustic Shock Protection (ASP) is a voice circuit-breaker feature that is designed to protect users, especially those wearing
                        headsets, from exposure to loud, sustained, and piercing tones, such as those produced by a fax machine. It is a workplace-safety
                        feature for voice calls. When the tone is present at the input of the ASP module, the audio path in the affected direction
                        is muted to protect the listener, and a gentle alert tone is played out for as long as the tone persists. ASP may be inserted
                        in either or both directions of a call, that is, applied to incoming packets to protect the ears of a listener on the Time-Division
                        Multiplexing (TDM) gateway, applied to incoming PSTN calls (microphone signal) to protect the ears of listeners at the other
                        end of the call, or applied to both simultaneously.

## Feature Information for Acoustic Shock Protection

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Acoustic Shock Protection

Baseline Functionality

Acoustic Shock Protection (ASP) is a voice circuit-breaker feature that is designed to protect users, especially those wearing
                                       headsets, from exposure to loud, sustained, and piercing tones, such as those produced by a fax machine. It is a workplace-safety
                                       feature for voice calls. ASP is supported on TDM gateways and on Cisco UBE.

The following commands were introduced or modified: media profile asp , and media service .

## Restrictions for ASP

Supported on PVDM3 only.

Supported only on flex codec complexity.

No support for H.32x video call, complex forking calls, and fax and modem calls.

No support for TDM hairpin call.

The configuration under dial peer has higher priority than the configuration at the global level.

No support for conference calls, IP/SIP phones, and the Skinny Client Control Protocol (SCCP).

CLI supports enabling ASP but not disabling ASP.

No support for dynamically enabling or disabling ASP during a call.

## Information About ASP

### Acoustic Shock Protection

Acoustic Shock Protection (ASP) is an adaptive signal processing algorithm on the Digital Signal Processor (DSP) that analyzes
                              incoming audio for the presence of offending tones that might harm humans. Offending tones include signals that are:

Loud

Tonal (energy concentrated around a single frequency)

Persistent (lasts longer than a few tens of milliseconds)

If an offending tone is present, the audio path in that direction is muted temporarily, and a quiet, alerting signal is played
                              out to the listener side. The call is never dropped; only the audio is muted temporarily. If or when the tone disappears from
                              the input, the mute is removed. ASP does not disrupt low-frequency tones (below 650 Hz) such as ringback, dial, and so forth.
                              Since ASP is designed to mute only single-frequency tones, it allows multi-tone signals such as Dual Tone Multi-Frequency
                              (DTMF) to pass unhindered. ASP is supported on TDM gateways (TDM-VoIP and TDM-TDM) and on the Cisco Unified Border Element
                              (Cisco UBE).

ASP is for voice calls only and not for faxes and modems.

Some of the best practices for ASP are as follows:

Use default values

Use ASP on dial peers where you are certain that people (not faxes) are listening.

Do not use ASP on dial peers associated with fax machines, modems, or TTY/TDD devices. Use fax-relay or modem-relay modes
                                       on dial peers dedicated to such devices.

ASP is designed for deployment in situations where customers have experienced acoustic shock safety issues. If there are issues
                                       like false triggering (for example, ASP alerts on regular voices), then you must turn off ASP. You can choose from three detector
                                       sensitivity modes: slow, auto, or fast. Fast mode is a highly sensitive hair-trigger. Auto mode is recommended. Slow mode
                                       lets more tone leak through, but has better rejection of false triggers.

## How to Configure ASP

### Create the Media Profile for ASP

Perform this task to create a media profile to configure acoustic shock protection.

### SUMMARY STEPS

- enable

- configure terminal

- media profile asp tag

- mode mode

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

media profile asp tag

#### Example:

```
Device(config)# media profile asp 5
```

Creates the media profile to configure ASP and enters media profile configuration mode. The range for the media profile tag
                                             is from 1 to 10000.

Step 4

mode mode

#### Example:

```
Device(cfg-mediaprofile)# mode auto
```

Sets the ASP sensitivity mode to preset = auto (which is default). Auto mode provides a good tradeoff between ASP speed and
                                             false trigger rejection. The other modes are:

slow—Presets ASP sensitivity mode to 1. This mode provides slower detection speed for reduced chance of false triggers.

fast—Presets ASP sensitivity mode to 2. This mode provides faster detection speed but higher chance of false triggers.

expert—This mode exposes direct control of individual ASP parameters and is recommended for test use only.

Step 5

end

#### Example:

```
Device(config)# end
```

Returns to privileged EXEC mode.

### Create the Media Profile to Enable ASP

After the media profile is created, you must create a media class to enable acoustic shock protection. Perform this task to
                                 create a media class.

### SUMMARY STEPS

- enable

- configure terminal

- media class tag

- asp profile tag

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

media class tag

#### Example:

```
Device(config)# media class 2
```

Creates the media class to enable the acoustic shock protection feature and enters media class configuration mode. The range
                                             for the media class tag is from 1 to 10000.

Step 4

asp profile tag

#### Example:

```
Device(cfg-mediaclass)# asp profile 200
```

Applies the media profile to the media class. The range for the media profile ASP tag is from 1 to 10000.

Step 5

end

#### Example:

```
Device(cfg-mediaclass)# end
```

Returns to privileged EXEC mode.

### Configure the Media Class at a Dial Peer Level for ASP

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag pots

- media-class tag

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

dial-peer voice tag pots

#### Example:

```
Device(config)# dial-peer voice 20 pots
```

Defines a particular dial peer and enters dial-peer voice configuration mode. The range for the dial-peer voice tag is from
                                             1 to 1073741823.

Step 4

media-class tag

#### Example:

```
Device(config-dial-peer)# media-class 2
```

Applies the media class to the specific dial peer. The range for the media class tag number is from 1 to 10000.

Step 5

end

#### Example:

```
Device(config-dial-peer)# end
```

Returns to privileged EXEC mode.

### Configure the Media Class Globally for ASP

### SUMMARY STEPS

- enable

- configure terminal

- media service

- enhancement

- tdm tag

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

media service

#### Example:

```
Device(config)# media service
```

Enters media service configuration mode.

Step 4

enhancement

#### Example:

```
Device(cfg-mediaservice)# enhancement
```

Enters the submode enhance of media service.

Step 5

tdm tag

#### Example:

```
Device(cfg-service-enhance)# tdm 2
```

Applies the TDM call globally. The range for the media class tag number is from 1 to 10000.

Step 6

end

#### Example:

```
Device(config-dial-peer)# end
```

Returns to privileged EXEC mode.

### Verify ASP

Perform this task to verify the voice quality metrics.

### SUMMARY STEPS

- enable

- show call active voice stats | b pid:

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Step 2

show call active voice stats | b pid:

#### Example:

```
Device# show call active voice stats | b pid:1300 11EC : 5 09:14:25.971 PDT Thu Jul 28 2011.1 +1130 pid:1300 Answer 1300 active dur 00:01:36 tx:17/321 rx:17/321 dscp:0 media:0
DSP/TX: PK=17, SG=0, NS=1, DU=90570, VO=320
DSP/RX: PK=17, SG=0, CF=1, RX=90570, VO=320, BS=0, BP=0, LP=0, EP=0
….
DSP/DL: RT=0, ED=0
MIC Direction:
DSP/NR: NR=1, ND=0, LV=257, IN=1, PN=0, ON=0
DSP/AS: AE=1, AD=0, AV=0, AM=0, NT=0, DT=0, TT=0, TD=0, LF=0, LD=0
EAR Direction:
DSP/NR: NR=0, ND=0, LV=0, IN=0, PN=0, ON=0
DSP/AS: AE=0, AD=0, AV=0, AM=0, NT=0, DT=0, TT=0, TD=0, LF=0, LD=0
11EC : 6 09:14:25.973 PDT Thu Jul 28 2011.2 +1130 pid:2300 Originate 2300 active dur 00:01:36 tx:17/457 rx:17/321 dscp:0 media:0
Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 1
```

Displays information about digital signal processing (DSP) voice quality metrics.

### Troubleshooting Tips

The following commands can help troubleshoot ASP:

debug voip hpi all

debug voip dsmp all

debug voip dsm all

debug voip vtsp all

debug vpm dsp all

## Configuration Examples for the Acoustic Shock Protection Feature

### Example: Enabling ASP Globally

```
media profile asp 6 
! 
media class 1
  asp profile 6
!
media service
  enhancement 
    tdm 1
```

### Example: Enabling ASP on a Dial Peer

```
media profile asp 4  
! 
media class 1
  asp profile 4
! 
dial-peer voice 2100 pots
  destination-pattern 2100 
  incoming called-number 1100 
  media-class 1 
  port 0/2/0:1
  forward-digits all
 dial-peer voice 1300 voip 
 destination-pattern 1300 session target ipv4:1.2.146.102 media-class 1
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Acoustic Shock Protection | Baseline Functionality | Acoustic Shock Protection (ASP) is a voice circuit-breaker feature that is designed to protect users, especially those wearing
                                       headsets, from exposure to loud, sustained, and piercing tones, such as those produced by a fax machine. It is a workplace-safety
                                       feature for voice calls. ASP is supported on TDM gateways and on Cisco UBE. The following commands were introduced or modified: media profile asp , and media service . |

| Note | ASP is for voice calls only and not for faxes and modems. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media profile asp tag Example: Device(config)# media profile asp 5 | Creates the media profile to configure ASP and enters media profile configuration mode. The range for the media profile tag
                                             is from 1 to 10000. |
| Step 4 | mode mode Example: Device(cfg-mediaprofile)# mode auto | Sets the ASP sensitivity mode to preset = auto (which is default). Auto mode provides a good tradeoff between ASP speed and
                                             false trigger rejection. The other modes are: slow—Presets ASP sensitivity mode to 1. This mode provides slower detection speed for reduced chance of false triggers. fast—Presets ASP sensitivity mode to 2. This mode provides faster detection speed but higher chance of false triggers. expert—This mode exposes direct control of individual ASP parameters and is recommended for test use only. |
| Step 5 | end Example: Device(config)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media class tag Example: Device(config)# media class 2 | Creates the media class to enable the acoustic shock protection feature and enters media class configuration mode. The range
                                             for the media class tag is from 1 to 10000. |
| Step 4 | asp profile tag Example: Device(cfg-mediaclass)# asp profile 200 | Applies the media profile to the media class. The range for the media profile ASP tag is from 1 to 10000. |
| Step 5 | end Example: Device(cfg-mediaclass)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag pots Example: Device(config)# dial-peer voice 20 pots | Defines a particular dial peer and enters dial-peer voice configuration mode. The range for the dial-peer voice tag is from
                                             1 to 1073741823. |
| Step 4 | media-class tag Example: Device(config-dial-peer)# media-class 2 | Applies the media class to the specific dial peer. The range for the media class tag number is from 1 to 10000. |
| Step 5 | end Example: Device(config-dial-peer)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media service Example: Device(config)# media service | Enters media service configuration mode. |
| Step 4 | enhancement Example: Device(cfg-mediaservice)# enhancement | Enters the submode enhance of media service. |
| Step 5 | tdm tag Example: Device(cfg-service-enhance)# tdm 2 | Applies the TDM call globally. The range for the media class tag number is from 1 to 10000. |
| Step 6 | end Example: Device(config-dial-peer)# end | Returns to privileged EXEC mode. |

| Step 1 | enable Example: Device> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | show call active voice stats \| b pid: Example: Device# show call active voice stats \| b pid:1300 11EC : 5 09:14:25.971 PDT Thu Jul 28 2011.1 +1130 pid:1300 Answer 1300 active dur 00:01:36 tx:17/321 rx:17/321 dscp:0 media:0
DSP/TX: PK=17, SG=0, NS=1, DU=90570, VO=320
DSP/RX: PK=17, SG=0, CF=1, RX=90570, VO=320, BS=0, BP=0, LP=0, EP=0
….
DSP/DL: RT=0, ED=0
MIC Direction:
DSP/NR: NR=1, ND=0, LV=257, IN=1, PN=0, ON=0
DSP/AS: AE=1, AD=0, AV=0, AM=0, NT=0, DT=0, TT=0, TD=0, LF=0, LD=0
EAR Direction:
DSP/NR: NR=0, ND=0, LV=0, IN=0, PN=0, ON=0
DSP/AS: AE=0, AD=0, AV=0, AM=0, NT=0, DT=0, TT=0, TD=0, LF=0, LD=0
11EC : 6 09:14:25.973 PDT Thu Jul 28 2011.2 +1130 pid:2300 Originate 2300 active dur 00:01:36 tx:17/457 rx:17/321 dscp:0 media:0
Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 1 Displays information about digital signal processing (DSP) voice quality metrics. |