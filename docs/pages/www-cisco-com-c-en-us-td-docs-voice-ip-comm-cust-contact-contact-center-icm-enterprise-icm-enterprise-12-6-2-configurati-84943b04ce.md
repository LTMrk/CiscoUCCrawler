---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-84943b04ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified_12_62/ucce_b_serviceability-guide-for-cisco-unified_12_6_chapter_00.html
retrieved_at: 2026-08-16T14:40:51.098898+00:00
---

Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

# Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

Updated: April 28, 2023

Chapter: Product Architecture

## Chapter: Product Architecture

# Product Architecture

## Cisco Unified
                        	 Contact Center

Unified CCE delivers intelligent contact routing, call treatment, network-to-desktop computer telephony integration (CTI),
                           and multichannel contact management over an IP infrastructure. It combines multichannel automatic call distributor (ACD) functionality
                           with IP telephony in a unified solution, enabling you to rapidly deploy a distributed contact center infrastructure.

Unified CCE provides
                           		the following services:

Segmentation of customers and monitoring of resource availability

Delivery of each contact to the most appropriate resource anywhere in the enterprise

Comprehensive customer profiles using contact-related data, such as dialed number and calling line ID

Routing to the most appropriate resource to meet caller needs based on real-time conditions (such as agent skills, availability,
                                 and queue lengths)

Unified CCE enables you to smoothly integrate inbound and outbound voice applications with internet applications such as real-time
                           chat, web collaboration, and email. This integration enables a single agent to support multiple interactions simultaneously
                           regardless of which communications channel the customer chooses.

Unified CCE is a distributed solution with no single-server implementation. Unified CCE employs multiple servers each with
                           multiple software components. Deployment options are flexible with performance, capacity, and network topology driving the
                           deployment design.

Unified CCE was
                           		derived from Unified ICME with the primary difference being that Unified CCE
                           		integrates only with the Cisco Unified Communications Manager (Unified CM) IP
                           		PBX. All other major components of the Unified CCE solution are the same as the
                           		Unified ICM solution.

The Unified ICM platform is designed to route calls between various nodes in the TDM phone network. It is designed with an
                           emphasis on reliability and flexibility. All processing in these components is message-based. The content of the message and
                           the current state of the process determines the processing of each message. The messages are delivered to these components
                           using the Unified ICM Message Delivery Service (MDS). MDS ensures that both processes are fed the exact same set of messages
                           in the same order.

One of the most
                           		important concepts to understand about Unified CCE is its redundancy strategy.
                           		The components that contain centralized state are run in duplex. Two of these
                           		components work in lockstep to ensure redundancy and immediate recovery from a
                           		fault.

From a device
                           		standpoint, a typical Unified CCE deployment looks as follows:

There are four major components of a Unified CCE deployment: the Router, the Logger, the Peripheral Gateway (PG), and the
                           Administration & Data Server. The basic function of each is as follows:

Router —Make the routing decisions. The router selects a peripheral or agent to receive an inbound contact (voice call, email, chat,
                                 and so on).

Logger —Store (and replicate) all configuration, real-time and historical data.

Peripheral Gateway —Act as a gateway to a peripheral device, like an IP PBX or a Voice Response Unit (VRU), and a CTI gateway linking agent desktops.

Administration & Data Server —A server implementation that provides configuration data (from the Logger), an interface for real-time data, and a platform
                                 for the historical data server (HDS). The Administration & Data Server also offers an interface for administrators to alter
                                 configuration and routing scripts (Script Editor, Internet Script Editor).

Note

Unified CCE applications do not report their resource usage to monitoring solutions, like Cisco Prime Collaboration. The monitoring
                                       solution retrieves CPU and memory usage data directly from the Windows Server operating system. On multicore systems, Windows
                                       Server might report usage greater than 100% while the Unified CCE solution is running as usual.

### Unified CM
                           	 Peripheral Support and CTI OS

