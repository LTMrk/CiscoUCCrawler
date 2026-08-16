---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-trusted-fw-html-c4e2e705e6
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-trusted-fw.html
retrieved_at: 2026-08-16T15:53:08.437423+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Cisco Unified Communication Trusted Firewall Control

## Chapter: Cisco Unified Communication Trusted Firewall Control

- Cisco Unified Communication Trusted Firewall Control

- Feature Information for Cisco Unified Communication Trusted Firewall Control

- Configure Cisco Unified Communication Trusted Firewall Control

# Cisco Unified Communication Trusted Firewall Control

Cisco Unified Communications Trusted Firewall Control pushes intelligent services onto the network through a Trusted Relay
                        Point (TRP) firewall. TRP is a Cisco IOS service feature, which is similar to the Resource Reservation Protocol (RSVP) agent.
                        Firewall traversal is accomplished using Session Traversal Utilities for NAT (STUN) on a TRP colocated with a Cisco Unified
                        Communications Manager Express (Cisco Unified CME), or a Cisco Unified Border Element.

The version II release introduces the following features:

Noncolocated firewall for UC SIP trunks

Support Firewall traversal for Cisco Unified Border Element call flows in which the media flow through the Media Termination
                              Points such as MTP, Transcoder, or Conference bridge with Trust Relay Point (TRP) enabled.

Firewall traversal for additional Cisco Unified Border Element call flows using STUN.

## Feature Information for Cisco Unified Communication Trusted Firewall Control

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Cisco Unified Communications Trusted Firewall Control

Baseline Functionality

Cisco Unified Communications Trusted Firewall Control pushes intelligent services into the network through Trust Relay Point
                                          (TRP).

The following commands were introduced or modified: stun , stun flowdata agent-id , stun flowdata keepalive , stun flowdata shared-secret , stun usage firewall-traversal flowdata , voice-class stun-usage , stun flowdata catlife .

## Configure Cisco Unified Communication Trusted Firewall Control

To enable this feature, see the Cisco Unified Communications Trusted Firewall Control feature guide.

Detailed command information for the stun , stun flowdata agent-id , stun flowdata keepalive , stun flowdata shared-secret , stun usage firewall-traversal flowdata , voice-class stun-usage , stun flowdata catlife commands are located in the Cisco IOS Voice Command Reference Guide .

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified Communications Trusted Firewall Control | Baseline Functionality | Cisco Unified Communications Trusted Firewall Control pushes intelligent services into the network through Trust Relay Point
                                          (TRP). The following commands were introduced or modified: stun , stun flowdata agent-id , stun flowdata keepalive , stun flowdata shared-secret , stun usage firewall-traversal flowdata , voice-class stun-usage , stun flowdata catlife . |