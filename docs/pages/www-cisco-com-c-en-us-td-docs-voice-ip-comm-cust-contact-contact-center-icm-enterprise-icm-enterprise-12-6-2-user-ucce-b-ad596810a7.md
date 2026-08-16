---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-ucce-b-ad596810a7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/ucce_b_1262_outbound_options_guide/ucce_m_1262_architectural-overview.html
retrieved_at: 2026-08-16T20:32:35.688282+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

Updated: August 19, 2025

Chapter: Architectural Overview

## Chapter: Architectural Overview

# Architectural Overview

## Unified CCE Software
                        	 Overview

This section
                              		  provides a high-level overview of Unified CCE software, which must be installed
                              		  and configured before installing Outbound Option.

Before installing
                              		  Unified CCE software, the virtual machine guests must have the Microsoft
                              		  Windows operating system and, for some components, Microsoft SQL Server
                              		  database management software installed. Also, ensure that there is enough disk
                              		  space available on each system to install the Unified CCE component.

See the Compatibility Matrix for
                                 			 Unified CCE for information on operating system and software
                              		  requirements.

Unified CCE software
                              		  contains the following components:

Router : The component of
                                    				the Central Controller that makes routing decisions. It gathers and distributes
                                    				data to and from remote sites.

Logger : The component of
                                    				the Central Controller that controls the central database.

Administration & Data
                                       				  Server : Known as the Admin Workstation in previous releases, the
                                    				Administration & Data Server is the user interface for Unified CCE
                                    				software. The Administration & Data Server can be located at any central or
                                    				remote site. It allows users to monitor call handling within the system and
                                    				change configuration data or routing scripts.

Peripheral Gateway : The
                                    				interface between the Unified CCE platform and third-party hardware in each
                                    				call center, such as an ACD. A Peripheral Gateway (PG) is typically located at
                                    				the call center.

Install the
                              		  Peripheral Gateway from the PG Setup program; install the other components from
                              		  the Web Setup program.

Together, the Router
                              		  and Logger compose the Central Controller and are installed at a central site.
                              		  At least one Peripheral Gateway is typically installed in each call center.
                              		  Administration & Data Servers can be installed at a central site, a call
                              		  center, or at a separate admin site.

## Outbound Option Software Components

This section provides details about the server processes of the Outbound Option
                              system:

Campaign Manager : Manages lists.

Outbound Option Import : Reads customer import files and generates
                                    database lists.

Outbound Option Dialer : Maximizes the resources in a contact center
                                    by dialing several customers per agent. This component resides on the PG server, where it
                                    performs the following actions:

Dials customers

Reserves agents

Performs call classification

Calculates agent availability

Keeps outbound dialing at a level where the abandon rate is below the maximum allowed
                                          abandon rate

The Outbound Option components provide a user interface where configuration data can be
                              entered. The Outbound Option server processes use this configuration data to configure
                              campaigns.

### Outbound Options Component Relationships

The following figure shows the component relationships within an Outbound Option
                                 deployment that uses the SIP Dialer. These relationships include the Unified CCE software
                                 components that Outbound Option uses.

### Outbound Option
                           	 Campaign Manager Component

The Campaign Manager
                                 		  component, which resides on the Logger, is responsible for:

Managing when a
                                       				campaign runs.

Maintaining
                                       				system and dialer configurations.

Deciding which
                                       				contact records to retrieve from a campaign based on configurable query rules
                                       				and delivering those contact records to dialers.

Records for
                                       				callbacks are sent to the Dialer only when agents are logged in, and are
                                       				controlled by registry values as described in Chapter 5, "Configuration of
                                       				Campaigns and Imports".

Distributing
                                       				configuration data to the import process and all available dialers in the
                                       				system.

Collecting
                                       				real-time and historical data and sending it to the Router.

Managing the Do
                                       				Not Call list to ensure that no records on it are sent to the Dialers.

Performing
                                       				record queries based on the following order:

Callback

Retry Zone1

Retry Zone2

Pending
                                             					 Zone1

Pending
                                             					 Zone1 DST

Pending
                                             					 Zone2

Pending
                                             					 Zone2 DST

Based on this
                                       				order, the priority for the Retry record is higher than for the Pending record.
                                       				However, the Pending record priority can be set above the Retry record by
                                       				setting the "PendingOverRetryEnabled" registry key to 1 (default
                                       				is 0). If the value is set to 1 , the
                                       				record query order would be:

Callback

Pending
                                             					 Zone1

Pending
                                             					 Zone1 DST

Pending
                                             					 Zone2

Pending
                                             					 Zone2 DST

Retry Zone1

Retry Zone2

For more
                                 		  information, see Appendix A, "Registry Settings".

### Outbound Option Import Component

The Outbound Option Import component resides on the Unified CCE  Logger. The Import component imports a  Contact list, which
                                 contains the phone numbers that
                                 Outbound Option dials. In addition, the Import component uses the scheduling configured in the Outbound
                                 Option components to process imports that are scheduled for a particular date and time.

When the Import component processes an import, the following steps
                                 occur:

Imports a Contact list into a table.

Builds a dialing list for a campaign.

Performs region prefix matching.

### Outbound Option Dialer Component

The Outbound Option SIP Dialer component, which resides on the PG server, performs the
                                 following actions:

Dials customers using the voice gateways.

