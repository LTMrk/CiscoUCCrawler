---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-virtualization-virtualization-packaged-contact-center-enterprise-h-a89545b7fb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-packaged-contact-center-enterprise.html
retrieved_at: 2026-08-21T04:32:46.191192+00:00
---

Virtualization for Packaged Contact Center Enterprise

# Virtualization for Packaged Contact Center Enterprise

Updated: January 10, 2019

## Virtualization for Packaged Contact Center Enterprise

The following virtualization details specify the supported third-party software (such as VMware and Nutanix) and its versions. Support for these software versions and their interoperability depends on the release cycles (patches and upgrades) of the third-party software. For example, support for ESXi depends on VMware release cycles.

## Version 15.0(1)

(top)

VM configuration requirements apply to both VMware and Nutanix deployments.

Component &

Capacity Point

VM Configuration Requirements

vCPU

Megahertz (MHz)

Physical CPU Base Frequency

vRAM

vDisk

vNIC

Rogger for 2K and 4K

4

5000

2.50 GHz

6 GB

1 x 150 GB

2

Router for 12K

4

4000

2.50 GHz

8 GB

1 x 150 GB

2

Logger for 12K

4

6000

2.50 GHz

8 GB

1 x 150 GB

2

Medium PG

2

4000

2.50 GHz

6 GB

1 x 150 GB

2

Administration Server - AW

1

750

2.50 GHz

2 GB

1 x 150 GB

1

AW-HDS

8

17500

2.50 GHz

16 GB

1 x 150 GB

1

AW-HDS-DDS

4

5000

2.50 GHz

16 GB

1 x 150 GB

1

HDS-DDS

8

17500

2.50 GHz

16 GB

1 x 150 GB

1

Live Data for 4K concurrent agents

4

5500

2.50 GHz

32 GB

1 x 146 GB

1

Live Data for 12K concurrent agents

8

16500

2.50 GHz

40 GB

1 x 146 GB

1

Cisco IdS 4K and 12K concurrent agents

4

1500

2.50 GHz

10 GB

1 x 146 GB

1

Notes

Common for Nutanix and VMware

- The VM configuration requirements in the table apply to both VMware and Nutanix deployments.

- The VM configurations apply to Release 15.0(1) and all subsequent 15.0(1) SU and ES updates.

- For notes applicable to both VMware and Nutanix, including the OVA download links, see Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS .

- This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for instructions on database drive creation after VM template deployment.

- Virtualization for Unified Contact Center Enterprise - Additional Information

- Notes on UCS Tested Reference Configuration and Specs-based Support or Notes on Megahertz (MHz) Sizing .

- For details on modeling VM placement on a user-defined hardware configuration, see the Quote Collab application .

- For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise .

VMware

- Supported versions of VMware vSphere ESXi: ESXi 7.0U1 and later, and ESXi 8.0U1 (inclusive of all updates, for all versions).

- The 15.0(1) VMware OVA is supported for 15.0(1) and all subsequent 15.0 SU updates.

Version refers to the major ESXi release (for example, 7.0 or 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1 or 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, see Required ESXi version .

If a base ESXi version is listed as supported, all subsequent major update releases, minor point releases, and corresponding patch levels are also supported unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is listed, ESXi 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 are also supported unless a specific exclusion is noted.

- For other details on hardware and VMware support, see Cisco Collaboration Infrastructure .

Nutanix

- Dedicated Nutanix-specific OVA files are available for Packaged CCE components. The resource requirements are the same as the standard 15.0(1) VMware OVAs shown in the table.

- Because Nutanix does not support multiple deployment options within a single OVA file, the existing multi-option OVAs are provided as separate OVA files for Nutanix deployments.

- For validated Nutanix software versions, see the Hypervisor compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) .

## Version 12.6(2)

(top)

Supported Versions of VMware vSphere ESXi = ESXi 6.7, ESXi 7.0 and ESXi 8.0U1 (inclusive of all updates, for all versions)

Component &

Capacity Point

VM Configuration Requirements

click to download OVA file for this version

vCPU

Megahertz (MHz)

Physical CPU Base Frequency

vRAM

vDisk

vNIC

Router

4

4000

