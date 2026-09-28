---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-nr-feat-html-a1cd1fee76
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-nr-feat.html
retrieved_at: 2026-08-16T15:51:45.208510+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Noise Reduction

## Chapter: Noise Reduction

# Noise Reduction

Noise Reduction (NR) is a voice enhancement process that improves the quality of incoming speech that has already been corrupted
                        with background noise; for example, a voice conference participant speaking on a cell-phone in a car. NR works best with steady
                        state broadband noises like engine noise but not as well with impulsive noises like nearby chatter.

## Feature Information for Noise Reduction

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Noise Reduction

Baseline Functionality

Noise Reduction (NR) is a voice enhancement or restoration process that improves the quality of incoming speech that has already
                                       been corrupted with background noise. NR is supported on TDM gateways and on the Cisco UBE.

The following commands were introduced or modified: intensity , media profile nr , media service , and noisefloor .

## Restrictions for NR

Supported only on PVDM3.

Supported only on flex codec complexity.

No support for H.32x video call, complex forking calls, and fax and modem calls.

No support for Time-Division Multiplexing (TDM) hairpin call.

Configurations under POTS dial peer has higher priority over VoIP dial peer for NR.

Configurations under the dial peer has higher priority than configurations at the global level.

No support for conference calls, IP/SIP phones, and the Skinny Client Control Protocol (SCCP).

CLI supports enabling NR but not disabling NR.

No support for dynamically enabling or disabling NR during a call.

## Information About NR

### Noise Reduction

Noise Reduction (NR) is an adaptive signal processing algorithm on the Digital Signal Processor (DSP) that analyzes incoming
                              audio, extracts a fingerprint of the background noise during talker pauses, and then performs ongoing spectral subtraction
                              of this noise after a short training period (a few seconds). NR constantly adapts to changes in background noises over time.

NR can affect music on hold signals by making the music quieter. NR may disrupt fax/modem/TDD devices, although it is designed
                              to self-disable in those cases. Use modem-relay mode for reliable fax/modem transmission. NR is supported on TDM gateways
                              (TDM-VoIP and TDM-TDM) and on the Cisco Unified Border Element (Cisco UBE).

Some of the best practices for NR are as follows:

Use default values.

Do not use NR on dial peers associated with fax machines. Use fax or modem-relay modes for those dial peers.

NR, when used without dynamic user control of intensity (as is the case with gateways), must be used at a low intensity (default
                                       or lower) since it is always on. High intensity is dramatic for demonstrations with loud background noises, but the NR process
                                       itself will degrade “normal” calls if NR is run at high intensity.

## How to Configure NR

### Creating the Media Profile for NR

Perform this task to create a media profile to configure noise reduction parameters.

### SUMMARY STEPS

- enable

- configure terminal

- media profile nr tag

- intensity level

- noisefloor level

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

media profile nr tag

#### Example:

```
Device(config)# media profile nr 2
```

Creates the media profile to configure noise reduction parameters and enters media profile configuration mode. The range for
                                             the media profile tag is from 1 to 10000.

Step 4

intensity level

#### Example:

```
Device(cfg-mediaprofile)# intensity 2
```

Configures the intensity level or depth of the noise reduction process. The range is from 0 to 6.

Step 5

noisefloor level

#### Example:

```
Device(cfg-mediaprofile)# noisefloor -50
```

Configures the noise level, in dBm, above which NR will operate. NR will allow noises quieter than this level to pass without
                                             processing. The range is from -58 to -20.

Step 6

end

#### Example:

```
Device(config)# end
```

Returns to the privileged EXEC mode.

### Creating the Media Class to Enable NR

After the media profile is created, you must create a media class to enable noise reduction. Perform this task to create
                                 a media class.

### SUMMARY STEPS

- enable

- configure terminal

- media class tag

- nr profile tag

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

Creates the media class to enable the noise reduction feature and enters media class configuration mode. The range for the
                                             media class tag is from 1 to 10000.

Step 4

nr profile tag

#### Example:

```
Device(cfg-mediaclass)# nr profile 200
```

Applies the media profile to the media class. The range for the media profile NR tag is from 1 to 10000.

