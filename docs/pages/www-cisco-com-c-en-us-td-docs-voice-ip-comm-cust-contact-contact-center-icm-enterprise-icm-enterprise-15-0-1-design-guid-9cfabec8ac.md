---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-design-guid-9cfabec8ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/design/guide/ucce_b_ucce_soldg-for-unified-cce-1501/rcct_m_unified-cce-reference-designs_15_0.html
retrieved_at: 2026-08-16T19:49:51.796246+00:00
---

Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Solution Design Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: March 15, 2025

Chapter: Unified CCE Reference Designs

## Chapter: Unified CCE Reference Designs

# Unified CCE Reference Designs

## Introduction to the Reference Designs

The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions:

Packaged Contact Center Enterprise

Unified Contact Center Enterprise

The Contact Center Enterprise
                                 						Reference Designs are a set of Cisco validated designs of our contact center enterprise solutions. The Reference Designs define the technologies
                           and topologies that fit the needs for most deployments. The Reference Designs focus on simplifying the contact center enterprise
                           solution design. They provide complete contact center functionality based on components that are strategic to Cisco.

We have defined the Reference Designs in the following table to cover most contact center needs:

Reference Design

Packaged CCE

Unified CCE

2000 Agents

Yes

Yes

4000 Agents

Yes

Yes

12000 Agents

Yes

Yes

24000 Agents

No

Yes

36000 Agents

No

Yes

48000 Agents

No

Yes

Contact Director

No

Yes

Non-Reference Designs

ICM-to-ICM Gateway

Yes

If your solution exceeds the configuration limits for a particular Reference Design, use a Reference Design with higher limits.
                           For example, if your 2000-agent deployment requires 350 active reporting users, use the 4000 Agent Reference Design for your
                           solution.

Contact center solutions that include something not covered by the Contact Center Enterprise
                                 						Reference Designs are called Non-Reference Designs .

You require Unified CCE for any other Non-Reference Design deployments.

### Reference Designs and Deployment Types

The Contact Center Enterprise
                                       						Reference Designs are mapped to specific contact center solutions through deployment types. Deployment types are system codes that impose system
                                 limits and apply congestion control.

This table maps the Reference Designs and Non-Reference Designs with the deployment type that you use for each.

Reference Design

Packaged CCE

Unified CCE

Label

Label

2000 Agent

Packaged CCE: 2000 Agents

UCCE: 2000 Agents

4000 Agent

Packaged CCE: 4000 Agents

UCCE: 4000 Agents

12000 Agent

Packaged CCE: 12000 Agents

UCCE: 12000 Agents

24000 Agent

NA

UCCE: 24000 Agents Router/Logger

36000 Agent

NA

UCCE: 36000 Agents Router/Logger

48000 Agent

NA

UCCE: 48000 Agents Router/Logger

Contact Director

NA

Contact Director

Non-Reference Designs

ICM-to-ICM Gateway

Packaged CCE: 4000 Agents

Packaged CCE: 12000 Agents

ICM Rogger

ICM Router/Logger

Lab Only Designs

Packaged CCE: Lab Mode

UCCE: Progger (Lab Only)

## Benefits of a Reference Design
                        Solution

Contact centers offer more possibilities with
                           each new generation of software and hardware. New technology can make previously
                           preferred methods obsolete for current contact centers. We created the Contact Center Enterprise
                                 						Reference Designs to simplify your design choices and speed the
                           development of your contact center. We expect that most new contact centers can use the
                           Reference Designs to meet their needs.

By following the Reference Designs, you can:

Guide your customers' expectations by presenting clear options.

Streamline your design process with standard models.

Avoid using components and features that are near the end of their lifecycle.

Find powerful and efficient replacements for obsolete features.

Align your designs with Cisco's vision of our
                                 future contact center developments.

Enjoy quicker and easier  approval processes.

## Specifications for a Reference Design Solution

The Reference Designs define our vision of the functionality that most contact centers use. The Reference Designs consist
                           of:

Core components —Components that make up every contact center:

Ingress, Egress

Unified Customer Voice Portal (Unified CVP)

Unified Contact Center Enterprise (Unified CCE)

Cisco Virtualized Voice Browser (VVB)

Unified Communications Manager (Unified CM)

Cisco Finesse

Cisco Unified Intelligence Center

Optional Cisco components —Components that add functionality that not every contact center needs.

Customer Collaboration Platform

Cisco Contact Center SIP Proxy

Enterprise Chat and
                                             						Email

Cisco IdS

Cloud Connect

Custom Remote Server

Optional third-party components —Third-party components that you can add to provide other features.

Load balancers

Recording

Speech servers - ASR/TTS

Wallboards

Workforce management

Integrated features —These features do not require you to add an optional solution component to enable them. But, these features can require configuration
                                 in multiple solution components to activate them. They can affect your solution sizing and might have specific design considerations.

Call flows —Standard contact handling and routing methods.

Inbound Calls:

New calls from a carrier

New internal calls

Supplementary services

Hold and resume

Transfers and conferences

Refer transfers

Network transfers

Requery and survivability

Topologies —Standard layouts for your contact center components:

Centralized

Distributed

Global

This figure shows the high-level services that are part of the solutions and the components that provide those services. It
                           also highlights some features and components that are outside of the Reference Designs:

This figure highlights only a few Non-Reference Design components and topologies. The Non-Reference Design sections expand
                                       on this list.

In general, you cannot use the ICM-to-ICM Gateway in Reference Designs. Only the Contact Director Reference Design allows
                                       you to use that gateway.

This figure encapsulates the basic requirements of a Reference Design-compliant deployment:

## Contact Center Enterprise Reference Designs

The following sections describe the Contact Center Enterprise
                                 						Reference Designs .

