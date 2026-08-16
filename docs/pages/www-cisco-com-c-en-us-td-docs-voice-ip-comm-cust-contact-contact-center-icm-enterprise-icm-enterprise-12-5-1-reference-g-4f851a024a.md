---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-reference-g-4f851a024a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/reference/guide/ucce_b_acd-supplement-guide-for-avaya-12_5/ucce_b_acd-supplement-guide-for-avaya-12_5_chapter_00.html
retrieved_at: 2026-08-16T19:46:15.369383+00:00
---

Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.5(1) and 12.5(2)

# Cisco Unified ICM ACD Supplement for Avaya Communication Manager, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Overview

## Chapter: Overview

# Overview

## Cisco Unified ICM
                        	 PG and Avaya ACD

The Cisco Unified Intelligent Contact Management (Unified ICM) Peripheral Gateway (PG) supports Avaya ACD using CVLAN or
                           TSAPI Service, running on Avaya Application Enablement Services (AES).

CVLAN and TSAPI are Avaya software options that allow the Unified ICM PG to communicate with the Avaya ACD. Both CVLAN and
                           TSAPI provide the PG with real time call events and allow the PG to query the ECS/MultiVantage/Avaya about splits, trunk groups,
                           and agents.

CVLAN and TSAPI allow the PG to perform post‑routing, station monitoring, and third-party call control.

The CVLAN and TSAPI software can be purchased from Avaya.

The Call Management
                              		  System (CMS) is the Avaya ACD Management Information System (MIS). It
                           		provides the PG with real‑time agent state data for non-station-monitored
                           		agents.

This chapter
                           		describes the options for connecting the Avaya ACD to the Unified ICM PG. To
                           		work with the system software, the Avaya ACD must meet several hardware and
                           		software requirements. This chapter lists the requirements for both CMS and
                           		non-CMS environments.

## Avaya ACD Interface Requirements

A basic, simplexed Unified ICM PG has the following interface requirements:

- You must have at least one CVLAN / TSAPI link on the Avaya ACD. Up to eight CVLAN links can be supported for higher call loads.

If CMS is used, the PG requires one Ethernet connection to the CMS system that is connected to the Avaya ACD.

If CMS is used, the PG requires a Unified ICM Real-Time Adherence (RTA) custom report. This report is developed and provided
                                 by Avaya for the Unified ICM system.

### Avaya ACD with CVLAN TSAPI Service running on Avaya AES

The AES interface allows the PG and Avaya ACD to communicate directly.

In this configuration, CVLAN / TSAPI Service runs on Avaya AES software.

The PG connects directly to the Avaya ACD through an Ethernet LAN. The PG acts as a client while the Avaya ACD acts as the
                              server. An adjunct processor platform is not required in this configuration.

The following figure
                              		shows an example of AES interface with Avaya ACD.

The CMS, if used,
                              		connects to Unified ICM visible LAN through a single Ethernet connection. A
                              		Cisco CMS custom report is installed on the CMS platform (one for each
                              		Peripheral Interface Manager).

The Avaya ACD Interface figure shows
                              		a two‑ACD site. Some sites may have a single ACD only.

Install the PG and
                              		Avaya ACD on the same LAN.

For specifics on AES Server installation and SCO UNIX patch requirements, see the Configuring AES section.

### Call Management System (CMS)

The Avaya CMS provides snapshots of the real-time agent login/logout and non-ACD-related agent state data to the PG through
                              the CMS Ethernet connection. In configurations that use CMS, a custom report is required to ensure that real-time call and
                              agent data is available to the system software.

Avaya has Unified ICM RTA custom reports in Expert Agent Selection (EAS) and non‑EAS versions. The Avaya CMS Professional
                                    Services Group installs the proper Unified ICM custom report (EAS or non‑EAS) on the CMS. To support EAS, the custom report
                                    must have a major revision of at least 3 (for example: 3.x.x).

One custom report must be installed on the CMS for each Peripheral Interface Manager (PIM) on the PG. A PIM is a system software
                                    module that allows communication between a peripheral and the PG. For example, if you have one Avaya ACD and a duplexed PG,
                                    each PG has one PIM. Therefore, the CMS requires two custom reports. If you have two ACDs and a duplexed PG, each PG has two
                                    PIMs. The CMS would therefore require four custom reports (two for each PG).