Cisco Finesse replaces CTI OS for Unified CCE.

CTI OS is no longer supported with Unified CCE. However, CTI OS is
                              		supported with UCCE System PG and other TDM peripheral types.

The CTI OS server setup now has the option to select UCCE System
                              		instead of UCCE. The setup also validates whether the selected peripheral is
                              		configured, through the Peripheral Gateway Setup, as UCCE System peripheral or
                              		not.

## Router

The Router is the
                           		brain of Unified CCE. Unified CCE can run user-defined scripts to make
                           		decisions on what happens with calls, and can determine how to get a call from
                           		one place to another. The Router communicates with several other components,
                           		including the Logger, the PGs, and the Administration & Data Servers
                           		(ADSs).

The Router receives notification from routing clients (PGs) that a call is in need of some form of routing. It then runs a
                           user-defined script to determine what to tell the routing client to do with the call.

In addition, the
                           		Router receives status events and reporting events from PGs. The Router uses
                           		these messages to update its current representation of the agents and resources
                           		in the system, which is used by the scripts to determine where to send calls.
                           		It also sends these messages to the Logger for storage and some of the messages
                           		to the Admin Workstations for real-time reporting.

Routers, Loggers and
                           		PGs are fault tolerant, having two instances of each component so that a
                           		failure of one provides for bump-less continuation of function through the
                           		remaining half of a duplex pair. Routers are duplex entities, which means that
                           		two separate, distributed instances (identified as Side A and Side B) use the
                           		MDS to keep in lockstep with the other side, ensuring that any outage of one
                           		side guarantees that the system continues operating without failures or
                           		impairments—the opposite side assuming sole responsibility for making routing
                           		decisions. All data as well as call control messaging is shared between sides
                           		to ensure that both sides have the same data by which to make (the same)
                           		routing decisions. Both Router sides are concurrently in service.

### Network Interface Controller

Like a PG, a Network Interface Controller (NIC) is a type of routing client. However, a NIC is more limited than a PG. A NIC
                              is used to interact with a telephony network, usually the TDM. A NIC is typically coresident with the Router and used for
                              Unified ICM deployments.

## Logger

Unified CCE uses the
                           		Logger to store historical data and configuration data about the call center.
                           		The Logger is the place where historical data is first stored, and from which
                           		it is later distributed. The Logger receives messages from the Router. These
                           		messages include detail messages about the calls and summary messages that the
                           		PGs compute and send through the Router. Examples of these summary messages are
                           		half-hour summaries (how many calls were received during a given period).

The Logger uses a
                           		synchronization process that is a little different than the Router. The
                           		messages coming to the Logger are sent only from the corresponding Router. Side
                           		A Router sends messages only to the Side A Logger. Side B Router sends messages
                           		only to the Side B Logger. Because the Routers are running in lockstep, it is
                           		guaranteed that while messages are flowing they are the same messages. However,
                           		recovery happens directly from Logger to Logger, using bulk database copy
                           		algorithms for efficiency.

The Loggers also
                           		distribute historical data to HDS and configuration and real-time data to the
                           		Administration & Data Servers through MDS. Loggers are duplex as well and
                           		are tightly coupled with their respective Router. In many deployments, a side
                           		of the Router and Logger are collocated on the same physical server. A
                           		Router/Logger combination is often referred to as the Central Controller.

## Peripheral
                        	 Gateway

The PG is the
                           		component that talks to the telephony devices through their own proprietary CTI
                           		interface in a Unified CCE system. These devices can be ACDs, IVR devices or,
                           		in cases such as with Unified CCE, an IP PBX. The PG normalizes whatever
                           		protocol the telephony device speaks, and keeps track of the state of agents
                           		and calls that are on that device. The PG sends this status to the Router, as
                           		well as forwards requests requiring customer logic to the Router.

