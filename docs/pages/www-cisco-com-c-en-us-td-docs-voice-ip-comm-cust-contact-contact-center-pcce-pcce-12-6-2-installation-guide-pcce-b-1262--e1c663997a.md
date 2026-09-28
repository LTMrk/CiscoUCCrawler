---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-installation-guide-pcce-b-1262--e1c663997a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/installation/guide/pcce_b_1262_cisco_pcce_installationandupgrade_guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_0100.html
retrieved_at: 2026-08-21T04:50:35.673320+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: March 9, 2026

Chapter: Packaged CCE 2000 Agents Installation

## Chapter: Packaged CCE 2000 Agents Installation

# Packaged CCE 2000 Agents Installation

## Installation Tasks

This section provides tasks to create and set up virtual machines (VM) of various components that are required for the Packaged
                              CCE 2000 Agents installation. For information about creating VMs on the appropriate data centers for specific components,
                              see the Unified CCE Reference Designs section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

If your Reference Design layout is on the Cisco HX220c-M5SX or Cisco HX220c-M6S servers, auto-discovery (to identify and validate the components on ESXi servers) is based only on the first node of the
                                          Hyperflex cluster.

If you have Cisco UCS C240 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S Tested Reference Configuration or Specification-Based hardware, make sure that the following core components are added on-box
                                          without changing the default annotations:

Unified CCE Rogger

Unified CCE AW/HDS/DDS

Unified CCE PG

Unified CVP Server

Unified Intelligence Center (with coresident LiveData and IDS)

Finesse

The following terms are reserved for core component annotations: Cisco, Finesse, CUIC, and CVP. Do not use these reserved
                                          terms in the annotations of any of the non-core component VMs.

Take a backup of the VM
                                          Snapshot before installing the Packaged CCE software, because uninstallation
                                          support is not provided.

Ensure that Internet Information Services (IIS) is disabled on Windows Server before installing Unified software with the
                                          ICM-CCE installer.

The table outlines the Packaged CCE 2000 Agents installation tasks.

Component Installation Tasks

1

Create VM for Unified CCE PG

2

Create VM for Unified CCE Rogger

3

Create VM for Unified CCE AW-HDS-DDS

4

Create VMs for the Cisco Unified Customer Voice Portal Servers

5

Create VM for Cisco Unified Communications Manager Publisher

6

Create VM for Cisco Unified Communications Manager Subscriber

7

Create VM for Cisco Finesse Primary

8

Create VM for Cisco Finesse Secondary

9

Create VM for Cisco Unified Intelligence Center Publisher

10

Create VM for Cisco Unified Intelligence Center Subscriber

11

Install Cisco Virtualized Voice Browser

12

(Optional) Create VM for Cloud Connect Publisher

13

(Optional) Create VM for Cloud Connect Subscriber

14

(Optional) Create VM for Cisco Unified CVP Reporting Server

15

(Optional) Install Media Server

16

(Optional) Install Enterprise Chat and Email

17

(Optional) Install the External HDS

For the post installation configurations of each component, see Post Installation Configuration section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### Create Virtual Machines for Components

#### Create VM for Unified CCE PG

Follow this sequence of tasks to create a virtual machine for the Unified CCE PG.

Sequence

Task

1

Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA .

Select Medium PG from the drop-down list.

2

Install Microsoft Windows Server

3

Install VMware Tools

4

Configure Network Adapters

5

Add Machine to Domain

6

Install Antivirus Software

7

Set Persistent Static Routes

8

Run Windows Updates

9

Install Cisco Unified Contact Center Enterprise

#### Create VM for Unified CCE Rogger

Follow this sequence of tasks to create a virtual machine for the Unified CCE Rogger.

Sequence

Task

1

Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA .

Select Rogger from the drop-down list.

2

Install Microsoft Windows Server

3

Install VMware Tools

4

Configure Network Adapters

5

Add Machine to Domain

6

Install Antivirus Software

7

Configure Database Drive

8

Set Persistent Static Routes

9

Run Windows Updates

10

Install Microsoft SQL Server

11

Install Cisco Unified Contact Center Enterprise

#### Create VM for Unified CCE AW-HDS-DDS

Follow this sequence of tasks to create a virtual machine for the Unified CCE AW-HDS-DDS.

Sequence

Task

1

Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA .

Select AW-HDS-DDS from the drop-down list.

2

Install Microsoft Windows Server

3

Install VMware Tools

4

Configure Network Adapter for Unified CCE AW-HDS-DDS, AW-HDS, HDS-DDS

5

Add Machine to Domain

6

Install Antivirus Software

7

Configure Database Drive

8

Run Windows Updates

9

Install Microsoft SQL Server

10

Install Cisco Unified Contact Center Enterprise

11

