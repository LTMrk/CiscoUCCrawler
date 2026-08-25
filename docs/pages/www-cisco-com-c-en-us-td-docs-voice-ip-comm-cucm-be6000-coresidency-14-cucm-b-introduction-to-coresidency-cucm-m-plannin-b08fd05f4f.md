---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-coresidency-14-cucm-b-introduction-to-coresidency-cucm-m-plannin-b08fd05f4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/Coresidency/14/cucm_b_introduction-to-coresidency/cucm_m_planning-for-coresidency.html
retrieved_at: 2026-08-25T11:01:28.816588+00:00
---

Cisco BE6000 and Cisco BE7000 (CSR 14) Coresidency Policy Requirements

# Cisco BE6000 and Cisco BE7000 (CSR 14) Coresidency Policy Requirements

Find Matches in This Book

## Results

Updated: June 14, 2021

Chapter: Planning for Coresidency

## Chapter: Planning for Coresidency

# Planning for Coresidency

## Sizing for Coresidency

When planning a coresident deployment, consider four areas: CPU, RAM, storage, and network.

For details on virtual to physical sizing rules in a coresidency context, see https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html

Co-residency examples may be found at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html#Intro

### CPU

See the CPU/Processor Requirements section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html#Specs . For assistance with aligning with these specs, use the QuoteCollab tool at https://cqc.cloudapps.cisco.com/#/ .

Sum of vCPUs must be less than or equal to the quantity of physical CPU cores.

Some applications will require their virtual machines to have ESXi setting "Latency Sensitivity" set to "High".

Due to Cisco application VM placement rules, no requirement to configure CPU reservations or limits.

### RAM

See the CPU/Processor Requirements section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html#Specs_Ram . For assistance with aligning with these specs, use the QuoteCollab tool at www.cisco.com/go/quotecollab .

Sum of vRAM must be less than or equal to physical RAM (less physical RAM required by ESXi).

The overhead reservation by ESXi hosts is not applicable to BE6000S release 11.0 and older. As BE6000S is a special configuration
                                             with deployment model restrictions, in release 11.0 and older, it does not ship with, or require extra memory for ESXi as
                                             described for other Business Edition models.

### Disk Storage and Performance

Replace entire section with See Storage Requirements & Guidelines section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html#Specs_Storage . For assistance with aligning with these specs, use the QuoteCollab tool at www.cisco.com/go/quotecollab .

Cisco Collaboration applications require max storage latency, min usable space and min IOPS capacity. BE6000/7000 appliance
                                 hardware specs follow these requirements for their targeted capacity points and application mixes. 3rd-party apps must abide
                                 by these rules; e.g. they must not overload the storage system (causing problems with latency or IOPS) and their required
                                 usable space must fit within what the appliance can provide.

### Network

See Network Requirements & Guidelines section at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html#Specs_Network . For assistance with aligning with these specs, use the QuoteCollab tool at www.cisco.com/go/quotecollab .

The total network load of Cisco applications and 3rd-party applications must not exceed the capacity of the appliance's physical
                                 networking interfaces.

Understand the networking requirements of the virtual machines that are deployed on the host and how to set up the host networking
                                 hardware to meet those needs. If we determine that application performance problems are due to networking congestion within
                                 the host, then some VMs must be moved off the host.

| Note | The overhead reservation by ESXi hosts is not applicable to BE6000S release 11.0 and older. As BE6000S is a special configuration
                                             with deployment model restrictions, in release 11.0 and older, it does not ship with, or require extra memory for ESXi as
                                             described for other Business Edition models. |
|---|---|