---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-b660f6f420
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_b_cisco-pcce-installationandupgrade-guide-12_5_chapter_00110.html
retrieved_at: 2026-08-21T16:39:09.192210+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: April 3, 2021

Chapter: Packaged CCE 12000 Agents Installation

## Chapter: Packaged CCE 12000 Agents Installation

# Packaged CCE 12000 Agents Installation

## Installation Tasks

This section provides the sequence to create and set up virtual machines of various components
                           that are required for the Packaged CCE 12000 Agents fresh installation. For information
                           about creating VMs on the appropriate data centers for specific components, see Unified CCE Reference Designs section in the Solution Design Guide for
                              Cisco Unified Contact Center Enterprise , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/design/guide/pcce_b_soldg-for-packaged-cce-12_5/pcce_b_soldg-for-packaged-cce-12_5_chapter_01.html .

The table outlines the Packaged CCE 12000 Agents fresh installation tasks.

Component Installation Tasks

1

Create VM for Unified CCE PG

2

Create VM for Unified CCE Logger

3

Create VM for Unified CCE Router

4

Create VM for Unified CCE AW-HDS

5

Create VM for Unified CCE HDS-DDS

6

Create VMs for the Cisco Unified Customer Voice Portal Servers

7

Create VM for Cisco Unified Communications Manager Publisher

8

Create VM for Cisco Unified Communications Manager Subscriber

9

Create VMs for Cisco Finesse Primary Nodes

10

Create VMs for Cisco Finesse Secondary Nodes

11

Create VM for Cisco Unified Intelligence Center Publisher

12

Create VM for Cisco Unified Intelligence Center Subscriber

13

Create VM for Live Data Primary Node

14

Create VM for Live Data Secondary Node

15

Create VM for Cisco Identity Service Publisher

16

Create VM for Cisco Identity Service Subscriber

17

Install Cisco Virtualized Voice Browser

18

(Optional) Create VM for Cisco Unified CVP Reporting Server

19

(Optional) Install Media Server

20

(Optional) Install Enterprise Chat and Email

21

(Optional) Install the External HDS

For the post installation configurations of each component, see Post Installation
                              Configuration section in the Cisco Packaged Contact Center Enterprise
                              Administration and Configuration Guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_01.html .

### Create Virtual Machines for Components

#### Create VM for Unified CCE Logger

Follow this sequence of tasks to create a virtual machine for the Unified CCE Logger.

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

Run Windows Updates

9

Install Microsoft SQL Server

10

Install Cisco Unified Contact Center Enterprise

#### Create VM for Unified CCE Router

Follow this sequence of tasks to create a virtual machine for the Unified CCE Router.

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

Run Windows Updates

8

Install Cisco Unified Contact Center Enterprise

#### Create VM for Unified CCE AW-HDS

Follow this sequence of tasks to create a virtual machine for the Unified CCE AW-HDS.

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

#### Create VM for Unified CCE HDS-DDS

Follow this sequence of tasks to create a virtual machine for the Unified CCE HDS-DDS.

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

| Component Installation Tasks |
|---|
| 1 | Create VM for Unified CCE PG |
| 2 | Create VM for Unified CCE Logger |
| 3 | Create VM for Unified CCE Router |
| 4 | Create VM for Unified CCE AW-HDS |
| 5 | Create VM for Unified CCE HDS-DDS |
| 6 | Create VMs for the Cisco Unified Customer Voice Portal Servers |
| 7 | Create VM for Cisco Unified Communications Manager Publisher |
| 8 | Create VM for Cisco Unified Communications Manager Subscriber |
| 9 | Create VMs for Cisco Finesse Primary Nodes |
| 10 | Create VMs for Cisco Finesse Secondary Nodes |
| 11 | Create VM for Cisco Unified Intelligence Center Publisher |
| 12 | Create VM for Cisco Unified Intelligence Center Subscriber |
| 13 | Create VM for Live Data Primary Node |
| 14 | Create VM for Live Data Secondary Node |
| 15 | Create VM for Cisco Identity Service Publisher |
| 16 | Create VM for Cisco Identity Service Subscriber |
| 17 | Install Cisco Virtualized Voice Browser |
| 18 | (Optional) Create VM for Cisco Unified CVP Reporting Server |
| 19 | (Optional) Install Media Server |
| 20 | (Optional) Install Enterprise Chat and Email |
| 21 | (Optional) Install the External HDS |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Configure Database Drive |
| 8 | Run Windows Updates |
| 9 | Install Microsoft SQL Server |
| 10 | Install Cisco Unified Contact Center Enterprise |

| Sequence | Task |
|---|---|
| 1 | Create a Virtual Machine from the OVA . |
| 2 | Install Microsoft Windows Server |
| 3 | Install VMware Tools |
| 4 | Configure Network Adapters |
| 5 | Add Machine to Domain |
| 6 | Install Antivirus Software |
| 7 | Run Windows Updates |
| 8 | Install Cisco Unified Contact Center Enterprise |

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