The Reference
                                 						Designs are supported for Cisco UCS C240 M5SX and Cisco UCS C240 M6SX Tested Reference Configuration (TRC) servers. For more details,
                           see the Cisco Collaboration Virtualization page for your solution at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

The following notes apply to all the Reference Designs:

Cisco UCS C240 M7 and Cisco UCS C240 M8 rack servers are supported in accordance with spec-based policies only.

For details on the Cisco UCS C240 M7 Rack Server, see the documentation at https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c240-m7-rack-server-ds.html

For details on the Cisco UCS C240 M8 Rack Server, see the documentation at https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-c240-m8-rack-server-ds.html

Contact Center Enterprise solutions use vCPU oversubscription.

The Reference Design layouts in this section do not show off-box components like Customer Collaboration Platform

The standard PG VM includes an Agent (Unified CM) PG, a VRU PG, and an MR PG. Unified CCE allow you to add more PGs and their
                                 peripherals onto this base layout.

On the Cisco UCS C240 M5SX or Cisco UCS C240 M6SX servers, Cloud Connect must be off-box.

Cloud Connect requires only 146 GB of disk space if the CCE Orchestration feature is not used.

CVP Reporting server and Cloud Connect are optional components.

VVB VMs are shown in the reference designs solely for completeness. They may be deployed anywhere that meets customer business
                                 needs, provided TRC specifications and specification-based provisioning policies are not violated.

The TRC layouts for Cisco UCS C240 M5SX and Cisco UCS C240 M6SX servers are identical. Note that only a single-socket 28-core
                                 CPU is used for the Cisco UCS C240 M6SX servers. If customers wish to use the additional socket on the Cisco UCS C240 M6SX
                                 servers with corresponding increase in cores, memory, and disks, the hardware will be supported under spec-based VM provisioning
                                 policies.

VVB with AppD enabled on Small OVA shows a warning "Memory Usage is too high" on AppD due to the upfront allocation of memory
                                 for the services. This has no impact on VVB services.

For information on the data source allocation of the components in the Reference Design layouts, see the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

### Virtual Machines Resource Provisioning Policy

The previously used Oversubscription policy is a part of the Virtual Machine (VM) Resource Provisioning Policy.

The Unified CCE Reference Designs support the virtual machine vCPU oversubscription of the physical CPU cores on a server.
                                 For the purposes of oversubscription, the hyper-thread cores do not count as physical cores. Whether or not you use oversubscription,
                                 use the VM Resource Provisioning policy. This policy limits the total available CPU MHz and the memory of a server that the
                                 host-resident VMs can consume.

Apply the VM Resource Provisioning policy when:

You change the documented Reference Design VM layout by adding or replacing VMs. This means that you use a custom or non-Reference
                                       VM layout in a Reference Design solution.

You provision a non-Reference Design server.

You provision a Reference Design server for optional and third-party components that are not given a reference VM layout.

You use UCS or third-party specifications-based servers.

You upgrade an existing solution and do not migrate to a Reference Design VM layout.

Apply the VM Resource Provisioning policy on a per-server basis. This policy does not apply to the Reference Design VM layouts.
                                             Your solution can contain servers that use the Reference Design VM layouts and other VM layouts that use the VM Resource Provisioning
                                             policy rules.

The application of the VM Resource Provisioning policy requires meeting the following conditions:

You can use up
                                       				to two vCPUs for every physical core on each server.

You can use up
                                       				to 65% of the total available CPU MHz on each server.

You can use up
                                       				to 80% of the total available memory on each server.

For more information on virtualization and specification-based server policies, see the Cisco Collaboration Virtualization at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

The Virtual Machine Placement Tool does not currently allow you to oversubscribe. This limitation is only an issue with the
                                             tool. You can oversubscribe within the limits that are provided here.

The custom remote server should have the same provisioning specification as Unified CVP server.

### 2000 Agent Reference Designs

All contact center enterprise solutions support the 2000 Agent Reference design on the Cisco UCS C240 M5SX or Cisco UCS C240 M6SX .

In this Reference Design, Cisco Unified Intelligence Center, Live Data, Identity Service for Single Sign-On are coresident
                                       on a single VM. In the larger Reference Designs, they reside in separate VMs.

You can optionally deploy the Unified Communications Manager Publisher and Subscribers on separate servers, instead of deploying
                                       them as shown in the 2000 Agent Reference Design layout. You should dedicate two of the subscribers to Unified CCE. All devices
                                       on these subscribers must be SIP.

In 2000 Agent Reference Designs, a coresident Unified CM can support a maximum of 2000 phones. This includes your phones for
                                       all types of agents, whether contact center agents or back-office workers. If your solution requires more than 2000 phones,
                                       use a Unified CM on a separate server instead.

In the global deployment topology, each remote site can have its own Unified CM cluster. A remote site cannot include a Cisco Unified Intelligence Center server.

You can deploy optional AW-HDS-DDS per site on external servers for longer data retention.

In 2000 Agent Reference Designs, you can deploy ECE Data Server on-box for up to 400 agents. Deploy ECE off-box for up to 1500 agents.

You can also deploy the ECE Data Server on a separate server.

Deploy the ECE Web Server on an external server. You can place that server either in the same data center as the ECE Data
                                       Server or in a DMZ if customer chat interactions require that.

Adding more disks is not permitted in the CCE 2000 agent deployment. Any changes to the number of disks will result in a VM
                                             validation error.

#### Support on the Cisco UCS C240 M5SX and Cisco UCS C240 M6SX Large TRC Servers

The following figure shows the base layout of the components in a 2000 Agent Reference Design on Cisco UCS C240 M5SX and Cisco
                                 UCS C240 M6SX Large TRC servers.

This table lists the specifications for VMs.

VM

vCPU

MHz

vRAM

vDisk 1

vDisk 2

vDisk 3

Rogger

4

5000

6

150

150

Unified CM

4

7200

14

110

Unified CVP OAMP

2

400

4

150

Unified CVP Server

4

3000

12

250

Unified CVP Reporting Server

4

1800

6

80

438

4

4000

20

80

50

300

CUIC-LD-IdS

4

5500

24

200

AW-HDS-DDS

4

5000

16

150

500

PG

2

4000

6

150

Finesse

4

5000

16

146

VVB

4

9000

10

146

Server

vCPU

MHz

vRAM

vDisk

Data Center Site A

36

46300

132

2496

Data Center Site B

34

40500

120

2754

Server 2

16

36000

40

584

### 4000 Agent Reference Designs

All contact center enterprise solutions support the 4000 Agent Reference design on the following TRC servers:

Cisco UCS C240 M5SX Large

Cisco UCS C240 M6SX Large

This model adds servers to scale up from the 2000 Agent Reference Design.

You can only deploy two AW-HDS-DDS per data center site in the 4000 Agent Reference Design. In larger solutions, you use a
                                          combination of HDS-DDS and AW-HDS.

#### Support on the Cisco UCS C240 M5SX and Cisco UCS C240 M6SX Large TRC Servers

This figure shows the base layout of the components in a 4000 Agent Reference Design on Cisco UCS C240 M5SX and Cisco UCS C240 M6SX TRC server s .

This table lists the specifications for VMs.

VM

vCPU

MHz

vRAM

vDisk 1

vDisk 2

Rogger

4

5000

6

150

150

Live Data

4

5500

146

IdS

4

1500

10

146

Unified CVP Reporting Server

4

1800

6

80

438

Unified CVP OAMP

2

400

4

150

Unified CM

4

7200

14

110

PG

2

4000

6

150

Unified CVP Server

4

3000

12

250

Finesse

4

5000

146

Unified Intelligence Center

4

3600

16

200

AW-HDS-DDS

4

5000

16

150

500

VVB

4

9000

10

146

Server

vCPU

MHz

vRAM

vDisk

Data Center Site A - Server 1A

34

44800

1736

Data Center Site B - Server 1B

28

37200

1476

Data Center Site A - Server 2A

36

41200

2792

Data Center Site B - Server 2B

36

41200

2792

Server 3

24

54000

60

876

### 12000 Agent Reference Designs

This Reference Design for a contact center enterprise solution supports 12000 agents on the following TRC servers:

Cisco UCS C240 M5SX Large

Cisco UCS C240 M6SX Large

This model adds servers to scale up from the 4000 Agent Reference Design.

Customers can customize the 12000 deployment to serve only 8000 agents by adjusting the number of Agent PG, CUCM Subscribers
                                          and Finesse clusters.

#### Support on the Cisco UCS C240 M5SX and Cisco UCS C240 M6SX Large TRC Servers

The following figure shows the base layout of the components in a 12000 Agent Reference Design on Cisco UCS C240 M5SX and
                                    Cisco UCS C240 M6SX Large TRC servers.

This table lists the specifications for VMs.

VM

vCPU

MHz

vRAM

vDisk 1

vDisk 2

Router

4

4000

8

150

Logger

4

6000

8

150

500

Live Data

8

16500

40

146

IdS

4

1500

10

146

Unified CVP Reporting Server

4

1800

6

80

438

Unified CVP OAMP

2

400

4

150

HDS-DDS

8

17500

16

150

500

AW-HDS

8

17500

16

150

500

PG

2

4000

6

150

Unified CVP Server

4

3000

12

250

Finesse

4

5000

16

146

Unified CM

4

7200

14

110

Unified Intelligence Center

4

3600

16

200

VVB

4

9000

10

146

Server

vCPU

MHz

vRAM

vDisk

Data Center Site A - Server 1A

34

47700

92

2410

Data Center Site B - Server 1B

32

47300

88

2260

Data Center Site A - Server 2A

40

58200

136

1768

Data Center Site B - Server 2B

36

51000

122

1658

Data Center Site A - Server 3A

36

51000

122

1658

Data Center Site B - Server 3B

36

51000

122

1658

Data Center Site A - Server 4A

24

52500

48

1950

Data Center Site B - Server 4B

24

52500

48

1950

Data Center Site A - Server 5A

40

58200

136

1768

Data Center Site B - Server 5B

36

51000

122

1658

Server 6

24

54000

60

876

#### Reporting Users in the 12000 Agent Reference Design Model

AW-HDS 3, AW-HDS 4, AW-HDS 5, and AW-HDS 6 in Servers 4A and 4B, are optional to support more than 400 reporting users. Servers
                                 5A and 5B are optional to support more than 8000 agents. Servers 6A and 6B are optional to support more than 400 reporting
                                 users.

This Reference Design supports a maximum of six CUIC VMs and six AW-HDS VMs, three VMs on each site. This limit can accommodate
                                 a maximum of 1200 reporting users. If one site shuts down, the remaining site can only support 600 reporting users on its
                                 three nodes.

### 24000 Agent Reference Designs

This Reference Design for a contact center enterprise solution supports 24000 agents on the following TRC servers:

Cisco UCS C240 M5SX Large

Cisco UCS C240 M6SX Large

This model adds servers to scale up from the 12000 Agent Reference Design.

A Unified CCE solution with PGs of version 11.6 and Packaged CCE do not support the 24000 Agent Deployment.

#### Support on the Cisco UCS C240 M5SX and Cisco UCS C240 M6SX Large TRC Servers

The following figure shows the base layout of the components in a 24000 Agent Reference Design on Cisco UCS C240 M5SX and
                                 Cisco UCS C240 M6SXLarge TRC server.

This table lists the specifications for VMs.

VM

vCPU

MHz

vRAM

vDisk 1

vDisk 2

Router

4

4000

8

150

Logger

4

6000

