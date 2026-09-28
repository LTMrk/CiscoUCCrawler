---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-installation-guide-pcce-b-cisco-aa52a4f1de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/installation/guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_6_1/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_0101.html
retrieved_at: 2026-08-21T16:40:06.442893+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Packaged CCE 4000 Agents Installation

## Chapter: Packaged CCE 4000 Agents Installation

# Packaged CCE 4000 Agents Installation

## Installation Tasks

This section provides the sequence to create and set up virtual machines of various components
                           that are required for the Packaged CCE 4000 Agents fresh installation. For information
                           about creating VMs on the appropriate data centers for specific components, see Unified CCE Reference Designs section in the Solution Design Guide for
                              Cisco Unified Contact Center Enterprise , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/design/guide/pcce_b_soldg-for-packaged-cce-12_5/pcce_b_soldg-for-packaged-cce-12_5_chapter_01.html .

The table outlines the Packaged CCE 4000 Agents fresh installation tasks.

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

Create VMs for Cisco Finesse Primary Nodes

8

Create VMs for Cisco Finesse Secondary Nodes

9

Create VM for Cisco Unified Intelligence Center Publisher

10

Create VM for Cisco Unified Intelligence Center Subscriber

11

Create VM for Live Data Primary Node

12

Create VM for Live Data Secondary Node

13

Create VM for Cisco Identity Service Publisher

14

Create VM for Cisco Identity Service Subscriber

15

Install Cisco Virtualized Voice Browser

16

(Optional) Create VM for Cisco Unified CVP Reporting Server

17

(Optional) Install Media Server

18

(Optional) Install Enterprise Chat and Email

19

(Optional) Install the External HDS

For the post installation configurations of each component, see Post Installation
                              Configuration section in the Cisco Packaged Contact Center Enterprise
                              Administration and Configuration Guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_01.html .

### Create Virtual Machines for Components

#### Create VM for Unified CCE PG

Follow this sequence of tasks to create a virtual machine for the Unified CCE PG.

Sequence

Task

1

Create a Virtual Machine from the OVA .

2

Install Microsoft Windows Server

3

Install VMware Tools

4

Configure Network Adapters

6

Add Machine to Domain

7

Install Antivirus Software

8

Set Persistent Static Routes

9

Run Windows Updates

10

Install Cisco Unified Contact Center Enterprise

#### Create VM for Unified CCE Rogger

Follow this sequence of tasks to create a virtual machine for the Unified CCE Rogger.

Sequence

Task

1

Create a Virtual Machine from the OVA .

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

Create a Virtual Machine from the OVA .

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

Create a Virtual Machine from the OVA .

Install Microsoft Windows Server

NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization .

Install VMware Tools

Add Machine to Domain

9

Install FTP Server

#### Create VM for Cisco Unified CVP Reporting Server

Follow this sequence of tasks to create a virtual machine for the Unified CVP Reporting Server.

Task

Create a Virtual Machine from the OVA .

The CVP Reporting Server can use the CVP Call Server’s OVA
                                                            template. However, the annotation name used should be
                                                            generic. By default, the VM annotation is named as CVP VM
                                                            template. After the VM is deployed, you must change the
                                                            name. Do not use the terms Cisco, Finesse, CUIC, and CVP in
                                                            the name because they are reserved for the core components.
                                                            For example, instead of CVP-VM-Reporting-Server.ova, use
                                                            SelfService-Reporting-Server.ova. If any of the core
                                                            component names are used, the CVP Reporting Server fails the
                                                            VM validation.

Install Microsoft Windows Server

NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization .

Install VMware Tools

Add Machine to Domain

#### Create VM for Cisco Unified Communications Manager Publisher

Follow this sequence of tasks to create the virtual machine for the Unified Communications Manager Publisher.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Unified Communications Manager Publisher.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

Configure the Cluster for Cisco Unified Communications Manager

Create a Unified Communications Manager AXL User Account

7

Generate and install the Unified Communications Manager License .

8

Activate Services

