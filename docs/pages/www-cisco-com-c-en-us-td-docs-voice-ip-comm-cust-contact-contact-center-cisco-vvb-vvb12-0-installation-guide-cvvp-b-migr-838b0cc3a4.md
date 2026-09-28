---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-0-installation-guide-cvvp-b-migr-838b0cc3a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_0/installation/guide/cvvp_b_migration-guide-1201/cvvp_b_migration-guide-1201_chapter_0100.html
retrieved_at: 2026-08-21T16:28:51.362747+00:00
---

Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

# Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

Updated: January 11, 2019

Chapter: Understanding the Difference

## Chapter: Understanding the Difference

- Understanding the Difference

- Understanding the                              	 Difference

# Understanding the Difference

## Understanding the
                        	 Difference

Following table maps
                           		the differences with respect to basic features and configuration terminology,
                           		between the Cisco IOS-VB and Cisco VVB.

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

Trigger
                                       					 configuration in CiscoVVB

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

AEF
                                       					 applications. By default Cisco VVB has the following applications pre-packaged:

CVPComprehensive.aef

Ringtone.aef

Error.aef

SelfService.aef

VRUComprehensive.aef

Customer cannot modify these.

CVP VXML
                                       					 documents

CVP OAMP
                                       					 downloaded VXML scripts:

bootstrap.vxml

CVPSelfServiceBootstrap.vxml

recovery.vxml

CiscoVVB
                                       					 has pre-packaged the VXML document files for various AEF applications.

Customer
                                                   						cannot modify these.

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

ASR/TTS
                                       					 server configuration by specifying hostname or IP Address of speech servers.

Load
                                       					 balancing done on round-robin basis.

Maximum
                                       					 sessions can be set for a server

No such
                                       					 configuration

Weight
                                       					 based load balancing between various servers configured

Weight
                                       					 based load balancing not supported.

CVP
                                       					 microapps dependency on MRCP v1

No
                                       					 dependency of CVP micorapps on MRCP v1

Option
                                       					 to configure mrcp client timers

No
                                       					 option to configure MRCP client timers

HTTP cache
                                       					 Configuration

Various
                                       					 CLIs for HTTP Cache Configuration

Equivalent
                                       					 CLI commands to configure http cache for media files

HTTP
                                       					 timers

Configurable

Configurable

Call
                                       					 Throttling

Based
                                       					 on RAI parameters (CPU & memory utilization, DSO , DSP)

Max
                                       					 calls supported by OVA profile.

Cisco
                                       					 VVB supports sending RAI information. For more details, see SIP RAI section SIP RAI

| Feature | Cisco
                                       					 IOS-VB Configuration | Cisco VVB
                                       					 Configuration |
|---|---|---|
| Service/Application | Service
                                       					 Configuration | Application configuration in Cisco VVB |
| Dial-Peer | Dial peer
                                       					 Configuration | Trigger
                                       					 configuration in CiscoVVB |
| TCL
                                       					 Scripts | CVP OAMP
                                       					 downloaded TCL scripts: bootstrap.tcl CVPSelfService.tcl cvp_ccb_poll.tcl ringtone.tcl ccb
                                             						  tcl scripts | AEF
                                       					 applications. By default Cisco VVB has the following applications pre-packaged: CVPComprehensive.aef Ringtone.aef Error.aef SelfService.aef VRUComprehensive.aef Note Customer cannot modify these. | Note | Customer cannot modify these. |
| Note | Customer cannot modify these. |
| CVP VXML
                                       					 documents | CVP OAMP
                                       					 downloaded VXML scripts: bootstrap.vxml CVPSelfServiceBootstrap.vxml recovery.vxml | CiscoVVB
                                       					 has pre-packaged the VXML document files for various AEF applications. Note Customer
                                                   						cannot modify these. | Note | Customer
                                                   						cannot modify these. |
| Note | Customer
                                                   						cannot modify these. |
| Codec
                                       					 config | Codec
                                       					 defined at dial-peer level | Codec
                                       					 defined at System level |
| MRCP
                                       					 Interface and Configuration | ASR/TTS
                                       					 configuration. voice
                                             						  class uri Using
                                             						  Dial-Peer to load balance ASR/TTS | ASR/TTS
                                       					 server configuration by specifying hostname or IP Address of speech servers. Load
                                       					 balancing done on round-robin basis. |
| Maximum
                                       					 sessions can be set for a server | No such
                                       					 configuration |
| Weight
                                       					 based load balancing between various servers configured | Weight
                                       					 based load balancing not supported. |
| CVP
                                       					 microapps dependency on MRCP v1 | No
                                       					 dependency of CVP micorapps on MRCP v1 |
| Option
                                       					 to configure mrcp client timers | No
                                       					 option to configure MRCP client timers |
| HTTP cache
                                       					 Configuration | Various
                                       					 CLIs for HTTP Cache Configuration | Equivalent
                                       					 CLI commands to configure http cache for media files |
| HTTP
                                       					 timers | Configurable | Configurable |
| Call
                                       					 Throttling | Based
                                       					 on RAI parameters (CPU & memory utilization, DSO , DSP) | Max
                                       					 calls supported by OVA profile. Cisco
                                       					 VVB supports sending RAI information. For more details, see SIP RAI section SIP RAI |

| Note | Customer cannot modify these. |
|---|---|

| Note | Customer
                                                   						cannot modify these. |
|---|---|