8

150

500

Live Data

12

24000

146

IdS

8

3000

10

146

Unified CVP Reporting Server

4

1800

6

80

438

Unified CVP OAMP

2

400

4

150

HDS-DDS

8

17500

16

150

500

AW-HDS

8

17500

16

150

500

PG

2

4000

6

150

Unified CVP Server

4

3000

12

250

Finesse

4

5000

146

Unified CM

4

7200

14

110

Unified Intelligence Center

4

3600

16

200

VVB

4

9000

10

146

Server

vCPU

MHz

vRAM

vDisk

Data Center Site A - Server 1A

42

56700

2410

Data Center Site B - Server 1B

40

56300

2260

Data Center Site A - Server 2A

40

58200

1768

Data Center Site B - Server 2B

36

51000

1658

Data Center Site A - Server 3A

36

51000

1658

Data Center Site B - Server 3B

36

51000

1658

Data Center Site A - Server 4A

24

52500

48

1950

Data Center Site B - Server 4B

24

52500

48

1950

Data Center Site A - Server 5A

40

58200

1768

Data Center Site B - Server 5B

36

51000

1658

Data Center Site A - Server 6A

36

51000

1658

Data Center Site B - Server 6B

36

51000

1658

Data Center Site A - Server 7A

36

54600

1568

Data Center Site B - Server 7B

32

47400

1458

Data Center Site A - Server 8A

32

47400

1458

Data Center Site B - Server 8B

32

47400

1458

Data Center Site A - Server 9A

24

54000

60

876

Data Center Site B - Server 9B

24

54000

60

876

Server 10

24

54000

60

876

#### Reporting Users in the 24000 Agent Reference Design Model

AW-HDS 3, AW-HDS 4, AW-HDS 5, and AW-HDS 6 in Servers 4A and 4B, are optional to support more than 400 reporting users. Servers
                                 5A and 5B are optional to support more than 8000 agents. Servers 6A and 6B are optional to support more than 400 reporting
                                 users.

This Reference Design supports a maximum of eight CUIC VMs and six AW-HDS VMs, three VMs on each site. This limit can accommodate
                                 a maximum of 1200 reporting users. If one site shuts down, the remaining site can only support 600 reporting users on its
                                 three nodes.

### Scale up to 36000 Agents

You can modify your existing 24000 agent reference design to scale up to 36000 agents.

36000 concurrent Agents and corresponding configuration limits while employing the 24000 Agent deployment model is not supported
                                             through CCMP.

The 36000 agent deployment must adhere to the spec-based constraints with respect to supported processors and ESXi server
                                 resource reservations. For more information, see Virtual Machines Resource Provisioning Policy . You must also adhere to specific configuration limits as described in Table 1 .

Add more agent PGs, Unified CVP nodes, and Cisco Finesse nodes to support 36000 agents as required. Add two Cisco Unified
                                 Communications Manager clusters to the deployment to support the additional 12000 agents, with no more than eight subscriber
                                 nodes and 8000 users per cluster.

To scale up to 36000 agents, OVA values such as vCPU allocation (MHz), RAM, and vDisk size for Logger, Live Data, and Cisco
                                 IdS will need to be increased. For the specific values, see the virtualization table for your CCE version on the Virtualization for Unified Contact Center Enterprise page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

To enable support for Agent Event Extended details, update the Logger OVA file as below:

Increase the number of vCPUs from 4 to 8, the vCPU MHZ reservation from 6000 to 12000, and RAM from 8 to 16 GB.

For Unified Intelligence Center, two 6-node clusters are required to support the overall reporting load. Dedicate one Unified
                                 Intelligence Center cluster to support 1200 reporting users and Live Data reports for a maximum of 18000 agents. Dedicate
                                 the second cluster to handle Live Data reports for the remaining agents. Configure Cisco Finesse desktop layouts so that each
                                 of the 12 Unified Intelligence Center nodes (across the two clusters) serves Live Data reports for a maximum of 3000 agents.

Parameter

Value

Agent Limits

Configured Agents

108000

Average Skills per Agent

5

Number of Agents in a Skill Group

Same limit as for 24000 Agents

Maximum Number of Agent PGs

24

Supervisor and Reporting User Limits

Active Supervisors

3600 Cisco Finesse Supervisors

No change to the number of reporting users

Configured Supervisors

10800

Precision Queue and Skill Groups Limits

Skill Groups per System

No change to the number of skill groups per system

System Load Limits

Maximum Inbound Calls per Second (CPS)

235

Congestion Control (CPS)

310

The agent event extended detail capabilites are supported only for 36000 agent deployment. For more information, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html

### Scale Up to 48000 Agents

You can modify your existing 24000 agent reference design to scale up to 48000 agents.

To fulfill the virtual memory requirement for Router in 48000 deployment, you must configure the Router service on both Side
                                             A and Side B to launch the Router process (router.exe) as a 64-bit application. To change your Router process build architecture
                                             from 32-bit to 64-bit, install 12.6(2) ES4 and perform the steps mentioned in the Readme file on the Software Downloads page.
                                             You must deploy 12.6(2) ES25 for logger.

The 48000 agent deployment must adhere to the spec-based constraints with respect to supported processors and ESXi server
                                 resource reservations. For more information, see Virtual Machines Resource Provisioning Policy . You must also adhere to specific configuration limits. For more information about the configuration limits, see the Parameter Values for 48000 Agents table.

Add more agent PGs, Unified CVP nodes, and Cisco Finesse nodes to support 48000 agents as required. Add three Cisco Unified
                                 Communications Manager clusters to the deployment to support the additional 24000 agents, with no more than 8 subscriber nodes
                                 and 8000 users per cluster.

To scale up to 48000 agents, OVA values such as vCPU allocation (MHz), RAM, and vDisk size for Router, Logger, Live Data,
                                 and Cisco IdS will need to be increased. For the specific values, see the virtualization table for your CCE version on the Virtualization for Unified Contact Center Enterprise page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

For Unified Intelligence Center, you need two 8-node cluster to support the overall reporting load. Use one Unified Intelligence
                                 Center cluster to support 1200 reporting users and Live Data reports for a maximum of 24000 Agents. Use the second cluster
                                 to handle Live Data reports for the remaining agents. Configure Cisco Finesse desktop layouts so that each of the 16 Unified
                                 Intelligence Center nodes (across the two clusters) serves Live Data reports for a maximum of 3000 Agents.

Use the Config Limit CLI tool to modify the value of calls per second (CPS) for your deployment. For more details, see the Change Limits for Calls Per Second to Support 36000 or 48000 Agents topic in the Appendix chapter of the Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

Parameter

Value

Agent Limits

Configured Agents

144000

Average Skills per Agent

5

Number of Agents in a Skill Group

Same limit as for 24000 Agents

Maximum Number of concurrent Agent PGs

48

Supervisor and Reporting User Limits

Active Supervisors

4800 Cisco Finesse Supervisors

No change to the number of reporting users

Configured Supervisors

14400

Precision Queue and Skill Groups Limits

Skill Groups per System

No change to the number of skill groups per system

System Load Limits

Maximum Inbound Calls per Second (CPS)

300

Congestion Control (CPS)

330

### Contact Director

Only Unified CCE supports the Contact Director reference design. The Contact Director distributes incoming calls to other
                              contact center instances. The targets can be Unified CCE instances that connect to third-party contact centers. The Contact
                              Director distributes incoming contacts to up to 3 Unified CCE instances, supporting a total of 24000 active agents.

In the above image, when a call comes into the Voice Gateway on the Contact Director,​ the Voice Gateway passes the call to
                              CVP for VRU processing.​ When the caller opts to speak to an agent, CVP passes the call data to the Router through the VRU
                              PG.​The Application Gateway forwards information to the Router, which directs calls to the selected target instance.

## Topologies for
                        	 Reference Designs

The Contact Center Enterprise
                                 						Reference Designs also define the allowed topologies for your deployment. The deployment topology
                           		consists of where you install the VMs for your data center and how your agents
                           		connect to the data center. This figure shows the basic topologies that you can
                           		use in a Reference Design.

The Main Site can use either a Centralized or a Distributed topology.

A Remote Site can be geographically colocated with the Main Site .

The Reference
                           		Designs allow the following topologies:

Topology

Description

Centralized

You host both sites of the redundant components in the same physical data center. Even when they are on the same LAN, the
                                       maximum round-trip time between the two sites is 80 ms. The data center includes the core contact center components and Unified
                                       CM.

Distributed

You host each site of the redundant components in a different geographical location. Distributed sites allow you to keep running on the other site if one site fails. You can also handle routing without sending a contact to a site in a different geographical region. The maximum round-trip time between the two sites is 80 ms.

Global

You have a centralized or distributed main site . You also have a remote site that is generally in a different geographical location. The remote site gives you local access in that geographic region. The remote site allows you to handle your global work load without creating another contact center instance.

The remote site requires a separate Unified CM cluster and a separate Cisco Finesse cluster if the RTT from the data center is greater than
                                       80 ms. The maximum round-trip time between the main site and remote sites is 400 ms.

A remote site cannot include a Cisco Unified Intelligence Center server.

This
                                       					 topology fits the outsourcer model where the outsourcer has a separate
                                       					 peripheral gateway and a corresponding peripheral.

Starting in Release 11.6, Packaged CCE supports this topology.

The Reference Designs allow the following methods for connecting your agents to a site :

Remote
                                       					 Office Topology

Description

Remote
                                       					 Office with Agents

A contact center office with agent workstations that connects to a site through a WAN router. The voice termination is at the site . All contacts go through the site first and then to the agents.

Remote
                                       					 Office with Agents and Local Trunk

A contact
                                       					 center office with a connection to the local PSTN. Contacts come in on the
                                       					 local trunk and the local gateway passes them to the data center for routing.

Home Agent
                                       					 with Broadband - Cisco Virtual Office (CVO)

An agent at a remote location with a VPN connection to a site . The agent has a Cisco IP Phone and a Cisco Finesse desktop. The agent can optionally use a Cisco Virtual Office (CVO) router
                                       for a permanent VPN connection.

Unified
                                       					 Mobile Agent

An agent
                                       					 who uses a PSTN phone.

The maximum
                                       		  allowed round-trip time between any remote office and the data center is 200
                                       		  ms.

## Non-Reference Design Solutions

The Contact Center Enterprise
                                 						Reference Designs define what you can use in your contact center solution. If your solution includes anything that the Reference Designs do
                           not explicitly allow, your solution is a Non-Reference Design. Most Non-Reference Design solutions require Unified CCE.

### Elements with Alternatives in the Reference Designs

There are newer technologies that supersede most of the components, options, features, and configurations that are not supported
                              in Reference Design solutions. Some of the elements in this category are:

Non-Reference Design Element

Reference Design Alternative

Cisco ICM to ICM Gateway (Except in the Contact Director model)

Contact Director

Unified IP IVR or third-party Voice Response Unit (VRU) applications

Unified CVP

Mismatch versions in Unified CCE subcomponents (This is allowed only while upgrading your contact center from one release
                                          to another.)

All versions match after upgrade

Unified CVP Call Director

Unified CVP Comprehensive call flow

Translation Route

Unified CVP Comprehensive call flow, except for third-party PGs

Multi-Unified CM PIM configuration

Multiple PGs on separate VMs

Unified CM Multi-cast Music on Hold (MoH)

Gateway-based MoH or Unicast MoH

Tomcat as the media server for Unified CVP

Prepackaged IIS included in the Unified CVP install

MGCP protocol

SIP

G.722, iSAC, and iLBC codecs

Mixed codec support

Dialed Number Plan (DNP)

Dialed Numbers and CTI Route Points

This is not an exhaustive list.

### Elements Without Alternatives in the Reference Designs

There are some elements that you cannot use in Reference Design solutions that do not have a defined alternative. Some of the elements in this category are:

Time-Division Multiplexing (TDM) (third-party legacy Automatic Call Distribution integration)

TDM NIC

Parent/Child topology for out-sourcing deployments

This is not an exhaustive list.

| Note | The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions: Packaged Contact Center Enterprise Unified Contact Center Enterprise For information about design considerations and guidelines specific to Unified CCE , see the remaining chapters. |
|---|---|

| Reference Design | Packaged CCE | Unified CCE |
|---|---|---|
| 2000 Agents | Yes | Yes |
| 4000 Agents | Yes | Yes |
| 12000 Agents | Yes | Yes |
| 24000 Agents | No | Yes |
| 36000 Agents | No | Yes |
| 48000 Agents | No | Yes |
| Contact Director | No | Yes |
| Non-Reference Designs | ICM-to-ICM Gateway | Yes |

| Reference Design | Packaged CCE | Unified CCE |
|---|---|---|
| Label | Label |
| 2000 Agent | Packaged CCE: 2000 Agents | UCCE: 2000 Agents |
| 4000 Agent | Packaged CCE: 4000 Agents | UCCE: 4000 Agents |
| 12000 Agent | Packaged CCE: 12000 Agents | UCCE: 12000 Agents |
| 24000 Agent | NA | UCCE: 24000 Agents Router/Logger |
| 36000 Agent | NA | UCCE: 36000 Agents Router/Logger |
| 48000 Agent | NA | UCCE: 48000 Agents Router/Logger |
| Contact Director | NA | Contact Director |
| Non-Reference Designs | ICM-to-ICM Gateway Packaged CCE: 4000 Agents Packaged CCE: 12000 Agents | ICM Rogger ICM Router/Logger |
| Lab Only Designs | Packaged CCE: Lab Mode | UCCE: Progger (Lab Only) |

| Note | This figure highlights only a few Non-Reference Design components and topologies. The Non-Reference Design sections expand
                                       on this list. |
|---|---|

| Note | In general, you cannot use the ICM-to-ICM Gateway in Reference Designs. Only the Contact Director Reference Design allows
                                       you to use that gateway. |
|---|---|

| Note | The previously used Oversubscription policy is a part of the Virtual Machine (VM) Resource Provisioning Policy. |
|---|---|

| Note | Apply the VM Resource Provisioning policy on a per-server basis. This policy does not apply to the Reference Design VM layouts.
                                             Your solution can contain servers that use the Reference Design VM layouts and other VM layouts that use the VM Resource Provisioning
                                             policy rules. |
|---|---|

| Note | The Virtual Machine Placement Tool does not currently allow you to oversubscribe. This limitation is only an issue with the
                                             tool. You can oversubscribe within the limits that are provided here. |
|---|---|

| Note | The custom remote server should have the same provisioning specification as Unified CVP server. |
|---|---|

| Note | Adding more disks is not permitted in the CCE 2000 agent deployment. Any changes to the number of disks will result in a VM
                                             validation error. |
|---|---|

| VM | vCPU | MHz | vRAM | vDisk 1 | vDisk 2 | vDisk 3 |
|---|---|---|---|---|---|---|
| Rogger | 4 | 5000 | 6 | 150 | 150 |  |
| Unified CM | 4 | 7200 | 14 | 110 |  |  |
| Unified CVP OAMP | 2 | 400 | 4 | 150 |  |  |
| Unified CVP Server | 4 | 3000 | 12 | 250 |  |  |
| Unified CVP Reporting Server | 4 | 1800 | 6 | 80 | 438 |  |
| ECE Dataserver 1 | 4 | 4000 | 20 | 80 | 50 | 300 |
| CUIC-LD-IdS | 4 | 5500 | 24 | 200 |  |  |
| AW-HDS-DDS | 4 | 5000 | 16 | 150 | 500 |  |
| PG | 2 | 4000 | 6 | 150 |  |  |
| Finesse | 4 | 5000 | 16 | 146 |  |  |
| VVB | 4 | 9000 | 10 | 146 |  |  |

| Server | vCPU | MHz | vRAM | vDisk |
|---|---|---|---|---|
| Data Center Site A | 36 | 46300 | 132 | 2496 |
| Data Center Site B | 34 | 40500 | 120 | 2754 |
| Server 2 | 16 | 36000 | 40 | 584 |

| Note | You can only deploy two AW-HDS-DDS per data center site in the 4000 Agent Reference Design. In larger solutions, you use a
                                          combination of HDS-DDS and AW-HDS. |
|---|---|

| VM | vCPU | MHz | vRAM | vDisk 1 | vDisk 2 |  |
|---|---|---|---|---|---|---|
| Rogger | 4 | 5000 | 6 | 150 | 150 |  |
| Live Data | 4 | 5500 | 32 | 146 |  |  |
| IdS | 4 | 1500 | 10 | 146 |  |  |
| Unified CVP Reporting Server | 4 | 1800 | 6 | 80 | 438 |  |
| Unified CVP OAMP | 2 | 400 | 4 | 150 |  |  |
| Unified CM | 4 | 7200 | 14 | 110 |  |  |
| PG | 2 | 4000 | 6 | 150 |  |  |
| Unified CVP Server | 4 | 3000 | 12 | 250 |  |  |
| Finesse | 4 | 5000 | 16 | 146 |  |  |
| Unified Intelligence Center | 4 | 3600 | 16 | 200 |  |  |
| AW-HDS-DDS | 4 | 5000 | 16 | 150 | 500 |  |
| VVB | 4 | 9000 | 10 | 146 |  |  |

