---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-design-guide-new-uccx-b-1-d17cf84272
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/design/guide_new/uccx_b_1251su1solution-design-gude/uccx_b_1252solution-design-gude_chapter_0100.html
retrieved_at: 2026-08-16T21:08:00.853199+00:00
---

Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU1

# Solution Design Guide for Cisco Unified Contact Center Express, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Unified CCX Solution Design Considerations

## Chapter: Unified CCX Solution Design Considerations

# Unified CCX Solution Design Considerations

## Core Components Design Considerations

### General Solution Requirements

#### Principal Design
                              	 Considerations for Call Center Sizing

This
                                    		  figure is a general overview of the design considerations for call sizing. For
                                    		  a detailed description of the call center sizing design process, refer to the
                                    		  section on sizing call center resources in the Cisco Unified
                                       			 Contact Center Enterprise Solution Reference Network Design Guide ,
                                    		  available online at the following URL:

http://www.cisco.com/go/ucsrnd

There are
                                    		  similar basic call center sizing considerations and steps for Unified CCE, and
                                    		  they also can be used in sizing a smaller contact center for Unified CCX. This
                                    		  call-sizing approach will provide you with the minimum number of IVR ports to
                                    		  support the total BHCA.

At a minimum,
                                             				plan on enough capacity to replace your existing system. The replacement system
                                             				should perform at least as well as the one it is replacing.

After all of
                                             				the Erlang (C and B) calculations are complete for the call center sizing, any
                                             				changes in queue times or agents will affect the total number of trunks and IVR
                                             				ports required for an Unified CCX solution.

As you
                                             				increase the size of the agent pool, very small changes in the average queue
                                             				time and percentage of queued calls will affect the required number of gateway
                                             				trunks and IVR ports.

Even if you
                                             				perform all of the calculations for a call center, there are still some
                                             				variables that you cannot plan for but that will affect the ports needed on a
                                             				Unified CCX system. For example, one or more agents could call in sick, and
                                             				that would affect the port count and queue time for each call. Just two agents
                                             				calling in sick could increase the port count by over 12 percent. This would
                                             				affect the price of the system and, if not planned for, would affect the
                                             				ability of the call center to meet caller requirements. Properly sizing call
                                             				center resources is integral to designing an effective Unified CCX system.

If all of
                                    		  the call sizing information is available, the next step is to apply Unified CCX
                                    		  sizing limits to the call center requirements. For this step, use the Cisco
                                    		  Unified Communications Sizing Tool, available online at:

http://tools.cisco.com/cucst

The Unified
                                    		  Communications downloadable sizing tools help you with the task of sizing
                                    		  Unified Communications deployments.

#### Preliminary
                              	 Information Requirements

Scope out the
                                             				preliminary configuration information for the Unified CCX server.

Size the
                                             				gateways for the system.

How many IVR
                                             				ports do you need?

How many PSTN
                                             				gateway trunk ports do you need?

How many
                                             				agents will answer incoming calls?

Metric

Description

Average
                                                   					 handle time (AHT)

Average duration (talk time) of a call plus after-call work time, which is the wrap-up time after the caller ends the call.

Average
                                                   					 IVR port usage time

The total
                                                   					 time for prompt playout and/or menu navigation (if any) in the Unified CCX
                                                   					 script. This time should not include the queue time the caller spends waiting
                                                   					 in queue before an agent becomes available. Queue time is calculated using
                                                   					 Erlang-C automatically.

Service
                                                   					 level goal for agents

Percentage
                                                   					 of calls answered by agents within a specific number of seconds.

Busy Hour
                                                   					 Call Attempts (BHCA)

Average
                                                   					 number of calls received in a busy hour.

Grade of
                                                   					 service (% blockage) for gateway ports to the PSTN

Percentage
                                                   					 of calls that get a busy tone (no gateway trunks available) out of the total
                                                   					 BHCA.

All of
                                    		  the metrics in this table are basic call-sizing metrics. After this information
                                    		  is obtained, calculate the number of gateway trunk ports, IVR ports, and agents
                                    		  using standard Erlang B and C calculators.

If the system
                                                			 being designed is a replacement for an existing ACD or an expansion to an
                                                			 installed Unified CCX or Cisco Unified IP IVR system, you might be able to use
                                                			 the historical reporting information from the existing system to arrive at the
                                                			 above metrics.

In
                                    		  addition, call sizing design considerations may vary if the call center is more
                                    		  self-service oriented.

#### Terminology

This figure illustrates the common port types and how they map to Unified CCX.