Step 5

end

#### Example:

```
Device(config)# end
```

Returns to privileged EXEC mode.

### Configuring the Media Class at a Dial Peer Level for NR

Perform this task to configure the media class for a dial peer.

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

Defines a particular dial peer and enters the dial-peer voice configuration mode. The range for the dial-peer voice tag is
                                             from 1 to 1073741823.

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

Returns to the privileged EXEC mode.

### Configuring the Media Class Globally for NR

Perform this task to configure a media class globally.

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

Returns to the privileged EXEC mode.

### Verifying NR

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

The following commands can help troubleshoot NR:

debug voip hpi all

debug voip dsmp all

debug voip dsm all

debug voip vtsp all

debug vpm dsp all

## Configuration Examples for the NR feature

### Example: Enabling NR globally

```
media profile nr 1
 intensity 1
! 
media profile nr 2
! 
media profile nr 3
 intensity 2
!
media profile nr 4
 intensity 3
!
media profile nr 5
 intensity 2
! 
media profile nr 7
 intensity 2
! 
media profile asp 6
! 
media class 1
 nr profile 5
 asp profile 6
! 
media service
 enhancement
  tdm 1
```

### Example: Enabling NR on a Dial Peer

```
media profile nr 1
 intensity 1
!
media profile nr 2
 intensity 2
!
media profile nr 3
 intensity 2
!
media profile asp 4
!
media class 1
 nr profile 2
 asp profile 4
!
dial-peer voice 2100 pots
 destination-pattern 2100
 incoming called-number 1100
 media-class 1
 port 0/2/0:1
 forward-digits all

dial-peer voice 1300 voip
 destination-pattern 1300
 session target ipv4:1.2.146.102
 media-class 1
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Noise Reduction | Baseline Functionality | Noise Reduction (NR) is a voice enhancement or restoration process that improves the quality of incoming speech that has already
                                       been corrupted with background noise. NR is supported on TDM gateways and on the Cisco UBE. The following commands were introduced or modified: intensity , media profile nr , media service , and noisefloor . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media profile nr tag Example: Device(config)# media profile nr 2 | Creates the media profile to configure noise reduction parameters and enters media profile configuration mode. The range for
                                             the media profile tag is from 1 to 10000. |
| Step 4 | intensity level Example: Device(cfg-mediaprofile)# intensity 2 | Configures the intensity level or depth of the noise reduction process. The range is from 0 to 6. |
| Step 5 | noisefloor level Example: Device(cfg-mediaprofile)# noisefloor -50 | Configures the noise level, in dBm, above which NR will operate. NR will allow noises quieter than this level to pass without
                                             processing. The range is from -58 to -20. |
| Step 6 | end Example: Device(config)# end | Returns to the privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media class tag Example: Device(config)# media class 2 | Creates the media class to enable the noise reduction feature and enters media class configuration mode. The range for the
                                             media class tag is from 1 to 10000. |
| Step 4 | nr profile tag Example: Device(cfg-mediaclass)# nr profile 200 | Applies the media profile to the media class. The range for the media profile NR tag is from 1 to 10000. |
| Step 5 | end Example: Device(config)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag pots Example: Device(config)# dial-peer voice 20 pots | Defines a particular dial peer and enters the dial-peer voice configuration mode. The range for the dial-peer voice tag is
                                             from 1 to 1073741823. |
| Step 4 | media-class tag Example: Device(config-dial-peer)# media-class 2 | Applies the media class to the specific dial peer. The range for the media class tag number is from 1 to 10000. |
| Step 5 | end Example: Device(config-dial-peer)# end | Returns to the privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | media service Example: Device(config)# media service | Enters media service configuration mode. |
| Step 4 | enhancement Example: Device(cfg-mediaservice)# enhancement | Enters the submode enhance of media service. |
| Step 5 | tdm tag Example: Device(cfg-service-enhance)# tdm 2 | Applies the TDM call globally. The range for the media class tag number is from 1 to 10000. |
| Step 6 | end Example: Device(config-dial-peer)# end | Returns to the privileged EXEC mode. |

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