The PG also exposes
                           		a normalized CTI interface to clients. These clients can be traditional CTI
                           		clients (wallboards, agent/supervisor desktop clients, and so on), or they can
                           		be another instance of Unified CCE, as is the case in a parent/child
                           		deployment.

The component of the
                           		PG that does the normalization is called a Peripheral Interface Manager (PIM).
                           		This component talks to the peripheral and translates whatever proprietary
                           		language it speaks into the normalized one that the Open Peripheral Controller
                           		(OPC) and the rest of the PG understand.

PGs fall into several groups. The first classification of PG includes those that talk to an ACD or Unified CM that has agents
                           on it. This is the typical case for a PG. It talks a proprietary CTI protocol to the switch, and maintains the state of agents
                           and calls in queue on the device. While all of these PGs report agent state to the Central Controller, they do it in a different
                           way. In the case of a PG talking to an ACD, the PG mirrors the state of the agents on the ACD; it keeps a copy of the primary
                           state of the agents tracked by the ACD. In the case of a PG attached to a Unified CM, the Unified CM does not know about agents
                           or agent states, it only knows about phone lines. In this case the PG is the primary for the agent state.

The second
                           		classification of PG is a VRU or Media Routing (MR) PG. These PGs expose an
                           		interface that is client-neutral. In the case of the VRU PG, this interface is
                           		tailored to voice calls; in the case of the MR PG, it is more generic task
                           		routing that is exposed. These PGs do not maintain agent state, but only
                           		maintain the state of calls (or tasks) and expose an interface for the devices
                           		to get instructions from the Router.

The third
                           		classification of PG is the group PG. There are two types of PGs that talk to
                           		groups of peripherals. The first is the Generic PG. This PG allows multiple
                           		PIMs of different types to reside inside of the same PG. Each peripheral on
                           		this PG behaves completely independently. Currently the Generic PG is supported
                           		only for Unified CCE, where it contains a Communications Manager PIM and a VRU
                           		PIM talking to an IP-IVR or Customer Voice Portal (CVP). The second type of
                           		group PG is a Unified CCE System PG. This PG, like the generic PG, has one Call
                           		Manager PIM and one or more VRU PIMs. The System PG ties these multiple PIMs
                           		together. In a traditional Unified CCE, a call that comes into the
                           		Communications Manager then gets transferred to the IP-IVR and then back to an
                           		agent looks like three separate calls to Unified CCE. The System PG coordinates
                           		these calls and makes that call look like a single call. This is what happens
                           		on a traditional TDM ACD, where the ACD also has a queue point.

The PG is duplexed
                           		using the same technology as the Central Controller, MDS. This means that there
                           		are two PGs operating at any time. All of the messages to the critical process
                           		on the PG (OPC) go through the MDS queue, to keep the two operating in
                           		lock-step. However, the PG operates slightly different from the Router – from a
                           		fault tolerance standpoint – in that while both sides share the same data, for
                           		many PG components, only one side is active. Should a fault occur, the opposite
                           		side activates and continues functioning, having the context of the other side
                           		without losing calls.

PGs use the Device
                           		Management Protocol (DMP) to communicate between themselves and the central
                           		controller. The following figure depicts the components involved in this
                           		communication and the communication links employed.

Coresident with the
                           		PG is the CTI Gateway (CG - CTI Server component).

### Open Peripheral Controller

The Open Peripheral Controller (OPC) computes and maintains the state of agents on the PG. The OPC  reports that state to
                              the Router, knows when a call requests instructions from the Router, and performs the CTI operations on the telephony device
                              as necessary. OPC is the critical process on the PG. It is kept in lock-step with its sibling on the other side.

### Peripheral Interface Manager

The Peripheral Interface Manager (PIM) is responsible for the connection to the peripheral (ACD, PBX, IVR). This process is
                              not a lock-step process nor is data shared between the two sides. Instead either the Side A or Side B PIM is active for each
                              peripheral. If one side loses its connection, the other side activates.