Call center sizing differentiates the port types as follows:

Gateway or PSTN trunk ports — Handles calls originating from the PSTN. They are purchased separately from Unified CCX.

Queue ports — IVR ports that queue calls (when no agents are available) prior to transferring the caller to an available agent. These
                                          ports are included at no additional cost with Unified CCX. However, they must be sized for proper capacity planning for the
                                          Unified CCX server.

IVR ports — Full-featured IVR ports available with the Cisco Unified IP IVR and Unified CCX Premium product.

If you want additional supporting features, such as automatic speech recognition (ASR), text-to-speech (TTS), email notification,
                                    web server or client functionality, and database operations, you only need to purchase the Premium package. Additional seats
                                    may also be purchased for IVR port licenses if the number of port licenses that come with the seat licenses is not sufficient.

The Unified CCX architecture differs slightly from the
                                    		  example TDM call center configuration in that IVR ports and queue ports (and
                                    		  P&C ports as well) are combined into one logical CTI port as shown in the
                                    		  figure above.

#### Effect of
                              	 Performance Criteria on Unified CCX Server

System performance criteria fall into two general categories:

Unified CCX and Cisco Unified IP IVR components — Applications,
                                          				software versions, capabilities, server types, and options and quantities that
                                          				your system requires.

System usage — The average number of calls placed and received per hour, the average call length, the scripts that run, and
                                          the grammar used for ASR.

##### Effect of Performance Criteria

Each performance criterion can have an effect on the performance of the Unified CCX or Cisco Unified IP IVR system. In general,
                                       the more Unified CCX or Cisco Unified IP IVR components that you install and the heavier the system usage, the higher the
                                       demand on the server. However, the performance criteria can also interact in various non-linear ways to affect performance.
                                       The Cisco Unified Communications Sizing Tool for Unified CCX and Cisco Unified IP IVR can help you see and evaluate the effects
                                       of performance criteria on the Unified CCX and Cisco Unified IP IVR server.

#### Impact of
                              	 Performance Criteria on the Unified CM Servers

Software release versions— Using the Cisco Unified Communications
                                             				sizing tool, make sure to select the Unified Communications Manager software
                                             				version with which Unified CCX will be working.

The type and quantity of devices registered such as:

CTI ports (IP IVR ports for queuing, call treatment, and
                                                   					 self-service)

Gateway (GW) ports

Agent phones

Route points

The load processed by these devices (calls per second)

Application call flows

IVR self-service

Call treatment/Prompt and collect

Routing to agents,% transfers and conferences

Special Unified Communications Manager configuration and services

Other non-Unified CCX devices—IP phones, GW ports, Unity
                                                   					 ports, and dial plan.

Music on Hold (MOH)

Tracing levels— Unified Communications Manager CPU resource
                                                   					 consumption varies depending on the trace level enabled. Changing trace level
                                                   					 from Default to Full on Unified CM can increase CPU consumption significantly
                                                   					 under high loads. Changing tracing level from Default to No tracing can also
                                                   					 decrease CPU consumption significantly at high loads (this configuration is not
                                                   					 supported by Cisco TAC). CPU consumption due to default trace will vary based
                                                   					 on load, Unified Communications Manager release, applications installed, and
                                                   					 call flow complexity.

Server platform type

### Cisco Finesse Design Considerations

#### Cisco
                              	 Finesse

##### Introduction

Cisco Finesse is a
                                 		next-generation agent and supervisor desktop designed to provide a
                                 		collaborative experience for the various communities that interact with your
                                 		customer service organization.

Cisco Finesse
                                 		provides:

A browser-based
                                       			 administration console and a browser-based desktop for agents and supervisors;
                                       			 no client-side installations are required.

IP phone based
                                       			 (FIPPA) agent login & state control with limited features.

A single,
                                       			 customizable cockpit or interface, that gives customer care providers quick and
                                       			 easy access to multiple assets and information sources.

REST APIs that
                                       			 simplify the development and integration of value-added applications and
                                       			 minimize the need for detailed desktop development expertise.

Desktop Chat feature to agents who have a configured chat identity in Cisco IM&P server.

The following table
                                 		lists the availability of the Cisco Finesse REST APIs by license packages:

Service

Unified CCX Premium

Unified CCX Enhanced

Cisco Finesse REST APIs

Available

Available

The following table
                                 	 lists the availability of the Cisco Finesse service in the Unified CCX
                                 	 packages:

Service

Unified CCX Premium

Unified CCX Enhanced

