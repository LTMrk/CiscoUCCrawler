---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-transrating-html-9a53e812cd
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_transrating.html
retrieved_at: 2026-08-16T15:51:02.461254+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Transrating Configuration

## Chapter: Transrating Configuration

# Transrating Configuration

## Transrating

Transrating is a
                           		process of configuring a different packetization for a voice codec. For
                           		example, transrating G.729 20ms to G.729 30ms.

## Voice
                        	 Packetization

After the voice
                           		wavelength is digitized, the DSP collects the digitized data for an amount of
                           		time until there is enough data to fill the payload of a single packet.

With G.711, either
                           		20 ms or 30 ms worth of voice is transmitted in a single packet. 20 ms worth of
                           		voice corresponds to 160 samples per packet. With 20 ms worth of voice per
                           		packet, 50 packets are created per second: 1 sec / 20 ms = 50.

The packetization rate has a direct effect on the total amount of bandwidth needed. More packets require more headers, and
                           each header adds 40 bytes to the packet.

Codecs such as G.729
                           		also compress the digitized output. G.729 creates a codeword for every 10 ms of
                           		voice. This “codeword” is a predefined representation of a 10-ms sample of
                           		human voice. Two codewords are contained in each packet at 50 packets per
                           		second or three codewords at 33.3 packets per second. Because the codewords
                           		need fewer bits, the overall bandwidth required is reduced.

G.729, G.729A, G.729B, G.729AB 8 Kbps

G.722—64 Kbps

## Configure Transrating for a Codec

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number voip

- codec codec-name bytes voice-payload-size [ fixed-bytes ]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device> configure terminal
```

Enters global
                                          				configuration mode.

Step 3

dial-peer voice number voip

### Example:

```
Device(config)# dial-peer voice 1 voip
```

Enters dial
                                          				peer configuration mode for the specified VoIP dial peer.

Step 4

codec codec-name bytes voice-payload-size [ fixed-bytes ]

### Example:

```
Device(config-dial-peer)# codec g729r8 bytes 30 fixed-byte
```

Configures a
                                          				different packetizations for a voice codec.

Step 5

end

### Example:

```
Device(config-dial-peer)# end
```

Exits to
                                          				privileged EXEC mode.

| Supported Codecs | Packetization (ms) |
|---|---|
| G.711 a-law 64 Kbps | 10, 20, 30 |
| G.711 law 64 Kbps | 10, 20, 30 |
| G.723 5.3/6/3 Kbps | 30, 60 |
| G.729, G.729A, G.729B, G.729AB 8 Kbps | 10, 20, 30, 40, 50, 60 |
| G.722—64 Kbps | 10, 20, 30 |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device> configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | dial-peer voice number voip Example: Device(config)# dial-peer voice 1 voip | Enters dial
                                          				peer configuration mode for the specified VoIP dial peer. |
| Step 4 | codec codec-name bytes voice-payload-size [ fixed-bytes ] Example: Device(config-dial-peer)# codec g729r8 bytes 30 fixed-byte | Configures a
                                          				different packetizations for a voice codec. |
| Step 5 | end Example: Device(config-dial-peer)# end | Exits to
                                          				privileged EXEC mode. |