Configure Permissions in the Local Machine

#### Create VMs for the Cisco Unified Customer Voice Portal Servers

Follow this sequence of tasks to create the virtual machines for the Unified CVP Servers. Each Unified CVP Server combines
                                 the Unified CVP Call Server, Media Server, and VXML Server functionality.

Task

Using Packaged-CCE-CVP.ova, Create a Virtual Machine from the OVA .

From the drop-down list:

Select Cisco Unified CVP Call Server-VXML Server from the drop-down list when you create the Unified CVP Server VM.

Install Microsoft Windows Server

NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization .

Install VMware Tools

Add Machine to Domain

9

Install FTP Server

#### Install Media Server

If the Media Server is external, install the following on the Media Server:

Installation Tasks

1

Setup Unified CVP Media Server IIS

2

Install FTP Server

#### Create VM for
                              	 Cisco Unified Communications Manager Publisher

Follow this sequence of tasks to create the virtual machine for the Unified Communications Manager Publisher.

For the Cisco UCS C240 M4SX Server, the Unified Communications Manager (CUCM) 12.5 and above installation must be off-box.

Task

Using Packaged-CCE-CUCM.ova. Create a Virtual Machine from the OVA .

Select CUCM 10000 user node from the drop-down list.

Configure DNS Server

Install
                                             					 the Unified Communications Manager Publisher.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

5

Configure the Cluster for Cisco Unified Communications Manager

6

Create a Unified Communications Manager AXL User Account

7

Generate and install the Unified Communications Manager License .

8

Activate Services

#### Create VM for
                              	 Cisco Unified Communications Manager Subscriber

Follow this sequence of tasks to create the virtual machine for the Cisco Unified Communications Manager Subscriber.

Task

Using Packaged-CCE-CUCM.ova, Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Unified Communications Manager Subscriber.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

5

Generate and install the Unified Communications Manager License .

6

Activate Services

#### Create VM for
                              	 Cisco Finesse Primary

Follow this sequence of steps to create a virtual machine for the Cisco Finesse Primary node.

Task

Using the Packaged-CCE-Finesse.ova, Create a Virtual Machine from the OVA .

Select 2000 HTTPS Agent from the drop-down list.

Configure DNS Server

Install
                                             					 the Cisco Finesse Primary node.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

Configure the Cluster for Cisco Finesse

#### Create VM for
                              	 Cisco Finesse Secondary

Follow this sequence of tasks to create the virtual machine for the Cisco Finesse Secondary node.

Task

Using Packaged-CCE-Finesse.ova, Create a Virtual Machine from the OVA .

Select 2000 HTTPS Agent from the drop-down list.

Configure DNS Server

Install
                                             					 the Cisco Finesse Secondary node.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for
                              	 Cisco Unified Intelligence Center Publisher

Follow this sequence of tasks to create the virtual machine for the Unified Intelligence Center Publisher. Live Data and the
                                 Cisco Identity Service are also installed on the same VM.

Task

Using Packaged-CCE-CUIC.ova, Create a Virtual Machine from the OVA .

Select Co-Resident from the drop-down list.

Configure DNS Server

Install the Cisco Unified Intelligence Center Publisher.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

Configure the Cluster for Cisco Unified Intelligence Center

#### Create VM for
                              	 Cisco Unified Intelligence Center Subscriber

Follow this sequence of tasks to create the virtual machine for the Unified Intelligence Center Subscriber. Live Data and
                                 the Cisco Identity Service are also installed on this VM.

Task

Using Packaged-CCE-CUIC.ova, Create a Virtual Machine from the OVA .

Select Co-Resident from the drop-down list.

Configure DNS Server

Install
                                             					 the Cisco Unified Intelligence Center Subscriber.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for
                              	 Cisco Unified CVP Reporting Server

Follow this sequence of tasks to create a virtual machine for the Unified CVP Reporting Server. The Unified CVP Reporting
                                 Server is an optional component.

Task

Using the Packaged-CCE-CVP.ova template, create a virtual machine. For more information, see Create a Virtual Machine from the OVA .

The CVP Reporting Server can use the CVP Call Server’s OVA template. However, the
                                                         									annotation name used should be generic. By default, the VM
                                                         									annotation is named as CVP VM template. After the VM is
                                                         									deployed, you must change the name. Do not use the terms Cisco,
                                                         									Finesse, CUIC, and CVP in the name because they are reserved for
                                                         									the core components. For example, instead of
                                                         									CVP-VM-Reporting-Server.ova, use
                                                         									SelfService-Reporting-Server.ova. If any of the core component
                                                         									names are used, the CVP Reporting Server fails the VM
                                                         									validation.

Select Cisco Unified CVP Reporting Server from the drop-down list.

Install Microsoft Windows Server

NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization .

Install VMware Tools

Add Machine to Domain

#### Create VM for Cloud Connect Publisher

Follow this sequence of tasks to create the virtual machine for the Cloud Connect Publisher.

Task

Using Packaged-CCE-cloudconnect.ova, Create a Virtual Machine from the OVA .

Install the Cloud Connect Publisher.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

#### Create VM for Cloud Connect Subscriber

Follow this sequence of tasks to create the virtual machine for the Cloud Connect Subscriber.

Task

Using Packaged-CCE-cloudconnect.ova, Create a Virtual Machine from the OVA .

2

Set Cloud Connect Secondary Node.

See Set Cloud Connect Secondary Node .

Install the Cloud Connect Subscriber.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

### Customers Also Viewed

- Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2) --- Reference

| Note | If your Reference Design layout is on the Cisco HX220c-M5SX or Cisco HX220c-M6S servers, auto-discovery (to identify and validate the components on ESXi servers) is based only on the first node of the
                                          Hyperflex cluster. |
|---|---|

| Note | If you have Cisco UCS C240 M5SX or Cisco UCS C240 M6SX or Cisco HX220c-M5SX or Cisco HX220c-M6S Tested Reference Configuration or Specification-Based hardware, make sure that the following core components are added on-box
                                          without changing the default annotations: Unified CCE Rogger Unified CCE AW/HDS/DDS Unified CCE PG Unified CVP Server Unified Intelligence Center (with coresident LiveData and IDS) Finesse The following terms are reserved for core component annotations: Cisco, Finesse, CUIC, and CVP. Do not use these reserved
                                          terms in the annotations of any of the non-core component VMs. |
|---|---|

| Note | Take a backup of the VM
                                          Snapshot before installing the Packaged CCE software, because uninstallation
                                          support is not provided. |
|---|---|

| Note | Ensure that Internet Information Services (IIS) is disabled on Windows Server before installing Unified software with the
                                          ICM-CCE installer. |
|---|---|

| Component Installation Tasks |
|---|
| 1 | Create VM for Unified CCE PG |
| 2 | Create VM for Unified CCE Rogger |
| 3 | Create VM for Unified CCE AW-HDS-DDS |
| 4 | Create VMs for the Cisco Unified Customer Voice Portal Servers |
| 5 | Create VM for Cisco Unified Communications Manager Publisher |
| 6 | Create VM for Cisco Unified Communications Manager Subscriber |
| 7 | Create VM for Cisco Finesse Primary |
| 8 | Create VM for Cisco Finesse Secondary |
| 9 | Create VM for Cisco Unified Intelligence Center Publisher |
| 10 | Create VM for Cisco Unified Intelligence Center Subscriber |
| 11 | Install Cisco Virtualized Voice Browser |
| 12 | (Optional) Create VM for Cloud Connect Publisher |
| 13 | (Optional) Create VM for Cloud Connect Subscriber |
| 14 | (Optional) Create VM for Cisco Unified CVP Reporting Server |
| 15 | (Optional) Install Media Server |
| 16 | (Optional) Install Enterprise Chat and Email |
| 17 | (Optional) Install the External HDS |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA . Select Medium PG from the drop-down list. |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Set Persistent Static Routes |
| 8 | Run Windows Updates |
| 9 | Install Cisco Unified Contact Center Enterprise |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA . Select Rogger from the drop-down list. |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Configure Database Drive |
| 8 | Set Persistent Static Routes |
| 9 | Run Windows Updates |
| 10 | Install Microsoft SQL Server |
| 11 | Install Cisco Unified Contact Center Enterprise |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-UCCE.ova, Create a Virtual Machine from the OVA . Select AW-HDS-DDS from the drop-down list. |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapter for Unified CCE AW-HDS-DDS, AW-HDS, HDS-DDS |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Configure Database Drive |
| 8 | Run Windows Updates |
| 9 | Install Microsoft SQL Server |
| 10 | Install Cisco Unified Contact Center Enterprise |
| 11 | Configure Permissions in the Local Machine |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-CVP.ova, Create a Virtual Machine from the OVA . From the drop-down list: Select Cisco Unified CVP Call Server-VXML Server from the drop-down list when you create the Unified CVP Server VM. |
| 2 | Install Microsoft Windows Server NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization . |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters for Cisco Unified CVP |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Run Windows Updates |
| 8 | Install Cisco Unified CVP Server |
| 9 | Install FTP Server |

| Sequence | Installation Tasks |
|---|---|
| 1 | Setup Unified CVP Media Server IIS |
| 2 | Install FTP Server |

