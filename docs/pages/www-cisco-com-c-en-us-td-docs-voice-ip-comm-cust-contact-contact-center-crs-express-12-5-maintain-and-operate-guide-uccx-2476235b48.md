---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-2476235b48
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide/uccx_b_uccx-125admin-and-operations-guide_chapter_00.html
retrieved_at: 2026-08-16T21:42:18.909841+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified CCX
	 Introduction

## Chapter: Unified CCX
	 Introduction

# Unified CCX
                     	 Introduction

Unified CCX provides a multimedia (voice, data, and web) IP-enabled customer-care application environment that enhances the
                           efficiency of contact centers by simplifying business integration, easing agent administration, increasing agent flexibility,
                           and enhancing network hosting.

All configuration values in Unified CCX must be entered in English language unless explicitly mentioned on the administration
                           screen.

The following sections provide an overview of the configuration and management components of the Unified CCX product family:

## Unified CCX
                        	 Components

This
                              		  section describes the following components of the Unified CCX system:

Unified
                                    				Gateway—Connects the Cisco Unified Communications family of products to the
                                    				Public Switched Telephone Network (PSTN) and to other private telephone systems
                                    				such as PBX.

Unified CM Server—The Cisco Unified Communications
                                       				  Manager ( Unified CM )
                                    				provides the features required to implement IP phones, manage gateways, provide
                                    				failover and redundancy service for the telephony system, and direct Voice over
                                    				IP (VoIP) traffic to the Unified CCX system.

Cisco Unified Communications Manager was previously
                                                				  known as Unified Call Manager. This guide uses Cisco Unified Communications
                                                   					 Manager at the first occurrence and Unified CM for
                                                				  later occurrences.

Unified CCX
                                    				Server—Contains the Unified CCXEngine that runs applications, including Cisco
                                    				script applications, 
                                    				 Busy applications, Ring No Answer applications,
                                    				and Voice Extensible Markup Language (VXML) 2.0 applications.

You can position your
                                    				Unified CCX application server anywhere on the IP network and administer your
                                    				applications from a web browser on any computer on the IP network. Because
                                    				Unified CCX uses an open architecture that supports industry standards, you can
                                    				integrate your applications with a wide variety of technologies and products,
                                    				such as Enterprise databases. The Unified CCX Server has the following
                                    				components:

Unified CCX Configuration Datastore (CDS)—Manages configuration, component, and application information within the Unified
                                          CCX cluster and communicates with Unified CM .

Historical Reports Database
                                          					 Server—Dedicated server that stores Unified CCX database for the following
                                          					 datastores: Configuration Datastore (CDS), Historical Datastore (HDS), and
                                          					 Repository Datastore (RDS).

Cisco Customer Collaboration Platform —Acts as the endpoint that hosts the widgets that end users and agents use during chat and email sessions. Customer Collaboration Platform accepts chat request, communicates with Unified CCX to allocate an agent for the chat and then establishes the chat session
                                          between agent and end user.

Customer Collaboration Platform fetches email messages from the email server, communicates with Unified CCX to allocate an agent, and provides the email
                                          management user interface components via the Finesse desktop.

Unified
                                    				CCXEditor—Allows application developers to use a simple Graphical User
                                    				Interface (GUI) to create, modify, and debug Unified CCX scripts for automating
                                    				customer interactions. Each script consists of a series of steps, implemented
                                    				as Java Beans.

Unified CCX
                                    				Administration and Unified CCX Serviceability web interfaces—Provides access
                                    				through a web browser for administrators to configure and manage Unified CCX
                                    				datastores, servers, and applications.

Cisco Finesse Agent and Supervisor Desktops—Desktop programs that allow Unified CCX agents and supervisors to log in to the
                                    system, change agent states, and monitor status.

Media Resource
                                    				Control Protocol (MRCP) Automatic Speech Recognition (ASR) server—(optional)
                                    				Dedicated server that performs real-time speech recognition.

MRCP
                                    				Text-to-Speech (TTS) server—(optional) Dedicated server that converts text into
                                    				speech and plays it back to the caller.

Support for
                                                				  high availability and remote servers is available only in multiple-server
                                                				  deployments.

Cisco Unified
                                    				Intelligence Center—A web-based reporting solution for historical reports that
                                    				provides detailed Call Contact Call Detail Records (CCDRs), application
                                    				performance, and traffic analysis information.

