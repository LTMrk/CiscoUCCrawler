---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--7e62f87e81
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_ucce_b_outbound-option-guide-for-unified_1261/ucce_b_ucce_b_outbound-option-guide-for-unified_1261_chapter_01.html
retrieved_at: 2026-08-16T20:39:20.471827+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(1)

Updated: August 22, 2023

Chapter: Outbound Option Business Concepts

## Chapter: Outbound Option Business Concepts

# Outbound Option Business Concepts

## Overview

This section provides a high-level overview of automatic dialers and the Cisco Outbound
                           Option solution.

### Automatic Dialers

Automatic dialers increase contact center efficiency because they save time, eliminate misdialing numbers, and make contact
                              center agents more
                              productive. By automatically dialing and screening for busy signals, no answer, and answering
                              machines, dialers ensure that agents do not waste time on the mechanical tasks of placing a call. Only when the dialer reaches
                              a live contact does the solution transfer the call
                              to the next available agent.

### Cisco Outbound Solution

Cisco Unified Intelligent Contact Management Enterprise and Cisco Unified Contact Center
                                 Enterprise help companies distribute inbound calls to various termination points:

Automatic call distributors (ACDs)

Voice response unit (VRU) systems

Home
                                       agents

The Cisco Outbound Option application,
                                 with its combination of outbound dialing modes, enables call centers to manage outbound calls.
                                 The ability for agents to handle both inbound and outbound contacts enables
                                 contact center resource optimization.

### Overview of Cisco
                           	 Outbound Option

The Cisco Outbound
                                 		  Option application provides outbound dialing functionality along with the
                                 		  existing inbound capabilities of Cisco Unified Contact Center Enterprise
                                 		  (Unified CCE). This application enables the contact center to dial customer
                                 		  contacts and directly contacted customers to agents or VRUs.

Conference or consult option is not available for Dialer Outbound calls.

With the Cisco
                                 		  Outbound Option, configure a contact center for automated outbound activities.

Enable the outbound option high availability to deploy a redundant pair of Campaign Managers. Combined with redundant SIP
                                 Dialers and bidirectional database replication, Outbound Option High Availability provides uninterrupted services.

### Outbound Option Features

#### Unified CCE Compatible Dialer

You can implement Unified CCE in a single-site environment or integrated
                                    into a multisite contact center enterprise. Unified CCE includes
                                    intelligent call routing, ACD functionality, network-to-desktop computer telephony
                                    integration (CTI), VRU integration, call queuing, and consolidated reporting.

With Unified CCE integration, you place customer calls through the Cisco Voice Gateway using Unified CM for call control.

Outbound Option on Unified CCE provides a built-in, multisite outbound dialing solution.

#### Campaign Management

Outbound Option supports advanced list management, which provides you with the
                                    following capabilities:

You can assign customer records to multiple lists, which you can merge into a single
                                          campaign.

You set up rules that decide when to call the various lists.

You assign agents to campaigns using skill groups.

#### Dedicated and Blended Dialing Modes

You assign agents to one of the following types:

Used for agents who only make calls for Outbound Option campaigns.

Enables agents to receive inbound calls and Outbound Option calls without switching between Inbound and Outbound skill groups.
                                       (In Blended mode, inbound calls receive precedence over Outbound Option calls.)

Outbound Option maximizes performance in both pure outbound and blended modes.

The outbound mode is a skill group attribute. You can control the outbound mode using administrative scripts.

The skill group mode variable is only a setting and has no impact on how the Router routes calls. For skill groups in Dedicated
                                             mode, create a corresponding routing script with an IF node to enforce the Dedicated mode. The IF node must state that, if
                                             the Outbound Control skill group setting is set to Dedicated, do not route inbound calls to that skill group.

#### Call Progress Analysis (CPA)

Call Progress Analysis (CPA) uses a combination of call signaling and media stream analysis to differentiate various types
                                    of calls.

You can enable CPA in the Outbound Option Campaign dialog box. On the Campaign Purpose tab, check the Call Progress Analysis checkbox.

You can enable CPA for each campaign individually on the Dialer. To enable record CPA, check the Record CPA checkbox.

You must enable the Record CPA option for debugging purposes only.

The Dialer can record a maximum of 100 simultaneous CPA streams. The streams are stored in .wav format. By default, the system
                                    automatically purges old recording files when the total size of CPA files stored reaches 500 MB.

#### Transfer to VRU

The transfer to VRU feature provides Outbound Option with another outbound mode. In this mode, the Dialer transfers every
                                    customer call for a specific skill group to a service control-based VRU, instead of an agent. This feature enables a contact
                                    center to run unassisted outbound campaigns using prerecorded messages in the Unified IP-IVR and Unified CVP products.

#### Sequential Dialing

The sequential dialing feature enables
                                    you to associate up to ten phone numbers with a customer record.

#### Cisco Unified CCE
                              	 Agent Re-Skilling

Cisco Unified CCE
                                    		  agent re-skilling is an optional feature that enables supervisors to change the
                                    		  skill groups for their agents. Use the Unified CCE Web Administration
                                    		  application to change the skill group designations of agents on your team. You
                                    		  can also quickly view skill group members and details about individual agents
                                    		  in this tool. Changes that you make to an agent’s skill group membership take
                                    		  place immediately without requiring the agent to re-logon to the system.

#### Abandoned and Retry Call Settings

The Campaign component contains fields to support abandoned and retry calls.

For more information on the abandoned and retry call settings, see the Outbound Option online help .

#### Campaign Prefix
                              	 Digits for Dialed Numbers