Reserves agents through the Media Routing (MR) interface.

Performs call classification.

Calculates agent availability by monitoring campaign skill groups through the CTI Server interface to the agent PG.

Transfers answered customer calls to reserved agents.

For Outbound campaigns, the Voice Gateway handles functions such as dialing, call control, and Call Progress Analysis (CPA).

The following summarizes SIP Dialer features:

Use the voice gateway or Cisco Unified Border Element (CUBE) dial peers and Unified SIP Proxy routing policies for outbound call routing.

No need to configure Unified CM translation pattern to support Campaign Automatic Number Identification (ANI).

Perform CPA at gateway DSP resource.

Unlike the physical CUBE, virtual CUBE does not have DSPs and cannot support CPA. Add a dedicated physical gateway for your
                                                   outbound traffic if you need CPA.

The following summarizes CPA support:

With Voice Gateway (T1/E1), CPA supports G.711 (both a-law and mu-law) and G.729 codecs.

With CUBE (IP-IP) flows, CPA only supports G711 (both a-law and mu-law).

With Outbound Option SIP dialer, CPA only supports G711 (both a-law and mu-law).

No need to configure dialer port on Unified CM.

The dialer does not need to be in proximity of the voice gateway.

Supports warm standby architecture.

Requires one MR PIM for MR PG.

Only connected outbound calls, which are transferred to agents or VRU, go through Agent PG and Unified CM.

Call Throttling supports 60 CPS per dialer.

Supports 3000 dialer ports.

These performance numbers can vary depending on the details of your deployment and your system configuration. To accurately
                                             size your Outbound deployment, use the Cisco Unified Collaboration Sizing Tool (Unified CST) available at https://tools.cisco.com/cucst/faces . For detailed instructions, see the online Help system for this tool.

The Unified CST is available to Cisco internal employees and Cisco partners, and proper login authentication is required.

#### Dialer Port Allocation

The dialer component reserves agents when it sees agents have become available. The
                                    Dialer requests skill group statistics from the agent PG every two seconds and attempts
                                    to reserve agents based on the number of available agents and the number of dialers active
                                    for this PG.

Each dialer checks agent availability to make reservation requests based on the skill group
                                    statistic refreshes that occur every two seconds. When skill groups for multiple campaigns
                                    are active for one or more of the same agents, then one campaign always reserves that
                                    agent or agents. You can avoid this situation by scripting the reservation scripts to queue
                                    reservation calls using the same mechanism that is described for queuing personal callback
                                    reservation requests. This resolution ensures a more even distribution of calls for active
                                    campaigns that share a common agent pool.

For example, in the following scenario where two campaigns are in
                                    progress:

Campaign 1 has four available agents and is dialing two lines per agent, which has a
                                          relative weight of eight (two lines each for four agents).

Campaign 2 has one available agent, but is dialing at four lines per agent, which has
                                          a relative weight of four (four lines for one agent).

To dial customers for all available agents requires 12 ports, but only 9 ports are available.

The results:

Campaign 1 gets 2/3 of the remaining ports, or six of the remaining ports.

Campaign 2 gets 1/3 of the remaining ports, or three of the remaining
                                          ports.

Each  dialer begins dialing using the ports assigned to it, and assigns additional
                                          ports to the campaigns when new ports become available.

#### Port Allocations for Campaign Modes

Preview, Predictive, and Progressive campaigns require at least two ports to place
                                    calls because they require at least one port to reserve the agent and one port to dial the
                                    customer. Because campaigns are shared across active dialers that service a PG, this maximum
                                    number of active campaigns applies to the PG.

Transfer to VRU and Direct Preview calls only require one port. Transfer to VRU calls do
                                    not reserve the VRU port before dialing, and Direct Preview calls use the agent's phone to
                                    place the call.

#### Transfer to Agent Call Flow: SIP Dialer with SIP Proxy

The following figure illustrates a Transfer to Agent Call Flow in a deployment with a
                                    SIP Dialer that is connected to a SIP Proxy.

1.   An agent campaign starts. Customer records are delivered to
                                    the Dialer.

2 to 5.  An agent is reserved with a virtual placeholder call.

6 to 7.The dialer asks the gateway (via proxy) to place a call, and it does.

8. The Voice Gateway performs Call Progress Analysis and detects live voice. Media is terminated at the VGW until the CPA
                                    completes.

9. The dialer is notified and asks the voice gateway (via proxy) to transfer the call to the agent.

10. The  Voice Gateway sets up the customer call with the voice agent (via proxy) and the UC Manager.

#### Transfer to VRU Call Flow: SIP Dialer with SIP Proxy

The following figure illustrates a Transfer to VRU Call Flow in an Outbound Option
                                    deployment with a SIP Dialer connected to a SIP Proxy.

An unattended VRU campaign starts. Customer records are delivered to
                                          the Dialer.

The Dialer asks the SIP Proxy to forward an invitation to an available gateway to start a
                                          call.

The Gateway places the call.

Voice Gateway does Call Progress Analysis and detects an answering machine. The Dialer
                                          is notified.

The Dialer asks the MR PG where the VRU is.

MR PG forwards the request to the Router.

The routing script identifies the VRU and notifies the MR PG.

The MR PG forwards the route response to the Dialer.

The Dialer notifies the voice gateway to transfer the call to the VRU.

The Gateway starts the transfer to the SIP Proxy, and the SIP Proxy forwards the
                                          invitation to the Unified CM . Unified CM forwards the call invitation to the VRU, and media is
                                          set up between the Gateway and the VRU.

#### Transfer to Agent - SIP Dialer with No SIP Proxy

The following figure illustrates a transfer to agent call flow in an Outbound Option
                                    deployment with a SIP Dialer without a SIP Proxy.

Import is scheduled and campaign starts. Records are delivered to Dialer.

The Dialer looks for an available agent via the Media Routing Interface.

MR PG forwards the request to the Router.

The routing script identifies an agent and responds to the MR PG.

Media Routing PIM notifies the Dialer that the agent is available.

Dialer signals the gateway to place a call to the customer.

The Gateway places a call to the customer, and the Dialer is notified it is
                                          trying.

Call Progress Analysis is performed at the gateway. Voice is detected, and Dialer is
                                          notified.

The Dialer asks the voice gateway to transfer the call to the reserved agent by its
                                          agent extension.

The Gateway directs the call to the agent via Unified CM using dial peer configuration to locate the Unified CM . Media is set up between the Gateway and the agent’s
                                          phone.

### Peripheral Gateway (PG)

The peripheral gateways (PGs) are redundant in a SideA - SideB configuration; one
                                 side is active and the other side runs in standby while waiting to be activated. The dialers are co-located with the agent
                                 PGs with the dialers running in a
                                 peer model.

### Agent PG

The agent PG is a primary data collection point for agent and skill group statistics. The
                                 Dialer connects to the agent PG through the CTI Server interface to monitor skill
                                 groups associated with campaigns. It uses the number of working
                                 agents and available agents to determine when to reserve agents and when to dial for agent
                                 campaigns. For 'Transfer to VRU' campaigns, the Dialer monitors the number of calls queued to determine when the Dialer component
                                 has reached the 
                                 limit of VRU ports for this campaign as
                                 specified  in the campaign skill group.

The agent PG also monitors all calls placed to the Dialer ports . The Dialer uses the PG representation of the call to push
                                 customer call context to the agent. The Dialer also provides information about call results so that the PG can report Outbound
                                 Option statistics for the campaign skill group.

Campaign statistics and skill group statistics both report the number of Outbound Option calls that reach agents. The Campaign
                                 Manager collects and reports campaign statistics. The PG collects and reports skill group statistics. The two reports can
                                 differ by a call or two for a given half hour, but they are reconciled at the end of the campaign.

### Media Routing
                           	 PG

The Media Routing PG (MR PG) is the interface the Dialer uses to make route requests to the Central Controller to find and
                                 reserve available agents. Each Dialer uses its own MR controller (MR PIM), and a separate dialed number is configured to differentiate
                                 requests for different campaign skill groups for agent campaigns.

For a quick reference on configuration limits and scalability constraints, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

### VRU

The Dialer uses the VRU for unassisted treatment of customer calls depending on campaign
                                 configuration for abandoned calls, answering machine treatment in an agent campaign, or for
                                 unassisted transfer to VRU campaigns.

VRU scripting is flexible in playing prompts to the user and collecting other  data. It can also be a queue point to wait
                                 for the next available agent.

Partition the ports accordingly when using the same VRU for inbound and outbound
                                 campaigns. For inbound calls, do not use ports allocated for the transfer to VRU feature. For
                                 VRU ports shared between inbound and outbound applications, the Dialer might transfer
                                 customers to a VRU which does not have any available ports left. In this case, the called
                                 party hears a fast busy signal or a 'ring no answer' message. To avoid this situation, ensure that the VRU has enough ports
                                 for both inbound and outbound traffic.

### Administration and Data Server: Configuration

Use the Administration & Data Server configuration tools to configure the
                                 Unified CCE system. Enable the tools for configuring Outbound Option
                                 by editing the Administration & Data Server setup.

### Cisco Unified Intelligence Center

Cisco Unified Intelligence Center (CUIC) is the standard Unified
                                 CCE reporting interface.

For details about Unified Intelligence Center, see the Cisco Unified Intelligence Center Documentation .

### Dialer
                           	 Reports

The Outbound Option
                                 		  Dialer reports provide information about the dialer platform. These predefined
                                 		  templates include information about performance and resource usage. The
                                 		  templates also enable you to determine whether you need more dialer ports to
                                 		  support more outbound calls.

For more
                                 		  information, see chapter 6, "Administrative and Supervisory Tasks".

### Outbound Option
                           	 Agent Desktops

Three desktops are available for the Outbound Option: CTI Object Server (CTI OS), the Cisco Agent Desktop (CAD), and Cisco
                                 Finesse.

Desktops available for the Outbound Option: Cisco Finesse.

Cisco Finesse supports Outbound Option-enabled agents.

#### Cisco Finesse

Cisco Finesse provides the following applications and tools:

A web-based desktop application for agents and supervisors. Agents and supervisors access their desktops by entering the following
                                          URL in their browsers: http:// hostname , where hostname is the hostname or IP address of the Finesse server.

A web service that provides contact center agent desktop functionality through a REST-like interface.

An administration console for configuring system settings, desktop layout, wrap-up reasons, and reason codes. Administrators
                                          access this console by entering the following URL in their browsers: http:// hostname /cfadmin, where hostname is the hostname or IP address of the primary Finesse server.

Cisco Finesse supports   Outbound Option as follows:

Finesse supports Progressive mode, Predictive mode, Preview mode, and Direct Preview mode.

You can schedule both regular callbacks and personal callbacks.

Agents who are on Progressive or Predictive Outbound Option  calls do not appear in the Talking - Outbound column of the Queue
                                                Statistics gadget on the supervisor desktop. This number only includes agents who are talking on outbound calls placed by
                                                those agents.

### Outbound Option Extended Call Context Variables

The Outbound Option Dialer uses CTI Extended Call Context (ECC) variables to exchange
                                 information with the Finesse desktop. The following table
                                 lists the ECC variables Outbound Option uses.

ECC Variable

Description

BACampaign

Indicates the name of the Outbound Option campaign to which the call belongs.

BAAccountNumber

Identifies a customer account number and can be used by the desktop application to
                                             perform a database lookup to obtain more customer data. This ECC variable is
                                             displayed only if the data was available in the customer import file.

BAResponse

Multipurpose placeholder that sends data from the Finesse desktop to the Outbound Option Dialer. This variable responds to the reservation call to schedule and cancel callbacks, and to changes
                                             to the callback phone number. See the following rows for more information about BAResponse.

On the Finesse desktop, when an agent uses the Accept , Reject , and Reject-Close buttons in Preview mode, BAResponse is set to one of the following values:

Accept : Accepts the current preview call.

Reject : Rejects the current preview call. Sets record to "R" for retry.

Reject-Close : Rejects the current preview call and closes the record so it will not be called again.

On the Finesse desktop, an agent in Preview mode can respond with the following options:

Agent Action

BAResponse setting

Description

Accept

Accept

Accepts the current preview call.

Decline > Reject

Reject

Rejects the current preview call. Sets record to "R" for retry.

Decline > Close

Reject-Close

Rejects the current preview call and closes the record so it will not be called again.

When an agent uses the Callback button, BAResponse is set
                                             to one of the following values:

Spaces are relevant and must be included in these
                                                         commands.

Callback mmddyyyy hh:mm: Schedules a callback for the indicated date and time

Callback Cancel: Cancels a previously scheduled callback for this call

P#xxxxxxxxxxxxxxxxxxxx: Changes the callback phone number to the number specified
                                                   by xxxx

For Preview modes, cancel the reservation call by clicking Reject .

For Predictive mode, cancel the reservation call by clicking Not
                                                Ready and then hang up the reservation call.

For Direct Preview calls, any connected customer call is classified as
                                             VOICE by the Dialer (default). To reclassify the call result, the agent can click the following buttons:

Voice : To reclassify a call as a voice call, set the BAResponse variable to REX_VOICE. Enable the Voice button only after pressing
                                                   one of the other buttons first. Pressing one of the other buttons first enables an agent to reclassify the call if needed.

Answering Machine : To reclassify the call as an answering machine
                                                   call, set the BAResponse variable to REX_ANS_MACHINE.

Fax/Modem : To reclassify the call as a fax/modem call, set the
                                                   BAResponse variable to REX_FAX.

Invalid :
                                                   To reclassify the call as an invalid call, set the BAResponse variable to
                                                   REX_INVALID.

BAResponse for answering machine detection in a transfer to VRU campaign

For answering machine detection on a transfer to VRU campaign, the
                                             BAResponse variable is evaluated to carry the CPA result of the customer call. Two new
                                             IF node configurations are supported:

Call.BAResponse= "CPA_AnswerMachine"

Call.BAResponse= "CPA_Voice"

These IF nodes route to separate External Scripts to allow for different treatment
                                             depending on whether a voice or an answering machine was detected.

BAStatus

Contains two characters indicating the mode and direction of the Outbound
                                             Option Dialer initiated call. The first character identifies the call
                                             mode:

R: Reservation call, Predictive mode

R: Reservation call, Predictive mode

G: Reservation call, Progressive mode

P: Reservation call, Preview mode

D: Direct Preview reservation call

C: Customer call

A: Reservation call, personal callback.

During a reservation call, the first character is P, R, G, or A.

When a customer call is transferred to an agent, the first character is C.

The second character of BAStatus indicates the call
                                             direction:

O: Outbound

I: Inbound

B: Blended

BADialedListID

Unique key identifying a specific customer record within the Dialing List table in
                                             the Outbound Option private database.

BATimeZone

Indicates the GMT offset, in minutes, for the customer’s time zone and obtains the
                                             customer’s local time. The format of this ECC variable is +/-#####.

This field’s first character is either a positive or negative sign,
                                             followed by 5 digits. For example:

This example indicates that the customer is one hour behind GMT:

BATimeZone = -00060

This example indicates that the customer is two hours ahead of GMT:

BATimeZone = +00120

BABuddyName

Contains the customer’s last and first name separated by a comma, which is compiled
                                             using the imported LastName, FirstName that was configured on the Import Rule Definition
                                             tab page.

### Desktop Button
                           	 Behavior

The following table
                                 		  explains the desktop button behavior when a call is placed using Outbound
                                 		  Option.

For more information
                                 		  about dialing modes, refer to Dialer Reports .

Dialing
                                             						Mode / Other Conditions

Call
                                             						Description

Buttons
                                             						Enabled

Preview

Reservation calls: Dialer places the call and agent is
                                             						available.

Accept , Reject , and Reject-Close buttons are enabled if the reservation call has not yet been accepted.

Initial
                                             						customer calls: Agent accepts the call and Dialer calls the customer.

No buttons
                                             						are enabled if the customer does not answer the call.

Transferred customer calls: Agent is talking to a customer.

Callback button is enabled.

Predictive and
                                                						  Progressive

Reservation calls: Dialer places the call and agent is
                                             						available.

No buttons
                                             						are enabled.

Initial
                                             						customer calls: Dialer calls the customer.

No buttons
                                             						are enabled if the customer does not answer the call.

Transferred customer calls: Agent is talking to a customer.

Callback button is enabled.

Direct Preview

Reservation calls: Dialer places the call and agent is
                                             						available.

Accept , Reject , and Reject-Close buttons are enabled if the reservation call has not yet been accepted.

Initial
                                             						customer calls: Agent accepts the call and calls a customer.

No buttons
                                             						are enabled if the customer does not answer the call.

Transferred customer calls: Agent is talking to a customer.

Callback , AnsMach , Fax ,
                                             						and Invalid buttons are enabled.

Personal Callback

BAStatus
                                             						is set to A and O or A and B for a reservation call.

Accept and Reject buttons are enabled, if the reservation call has not
                                             						been accepted yet.

Initial
                                             						customer calls: Agent accepts the call and calls a customer.

No buttons
                                             						are enabled if the customer does not answer the call.

Transferred customer calls: Agent is talking to a customer.

Callback button is enabled.

## Scripts for Outbound Option

Outbound Option uses Unified CCE scripting configured on the Administrative Workstation to manage campaigns.

There are two types of scripts:

Administrative scripts to enable, disable, or throttle campaign skill groups for outbound campaigns.

Agent reservation routing scripts to reserve agents for specific outbound campaigns and personal callbacks. These scripts
                                 can also transfer calls to VRU campaign or transfer calls to non-VRU campaigns for answering machine or abandons.

## Fault Recovery

This section describes Outbound Option behavior when specific components fail and recover.

### Outbound Option High Availability

If you use the optional Outbound Option High Availability deployment, the active Outbound Option components manage all updates
                                 to the database such as importing new records and updating Dialing Lists. This process of managing updates to the database
                                 is also applicable when you use the Outbound Option API for importing records.

The data is replicated to the standby Outbound Option database by the Campaign Manager process running on the standby side.

The standby Campaign Manager connects to a file share that is automatically created via Web setup when Outbound Option High
                                 Availability is selected on the active side. The file share contains a series of files representing Imports, API-generated
                                 imported files, and updates to the outbound database.

Replication data is first written to a series of temporary files (extension .tmp), which represent an ongoing operation on
                                 the active side. The temporary files are later renamed to replication files (.repl extension) and are then available for the
                                 standby Campaign Manager for any action. When these files are consumed by the standby Campaign Manager and the standby Outbound
                                 Option database is brought in sync, they are deleted from the active side.

In a process or network failure, the active Campaign Manager fails over, and the standby campaign Manager attempts to become
                                 active. If the formerly active Logger file share is still reachable and replication is not fully synchronized, the Campaign
                                 Manager continues to process the replication files until it is synchronized, and then goes active. Dialers then connect to
                                 the newly active side and the operations continue, using the data that was replicated. All the updates to the database are
                                 again made by the newly active Campaign Manager, and data is replicated to the standby side. If a Logger server goes down,
                                 Outbound Option database updates the pending records until the server recovers. That data is then replicated to the database.

If a Logger side remains down for a sustained period while the active Logger continues to dial, the replication file share
                                 continues to store all the data required to bring the other database into synchronization.

There may be substantial amount of data to be managed depending upon the number of imports, the rate at which the system is
                                 Dialing, and the duration of downtime for the Logger. Therefore, the drive that the Logger service resides on should contain
                                 enough space to handle such an event.

You can consider the following estimate for drive space:

A 1 million record import with a single phone number, name, and account number takes approximately 120 MB of replication drive
                                       space. Additional phone numbers and optional columns increases this usage.

Dialing a million records results in 3 times as many updates, although the amount of data is smaller. However, a safe estimate
                                       is approximately 360 MB of replication drive space.

### Campaign Manager
                           	 Fault Recovery

Campaign Manager is an MDS client for the router and is enabled on the router. The duplex structure for high availability
                                 requires a Side B router that replicates Side A. When Campaign Manager on the Side A fails over, the Campaign Manager on Side
                                 B is moved to Active state.

The Campaign Manager
                                 		  resides on the Logger.

If the Unified CCE Router and MR PG are still accessible when the Campaign Manager process shuts down, the Dialer can still
                                 reserve agents for an agent campaign. In this case, the Dialer continues to dial contacts and saves the results until it processes
                                 all the cached calls in memory.

After processing all its cached records, the Dialer cannot dial more calls until the Campaign Manager process recovers and
                                 sends it more records.

When the Campaign Manager is back online, it updates call results based on the information it receives from the Dialer. A
                                 few records can be lost when the Campaign Manager is not available. If High Availablity is enabled, CampaignManager resumes
                                 the replication of pending records from the active side to idle side.

### Dialer Fault
                           	 Recovery

You deploy the SIP
                                 		  Dialer in redundant pairs in warm-standby mode. You can have one redundant pair
                                 		  for each Agent PG. To install multiple Dialers, install each on a separate PG
                                 		  VM, but assign them the same Dialer Name.

When the Campaign
                                 		  Manager detects that a Dialer state change from ready to not ready or that the
                                 		  connection from the active Dialer is lost, the Campaign Manager activates the
                                 		  standby Dialer, if there is a standby Dialer in ready state.

For regulatory
                                 		  compliance, the SIP Dialer does not automatically re-attempt calls that were in
                                 		  progress during a failover. Instead, the Dialer sends all active and pending
                                 		  customer records to the Campaign Manager. If the Campaign Manager is not
                                 		  available, the dialer closes them internally.

Active calls are
                                 		  handled as follows:

Canceled if
                                       				the call is not connected.

Abandoned if
                                       				the call is connected but not yet transferred to the agent or VRU.

Continued if
                                       				the call is already transferred and the PG/CG does not fail during that time.

If the standby
                                 		  Dialer does not respond during a set period, the Campaign Manager marks all
                                 		  outstanding records with an Unknown status and returns them to Pending status.

Calls, that were
                                             			 already connected to an agent, continue during failover. However, the Dialer
                                             			 Detail table changes the call from Closed to Dialed (D) state while the agent
                                             			 is still talking to the customer. When the call ends, the Dialer Detail record
                                             			 for that call may show an earlier end time than the actual end of the call.

#### Dialer Redundancy
                              	 in Outbound Option High Availability

The Dialer updates
                                 		the Campaign Manager with the intermediate Dialed (D) state of the customer
                                 		records. This ensures that the Campaign Manager tracks the next set of actions
                                 		for the dialed calls when the active dialer fails and the standby dialer is
                                 		activated.

When the dialer
                                 		calls a customer by sending a SIP Invite, it updates the state of the customer
                                 		record in the Campaign Manager to the D (Dialed) state. The Campaign Manager
                                 		receives the D state message and updates the CallStatus of the record to the D
                                 		state in the DialingList (DL) table.

The Campaign Manager
                                 		again updates the state of the customer record in the DL table and the
                                 		DialerDetail table in the following events:

When the call is
                                          				successful : The Campaign Manager receives a message to close the customer
                                       			 records and it updates the state to the C state.

When the communication
                                          				between the Dialer and Campaign Manager breaks : The Campaign Manager does
                                       			 not receive any message to close the customer records. Here, all the D state
                                       			 records remain in the D state and the A state records move to the U state.

When the communication
                                          				between the dialer and the CTI server breaks : The Campaign Manager receives
                                       			 a close customer record message for all the customer calls that are in progress
                                       			 and updates these records to the C state. Next, the Campaign Manager sends the
                                       			 dialer disconnected status and all the A state records move to the U state and
                                       			 the D state records remain in the D state.

When the communication
                                          				between the dialer, and the SIP gateway (GW), breaks : All the calls that
                                       			 were in progress get disconnected from the phone but the call remains on the
                                       			 Agent Desktop. Campaign Manager receives Close customer record message once the
                                       			 call is released from the Agent Desktop. In this condition, all the D state
                                       			 records moves to C state once the call is released from Agent Desktop and the A
                                       			 state records move to the U state.

When the communication
                                          				between the dialer and the MR PIM breaks : The Campaign Manager receives
                                       			 only the dialer status when the MR interface fails. The ongoing calls continue.
                                       			 When the call is complete, the record is updated to the Closed (C) state.

The callresult
                                 		statistic for records in D state is zero.

## Campaign Manager Congestion Control

The Campaign Manager depends on an internal  dispatch thread to process messages between the Campaign Manager and its registered
                           Dialers.  At times of high call rates, the Campaign Manager cannot process the volume of inbound messages from the Dialers
                           fast enough and the number of messages queued to the dispatch thread, the queue depth , increases.   Under these conditions, the Campaign Manager performance can be decreased, and if the queue depth becomes too
                           large, the Campaign Manager  restarts.

To protect the Campaign Manager from these overload conditions, the Congestion Control feature dynamically reduces the dialing
                           rate of the registered Dialers as the queue depth increases. Congestion control is triggered when the Campaign Manager message
                           queue depth reaches predefined thresholds, the Congestion Levels. As each level is reached, the Campaign Manager instructs
                           all the registered Dialers to reduce their dialing rate by a specified percentage of the configured Port Throttle value, reducing
                           the number of records dialed. As the congestion eases, the Campaign Manager updates the dialers to a lower Congestion Level
                           and a reduced throttle percentage until the system returns to usual state and no additional throttling is applied.

The following table summarizes the Congestion Levels, the queue depth threshold for each level, and the throttle percentage
                           applied at each level.

Congestion Level

Queue Depth Thresholds to Increase Level

Throttle Percentage

Queue Depth Thresholds to Decrease Level

0 - Normal operation

Queue depth is below 3,000 messages

No throttling

N/A

1 - Slightly congested

Queue depth increases to 3,000 messages

25%

Level 1 decreases to Level 0 when queue depth decreases to 1,500 messages

2 - Moderately congested

Queue depth increases to 5,000 messages

50%

Level 2 decreases to Level 1 when queue depth decreases to 2,500 messages

3 - Heavily congested

Queue depth increases to 7,500 messages

90%

Level 3 decreases to Level 2 when queue depth decreases to 4,500 messages

| Note | See Chapters 3-5
                                       		  for detailed information about installing Unified CCE and Outbound Option
                                       		  software. |
|---|---|

| Note | Directly modifying or updating any Logger database tables isn’t supported. |
|---|---|

| Note | Outbound Option can continue to run a campaign while an import is in progress; however,
                                          some of the campaign’s query rules might be disabled. |
|---|---|

| Note | Unlike the physical CUBE, virtual CUBE does not have DSPs and cannot support CPA. Add a dedicated physical gateway for your
                                                   outbound traffic if you need CPA. |
|---|---|

| Note | These performance numbers can vary depending on the details of your deployment and your system configuration. To accurately
                                             size your Outbound deployment, use the Cisco Unified Collaboration Sizing Tool (Unified CST) available at https://tools.cisco.com/cucst/faces . For detailed instructions, see the online Help system for this tool. The Unified CST is available to Cisco internal employees and Cisco partners, and proper login authentication is required. |
|---|---|

| Note | The transfer speed between the Dialer and the VRU is usually under two seconds, but can be longer depending on the network
                                          design and
                                          configuration. |
|---|---|

| Note | Cisco Finesse supports   Outbound Option as follows: Finesse supports Progressive mode, Predictive mode, Preview mode, and Direct Preview mode. You can schedule both regular callbacks and personal callbacks. |
|---|---|

| Note | Agents who are on Progressive or Predictive Outbound Option  calls do not appear in the Talking - Outbound column of the Queue
                                                Statistics gadget on the supervisor desktop. This number only includes agents who are talking on outbound calls placed by
                                                those agents. |
|---|---|

| Note | You can use a custom ECC payload to pass the Dialer ECC Variables to a VRU. |
|---|---|

| ECC Variable | Description |
|---|---|
| BACampaign | Indicates the name of the Outbound Option campaign to which the call belongs. |
| BAAccountNumber | Identifies a customer account number and can be used by the desktop application to
                                             perform a database lookup to obtain more customer data. This ECC variable is
                                             displayed only if the data was available in the customer import file. Note The maximum character length of this ECC variable is 30 characters. | Note | The maximum character length of this ECC variable is 30 characters. |
| Note | The maximum character length of this ECC variable is 30 characters. |
| BAResponse | Multipurpose placeholder that sends data from the Finesse desktop to the Outbound Option Dialer. This variable responds to the reservation call to schedule and cancel callbacks, and to changes
                                             to the callback phone number. See the following rows for more information about BAResponse. |
| BAResponse for Preview mode | On the Finesse desktop, when an agent uses the Accept , Reject , and Reject-Close buttons in Preview mode, BAResponse is set to one of the following values: Accept : Accepts the current preview call. Reject : Rejects the current preview call. Sets record to "R" for retry. Reject-Close : Rejects the current preview call and closes the record so it will not be called again. On the Finesse desktop, an agent in Preview mode can respond with the following options: Agent Action BAResponse setting Description Accept Accept Accepts the current preview call. Decline > Reject Reject Rejects the current preview call. Sets record to "R" for retry. Decline > Close Reject-Close Rejects the current preview call and closes the record so it will not be called again. | Agent Action | BAResponse setting | Description | Accept | Accept | Accepts the current preview call. | Decline > Reject | Reject | Rejects the current preview call. Sets record to "R" for retry. | Decline > Close | Reject-Close | Rejects the current preview call and closes the record so it will not be called again. |
| Agent Action | BAResponse setting | Description |
| Accept | Accept | Accepts the current preview call. |
| Decline > Reject | Reject | Rejects the current preview call. Sets record to "R" for retry. |
| Decline > Close | Reject-Close | Rejects the current preview call and closes the record so it will not be called again. |
| BAResponse for the Callback button | When an agent uses the Callback button, BAResponse is set
                                             to one of the following values: Note Spaces are relevant and must be included in these
                                                         commands. Callback mmddyyyy hh:mm: Schedules a callback for the indicated date and time Callback Cancel: Cancels a previously scheduled callback for this call P#xxxxxxxxxxxxxxxxxxxx: Changes the callback phone number to the number specified
                                                   by xxxx For Preview modes, cancel the reservation call by clicking Reject . For Predictive mode, cancel the reservation call by clicking Not
                                                Ready and then hang up the reservation call. | Note | Spaces are relevant and must be included in these
                                                         commands. |
| Note | Spaces are relevant and must be included in these
                                                         commands. |
| BAResponse for Direct Preview calls | For Direct Preview calls, any connected customer call is classified as
                                             VOICE by the Dialer (default). To reclassify the call result, the agent can click the following buttons: Voice : To reclassify a call as a voice call, set the BAResponse variable to REX_VOICE. Enable the Voice button only after pressing
                                                   one of the other buttons first. Pressing one of the other buttons first enables an agent to reclassify the call if needed. Answering Machine : To reclassify the call as an answering machine
                                                   call, set the BAResponse variable to REX_ANS_MACHINE. Fax/Modem : To reclassify the call as a fax/modem call, set the
                                                   BAResponse variable to REX_FAX. Invalid :
                                                   To reclassify the call as an invalid call, set the BAResponse variable to
                                                   REX_INVALID. |