#### Create VM for Cisco Unified Communications Manager Subscriber

Follow this sequence of tasks to create the virtual machine for the Cisco Unified Communications Manager Subscriber.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Unified Communications Manager Subscriber.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

5

Generate and install the Unified Communications Manager License .

6

Activate Services

#### Create VMs for Cisco Finesse Primary Nodes

Follow this sequence of steps to create a virtual machine for each of the Cisco Finesse Primary nodes.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Finesse Primary node.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

Configure the Cluster for Cisco Finesse

#### Create VMs for Cisco Finesse Secondary Nodes

Follow this sequence of tasks to create the virtual machine for each of the Cisco Finesse Secondary nodes.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Finesse Secondary node.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for Cisco Unified Intelligence Center Publisher

Follow this sequence of tasks to create the virtual machine for the Unified Intelligence Center Publisher.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Unified Intelligence Center Publisher.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

Configure the Cluster for Cisco Unified Intelligence Center

#### Create VM for Cisco Unified Intelligence Center Subscriber

Follow this sequence of tasks to create the virtual machine for the Unified Intelligence Center Subscriber nodes.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Unified Intelligence Center Subscriber.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for Live Data Primary Node

Follow this sequence of steps to create a virtual machine for the Cisco Live Data Primary node.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Live Data Primary node.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for Live Data Secondary Node

Follow this sequence of steps to create a virtual machine for the Cisco Live Data Secondary node.

Task

Create a Virtual Machine from the OVA .

Select Small Live Data Server from the drop-down list for 4000 Agents deployment.

Select Larger Live Data Server from the drop-down list for 12000 Agents deployment.

Configure DNS Server

Install the Cisco Live Data Secondary node.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

4

Set Live Data Secondary Node

Install VMware Tools

#### Create VM for Cisco Identity Service Publisher

Follow this sequence of steps to create a virtual machine for the Cisco Identity Service Publisher node.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Identity Service Publisher node.

See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications .

Install VMware Tools

#### Create VM for Cisco Identity Service Subscriber

Follow this sequence of steps to create a virtual machine for the Cisco Identity Service Subscriber node.

Task

Create a Virtual Machine from the OVA .

Configure DNS Server

Install the Cisco Identity Service Subscriber node.

See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications .

4

Set IdS Subscriber Node

Install VMware Tools

| Component Installation Tasks |
|---|
| 1 | Create VM for Unified CCE PG |
| 2 | Create VM for Unified CCE Rogger |
| 3 | Create VM for Unified CCE AW-HDS-DDS |
| 4 | Create VMs for the Cisco Unified Customer Voice Portal Servers |
| 5 | Create VM for Cisco Unified Communications Manager Publisher |
| 6 | Create VM for Cisco Unified Communications Manager Subscriber |
| 7 | Create VMs for Cisco Finesse Primary Nodes |
| 8 | Create VMs for Cisco Finesse Secondary Nodes |
| 9 | Create VM for Cisco Unified Intelligence Center Publisher |
| 10 | Create VM for Cisco Unified Intelligence Center Subscriber |
| 11 | Create VM for Live Data Primary Node |
| 12 | Create VM for Live Data Secondary Node |
| 13 | Create VM for Cisco Identity Service Publisher |
| 14 | Create VM for Cisco Identity Service Subscriber |
| 15 | Install Cisco Virtualized Voice Browser |
| 16 | (Optional) Create VM for Cisco Unified CVP Reporting Server |
| 17 | (Optional) Install Media Server |
| 18 | (Optional) Install Enterprise Chat and Email |
| 19 | (Optional) Install the External HDS |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters |
| 6 | Add Machine to Domain |
| 7 | Install Antivirus Software |
| 8 | Set Persistent Static Routes |
| 9 | Run Windows Updates |
| 10 | Install Cisco Unified Contact Center Enterprise |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
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
| 1 | Create a Virtual Machine from the OVA . |
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
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Install Microsoft Windows Server NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization . |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters for Cisco Unified CVP |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Run Windows Updates |
| 8 | Install Cisco Unified CVP Server |
| 9 | Install FTP Server |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . Note The CVP Reporting Server can use the CVP Call Server’s OVA
                                                            template. However, the annotation name used should be
                                                            generic. By default, the VM annotation is named as CVP VM
                                                            template. After the VM is deployed, you must change the
                                                            name. Do not use the terms Cisco, Finesse, CUIC, and CVP in
                                                            the name because they are reserved for the core components.
                                                            For example, instead of CVP-VM-Reporting-Server.ova, use
                                                            SelfService-Reporting-Server.ova. If any of the core
                                                            component names are used, the CVP Reporting Server fails the
                                                            VM validation. | Note | The CVP Reporting Server can use the CVP Call Server’s OVA
                                                            template. However, the annotation name used should be
                                                            generic. By default, the VM annotation is named as CVP VM
                                                            template. After the VM is deployed, you must change the
                                                            name. Do not use the terms Cisco, Finesse, CUIC, and CVP in
                                                            the name because they are reserved for the core components.
                                                            For example, instead of CVP-VM-Reporting-Server.ova, use
                                                            SelfService-Reporting-Server.ova. If any of the core
                                                            component names are used, the CVP Reporting Server fails the
                                                            VM validation. |
