---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-5bde58fd60
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_cti-planning126.html
retrieved_at: 2026-08-16T20:03:25.719043+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: CTI Planning

## Chapter: CTI Planning

# CTI Planning

Cisco CTI software provides an interface between the Unified ICM software and agent
                        desktop and server applications. The CTI software works with a Peripheral Gateway's ACD
                        and VRU interface software and associated ACDs to track call events and transactions and
                        forward call- and transaction-related data to an agent's desktop computer.

Pre-installation planning for CTI involves several tasks:

Review CTI Server communications and platform options.

Become familiar with the desktop options available with CTI Server.

Estimate CTI message traffic.

Plan fault tolerance for the CTI Server.

Review ACD support for client control and third-party call control.

## CTI Server

CTI Server, the
                              		  basic server component of Cisco CTI, enables the Unified ICM software to
                              		  deliver agent, call, and customer data in real-time to a server and/or
                              		  workstation application as events occur throughout the life of a call. The CTI
                              		  Server is a software process that runs on a Peripheral Gateway (PG). It is the
                              		  CTI gateway into the Unified ICM software's data and services.

The following figure
                              		  shows a sample CTI Server system. CTI Servers may be running at one or several
                              		  call centers in the enterprise.

One function of the
                              		  CTI Server is to forward pre-route indications to CTI application servers.
                              		  Pre-route indications identify the caller and provide CTI applications with
                              		  other call attributes while the call is still in the public or private network
                              		  (that is, before the call is connected to an agent or IVR 
                              		  resource).

CTI Server also
                              		  reports call events and agent work state changes as they occur through each
                              		  stage of the call flow—from the moment a call arrives at an answering resource
                              		  (ACD, PBX, IVR), until the caller hangs up. In a desktop application
                              		  environment, call event information is delivered to the targeted agent desktop
                              		  at the same time the call is delivered.

### CTI Server
                           	 Communications

The CTI Server uses
                                 		  TCP/IP Ethernet for communication with clients. You can use multi-protocol IP
                                 		  routers to provide connectivity to clients on other types of LANs. You can use
                                 		  the same LAN for the Peripheral Gateway's visible network interface and for CTI
                                 		  client-to-server communications.

### CTI Server Platform
                           	 Options

The CTI Server runs
                                 		  on a machine that is also running a Cisco ACD (or VRU) PG process. The shared
                                 		  platform option is shown in the following figure.

### CTI Server Fault
                           	 Tolerance

You can implement
                                 		  the CTI Server in a duplexed, fully fault-tolerant configuration. In a duplexed
                                 		  configuration, the CTI Server is installed on a pair of server platforms. In
                                 		  the event of a failed CTI client connection, the client process can
                                 		  automatically reestablish a connection to either side of the duplexed CTI
                                 		  Servers. The call's CTI client history list and any updates to call variables
                                 		  remain in effect when the connection is reestablished. The following figure
                                 		  shows a duplexed CTI Server configuration.

### Cisco CTI Object Server (CTI OS)

CTI Object Server
                                 		  (CTI OS) is a high-performance, scalable, fault-tolerant server-based solution
                                 		  for deploying CTI applications. CTI OS serves as a single point of integration
                                 		  for third-party applications, including Customer Relationship Management (CRM)
                                 		  systems, data mining, and workflow solutions.

Configuration data
                                 		  is managed at the server, which helps simplify customization, updates, and
                                 		  maintenance of CTI applications. You can access and manage servers remotely.
                                 		  Thin-client and browser-based applications that do not require Cisco software
                                 		  on the desktop can be developed and deployed with CTI OS.

CTI OS incorporates
                                 		  the following major components:

CTI OS Toolkit

Client Interface
                                       				Library

CTI OS Combo
                                       				Desktop for Agents and Supervisors

CTI OS is a client
                                 		  of CTI Server. It has a single all-events connection to Cisco CTI Server. In
                                 		  turn, CTI OS accepts client connections using session, agent, and call
                                 		  interfaces. These interfaces are implemented in .NET, COM, Java, C++, and C,
                                 		  allowing for a wide range of application development uses. The interfaces are
                                 		  used for call control, to access data values, and to receive event
                                 		  notifications.

For complete and current information about the number of agents supported for CTI OS and other configurations, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . See Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html for hardware requirements for Unified CCE virtualized systems.

For all installations, the CTI OS Server must be co-resident with the PG.

For more information on CTI OS, refer to the CTI OS document set.

## CTI Server Client
                        	 Application Models

You can use either
                              		  of two client models to integrate call center applications with the Unified
                              		  ICM: agent workstation and CTI Bridge.

### Agent Workstation
                           	 Application

In the agent
                                 		  workstation model, the client is an application running on a personal computer
                                 		  on an agent's desktop. This client is interested in the call data and call
                                 		  events related to a single agent teleset. The agent workstation application can
                                 		  also be interested in agent state changes.

Typically, when the
                                 		  agent workstation application is informed of an incoming call, it uses the call
                                 		  data collected by the Unified ICM system to retrieve caller-specific data from
                                 		  a database. This data is presented on the agent workstation screen at
                                 		  approximately the same time that the incoming call is connected to the agent.

While handling the
                                 		  call, the agent can update some of the call data. For example, an agent who is
                                 		  processing an insurance claim can make some adjustments to the call data; an
                                 		  update ensures that the changes are not lost before the call is transferred to
                                 		  a second agent.

Upon completion of
                                 		  the call, the agent can use the client to add call-specific, wrap-up
                                 		  information to the Termination_Call_Detail record logged in the Unified ICM
                                 		  central database. This wrap-up data is a key value that can help locate more
                                 		  detailed transaction information in some other database. If the agent
                                 		  conferences with or transfers the call to another agent on the same ACD with a
                                 		  CTI client workstation, then that agent's CTI client also receives the incoming
                                 		  call data, including any updates made by the first agent. If the transfer or
                                 		  conference involves an agent on another ACD, the call data is provided to the
                                 		  remote CTI client if a translation route is used.

### CTI Bridge
                           	 Application

CTI Bridge
                                 		  applications are interested in all call and agent state events that occur on
                                 		  the ACD, unlike agent workstation applications that are interested only in the
                                 		  events associated with a particular teleset. The CTI Bridge application is a
                                 		  user-written program that converts or adapts some or all of the CTI Server
                                 		  messages into another format; a single CTI Bridge application provides such
                                 		  services for multiple agent desktops. You can design the CTI Bridge application
                                 		  to interface with CTI Servers or similar applications on systems that are
                                 		  already in use in the call center.

Some examples of CTI
                                 		  Bridge applications include:

Message
                                       				converter applications. For example, an application can convert the CTI Server
                                       				message set to the message set of a foreign telephony server.

Server-to-server
                                       				communication applications. For example, an application can enable the CTI
                                       				Server to speak directly to a help desk application's middle tier server.

In a CTI Bridge
                                       				configuration, a CTI Bridge application provides the connection between an
                                       				existing desktop CTI application and the Unified ICM.

## CTI Server Network and Database Planning

Some pre-installation planning is
                           necessary to prepare your CTI desktop and network environment for the
                           introduction of a CTI Server.

### Network Topology

The machine running CTI Server connects to the
                                 CTI desktop environment via an Ethernet LAN. Therefore, the CTI desktop
                                 environment must reside on an Ethernet LAN. Other networks, such as Token-Ring,
                                 can require additional network hardware if you are connecting them to a CTI
                                 Server.

### Network Security

Be sure that the CTI
                                 desktop environment IP routing scheme is compatible with the Unified ICM system
                                 and CTI Server. For example, if you have a firewall set up on the CTI
                                 environment LAN, you may need to change your system access setup or network
                                 configuration.

### Software Distribution Strategy

If you are installing the
                                 CTIOS or CTI Desktop software components on multiple desktops, you must create
                                 a distribution strategy. For example, if you place the software on a
                                 centralized server and allow certain desktops within the enterprise to download
                                 the software, you must ensure that all sites have access to the centralized
                                 server.

### Well-Known Port for CTI Server

A well-known port number identifies CTI Server as an application
                                 		  running in your intranet. All CTI clients, as well as the system administrator,
                                 		  must know this well-known port number. If you do not want to use CTI
                                 		  Server's default port numbering scheme, you can choose a well-known port
                                 		  number that fits into your overall network environment. You can use the
                                 		  Peripheral Gateway Setup to override the default port settings used to install
                                 		  the CTI Server PGs.

### Fail-over Strategy
                           	 for CTI Clients

Cisco CTI includes
                                 		  automatic fail-over and recovery mechanisms. Ensure that each CTI client has a
                                 		  clear and established network path to a CTI Server in case of a fail-over. For
                                 		  example, you may plan for each CTI client to have access to local and remote
                                 		  CTI Servers.

### Database
                           	 Strategy