## Unified CCX Product
                        	 Family

The Unified
                              		  CCX product family provides contact-processing functions for your Cisco Unified
                              		  Communications solution.

The
                              		  software package that you choose determines which steps, components, and
                              		  subsystems you receive. Each Unified CCX product includes Unified CCXEngine
                              		  and Unified CCXEditor.

### Unified IP
                           	 IVR

The Unified
                                 		  IP IVR is a multimedia (voice, data, web) IP-enabled interactive voice response
                                 		  solution that offers an open and feature-rich foundation for the creation and
                                 		  delivery of Unified IP IVR applications through Internet technology.

Unified IP
                                 		  IVR automates call handling by autonomously interacting with contacts. Using
                                 		  Unified IP IVR, you can create applications that answer calls, provide menu
                                 		  choices for callers, obtain caller data such as passwords or account
                                 		  identification, and transfer calls to caller-selected extensions. You can also
                                 		  create Unified IP IVR applications that respond to HTTP requests, perform
                                 		  outbound calling, send e-mail, and process VXML 2.0 commands.

The Unified
                                 		  IP IVR package provides the following features:

Java Database
                                       				Connectivity (JDBC) support—Unified IP IVR applications can access Oracle,
                                       				Sybase, and IBM DB2 databases.

Real-time
                                       				reporting client—Unified IP IVR applications can generate a variety of reports
                                       				that provide detailed information about the real-time status of your system.

Cisco Unified
                                       				Intelligence Center—A web-based reporting solution for historical reports that
                                       				provides detailed Call Contact Call Detail Records (CCDRs), application
                                       				performance, and traffic analysis information.

Automatic Speech
                                       				Recognition (ASR)—Unified IP IVR applications can take advantage of ASR to
                                       				provide callers with the option to use speech to navigate through menu options.

Text-to-Speech
                                       				(TTS)—Unified IP IVR applications can use TTS to read back documents and
                                       				prescripted prompts to callers.

### Unified Contact
                           	 Center Express

Cisco Unified Contact Center Express (Unified CCX) is
                                 		  an IP-based Automated Call Distribution (ACD) system that queues and
                                 		  distributes incoming calls to Unified CCX agents, who can be groups of Unified
                                 		  CM users for Unified CM integration.

You can use
                                 		  Unified CCX applications to route calls to specific agents. You can also
                                 		  integrate Unified CCX with Unified IP IVR to gather caller data and classify
                                 		  incoming calls.

Unified CCX
                                 		  includes a web-based real-time and historical reporting system that you can use
                                 		  to monitor system, Contact Service Queue (CSQ), and resource performance.

The Unified
                                 		  CCX system consists of the following major components:

Resource
                                       				Manager—Application program that monitors Unified CCX agent phones and allows
                                       				you to organize agents into resource groups or skills-based partitions
                                       				according to the types of calls each group can handle.

CSQ—Application
                                       				program that places incoming calls in a queue and distributes them to the
                                       				appropriate set of agents as the agents become available.

The
                                 		  following licensing options are available for the Unified CCX system:

Unified CCX
                                       				Premium—Adds full Unified IP IVR support (except for Unified ICM integration)
                                       				including database integration, Voice eXtensible Markup Language (VoiceXML),
                                       				HTML web integration, custom Java extensions, and e-Notification services. The
                                       				outbound feature is now bundled with the Premium package. You will receive one
                                       				outbound seat free with each premium seat. The maximum number of outbound seats
                                       				supported will be based on the hardware type.

The licensed IVR ports for outbound.

The licensed agent seats for outbound.

The sum of the dedicated IVR ports configured for IVR-based outbound campaigns.

The agent seats that currently in use for agent-based outbound campaigns.

The dedicated outbound IVR ports for a campaign is the number of IVR ports that you want to reserve for a campaign from the
                                                      total number of CTI ports available in the outbound call control group.

The Unified CCX
                                             			 Enhanced package and the Unified CCX Premium package are provisioned in the
                                             			 same way.

## Unified CCX Cluster
                        	 Architecture

Support for high
                                          			 availability and remote servers is available only in multiple-server
                                          			 deployments.

The Unified
                              		  CCX cluster consists of one or more servers (nodes) that are running Unified
                              		  CCX components in your Unified CCX deployment.