The Campaign prefix digits field on the Campaign General tab enables you to configure prefix digits for dialed numbers by campaign. If you configure a prefix, the dialer inserts
                                    those digits before the Dial prefix for all numbers dialed in a campaign. This prefix enables an administrator to create campaign-specific
                                    Unified CM translation patterns. You can use the translation patterns to tailor the Automatic Number Identification (ANI)
                                    seen by a customer. For example, customers for Campaign A see a caller ID of "1-800-333-4444," and customers for Campaign B see a caller ID of "1-800-555-1212."

## Outbound
                        	 API

Outbound API
                              		  allows you to use REST APIs to create, modify, and delete Outbound Option
                              		  campaigns.

Outbound API provides a streamlined mechanism for creating campaigns with a single preconfigured query rule and import rule. As such, if you use the API to create a campaign, that campaign is not available in the Outbound Option Campaign Configuration
                                 tool. If a campaign was created with the API, you must use the API to view, edit, or delete it. If a campaign was created
                                 with the Outbound Option Campaign Configuration tool, you must use that tool to view, edit, or delete it.

Administrative
                              		  scripts are not required for Outbound Option campaigns created with the
                              		  Outbound API. If an administrative script is provided, the information in the
                              		  script overrides the information defined in the API.

Outbound API
                              		  consists of the following APIs:

Outbound
                                    				Campaign API: Use this API to define new Outbound Option campaigns, and to
                                    				view, edit, or delete existing campaigns. You can also use this API to disable
                                    				all campaigns at once (emergency stop).

Do Not Call
                                    				API: Use this API to set the Do Not Call (DNC) import rule configuration for
                                    				Outbound Option. This prevents the Dialer from dialing the numbers on the DNC
                                    				list.

Import API:
                                    				Use this API to import customer contact information for an Outbound Option
                                    				campaign.

Time Zone API:
                                    				Use this API to list all available time zones and to get information for a
                                    				specified time zone. You also use this API with the Outbound Campaign API to
                                    				set the default time zone for an Outbound Option campaign.

Campaign
                                    				Status API: Use this API to get the real-time status of running Outbound Option
                                    				campaigns.

Personal Callback (PCB) API: Use this API to configure your Outbound Option campaign to
                                    						handle personal callbacks. You can create personal callback records
                                    						individually or in bulk. You can also use this API to update or delete
                                    						personal callback records.

For more information about Outbound API, see the Cisco Unified Contact Center Enterprise Developer Reference Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html .

## Dialing
                        	 Modes

Outbound Option supports various dialing modes, described in the following sections.

All dialing modes reserve an agent at the beginning of every Outbound Option call cycle by sending a reservation call to the
                                          agent.

### Predictive
                           	 Dialing

In predictive
                                 		  dialing, the dialer determines the number of customers to dial per agent based
                                 		  on the number of lines available per agent and the configured maximum
                                 		  abandon rate. The agent must take the call if that agent is logged in to
                                 		  a campaign skill group.

A Predictive Dialer
                                 		  is designed to increase the resource utilization in a call center. It is
                                 		  designed to dial several customers per agent. After reaching a live contact,
                                 		  the Predictive Dialer transfers the customer to a live agent along with a
                                 		  screen pop to the agent’s desktop. The Predictive Dialer determines the number
                                 		  of lines to dial per available agent based on the target abandoned percentage.

Outbound Option predictive dialing works by keeping outbound
                                 		  dialing at a level where the abandon rate is below the maximum allowed abandon
                                 		  rate. Each campaign is configured with a maximum allowed abandon rate. In
                                 		  Predictive mode, the dialer continuously increments the number of lines it
                                 		  dials per agent until the abandon rate approaches the configured maximum
                                 		  abandon rate. The dialer lowers the lines per agent
                                 		  until the abandon rate goes below the configured maximum. In this way, the
                                 		  dialer stays just below the configured maximum abandon rate. Under ideal
                                 		  circumstances, the dialer internally targets an abandon rate of 85% of the
                                 		  configured maximum abandon rate. Due to the random nature of outbound
                                 		  dialing, the actual attainable abandon rate at any point in time may vary for
                                 		  your dialer.

### Preview
                           	 Dialing

Preview dialing reserves an agent before initiating an outbound call and presents the agent with a popup window. The agent
                                 can then Accept or Reject the call with the following results:

Accept : The customer is
                                       				dialed and transferred to the agent.

Reject :
                                       				The agent is released. The system then delivers another call to the
                                       				agent, either another Preview outbound call, or a new inbound call.

Rejects-Close : The agent is released and the record is
                                       				closed so it is not called again. The system then delivers another
                                       				call to the agent, either another Preview outbound call or a new inbound call.

### Direct Preview
                           	 Dialing

The Direct Preview
                                 		  mode is similar to the Preview mode, except that the dialer  automatically
                                 		  places the call from the agent's phone after the agent accepts. Because
                                 		  the call is initiated from the agent's phone, the agent hears the ringing, and
                                 		  there is no delay when the customer answers. However, in this mode, the agent
                                 		  must deal with answering machines and other results that the Dialer Call
                                 		  Progress Analysis (CPA) handles for other campaign dialing modes.

The CPA and the transfer to VRU features are not available while using Direct Preview Dialing mode.

A zip tone is a tone that announces incoming calls. There is no zip tone in Direct Preview
                                                   				  mode.

If you select personal callback as the callback option for a Direct Preview mode campaign, a personal callback is dialed in Preview mode. The personal callback is processed like a call in the Preview mode.

### Progressive
                           	 Dialing

Progressive Dialing
                                 		  is similar to predictive dialing (see Predictive Dialing ).
                                 		  The only difference is that in Progressive Dialing mode, Outbound Option does
                                 		  not calculate the number of lines to dial per agent, but allows users to
                                 		  configure a fixed number of lines that will always be dialed per available
                                 		  agent.

In the Outbound
                                             			 dialer log, the Progressive dialing mode is also logged as Predictive.

## Callbacks