| BAResponse for answering machine detection in a transfer to VRU campaign | For answering machine detection on a transfer to VRU campaign, the
                                             BAResponse variable is evaluated to carry the CPA result of the customer call. Two new
                                             IF node configurations are supported: Call.BAResponse= "CPA_AnswerMachine" Call.BAResponse= "CPA_Voice" These IF nodes route to separate External Scripts to allow for different treatment
                                             depending on whether a voice or an answering machine was detected. |
| BAStatus | Contains two characters indicating the mode and direction of the Outbound
                                             Option Dialer initiated call. The first character identifies the call
                                             mode: R: Reservation call, Predictive mode R: Reservation call, Predictive mode G: Reservation call, Progressive mode P: Reservation call, Preview mode D: Direct Preview reservation call C: Customer call A: Reservation call, personal callback. During a reservation call, the first character is P, R, G, or A. When a customer call is transferred to an agent, the first character is C. The second character of BAStatus indicates the call
                                             direction: O: Outbound I: Inbound B: Blended |
| BADialedListID | Unique key identifying a specific customer record within the Dialing List table in
                                             the Outbound Option private database. |
| BATimeZone | Indicates the GMT offset, in minutes, for the customer’s time zone and obtains the
                                             customer’s local time. The format of this ECC variable is +/-#####. This field’s first character is either a positive or negative sign,
                                             followed by 5 digits. For example: This example indicates that the customer is one hour behind GMT: BATimeZone = -00060 This example indicates that the customer is two hours ahead of GMT: BATimeZone = +00120 |
| BABuddyName | Contains the customer’s last and first name separated by a comma, which is compiled
                                             using the imported LastName, FirstName that was configured on the Import Rule Definition
                                             tab page. |

| Note | The maximum character length of this ECC variable is 30 characters. |
|---|---|

| Agent Action | BAResponse setting | Description |
|---|---|---|
| Accept | Accept | Accepts the current preview call. |
| Decline > Reject | Reject | Rejects the current preview call. Sets record to "R" for retry. |
| Decline > Close | Reject-Close | Rejects the current preview call and closes the record so it will not be called again. |

| Note | Spaces are relevant and must be included in these
                                                         commands. |
|---|---|

| Dialing
                                             						Mode / Other Conditions | Call
                                             						Description | Buttons
                                             						Enabled |
|---|---|---|
| Preview | Reservation calls: Dialer places the call and agent is
                                             						available. | Accept , Reject , and Reject-Close buttons are enabled if the reservation call has not yet been accepted. |
| Initial
                                             						customer calls: Agent accepts the call and Dialer calls the customer. | No buttons
                                             						are enabled if the customer does not answer the call. |
| Transferred customer calls: Agent is talking to a customer. | Callback button is enabled. |
| Predictive and
                                                						  Progressive | Reservation calls: Dialer places the call and agent is
                                             						available. | No buttons
                                             						are enabled. |
| Initial
                                             						customer calls: Dialer calls the customer. | No buttons
                                             						are enabled if the customer does not answer the call. |
| Transferred customer calls: Agent is talking to a customer. | Callback button is enabled. |
| Direct Preview | Reservation calls: Dialer places the call and agent is
                                             						available. | Accept , Reject , and Reject-Close buttons are enabled if the reservation call has not yet been accepted. |
| Initial
                                             						customer calls: Agent accepts the call and calls a customer. | No buttons
                                             						are enabled if the customer does not answer the call. |
| Transferred customer calls: Agent is talking to a customer. | Callback , AnsMach , Fax ,
                                             						and Invalid buttons are enabled. Note You can
                                                      						revert to voice if you make a mistake. | Note | You can
                                                      						revert to voice if you make a mistake. |
| Note | You can
                                                      						revert to voice if you make a mistake. |
| Personal Callback | BAStatus
                                             						is set to A and O or A and B for a reservation call. | Accept and Reject buttons are enabled, if the reservation call has not
                                             						been accepted yet. |
| Initial
                                             						customer calls: Agent accepts the call and calls a customer. | No buttons
                                             						are enabled if the customer does not answer the call. |
| Transferred customer calls: Agent is talking to a customer. | Callback button is enabled. |

| Note | You can
                                                      						revert to voice if you make a mistake. |
|---|---|

| Note | Calls, that were
                                             			 already connected to an agent, continue during failover. However, the Dialer
                                             			 Detail table changes the call from Closed to Dialed (D) state while the agent
                                             			 is still talking to the customer. When the call ends, the Dialer Detail record
                                             			 for that call may show an earlier end time than the actual end of the call. |
|---|---|

| Congestion Level | Queue Depth Thresholds to Increase Level | Throttle Percentage | Queue Depth Thresholds to Decrease Level |
|---|---|---|---|
| 0 - Normal operation | Queue depth is below 3,000 messages | No throttling | N/A |
| 1 - Slightly congested | Queue depth increases to 3,000 messages | 25% | Level 1 decreases to Level 0 when queue depth decreases to 1,500 messages |
| 2 - Moderately congested | Queue depth increases to 5,000 messages | 50% | Level 2 decreases to Level 1 when queue depth decreases to 2,500 messages |
| 3 - Heavily congested | Queue depth increases to 7,500 messages | 90% | Level 3 decreases to Level 2 when queue depth decreases to 4,500 messages |