If you
                              		  deploy Unified CCX components on a single server, the Unified CCX cluster
                              		  (often referred to as cluster in
                              		  this manual) consists of that server. If you deploy Unified CCX on multiple
                              		  servers, the cluster includes the Unified CCX server and standby server on
                              		  which you installed Unified CCX. The Unified CCX cluster can support up to two
                              		  Unified CCX Servers, one designated as the active Unified CCX
                                 			 Server and the other designated as the standby Unified
                                 			 CCX Server for high availability purposes.

When you
                              		  install or upgrade Unified CCX on a server, you designate the cluster to which
                              		  the server will belong by designating the cluster profile for that cluster.

Cluster
                              		  architecture accommodates high availability and failover because if a component
                              		  fails, a secondary server will take over the functionality lost by that failed
                              		  component.

All Unified
                              		  CCX servers within the cluster are configured identically and installed with
                              		  the same features. One server is designated the active server .

### Unified CCX Active
                           	 Server

Support for high
                                             			 availability and remote servers is available only in multiple-server
                                             			 deployments.

The Unified
                                 		  CCX active server makes global decisions for the cluster and keeps track of
                                 		  calls in the CSQs, agent states (if Unified CCX is installed) and generating
                                 		  historical detail records.

Only one server in
                                             			 the cluster can be the active server at any given time.

If the
                                 		  active server fails, the Unified CCX provides automatic failover to the standby
                                 		  server. If the active server fails (for example, in the event a hardware
                                 		  failure occurs or the Unified CCX Engine process terminates), some calls being
                                 		  handled by the server are lost. The lost calls are restricted to those being
                                 		  handled by the system (those in the IVR stage or in queue). Calls answered by
                                 		  agents continue to remain live even though related data on the agent desktop is
                                 		  lost. When the standby server takes over as the new active server, call
                                 		  processing continues.

A Unified
                                 		  CCX cluster consists of the one or more servers (nodes) that run Unified CCX
                                 		  components in your Unified CCX deployment.

Receives
                                          				  updates about cluster status and subsystem states.

Java code that
                                          				  interacts with Platform Service Manager and implements internode communication
                                          				  on behalf of the cluster. It detects availability of the other nodes,
                                          				  components and services, provides consistent cluster view, and dynamically
                                          				  elects a master service.

The CVD has
                                 		  two interfaces:

Node Manager
                                                					 to monitor and control local processes

Cluster
                                                					 Manager publisher or subscriber to communicate with local applications, such as
                                                					 Engine and Application Administration

One that
                                       				monitors outside the node and communicates with other nodes in the cluster

## Unified CCX
                        	 Engine

The
                              		  Unified CCXEngine enables you to run multiple applications to handle Unified CM Telephony calls or HTTP requests.

The
                              		  Unified CCXEngine uses the Unified CM Telephony subsystem to request and receive services from the Computer Telephony
                              		  Interface (CTI) manager that controls Unified CM clusters. The Unified CCXEngine is implemented as a service that supports
                              		  multiple applications.

You can
                              		  use a web browser to administer the Unified CCXEngine and your Unified CCX
                              		  applications from any computer on the network. Unified CCX provides you the
                              		  following two web interfaces:

Unified CCX
                                    				Administration web interface— Used to configure system parameters, subsystems,
                                    				view real-time reports that include total system activity and application
                                    				statistics, and so on

Unified
                                    				CCXServiceability web interface— Used to view alarm and trace definitions for
                                    				Unified CCX services, start and stop the Unified CCX Engine, monitor Unified
                                    				CCX Engine activity, and so on

Ensure that the popup blocker is disabled on your browser.

Allows
                                       				  Unified CCX to configure and manage Chat and Email.

## Set Up Unified
                        	 CCX

After you
                              		  install the Unified CCX system and perform the initial setup as described in Cisco Unified
                                 			 Contact Center Express Installation Guide , you can start provisioning
                              		  and configuring the system:

Provisioning is the
                                    				process of allocating resources and devising strategies for using the resources
                                    				to support the needs of your business.

Configuring is the
                                    				process of making applications available to the Unified CCX system.

### Provision Telephony
                           	 and Media Subsystems

The
                                 		  Unified CCX telephony and media subsystems manage telephony and media resources
                                 		  and communicate with supporting telephony and media systems.