When the system contacts a customer and transfers the call to an agent, the customer can request to be called back later.
                              The agent enters the date
                              and time that the customer wants a callback in the agent application to schedule  the callback. There are two types of callbacks:
                              regular callbacks and personal callbacks.

The callback number can be different from the number originally dialed.

Depending on the Outbound Option campaign settings, you can schedule a regular callback or a personal callback.

### About Regular Callbacks

Any agent who is assigned to the campaign can handle regular callbacks.

Callbacks
                                 are handled in the same mode as the campaign type. If an agent schedules a callback for a predictive 
                                 campaign, the callback for that campaign is handled in Predictive mode.

The campaign dialing times do not constrain the callback time. CallbackTimeLimit
                                 determines the time range when the
                                 callback can occur.

If the dialer cannot reach
                                 the customer, the callback time is rescheduled.

The CallbackTime limit might be exceeded if no agents are available. If the elapsed time
                                 exceeds the CallbackTimeLimit and RescheduleCallback is enabled, the record returns to the Pending state at TimeToResetDailyStats.

### About Personal
                           	 Callbacks

The Outbound Option personal
                                    			 callback feature schedules a specific agent to handle a customer
                                 		  callback. The feature enables the customer to continue working with the same
                                 		  agent who spoke with them initially.

Callbacks on
                                 		  personal callbacks are handled in the associated campaign mode.

Only an agent who
                                 		  dealt with the original call can set a personal callback. The dialer offers the
                                 		  agent the personal callback using a mode similar to the Preview dialing mode.

This feature is similar to Preview mode in that an agent reservation occurs first. When the agent is reserved, they can either
                                 accept the customer call or reject it. Clicking Close sets the BAResponse variable to indicate a close operation. The record is not dialed again.

Personal callbacks
                                             			 are not dependent on a particular campaign, and do not require a running
                                             			 campaign when the call is placed. This feature enables personal callbacks to
                                             			 occur with active campaigns containing either predictive or preview skill
                                             			 groups. Agents can receive a personal callback request while logged in to any
                                             			 inbound, outbound, or blended skill group. The callback is linked to the agent
                                             			 ID. If the agent logs in with a different agent ID, they cannot receive the
                                             			 callback request. Only one dialer on a particular peripheral is assigned
                                             			 personal callback records.

When an agent is on PCB reservation call, the real time reporting shows the
                                             					agent's status as Talking . This status is shown because the
                                             					dialer reserves the agent and puts a virtual hold.

The
                                 		  Personal_Callback_List table maintains a list of the customer records scheduled
                                 		  to be called back by a specific agent. The Campaign Manager creates records in
                                 		  the Personal_Callback_List table when an agent schedules a personal callback.

You can use an Outbound API to insert customer records directly into the Personal_Callback_List table to support scheduling
                                 customer calls for a specific time. For information on Outbound APIs, see the Cisco Unified Contact Center Enterprise Developer Reference at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html

When modifying the
                                             			 Personal_Callback_List table, be aware of the following restrictions:

Applications
                                                   				  that insert new records into this table must populate the
                                                   				  InsertedIntoDBDateTime column with the current date and time. However, do not
                                                   				  modify SentToDialerDateTime. This date and time is set by the Campaign Manager.

Do not close
                                                   				  or delete Records when the Status is 'A'. Records that are pending can be
                                                   				  marked as closed or deleted in a Campaign Dialing List if they are not in the
                                                   				  Active state.

If Outbound Option High Availability is enabled, you must use the Personal_Callback API to insert data into the Personal_Calback_List
                                                   table.

Personal callback
                                 		  supports three callback modes:

Use Campaign DN

Reschedule the
                                       				personal callback to the same time the next business day.

Abandon the
                                       				personal callback.

The following
                                 		  actions can take place during a personal callback:

If the customer
                                       				is unreachable during the callback time, the call is rescheduled up to the
                                       				maximum attempts or abandoned based on the configuration setup.

If the dialer
                                       				detects an answering machine response, the call is still transferred to the
                                       				scheduled agent. The agent can leave a message or reschedule the callback for
                                       				another convenient time.

When the
                                       				callback mode is set to Reschedule or Abandon:

If the agent
                                             					 is logged in at any point during the callback period, Outbound Option reserves
                                             					 the agent and places the callback.

If the
                                             					 agent is unavailable during the entire callback period, the personal callback
                                             					 fails. The call is rescheduled or abandoned based on the configuration setup.

When the
                                       				callback mode is set to Campaign DN:

If the agent
                                             					 is unavailable at the callback time, Outbound Option reserves another agent for
                                             					 the callback using the dialed number of the associated campaign skill group.

If an alternate agent is also unavailable from Campaign DN script, retry action is No Answer.

For more
                                 		  information, see Appendix F, "Personal_Callback_List Table".

The valid range for Callbacktime is from midnight, January 1, 1970 through December 31, 3000 Universal Coordinated Time (UTC).
                                             If Callbacktime is specified  out of range then it is defaulted to NULL.

## Relationships
                        	 Between Outbound Option Components

The following figure
                              		  shows the component relationships within Outbound Option.

Concept

Description

Import

Defines when
                                          					 and how Outbound Option reads in user-generated lists of customers to call and
                                          					 not to call.

Query Rule

A set of
                                          					 criteria for selecting customer contacts from a customer list.

Campaign

Create the
                                          					 agent skill groups and associate them with one or more dialing lists by
                                          					 assigning them to a campaign.

With
                                          					 Outbound Option, you can configure these types of campaigns:

Agent-based campaign —In
                                                						  this campaign type, the Dialer transfers customer calls to an agent.

Transfer to VRU
                                                   							 campaign —In this campaign type, the Dialer transfers customer calls to a
                                                						  service control-based VRU, instead of an agent. This feature enables a contact
                                                						  center to run unassisted outbound campaigns using pre-recorded messages in the
                                                						  VRU.

Skill Group

Defines a
                                          					 selection of agents for a campaign. Each skill group can only have one campaign
                                          					 assignment, but a campaign can service multiple skill groups.

Their skill group associations tie the agents to the campaign. Agents might belong to multiple skill groups and be part of
                                          multiple campaigns.

You cannot associate a specific dialing list to a specific skill group unless there is only one dialing list and one skill group in the campaign.

Agent
                                          					 Peripheral Gateway (PG)

A collection
                                          					 of agents and skill groups that are bound to a specific Unified CM. The dialer
                                          					 is bound to serve the group of agents in a specific call center site.

Dialer

The
                                          					 component that places Outbound Option calls. The dialer is associated with the
                                          					 agent peripheral at a call center site. Outbound Option sends calls to a dialer
                                          					 based on the campaign skill group relationship for the agent controller at that
                                          					 site. The dialer monitors campaign skill groups and is mapped to an agent
                                          					 peripheral.

Customer
                                          					 List

List of
                                          					 contact information that you provide during import. This is a user-configured
                                          					 item.

Do Not Call List

List of contact information that must not be included in the
                                          					 Dialing List. This is a user-configured item.

Contact List

An internal
                                          					 table, to which an import applies a query rule to determine which records to
                                          					 insert in the dialing list. There is one Contact List for each import.

Dialing List

The list of
                                          					 customer contacts to which Outbound Option makes calls. There is one dialing
                                          					 list for each campaign query rule.

Each
                                          					 campaign query rule combination results in a unique dialing list.

Only one
                                          					 dialing list is active at a time for a particular campaign. Whenever a dialing
                                          					 list is active, the list is distributed to all skill groups in the campaign.
                                          					 You cannot map a specific dialing list to a specific skill group in a campaign.

Using some of the
                              		  preceding terms, the following example demonstrates what happens during an
                              		  Outbound Option import:

Outbound Option imports your customer list into an internal table of customer contacts.

During the
                                    				import process, a query rule filter selects and inserts data from the customer
                                    				contacts into a dialing list.

Outbound Option
                                    				reads in records from the dialing list for the campaign. Outbound Option sends
                                    				the records to contact to dialers that are colocated on the peripherals for the
                                    				associated skill groups.

## Imports

You can import a list of customer contact information and a list of customers to
                              not call. You can configure Outbound Option to import both types of lists either by
                              continuously polling or at scheduled intervals. Imported lists can
                              replace existing lists or be appended to them.

### Do Not Call List
                           	 Imports

Many countries
                                 		  require phone solicitors to maintain do not call lists. A Do Not Call (DNC)
                                 		  list ensures that your contact center does not call those customers who request
                                 		  that you do not contact them.

The Do Not Call list is a list of numbers that are identified as off-limits for outbound calling. This list can include numbers
                                 from a national DNC list and numbers from customers who have directly requested that you not contact them. Outbound Option
                                 does not dial entries in the Do Not Call list even if they are included in a contact list. The DNC list is shared across all
                                 campaigns and contains only phone numbers.

The
                                 		  campaign validates that a number in the dialing list is not in the Do Not Call
                                 		  list before sending it to a dialer. The solution checks the list at the last
                                 		  minute before placing the call. You can update a Do Not Call list while a
                                 		  campaign is running.

When you
                                 		  enable Outbound Option High Availability and import the Do Not Call list data
                                 		  to the active Campaign Manager side, it may some time
                                 		  for the import of data (from the Do_Not_Call table in the database) to
                                 		  complete. It may take additional time for the data to replicate to the standby
                                 		  side before the standby Campaign Manager is able to read the data. After
                                 		  Campaign Manager loads records, Do Not Call numbers are in effect. If the
                                 		  Campaign Manager has already sent a record to the dialer, an update to the list
                                 		  does not stop the dialer from placing the call.

The import process
                                 		  validates Do Not Call imports for improper formatting and field lengths. The
                                 		  import process flags invalid records and writes them to an error file.

### Contact List
                           	 Imports

The contact list import reads in a user-generated text file of customer contacts and associated phone numbers to an internal
                                 contact table. The import includes validation that flags improperly formatted records and writes them to an error file. The
                                 error files are in the \la\logfiles directory directory on the Side A Logger and lb\logfiles directory on the Side B Logger. The filenames are based on the Target Table Name, the date, and time of the import. Phone numbers without
                                 prefix matches are not placed in a file.

You can add business-specific attributes to the contact list import file before the import occurs. You can use these attributes
                                 to segment a campaign with a query rule. In this way, a single import can contain records for multiple dialing lists for the
                                 same campaign. However, don't include the campaign customer contacts in multiple dialing lists because you might dial the
                                 same customer twice.

The U.S. area code mappings are available in the product. International customers must add their own data to the database.

The contact list import process assigns time zone and daylight saving time information to each contact by matching phone numbers
                                 to region prefix strings. If a phone number for a contact doesn't match a configured region prefix, the import uses the default
                                 time zone data for the campaign.

Things to know about campaign imports:

Continuous imports of 10,000 records or more can cause the Campaign Manager to reach congestion control level which reduces
                                                   the system port throttle until it catches up with requested work in its queue.

Continuous imports for a given campaign can cause problems for the import process.

Overwrite imports are more intensive than append imports. We recommend that you run overwrite imports during off hours to
                                                   clear out the activity of that day, if possible.

The import fails if the import file has more than 10,000 errors.

Typically, the Campaign Manager sends dialing records to the dialer based on the DialingListID in an increasing order. However,
                                                   the records imported on the Logger-B side has a negative DialingListID, so the newer records are sent for dialing before the
                                                   older records.

Overwriting imports against active dialing campaigns may result in the rejection of the latest imported record due to a conflict
                                                   with the ongoing records dialing list ID.