| Note | For the Cisco UCS C240 M4SX Server, the Unified Communications Manager (CUCM) 12.5 and above installation must be off-box. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-CUCM.ova. Create a Virtual Machine from the OVA . Select CUCM 10000 user node from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install
                                             					 the Unified Communications Manager Publisher. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Unified Communications Manager |
| 6 | Create a Unified Communications Manager AXL User Account |
| 7 | Generate and install the Unified Communications Manager License . |
| 8 | Activate Services |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-CUCM.ova, Create a Virtual Machine from the OVA . Select CUCM 7500 user node from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install the Unified Communications Manager Subscriber. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Generate and install the Unified Communications Manager License . |
| 6 | Activate Services |

| Sequence | Task |
|---|---|
| 1 | Using the Packaged-CCE-Finesse.ova, Create a Virtual Machine from the OVA . Select 2000 HTTPS Agent from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install
                                             					 the Cisco Finesse Primary node. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Finesse |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-Finesse.ova, Create a Virtual Machine from the OVA . Select 2000 HTTPS Agent from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install
                                             					 the Cisco Finesse Secondary node. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-CUIC.ova, Create a Virtual Machine from the OVA . Select Co-Resident from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Unified Intelligence Center Publisher. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Unified Intelligence Center |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-CUIC.ova, Create a Virtual Machine from the OVA . Select Co-Resident from the drop-down list. |
| 2 | Configure DNS Server |
| 3 | Install
                                             					 the Cisco Unified Intelligence Center Subscriber. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Using the Packaged-CCE-CVP.ova template, create a virtual machine. For more information, see Create a Virtual Machine from the OVA . Note The CVP Reporting Server can use the CVP Call Server’s OVA template. However, the
                                                         									annotation name used should be generic. By default, the VM
                                                         									annotation is named as CVP VM template. After the VM is
                                                         									deployed, you must change the name. Do not use the terms Cisco,
                                                         									Finesse, CUIC, and CVP in the name because they are reserved for
                                                         									the core components. For example, instead of
                                                         									CVP-VM-Reporting-Server.ova, use
                                                         									SelfService-Reporting-Server.ova. If any of the core component
                                                         									names are used, the CVP Reporting Server fails the VM
                                                         									validation. Select Cisco Unified CVP Reporting Server from the drop-down list. | Note | The CVP Reporting Server can use the CVP Call Server’s OVA template. However, the
                                                         									annotation name used should be generic. By default, the VM
                                                         									annotation is named as CVP VM template. After the VM is
                                                         									deployed, you must change the name. Do not use the terms Cisco,
                                                         									Finesse, CUIC, and CVP in the name because they are reserved for
                                                         									the core components. For example, instead of
                                                         									CVP-VM-Reporting-Server.ova, use
                                                         									SelfService-Reporting-Server.ova. If any of the core component
                                                         									names are used, the CVP Reporting Server fails the VM
                                                         									validation. |
| Note | The CVP Reporting Server can use the CVP Call Server’s OVA template. However, the
                                                         									annotation name used should be generic. By default, the VM
                                                         									annotation is named as CVP VM template. After the VM is
                                                         									deployed, you must change the name. Do not use the terms Cisco,
                                                         									Finesse, CUIC, and CVP in the name because they are reserved for
                                                         									the core components. For example, instead of
                                                         									CVP-VM-Reporting-Server.ova, use
                                                         									SelfService-Reporting-Server.ova. If any of the core component
                                                         									names are used, the CVP Reporting Server fails the VM
                                                         									validation. |
| 2 | Install Microsoft Windows Server NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization . |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters for Cisco Unified CVP |
| 5 | Install Antivirus Software |
| 6 | Configure Database Drive |
| 7 | Run Windows Updates |
| 8 | Install Cisco Unified CVP Reporting Server |
| 9 | Add Machine to Domain |

| Note | The CVP Reporting Server can use the CVP Call Server’s OVA template. However, the
                                                         									annotation name used should be generic. By default, the VM
                                                         									annotation is named as CVP VM template. After the VM is
                                                         									deployed, you must change the name. Do not use the terms Cisco,
                                                         									Finesse, CUIC, and CVP in the name because they are reserved for
                                                         									the core components. For example, instead of
                                                         									CVP-VM-Reporting-Server.ova, use
                                                         									SelfService-Reporting-Server.ova. If any of the core component
                                                         									names are used, the CVP Reporting Server fails the VM
                                                         									validation. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-cloudconnect.ova, Create a Virtual Machine from the OVA . |
| 2 | Install the Cloud Connect Publisher. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |

| Sequence | Task |
|---|---|
| 1 | Using Packaged-CCE-cloudconnect.ova, Create a Virtual Machine from the OVA . |
| 2 | Set Cloud Connect Secondary Node. See Set Cloud Connect Secondary Node . |
| 3 | Install the Cloud Connect Subscriber. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |