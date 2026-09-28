---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-10-51-cucm-bk-bc403831-00-be6k-install-guide-1-d5c802bb51
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/10_51/CUCM_BK_BC403831_00_be6k-install-guide-1051/CUCM_BK_BC403831_00_be6k-install-guide-1051_appendix_0100.html
retrieved_at: 2026-08-21T22:55:18.703835+00:00
---

Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

# Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

Updated: June 6, 2014

Chapter: Business Edition 6000 Application Requirements

## Chapter: Business Edition 6000 Application Requirements

Contents

- Business Edition 6000 Application Requirements

# Business Edition 6000 Application Requirements

For more information, see Cisco Unified Communications for Midsize Businesses: Virtualization Options Solution Overview and Cisco Business Edition 6000 Co-Residency Policy Requirements Overview at http:/​/​www.cisco.com/​go/​be6000 .

Contents

- Business Edition 6000 Application Requirements

# Business Edition 6000 Application Requirements

For more information, see Cisco Unified Communications for Midsize Businesses: Virtualization Options Solution Overview and Cisco Business Edition 6000 Co-Residency Policy Requirements Overview at http:/​/​www.cisco.com/​go/​be6000 .

| Cisco BE6000 UC Applications | Scale | vCPU | vRAM | vDisk |
|---|---|---|---|---|
| Cisco Unified Communications Manager | 1000 Users | 2 | 4 GB | 1x80GB |
| Cisco Unity Connection | 1000 Users | 1 Note One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. | Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. | 4 GB | 1x160GB |
| Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. |
| UCM IM and Presence Service | 1000 Users | 1 | 2 GB | 1x80GB |
| Cisco Prime Collaboration Provisioning | 1000 Users | 1 | 2 GB | 1x90GB |
| Cisco Unified Contact Center Express | 100 Agents | 2 | 8 GB | 1x146GB |
| Cisco Emergency Responder | 1000 Users | 2 | 4 GB | 1x80GB |
| Cisco Telepresence Video Communication Server  (Expressway) | 100 Video or 200 Audio sessions | 2 | 4 GB | 1x128GB |
| Cisco Conductor | 30 MCU / TS resources and 2400 Call session | 2 | 4 GB | 1x128GB |
| Paging Server | 1000 users | 1 | 4 GB | 1x80GB |
| Cisco Unified Attendant Console | Varies by Edition | 1 | 4 GB | 1x72GB |

| Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. |
|---|---|

| Note | VMware Hypervisor ESXi 5.1 reserves 2GB RAM. |
|---|---|

| Cisco BE6000 UC Applications | Scale | vCPU | vRAM | vDisk |
|---|---|---|---|---|
| Cisco Unified Communications Manager | 1000 Users | 2 | 4 GB | 1x80GB |
| Cisco Unity Connection | 1000 Users | 1 Note One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. | Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. | 4 GB | 1x160GB |
| Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. |
| UCM IM and Presence Service | 1000 Users | 1 | 2 GB | 1x80GB |
| Cisco Prime Collaboration Provisioning | 1000 Users | 1 | 2 GB | 1x90GB |
| Cisco Unified Contact Center Express | 100 Agents | 2 | 8 GB | 1x146GB |
| Cisco Emergency Responder | 1000 Users | 2 | 4 GB | 1x80GB |
| Cisco Telepresence Video Communication Server  (Expressway) | 100 Video or 200 Audio sessions | 2 | 4 GB | 1x128GB |
| Cisco Conductor | 30 MCU / TS resources and 2400 Call session | 2 | 4 GB | 1x128GB |
| Paging Server | 1000 users | 1 | 4 GB | 1x80GB |
| Cisco Unified Attendant Console | Varies by Edition | 1 | 4 GB | 1x72GB |

| Note | One vCPU should be reserved for ESXi scheduler if Cisco Unity Connection is deployed in a VM. |
|---|---|

| Note | VMware Hypervisor ESXi 5.1 reserves 2GB RAM. |
|---|---|