2.50 GHz

8 GB

1 x 80 GB

2

Logger

4

6000

2.50 GHz

8 GB

1 x 80 GB

2

Rogger

4

5000

2.50 GHz

6 GB

1 x 80 GB

2

Medium PG

2

4000

2.50 GHz

6 GB

1 x 80 GB

2

Administration Server - AW

1

750

2.50 GHz

2 GB

1 x 80 GB

1

AW-HDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

AW-HDS-DDS

4

5000

2.50 GHz

16 GB

1 x 80 GB

1

HDS-DDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

Live Data for 12000 concurrent agents

8

16500

2.50 GHz

40 GB

1 x 146 GB

1

Live Data for 4000 concurrent agents

4

5500

2.50 GHz

32 GB

1 x 146 GB

1

Cisco Identity Service (IdS) Server

4

1500

2.50 GHz

10 GB

1 x 146 GB

1

Notes:

- Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted.

- This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment.

- For more information on VM configurations, see

- For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure .

- For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application.

- For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise .

## Version 12.6(1)

(top)

Supported Versions of VMware vSphere ESXi = ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, ESXi 6.7, ESXi 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions)

Component &

Capacity Point

VM Configuration Requirements

click to download OVA file for this version

vCPU

Megahertz (MHz)

Physical CPU Base Frequency

vRAM

vDisk

vNIC

Router

4

4000

2.50 GHz

8 GB

1 x 80 GB

2

Logger

4

6000

2.50 GHz

8 GB

1 x 80 GB

2

Rogger

4

5000

2.50 GHz

6 GB

1 x 80 GB

2

Medium PG

2

4000

2.50 GHz

6 GB

1 x 80 GB

2

Administration Server - AW

1

750

2.50 GHz

2 GB

1 x 80 GB

1

AW-HDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

AW-HDS-DDS

4

5000

2.50 GHz

16 GB

1 x 80 GB

1

HDS-DDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

Live Data for 12000 concurrent agents

8

16500

2.50 GHz

32 GB

1 x 146 GB

1

Live Data for 4000 concurrent agents

4

5500

2.50 GHz

32 GB

1 x 146 GB

1

Cisco Identity Service (IdS) Server

4

1500

2.50 GHz

10 GB

1 x 146 GB

1

Notes:

- Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted.

- This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment.

- For more information on VM configurations, see

- For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure .

- For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application.

- For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise .

## Version 12.5

(top)

Supported Versions of VMware vSphere ESXi = 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions)

Component &

Capacity Point

VM Configuration Requirements

click to download OVA file for this version

vCPU

Megahertz (MHz)

Physical CPU Base Frequency

vRAM

vDisk

vNIC

Router

4

4000

2.50 GHz

8 GB

1 x 80 GB

2

Logger

4

6000

2.50 GHz

8 GB

1 x 80 GB

2

Rogger

4

5000

2.50 GHz

6 GB

1 x 80 GB

2

Small PG

2

2000

2.50 GHz

6 GB

1 x 80 GB

2

Medium PG

2

4000

2.50 GHz

6 GB

1 x 80 GB

2

Administration Server - AW

1

750

2.50 GHz

2 GB

1 x 80 GB

1

AW-HDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

AW-HDS-DDS

4

5000

2.50 GHz

16 GB

1 x 80 GB

1

HDS-DDS

8

17500

2.50 GHz

16 GB

1 x 80 GB

1

Live Data for 12000 concurrent agents

8

16500

2.50 GHz

30 GB

1 x 146 GB

1

Live Data for 4000 concurrent agents

4

5500

2.50 GHz

30 GB

1 x 146 GB

1

Cisco Identity Service (IdS) Server

4

1500

2.50 GHz

10 GB

1 x 146 GB

1

Notes:

- Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted.

- This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment.

- For more information on VM configurations, see

- For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure .

- For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application.

- For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise .

Contacts | Feedback

