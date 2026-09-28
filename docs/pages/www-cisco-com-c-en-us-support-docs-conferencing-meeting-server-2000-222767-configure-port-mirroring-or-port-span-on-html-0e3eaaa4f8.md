---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-2000-222767-configure-port-mirroring-or-port-span-on-html-0e3eaaa4f8
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-2000/222767-configure-port-mirroring-or-port-span-on.html
retrieved_at: 2026-08-18T23:48:16.935593+00:00
---

Configure Port Mirroring or Port SPAN on CMS 2000

# Configure Port Mirroring or Port SPAN on CMS 2000

### Download Options

Updated: February 13, 2025

Document ID: 222767

Contents

## Contents

## Introduction

This document describes the process and steps needed to configure port mirroring on a Cisco Meeting Server CMS 2000.

## Prerequisites

### Requirements

Physical access to these equipment:

- The Cisco Meeting server (CMS) 2000. It is typically deployed on a Cisco UCS B-Series Blade Server (UCS B200-M4)

- 10GB or 1GB Copper Small Form-factor Pluggable connectors (SFP) ( Cisco GLC-TE  - 1000BASE-T SFP was used in our case. A list of all supported SFPs can be found in the Related Information section)

- Ethernet cables

Cisco recommends that you have knowledge of these topics:

- Basic network functionality

- Basic understanding of UCS servers

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

T hese steps outline the configuration procedure.

Step 1. Access the UCS manager WEB GUI via the UCS management IP.

Step 2 . Select the Equipment tab on the left. Verify which of the two Fabric Interconnect is the Primary and which is the Subordinary. In our example our Primary Fabric Interconnect is B.

Step 3 . Select the Primary Fabric Interconnect. Then navigate to Fixed Module > Ethernet Ports > Port 2 . Typically Port 1 is used as the Uplink for all traffic to and from CMS. So, we can choose to use port 2, 3 or 4. In this example we select Port 2. This is the port on which we apply the SPAN Monitor.

Step 4 . If this port is already configured for some purpose, you must remove any configuration on it and therefore we select the Action Unconfigure . If the port is already unconfigured (which is what we need) then we navigate to the next step (the image shows the correct configuration of an Unconfigured port).

Step 5 . Once this is done, navigate to the LAN > Traffic Monitoring Sessions > Fabric Interconnect B . There we select add and begin the configuration of the SPAN Monitor:

- Name : Give it a name, in our example SPAN-Session

- Admin State : Enable

- Destination : Fabric Interconnect B Port 2 (as this is the port we are going to use to apply the SPAN template on)

- Admin Speed : 1Gbps (as we are using regular ethernet cables to connect to a laptop and our SFP is 1GB)

Based on how the CMS is configured on the UCS, different options can be configured. On typical deployments and in our case, we configure only two additional components for the SPAN Monitor:

Step 6 . Add an Uplink Ethernet Ports:

- Select Source : Fabric Interconnect B Port 1 (It is important to note here that this is the source port we are copying/mirroring traffic from for the SPAN, which must be the port that CMS is using for network traffic to and from CMS towards the network)

- Direction : Both (you can decide whether to capture inbound traffic, outbound traffic or both)

Step 7 . Add a VLAN:

- Select Source : VLAN CMS2000-MEDIA-VLAN (the VLAN your CMS uses for media)

Once you have completed the configuration of the SPAN monitor session, you must see the Operational State of the SPAN Monitor change to UP and the Operational State Reason must show as Active .

You can then connect your laptop to Fabric Interconnect B port 2 of your UCS Blade server and collect traces with Wireshark or tcpdump.

To ensure the SPAN port is configured correctly and applied correctly, the Fabric Interconnect B Port 2 must show you the Overall Status as Active .

To revert everything back just delete the SPAN-Session Monitor.

## Troubleshooting

This section provides information you can use in order to troubleshoot your configuration.

Once you have configured everything, but you are still seeing the Overall Status as Link Down , try to:

- Disable and Re-enable the SPAN Monitor

- Change cable

- Ensure the laptop is accepting the ethernet connection

- Ensure the SFP is being recognised. You must see the details of the SFP in the properties section and must not be seeing in the Additional Info and error regarding the compatibility with the SFP

## Related Information

Cisco UCS Manager System Monitoring Guide, Release 3.1

Cisco UCS 5100 Series Blade Server Chassis Data Sheet

Cisco UCS 6324 Fabric Interconnect Data Sheet

### Revision History

1.0

13-Feb-2025

Initial Release

### Contributed by Cisco Engineers

Hassan Mohseni Pour Samii

TAC

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 13-Feb-2025 | Initial Release |