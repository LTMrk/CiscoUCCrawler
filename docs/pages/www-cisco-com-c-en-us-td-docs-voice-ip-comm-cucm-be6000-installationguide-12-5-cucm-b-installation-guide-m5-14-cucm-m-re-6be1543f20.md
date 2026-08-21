---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-12-5-cucm-b-installation-guide-m5-14-cucm-m-re-6be1543f20
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/12_5/cucm_b_installation-guide-m5-14/cucm_m_rebuilding-a-business-edition-6000.html
retrieved_at: 2026-08-21T22:54:57.597356+00:00
---

Installation Guide for Cisco Business Edition 6000H/M (M5), Release 12.5(CSR 12.7)

# Installation Guide for Cisco Business Edition 6000H/M (M5), Release 12.5(CSR 12.7)

Updated: February 19, 2021

Chapter: Rebuilding a Business Edition 6000 or 7000 Appliance

## Chapter: Rebuilding a Business Edition 6000 or 7000 Appliance

- Rebuilding a Business Edition 6000 or 7000 Appliance

- Hardware and Virtualization Software Reinstall

# Rebuilding a Business Edition 6000 or 7000 Appliance

## Hardware and Virtualization Software Reinstall

To setup hardware, follow the instructions in the install guide for the leveraged base server:

BE6000: Cisco UCS C220 M6 Server Installation and Service Guide

BE7000: Cisco UCS C240 M6 Server Installation and Service Guide

Note the following appliance characteristics:

BE6000/7000 M6 appliances do not ship with Cable Management Arms, only Rack-mounting Kits.

BE6000M (M6) appliance does not ship with any NICs, only motherboard LoM ports.

BE7000M/H (M6) appliances ship with motherboard LoM ports as well as dual NICs (each quad 10-Gigabit-Ethernet copper).

BE6000/7000 M6 appliances ship with latest firmware at time of factory build that is compatible with ESXi 7.0 U1. At install
                                    time, there may be newer firmware available that you can freshen the appliance to.

BE6000M (M6) appliance requires single virtual drive, RAID5, physical disks 1-6.

BE7000M (M6) appliance requires four virtual drives, each RAID5 with 4 physical disks.

BE7000H (M6) appliance requires four virtual drives, each RAID5 with 6 physical disks.

BE6000/7000 M6 appliances require virtual drives to be configured as:

Access Policy Read Write

Read Policy Always Read Ahead

Cache policy as Cached IO

Disk Cache policy as Enabled

Write policy as Write Back Good BBU

The first virtual drive is set as the Boot Drive .

To install and setup VMware vSphere ESXi:

Identify an ESXi version that is compatible with the appliance (minimum is ESX 7.0 U1) as well as the application versions
                                    you are running.

Locate the Cisco UCS-specific installer image for ESXi, or contact TAC for assistance. BE6000/7000 use the same ESXi installer
                                    images as UCS C220 M6S / C240 M6SX.

ESXi must be installed to the first virtual drive (configured as the Boot Drive).

Other ESXi settings can be found at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html .

Apply your license for VMware vSphere ESXi. A license is required, but not included with the appliance.

After hardware setup and ESXi setup, follow steps in Set Up Your Appliance to complete the appliance rebuild.