#### Unified
                              	 Communications Manager PIM

Unified CCE Only

The Communications
                                 		Manager PIM provides the interface between the Unified CM and the Unified CCE
                                 		OPC process. This PIM communicates with Unified CM through the JTAPI Gateway.

#### VRU PIM

The VRU PIM provides an interface to a VRU (or IVR). The communication protocol used between the PIM and the VRU is GED-125.

#### Media Routing PIM

The Media Routing (MR) PIM provides the integration point for multimedia contacts such as emails or collaboration (chat) sessions.
                                 It is also a necessary component for integration of the Outbound Option Dialer.

#### TDM ACD PIMs

The TDM ACD PIMs provide interfaces to various manufacturers’ Automatic Call Distributors. The communication protocol between
                                 the PIM and the ACD is typically proprietary.

### JTAPI Gateway

Unified CCE only

The JTAPI Gateway is a process that connects to the Unified CM CTI Manager and provides the link between the peripheral gateway
                              and the Unified CM cluster. The Unified CM CTI Manager communicates CTI messages to and from other nodes in the Unified CM
                              cluster. The JTAPI Gateway provides an added level of translation between the (Java) JTAPI interface and the (C++) Unified
                              Communications Manager PIM.

### CTI Gateway (CTI Server)

The CTI Server is the interface from OPC to CTI clients. It provides an interface (protocol) specified as GED-188.
                              This interface has many variances and message sets. It was used as a direct CTI connection to agent desktops or third-party
                              desktops. This use is deprecated.

GED-188 helps to hide the details of individual peripherals, but does not fully complete the job. The
                              messages sent from a CTI Server connected to an Aspect PG differ from the messages sent from a CTI Server connected to a Unified
                              CCE PG.

Today the CTI Server connects to several types of clients:

- Agent Reporting and Monitoring (ARM) clients – this variance of GED-188 allows reporting agent status and
                                 receiving information about the status of agents. It is one of the integration points for multichannel (email and web collaboration)
                                 applications and for the Outbound Dialing options.

- Parent ICM – a single connection is allowed to a CTI Server attached to a Unified CCE System PG. This
                                 connection allows the parent ICM to receive status about agents and calls on this PG, and to take control of certain incoming
                                 calls and route them itself. This variance of GED-188 is known as ACMI.

At any given time, only Side A or Side B CTI Server is active, not both. Clients must connect to one or the
                              other.

## Configuration System

The Unified CCE configuration system is also based around the concept of reliability and scalability. There can be multiple
                           configuration database copies, which are kept in sync using MDS and a synchronization process from the central controller.
                           Each of these can send updates to the Router, but only the Logger configuration database is authoritative.

The configuration system consists of the DBAgent process on the Router, which accepts connections from the Administration
                           & Data Servers, and distributes configuration updates to those Administration & Data Servers. The Administration & Data Servers
                           have a copy of the configuration and expose a GUI for browsing and making changes.  The Administration & Data Servers also
                           expose an API (ConAPI) for accessing the configuration information and for making changes.

### Administration & Data Server

The Administration & Data Server is the main interface to the Unified ICM/Unified CCE configuration. On the
                              Administration & Data Server resides a database that contains a copy of the configuration information in the Logger. A Distributor
                              process, which receives updates from the central controller, writes to the database to keep everything in sync. Multiple clients
                              read the configuration
                              from the database and send update messages to the central controller DBAgent process.

The two main clients in the Administration & Data Server are the configuration tools, and the Configuration Management Server
                              (CMS) process. The configuration tools are used to
                              provide a GUI to update the configuration.  The CMS process  is used to provide the Configuration API (ConAPI).

Processes that connect to ConAPI are the multichannel components for agent and skill group management and
                              CCMP.

The Administration & Data Server does not have a dependent twin, but rather provides fault tolerance in
                              numbers (N+1 model). A typical Unified ICM/Unified CCE deployment often has two or more Administration & Data Servers. Administration
                              & Data Servers connect to each central controller side – a primary and a secondary.   If a failure occurs on the primary link,
                              the
                              secondary recovers from the failure and restores connectivity.

- Administration Server and Real-time Data Server (AW Distributor) (with no HDS; configuration and
                                    real-time data but no historical or call detail data)

- Administration Server, Real-time and Historical Data Server, and Detail Data Server (AW-HDS-DDS),
                                    (configuration, real-time, historical, and call detail data)

- Administration Server and Real-time and Historical Data Server (AW-HDS) (configuration, real-time and
                                    historical data but no call detail data)

- Administration & Data Server configuration (AW-CONFIG, configuration data only)

Configuration changes are not supported on the HDS-DDS type (which includes historical and call detail data but
                              excludes real-time data). The HDS-DDS type includes only configuration data needed for historical reporting purposes.

### Configuration
                           	 Updates

- In the first step (not
                                    		  shown) an Administration Client reads configuration from the database, and
                                    		  determines that a change is required.

- When this determination
                                    		  happens, the GUI connects to the DBAgent process on the central controller and
                                    		  sends the update (Step 1).

- DBAgent sends the message
                                    		  to the Router, through MDS (Steps 2, 3).

- The Router validates the configuration message and sends it to the Logger to be run (Steps 4, 5).

- The Logger updates its configuration
                                    		  (Step 6).

- The Logger sends confirmation of the
                                    		  update to the Router (Steps 7, 8).

- The Router then
                                    		  sends the update to all its clients (DBAgent, PGs, and so on) (Step 9, 10).

- DBAgent sends
                                    		  this message to each of its Administration Server and Real-time Data Servers
                                    		  (Step 11). The Administration Server and Real-time Data Servers update their
                                    		  database (Step 12).

- The Configuration
                                    		  GUI detects the change happen (Step 13).

## Reporting
                        	 System

The reporting system
                           		for Unified ICM/Unified CCE is similar to its configuration system; they use
                           		the same distribution channel:

Reporting messages
                           		are generated by PGs (this includes both detail messages and summary messages)
                           		and then are sent to the Central Controller, which consists of the Router and
                           		the Logger.

The Router feeds
                           		real-time data to the Administration Server and Real-time Data Servers.

The Logger stores
                           		historical data and replicates it to the Historical Database.

Administration
                           		Server and Real-time Data Servers write those records into the real-time
                           		reporting database. Those Administration Server and Real-time Data Servers that
                           		are configured to have Historical Data Servers also write the appropriate
                           		records to the historical database. Cisco Unified Intelligence Suite (Unified
                           		IS) are web applications that uses Java Servlets to build reports to be viewed
                           		from thin (web browser) clients.

### Historical Data Server

The Historical Data Server (HDS) is an option to be installed with an Administration Server and Real-time Data
                              Server. It uses the same distributor technology used to keep the configuration database up to date. The HDS provides a long-term
                              repository for historical data and offloads historical reporting from the Logger. Historical data is replicated from the Logger
                              to one or more HDSs.

- Administration Server, Real-time and Historical Data Server, and Detail Data Server (AW-HDS-DDS) :
                                    HDS with call detail data store. This type includes both real-time and configuration data and you can use it to source historical
                                    data for the Analysis Call Path tool. This type is intended for small- to medium-sized deployments. There may be a maximum
                                    of two AW-HDS-DDS servers
                                    per Logger side in small or medium deployments but only one per Logger side in a large deployment (presumably with multiple
                                    AW-HDS servers).

- Administration Server and Real-time and Historical Data Server (AW-HDS) : HDS without a call
                                    detail data store (no call detail, call variable, agent state data). This type also includes both real-time and configuration
                                    data but you cannot use it to source data for the Analysis Call Path tool. This type is intended for large deployments. There
                                    may be a maximum of three
                                    AW-HDS per Logger side.

- HDS-DDS : HDS with call detail data store but no real-time data or configuration data. This type
                                    may be used to source historical data for the Analysis Call Path tool. This type is intended for large deployments and for
                                    use with multiple AW-HDS servers. There may be a maximum of one HDS-DDS per Logger side (presumably with multiple AW-HDS servers).

### Unified Intelligence Center

Unified Intelligence Center is a web-based reporting platform for the Cisco Unified Communications products and is supported
                              by Unified ICME and Unified CCE.

You can install Unified Intelligence Center as a standalone server or in a cluster of a maximum of eight server
                              nodes. There is one mandatory publisher node (called the Controller) and up to seven subscriber nodes (called Members). The
                              Controller node includes a Member, which means a deployment can consist of a Controller only.

Cisco Unified Intelligence Center offers both a web-based reporting application and an administration interface.
                              The reporting application runs on the Members. The administration application runs on the Controller.

Unified Intelligence Center reporting features include multi-user support, customized reports, security, multiple
                              display formats, web accessibility, and Web 2.0-like mashup support to display data from multiple sources on a single dashboard.
                              These features make Unified Intelligence Center a valuable tool in the information technology arsenal of any organization
                              and position it as a drop-in
                              replacement or solution for most reporting requirements.

- Web 2.0 based dashboard mashups

- Powerful grid presentations of reports with sorting and grouping

- Chart and gauge presentations of reports

- Association of multiple report displays with the same report definition

- Custom filters

- Custom thresholds to alert on the data

- Pre-installed stock report templates for Unified CCE data

- Ability to report data from JDBC compatible data sources

- Multiple users

- Customized dashboards and custom reports

- Report scheduler

- Detailed security levels and LDAP/local database authentication

- Import and export of report XML files

- Export of grid reports to Microsoft Excel

- Multiple languages

- Clustered deployment

- Management support through Simple Network Management Protocol (SNMP), Java Management Extensions (JMX),
                                    and Cisco Analysis Manager

#### Unified
                              	 Intelligence Center Standard Deployment Model

The Unified
                                 		Intelligence Center deployment with Unified CCE uses the AW-HDS as its data
                                 		source server. You can connect to multiple AW-HDS databases to handle the load
                                 		from multiple Unified Intelligence Center reporting nodes. You can use other
                                 		data sources, such as the CVP Reporting Server, along with the Unified CCE
                                 		AW-HDS as data source servers. The ACE load balancer, an optional component,
                                 		provides load balancing for report queries across the multiple reporting nodes
                                 		and servers as a single point of access to the cluster.

You can use Unified CCE deployments with a distributed AW-HDS as a data source for Unified Intelligence Center reports. However,
                                 local area network AW-HDS access ensures enhanced throughput in data extracted and ensures faster response times for reports,
                                 especially real-time reports with repeated refresh intervals.

#### Unified
                              	 Intelligence Center Scaled Deployment Model

You can deploy
                                 		Unified Intelligence Center as the reporting solution with Unified CCE
                                 		deployments that scale over WAN networks. In these deployments, Unified
                                 		Intelligence Center is deployed locally with one section or data center of the
                                 		scaled Unified CCE deployment. Unified Intelligence Center can access the local
                                 		AW-HDS over the Local Area Network (LAN), and the remote AW-HDS, which is
                                 		deployed along with the remote section of Unified CCE over the Wide Area
                                 		Network (WAN).

You can deploy other data sources, such as the Cisco Unified Customer Voice Portal, along with Unified CCE. Firewall considerations
                                 when you deploy over the WAN apply to the data source servers. Open appropriate ports as described in Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/tsd_products_support_series_home.html , depending on the remote database configuration.

### Unified Contact
                           	 Center Management Portal

Unified CCMP is a suite of server components that simplify the operations and procedures for performing basic administrative
                              functions such as managing agents and equipment, and provide a common, web-based user interface within the entire Unified
                              CCE product set. Unified CCMP consists of four components:

- RDBMS Database (known as
                                       				the datamart) holds the imported enterprise data.

- Reporting Services Database
                                       				imports and processes data from the datamart so that SQL Server Reporting
                                       				Services can use it to populate reports.

- The Application Server component manages security and failover. It manages security by ensuring that users can view only specific
                                 folders and folder content as defined by their security sign-in credentials. It verifies that a user is valid and then loads
                                 the system configuration that applies to that user. It also manages failover. So if one database server fails, the application
                                 can automatically retrieve the required data via an alternative database server.

- The Web Server component provides a user interface to the platform. The user interface allows users to work with report data,
                                 and perform administrative functions.

- The Data Import Server
                                 		  component is an Extract, Transform, and Load (ETL) server for data warehouses.
                                 		  The Data Import component imports the data used to build reports. It is
                                 		  designed to handle high volume data (facts) such as call detail records and
                                 		  data that is rarely changed (dimensions) such as agents, peripherals, and skill
                                 		  groups.

If you install these components on more than one server, you generally install the Data Import and Database components on
                              the Database Server. You usually install the Application and Web components on the Web Application Server.

Unified CCMP maintains a complete data model of the contact center equipment to which it is connected and periodically synchronized.
                              In addition to configuration information such as agents or skill groups, the Unified CCMP can optionally record the events
                              logged by the equipment. These records are used for management information and reporting purposes. Unified CCMP data model
                              and synchronization activity allows for items to be provisioned either through the Unified CCMP Web interface or from the
                              standard equipment specific user interfaces.

The following
                              		illustration shows the Unified CCMP system architecture. The top half of the
                              		diagram is a traditional three tier application. This application includes a
                              		presentation layer (an ASP.NET web application), a business logic application
                              		server, and a SQL Server database. The lower half of the system architecture is
                              		a process orchestration and systems integration layer called the Data Import
                              		Server.

#### Web
                                 		  Application

The user interface to Unified CCMP is via a web application that you access using a web browser. You gain access to the Unified
                                 CCMP application through a secure sign-in screen. Every user has a unique username. This user is assigned privileges by the
                                 system administrator, which defines the system functions the user can access and perform.

The user interface
                                 		  is time-zone aware and connections to it are secured through HTTPS. The web
                                 		  application is hosted on the server by Microsoft Internet Information Services
                                 		  (IIS) so it is suitable for lockdown in secure environments.

#### Application
                                 		  Server

The Unified CCMP
                                 		  Application Server component provides a secure layer in which all business
                                 		  logic is implemented. The application server component runs in a separate
                                 		  service and is always hosted with the web server component. The application
                                 		  server component also includes caching to improve performance and audits all
                                 		  actions taken by signed-in users.

#### Reporting
                                 		  Services

Unified CCMP uses
                                 		  Microsoft Reporting Services technology for generating reports. Microsoft
                                 		  Reporting Services is a part of SQL Server Enterprise Edition. Unified CCMP
                                 		  provides a flexible reporting system in which reports are authored in the
                                 		  industry standard Report Definition Language (RDL).

#### Data Import
                                 		  Server

The Data Import
                                 		  Server component is an Extract, Transform, and Load application for Unified
                                 		  CCMP. The Data Import Server component imports the data used in Unified CCMP.
                                 		  The Data Import Server component is designed to handle high volume data
                                 		  (facts), such as call detail records and data which is changed irregularly
                                 		  (resources), such as agents, peripherals, and skill groups. The Data Import
                                 		  Server component is also responsible for monitoring changes in Unified CCMP
                                 		  system and ensuring that those changes are updated onto Unified ICM/Unified CCE
                                 		  and Unified Communications Manager. The Data Import Server component
                                 		  orchestrates the creation, deletion, and update of resources to Unified
                                 		  ICM/Unified CCE and Unified Communications Manager. The Microflow Runtime is
                                 		  the heart of the Data Import Server component. It orchestrates systems without
                                 		  resorting to low level programming languages. The Microflow Runtime is a
                                 		  general purpose scripting environment and can be applied to a wide range of
                                 		  problems. The term microflow describes any modular, reusable, and independent
                                 		  unit of business logic. An example microflow might update an agent on Unified
                                 		  ICM/Unified CCE when changes are made in the Unified Communications Manager web
                                 		  server component.

