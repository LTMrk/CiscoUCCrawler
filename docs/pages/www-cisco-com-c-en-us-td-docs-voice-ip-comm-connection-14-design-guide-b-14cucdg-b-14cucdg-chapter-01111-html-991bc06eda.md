---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-design-guide-b-14cucdg-b-14cucdg-chapter-01111-html-991bc06eda
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/design/guide/b_14cucdg/b_14cucdg_chapter_01111.html
retrieved_at: 2026-08-17T02:14:31.289780+00:00
---

Design Guide for Cisco Unity Connection 14

# Design Guide for Cisco Unity Connection 14

Updated: August 14, 2024

Chapter: Overview of Cisco Unity Connection SRSV

## Chapter: Overview of Cisco Unity Connection SRSV

# Overview of Cisco Unity Connection SRSV

## Overview of Cisco Unity Connection SRSV

### Introduction

Cisco Unity Connection Survivable Remote Site Voicemail (Unity Connection SRSV) is a backup voicemail solution that allows
                              you to receive voice messages during WAN outages. It works in conjunction with Cisco Unified Survivable Remote Site Telephony
                              (SRST) for providing voicemail service to a branch when the connectivity with the central Unity Connection voicemail service
                              is lost.

Unity Connection SRSV is used in the centralized Cisco Unified Communications Manager and Cisco Unity Connection environment
                              with multiple branch offices or small sites. It provides limited voicemail and auto-attendant features that remain in synchronization
                              with the central Unity Connection voicemail service so that when the WAN outage or failure occurs, the Unity Connection SRSV
                              solution can provide voicemail service to the subscribers at the branch. However, as soon as the network is restored, all
                              the voicemails received by the branch subscribers are automatically uploaded to the central Unity Connection voicemail server.

Unity Connection SRSV solution requires the following two components:

Unity Connection: It is deployed at the central site alongside with Cisco Unified CM to deliver powerful integrated messaging
                                    and voicemail services.

Unity Connection SRSV: The SRSV component is natively a part of Unity Connection which is deployed at the branch site alongside
                                    with Cisco Unified CM Express or SRST. Unity Connection SRSV is hosted on Cisco Integrated Service Routers Generation 2 (ISR
                                    G2) platform using Services Ready Engine Virtualization.

### Supported SRSV
                           	 Topologies

Unity Connection SRSV supports several topologies based on the
                              		configuration of the router. You can deploy either original SRST or
                              		CUCME-as-SRST (also known as SRST Fallback Mode) at branch.

Following figures show three topologies supported by Unity
                              		Connection SRSV:

Figure 16-1 : Shows a
                              		topology in which SRST is deployed at the branch site. If the WAN occurs or
                              		PSTN goes down, Unity Connection SRSV at the branch site provides limited
                              		voicemail support in the failover mode.

Figure 16-2 : Shows a
                              		topology where CUCME-as-SRST (also known as SRST Fallback Mode) is providing
                              		call control at the branch site.

Figure 16-3 : Shows a
                              		topology where multiple CUCME-as-SRST and SRSV devices are paired for load
                              		balancing at the survivable branch site. In this scenario, the administrator
                              		uses Cisco Unified Communications Manager to divide the branch users between
                              		CUCME-SRST-1 and CUCME-SRST-2. The central Unity Connection server detects that
                              		and then sends the appropriate configuration to SRSV-1 and SRSV-2 at the branch
                              		site. In the event of WAN failure, each SRSV device handles calls directed to
                              		it from the paired CUCME-as-SRST device.

### SRSV with High Availability

When you deploy SRSV and the central Unity
                              		Connection node in an HA pair, SRSV functions even if the primary server is
                              		down. There is no additional configuration needed to support this feature, it
                              		is automatically supported.

### Scalability

Each Unity Connection SRSV branch supports 500 users per branch with a maximum of 35 branches per centralized Unity Connection
                              server.

### Software Requirements

Unity Connection SRSV requires Unity Connection minimum version 11.x for both the central Unity Connection server as well
                              as the SRSV branches.

The Unity Connection SRSV administrator workstation must be configured as per the software requirements. For more information,
                              see the " Software Requirements—Administrator Workstations (Unity Connection and Unity Connection SRSV ) " section of the System Requirements for Cisco Unity Connection, Release 11.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/requirements/b_11xcucsysreqs.html .

### Supported
                           	 Hardware

Any supported Unity Connection hardware is suitable for Unity Connection SRSV. For information on the current supported platforms
                              list for the most up to date list of supported hardware, see the “ Specifications for the Virtual Platform Overlays Supported by Unity Connection SRSV ” section of the Cisco Unity Connection 14 Supported Platform List, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/supported_platforms/b_14cucspl.html .

### Limitations

No interaction between existing Unified Messaging Gateway (UMG) based SRSV and Unity Connection based SRSV

No migration from UMG based SRSV

For a complete comparison of Unity Connection SRSV to UMG SRSV, see the comparison guide: http://www.cisco.com/en/US/prod/collateral/voicesw/ps6789/ps5745/ps2237/product_data_sheet0900aecd806bfc37.html .

| Note | If
                                       		you are running SRST at the branch site, you cannot deploy the E-SRST feature. |
|---|---|

| Note | After recovering from a network outage, the bandwidth
                                       		requirements for synchronization to the central Unity Connection server does
                                       		not have any bandwidth requirements. |
|---|---|