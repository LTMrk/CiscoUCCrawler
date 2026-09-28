---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-cube-dp-html-bb9f39b109
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_cube-dp.html
retrieved_at: 2026-08-16T15:44:47.678683+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure Dial Peers

## Chapter: Configure Dial Peers

# Configure Dial Peers

## Overview

Cisco Unified Border Element (CUBE) allows VoIP-to-VoIP connection by routing calls from one VoIP dial peer to another. VoIP interworking is achieved by connecting
                           an inbound dial peer with an outbound dial peer.

All CUBE Enterprise deployments must have signaling and media bind statements that are specified at the dial-peer or Voice Class Tenants
                                       level. For voice call tenants, you must apply tenants to dial-peers used for CUBE call flows if these dial-peers do not have bind statements that are specified.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

A dial peer is a static routing table, mapping phone numbers to interfaces or IP addresses.

A call leg is a logical connection between two routers or between a router and a VoIP endpoint. A dial peer is associated
                           or matched to each call leg according to attributes that define a packet-switched network, such as the destination address.

Voice-network dial peers are matched to call legs based on configured parameters, after which an outbound dial peer is provisioned
                           to an external component using the component's IP address. For more information, refer to the Dial Peer Configuration Guide .

Dial-peer matching is done based on the VRF ID associated with a particular interface. For more information, see Inbound Dial-Peer Matching Based on Multi-VRF .

In CUBE , dial peers are classified as LAN dial peers and WAN dial peers based on the connecting entity from which CUBE sends or receives calls.

A dial peer is used to send or receive calls between CUBE and the PBX (PBX)—a system of phone extensions within enterprise. Following are examples of inbound and outbound dial peers:

An another set of dial peer is used to send or receive calls between CUBE and the SIP trunk provider. Given below are examples of inbound and outbound dial peers.

## Preferences

The following is the
                           		order in which inbound dial-peer is matched for SIP call-legs:

voice class uri URI-class-identifier with incoming uri { via } URI-class-identifier

voice class uri URI-class-identifier with incoming uri { request } URI-class-identifier

voice class uri URI-class-identifier with incoming uri { to } URI-class-identifier

voice class uri URI-class-identifier with incoming uri { from } URI-class-identifier

incoming called-number DNIS-string

answer-address ANI-string

The following is the order in which outbound dial-peer is matched for SIP call-legs:

destination route-string

destination URI-class-identifier with target carrier-id string

destination-pattern with target carrier-id string

destination URI-class-identifier

destination-pattern

target carrier-id string

CUCME System dial peers take preference over configured SIP Dail peers.

## Configure Inbound and Outbound Dial-Peer Matching

The following commands are used for inbound and outbound dial peer matching:

This command uses the destination number that was called to match the incoming call leg to an inbound dial peer. This number
                                       is called the Dialed Number Identification Service (DNIS) number.

This command uses the calling number to match the incoming call leg to an inbound dial peer. This number is called the originating
                                       calling number or Automatic Number Identification (ANI) string.

This
                                       				  command uses the inbound call leg to the inbound dial peer.

ANI string
                                       				  for inbound

This command
                                       				  uses a group of incoming called (DNIS) or incoming calling (ANI) number
                                       				  patterns to match the inbound call leg to an inbound dial peer.

The command
                                       				  calls a globally defined voice class identifier where the E.164 pattern groups
                                       				  are configured.

When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures.

This command uses the directory URI (Uniform Resource Identifier) number of an incoming INVITE from a SIP entity to match
                                       an inbound dial peer. This directory URI is part of the SIP address of a device.

The command calls a globally defined voice class identifier where the directory URI is configured.

Directory
                                       				  URI

This
                                       				  command uses DNIS string to match the outbound call leg to the outbound dial
                                       				  peer.

ANI string
                                       				  for inbound

This command
                                       				  uses the directory URI (Uniform Resource Identifier) number to match the
                                       				  outgoing call leg to an outgoing dial peer. This directory URI is part of the
                                       				  SIP address of a device.

The command
                                       				  actually refers to a globally defined voice class identifier where the
                                       				  directory URI is configured.

This command
                                       				  uses a group of destination number patterns to match the outbound call leg to
                                       				  an outbound dial peer.

The command
                                       				  calls a globally defined voice class identifier where the E.164 pattern groups
                                       				  are configured.

| Note | All CUBE Enterprise deployments must have signaling and media bind statements that are specified at the dial-peer or Voice Class Tenants
                                       level. For voice call tenants, you must apply tenants to dial-peers used for CUBE call flows if these dial-peers do not have bind statements that are specified. |
|---|---|

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Note | CUCME System dial peers take preference over configured SIP Dail peers. |
|---|---|

| Command in
                                    				Dial-Peer Configuration | Description | Call Setup
                                    				Element |
|---|---|---|
| incoming called-number DNIS-string | This command uses the destination number that was called to match the incoming call leg to an inbound dial peer. This number
                                       is called the Dialed Number Identification Service (DNIS) number. | DNIS
                                    				number |
| answer-address ANI-string | This command uses the calling number to match the incoming call leg to an inbound dial peer. This number is called the originating
                                       calling number or Automatic Number Identification (ANI) string. | ANI string |
| destination-pattern ANI-string | This
                                       				  command uses the inbound call leg to the inbound dial peer. | ANI string
                                       				  for inbound |
| { incoming called \| incoming
                                          					 calling } e164-pattern-map pattern-map-group-id | This command
                                       				  uses a group of incoming called (DNIS) or incoming calling (ANI) number
                                       				  patterns to match the inbound call leg to an inbound dial peer. The command
                                       				  calls a globally defined voice class identifier where the E.164 pattern groups
                                       				  are configured. Note When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. | Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. | E.164
                                    				Patterns |
| Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. |
| voice class uri URI-class-identifier with incoming uri { from \| request \| to \|
                                          					 via } URI-class-identifier | This command uses the directory URI (Uniform Resource Identifier) number of an incoming INVITE from a SIP entity to match
                                       an inbound dial peer. This directory URI is part of the SIP address of a device. The command calls a globally defined voice class identifier where the directory URI is configured. | Directory
                                       				  URI |

| Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. |
|---|---|

| Dial-Peer
                                    				Command | Description | Call Setup
                                    				Element |
|---|---|---|
| destination-pattern DNIS-string | This
                                       				  command uses DNIS string to match the outbound call leg to the outbound dial
                                       				  peer. | DNIS
                                    				string for outbound ANI string
                                       				  for inbound |
| destination URI-class-identifier | This command
                                       				  uses the directory URI (Uniform Resource Identifier) number to match the
                                       				  outgoing call leg to an outgoing dial peer. This directory URI is part of the
                                       				  SIP address of a device. The command
                                       				  actually refers to a globally defined voice class identifier where the
                                       				  directory URI is configured. | Directory
                                    				URI |
| destination e164-pattern-map pattern-map-group-id | This command
                                       				  uses a group of destination number patterns to match the outbound call leg to
                                       				  an outbound dial peer. The command
                                       				  calls a globally defined voice class identifier where the E.164 pattern groups
                                       				  are configured. | E.164
                                    				patterns |