---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-virtual-chcs-b-cisco-collaboration-on-virtual-servers-chcs-m-preparatio-830566ced8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/virtual/chcs_b_cisco-collaboration-on-virtual-servers/chcs_m_preparation.html
retrieved_at: 2026-08-17T00:09:24.631053+00:00
---

Cisco Collaboration on Virtual Servers

# Cisco Collaboration on Virtual Servers

Updated: November 18, 2020

Chapter: Preparation

## Chapter: Preparation

# Preparation

## Introduction

This book provides an overview of how to install and migrate to virtual servers for Cisco Collaboration applications using
                              Tested Reference Configurations.

## Installation and Migration Scenarios

For ordering information and part numbers, see the Business Edition datasheets at https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html or https://www.cisco.com/c/en/us/products/unified-communications/business-edition-7000/index.html and the Tested Reference Configurations at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html#trc .

TRC Capacity

Form Factor

TRC Name*

Appliance Based on this TRC**

Extra-Large TRC

2RU rack-mount server

UCS C260 M2 TRC#1 (End of Sale)

N/A

Large TRC

2RU rack-mount server

UCS 240 M5SXTRC#2

Cisco Business Edition 7000H (M5)

UCS C240 M4SX TRC#1

Cisco Business Edition 7000H (M4)

UCS C240 M3S TRC#1 (End of Sale)

N/A

Medium TRC

2RU rack-mount server

UCS 240 M5SX TRC#1

Cisco Business Edition 7000M (M5)

UCS C240 M4S2 TRC#1

Cisco Business Edition 7000M (M4)

UCS C240 M3S TRC#2 (End of Sale)

Cisco Business Edition 7000M (M3)

1RU rack-mount server

UCS C220 M3S TRC#1 (End of Sale)

N/A

2RU rack-mount server

UCS C210 M2 TRCs #1,2,3 (End of Sale)

N/A

UCS C210 M1 TRCs #1,2,3,4 (End of Sale)

N/A

Small Plus TRC

1RU rack-mount server

UCS220 M5SX TRC#2

Cisco Business Edition 6000H (M5)

UCS C220 M4S TRC#2

Cisco Business Edition 6000H (M4)

UCS C220 M3S TRC#3 (End of Sale)

Cisco Business Edition 6000H (M3)

Small TRC

1RU rack-mount server

UCS C220 M5SX TRC#1

Cisco Business Edition 6000M (M5)

UCS C220 M4S TRC#1

Cisco Business Edition 6000M (M4)

* When purchased as a UC on UCS TRC, there is no factory-setup or factory-installation of the hardware or software. Follow
                           instructions in this doc for first time setup or rebuilds.

** When purchased as a Cisco Business Edition solution, the hardware is factory-setup and the software is factory-installed.
                           For first-time setup, DO NOT follow the instructions in this doc or you will overwrite the preload. Instead, follow the Cisco
                           Business Edition Installation Guides at either https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html or https://www.cisco.com/c/en/us/products/unified-communications/business-edition-7000/index.html . Follow the instructions in this document only if you have to rebuild a BE6000 or BE7000 server from scratch.

TRC Capacity

Form Factor

TRC Name

Extra-Extra-Large Blade TRC

Full-width blade server

UCS B440 M2 TRC#1 (End of Sale)

Extra-Large Blade TRC

Half-width blade server

UCS B230 M2 TRC#1 (End of Sale)

Large Blade TRC

Half-width blade server

UCS B200 M4 TRC#1

UCS B200 M3 TRC#1 (End of Sale)

Medium Blade TRCs

Half-width blade server

UCS B200 M2/M1 TRCs (End of Sale)

TRC Capacity

Form Factor

TRC Name

Appliance Based on this TRC**

Extra-Small TRC

Single-wide blade server for Cisco Integrated Services (Cisco ISR)

UCS E160S M3 TRC#1

N/A

Extra-Small TRC

Double-wide blade server for Cisco Integrated Services (Cisco ISR)

UCS E160D M2 TRC#1

Blade server component of Cisco Business Edition 6000S (M2) appliance

Cisco Business Edition 6000S appliance is End of Sale.

* When purchased as a UC on UCS TRC, the hardware definition is only for the UCS E-Series blade server and not for the Cisco
                           ISR router housing the server. There is also no factory-setup or factory-installation of the hardware or software. Follow
                           instructions in this doc for first-time setup or rebuilds of the blade server. See http://www.cisco.com/go/isr for documentation on Cisco ISR routers.

** When purchased as a Cisco Business Edition solution, the Cisco ISR router and UCS E-Series blade server hardware are factory-setup
                           and the software is factory-installed. For first-time setup, DO NOT follow the instructions in this doc or you will overwrite
                           the preload. Instead, follow the Cisco Business Edition 6000 Installation Guides at https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html . Follow the instructions in this document only if you have to rebuild a BE6000 or BE7000 server from scratch.

TRC Capacity

Form Factor

TRC Name

Large HyperFlex TRCs

1RU rack-mount HyperFlex node

HX220c M5SX TRC#1

Large HyperFlex TRC

2RU rack-mount HyperFlex node

HX240c M4SX TRC#1

## System Requirements

This document is for virtualized Cisco UCS servers and Cisco HyperFlex configured as Tested Reference Configurations (TRCs) for the UC on UCS. For more information see http://www.cisco.com/go/virtualized-collaboration .

For newly purchased/installed Cisco Business Edition 6000 and 7000 appliance servers, do not follow the procedures in this
                                    document because your server ships with factory-setup hardware and preloaded software. If you follow the procedures in this
                                    document, you will overwrite the preloaded software and licensing. Instead, use the Cisco Business Edition 6000 or 7000 Installation
                                    Guide at https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html or https://www.cisco.com/c/en/us/products/unified-communications/business-edition-7000/index.html . Follow this document only if you must rebuild your server from scratch such as recovering from a catastrophic event.

If you want to deploy Cisco Collaboration on a virtualized 3 rd -party Specs-based server or Cisco UCS Specs-based server, see the application support information at http://www.cisco.com/go/virtualized-collaboration , and the Specs-based support information at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html . Installation procedures will vary from this document and can be found at vmware.com, http://www.cisco.com/go/ucs , or the 3 rd -party server vendor's website.

Additional detail on supported virtualization software vendors, products, versions and features can be found at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html .

To run Cisco UCS servers or HyperFlex nodes, your system must meet the requirements listed in the following table.

Supported Application Co-residency and Virtual-to-Physical Sizing

See the application links at http://www.cisco.com/go/virtualized-collaboration .

See sizing information at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html and http://www.cisco.com/go/vmpt .

Supported Virtual Machine Configuration

Refer to the documentation at: http://www.cisco.com/go/virtualized-collaboration

To ensure that the VMs are correctly configured, use the Cisco-provided OVA template to create VMs. Refer to Download Virtual Machine Templates (OVA Templates)

For more information about VM configurations, refer to the documentation at: http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html#ova .

Supported virtualization software vendors, products, versions and features

See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html .

Supported hardware

See http://www.cisco.com/go/virtualized-collaboration and http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html .

CPU and RAM over subscription

None

Storage capacity and IOPS requirements

See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html#storage and the application links at http://www.cisco.com/go/virtualized-collaboration

To operate Cisco UCS servers successfully, you should have the experience and skills to manage a host server running VMware
                              ESXi.

## External Media for Cisco Collaboration Applications

Cisco UCS servers use "soft media" such as ISO or FLP (virtual floppy) for procedures that require external media (such as installation and upgrade). Physical
                              external devices such as USB drives are not supported.

Backup and restore for Cisco Collaboration applications are not supported on soft media.

The virtual USB interface is not supported for Cisco Collaboration applications running on VMware. The following are examples
                              of differences in external media support between non-virtualized Cisco Media Convergence servers and virtualized Cisco UCS
                              servers:

Install logs cannot be dumped to a USB key. These logs are dumped to a file through the serial port of the VM.

The answer file that is generated by the Answer File Generator (platformConfig.xml) cannot be read from a USB key to perform
                                    an unattended installation. Instead, you must put the answer file into an FLP image to be mounted in the floppy drive.

USB tape drive backup is not supported. Use SFTP instead.

Music On Hold through a USB connection is not supported. Use multicast MOH instead.

## Requirements for Cisco Tested Reference Configuration Installation