| Server | vCPU | MHz | vRAM | vDisk |
|---|---|---|---|---|
| Data Center Site A - Server 1A | 34 | 44800 | 110 | 1736 |
| Data Center Site B - Server 1B | 28 | 37200 | 92 | 1476 |
| Data Center Site A - Server 2A | 36 | 41200 | 132 | 2792 |
| Data Center Site B - Server 2B | 36 | 41200 | 132 | 2792 |
| Server 3 | 24 | 54000 | 60 | 876 |

| Note | Customers can customize the 12000 deployment to serve only 8000 agents by adjusting the number of Agent PG, CUCM Subscribers
                                          and Finesse clusters. |
|---|---|

| VM | vCPU | MHz | vRAM | vDisk 1 | vDisk 2 |
|---|---|---|---|---|---|
| Router | 4 | 4000 | 8 | 150 |  |
| Logger | 4 | 6000 | 8 | 150 | 500 |
| Live Data | 8 | 16500 | 40 | 146 |  |
| IdS | 4 | 1500 | 10 | 146 |  |
| Unified CVP Reporting Server | 4 | 1800 | 6 | 80 | 438 |
| Unified CVP OAMP | 2 | 400 | 4 | 150 |  |
| HDS-DDS | 8 | 17500 | 16 | 150 | 500 |
| AW-HDS | 8 | 17500 | 16 | 150 | 500 |
| PG | 2 | 4000 | 6 | 150 |  |
| Unified CVP Server | 4 | 3000 | 12 | 250 |  |
| Finesse | 4 | 5000 | 16 | 146 |  |
| Unified CM | 4 | 7200 | 14 | 110 |  |
| Unified Intelligence Center | 4 | 3600 | 16 | 200 |  |
| VVB | 4 | 9000 | 10 | 146 |  |

| Server | vCPU | MHz | vRAM | vDisk |
|---|---|---|---|---|
| Data Center Site A - Server 1A | 34 | 47700 | 92 | 2410 |
| Data Center Site B - Server 1B | 32 | 47300 | 88 | 2260 |
| Data Center Site A - Server 2A | 40 | 58200 | 136 | 1768 |
| Data Center Site B - Server 2B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 3A | 36 | 51000 | 122 | 1658 |
| Data Center Site B - Server 3B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 4A | 24 | 52500 | 48 | 1950 |
| Data Center Site B - Server 4B | 24 | 52500 | 48 | 1950 |
| Data Center Site A - Server 5A | 40 | 58200 | 136 | 1768 |
| Data Center Site B - Server 5B | 36 | 51000 | 122 | 1658 |
| Server 6 | 24 | 54000 | 60 | 876 |

| Note | A Unified CCE solution with PGs of version 11.6 and Packaged CCE do not support the 24000 Agent Deployment. |
|---|---|

| VM | vCPU | MHz | vRAM | vDisk 1 | vDisk 2 |
|---|---|---|---|---|---|
| Router | 4 | 4000 | 8 | 150 |  |
| Logger | 4 | 6000 | 8 | 150 | 500 |
| Live Data | 12 | 24000 | 50 | 146 |  |
| IdS | 8 | 3000 | 10 | 146 |  |
| Unified CVP Reporting Server | 4 | 1800 | 6 | 80 | 438 |
| Unified CVP OAMP | 2 | 400 | 4 | 150 |  |
| HDS-DDS | 8 | 17500 | 16 | 150 | 500 |
| AW-HDS | 8 | 17500 | 16 | 150 | 500 |
| PG | 2 | 4000 | 6 | 150 |  |
| Unified CVP Server | 4 | 3000 | 12 | 250 |  |
| Finesse | 4 | 5000 | 16 | 146 |  |
| Unified CM | 4 | 7200 | 14 | 110 |  |
| Unified Intelligence Center | 4 | 3600 | 16 | 200 |  |
| VVB | 4 | 9000 | 10 | 146 |  |

| Server | vCPU | MHz | vRAM | vDisk |
|---|---|---|---|---|
| Data Center Site A - Server 1A | 42 | 56700 | 102 | 2410 |
| Data Center Site B - Server 1B | 40 | 56300 | 98 | 2260 |
| Data Center Site A - Server 2A | 40 | 58200 | 136 | 1768 |
| Data Center Site B - Server 2B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 3A | 36 | 51000 | 122 | 1658 |
| Data Center Site B - Server 3B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 4A | 24 | 52500 | 48 | 1950 |
| Data Center Site B - Server 4B | 24 | 52500 | 48 | 1950 |
| Data Center Site A - Server 5A | 40 | 58200 | 136 | 1768 |
| Data Center Site B - Server 5B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 6A | 36 | 51000 | 122 | 1658 |
| Data Center Site B - Server 6B | 36 | 51000 | 122 | 1658 |
| Data Center Site A - Server 7A | 36 | 54600 | 120 | 1568 |
| Data Center Site B - Server 7B | 32 | 47400 | 106 | 1458 |
| Data Center Site A - Server 8A | 32 | 47400 | 106 | 1458 |
| Data Center Site B - Server 8B | 32 | 47400 | 106 | 1458 |
| Data Center Site A - Server 9A | 24 | 54000 | 60 | 876 |
| Data Center Site B - Server 9B | 24 | 54000 | 60 | 876 |
| Server 10 | 24 | 54000 | 60 | 876 |

| Note | 36000 concurrent Agents and corresponding configuration limits while employing the 24000 Agent deployment model is not supported
                                             through CCMP. |
|---|---|

| Note | To enable support for Agent Event Extended details, update the Logger OVA file as below: Increase the number of vCPUs from 4 to 8, the vCPU MHZ reservation from 6000 to 12000, and RAM from 8 to 16 GB. |
|---|---|