| Virtualization for Packaged Contact Center Enterprise The following virtualization details specify the supported third-party software (such as VMware and Nutanix) and its versions. Support for these software versions and their interoperability depends on the release cycles (patches and upgrades) of the third-party software. For example, support for ESXi depends on VMware release cycles. |
|---|
| Version 15.0(1) | (top) |
| VM configuration requirements apply to both VMware and Nutanix deployments. Component & Capacity Point VM Configuration Requirements vCPU Megahertz (MHz) Physical CPU Base Frequency vRAM vDisk vNIC Rogger for 2K and 4K 4 5000 2.50 GHz 6 GB 1 x 150 GB 2 Router for 12K 4 4000 2.50 GHz 8 GB 1 x 150 GB 2 Logger for 12K 4 6000 2.50 GHz 8 GB 1 x 150 GB 2 Medium PG 2 4000 2.50 GHz 6 GB 1 x 150 GB 2 Administration Server - AW 1 750 2.50 GHz 2 GB 1 x 150 GB 1 AW-HDS 8 17500 2.50 GHz 16 GB 1 x 150 GB 1 AW-HDS-DDS 4 5000 2.50 GHz 16 GB 1 x 150 GB 1 HDS-DDS 8 17500 2.50 GHz 16 GB 1 x 150 GB 1 Live Data for 4K concurrent agents 4 5500 2.50 GHz 32 GB 1 x 146 GB 1 Live Data for 12K concurrent agents 8 16500 2.50 GHz 40 GB 1 x 146 GB 1 Cisco IdS 4K and 12K concurrent agents 4 1500 2.50 GHz 10 GB 1 x 146 GB 1 Notes Common for Nutanix and VMware The VM configuration requirements in the table apply to both VMware and Nutanix deployments. The VM configurations apply to Release 15.0(1) and all subsequent 15.0(1) SU and ES updates. For notes applicable to both VMware and Nutanix, including the OVA download links, see Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS . This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for instructions on database drive creation after VM template deployment. For more information on VM configurations, see: Virtualization for Unified Contact Center Enterprise - Additional Information Notes on UCS Tested Reference Configuration and Specs-based Support or Notes on Megahertz (MHz) Sizing . For details on modeling VM placement on a user-defined hardware configuration, see the Quote Collab application . For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . VMware Supported versions of VMware vSphere ESXi: ESXi 7.0U1 and later, and ESXi 8.0U1 (inclusive of all updates, for all versions). The 15.0(1) VMware OVA is supported for 15.0(1) and all subsequent 15.0 SU updates. Version refers to the major ESXi release (for example, 7.0 or 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1 or 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, see Required ESXi version . If a base ESXi version is listed as supported, all subsequent major update releases, minor point releases, and corresponding patch levels are also supported unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is listed, ESXi 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 are also supported unless a specific exclusion is noted. For other details on hardware and VMware support, see Cisco Collaboration Infrastructure . Nutanix Dedicated Nutanix-specific OVA files are available for Packaged CCE components. The resource requirements are the same as the standard 15.0(1) VMware OVAs shown in the table. Because Nutanix does not support multiple deployment options within a single OVA file, the existing multi-option OVAs are provided as separate OVA files for Nutanix deployments. For validated Nutanix software versions, see the Hypervisor compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) . | VM configuration requirements apply to both VMware and Nutanix deployments. | Component & Capacity Point | VM Configuration Requirements | vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC | Rogger for 2K and 4K | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 | Router for 12K | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 | Logger for 12K | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 | Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 | Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 150 GB | 1 | AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 | AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 | HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 | Live Data for 4K concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 | Live Data for 12K concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 | Cisco IdS 4K and 12K concurrent agents | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 | Notes Common for Nutanix and VMware The VM configuration requirements in the table apply to both VMware and Nutanix deployments. The VM configurations apply to Release 15.0(1) and all subsequent 15.0(1) SU and ES updates. For notes applicable to both VMware and Nutanix, including the OVA download links, see Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS . This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for instructions on database drive creation after VM template deployment. For more information on VM configurations, see: Virtualization for Unified Contact Center Enterprise - Additional Information Notes on UCS Tested Reference Configuration and Specs-based Support or Notes on Megahertz (MHz) Sizing . For details on modeling VM placement on a user-defined hardware configuration, see the Quote Collab application . For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . VMware Supported versions of VMware vSphere ESXi: ESXi 7.0U1 and later, and ESXi 8.0U1 (inclusive of all updates, for all versions). The 15.0(1) VMware OVA is supported for 15.0(1) and all subsequent 15.0 SU updates. Version refers to the major ESXi release (for example, 7.0 or 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1 or 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, see Required ESXi version . If a base ESXi version is listed as supported, all subsequent major update releases, minor point releases, and corresponding patch levels are also supported unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is listed, ESXi 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 are also supported unless a specific exclusion is noted. For other details on hardware and VMware support, see Cisco Collaboration Infrastructure . Nutanix Dedicated Nutanix-specific OVA files are available for Packaged CCE components. The resource requirements are the same as the standard 15.0(1) VMware OVAs shown in the table. Because Nutanix does not support multiple deployment options within a single OVA file, the existing multi-option OVAs are provided as separate OVA files for Nutanix deployments. For validated Nutanix software versions, see the Hypervisor compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) . |
| VM configuration requirements apply to both VMware and Nutanix deployments. |
| Component & Capacity Point | VM Configuration Requirements |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Rogger for 2K and 4K | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 |
| Router for 12K | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 |
| Logger for 12K | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 150 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| Live Data for 4K concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Live Data for 12K concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 |
| Cisco IdS 4K and 12K concurrent agents | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes Common for Nutanix and VMware The VM configuration requirements in the table apply to both VMware and Nutanix deployments. The VM configurations apply to Release 15.0(1) and all subsequent 15.0(1) SU and ES updates. For notes applicable to both VMware and Nutanix, including the OVA download links, see Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS . This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for instructions on database drive creation after VM template deployment. For more information on VM configurations, see: Virtualization for Unified Contact Center Enterprise - Additional Information Notes on UCS Tested Reference Configuration and Specs-based Support or Notes on Megahertz (MHz) Sizing . For details on modeling VM placement on a user-defined hardware configuration, see the Quote Collab application . For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . VMware Supported versions of VMware vSphere ESXi: ESXi 7.0U1 and later, and ESXi 8.0U1 (inclusive of all updates, for all versions). The 15.0(1) VMware OVA is supported for 15.0(1) and all subsequent 15.0 SU updates. Version refers to the major ESXi release (for example, 7.0 or 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1 or 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, see Required ESXi version . If a base ESXi version is listed as supported, all subsequent major update releases, minor point releases, and corresponding patch levels are also supported unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is listed, ESXi 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 are also supported unless a specific exclusion is noted. For other details on hardware and VMware support, see Cisco Collaboration Infrastructure . Nutanix Dedicated Nutanix-specific OVA files are available for Packaged CCE components. The resource requirements are the same as the standard 15.0(1) VMware OVAs shown in the table. Because Nutanix does not support multiple deployment options within a single OVA file, the existing multi-option OVAs are provided as separate OVA files for Nutanix deployments. For validated Nutanix software versions, see the Hypervisor compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) . |
| Version 12.6(2) | (top) |
| Supported Versions of VMware vSphere ESXi = ESXi 6.7, ESXi 7.0 and ESXi 8.0U1 (inclusive of all updates, for all versions) Component & Capacity Point VM Configuration Requirements click to download OVA file for this version vCPU Megahertz (MHz) Physical CPU Base Frequency vRAM vDisk vNIC Router 4 4000 2.50 GHz 8 GB 1 x 80 GB 2 Logger 4 6000 2.50 GHz 8 GB 1 x 80 GB 2 Rogger 4 5000 2.50 GHz 6 GB 1 x 80 GB 2 Medium PG 2 4000 2.50 GHz 6 GB 1 x 80 GB 2 Administration Server - AW 1 750 2.50 GHz 2 GB 1 x 80 GB 1 AW-HDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 AW-HDS-DDS 4 5000 2.50 GHz 16 GB 1 x 80 GB 1 HDS-DDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 Live Data for 12000 concurrent agents 8 16500 2.50 GHz 40 GB 1 x 146 GB 1 Live Data for 4000 concurrent agents 4 5500 2.50 GHz 32 GB 1 x 146 GB 1 Cisco Identity Service (IdS) Server 4 1500 2.50 GHz 10 GB 1 x 146 GB 1 Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . | Supported Versions of VMware vSphere ESXi = ESXi 6.7, ESXi 7.0 and ESXi 8.0U1 (inclusive of all updates, for all versions) | Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version | vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC | Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 | AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 | Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 | Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 | Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Supported Versions of VMware vSphere ESXi = ESXi 6.7, ESXi 7.0 and ESXi 8.0U1 (inclusive of all updates, for all versions) |
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Version 12.6(1) | (top) |
| Supported Versions of VMware vSphere ESXi = ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, ESXi 6.7, ESXi 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) Component & Capacity Point VM Configuration Requirements click to download OVA file for this version vCPU Megahertz (MHz) Physical CPU Base Frequency vRAM vDisk vNIC Router 4 4000 2.50 GHz 8 GB 1 x 80 GB 2 Logger 4 6000 2.50 GHz 8 GB 1 x 80 GB 2 Rogger 4 5000 2.50 GHz 6 GB 1 x 80 GB 2 Medium PG 2 4000 2.50 GHz 6 GB 1 x 80 GB 2 Administration Server - AW 1 750 2.50 GHz 2 GB 1 x 80 GB 1 AW-HDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 AW-HDS-DDS 4 5000 2.50 GHz 16 GB 1 x 80 GB 1 HDS-DDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 Live Data for 12000 concurrent agents 8 16500 2.50 GHz 32 GB 1 x 146 GB 1 Live Data for 4000 concurrent agents 4 5500 2.50 GHz 32 GB 1 x 146 GB 1 Cisco Identity Service (IdS) Server 4 1500 2.50 GHz 10 GB 1 x 146 GB 1 Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . | Supported Versions of VMware vSphere ESXi = ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, ESXi 6.7, ESXi 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) | Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version | vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC | Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 | AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 | Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 | Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 | Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Supported Versions of VMware vSphere ESXi = ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, ESXi 6.7, ESXi 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) |
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Version 12.5 | (top) |
| Supported Versions of VMware vSphere ESXi = 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) Component & Capacity Point VM Configuration Requirements click to download OVA file for this version vCPU Megahertz (MHz) Physical CPU Base Frequency vRAM vDisk vNIC Router 4 4000 2.50 GHz 8 GB 1 x 80 GB 2 Logger 4 6000 2.50 GHz 8 GB 1 x 80 GB 2 Rogger 4 5000 2.50 GHz 6 GB 1 x 80 GB 2 Small PG 2 2000 2.50 GHz 6 GB 1 x 80 GB 2 Medium PG 2 4000 2.50 GHz 6 GB 1 x 80 GB 2 Administration Server - AW 1 750 2.50 GHz 2 GB 1 x 80 GB 1 AW-HDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 AW-HDS-DDS 4 5000 2.50 GHz 16 GB 1 x 80 GB 1 HDS-DDS 8 17500 2.50 GHz 16 GB 1 x 80 GB 1 Live Data for 12000 concurrent agents 8 16500 2.50 GHz 30 GB 1 x 146 GB 1 Live Data for 4000 concurrent agents 4 5500 2.50 GHz 30 GB 1 x 146 GB 1 Cisco Identity Service (IdS) Server 4 1500 2.50 GHz 10 GB 1 x 146 GB 1 Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . | Supported Versions of VMware vSphere ESXi = 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) | Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version | vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC | Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 | Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Small PG | 2 | 2000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 | Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 | AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 | Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 | Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 | Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 | Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Supported Versions of VMware vSphere ESXi = 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) |
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Small PG | 2 | 2000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |
| Contacts \| Feedback |

