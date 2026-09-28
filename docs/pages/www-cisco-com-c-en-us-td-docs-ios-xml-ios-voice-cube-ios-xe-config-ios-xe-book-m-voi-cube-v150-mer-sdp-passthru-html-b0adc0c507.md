---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-v150-mer-sdp-passthru-html-b0adc0c507
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-v150-mer-sdp-passthru.html
retrieved_at: 2026-08-16T15:52:01.385661+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: V150.1 MER Support in SDP Passthrough Mode

## Chapter: V150.1 MER Support in SDP Passthrough Mode

# V150.1 MER Support in SDP Passthrough Mode

The Cisco V.150.1 Minimum Essential Requirements (MER) feature complies with the requirements of the National Security Agency
                        (NSA) SCIP-216 Minimum Essential Requirements for V.150.1 recommendation, which provides for four states: audio, voice-band
                        data (VBD), modem relay, and T.38. This feature is added in CUBE (IP-IP gateway) for  V.150.1 calls to traverse a CUBE in
                        SDP passthrough flow-through mode.

## Feature Information for V.150.1 MER Support for SDP Passthrough

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

V.150.1 MER Support for SDP Passthrough

Baseline Functionality

The Cisco V.150.1 Minimum Essential Requirements (MER) feature complies with the requirements of the National Security Agency
                                          (NSA) SCIP-216 Minimum Essential Requirements for V.150.1 recommendation, which provides for four states: audio, voice-band
                                          data (VBD), modem relay, and T.38. This feature is added in CUBE (IP-IP gateway) for  V.150.1 calls to traverse a CUBE in
                                          SDP passthrough flow-through mode.

The following commands were introduced or modified: pass-thru content sdp mode non-rtp and voice-class sip pass-thru content sdp mode non-rtp

## Information About VER.150.1 MER Support in SDP Passthrough Mode

### V.150.1 MER Support in SDP Passthrough Mode

V.150.1 is an ITU standard for relaying modem or fax  transmission that uses state signaling event (SSE) packets to trigger
                              the transition from audio to modem-relay mode or fax-relay mode. The SSE headers are carried in the RTP packet.
                              After call setup, in-band signaling through Simple Packet Relay Transport (SPRT) and SSE messages is used to transition from
                              one state to another. SPRT packets (non-RTP packets) carry the data after the digital signal processor (DSP) transitions into
                              modem relay mode. UDPTL packets carry the data after the DSP transitions into fax-relay mode.

This feature is added in CUBE (IP-to-IP gateway) to support the  V.150.1 MER modem relay in SDP passthrough mode. This is
                              of importance when CUBE is in the media path between V.150.1 MER supported gateways and needs to handle non-RTP packets (such
                              as SPRT packets).

### Modem Relay Topology

## How to Configure V.150.1 MER Support for SDP Passthrough

### Configuring V.150.1 MER Support for SDP Passthrough

### SUMMARY STEPS

- enable

- configure terminal

- Set passthrough SDP mode to non-RTP:

- voice-class sip
                                          					 pass-thru content sdp mode non-rtp in the dial-peer configuration mode.

- pass-thru content sdp mode non-rtp in the global VoIP SIP configuration mode.

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Set passthrough SDP mode to non-RTP:

- voice-class sip
                                                   					 pass-thru content sdp mode non-rtp in the dial-peer configuration mode.

- pass-thru content sdp mode non-rtp in the global VoIP SIP configuration mode.

#### Example:

```
!Setting passthrough SDP mode for one dial peer only
Device (config)# dial-peer voice 20 voip Device (config-dial-peer)# voice-class sip pass-thru content sdp mode non-rtp Device (config-dial-peer)# end
```

#### Example:

```
!Setting passthrough SDP mode globally
Device(config)# voice service voip Device (conf-voi-serv)# sip Device (conf-serv-sip)# pass-thru content sdp mode non-rtp Device (conf-serv-sip)# end
```

Step 4

end

Exits to privileged EXEC mode.

### Verifying V.150.1 MER Support in SDP Passthrough Mode

### SUMMARY STEPS

- enable

- debug ccsip verbose

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Step 2

debug ccsip verbose

#### Example:

```
Device# debug ccsip verbose 010362: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_SetSdpPthruCfg:
010363: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_IsSDPPassthruEnabled:
010364: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Info/critical/8192/sipSPI_ipip_IsSDPPassthruEnabled:  - 1
010365: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_SetSDPPassthruMode:
010366: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Info/info/128/sipSPI_ipip_SetSDPPassthruMode: SDP Passthru Mode is set to – 1

011365: *Jan 31 12:34:02.604: //31/14B4F1000000/SIP/Function/sipSPIGetStream:
011366: *Jan 31 12:34:02.604: //32/14B4F1000000/SIP/Info/info/128/sipSPI_ipip_UpdatePthruStreamRtcpInfo: Setting stream xmit function to voip_udp_xmit
011367: *Jan 31 12:34:02.604: //32/14B4F1000000/SIP/Function/sipSPIGetRSVPIPTos
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| V.150.1 MER Support for SDP Passthrough | Baseline Functionality | The Cisco V.150.1 Minimum Essential Requirements (MER) feature complies with the requirements of the National Security Agency
                                          (NSA) SCIP-216 Minimum Essential Requirements for V.150.1 recommendation, which provides for four states: audio, voice-band
                                          data (VBD), modem relay, and T.38. This feature is added in CUBE (IP-IP gateway) for  V.150.1 calls to traverse a CUBE in
                                          SDP passthrough flow-through mode. The following commands were introduced or modified: pass-thru content sdp mode non-rtp and voice-class sip pass-thru content sdp mode non-rtp |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Set passthrough SDP mode to non-RTP: voice-class sip
                                                   					 pass-thru content sdp mode non-rtp in the dial-peer configuration mode. pass-thru content sdp mode non-rtp in the global VoIP SIP configuration mode. Example: In
                                          			 dial-peer configuration mode !Setting passthrough SDP mode for one dial peer only
Device (config)# dial-peer voice 20 voip Device (config-dial-peer)# voice-class sip pass-thru content sdp mode non-rtp Device (config-dial-peer)# end Example: In
                                          			 global VoIP SIP mode !Setting passthrough SDP mode globally
Device(config)# voice service voip Device (conf-voi-serv)# sip Device (conf-serv-sip)# pass-thru content sdp mode non-rtp Device (conf-serv-sip)# end |  |
| Step 4 | end | Exits to privileged EXEC mode. |

| Step 1 | enable Example: Device> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | debug ccsip verbose Example: Device# debug ccsip verbose 010362: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_SetSdpPthruCfg:
010363: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_IsSDPPassthruEnabled:
010364: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Info/critical/8192/sipSPI_ipip_IsSDPPassthruEnabled:  - 1
010365: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Function/sipSPI_ipip_SetSDPPassthruMode:
010366: *Jan 31 12:34:00.148: //31/14B4F1000000/SIP/Info/info/128/sipSPI_ipip_SetSDPPassthruMode: SDP Passthru Mode is set to – 1

011365: *Jan 31 12:34:02.604: //31/14B4F1000000/SIP/Function/sipSPIGetStream:
011366: *Jan 31 12:34:02.604: //32/14B4F1000000/SIP/Info/info/128/sipSPI_ipip_UpdatePthruStreamRtcpInfo: Setting stream xmit function to voip_udp_xmit
011367: *Jan 31 12:34:02.604: //32/14B4F1000000/SIP/Function/sipSPIGetRSVPIPTos |