| Parameter | Value |
|---|---|
| Agent Limits |
| Configured Agents | 108000 |
| Average Skills per Agent | 5 |
| Number of Agents in a Skill Group | Same limit as for 24000 Agents |
| Maximum Number of Agent PGs | 24 |
| Supervisor and Reporting User Limits |
| Active Supervisors | 3600 Cisco Finesse Supervisors No change to the number of reporting users |
| Configured Supervisors | 10800 |
| Precision Queue and Skill Groups Limits |
| Skill Groups per System | No change to the number of skill groups per system |
| System Load Limits |
| Maximum Inbound Calls per Second (CPS) | 235 |
| Congestion Control (CPS) | 310 |

| Note | The agent event extended detail capabilites are supported only for 36000 agent deployment. For more information, see the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html |
|---|---|

| Note | To fulfill the virtual memory requirement for Router in 48000 deployment, you must configure the Router service on both Side
                                             A and Side B to launch the Router process (router.exe) as a 64-bit application. To change your Router process build architecture
                                             from 32-bit to 64-bit, install 12.6(2) ES4 and perform the steps mentioned in the Readme file on the Software Downloads page.
                                             You must deploy 12.6(2) ES25 for logger. |
|---|---|

| Parameter | Value |
|---|---|
| Agent Limits |
| Configured Agents | 144000 |
| Average Skills per Agent | 5 |
| Number of Agents in a Skill Group | Same limit as for 24000 Agents |
| Maximum Number of concurrent Agent PGs | 48 |
| Supervisor and Reporting User Limits |
| Active Supervisors | 4800 Cisco Finesse Supervisors No change to the number of reporting users |
| Configured Supervisors | 14400 |
| Precision Queue and Skill Groups Limits |
| Skill Groups per System | No change to the number of skill groups per system |
| System Load Limits |
| Maximum Inbound Calls per Second (CPS) | 300 |
| Congestion Control (CPS) | 330 |

| Topology | Description |
|---|---|
| Centralized | You host both sites of the redundant components in the same physical data center. Even when they are on the same LAN, the
                                       maximum round-trip time between the two sites is 80 ms. The data center includes the core contact center components and Unified
                                       CM. |
| Distributed | You host each site of the redundant components in a different geographical location. Distributed sites allow you to keep running on the other site if one site fails. You can also handle routing without sending a contact to a site in a different geographical region. The maximum round-trip time between the two sites is 80 ms. |
| Global | You have a centralized or distributed main site . You also have a remote site that is generally in a different geographical location. The remote site gives you local access in that geographic region. The remote site allows you to handle your global work load without creating another contact center instance. The remote site requires a separate Unified CM cluster and a separate Cisco Finesse cluster if the RTT from the data center is greater than
                                       80 ms. The maximum round-trip time between the main site and remote sites is 400 ms. Note A remote site cannot include a Cisco Unified Intelligence Center server. This
                                       					 topology fits the outsourcer model where the outsourcer has a separate
                                       					 peripheral gateway and a corresponding peripheral. Note Starting in Release 11.6, Packaged CCE supports this topology. | Note | A remote site cannot include a Cisco Unified Intelligence Center server. | Note | Starting in Release 11.6, Packaged CCE supports this topology. |
| Note | A remote site cannot include a Cisco Unified Intelligence Center server. |
| Note | Starting in Release 11.6, Packaged CCE supports this topology. |

| Note | A remote site cannot include a Cisco Unified Intelligence Center server. |
|---|---|

| Note | Starting in Release 11.6, Packaged CCE supports this topology. |
|---|---|

| Remote
                                       					 Office Topology | Description |
|---|---|
| Remote
                                       					 Office with Agents | A contact center office with agent workstations that connects to a site through a WAN router. The voice termination is at the site . All contacts go through the site first and then to the agents. |
| Remote
                                       					 Office with Agents and Local Trunk | A contact
                                       					 center office with a connection to the local PSTN. Contacts come in on the
                                       					 local trunk and the local gateway passes them to the data center for routing. |
| Home Agent
                                       					 with Broadband - Cisco Virtual Office (CVO) | An agent at a remote location with a VPN connection to a site . The agent has a Cisco IP Phone and a Cisco Finesse desktop. The agent can optionally use a Cisco Virtual Office (CVO) router
                                       for a permanent VPN connection. |
| Unified
                                       					 Mobile Agent | An agent
                                       					 who uses a PSTN phone. |

| Note | The maximum
                                       		  allowed round-trip time between any remote office and the data center is 200
                                       		  ms. |
|---|---|

| Non-Reference Design Element | Reference Design Alternative |
|---|---|
| Cisco ICM to ICM Gateway (Except in the Contact Director model) | Contact Director |
| Unified IP IVR or third-party Voice Response Unit (VRU) applications | Unified CVP |
| Mismatch versions in Unified CCE subcomponents (This is allowed only while upgrading your contact center from one release
                                          to another.) | All versions match after upgrade |
| Unified CVP Call Director | Unified CVP Comprehensive call flow |
| Translation Route | Unified CVP Comprehensive call flow, except for third-party PGs |
| Multi-Unified CM PIM configuration | Multiple PGs on separate VMs |
| Unified CM Multi-cast Music on Hold (MoH) | Gateway-based MoH or Unicast MoH |
| Tomcat as the media server for Unified CVP | Prepackaged IIS included in the Unified CVP install |
| MGCP protocol | SIP |
| G.722, iSAC, and iLBC codecs | Mixed codec support |
| Dialed Number Plan (DNP) | Dialed Numbers and CTI Route Points |

| Note | This is not an exhaustive list. |
|---|---|

| Note | This is not an exhaustive list. |
|---|---|