### Import Rule Reports

The Do Not Call and Contact List imports use the same import rule reports. The reports display the following historical data:

When an import occurred

The number of imported records

The number of invalid records due to length constraints or improper formatting

For contact list imports, the reports also list:

The number of contacts that the import assigned to the default time zone

The number of contacts that the import included in the dialing list after performing the query rule and format validation

## Query Rules

The query rule determines which customer contacts from the import to use for a campaign.
                              You can associate multiple query rules with a campaign. You can use the query rules to segment
                              a campaign for prioritization or other logical groupings. For example, if you want to dial certain customers between 9 AM
                              and 11 AM, set up a
                              query rule to only dial during those times. You then configure the campaign to switch to another
                              query rule outside those times.

When dialing, only one query rule is active at any time for each campaign.

You can change query rules based on conditions such as configured time limit,
                              several records attempted (referred to as penetration), current time, or current hit rate. The query rule automatically switches
                              to another available query
                              rule if the query rule runs out of numbers that can be dialed now.

## Campaigns

A campaign is made up of one or more dialing lists and one or more
                              campaign skill groups. Outbound Option reads in contacts from the dialing list for
                              the currently active query rule in the campaign. The Campaign Manager then  directs dialers to place customer calls. The
                              dialer then directs contacted customers to agents or a VRU in
                              the campaign skill group.

In the Outbound Option Campaign component, you can:

Create a campaign.

Modify a campaign.

Delete a campaign.

A campaign is either an agent-based campaign or a transfer to VRU campaign. A campaign cannot combine both types of calls.

### Agent Campaigns

In an agent campaign, Outbound Option dials customers and transfers them to agents in
                                 targeted skill groups. The dialer monitors for available agents. When the dialer finds an available agent, the peripheral
                                 gateway (PG) places a virtual reservation call to
                                 prevent the router from using that agent for other calls. The agent phone
                                 does not actually ring, but the agent desktop updates to show a call in progress. After the agent is reserved, the dialer
                                 places a call using the dialing mode for the campaign skill
                                 group. After the dialer identifies a customer, the call transfers to the agent. The agent
                                 should stay on the reservation call until a customer call is reached to avoid abandoned calls. Once a customer call is reached,
                                 the dialer disconnects the
                                 reservation call from the agent desktop.

An internal call can interrupt an agent on a reservation call. The dialer still sends the call to the agent. The call is dropped
                                             unless call waiting is enabled on the agent extension. You can avoid this scenario by giving the agent a second line for internal
                                             call use, and make sure the line is interruptible with call waiting enabled.

The agent can still mark the call as a wrong number, wrong party, or schedule a callback for later which does not close out
                                 the record. If more than one line is dialed for the agent, several customers might answer their calls. The first call is assigned
                                 to the agent. The dialer then determines what to do with the extra answered calls. If another agent is reserved in the campaign,
                                 the call transfers to that agent. Otherwise, the call may be transferred to a VRU to handle the abandoned call. If no VRU
                                 is configured, then the call drops with no treatment. Specify a VRU in the campaign's Abandon to IVR setting to avoid dialer
                                 abandons. The VRU can play prompts, collect data, and redirect the customer to a properly skilled agent in the contact center.

### CallerID Masking by Campaign

Outbound Option allows you to configure up to 15 prefix digits for dialed numbers in a
                                 campaign. If you configure a prefix, the dialer inserts the prefix before the Dial prefix for all
                                 numbers dialed in a campaign.

### Transfer to VRU Campaigns

A transfer to VRU campaign, also known as an unattended or unassisted campaign, can send
                                 both live customer and answering machine calls to VRUs for customer treatment. This customer
                                 treatment includes playing prompts, collecting data from the customer, and redirecting the
                                 call to appropriate agents in the contact center.

The configuration allocates the maximum VRU ports to use for transfer to VRU campaigns. The campaign attempts to keep them
                                 busy within the dialing constraints.

An unattended campaign can use either Progressive or Predictive modes. You can play a different prompt for a live customer
                                 or for an answering machine.

You cannot use the transfer to VRU feature in the Direct Preview mode or the regular Preview modes.

### Dialing
                           	 Order

A contact can have
                                 		  several numbers configured (on the Call Target tab in the Campaign
                                 		  configuration). The campaign dials each number for the contact once, in the
                                 		  configured order. The campaign can then retry the numbers.

For more
                                 		  information, see Configuration of Campaigns and Imports chapter.

#### Sequential Dialing

The sequential dialing feature enables you to associate up to ten phone numbers with each
                                    customer record. You can configure two time periods, called "zones," to call the customers for each campaign. Each time period (zone) lists which of the ten phone numbers
                                    to call during that time. You can call a phone number during either zone or both
                                    zones.

Customers are dialed based on the time zone of the first phone that is configured on this tab. The time zone is based on
                                                the prefix of the phone number and the region prefix configuration. If two phone numbers for the same customer have different
                                                time zones, the time zone for the first phone number in the list sets the times for calling both numbers.

#### Contact Priority for
                              	 Callbacks, Retries, and Pending Contacts

The contact priority
                                    		  order is as follows:

Top priority is
                                          				given to customers who requested callbacks . This priority ensures that the customers are
                                          				called at the requested time.

Retries get second
                                          				priority. After all the numbers for the contact are tried once, the system can
                                          				retry a contact if some of their numbers had an appropriate call result.

Pending contacts get
                                          				third priority. A customer record is pending until all of its eligible phone
                                          				numbers are tried once.

You can change the default priority order by changing the PendingOverRetryEnabled registry setting to 1 in the Campaign Manager.
                                                This setting ensures that all numbers and records are tried once before retries are attempted.

### Campaign
                           	 Reports

