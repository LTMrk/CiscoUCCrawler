---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-design-guide-pcce-b-soldg-for-p-79585ccb7d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/design/guide/pcce_b_soldg-for-packaged-cce-12_6_2/pcce_b_soldg-for-packaged-cce-12_6_chapter_0100.html
retrieved_at: 2026-08-21T04:49:42.063678+00:00
---

Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 12.6(2)

# Solution Design Guide for Cisco Packaged Contact Center Enterprise, Release 12.6(2)

Updated: June 16, 2023

Chapter: Configuration Limits and Feature Availability for Reference Designs

## Chapter: Configuration Limits and Feature Availability for Reference Designs

# Configuration Limits and Feature Availability for Reference Designs

## Reference Design Configuration Limits

The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions:

Packaged Contact Center Enterprise

Unified Contact Center Enterprise

The following tables list key configuration
                           limits for Contact Center Enterprise
                                 						Reference Designs solutions.

Some of these limits are interdependent and dynamically change depending on the elements in your solution. For example, the
                           number of skills per agent affects the maximum number of agents.

Limits that are listed as "per PG" always refer to a redundant pair of PGs.

Important

Your contact center enterprise solution can only use the new higher configuration limits with the standard three coresident
                                       PG layout.

### Agent Limits

The figures in the Contact Director column refer to what are configured on the Contact Director. The figures do not include
                                             what is configured on the target systems to which the Contact Director connects.

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Active Agents 1

2000

4000

12,000

24,000

24,000 (cumulative on 3 target systems)

Active Agents on each Unified CM cluster

2000

4000

8000

8000

NA

Configured Agents

12,000

24,000

72,000

72,000

NA

12000

12000

12000

12000

NA

Agents with TraceON enabled

100

100

400

400

NA

Agent Desk Settings

2000

4000

12,000

12,000

NA

Active Mobile Agents per Agent PG 2 3

2000 with nailed-up connections

Or

1500 with call-by-call connections

2000 with nailed-up connections

Or

1500 with call-by-call connections

2000 with nailed-up connections

Or

1500 with call-by-call connections

2000 with nailed-up connections

Or

1500 with call-by-call connections

NA

Active ECE Multimedia Agents

1500 4

4000 5

12,000 6

24,000 7

NA

Agents per team

50

50

50

50

NA

Teams to which an agent can belong

1

1

1

1

NA

Skills per agent

15

Refer to the section on dynamic sizing for details.

15

Refer to the section on dynamic sizing for details.

15

Refer to the section on dynamic sizing for details.

10

Refer to the section on dynamic sizing for details.

NA

Number of agents in a skill group

12,000

24,000

72,000

72,000

NA

Attributes per agent

50

50

50

50

NA

### Supervisor and Reporting User Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

Unified CCE 24000 Agent Reference Design Model

Contact Director Reference Design Model

Active Supervisors 8

200

400

1200

2400 9

NA

Configured Supervisors

1200

2400

7200

7200

NA

Active teams

200

400

1200

2400

NA

Configured teams

1200

2400

7200

7200

NA

Supervisors per Team

20

20

20

20

NA

Teams per supervisor

20

20

20

20

NA

Agents per supervisor

1000

1000

1000

1000

NA

Active Cisco Unified Intelligence Center Reporting users

200

400

1200 10

1200 11

NA

Configured Cisco Unified Intelligence Center Reporting users

1200

2400

7200

7200

NA

Reporting users per CUIC node

100

200

200

200

### Access Control Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Active Administrators per distributor 12

50

50

50

50

50

Configured Web Administrators

100

100

100

100

NA

Roles—Packaged CCE only

30

30

30

NA

NA

Departments—Packaged CCE only

200

200

200

NA

NA

Department per Administrator—Packaged CCE only

10

10

10

NA

NA

Machines in inventory

1000

1000

1000

1000

NA

### Outbound Campaign Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Outbound dialer per system

1 per Agent PG

1 per Agent PG

1 per Agent PG

1 per Agent PG

NA

Outbound dialer maximum calls per second

60

120

240

240

NA

Outbound dialer maximum calls per second per dialer 13

60

60

60

60

NA

Outbound dialer maximum ports on each SIP dialer

3000

3000

3000

3000

NA

Outbound dialer maximum ports on each system (total)

3000

6000

12000

12000

NA

Number of Preview Campaigns per System

1500 campaigns

Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM.

1500 campaigns

Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM.

1500 campaigns

Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM.

1500 campaigns

Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM.

NA

Number of Predictive Campaigns per system (Agent or VRU based)

375

750

1500

1500

Campaign skill groups per Campaign

20

20

20

20

NA

Predictive Campaign Skill Groups per Peripheral

375

375

375

375

NA

Maximum Outbound Skills per Agent

5

5

5

5

NA

Do Not Call Records per Import

1,000,000

20,000,000

60,000,000

60,000,000

NA

### Precision Queue and Skill Groups Limits

Each Precision Queue has an associated Skill Group. Each Precision Queue effectively has a weight of two Skill Groups.

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Skill Groups per System

16,000 14

16,000

27,000

48,000

54,000

Enterprise Skill Groups

4000

4000

4000

4000

4000

Maximum combined configured Skill Groups and Precision Queues per peripheral

4000

4000

4000

4000

NA

Configured Precision Queues per system

4000

4000

The smaller of:

4000

Or

27,000 divided by the number of agent peripherals

The smaller of:

4000

Or

48,000 divided by the number of agent peripherals

8000 of the maximum 54,000 queues

Precision Queue steps

10,000

10,000

10,000

10,000

NA

Precision Queue term per Precision Queue

10

10

10

10

NA

Precision steps per Precision Queue

10

10

10

10

NA

Unique attributes per Precision Queue

10

10

10

10

NA

Max Unique Skills per Team

50

50

50

50

NA

Configured labels

100,000

100,000

160,000

160,000

160,000

Precision Routing Attributes on each system

10,000

10,000

10,000

10,000

NA

Precision Routing Attributes for each Agent

50

50

50

50

NA

Skill Group statistics refresh rate

10 seconds (default)

10 seconds (default)

10 seconds (default)

10 seconds (default)

NA

Skill Groups per PG

4000

4000

4000

4000

NA

Queues 17 per Contact Sharing Group

NA

NA

NA

NA

100

Contact Sharing Rules

NA

NA

NA

NA

100

Contact Sharing Groups

NA

NA

NA

NA

1000

### Task Routing Limits

Resource

2000 Agent Reference Design

4000 Agent Reference Design

12000 Agent Reference Design

24000 Agent Reference Design

Contact Director Reference Design

Maximum active agents assigned to tasks per system

2000

2000

2000

2000

NA

Maximum reserved and active tasks per agent 18

15

15

15

15

NA

Maximum incoming tasks/sec across all MRDs 19

5

5

5

5

NA

Task Routing API request/hr through Customer Collaboration Platform

15,000

15,000

15,000

15,000

NA

### Digital Routing Limits

Resource

2000 Agent Reference Design

4000 Agent Reference Design

12000 Agent Reference Design

24000 Agent Reference Design

36000 Agent Reference Design

Maximum active omnichannel agents assigned to tasks

2000

4000

4000

4000

4000

Maximum reserved and active tasks per agent 20

15

15

15

15

15

Maximum incoming tasks/sec across all MRDs for digital channels

8

15

15

15

15

Maximum tasks and voice calls per second

18

35

105

105

105

The DR API service enhances the limit of tasks that can be queued in the Digital Routing service memory to be 100,000. However,
                                 there are four separate sub-limits of queued tasks based on the Media Types. The number of physical queues in the Digital
                                 Routing service is dependent on the number of unique MRD's apart from the Cisco_Voice MRD that you employ to ensure right
                                 prioritization of tasks per MRD. These queues ensure that the tasks are injected into the CCE system based on the nature of
                                 the channel on which the request was received. For more information on Queue Settings, see the Configure queue settings section in the Cisco Packaged Contact Center Enterprise Features Guide .

### Dialed Number Limits

In the Global topology, each remote site can support the full limit of Dialed Numbers as mentioned in the table.

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Dialed Numbers on each CVP peripheral (External Voice and Post Call Survey ) 21

4000

4000

12,000

12,000

12,000

Dialed Number on each Unified CM peripheral (Internal Voice)

2000

2000

2000

2000

NA

Dialed Number on each MR peripheral (Multichannel)

1000

1000

1000

1000

NA

Dialed Number on each Unified CM peripheral (Outbound Voice)

1000

1000

1000

1000

NA

### System Load Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

VRU Ports in a Reference Layout 22 23

3000

6000

18,000

36,000

36,000

Maximum VRU Ports with Added PGs 24

6000

12,000

36,000

48,000

72,000

Maximum Inbound Calls per Second (CPS)

15

30

90

90

300 , of which Contact Sharing can handle 120 and the remainder is for self-service and line-of-business direct routing.

Congestion Control CPS 25

18

35

105

105

300

Maximum Inbound CPS per VRU PG 26

15

15

15

15

NA

Maximum VRU PIM per VRU PG

2

2

2

2

NA

Dynamic Reskilling (operations/hr.)

7200

7200

7200

7200

NA

Maximum Queued Calls and Tasks

15,000

15,000

15,000

15,000 27

15,000

Media Routing Domains per system

20

20

20

20

NA

Agent Callback requests through Customer Collaboration Platform (requests/hr.)

1000

1000

1000

1000

NA

ECE Email or Chat requests per hour for 400 agent deployment

6 per agent

6 per agent

6 per agent

6 per agent

NA

ECE Email or Chat requests per hour for 1500 agent deployment 28

6 per agent

6 per agent

6 per agent

6 per agent

NA

Incoming Messages per Second for CVP Reporting Server

420

420

420

420

420

Reports per user

For more details, see Resource Requirements for Reporting

2 Live Data reports

2 AW-RealTime reports

2 historical reports

2 Live Data reports

2 AW-RealTime reports

2 historical reports

2 Live Data reports

2 AW-RealTime reports

2 historical reports

2 Live Data reports

2 AW-RealTime reports

2 historical reports

NA

Maximum rows per report 29

3000 for real-time

8000 for historical

3000 for real-time

8000 for historical

3000 for real-time

8000 for historical

3000 for real-time

8000 for historical

NA

Configured Business Hour Objects

1000

1000

1000

1000

1000

Configured Schedule Objects per Business Hours Object 30

50

50

50

50

50

### Call Variable Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Persistent Enabled Expanded Call Variables (Default) 31

5

5

5

5

5

Persistent Enabled Expanded Call Variable Arrays

0

0

0

0

0

Maximum Contents per ECC (Expanded Call Context) Variable (bytes)

210

210

210

210

210

Maximum Total ECC Contents Size per ECC Payload (bytes)

2000

2000

2000

2000

2000

Maximum ECC Variable Name (bytes without null character)

32

32

32

32

32

Maximum Total Contents and Name Size for ECC Variables per ECC Payload (bytes)

2500

2500

2500

2500

2500

Maximum ECC Variables Contents per Call (bytes)

6000

6000

6000

6000

6000

Maximum System-wide ECC Variable Contents (bytes) 32

90,000,000

90,000,000

90,000,000

90,000,000

NA

Number of Peripheral Variables

10

10

10

10

10

Call Context for Peripheral Variables 1-10 (bytes)

40

40

40

40

40

### Other Limits

Resource

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

24000 Agent Reference Design Model

Contact Director Reference Design Model

Maximum Agent PGs with Live Data, Precision Queueing, or Single Sign-On enabled 33

4 34

4

12 (when using the 12000 agents Live Data OVA)

12

24 (when using the 24000 agents Live Data OVA)

24

50

Maximum PGs 35

30

100

150

150

NA

Maximum Agent PGs on each VM

1

1

1

1

NA

Maximum Cisco Finesse server pairs per PG pair 36

2

2

2

2

NA

MR PIMs on each MR PG

4

4

4

4

NA

Custom Application Gateway

20

20

20

20

20 per enterprise system

Bucket Intervals

2000

4000

12,000

12,000

NA

Configured Call Types

8000

8000

15,000

15,000

15,000

Call Type Skill Group per Interval 37

70,000

70,000

70,000

70,000

NA

Active Routing Scripts

1000

2000

6000

6000

6000

Configured Routing Scripts

2000

4000

12,000

12,000

12,000

Network VRU Scripts

2000

4000

12,000

12,000

12,000

System-wide Maximum Configured Reason Codes and Labels

2800, plus 21 system-defined

3800, plus 21 system-defined

7800, plus 21 system-defined

7800, plus 21 system-defined

NA

Not-ready Reason Codes

100 global codes

100 associated reason codes for each team

500 configured team reason codes

100 global codes

100 associated reason codes for each team

1000 configured team reason codes

100 global codes

100 associated reason codes for each team

3000 configured team reason codes

100 global codes

100 associated reason codes for each team

NA

Sign-out Reason Codes

100 global codes

100 associated reason codes for each team

500 configured team reason codes

100 global codes

100 associated reason codes for each team

1000 configured team reason codes

100 global codes

100 associated reason codes for each team

3000 configured team reason codes

100 global codes

100 associated reason codes for each team

NA

Wrap-up Reason labels 38

100 global labels

1500 team labels

100 global labels

1500 team labels

100 global labels

1500 team labels

100 global labels

1500 team labels

NA

Administration Bulk Jobs 39

200

200

200

200

NA

CTI AllEventClients 40

7/Medium PG

20/Large PG 41

7/Medium PG

20/Large PG 42

7/Medium PG

20/Large PG 43

7/Medium PG

20/Large PG

NA

Real-Time Only Distributors (for configuration only)

4 (2 on each side)

4 (2 on each side)

10 (5 on each side)

10 (5 on each side)

10 (5 on each side)

Agent Targeting Rule (ATR)

1000

1000

1000

1000

The following table lists the configuration limits for adding external machines in the Packaged CCE deployments.

External Machines

2000 Agent Reference Design Model

4000 Agent Reference Design Model

12000 Agent Reference Design Model

Main Site

Remote Site

Main Site

Remote Site

Main Site

Remote Site

Gateways

0 or more

0 or more

0 or more

0 or more

0 or more

0 or more

Customer Collaboration Platform

0 or 1

None

0 or 1

None

0 or 1

None

Cisco Unified CVP Reporting

0 or 1

0 or 1

0 or 1

0 or more

0 or 1

0 or more

Cisco Enterprise Chat and Email (ECE)

0 or 1

4 44

0 or 1

0 or more

0 or 1

0 or more

Third-party Multichannel

0 or 1

4 45

0 or 1

0 or more

0 or 1

0 or more

## Feature Availability for
                        	 Reference Designs

These sections summarize the features available in contact center solutions that follow the Contact Center Enterprise
                                 						Reference Designs .

### Agent and
                           	 Supervisor

Capability

Supported

Notes

Call Flows

Post-route by CVP

Comprehensive call flow:

Inbound and outbound calls

Supplementary services

Hold and resume

Blind, consult, and refer transfers
                                                      												and conferences

Router requery

Outbound
                                          					 campaigns

Cisco
                                          					 Outbound Option supports these dialing modes:

Predictive

Preview

Direct Preview

Progressive

The SIP
                                          					 Dialer uses the UDP transfer protocol for SIP.

Mobile
                                          					 Agent

Nailed-up
                                          					 and Call-by-call modes

Silent
                                          					 Monitoring

Unified
                                          					 CM-based (BiB)

You cannot monitor mobile agents with
                                          								Unified CM-based silent monitoring.

Recording

Unified
                                          					 CM-based

Network-based Recording

CUBE(E)-based

TDM
                                          					 gateway-based

CRM
                                          					 Integration

CRM
                                          					 integration is available through the Cisco Finesse Web API, Finesse gadgets,
                                          					 and existing CRM connectors.

You can
                                          					 integrate with a CRM using the following methods:

CRM
                                                						  iFrame in the Finesse container. This method is simple and easy but does not
                                                						  provide deep CRM integration.

Third-party gadget in the Finesse container. This method
                                                						  achieves full CRM integration but requires custom development using third-party
                                                						  and Finesse APIs.

Finesse gadgets in a CRM browser-based desktop. This method provides
                                                						  lightweight integration into the CRM application.

Finesse Web API s or the CTI Server protocol to integrate into a CRM
                                                						  application. This method provides deep CRM integration but requires custom
                                                						  development.

Desktop

Cisco
                                          					 Finesse

Finesse IP
                                          					 Phone Agent

FIPPA only
                                          					 supports a subset of Finesse's features.

Desktop
                                          					 Customization

Cisco
                                          					 Finesse API

### Voice and
                           	 Infrastructure

Capability

Supported

Notes

Music on
                                          					 Hold

Unicast with Unified CM subscriber or voice gateway

Multicast
                                          					 using voice gateway

Proxy / CUSP

SIP Proxy
                                          					 is an optional component.

Instead of using CUSP , some deployments can achieve High Availability (HA) and load balancing using these solution components:

Time
                                                						  Division Multiplexing (TDM) gateway and Unified CM, which use the SIP Options
                                                						  heartbeat mechanism to perform HA.

Unified CVP servers, which use the SIP server group and SIP Options heartbeat
                                                						  mechanism to perform HA and load balancing.

Outbound Option. The Outbound dialer can connect to only one
                                                						  physical gateway, if SIP proxy is not used.

Ingress
                                          					 Gateways

See the Compatibility Matrix for your solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for the supported hardware.

Protocol

Session
                                          					 Initiation Protocol (SIP) over Transmission Control Protocol (TCP)

Session Initiation Protocol (SIP) over
                                          								User Datagram Protocol (UDP) for Outbound Option SIP Dialer to
                                          								egress voice gateway. All subsequent transfers to endpoints must use
                                          								SIP TCP.

Secure SIP
                                          					 to SIP signaling

Contact center enterprise solutions do
                                          								not support H.323.

You can use SIP over UDP only for the Outbound Dialer.

From the Outbound Option SIP Dialer to
                                          								the egress gateway has to use UDP.

Codec

For VRU: G.711 mu-law and G.711 a-law

For voice agents: G.711 mu-law, G.711 a-law, G.729, and G.729a

For video:

Video
                                                						  track: H.264

Contact center enterprise solutions do
                                          								not support iSAC or iLBC.

Mixed
                                          					 codecs for Mobile Agent. Remote and Local ports must use the same codec.

Mixed
                                          					 codecs for CVP prompts. CVP prompts must all use the same codec.

Media
                                          					 Resources

Gateway or Unified CM based:

Conference bridges

Transcoders and Universal Transcoders

Hardware and IOS Software Media Termination Points

For Unified CM-based resources,
                                          								appropriately size Unified CM for this load.

### IP Phone
                           	 Support

For a list of supported phones, see the Compatibility Matrix for your solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . Supported phones need the Built-In-Bridge (BIB), CTI-controlled features under SIP line side.

SCCP-based line side protocol is not supported in newer phones.

### Administration
                           	 Interfaces

Capability

Supported

Notes

Core Component Provisioning

Gateways - CLI

Unified CVP - Web-based Packaged CCE Administration

Unified CCE - Web-based administration and thick client configuration tools

Unified CCMP for Unified CCE solutions

Cisco VVB - Web-based Packaged CCE Administration and operations console

Unified CM - Web-based administration

Cisco Finesse - Web-based Packaged CCE Administration

Unified Intelligence Center - Web-based administration

For provisioning, Packaged CCE does not support CCMP or CCDM.

Service
                                          					 Creation Environment

Unified
                                          					 CCE Internet Script Editor

Unified
                                          					 CCE Script Editor

CVP Call
                                          					 Studio

Serviceability

Cisco
                                          					 Prime Collaboration - Assurance

Unified
                                          					 System Command Line Interface (CLI)

RTMT
                                          					 Analysis Manager Diagnosis

SNMP

syslog

Contact
                                          					 center enterprise solutions do not support RTMT Analysis Manager Analyze Call
                                          					 Path.

Finesse supports RTMT only for log collection.

### VRU and
                           	 Queueing

This table lists the
                              		VRU and call queuing features that optimize inbound call management.

Capability

Supported

Notes

Voice
                                          					 Response Unit (VRU)

Unified
                                          					 CVP Comprehensive Model Type 10

Caller
                                          					 Input

DTMF -
                                          					 RFC2833

Automatic
                                          					 Speech Recognition and Text-to-speech (ASR/TTS)

Video

CVP and
                                          					 Video Basic

CVP Video
                                          					 in Queue

CVP Media
                                          					 Server

The CVP
                                          					 Media Server uses the third-party Microsoft Internet Information Services
                                          					 (IIS). The CVP installer adds the CVP Media Server coresident on the Unified
                                          					 CVP Server.

### Reporting

Capability

Supported

Notes

Reporting
                                          					 tools

Cisco
                                          					 Unified Intelligence Center

Third-party
                                          								reporting applications

Custom reporting

For
                                          								Packaged CCE, Exony VIM is supported for reporting only. Packaged
                                          								CCE does not support Exony VIM provisioning features.

Database
                                          					 sources

Unified
                                          					 CCE AW-HDS-DDS

Unified
                                          					 CCE Live Data

Unified
                                          					 CVP Reporting

For a typical 1000 agent deployment with an average rate of 8 calls per second, the retention period is approximately 24 months.
                                          For a longer retention period, install an external HDS.

To size the needs for your deployment, use the DB Estimator tool in the ICMDBA tool.

Database Integration

CVP Database Element

Unified CVP VXML Server  supports connections to third-party Microsoft SQL Server databases.

Retention

All contact center enterprise solutions
                                          								have a fixed retention size for the AW-HDS-DDS. For more retention,
                                          								you need an external HDS-DDS node. Use the DB Estimator Tool in the
                                          								ICMDBA tool to calculate the vDisk size based on your solution
                                          								sizing and customer retention requirements. The DB vDisk of the
                                          								AW-HDS-DDS can be custom-sized when you deploy the OVA.

A 2000 Agent Reference Design can have up to 4 external HDS.

For more information about the HDS sizing, see the Cisco Collaboration Virtualization page for your solution at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

Report
                                          					 capacities

Two hundred Unified Intelligence Center users can concurrently run:

Two real-time reports with 100 rows per report, with 10 columns each.

Two historical reports with 2000 rows, with 10 columns each.

Two live data reports with 100 rows, with 10 columns each. (Adjust this based on the deployment type whether LD runs or not).

This is applicable for both Unified CCE and Packaged CCE solutions.

Do not run more than ten concurrent reports on any client machine. This is a combined limit for reports that run on the Unified
                                                            Intelligence Center User Interface, Permalinks, and Dashboards on the client machine.

However, you cannot run ten concurrent reports for the 200 maximum reporting users on each node.

You have fewer reporting users on a node, they can run proportionally more reports. But, no client machine can exceed the
                                                            ten report limit.

In addition, 30 users each running one real-time XML permalink and one historical XML permalink is supported. (This results
                                          in approximately 7200 real-time XML permalink executions per hour and 60 Historical XML permalink executions per hour.)

The real-time reports have the capacity of 100 rows per report, with 10 columns each and the historical reports have the capacity
                                          of 2000 rows, with 10 columns each.

### Third-Party
                           	 Integrations

Option

Notes

Recording

Recording
                                          					 Methods:

CUCM-based (BiB)

Network-based Recording

CUBE
                                                						  Forking

Optionally, you can use a third-party recording server integration.

Wallboards

Wallboard
                                          					 provide real-time monitoring of your service to customers. They display
                                          					 information on customer service metrics, such as number of calls waiting,
                                          					 waiting call length, and service levels.

Workforce
                                          					 Management

WFM allows
                                          					 the scheduling of multiple Contact Service Queue (CSQs) and sites.

You can
                                          					 use a single WFM implementation worldwide.

Cisco
                                          					 Solution Plus

Refer to the Cisco Solution Plus
                                          								program for supported options.

Automated
                                          					 Call Distributor (ACD)

You cannot
                                          					 use a third-party ACD in a Reference Design.

| Note | The first four chapters of this book are for anyone who wants to get familiar with the contact center enterprise solutions: Packaged Contact Center Enterprise Unified Contact Center Enterprise For information about design considerations and guidelines specific to Packaged CCE , see the remaining chapters. |
|---|---|

| Important | Your contact center enterprise solution can only use the new higher configuration limits with the standard three coresident
                                       PG layout. |
|---|---|

| Note | The figures in the Contact Director column refer to what are configured on the Contact Director. The figures do not include
                                             what is configured on the target systems to which the Contact Director connects. |
|---|---|

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Active Agents 1 | 2000 | 4000 | 12,000 | 24,000 | 24,000 (cumulative on 3 target systems) |
| Active Agents on each Unified CM cluster | 2000 | 4000 | 8000 | 8000 | NA |
| Configured Agents | 12,000 | 24,000 | 72,000 | 72,000 | NA |
| Configured Agents per PG | 12000 | 12000 | 12000 | 12000 | NA |
| Agents with TraceON enabled | 100 | 100 | 400 | 400 | NA |
| Agent Desk Settings | 2000 | 4000 | 12,000 | 12,000 | NA |
| Active Mobile Agents per Agent PG 2 3 | 2000 with nailed-up connections Or 1500 with call-by-call connections | 2000 with nailed-up connections Or 1500 with call-by-call connections | 2000 with nailed-up connections Or 1500 with call-by-call connections | 2000 with nailed-up connections Or 1500 with call-by-call connections | NA |
| Active ECE Multimedia Agents | 1500 4 | 4000 5 | 12,000 6 | 24,000 7 | NA |
| Agents per team | 50 | 50 | 50 | 50 | NA |
| Teams to which an agent can belong | 1 | 1 | 1 | 1 | NA |
| Skills per agent | 15 Refer to the section on dynamic sizing for details. | 15 Refer to the section on dynamic sizing for details. | 15 Refer to the section on dynamic sizing for details. | 10 Refer to the section on dynamic sizing for details. | NA |
| Number of agents in a skill group | 12,000 | 24,000 | 72,000 | 72,000 | NA |
| Attributes per agent | 50 | 50 | 50 | 50 | NA |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | Unified CCE 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Active Supervisors 8 | 200 | 400 | 1200 | 2400 9 | NA |
| Configured Supervisors | 1200 | 2400 | 7200 | 7200 | NA |
| Active teams | 200 | 400 | 1200 | 2400 | NA |
| Configured teams | 1200 | 2400 | 7200 | 7200 | NA |
| Supervisors per Team | 20 | 20 | 20 | 20 | NA |
| Teams per supervisor | 20 | 20 | 20 | 20 | NA |
| Agents per supervisor | 1000 | 1000 | 1000 | 1000 | NA |
| Active Cisco Unified Intelligence Center Reporting users | 200 | 400 | 1200 10 | 1200 11 | NA |
| Configured Cisco Unified Intelligence Center Reporting users | 1200 | 2400 | 7200 | 7200 | NA |
| Reporting users per CUIC node | 100 | 200 | 200 | 200 | NA |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Active Administrators per distributor 12 | 50 | 50 | 50 | 50 | 50 |
| Configured Web Administrators | 100 | 100 | 100 | 100 | NA |
| Roles—Packaged CCE only | 30 | 30 | 30 | NA | NA |
| Departments—Packaged CCE only | 200 | 200 | 200 | NA | NA |
| Department per Administrator—Packaged CCE only | 10 | 10 | 10 | NA | NA |
| Machines in inventory | 1000 | 1000 | 1000 | 1000 | NA |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Outbound dialer per system | 1 per Agent PG | 1 per Agent PG | 1 per Agent PG | 1 per Agent PG | NA |
| Outbound dialer maximum calls per second | 60 | 120 | 240 | 240 | NA |
| Outbound dialer maximum calls per second per dialer 13 | 60 | 60 | 60 | 60 | NA |
| Outbound dialer maximum ports on each SIP dialer | 3000 | 3000 | 3000 | 3000 | NA |
| Outbound dialer maximum ports on each system (total) | 3000 | 6000 | 12000 | 12000 | NA |
| Number of Preview Campaigns per System | 1500 campaigns Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM. | 1500 campaigns Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM. | 1500 campaigns Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM. | 1500 campaigns Preview and Direct Preview modes support up to 750 campaign skill groups on a Medium PG VM and 1500 campaign skill groups
                                             on a Large PG VM. | NA |
| Number of Predictive Campaigns per system (Agent or VRU based) | 375 | 750 | 1500 | 1500 |  |
| Campaign skill groups per Campaign | 20 | 20 | 20 | 20 | NA |
| Predictive Campaign Skill Groups per Peripheral | 375 | 375 | 375 | 375 | NA |
| Maximum Outbound Skills per Agent | 5 | 5 | 5 | 5 | NA |
| Do Not Call Records per Import | 1,000,000 | 20,000,000 | 60,000,000 | 60,000,000 | NA |

| Note | Each Precision Queue has an associated Skill Group. Each Precision Queue effectively has a weight of two Skill Groups. |
|---|---|

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Skill Groups per System | 16,000 14 | 16,000 | 27,000 | 48,000 | 54,000 |
| Enterprise Skill Groups | 4000 | 4000 | 4000 | 4000 | 4000 |
| Maximum combined configured Skill Groups and Precision Queues per peripheral | 4000 | 4000 | 4000 | 4000 | NA |
| Configured Precision Queues per system | 4000 15 | 4000 16 | The smaller of: 4000 Or 27,000 divided by the number of agent peripherals | The smaller of: 4000 Or 48,000 divided by the number of agent peripherals | 8000 of the maximum 54,000 queues |
| Precision Queue steps | 10,000 | 10,000 | 10,000 | 10,000 | NA |
| Precision Queue term per Precision Queue | 10 | 10 | 10 | 10 | NA |
| Precision steps per Precision Queue | 10 | 10 | 10 | 10 | NA |
| Unique attributes per Precision Queue | 10 | 10 | 10 | 10 | NA |
| Max Unique Skills per Team | 50 | 50 | 50 | 50 | NA |
| Configured labels | 100,000 | 100,000 | 160,000 | 160,000 | 160,000 |
| Precision Routing Attributes on each system | 10,000 | 10,000 | 10,000 | 10,000 | NA |
| Precision Routing Attributes for each Agent | 50 | 50 | 50 | 50 | NA |
| Skill Group statistics refresh rate | 10 seconds (default) | 10 seconds (default) | 10 seconds (default) | 10 seconds (default) | NA |
| Skill Groups per PG | 4000 | 4000 | 4000 | 4000 | NA |
| Queues 17 per Contact Sharing Group | NA | NA | NA | NA | 100 |
| Contact Sharing Rules | NA | NA | NA | NA | 100 |
| Contact Sharing Groups | NA | NA | NA | NA | 1000 |

| Resource | 2000 Agent Reference Design | 4000 Agent Reference Design | 12000 Agent Reference Design | 24000 Agent Reference Design | Contact Director Reference Design |
|---|---|---|---|---|---|
| Maximum active agents assigned to tasks per system | 2000 | 2000 | 2000 | 2000 | NA |
| Maximum reserved and active tasks per agent 18 | 15 | 15 | 15 | 15 | NA |
| Maximum incoming tasks/sec across all MRDs 19 | 5 | 5 | 5 | 5 | NA |
| Task Routing API request/hr through Customer Collaboration Platform | 15,000 | 15,000 | 15,000 | 15,000 | NA |

| Resource | 2000 Agent Reference Design | 4000 Agent Reference Design | 12000 Agent Reference Design | 24000 Agent Reference Design | 36000 Agent Reference Design |
|---|---|---|---|---|---|
| Maximum active omnichannel agents assigned to tasks | 2000 | 4000 | 4000 | 4000 | 4000 |
| Maximum reserved and active tasks per agent 20 | 15 | 15 | 15 | 15 | 15 |
| Maximum incoming tasks/sec across all MRDs for digital channels | 8 | 15 | 15 | 15 | 15 |
| Maximum tasks and voice calls per second | 18 | 35 | 105 | 105 | 105 |

| Note | In the Global topology, each remote site can support the full limit of Dialed Numbers as mentioned in the table. |
|---|---|

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Dialed Numbers on each CVP peripheral (External Voice and Post Call Survey ) 21 | 4000 | 4000 | 12,000 | 12,000 | 12,000 |
| Dialed Number on each Unified CM peripheral (Internal Voice) | 2000 | 2000 | 2000 | 2000 | NA |
| Dialed Number on each MR peripheral (Multichannel) | 1000 | 1000 | 1000 | 1000 | NA |
| Dialed Number on each Unified CM peripheral (Outbound Voice) | 1000 | 1000 | 1000 | 1000 | NA |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| VRU Ports in a Reference Layout 22 23 | 3000 | 6000 | 18,000 | 36,000 | 36,000 |
| Maximum VRU Ports with Added PGs 24 | 6000 | 12,000 | 36,000 | 48,000 | 72,000 |
| Maximum Inbound Calls per Second (CPS) | 15 | 30 | 90 | 90 | 300 , of which Contact Sharing can handle 120 and the remainder is for self-service and line-of-business direct routing. |
| Congestion Control CPS 25 | 18 | 35 | 105 | 105 | 300 |
| Maximum Inbound CPS per VRU PG 26 | 15 | 15 | 15 | 15 | NA |
| Maximum VRU PIM per VRU PG | 2 | 2 | 2 | 2 | NA |
| Dynamic Reskilling (operations/hr.) | 7200 | 7200 | 7200 | 7200 | NA |
| Maximum Queued Calls and Tasks | 15,000 | 15,000 | 15,000 | 15,000 27 | 15,000 |
| Media Routing Domains per system | 20 | 20 | 20 | 20 | NA |
| Agent Callback requests through Customer Collaboration Platform (requests/hr.) | 1000 | 1000 | 1000 | 1000 | NA |
| ECE Email or Chat requests per hour for 400 agent deployment | 6 per agent | 6 per agent | 6 per agent | 6 per agent | NA |
| ECE Email or Chat requests per hour for 1500 agent deployment 28 | 6 per agent | 6 per agent | 6 per agent | 6 per agent | NA |
| Incoming Messages per Second for CVP Reporting Server | 420 | 420 | 420 | 420 | 420 |
| Reports per user For more details, see Resource Requirements for Reporting | 2 Live Data reports 2 AW-RealTime reports 2 historical reports | 2 Live Data reports 2 AW-RealTime reports 2 historical reports | 2 Live Data reports 2 AW-RealTime reports 2 historical reports | 2 Live Data reports 2 AW-RealTime reports 2 historical reports | NA |
| Maximum rows per report 29 | 3000 for real-time 8000 for historical | 3000 for real-time 8000 for historical | 3000 for real-time 8000 for historical | 3000 for real-time 8000 for historical | NA |
| Configured Business Hour Objects | 1000 | 1000 | 1000 | 1000 | 1000 |
| Configured Schedule Objects per Business Hours Object 30 | 50 | 50 | 50 | 50 | 50 |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Persistent Enabled Expanded Call Variables (Default) 31 | 5 | 5 | 5 | 5 | 5 |
| Persistent Enabled Expanded Call Variable Arrays | 0 | 0 | 0 | 0 | 0 |
| Maximum Contents per ECC (Expanded Call Context) Variable (bytes) | 210 | 210 | 210 | 210 | 210 |
| Maximum Total ECC Contents Size per ECC Payload (bytes) | 2000 | 2000 | 2000 | 2000 | 2000 |
| Maximum ECC Variable Name (bytes without null character) | 32 | 32 | 32 | 32 | 32 |
| Maximum Total Contents and Name Size for ECC Variables per ECC Payload (bytes) | 2500 | 2500 | 2500 | 2500 | 2500 |
| Maximum ECC Variables Contents per Call (bytes) | 6000 | 6000 | 6000 | 6000 | 6000 |
| Maximum System-wide ECC Variable Contents (bytes) 32 | 90,000,000 | 90,000,000 | 90,000,000 | 90,000,000 | NA |
| Number of Peripheral Variables | 10 | 10 | 10 | 10 | 10 |
| Call Context for Peripheral Variables 1-10 (bytes) | 40 | 40 | 40 | 40 | 40 |

| Resource | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model | 24000 Agent Reference Design Model | Contact Director Reference Design Model |
|---|---|---|---|---|---|
| Maximum Agent PGs with Live Data, Precision Queueing, or Single Sign-On enabled 33 | 4 34 | 4 12 (when using the 12000 agents Live Data OVA) | 12 24 (when using the 24000 agents Live Data OVA) | 24 | 50 |
| Maximum PGs 35 | 30 | 100 | 150 | 150 | NA |
| Maximum Agent PGs on each VM | 1 | 1 | 1 | 1 | NA |
| Maximum Cisco Finesse server pairs per PG pair 36 | 2 | 2 | 2 | 2 | NA |
| MR PIMs on each MR PG | 4 | 4 | 4 | 4 | NA |
| Custom Application Gateway | 20 | 20 | 20 | 20 | 20 per enterprise system |
| Bucket Intervals | 2000 | 4000 | 12,000 | 12,000 | NA |
| Configured Call Types | 8000 | 8000 | 15,000 | 15,000 | 15,000 |
| Call Type Skill Group per Interval 37 | 70,000 | 70,000 | 70,000 | 70,000 | NA |
| Active Routing Scripts | 1000 | 2000 | 6000 | 6000 | 6000 |
| Configured Routing Scripts | 2000 | 4000 | 12,000 | 12,000 | 12,000 |
| Network VRU Scripts | 2000 | 4000 | 12,000 | 12,000 | 12,000 |
| System-wide Maximum Configured Reason Codes and Labels | 2800, plus 21 system-defined | 3800, plus 21 system-defined | 7800, plus 21 system-defined | 7800, plus 21 system-defined | NA |
| Not-ready Reason Codes | 100 global codes 100 associated reason codes for each team 500 configured team reason codes | 100 global codes 100 associated reason codes for each team 1000 configured team reason codes | 100 global codes 100 associated reason codes for each team 3000 configured team reason codes | 100 global codes 100 associated reason codes for each team | NA |
| Sign-out Reason Codes | 100 global codes 100 associated reason codes for each team 500 configured team reason codes | 100 global codes 100 associated reason codes for each team 1000 configured team reason codes | 100 global codes 100 associated reason codes for each team 3000 configured team reason codes | 100 global codes 100 associated reason codes for each team | NA |
| Wrap-up Reason labels 38 | 100 global labels 1500 team labels | 100 global labels 1500 team labels | 100 global labels 1500 team labels | 100 global labels 1500 team labels | NA |
| Administration Bulk Jobs 39 | 200 | 200 | 200 | 200 | NA |
| CTI AllEventClients 40 | 7/Medium PG 20/Large PG 41 | 7/Medium PG 20/Large PG 42 | 7/Medium PG 20/Large PG 43 | 7/Medium PG 20/Large PG | NA |
| Real-Time Only Distributors (for configuration only) | 4 (2 on each side) | 4 (2 on each side) | 10 (5 on each side) | 10 (5 on each side) | 10 (5 on each side) |
| Agent Targeting Rule (ATR) | 1000 | 1000 | 1000 | 1000 | NA |

| External Machines | 2000 Agent Reference Design Model | 4000 Agent Reference Design Model | 12000 Agent Reference Design Model |
|---|---|---|---|
|  | Main Site | Remote Site | Main Site | Remote Site | Main Site | Remote Site |
| Gateways | 0 or more | 0 or more | 0 or more | 0 or more | 0 or more | 0 or more |
| Customer Collaboration Platform | 0 or 1 | None | 0 or 1 | None | 0 or 1 | None |
| Cisco Unified CVP Reporting | 0 or 1 | 0 or 1 | 0 or 1 | 0 or more | 0 or 1 | 0 or more |
| Cisco Enterprise Chat and Email (ECE) | 0 or 1 | 4 44 | 0 or 1 | 0 or more | 0 or 1 | 0 or more |
| Third-party Multichannel | 0 or 1 | 4 45 | 0 or 1 | 0 or more | 0 or 1 | 0 or more |

| Capability | Supported | Notes |
|---|---|---|
| Call Flows | Post-route by CVP Comprehensive call flow: Inbound and outbound calls Supplementary services Hold and resume Blind, consult, and refer transfers
                                                      												and conferences Router requery |  |
| Outbound
                                          					 campaigns | Cisco
                                          					 Outbound Option supports these dialing modes: Predictive Preview Direct Preview Progressive | The SIP
                                          					 Dialer uses the UDP transfer protocol for SIP. |
| Mobile
                                          					 Agent | Nailed-up
                                          					 and Call-by-call modes |  |
| Silent
                                          					 Monitoring | Unified
                                          					 CM-based (BiB) | You cannot monitor mobile agents with
                                          								Unified CM-based silent monitoring. |
| Recording | Unified
                                          					 CM-based Network-based Recording CUBE(E)-based TDM
                                          					 gateway-based |  |
| CRM
                                          					 Integration | CRM
                                          					 integration is available through the Cisco Finesse Web API, Finesse gadgets,
                                          					 and existing CRM connectors. | You can
                                          					 integrate with a CRM using the following methods: CRM
                                                						  iFrame in the Finesse container. This method is simple and easy but does not
                                                						  provide deep CRM integration. Third-party gadget in the Finesse container. This method
                                                						  achieves full CRM integration but requires custom development using third-party
                                                						  and Finesse APIs. Finesse gadgets in a CRM browser-based desktop. This method provides
                                                						  lightweight integration into the CRM application. Finesse Web API s or the CTI Server protocol to integrate into a CRM
                                                						  application. This method provides deep CRM integration but requires custom
                                                						  development. |
| Desktop | Cisco
                                          					 Finesse Finesse IP
                                          					 Phone Agent | FIPPA only
                                          					 supports a subset of Finesse's features. |
| Desktop
                                          					 Customization | Cisco
                                          					 Finesse API |  |

| Capability | Supported | Notes |
|---|---|---|
| Music on
                                          					 Hold | Unicast with Unified CM subscriber or voice gateway Multicast
                                          					 using voice gateway |  |
| Proxy / CUSP | SIP Proxy
                                          					 is an optional component. | Instead of using CUSP , some deployments can achieve High Availability (HA) and load balancing using these solution components: Time
                                                						  Division Multiplexing (TDM) gateway and Unified CM, which use the SIP Options
                                                						  heartbeat mechanism to perform HA. Unified CVP servers, which use the SIP server group and SIP Options heartbeat
                                                						  mechanism to perform HA and load balancing. Outbound Option. The Outbound dialer can connect to only one
                                                						  physical gateway, if SIP proxy is not used. |
| Ingress
                                          					 Gateways | See the Compatibility Matrix for your solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for the supported hardware. |  |
| Protocol | Session
                                          					 Initiation Protocol (SIP) over Transmission Control Protocol (TCP) Session Initiation Protocol (SIP) over
                                          								User Datagram Protocol (UDP) for Outbound Option SIP Dialer to
                                          								egress voice gateway. All subsequent transfers to endpoints must use
                                          								SIP TCP. Secure SIP
                                          					 to SIP signaling | Contact center enterprise solutions do
                                          								not support H.323. You can use SIP over UDP only for the Outbound Dialer. From the Outbound Option SIP Dialer to
                                          								the egress gateway has to use UDP. |
| Codec | For VRU: G.711 mu-law and G.711 a-law For voice agents: G.711 mu-law, G.711 a-law, G.729, and G.729a For video: Video
                                                						  track: H.264 | Contact center enterprise solutions do
                                          								not support iSAC or iLBC. Mixed
                                          					 codecs for Mobile Agent. Remote and Local ports must use the same codec. Mixed
                                          					 codecs for CVP prompts. CVP prompts must all use the same codec. |
| Media
                                          					 Resources | Gateway or Unified CM based: Conference bridges Transcoders and Universal Transcoders Hardware and IOS Software Media Termination Points | For Unified CM-based resources,
                                          								appropriately size Unified CM for this load. |

