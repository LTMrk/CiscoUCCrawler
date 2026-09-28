---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sipsip-sbc-html-d427f64d44
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sipsip-sbc.html
retrieved_at: 2026-08-16T15:47:02.065149+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP-to-SIP Supplementary Services for Session Border Controller

## Chapter: SIP-to-SIP Supplementary Services for Session Border Controller

# SIP-to-SIP Supplementary Services for Session Border Controller

The SIP-to-SIP Supplementary Services for Session Border Controller (SBC) feature enhances the terminating and reoriginating
                        of signaling and media between VoIP and video networks.

## Feature Information for SIP-to-SIP Supplementary Services for Session Border Controller

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP-to-SIP Supplementary Services for Session Border Controller

Baseline Functionality

The SIP-to-SIP Supplementary Services for Session Border Controller feature enhances terminating and reoriginating of signaling
                                          and media between VoIP and video networks.

## Information About SIP-to-SIP Supplementary Services for Session Border Controller

### SIP-to-SIP Supplementary Services for Session Border Controller

The SIP-to-SIP Supplementary Services for Session Border Controller (SBC) feature enhances terminating and reoriginating
                              of signaling and media between VoIP and video networks by supporting the following features:

IP Address-Hiding in all Session Initiation Protocol (SIP) messages including supplementary services

Media Flow Around

Hosted Network Address Translation (NAT) Traversal for SIP

Support on Cisco AS5350XM and Cisco AS5400XM platforms

The following features of SIP-to-SIP Supplementary services using REFER/3xx method are enabled by default:

- Message Waiting Indication

- Call Waiting

- Call Transfer (Blind, Consult, Alerting)

- Call Forward (All, Busy, No Answer)

- Distinctive Ringing

- Call Hold/Resume

- Music on Hold

### Digital Signal Processors (DSPs) and SIP Call Hold/Resume

Digital Signal Processors (DSPs) generate and transmit Real-time Transport Protocol (RTP) media packets from a source to
                              a destination address during a SIP call session. However, when a SIP call is put on hold, DSPs stop generating the RTP media
                              packets and resumes generating and transmitting the RTP media packets after the SIP call is resumed. This ensures that the
                              RTP sequence number is continuous from the time of origin until the end of the SIP call.

## How to Configure SIP-to-SIP Supplementary Services for Session Border Controller

To configure the SIP-to-SIP Supplementary Services for Session Border Controller feature, see the Supplementary Services
                           Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide at the following URL: http://www.cisco.com/en/US/docs/ios/voice/fxs/configuration/guide/15_0/fxs_15_0_cg.html
                           .

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP-to-SIP Supplementary Services for Session Border Controller | Baseline Functionality | The SIP-to-SIP Supplementary Services for Session Border Controller feature enhances terminating and reoriginating of signaling
                                          and media between VoIP and video networks. |

| Note | The following features of SIP-to-SIP Supplementary services using REFER/3xx method are enabled by default: |
|---|---|