On a single Avaya ACD duplexed PG environment two CMS reports are installed. However, only one of the reports provide agent
                                    state data to the PG at any given time.

In other words, only one CMS report is running at any given time per Avaya ACD. From a resource utilization perspective on
                                    CMS, a single CMS report (when running) is equivalent to one more Supervisor running a real‑time report.

For more information on CMS report requirements, see the CMS Cisco Real-Time Report section.

Customers who are using CMS with Unified ICM, over 1,000 agents/high call loads, may want to change certain ICM ACD PIM default
                                          settings. Changing settings may improve agent station visibility. But it can also cause a possible increase in message traffic
                                          to the Avaya ACD, switch CPU load, and network traffic between the PG and Central Controller (CC). Customers are supposed
                                          to work with the Cisco Content Security and Control (CSC) to evaluate and mitigate any possible issues. Cisco CSC must refer
                                          to internal documents on PIM registry configuration.

### Avaya “CMS-less”
                           	 Interface

ICM software support Avaya ACD configurations that do not use the Avaya CMS. Typically, this configuration is available only
                              when agent count is less than 1,000 agents. However, the suitability of a CMS-less installation for a site may depend on several
                              factors. This includes agent counts, Busy Hour Call Rate (BHCR), third-party activity, post-routing, and other Avaya CTI applications (if any).

If a CMS-less solution is used, all references to CMS requirements in this document do not apply.

In a CMS-less environment, both Unified ICM and Avaya ACD systems must meet more configuration requirements:

Additional Unified ICM Software Configuration

The following changes are possible using the Configure ICM tools.

It is necessary for you to set all agents in the Unified ICM database.

Map agents to skill groups in the Unified ICM database. The agent to-skill-group mapping must match the Avaya ACD configuration.
                                                In addition, the subgroup must correctly map to the agent’s priority.

It is essential for you to set monitored instruments in the Peripheral Monitor table of the Unified ICM database. Agent stations
                                                are to be monitored.

Set up Peripheral Targets in the Unified ICM database for all Vector Directory Numbers (VDNs) through which monitored calls
                                                flow.

Additional Avaya Requirements

In a PG configuration that does not use CMS, additional configuration is necessary on Avaya.

PG requires skill groups to be monitored to track agent login and logout events. No agents can log in to that skill group
                                    if a skill group is not monitored. PG uses 3PDC or Monitor request API's to monitor a skill group, based on the interface (CVLAN/TSAPI).

Avaya currently restricts one application to third-party domain control of a skill group.

Enable Event Minimization for the CVLAN CTI links used by the Peripheral Gateway. This is not applicable when PG uses TSAPI Interface to connect to AES .

- External applications that alter agent state on the Avaya ACM should use the CTI Server interface of the PG.

### Busy Hour Call
                           	 Rates for Ethernet CTI Link

Each Avaya Ethernet CTI link can support a BHCR. This BHCR is of approximately 32,000 in general use by the PG and excludes
                              Post-Routing or third-party call control. This is an approximate value. This value are affected by following factors:

The number of agents

Anticipated peak busy hour call rate

Average number of CTI events/calls

Number of splits

Trunk groups

VDNs

Establish a
                              		dedicated Ethernet CTI link for Unified ICM application.

For more information on Ethernet BHCRs, see the Ethernet Busy Hour Call Rates section.

## Hardware and
                        	 Software Requirements

In order to work with Unified ICM software, the Avaya ACD must meet the hardware and software requirements listed in these
                           tables.

Releases Supported

Avaya ACD

CVLAN and TSAPI. For specific release information on Avaya ACD, CVLAN and TSAPI see the Cisco ICM Software Supported Switches (ACD) document.

Features Required

Call
                                       				Management System (CMS)

For specific
                                       				release information for CMS, see the Cisco ICM
                                          				  Software Supported Switches (ACD) document.

Call Vectoring

CTI Monitoring

CTI Host-Based
                                       				Routing (only for systems using Unified ICM Post-Routing)