This section describes how to prepare to install a Cisco UCS Server in a standalone configuration (it is not in a datacenter).

If your server is ordered as a Cisco Business Edition 6000 or Cisco Business Edition 7000 appliance, the server ships with
                                       factory-setup hardware and factory-preloaded software. DO NOT follow the configuration procedures that are outlined in this
                                       document or you will overwrite the preloaded software. Follow this document only if you must rebuild your server from scratch.
                                       Unless you are rebuilding your server from scratch, such as recovering from a catastrophic situation, use the Installation
                                       Guides for Cisco Business Edition 6000 or 7000 at https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html or https://www.cisco.com/c/en/us/products/unified-communications/business-edition-7000/index.html .

Cisco suggests that you allocate the following resources before installation:

Space in a rack to receive the Business Edition appliance, Cisco C-Series rack-mount server, HX-Series HyperFlex nodes (with
                                 their UCS 6200 Fabric Interconnect Switches), Cisco ISR housing UCS E-Series blade server, or UCS 5100 Blade Server Chassis
                                 housing UCS B-Series blade server (and its UCS 6300/6200/6100 Fabric Interconnect Switches).

Ethernet ports on a switch close to the Cisco UCS Server or HyperFlex node. For port details specific to your hardware, see
                                 the table that follows.

An IP address for Cisco IMC or UCS Manager management. If the dedicated port is used, attach it to the appropriate LAN.

A VLAN ID and IP address for the host. This address is the Cisco UCS Server ESXi management address.

A hostname and configured DNS, if desired, for the hostname.

VLAN IDs and IP addresses for the VMs.

Cisco UCS Server

Ethernet Port Allocation

For each HyperFlex cluster node:

One motherboard CIMC management port (not used)

Two motherboard LOM ports

Two 40-Gigabit ports (Cisco VIC)

HX240c M4SX TRC1 (Large HyperFlex TRC)

For each node:

One motherboard CIMC management port (not used)

Two motherboard LOM ports

Two 10-Gigabit ports (Cisco VIC)

Minimum system requires four nodes and two 6200 Fabric Interconnect switches.

UCS C240 M5SX TRC2 (Large TRC / BE7000H M5)

Eleven Ethernet ports:

One 1 GbE LOM port for dedicated CIMC management.

Eight 1 GbE ports for quad-port Intel NICs for network access.

Two 10 GbE LOM ports for network access.

UCS C240 M5SX TRC1 (Medium TRC / BE7000M M5)

One 1 GbE LOM port for dedicated CIMC management.

Eight 1 GbE ports for quad-port Intel NICs for network access.

Two 10 GbE LOM ports for network access.

UCS C220 M5SX TRCs (Small TRC / BE6000M M5 and Small Plus TRC / BE6000H M5)

For Small TRC:

Three Ethernet ports:

One 1 GbE LOM port for dedicated CIMC management.

Two 10 GbE LOM ports for network access.

For Small Plus or Medium TRC:

Seven Ethernet ports:

One 1 GbE port for dedicated CIMC management.

Four 1 GbE ports for quad-port Intel NICs.

Two 10 GbE LOM ports for network access.

UCS E160S M3 TRC1(Extra-Small TRC)

3 external (front of E160D M2) Ethernet ports:

One "M" port for dedicated CIMC management. CIMC is also accessible via the following internal ports:

Two ports for LAN access

The two internal ports of the UCS E-Series server are to ISR backplane for connectivity to other ISR interfaces.

(End of Sale) UCS C240 M4SX TRC1 (Large TRC / BE7000H M4)

Eleven ethernet ports:

One port for dedicated CIMC management.

Eight ports for quad-port Intel NICs.

Two ports for the LOM, if required.

(End of Sale) UCS C260 M2 TRC1 (Extra-Large TRCs)

Ten Ethernet ports:

One port for dedicated Cisco Integrated Management Controller (CIMC) management

Four ports for quad-port Intel NICs

Two ports for the LAN on Motherboard (LOM)

Two 10-Gigabit Modular LOM

(End of Sale) UCS C240 M4S2 TRC1 (Medium TRC / BE7000M M4)

Eleven ethernet ports:

One port for dedicated CIMC management.

Eight ports for quad-port Intel NICs.