| Note | The CVP Reporting Server can use the CVP Call Server’s OVA
                                                            template. However, the annotation name used should be
                                                            generic. By default, the VM annotation is named as CVP VM
                                                            template. After the VM is deployed, you must change the
                                                            name. Do not use the terms Cisco, Finesse, CUIC, and CVP in
                                                            the name because they are reserved for the core components.
                                                            For example, instead of CVP-VM-Reporting-Server.ova, use
                                                            SelfService-Reporting-Server.ova. If any of the core
                                                            component names are used, the CVP Reporting Server fails the
                                                            VM validation. |
| 2 | Install Microsoft Windows Server NTP configuration is required if this machine is not in the same domain as the Unified CCE Roggers, AWs, and PGs. See NTP and Time Synchronization . |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters for Cisco Unified CVP |
| 5 | Install Antivirus Software |
| 6 | Configure Database Drive |
| 7 | Run Windows Updates |
| 8 | Install Cisco Unified CVP Reporting Server |
| 9 | Add Machine to Domain |

| Note | The CVP Reporting Server can use the CVP Call Server’s OVA
                                                            template. However, the annotation name used should be
                                                            generic. By default, the VM annotation is named as CVP VM
                                                            template. After the VM is deployed, you must change the
                                                            name. Do not use the terms Cisco, Finesse, CUIC, and CVP in
                                                            the name because they are reserved for the core components.
                                                            For example, instead of CVP-VM-Reporting-Server.ova, use
                                                            SelfService-Reporting-Server.ova. If any of the core
                                                            component names are used, the CVP Reporting Server fails the
                                                            VM validation. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Unified Communications Manager Publisher. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Unified Communications Manager |
| 6 | Create a Unified Communications Manager AXL User Account |
| 7 | Generate and install the Unified Communications Manager License . |
| 8 | Activate Services |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Unified Communications Manager Subscriber. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Generate and install the Unified Communications Manager License . |
| 6 | Activate Services |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Finesse Primary node. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Finesse |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Finesse Secondary node. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Unified Intelligence Center Publisher. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |
| 5 | Configure the Cluster for Cisco Unified Intelligence Center |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Unified Intelligence Center Subscriber. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Live Data Primary node. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . Select Small Live Data Server from the drop-down list for 4000 Agents deployment. Select Larger Live Data Server from the drop-down list for 12000 Agents deployment. |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Live Data Secondary node. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Set Live Data Secondary Node |
| 5 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Identity Service Publisher node. See Install Publishers/Primary Nodes of VOS-Based Contact Center Applications . |
| 4 | Install VMware Tools |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Configure DNS Server |
| 3 | Install the Cisco Identity Service Subscriber node. See Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications . |
| 4 | Set IdS Subscriber Node |
| 5 | Install VMware Tools |