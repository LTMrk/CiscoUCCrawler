---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-callesc-voice2vid-html-d3647a1619
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi_callesc_voice2vid.html
retrieved_at: 2026-08-16T15:45:30.049062+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Call Escalation from Voice to Video

## Chapter: Call Escalation from Voice to Video

# Call Escalation from Voice to Video

## Call Escalation from Voice to Video

The Call Escalation from Voice to Video feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice
                           calls to video. The call initially starts as an audio-only call. When the call is in progress, media renegotiation results
                           in a video stream being added to the call, leading to call escalation from an audio-only call to an audio and video call.

### Finding Feature Information

For the latest feature information and caveats, see the release notes for your platform and software release.

Use Cisco Feature Navigator to find information about platform support and Cisco IOS software image support. To access Cisco
                              Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

### Prerequisites for Call Escalation from Voice to Video

#### Cisco Unified Border Element

Cisco IOS Release 15.1(4)M or a later release must be installed and running on your Cisco Unified Border Element.

#### Cisco Unified Border Element (Enterprise)

Cisco IOS XE Release 3.8S or a later release must be installed and running on your Cisco ASR 1000 Series Router.

### How to Configure Call Escalation from Voice to Video

The Call Escalation from Voice to Video feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice
                              calls to video. The call initially starts as an audio-only call. When the call is in progress, media renegotiation results
                              in a video stream being added to the call, leading to call escalation from an audio-only call to an audio and video call.

#### Configuring Call Escalation from Voice to Video

To configure call escalation for SIP-to-SIP calls from voice calls to video, perform the following task:

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- allow-connections from-type to to-type

- exit

- dial-peer voice tag voip

- session protocol sipv2

- codec transparent

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

##### Example:

```
Device(config)# voice service voip
```

Enters VoIP voice service configuration mode.

Step 4

allow-connections from-type to to-type

##### Example:

```
Device(config-voi-srv)# allow-connections sip to sip
```

Allows connections between specific types of endpoints in an Cisco UBE. Arguments are as follows:

from-type—Type of connection. Valid values: h323, sip

to-type—Type of connection. Valid values: h323. sip

H.323-to-H.323: By default, H.323-to-H.323 connections are disabled and POTS-to-any and any-to-POTS connections are enabled.

Step 5

exit

##### Example:

```
Router(config-voi-serv)# exit
```

Exits VoIP service configuration mode and returns to global configuration mode.

Step 6

dial-peer voice tag voip

##### Example:

```
Device(config)# dial-peer voice 1 voip
```

Enters dial-peer voice configuration mode for the specified VoIP dial peer.

Step 7

session protocol sipv2

##### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Enters the session protocol type as SIP.

Step 8

codec transparent

##### Example:

```
Device(config-dial-peer)# codec transparent
```

Specifies the voice codec rate of speech for a dial peer.

transparent—Enables codec capabilities to be passed transparently between endpoints in a Cisco Unified Border Element (UBE).

The transparent keyword is available only on the Cisco 2600, 3600, 7200, and 7500 series routers.

Step 9

end

##### Example:

```
Device(config-dial-peer)# end
```

Exits dial-peer voice configuration mode.

### Feature Information for Call Escalation from Voice to Video

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Call Escalation from Voice to Video

15.1(4)M

This feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.This feature supports
                                          mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.

Call Escalation from Voice to Video

Cisco IOS XE Release 3.8S

This feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.This feature supports
                                          mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters VoIP voice service configuration mode. |
| Step 4 | allow-connections from-type to to-type Example: Device(config-voi-srv)# allow-connections sip to sip | Allows connections between specific types of endpoints in an Cisco UBE. Arguments are as follows: from-type—Type of connection. Valid values: h323, sip to-type—Type of connection. Valid values: h323. sip Note H.323-to-H.323: By default, H.323-to-H.323 connections are disabled and POTS-to-any and any-to-POTS connections are enabled. | Note | H.323-to-H.323: By default, H.323-to-H.323 connections are disabled and POTS-to-any and any-to-POTS connections are enabled. |
| Note | H.323-to-H.323: By default, H.323-to-H.323 connections are disabled and POTS-to-any and any-to-POTS connections are enabled. |
| Step 5 | exit Example: Router(config-voi-serv)# exit | Exits VoIP service configuration mode and returns to global configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 1 voip | Enters dial-peer voice configuration mode for the specified VoIP dial peer. |
| Step 7 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Enters the session protocol type as SIP. |
| Step 8 | codec transparent Example: Device(config-dial-peer)# codec transparent | Specifies the voice codec rate of speech for a dial peer. transparent—Enables codec capabilities to be passed transparently between endpoints in a Cisco Unified Border Element (UBE). Note The transparent keyword is available only on the Cisco 2600, 3600, 7200, and 7500 series routers. | Note | The transparent keyword is available only on the Cisco 2600, 3600, 7200, and 7500 series routers. |
| Note | The transparent keyword is available only on the Cisco 2600, 3600, 7200, and 7500 series routers. |
| Step 9 | end Example: Device(config-dial-peer)# end | Exits dial-peer voice configuration mode. |

| Note | H.323-to-H.323: By default, H.323-to-H.323 connections are disabled and POTS-to-any and any-to-POTS connections are enabled. |
|---|---|

| Note | The transparent keyword is available only on the Cisco 2600, 3600, 7200, and 7500 series routers. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Call Escalation from Voice to Video | 15.1(4)M | This feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.This feature supports
                                          mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video. |
| Call Escalation from Voice to Video | Cisco IOS XE Release 3.8S | This feature supports mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video.This feature supports
                                          mid-call escalation of SIP-to-SIP calls via signaling from voice calls to video. |