Two ports for the LOM, if required.

(End of Sale) UCS C240 M3S TRC1 (Large TRC)

Eleven Ethernet ports:

One port for dedicated CIMC management

Eight ports for quad-port Intel NICs

Two ports for the LOM, if necessary.

(End of Sale) UCS C240 M3S TRC2 (Medium TRC / BE7000M M3)

Eleven Ethernet ports:

One port for dedicated CIMC management

Eight ports for quad-port Intel NICs

Two ports for the LOM, if necessary.

(End of Sale) UCS C210 M2/M1 TRCs (Medium TRCs)

Seven Ethernet ports:

One port for dedicated CIMC management

Four ports for quad-port Intel NICs

Two ports for the LOM

(End of Sale) UCS C220 M4S TRCs (Small TRC/ BE6000M M4 and Small Plus TRC / BE6000H M4)

For Small TRC:

Three ethernet ports:

One port for dedicated CIMC management.

Two ports for the LOM, if required.

For Small Plus or Medium TRC:

Seven ethernet ports:

One port for dedicated CIMC management.

Four ports for quad-port Intel NICs.

Two ports for the LOM, if required.

(End of Sale) UCS C220 M3S TRCs (Small TRC / BE6000M M3, Small Plus TRC / BE6000H M3 and Medium TRC)

For Small TRC:

Three Ethernet ports:

One port for dedicated CIMC management

Two ports for the LOM, if necessary.

For Small Plus or Medium TRC:

Seven Ethernet ports:

One port for dedicated CIMC management

Four ports for quad-port Intel NICs

Two ports for the LOM, if necessary.

(End of Sale) UCS C200 M2 TRC1 (Small TRC / BE6000M M2)

Three Ethernet ports:

One port for dedicated CIMC management

Two ports for the LOM

(End of Sale) UCS E160D M2 TRC1 (Extra-Small TRC / BE6000S M2)

3 "external" (front of E160D M2) ethernet ports:

One "M" port for dedicated CIMC management (CIMC is also accessible via the "internal" ports described below)

Two ports for LAN access.

The two "internal" ports of the UCS E-Series server are to ISR backplane for connectivity to other ISR interfaces.

| Note | For Cisco Business Edition 6000 and 7000 appliance servers, do not follow the procedures in this document as the appliance
                                       servers ship with factory-setup hardware and factory-preloaded software and you will overwrite the preloaded software. Instead,
                                       use the Cisco Business Edition 6000 or 7000 Installation Guide at https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/tsd-products-support-series-home.html or https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/tsd-products-support-series-home.html . Follow this document only if you must rebuild your appliance server from scratch, such as after hardware replacement or
                                       recovering from a catastrophic event. |
|---|---|

| TRC Capacity | Form Factor | TRC Name* | Appliance Based on this TRC** |
|---|---|---|---|
| Extra-Large TRC | 2RU rack-mount server | UCS C260 M2 TRC#1 (End of Sale) | N/A |
| Large TRC | 2RU rack-mount server | UCS 240 M5SXTRC#2 | Cisco Business Edition 7000H (M5) |
| UCS C240 M4SX TRC#1 | Cisco Business Edition 7000H (M4) |
| UCS C240 M3S TRC#1 (End of Sale) | N/A |
| Medium TRC | 2RU rack-mount server | UCS 240 M5SX TRC#1 | Cisco Business Edition 7000M (M5) |
| UCS C240 M4S2 TRC#1 | Cisco Business Edition 7000M (M4) |
| UCS C240 M3S TRC#2 (End of Sale) | Cisco Business Edition 7000M (M3) |
| 1RU rack-mount server | UCS C220 M3S TRC#1 (End of Sale) | N/A |
| 2RU rack-mount server | UCS C210 M2 TRCs #1,2,3 (End of Sale) | N/A |
| UCS C210 M1 TRCs #1,2,3,4 (End of Sale) | N/A |
| Small Plus TRC | 1RU rack-mount server | UCS220 M5SX TRC#2 | Cisco Business Edition 6000H (M5) |
| UCS C220 M4S TRC#2 | Cisco Business Edition 6000H (M4) |
| UCS C220 M3S TRC#3 (End of Sale) | Cisco Business Edition 6000H (M3) |
| Small TRC | 1RU rack-mount server | UCS C220 M5SX TRC#1 | Cisco Business Edition 6000M (M5) |
| UCS C220 M4S TRC#1 | Cisco Business Edition 6000M (M4) |

| TRC Capacity | Form Factor | TRC Name |
|---|---|---|
| Extra-Extra-Large Blade TRC | Full-width blade server | UCS B440 M2 TRC#1 (End of Sale) |
| Extra-Large Blade TRC | Half-width blade server | UCS B230 M2 TRC#1 (End of Sale) |
| Large Blade TRC | Half-width blade server | UCS B200 M4 TRC#1 |
| UCS B200 M3 TRC#1 (End of Sale) |
| Medium Blade TRCs | Half-width blade server | UCS B200 M2/M1 TRCs (End of Sale) |

| TRC Capacity | Form Factor | TRC Name | Appliance Based on this TRC** |
|---|---|---|---|
| Extra-Small TRC | Single-wide blade server for Cisco Integrated Services (Cisco ISR) | UCS E160S M3 TRC#1 | N/A |
| Extra-Small TRC | Double-wide blade server for Cisco Integrated Services (Cisco ISR) | UCS E160D M2 TRC#1 | Blade server component of Cisco Business Edition 6000S (M2) appliance Note Cisco Business Edition 6000S appliance is End of Sale. | Note | Cisco Business Edition 6000S appliance is End of Sale. |
| Note | Cisco Business Edition 6000S appliance is End of Sale. |

| Note | Cisco Business Edition 6000S appliance is End of Sale. |
|---|---|

| TRC Capacity | Form Factor | TRC Name |
|---|---|---|
| Large HyperFlex TRCs | 1RU rack-mount HyperFlex node | HX220c M5SX TRC#1 |
| Large HyperFlex TRC | 2RU rack-mount HyperFlex node | HX240c M4SX TRC#1 |

| Parameter | Value |
|---|---|
| Supported Application Co-residency and Virtual-to-Physical Sizing | See the application links at http://www.cisco.com/go/virtualized-collaboration . See sizing information at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html and http://www.cisco.com/go/vmpt . |
| Supported Virtual Machine Configuration | Refer to the documentation at: http://www.cisco.com/go/virtualized-collaboration To ensure that the VMs are correctly configured, use the Cisco-provided OVA template to create VMs. Refer to Download Virtual Machine Templates (OVA Templates) For more information about VM configurations, refer to the documentation at: http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html#ova . |
| Supported virtualization software vendors, products, versions and features | See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html . |
| Supported hardware | See http://www.cisco.com/go/virtualized-collaboration and http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html . |
| CPU and RAM over subscription | None |
| Storage capacity and IOPS requirements | See http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html#storage and the application links at http://www.cisco.com/go/virtualized-collaboration |

| Note | Backup and restore for Cisco Collaboration applications are not supported on soft media. |
|---|---|

| Caution | If your server is ordered as a Cisco Business Edition 6000 or Cisco Business Edition 7000 appliance, the server ships with
                                       factory-setup hardware and factory-preloaded software. DO NOT follow the configuration procedures that are outlined in this
                                       document or you will overwrite the preloaded software. Follow this document only if you must rebuild your server from scratch.
                                       Unless you are rebuilding your server from scratch, such as recovering from a catastrophic situation, use the Installation
                                       Guides for Cisco Business Edition 6000 or 7000 at https://www.cisco.com/c/en/us/products/unified-communications/business-edition-6000/index.html or https://www.cisco.com/c/en/us/products/unified-communications/business-edition-7000/index.html . |
|---|---|

| Cisco UCS Server | Ethernet Port Allocation |
|---|---|
| HX220c M5SX TRC1 (Large HyperFlex TRC) | For each HyperFlex cluster node: One motherboard CIMC management port (not used) Two motherboard LOM ports Two 40-Gigabit ports (Cisco VIC) |
| HX240c M4SX TRC1 (Large HyperFlex TRC) | For each node: One motherboard CIMC management port (not used) Two motherboard LOM ports Two 10-Gigabit ports (Cisco VIC) Minimum system requires four nodes and two 6200 Fabric Interconnect switches. |
| UCS C240 M5SX TRC2 (Large TRC / BE7000H M5) | Eleven Ethernet ports: One 1 GbE LOM port for dedicated CIMC management. Eight 1 GbE ports for quad-port Intel NICs for network access. Two 10 GbE LOM ports for network access. |
| UCS C240 M5SX TRC1 (Medium TRC / BE7000M M5) | One 1 GbE LOM port for dedicated CIMC management. Eight 1 GbE ports for quad-port Intel NICs for network access. Two 10 GbE LOM ports for network access. |
| UCS C220 M5SX TRCs (Small TRC / BE6000M M5 and Small Plus TRC / BE6000H M5) | For Small TRC: Three Ethernet ports: One 1 GbE LOM port for dedicated CIMC management. Two 10 GbE LOM ports for network access. For Small Plus or Medium TRC: Seven Ethernet ports: One 1 GbE port for dedicated CIMC management. Four 1 GbE ports for quad-port Intel NICs. Two 10 GbE LOM ports for network access. |
| UCS E160S M3 TRC1(Extra-Small TRC) | 3 external (front of E160D M2) Ethernet ports: One "M" port for dedicated CIMC management. CIMC is also accessible via the following internal ports: Two ports for LAN access The two internal ports of the UCS E-Series server are to ISR backplane for connectivity to other ISR interfaces. |
| (End of Sale) UCS C240 M4SX TRC1 (Large TRC / BE7000H M4) | Eleven ethernet ports: One port for dedicated CIMC management. Eight ports for quad-port Intel NICs. Two ports for the LOM, if required. |
| (End of Sale) UCS C260 M2 TRC1 (Extra-Large TRCs) | Ten Ethernet ports: One port for dedicated Cisco Integrated Management Controller (CIMC) management Four ports for quad-port Intel NICs Two ports for the LAN on Motherboard (LOM) Two 10-Gigabit Modular LOM |
| (End of Sale) UCS C240 M4S2 TRC1 (Medium TRC / BE7000M M4) | Eleven ethernet ports: One port for dedicated CIMC management. Eight ports for quad-port Intel NICs. Two ports for the LOM, if required. |
| (End of Sale) UCS C240 M3S TRC1 (Large TRC) | Eleven Ethernet ports: One port for dedicated CIMC management Eight ports for quad-port Intel NICs Two ports for the LOM, if necessary. |
| (End of Sale) UCS C240 M3S TRC2 (Medium TRC / BE7000M M3) | Eleven Ethernet ports: One port for dedicated CIMC management Eight ports for quad-port Intel NICs Two ports for the LOM, if necessary. |
| (End of Sale) UCS C210 M2/M1 TRCs (Medium TRCs) | Seven Ethernet ports: One port for dedicated CIMC management Four ports for quad-port Intel NICs Two ports for the LOM |
| (End of Sale) UCS C220 M4S TRCs (Small TRC/ BE6000M M4 and Small Plus TRC / BE6000H M4) | For Small TRC: Three ethernet ports: One port for dedicated CIMC management. Two ports for the LOM, if required. For Small Plus or Medium TRC: Seven ethernet ports: One port for dedicated CIMC management. Four ports for quad-port Intel NICs. Two ports for the LOM, if required. |
| (End of Sale) UCS C220 M3S TRCs (Small TRC / BE6000M M3, Small Plus TRC / BE6000H M3 and Medium TRC) | For Small TRC: Three Ethernet ports: One port for dedicated CIMC management Two ports for the LOM, if necessary. For Small Plus or Medium TRC: Seven Ethernet ports: One port for dedicated CIMC management Four ports for quad-port Intel NICs Two ports for the LOM, if necessary. |
| (End of Sale) UCS C200 M2 TRC1 (Small TRC / BE6000M M2) | Three Ethernet ports: One port for dedicated CIMC management Two ports for the LOM |
| (End of Sale) UCS E160D M2 TRC1 (Extra-Small TRC / BE6000S M2) | 3 "external" (front of E160D M2) ethernet ports: One "M" port for dedicated CIMC management (CIMC is also accessible via the "internal" ports described below) Two ports for LAN access. The two "internal" ports of the UCS E-Series server are to ISR backplane for connectivity to other ISR interfaces. |