| Capability | Supported | Notes |
|---|---|---|
| Core Component Provisioning | Gateways - CLI Unified CVP - Web-based Packaged CCE Administration Unified CCE - Web-based administration and thick client configuration tools Unified CCMP for Unified CCE solutions Cisco VVB - Web-based Packaged CCE Administration and operations console Unified CM - Web-based administration Cisco Finesse - Web-based Packaged CCE Administration Unified Intelligence Center - Web-based administration | For provisioning, Packaged CCE does not support CCMP or CCDM. |
| Service
                                          					 Creation Environment | Unified
                                          					 CCE Internet Script Editor Unified
                                          					 CCE Script Editor CVP Call
                                          					 Studio |  |
| Serviceability | Cisco
                                          					 Prime Collaboration - Assurance Unified
                                          					 System Command Line Interface (CLI) RTMT
                                          					 Analysis Manager Diagnosis SNMP syslog | Contact
                                          					 center enterprise solutions do not support RTMT Analysis Manager Analyze Call
                                          					 Path. Finesse supports RTMT only for log collection. |

| Capability | Supported | Notes |
|---|---|---|
| Voice
                                          					 Response Unit (VRU) | Unified
                                          					 CVP Comprehensive Model Type 10 |  |
| Caller
                                          					 Input | DTMF -
                                          					 RFC2833 Automatic
                                          					 Speech Recognition and Text-to-speech (ASR/TTS) |  |
| Video | CVP and
                                          					 Video Basic CVP Video
                                          					 in Queue |  |
| CVP Media
                                          					 Server | The CVP
                                          					 Media Server uses the third-party Microsoft Internet Information Services
                                          					 (IIS). The CVP installer adds the CVP Media Server coresident on the Unified
                                          					 CVP Server. |  |

| Capability | Supported | Notes |
|---|---|---|
| Reporting
                                          					 tools | Cisco
                                          					 Unified Intelligence Center Third-party
                                          								reporting applications Custom reporting | For
                                          								Packaged CCE, Exony VIM is supported for reporting only. Packaged
                                          								CCE does not support Exony VIM provisioning features. |
| Database
                                          					 sources | Unified
                                          					 CCE AW-HDS-DDS Unified
                                          					 CCE Live Data Unified
                                          					 CVP Reporting | For a typical 1000 agent deployment with an average rate of 8 calls per second, the retention period is approximately 24 months.
                                          For a longer retention period, install an external HDS. To size the needs for your deployment, use the DB Estimator tool in the ICMDBA tool. |
| Database Integration | CVP Database Element | Unified CVP VXML Server  supports connections to third-party Microsoft SQL Server databases. |
| Retention | All contact center enterprise solutions
                                          								have a fixed retention size for the AW-HDS-DDS. For more retention,
                                          								you need an external HDS-DDS node. Use the DB Estimator Tool in the
                                          								ICMDBA tool to calculate the vDisk size based on your solution
                                          								sizing and customer retention requirements. The DB vDisk of the
                                          								AW-HDS-DDS can be custom-sized when you deploy the OVA. A 2000 Agent Reference Design can have up to 4 external HDS. For more information about the HDS sizing, see the Cisco Collaboration Virtualization page for your solution at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |  |
| Report
                                          					 capacities | Two hundred Unified Intelligence Center users can concurrently run: Two real-time reports with 100 rows per report, with 10 columns each. Two historical reports with 2000 rows, with 10 columns each. Two live data reports with 100 rows, with 10 columns each. (Adjust this based on the deployment type whether LD runs or not). This is applicable for both Unified CCE and Packaged CCE solutions. Note Do not run more than ten concurrent reports on any client machine. This is a combined limit for reports that run on the Unified
                                                            Intelligence Center User Interface, Permalinks, and Dashboards on the client machine. However, you cannot run ten concurrent reports for the 200 maximum reporting users on each node. You have fewer reporting users on a node, they can run proportionally more reports. But, no client machine can exceed the
                                                            ten report limit. | Note | Do not run more than ten concurrent reports on any client machine. This is a combined limit for reports that run on the Unified
                                                            Intelligence Center User Interface, Permalinks, and Dashboards on the client machine. However, you cannot run ten concurrent reports for the 200 maximum reporting users on each node. You have fewer reporting users on a node, they can run proportionally more reports. But, no client machine can exceed the
                                                            ten report limit. | In addition, 30 users each running one real-time XML permalink and one historical XML permalink is supported. (This results
                                          in approximately 7200 real-time XML permalink executions per hour and 60 Historical XML permalink executions per hour.) The real-time reports have the capacity of 100 rows per report, with 10 columns each and the historical reports have the capacity
                                          of 2000 rows, with 10 columns each. |
| Note | Do not run more than ten concurrent reports on any client machine. This is a combined limit for reports that run on the Unified
                                                            Intelligence Center User Interface, Permalinks, and Dashboards on the client machine. However, you cannot run ten concurrent reports for the 200 maximum reporting users on each node. You have fewer reporting users on a node, they can run proportionally more reports. But, no client machine can exceed the
                                                            ten report limit. |

| Note | Do not run more than ten concurrent reports on any client machine. This is a combined limit for reports that run on the Unified
                                                            Intelligence Center User Interface, Permalinks, and Dashboards on the client machine. However, you cannot run ten concurrent reports for the 200 maximum reporting users on each node. You have fewer reporting users on a node, they can run proportionally more reports. But, no client machine can exceed the
                                                            ten report limit. |
|---|---|

| Option | Notes |
|---|---|
| Recording | Recording
                                          					 Methods: CUCM-based (BiB) Network-based Recording CUBE
                                                						  Forking Optionally, you can use a third-party recording server integration. |
| Wallboards | Wallboard
                                          					 provide real-time monitoring of your service to customers. They display
                                          					 information on customer service metrics, such as number of calls waiting,
                                          					 waiting call length, and service levels. |
| Workforce
                                          					 Management | WFM allows
                                          					 the scheduling of multiple Contact Service Queue (CSQs) and sites. You can
                                          					 use a single WFM implementation worldwide. |
| Cisco
                                          					 Solution Plus | Refer to the Cisco Solution Plus
                                          								program for supported options. |
| Automated
                                          					 Call Distributor (ACD) | You cannot
                                          					 use a third-party ACD in a Reference Design. |