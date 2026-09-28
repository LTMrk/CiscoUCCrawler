---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-cpa-html-8a136867cc
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-cpa.html
retrieved_at: 2026-08-16T15:51:07.185467+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Call Progress Analysis

## Chapter: Call Progress Analysis

# Call Progress Analysis

## Call Progress Analysis Over IP-to-IP Media Session

The Call Progress Analysis Over IP-IP Media Session feature enables the detection of automated answering systems and live
                           human voices on outbound calls and communicates the detected information to the external application. Typically, call progress
                           analysis (CPA) is extensively used in contact center deployments in conjunction with the outbound Session Initiation Protocol
                           (SIP) dialer, where CPA is enabled on the Cisco Unified Border Element (CUBE) , and digital signal processors (DSP) perform the CPA functionality.

### Call Progress Analysis

Call progress analysis (CPA) is a DSP algorithm that analyzes the Real-Time Transport Protocol (RTP) voice stream to look
                              for special information tones (SIT), fax or modem tones, human speech, and answering machine tones. CPA also passes the voice
                              information to Cisco IOS or CUBE .

CPA is initiated on receiving a new SIP INVITE with x-cisco-cpa content. While a call is in progress, the DSP or the Xcoder
                              analyzes the incoming voice or media stream. The DSP identifies the type of voice stream based on statistical voice patterns
                              or specific tone frequencies and provides the information to the CUBE . The CUBE notifies the dialer with a SIP UPDATE with x-cisco-cpa content along with the detected event. Based on the report, the caller
                              (dialer) can decide to either transfer the call or terminate the call.

To use the CPA functionality, you must enable CPA and configure CPA timing and threshold parameters.

SIP Message

Direction of Message

Meaning

18x or 200

Cisco IOS to dialer

CUBE informs the dialer if CPA is enabled for a call or not.

New INVITE

Dialer to Cisco IOS

Dialer requests Cisco IOS or the CUBE to activate the CPA algorithm for this session.

UPDATE

Cisco IOS to dialer

Cisco IOS or the CUBE notifies the dialer about the detected event.

### CPA Events

CPA Event

Definition

Asm

Answer machine

AsmT

Answer machine terminate tone

CpaS

Start of the Call Progress Analysis

FT

Fax/Modem tone

LS

Live human speech

LV

Low volume or dead air call

SitIC

Special information tone IC -- Intercept -- Vacant number or Automatic Identification System (AIS)

SitNC

SIT tone NC—No Circuit (NC), Emergency, or Trunk Blockage

SitVC

SIT tone VC—Vacant Code

SitRO

SIT tone RO—Reorder Announcement

SitMT

Miscellaneous SIT Tone

## Feature
                        	 Information for Call Progress Analysis Over IP-IP Media Session

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                       				  Information

Call
                                       				  Progress Analysis Over IP-to-IP Media Session

15.3(2)T

The Call
                                       				  Progress Analysis Over IP-to-IP Media Session feature enables detection of
                                       				  automated answering systems and live human voices on outbound calls and
                                       				  communicates the detected information to an external application.

The
                                       				  following command was introduced: call-progress-analysis .

Call
                                       				  Progress Analysis Over IP-to-IP Media Session

Cisco IOS XE
                                       				  Release 3.9S

The Call
                                       				  Progress Analysis Over IP-to-IP Media Session feature enables detection of
                                       				  automated answering systems and live human voices on outbound calls and
                                       				  communicates the detected information to an external application.

The
                                       				  following command was introduced: call-progress-analysis .

Support for
                                       				  additional call flows

15.5(2)T

Cisco IOS XE
                                       				  Release 3.15S

Call Progress Analysis feature is enhanced to support the following call-flows:

180 SIP response received without SDP

Direct call connect (without 18x from Service Provider)

Multiple 18x response to INVITE

Early dialog UPDATE

Dialer-CUBE CPA call record

## Restrictions for
                        	 Call Progress Analysis Over IP-to-IP Media Session

Only SIP-to-SIP
                                    				Early Offer (EO-to-EO) call flows are supported.

Session
                                    				Description Protocol (SDP) passthrough and flow-around media calls are not
                                    				supported.

Only the G711
                                    				flavor of codec is supported.

High
                                    				Availability (HA) is not supported.

Skinny Client
                                    				Control Protocol (SCCP)-based digital signal processor (DSP) farm is not
                                    				supported.

CPA cannot not be detected if Dialer uses Inband as DTMF relay
                                    				mechanism, that is, Inband to RTP-NTE DTMF inter-working is not supported with
                                    				CPA.

CPA call record is not supported for "180 without SDP" and "Direct
                                    				Call Connect (without 18x)" call flows from Service Provider.

With VCC codec configured on the dial-peer, the list of codecs in the VCC should match with the list of codec provisioned
                                    in DSP transcoder profile when CPA is enabled.

## Configure Call Progress Analysis Over IP-to-IP Media Session

