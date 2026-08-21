---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-5-installation-guide-ccvp-b-125-7bea3bebd5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/VVB_12_5/installation/guide/ccvp_b_1251-migration-guide-for-cisco-virtualized-voice-browser-release-1251/ccvp_b_1251-migration-guide-for-cisco-virtualized-voice-browser-release-1251_chapter_0100.html
retrieved_at: 2026-08-21T16:28:13.473363+00:00
---

Migration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

# Migration Guide for Cisco Virtualized Voice Browser, Release 12.5(1)

Updated: January 31, 2020

Chapter: Understanding the Difference

## Chapter: Understanding the Difference

- Understanding the Difference

- Differences

# Understanding the Difference

## Differences

The following table lists the feature and configuration differences between Cisco IOS-VB and Cisco VVB.

Feature

Cisco
                                       					 IOS-VB Configuration

Cisco VVB
                                       					 Configuration

Service/Application

Service
                                       					 Configuration

Application configuration in Cisco VVB

Dial-Peer

Dial peer
                                       					 Configuration

Trigger configuration in Cisco VVB

TCL
                                       					 Scripts

CVP OAMP
                                       					 downloaded TCL scripts:

bootstrap.tcl

CVPSelfService.tcl

cvp_ccb_poll.tcl

ringtone.tcl

ccb
                                             						  tcl scripts

AEF applications. By default, Cisco VVB includes the following prepackaged applications:

CVPComprehensive.aef

Ringtone.aef

Error.aef

SelfService.aef

VRUComprehensive.aef

You can’t modify these applications.

CVP VXML
                                       					 documents

CVP OAMP
                                       					 downloaded VXML scripts:

bootstrap.vxml

CVPSelfServiceBootstrap.vxml

recovery.vxml

Cisco VVB has prepackaged the VXML document files for various AEF applications.

You can’t modify these applications.

Codec
                                       					 config

Codec
                                       					 defined at dial-peer level

Codec
                                       					 defined at System level

MRCP
                                       					 Interface and Configuration

ASR/TTS
                                       					 configuration.

voice
                                             						  class uri

Using
                                             						  Dial-Peer to load balance ASR/TTS

ASR/TTS server configuration by specifying the hostname or IP Address of speech servers.

Load balancing is done on a round-robin basis.

Maximum sessions that can be set for a server

No such
                                       					 configuration

Weight-based load balancing between various servers configured

Weight-based load balancing isn’t supported.

CVP
                                       					 microapps dependency on MRCP v1

No dependency of CVP microapps on MRCP v1

Option to configure MRCP client timers

No
                                       					 option to configure MRCP client timers

HTTP cache
                                       					 Configuration

Various
                                       					 CLIs for HTTP Cache Configuration

Equivalent CLI commands to configure HTTP cache for media files

HTTP
                                       					 timers

Can be configured

Can be configured

Call
                                       					 Throttling

Based on RAI parameters (CPU and memory utilization, DSO, DSP)

Max
                                       					 calls supported by OVA profile.

Cisco VVB supports sending RAI information. For more details, see SIP RAI section.

Audio prompts

All prompts are played from start to end.

Cisco VVB is compliant with VoiceXML, so prompts are queued instead of being played when the Audio element is run. The queued
                                       prompts are played:

When the browser reaches a waiting state such as recognition.

When the browser fetches a resource while the fetchaudio attribute is set on the corresponding fetch element.

When the browser has reached the end of the application.

| Feature | Cisco
                                       					 IOS-VB Configuration | Cisco VVB
                                       					 Configuration |
|---|---|---|
| Service/Application | Service
                                       					 Configuration | Application configuration in Cisco VVB |
| Dial-Peer | Dial peer
                                       					 Configuration | Trigger configuration in Cisco VVB |
| TCL
                                       					 Scripts | CVP OAMP
                                       					 downloaded TCL scripts: bootstrap.tcl CVPSelfService.tcl cvp_ccb_poll.tcl ringtone.tcl ccb
                                             						  tcl scripts | AEF applications. By default, Cisco VVB includes the following prepackaged applications: CVPComprehensive.aef Ringtone.aef Error.aef SelfService.aef VRUComprehensive.aef Note You can’t modify these applications. | Note | You can’t modify these applications. |
| Note | You can’t modify these applications. |
| CVP VXML
                                       					 documents | CVP OAMP
                                       					 downloaded VXML scripts: bootstrap.vxml CVPSelfServiceBootstrap.vxml recovery.vxml | Cisco VVB has prepackaged the VXML document files for various AEF applications. Note You can’t modify these applications. | Note | You can’t modify these applications. |
| Note | You can’t modify these applications. |
| Codec
                                       					 config | Codec
                                       					 defined at dial-peer level | Codec
                                       					 defined at System level |
| MRCP
                                       					 Interface and Configuration | ASR/TTS
                                       					 configuration. voice
                                             						  class uri Using
                                             						  Dial-Peer to load balance ASR/TTS | ASR/TTS server configuration by specifying the hostname or IP Address of speech servers. Load balancing is done on a round-robin basis. |
| Maximum sessions that can be set for a server | No such
                                       					 configuration |
| Weight-based load balancing between various servers configured | Weight-based load balancing isn’t supported. |
| CVP
                                       					 microapps dependency on MRCP v1 | No dependency of CVP microapps on MRCP v1 |
| Option to configure MRCP client timers | No
                                       					 option to configure MRCP client timers |
| HTTP cache
                                       					 Configuration | Various
                                       					 CLIs for HTTP Cache Configuration | Equivalent CLI commands to configure HTTP cache for media files |
| HTTP
                                       					 timers | Can be configured | Can be configured |
| Call
                                       					 Throttling | Based on RAI parameters (CPU and memory utilization, DSO, DSP) | Max
                                       					 calls supported by OVA profile. Cisco VVB supports sending RAI information. For more details, see SIP RAI section. |
| Audio prompts | All prompts are played from start to end. | Cisco VVB is compliant with VoiceXML, so prompts are queued instead of being played when the Audio element is run. The queued
                                       prompts are played: When the browser reaches a waiting state such as recognition. When the browser fetches a resource while the fetchaudio attribute is set on the corresponding fetch element. When the browser has reached the end of the application. |

| Note | You can’t modify these applications. |
|---|---|

| Note | You can’t modify these applications. |
|---|---|