---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-business-edition-7000-223082-uc-on-ucs-hardware-replacement-fo-1369c3002d
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/business-edition-7000/223082-uc-on-ucs-hardware-replacement-for.html
retrieved_at: 2026-08-17T01:47:08.698761+00:00
---

UC on UCS: Hardware Replacement for BE6K, BE7K, MM400v, MM410V, CMS1000, CMS2000, TCS

# UC on UCS: Hardware Replacement for BE6K, BE7K, MM400v, MM410V, CMS1000, CMS2000, TCS

### Download Options

Updated: June 10, 2025

Document ID: 223082

Contents

## Contents

## Introduction

This article will document the CIBU products that use SAVBU UCS hardware (aka UCS adopter product) and how hardware support works within TAC for each of them.

NOTE: This does not work for Federal Customers. If the customer is a Federal customer, the partner must be the one who opens the DOA request. TAC/HTTS will be rejected if they attempt to open a DOA request for Federal customers.

A customer-facing version of this information can be found at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html .

The producuts this document covers are

- BE6K – models BE6000S, BE6000M, BE6000H

- BE7K – models BE7000M, BE7000H

- Cisco Media Server

- Media 400V

- Telepresence Content Server

- Expressway CE - CE1400V, CE1300, CE1200

Definitions of Terms used in this document

- BExK - Cisco Business Edition Server

- CE1xK - Cisco Expressway Server

- SKU - Stock Keeping Unit, a Cisco part number which may be purchased by a customer

- FRU - Field Replaceable Unit, a part which can be RMAd and installed by a customer with specific knowledge or FE

- CRU - Customer Replaceable Unit, a part which can be RMAd and installed by the customer with no specific training

- BOM - Bill of Materials, a list of sub-components that are included in a confiurable SKU

## Hardware Support Strategy for CIBU UCS Adopter Products

All of the products included in this document adhere to the same hardware support strategy as UCS-C servers.

This means Cisco RMA Depots do not stock and SVO does not support full-server, configured RMAs.

Hardware replacement must be done at the component level based on the diagnosis of the customer, partner, and/or TAC.

## DOA or MFG-NEW RMAs

Because the full server, configured chassis are not in the SVO tool a DOA RMA must be placed as MFG-New, using the part " CLR-MISC " with the correct product PID noted in the RMA's special instructions.

Any RMA for a product that includes preinstalled software must be processed as MFG-NEW in order for the hypervisor and apps to be preinstalled at the factory. There is the potential for a limited stock of BE6K MD servers to be in Cisco RMA depots however these servers will not have any preinstalled software.

!! IMPORTANT !!

Typically when a new version of the BE server (e.g. M5 replacing the M4 servers) is available the previous version quickly becomes End of Sale.

MFG-NEW RMAs are only possible for a PID that has not reached End of Sale.

As of October 2018 this means that TAC cannot use this option for M4-based BE6K or BE7K servers because they are EOS . Only M5-based servers can be ordered.

TAC (both UC and SV) should continue to troubleshoot difficult hardware problems, and escalate internally and even via BEMS as needed. Replacing the entire server is no longer an option as a last resort.

Note for Mainboard/Motherboard replacement:

UCSC mainboards are traditionally replaced using the chassis top-level FRU.  For the UC products in this document that are M4-based servers the SVO tool will automatically replace the UC SKU with the UCS one. This means if you RMA the top-level PID your customer will get a chassis and mainboard with no HDD, RAM, etc.

Note: For the M3-based "be6k" servers (BE6K-ST-BDL*) the product is End Of Support.

https://www.cisco.com/c/en/us/products/collateral/unified-communications/business-edition-6000/eos-eol-notice-c51-734760.html

## BE4000

Cisco ® Business Edition 4000 (BE4000) is based on the ISR4321 and has no UCS component as part of the solution. SKU: BE4S-V-K9 Cisco Business Edition 4000 Appliance Individual components, outside of of Network Interface Modules (NIMs) are not available for RMA.

## BE6000

Cisco ® Business Edition 6000 (BE6000) was the first UCS adopter product offered for UC products to ship with factory-installed virtualization software (ESXi) and includes OVA and ISO installation media for UC software on the ESXi datastore. It includes ESXi preinstalled from the factory along with a set of core UC VMs created and potentially preinstalled.

There are three versions of the BE6K, each with different capabilities and different hardware.

BE6K MD supports 1000 users, up to 1200 devices, and 4+1 * UC Apps

BE6K HD supports 1000 users, up to 2500 devices, and 8+1 * UC Apps

BE6000S supports 150 users, up to 300 devices, and runs a fixed configuration of 5 UC Apps. It comes bundled with an ISR 2921V. The three SKUs for the product indicate the type of VWIC the ISR will ship with for PSTN connectivity (FXO, PRI, or BRI).

* The +1 app for BE6K is always Prime Collaboration Provisioning for BE.

### BE6K SKUs

BE6K-ST-BDL-K9

BE6K-ST-BDL-XU

BE6K Medium Density Server, Export Restricted SW (UCS M3)

BE6K Medium Density Server, Export Unrestricted SW (UCS M3)

BE6K-STBDL-PLS-K9

BE6K-STBDL-PLS-XU

BE6K High Density Server, Export Restricted SW (UCS M3)

BE6K High Density Server, Export Unrestricted SW (UCS M3)

Blue Lagoon

BE6000S, 2921V, PRI (UCS E160D M2)

Canberra

BE6000S, 2921V, BRI (UCS E160D M2)

Canberra

BE6000S, 2921V, FXO (UCS E160D M2)

Canberra

BE6M-M4-K9

BE6M-M4-XU

BE6000 Medium Density Server, Export Restricted SW (UCS M4)

BE6000 Medium Density Server, Export Unrestricted SW (UCS M4)

BlueMoon

BE6H-M4-K9

BE6H-M4-XU

BE6000 High Density Server, Export Restricted SW (UCS M4)

BE6000 High Density Server, Export Unrestricted SW (UCS M4)

BlueMoon

BE6M-M5-K9

BE6M-M5-XU

Cisco Business Edition 6000M (M5) Appliance, Export Restr SW

Cisco Business Edition 6000M (M5) Appliance, Exp Unrestr SW

BE6H-M5-K9

BE6H-M5-XU

Cisco Business Edition 6000H (M5) Appliance, Export Restr SW

Cisco Business Edition 6000H (M5), Exp Unrestr SW

BE6K-M6-K9

BE6K-M6-XU

Cisco Business Edition 6000 (M6) Appliance, Export Restr SW

Cisco Business Edition 6000 (M6) Appliance, Exp Unrestr SW

BE6K-M7-K9

BE6K-M7-XU

Cisco Business Edition 6000 (M7) Appliance, Export Restr SW

Cisco Business Edition 6000 (M7) Appliance, Exp Unrestr SW

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the BE6K.

### BOM for BE6K-ST-BDL (K9/XU)

BE6K-ST-BDL-K9

or

BE6K-ST-BDL-XU

BE6K-ST-BDL-K9=

or

BE6K-ST-BDL-XU=

### BOM for BE6K-STBDL-PLS (K9/XU)

BE6K-STBDL-PLS-K9

or

BE6K-STBDL-PLS-XU

BE6K-STBDL-PLS-K9

or

BE6K-STBDL-PLS-XU

### BOM for BE6S- PRI / BRI / FXO -M2-K9

UCS E160D Components

UCS-E160D-M2BUN/K9

Upgrades E140/160 First memory dimm from 8 to 16GB.

1333MHz RDIMM/PC3-10600

DISK-MODE-RAID-5

### BOM for BE6M-M4 (K9/XU)

The BE6M-M4's 6 physical disks are configured into a single RAID5 volume.

Note: CIT-MR-1X162RU-A  was replaced by CIT-MR-1X162RV-A on 29 March, 2017.

### BOM for BE6M-M5 (K9/XU)

The BE6M-M5's 6 physical disks are configured into a single RAID5 volume.

### BOM for BE6H-M4 (K9/XU)

The BE6H-M4's 8 physical disks are configured into a single RAID5 volume.

Note: CIT-MR-1X081RU-A was replaced by CIT-MR-1X081RV-A on 29 March, 2017.

### BOM for BE6H-M5 (K9/XU)

The BE6H-M5's 8 physical disks are configured into a single RAID5 volume.

### BOM for BE6K-M6 (K9/XU)

*Note: BE6H does not have a M6 1:1 replacement as the previous versions did.

### BOM for BE6K-M7 (K9/XU)

BE6CE-RAIDCTRLR-M7

## BE7000

Cisco ® Business Edition 7000 (BE7000) is a bigger version of the BE6000. It includes ESXi preinstalled from the factory along with a set of core UC VMs created and potentially preinstalled.

BE7000 supports 1000+ users. It supports 4-6 UC Applications.

BE7000 is intended to be used as a "building block" as a Medium-sized TRC that takes advantage of the ease in ordering and deployment introduced with BE6000.

### BE7K SKUs

BE7K-K9

BE7K-XU

BE7K Server, Export Restricted (K9) SW

BE7K Server, Export Unrestricted (XU) SW (UCS M3)

BE7M-M4-K9

BE7M-M4-XU

BE7K Medium-Density Server, Export Restricted (K9) SW

BE7K Medium-Density Server, Export Unrestricted (XU) SW (UCS M4)

BlueMoon

BE7H-M4-K9

BE7H-M4-XU

BE7K High-Density Server, Export Restricted (K9) or Unrestricted (XU) SW

BE7K High-Density Server, Export Unrestricted (XU) SW (UCS M4)

BlueMoon

BE7M-M5-K9

BE7M-M5-XU

Cisco Business Edition 7000M (M5) Appliance, Export Restr SW

Cisco Business Edition 7000M (M5) Appliance, Exp Unrestr SW

Blue Beetle

BE7H-M5-K9

BE7H-M5-XU

Cisco Business Edition 7000H (M5) Appliance, Export Restr SW