Depending
                                 		  on the Unified CCX applications you plan to use, you need to provision some or
                                 		  all of the following subsystems:

- Unified CM Telephony— The Unified CM Telephony subsystem controls the Unified CM Telephony resources for the Unified CCX system.

Caution

While Unified CM
                                             			 supports Unicode characters in first and last names, those characters become
                                             			 corrupted in Unified CCX Administration web pages for Real-Time Reporting.

- Cisco Media— The Cisco
                                    			 Media subsystem controls the CMT media resources for the Unified CCX system.

- MRCP ASR— The MRCP ASR
                                    			 subsystem controls the ASR media resources for the Unified CCX system.

- MRCP TTS— The MRCP TTS
                                    			 subsystem controls the TTS media resources for the Unified CCX system.

### Configure Unified CCX Subsystems

You need to provision your Unified CCX subsystems to enable
                                 		  the Unified CCX Engine to run multiple applications to handle Unified
                                 		  Communications calls or HTTP requests.

You need to configure a particular subsystem only if you are using
                                             			 Unified CCX applications that require it and which are installed and activated
                                             			 using the appropriate license.

To continue the Unified CCX system configuration process, connect to the Unified CCX Administration web interface and perform
                                 the task in the links listed in the Related Topics section.

#### Provision Unified
                              	 CCX Subsystem

If you
                                    		  have purchased any of the three versions of Unified CCX, you must provision the
                                    		  Unified CCX subsystem.

RmCm Provider

The Resource
                                             				Manager (RM) of the Unified CCX system uses a Unified CM user
                                             				(called a Unified CM Telephony provider) for monitoring agent phones, controlling agent states, and
                                             				routing and queueing calls.

Resources

Agents that answer calls are also called resources . After you create a resource group, you must assign agents (resources) to that group.

Resource Groups

Collections of
                                             				agents that your CSQ uses to handle incoming calls. To use resource group-based
                                             				CSQs, you must specify a resource group.

Skills

Customer-definable labels that are assigned to agents. You can route incoming calls to agents who have the necessary
                                             skills or set of skills to handle the call.

CSQs

After you assign
                                             				an agent to a resource group or assign skills to an agent, you need to
                                             				configure the agent for the CSQ to which the agent will be assigned.

Agent-Based Routing
                                                				  Settings

You can
                                             				configure Automatic Work and Wrapup Time settings for the agent-based routing
                                             				feature from the Agent-Based Routing Settings page.

Teams

If you want to
                                             				create or associate teams with various agents, CSQs, and supervisors, you need
                                             				to configure team settings.

#### Provision Additional
                              	 Unified CCX Subsystems

The
                                    		  additional Unified CCX subsystems provide 
                                    		   HTTP, Database, and email features.

HTTP— The HTTP subsystem
                                             				enables Unified CCX applications to respond to requests from a variety of web
                                             				clients.

Database— The Database
                                             				subsystem enables Unified CCX applications to communicate with enterprise
                                             				database servers.

eMail— The eMail subsystem
                                             				enables Unified CCX applications to create and send email.

### View License Information

The initial license configuration is part of the installation of Unified CCX. For more information on obtaining and installing
                                 licenses for Cisco Unified CCX, see Cisco Unified Contact Center Express Install and Upgrade Guide . For more information on licensing, see License Management

### Configure Unified CCX Applications

After you provision the Unified CCX subsystems and view your license
                                 				information, you need to configure Unified CCX applications to interact with
                                 				contacts and perform a wide variety of functions.

To continue the Unified CCX system configuration process, connect to the
                                 				Unified CCX Administration web interface and manage the following tasks:

Available Applications

Manage Scripts Prompts, Grammars, and Documents

#### Available
                              	 Applications

There are
                                    		  several types of applications you can configure for Unified CCX:

Script
                                          				applications perform such functions as receiving calls, playing back prompts,
                                          				receiving caller input, transferring calls, and queueing calls.

The Busy
                                          				application simulates a busy signal.

The
                                          				Ring-No-Answer application simulates a ringtone.

After
                                    		  adding a Unified CCX application, you need to define a trigger so
                                    		  that this application can respond to telephone calls and HTTP requests.
                                    		  Triggers are specified signals that invoke application scripts in response to
                                    		  incoming contacts.