You may have CTI applications that perform database queries to retrieve customer information for use in call processing. Some
                                 CTI applications acquire database records "pre-call" (that is, before the call arrives at an agent's desktop). Other applications query a database immediately after the call
                                 arrives at the agent's deskset. Plan a strategy for running database queries in the most efficient and timely manner possible.

## CTI Server
                        	 Messages

The CTI Server makes
                              		  traffic call data available to applications in real time. To accomplish this
                              		  task, the CTI Server responds to requests from clients and originates
                              		  unsolicited messages. All messages share a common message header and use the
                              		  same set of data types.

The table titled CTI Server Message
                                 			 Categories groups the messages into broad categories based on the nature of
                              		  the message data.

Category

Description

Session
                                          					 Management

Messages
                                          					 related to the establishment and maintenance of a client connection to the CTI
                                          					 Server. These messages typically happen at client startup, shutdown, and during
                                          					 auto-recovery.

Miscellaneous

Messages
                                          					 related to system-level events on the PG (for example, peripheral offline, loss
                                          					 of PG-to-central controller communications).

Call Events

Messages
                                          					 related to call state changes.

Agent Events

Messages
                                          					 related to agent state changes.

Call Data
                                          					 Update

Messages
                                          					 related to CTI client modification of call data.

Client
                                          					 Control

Messages
                                          					 related to the direct control of agent state (for example, sign-in, sign-out)
                                          					 as well as control of inbound and outbound calls.

CTI Server imposes
                              		  varying degrees of message traffic against the PG based on the specific call
                              		  center and CTI application environment in which it is deployed. Document a
                              		  typical call scenario in your CTI application environment, prepare for adequate
                              		  bandwidth, and order the proper server platform.

### Typical Call Scenario

To estimate CTI
                                 Server message traffic, document a typical call scenario in your CTI
                                 application environment. The goal of this exercise is to account for all types
                                 of potential message traffic in the link between the CTI Server and the CTI
                                 application environment.

For example, you can handle a
                                 typical call as follows:

The call is
                                       pre-routed.

The call receives a call treatment such as a
                                       request to set call data.

A simple call release, hold,
                                       transfer, or post-route request takes place.

During this
                                       time an agent state may change (for example, from ready to work
                                       ready).

### Message Load and Bandwidth

Ensure that you have enough bandwidth in the
                                 datacom connection to handle the message traffic between the CTI Server and the
                                 CTI application environment. For example, are you sure that a 56-Kbps
                                 connection is adequate for your environment?

The call scenario
                                 process helps you to estimate the message load and calculate how much bandwidth
                                 is required in the link between the CTI Server and the CTI application
                                 environment (for example, 56K, 256K, or more).

### CTI Server
                           	 Platform

Ensure that the CTI
                                 		  Server platform has adequate CPU processing speed and RAM to handle the message
                                 		  activity. You may require a high-end Cisco CTI Server/PG platform for the CTI
                                 		  Server.

## Third-Party Call Control

Call control is the ability of an application that is external to the
                              		  ACD to programmatically control a telephone call. For example, a CTI
                              		  application can put a call on hold, transfer the call, or hang up the call.

CTI Server products support third-party call control. Any call control
                              		  initiated outside the ACD/teleset domain is referred to as third-party. With
                              		  third-party call control, there is no physical connection between the computer
                              		  and the teleset (see the following figure).

The desktop CTI application communicates with the Cisco CTI Server
                              		  over a LAN. The CTI Server in turn communicates with the ACD to send call
                              		  control requests. In this model, the CTI application is not bound to any
                              		  particular teleset. The CTI application can control any teleset connected to
                              		  the ACD and CTI Server.

Depending on the specific ACD, the client application can perform all
                              		  or most of the following telephony functions:

Answer/Hang up

Agent Login and Wrap-up data

Consultative/Blind Conference

Consultative/Blind Transfer

Generate DTMF tones

Get/Set Agent states

Get/Set ICM call data (ANI, DNIS, CED, UUI, call vars)

Hold/Unhold/Swap Hold

Make a call

Redirect

## ACD Support for
                        	 Client and Third-Party Call Control

Different peripheral
                              		  types implement and support varying levels of CTI functionality. For example, a
                              		  different set of client control requests and call event types are available
                              		  depending on the peripheral type. In addition, there can be other CTI-related
                              		  restrictions and implementation differences based on the type of peripheral.
                              		  Consider these differences when you write a CTI client application that
                              		  interfaces with third-party switches and devices.

As part of CTI
                              		  pre-installation planning, review ACD support for client control and
                              		  third-party call control.

| Note | All of the
                                          		  functionality found in the agent workstation (desktop) model is also available
                                          		  in the CTI Bridge application model. However, you must write the CTI Bridge
                                          		  application to support this functionality. |
|---|---|

| Category | Description |
|---|---|
| Session
                                          					 Management | Messages
                                          					 related to the establishment and maintenance of a client connection to the CTI
                                          					 Server. These messages typically happen at client startup, shutdown, and during
                                          					 auto-recovery. |
| Miscellaneous | Messages
                                          					 related to system-level events on the PG (for example, peripheral offline, loss
                                          					 of PG-to-central controller communications). |
| Call Events | Messages
                                          					 related to call state changes. |
| Agent Events | Messages
                                          					 related to agent state changes. |
| Call Data
                                          					 Update | Messages
                                          					 related to CTI client modification of call data. |
| Client
                                          					 Control | Messages
                                          					 related to the direct control of agent state (for example, sign-in, sign-out)
                                          					 as well as control of inbound and outbound calls. |

| Note | For a description
                                       		  of the session management messages, see the latest version of the CTI Server Message Reference Guide for Cisco Unified Contact Center Enterprise for more information.. |
|---|---|

| Note | Most, but not all, ACDs support third-party call control. |
|---|---|