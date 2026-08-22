---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-1270ba63b0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_b_pre-installation-planning-guide-for-cisco_chapter_010.html
retrieved_at: 2026-08-22T00:10:54.233389+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.5(1)

Updated: February 4, 2020

Chapter: Cisco Unified ICM Overview

## Chapter: Cisco Unified ICM Overview

# Cisco Unified ICM Overview

In the initial phase of pre-installation planning, you need to become familiar with the Unified ICM system and understand
                        how it fits into your overall enterprise contact center. You can then determine which products and components you want to
                        deploy in an Unified ICM virtual contact center.

In this chapter,
                        		complete the following pre-installation tasks:

Determine the role of the Unified ICM software in your enterprise. Understand how the Unified ICM software fits into the enterprise
                              contact center and carrier networks.

Choose Unified ICM products. Will your system be a complete pre-routing and post-routing system? Will you have other options
                              such as Unified ICM Gateway SQL, Cisco CTI, or Unified IP IVR?

## How Unified ICME
                        	 Software Works

The Unified ICME
                              		  Edition works with your contact center equipment and the IXC carrier
                              		  network to create a virtual contact center. In the virtual contact center
                              		  model, multiple distributed contact centers link to form one Unified CCE. The
                              		  agents within the Unified CCE become members of a single team that is capable
                              		  of servicing customer contacts throughout the enterprise.

### Unified ICM Call
                           	 Routing

The Unified ICM software makes the best use of your contact handling resources while ensuring that each customer is directed
                                 to the most appropriate resource available. To get an idea of how the Unified ICM software fits into the contact center and
                                 carrier environments, refer the following sections. These sections examine how the Unified ICM software routes telephone calls.

#### Pre-routing

The Unified ICM software executes call routing decisions before a call
                                 terminates at a contact center. This concept is called pre-routing. As shown in
                                 the preceding figure, calls to be routed usually originate in the public
                                 telephone network as calls to a toll-free number (1).

#### The IXC Network

The Unified ICM software is configured in the intelligent network of the
                                 		IntereXchange Carrier (IXC) to receive a route request for each designated
                                 		incoming call (2). A subsystem of the Unified ICM software, called the Network
                                 		Interface Controller (NIC), communicates with the carrier's network
                                 		through an intelligent network interface.

#### Route Requests

The NIC translates the network's description of the call, including
                                 		point of origin, number dialed, and any customer entered digits, into the
                                 		language of the Unified ICM software. The NIC passes this call information to
                                 		the CallRouter in the form of a route request (3).

#### Route Responses

At this point, the Unified ICM software may query an ANI or customer
                                 profile database before returning a route response to the NIC (4). The NIC
                                 passes a destination for the call back to the IXC network. The IXC connects the call and maintains the voice
                                 path.

#### ACDs

Each contact center has one or more Automatic
                                 Call Distributor (ACD) systems that direct incoming calls to the telephone sets
                                 of individual agents (5). The Unified ICM software maintains real-time
                                 communications with the ACDs in each contact center by using a Peripheral
                                 Gateway (PG).

#### Peripheral
                              	 Gateway

The PG communicates
                                 		with the ACD over the switch vendor Computer Telephony Integration (CTI) link
                                 		(6). To make optimal decisions, the Unified ICM software must know the latest
                                 		status for every call, agent, and agent group in its network. One purpose of
                                 		the PG is to extract this status information from the ACD and forward it to the
                                 		CallRouter in-memory database. You can also use the PG as a CTI Server and as a
                                 		communications interface between the Unified ICM and Voice Response Unit (VRU)
                                 		systems located at contact center sites or in the network.

#### Post-routing

In private network
                                 		configurations, ACDs can also originate call routing requests. This is called
                                 		post-routing. Post-routing provides the same intelligence used in pre-Routing,
                                 		but applies it to calls originating from a private network of ACD, PBX, and VRU
                                 		systems. The PG assists in post-routing by forwarding routing requests to the
                                 		Unified ICM software and returning the target destinations to the ACD (7).

#### CTI Server

External server or workstation applications can subscribe with a PG that
                                 		acts as a CTI Server (8). The CTI Server provides call and agent event data
                                 		that can be used in screen-pops and other CTI applications. At the desktop
                                 		level, the Unified ICM CTI desktop provides an environment for integrating
                                 		soft-phone, screen-pop, and data entry at the agent's workstation.

#### Monitoring and Reporting

All event data that the PG and router gathers is forwarded
                                 to the Unified ICM software and stored in an industry-standard relational
                                 database (9). This data is used in real-time monitoring and historical
                                 reporting. You can modify the standard Unified ICM monitoring screens and
                                 reports with Unified ICM-provided database access tools. Optionally, you can
                                 access the data directly with SQL or Open Database Connectivity (ODBC)
                                 tools.

#### Administration & Data Server

An Administration & Data Server (10) monitors and controls the
                                 		overall operation of the Unified ICM software. The Unified ICM software can
                                 		support multiple Administration & Data Servers located throughout the
                                 		contact center network.

## Unified ICM System
                        	 Software Components

Pre-installation
                              		  planning involves many different Unified ICM system software components. You
                              		  may want to familiarize yourself with the role of the components in the Unified
                              		  ICM system.

### CallRouter

The CallRouter is
                                 		  the part of the Unified ICM system that contains the call routing logic. The
                                 		  Unified ICM software receives call routing requests and determines the best
                                 		  destination for each call. It also collects information about the entire
                                 		  system. The Unified ICM software serves as a real-time server by forwarding
                                 		  performance and monitoring information to Administration & Data servers.

### Logger

The Logger is the
                                 		  interface between the Unified ICM software and the database manager (Microsoft
                                 		  SQL Server). The Unified ICM software collects performance and
                                 		  monitoring information about the system and passes the information to the
                                 		  Logger for short-term storage in a central relational database. The Logger
                                 		  forwards historical information to the Historical Data Server (HDS). The HDS on
                                 		  the Logger maintains statistics and data for monitoring and reporting.

### Network Interface Controller (NIC)

The NIC connects the Unified ICM software
                                 to the IXC signaling network. The NIC receives a route request from the
                                 signaling network for each incoming call and passes the request to the Unified
                                 ICM software. The Unified ICM software responds with routing information (a
                                 routing label), which the NIC passes back to the IXC signaling network.

### Peripheral
                           	 Gateways

Each contact center
                                 		  device (ACD, PBX, or VRU) communicates with a Peripheral Gateway (PG). The PG
                                 		  reads status information from the device and passes it back to the Unified ICM
                                 		  software. The PG runs one or more Peripheral Interface Manager (PIM) processes,
                                 		  which are the software components that communicate with proprietary ACD
                                 		  systems. A single PIM is required for each peripheral to which the PG will
                                 		  interface. Therefore, a single PG (and its associated PIMs) can serve multiple
                                 		  peripherals of the same kind. For example, one PG with four Aspect ACD PIMs can
                                 		  serve four Aspect ACDs in the contact center.

A single server can
                                 		  support up to two PGs. For details, refer to the .

### Administration and
                           	 Data Server Control Console

The Administration
                                 		  & Data Server is the human interface to the Unified ICM software. It serves
                                 		  as a control console from which you can monitor agent and contact center
                                 		  activity and change how the Unified ICM software routes calls. For example, you
                                 		  can use the Administration & Data Server to configure the Unified ICM
                                 		  contact center data, create call routing scripts, and monitor and report on the
                                 		  Unified ICM system or some part of the system. Administration & Data
                                 		  Servers can be located anywhere, as long as they have LAN or WAN connections to
                                 		  the Unified ICM software.

Administration &
                                 		  Data Servers have several roles: Administration, Real-time data server,
                                 		  Historical Data Server, and Detail Data Server. A Unified ICM deployment must
                                 		  have Administration & Data Servers to fill these roles. The servers can be
                                 		  deployed in the following combinations to achieve the needed scalability with
                                 		  the minimum number of servers:

Administration
                                       				Server and Real-time Data Server (AW)

Configuration
                                       				only Administration Server

Administration
                                       				Server, Real-time and Historical Data Server and Detail Data Server
                                       				(AW-HDS-DDS)

Administration
                                       				Server and Real-time and Historical Data Server (AW-HDS)

Historical Data
                                       				Server and Detail Data Server (HDS-DDS)