Cisco Business Edition 7000H (M5) Appliance, Exp Unrestr SW

Blue Beetle

BE7M-M6-K9

BE7M-M6-XU

Cisco Business Edition 7000M (M6) Appliance, Export Restr SW

Cisco Business Edition 7000M (M6) Appliance, Exp Unrestr SW

Duros 4

BE7H-M6-K9

BE7H-M6-XU

Cisco Business Edition 7000H (M6) Appliance, Export Restr SW

Cisco Business Edition 7000H (M6) Appliance, Exp Unrestr SW

Duros 4

BE7M-M7-K9

BE7M-M7-XU

Cisco Business Edition 7000M (M7) Appliance, Export Restr SW

Cisco Business Edition 7000M (M7) Appliance, Exp Unrestr SW

KreeAC4

BE7H-M7-K9

BE7H-M7-XU

Cisco Business Edition 7000H (M7) Appliance, Export Restr SW

Cisco Business Edition 7000H (M7) Appliance, Exp Unrestr SW

KreeAC4

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the BE7K.

### BOM for BE7K-(K9/XU)

### BOM for BE7M-M4-(K9/XU)

The BE7M-M4's 12 physical disks are configured into two RAID5 volumes of 6 physical disks each.

Note: CIT2-MR-1X162RU-A was replaced by CIT2-MR-1X162RV-A on 29 March, 2017.

### BOM for BE7M-M5-(K9/XU)

The BE7M-M5's 14 physical disks are configured into two RAID5 volumes of 7 physical disks each.

### BOM for BE7M-M6-(K9/XU)

### BOM for BE7M-M7 (K9/XU)

BE7K-RAIDCTRLR-M7

BECE-DISK-M7

BECE-OCPNIC-M7

BECE-PCIENIC-M7

BECE-PSU-M7

BECE-TPM-M7

BECE-MLOMNICKIT-M7

### BOM for BE7H-M4-(K9/XU)

The BE7H-M4's 20 physical disks are configured into four RAID5 volumes of 5 physical disks each.

Note: CIT2-MR-1X162RU-A was replaced by CIT2-MR-1X162RV-A on 29 March, 2017.

### BOM for BE7H-M5-(K9/XU)

The BE7H-M5's 24 physical disks are configured into four RAID5 volumes of 6 physical disks each.

### BOM for BE7H-M6-(K9/XU)

### BOM for BE7H-M7 (K9/XU)

BE7K-CPU-M7

BECE-RAM-M7

BE7K-RAIDCTRLR-M7

BECE-DISK-M7

BECE-OCPNIC-M7

BECE-PCIENIC-M7

BE7K-PCIERISER-M7

BECE-PSU-M7

BECE-TPM-M7

## MultiParty Media 400v Virtual Telepresence Server Appliance

The Multiparty Media 400v is a UCS adopter product optimized for a virtual Telepresence Server (vTS).  This appliance is intended to run the virtualization software and a single vTS virtual machine. The MM400v does not ship with any factory-installed software and customers must purchase and license virtualization software and vTS separately.

### MultiParty Media 400v SKUs

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the MM400v.

### BOM for VTS-LSVR-M3

## MultiParty Media 410 Virtual Telepresence Server Appliance

The Multiparty Media 410 is a UCS adopter product optimized for a virtual Telepresence Server (vTS).  This appliance is intended to run the virtualization software and a single vTS virtual machine. The mm410 is available as both a chassis and blade UCS server.

### MultiParty Media 410v SKUs

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the MM410.

### BOM for CTI-410V-VTS-K9

### BOM for CTI-410VB-VTS-K9

## Cisco Meeting Server 1000

The Cisco Meeting Server 1000 is a UCS adopter product optimized for both virtual Telepresence Server (vTS) and Cisco Meeting Server (CMS, formerly Acano).  This appliance is intended to run the virtualization software and a single CMS or vTS virtual machine. The CMS 1000 is only available in a rack-mountable chassis form.

### CMS 1000 SKU (M4)

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the previous (M4) versions of the CMS 1000.

### BOM for CTI-CMS-1000-K9 (M4)

More information:

### CMS 1000 SKU (M5)

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the CMS 1000.

### BOM for CTI-CMS-1000-K9 (M5)

More information:

### CMS 1000 SKU (M6)

### BOM for CTI-CMS-1000-K9 (M6)

CMS PID

UCS PID

Description

Quantity

CTI-CMS-1K-M6-K9

UCSC-C220-M6S

UCS C220 M6 Rack w/o CPU, mem, drives, 1U wSFF HDD backplane

1

CIT3-CPU-I6336Y

UCS-CPU-I6336Y

Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz

2

CIT3-MR-X16G1RW

UCS-MR-X16G1RW

16GB RDIMM SRx4 3200 (8Gb)

16

CIT3-SDB960SA1V

UCS-SDB960SA1V

960GB 2.5 inch Enterprise Value 6G SATA SSD

2

CIT3-RAID-220M6

UCSC-RAID-M6T

Cisco 12G SAS RAID Controller w/4GB FBWC (16 Drv) w/1U Brkt

1

CIT3-PSU1-1050W

UCSC-PSU1-1050W

Cisco UCS 1050W AC Power Supply for Rack Server

2

CIT3-TPM-002C

UCSX-TPM-002C

TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers

1

Auto Expanded PIDs

CIMC-LATEST

IMC SW (Recommended) latest release for C-Series Servers

1

UCS-DIMM-BLK

UCS DIMM Blanks

16

UCSC-HSLP-M6

Heatsink for 1U/2U LFF/SFF GPU SKU

2

UCSC-R2R3-C220M6

C220 / C225 M6 UCSC -HH Riser2 and Riser 3 KIT

1

CBL-SAS-C220M6

C220M6 SAS cable (1U); (Pismo HBA)

1

CBL-SCAP-C220M6

C220/C240M6 1U/2U Super Cap cable

1

UCSC-BBLKD-S2

UCS C-Series M5 SFF drive blanking panel

8

UCS-SCAP-M6

M6 SuperCap

1

UCSC-RAIL-M6

ASY,MECH,RAIL KIT,BALL BEARING,M6

1

## Cisco Meeting Server 2000

The Cisco Meeting Server 2000 is a UCS adopter product optimized for Cisco Meeting Server (CMS, formerly Acano).  This appliance is intended to run bare metal. The CMS 2000 is only available in a rack-mountable chassis form.

### CMS 2000 SKU

(M4 - sold and shipped from initial release in June 2017 through to February 2019.)

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the previous (M4) versions of the CMS 2000.

### BOM for CMS2000 Chassis

(M4 - sold and shipped from initial release in June 2017 through to February 2019.)

UCS SP Select 5108 AC2 Chassis w/FI6324

UCSB-5108-AC2=

UCS-FI-M-6324=

N20-FAN5=

N20-CAK=

### BOM for CMS2000 Primary Blade

(M4 - sold and shipped from initial release in June 2017 through to February 2019.)

UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG)

UCSB-B200-M4=

UCS-CPU-E52695E=

UCSB-MLOM-40G-03=

UCSB-MLOM-PT-01=

UCSB-HS-EP-M4-R=

UCSB-HS-EP-M4-F=

UCS-HD300G10K12G=

UCSB-MRAID12G=

UCS-MR-1X081RV-A=

### BOM for CMS2000 Secondary Blades

(M4 - sold and shipped from initial release in June 2017 through to February 2019.)

UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG)

UCSB-B200-M4=

UCS-CPU-E52695E=

UCSB-MLOM-40G-03=

UCSB-MLOM-PT-01=

UCSB-HS-EP-M4-R=

UCSB-HS-EP-M4-F=

UCSB-LSTOR-BK=

UCS-MR-1X081RV-A=

### CMS 2000 SKU

(M5 - sold and shipped from February 2019.)

*Project Codename is where the product was first introduced.  Later programs may introduce hardware and software pre-load updates.

The tables below show the BOM for the current shipping versions of the CMS 2000.

### BOM for CMS2000 Chassis

(M5 - sold and shipped from February 2019.)

UCS 5108 Blade Server AC2 Chassis, 0 PSU/8 fans/0 FEX

UCSB-5108-AC2=

UCS-FI-M-6324=

N20-FAN5=

N20-CAK=

### BOM for CMS2000 Primary Blade

( M5 - sold and shipped from February 2019. )

UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG)

UCS-CPU-6140=

UCSB-MLOM-40G-03=

UCSB-MLOM-PT-01=

UCSB-HS-M5-R=

UCSB-HS-M5-R=

UCS-HD300G10K12G=

UCSB-MRAID12G=

UCS-MR-X16G1RS-H=

UCS-DIMM-BLK=

### BOM for CMS2000 Secondary Blades

( M5 - sold and shipped from February 2019. )

UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG)

UCS-CPU-6140=

UCSB-MLOM-40G-03=

UCSB-MLOM-PT-01=

UCSB-HS-M5-R=

UCSB-HS-M5-F=

UCSB-LSTOR-BK=

UCS-DIMM-BLK=

### BOM for CMS2000 Chassis (M6)

CTI-CMS-2K-M6-K9

CIT3-FAN5

N20-FAN5

Fan module for UCS 5108

8

CIT3-PSUT2500ACDV

UCSB-PSUT2500ACDV

2500W Titanium AC Hot Plug Power Supply - DV

4

CIT3-UAC1

N01-UAC1

Single phase AC power module for UCS 5108

1

CIT3-FI-M-6324

UCS-FI-M-6324

UCS 6324 In-Chassis FI with 4 UP, 1x40G Exp Port, 16 10Gb

2

CIT3-5108-PKG-HW

UCSB-5108-PKG-HW

UCS 5108 Packaging for chassis with half width blades.

1

### BOM for CMS2000 Control Blade (M6)

CIT3-B200-M6-CON

UCSB-B200-M6

CMS Control Blade

CIT3-CPU-I6336Y

UCS-CPU-I6336Y

Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz

2

CIT3-MR-X16G1RW

UCS-MR-X16G1RW

16GB RDIMM SRx4 3200 (8Gb)

16

CIT3-RAID12G-M6

UCSB-RAID12G-M6

Cisco M6 FlexStorage 12G SAS RAID Controller

1

CIT3-SDC960SA1V

UCS-SDC960SA1V

960GB 2.5 inch Enterprise Value 6G SATA SSD

2

CIT3-MLOM-40G-04

UCSB-MLOM-40G-04

Cisco UCS VIC 1440 modular LOM for Blade Servers

1

CIT3-MLOM-PT-01

UCSB-MLOM-PT-01

Cisco UCS Port Expander Card (mezz) for VIC

1

CIT3-TPM-002C

UCSX-TPM-002C

TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers

1

### BOM for CMS2000 Media Blades (M6)

CIT3-B200-M6

UCSB-B200-M6-U

CMS Media Blade

CIT3-CPU-I6336Y

UCS-CPU-I6336Y

Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz

14

CIT3-MR-X16G1RW

UCS-MR-X16G1RW

16GB RDIMM SRx4 3200 (8Gb)

112

CIT3-MLOM-40G-04

UCSB-MLOM-40G-04

Cisco UCS VIC 1440 modular LOM for Blade Servers

7

CIT3-MLOM-PT-01

UCSB-MLOM-PT-01

Cisco UCS Port Expander Card (mezz) for VIC

7

N20-CAK

Access. kit for 5108 Blade Chassis incl Railkit, KVM dongle

1

N20-FW018

UCS 5108 Blade Chassis FW Package 4.2

8

UCSB-HS-M6-F

CPU Heat Sink for UCS B-Series M6 CPU socket (Front)

8

UCSB-HS-M6-R

CPU Heat Sink for UCS B-Series M6 CPU socket (Rear)

8

UCS-DIMM-BLK

UCS DIMM Blanks

128

N10-MGT018

UCS Manager v4.2 and Intersight Managed Mode v4.2

1

UCSB-FBLK-M6

Cisco B200 M6 Front Drive Blank Sleds

14

N20-CBLKB1

Blade slot blanking panel for UCS 5108/single slot

7

## Older PIDs

## Telepresence Content Server

TheTelepresence Content Serveris a UCS adopter product optimized for TelePresence ® Content Server (TCS). Organizations can share knowledge and enhance communication by recording videoconferences. They can access live and on-demand presentations, distance education classes, and corporate training sessions. In addition, TCS can distribute live or recorded content to any computer or download to your favorite portable media device. Cisco TelePresence Content Server is available as a dedicated appliance or as a virtualized application on VMware. This appliance is intended to run bare metal.

### TCS SKU

TCS-M4-PROBUN-K9

TCS with 5 Record/ 2 Live with Premium Resolution licenses

TCS-M4-PRO10P-K9

TCS with 10 Record/ 2 Live with Premium Resolution licenses

### BOM for TCS SKUS (M4 BOM is the same for all PIDS listed above)

TCS-M4-PROBUN-K9

TCS-M4-PRO10P-K9

## Expressway CE

### CE1xK SKUs

CE1400V-M7-K9

Cisco Expressway CE1400V Appliance

The tables below show the BOM for the current shipping versions of the CE1xK.

### BOM for CE1400V-M7-K9

BECE-RAM-M7

BE6CE-RAIDCTRLR-M7

BECE-DISK-M7

BECE-OCPNIC-M7

BECE-PCIENIC-M7

BECE-PSU-M7

BECE-TPM-M7

## External References

### Revision History

1.0

10-Jun-2025

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### Customers Also Viewed

- Upgrade ESXi for a Business Edition (BE6K/7K) via vKVM

### This Document Applies to These Products

- Business Edition 7000

| SKU | Description | Project Codename * |
|---|---|---|
| BE6K-ST-BDL-K9 BE6K-ST-BDL-XU | BE6K Medium Density Server, Export Restricted SW (UCS M3) BE6K Medium Density Server, Export Unrestricted SW (UCS M3) | Blue Bird |
| BE6K-STBDL-PLS-K9 BE6K-STBDL-PLS-XU | BE6K High Density Server, Export Restricted SW (UCS M3) BE6K High Density Server, Export Unrestricted SW (UCS M3) | Blue Lagoon |
| BE6S-PRI-M2-K9 | BE6000S, 2921V, PRI (UCS E160D M2) | Canberra |
| BE6S-BRI-M2-K9 | BE6000S, 2921V, BRI (UCS E160D M2) | Canberra |
| BE6S-FXO-M2-K9 | BE6000S, 2921V, FXO (UCS E160D M2) | Canberra |
| BE6M-M4-K9 BE6M-M4-XU | BE6000 Medium Density Server, Export Restricted SW (UCS M4) BE6000 Medium Density Server, Export Unrestricted SW (UCS M4) | BlueMoon |
| BE6H-M4-K9 BE6H-M4-XU | BE6000 High Density Server, Export Restricted SW (UCS M4) BE6000 High Density Server, Export Unrestricted SW (UCS M4) | BlueMoon |
| BE6M-M5-K9 BE6M-M5-XU | Cisco Business Edition 6000M (M5) Appliance, Export Restr SW Cisco Business Edition 6000M (M5) Appliance, Exp Unrestr SW | Blue Beetle |
| BE6H-M5-K9 BE6H-M5-XU | Cisco Business Edition 6000H (M5) Appliance, Export Restr SW Cisco Business Edition 6000H (M5), Exp Unrestr SW | Blue Beetle |
| BE6K-M6-K9 BE6K-M6-XU | Cisco Business Edition 6000 (M6) Appliance, Export Restr SW Cisco Business Edition 6000 (M6) Appliance, Exp Unrestr SW | Duros 4 |
| BE6K-M7-K9 BE6K-M7-XU | Cisco Business Edition 6000 (M7) Appliance, Export Restr SW Cisco Business Edition 6000 (M7) Appliance, Exp Unrestr SW | KreeAC4 |

| CITG Adopter SKU | SAVBU SKU | Description | Quantity | FRU / SAVBU SKU |
|---|---|---|---|---|
| BE6K-ST-BDL-K9 or BE6K-ST-BDL-XU | UCSC-C220-M3S | UCS C220 M3 Chassis and Motherboard | 1 | BE6K-ST-BDL-K9= or BE6K-ST-BDL-XU= |
|  | N20-BBLKD | UCS 2.5 inch HDD blanking panel | 4 |  |
|  | UCSC-HS-C220M3 | Heat Sink for UCS C220 M3 Rack Server | 2 |  |
|  | UCSC-PSU-BLKP | Power supply blanking panel/filler | 1 |  |
|  | UCSC-RAIL1 | 2U Rail Kit for C220 servers | 1 |  |
|  | UCSC-PCIF-01F | Full height PCIe filler for C-Series | 1 |  |
| UCS-CPU-E5-2609 | UCS-CPU-E5-2609 | 2.4 GHz E5-2609/80W 4C/10MB Cache/DDR3 1066MHz | 2 | UCS-CPU-E5-2609= |
| UC-MR-1X082RY-A | UCS-MR-1X041RY-A | 4GB DDR3-1600-MHz RDIMM/PC3-12800/single rank/x4/1.35V-1.5V/35nm | 4 | UCS-MR-1X041RY-A= |
| UC-A03-D500GC3 | A03-D500GC3 | 500GB 6Gb SATA 7.2K RPM SFF hot plug/drive sled mounted | 4 | A03-D500GC3= |
| UC-PSU-650W | UCSC-PSU-650W | 650W power supply for C-series rack servers | 1 | UCSC-PSU-650W= |
| UC-RAID-9271 | UCS-RAID9271CV-8I | MegaRAID 9271CV Raid card with 8 internal SAS/SATA parts, S | 1 | UCS-RAID9271CV-8I= |
| CIT-SD-16G-C220 | UCSC-SD-16G-C220 | 16GB SD Card Module for C220 servers | 1 | UCSC-SD-16G-C220= |

| CITG Adopter SKU | SKU | Description | Quantity | FRU |
|---|---|---|---|---|
| BE6K-STBDL-PLS-K9 or BE6K-STBDL-PLS-XU | UCSC-C220-M3S= | SL1 Ivy Bridge Chassis and Motherboard | 1 | BE6K-STBDL-PLS-K9 or BE6K-STBDL-PLS-XU |
| CIT-CPU-E5-2665 | UCS-CPU-E5-2665= | 2.40 GHz E5-2665/115W 8C/20MB Cache/DDR3 1600MHz | 2 | UCS-CPU-E5-2609= |
| UC-MR-1X082RY-A | UCS-MR-1X082RY-A | 4GB DDR3-1600-MHz RDIMM/PC3-12800/single rank/x4/1.35V-1.5V/35nm | 6 | UCS-MR-1X041RY-A= |
| CIT-HDD300GI2F105 | UCS-HDD300GI2F105 | 500GB 6Gb SATA 7.2K RPM SFF hot plug/drive sled mounted | 8 | UCS-HDD300GI2F105= |
| UC-PSU-650W | UCSC-PSU-650W | 650W power supply for C-series rack servers | 2 | UCSC-PSU-650W |
| UC-RAID-9271 | UCS-RAID9271CV-8I | MegaRAID 9271CV Raid card with 8 internal SAS/SATA parts, S | 1 | UCS-RAID9271CV-8I |
| CIT-PCIE-IRJ45 | UCSC-PCIE-IRJ45 | Intel Quad GbE adapter | 1 | UCSC-PCIE-IRJ45 |
|  | R2XX-RAID5 | Enable Raid 5 Setting | 1 | N/A - Config Only |

| CITG Adopter SKU | SAVBU SKU | Description | Quantity | FRU / SAVBU SKU |
|---|---|---|---|---|
| UCS E160D Components |
| UCS-E160D-M2BUN/K9 | UCS-E160D-M2BUN/K9 | UCS E160D M2 Chassis, E5-2418LV2 6-core 2.0GHz | 1 | E160DM2-SVC |
| E100-8-16-MEM-UPG | E100-8-16-MEM-UPG | Upgrades E140/160 First memory dimm from 8 to 16GB. 1333MHz RDIMM/PC3-10600 | 1 | E100D-MEM-RDIM16G= |
| E100D-HDSASED600G | E100D-HDSASED600G | 600 GB, SAS SED hard disk drive for DoubleWide UCS-E | 3 | E100D-HDSASED600G= |
| E100-SD-8G | E100-SD-8G | 8 GB SD Card for SingleWide and DoubleWide UCS-E | 1 | E100-SD-8G= |
| DISK-MODE-RAID-5 | DISK-MODE-RAID-5 | Configure Hard Drives as RAID 5 | 1 | N/A |
| ISR 2921V Components |
| CISCO2921-V/K9 | -- | Cisco 2921 w/3 GE,4 EHWIC,3 DSP,1 SM,256MB CF,512MB DRAM,IPB | 1 | CISCO2921/K9 |
| PWR-2921-51-AC | -- | Cisco 2921/2951 AC Power Supply | 1 | PWR-2921-51-AC= |
| MEM-2900-512U1GB | -- | Cisco 2900 1GB DRAM Upgrade | 1 | MEM-2900-1GB= |
| MEM-CF-256MB | -- | 256MB Compact Flash for Cisco 1900, 2900, 3900 ISR | 1 | MEM-CF-256MB= |
| PVDM3-32 | -- | 32-channel high-density voice and video DSP module SPARE |  | PVDM3-32= |
| CAB-ETH-S-RJ45 | -- | Yellow Cable for Ethernet, Straight-through, RJ-45, 6 feet | 1 | CAB-ETH-S-RJ45= |
| CAB-CONSOLE-USB | -- | Console Cable 6 ft with USB Type A and mini-B | 1 | CAB-CONSOLE-USB= |
| ISR Software and Licenses |
| S29UK9-15403M | -- | IOS Preload for 15.4(3M) | -- | -- |
| SL-29-IPB-K9 | -- | IP Base License for Cisco 2901-2951 | -- | -- |
| SL-29-UC-K9 | -- | Unified Communication License for Cisco 2901-2951 | -- | -- |
| ISR-CCP-EXP | -- | Cisco Config Pro Express on Router Flash | -- | -- |
| FL-CUBEE-5 | -- | Unified Border Element Enterprise License - 5 sessions | -- | -- |
| One of these, based on top-level SKU (PRI, BRI, FXO) |
| VWIC3-1MFT-T1/E1 | -- | 1-Port 3rd Gen Multiflex Trunk Voice/WAN Int. Card - T1/E1 | 1 | VWIC3-1MFT-T1/E1= |
| VIC2-2BRI-NT/TE | -- | Two-port Voice Interface Card - BRI (NT and TE) | 1 | VIC2-2BRI-NT/TE= |
| VIC2-4FXO | -- | Four-port Voice Interface Card - FXO (Universal) | 1 | VIC2-4FXO= |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M4S | UCS C220 M4 SFF w/o CPU, mem, HD, PCIe, PSU, rail kit | 1 | UCSC-C220-M4S= |
| CIT-CPU-E52630D | 2.40 GHz E5-2630 v3/85W 8C/20MB Cache/DDR4 1866MHz | 1 | UCS-CPU-E52630D= |
| CIT-MR-1X162R V -A | 16GB DDR4-2133-MHz RDIMM/PC4-17000/dual rank/x4/1.2v | 2 | UCS-MR-1X162RV-A= |
| CIT-A03-D300GA2 | 300GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted | 6 | A03-D300GA2= |
| CIT-PSU1-770W | 770W AC Hot-Plug Power Supply for 1U C-Series Rack Server | 2 | UCSC-PSU1-770W= |
| CIT-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| CIT-MRAID12G-1GB | Cisco 12Gbps SAS 1GB FBWC Cache module (Raid 0/1/5/6) | 1 | UCSC-MRAID12G-1GB= |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M5SX | UCS C220 M5 SFF 10 HD w/o CPU, mem, HD, PCIe, PSU | 1 |  |
| UCS-CPU-4114 | 2.2 GHz 4114/85W 10C/13.75MB Cache/DDR4 2400MHz | 1 |  |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 3 |  |
| UCS-HD300G10K12N | 300GB 12G SAS 10K RPM SFF HDD | 6 |  |
| UCSC-PSU1-770W | Cisco UCS 770W AC Power Supply for Rack Server | 1 |  |
| UCSC-RAID-M5 | Cisco 12G Modular RAID controller with 2GB cache | 1 |  |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M4S | UCS C220 M4 SFF w/o CPU, mem, HD, PCIe, PSU, rail kit | 1 | UCSC-C220-M4S= |
| CIT-CPU-E52630D | 2.40 GHz E5-2630 v3/85W 8C/20MB Cache/DDR4 1866MHz | 2 | UCS-CPU-E52630D= |
| CIT-MR-1X081RV-A | 8GB DDR4-2133-MHz RDIMM/PC4-17000/single rank/x4/1.2v | 6 | UCS-MR-1X081RV-A= |
| CIT-A03-D300GA2 | 300GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted | 8 | A03-D300GA2= |
| CIT-PSU1-770W | 770W AC Hot-Plug Power Supply for 1U C-Series Rack Server | 2 | UCSC-PSU1-770W= |
| CIT-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| CIT-MRAID12G-1GB | Cisco 12Gbps SAS 1GB FBWC Cache module (Raid 0/1/5/6) | 1 | UCSC-MRAID12G-1GB= |
| CIT-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 1 | UCSC-PCIE-IRJ45= |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M5SX | UCS C220 M5 SFF 10 HD w/o CPU, mem, HD, PCIe, PSU | 1 |  |
| UCS-CPU-4114 | 2.2 GHz 4114/85W 10C/13.75MB Cache/DDR4 2400MHz | 2 |  |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 4 |  |
| UCS-HD300G10K12N | 300GB 12G SAS 10K RPM SFF HDD | 8 |  |
| UCSC-PSU1-770W | Cisco UCS 770W AC Power Supply for Rack Server | 2 |  |
| UCSC-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 1 |  |
| UCSC-RAID-M5 | UCSC-RAID-M5 | 1 |  |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | FRU | Description | Quantity |
|---|---|---|---|
| BE6K-M6-K9 BE6K-M6-XU | UCSC-C220-M6S= | UCS C220 M6 Rack w/o CPU, mem, drives, 1U wSFF HDD backplane | 1 |
| BE6K-CPU-M6 | UCS-CPU-I4310T= | Intel 4310T 2.3GHz/105W 10C/15MB DDR4 2667MHz | 1 |
| BE6K-RAM-M6-M5 | UCS-MR-X16G1RW= | 16GB RDIMM SRx4 3200 (8Gb) | 4 |
| BE6K-RAIDCTRLR-M6 | UCSC-RAID-220M6= | Cisco 12G SAS RAID Controller w/4GB FBWC (16 Drv) w/1U Brkt | 1 |
| BE6K-DISK-M6 | UCS-HD600G10K12N= | 600GB 12G SAS 10K RPM SFF HDD | 6 |
| BE6K-PSU-M6 | UCSC-PSU1-1050W= | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |
| BE6K-TPM-M6 | UCSX-TPM-002C= | TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers | 1 |

|  | Description | PID | Adopter PID |
|---|---|---|---|
| Leveraged Base Server | UCS-M7-MLB | UCSC-C220-M7S |  |
| CPU | (12C/2.0GHz) | UCS-CPU-I4510T | BE6K-CPU-M7 |
| Memory | 5600MHz 16GB DIMMs | UCS-MRX16G1RE3 | BECE-RAM-M7 |
| Storage | RAID Controller | UCSC-RAID-M1L16 | BE6CE-RAIDCTRLR-M7 |
| 600GB 10K SAS HDD | UCS-HD600G10KJ4-D | BECE-DISK-M7 |
| Network + IO | OCP 3.0 MLoM NIC | UCSC-O-ID10GC-D | BECE-OCPNIC-M7 |
| PCIe NIC (4x10GE SFP+) | UCSC-PCIEIQ10GF-D | BECE-PCIENIC-M7 |
| 10GE Fiber SFP+ | SFP-10G-SR | SFP-10G-SR |
| 10GE Cu RJ45 SFP+ | GLC-TE | GLC-TE |
| PCIe Riser | UCSC-RIS1A-22XM7 | BE6CE-PCIERISR1-M7 |
| Misc. | Power Supplies | UCSC-PSU1-1200W-D | BECE-PSU-M7 |
| Trusted Platform Module | UCSX-TPM-002C-D | BECE-TPM-M7 |
| Rack-mounting kit | UCSC-RAIL-D |  |
| (Autoexpands) | Heat sinks for CPU | UCSC-HSLP-C220M7 |  |
| Blanking panel (DIMM slot) | UCS-DDR5-BLK |  |
| Blanking panel (disk slot) | UCSC-BBLKD-M7 |  |
| Storage cable | CBL-SAS-Y-C220M7 |  |
| RAID Controller Bracket | UCSC-HPBKT-22XM7 |  |
| Daughterboard for OCP NIC | UCSC-OCP3-KIT-D | BECE-MLOMNICKIT-M7 |
| Blanking panel (Riser2) | UCSC-FBRS2-C220M7 |  |
| Blanking panel (Riser3) | UCSC-FBRS-C220-D |  |

| SKU | Description | Project Codename * |
|---|---|---|
| BE7K-K9 BE7K-XU | BE7K Server, Export Restricted (K9) SW BE7K Server, Export Unrestricted (XU) SW (UCS M3) | Touvlo |
| BE7M-M4-K9 BE7M-M4-XU | BE7K Medium-Density Server, Export Restricted (K9) SW BE7K Medium-Density Server, Export Unrestricted (XU) SW (UCS M4) | BlueMoon |
| BE7H-M4-K9 BE7H-M4-XU | BE7K High-Density Server, Export Restricted (K9) or Unrestricted (XU) SW BE7K High-Density Server, Export Unrestricted (XU) SW (UCS M4) | BlueMoon |
| BE7M-M5-K9 BE7M-M5-XU | Cisco Business Edition 7000M (M5) Appliance, Export Restr SW Cisco Business Edition 7000M (M5) Appliance, Exp Unrestr SW | Blue Beetle |
| BE7H-M5-K9 BE7H-M5-XU | Cisco Business Edition 7000H (M5) Appliance, Export Restr SW Cisco Business Edition 7000H (M5) Appliance, Exp Unrestr SW | Blue Beetle |
| BE7M-M6-K9 BE7M-M6-XU | Cisco Business Edition 7000M (M6) Appliance, Export Restr SW Cisco Business Edition 7000M (M6) Appliance, Exp Unrestr SW | Duros 4 |
| BE7H-M6-K9 BE7H-M6-XU | Cisco Business Edition 7000H (M6) Appliance, Export Restr SW Cisco Business Edition 7000H (M6) Appliance, Exp Unrestr SW | Duros 4 |
| BE7M-M7-K9 BE7M-M7-XU | Cisco Business Edition 7000M (M7) Appliance, Export Restr SW Cisco Business Edition 7000M (M7) Appliance, Exp Unrestr SW | KreeAC4 |
| BE7H-M7-K9 BE7H-M7-XU | Cisco Business Edition 7000H (M7) Appliance, Export Restr SW Cisco Business Edition 7000H (M7) Appliance, Exp Unrestr SW | KreeAC4 |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C240-M3S= | SL2 Ivy Bridge Chassis | 1 | UCSC-C240-M3S= |
| CIT2-CPU-E5-2640= | 2.50 GHz E5-2640/95W 6C/15MB Cache/DDR3 1333MHz | 2 | UCS-CPU-E5-2640= |
| CIT2-MR-1X082RY-A= | 8GB DDR3-1600-MHz RDIMM/PC3-12800/dual rank/1.35v | 8 | UCS-MR-1X082RY-A= |
| CIT2-A03-D300GA2= | 2.5" 300GB, 10K RPM, SAS 146Gb | 12 | A03-D300GA2= |
| CIT2-PSU2-1200= | 1200W 2u Power Supply For UCS | 2 | UCSC-PSU2-1200= |
| CIT2-RAID-9271CV | MegaRAID 9271CV Raid card with 8 internal SAS/SATA parts, S | 1 | UCS-RAID9271CV-8I= |
| CIT2-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 2 | UCSC-PCIE-IRJ45 |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C240-M4S2 | UCS C240 M4 SFF 16 HD w/o CPU,mem,HD,PCIe,PS,rail w/expndr | 1 | UCSC-C240-M4S2= |
| CIT2-CPU-E52680D | 2.50 GHz E5-2680 v3/120W 12C/30MB Cache/DDR4 2133MHz | 1 | UCS-CPU-E52680D= |
| CIT2-MR-1X162RV-A | 8GB DDR3-1600-MHz RDIMM/PC3-12800/dual rank/1.35v | 4 | UCS-MR-1X162RV-A= |
| CIT2-A03-D300GA2 | 2.5" 300GB, 10K RPM, SAS 146Gb | 12 | A03-D300GA2= |
| CIT2-PSU2V2-1200W | 1200W / 800W V2 AC Power Supply for 2U C-Series Servers | 2 | UCSC-PSU2V2-1200W= |
| CIT2-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| CIT2-MRAID12G-1GB | Cisco 12Gbps SAS 1GB FBWC Cache module (Raid 0/1/5/6) | 1 | UCSC-MRAID12G-1GB= |
| CIT2-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 2 | UCSC-PCIE-IRJ45= |
| CIT2-PCI-1B-240M4 | Right PCIe Riser Board (Riser 1) (3 x8) for 6 PCI slots | 1 | UCSC-PCI-1B-240M4= |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C240-M5SX | UCS C240 M5 24 SFF + 2 rear drives w/o CPU,mem,HD,PCIe,PS | 1 |  |
| UCS-CPU-6132 | 2.6 GHz 6132/140W 14C/19.25MB Cache/DDR4 2666MHz | 1 |  |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 6 |  |
| UCS-HD300G10K12N | 300GB 12G SAS 10K RPM SFF HDD | 14 |  |
| UCSC-PSU1-1050W | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |  |
| UCSC-RAID-M5HD | Cisco 12G Modular RAID controller with 4GB cache | 1 |  |
| UCSC-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 2 |  |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | FRU | Description | Qty |
|---|---|---|---|
| BE7M-M6-K9 BE7M-M6-XU | UCSC-C240-M6SX= | UCS C240 M6 Rack w/o CPU, mem, drives, 2U w 24 | 1 |
| BE7M-CPU-M6 | UCS-CPU-I6326= | Intel 6326 2.9GHz/185W 16C/24MB DDR4 3200MHz | 1 |
| BE7K-RAM-M6-M5 | UCS-MR-X16G1RW= | 16GB RDIMM SRx4 3200 (8Gb) | 6 |
| BE7K-RAIDCTRLR-M6 | UCSC-RAID-M6SD= | Cisco 12G SAS RAID Controller w/4GB FBWC (16 Drv) w/1U Brkt | 1 |
| BE7K-DISK-M6 | UCS-HD600G10K12N= | 600GB 12G SAS 10K RPM SFF HDD | 16 |
| BE7K-NIC-M6 | UCSC-P-IQ10GC= | Cisco-Intel X710T4LG 4x10 GbE RJ45 PCIe NIC | 2 |
| BE7K-PCIERISER-M6 | UCSC-RIS1A-240M6= | C240 M6 Riser1A; (x8;x16x, x8); StBkt; (CPU1) | 1 |
| BE7K-PSU | UCSC-PSU1-1050W= | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |
| BE7K-TPM-M6 | UCSX-TPM-002C= | TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers | 1 |

|  | Description | PID | Adopter PID |
|---|---|---|---|
| Leveraged Base Server | UCS-M7-MLB | UCSC-C240-M7SX |  |
| CPU | (16C/2.8GHz) | UCS-CPU-I6526Y | BE7K-CPU-M7 |
| Memory | 5600MHz 16GB DIMMs | UCS-MRX16G1RE3 | BECE-RAM-M7 |
| Storage | RAID Controller | UCSC-RAID-MP1L32 | BE7K-RAIDCTRLR-M7 |
| 600GB 10K SAS HDD | UCS-HD600G10KJ4-D | BECE-DISK-M7 |
| Network + IO | OCP 3.0 MLoM NIC | UCSC-O-ID10GC-D | BECE-OCPNIC-M7 |
| PCIe NIC (4x10GE SFP+) | UCSC-PCIEIQ10GF-D | BECE-PCIENIC-M7 |
| 10GE Fiber SFP+ | SFP-10G-SR | SFP-10G-SR |
| 10GE Cu RJ45 SFP+ | GLC-TE | GLC-TE |
| PCIe Riser | UCSC-RIS1A-240-D | BE7K-PCIERISER-M7 |
| Misc. | Power Supplies | UCSC-PSU1-1200W-D | BECE-PSU-M7 |
| Trusted Platform Module | UCSX-TPM-002C-D | BECE-TPM-M7 |
| Rack-mounting kit | UCSC-RAIL-D |  |
| (Autoexpands) | Heat sinks for CPU | UCSC-HSHP-C240M7 |  |
| Blanking panel (DIMM slot) | UCS-DDR5-BLK |  |
| Blanking panel (disk slot) | UCSC-BBLKD-M7 |  |
| Storage cable | CBL-SAS-Y-C240M7 |  |
| RAID Controller Bracket | UCSC-SDBKT-24XM7 |  |
| Daughterboard for OCP NIC | UCSC-OCP3-KIT-D | BECE-MLOMNICKIT-M7 |
| Blanking panel (Riser2) | UCSC-FBRS2-C240-D |  |
| Blanking panel (Riser3) | UCSC-FBRS3-C240-D |  |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C240-M4SX | UCS C240 M4 SFF 24 HD w/o CPU,mem,HD,PCIe,PS,rail w/expndr | 1 | UCSC-C240-M4SX= |
| CIT2-CPU-E52660D | 2.60 GHz E5-2660 v3/105W 10C/25MB Cache/DDR4 2133MHz | 2 | UCS-CPU-E52660D= |
| CIT2-MR-1X162RV-A | 8GB DDR3-1600-MHz RDIMM/PC3-12800/dual rank/1.35v | 8 | UCS-MR-1X162RV-A= |
| CIT2-A03-D300GA2 | 2.5" 300GB, 10K RPM, SAS 146Gb | 20 | A03-D300GA2= |
| CIT2-PSU2-1400W | 1400W AC Power Supply for 2U & 4U C Series Servers | 2 | UCSC-PSU2-1400W= |
| CIT2-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| CIT2-MRAID12G-4GB | Cisco 12Gbps SAS 4GB FBWC Cache module (Raid 0/1/5/6) | 1 | UCSC-MRAID12G-4GB= |
| CIT2-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 2 | UCSC-PCIE-IRJ45= |
| CIT2-PCI-1B-240M4 | Right PCIe Riser Board (Riser 1) (3 x8) for 6 PCI slots | 1 | UCSC-PCI-1B-240M4= |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C240-M5SX | UCS C240 M5 24 SFF + 2 rear drives w/o CPU,mem,HD,PCIe,PS | 1 |  |
| UCS-CPU-6132 | 2.6 GHz 6132/140W 14C/19.25MB Cache/DDR4 2666MHz | 2 |  |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 12 |  |
| UCS-HD300G10K12N | 300GB 12G SAS 10K RPM SFF HDD | 24 |  |
| UCSC-PSU1-1050W | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |  |
| UCSC-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 2 |  |
| UCSC-RAID-M5HD | Cisco 12G Modular RAID controller with 4GB cache | 1 |  |
| R2XX-RAID5 | Enable RAID 5 Setting | 1 | N/A - Config Only |

| SKU | FRU | Description | Quantity |
|---|---|---|---|
| BE7H-M6-K9 BE7H-M6-XU | UCSC-C240-M6SX= | UCS C240 M6 Rack w/o CPU, mem, drives, 2U w 24 | 1 |
| BE7H-CPU-M6 | UCS-CPU-I6348= | Intel 6348 2.6GHz/235W 28C/42MB DDR4 3200MH | 1 |
| BE7K-RAM-M6-M5 | UCS-MR-X16G1RW= | 16GB RDIMM SRx4 3200 (8Gb) | 12 |
| BE7K-RAIDCTRLR-M6 | UCSC-RAID-M6SD= | Cisco 12G SAS RAID Controller w/4GB FBWC (16 Drv) w/1U Brkt | 1 |
| BE7K-DISK-M6 | UCS-HD600G10K12N= | 600GB 12G SAS 10K RPM SFF HDD | 24 |
| BE7K-NIC-M6 | UCSC-P-IQ10GC= | Cisco-Intel X710T4LG 4x10 GbE RJ45 PCIe NIC | 2 |
| BE7K-PCIERISER-M6 | UCSC-RIS1A-240M6= | C240 M6 Riser1A; (x8;x16x, x8); StBkt; (CPU1) | 1 |
| BE7K-PSU | UCSC-PSU1-1050W= | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |
| BE7K-TPM-M6 | UCSX-TPM-002C= | TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers | 1 |

|  | Description | PID | Adopter PID |
|---|---|---|---|
| Leveraged Base Server | UCS-M7-MLB | UCSC-C240-M7SX |  |
| CPU | (16C/2.8GHz) | UCS-CPU-I6526Y | BE7K-CPU-M7 |
| Memory | 5600MHz 16GB DIMMs | UCS-MRX16G1RE3 | BECE-RAM-M7 |
| Storage | RAID Controller | UCSC-RAID-MP1L32 | BE7K-RAIDCTRLR-M7 |
| 600GB 10K SAS HDD | UCS-HD600G10KJ4-D | BECE-DISK-M7 |
| Network + IO | OCP 3.0 MLoM NIC | UCSC-O-ID10GC-D | BECE-OCPNIC-M7 |
| PCIe NIC (4x10GE SFP+) | UCSC-PCIEIQ10GF-D | BECE-PCIENIC-M7 |
| 10GE Fiber SFP+ | SFP-10G-SR | SFP-10G-SR |
| 10GE Cu RJ45 SFP+ | GLC-TE | GLC-TE |
| PCIe Riser | UCSC-RIS1A-240-D | BE7K-PCIERISER-M7 |
| Misc. | Power Supplies | UCSC-PSU1-1200W-D | BECE-PSU-M7 |
| Trusted Platform Module | UCSX-TPM-002C-D | BECE-TPM-M7 |
| Rack-mounting kit | UCSC-RAIL-D |  |
| (Autoexpands) | Heat sinks for CPU | UCSC-HSHP-C240M7 |  |
| Blanking panel (DIMM slot) | UCS-DDR5-BLK |  |
| Blanking panel (disk slot) | UCSC-BBLKD-M7 |  |
| Storage cable | CBL-SAS-Y-C240M7 |  |
| RAID Controller Bracket | UCSC-SDBKT-24XM7 |  |
| Daughterboard for OCP NIC | UCSC-OCP3-KIT-D | BECE-MLOMNICKIT-M7 |
| Blanking panel (Riser2) | UCSC-FBRS2-C240-D |  |
| Blanking panel (Riser3) | UCSC-FBRS3-C240-D |  |

| SKU | Description | Project Codename * |
|---|---|---|
| VTS-LSVR-M3 | Cisco Multiparty Media 400v HW-only (UCS M3) No SW preloads or ESXi | Movellan |

| SKU | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M3S= | SL1 (Ivy Bridge) | 1 | UCSC-C220-M3S= |
| CIT3-CPU-E5-2667B= | IC-MP,X86,64BIT,3.3GHz,LGA2011,130W,C-TEMP 0 to 70'C,Xeon E5-2667 v2/8C/25M Cache,IVY BRIDGE-EP,Pb free | 2 | UCS-CPU-E52667B= |
| CIT2-MR-1X082RY-A= | 8GB DDR3-1600-MHz RDIMM/PC3-12800/dual rank/1.35v | 2 | UCS-MR-1X082RY-A= |
| CIT3-A03-D300GA2= | 2.5" 300GB, 10K RPM, SAS 6Gb | 2 | A03-D300GA2= |
| CIT3-PSU-450W= | 450W power supply for C-series rack servers | 1 | UCSC-PSU-450W= |
| CIT3-RAID-MZ-220= | Cisco UCS RAID SAS 2008M-8i Mezz Card for C220 | 1 | UCSC-RAID-MZ-220= |
| R2XX-RAID1= | Enable Raid 1 Setting | 1 | N/A - Config Only |

| SKU | Description | Project Codename * |
|---|---|---|
| CTI-410V-VTS-K9 | Cisco Multiparty Media 410v (UCS C220-M4) No SW preloads or ESXi | Blue Steel |
| CTI-410VB-VTS-K9 | Cisco Multiparty Media 410b (UCS B200-M4) No SW preloads or ESXi | Blue Jays |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M4S | UCS C220 M4 SFF w/o CPU mem HDD PCIe PSU w/ rail kit | 1 | UCSC-C220-M4S= |
| CIT3-CPU-E52690D | 2.60 GHz E5-2690 v3/135W 12C/30MB Cache/DDR4 2133MHz | 2 | UCS-CPU-E52690D= |
| CIT3-MR-1X081RU-A | 8GB DDR4-2133-MHz RDIMM-PC4-17000/single rank/x4/1.2v | 8 | UCS-MR-1X081RU-A= |
| CIT3-A03-D300GA2 | 300GB 6Gb SAS 10K PRM SFF HDD/hot plug/drive sled mounted | 2 | A03-D300GA2= |
| CIT3-PSU1-770W | 770W AC Hot-Plug Power Supply for 1U C-Series Rack Server | 2 | UCSC-PSU1-770W= |
| CIT3-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| R2XX-RAID1= | Enable Raid 1 Setting | 1 | N/A - Config Only |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-B200-M4-U | UCS B200 M4 w/o CPU mem drive bays HDD mezz | 1 | UCSB-B200-M4= |
| CIT3-CPU-E52690D | 2.60 GHz E5-2690 v3/135W 12C/30MB Cache/DDR4 2133MHz | 2 | UCS-CPU-E52690D= |
| CIT3-MR-1X081RU-A | 8GB DDR4-2133-MHz RDIMM-PC4-17000/single rank/x4/1.2v | 8 | UCS-MR-1X081RU-A= |
| CIT3-A03-D300GA2 | 300GB 6Gb SAS 10K PRM SFF HDD/hot plug/drive sled mounted | 2 | A03-D300GA2= |
| CIT3-MLOM-40G-01 | Cisco UCS VIC 1240 modular LOM for M3 blade servers | 1 | UCSB-MLOM-40G-01= |
| CIT3-UCSB-MRAID12G | Cisco FlexStorage 12G SAS RAID controller with Drive bays | 1 | UCSB-MRAID12G= |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| CTI-CMS-1000-K9 | Cisco Meeting Server 1000 | Puffin Island |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSC-C220-M4S | UCS C220 M4 SFF w/o CPU mem HDD PCIe PSU w/ rail kit | 1 | UCSC-C220-M4S= |
| CIT3-CPU-E52695E | 2.10 GHz E5-2695 v4/120W 18C/45MB Cache/DDR4 2400MHz | 2 | UCS-CPU-E52695E= |
| CIT3-MR-1X081RV-A | 8GB DDR4-2400-MHz RDIMM/PC4-19200/single rank/x4/1.2v | 8 | UCS-MR-1X081RV-A= |
| CIT3-HD300G10K12G | 300GB 12G SAS 10K RPM SFF HDD | 2 | UCS-HD300G10K12G= |
| CIT3-PSU1-770W | 770W AC Hot-Plug Power Supply for 1U C-Series Rack Server | 2 | UCSC-PSU1-770W= |
| CIT3-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| R2XX-RAID1= | Enable Raid 1 Setting | 1 | N/A - Config Only |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| CTI-CMS1KM5-BUN-K9 | Cisco Meeting Server 1000 | ???? |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCS-C-C220-M5SX | UCS C220 M5 SFF 10 HD w/o CPU mem HDD PCIe PSU | 1 | UCSC-C220-M5SX= |
| UCS-CPU-6140 | 2.3GHz Xeon Gold 6140 140W 18C 24.75MB Cache | 2 | UCS-CPU-6140= |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666MHz RDIMM/PC4-21300 | 8 | UCS-MR-X16G1RS-H= |
| UCS-HD300G10K12N | 300GB 12G SAS 10K RPM SFF HDD | 2 | UCS-HD300G10K12N= |
| CIMC-LATEST | IMC SW (Recommended) latest release for C-Series Servers | 1 |  |
| UCSC-PSU1-770W | Cisco UCS 770W AC Power Supply for Rack Server | 2 | UCSC-PSU1-770W= |
| UCSC-RAILB-M4 | Ball Bearing Rail Kit for C220 & C240 M4 & M5 rack servers | 1 | UCSC-RAILB-M4= |
| UCSC-HS-C220M5 | Heat sink for UCS C220 M5 rack servers 150W CPUs & below | 2 | UCSC-HS-C220M5= |
| UCSC-BBLKD-S2 | UCS C-Series M5 SFF drive blanking panel | 8 | UCSC-BBLKD-S2= |
| CBL-SC-MR12GM52 | Super Cap cable for UCSC-RAID-M5 on C240 M5 Servers | 1 | CBL-SC-MR12GM52= |
| UCSC-SCAP-M5 | Super Cap for UCSC-RAID-M5, UCSC-MRAID1GB-KIT | 1 | UCSC-SCAP-M5= |
| UCSC-RAID-M5 | Cisco 12G Modular RAID controller with 2GB cache | 1 | UCSC-RAID-M5= |
| C1UCS-OPT-OUT | Cisco ONE Data Center Compute Opt Out Option | 1 |  |
| R2xx-RAID1 | Enable RAID 1 Setting | 1 |  |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| CTI-CMS-1K-M6-K9 | Cisco Meeting Server 1000 | ???? |

| CMS PID | UCS PID | Description | Quantity |
|---|---|---|---|
| CTI-CMS-1K-M6-K9 | UCSC-C220-M6S | UCS C220 M6 Rack w/o CPU, mem, drives, 1U wSFF HDD backplane | 1 |
| CIT3-CPU-I6336Y | UCS-CPU-I6336Y | Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz | 2 |
| CIT3-MR-X16G1RW | UCS-MR-X16G1RW | 16GB RDIMM SRx4 3200 (8Gb) | 16 |
| CIT3-SDB960SA1V | UCS-SDB960SA1V | 960GB 2.5 inch Enterprise Value 6G SATA SSD | 2 |
| CIT3-RAID-220M6 | UCSC-RAID-M6T | Cisco 12G SAS RAID Controller w/4GB FBWC (16 Drv) w/1U Brkt | 1 |
| CIT3-PSU1-1050W | UCSC-PSU1-1050W | Cisco UCS 1050W AC Power Supply for Rack Server | 2 |
| CIT3-TPM-002C | UCSX-TPM-002C | TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers | 1 |
| Auto Expanded PIDs |
|  | CIMC-LATEST | IMC SW (Recommended) latest release for C-Series Servers | 1 |
|  | UCS-DIMM-BLK | UCS DIMM Blanks | 16 |
|  | UCSC-HSLP-M6 | Heatsink for 1U/2U LFF/SFF GPU SKU | 2 |
|  | UCSC-R2R3-C220M6 | C220 / C225 M6 UCSC -HH Riser2 and Riser 3 KIT | 1 |
|  | CBL-SAS-C220M6 | C220M6 SAS cable (1U); (Pismo HBA) | 1 |
|  | CBL-SCAP-C220M6 | C220/C240M6 1U/2U Super Cap cable | 1 |
|  | UCSC-BBLKD-S2 | UCS C-Series M5 SFF drive blanking panel | 8 |
|  | UCS-SCAP-M6 | M6 SuperCap | 1 |
|  | UCSC-RAIL-M6 | ASY,MECH,RAIL KIT,BALL BEARING,M6 | 1 |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| CTI-CMS-2K-BUN-K9 | Cisco Meeting Server 2000 Hardware and Software Bundle | South Stack |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCS-SPM-MINI | UCS SP Select 5108 AC2 Chassis w/FI6324 | 1 | UCSB-5108-AC2= |
| UCSB-PSU-2500ACDV | 2500W Platinum AC Hot Plug Power Supply -DV | 4 | UCSB-PSU-2500ACDV= |
| N01-UAC1 | Single phase AC power module for UCS 5108 | 1 | N01-UAC1= |
| UCSB-5108-PKG-HW | UCS 5108 Packaging for chassis with half width blades. | 1 |  |
| UCS-FI-M-6324 | UCS 6324 In-Chassis FI with 4 UP, 1x40G ExpPort, 16 10Gb | 2 | UCS-FI-M-6324= |
| N10-MGT013 | UCS Manager 3.0 for FI 6324 use only | 2 |  |
| N20-FW014 | UCS 5108 BladeChassisFW Package 3.1 | 1 |  |
| N20-FAN5 | Fan module for UCS 5108 | 8 | N20-FAN5= |
| N20-CAK | Accessory kit for UCS 5108 Blade Server Chassis | 1 | N20-CAK= |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-B200-M4-U | UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG) | 1 | UCSB-B200-M4= |
| UCS-CPU-E52695E | 2.10 GHz E5-2695 v4/120W 18C/45MB Cache/DDR4 2400MHz | 2 | UCS-CPU-E52695E= |
| UCSB-MLOM-40G-03 | Cisco UCS VIC 1340 modular LOM for blade servers | 1 | UCSB-MLOM-40G-03= |
| UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 1 | UCSB-MLOM-PT-01= |
| UCSB-HS-EP-M4-R | CPU Heat Sink for UCS B200 M4/B420 M4 (Rear) | 1 | UCSB-HS-EP-M4-R= |
| UCSB-HS-EP-M4-F | CPU Heat Sink for UCS B200 M4/B420 M4 (Front) | 1 | UCSB-HS-EP-M4-F= |
| C1UCS-OPT-OUT | Cisco ONE Data CenterCompute Opt Out OptionSingleLicense Key | 1 |  |
| UCS-HD300G10K12G | 300GB 12G SAS 10K RPM SFF HDD | 2 | UCS-HD300G10K12G= |
| UCSB-MRAID12G | Cisco FlexStorage12G SAS RAID controller with Drive bays | 1 | UCSB-MRAID12G= |
| UCS-MR-1X081RV-A | 8GB DDR4-2400-MHz RDIMM/PC4-19200/single rank/x4/1.2v | 8 | UCS-MR-1X081RV-A= |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-B200-M4-U | UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG) | 7 | UCSB-B200-M4= |
| UCS-CPU-E52695E | 2.10 GHz E5-2695 v4/120W 18C/45MB Cache/DDR4 2400MHz | 14 | UCS-CPU-E52695E= |
| UCSB-MLOM-40G-03 | Cisco UCS VIC 1340 modular LOM for blade servers | 7 | UCSB-MLOM-40G-03= |
| UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 7 | UCSB-MLOM-PT-01= |
| UCSB-HS-EP-M4-R | CPU Heat Sink for UCS B200 M4/B420 M4 (Rear) | 7 | UCSB-HS-EP-M4-R= |
| UCSB-HS-EP-M4-F | CPU Heat Sink for UCS B200 M4/B420 M4 (Front) | 7 | UCSB-HS-EP-M4-F= |
| C1UCS-OPT-OUT | Cisco ONE Data CenterCompute Opt Out OptionSingleLicense Key | 7 |  |
| UCSB-LSTOR-BK | FlexStorageblanking panels w/o controller, w/o drive bays | 14 | UCSB-LSTOR-BK= |
| UCS-MR-1X081RV-A | 8GB DDR4-2400-MHz RDIMM/PC4-19200/single rank/x4/1.2v | 56 | UCS-MR-1X081RV-A= |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| CTI-CMS2KM5-BUN-K9 | Cisco Meeting Server 2000 Hardware and Software Bundle | ??? |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-5108-AC2 | UCS 5108 Blade Server AC2 Chassis, 0 PSU/8 fans/0 FEX | 1 | UCSB-5108-AC2= |
| UCSB-PSU-2500ACDV | 2500W Platinum AC Hot Plug Power Supply -DV | 4 | UCSB-PSU-2500ACDV= |
| N01-UAC1 | Single phase AC power module for UCS 5108 | 1 | N01-UAC1= |
| UCSB-5108-PKG-HW | UCS 5108 Packaging for chassis with half width blades. | 1 |  |
| UCS-FI-M-6324 | UCS 6324 In-Chassis FI with 4 UP, 1x40G ExpPort, 16 10Gb | 2 | UCS-FI-M-6324= |
| N10-MGT016 | UCS Manager v4.0 | 2 |  |
| N20-FW016 | UCS 5108 Blade Chassis FW Package 4.0 | 1 |  |
| N20-FAN5 | Fan module for UCS 5108 | 8 | N20-FAN5= |
| N20-CAK | Accessory kit for UCS 5108 Blade Server Chassis | 1 | N20-CAK= |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-B200-M5 | UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG) | 1 | UCSB-B200-M5= |
| UCS-CPU-6140 | 2.3 GHz 6140/140W 18C/24.75MB Cache/DDR4 2666MHz | 2 | UCS-CPU-6140= |
| UCSB-MLOM-40G-03 | Cisco UCS VIC 1340 modular LOM for blade servers | 1 | UCSB-MLOM-40G-03= |
| UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 1 | UCSB-MLOM-PT-01= |
| UCSB-HS-M5-R | CPU Heat Sink for UCS B-Series M5 CPU socket (Rear) | 1 | UCSB-HS-M5-R= |
| UCSB-HS-M5-F | CPU Heat Sink for UCS B-Series M5 CPU socket (Front) | 1 | UCSB-HS-M5-R= |
| C1UCS-OPT-OUT | Cisco ONE Data CenterCompute Opt Out OptionSingleLicense Key | 1 |  |
| UCS-HD300G10K12G | 300GB 12G SAS 10K RPM SFF HDD | 2 | UCS-HD300G10K12G= |
| UCSB-MRAID12G | Cisco FlexStorage12G SAS RAID controller with Drive bays | 1 | UCSB-MRAID12G= |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 8 | UCS-MR-X16G1RS-H= |
| UCS-DIMM-BLK | UCS DIMM Blanks | 12 | UCS-DIMM-BLK= |