#### Manage Scripts
                              	 Prompts, Grammars, and Documents

The
                                    		  process of configuring Ciscoscript applications includes uploading Unified CCX
                                    		  scripts and prerecorded prompts, installing grammars and customized languages,
                                    		  and adding triggers to applications.

Depending
                                    		  on your particular Unified CCX implementation, you may need to perform most or
                                    		  all of the following tasks to configure a Ciscoscript application:

- Manage scripts—Ciscoscript
                                       			 applications are based on scripts that you must upload to the repository and
                                       			 make available to the Unified CCX system.

- Manage prompts—Many
                                       			 applications make use of prerecorded prompts, stored as .wav files, which are
                                       			 played back to callers to provide information and elicit caller response. You
                                       			 must upload these .wav files to the repository and make them available to the
                                       			 Unified CCX system.

- Install grammars—A grammar is a
                                       			 specific set of all possible spoken phrases and Dual Tone Multi-Frequency
                                       			 (DTMF) digits to be recognized by Unified CCX applications and acted upon
                                       			 during run time. The Unified CCX system uses specific grammars when recognizing
                                       			 and responding to caller responses to prompts. You must store these grammars in
                                       			 a directory to make them available to the Unified CCX system.

- Install customized Unified
                                       			 CCX languages—Language packs, such as American English and Canadian French, are
                                       			 installed with Unified CCX.

### Configure Unified CCX Historical Reporting

When you install the Unified CCX system, the installation
                                 		  process creates a database named db_cra. This database contains:

- Information for historical
                                    			 reports, including Unified CCX configuration information, stored procedures,
                                    			 and some call statistics

- The ContactCallDetail
                                    			 table, which is the main table for call statistics

To conclude the Unified CCX system configuration process,
                                 		  connect to the Unified CCX Administration web interface and perform the
                                 		  following Historical Reporting Configuration tasks:

Step 1

Define the maximum number of database connections for report
                                          			 client sessions.

Step 2

Assign historical reporting capability to users.

Step 3

Configure the Daily Purge Schedule and specify notification
                                          			 parameters.

## Manage Unified
                        	 CCX

To manage
                              		  your Unified CCX, you must first provision and configure it. The day-to-day
                              		  administration of the Unified CCX system and datastores consist of many tasks,
                              		  such as:

- Starting and stopping the Unified CCX
                                 			 Engine and processes.

Support for
                                                				  high availability and remote servers is available only in multiple-server
                                                				  deployments.

| Note | Cisco Unified Communications Manager was previously
                                                				  known as Unified Call Manager. This guide uses Cisco Unified Communications
                                                   					 Manager at the first occurrence and Unified CM for
                                                				  later occurrences. |
|---|---|

| Note | Support for
                                                				  high availability and remote servers is available only in multiple-server
                                                				  deployments. |
|---|---|

| Note | The dedicated outbound IVR ports for a campaign is the number of IVR ports that you want to reserve for a campaign from the
                                                      total number of CTI ports available in the outbound call control group. |
|---|---|

| Note | The Unified CCX
                                             			 Enhanced package and the Unified CCX Premium package are provisioned in the
                                             			 same way. |
|---|---|

| Note | Support for high
                                          			 availability and remote servers is available only in multiple-server
                                          			 deployments. |
|---|---|

| Note | Support for high
                                             			 availability and remote servers is available only in multiple-server
                                             			 deployments. |
|---|---|

| Note | Only one server in
                                             			 the cluster can be the active server at any given time. |
|---|---|

| Note | Ensure that the popup blocker is disabled on your browser. |
|---|---|

| Caution | While Unified CM
                                             			 supports Unicode characters in first and last names, those characters become
                                             			 corrupted in Unified CCX Administration web pages for Real-Time Reporting. |
|---|---|

| Note | You need to configure a particular subsystem only if you are using
                                             			 Unified CCX applications that require it and which are installed and activated
                                             			 using the appropriate license. |
|---|---|

| Step 1 | Define the maximum number of database connections for report
                                          			 client sessions. |
|---|---|
| Step 2 | Assign historical reporting capability to users. |
| Step 3 | Configure the Daily Purge Schedule and specify notification
                                          			 parameters. |

| Note | Support for
                                                				  high availability and remote servers is available only in multiple-server
                                                				  deployments. |
|---|---|