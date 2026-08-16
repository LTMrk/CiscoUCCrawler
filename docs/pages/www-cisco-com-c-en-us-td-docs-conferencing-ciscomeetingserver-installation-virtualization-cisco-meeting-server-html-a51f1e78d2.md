---
doc_id: www-cisco-com-c-en-us-td-docs-conferencing-ciscomeetingserver-installation-virtualization-cisco-meeting-server-html-a51f1e78d2
source_url: https://www.cisco.com/c/en/us/td/docs/conferencing/ciscoMeetingServer/Installation/virtualization-cisco-meeting-server.html
retrieved_at: 2026-08-16T14:20:20.514050+00:00
---

Virtualization for Cisco Meeting Server

# Virtualization for Cisco Meeting Server

Log in to Save Content

# Virtualization for Cisco Meeting Server

## Version 3.13

Meeting Server supports deployment on Nutanix clusters. This configuration is supported on 220 M7+ HCI nodes.

Qualified versions of prism element: AHV Version: 10.3.1.2 ; AOS Version: 7.3.1.2

Supported Versions of VMware vSphere ESXi: ESXi 8.0 U3e

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- Recorder VM: 1GB per hour required per 720p recording.

- Recorder VM: 4vCPU with 4GB RAM supports 80 concurrent 720p recordings.

- Streamer VM: 4vCPU with 4GB RAM supports 50 concurrent 720p streams.

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.12

Supported Versions of VMware vSphere ESXi: ESXi 8.0.3 P05

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- Recorder VM: 1GB per hour required per 720p recording.

- Recorder VM: 4vCPU with 4GB RAM supports 80 concurrent 720p recordings.

- Streamer VM: 4vCPU with 4GB RAM supports 50 concurrent 720p streams.

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.11

Supported Versions of VMware vSphere ESXi: ESXi 7.0 Update 3s and ESXi 8.0 Update 3d

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- Recorder VM: 1GB per hour required per 720p recording.

- Recorder VM: 4vCPU with 4GB RAM supports 80 concurrent 720p recordings.

- Streamer VM: 4vCPU with 4GB RAM supports 50 concurrent 720p streams.

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.10

Supported Versions of VMware vSphere ESXi: ESXi 7.0 Update 3q and ESXi-8.0U3

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.9

Supported Versions of VMware vSphere ESXi: 7.0 Update 3o

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.8

Supported Versions of VMware vSphere ESXi: 7.0 Update 3n

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75k of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.7

Supported Versions of VMware vSphere ESXi: 6.5 P09, 6.7 P08, 7.0 U3j

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75k of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.6

Supported Versions of VMware vSphere ESXi: 6.5 EP 26, 6.7 EP 23, 7.0 U3d

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75k of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.5

Supported Versions of VMware vSphere ESXi: 6.5 P07, 6.7 EP 23, 7.0 U3d

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75k of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.4

Supported Versions of VMware vSphere ESXi: 6.5 P07, 6.7 P05, 7.0 U2a

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.3

Supported Versions of VMware vSphere ESXi: 6.5 U3, 6.7 U3, 7.0 U2a

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.2

Supported Versions of VMware vSphere ESXi: 6.5 U2, 6.7, 7.0 U1c

Notes:

- * vRAM requirements are 1GB per vCPU with a minimum of 4GB of RAM, but recommended minimum of 8GB. A Combined VM (Edge + Callbridge + DB + Scheduler) only supports 1000 cospaces as a base opposed to the 75,000 of a dedicated Callbridge VM. To support additonal cospaces in a deployment an additional 1GB per 100,000 cospaces is required across all CMS VMs using the Callbridge or Database components. For example, a separate Callbridge VM and Database VM deployment to support 20HD ports and 275,000 cospaces would be required. Additionally, running a Scheduler requires an additional 4GB of RAM.

- Callbridge VM: 16vCPU with 18GB RAM (16vCPU to give 20HD ports. 16GB RAM to support the HD ports plus 2GB of RAM for 200,000 co-spaces in excess of 75,000).

- Database VM: 8vCPU with 10GB RAM (8vCPU with 8GB RAM base Database VM with 2GB addition RAM for 200,000 additional cospaces in excess of 75,000).

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.1

Supported Versions of VMware vSphere ESXi: 6.5 U2, 6.7, 7.0

Notes:

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

## Version 3.0 (with ESXi 7.0)

Supported Versions of VMware vSphere ESXi: 7.0

Notes:

- This information listed here for convenience. For latest information, when in doubt, conflict, review the Cisco Meeting Server documentation .

- For more details, see Notes for VM Configurations .

- For all other details on hardware and VMware support, refer to Cisco Collaboration Infrastructure .

- Refer to Quote Collab for modeling VM placement on a user defined hardware configuration.

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |
| MeetingApps | 8 |  | 16 GB | 1 x 100GB |  |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |
| MeetingApps | 8 |  | 16 GB | 1 x 100GB |  |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |
| MeetingApps | 8 |  | 16 GB | 1 x 100GB |  |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |
| MeetingApps | 8 |  | 16 GB | 1 x 100GB |  |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |
| MeetingApps | 8 |  | 16 GB | 1 x 100GB |  |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |

| Component & Capacity Point | VM Configuration Requirements click to download OVA file for this version |
|---|---|
| vCPU | Physical CPU Base Frequency | vRAM | vDisk | vNIC |
| Callbridge VM or Combined VM (Edge + Callbridge + DB + Scheduler) | 4 + (1 vCPU per 1.25 HD ports) | Min: 2.0GHz; Recommended: 2.5GHz | 1GB per vCPU (*See Notes) | 1 x 100GB | 1 |
| Small Edge VM | 4 | 2.5 GHz recommended | 4 GB | 1 x 100GB | 1 |
| Large Edge VM | 16 | 2.5 GHz recommended | 8 GB | 1 x 100GB | 10 Gbps |
| Database VM | 8 | Min: 2.0GHz; Recommended: 2.5GHz | 8 GB | 1 x 100GB | 1 |
| Recording VM | Min 4 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4GB and .5GB per vCPU | 1 x 100GB | 1 |
| Streaming VM | Min 4; Max 8 | Min: 2.0GHz; Recommended: 2.5GHz | Min 4 GB; recommended 8 GB | 1 x 100GB | 1 |