| SKU / PID | Description | Quantity | FRU |
|---|---|---|---|
| UCSB-B200-M5 | UCS B200 M4 w/o CPU, mem, drive bays, HDD, mezz(UPG) | 7 | UCSB-B200-M5= |
| UCS-CPU-6140 | 2.3 GHz 6140/140W 18C/24.75MB Cache/DDR4 2666MHz | 14 | UCS-CPU-6140= |
| UCSB-MLOM-40G-03 | Cisco UCS VIC 1340 modular LOM for blade servers | 7 | UCSB-MLOM-40G-03= |
| UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 7 | UCSB-MLOM-PT-01= |
| UCSB-HS-M5-R | CPU Heat Sink for UCS B-Series M5 CPU socket (Rear) | 7 | UCSB-HS-M5-R= |
| UCSB-HS-M5-F | CPU Heat Sink for UCS B-Series M5 CPU socket (Front) | 7 | UCSB-HS-M5-F= |
| C1UCS-OPT-OUT | Cisco ONE Data CenterCompute Opt Out OptionSingleLicense Key | 7 |  |
| UCSB-LSTOR-BK | FlexStorageblanking panels w/o controller, w/o drive bays | 14 | UCSB-LSTOR-BK= |
| UCS-MR-X16G1RS-H | 16GB DDR4-2666-MHz RDIMM/PC4-21300/single rank/x4/1.2v | 56 | UCS-MR-X16G1RS-H= |
| UCS-DIMM-BLK | UCS DIMM Blanks | 12 | UCS-DIMM-BLK= |

| CTI-CMS-2K-M6-K9 |  |  |  |
|---|---|---|---|
| CIT3-FAN5 | N20-FAN5 | Fan module for UCS 5108 | 8 |
| CIT3-PSUT2500ACDV | UCSB-PSUT2500ACDV | 2500W Titanium AC Hot Plug Power Supply - DV | 4 |
| CIT3-UAC1 | N01-UAC1 | Single phase AC power module for UCS 5108 | 1 |
| CIT3-FI-M-6324 | UCS-FI-M-6324 | UCS 6324 In-Chassis FI with 4 UP, 1x40G Exp Port, 16 10Gb | 2 |
| CIT3-5108-PKG-HW | UCSB-5108-PKG-HW | UCS 5108 Packaging for chassis with half width blades. | 1 |

| CIT3-B200-M6-CON | UCSB-B200-M6 | CMS Control Blade |  |
|---|---|---|---|
| CIT3-CPU-I6336Y | UCS-CPU-I6336Y | Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz | 2 |
| CIT3-MR-X16G1RW | UCS-MR-X16G1RW | 16GB RDIMM SRx4 3200 (8Gb) | 16 |
| CIT3-RAID12G-M6 | UCSB-RAID12G-M6 | Cisco M6 FlexStorage 12G SAS RAID Controller | 1 |
| CIT3-SDC960SA1V | UCS-SDC960SA1V | 960GB 2.5 inch Enterprise Value 6G SATA SSD | 2 |
| CIT3-MLOM-40G-04 | UCSB-MLOM-40G-04 | Cisco UCS VIC 1440 modular LOM for Blade Servers | 1 |
| CIT3-MLOM-PT-01 | UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 1 |
| CIT3-TPM-002C | UCSX-TPM-002C | TPM 2.0, TCG, FIPS140-2, CC EAL4+ Certified, for M6 servers | 1 |

| CIT3-B200-M6 | UCSB-B200-M6-U | CMS Media Blade |  |
|---|---|---|---|
| CIT3-CPU-I6336Y | UCS-CPU-I6336Y | Intel 6336Y 2.4GHz/185W 24C/36MB DDR4 3200MHz | 14 |
| CIT3-MR-X16G1RW | UCS-MR-X16G1RW | 16GB RDIMM SRx4 3200 (8Gb) | 112 |
| CIT3-MLOM-40G-04 | UCSB-MLOM-40G-04 | Cisco UCS VIC 1440 modular LOM for Blade Servers | 7 |
| CIT3-MLOM-PT-01 | UCSB-MLOM-PT-01 | Cisco UCS Port Expander Card (mezz) for VIC | 7 |
|  | N20-CAK | Access. kit for 5108 Blade Chassis incl Railkit, KVM dongle | 1 |
|  | N20-FW018 | UCS 5108 Blade Chassis FW Package 4.2 | 8 |
|  | UCSB-HS-M6-F | CPU Heat Sink for UCS B-Series M6 CPU socket (Front) | 8 |
|  | UCSB-HS-M6-R | CPU Heat Sink for UCS B-Series M6 CPU socket (Rear) | 8 |
|  | UCS-DIMM-BLK | UCS DIMM Blanks | 128 |
|  | N10-MGT018 | UCS Manager v4.2 and Intersight Managed Mode v4.2 | 1 |
|  | UCSB-FBLK-M6 | Cisco B200 M6 Front Drive Blank Sleds | 14 |
|  | N20-CBLKB1 | Blade slot blanking panel for UCS 5108/single slot | 7 |

| SKU / PID | Description | End of Sale? |
|---|---|---|
| UCSC-C220-M3SBE | Medium TRC#2, HW Only equivalent of original BE6K MD | N |

| SKU / PID | Description | Project Codename * |
|---|---|---|
| TCS-M4-PROBUN-K9 | TCS with 5 Record/ 2 Live with Premium Resolution licenses | Sonoma Beach |
| TCS-M4-PRO10P-K9 | TCS with 10 Record/ 2 Live with Premium Resolution licenses | Sonoma Beach |
|  |  |  |
|  |  |  |

| CITG Adopter PID | SAVBU PN | Description | QTY | SAVBU FRU |
|---|---|---|---|---|
| TCS-M4-PROBUN-K9 TCS-M4-PRO10P-K9 | UCSC-C220-M4S | UCS C220 M4 SFF w/o CPU  mem  HD  PCIe  PSU  rail kit | 1 | UCSC-C220-M4S= |
| CVC-CPU-E52640D | UCS-CPU-E52640D | 2.60 GHz E5-2640 v3/90W 8C/20MB Cache/DDR4 1866MHz | 2 | UCS-CPU-E52640D= |
| CVC-MR-1X081RU-A | UCS-MR-1X081RU-A | 8GB DDR4-2133-MHz RDIMM/PC4-17000/single rank/x4/1.2v | 4 | UCS-MR-1X081RU-A= |
| CVC-A03-D600GA2 | A03-D600GA2 | 600GB 6Gb SAS 10K RPM SFF HDD/hot plug/drive sled mounted | 2 | A03-D600GA2= |
| UCSC-RAILB-M4 | UCSC-RAILB-M4 | Ball Bearing Rail Kit for C220 M4 and C240 M4 rack servers | 1 | UCSC-RAILB-M4= |
| CVC-PSU1-770W | UCSC-PSU1-770W | 770W AC Hot-Plug Power Supply for 1U C-Series Rack Server | 2 | UCSC-PSU1-770W= |
| CAB-9K12A-NA | CAB-9K12A-NA | Power Cord 200/240V 6A North America | 2 | CAB-9K12A-NA= |
| UCSC-SCCBL220 | UCSC-SCCBL220 | Supercap cable 950mm | 1 | UCSC-SCCBL220= |
| UCSC-HS-C220M4 | UCSC-HS-C220M4 | Heat sink for UCS C220 M4 rack servers | 2 | UCSC-HS-C220M4= |
| UCSC-MLOM-BLK | UCSC-MLOM-BLK | MLOM Blanking Panel | 1 | UCSC-MLOM-BLK= |
| N20-BBLKD | N20-BBLKD | UCS 2.5 inch HDD blanking panel | 6 | N20-BBLKD= |
| CVC-MRAID12G | UCSC-MRAID12G | Cisco 12G SAS Modular Raid Controller | 1 | UCSC-MRAID12G= |
| CVC-PCIE-IRJ45 | UCSC-PCIE-IRJ45 | Intel i350 Quad Port 1Gb Adapter | 1 | UCSC-PCIE-IRJ45= |

| SKU | Description | Project Codename |
|---|---|---|
| CE1400V-M7-K9 | Cisco Expressway CE1400V Appliance | KreeAC4 |

|  | Description | PID | Adopter PID |
|---|---|---|---|
| Leveraged Base Server | UCS-M7-MLB | UCSC-C220-M7S |  |
| CPU | (16C/3.6GHz) | UCS-CPU-I6544Y | CE-CPU-M7 |
| Memory | 5600MHz 16GB DIMMs | UCS-MRX16G1RE3 | BECE-RAM-M7 |
| Storage | RAID Controller | UCSC-RAID-M1L16 | BE6CE-RAIDCTRLR-M7 |
| 600GB 10K SAS HDD | UCS-HD600G10KJ4-D | BECE-DISK-M7 |
| Network + IO | OCP 3.0 MLoM NIC | UCSC-O-ID10GC-D | BECE-OCPNIC-M7 |
| PCIe NIC (4x10GE SFP+) | UCSC-PCIEIQ10GF-D | BECE-PCIENIC-M7 |
| 10GE Fiber SFP+ | SFP-10G-SR | SFP-10G-SR |
| 10GE Cu RJ45 SFP+ | GLC-TE | GLC-TE |
| PCIe Riser | UCSC-RIS1A-22XM7 | BE6CE-PCIERISR1-M7 |
| UCSC-RIS2A-22XM7 | CE-PCIERISER2-M7 |
| Misc. | Power Supplies | UCSC-PSU1-1200W-D | BECE-PSU-M7 |
| Trusted Platform Module | UCSX-TPM-002C-D | BECE-TPM-M7 |
| Rack-mounting kit | UCSC-RAIL-D |  |
| (Autoexpands) | Heat sinks for CPU | UCSC-HSLP-C220M7 |  |
| Blanking panel (DIMM slot) | UCS-DDR5-BLK |  |
| Blanking panel (disk slot) | UCSC-BBLKD-M7 |  |
| Storage cable | CBL-SAS-Y-C220M7 |  |
| RAID Controller Bracket | UCSC-HPBKT-22XM7 |  |
| Daughterboard for OCP NIC | UCSC-OCP3-KIT-D | BECE-MLOMNICKIT-M7 |
| Blanking panel (Riser3) | UCSC-FBRS-C220-D |  |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Jun-2025 | Initial Release |