Unified IP IVR

Cisco Finesse

Available

Available

Not available

Cisco Finesse
                                    		functionalities

Cisco Finesse
                                 	 supports the following functionalities:

Basic call
                                       		  control—Answer, hold, retrieve, end, and make calls.

Advanced call
                                       		  control—Make a consultation call and transfer or conference the call after the
                                       		  consultation.

Not Ready and Sign
                                       		  Out reason codes—Reasons that agents can select when they change their state to
                                       		  Not Ready.

Wrap-up
                                       		  codes—Reasons that agents can apply to calls.

Phone books—List
                                       		  of contacts from which agents can select one to call.

Live data
                                       		  gadgets—Display current state of agents, teams and CSQs in the contact center.

Customizable
                                       		  third-party gadgets.

Recording using Workforce Optimization.

Scheduled call
                                       		  back—Request a callback at a specific callback phone number and also specify
                                       		  the time or date of the callback.

Reclassify—Reclassify a direct preview outbound call as busy,
                                       		  answering machine, fax, invalid number, or voice.

Outbound
                                       		  agent—Supports outbound dialing including progressive, predictive, and direct
                                       		  preview modes, allowing agents to handle both inbound and outbound dialing
                                       		  tasks.

Multisession
                                       		  webchat—Allows agents to work on multiple chat sessions at the same time for
                                       		  increased agent resource usage.

Multisession
                                       		  email—Allows agents to work on multiple email sessions at the same time for
                                       		  increased agent resource usage.

Extension
                                       		  mobility—Allows users to temporarily access their Cisco Unified IP Phone
                                       		  configuration such as line appearances, services, and speed dials from other
                                       		  Cisco Unified IP Phones.

Desktop Chat - Allows users to initiate chat sessions with any other user logged in to the Cisco IM&P either from the Desktop
                                       Chat gadget or from a desktop client like Jabber.

Team Message - Allows supervisors to broadcast messages to their teams. Allows agents to view the messages broadcasted by
                                       their supervisors. This is a one-way communication from supervisors to agents.

Team
                                                      				composition changes in Cisco Finesse are not updated dynamically. Log in again
                                                      				or refresh the browser session to see the changes.

Transition
                                                      				to Logout state is possible only from Not Ready state.

You can configure
                                    		the Cisco Finesse Agent and Supervisor Desktops to use Cisco gadgets and
                                    		third-party gadgets through a layout management method. You can customize the
                                    		Cisco Finesse Agent and Supervisor Desktops through the Cisco Finesse
                                    		administration console. The administrators can define the tab names that appear
                                    		on the desktops and configure which gadgets appear on each tab.

For information
                                    		about supported browsers and operating systems, see the Unified CCX
                                    		Compatibility related information located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

Video is now supported if you are using Cisco Jabber as agent phone. The agent desktop where Jabber is used for Video should
                                                comply to the Cisco Jabber hardware requirements listed in the Release Notes for Cisco Jabber for Windows , located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html and in the Release Notes for Cisco Jabber for Mac , located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-mac/products-release-notes-list.html .

##### Administration

The administrator
                                    		can access the Cisco Finesse administration web user interface in read and
                                    		write mode from the Unified CCX publisher node. The Unified CCX subscriber node
                                    		provides read-only access.

##### Cisco Finesse
                                    		REST API

Cisco Finesse
                                    		provides a REST API that allows client applications to access the supported
                                    		features. The REST API uses secure HTTP (HTTPS) as the transport with XML
                                    		payloads.

Cisco Finesse
                                    		provides a JavaScript library and sample gadget code that can help expedite
                                    		third-party integration. You can find developer documentation for the REST API,
                                    		the JavaScript library, and sample gadgets at this location: https://developer.cisco.com/site/finesse/ .

##### Silent
                                    		monitoring

The supervisors
                                    		can monitor agents calls using Unified Communications Manager-based silent
                                    		monitoring with Cisco Finesse.

Cisco Finesse does
                                    		not support SPAN port-based monitoring and desktop monitoring to silent monitor
                                    		the agent.

##### Recording

Cisco Finesse workflows can be used to record agent calls using Cisco Unified Communications Manager with Cisco Workforce
                                    Optimization.

The agent phone
                                                		  must have built-in-bridge (BIB) support enabled for Cisco Unified
                                                		  Communications Manager-based call recording and monitoring to work with Cisco
                                                		  Finesse.

For information
                                                		  about the phones that have built-in-bridge support, see the Unified CCX
                                                		  Compatibility related information located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

For information
                                    		about recording APIs, see the at http://developer.cisco.com/web/finesse/docs .

##### Multiline
                                    		support

You can configure one or more secondary lines on an agent phone. Unified CCX monitors the first four configured lines. The
                                    agent's ACD line must be in button positions 1 - 4. Any calls on the observed lines are reported in the historical reports.
                                    Finesse displays the calls that are present in the Agent's ACD line.

Direct Transfer
                                    		Across Line (DTAL) and Join Across Line (JAL) are not supported.

##### NAT support

Cisco Finesse
                                    		supports static NAT only with one-to-one mapping between public and private IP
                                    		addresses. Finesse desktops support Fully Qualified Domain Names (FQDNs) only,
                                    		where FQDN resolves to the external IP address.

##### E.164
                                    		support

Unified CCX agents and supervisors can login to Finesse with ‘+’ (plus sign) as prefix. Finesse also supports E.164 for the
                                    following:

Enterprise Data

Phone Book Contacts

Workflow Rules or Conditions

#### Cisco Finesse IP
                              	 Phone Agent

With Cisco
                                    		  Finesse IP Phone Agent (IPPA), agents and supervisors can access Finesse
                                    		  features on their Cisco IP Phones as an alternative to accessing Cisco Finesse
                                    		  through the browser. Cisco Finesse IPPA allows agents and supervisors to
                                    		  receive and manage calls if they lose or do not have access to Cisco Finesse
                                    		  through a browser. It supports fewer features than the Finesse desktop in the
                                    		  browser.

##### Supervisor
                                    		  Tasks

Cisco Finesse
                                    		  IPPA does not support supervisor tasks such as monitor, barge, and intercept,
                                    		  but supervisors can sign in and perform all agent tasks on their IP Phones. For
                                    		  reporting purpose the supervisor will have to log in to Cisco Unified
                                    		  Intelligence Center to view the live data reports.

##### Reason Code
                                    		  Limits

On the IP Phone,
                                    		  Cisco Finesse can display a maximum of 100 Not Ready or Sign Out reason codes.
                                    		  If more than 100 codes are configured, the phone lists the first 100 applicable
                                    		  codes (global codes or applicable team codes).

#### Desktop Chat

Desktop Chat is a XMPP browser based chat, which is powered by Cisco Instant Messaging and Presence (IM&P) service. Desktop
                                    Chat allows agents, supervisors, and Subject Matter Experts (SMEs) within the organization to chat with each other.

For more details see, https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

Instant Messaging and Presence (IM&P) provides presence and chat capabilities within the Unified CM platform. The Desktop
                                    Chat interface is hosted by the Finesse Agent desktop and requires a separate log in to the IM&P service.

Desktop Chat does not support Cisco Mobile Remote Agent /VPN based access to the IM&P server. Desktop Chat requires direct
                                                access to the IM&P server to connect to the chat service.

##### Cisco Instant Messaging and Presence (IM&P)

IM&P incorporates the Jabber platform and supports XMPP protocol and can track the user's presence via multiple devices. IM&P
                                       pulls its user list from users who have been enabled for chat capabilities, from Unified CM (or LDAP if LDAP integration is
                                       enabled). Only Unified CM users enabled for chat capability can login to IM&P.

###### Identity, Presence, Jabber

A User is identified in the IM&P service with a unique identity which is in the form of username@FQDN.com .

A user is described in terms of the identity of the user, presence status, (available, unavailable, or busy) and the presence
                                       capabilities of the user.

The presence status of the user is not related to the Agent Status and has to be managed independently by the user post login.

Cisco IM&P service combines the presence status of user across multiple devices and publishes them for subscribers who have
                                       added the contact in their contact list.

IM&P supports a composed presence for the users, which is derived from the state matrix of all the devices that the agent
                                       is logged into. Cisco IM&P takes sources of presence from the XMPP client for the user, on-hook and off-hook status from CUCM,
                                       and in a meeting status from Microsoft Exchange to generate the users overall composed presence. Desktop Chat displays the
                                       composed presence of the user. For details about how to arrive at the composed presence, refer to the Cisco IM&P User Guide at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-user-guide-list.html .

Irrespective of the deployment type, the Desktop Chat requires an explicit login using the IM&P identity of the user after
                                       logging into the Finesse Desktop.

SSO is not supported with Desktop Chat and thus an explicit login is required in SSO mode.

Desktop Chat presence indicates the availability of users to communicate across the configured devices.

Desktop Chat availability will also be reflected in the combined IM&P presence of the user.