Cisco Unified
                                       				ICM real-time adherence custom report (developed and provided by Avaya for
                                       				Cisco). The CMS requires one report for each PIM in service on the PG.

Performance

CMS minimum
                                       				refresh rate: 3 seconds

Releases Supported

Avaya ACD

CVLAN and

TSAPI

For more information on Avaya ACD

CVLAN

and TSAPI support, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Features Required

Call Vectoring

CTI Monitoring

CTI Host-Based
                                       				Routing (only for systems using Unified ICM Post-Routing)

### Supported Unified
                           	 ICM Software Features

The 
                              		Avaya PG 
                              		supports the following 
                              		Unified ICM software features:

Pre-Routing

Post-Routing

Enterprise CTI
                                    			 (includes third-party call control)

Agent reporting

Duplexed PG
                                    			 implementation

The Avaya PG does not support Unified ICM integration with the Avaya ProLogix System.

PIM supports a maximum of eight CTI links per CVLAN and a maximum of two CVLANs.

| Note | Avaya ACD is used
                                    		across this document to represent the different names used by Avaya for their
                                    		platform. Some of these names are Avaya Aura Communication Manager, Avaya
                                    		Communication Manager, MultiVantage, Definity, and so on. |
|---|---|

| Note | A configuration without the CMS may be possible, subject to the restrictions listed in  Avaya "CMS-less" Interface later
                                    in this chapter. If a "CMS-less" solution is possible, all references to CMS requirements in this document do not apply. |
|---|---|

| Note | Customers who are using CMS with Unified ICM, over 1,000 agents/high call loads, may want to change certain ICM ACD PIM default
                                          settings. Changing settings may improve agent station visibility. But it can also cause a possible increase in message traffic
                                          to the Avaya ACD, switch CPU load, and network traffic between the PG and Central Controller (CC). Customers are supposed
                                          to work with the Cisco Content Security and Control (CSC) to evaluate and mitigate any possible issues. Cisco CSC must refer
                                          to internal documents on PIM registry configuration. |
|---|---|

| Note | If a CMS-less solution is used, all references to CMS requirements in this document do not apply. In a CMS-less environment, both Unified ICM and Avaya ACD systems must meet more configuration requirements: Additional Unified ICM Software Configuration The following changes are possible using the Configure ICM tools. It is necessary for you to set all agents in the Unified ICM database. Map agents to skill groups in the Unified ICM database. The agent to-skill-group mapping must match the Avaya ACD configuration.
                                                In addition, the subgroup must correctly map to the agent’s priority. It is essential for you to set monitored instruments in the Peripheral Monitor table of the Unified ICM database. Agent stations
                                                are to be monitored. Set up Peripheral Targets in the Unified ICM database for all Vector Directory Numbers (VDNs) through which monitored calls
                                                flow. |
|---|---|

| Releases Supported | Avaya ACD CVLAN and TSAPI. For specific release information on Avaya ACD, CVLAN and TSAPI see the Cisco ICM Software Supported Switches (ACD) document. |
|---|---|
| Features Required | Call
                                       				Management System (CMS) For specific
                                       				release information for CMS, see the Cisco ICM
                                          				  Software Supported Switches (ACD) document. |
| Call Vectoring |
| CTI Monitoring |
| CTI Host-Based
                                       				Routing (only for systems using Unified ICM Post-Routing) |
| Cisco Unified
                                       				ICM real-time adherence custom report (developed and provided by Avaya for
                                       				Cisco). The CMS requires one report for each PIM in service on the PG. |
| Performance | CMS minimum
                                       				refresh rate: 3 seconds |

| Releases Supported | Avaya ACD CVLAN and TSAPI For more information on Avaya ACD CVLAN and TSAPI support, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . |
|---|---|
| Features Required | Call Vectoring |
| CTI Monitoring |
| CTI Host-Based
                                       				Routing (only for systems using Unified ICM Post-Routing) |

| Note | The Avaya PG does not support Unified ICM integration with the Avaya ProLogix System. PIM supports a maximum of eight CTI links per CVLAN and a maximum of two CVLANs. |
|---|---|