The query rule call
                                 		  activity and pending record reports are available as campaign roll-ups for
                                 		  multiple query rules in a campaign.

There are also consolidated reports, that blend campaign call activity reporting information with skill group performance
                                 reports for a clear overview of the business activity. Because the consolidated reports mix data from different reporting
                                 engines, the reports have a few caveats. The reports include descriptions of these caveats. These reports provide a rough
                                 overview of agent activity, average time between calls, abandon rate, and so on.

#### Campaign Query Rule Reports

There are two general categories of campaign query rule reports:

Reports that show the number of records closed, in Pending state, and
                                          the total records in the query rule’s dialing list.

Reports that provide different views into the call result activity.

#### Transfer to VRU Reports

The campaign and query rule call activity reports display call activity for
                                    calls that are not transferred to a VRU. The campaign and query rule activity reports also count calls that are transferred
                                    to a VRU, but those reports do not
                                    show what happens after the call is sent to the VRU. If calls are queued and transferred
                                    back to an agent, the calls are treated as new inbound calls in the reports.

#### Call Type Reports

The call type is a Unified CCE concept that maps a route point dialed number to a
                                    routing script. The call type is also a useful reporting object to describe all
                                    calls that traversed a specific routing script. The call type applies primarily to inbound
                                    traffic in the call center. The dialer does not use the routing script when placing
                                    outbound calls. However, the Outbound Option does use routing scripts to reserve agents and to
                                    transfer calls to the VRU. So, the call type can provide some insight into how calls are routed.

## Campaign Skill Groups

A campaign skill group describes the campaign resource pool and the
                           information for managing the campaign. In deployments with
                           multiple sites that have different hours and different equipment, you have different skill groups for each site. Dialing Mode
                           is a
                           skill group attribute that enables you to open and close skill groups at
                           different times for shared campaigns.

The dialer uses campaign skill groups to monitor resource availability. In agent
                           campaigns, the dialer looks at the number of available agents. In Transfer to VRU campaigns,
                           the dialer monitors the number of calls in queue for each campaign skill group. The dialer
                           ensures that no skill group  exceeds its quota of configured VRU ports.

You associate each dialer with a peripheral (PG). The dialer monitors the skill groups
                           on its own peripheral for resource availability and requests records for the appropriate campaigns.

The dialer only places calls for agents or VRUs that are located on its PG.

Multiple dialers can serve one campaign if skill groups from each dialer's PG are assigned to the campaign. This assignment
                                       enables campaigns to be site-specific or shared across the enterprise, depending on the configuration.

### Smaller Skill Groups

Predictive mode campaigns are more efficient when there are more agents or VRU ports in a campaign skill
                              group. The dialer adjusts its dialing rate based on the abandon rate. The more frequently calls are placed, the more often
                              the dialer can adjust the dialing rate.
                              The dialer cannot make  accurate adjustments frequently enough when there
                              are fewer than 10 agents in the campaign.

### Blended Campaigns/Skill Groups

In blended campaigns, agents take inbound calls and outbound calls at the same time. The inbound program can use the same
                              or a different skill group as the outbound campaign skill group. You can set up the campaign skill group to use a percentage
                              of active agents and to reserve the rest for inbound calls. If an inbound customer is in queue, blended agents are not reserved
                              for the campaign. These mechanisms result in the inbound calls generally receiving priority.

An agent on an outbound reservation call is not interrupted with a routed inbound
                              call. An agent reservation call lasts until one of the following conditions occurs:

The agent closes the reservation call.

The campaign closes out for that skill group.

The reservation times out.

An internal call can interrupt an agent on a reservation call. This interruption generally causes the reservation call to
                              drop. Because the dialer is dialing customers for that agent during a reservation call, the interruption can also result in
                              abandoned calls if no agents are available.

### Agents Skilled for
                           	 Multiple Active Campaigns

You can skills agents
                              		for multiple active campaigns. Multiple campaigns cannot place simultaneous
                              		reservations on the same available agent.

For example, assume
                              		that you have an agent in three active campaign skill groups. That agent
                              		becomes available in all three skill groups at the same time. The dialer that
                              		monitors the skill groups for available agents sends up three reservation
                              		requests, one for each campaign skill group. The first campaign skill group in
                              		the dialer memory gets priority over the other requests. Over time, this
                              		situation results in an imbalance of agents between skill groups.

To work around this
                              		issue, you can queue reservation calls in a similar way to personal callbacks.
                              		This workaround services reservation requests in the second and third campaign
                              		skill groups first the next time an agent becomes available. This method evenly
                              		distributes calls across the active campaigns when agents are skilled in
                              		multiple campaigns.

### Campaign Skill Group Reports

Skill Group reports provide information about agent activity for outbound and inbound
                              agents.

#### Blended Campaign
                              	 Skill Group Reports

If you use the same
                                    		  skill group for both inbound and outbound, then the campaign consolidated
                                    		  reports can provide a consolidated overview of business activity for both
                                    		  inbound and outbound calls.

## Customer Time Versus System Time

This section describes when Outbound Option activities use the customer time zone rather than the system time .

### Customer Time

The Outbound Option uses area code prefixes to determine the time zone. With cell phones or VoIP phones, the area code might
                                             not correspond to the actual time zone where the call is received.

A campaign can include customers  across multiple time zones, as long
                                 as the time zones follow the same rules for when daylight saving time changes.

Unified CCE determines the time zone offset of each contact with a
                                 configurable region prefix database . The database contains area code prefixes, assigned
                                 time zone offsets, and a daylight saving time flag. The Outbound Option
                                 import uses this database to associate time zone offsets with customers. When the campaign searches for records in the active
                                 query rule’s dialing list, the search considers the time zone
                                 offset when choosing contacts. This approach
                                 does not account for daylight saving time changes from time zone to time zone. Those changes are managed at the campaign level,
                                 so that campaigns take into account when each time zone changes over to daylight saving time.