#### Unified CCMP
                                 		  Services

- Management Portal, Data
                                       				Import Server : The Data Import Server is responsible for importing new
                                    			 dimensions and changes to dimensions such as agents, skill groups, call types,
                                    			 and dialed numbers from Unified CCE. The Data Import Server periodically checks
                                    			 whether there are any new dimensions to import or whether there have been any
                                    			 changes made to dimensions that have already been imported. This periodic check
                                    			 allows for closed-loop management of changes made to dimensions provisioned by
                                    			 Unified CCMP.

- Management Portal,
                                       				Provisioning Server : The Provisioning Server is responsible for sending
                                    			 provisioning requests from Unified CCMP to Unified CCE. The requests are move,
                                    			 add, change, and delete (MACD) operations for the resource types that Unified
                                    			 CCMP can manage such as creation of new resources, for example a new agent, or
                                    			 new memberships, such as an Agent to Skill Group membership. These updates are
                                    			 applied via the ConAPI interface.

Unified CCMP
                                 		  exposes a rich set of performance (known as PerfMon) counters that you can
                                 		  monitor in real time to gauge status, performance and health.

A shortcut to the
                                 		  32-bit version of Performance Monitor application is available in the Cisco
                                 		  Unified CCE Tools folder for easy access. This shortcut launches the 32-bit
                                 		  version of PerfMon utility so that you can easily monitor the Unified CCE
                                 		  processes.

## Outbound
                        	 Option

Unified ICM and
                           		Unified CCE support outbound campaign dialing through its Outbound Dialing
                           		subsystem (also known as Blended Agent or BA). The Outbound Dialing subsystem
                           		consists of three major components: the Campaign Manager, the Import Process,
                           		and the Dialers.

Outbound campaigns
                           		start with the Import process. Use the Import process to import a set of
                           		outbound calls into the BA database. This data defines what calls are made and
                           		how they are made.

The Campaign Manager
                           		is responsible for running the Outbound Dialing campaigns. It reads the
                           		campaigns from the BA DB. It then distributes the calls to be made to the
                           		Dialers. It takes the results of calls and sends reporting information to the
                           		Unified ICM/Unified CCE central controller where it is recorded in Unified
                           		ICM/Unified CCE reporting database.

The Outbound Option
                           		Dialer maximizes the resources in a contact center by dialing several customers
                           		per agent. This component resides on the PG server.

The outbound Option deployment uses the Session Initiation Protocol (SIP) Dialer. The SIP dialer performs dialing, call control,
                           Voice Gateway Interaction functionality instead of using resources on managing the  call. In an Outbound Option deployment
                           that uses the SIP Dialer handles the Call Progress Analysis for Outbound campaigns. This helps in increasing the number of
                           outbound agents that a deployment can service on a PG. This reduces the number of PGs and Dialers deployed for larger enterprise
                           systems.

The following
                           		diagram provides a high-level view of the Outbound Option components and their
                           		relationship with other Unified ICM components.

Enable the Outbound Option
                           		high availability option to provides continuous service without any
                           		disruptions, using redundant SIP Dialers and Campaign Managers.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | Unified CCE applications do not report their resource usage to monitoring solutions, like Cisco Prime Collaboration. The monitoring
                                       solution retrieves CPU and memory usage data directly from the Windows Server operating system. On multicore systems, Windows
                                       Server might report usage greater than 100% while the Unified CCE solution is running as usual. |
|---|---|