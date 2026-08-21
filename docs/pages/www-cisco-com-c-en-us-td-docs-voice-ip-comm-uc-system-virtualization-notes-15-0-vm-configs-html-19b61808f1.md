---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-virtualization-notes-15-0-vm-configs-html-19b61808f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/notes_15_0_vm_configs.html
retrieved_at: 2026-08-21T04:31:41.657639+00:00
---

Notes on Unified CCE Release 15.0(1) VM Configurations

# Notes on Unified CCE Release 15.0(1) VM Configurations

# Notes on Unified CCE Release 
15.0(1) VM Configurations and IOPS

## Notes on VMware VM Templates for 15.0(1) (top

To access the Unified CCE VM templates, go to the Cisco Software Downloads page and search for Contact Center . From the search results, select Contact Center Solutions > Unified Contact Center Enterprise and then choose the Unified Contact Center Enterprise Virtual Machine as the Templates Software Type and download the following OVA templates:

- Cisco Unified Contact Center Enterprise 15.0(1) Administrative Client Virtual Machine Template for Windows 10 & 11: Administrative_Client_OVA_15.0.1.zip

- UCCE ova files: ucce-ova-15.0.1.zip

For Packaged CCE, select Contact Center Solutions > Packaged Contact Center Enterprise , and then choose the Packaged Contact Center Enterprise Virtual Machine Templates Software Type.

For the VM templates of the remaining CCE components, navigate to Contact Center > Options for Contact Center Solutions to download the OVA templates of the following components:

- Enterprise Chat and Email

- Finesse - same path includes standalone IdS OVA Template for 15.0(1)

- Unified Call Studio

- Unified Contact Center Management Portal

- Unified Customer Voice Portal

- Unified Intelligence Center - same path includes standalone LiveData OVA Template for 15.0(1)

- Virtualized Voice Browser

Reverse Proxy can be downloaded in the following paths:

For Packaged CCE, select Contact Center Solutions > Packaged Contact Center Enterprise , and then choose the Contact Center Reverse Proxy Installer Software Type.

## Notes on Nutanix VM Templates for 15.0(1) SU2 (top

Fresh Install on Nutanix is supported for all Windows-based and VOS-based CCE components. Use the Nutanix OVA and follow the existing install procedures in the Installation chapter of the Cisco Unified CCE or Packaged CCE Installation and Upgrade Guide, Release 15.0(1).

To migrate CCE VOS-based components from an existing 12.6(2) or 15.0(1) VMware deployment to 15.0(1) SU2 on Nutanix, use the Fresh Install with Import option. See the Migration from VMware to Nutanix chapter in the same guides.

See the Installation chapter for Fresh Install and the Migration from VMware to Nutanix chapter for migration in the following guides:

- Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

- Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

## Notes on Router VM Configuration for Version 15.0(1) (top

For information on the capacity limits such as Agent Limits, see the Solution Design Guide for Cisco Unified Contact Center Enterprise.

## Notes on Logger VM Configuration for Version 15.0(1) (top)

For information on the capacity limits such as Agent Limits, see the Solution Design Guide for Cisco Unified Contact Center Enterprise.

## Notes on Small PG VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Small Peripheral Gateway 
	(PG) Virtual Machine configuration sized for a maximum capacity of 250 
	agents.

## Notes on Medium PG VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Medium Peripheral Gateway 
	(PG) Virtual Machine configuration sized for a maximum capacity of 2,000 
	active agents and 7 All Events Clients. This OVA must be used for the 
	following PGs in a Virtual Machine configuration.

- Agent PG

- VRU PG

- MR PG

## Notes on Large PG VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Large Peripheral Gateway 
	(PG) Virtual Machine configuration sized for a maximum capacity of 2,000 
	active agents and 20 All Events Clients. This OVA must be used for the 
	following PGs in a Virtual Machine configuration.

- Agent PG

- VRU PG

- MR PG

## Notes on Administration Client VM Configuration for Version 15.0(1) (top)

Used for Unified CCE Administration Clients. May also be used for ISE.

The OVA is also supported on Windows client operating systems.

## Notes on Administration Server - AW VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Administration Workstation 
	(AW) Server Virtual Machine configuration sized for an administration and 
	data server with a maximum capacity of 50 reporting users.

## Notes on AW-HDS VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Administration 
	Workstation-Historical Data Server (AW-HDS) Virtual Machine configuration 
	sized for a real-time and historical administration and data server with a 
	maximum capacity of 200 reporting users.

## Notes on AW-HDS-DDS VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Administration 
	Workstation-Historical Data Server-Detailed Data Server (AW-HDS-DDS) Virtual 
	Machine configuration sized for a real-time, historical, and detailed data 
	administration and data server with a maximum capacity of 200 reporting 
	users.

## Notes on HDS-DDS VM Configuration for Version 15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Historical Data 
	Server-Detailed Data Server (HDS-DDS) Virtual Machine configuration sized 
	for a historical and detailed data server with a maximum capacity of 200 
	reporting users.

## Notes on Live Data Server VM Configuration for Version 
	15.0(1) (top)

Cisco Unified Contact Center Enterprise (CCE) Large Live Data Server 
	sized for the capacity limits shown below.

Capacity Limits for 48000 Agents:

- 48000 Live Data clients

- Up to 48 Unified CCE Agent Peripherals

Capacity Limits for 36000 Agents:

- 36000 Live Data clients

- Up to 36 Unified CCE Agent Peripherals

Capacity Limits for 24000 Agents:

- 24000 Live Data clients

- Up to 24 Unified CCE Agent Peripherals

Capacity Limits for 12000 Agents:

- 12000 Live Data clients

- Up to 12 Unified CCE Agent Peripherals

Capacity Limits for 4000 Agents:

- 4000 Live Data clients

- Up to 4 Unified CCE Agent Peripherals

## Notes on Co-resident Live Data, Unified Intelligence Center, Cisco Identity 
	Service for Version 15.0(1) (top)

Capacity Limits for 2000 Agents:

- 2000 Live Data Reporting Clients

- 200 Unified Intelligence Center Reporting Clients

- Up to 4 Unified CCE Agent Peripherals

## Notes on Cisco Enterprise 
	Chat and Email for Version 15.0(1) (top)

Cisco Enterprise Chat and Email (ECE) specifications apply only for ECE 
	400 agent on-box deployments. The disk storage comprises of 3 datastores with the 
	following capacities each: 80 GB, 50 GB, and 300 GB.

## Notes on VM vDisk Configuration 
	for Databases (top)

This Virtual Machine Template does not automatically provision the 
	required application database virtual disk drive. Refer to the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide and the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, for instructions on database drive 
	creation post-VM template deployment.

## IOPS and Storage System Performance Requirements 
	for Databases (top)

Contact Center Enterprise (CCE) follows UC storage system design requirements. For more 
	information, see UC Virtualization Storage System Design 
	Requirements.

For information about TRC versus specs-based support for storage systems, 
	see UC Virtualization Supported Hardware .

All CCE VM vDisks must be deployed Thick Provisioned, Lazy, or Eager Zeroed. Thin Provisioned vDisks are not supported.

For IOPS information about CUIC, see the CUIC IOPS
	information.

Storage Area Networks and Specs-based policy storage solutions must be able 
	to handle the following CCE application disk I/O characteristics. Tested Reference Configurations (TRC) for Cisco UCS C-Series servers do not need to apply these requirements against their Direct Attached Storage Arrays (DAS).

### Contact Center Enterprise 15.0(1)

Note that the data in this table is arrived based on the Cisco Collaboration Infrastructure Requirements and is provided only for 
	planning purposes. The results will vary based on the hardware, load, and 
	other factors that are applicable to your deployment.

### 15.0(1) SU2 IOPS for Nutanix

| Contact Center Enterprise Components | IOPS | Disk Read KBytes / sec | Disk Write KBytes / sec | Operating Conditions |
|---|---|---|---|---|
| Peak | Avg. | 95th Percentile | Peak | Avg. | 95th Percentile | Peak | Avg. | 95th Percentile |
| Rogger | 1915 | 61 | 165 | 22523 | 253 | 712 | 17491 | 1467 | 4815 | 4000 agents; 30 CPS; ECC; 5 scalars @ 40 bytes each; 200 Reporting users at max query load. |
| AW-HDS-DDS | 7595 | 1453 | 2768 | 68704 | 1206 | 11275 | 97277 | 5626 | 18304 |
| Cisco Identity Server (Ids) | 18 | 7 | 11 | 6 | 0.009 | 0 | 3123 | 118 | 186 |
| Small Live Data | 276 | 9 | 13 | 1914 | 12 | 27 | 10161 | 207 | 276 |
| Rogger | 2858 | 281 | 1444 | 65897 | 2066 | 12658 | 27042 | 4004 | 14970 | 2000 agents; 15 CPS; ECC; 5 scalars @ 40 bytes each; 
		100 Reporting 
		users at max query load and 7 CTI Clients. |
| AW-HDS-DDS | 2997 | 936 | 1880 | 47296 | 1136 | 8928 | 58333 | 3841 | 11557 |
| Medium PG | 170 | 74 | 104 | 337 | 4 | 23 | 3442 | 1007 | 2467 |
| CUIC-LD-IdS | 803 | 51 | 59 | 2875 | 24 | 75 | 45165 | 3426 | 4090 |

| Nutanix Metrics Unified CCE Components | Storage Controller IOPS | Storage Controller Bandwidth – Read | Storage Controller Bandwidth – Write | Operating Conditions |
|---|---|---|---|---|
| Peak | Avg. | 95th Percentile | Peak | Avg. | 95th Percentile | Peak | Avg. | 95th Percentile |
| Rogger | 6410 | 131 | 208 | 507406 | 1174 | 351 | 11820 | 1770 | 5742 | 4,000 agents; 30 CPS; ECC; 5 scalars @ 40 bytes each; 200 Reporting users at max query load. |
| AW-HDS-DDS | 2609 | 1311 | 1518 | 24297 | 39 | 41 | 57204 | 6695 | 9223 |
| Cisco Identity Server (IdS) | 15 | 6 | 10 | 0 | 0 | 0 | 2164 | 116 | 164 |
| Small Live Data | 357 | 8 | 12 | 783 | 3 | 5 | 1761 | 158 | 223 |
| Rogger | 13,181 | 6,982 | 10,531 | 1,121,740 | 601,873 | 885,353 | 48,360 | 2,370 | 9,642 | 2,000 agents; 15 CPS; ECC; 5 scalars @ 40 bytes each; 100 Reporting users at max query load and 7 CTI Clients. |
| AW-HDS-DDS | 1,586 | 757 | 1,015 | 7,922 | 46 | 38 | 30,546 | 5,799 | 10,461 |
| Medium PG | 466 | 33 | 42 | 10,531 | 40 | 105 | 3,810 | 2,488 | 3,289 |
| CUIC-LD-IdS | 96 | 46 | 73 | 317 | 9 | 78 | 3,499 | 520 | 940 |