For example, North America has time zone regions that do not observe
                                 daylight saving time, or that switch over on different days. A campaign that dials Houston,
                                 Texas and Mexico City, Mexico must account for these locations changing over
                                 to daylight saving time on different days.

If a contact’s number does not match any of the configured region prefixes, then the
                                 campaign uses its default time zone offset. If all the customers are in one time
                                 zone, then you do not need the region prefix information.

Outbound Option receives its list of daylight saving zones from Microsoft Windows. Ensure that all Outbound Option components
                                 run on the same version of Windows as the Logger and AW VMs to keep the time zone information in synch.

### System Time

The system time is based on the Central Controller's time. System time is used in scheduled imports and in the query
                                 rule time of day for switching contact lists.

## Call Progress Analysis (Answering Machine Detection)

Call Progress Analysis (CPA) uses call signaling and media stream analysis to differentiate types of calls. CPA can detect
                              the following:

Fax or modem detection looks for specific tones in the media stream.

Voice detection looks in the media stream for alternate voice and silence patterns after the call connects.

Answering Machine Detection (AMD) uses media stream analysis to look for a longer voice stream with minimal silence periods.
                                    AMD can also use terminating tone detection.

Operator Intercept relies on call signaling network identification. This method does not analyze the media stream looking
                                    for specific tri-tones.

CPA creates a delay before the call is transferred to an agent. Some countries require customer calls to be transferred to
                                          an agent in a certain amount of time. In those cases, you may not be able to use CPA.

Because virtual CUBE does not have the Digital Signal Processors (DSP) that a physical CUBE has, it cannot support CPA. Add
                                          a dedicated physical outbound gateway to support CPA.

### Answering Machine Detection

Enable Answering Machine Detection on a campaign-by-campaign basis, depending upon the requirements of the campaign or the
                              purpose of the call.

Enable IP AMD when using CPA. If you do not enable IP AMD, the SIP dialer instructs the gateway to transfer the call to an
                                          agent without waiting for detection.

AMD uses speech patterns and silence between voice patterns to differentiate a live voice from an answering machine recording
                              and background noise. There are parameters in the Outbound Option Campaign Configuration component that modify the amount
                              of silence or the expected time of greeting. Accuracy levels depend on such factors as the campaign list quality and the phone
                              number types.

## Two-Way Outbound
                        	 Option Database Replication

If you choose to
                           		enable Outbound Option, you can also enable Outbound Option High Availability.
                           		Outbound Option High Availability supports two-way replication between the
                           		Outbound Option database on Logger Side A and the Outbound Option database on
                           		Logger Side B.

You create an
                           		Outbound Option database on Side A and Side B either by:

