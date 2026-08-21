---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-telepresence-video-communication-server-vcs-118884-config-vcs--e77dd6da94
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/telepresence-video-communication-server-vcs/118884-config-vcs-00.html
retrieved_at: 2026-08-21T13:39:55.325324+00:00
---

Dial IP Addresses from Endpoints Registered to CUCM with VCS / Expressway Configuration Example

# Dial IP Addresses from Endpoints Registered to CUCM with VCS / Expressway Configuration Example

### Download Options

Updated: March 31, 2016

Document ID: 118884

Contents

## Contents

## Introduction

This document describes how you can dial IP addresses from endpoints registered to Cisco Unified Communications Manager (CUCM) with Cisco Video Communication Server (VCS) or Cisco Expressway as a solution.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Neighbor zones on Cisco VCS / Expressway

- Transforms and search rules on Cisco VCS / Expressway

- Session Initiation Protocol (SIP) route patterns and SIP trunks on CUCM

Note : It is assumed in this document that the traversal zone from the VCS Control / Expressway-C towards the VCS Expressway / Expressway-E is active and that the interworking key is installed on the VCS / Expressway.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco VCS x8.1 and later

- CUCM Release 9 and later

Note : The same document can be used for Expressway series deployments.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background

CUCM does not support IP address dialing. If you want to use IP address dialing, Cisco recommends one of the two procedures described in this article. An example use case would be for endpoints registered to CUCM to dial an H.323 endpoint by IP address.

### Option 1

- Add a suffix to the IP address, so that the string resembles a SIP Uniform Resource Identifier (URI).

- For example, in order to dial the IP address 198.51.100.2 , users will dial 198.51.100.2@domain .

- Admin has to educate users to dial <IP address>@domain. This domain can be either the corporate internal domain or a dummy domain. This document is based on use of the VCS domain.

### Option 2

- Replace the dots with a symbol in order to turn the IP address into a string.

- For example, in order to dial the IP address 198.51.100.2 , users will dial 198*51*100*2 .

Note : In both options, the Expressway-E tries to call the IP address with the H.323 protocol. If the destination endpoint does not support H.323, you must enable SIP UDP. Otherwise keep SIP UDP disabled.

Note : Option 2 can be used either with IP phones or when you dial from the CLI or Web GUI of endpoints that use Tandberg Codec (TC) software . When you try to dial * with Touch Panel or Remote Control, this might not work as the * is automatically converted to . when you use these options in order to dial.

## Configuration

Note : This configuration is applicable to both of the previously stated options.

### CUCM Configuration

On the CUCM, the administrator has to configure a SIP trunk security profile for VCS on port 5060 (this assumes that 5060 is the port used on the VCS towards the CUCM via TCP).

Note : If you use port 5060 / 5061 for Mobile and Remote Access (MRA), use a different TCP port (such as 5075) for the SIP trunk security profile.

Choose System > Security > SIP Trunk Security Profile on CUCM and click Add New .

Create a SIP trunk security profile as shown in this screenshot.

On the CUCM, add a SIP trunk towards the VCS Control/Expressway-C.

Choose Device > Trunk and click Add New .

These trunk settings are design dependent.

### VCS Control Configuration

Create a neighbor zone on the VCS Control / Expressway-C towards CUCM.

Choose Configuration > Zones  > Zones and click New in order to add the zone.

These zone settings are design dependent.

Ensure that the Calls to unknown IP addresses parameter is set to Indirect on the VCS Control / Expressway-C. In order to do so, choose Configuration > Dial Plan > Configuration .

### VCS Expressway Configuration

In the Calls to unknown IP addresses drop-down list, choose Direct on the VCS Expressway / Expressway-E. A search rule is not required on the VCS Expressway / Expressway-E in order to route IP-based calls.

#### Option 1 - Add a Suffix to the IP Address

On CUCM, add a SIP route pattern in order to send calls with the suffix as vcs.domain to the VCS Control/Expressway-C trunk.

Choose Call Routing > SIP Route Pattern and click Add New .

Set the SIP route pattern settings as shown here.

IPV4 Pattern: vcs.domain

On the VCS Control / Expressway-C, transform the strip domain portion of an alias when an IP address is dialed.

Choose Configuration > Dial Plan > Transforms and click New.

Create the transform as shown here.

Pattern String: (.*)\.(.*)\.(.*)\.(.*)@vcs.domain

Replace String: \1.\2.\3.\4

On the VCS Control / Expressway-C you need a search rule that sends the call to the VCS Expressway / Expressway-E when an IP address is dialed.

Choose Configuration > Dial Plan > Search Rules and click New .

Create this search rule towards the VCS Expressway / Expressway-E.

#### Option 2 - Turn the IP Address into a String

On the CUCM add a route pattern to send calls with pattern !*!*!*! to the VCS Control / Expressway-C trunk.

Choose Call Routing > Route/Hunt > Route Pattern and click Add New.

Add a new route pattern as shown here.

Route Pattern: !*!*!*!

Note : The !*!*!*! might cause delays with processing other Route Patterns so care needs to be taken when you use this pattern. A good way would be to put this Route Pattern in a separate partition and only have the endpoints that need to dial IP addresses access to this partition .

On the VCS Control / Expressway-C you need a transform that modifies the alias with "*" to "." when an IP address is dialed.

Choose Configuration > Dial Plan > Transforms and click New.

Create the transform as shown here.

Pattern String: (\d\d?\d?)(\*)(\d\d?\d?)(\*)(\d\d?\d?)(\*)(\d\d?\d?)(.*)

Replace String: \1.\3.\5.\7

On the VCS Control / Expressway-C you need a search rule that sends the call to the VCS Expressway / Expressway-E when an IP address is dialed.

Choose Configuration > Dial Plan > Search Rules and click New .

Create this search rule towards the VCS Expressway / Expressway-E.

Note : If SIP UDP mode is enabled, the VCS Expressway / Expressway-E initiates the SIP call as a native call first. In case the destination device does not respond to the SIP invite, the VCS Expressway / Expressway-E continues to run the SIP UDP call until the standard call negotiation timeout (approximately 32 seconds). It then fall backs to an H.323 interworking call as designed behavior.

## Verify

Use this section to confirm that your configuration works properly.

Once the previous steps are completed, dial the IP address as a string or the IP address with the domain appended (this is dependent on the configuration option you selected) and see if the call to the far end works.

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

Collect detailed System Diagnostic Interface / Signal Distribution Layer (SDI / SDL) logs from the CUCM and "debug level" diagnostic logs from the VCS-Control / Expressway-C and VCS-Expressway / Expressway-E. Provide these logs to the Cisco Technical Assistance Center (TAC) for analysis if the calling does not work after the previous configuration steps are completed.

### Contributed by Cisco Engineers

Alok Jaiswal and Ishan Sambhi

Cisco TAC Engineers.

### This Document Applies to These Products

- TelePresence Video Communication Server (VCS)

- Unified Communications Manager (CallManager)