| VM configuration requirements apply to both VMware and Nutanix deployments. |
|---|
| Component & Capacity Point | VM Configuration Requirements |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Rogger for 2K and 4K | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 |
| Router for 12K | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 |
| Logger for 12K | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 150 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 150 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 150 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 150 GB | 1 |
| Live Data for 4K concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Live Data for 12K concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 |
| Cisco IdS 4K and 12K concurrent agents | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes Common for Nutanix and VMware The VM configuration requirements in the table apply to both VMware and Nutanix deployments. The VM configurations apply to Release 15.0(1) and all subsequent 15.0(1) SU and ES updates. For notes applicable to both VMware and Nutanix, including the OVA download links, see Notes on Unified CCE Release 15.0(1) VM Configurations and IOPS . This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide for instructions on database drive creation after VM template deployment. For more information on VM configurations, see: Virtualization for Unified Contact Center Enterprise - Additional Information Notes on UCS Tested Reference Configuration and Specs-based Support or Notes on Megahertz (MHz) Sizing . For details on modeling VM placement on a user-defined hardware configuration, see the Quote Collab application . For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . VMware Supported versions of VMware vSphere ESXi: ESXi 7.0U1 and later, and ESXi 8.0U1 (inclusive of all updates, for all versions). The 15.0(1) VMware OVA is supported for 15.0(1) and all subsequent 15.0 SU updates. Version refers to the major ESXi release (for example, 7.0 or 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1 or 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, see Required ESXi version . If a base ESXi version is listed as supported, all subsequent major update releases, minor point releases, and corresponding patch levels are also supported unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is listed, ESXi 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 are also supported unless a specific exclusion is noted. For other details on hardware and VMware support, see Cisco Collaboration Infrastructure . Nutanix Dedicated Nutanix-specific OVA files are available for Packaged CCE components. The resource requirements are the same as the standard 15.0(1) VMware OVAs shown in the table. Because Nutanix does not support multiple deployment options within a single OVA file, the existing multi-option OVAs are provided as separate OVA files for Nutanix deployments. For validated Nutanix software versions, see the Hypervisor compatibility section in the Contact Center Enterprise Solution Compatibility Matrix, Release 15.0(1) . |

| Supported Versions of VMware vSphere ESXi = ESXi 6.7, ESXi 7.0 and ESXi 8.0U1 (inclusive of all updates, for all versions) |
|---|
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 40 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |

| Supported Versions of VMware vSphere ESXi = ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, ESXi 6.7, ESXi 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) |
|---|
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 32 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |

| Supported Versions of VMware vSphere ESXi = 7.0 and ESXi 8.0 U1 (inclusive of all updates, for all versions) |
|---|
| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
| vCPU | Megahertz (MHz) | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Router | 4 | 4000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Logger | 4 | 6000 | 2.50 GHz | 8 GB | 1 x 80 GB | 2 |
| Rogger | 4 | 5000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Small PG | 2 | 2000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Medium PG | 2 | 4000 | 2.50 GHz | 6 GB | 1 x 80 GB | 2 |
| Administration Server - AW | 1 | 750 | 2.50 GHz | 2 GB | 1 x 80 GB | 1 |
| AW-HDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| AW-HDS-DDS | 4 | 5000 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| HDS-DDS | 8 | 17500 | 2.50 GHz | 16 GB | 1 x 80 GB | 1 |
| Live Data for 12000 concurrent agents | 8 | 16500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 |
| Live Data for 4000 concurrent agents | 4 | 5500 | 2.50 GHz | 30 GB | 1 x 146 GB | 1 |
| Cisco Identity Service (IdS) Server | 4 | 1500 | 2.50 GHz | 10 GB | 1 x 146 GB | 1 |
| Notes: Version refers to the major ESXi release (for example, 7.0, 8.0), while updates are incremental changes to these major ESXi versions (for example, 8.0U1, 8.0U1a). The specified version or update indicates the minimum supported version or update required for that release. For more information, refer to Required ESXi version . If a base ESXi version is listed as supported, then all its subsequent major update releases, minor point releases, and corresponding patch levels are also considered supported, unless explicitly stated otherwise. For example, if "ESXi 8.0U1 (inclusive of all updates, for all versions)" is mentioned, then 8.0U1, 8.0U1a, 8.0U2, 8.0U2c, and 8.0U3 would also be supported, unless a specific exclusion is noted. This Virtual Machine Template does not automatically provision the required application database virtual disk drive. See the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide and the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide , for instructions on database drive creation post-VM template deployment. For more information on VM configurations, see For all other details on hardware and VMware support, see Cisco Collaboration Infrastructure . For details on modeling VM placement on a user defined hardware configuration, see the Quote Collab application. For details about Live Data deployment, see the Other Limits section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise . |