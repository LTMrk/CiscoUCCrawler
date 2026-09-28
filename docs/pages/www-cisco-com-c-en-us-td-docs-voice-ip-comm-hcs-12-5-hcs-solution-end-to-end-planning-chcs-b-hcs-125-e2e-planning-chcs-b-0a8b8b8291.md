---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-end-to-end-planning-chcs-b-hcs-125-e2e-planning-chcs-b-0a8b8b8291
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/End_to_End_Planning/chcs_b_hcs-125-e2e-planning/chcs_b_hcs-125-e2e-planning_chapter_0111.html
retrieved_at: 2026-09-01T20:56:55.691014+00:00
---

Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

# Cisco Hosted Collaboration Solution, Release 12.5 End-to-End Planning Guide

Updated: June 25, 2019

Chapter: Service Assurance

## Chapter: Service Assurance

# Service Assurance

## Prerequisites

- Review and have access to the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide

- Initial system requirements
                                       				and planned growth

- Data center requirements

- Licensing

- Customer premise equipment

- Service fulfilment
                                       				requirements

## Prime
                        	 Collaboration Assurance Workflow

## Prime Collaboration Assurance Architecture Considerations

- Required interfaces to the Cisco Hosted Collaboration Fulfilment system.

- Cisco Prime Collaboration Assurance NBI. Information on the Prime Collaboration Assurance northbound interfaces, and how to
                                 use them is available at: http://<pc-server-ip>/emsam/nbi/nbiDocumentation.

- Service assurance management when using Cisco Prime Collaboration Assurance.

## Prime Collaboration Assurance Management Considerations

Prime Collaboration Assurance helps you manage Cisco Hosted Collaboration Solution components. Features include:

Support for Unified Communications components including Cisco Unified CM, Unity Connection, and Cisco IM and Presence

End to end monitoring and real-time diagnostics

Multi-customer support in Prime Collaboration voice and video assurance

Customer summary dashboard for per customer summaries- devices and endpoints, alarms, video sessions with alarms, and voice
                                 calls with poor quality

Voice and Video assurance - Telepresence Exchange dashboard shows the health of TelePresence Hosted Infrastructure; CTX cluster,
                                 SBC, Conference Hardware, IVR, Regions, and Resource Pools

Full Contact Center View - dashboard and topology

## Northbound Interface to OSS/BSS Considerations

- The ability to integrate with a MoM to proactively notify operators of issues and facilitates rapid resolution of problems.

- SNMP Traps integrate with existing MoM

- MoM integration for trouble ticketing

- Time-based correlation

- Threshold-based correlation

- Root cause correlation

Voice, Video, and Contact Center Correlation with Built-in rules for the most common use cases.

- The ability to configure correlation engine to generate events based on user defined criteria (for example selecting metrics
                                 and setting up violation rules based on an expected range of values).

- The ability to add event correlation rules on-demand.

## Interface to Cisco
                        	 HCM-F Considerations

- HCM-F through DMA-SA
                                 		  interacts with the Shared Data Repository (SDR) to a source of information
                                 		  about services, devices, and relationships used by Prime Collaboration
                                 		  Assurance.

- HCM-F interacts directly
                                 		  with Prime Collaboration Assurance to provide information from SDR about users.

- To monitor the Prime
                                 		  Collaboration Assurance device discovery process and to highlight any errors
                                 		  that take place during this discovery process.

- Information about devices
                                          			 added directly through the Prime Collaboration Assurance GUI will not be
                                          			 propagated back through HCM-F to the SDR and as a result HCS will not be aware
                                          			 of these devices.

- Changes made in the Prime
                                          			 Collaboration Assurance GUI to an existing device may be overwritten by
                                          			 subsequent updates to the device from HCM-F.

- Basic IP phones
                                          			 (non-Telepresence) are discovered and monitored directly by Prime Collaboration
                                          			 Assurance. TelePresence devices are configured in HCM-F and information about
                                          			 these devices is provided to Prime Collaboration Assurance through DMA-SA.

For information on
                           		the interface to between Prime Collaboration Assurance and HCM-F see the Cisco Hosted Collaboration Mediation Fulfillment Planning Guide .

## Prime
                        	 Collaboration Assurance for all Deployments

Prime Collaboration
                           		Assurance interacts with the service assurance domain manager (DMA-SA) on the
                           		Hosted Collaboration Mediation Fulfillment (HCM-F) system to collect
                           		information about customers, clusters, and applications. Cisco Prime
                           		Collaboration Assurance is a required component for all HCS deployments.

Planning considerations:

Prime Collaboration Assurance runs on any VMware-certified hardware with ESXi 4.1, 5.0, and 5.1 installed. Large and very
                                 large deployment models require ESXi 5.0 or later.

One virtual machine is required to install Prime Collaboration Assurance.

Northbound Interfaces are via Web Services API and SNMP gateway.

Use HCM-F for provisioning customers and devices.

Cisco recommends that Prime Collaboration Assurance be installed in the management VLAN.