Logging into Desktop Chat, by default sets the users state as available.

An agent logging into Desktop Chat can thus be seen as available in Jabber or other XMPP platforms connected with IM&P and
                                       can communicate with these users.

File transfer is supported only for users communicating using Desktop Chat. For more information on the supported file types
                                                   and the maximum size of file attachments see, Desktop Properties CLIs section in the Cisco Unified Contact Center Express Administration and Operations Guide .

Example for Desktop Chat availability:

A Desktop Chat user can be logged into the Desktop Chat and Jabber at the same time. Incoming chats will be relayed to all
                                       the logged in clients including Desktop Chat. However, Desktop Chat does not support Multi-Device-Messaging. So messages being
                                       sent from other XMPP clients like Jabber will not be displayed within the Desktop Chat. Once alternate clients are used to
                                       respond to incoming chats, further messages are not shown in Desktop Chat until the user starts responding using the Desktop
                                       Chat.

For more information on network designs, refer to the Solution Reference Network Design guide https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-implementation-design-guides-list.html .

##### Cisco IM&P Design Considerations

Finesse browser makes a separate connection to Cisco IM&P over HTTPS, after it retrieves the chat server URI from the Finesse
                                       server. This requires separate certificates to be accepted if self-signed certificates are employed, in an HTTPS deployment.

The chat interaction happens over XMPP protocol, on the HTTP connection with long polling or BOSH established with Cisco IM&P.

There are no other interactions between Finesse server and browser for chat related capabilities, except for retrieving the
                                       Cisco IM&P server configurations.

Chat log persistence is available with the browser during the desktop session.

User search capabilities require Unified CM LDAP integration. In its absence, remote contacts have to be manually added by
                                       the user.

If the user is an existing Jabber user, the same contacts are shared between the Desktop Chat and Jabber which are also persisted
                                       across sessions.

There are no limits on the number of ongoing chats or the contacts in Desktop Chat apart from the restrictions or guidelines
                                       advised by Cisco IM&P. For the limit on the number of ongoing chats or the contacts and how to configure the Cisco IM&P server
                                       for chat, see the IM&P Solution Reference Networking Guide .

Desktop Chat requires the Cisco IM and Presence certificates to be trusted. For more information on accepting certificates,
                                                   see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html .

### Cisco Unified Intelligence Center Design Considerations

#### Unified
                              	 Intelligence Center Deployments

In Unified CCX deployments, both Unified Intelligence Center and Finesse
                                 		are coresident on the same server along with Unified CCX.

The above diagram depicts the HA configuration of Unified CCX, where the
                                 		primary node, by default, is the master, and the secondary node is the warm
                                 		standby. Historical reports are not available as gadgets.

Websocket Server - Only one instance of Websocket server is installed
                                 		in the Unified CCX node.

Live Data gadget on Finesse desktop - The live-data gadget is loaded on
                                 		the Finesse desktop only after an Agent or Supervisor has logged in and the
                                 		Finesse container is initialized. One of the reporting gadgets set up the
                                 		websocket tunnel. This common tunnel is shared by all the Unified Intelligence
                                 		Center gadgets.

Live Data report in Unified Intelligence Center Report Viewer or through a core permalink - All the Javascript libraries
                                 are required to create the Websocket tunnel and the OpenAjaxHub in the browser are loaded as part of the web page. A Websocket
                                 tunnel is then created from the client window to the Websocket server, and shared by all the Live Data reports that are run
                                 in the client window.

The system diagram for Live Data gadgets embedded in the Finesse desktop
                                 		and for Live Data reports running in the Unified Intelligence Center Report
                                 		Viewer is shown below.

#### Standalone Cisco
                              	 Unified Intelligence Center

Unified CCX 12.5(1) has been integrated with premium Cisco Unified Intelligence Center license. However, you can still use
                                 standalone Cisco Unified Intelligence Center.

The version of the standalone Cisco Unified Intelligence Center should be the same as the Unified Intelligence Center that
                                 is embedded in Unified CCX. The Standalone Cisco Unified Intelligence Center supports multiple data sources including Unified
                                 CCX.

In a Unified CCX High Availability deployment, the standalone Cisco Unified Intelligence Center should be connected to the
                                 standby node on Unified CCX to minimize the load on the master node. In case of failover of Unified CCX the Cisco Unified
                                 Intelligence Center connects to the new standby node. Standalone Cisco Unified Intelligence Center doesn't support high availability.