### Enable CPA and Setting the CPA Parameters

Perform the following task to enable CPA and set the CPA timing and threshold parameters:

### SUMMARY STEPS

- enable

- configure terminal

- dspfarm profile profile-identifier transcode

- call-progress-analysis

- exit

- voice service voip

- cpa timing live-person max-duration

- cpa timing term-tone max-duration

- cpa threshold active-signal signal-threshold

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

dspfarm profile profile-identifier transcode

#### Example:

```
Device(config)# dspfarm profile 15 transcode
```

Enters DSP farm profile configuration mode, defines a profile for
                                             DSP farm services, and enables the profile for transcoding.

Step 4

call-progress-analysis

#### Example:

```
Device(config-dspfarm-profile)# call-progress-analysis
```

Enables call progress analysis (CPA) on CUBE .

You must configure this command to activate the CPA feature and set CPA parameters.

Step 5

exit

#### Example:

```
Device(config-dspfarm-profile)# exit
```

Exits DSP farm profile configuration mode and enters global configuration mode.

Step 6

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters voice service configuration mode.

Step 7

cpa timing live-person max-duration

#### Example:

```
Device(conf-voi-serv)# cpa timing live-person 2501
```

(Optional) Sets the maximum waiting time (in milliseconds) that the CPA algorithm uses to determine if a call is answered
                                             by a live human.

Step 8

cpa timing term-tone max-duration

#### Example:

```
Device(conf-voi-serv)# cpa timing term-tone 15500
```

(Optional) Sets the maximum waiting time (in milliseconds) that the CPA algorithm uses to wait for the answering machine termination
                                             tone after the answering machine is detected.

Step 9

cpa threshold active-signal signal-threshold

#### Example:

```
Device(conf-voi-serv)# cpa threshold active-signal 18db
```

(Optional) Sets the threshold (in decibels) of an active signal that is related to the measured noise floor level.

If a signal threshold configured by this command is greater than the measured noise floor level, then the signal is considered
                                                   as active. The active signal thresholds that you can configure are 9, 12, 15, 18, and 21 decibels.

Step 10

end

#### Example:

```
Device(conf-voi-serv)# end
```

Exits voice service configuration mode and returns to privileged EXEC mode.

#### Example: Enabling CPA and Setting the CPA Parameters

The following example shows how to enable CPA and set a few timing and threshold parameters. Depending on your requirements,
                                    you can configure more timing and threshold parameters.

```
Device> enable Device# configure terminal Device(config)# dspfarm profile 15 transcode Device(config-dspfarm-profile)# call-progress-analysis Device(config-dspfarm-profile)# exit Device(config)# voice service voip Device(conf-voi-serv)# cpa timing live-person 2501 Device(conf-voi-serv)# cpa timing term-tone 15500 Device(conf-voi-serv)# cpa threshold active-signal 18db Device(conf-voi-serv)# end
```

### Verify the Call Progress Analysis Over IP-to-IP Media Session

Perform this task to verify that call progress analysis  
                                 	 has been configured for a digital signal processor (DSP) farm profile.

### SUMMARY STEPS

- enable

- show dspfarm profile profile-identifier

### DETAILED STEPS

Step 1

enable

Enables privileged EXEC mode.

#### Example:

```
Device> enable
```

Step 2

show dspfarm profile profile-identifier

Displays the configured DSP farm profile
                                             information for a selected Cisco Call Manager group. In the following sample output, the Call Progress Analysis field shows
                                             that CPA is enabled.

#### Example:

```
Device# show dspfarm profile 3 Profile ID = 3, Service =Universal TRANSCODING, Resource ID = 3
 Profile Description :
 Profile Service Mode : Non Secure
 Profile Admin State : UP
 Profile Operation State : ACTIVE
 Application : CUBE   Status : ASSOCIATED
 Resource Provider : FLEX_DSPRM   Status : UP
 Number of Resource Configured : 4
 Number of Resources Out of Service : 0
 Number of Resources Active : 0
 Codec Configuration: num_of_codecs:4
 Codec : g711ulaw, Maximum Packetization Period : 30
 Codec : g711alaw, Maximum Packetization Period : 30
 Codec : g729ar8, Maximum Packetization Period : 60
 Codec : g729abr8, Maximum Packetization Period : 60
 Noise Reduction : ENABLED
 Call Progress Analysis : ENABLED
```

### Tips to Troubleshoot

Use the following commands to troubleshoot the call progress analysis for SIP-to-SIP calls:

debug ccsip all

debug voip ccapi inout

debug voip hpi all

debug voip ipipgw

debug voip media resource provisioning all

| SIP Message | Direction of Message | Meaning |
|---|---|---|
| 18x or 200 | Cisco IOS to dialer | CUBE informs the dialer if CPA is enabled for a call or not. |
| New INVITE | Dialer to Cisco IOS | Dialer requests Cisco IOS or the CUBE to activate the CPA algorithm for this session. |
| UPDATE | Cisco IOS to dialer | Cisco IOS or the CUBE notifies the dialer about the detected event. |