Disable hyperthreading in the server (BIOS level) for better performance of Prime Collaboration. This is to avoid CPU-related
                                 issues that may occur when hyperthreading is enabled. See your hardware documentation for information about disabling hyperthreading.

vCPU speed depends on the UCS server or the virtualized hardware.

We do not support oversubscribing server parameters (not using a 1:1 ratio of physical to virtual resources), such as, vCPU
                                 and memory.

The OVA defines configuration of the virtual machine that includes the CPU, memory, disk, and network resources.

We recommend that you install and run Prime Collaboration on Cisco Unified Computing System (UCS), which is VMware-certified.

Prime Collaboration Assurance allows you to configure a second NIC (network adapter). See the Cisco Hosted Collaboration Solution, Customer Onboarding Guide for details.

### Cisco Prime Collaboration Assurance NBI

For details on Cisco Prime Collaboration Assurance NBI support, see Cisco Prime Collaboration Assurance Guide - Advanced .

### NAT Planning Considerations

In an HCS-LE deployment (single customer only), implementing a NAT between your management applications and Unified Communications
                              applications is not required. Be aware that if a NAT is implemented in this scenario that the synthetic call feature will
                              not be available.

### Provisioning Considerations

When you are planning an HCS installation, provisioning is an important consideration. Determine if auto or manual provisioning
                                 will be used. Auto-provisioning of customers and services is available using HCM-F as opposed to manual provisioning.

For Cisco Prime Collaboration Assurance to monitor Unified Communications applications and customer equipment devices, these
                                 devices must be configured with event destinations (SNMP trap, syslog, or RTMT API) to the Prime Collaborations Assurance
                                 server. The Cisco HCS Provisioning Adapter (CHPA) service automatically configures event destinations on the Cisco Unified
                                 Communications Manager. You must manually set up other applications and devices to forward events to the Prime Collaboration
                                 Assurance server.

### Estimate Prime
                           	 Collaboration Assurance OVA Requirements

For information on the OVA requirements for Prime Collaboration Assurance application, see the Cisco Hosted Collaboration Solution Release 12.5 Capacity Planning Guide at http://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/products-implementation-design-guides-list.html .

### Estimate Prime
                           	 Collaboration Assurance Scale Numbers

For Prime Collaboration Assurance scale numbers see the Cisco Hosted Collaboration Solution Release 12.5 Capacity Planning Guide at http://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/products-implementation-design-guides-list.html .

### Acquire Prime Collaboration Assurance Licenses

As a part of service assurance planning, be sure to acquire the necessary Cisco Prime Collaboration Assurance license files.
                                 Prime Collaboration Assurance images are delivered using the Cisco electronic software delivery site and are delivered the
                                 same way as the Cisco Unified Communication Manager software. The licenses are also pulled from this site as a PAK to be registered
                                 to the PC server MAC.

This includes license for Prime Collaboration Analytics if you are using Prime Collaboration Assurance - Advanced 11.5 in
                                 MSP mode. For information on Cisco Prime Collaboration Analytics Licensing, see Cisco Prime Collaboration Analytics guide.

Licensing is ordered based on the endpoint type (Phone or Cisco TelePresence) and the quantity of those endpoints. The type
                                 of an endpoint determines which licenses you need, and the quantity of the endpoints determines the tier and number of licenses
                                 that you need to purchase to manage your network.

### Determine Required
                           	 Bandwidth

Bandwidth
                                 		  considerations are particularly relevant when considering a split data center
                                 		  with on-premise equipment. For more information on bandwidth considerations,
                                 		  see the Data center requirements chapter.

### Determine
                           	 Necessary Ports and Protocols Requirements

For details on ports and protocols, see the System Security chapter in the Cisco Hosted Collaboration Solution Release 12.5 Solution Reference Network Design Guide .

For details on
                                 		  ports and protocols, see http://docwiki.cisco.com/wiki/Required_Ports_for_Prime_Collaboration .

|  |
|---|

| Note | Information about devices
                                          			 added directly through the Prime Collaboration Assurance GUI will not be
                                          			 propagated back through HCM-F to the SDR and as a result HCS will not be aware
                                          			 of these devices. Changes made in the Prime
                                          			 Collaboration Assurance GUI to an existing device may be overwritten by
                                          			 subsequent updates to the device from HCM-F. Basic IP phones
                                          			 (non-Telepresence) are discovered and monitored directly by Prime Collaboration
                                          			 Assurance. TelePresence devices are configured in HCM-F and information about
                                          			 these devices is provided to Prime Collaboration Assurance through DMA-SA. |
|---|---|

| Note | The OVA defines configuration of the virtual machine that includes the CPU, memory, disk, and network resources. We recommend that you install and run Prime Collaboration on Cisco Unified Computing System (UCS), which is VMware-certified. Prime Collaboration Assurance allows you to configure a second NIC (network adapter). See the Cisco Hosted Collaboration Solution, Customer Onboarding Guide for details. |
|---|---|