Using the ICMDBA
                                 			 tool (if you haven't set up Outbound Option at all).

Backing up the Outbound Option database on Logger Side A and restoring it to Logger Side B (if you have already set up Outbound
                                 Option on Side A).

You then use Web
                           		Setup to configure the Loggers to support Outbound Option and Outbound Option
                           		High Availability.

| Note | Conference or consult option is not available for Dialer Outbound calls. |
|---|---|

| Note | The skill group mode variable is only a setting and has no impact on how the Router routes calls. For skill groups in Dedicated
                                             mode, create a corresponding routing script with an IF node to enforce the Dedicated mode. The IF node must state that, if
                                             the Outbound Control skill group setting is set to Dedicated, do not route inbound calls to that skill group. |
|---|---|

| Note | You must enable the Record CPA option for debugging purposes only. |
|---|---|

| Note | All dialing modes reserve an agent at the beginning of every Outbound Option call cycle by sending a reservation call to the
                                          agent. |
|---|---|

| Note | The CPA and the transfer to VRU features are not available while using Direct Preview Dialing mode. A zip tone is a tone that announces incoming calls. There is no zip tone in Direct Preview
                                                   				  mode. If you select personal callback as the callback option for a Direct Preview mode campaign, a personal callback is dialed in Preview mode. The personal callback is processed like a call in the Preview mode. |
|---|---|

| Note | In the Outbound
                                             			 dialer log, the Progressive dialing mode is also logged as Predictive. |
|---|---|

| Note | The callback number can be different from the number originally dialed. |
|---|---|

| Note | Personal callbacks
                                             			 are not dependent on a particular campaign, and do not require a running
                                             			 campaign when the call is placed. This feature enables personal callbacks to
                                             			 occur with active campaigns containing either predictive or preview skill
                                             			 groups. Agents can receive a personal callback request while logged in to any
                                             			 inbound, outbound, or blended skill group. The callback is linked to the agent
                                             			 ID. If the agent logs in with a different agent ID, they cannot receive the
                                             			 callback request. Only one dialer on a particular peripheral is assigned
                                             			 personal callback records. |
|---|---|

| Note | When an agent is on PCB reservation call, the real time reporting shows the
                                             					agent's status as Talking . This status is shown because the
                                             					dialer reserves the agent and puts a virtual hold. |
|---|---|

| Note | When modifying the
                                             			 Personal_Callback_List table, be aware of the following restrictions: Applications
                                                   				  that insert new records into this table must populate the
                                                   				  InsertedIntoDBDateTime column with the current date and time. However, do not
                                                   				  modify SentToDialerDateTime. This date and time is set by the Campaign Manager. Do not close
                                                   				  or delete Records when the Status is 'A'. Records that are pending can be
                                                   				  marked as closed or deleted in a Campaign Dialing List if they are not in the
                                                   				  Active state. If Outbound Option High Availability is enabled, you must use the Personal_Callback API to insert data into the Personal_Calback_List
                                                   table. |
|---|---|

| Note | The valid range for Callbacktime is from midnight, January 1, 1970 through December 31, 3000 Universal Coordinated Time (UTC).
                                             If Callbacktime is specified  out of range then it is defaulted to NULL. |
|---|---|

| Note | The following
                                       		  figure and table only describe Outbound Option components and concepts; they do
                                       		  not describe the Outbound Option process. |
|---|---|

| Note | You configure the blue-outlined items in this figure. |
|---|---|

| Concept | Description |
|---|---|
| Import | Defines when
                                          					 and how Outbound Option reads in user-generated lists of customers to call and
                                          					 not to call. |
| Query Rule | A set of
                                          					 criteria for selecting customer contacts from a customer list. |
| Campaign | Create the
                                          					 agent skill groups and associate them with one or more dialing lists by
                                          					 assigning them to a campaign. With
                                          					 Outbound Option, you can configure these types of campaigns: Agent-based campaign —In
                                                						  this campaign type, the Dialer transfers customer calls to an agent. Transfer to VRU
                                                   							 campaign —In this campaign type, the Dialer transfers customer calls to a
                                                						  service control-based VRU, instead of an agent. This feature enables a contact
                                                						  center to run unassisted outbound campaigns using pre-recorded messages in the
                                                						  VRU. |
| Skill Group | Defines a
                                          					 selection of agents for a campaign. Each skill group can only have one campaign
                                          					 assignment, but a campaign can service multiple skill groups. Their skill group associations tie the agents to the campaign. Agents might belong to multiple skill groups and be part of
                                          multiple campaigns. You cannot associate a specific dialing list to a specific skill group unless there is only one dialing list and one skill group in the campaign. |
| Agent
                                          					 Peripheral Gateway (PG) | A collection
                                          					 of agents and skill groups that are bound to a specific Unified CM. The dialer
                                          					 is bound to serve the group of agents in a specific call center site. |
| Dialer | The
                                          					 component that places Outbound Option calls. The dialer is associated with the
                                          					 agent peripheral at a call center site. Outbound Option sends calls to a dialer
                                          					 based on the campaign skill group relationship for the agent controller at that
                                          					 site. The dialer monitors campaign skill groups and is mapped to an agent
                                          					 peripheral. |
| Customer
                                          					 List | List of
                                          					 contact information that you provide during import. This is a user-configured
                                          					 item. |
| Do Not Call List | List of contact information that must not be included in the
                                          					 Dialing List. This is a user-configured item. |
| Contact List | An internal
                                          					 table, to which an import applies a query rule to determine which records to
                                          					 insert in the dialing list. There is one Contact List for each import. |
| Dialing List | The list of
                                          					 customer contacts to which Outbound Option makes calls. There is one dialing
                                          					 list for each campaign query rule. Each
                                          					 campaign query rule combination results in a unique dialing list. Only one
                                          					 dialing list is active at a time for a particular campaign. Whenever a dialing
                                          					 list is active, the list is distributed to all skill groups in the campaign.
                                          					 You cannot map a specific dialing list to a specific skill group in a campaign. |

| Note | Things to know about campaign imports: Continuous imports of 10,000 records or more can cause the Campaign Manager to reach congestion control level which reduces
                                                   the system port throttle until it catches up with requested work in its queue. Continuous imports for a given campaign can cause problems for the import process. Overwrite imports are more intensive than append imports. We recommend that you run overwrite imports during off hours to
                                                   clear out the activity of that day, if possible. The import fails if the import file has more than 10,000 errors. Typically, the Campaign Manager sends dialing records to the dialer based on the DialingListID in an increasing order. However,
                                                   the records imported on the Logger-B side has a negative DialingListID, so the newer records are sent for dialing before the
                                                   older records. Overwriting imports against active dialing campaigns may result in the rejection of the latest imported record due to a conflict
                                                   with the ongoing records dialing list ID. |
|---|---|

| Note | An internal call can interrupt an agent on a reservation call. The dialer still sends the call to the agent. The call is dropped
                                             unless call waiting is enabled on the agent extension. You can avoid this scenario by giving the agent a second line for internal
                                             call use, and make sure the line is interruptible with call waiting enabled. |
|---|---|

| Note | You cannot use the transfer to VRU feature in the Direct Preview mode or the regular Preview modes. |
|---|---|

| Note | Customers are dialed based on the time zone of the first phone that is configured on this tab. The time zone is based on
                                                the prefix of the phone number and the region prefix configuration. If two phone numbers for the same customer have different
                                                time zones, the time zone for the first phone number in the list sets the times for calling both numbers. |
|---|---|

| Note | You can change the default priority order by changing the PendingOverRetryEnabled registry setting to 1 in the Campaign Manager.
                                                This setting ensures that all numbers and records are tried once before retries are attempted. |
|---|---|

| Note | Multiple dialers can serve one campaign if skill groups from each dialer's PG are assigned to the campaign. This assignment
                                       enables campaigns to be site-specific or shared across the enterprise, depending on the configuration. |
|---|---|

| Note | The configuration of blended agent with multiple skill groups per campaign is not supported in Preview/Direct Preview dialing. |
|---|---|

| Note | The Outbound Option uses area code prefixes to determine the time zone. With cell phones or VoIP phones, the area code might
                                             not correspond to the actual time zone where the call is received. |
|---|---|

| Note | CPA creates a delay before the call is transferred to an agent. Some countries require customer calls to be transferred to
                                          an agent in a certain amount of time. In those cases, you may not be able to use CPA. Because virtual CUBE does not have the Digital Signal Processors (DSP) that a physical CUBE has, it cannot support CPA. Add
                                          a dedicated physical outbound gateway to support CPA. |
|---|---|

| Note | Enable IP AMD when using CPA. If you do not enable IP AMD, the SIP dialer instructs the gateway to transfer the call to an
                                          agent without waiting for detection. |
|---|---|