| CPA Event | Definition |
|---|---|
| Asm | Answer machine |
| AsmT | Answer machine terminate tone |
| CpaS | Start of the Call Progress Analysis |
| FT | Fax/Modem tone |
| LS | Live human speech |
| LV | Low volume or dead air call |
| SitIC | Special information tone IC -- Intercept -- Vacant number or Automatic Identification System (AIS) |
| SitNC | SIT tone NC—No Circuit (NC), Emergency, or Trunk Blockage |
| SitVC | SIT tone VC—Vacant Code |
| SitRO | SIT tone RO—Reorder Announcement |
| SitMT | Miscellaneous SIT Tone |

| Feature Name | Releases | Feature
                                       				  Information |
|---|---|---|
| Call
                                       				  Progress Analysis Over IP-to-IP Media Session | 15.3(2)T | The Call
                                       				  Progress Analysis Over IP-to-IP Media Session feature enables detection of
                                       				  automated answering systems and live human voices on outbound calls and
                                       				  communicates the detected information to an external application. The
                                       				  following command was introduced: call-progress-analysis . |
| Call
                                       				  Progress Analysis Over IP-to-IP Media Session | Cisco IOS XE
                                       				  Release 3.9S | The Call
                                       				  Progress Analysis Over IP-to-IP Media Session feature enables detection of
                                       				  automated answering systems and live human voices on outbound calls and
                                       				  communicates the detected information to an external application. The
                                       				  following command was introduced: call-progress-analysis . |
| Support for
                                       				  additional call flows | 15.5(2)T Cisco IOS XE
                                       				  Release 3.15S | Call Progress Analysis feature is enhanced to support the following call-flows: 180 SIP response received without SDP Direct call connect (without 18x from Service Provider) Multiple 18x response to INVITE Early dialog UPDATE Dialer-CUBE CPA call record |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dspfarm profile profile-identifier transcode Example: Device(config)# dspfarm profile 15 transcode | Enters DSP farm profile configuration mode, defines a profile for
                                             DSP farm services, and enables the profile for transcoding. |
| Step 4 | call-progress-analysis Example: Device(config-dspfarm-profile)# call-progress-analysis | Enables call progress analysis (CPA) on CUBE . You must configure this command to activate the CPA feature and set CPA parameters. |
| Step 5 | exit Example: Device(config-dspfarm-profile)# exit | Exits DSP farm profile configuration mode and enters global configuration mode. |
| Step 6 | voice service voip Example: Device(config)# voice service voip | Enters voice service configuration mode. |
| Step 7 | cpa timing live-person max-duration Example: Device(conf-voi-serv)# cpa timing live-person 2501 | (Optional) Sets the maximum waiting time (in milliseconds) that the CPA algorithm uses to determine if a call is answered
                                             by a live human. |
| Step 8 | cpa timing term-tone max-duration Example: Device(conf-voi-serv)# cpa timing term-tone 15500 | (Optional) Sets the maximum waiting time (in milliseconds) that the CPA algorithm uses to wait for the answering machine termination
                                             tone after the answering machine is detected. |
| Step 9 | cpa threshold active-signal signal-threshold Example: Device(conf-voi-serv)# cpa threshold active-signal 18db | (Optional) Sets the threshold (in decibels) of an active signal that is related to the measured noise floor level. If a signal threshold configured by this command is greater than the measured noise floor level, then the signal is considered
                                                   as active. The active signal thresholds that you can configure are 9, 12, 15, 18, and 21 decibels. |
| Step 10 | end Example: Device(conf-voi-serv)# end | Exits voice service configuration mode and returns to privileged EXEC mode. |

| Step 1 | enable Enables privileged EXEC mode. Example: Device> enable |
|---|---|
| Step 2 | show dspfarm profile profile-identifier Displays the configured DSP farm profile
                                             information for a selected Cisco Call Manager group. In the following sample output, the Call Progress Analysis field shows
                                             that CPA is enabled. Example: Device# show dspfarm profile 3 Profile ID = 3, Service =Universal TRANSCODING, Resource ID = 3
 Profile Description :
 Profile Service Mode : Non Secure
 Profile Admin State : UP
 Profile Operation State : ACTIVE
 Application : CUBE   Status : ASSOCIATED
 Resource Provider : FLEX_DSPRM   Status : UP
 Number of Resource Configured : 4
 Number of Resources Out of Service : 0
 Number of Resources Active : 0
 Codec Configuration: num_of_codecs:4
 Codec : g711ulaw, Maximum Packetization Period : 30
 Codec : g711alaw, Maximum Packetization Period : 30
 Codec : g729ar8, Maximum Packetization Period : 60
 Codec : g729abr8, Maximum Packetization Period : 60
 Noise Reduction : ENABLED
 Call Progress Analysis : ENABLED |