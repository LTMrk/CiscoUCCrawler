---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-161bb20fa7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_1261_staging-guide/ucce_b_1261_staging-guide_chapter_01001.html
retrieved_at: 2026-08-16T20:02:43.576334+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Staging Prerequisites

## Chapter: Staging Prerequisites

# Staging Prerequisites

## System Design
                        	 Specification

Before you begin the
                              		  Unified ICM staging process, ensure that a Unified ICM/Cisco Unified Contact
                              		  Center Enterprise System Design Specification is created and approved.

Persons creating and
                              		  approving this specification must be familiar with the following:

Windows
                                    				Operating System

AD

Security
                                          					 concepts

Network
                                          					 configuration and operation

SQL Server

Enterprise
                                          					 Manager

Query
                                          					 Analyzer

SQL
                                          					 scripting

Unified
                                    				ICM/Cisco Unified Contact Center Enterprise

Unified
                                          					 ICM/Cisco Unified Contact Center Enterprise Nodes (Router, Logger,
                                          					 Administration & Data Server, PGs)

HDS Schema
                                          					 knowledge

Deployment
                                          					 models

The
                                          					 appropriate release of the Contact Center Enterprise Compatibility Matrix and Solution Design Guide for Cisco Unified Contact Center Enterprise .

The System Design
                              		  Specification must contain the following specifications:

Description of
                                    				Unified ICM Sites and Nodes

Data
                                    				Communications Infrastructure

Event
                                    				Notification and Remote Access Points

Naming
                                    				Conventions

IP Addressing
                                    				Scheme

AD Plan,
                                    				including:

AD Sites

Global
                                          					 Catalog Servers

Domain
                                          					 Controllers

Trust
                                          					 Relationships

Domain
                                          					 Members

Standalone
                                          					 Servers

Time Source

DNS Plan (follow Microsoft Guidelines), including:

DNS Servers
                                          					 and Clients

DNS Forward
                                          					 and Reverse Lookup Zones and Records

System Diagrams

Configuration
                                    				Settings, including:

Physical
                                          					 Controller IDs

Logical
                                          					 Controller IDs

Peripheral
                                          					 Controller IDs

Third-party Host
                                    				Forms – A section containing the detailed build information for each server
                                    				containing the entries and values for fields which are different from defaults
                                    				presented during third-party software installation and setup. Some examples of
                                    				this information include: Network Card configuration and binding order, Drive
                                    				Partitioning Information, System Properties, and passwords.

## Platform Hardware and Software

During the System Design phase of the Unified ICM/CCE deployment, you define the hardware specifications, virtualization environment,
                              and third-party software requirements. For supported third-party software, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . For information about Unified ICM/CCE virtualized systems, see the Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

## Set Staging
                        	 Environment

Step 1

Stage all
                                       			 computers in racks or on a work surface.

Step 2

Ensure that all
                                       			 software CDs, driver software, and documentation are in the work area.

Step 3

Ensure that you
                                       			 have all software license numbers available.

Step 4

Ensure that the Unified ICM network is in place and tested. Check that:

All LAN switches are configured for required subnets per the System Design Specification.

All IP Routers are configured as required.

There’s IP connectivity between all subnets.

Required Ethernet connections are in place between Unified ICM software servers and LAN switches.

Required packet prioritization is configured on IP Routers.

Latency is critical for contact center operations, so you must disable the Large Receive Offload (LRO) settings.

Step 5

To disable LRO, log in to the ESXi host or its vCenter with vSphere Client.

Step 6

Select the host and choose Configuration > Advanced Settings .

Step 7

Select Net and scroll down slightly to set the following parameters from 1to 0:

Net.VmxnetSwLROSL

Net.Vmxnet3SwLRO

Net.Vmxnet3HwLRO

Net.Vmxnet2SwLRO

Net.Vmxnet2HwLRO

Step 8

Reboot the ESXi host to activate the changes.

Step 9

Ensure that assigned engineers follow the specifications in these documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html

Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html

Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

| Step 1 | Stage all
                                       			 computers in racks or on a work surface. |
|---|---|
| Step 2 | Ensure that all
                                       			 software CDs, driver software, and documentation are in the work area. |
| Step 3 | Ensure that you
                                       			 have all software license numbers available. |
| Step 4 | Ensure that the Unified ICM network is in place and tested. Check that: All LAN switches are configured for required subnets per the System Design Specification. All IP Routers are configured as required. There’s IP connectivity between all subnets. Required Ethernet connections are in place between Unified ICM software servers and LAN switches. Required packet prioritization is configured on IP Routers. Note Latency is critical for contact center operations, so you must disable the Large Receive Offload (LRO) settings. | Note | Latency is critical for contact center operations, so you must disable the Large Receive Offload (LRO) settings. |
| Note | Latency is critical for contact center operations, so you must disable the Large Receive Offload (LRO) settings. |
| Step 5 | To disable LRO, log in to the ESXi host or its vCenter with vSphere Client. |
| Step 6 | Select the host and choose Configuration > Advanced Settings . |
| Step 7 | Select Net and scroll down slightly to set the following parameters from 1to 0: Net.VmxnetSwLROSL Net.Vmxnet3SwLRO Net.Vmxnet3HwLRO Net.Vmxnet2SwLRO Net.Vmxnet2HwLRO |
| Step 8 | Reboot the ESXi host to activate the changes. |
| Step 9 | Ensure that assigned engineers follow the specifications in these documents: Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html |

| Note | Latency is critical for contact center operations, so you must disable the Large Receive Offload (LRO) settings. |
|---|---|