---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-15-cucm-b-installation-guide-6k-7k-m7-15-cucm--ad76e3c156
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/15/cucm_b_installation-guide-6k_7k_m7_15/cucm_m_rebuilding-a-business-edition-6000-m7.html
retrieved_at: 2026-08-21T22:40:38.900107+00:00
---

Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M7 Appliances, zero factory preload 14X15X-K9-17 / 14X15X-XU-17)

# Installation Guide for Cisco Business Edition 6000 and 7000, Release 15 (M7 Appliances, zero factory preload 14X15X-K9-17 / 14X15X-XU-17)

Updated: June 23, 2025

Chapter: Rebuilding a Business Edition 6000 or 7000 Appliance

## Chapter: Rebuilding a Business Edition 6000 or 7000 Appliance

- Rebuilding a Business Edition 6000 or 7000 Appliance

- Hardware and Virtualization Software Reinstall

# Rebuilding a Business Edition 6000 or 7000 Appliance

## Hardware and Virtualization Software Reinstall

To set up hardware, follow the instructions in the install guide for the leveraged base server:

BE6000: Cisco UCS C220 M7 Server Installation and Service Guide

BE7000: Cisco UCS C240 M7 Server Installation and Service Guide

Note the following appliance characteristics:

BE6000/7000 M7 appliances do not ship with Cable Management Arms, only Rack-mounting Kits.

BE7000/7000 M7 appliances ship with motherboard LOM ports and dual NICs (each quad 10-Gigabit-Ethernet copper).

BE6000/7000 M7 appliances ship with the latest firmware at the time of factory build that is compatible with ESXi 7.0 U3i.
                                    At the install time, there may be newer firmware available that you can freshen the appliance to.

BE6000M (M7) appliance requires a single virtual drive, RAID5, physical disks 1-6.

BE7000M (M7) appliance requires four virtual drives, each RAID5 with 4 physical disks.

BE7000H (M7) appliance requires four virtual drives, each RAID5 with 6 physical disks.

BE6000/7000 M7 appliances require virtual drives to be configured as:

Access Policy Read Write

Read Policy Always Read Ahead

Cache policy as Cached IO

Disk Cache policy as Enabled

Write policy as Write Back Good BBU

The first virtual drive is set as the Boot Drive .

To install and set up VMware vSphere ESXi:

Identify an ESXi version that is compatible with the appliance (minimum is ESX 7.0 U3i) and the application versions you are
                                    running.

Locate the Cisco UCS-specific installer image for ESXi on Broadcom.com. BE6000/7000 use the same ESXi installer images as
                                    UCS C220 M7S / C240 M7SX.

ESXi must be installed to the first virtual drive (configured as the Boot Drive).

Other ESXi settings can be found at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html .

Apply for your license for VMware vSphere ESXi. A license is required, but not included with the appliance.

After hardware setup and ESXi setup, follow the steps in Set Up Your Appliance to complete the appliance rebuild.