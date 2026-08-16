---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-f29e9baf00
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_pre-installation-planning-overview126.html
retrieved_at: 2026-08-16T20:03:04.439236+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: Pre-installation Planning Overview

## Chapter: Pre-installation Planning Overview

# Pre-installation Planning Overview

The Unified ICM software is a distributed application that routes telephone calls, web inquiries, and e-mail across geographically
                        distributed contact centers. A typical Unified ICM system includes servers located at several sites, with the number of servers
                        depending on factors such as call volume requirements.

Because the Unified ICM software works with different types of contact center equipment and sometimes one or more carrier
                        networks, some pre-installation planning is necessary to ensure that the Unified ICM installation process proceeds smoothly
                        and on schedule.

This chapter provides an overview of the Unified ICM pre-installation planning process. It also contains a pre-installation
                        planning document roadmap, which provides an order in which you can start the tasks.

## Pre-requisites to Install Unified ICM

To install and run Unified ICM 12.6(1) , you need the following specifications:

Windows Server  - For more information, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

SQL Server  - For more information, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

For information on all supported configurations and versions for Unified ICM in the Unified CCE solution, see the latest Compatibility
                                 Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

For information on supported OVA templates, see the Virtualization Wiki at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

## Planning Process

The Unified ICM pre-installation planning process involves
                              coordinating and scheduling several tasks so you can complete them before the Unified ICM server platforms arrive. You typically
                              prepare each site that is to contain Unified ICM components. Some
                              pre-installation tasks take longer than others. Therefore, start the
                              time-consuming tasks early and continue working in parallel on the other
                              pre-installation tasks.

### Coordinating and
                           	 Scheduling Tasks

Designate one person
                                 		  in your organization to have overall responsibility for coordinating and
                                 		  scheduling the pre-installation planning tasks. This person can also delegate
                                 		  responsibility and assign tasks to people with the applicable expertise. For
                                 		  example, your MIS expert can begin working with Cisco to order the server
                                 		  platforms and at the same time, your data communications expert can start
                                 		  provisioning network facilities at each contact center site.

### Preinstallation Information Road Map

This document provides guidance on topics such as provisioning IXC access, preparing ACDs, and determining the Unified ICM
                                 datacom requirements. In each case, one or more preinstallation tasks are covered. For most tasks, you can find additional
                                 information in other Cisco documents listed in the task outline.

It takes several weeks to provision IXC access so plan accordingly. After you compete the preinstallation tasks, make sure
                                 your contact center equipment (ACDs, PBXs, VRUs) have the necessary software releases and options. While those tasks are in
                                 progress, you can select Unified ICM product options and component platforms and begin preparing the installation sites.

The preinstallation tasks, activities associated with each task, and references to additional information for performing these
                                 tasks are as follows:

Getting Started

Understand the Unified ICM software.

Review the Unified ICM product options.

Determine the Unified ICM configuration.

Provide configuration data for contact center sites.

Document the current contact handling procedures.

See the Unified CCE overview section of this guide and the Administration Guide for Cisco Unified Contact Center Enterprise .

IXC Access

Review ICM/IXC interaction.

Review IXC access specifics.

Determine a fault tolerance strategy for your network links.

See IXC Overview and the relevant Cisco NIC Supplement document.

Switch Preparation

Determine ACD requirements.

Determine CTI and MIS link requirements.

Order required upgrades and enhancements.

See the switch overview, site preparation, and peripheral gateway configuration sections of this guide and the relevant Cisco
                                       ACD Supplement documents.

Product Options and System Integration

Determine product option requirements.

Order any required upgrades or enhancements.

See the CTI planning, site preparation, and ICM application gateway sections of this guide.

Estimating System Size

Enter data using the Unified ICM database sizing tool.

Note the specifications provided by the tool.

Determine the number of servers required.

See the ICM platform planning section of this guide and the discussion of the ICM Database Administration tool (ICMDBA) in
                                       the Administration Guide for Cisco Unified Contact Center Enterprise .

Network and Site Requirements

Determine requirements for Unified ICM networking.

Order any additional network hardware.

Allocate IP addresses.

Meet basic site requirements.

Order any extra cabling or other required equipment.

See the datacom requirements, site preparation, and IP address worksheet sections of this guide.

Preinstallation End-of Life (EOL) Component Check

The ICM Installer checks for installed EOL components before upgrading the server. The installer prompts you for confirmation
                                       to remove them.

See the Release Notes for Cisco Unified Contact Center Enterprise Solutions for a list of EOL components for each release.

### NIC and ACD
                           	 Supplements

The NIC Supplements
                                 		  are reference documents that contain specific information on how the Unified
                                 		  ICM Network Interface Controller (NIC) interfaces with the supported IXC
                                 		  carrier networks. The NIC is the software process that allows the Unified ICM
                                 		  system to communicate with the carrier's intelligent switching network. For
                                 		  detailed technical information, refer to the NIC supplements when you are
                                 		  planning for IXC access.

The ACD Supplements
                                 		  are reference documents that contain the specific information you need to
                                 		  maintain Unified ICM Peripheral Gateways (PGs) in an Unified ICM environment.
                                 		  The PG is the Unified ICM component that provides an interface to proprietary
                                 		  ACD systems.

| Note | This manual deals with Unified ICM. For information on Unified CCE, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
|---|---|