To install
                                 		standalone Cisco Unified Intelligence Center, see the Installation and Upgrade
                                 		Guide for Cisco Unified Intelligence Center, located at: http://www.cisco.com/en/US/products/ps9755/prod_installation_guides_list.html .

For more information
                                 		on how to create custom reports, see the Cisco Unified Contact Center Express
                                 		Report Developer Guide, located at: http://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_user_guide_list.html .

Live Data is not supported on the standalone Cisco Unified Intelligence Center.

Cisco Unified Intelligence Center user sync is not supported with the standalone Cisco Unified Intelligence Center and the
                                             Unified CCX server.

For standalone Cisco Unified Intelligence Center (CUIC), import the self-signed Tomcat certificate from CUIC and upload it
                                             into the Unified CCX Tomcat trust store.

| Metric | Description |
|---|---|
| Average
                                                   					 handle time (AHT) | Average duration (talk time) of a call plus after-call work time, which is the wrap-up time after the caller ends the call. |
| Average
                                                   					 IVR port usage time | The total
                                                   					 time for prompt playout and/or menu navigation (if any) in the Unified CCX
                                                   					 script. This time should not include the queue time the caller spends waiting
                                                   					 in queue before an agent becomes available. Queue time is calculated using
                                                   					 Erlang-C automatically. |
| Service
                                                   					 level goal for agents | Percentage
                                                   					 of calls answered by agents within a specific number of seconds. |
| Busy Hour
                                                   					 Call Attempts (BHCA) | Average
                                                   					 number of calls received in a busy hour. |
| Grade of
                                                   					 service (% blockage) for gateway ports to the PSTN | Percentage
                                                   					 of calls that get a busy tone (no gateway trunks available) out of the total
                                                   					 BHCA. |

| Note | If the system
                                                			 being designed is a replacement for an existing ACD or an expansion to an
                                                			 installed Unified CCX or Cisco Unified IP IVR system, you might be able to use
                                                			 the historical reporting information from the existing system to arrive at the
                                                			 above metrics. |
|---|---|

| Service | Unified CCX Premium | Unified CCX Enhanced |
|---|---|---|
| Cisco Finesse REST APIs | Available | Available |

| Service | Unified CCX Premium | Unified CCX Enhanced | Unified IP IVR |
|---|---|---|---|
| Cisco Finesse | Available | Available | Not available |

| Note | Team
                                                      				composition changes in Cisco Finesse are not updated dynamically. Log in again
                                                      				or refresh the browser session to see the changes. Transition
                                                      				to Logout state is possible only from Not Ready state. |
|---|---|

| Note | Video is now supported if you are using Cisco Jabber as agent phone. The agent desktop where Jabber is used for Video should
                                                comply to the Cisco Jabber hardware requirements listed in the Release Notes for Cisco Jabber for Windows , located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html and in the Release Notes for Cisco Jabber for Mac , located at http://www.cisco.com/c/en/us/support/unified-communications/jabber-mac/products-release-notes-list.html . |
|---|---|

| Note | The agent phone
                                                		  must have built-in-bridge (BIB) support enabled for Cisco Unified
                                                		  Communications Manager-based call recording and monitoring to work with Cisco
                                                		  Finesse. For information
                                                		  about the phones that have built-in-bridge support, see the Unified CCX
                                                		  Compatibility related information located at: http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
|---|---|

| Note | Desktop Chat does not support Cisco Mobile Remote Agent /VPN based access to the IM&P server. Desktop Chat requires direct
                                                access to the IM&P server to connect to the chat service. |
|---|---|

| Note | File transfer is supported only for users communicating using Desktop Chat. For more information on the supported file types
                                                   and the maximum size of file attachments see, Desktop Properties CLIs section in the Cisco Unified Contact Center Express Administration and Operations Guide . |
|---|---|

| Note | Desktop Chat requires the Cisco IM and Presence certificates to be trusted. For more information on accepting certificates,
                                                   see the Accept Security Certificates section, in the Common Tasks chapter of Cisco Finesse Agent and Supervisor Desktop User Guide for Cisco Unified Contact Center Express at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-user-guide-list.html . |
|---|---|

| Note | Live Data is not supported on the standalone Cisco Unified Intelligence Center. Cisco Unified Intelligence Center user sync is not supported with the standalone Cisco Unified Intelligence Center and the
                                             Unified CCX server. For standalone Cisco Unified Intelligence Center (CUIC), import the self-signed Tomcat certificate from CUIC and upload it
                                             into the Unified CCX Tomcat trust store. |
|---|---|