An Administration
                                 		  Client (formerly known as a "client AW" )
                                 		  serves the administration role, but is deployed as a client to an
                                 		  Administration Server for scalability. The Administration Client can view and
                                 		  modify the configuration, and receive real-time reporting data from the
                                 		  Administration & Data Server, but does not store the data itself, and does
                                 		  not have a database. You must install each Administration & Data Server on
                                 		  a separate server for production systems to ensure no interruptions to the
                                 		  real-time call processing of the Call Router and Logger processes. For lab or
                                 		  prototype systems, you can install the Administration & Data Server on the
                                 		  same server as the Call Router and Logger.

### Historical Data
                           	 Server and Detail Data Server

Administration &
                                 		  Data Servers need to access historical data (half hour data, call detail, and
                                 		  so on) for historical reporting in the Script Editor or in third-party tools.
                                 		  You must install at least one real-time Administration & Data Server in a
                                 		  system with a Historical Data Server (HDS) to support reporting and long-term
                                 		  historical data storage. The HDS IP address requirements are identical to those
                                 		  of a standard Administration & Data Server.

The Historical Data Server (HDS) and Detail Data Server (DDS) are used
                                 		  for longer-term historical data storage. The HDS stores historical data
                                 		  summarized in 15 or 30 minute intervals and is used for reporting.

DDS stores detailed information about each call or call segment and is
                                 		  used for call tracing. Data may be extracted from either of these sources for
                                 		  warehousing and custom reporting.

Typically these Data Servers are deployed with a primary AW as a
                                 		  single server serving all three roles (AW-HDS-DDS).

### ICM
                           	 Reporting

The Unified ICM
                                 		  Reporting solution provides a Unified Intelligence Center interface to access
                                 		  data describing the historical and real-time states of the system.

Reporting concepts
                                 		  and data descriptions are described in ;
                                 		  this description is independent of the reporting user interface being used.

#### Cisco Unified
                              	 Intelligence Center

Cisco Unified
                                 		Intelligence Center (Unified Intelligence Center) is an advanced reporting
                                 		product used for Unified CCE and other products. This platform is a web-based
                                 		application offering many Web 2.0 features, high scalability, performance, and
                                 		advanced features such as the ability to integrate data from other Cisco
                                 		Unified Communications products or third-party data sources. Unified
                                 		Intelligence Center incorporates a security model which defines different
                                 		access and capabilities for specific users. Unified Intelligence Center
                                 		Standard is included with Unified ICM. Unified Intelligence Center Premium is
                                 		an optional product with additional features. You must install Unified
                                 		Intelligence Center on a separate server; it cannot be co-resident with other
                                 		Unified ICM components.

For a complete
                                 		description of both Unified Intelligence Center products see .

## ICM Options and
                        	 Related Products

You can set up the
                              		  Unified ICM software with various options. You can add software to
                              		  perform database lookups or perform  secondary call routing after a call terminates at an ACD. In some cases, the Unified
                              ICM software is part of other Cisco contact center products. Review the Unified
                              		  ICM software options and related products to learn about the different ways to deploy the
                              		  Unified ICM software in a Unified CCE.

### Pre-routing

The Unified ICM software uses pre-routing to execute routing decisions
                                 		  before a call terminates at a contact center. With pre-routing, the Network
                                 		  Interface Controller (NIC) receives the route request from the IXC and passes
                                 		  the call information to the Unified ICM software. The Unified ICM software
                                 		  processes the route request through a call routing script, which defines how
                                 		  the call should be routed. The Unified ICM software returns a route response to
                                 		  the NIC, which in turn forwards it to the IXC. The route response contains the
                                 		  call's final destination.

In pre-routing, the Peripheral Gateway's role is to keep the
                                 		  Unified ICM software informed of the real-time status of switches, calls, and
                                 		  agents in the Unified CCE. The Unified ICM software uses this real-time data to
                                 		  make an informed call routing decision.

Pre-Routing systems require the following components:

Network Interface Controller (NIC)

CallRouter

Logger

Administration & Data Server

Peripheral Gateway (PG)

The pre-routing capabilities are enabled through the Network Interface
                                 		  Controller (NIC) and the CallRouter processes. NICs are implemented as software
                                 		  on the Unified ICM software platform (for example, on the CallRouter or Logger
                                 		  machines).

The Unified ICM routes calls within the public network based on
                                 		  several dynamic variables. You can use any combination of the following
                                 		  variables to route calls:

Agent availability

Day of week

Agent skills

Number dialed

Caller-entered digits

Origin of call

Cost of the call

Cost of the transaction

Customer database lookup

Scheduled agents

Customer-defined business rules

Time of day

Calls are routed in the most efficient manner possible given the
                                 		  current contact center load conditions.

### Post-routing

In a traditional
                                 		  time-division multiplexing (TDM) environment, post-routing systems have
                                 		  software that allows the CallRouter to make secondary routing decisions after a
                                 		  call is received at a contact center. In post-routing, the ACD or VRU submits a
                                 		  route request to the Unified ICM software. The Unified ICM software executes
                                 		  scripts to process the routing request and return a destination address to the
                                 		  ACD. The Unified ICM software then directs the ACD to transfer the call to an
                                 		  agent, skill group, or service, either in the same contact center or at a
                                 		  different contact center. In making a post-routing decision, the Unified ICM
                                 		  software can use the same information and script it uses in pre-routing. In
                                 		  other words, the same call routing intelligence that is used in the pre-routing
                                 		  of calls is applied to calls that are interflowed between contact center sites,
                                 		  transferred between agents, or transferred into or out of VRU's.

### Pre- and Post-routing Systems

A pre- and post-routing Unified ICM system is a
                                 complete intelligent call routing, monitoring, and reporting system. The
                                 Unified ICM software can execute routing decisions before a call terminates at
                                 a contact center. It can also make secondary routing decisions after a call is
                                 received at a contact center. You can expand a Pre- and post-routing system
                                 with optional features such as Unified ICM Application Gateway, Unified ICM
                                 Gateway SQL, Unified ICM IVR interface, and CTI Server to create an intelligent
                                 call routing and management solution in which all the elements of the Unified
                                 CCE play a role in intelligent routing.

### Computer Telephony
                           	 Integration (CTI)

Cisco CTI software
                                 		  provides an interface between the Unified ICM software and agent desktop and
                                 		  server applications. The CTI software works with a PG's ACD and IVR
                                 		  interface software and all associated ACDs to track events and transactions and
                                 		  forward call- and transaction-related data to an agent's desktop computer.

The CTI software has
                                 		  full third-party call control features that allow agents and integrated desktop
                                 		  applications to perform tasks such as transferring calls, conferencing calls,
                                 		  and setting call data all within an enterprise framework. An agent at the
                                 		  desktop can transfer voice and data in the form of a screen-pop among agents
                                 		  and across different ACD platforms. This allows customer and transaction data
                                 		  to accompany a call from an IVR or web server to the agent and from
                                 		  site-to-site as required. The Unified ICM system can also use CTI data to
                                 		  determine call destinations based on factors such as customer value, business
                                 		  objectives, market penetration, and personalized service.

#### CTI Server

CTI Server, the basic
                                 		server component of Cisco CTI, enables the Unified ICM software to deliver
                                 		agent, call, and customer data in real-time to a server and/ or workstation
                                 		application as events occur throughout the life of a call. The CTI Server is a
                                 		software process that runs on a Peripheral Gateway (PG).

It is a gateway into
                                 		the Unified ICM software data and services.

Pre-route
                                       			 indications identify a caller and provide associated attributes to applications
                                       			 while the call is still in the public or private network and before the caller
                                       			 is connected to an agent, web server or VRU.

Call events are
                                       			 provided throughout all stages of the call flow, from the moment a call arrives
                                       			 at an answering location (ACD, PBX, VRU, web server) until the caller hangs up.

Agent work state
                                       			 changes are reported as they occur.

#### Cisco CTI Object Server (CTIOS)

CTI Object Server (CTIOS) is a high-performance,
                                 scalable, fault-tolerant server-based solution for deploying CTI applications.
                                 It serves as a single point of integration for third-party applications,
                                 including Customer Relationship Management (CRM) systems, data mining, and
                                 workflow solutions.

CTIOS is a client of CTI Server and has a
                                 single all-events connection to Cisco CTI Server. In turn, CTIOS accepts client
                                 connections using session, agent, and call interfaces. These interfaces are
                                 implemented in .NET, COM, Java, and C++, allowing for a wide range of
                                 application development uses. The interfaces are used for call control, to
                                 access data values, and to receive event notifications.

CTIOS
                                 configuration and behavior information is managed at the CTIOS server,
                                 simplifying customization, updates, and maintenance. You can access and manage
                                 the servers remotely. Thin-client and browser-based applications that do not
                                 require Cisco software on the desktop can be developed and deployed with CTIOS.

CTIOS incorporates the following major
                                 components:

CTIOS Toolkit

Client Interface Library

CTIOS Combo Desktop for
                                       Agents and Supervisors

### VRU
                           	 Interface

The Voice Response
                                 		  (VRU) interface software runs on a PG platform. It allows the Cisco Unified ICM
                                 		  software to route calls to targets on VRU's and collect data from VRU's for use
                                 		  in call routing, real-time monitoring, and historical reporting.

The VRU interface
                                 		  can also provide queuing at a network-based or premises-based VRU. With this
                                 		  feature, calls can be directed to an VRU queue when no other appropriate
                                 		  answering resource is available. The VRU interface is not specific to a
                                 		  particular VRU system or manufacturer. It is based on an open VRU model. Many
                                 		  VRU systems support Cisco's Open VRU Interface Specification, including Unified
                                 		  CVP.

The Cisco Customer
                                 		  Voice Portal integrates with both traditional time-division multiplexing (TDM)
                                 		  and IP-based contact centers to provide a call-management and call-treatment
                                 		  solution with a self-service VRU option that can use information available to
                                 		  customers on the corporate Web server. With support for automated speech
                                 		  recognition (ASR) and text-to-speech (TTS) capabilities, callers can obtain
                                 		  personalized information and can conduct business without interacting with a
                                 		  live agent.

For a list of VRU's
                                 		  that support this interface, contact your Cisco representative.

### ICM Application Gateway

The Cisco Unified ICM Application Gateway option allows the Cisco
                                 		  Unified ICM software to interact with a host system that is running another
                                 		  contact center application. Within the Cisco Unified ICM software, the Gateway
                                 		  feature is implemented as an Application Gateway node in a call routing script.
                                 		  You add an Application Gateway node to a script to instruct the system to
                                 		  execute an external application. This allows the script to evaluate responses
                                 		  from the external application and base subsequent routing decisions on the
                                 		  results produced by the application.

The Gateway option allows the Cisco Unified ICM system to interface
                                 		  with any external application, not just database applications.

You can use the Gateway option within the Cisco Unified ICM system to:

Allow other applications to select a call's destination.

Control or trigger external applications through Cisco Unified ICM
                                       				call routing scripts.

Pass data to and collect data from other contact center
                                       				applications.

For example, a simple Gateway application might return a variable to
                                 		  the CallRouter that identifies the caller as having a premium account. The
                                 		  routing script can use this information to control where and how the call is
                                 		  routed. Optionally, the Cisco Unified ICM can pass the retrieved information to
                                 		  the site that is receiving the call. Data such as account numbers, dates,
                                 		  billing phone numbers, and addresses can be passed along with the call to an
                                 		  answering resource.

### ICM Gateway
                           	 SQL

Cisco Unified ICM
                                 		  Gateway SQL allows the Cisco Unified ICM software to query an external
                                 		  Microsoft SQL Server database and use the data in call routing. If you have
                                 		  databases that contain customer account or profile information, you can perform
                                 		  database lookups to assist in call routing. You can base the database lookups
                                 		  on Calling Line ID (CLID), Dialed Number (DN), or Caller Entered Digits (CED)
                                 		  such as account or social security numbers.

A typical Gateway
                                 		  SQL application can prioritize callers. For example, a call routing script can
                                 		  use the caller's CLID to access a database and retrieve data about the caller
                                 		  such as the caller's average monthly bill. Based on this information, the
                                 		  routing script routes the caller to the most appropriate answering resource.

Before implementing the Gateway SQL and DB Lookup functionality, consider a Unified CVP VXML Application for database lookup
                                             instead. The DB Lookup node will interrupt routing while doing it's queries. The Unified CVP VXML Application will scale well.

The following figure
                                 		  shows a basic Gateway SQL configuration. Note that this configuration requires
                                 		  an additional database server on which you can load the external Microsoft SQL
                                 		  Server database and data.

