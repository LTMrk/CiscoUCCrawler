---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-ilbc-support-html-2747e13b4c
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-ilbc-support.html
retrieved_at: 2026-08-16T15:51:36.757682+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: iLBC Support for SIP

## Chapter: iLBC Support for SIP

# iLBC Support for SIP

The internet Low Bitrate Codec (iLBC) is a standard, high-complexity speech codec suitable for robust voice communication
                        over IP. The iLBC has built-in error correction functionality that helps the codec perform in networks with high-packet loss.
                        This codec is supported on Session Initiation Protocol (SIP).

## Feature Information for iLBC Support for SIP

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

iLBC Support for SIP

12.2(11)T

12.2(15)T

The iLBC is a standard, high-complexity speech codec suitable for robust voice communication over IP. The iLBC has built-in
                                          error correction functionality that helps the codec perform in networks with high-packet loss. This codec is supported on
                                          both Session Initiation Protocol (SIP).

The following commands were introduced or modified: codec ilbc , codec preference , and rtp payload-type .

iLBC Support for SIP

Cisco IOS XE Release 2.5

The iLBC is a standard, high-complexity speech codec suitable for robust voice communication over IP. The iLBC has built-in
                                          error correction functionality that helps the codec perform in networks with high-packet loss. This codec is supported on
                                          both Session Initiation Protocol (SIP).

The following commands were introduced or modified: codec ilbc , codec preference , and rtp payload-type .

## Restrictions for iLBC Support for SIP

The iLBC for SIP is supported on the following:

IP-to-IP gateways with no transcoding and conferencing

All c5510 DSP-based platforms

## Information About iLBC Support for SIP

The internet Low Bit Rate Codec (iLBC) is designed for narrow band speech and results in a payload bit rate of 13.33 kbits
                           per second for 30-millisecond (ms) frames and 15.20 kbits per second for 20 ms frames.

When the codec operates at block lengths of 20 ms, it produces 304 bits per block, which is packetized as defined in RFC 3952.
                           Similarly, for block lengths of 30 ms it produces 400 bits per block, which is packetized as defined in RFC 3952.

The iLBC has built-in error correction functionality to provide better performance in networks with higher packet loss.

## How to Configure an iLBC Codec

### Configure an iLBC Codec on a Dial Peer

