---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-6aaf5916cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_switch-overview125.html
retrieved_at: 2026-08-16T20:03:16.962686+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: Switch Overview

## Chapter: Switch Overview

- Switch Overview

- PG-to-Peripheral                              	 Connections

- Supported ACD Switches

# Switch Overview

Each contact center device (ACD, PBX, or VRU) communicates with an Unified ICM Peripheral
                        Gateway (PG). The PG reads status information from the device and passes it back to the
                        Unified ICM software. The PG runs one or more Peripheral Interface Manager (PIM)
                        processes, which are the software components that communicate with proprietary ACD
                        systems. One PIM is required for each peripheral to which the PG will interface, so if
                        you have two identical ACDs, your PG requires two PIMs.

A single PG can serve multiple peripherals of the same kind. For example, one computer
                        with an Aspect PG and several Aspect PIMs can serve several Aspect ACDs in the contact
                        center. Another PG and PIM on the same computer can serve an VRU.

This chapter provides an overview of how the PG interfaces with ACDs in a contact center
                        environment.

## PG-to-Peripheral
                        	 Connections

Each contact center
                              		  peripheral (ACD, PBX, or VRU) requires a connection to a Cisco Peripheral
                              		  Gateway (PG). The Peripheral Gateway provides a software interface between ACD,
                              		  PBX, and VRU systems and the Unified ICM routing software.

The PG connects to a
                              		  peripheral via the peripheral's computer telephony integration (CTI) link. In
                              		  some cases, the PG also connects to the peripheral's MIS subsystem. The MIS
                              		  subsystem can be on a separate hardware platform or it can be integrated with
                              		  the ACD, PBX, or VRU. The relationship of the Peripheral Gateway to an ACD
                              		  system is shown in the following figure.

Through the CTI
                              		  link, the PG monitors changes in agent status, calculates call handling
                              		  performance statistics, and forwards events to the CallRouter. The MIS
                              		  connection provides additional information such as the mapping of individual
                              		  agents to skill types and the current status of agents (either by themselves or
                              		  relative to a given agent group or skill group). Typical agent states include
                              		  Logged In, Ready, Talking In, Talking Out, and Work Not Ready. The MIS link
                              		  also provides the Unified ICM system with ACD configuration data and historical
                              		  reports.

Each PG has one or
                              		  more connections to the peripheral. The type of connection used depends on the
                              		  type of peripheral. For example, some ACDs use a TCP/IP Ethernet connection,
                              		  while others require X.25 links. Refer to the Cisco Unified ICM Software
                              		  Supported Switches (ACDs) documentation for more information.

## Supported ACD Switches

To ensure that your ACD software version is compatible with Unified ICM software, refer to the Unified CCE compatibility information at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . This document contains the latest information on Unified ICM switch support.

| Note | A single PG can support both ACD PIMs and VRU PIMs, though the ACD PIMs must all be of
                                 the same kind. |
|---|---|

| Note | For more details on how ACDs interface with the Unified ICM software,
                                    		see the appropriate Cisco Unified ICM software ACD Supplement. The ACD
                                    		Supplements provide more technical details on the ICM-to-ACD interface than is
                                    		provided in this document. |
|---|---|