### Internet Script Editor

Internet Script Editor is an application that works with routing and
                                 		  administration scripts. It provides the same functionality as the Cisco Unified
                                 		  ICM Script Editor software, without the need for an Administration & Data
                                 		  Server.

Internet Script Editor works through the IIS Web server on Cisco
                                 		  Unified ICM software, using HTTP to communicate with the Cisco Unified ICM
                                 		  software.

The Internet Script Editor and the Cisco Unified ICM Script Editor
                                 		  GUIs are essentially the same. The menus, toolbars, palette, and work space are
                                 		  utilized in the same manner in both applications. The differences between the
                                 		  two occur primarily in the method by which each application communicates with
                                 		  the Cisco Unified ICM software.

### Cisco Unified
                           	 Contact Center

Cisco Unified
                                 		  Contact Center combines Cisco IP telephony products and Cisco Unified ICM
                                 		  software to create an IP-based contact management solution. Cisco Unified
                                 		  Contact Center provides a migration path to an IP-based contact center by
                                 		  supporting integration with legacy call center platforms and networks. With
                                 		  Cisco Unified Contact Center, agents can use Cisco IP phones to receive both
                                 		  time-TDM and VoIP phone calls. Capabilities of the Cisco Unified Contact Center
                                 		  include intelligent call routing, ACD functionality, network-to-desktop CTI,
                                 		  Unified IP IVR integration, call queuing, and consolidated
                                 		  reporting.

Cisco Unified
                                 		  Contact Center is based mainly on two Cisco products: Unified CM and ICM
                                 		  software. Unified CM provides traditional PBX telephony features in an IP
                                 		  telephony environment. Unified ICM software provides enterprise-wide management
                                 		  and distribution of voice and data from ACDs, Unified IP IVR
                                 		  systems, small office/home office (SOHO) agents, and desktop applications.
                                 		  Cisco Unified IP phones and Unified IP IVRs (as well as traditional
                                 		  TDM IVRs) are also part of the Cisco Unified Contact Center.

| Note | Figures usually show the NIC as a separate
                                          		computer. Actually, NICs are implemented as software on the Unified ICM
                                          		software platform (usually on the CallRouter or CallRouter/Logger [Rogger]
                                          		machines). |
|---|---|

| Note | Not every
                                       		  component is used in every Unified ICM system. |
|---|---|

| Note | Figures usually show  the NIC as a separate computer.
                                          Actually, NICs are implemented as software on the Unified ICM software platform
                                          (usually on the CallRouter or CallRouter/Logger [Rogger]
                                          machines). |
|---|---|

| Note | A single PG can
                                          		  support both ACD PIMs and VRU PIMs; however, the ACD PIMs and the VRU PIMs must
                                          		  all be the same type of PIM (ACD PIMs must be the same type; VRU PIMs must be
                                          		  the same type). |
|---|---|

| Agent availability | Day of week |
|---|---|
| Agent skills | Number dialed |
| Caller-entered digits | Origin of call |
| Cost of the call | Cost of the transaction |
| Customer database lookup | Scheduled agents |
| Customer-defined business rules | Time of day |

| Note | Refer to the Cisco CTIOS Software
                                          documentation for more information. |
|---|---|

| Note | You can
                                          		  integrate VRU systems into the Cisco Unified ICM software in several ways. Interactive Voice Response (VRU) Systems provides more information on VRU integration as well as examples of how you can
                                          		  integrate VRU's with the Cisco Unified ICM system. |
|---|---|

| Note | ICM Application Gateway and ICM Gateway SQL planning provides more information on planning for the Gateway feature. |
|---|---|

| Note | Before implementing the Gateway SQL and DB Lookup functionality, consider a Unified CVP VXML Application for database lookup
                                             instead. The DB Lookup node will interrupt routing while doing it's queries. The Unified CVP VXML Application will scale well. |
|---|---|

| Note | You must perform
                                          		  some pre-installation planning if you are going to use the Cisco Unified ICM
                                          		  Gateway SQL option. ICM Application Gateway and ICM Gateway SQL planning provides more information on
                                          		  planning for the Cisco Unified ICM Gateway SQL feature. |
|---|---|

| Note | For information
                                          		  on Unified CCE, see the at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html and
                                          		  the . |
|---|---|