The iLBC is intended for packet-based communication. Perform the following steps to configure the iLBC codec on a dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- rtp payload-type cisco-codec-ilbc [ number

- codec ilbc [ mode frame_size [ bytes payload_size ]]

- exit

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
Device(config)# dial-peer voice 10 voip
```

Enters dial-peer configuration mode for the VoIP dial peer designated by tag .

Step 4

rtp payload-type cisco-codec-ilbc [ number

#### Example:

```
Device(config-dial-peer)# rtp payload-type cisco-codec-ilbc 100
```

Identifies the payload type of a Real-Time Transport Protocol (RTP) packet. Keyword and argument are as follows:

cisco-codec-ilbc [ number ]–Payload type is for internet Low Bit Rate Codec (iLBC). Range: 96 to 127. Default: 116.

Do not use the following numbers because they have preassigned values: 96, 97, 100, 117, 121 to 123, and 125 to 127. If you
                                                         use these values, the command will fail. You must first reassign the value in use to a different unassigned number, for example:

```
rtp payload-type nse 105
rtp payload-type cisco-codec-ilbc 100
```

Step 5

codec ilbc [ mode frame_size [ bytes payload_size ]]

#### Example:

```
Device(config-dial-peer)# codec ilbc mode 30 bytes 200
```

Specifies the voice coder rate of speech for a dial peer. Keywords and arguments are as follows:

mode frame_size –The iLBC operating frame mode that will be encapsulated in each packet. Valid entries are 20 (20ms frames for 15.2kbps bit
                                                   rate) or 30 (30ms frames for 13.33 kbps bit rate). Default is 20.

bytes payload_size –Number of bytes in an RTP packet. For mode 20, valid values are 38 (default), 76, 114, 152, 190, and 228. For mode 30, valid
                                                   values are 50(default), 100, 150, and 200.

Step 6

exit

#### Example:

```
Device(config-dial-peer)# exit
```

Exits the current mode.

### Configure an iLBC Codec in the Voice Class

When using multiple codecs, you must create a voice class in which you define a selection order for codecs; then, you can
                                 apply the voice class to VoIP dial peers. The voice class codec global configuration command allows you to define the voice class that contains the codec selection order. Then, use the voice-class codec dial-peer configuration command to apply the class to individual dial peers.

To configure an iLBC in the voice class for multiple-codec selection order, perform the following steps.

You can configure more than one voice class codec list for your network. Configure the codec lists and apply them to one or
                                 more dial peers based on which codecs (and the order) you want supported for the dial peers. Define a selection order if you
                                 want more than one codec supported for a given dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- voice class codec tag

- codec preference value ilbc [ mode frame_size ] [ bytes payload_size ]

- exit

- dial-peer voice tag voip

- voice-class codec tag

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enters privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice class codec tag

#### Example:

```
Device(config)# voice class codec 99
```

Enters voice-class configuration mode and assigns an identification tag number for a codec voice class. The argument is as
                                             follows:

tag --Unique identifier on the router. Range is 1 to 10000.

Step 4

codec preference value ilbc [ mode frame_size ] [ bytes payload_size ]

#### Example:

```
Device(config-voice-class)# codec preference 1 ilbc 30 200
```

Specifies a list of preferred codecs to use on a dial peer. Keywords and arguments are as follows:

value –Order of preference, with 1 being the most preferred and 14 being the least preferred.

mode frame_size –The iLBC operating frame mode that will be encapsulated in each packet. Valid entries are 20 (20ms frames for 15.2kbps bit
                                                   rate) or 30 (30ms frames for 13.33 kbps bit rate). Default is 20.

bytes payload_size –Number of bytes in an RTP packet. For mode 20, valid values are 38 (default), 76, 114, 152, 190, and 228. For mode 30, valid
                                                   values are 50(default), 100, 150, and 200.

Step 5

exit

#### Example:

```
Device(config-voice-class)# exit
```

Exits the current mode.

Step 6

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 16 voip
```

Enters dial-peer configuration mode for the specified VoIP dial peer.

Step 7

voice-class codec tag

#### Example:

```
Device(config-dial-peer)# voice-class codec 99
```

Assigns a previously configured codec selection preference list (the codec voice class that you defined in step 3) to the
                                             specified VoIP dial peer.

The voice-class codec command in dial-peer configuration mode contains a hyphen. The voice class command in global configuration mode does not contain a hyphen.

Step 8

exit

#### Example:

```
Device(config-dial-peer)# exit
```

Exits the current mode.

### Verify iLBC Support for SIP

You can use the following commands to check iLBC status:

show voice call summary

show voice call status

show voice dsmp stream

show call active voice

show call history voice

show voice dsp and its extensions

show dial-peer voice

show voice dsp channel operational-status

| Feature Name | Releases | Feature Information |
|---|---|---|
| iLBC Support for SIP | 12.2(11)T 12.2(15)T | The iLBC is a standard, high-complexity speech codec suitable for robust voice communication over IP. The iLBC has built-in
                                          error correction functionality that helps the codec perform in networks with high-packet loss. This codec is supported on
                                          both Session Initiation Protocol (SIP). The following commands were introduced or modified: codec ilbc , codec preference , and rtp payload-type . |
| iLBC Support for SIP | Cisco IOS XE Release 2.5 | The iLBC is a standard, high-complexity speech codec suitable for robust voice communication over IP. The iLBC has built-in
                                          error correction functionality that helps the codec perform in networks with high-packet loss. This codec is supported on
                                          both Session Initiation Protocol (SIP). The following commands were introduced or modified: codec ilbc , codec preference , and rtp payload-type . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 10 voip | Enters dial-peer configuration mode for the VoIP dial peer designated by tag . |
| Step 4 | rtp payload-type cisco-codec-ilbc [ number Example: Device(config-dial-peer)# rtp payload-type cisco-codec-ilbc 100 | Identifies the payload type of a Real-Time Transport Protocol (RTP) packet. Keyword and argument are as follows: cisco-codec-ilbc [ number ]–Payload type is for internet Low Bit Rate Codec (iLBC). Range: 96 to 127. Default: 116. Note Do not use the following numbers because they have preassigned values: 96, 97, 100, 117, 121 to 123, and 125 to 127. If you
                                                         use these values, the command will fail. You must first reassign the value in use to a different unassigned number, for example: rtp payload-type nse 105
rtp payload-type cisco-codec-ilbc 100 | Note | Do not use the following numbers because they have preassigned values: 96, 97, 100, 117, 121 to 123, and 125 to 127. If you
                                                         use these values, the command will fail. You must first reassign the value in use to a different unassigned number, for example: |
| Note | Do not use the following numbers because they have preassigned values: 96, 97, 100, 117, 121 to 123, and 125 to 127. If you
                                                         use these values, the command will fail. You must first reassign the value in use to a different unassigned number, for example: |
| Step 5 | codec ilbc [ mode frame_size [ bytes payload_size ]] Example: Device(config-dial-peer)# codec ilbc mode 30 bytes 200 | Specifies the voice coder rate of speech for a dial peer. Keywords and arguments are as follows: mode frame_size –The iLBC operating frame mode that will be encapsulated in each packet. Valid entries are 20 (20ms frames for 15.2kbps bit
                                                   rate) or 30 (30ms frames for 13.33 kbps bit rate). Default is 20. bytes payload_size –Number of bytes in an RTP packet. For mode 20, valid values are 38 (default), 76, 114, 152, 190, and 228. For mode 30, valid
                                                   values are 50(default), 100, 150, and 200. |
| Step 6 | exit Example: Device(config-dial-peer)# exit | Exits the current mode. |

| Note | Do not use the following numbers because they have preassigned values: 96, 97, 100, 117, 121 to 123, and 125 to 127. If you
                                                         use these values, the command will fail. You must first reassign the value in use to a different unassigned number, for example: |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice class codec tag Example: Device(config)# voice class codec 99 | Enters voice-class configuration mode and assigns an identification tag number for a codec voice class. The argument is as
                                             follows: tag --Unique identifier on the router. Range is 1 to 10000. |
| Step 4 | codec preference value ilbc [ mode frame_size ] [ bytes payload_size ] Example: Device(config-voice-class)# codec preference 1 ilbc 30 200 | Specifies a list of preferred codecs to use on a dial peer. Keywords and arguments are as follows: value –Order of preference, with 1 being the most preferred and 14 being the least preferred. mode frame_size –The iLBC operating frame mode that will be encapsulated in each packet. Valid entries are 20 (20ms frames for 15.2kbps bit
                                                   rate) or 30 (30ms frames for 13.33 kbps bit rate). Default is 20. bytes payload_size –Number of bytes in an RTP packet. For mode 20, valid values are 38 (default), 76, 114, 152, 190, and 228. For mode 30, valid
                                                   values are 50(default), 100, 150, and 200. |
| Step 5 | exit Example: Device(config-voice-class)# exit | Exits the current mode. |
| Step 6 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 16 voip | Enters dial-peer configuration mode for the specified VoIP dial peer. |
| Step 7 | voice-class codec tag Example: Device(config-dial-peer)# voice-class codec 99 | Assigns a previously configured codec selection preference list (the codec voice class that you defined in step 3) to the
                                             specified VoIP dial peer. Note The voice-class codec command in dial-peer configuration mode contains a hyphen. The voice class command in global configuration mode does not contain a hyphen. | Note | The voice-class codec command in dial-peer configuration mode contains a hyphen. The voice class command in global configuration mode does not contain a hyphen. |
| Note | The voice-class codec command in dial-peer configuration mode contains a hyphen. The voice class command in global configuration mode does not contain a hyphen. |
| Step 8 | exit Example: Device(config-dial-peer)# exit | Exits the current mode. |

| Note | The voice-class codec command in dial-peer configuration mode contains a hyphen. The voice class command in global configuration mode does not contain a hyphen. |
|---|---|