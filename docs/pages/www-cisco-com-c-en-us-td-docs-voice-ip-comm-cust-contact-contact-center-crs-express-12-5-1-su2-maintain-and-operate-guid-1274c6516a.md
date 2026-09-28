---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-maintain-and-operate-guid-1274c6516a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/maintain_and_operate/guide/uccx_b_1251su2_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_01101.html
retrieved_at: 2026-08-16T21:36:29.260589+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Unified CCX Outbound Dialer Configuration

## Chapter: Unified CCX Outbound Dialer Configuration

# Unified CCX Outbound Dialer Configuration

## Outbound Feature for
                        	 Unified CCX

The Outbound feature
                              		  provides outbound dialing functionality in addition to existing Unified CCX
                              		  inbound capabilities.

The Unified CCX
                              		  Direct Preview Outbound feature is bundled along with the Unified CCX Premium
                              		  license package. The Unified CCX IVR and Agent Progressive and Predictive
                              		  Outbound feature is available with the Unified CCX Outbound license. When you
                              		  upload the Premium license, the Outbound subsystem will automatically appear in
                              		  the Subsystems menu. With this Outbound feature, you can maintain high agent
                              		  productivity by configuring contact centers for automated Outbound activities
                              		  to perform Outbound calls.

### Outbound
                           	 Characteristics

The
                                 		  Outbound feature has the following characteristics:

An Outbound
                                       				subsystem that can be monitored from the control center

IVR and Agent
                                       				Progressive and Predictive Outbound

Dialing modes
                                       				- Direct preview, Progressive and Predictive

Unified CCX
                                       				Administration web pages, REST API to configure the Outbound feature

Outbound
                                       				Historical reports

Outbound Live
                                       				Data reports (Unified Intelligence Center)

Real-Time reports are part of the Unified CCX Administration GUI real-time reporting swing application.

Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report

Access to
                                       				real-time Outbound data from the GetReportingStatistics step for Direct Preview
                                       				Outbound

### Unified CCX
                           	 Requirements

To use the
                                 		  Outbound feature, you must adhere to the following requirements:

#### Unified CCX
                                 		  Licensing Requirements

The licensing
                                 		  requirements for Outbound feature in Unified CCX will vary depending on the
                                 		  dialing modes.

For Unified CCX Outbound Direct Preview Dialer— The Unified CCX Outbound Direct Preview Dialer feature is automatically available with Premium license package without any
                                       additional license. It is no longer available with Enhanced license.

For Unified CCX Outbound
                                          				  IVR Dialer— You need to upload an Outbound license on top of the Unified CCX
                                       				premium license with the required number of IVR ports that you would like to
                                       				use for the Outbound feature.

For Unified CCX Outbound
                                          				  Agent Dialer— You need to upload an Outbound license on top of the Unified
                                       				CCX premium license with the required number of agent seats that you would like
                                       				to use for the Outbound feature.

The sum of inbound
                                             			 and outbound IVR ports should be less than or equal to a maximum number of IVR
                                             			 ports supported for your hardware model.

Once you obtain the
                                 		  Outbound license for a specific number of ports, the IVR ports will be
                                 		  distributed between the inbound and outbound IVR calls using the following
                                 		  approach based on the different scenarios explained below.

You can view the
                                 		  licensed IVR ports for outbound and inbound and the dedicated ports for both
                                 		  outbound and inbound calls by navigating to System > License
                                       				Information > Display License(s) submenu from the
                                 		  Unified CCX Administration menu bar.

Scenario 1:

If your Contact Center is already utilizing maximum licensed IVR ports supported for your hardware model, then:

Inbound calls will take precedence over the configured Outbound IVR calls.

If IVR ports are dedicated for a campaign, then the Outbound IVR ports available for the campaign will be gradually incremented
                                       as and when the inbound ports become free.

For example, if you
                                 		  have an UCS C220 hardware that supports maximum of 300 IVR ports and if you
                                 		  have 200 premium seats, then the current licensed IVR ports = 300 (Minimum of
                                 		  [seats*2, maximum supported for platform]).

In this case, if you upload
                                 		  an Outbound add-on license for 100 IVR ports and add 3 campaigns with 20
                                 		  dedicated ports each running at the same time, then the 60 Outbound IVR ports
                                 		  will be available to the campaigns only when the number of inbound ports are
                                 		  freed up to support the Outbound IVR calls.

In other words, if
                                 		  the number of inbound ports that are used during the outbound IVR campaign time
                                 		  is 280, then only 20 Outbound IVR ports will be available to the campaigns. The
                                 		  number of Outbound IVR ports will be gradually incremented depending on the
                                 		  availability of free inbound ports.

Scenario 2:

If your Contact
                                 		  Center is close to utilizing the maximum IVR ports supported for your hardware
                                 		  model, then:

Inbound calls
                                       				will take precedence over the configured Outbound IVR calls.

If IVR ports are
                                       				dedicated for a campaign and if you reach the maximum inbound call limit, then
                                       				the Outbound IVR ports available for the campaign will be gradually incremented
                                       				as and when the inbound ports become free.

For example, if you
                                 		  have an UCS C220 hardware that supports a maximum of 300 IVR ports and if you
                                 		  have 130 premium seats, then the current licensed IVR ports = 260 (Minimum of
                                 		  [seats*2, max supported for platform]).

In this case, if you upload
                                 		  an Outbound add-on license for 50 IVR ports and add 2 campaigns with 25
                                 		  dedicated ports each running at the same time and if you reach the inbound call
                                 		  limit of 260 during the outbound IVR campaign time, then only 40 ports
                                 		  (300-260) will be freed up initially for Outbound IVR calls. The number of
                                 		  Outbound IVR ports will be gradually incremented depending on the availability
                                 		  of free inbound ports.

Scenario 3:

If your Contact
                                 		  Center is using fewer ports than the maximum licensed ports supported for your
                                 		  hardware model, then the number of available IVR ports for inbound will
                                 		  continue to remain the same.

For example, if you
                                 		  have an UCS C220 hardware that supports maximum of 300 IVR ports and if you
                                 		  have 60 premium seats, then the current licensed IVR ports = 120 (Minimum of
                                 		  [seats*2, max supported for platform]).

In this case if you upload
                                 		  an Outbound add-on license for 50 IVR Outbound ports, and add 2 campaigns with
                                 		  20 dedicated ports each running at the same time, then Unified CCX will support
                                 		  40 IVR Outbound calls, and the inbound port limit will continue to be 120 as
                                 		  the sum of both inbound and outbound ports (160) are within the maximum
                                 		  licensed ports (300) for the platform.

The total number of dedicated IVR ports in all the IVR campaigns
                                             			 must be less than twice the number of Premium Seats that is equivalent to the
                                             			 Total Licensed Inbound IVR ports.

#### Unified CCX
                                 		  Subsystem Requirements

The Outbound
                                       				subsystem must be IN SERVICE.

The RmCm
                                       				subsystem must be IN SERVICE.

The Unified CM Telephony subsystem must be IN SERVICE.

The Unified CCX
                                       				Database must be IN SERVICE.

#### Geographic
                                 		  Region Support

The Outbound
                                       				feature can be used in any geographic region supported by Unified CCX. The area
                                       				codes and time zones mapping for North America are automatically prepopulated
                                       				in the system. The system uses this information to determine the time zone of a
                                       				customer’s phone number.

For regions
                                       				outside North America, administrators must enter the mapping of the
                                       				international area codes and their time zones using the Unified CCX
                                       				Administration GUI or REST API.

The national
                                       				do_not_call list is not supported in this release. Be sure to abide by the
                                       				national do_not_call list.

### Outbound
                           	 Components

This
                                 		  section provides details about the following Outbound feature components:

Unified CCX
                                       				Administration—Enables the Outbound subsystem configuration, creates campaigns,
                                       				and imports contacts to generate the dialing list.

Outbound
                                       				subsystem—Is responsible for the following tasks:

Manages
                                             					 campaigns

Maintains
                                             					 Outbound system configurations

Manages
                                             					 the dialing list

Reserves
                                             					 agents

Makes
                                             					 Outbound calls

Updates
                                             					 the call data in the dialing list based on the outcome of the call

Decides
                                             					 which contact records to retrieve from a campaign

The
                                 		  Outbound subsystem views campaigns as logical entities that group a set of
                                 		  contacts together in a dialing list. Campaigns deliver outgoing calls to
                                 		  agents. Agents are assigned to campaigns using CSQs.

## Supported Dialers
                        	 and Dialing Modes for Outbound

In
                              		  addition to the existing Direct Preview Outbound dialer option, Unified CCX
                              		  supports IVR-based and agent-based dialing. If you select the
                              		  IVR-based option for a campaign, the outbound calls are handled by IVR scripts.
                              		  If you select the agent-based option for a campaign, the outbound calls are
                              		  handled by agents. Typical applications include appointment and bill-payment
                              		  reminders.

### Unified CCX
                           	 Outbound Dialing Modes

The Outbound feature in Unified CCX Release supports the following dialing modes:

Direct preview dialing mode

Progressive dialing mode

Predictive dialing mode

Tip

For agent predictive and agent progressive outbound calls, disable the Call Waiting option on the agent's phone to allow agents
                                             to preview a customer call on Finesse Desktop before the call is placed. The Call Waiting option must be disabled (default)
                                             in Unified Communications Manager on each Outbound agent phone to ensure that every customer call successfully transfers to an available agent.

When an Outbound call is transferred or conferenced to another agent, the second or subsequent agents are not counted towards
                                 the number of Outbound licenses. For example, if you have five seats licensed for Outbound and Agent1 gets an Outbound call,
                                 Agent1 accepts the call and conferences in Agent2 and Agent3. Now, three agents are on one Outbound call but only Agent1 is
                                 considered an Outbound agent and you are only using one licensed seat. Consequently, your system allows four more Outbound
                                 calls to agents.

### Direct Preview
                           	 Dialing Mode

The direct preview
                                 		  dialing mode allows agents to preview a customer call on Cisco Finesse before
                                 		  the call is placed. The advantage of this mode is that an agent is already on
                                 		  the call when the customer answers and can quickly begin talking with the
                                 		  customer immediately.

### Progressive
                           	 Dialing Mode

In the Progressive
                                 		  Dialing mode, you can specify a fixed number of lines that will always be
                                 		  dialed per available IVR port or per available agent. You can configure the
                                 		  progressive dialer settings for each campaign while creating the campaign
                                 		  through Unified CCX Application Administration web interface. You can also
                                 		  update the configuration at a later date.

### Predictive Dialing
                           	 Mode

The Predictive
                                 		  Dialing mode works similar to the Progressive Dialing mode in terms of dialing
                                 		  the Outbound calls. The difference remains in tuning the lines per port or per
                                 		  agent depending on the abandoned call-rate thus eliminating manual intervention
                                 		  as in the case of the Progressive Dialer.

In other words, in
                                 		  the Predictive Dialing mode, the Dialer adjusts the number of customers to dial
                                 		  per available IVR port or per available agent. The number of lines to dial is
                                 		  calculated by an algorithm and gets updated automatically.

## Configure Outbound
                        	 Subsystem in Unified CCX

Step 1

Configure the
                                       			 general properties of the outbound subsystem. See Configure General Outbound Properties .

Step 2

(Optional) If
                                       			 the dialing list contains contacts outside of North America or if Unified CCX
                                       			 is installed outside of North America, manually add the area codes and their
                                       			 corresponding time zones. See Add New Area Code .

Step 3

Configure the
                                       			 SIP Gateway parameters to enable communication between Unified CCX and the SIP
                                       			 gateway for IVR and agent-based progressive and predictive campaigns. See Configure SIP Gateway .

Step 4

Configure the
                                       			 campaign. See Add New Campaign .

## Configure General
                        	 Outbound Properties

General
                              		  Outbound properties refer to the settings that is common for all the campaigns.

Caution

Area code and long
                                          			 distance prefix configuration changes made to the Outbound subsystem do not
                                          			 take effect for the calls/contacts that are currently in the Outbound
                                          			 subsystem’s memory. For example, if you change the long distance prefix or
                                          			 local area code, the contacts that are already in the Outbound subsystem's
                                          			 memory will continue to use the old long distance prefix and local area code.

To
                              		  configure general Outbound properties, complete the following steps.

Step 1

From the Unified
                                       			 CCX Administration menu bar, choose Subsystems > Outbound > General .

The General
                                          				Configuration web page opens.

Step 2

Specify the
                                       			 following fields in the General Configuration section:

Field

Description

Customer Dialing Time Range (hh:mm)

Start Time/End Time

The
                                                      							 time range during which a customer can be called. This time range supersedes
                                                      							 the time range of the individual campaigns and ensures that a customer is never
                                                      							 called outside the legally allowed time range for that country. This is a
                                                      							 mandatory field.

For
                                                      							 example, in the USA, the Federal Communications Commission (FCC) specifies the
                                                      							 legal time range as 8 AM to 9 PM. This does not apply to callbacks, since the
                                                      							 customer explicitly requested to be called at a certain time. This time range
                                                      							 is always converted to the local time for each contact record.

Default = 8:00 AM to 9:00 PM (USA FCC regulations)

Outbound Call Timeout (seconds)

If an agent does not respond to the
                                                      											Outbound preview call on Finesse Desktop within the
                                                      											timeout duration that is specified in this field, the
                                                      											system sets the agent to the Not Ready state.

If an agent does not respond to the Outbound progressive or predictive call on Finesse
                                                      											Desktop within the timeout duration that is specified in
                                                      											this field, then the call is dropped. The system sets
                                                      											the agent to the Ready or Not Ready state depending on
                                                      											the option that is selected for Agent State after Ring
                                                      											No Answer field in the System Parameters Configuration
                                                      											Web Page. This is a mandatory field.

Default = 60 seconds, Range = 5 to 3600 seconds.

If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call.

Dialing Prefix

The
                                                      							 number that is prefixed to the phone number when the dialer dials an outgoing
                                                      							 call (also referred to as switch prefix). This number can have a numeric value,
                                                      							 including 0 or leading zeros. This is a user defined value.

For
                                                      							 example, if the dialing prefix is set as 9 and the phone number of the contact
                                                      							 is 54321, then the dialer will dial out '954321'.

Long
                                                      							 Distance Prefix

This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the long distance prefix in the phone number that is dialed by the
                                                      							 dialer. It is first determined whether it is an international or domestic
                                                      							 number by the presence of any matching International Prefix set in the General configurations page.

When
                                                      							 the phone number is a domestic number, based on the matching local area code
                                                      							 set, it is determined if it is a local number or a long distance number.

For
                                                      							 example, if the long distance prefix is set as 044, the phone number of the
                                                      							 contact is 54321, and if the Include Long Distance Prefix is enabled, then the dialer dials out '4454321'.

International Prefix

This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the international prefix in the phone number for that international
                                                      							 number. If there is no International Prefix, then the number is considered to
                                                      							 be a domestic number.

If
                                                      							 the imported number doesn't contain an international prefix but has a "+" sign
                                                      							 prefixed to the phone number, then it is considered to be an international
                                                      							 number.

Local Area Code

The
                                                      							 area code of the location from where the PSTN call is made from. This number
                                                      							 can have a numeric value, including 0 or leading zeros. The local area code
                                                      							 when set in the General configurations page, helps to determine the
                                                      							 prefix value in the domestic phone number which is included in the outgoing
                                                      							 call if the Do Not Remove Local Area Code When Dialing is
                                                      							 checked.

Do
                                                      							 Not Remove Local Area Code When Dialing

If
                                                      							 this box is checked, the local area code is included when dialing the phone
                                                      							 numbers within this area code. If it is unchecked, then the local area code is
                                                      							 stripped from the phone number before dialing the local numbers. It is expected
                                                      							 that when contacts are imported into the system, the phone numbers include the
                                                      							 area code. For international phone numbers, the country code must be included
                                                      							 when importing contacts.

Include Long Distance Prefix

This
                                                      							 field will be displayed only if you check the Do Not Remove Local Area Code When Dialing check
                                                      							 box. For local numbers, the long distance prefix will be prefixed only if this
                                                      							 check box is checked.

The
                                                      							 long distance prefix will be prefixed to the phone number for all non-local
                                                      							 numbers (the numbers that do not start with local area code) irrespective of
                                                      							 the status (checked/unchecked) of this check box.

Auto Answer

If this box is checked, any agent-based progressive or predictive campaign call that
                                                      											gets transferred to the agent is automatically answered
                                                      											by Unified CCX. A beep tone always notifies the agent
                                                      											that the call has been answered. This option is enabled
                                                      											by default.

If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box.

Assigned CSQs

Assigned CSQs are CSQs that are used by the Outbound subsystem.
                                                      							 This is a mandatory field. To allocate CSQs for Outbound:

Select a CSQ in the Available CSQs list.

Select a value from the % of Logged in Agents for Outbound drop-down list to indicate what percentage of the CSQ is allocated for Outbound.

Click the left arrow icon to move the CSQ to the Assigned CSQs list.

The
                                                      							 selected CSQ is removed from the Available CSQs box and appears in the Assigned CSQs box with the percentage allocation in
                                                      							 parentheses next to the CSQ name.

Available CSQs

The
                                                      							 Available CSQs pane displays all CSQs configured in the CSQ Configuration page
                                                      							 under the RmCm subsystem configuration.

% of
                                                      							 Logged in Agents for Outbound

The
                                                      							 % of Logged in Agents for Outbound field indicates the percentage of logged in
                                                      							 agents in each of the selected CSQs that are allocated for handling Outbound
                                                      							 calls.

The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level.

The number of agents allocated for OB is considered as
                                                      							 the whole number of the % of Logged in Agents for Outbound . Any decimal
                                                      							 value in the value is not considered. For example, If the percentage of
                                                      							 allocation is 95% and 4 agents are logged in, then the number of agents
                                                      							 allocated for OB are 3 [95% * 4 = 3.8 (decimal value is neglected)]. If the
                                                      							 percentage of allocation is 80% and 4 agents were logged in, then the number of
                                                      							 agents allocated for OB are 3 [(80% * 4 = 3.2 (decimal value is neglected)].

Step 3

Click Update icon that is displayed in the tool bar in the
                                       			 upper, left corner of the window or the Update button that is displayed at the bottom of the
                                       			 window.

The System
                                          				Options components are now updated.

### Callbacks

A
                                 		  customer can request a callback at a specific callback phone number and also
                                 		  specify the time/date of the callback. The Outbound subsystem stores this
                                 		  information (the callback phone number, date, time) in the dialing list table.

The
                                 		  Outbound subsystem handles the callback as follows:

Convert to
                                       				GMT—The callback date and time specified with respect to the customer's time
                                       				zone is converted to GMT time zone and then stored in the database.

Agent not
                                       				Available—When the Outbound subsystem looks up the database for contacts, it
                                       				first checks the callbacks. The default callback time limit is 15 minutes (can
                                       				be changed) before and after the customer-specified time. If an agent is
                                       				available, then the Outbound subsystem places the callback. If an agent is not
                                       				available, the Outbound subsystem retries agent availability (agent state)
                                       				after 10 minutes.

Missed
                                       				Callbacks—If the Unified CCX system is unable to process a callback request in
                                       				the specified time, you have three action options:

Reschedule
                                             					 it to the same time on the next business day.

Mark it as
                                             					 another retry (the callback phone number is removed and the callback date time
                                             					 is ignored). In this case, it moves out of the call back state and into the
                                             					 retry state.

Close the
                                             					 record (never dialed again).

Agent reclassifications—If calls were retrieved and presented to the agent and if the agent reclassifies it (for example,
                                       changed it to answering machine status), then the call status is updated to the answering machine.

Caution

If a callback is presented and the callback number is invalid (or busy), the callback continues to be retried irrespective
                                             of the number of retries set (for normal busy/invalid). It will be retried until the callback time limit expires.

### Outbound Area Code Functionality

In the Outbound option, the area code determines the
                                 		  geographical location of the phone number you dial, which correspondingly
                                 		  provides the Greenwich Meridian Time (GMT) zone. The db_cra database contains a
                                 		  mapping of the area codes to the time zones.

The U.S. area code mappings are provided along with the
                                 		  product. International customers should provide their own data and add it to
                                 		  the database.

### Configuration Updates

Whenever Outbound parameters are modified in the Unified CCX
                                 		  Administration GUI, the changes take effect immediately. If a new CSQ is added
                                 		  using the Subsystems > RmCm > Contact
                                       				Service Queues menu option, it is instantly displayed
                                 		  in the list of available CSQs in the General configuration page in the Unified
                                 		  CCX Administration GUI, as this list is dynamically updated. If a CSQ is
                                 		  modified and if this impacts the allocation of agents, the Outbound subsystem
                                 		  is aware of this change as it refreshes the list of agents in each relevant CSQ
                                 		  periodically.

If a configuration change affects the Outbound contacts dialing
                                       				process (for example, if a campaign is disabled or a CSQ is removed from a
                                       				campaign), the Outbound subsystem stops processing the Outbound contacts,
                                       				recalls these contacts to the database, and resets the call status to Pending.

If a campaign start time is changed, the Outbound subsystem checks
                                       				if the campaign is enabled. If it is enabled, and if the new start time is
                                       				after the current time, it performs the following actions:

Sends a recall contact message to the Outbound subsystem
                                             					 passing the campaign ID.

For all Outbound contacts for this campaign in the Outbound
                                             					 subsystem's memory that are waiting to be dialed out, it resets all Outbound contacts to the Pending state
                                             					 and clears them from memory.

If the campaign is disabled or if the new start time is before
                                       					 the current time, the Outbound subsystem ignores this change.

If campaign end time is changed, the Outbound subsystem checks if
                                       				the campaign is enabled. If it is enabled, and if the new end time is before
                                       				the current time, it performs the following actions:

Sends a recall contact message to the Outbound subsystem
                                             					 passing the campaign ID.

For all the Outbound contacts for this campaign in Outbound
                                             					 subsystem's memory that are waiting to be dialed out, it resets all the Outbound contacts to the Pending
                                             					 state and clears them from memory.

If the campaign is disabled or if the new end time is after
                                       					 the current time, the Outbound subsystem ignores this change.

If a CSQ is deleted from a campaign or if the CSQ itself is
                                       				deleted, the Outbound subsystem sends a recall contacts message with the csq ID
                                       				of the deleted CSQ. It also reallocates any Outbound contacts in its memory
                                       				that are currently allocated to this CSQ among the other existing CSQs for this
                                       				campaign.

### CSQ Agent Pool Allocation

You need to specify a percentage of total agents in the
                                 		  assigned CSQs to be allocated for Outbound calls. This pool of agents is shared
                                 		  by all Outbound campaigns.

Tip

The CSQs for Outbound are the same as the CSQs for inbound. If you
                                             			 need more CSQs, you must first configure them in Unified CCX and assign the
                                             			 required CSQs for agents as required by your configuration, before allocating
                                             			 them.

## Configure
                        	 Application and Trigger for Outbound Campaign

For IVR campaigns,
                              		  configure application and trigger before you create the campaign.

For an agent-based
                              		  predictive campaign and an agent-based progressive campaign, configure the
                              		  application and trigger if you configure the answering machine and the
                              		  abandoned call treatment to transfer to IVR.

Step 1

Create a Call
                                       			 Control Group for Outbound type with the required number of IVR ports to be
                                       			 used for outbound campaigns. See Add New Call Control Group .

Step 2

Create an
                                       			 application, which will be used for the outbound campaign. See Cisco Applications Configuration .

Step 3

Create a
                                       			 trigger and assign the newly created Outbound Call Control group to this
                                       			 trigger. See Cisco Applications Configuration .

Step 4

Create a new
                                       			 progressive or predictive outbound campaign. See Add New Campaign .

Step 5

Import
                                       			 contacts for the campaign. See Import Contacts for Campaign .

## Add New
                        	 Campaign

Use the
                              		  Campaign component to configure properties for the campaign, including the
                              		  campaign name and description, CSQ selection, and the time range when a
                              		  campaign can call contacts.

Complete
                              		  the following steps to define or modify the settings that apply to a campaign.

Step 1

From the
                                       			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns .

The Campaign
                                          				web page opens, displaying the details of existing campaigns, if any. Click an
                                          				existing campaign to view or update the configuration settings for the
                                          				campaign.

Step 2

Click
                                       			 the Add
                                          				New icon in the tool bar in the upper, left corner of the window or
                                       			 the Add
                                          				New button at the bottom of the window.

Add a New
                                          				Campaign web page opens up where you can specify the campaign type and the
                                          				dialer type for the campaign using the following fields.

You need to
                                                      				  upload an Outbound license on top of the Premium license for Unified CCX to
                                                      				  create a campaign for Outbound.

Field

Description

Select the type of the
                                                         								campaign

Campaign Type

Type
                                                      							 of the campaign to be used for outbound calls. You can specify any one of the
                                                      							 following two campaign types:

Agent-based—If you select this, all the outbound calls in a campaign will be handled by the available agents.

IVR-based—If you select the IVR-based option, the outbound calls in a campaign will be handled by the IVR scripts.

Select the type of dialer
                                                         								for the campaign

Description

The dialer type options available for a campaign will vary depending on the selected Campaign Type.

If you select Agent-based campaign type, then you can select any one of the following dialer types:

Direct Preview (default)

Progressive

Predictive

If you select IVR-based campaign type, then you can select any one of the following dialer types:

Progressive (default)

Predictive

Once the campaign is created, you cannot change the Campaign Type and Dialer Type.

After you select the campaign type and dialer type, click Next to continue. The Campaign Configuration web page opens, displaying the following three column headings:

Parameter
                                                					 Name

Parameter
                                                					 Value

Suggested
                                                					 Value

You can
                                          				specify values for a new campaign or modify values for an campaign using the
                                          				fields listed in the Parameter Value column. See the table below for a list of
                                          				fields along with their description.

The Suggested Value displays the default configuration value for each campaign. You can refer to these values if you want
                                          to revert any changes made to one or more parameters listed in the Campaign Configuration web page.

Field

Description

Campaign Name

Name
                                                      							 of the campaign (must be a unique identifier). This is a mandatory field.

Enabled

Indicates the current state of the campaign to the Outbound
                                                      							 subsystem.

Yes
                                                      							 = The campaign is currently active.

No =
                                                      							 The campaign is currently inactive (default).

Description

Description of the campaign.

Start Time/End Time (hh:mm) AM PM Time Zone

Indicate the time range during which the campaign runs. These
                                                      							 are mandatory fields. The name of the primary time zone is also displayed
                                                      							 adjacent to these two field values.

Default = 8:00 AM - 9:00 PM Pacific Standard Time (USA FCC
                                                      							 regulations).

Campaign Calling Number

The campaign calling number is the number that will be displayed to the contact. This number is used by the dialer. This is
                                                      a mandatory field.

Maximum Attempts to Dial Contact

The maximum number of times the Outbound subsystem attempts to
                                                      							 dial a contact beyond which the call status will be marked as closed. You can
                                                      							 choose this value from the drop-down list box.

Default = 3, Range = 1 to 3.

Callback Time Limit

The time period before and after the scheduled callback time
                                                      							 during which the Outbound subsystem attempts to dial out a callback. For
                                                      							 example, if a callback was scheduled for 9:30 am and if the Callback Time Limit
                                                      							 is set to 15 minutes, then the Outbound subsystem calls the customer anytime
                                                      							 between 9:15 am to 9:45 am.

This field is also used to determine the dialing time range for
                                                      							 the Retries settings in the Add New Campaign web page.

Default = 15 minutes, Range = 1 to 60 minutes.

Fields displayed only if
                                                         								you have selected IVR-based campaign type

Application Trigger

This is the JTAPI trigger associated with this campaign. There
                                                      							 will one-to-one mapping between a campaign and an application trigger. Only
                                                      							 those triggers that are not associated with any other campaigns are displayed
                                                      							 in the trigger list.

Application Name

The name of the application associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated.

Fields displayed only if
                                                         								you have selected Agent-based campaign type

Abandoned Call Treatment

If the agent is not available to handle the call, you can choose to abandon the
                                                      							 call or transfer it to IVR by selecting the desired radio button in this field.
                                                      							 If you choose to transfer the call to IVR, a trigger field and an application
                                                      							 name field appears for selection.

The trigger field is a drop-down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list.

The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated.

Transfer to IVR radio button is enabled by default.

This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign.

If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port.

Assigned CSQs

The CSQs from which agents are selected for Outbound calls for
                                                      							 this campaign. This is a mandatory field.

For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign.

CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns.

CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns.

Available CSQs

For direct preview campaigns—CSQs that are allocated for
                                                      							 outbound but not assigned to any progressive or predictive agent-based
                                                      							 campaign.

For progressive and predictive agent-based campaigns—CSQs that
                                                      							 are allocated for outbound and not assigned to any other campaign.

Fields displayed only if
                                                         								you have selected Direct Preview dialer type for an Agent-based campaign

Contact Records Cache Size

The number of contact records the Outbound subsystem retrieves
                                                      							 from the database in bulk for dialing. The allowed values are 1–100. This is a
                                                      							 mandatory field. For example, if 50 records are retrieved in bulk for campaign1
                                                      							 and 10 for campaign2 and they are running at the same time, the Outbound
                                                      							 subsystem attempts to place 50 Outbound calls for campaign1 and 10 Outbound
                                                      							 calls for campaign2. The number of Outbound calls actually placed for each
                                                      							 campaign depends upon the number of agents available for the respective
                                                      							 campaigns.

Once all the records retrieved for a campaign have been dialed,
                                                      							 the Outbound subsystem retrieves another batch of records for that campaign.
                                                      							 Over a period of time, it is likely that more contacts would have been called
                                                      							 from campaign1 than from campaign2.

If
                                                      							 two campaigns run simultaneously and share CSQs or agents, the records in both
                                                      							 campaigns may not be processed at the same rate even if their contact cache
                                                      							 sizes are identical. It is possible that more records from one of these two
                                                      							 campaigns is processed before the other.

Default = 20, Range = 1 to 100

Answering Machine Retry

If
                                                      							 you select Yes, then the Outbound subsystem retries the contact after all the
                                                      							 callbacks and pending contacts for the campaign are dialed out.

Default = No

The following fields in
                                                         								Dialing Options are displayed if you have selected IVR-based campaign type

Number of Dedicated Ports

Number of dedicated IVR ports that you want to reserve for this
                                                      							 campaign based on the number of CTI ports available in the outbound call
                                                      							 control group for the campaign duration. That is, the total number of dedicated
                                                      							 IVR ports for the selected campaign cannot exceed the maximum licensed ports
                                                      							 for outbound IVR minus the sum total of IVR ports dedicated to other campaigns
                                                      							 running at the same time.

You can enter or update this value for a campaign only after
                                                      							 associating a trigger with the campaign. Default value = 0, Range = 0 to number
                                                      							 of available ports for the campaign duration.

For example, if you have a medium or large profile VM, which
                                                      							 supports maximum of 300 IVR ports with 50 licensed ports for outbound IVR and
                                                      							 you have already dedicated:

20 ports for Campaign1, which runs between 10–12 pm

10 ports for Campaign2, which runs between 2–4 pm, then the
                                                            								  number of dedicated IVR ports that you can enter in this field for a new
                                                            								  campaign cannot exceed:

30 ports if the new campaign runs between 10–12 pm and

40 ports if the new campaign runs between 2–4 pm and

50 ports if the new campaign runs during any time other than
                                                                  										10–12 pm and 2–4 pm

If
                                                      							 the number of configured ports for a campaign is greater than the available
                                                      							 number of licensed ports at the specified campaign time, then an alert message
                                                      							 stating the same will be shown while saving the campaign.

Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns.

See Unified CCX Requirements to know how the licensed IVR ports are distributed between the inbound and
                                                      							 outbound IVR calls in different scenarios.

Lines Per Port (1-3)

Number of lines to be dialed for each port. The dialer will try
                                                      							 to connect as many live voices to the available port(s) where IVR script is
                                                      							 playing and it will disconnect the remaining calls. The probability of
                                                      							 abandoned calls increases geometrically as the lines per port increases.

In
                                                      							 an IVR based progressive campaign, you can configure the number of lines to
                                                      							 dial per port at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per port * Available number of
                                                      							 ports.

In
                                                      							 an IVR based predictive campaign, this is the seed value that is passed to the
                                                      							 predictive algorithm. Initially the dialer starts dialing with this value.

This is a mandatory field.

Default value = 1.5; Range = 1 to 3.

The following fields in
                                                         								Dialing Options are displayed if you have selected Agent-based campaign
                                                         								type

Lines Per Agent (1-3)

Number of lines to be dialed for each agent. The dialer will try
                                                      							 to connect as many live voices to the available agent(s) and it will disconnect
                                                      							 the remaining calls. The probability of abandoned calls increases geometrically
                                                      							 as the lines per agent increases.

In
                                                      							 an agent-based progressive campaign, you can configure the number of lines to
                                                      							 dial per agent at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per agent * Available number of
                                                      							 agents.

In an agent-based predictive campaign, this is the seed value that is passed to the predictive algorithm. Initially the dialer
                                                      starts dialing with this value.

This is a mandatory field.

Default value = 1.5; Range = 1 to 3.

Callback Missed

Determines the action that should be taken on the contacts that
                                                      							 were not called back. The three options for this field are:

Reschedule for same time next business day (default)

Mark it for a retry

Close the record.

The following fields in
                                                         								Dialing Options are common if you have selected Progressive or Predictive
                                                         								dialer type for IVR-based and Agent-based campaigns

Handle Low Volume as Voice

Determines whether a low volume call should be treated as voice
                                                      							 or disconnected. Select Yes or No radio button accordingly.

Default is Yes, which means low volume calls are handled as
                                                      							 voice and they are connected to an IVR port or an agent.

Answering Machine Treatment

If
                                                      							 the outbound call detects an answering machine, you can choose to end the call
                                                      							 or transfer it to IVR by selecting the desired radio button in this field.

For agent-based campaigns, if you choose to transfer the call to IVR, a trigger
                                                      							 field and an application name field appears for selection.

The trigger field is a drop down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list.

The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated.

Transfer to IVR radio button is enabled by default.

The following fields in
                                                         								Dialing Options are common if you have selected Predictive dialer type for
                                                         								IVR-based and Agent-based campaigns

Predictive Correction Pace (10-1000)

The number of calls that were answered by live voice that the
                                                      							 predictive algorithm should consider for each iteration. This is directly
                                                      							 proportional with the correction frequency made in the Lines Per Port or Lines
                                                      							 Per Agent parameter. This is a mandatory field. Default value = 100, Range = 10
                                                      							 to 1000.

It is advisable not to change this value.

Predictive Gain

The Gain parameter controls the size of the lines per port or
                                                      							 lines per agent corrections. This is directly proportional to the size of the
                                                      							 lines per port or lines per agent correction.

This is a mandatory field. Default value = 1.0, Range = Greater
                                                      							 than 0 to 1.0.

It is advisable not to change this value.

Call Abandon Limit (0-100)

Call abandon percentage, which should be within the limit
                                                      							 specified by Federal Trade Commission (FTC). This is a mandatory field.

Default value - 3%, Range 0-100%. This means that no more than
                                                      							 three percent of calls that are answered by a person are abandoned, measured
                                                      							 per day per calling campaign.

The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an IVR-based campaign

Maximum Lines Per Port (1-3)

Maximum number of lines to be dialed for each port. You can
                                                      							 configure the maximum number of lines that can be dialed per port and the
                                                      							 predictive algorithm ensures that it does not exceed this number.

This is a mandatory field. Default value = 3.0, Range = 1 to 3.

The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an Agent-based campaign

Maximum Lines Per Agent (1-3)

Maximum number of lines to be dialed for each agent. You can
                                                      							 configure the maximum number of lines that can be dialed per agent and the
                                                      							 predictive algorithm ensures that it does not exceed this number.

This is a mandatory field. Default value = 3.0, Range = 1 to 3.

Dial Settings (displayed
                                                         								if you have selected IVR-based or Agent-based campaign types)

No
                                                      							 Answer Ring Limit

The duration for which the progressive/predictive dialer should
                                                      							 allow the customer phone to ring before disconnecting an unanswered call.

The duration is calculated from the time the dialer receives the
                                                      							 ringing message from the gateway. If the dialer does not receive any ringing
                                                      							 message from the gateway within the time duration entered for this field, then
                                                      							 the dialer waits for the same time duration one more time before disconnecting
                                                      							 the call.

For example, if you have configured the value for No Answer Ring
                                                      							 Limit as 30 seconds, then the dialer will wait for 60 seconds before
                                                      							 disconnecting the call.

Default = 15 seconds, Range = 1 to 60 seconds.

This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field.

For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds.

Abandoned Call Wait Time

For IVR-based progressive and predictive outbound campaigns, if
                                                      							 the customer disconnects the call within the time set here, then the call is
                                                      							 classified as customer abandoned.

For agent-based progressive and predictive outbound campaigns,
                                                      							 if the customer or the agent disconnects the call within the time set here,
                                                      							 then the call is classified as customer abandoned.

This is a mandatory field.

Default value = 2 seconds, Range = 1 to 10 seconds.

Retries (displayed if you
                                                         								have selected IVR-based or Agent-based campaign types): Set the value for
                                                      							 the following four fields as “0” if you want to disable retry option for an
                                                      							 existing IVR or agent based outbound campaign.

No
                                                      							 Answer Delay

The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a no-answer call.

Default value = 60 minutes.

Though the default value is 60 minutes, the retry attempt will
                                                      							 not be made after 60 minutes. This is based on the value set for the Callback
                                                      							 Time Limit configured in the subsystem. For example, if a callback was
                                                      							 scheduled for 9:30 am and if the Callback Time Limit is set to 15 minutes, then
                                                      							 the Outbound subsystem calls the customer anytime between 9:15 am to 9:45 am.

The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit.

Busy Signal Delay

The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a busy telephone number.

Default value = 60 minutes.

This parameter is also based on the value set for the
                                                      							 Callback Time Limit as described above in the No Answer Delay.

Customer Abandoned Delay

For IVR-based progressive and predictive outbound campaigns, if a customer abandons a call, the time duration (in minutes)
                                                            after which the dialer should call the customer back.

For agent-based progressive and predictive outbound campaigns, if a customer or an agent abandons a call, the time duration
                                                            (in minutes) after which the dialer should call the customer back.

Default value = 0

Dialer Abandoned Delay

If
                                                      							 the dialer abandons a call, the time duration (in minutes) after which the
                                                      							 dialer should call back the customer.

Default value = 0

Step 3

Click Add or Save to save the configuration changes. While saving
                                       			 a new or updated campaign, the Outbound subsystem validates the Session values
                                       			 in the application and trigger pages based on following criteria, and it might
                                       			 display an alert message to increase Session value in application and trigger
                                       			 pages:

In case
                                                					 of a Progressive campaign, the outbound subsystem checks whether the Lines Per
                                                					 Port * Dedicated Port for IVR-based campaigns and Lines Per Agent * Dedicated
                                                					 Agent for agent-based campaigns is greater than the minimum of the Session
                                                					 value in application and trigger.

In case
                                                					 of a Predictive campaign, the outbound subsystem checks whether the maximum
                                                					 Lines Per Port * Dedicated Port for IVR-based campaigns and maximum Lines Per
                                                					 Agent * Dedicated Agent for agent-based campaigns is greater than minimum of
                                                					 the Session value in application and trigger.

You should
                                          				increase the Session values in the application and trigger to the suggested
                                          				value in the alert message to reduce the number of abandoned calls in an
                                          				Outbound campaign.

Once you
                                          				create a campaign, you need to import contacts for the campaign.

## Import Contacts
                        	 for Campaign

Caution

You must verify
                                       		  all the contacts against the national do_not_call list before importing them.

When you import contacts that have agent extension numbers, ensure that the agents are not logged in when the campaigns are
                                             running.

When you import contacts for campaign, the order of field names is as per the last selected order for that campaign.

When Allow Duplicate Contacts option is not selected in both Manual and Automatic import, there could be a difference between the number of contacts imported
                                             and the number of remaining contacts. This is because many of the contacts imported could be duplicates in the database and
                                             are overwritten.

When Phone 1 of a contact is dialed and the CPA marks it as Busy or Unanswered the same number is retried based on the retry
                                             count and delay configured in the campaign. When the retry count reaches the maximum value, the contact is marked as closed.
                                             The other phone number for a given contact is dialed only when the called number is classified as Modem, Fax or Invalid.

Each time contacts are imported, they are appended to the existing list of contacts for the selected campaign. If the new
                                             list contains a contact with the same Phone 1 value as the Phone 1, Phone 2, or Phone 3 value, or the same Phone 2 value as
                                             the Phone 1, Phone 2, or Phone 3 value, or the same Phone 3 value as the Phone 1, Phone 2, or Phone 3 value, of an existing
                                             contact, the existing contact is overwritten with the new contact information. The call history for the contact (if any) is
                                             retained.

For supervisors to Schedule Import of contacts for a campaign, you must configure the campaign to use SFTP or HTTPS.

For a manual import of contacts :

Attention

The contacts file should be ASCII-encoded or UTF-8 encoded if it contains special characters (for example, if the contact
                                             names are in Chinese, Russian, Japanese, and so on).

When you want to import multiple dialing lists, ensure that you select one dialing list at a time.

The maximum limit of contacts in the contacts file is 100 thousand.

The maximum limit of contacts that can be imported per campaign is determined by:

Number of contacts that are already imported and yet to be dialed out.

The number of contacts present in the contacts file being imported.

You must not initiate the manual import of contacts and automatic import of contacts using SFTP or HTTPS at the same time.
                                             If a manual import is attempted when an automatic import is in progress, it would fail.

For a scheduled import of contacts :

Attention

The contacts file should be ASCII-encoded or UTF-8 encoded if it contains special characters (for example, if the contact
                                             names are in Chinese, Russian, Japanese, and so on).

The maximum limit of contacts in the contacts file is 100 thousand.

The automatic import process would stop importing contacts for a campaign after the campaign has 20,000 contacts remaining
                                             (yet to be dialed out). After the contacts are dialed out, then the next scheduled import would import additional contacts.

The maximum limit of contacts that can be imported per campaign is determined by:

Number of contacts that are already imported and yet to be dialed out.

The number of contacts present in the contacts file being imported.

For example: Assume a new campaign and a contacts file has 100 thousand contacts that are scheduled for import. When the import
                                                   is attempted for the first time, the first 20,000 (from 1 to 20,000 contact) contacts are fetched and imported for the campaign.

Before the next scheduled import, assume system has successfully dialed out 5000 contacts and 15000 contacts are remaining.
                                                   In this, case, when next import is attempted as per the schedule, the system would import 5000 contacts for the remaining
                                                   capacity of the campaign (20000-15000=5000 contacts). Thus, assuming that the contacts file has not changed across the imports,
                                                   the system would import the contacts from 20001 to 25000 in the contacts file.

You must not initiate the manual import of contacts and automatic import of contacts using SFTP or HTTPS at the same time.
                                             If a manual import is attempted when an automatic import is in progress, it would fail.

If there are multiple imports scheduled at the same time, the import of contacts happen one at a time.

When an automatic import of contacts is in progress and if there is a Unified CCX Engine fail over, the import will be terminated
                                             and its status is not available on the Automatic Import Contacts page.

### Manual Import of
                           	 Contacts for Campaign

To
                                 		  import contacts manually for a selected campaign, complete the following steps.

Step 1

From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns .

The Campaigns
                                             				web page opens, displaying the details of existing campaigns.

Step 2

Click the
                                          			 hyperlink below the Name column for the campaign for which you want to import
                                          			 the contacts.

The Campaign
                                             				Configuration web page opens for the selected campaign.

Step 3

Click Import
                                             				Contacts . The Import Contacts web page opens.

Step 4

To import
                                          			 contacts from a CSV or a TXT file, click the Manual
                                             				Import Contacts tab.

Step 5

Navigate to
                                          			 the directory that contains the imported fields in the same
                                             				order as they appear in the text file. Specify a filename to import the
                                          			 contacts from the fields being imported.

A contact list can contain up to 7 fields:

Account Number - The account number of a contact. The account number can be a maximum length of 25 characters.

First Name - The first name of a contact. The first name can be a maximum length of 50 characters.

Last Name - The last name of a contact. The last name can be a maximum length of 50 characters.

Phone1 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone1 is
                                                   mandatory and must be specified.

Phone2 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number.

Phone3 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number.

Dial Time - The time to dial a number for individual contacts on the current date. The format to be used for this field is
                                                   HH:MM. For example, to specify the dialing time as 08:25 am, the dial time field value should be 08:25 and for 03:45 pm, the
                                                   dial time field value should be 15:45. This field is applicable only for Direct Preview Outbound campaigns.

Step 6

Check the Allow Duplicate Contacts option, if required.

Allow Duplicate Contacts

A record is considered duplicate when the phone number in any of the three phone fields (Phone 1, Phone 2, and Phone 3) of
                                             the records being imported:

Exists in any of the three phone fields of the other contacts being imported.

Exists in any of the three phone fields of the contacts previously imported for the campaign that are dialed out since last
                                                   midnight or yet to be dialed out.

If this option is not selected:

The contacts identified as duplicates are not imported for the campaign.

If this option is selected:

The check for duplicate contacts is not performed and all contacts are imported as is.

By
                                                         				  default this option is not selected.

Step 7

Click Import .

#### What to do next

While uploading
                                 		  outbound contacts in a HA over WAN deployment of Unified CCX, if all the
                                 		  contacts that are being uploaded exist in the database and are being modified,
                                 		  follow these guidelines to avoid long delays:

Upload the
                                       				contacts during non-peak hours.

Upload in
                                       				batches of 500 contacts or less.

### Schedule Import of
                           	 Contacts Using SFTP or HTTPS

Step 1

From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns .

The Campaigns
                                             				web page opens, displaying the details of existing campaigns.

Step 2

Click the
                                          			 hyperlink below the Name column for the campaign for which you want to import
                                          			 the contacts.

The Campaign
                                             				Configuration web page opens for the selected campaign.

Step 3

Click Import
                                             				Contacts . The Import Contacts web page opens.

Step 4

To
                                          			 automatically import contacts from a remote server using SFTP or HTTPS, click
                                          			 the Automatic Import Contacts tab. SFTP is the default
                                          			 option.

Step 5

Select the
                                          			 server type as SFTP or HTTPS . Enter the SFTP or the HTTPS remote server
                                          			 details to import contacts from a remote server using SFTP or HTTPS
                                          			 respectively.

If you select SFTP, enter the following details for the Remote SFTP Server:

IP Address /FQDN—The IP address or the Fully Qualified Domain Name of the remote SFTP server.

RSA Key—The RSA public key of the remote SFTP server. This is optional and is used for trust verification of the SFTP server
                                                   by the Unified CCX server.

User Name—The username that is required to log in to the remote SFTP server.

Password—The password that is required to log in to the remote SFTP server.

CSV File Path—The CSV file path (.csv or .txt file path) to import contacts from the remote SFTP server. This is the fully
                                                   qualified file name. For example:

If you select HTTPS, enter the following details for the Remote HTTPS Server:

URL—The URL to access the contacts over the remote HTTPS Server.

User Name—The username that is required to log in to the remote HTTPS server.

Password—The password that is required to log in to the remote HTTPS server.

HTTPS Certificate—The check box to confirm that:

You have uploaded the HTTPS Certificate in the Unified OS Administration web interface at, Security > Certificate Management .

This is required for trust verification of the HTTPS server by the Unified CCX server.

Restarted the Cisco Tomcat and Cisco Unified CCX Engine on both the node.

Step 6

Check the Allow Duplicate Contacts option, if required.

Allow Duplicate Contacts

A record is considered duplicate when the phone number in any of the three phone fields (Phone 1, Phone 2, and Phone 3) of
                                             the records being imported:

Exists in any of the three phone fields of the other contacts being imported.

Exists in any of the three phone fields of the contacts previously imported for the campaign that are dialed out since last
                                                   midnight or yet to be dialed out.

If this option is not selected:

The contacts identified as duplicates are not imported for the campaign.

If this option is selected:

The check for duplicate contacts is not performed and all contacts are imported as is.

By
                                                         				  default this option is not selected.

Step 7

Click Test
                                             				Connection to check the connectivity with the remote SFTP or HTTPS
                                          			 server.

Step 8

Set the order
                                          			 of field names and a schedule to automatically import contacts in regular
                                          			 intervals.

A contact list can contain up to 7 fields:

Account Number - The account number of a contact. The account number can be a maximum length of 25 characters.

First Name - The first name of a contact. The first name can be a maximum length of 50 characters.

Last Name - The last name of a contact. The last name can be a maximum length of 50 characters.

Phone1 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone1 is
                                                   mandatory and must be specified.

Phone2 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number.

Phone3 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number.

Dial Time - The time to dial a number for individual contacts on the current date. The format to be used for this field is
                                                   HH: MM. For example, to specify the dialing time as 08:25 am, the dial time field value should be 08:25 and for 03:45 pm,
                                                   the dial time field value should be 15:45. This field is applicable only for Direct Preview Outbound campaigns.

Step 9

Set the
                                          			 Schedule for the automatic import of contacts.

Select
                                                				  the date.

Set the Start Time .

Check
                                                				  the Repeat Every checkbox and set the reoccurrence of
                                                				  the automatic schedule.

The
                                                               						Outbound schedule time is based on the Unified CCX server time zone.

Avoid
                                                               						scheduling the import of contacts during peak hours.

Step 10

Select Enable or Disable option for automatic schedule of import of
                                          			 contacts.

Step 11

Click Save to save the configurations done for Automatic Import Contacts .

## Enable Campaigns

You must verify that the configured campaigns are active and
                              		  that the start and end times for the enabled campaigns are specified as
                              		  required.

To verify the state of the required campaign, complete the
                              		  following steps.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns .

The Campaigns web page opens, displaying following information for
                                          				the existing campaigns:

Field

Description

Name

Name of the campaign.

Start Time/End Time (hh:mm) AM PM

Start Time and End Time fields indicate the time range
                                                      							 during which the campaign runs.

Remaining Contacts

The Remaining Contacts field indicates the number of
                                                      							 contacts that are yet to be dialed for each campaign. In addition to the
                                                      							 contacts that have not been dialed, this number also includes contacts that
                                                      							 have requested a callback and contacts that will be tried again because of
                                                      							 unsuccessful prior attempt(s) (for example, the contact was busy or unavailable). A
                                                      							 detailed breakdown of the pending contacts is provided in the Printable Reports
                                                      							 page for each campaign.

Enabled

The Enabled field indicates to the Outbound subsystem
                                                      							 whether this campaign is currently active.

Campaign Type

Denotes whether a specific campaign is IVR-based or
                                                      							 Agent-based. The existing campaigns will be marked as Agent-based after an
                                                      							 upgrade.

Delete

Click Delete icon next to the name of
                                                      							 the campaign that you want to delete.

Step 2

Verify that the Enabled field is set to TRUE and that the start and end times are specified as
                                       			 required.

## Outbound Subsystem
                        	 and Time Detection

The
                              		  Outbound subsystem uses the area code of a contact's phone number to determine
                              		  the time zone of the contact's calling area. The contact's phone number can
                              		  also be in E.164 format.

The
                              		  subsystem provides the mapping for North American area codes to their
                              		  corresponding time zones. The default North American area codes are used to
                              		  determine the time zone for phone numbers that are not in the E.164 format (for
                              		  example, 234-567-8900). The Area Codes web page allows you to add, modify, and
                              		  delete any area-code-to-time-zone mapping. Some area codes extend across
                              		  multiple time zones. For such area codes, you can edit the default time zone
                              		  for that area code and specify a different one, if required.

Changes
                              		  to area codes take affect the next time you import contacts. For example, if
                              		  the time zone of area code 603 is changed from 16 to 17, contacts already
                              		  present in the system that have an area code of 603 continue to have the GMT
                              		  Offset of 16. Any contacts with area code 603 that are imported after the area
                              		  code change have 17 for the GMT Offset.

When
                              		  Outbound contacts are imported into the database, all contacts are assigned a
                              		  GMT time zone for the three phone numbers provided. The Outbound subsystem
                              		  determines this GMT time zone by extracting the area code of each phone number
                              		  and checking it against the Area Codes table to obtain the corresponding time
                              		  zone. If the area code cannot be matched, the Outbound subsystem uses the local
                              		  time zone and Daylight Savings Time (DST) setting of the server. The Outbound
                              		  subsystem also considers the DST to determine if an Outbound contact can be
                              		  called at a given time.

The
                              		  Outbound subsystem ensures that the contacts are dialed at valid times. For
                              		  Outbound contacts which have been scheduled for callback, the scheduled
                              		  callback time is converted to GMT time zone and stored in the callbackDateTime
                              		  field in the database.

For
                              		  pending records, the Outbound subsystem ensures that Outbound contacts are
                              		  called only within the Customer Dialing Time Range (hh:mm) detected by the
                              		  MinCustomerDialTime and MaxCustomerDialTime, as per federal regulations. You
                              		  can configure this time in the Unified CCX Administration GUI.

## Add Area
                        	 Codes

Caution

Area code and long
                                          			 distance prefix configuration changes made to the Outbound subsystem do not
                                          			 take effect for calls/contacts currently in the Outbound subsystem's memory.
                                          			 For example, if you change the long distance prefix or local area code, the
                                          			 contacts already in the Outbound subsystem's memory will continue to use the
                                          			 old long distance prefix and local area code.

The
                              		  Outbound subsystem provides all of the mappings from North American area codes
                              		  to their corresponding time zones at the time of product release. The Area
                              		  Codes page allows the administrator to add, modify, and delete any
                              		  area-code-to-time-zone mappings.

Some area
                              		  codes extend across multiple time zones. For such area codes, an administrator
                              		  can edit the default time zone for that area code and specify a different one,
                              		  if required.

The Area
                              		  Codes Management page allows users to find, add, delete, and modify the mapping
                              		  of area codes and time zones. The Outbound subsystem uses the area code of a
                              		  contact's phone number to determine the time zone of the contact's calling
                              		  area. This page can also be used for adding international area codes.
                              		  International area codes must include the country code and the city code.

To add an
                              		  area code, complete the following steps.

Step 1

From the Unified
                                       			 CCX Administration menu bar, choose Subsystems > Outbound > Area
                                             				  Codes .

The Area Codes
                                          				Management web page opens.

Step 2

In the Area Code
                                       			 field, specify a unique identifier for the area code. This field can have any
                                       			 numeric value, including 0 or leading zeros. This is a mandatory field.

Step 3

Click the Add
                                          				New icon that is displayed in the tool bar in the upper, left
                                       			 corner of the window or the Add
                                          				New button that is displayed at the bottom of the window.

The new Area
                                          				Code information is updated.

## Call Status Values

For each contact, the call statuses and their corresponding
                              		  values are recorded in the database and described in the following table:

Call Status

Value (stored in database)

Description

Pending

1

The call is pending. This is the initial state for all
                                          						records.

Active

2

The record was retrieved by the Outbound subsystem for
                                          						dialing.

Closed

3

The record is closed (not dialed).

Callback

4

The record is marked for a callback.

Max Calls

5

Maximum attempts have been reached for this record
                                          						(considered closed).

Retry

6

The record is redialed immediately whenever there is any
                                          						miss in the callbacks for Retries with Delay.

Unknown

7

If the Outbound subsystem was restarted with records in the
                                          						Active (2) state, they are moved to this state.

Retries with Delay

8

The record is redialed as it was either busy, no answer,
                                          						customer abandoned or system abandoned. Retry time is set as per the
                                          						corresponding configuration in Unified CCX Application Administration web
                                          						interface.

### Contact States
                           	 Reset at Midnight

The
                                 		  Outbound subsystem performs the following actions at midnight:

The DialingListConfig records with a call status of Unknown are reset to Pending.

Outbound contacts with a call status of Unknown indicate that the these contacts were retrieved from the database but the
                                                   system went down before they could be dialed out.

Missed
                                       				callback records (dialingListConfig records that have call status callback and
                                       				a callBackDateTime smaller than the current time) are updated depending on the
                                       				missed callback action configured in the Unified CCX Administration GUI.

MissedCallbackAction: Reschedule (for the same time on the next
                                             					 business day)

MissedCallbackAction: Retry (sets the call status to Retry and
                                             					 retries at the start of next business day)

MissedCallbackAction: Close (sets the call status to Closed)

Dialing
                                             					 list records with a call status of Closed or Max_Calls are moved to a separate
                                             					 historical data table

The
                                                         						records marked as closed today will be moved the next day at midnight. For
                                                         						example, the records closed on 4th June will be moved on 5th June at midnight.

The
                                       				DialingListConfig records with a call status of "Retries with
                                          				  delay" and which could not be retried due to lapsed time are marked for
                                       				immediate retry at midnight.

When the
                                       				Unified CCX engine goes from offline to online (for example, the standby server
                                       				becomes active [online] if the active [first] server fails), the dialing list
                                       				records with a status of Unknown are reset to Pending.

## Call Result
                        	 Values

For each contact, the
                              		  call results (as marked by the agent on Finesse or automatically deleted by the
                              		  system) and their corresponding values are recorded in the database and
                              		  described in the following table:

Call
                                          						Result

Value
                                          						(stored in database)

Description

Voice

1

Customer
                                          						answered and was connected to agent.

Fax

2

Fax
                                          						machine or modem detected.

Answering machine

3

Answering machine detected.

Invalid

4

Number
                                          						reported as invalid by the network.

Callback

8

Customer
                                          						requested callback.

Agent
                                          						Rejected

9

Agent rejected the preview call.

Agent
                                          						Closed

10

Agent rejected the preview call with the close option (not dialed).

Busy

11

Busy
                                          						tone detected.

Ring No
                                          						Answer

12

Agent
                                          						did not respond to the preview call within the time out duration.

You
                                                      						  can configure the time out duration using the Preview Call Timeout field
                                                      						  detailed in the Configure General Outbound Properties .

Callback Failed

13

This
                                          						value should not be written to the database; this is for internal use only.

Callback Missed

14

Callback missed and marked for Retry.

Timeout

15

Customer phone timed out either due to Ring No Answer (RNA) or
                                          						Gateway failure.

Call
                                          						Abandoned

16

Call
                                          						was abandoned because IVR port was unavailable or Unified CCX failed due to
                                          						transfer the call to the IVR port.

Call
                                          						Failed

17

Call
                                          						failed due any one of the following reasons:

Dialer asked the Gateway to cancel a call that has not yet been placed

Gateway has declined the call

Gateway is down or Gateway has timed out while placing the call

Gateway failure or configuration issues at the Gateway

Customer Abandoned

18

Customer abandoned as customer disconnected the call within the
                                          						time limit as configured in "Abandoned Call Wait Time" in Unified CCX Application
                                          						Administration web interface.

## Reclassification Status Behavior

When the Outbound contacts are imported into the database from the Unified CCX Administration GUI, the Call Status column
                              in the Dialing List table is assigned the default value of 1 (Pending), indicating that these Outbound contacts are yet to
                              be dialed. When the Outbound subsystem retrieves a batch of contacts from the database, the Call Status is set to 2 (Active). After a call is placed to the Outbound contact, the Call Status is set to 3 (Closed) and the Call Result is set to 1 (Voice), as all Outbound calls are classified by the agent desktop as Voice by default. If the agent clicks the
                              reclassification button on the agent desktop and reclassifies the call as Answering Machine/Fax/Busy/Invalid or selects the
                              Callback button and schedules a call back, the Outbound subsystem updates the Call Result field accordingly and, based on the call result, it also updates the Call Status .

The following table describes the relationship between Call Status and Call Result values and the resulting behavior of the system. The values in brackets are the actual values stored in the database.

The following information is applicable only for Preview Dialer.

Call Result

Call Status

Behavior

Voice (1)

Closed (3)

This contact is not dialed again.

Fax (2)

Retry (6)

This contact is retried, using a different phone number provided for this contact. If alternate phone numbers are not available,
                                          the call status is closed.

Answering machine (3)

Retry (6)

This contact is retried, with the same phone number as before.

Invalid Number (4)

Retry (6)

This contact is retried, using a different phone number provided for this contact. If alternate phone numbers are not available,
                                          the call status is closed.

Busy

Retry (6)

This contact is retried, with the same phone number as before.

The Call Status is set to 3 (Closed) when the Outbound contact is no longer dialed for this campaign. This also happens automatically if
                              the system reaches the maximum attempts limit for an Outbound contact, which means that the system tried dialing the Outbound
                              contact the maximum number of times configured in the Unified CCX Administration GUI.

## Call Retrieval
                        	 Priority

While
                              		  retrieving Outbound contacts from the database, records that have scheduled
                              		  callbacks have priority as the callback time must be adhered to. Outbound
                              		  contacts are retrieved in the following order of priority:

Priority 1—Outbound contacts with a scheduled callback (call status = 4) and the current time is within the CallbackTimeLimit
                                    configured on the Campaigns page (default value is15 minutes) of the scheduled callback time.

Priority
                                    				2—Outbound contacts to be retried after a specific delay. This is not
                                    				applicable for direct preview campaigns (call status = 8).

Priority
                                    				3—Outbound contacts in the Pending state (call status = 1).

Priority 4—Outbound contacts in the Retry state (call status = 6).

The Call Retrieval Priority is on a per campaign basis. If an agent is part of multiple CSQs that are part of different campaigns,
                                          priority of callbacks may be overridden by different queues. For example, Priority 4 in a particular queue may take precedence
                                          over Priority 1 of another queue.

## Failover and System Restarts

Outbound contacts with an Active call status during a
                              		  failover indicate that these contacts were retrieved from the database but the
                              		  system went down either before they could be dialed or after they were dialed
                              		  but before the call status and call result columns were updated. When the
                              		  system restarts, the call status for all such Outbound contacts is changed to 7
                              		  (Unknown). All Outbound contacts in the Unknown state will be reset to the
                              		  Pending state (should be retrieved for dialing again) at midnight every night.

If there is an Outbound call in progress during a failover,
                              		  they cannot be dialed again, as the call status is set to Closed as soon as an
                              		  Outbound call is placed and these records will not be retrieved for dialing
                              		  again when the system comes back. However, if the failover happened before the
                              		  system could update the call status to Closed, these records remain in the
                              		  Active state and are marked Unknown so they transition to Pending state after
                              		  midnight. Once they are in the Pending state, they will be dialed again.

| Note | Calls made by the Outbound subsystem will not be displayed in the Contacts Summary Real-Time Report |
|---|---|

| Note | The sum of inbound
                                             			 and outbound IVR ports should be less than or equal to a maximum number of IVR
                                             			 ports supported for your hardware model. |
|---|---|

| Note | The total number of dedicated IVR ports in all the IVR campaigns
                                             			 must be less than twice the number of Premium Seats that is equivalent to the
                                             			 Total Licensed Inbound IVR ports. |
|---|---|

| Tip | For agent predictive and agent progressive outbound calls, disable the Call Waiting option on the agent's phone to allow agents
                                             to preview a customer call on Finesse Desktop before the call is placed. The Call Waiting option must be disabled (default)
                                             in Unified Communications Manager on each Outbound agent phone to ensure that every customer call successfully transfers to an available agent. |
|---|---|

| Step 1 | Configure the
                                       			 general properties of the outbound subsystem. See Configure General Outbound Properties . |
|---|---|
| Step 2 | (Optional) If
                                       			 the dialing list contains contacts outside of North America or if Unified CCX
                                       			 is installed outside of North America, manually add the area codes and their
                                       			 corresponding time zones. See Add New Area Code . |
| Step 3 | Configure the
                                       			 SIP Gateway parameters to enable communication between Unified CCX and the SIP
                                       			 gateway for IVR and agent-based progressive and predictive campaigns. See Configure SIP Gateway . |
| Step 4 | Configure the
                                       			 campaign. See Add New Campaign . |

| Caution | Area code and long
                                          			 distance prefix configuration changes made to the Outbound subsystem do not
                                          			 take effect for the calls/contacts that are currently in the Outbound
                                          			 subsystem’s memory. For example, if you change the long distance prefix or
                                          			 local area code, the contacts that are already in the Outbound subsystem's
                                          			 memory will continue to use the old long distance prefix and local area code. |
|---|---|

| Step 1 | From the Unified
                                       			 CCX Administration menu bar, choose Subsystems > Outbound > General . The General
                                          				Configuration web page opens. |
|---|---|
| Step 2 | Specify the
                                       			 following fields in the General Configuration section: Field Description Customer Dialing Time Range (hh:mm) Start Time/End Time The
                                                      							 time range during which a customer can be called. This time range supersedes
                                                      							 the time range of the individual campaigns and ensures that a customer is never
                                                      							 called outside the legally allowed time range for that country. This is a
                                                      							 mandatory field. For
                                                      							 example, in the USA, the Federal Communications Commission (FCC) specifies the
                                                      							 legal time range as 8 AM to 9 PM. This does not apply to callbacks, since the
                                                      							 customer explicitly requested to be called at a certain time. This time range
                                                      							 is always converted to the local time for each contact record. Default = 8:00 AM to 9:00 PM (USA FCC regulations) Outbound Call Timeout (seconds) If an agent does not respond to the
                                                      											Outbound preview call on Finesse Desktop within the
                                                      											timeout duration that is specified in this field, the
                                                      											system sets the agent to the Not Ready state. If an agent does not respond to the Outbound progressive or predictive call on Finesse
                                                      											Desktop within the timeout duration that is specified in
                                                      											this field, then the call is dropped. The system sets
                                                      											the agent to the Ready or Not Ready state depending on
                                                      											the option that is selected for Agent State after Ring
                                                      											No Answer field in the System Parameters Configuration
                                                      											Web Page. This is a mandatory field. Default = 60 seconds, Range = 5 to 3600 seconds. Note If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. Dialing Prefix The
                                                      							 number that is prefixed to the phone number when the dialer dials an outgoing
                                                      							 call (also referred to as switch prefix). This number can have a numeric value,
                                                      							 including 0 or leading zeros. This is a user defined value. For
                                                      							 example, if the dialing prefix is set as 9 and the phone number of the contact
                                                      							 is 54321, then the dialer will dial out '954321'. Long
                                                      							 Distance Prefix This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the long distance prefix in the phone number that is dialed by the
                                                      							 dialer. It is first determined whether it is an international or domestic
                                                      							 number by the presence of any matching International Prefix set in the General configurations page. When
                                                      							 the phone number is a domestic number, based on the matching local area code
                                                      							 set, it is determined if it is a local number or a long distance number. For
                                                      							 example, if the long distance prefix is set as 044, the phone number of the
                                                      							 contact is 54321, and if the Include Long Distance Prefix is enabled, then the dialer dials out '4454321'. International Prefix This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the international prefix in the phone number for that international
                                                      							 number. If there is no International Prefix, then the number is considered to
                                                      							 be a domestic number. If
                                                      							 the imported number doesn't contain an international prefix but has a "+" sign
                                                      							 prefixed to the phone number, then it is considered to be an international
                                                      							 number. Local Area Code The
                                                      							 area code of the location from where the PSTN call is made from. This number
                                                      							 can have a numeric value, including 0 or leading zeros. The local area code
                                                      							 when set in the General configurations page, helps to determine the
                                                      							 prefix value in the domestic phone number which is included in the outgoing
                                                      							 call if the Do Not Remove Local Area Code When Dialing is
                                                      							 checked. Do
                                                      							 Not Remove Local Area Code When Dialing If
                                                      							 this box is checked, the local area code is included when dialing the phone
                                                      							 numbers within this area code. If it is unchecked, then the local area code is
                                                      							 stripped from the phone number before dialing the local numbers. It is expected
                                                      							 that when contacts are imported into the system, the phone numbers include the
                                                      							 area code. For international phone numbers, the country code must be included
                                                      							 when importing contacts. Include Long Distance Prefix This
                                                      							 field will be displayed only if you check the Do Not Remove Local Area Code When Dialing check
                                                      							 box. For local numbers, the long distance prefix will be prefixed only if this
                                                      							 check box is checked. The
                                                      							 long distance prefix will be prefixed to the phone number for all non-local
                                                      							 numbers (the numbers that do not start with local area code) irrespective of
                                                      							 the status (checked/unchecked) of this check box. Auto Answer If this box is checked, any agent-based progressive or predictive campaign call that
                                                      											gets transferred to the agent is automatically answered
                                                      											by Unified CCX. A beep tone always notifies the agent
                                                      											that the call has been answered. This option is enabled
                                                      											by default. Note If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. Assigned CSQs Assigned CSQs are CSQs that are used by the Outbound subsystem.
                                                      							 This is a mandatory field. To allocate CSQs for Outbound: Select a CSQ in the Available CSQs list. Select a value from the % of Logged in Agents for Outbound drop-down list to indicate what percentage of the CSQ is allocated for Outbound. Click the left arrow icon to move the CSQ to the Assigned CSQs list. The
                                                      							 selected CSQ is removed from the Available CSQs box and appears in the Assigned CSQs box with the percentage allocation in
                                                      							 parentheses next to the CSQ name. Available CSQs The
                                                      							 Available CSQs pane displays all CSQs configured in the CSQ Configuration page
                                                      							 under the RmCm subsystem configuration. % of
                                                      							 Logged in Agents for Outbound The
                                                      							 % of Logged in Agents for Outbound field indicates the percentage of logged in
                                                      							 agents in each of the selected CSQs that are allocated for handling Outbound
                                                      							 calls. Note The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. The number of agents allocated for OB is considered as
                                                      							 the whole number of the % of Logged in Agents for Outbound . Any decimal
                                                      							 value in the value is not considered. For example, If the percentage of
                                                      							 allocation is 95% and 4 agents are logged in, then the number of agents
                                                      							 allocated for OB are 3 [95% * 4 = 3.8 (decimal value is neglected)]. If the
                                                      							 percentage of allocation is 80% and 4 agents were logged in, then the number of
                                                      							 agents allocated for OB are 3 [(80% * 4 = 3.2 (decimal value is neglected)]. | Field | Description | Customer Dialing Time Range (hh:mm) Start Time/End Time | The
                                                      							 time range during which a customer can be called. This time range supersedes
                                                      							 the time range of the individual campaigns and ensures that a customer is never
                                                      							 called outside the legally allowed time range for that country. This is a
                                                      							 mandatory field. For
                                                      							 example, in the USA, the Federal Communications Commission (FCC) specifies the
                                                      							 legal time range as 8 AM to 9 PM. This does not apply to callbacks, since the
                                                      							 customer explicitly requested to be called at a certain time. This time range
                                                      							 is always converted to the local time for each contact record. Default = 8:00 AM to 9:00 PM (USA FCC regulations) | Outbound Call Timeout (seconds) | If an agent does not respond to the
                                                      											Outbound preview call on Finesse Desktop within the
                                                      											timeout duration that is specified in this field, the
                                                      											system sets the agent to the Not Ready state. If an agent does not respond to the Outbound progressive or predictive call on Finesse
                                                      											Desktop within the timeout duration that is specified in
                                                      											this field, then the call is dropped. The system sets
                                                      											the agent to the Ready or Not Ready state depending on
                                                      											the option that is selected for Agent State after Ring
                                                      											No Answer field in the System Parameters Configuration
                                                      											Web Page. This is a mandatory field. Default = 60 seconds, Range = 5 to 3600 seconds. Note If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. | Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. | Dialing Prefix | The
                                                      							 number that is prefixed to the phone number when the dialer dials an outgoing
                                                      							 call (also referred to as switch prefix). This number can have a numeric value,
                                                      							 including 0 or leading zeros. This is a user defined value. For
                                                      							 example, if the dialing prefix is set as 9 and the phone number of the contact
                                                      							 is 54321, then the dialer will dial out '954321'. | Long
                                                      							 Distance Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the long distance prefix in the phone number that is dialed by the
                                                      							 dialer. It is first determined whether it is an international or domestic
                                                      							 number by the presence of any matching International Prefix set in the General configurations page. When
                                                      							 the phone number is a domestic number, based on the matching local area code
                                                      							 set, it is determined if it is a local number or a long distance number. For
                                                      							 example, if the long distance prefix is set as 044, the phone number of the
                                                      							 contact is 54321, and if the Include Long Distance Prefix is enabled, then the dialer dials out '4454321'. | International Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the international prefix in the phone number for that international
                                                      							 number. If there is no International Prefix, then the number is considered to
                                                      							 be a domestic number. If
                                                      							 the imported number doesn't contain an international prefix but has a "+" sign
                                                      							 prefixed to the phone number, then it is considered to be an international
                                                      							 number. | Local Area Code | The
                                                      							 area code of the location from where the PSTN call is made from. This number
                                                      							 can have a numeric value, including 0 or leading zeros. The local area code
                                                      							 when set in the General configurations page, helps to determine the
                                                      							 prefix value in the domestic phone number which is included in the outgoing
                                                      							 call if the Do Not Remove Local Area Code When Dialing is
                                                      							 checked. | Do
                                                      							 Not Remove Local Area Code When Dialing | If
                                                      							 this box is checked, the local area code is included when dialing the phone
                                                      							 numbers within this area code. If it is unchecked, then the local area code is
                                                      							 stripped from the phone number before dialing the local numbers. It is expected
                                                      							 that when contacts are imported into the system, the phone numbers include the
                                                      							 area code. For international phone numbers, the country code must be included
                                                      							 when importing contacts. | Include Long Distance Prefix | This
                                                      							 field will be displayed only if you check the Do Not Remove Local Area Code When Dialing check
                                                      							 box. For local numbers, the long distance prefix will be prefixed only if this
                                                      							 check box is checked. The
                                                      							 long distance prefix will be prefixed to the phone number for all non-local
                                                      							 numbers (the numbers that do not start with local area code) irrespective of
                                                      							 the status (checked/unchecked) of this check box. | Auto Answer | If this box is checked, any agent-based progressive or predictive campaign call that
                                                      											gets transferred to the agent is automatically answered
                                                      											by Unified CCX. A beep tone always notifies the agent
                                                      											that the call has been answered. This option is enabled
                                                      											by default. Note If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. | Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. | Assigned CSQs | Assigned CSQs are CSQs that are used by the Outbound subsystem.
                                                      							 This is a mandatory field. To allocate CSQs for Outbound: Select a CSQ in the Available CSQs list. Select a value from the % of Logged in Agents for Outbound drop-down list to indicate what percentage of the CSQ is allocated for Outbound. Click the left arrow icon to move the CSQ to the Assigned CSQs list. The
                                                      							 selected CSQ is removed from the Available CSQs box and appears in the Assigned CSQs box with the percentage allocation in
                                                      							 parentheses next to the CSQ name. | Available CSQs | The
                                                      							 Available CSQs pane displays all CSQs configured in the CSQ Configuration page
                                                      							 under the RmCm subsystem configuration. | % of
                                                      							 Logged in Agents for Outbound | The
                                                      							 % of Logged in Agents for Outbound field indicates the percentage of logged in
                                                      							 agents in each of the selected CSQs that are allocated for handling Outbound
                                                      							 calls. Note The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. The number of agents allocated for OB is considered as
                                                      							 the whole number of the % of Logged in Agents for Outbound . Any decimal
                                                      							 value in the value is not considered. For example, If the percentage of
                                                      							 allocation is 95% and 4 agents are logged in, then the number of agents
                                                      							 allocated for OB are 3 [95% * 4 = 3.8 (decimal value is neglected)]. If the
                                                      							 percentage of allocation is 80% and 4 agents were logged in, then the number of
                                                      							 agents allocated for OB are 3 [(80% * 4 = 3.2 (decimal value is neglected)]. | Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |
| Field | Description |
| Customer Dialing Time Range (hh:mm) Start Time/End Time | The
                                                      							 time range during which a customer can be called. This time range supersedes
                                                      							 the time range of the individual campaigns and ensures that a customer is never
                                                      							 called outside the legally allowed time range for that country. This is a
                                                      							 mandatory field. For
                                                      							 example, in the USA, the Federal Communications Commission (FCC) specifies the
                                                      							 legal time range as 8 AM to 9 PM. This does not apply to callbacks, since the
                                                      							 customer explicitly requested to be called at a certain time. This time range
                                                      							 is always converted to the local time for each contact record. Default = 8:00 AM to 9:00 PM (USA FCC regulations) |
| Outbound Call Timeout (seconds) | If an agent does not respond to the
                                                      											Outbound preview call on Finesse Desktop within the
                                                      											timeout duration that is specified in this field, the
                                                      											system sets the agent to the Not Ready state. If an agent does not respond to the Outbound progressive or predictive call on Finesse
                                                      											Desktop within the timeout duration that is specified in
                                                      											this field, then the call is dropped. The system sets
                                                      											the agent to the Ready or Not Ready state depending on
                                                      											the option that is selected for Agent State after Ring
                                                      											No Answer field in the System Parameters Configuration
                                                      											Web Page. This is a mandatory field. Default = 60 seconds, Range = 5 to 3600 seconds. Note If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. | Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. |
| Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. |
| Dialing Prefix | The
                                                      							 number that is prefixed to the phone number when the dialer dials an outgoing
                                                      							 call (also referred to as switch prefix). This number can have a numeric value,
                                                      							 including 0 or leading zeros. This is a user defined value. For
                                                      							 example, if the dialing prefix is set as 9 and the phone number of the contact
                                                      							 is 54321, then the dialer will dial out '954321'. |
| Long
                                                      							 Distance Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the long distance prefix in the phone number that is dialed by the
                                                      							 dialer. It is first determined whether it is an international or domestic
                                                      							 number by the presence of any matching International Prefix set in the General configurations page. When
                                                      							 the phone number is a domestic number, based on the matching local area code
                                                      							 set, it is determined if it is a local number or a long distance number. For
                                                      							 example, if the long distance prefix is set as 044, the phone number of the
                                                      							 contact is 54321, and if the Include Long Distance Prefix is enabled, then the dialer dials out '4454321'. |
| International Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the international prefix in the phone number for that international
                                                      							 number. If there is no International Prefix, then the number is considered to
                                                      							 be a domestic number. If
                                                      							 the imported number doesn't contain an international prefix but has a "+" sign
                                                      							 prefixed to the phone number, then it is considered to be an international
                                                      							 number. |
| Local Area Code | The
                                                      							 area code of the location from where the PSTN call is made from. This number
                                                      							 can have a numeric value, including 0 or leading zeros. The local area code
                                                      							 when set in the General configurations page, helps to determine the
                                                      							 prefix value in the domestic phone number which is included in the outgoing
                                                      							 call if the Do Not Remove Local Area Code When Dialing is
                                                      							 checked. |
| Do
                                                      							 Not Remove Local Area Code When Dialing | If
                                                      							 this box is checked, the local area code is included when dialing the phone
                                                      							 numbers within this area code. If it is unchecked, then the local area code is
                                                      							 stripped from the phone number before dialing the local numbers. It is expected
                                                      							 that when contacts are imported into the system, the phone numbers include the
                                                      							 area code. For international phone numbers, the country code must be included
                                                      							 when importing contacts. |
| Include Long Distance Prefix | This
                                                      							 field will be displayed only if you check the Do Not Remove Local Area Code When Dialing check
                                                      							 box. For local numbers, the long distance prefix will be prefixed only if this
                                                      							 check box is checked. The
                                                      							 long distance prefix will be prefixed to the phone number for all non-local
                                                      							 numbers (the numbers that do not start with local area code) irrespective of
                                                      							 the status (checked/unchecked) of this check box. |
| Auto Answer | If this box is checked, any agent-based progressive or predictive campaign call that
                                                      											gets transferred to the agent is automatically answered
                                                      											by Unified CCX. A beep tone always notifies the agent
                                                      											that the call has been answered. This option is enabled
                                                      											by default. Note If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. | Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. |
| Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. |
| Assigned CSQs | Assigned CSQs are CSQs that are used by the Outbound subsystem.
                                                      							 This is a mandatory field. To allocate CSQs for Outbound: Select a CSQ in the Available CSQs list. Select a value from the % of Logged in Agents for Outbound drop-down list to indicate what percentage of the CSQ is allocated for Outbound. Click the left arrow icon to move the CSQ to the Assigned CSQs list. The
                                                      							 selected CSQ is removed from the Available CSQs box and appears in the Assigned CSQs box with the percentage allocation in
                                                      							 parentheses next to the CSQ name. |
| Available CSQs | The
                                                      							 Available CSQs pane displays all CSQs configured in the CSQ Configuration page
                                                      							 under the RmCm subsystem configuration. |
| % of
                                                      							 Logged in Agents for Outbound | The
                                                      							 % of Logged in Agents for Outbound field indicates the percentage of logged in
                                                      							 agents in each of the selected CSQs that are allocated for handling Outbound
                                                      							 calls. Note The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. The number of agents allocated for OB is considered as
                                                      							 the whole number of the % of Logged in Agents for Outbound . Any decimal
                                                      							 value in the value is not considered. For example, If the percentage of
                                                      							 allocation is 95% and 4 agents are logged in, then the number of agents
                                                      							 allocated for OB are 3 [95% * 4 = 3.8 (decimal value is neglected)]. If the
                                                      							 percentage of allocation is 80% and 4 agents were logged in, then the number of
                                                      							 agents allocated for OB are 3 [(80% * 4 = 3.2 (decimal value is neglected)]. | Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |
| Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |
| Step 3 | Click Update icon that is displayed in the tool bar in the
                                       			 upper, left corner of the window or the Update button that is displayed at the bottom of the
                                       			 window. The System
                                          				Options components are now updated. |

| Field | Description |
|---|---|
| Customer Dialing Time Range (hh:mm) Start Time/End Time | The
                                                      							 time range during which a customer can be called. This time range supersedes
                                                      							 the time range of the individual campaigns and ensures that a customer is never
                                                      							 called outside the legally allowed time range for that country. This is a
                                                      							 mandatory field. For
                                                      							 example, in the USA, the Federal Communications Commission (FCC) specifies the
                                                      							 legal time range as 8 AM to 9 PM. This does not apply to callbacks, since the
                                                      							 customer explicitly requested to be called at a certain time. This time range
                                                      							 is always converted to the local time for each contact record. Default = 8:00 AM to 9:00 PM (USA FCC regulations) |
| Outbound Call Timeout (seconds) | If an agent does not respond to the
                                                      											Outbound preview call on Finesse Desktop within the
                                                      											timeout duration that is specified in this field, the
                                                      											system sets the agent to the Not Ready state. If an agent does not respond to the Outbound progressive or predictive call on Finesse
                                                      											Desktop within the timeout duration that is specified in
                                                      											this field, then the call is dropped. The system sets
                                                      											the agent to the Ready or Not Ready state depending on
                                                      											the option that is selected for Agent State after Ring
                                                      											No Answer field in the System Parameters Configuration
                                                      											Web Page. This is a mandatory field. Default = 60 seconds, Range = 5 to 3600 seconds. Note If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. | Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. |
| Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. |
| Dialing Prefix | The
                                                      							 number that is prefixed to the phone number when the dialer dials an outgoing
                                                      							 call (also referred to as switch prefix). This number can have a numeric value,
                                                      							 including 0 or leading zeros. This is a user defined value. For
                                                      							 example, if the dialing prefix is set as 9 and the phone number of the contact
                                                      							 is 54321, then the dialer will dial out '954321'. |
| Long
                                                      							 Distance Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the long distance prefix in the phone number that is dialed by the
                                                      							 dialer. It is first determined whether it is an international or domestic
                                                      							 number by the presence of any matching International Prefix set in the General configurations page. When
                                                      							 the phone number is a domestic number, based on the matching local area code
                                                      							 set, it is determined if it is a local number or a long distance number. For
                                                      							 example, if the long distance prefix is set as 044, the phone number of the
                                                      							 contact is 54321, and if the Include Long Distance Prefix is enabled, then the dialer dials out '4454321'. |
| International Prefix | This
                                                      							 is a user defined value that can have a numeric value, including 0 or leading
                                                      							 zeros. When this value is set and an outgoing call is made, it helps to
                                                      							 determine the international prefix in the phone number for that international
                                                      							 number. If there is no International Prefix, then the number is considered to
                                                      							 be a domestic number. If
                                                      							 the imported number doesn't contain an international prefix but has a "+" sign
                                                      							 prefixed to the phone number, then it is considered to be an international
                                                      							 number. |
| Local Area Code | The
                                                      							 area code of the location from where the PSTN call is made from. This number
                                                      							 can have a numeric value, including 0 or leading zeros. The local area code
                                                      							 when set in the General configurations page, helps to determine the
                                                      							 prefix value in the domestic phone number which is included in the outgoing
                                                      							 call if the Do Not Remove Local Area Code When Dialing is
                                                      							 checked. |
| Do
                                                      							 Not Remove Local Area Code When Dialing | If
                                                      							 this box is checked, the local area code is included when dialing the phone
                                                      							 numbers within this area code. If it is unchecked, then the local area code is
                                                      							 stripped from the phone number before dialing the local numbers. It is expected
                                                      							 that when contacts are imported into the system, the phone numbers include the
                                                      							 area code. For international phone numbers, the country code must be included
                                                      							 when importing contacts. |
| Include Long Distance Prefix | This
                                                      							 field will be displayed only if you check the Do Not Remove Local Area Code When Dialing check
                                                      							 box. For local numbers, the long distance prefix will be prefixed only if this
                                                      							 check box is checked. The
                                                      							 long distance prefix will be prefixed to the phone number for all non-local
                                                      							 numbers (the numbers that do not start with local area code) irrespective of
                                                      							 the status (checked/unchecked) of this check box. |
| Auto Answer | If this box is checked, any agent-based progressive or predictive campaign call that
                                                      											gets transferred to the agent is automatically answered
                                                      											by Unified CCX. A beep tone always notifies the agent
                                                      											that the call has been answered. This option is enabled
                                                      											by default. Note If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. | Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. |
| Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. |
| Assigned CSQs | Assigned CSQs are CSQs that are used by the Outbound subsystem.
                                                      							 This is a mandatory field. To allocate CSQs for Outbound: Select a CSQ in the Available CSQs list. Select a value from the % of Logged in Agents for Outbound drop-down list to indicate what percentage of the CSQ is allocated for Outbound. Click the left arrow icon to move the CSQ to the Assigned CSQs list. The
                                                      							 selected CSQ is removed from the Available CSQs box and appears in the Assigned CSQs box with the percentage allocation in
                                                      							 parentheses next to the CSQ name. |
| Available CSQs | The
                                                      							 Available CSQs pane displays all CSQs configured in the CSQ Configuration page
                                                      							 under the RmCm subsystem configuration. |
| % of
                                                      							 Logged in Agents for Outbound | The
                                                      							 % of Logged in Agents for Outbound field indicates the percentage of logged in
                                                      							 agents in each of the selected CSQs that are allocated for handling Outbound
                                                      							 calls. Note The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. The number of agents allocated for OB is considered as
                                                      							 the whole number of the % of Logged in Agents for Outbound . Any decimal
                                                      							 value in the value is not considered. For example, If the percentage of
                                                      							 allocation is 95% and 4 agents are logged in, then the number of agents
                                                      							 allocated for OB are 3 [95% * 4 = 3.8 (decimal value is neglected)]. If the
                                                      							 percentage of allocation is 80% and 4 agents were logged in, then the number of
                                                      							 agents allocated for OB are 3 [(80% * 4 = 3.2 (decimal value is neglected)]. | Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |
| Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |

| Note | If the Unified CCX Engine or Finesse Desktop restarts when an outbound campaign call
                                                                        												is being presented to an agent, then the timeout
                                                                        												value specified in the Outbound Call Timeout field
                                                                        												will not be applicable for that call. |
|---|---|

| Note | If the workflow is enabled, it will be run irrespective of the status (Checked/unchecked) of the Auto Answer check box. |
|---|---|

| Note | The CSQ allocation percentage is defined at the global level and
                                                                  								not at a campaign level. |
|---|---|

| Note | The selected status for the Missed Callbacks is applied at midnight. |
|---|---|

| Caution | If a callback is presented and the callback number is invalid (or busy), the callback continues to be retried irrespective
                                             of the number of retries set (for normal busy/invalid). It will be retried until the callback time limit expires. |
|---|---|

| Tip | The CSQs for Outbound are the same as the CSQs for inbound. If you
                                             			 need more CSQs, you must first configure them in Unified CCX and assign the
                                             			 required CSQs for agents as required by your configuration, before allocating
                                             			 them. |
|---|---|

| Step 1 | Create a Call
                                       			 Control Group for Outbound type with the required number of IVR ports to be
                                       			 used for outbound campaigns. See Add New Call Control Group . |
|---|---|
| Step 2 | Create an
                                       			 application, which will be used for the outbound campaign. See Cisco Applications Configuration . |
| Step 3 | Create a
                                       			 trigger and assign the newly created Outbound Call Control group to this
                                       			 trigger. See Cisco Applications Configuration . |
| Step 4 | Create a new
                                       			 progressive or predictive outbound campaign. See Add New Campaign . |
| Step 5 | Import
                                       			 contacts for the campaign. See Import Contacts for Campaign . |

| Step 1 | From the
                                       			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns . The Campaign
                                          				web page opens, displaying the details of existing campaigns, if any. Click an
                                          				existing campaign to view or update the configuration settings for the
                                          				campaign. |
|---|---|
| Step 2 | Click
                                       			 the Add
                                          				New icon in the tool bar in the upper, left corner of the window or
                                       			 the Add
                                          				New button at the bottom of the window. Add a New
                                          				Campaign web page opens up where you can specify the campaign type and the
                                          				dialer type for the campaign using the following fields. Note You need to
                                                      				  upload an Outbound license on top of the Premium license for Unified CCX to
                                                      				  create a campaign for Outbound. Field Description Select the type of the
                                                         								campaign Campaign Type Type
                                                      							 of the campaign to be used for outbound calls. You can specify any one of the
                                                      							 following two campaign types: Agent-based—If you select this, all the outbound calls in a campaign will be handled by the available agents. IVR-based—If you select the IVR-based option, the outbound calls in a campaign will be handled by the IVR scripts. Select the type of dialer
                                                         								for the campaign Description The dialer type options available for a campaign will vary depending on the selected Campaign Type. If you select Agent-based campaign type, then you can select any one of the following dialer types: Direct Preview (default) Progressive Predictive If you select IVR-based campaign type, then you can select any one of the following dialer types: Progressive (default) Predictive Note Once the campaign is created, you cannot change the Campaign Type and Dialer Type. After you select the campaign type and dialer type, click Next to continue. The Campaign Configuration web page opens, displaying the following three column headings: Parameter
                                                					 Name Parameter
                                                					 Value Suggested
                                                					 Value You can
                                          				specify values for a new campaign or modify values for an campaign using the
                                          				fields listed in the Parameter Value column. See the table below for a list of
                                          				fields along with their description. The Suggested Value displays the default configuration value for each campaign. You can refer to these values if you want
                                          to revert any changes made to one or more parameters listed in the Campaign Configuration web page. Field Description Campaign Name Name
                                                      							 of the campaign (must be a unique identifier). This is a mandatory field. Enabled Indicates the current state of the campaign to the Outbound
                                                      							 subsystem. Yes
                                                      							 = The campaign is currently active. No =
                                                      							 The campaign is currently inactive (default). Description Description of the campaign. Start Time/End Time (hh:mm) AM PM Time Zone Indicate the time range during which the campaign runs. These
                                                      							 are mandatory fields. The name of the primary time zone is also displayed
                                                      							 adjacent to these two field values. Default = 8:00 AM - 9:00 PM Pacific Standard Time (USA FCC
                                                      							 regulations). Campaign Calling Number The campaign calling number is the number that will be displayed to the contact. This number is used by the dialer. This is
                                                      a mandatory field. Note This field is not available if you have selected the direct preview dialer type for an agent based campaign. Maximum Attempts to Dial Contact The maximum number of times the Outbound subsystem attempts to
                                                      							 dial a contact beyond which the call status will be marked as closed. You can
                                                      							 choose this value from the drop-down list box. Default = 3, Range = 1 to 3. Callback Time Limit The time period before and after the scheduled callback time
                                                      							 during which the Outbound subsystem attempts to dial out a callback. For
                                                      							 example, if a callback was scheduled for 9:30 am and if the Callback Time Limit
                                                      							 is set to 15 minutes, then the Outbound subsystem calls the customer anytime
                                                      							 between 9:15 am to 9:45 am. This field is also used to determine the dialing time range for
                                                      							 the Retries settings in the Add New Campaign web page. Default = 15 minutes, Range = 1 to 60 minutes. Fields displayed only if
                                                         								you have selected IVR-based campaign type Application Trigger This is the JTAPI trigger associated with this campaign. There
                                                      							 will one-to-one mapping between a campaign and an application trigger. Only
                                                      							 those triggers that are not associated with any other campaigns are displayed
                                                      							 in the trigger list. Application Name The name of the application associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Fields displayed only if
                                                         								you have selected Agent-based campaign type Abandoned Call Treatment If the agent is not available to handle the call, you can choose to abandon the
                                                      							 call or transfer it to IVR by selecting the desired radio button in this field.
                                                      							 If you choose to transfer the call to IVR, a trigger field and an application
                                                      							 name field appears for selection. The trigger field is a drop-down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. Note This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. Assigned CSQs The CSQs from which agents are selected for Outbound calls for
                                                      							 this campaign. This is a mandatory field. Note For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. Available CSQs For direct preview campaigns—CSQs that are allocated for
                                                      							 outbound but not assigned to any progressive or predictive agent-based
                                                      							 campaign. For progressive and predictive agent-based campaigns—CSQs that
                                                      							 are allocated for outbound and not assigned to any other campaign. Fields displayed only if
                                                         								you have selected Direct Preview dialer type for an Agent-based campaign Contact Records Cache Size The number of contact records the Outbound subsystem retrieves
                                                      							 from the database in bulk for dialing. The allowed values are 1–100. This is a
                                                      							 mandatory field. For example, if 50 records are retrieved in bulk for campaign1
                                                      							 and 10 for campaign2 and they are running at the same time, the Outbound
                                                      							 subsystem attempts to place 50 Outbound calls for campaign1 and 10 Outbound
                                                      							 calls for campaign2. The number of Outbound calls actually placed for each
                                                      							 campaign depends upon the number of agents available for the respective
                                                      							 campaigns. Once all the records retrieved for a campaign have been dialed,
                                                      							 the Outbound subsystem retrieves another batch of records for that campaign.
                                                      							 Over a period of time, it is likely that more contacts would have been called
                                                      							 from campaign1 than from campaign2. If
                                                      							 two campaigns run simultaneously and share CSQs or agents, the records in both
                                                      							 campaigns may not be processed at the same rate even if their contact cache
                                                      							 sizes are identical. It is possible that more records from one of these two
                                                      							 campaigns is processed before the other. Default = 20, Range = 1 to 100 Answering Machine Retry If
                                                      							 you select Yes, then the Outbound subsystem retries the contact after all the
                                                      							 callbacks and pending contacts for the campaign are dialed out. Default = No The following fields in
                                                         								Dialing Options are displayed if you have selected IVR-based campaign type Number of Dedicated Ports Number of dedicated IVR ports that you want to reserve for this
                                                      							 campaign based on the number of CTI ports available in the outbound call
                                                      							 control group for the campaign duration. That is, the total number of dedicated
                                                      							 IVR ports for the selected campaign cannot exceed the maximum licensed ports
                                                      							 for outbound IVR minus the sum total of IVR ports dedicated to other campaigns
                                                      							 running at the same time. You can enter or update this value for a campaign only after
                                                      							 associating a trigger with the campaign. Default value = 0, Range = 0 to number
                                                      							 of available ports for the campaign duration. For example, if you have a medium or large profile VM, which
                                                      							 supports maximum of 300 IVR ports with 50 licensed ports for outbound IVR and
                                                      							 you have already dedicated: 20 ports for Campaign1, which runs between 10–12 pm 10 ports for Campaign2, which runs between 2–4 pm, then the
                                                            								  number of dedicated IVR ports that you can enter in this field for a new
                                                            								  campaign cannot exceed: 30 ports if the new campaign runs between 10–12 pm and 40 ports if the new campaign runs between 2–4 pm and 50 ports if the new campaign runs during any time other than
                                                                  										10–12 pm and 2–4 pm If
                                                      							 the number of configured ports for a campaign is greater than the available
                                                      							 number of licensed ports at the specified campaign time, then an alert message
                                                      							 stating the same will be shown while saving the campaign. Note Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. See Unified CCX Requirements to know how the licensed IVR ports are distributed between the inbound and
                                                      							 outbound IVR calls in different scenarios. Lines Per Port (1-3) Number of lines to be dialed for each port. The dialer will try
                                                      							 to connect as many live voices to the available port(s) where IVR script is
                                                      							 playing and it will disconnect the remaining calls. The probability of
                                                      							 abandoned calls increases geometrically as the lines per port increases. In
                                                      							 an IVR based progressive campaign, you can configure the number of lines to
                                                      							 dial per port at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per port * Available number of
                                                      							 ports. In
                                                      							 an IVR based predictive campaign, this is the seed value that is passed to the
                                                      							 predictive algorithm. Initially the dialer starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. The following fields in
                                                         								Dialing Options are displayed if you have selected Agent-based campaign
                                                         								type Lines Per Agent (1-3) Number of lines to be dialed for each agent. The dialer will try
                                                      							 to connect as many live voices to the available agent(s) and it will disconnect
                                                      							 the remaining calls. The probability of abandoned calls increases geometrically
                                                      							 as the lines per agent increases. In
                                                      							 an agent-based progressive campaign, you can configure the number of lines to
                                                      							 dial per agent at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per agent * Available number of
                                                      							 agents. In an agent-based predictive campaign, this is the seed value that is passed to the predictive algorithm. Initially the dialer
                                                      starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. Note This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. Callback Missed Determines the action that should be taken on the contacts that
                                                      							 were not called back. The three options for this field are: Reschedule for same time next business day (default) Mark it for a retry Close the record. The following fields in
                                                         								Dialing Options are common if you have selected Progressive or Predictive
                                                         								dialer type for IVR-based and Agent-based campaigns Handle Low Volume as Voice Determines whether a low volume call should be treated as voice
                                                      							 or disconnected. Select Yes or No radio button accordingly. Default is Yes, which means low volume calls are handled as
                                                      							 voice and they are connected to an IVR port or an agent. Answering Machine Treatment If
                                                      							 the outbound call detects an answering machine, you can choose to end the call
                                                      							 or transfer it to IVR by selecting the desired radio button in this field. For agent-based campaigns, if you choose to transfer the call to IVR, a trigger
                                                      							 field and an application name field appears for selection. The trigger field is a drop down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. The following fields in
                                                         								Dialing Options are common if you have selected Predictive dialer type for
                                                         								IVR-based and Agent-based campaigns Predictive Correction Pace (10-1000) The number of calls that were answered by live voice that the
                                                      							 predictive algorithm should consider for each iteration. This is directly
                                                      							 proportional with the correction frequency made in the Lines Per Port or Lines
                                                      							 Per Agent parameter. This is a mandatory field. Default value = 100, Range = 10
                                                      							 to 1000. Note It is advisable not to change this value. Predictive Gain The Gain parameter controls the size of the lines per port or
                                                      							 lines per agent corrections. This is directly proportional to the size of the
                                                      							 lines per port or lines per agent correction. This is a mandatory field. Default value = 1.0, Range = Greater
                                                      							 than 0 to 1.0. Note It is advisable not to change this value. Call Abandon Limit (0-100) Call abandon percentage, which should be within the limit
                                                      							 specified by Federal Trade Commission (FTC). This is a mandatory field. Default value - 3%, Range 0-100%. This means that no more than
                                                      							 three percent of calls that are answered by a person are abandoned, measured
                                                      							 per day per calling campaign. The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an IVR-based campaign Maximum Lines Per Port (1-3) Maximum number of lines to be dialed for each port. You can
                                                      							 configure the maximum number of lines that can be dialed per port and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an Agent-based campaign Maximum Lines Per Agent (1-3) Maximum number of lines to be dialed for each agent. You can
                                                      							 configure the maximum number of lines that can be dialed per agent and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. Dial Settings (displayed
                                                         								if you have selected IVR-based or Agent-based campaign types) No
                                                      							 Answer Ring Limit The duration for which the progressive/predictive dialer should
                                                      							 allow the customer phone to ring before disconnecting an unanswered call. The duration is calculated from the time the dialer receives the
                                                      							 ringing message from the gateway. If the dialer does not receive any ringing
                                                      							 message from the gateway within the time duration entered for this field, then
                                                      							 the dialer waits for the same time duration one more time before disconnecting
                                                      							 the call. For example, if you have configured the value for No Answer Ring
                                                      							 Limit as 30 seconds, then the dialer will wait for 60 seconds before
                                                      							 disconnecting the call. Default = 15 seconds, Range = 1 to 60 seconds. Note This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. Abandoned Call Wait Time For IVR-based progressive and predictive outbound campaigns, if
                                                      							 the customer disconnects the call within the time set here, then the call is
                                                      							 classified as customer abandoned. For agent-based progressive and predictive outbound campaigns,
                                                      							 if the customer or the agent disconnects the call within the time set here,
                                                      							 then the call is classified as customer abandoned. This is a mandatory field. Default value = 2 seconds, Range = 1 to 10 seconds. Retries (displayed if you
                                                         								have selected IVR-based or Agent-based campaign types): Set the value for
                                                      							 the following four fields as “0” if you want to disable retry option for an
                                                      							 existing IVR or agent based outbound campaign. Note The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. No
                                                      							 Answer Delay The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a no-answer call. Default value = 60 minutes. Though the default value is 60 minutes, the retry attempt will
                                                      							 not be made after 60 minutes. This is based on the value set for the Callback
                                                      							 Time Limit configured in the subsystem. For example, if a callback was
                                                      							 scheduled for 9:30 am and if the Callback Time Limit is set to 15 minutes, then
                                                      							 the Outbound subsystem calls the customer anytime between 9:15 am to 9:45 am. Note The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. Busy Signal Delay The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a busy telephone number. Default value = 60 minutes. This parameter is also based on the value set for the
                                                      							 Callback Time Limit as described above in the No Answer Delay. Customer Abandoned Delay For IVR-based progressive and predictive outbound campaigns, if a customer abandons a call, the time duration (in minutes)
                                                            after which the dialer should call the customer back. For agent-based progressive and predictive outbound campaigns, if a customer or an agent abandons a call, the time duration
                                                            (in minutes) after which the dialer should call the customer back. Default value = 0 Dialer Abandoned Delay If
                                                      							 the dialer abandons a call, the time duration (in minutes) after which the
                                                      							 dialer should call back the customer. Default value = 0 | Note | You need to
                                                      				  upload an Outbound license on top of the Premium license for Unified CCX to
                                                      				  create a campaign for Outbound. | Field | Description | Select the type of the
                                                         								campaign | Campaign Type | Type
                                                      							 of the campaign to be used for outbound calls. You can specify any one of the
                                                      							 following two campaign types: Agent-based—If you select this, all the outbound calls in a campaign will be handled by the available agents. IVR-based—If you select the IVR-based option, the outbound calls in a campaign will be handled by the IVR scripts. | Select the type of dialer
                                                         								for the campaign | Description | The dialer type options available for a campaign will vary depending on the selected Campaign Type. If you select Agent-based campaign type, then you can select any one of the following dialer types: Direct Preview (default) Progressive Predictive If you select IVR-based campaign type, then you can select any one of the following dialer types: Progressive (default) Predictive | Note | Once the campaign is created, you cannot change the Campaign Type and Dialer Type. | Field | Description | Campaign Name | Name
                                                      							 of the campaign (must be a unique identifier). This is a mandatory field. | Enabled | Indicates the current state of the campaign to the Outbound
                                                      							 subsystem. Yes
                                                      							 = The campaign is currently active. No =
                                                      							 The campaign is currently inactive (default). | Description | Description of the campaign. | Start Time/End Time (hh:mm) AM PM Time Zone | Indicate the time range during which the campaign runs. These
                                                      							 are mandatory fields. The name of the primary time zone is also displayed
                                                      							 adjacent to these two field values. Default = 8:00 AM - 9:00 PM Pacific Standard Time (USA FCC
                                                      							 regulations). | Campaign Calling Number | The campaign calling number is the number that will be displayed to the contact. This number is used by the dialer. This is
                                                      a mandatory field. Note This field is not available if you have selected the direct preview dialer type for an agent based campaign. | Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. | Maximum Attempts to Dial Contact | The maximum number of times the Outbound subsystem attempts to
                                                      							 dial a contact beyond which the call status will be marked as closed. You can
                                                      							 choose this value from the drop-down list box. Default = 3, Range = 1 to 3. | Callback Time Limit | The time period before and after the scheduled callback time
                                                      							 during which the Outbound subsystem attempts to dial out a callback. For
                                                      							 example, if a callback was scheduled for 9:30 am and if the Callback Time Limit
                                                      							 is set to 15 minutes, then the Outbound subsystem calls the customer anytime
                                                      							 between 9:15 am to 9:45 am. This field is also used to determine the dialing time range for
                                                      							 the Retries settings in the Add New Campaign web page. Default = 15 minutes, Range = 1 to 60 minutes. | Fields displayed only if
                                                         								you have selected IVR-based campaign type | Application Trigger | This is the JTAPI trigger associated with this campaign. There
                                                      							 will one-to-one mapping between a campaign and an application trigger. Only
                                                      							 those triggers that are not associated with any other campaigns are displayed
                                                      							 in the trigger list. | Application Name | The name of the application associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. | Fields displayed only if
                                                         								you have selected Agent-based campaign type | Abandoned Call Treatment | If the agent is not available to handle the call, you can choose to abandon the
                                                      							 call or transfer it to IVR by selecting the desired radio button in this field.
                                                      							 If you choose to transfer the call to IVR, a trigger field and an application
                                                      							 name field appears for selection. The trigger field is a drop-down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. Note This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. | Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. | Assigned CSQs | The CSQs from which agents are selected for Outbound calls for
                                                      							 this campaign. This is a mandatory field. Note For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. | Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. | Available CSQs | For direct preview campaigns—CSQs that are allocated for
                                                      							 outbound but not assigned to any progressive or predictive agent-based
                                                      							 campaign. For progressive and predictive agent-based campaigns—CSQs that
                                                      							 are allocated for outbound and not assigned to any other campaign. | Fields displayed only if
                                                         								you have selected Direct Preview dialer type for an Agent-based campaign | Contact Records Cache Size | The number of contact records the Outbound subsystem retrieves
                                                      							 from the database in bulk for dialing. The allowed values are 1–100. This is a
                                                      							 mandatory field. For example, if 50 records are retrieved in bulk for campaign1
                                                      							 and 10 for campaign2 and they are running at the same time, the Outbound
                                                      							 subsystem attempts to place 50 Outbound calls for campaign1 and 10 Outbound
                                                      							 calls for campaign2. The number of Outbound calls actually placed for each
                                                      							 campaign depends upon the number of agents available for the respective
                                                      							 campaigns. Once all the records retrieved for a campaign have been dialed,
                                                      							 the Outbound subsystem retrieves another batch of records for that campaign.
                                                      							 Over a period of time, it is likely that more contacts would have been called
                                                      							 from campaign1 than from campaign2. If
                                                      							 two campaigns run simultaneously and share CSQs or agents, the records in both
                                                      							 campaigns may not be processed at the same rate even if their contact cache
                                                      							 sizes are identical. It is possible that more records from one of these two
                                                      							 campaigns is processed before the other. Default = 20, Range = 1 to 100 | Answering Machine Retry | If
                                                      							 you select Yes, then the Outbound subsystem retries the contact after all the
                                                      							 callbacks and pending contacts for the campaign are dialed out. Default = No | The following fields in
                                                         								Dialing Options are displayed if you have selected IVR-based campaign type | Number of Dedicated Ports | Number of dedicated IVR ports that you want to reserve for this
                                                      							 campaign based on the number of CTI ports available in the outbound call
                                                      							 control group for the campaign duration. That is, the total number of dedicated
                                                      							 IVR ports for the selected campaign cannot exceed the maximum licensed ports
                                                      							 for outbound IVR minus the sum total of IVR ports dedicated to other campaigns
                                                      							 running at the same time. You can enter or update this value for a campaign only after
                                                      							 associating a trigger with the campaign. Default value = 0, Range = 0 to number
                                                      							 of available ports for the campaign duration. For example, if you have a medium or large profile VM, which
                                                      							 supports maximum of 300 IVR ports with 50 licensed ports for outbound IVR and
                                                      							 you have already dedicated: 20 ports for Campaign1, which runs between 10–12 pm 10 ports for Campaign2, which runs between 2–4 pm, then the
                                                            								  number of dedicated IVR ports that you can enter in this field for a new
                                                            								  campaign cannot exceed: 30 ports if the new campaign runs between 10–12 pm and 40 ports if the new campaign runs between 2–4 pm and 50 ports if the new campaign runs during any time other than
                                                                  										10–12 pm and 2–4 pm If
                                                      							 the number of configured ports for a campaign is greater than the available
                                                      							 number of licensed ports at the specified campaign time, then an alert message
                                                      							 stating the same will be shown while saving the campaign. Note Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. See Unified CCX Requirements to know how the licensed IVR ports are distributed between the inbound and
                                                      							 outbound IVR calls in different scenarios. | Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. | Lines Per Port (1-3) | Number of lines to be dialed for each port. The dialer will try
                                                      							 to connect as many live voices to the available port(s) where IVR script is
                                                      							 playing and it will disconnect the remaining calls. The probability of
                                                      							 abandoned calls increases geometrically as the lines per port increases. In
                                                      							 an IVR based progressive campaign, you can configure the number of lines to
                                                      							 dial per port at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per port * Available number of
                                                      							 ports. In
                                                      							 an IVR based predictive campaign, this is the seed value that is passed to the
                                                      							 predictive algorithm. Initially the dialer starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. | The following fields in
                                                         								Dialing Options are displayed if you have selected Agent-based campaign
                                                         								type | Lines Per Agent (1-3) | Number of lines to be dialed for each agent. The dialer will try
                                                      							 to connect as many live voices to the available agent(s) and it will disconnect
                                                      							 the remaining calls. The probability of abandoned calls increases geometrically
                                                      							 as the lines per agent increases. In
                                                      							 an agent-based progressive campaign, you can configure the number of lines to
                                                      							 dial per agent at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per agent * Available number of
                                                      							 agents. In an agent-based predictive campaign, this is the seed value that is passed to the predictive algorithm. Initially the dialer
                                                      starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. Note This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. | Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. | Callback Missed | Determines the action that should be taken on the contacts that
                                                      							 were not called back. The three options for this field are: Reschedule for same time next business day (default) Mark it for a retry Close the record. | The following fields in
                                                         								Dialing Options are common if you have selected Progressive or Predictive
                                                         								dialer type for IVR-based and Agent-based campaigns | Handle Low Volume as Voice | Determines whether a low volume call should be treated as voice
                                                      							 or disconnected. Select Yes or No radio button accordingly. Default is Yes, which means low volume calls are handled as
                                                      							 voice and they are connected to an IVR port or an agent. | Answering Machine Treatment | If
                                                      							 the outbound call detects an answering machine, you can choose to end the call
                                                      							 or transfer it to IVR by selecting the desired radio button in this field. For agent-based campaigns, if you choose to transfer the call to IVR, a trigger
                                                      							 field and an application name field appears for selection. The trigger field is a drop down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. | The following fields in
                                                         								Dialing Options are common if you have selected Predictive dialer type for
                                                         								IVR-based and Agent-based campaigns | Predictive Correction Pace (10-1000) | The number of calls that were answered by live voice that the
                                                      							 predictive algorithm should consider for each iteration. This is directly
                                                      							 proportional with the correction frequency made in the Lines Per Port or Lines
                                                      							 Per Agent parameter. This is a mandatory field. Default value = 100, Range = 10
                                                      							 to 1000. Note It is advisable not to change this value. | Note | It is advisable not to change this value. | Predictive Gain | The Gain parameter controls the size of the lines per port or
                                                      							 lines per agent corrections. This is directly proportional to the size of the
                                                      							 lines per port or lines per agent correction. This is a mandatory field. Default value = 1.0, Range = Greater
                                                      							 than 0 to 1.0. Note It is advisable not to change this value. | Note | It is advisable not to change this value. | Call Abandon Limit (0-100) | Call abandon percentage, which should be within the limit
                                                      							 specified by Federal Trade Commission (FTC). This is a mandatory field. Default value - 3%, Range 0-100%. This means that no more than
                                                      							 three percent of calls that are answered by a person are abandoned, measured
                                                      							 per day per calling campaign. | The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an IVR-based campaign | Maximum Lines Per Port (1-3) | Maximum number of lines to be dialed for each port. You can
                                                      							 configure the maximum number of lines that can be dialed per port and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. | The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an Agent-based campaign | Maximum Lines Per Agent (1-3) | Maximum number of lines to be dialed for each agent. You can
                                                      							 configure the maximum number of lines that can be dialed per agent and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. | Dial Settings (displayed
                                                         								if you have selected IVR-based or Agent-based campaign types) | No
                                                      							 Answer Ring Limit | The duration for which the progressive/predictive dialer should
                                                      							 allow the customer phone to ring before disconnecting an unanswered call. The duration is calculated from the time the dialer receives the
                                                      							 ringing message from the gateway. If the dialer does not receive any ringing
                                                      							 message from the gateway within the time duration entered for this field, then
                                                      							 the dialer waits for the same time duration one more time before disconnecting
                                                      							 the call. For example, if you have configured the value for No Answer Ring
                                                      							 Limit as 30 seconds, then the dialer will wait for 60 seconds before
                                                      							 disconnecting the call. Default = 15 seconds, Range = 1 to 60 seconds. Note This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. | Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. | Abandoned Call Wait Time | For IVR-based progressive and predictive outbound campaigns, if
                                                      							 the customer disconnects the call within the time set here, then the call is
                                                      							 classified as customer abandoned. For agent-based progressive and predictive outbound campaigns,
                                                      							 if the customer or the agent disconnects the call within the time set here,
                                                      							 then the call is classified as customer abandoned. This is a mandatory field. Default value = 2 seconds, Range = 1 to 10 seconds. | Retries (displayed if you
                                                         								have selected IVR-based or Agent-based campaign types): Set the value for
                                                      							 the following four fields as “0” if you want to disable retry option for an
                                                      							 existing IVR or agent based outbound campaign. Note The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. | Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. | No
                                                      							 Answer Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a no-answer call. Default value = 60 minutes. Though the default value is 60 minutes, the retry attempt will
                                                      							 not be made after 60 minutes. This is based on the value set for the Callback
                                                      							 Time Limit configured in the subsystem. For example, if a callback was
                                                      							 scheduled for 9:30 am and if the Callback Time Limit is set to 15 minutes, then
                                                      							 the Outbound subsystem calls the customer anytime between 9:15 am to 9:45 am. Note The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. | Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. | Busy Signal Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a busy telephone number. Default value = 60 minutes. This parameter is also based on the value set for the
                                                      							 Callback Time Limit as described above in the No Answer Delay. | Customer Abandoned Delay | For IVR-based progressive and predictive outbound campaigns, if a customer abandons a call, the time duration (in minutes)
                                                            after which the dialer should call the customer back. For agent-based progressive and predictive outbound campaigns, if a customer or an agent abandons a call, the time duration
                                                            (in minutes) after which the dialer should call the customer back. Default value = 0 | Dialer Abandoned Delay | If
                                                      							 the dialer abandons a call, the time duration (in minutes) after which the
                                                      							 dialer should call back the customer. Default value = 0 |
| Note | You need to
                                                      				  upload an Outbound license on top of the Premium license for Unified CCX to
                                                      				  create a campaign for Outbound. |
| Field | Description |
| Select the type of the
                                                         								campaign |
| Campaign Type | Type
                                                      							 of the campaign to be used for outbound calls. You can specify any one of the
                                                      							 following two campaign types: Agent-based—If you select this, all the outbound calls in a campaign will be handled by the available agents. IVR-based—If you select the IVR-based option, the outbound calls in a campaign will be handled by the IVR scripts. |
| Select the type of dialer
                                                         								for the campaign |
| Description | The dialer type options available for a campaign will vary depending on the selected Campaign Type. If you select Agent-based campaign type, then you can select any one of the following dialer types: Direct Preview (default) Progressive Predictive If you select IVR-based campaign type, then you can select any one of the following dialer types: Progressive (default) Predictive |
| Note | Once the campaign is created, you cannot change the Campaign Type and Dialer Type. |
| Field | Description |
| Campaign Name | Name
                                                      							 of the campaign (must be a unique identifier). This is a mandatory field. |
| Enabled | Indicates the current state of the campaign to the Outbound
                                                      							 subsystem. Yes
                                                      							 = The campaign is currently active. No =
                                                      							 The campaign is currently inactive (default). |
| Description | Description of the campaign. |
| Start Time/End Time (hh:mm) AM PM Time Zone | Indicate the time range during which the campaign runs. These
                                                      							 are mandatory fields. The name of the primary time zone is also displayed
                                                      							 adjacent to these two field values. Default = 8:00 AM - 9:00 PM Pacific Standard Time (USA FCC
                                                      							 regulations). |
| Campaign Calling Number | The campaign calling number is the number that will be displayed to the contact. This number is used by the dialer. This is
                                                      a mandatory field. Note This field is not available if you have selected the direct preview dialer type for an agent based campaign. | Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. |
| Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. |
| Maximum Attempts to Dial Contact | The maximum number of times the Outbound subsystem attempts to
                                                      							 dial a contact beyond which the call status will be marked as closed. You can
                                                      							 choose this value from the drop-down list box. Default = 3, Range = 1 to 3. |
| Callback Time Limit | The time period before and after the scheduled callback time
                                                      							 during which the Outbound subsystem attempts to dial out a callback. For
                                                      							 example, if a callback was scheduled for 9:30 am and if the Callback Time Limit
                                                      							 is set to 15 minutes, then the Outbound subsystem calls the customer anytime
                                                      							 between 9:15 am to 9:45 am. This field is also used to determine the dialing time range for
                                                      							 the Retries settings in the Add New Campaign web page. Default = 15 minutes, Range = 1 to 60 minutes. |
| Fields displayed only if
                                                         								you have selected IVR-based campaign type |
| Application Trigger | This is the JTAPI trigger associated with this campaign. There
                                                      							 will one-to-one mapping between a campaign and an application trigger. Only
                                                      							 those triggers that are not associated with any other campaigns are displayed
                                                      							 in the trigger list. |
| Application Name | The name of the application associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. |
| Fields displayed only if
                                                         								you have selected Agent-based campaign type |
| Abandoned Call Treatment | If the agent is not available to handle the call, you can choose to abandon the
                                                      							 call or transfer it to IVR by selecting the desired radio button in this field.
                                                      							 If you choose to transfer the call to IVR, a trigger field and an application
                                                      							 name field appears for selection. The trigger field is a drop-down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. Note This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. | Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. |
| Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. |
| Assigned CSQs | The CSQs from which agents are selected for Outbound calls for
                                                      							 this campaign. This is a mandatory field. Note For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. | Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. |
| Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. |
| Available CSQs | For direct preview campaigns—CSQs that are allocated for
                                                      							 outbound but not assigned to any progressive or predictive agent-based
                                                      							 campaign. For progressive and predictive agent-based campaigns—CSQs that
                                                      							 are allocated for outbound and not assigned to any other campaign. |
| Fields displayed only if
                                                         								you have selected Direct Preview dialer type for an Agent-based campaign |
| Contact Records Cache Size | The number of contact records the Outbound subsystem retrieves
                                                      							 from the database in bulk for dialing. The allowed values are 1–100. This is a
                                                      							 mandatory field. For example, if 50 records are retrieved in bulk for campaign1
                                                      							 and 10 for campaign2 and they are running at the same time, the Outbound
                                                      							 subsystem attempts to place 50 Outbound calls for campaign1 and 10 Outbound
                                                      							 calls for campaign2. The number of Outbound calls actually placed for each
                                                      							 campaign depends upon the number of agents available for the respective
                                                      							 campaigns. Once all the records retrieved for a campaign have been dialed,
                                                      							 the Outbound subsystem retrieves another batch of records for that campaign.
                                                      							 Over a period of time, it is likely that more contacts would have been called
                                                      							 from campaign1 than from campaign2. If
                                                      							 two campaigns run simultaneously and share CSQs or agents, the records in both
                                                      							 campaigns may not be processed at the same rate even if their contact cache
                                                      							 sizes are identical. It is possible that more records from one of these two
                                                      							 campaigns is processed before the other. Default = 20, Range = 1 to 100 |
| Answering Machine Retry | If
                                                      							 you select Yes, then the Outbound subsystem retries the contact after all the
                                                      							 callbacks and pending contacts for the campaign are dialed out. Default = No |
| The following fields in
                                                         								Dialing Options are displayed if you have selected IVR-based campaign type |
| Number of Dedicated Ports | Number of dedicated IVR ports that you want to reserve for this
                                                      							 campaign based on the number of CTI ports available in the outbound call
                                                      							 control group for the campaign duration. That is, the total number of dedicated
                                                      							 IVR ports for the selected campaign cannot exceed the maximum licensed ports
                                                      							 for outbound IVR minus the sum total of IVR ports dedicated to other campaigns
                                                      							 running at the same time. You can enter or update this value for a campaign only after
                                                      							 associating a trigger with the campaign. Default value = 0, Range = 0 to number
                                                      							 of available ports for the campaign duration. For example, if you have a medium or large profile VM, which
                                                      							 supports maximum of 300 IVR ports with 50 licensed ports for outbound IVR and
                                                      							 you have already dedicated: 20 ports for Campaign1, which runs between 10–12 pm 10 ports for Campaign2, which runs between 2–4 pm, then the
                                                            								  number of dedicated IVR ports that you can enter in this field for a new
                                                            								  campaign cannot exceed: 30 ports if the new campaign runs between 10–12 pm and 40 ports if the new campaign runs between 2–4 pm and 50 ports if the new campaign runs during any time other than
                                                                  										10–12 pm and 2–4 pm If
                                                      							 the number of configured ports for a campaign is greater than the available
                                                      							 number of licensed ports at the specified campaign time, then an alert message
                                                      							 stating the same will be shown while saving the campaign. Note Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. See Unified CCX Requirements to know how the licensed IVR ports are distributed between the inbound and
                                                      							 outbound IVR calls in different scenarios. | Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. |
| Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. |
| Lines Per Port (1-3) | Number of lines to be dialed for each port. The dialer will try
                                                      							 to connect as many live voices to the available port(s) where IVR script is
                                                      							 playing and it will disconnect the remaining calls. The probability of
                                                      							 abandoned calls increases geometrically as the lines per port increases. In
                                                      							 an IVR based progressive campaign, you can configure the number of lines to
                                                      							 dial per port at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per port * Available number of
                                                      							 ports. In
                                                      							 an IVR based predictive campaign, this is the seed value that is passed to the
                                                      							 predictive algorithm. Initially the dialer starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| The following fields in
                                                         								Dialing Options are displayed if you have selected Agent-based campaign
                                                         								type |
| Lines Per Agent (1-3) | Number of lines to be dialed for each agent. The dialer will try
                                                      							 to connect as many live voices to the available agent(s) and it will disconnect
                                                      							 the remaining calls. The probability of abandoned calls increases geometrically
                                                      							 as the lines per agent increases. In
                                                      							 an agent-based progressive campaign, you can configure the number of lines to
                                                      							 dial per agent at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per agent * Available number of
                                                      							 agents. In an agent-based predictive campaign, this is the seed value that is passed to the predictive algorithm. Initially the dialer
                                                      starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. Note This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. | Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. |
| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. |
| Callback Missed | Determines the action that should be taken on the contacts that
                                                      							 were not called back. The three options for this field are: Reschedule for same time next business day (default) Mark it for a retry Close the record. |
| The following fields in
                                                         								Dialing Options are common if you have selected Progressive or Predictive
                                                         								dialer type for IVR-based and Agent-based campaigns |
| Handle Low Volume as Voice | Determines whether a low volume call should be treated as voice
                                                      							 or disconnected. Select Yes or No radio button accordingly. Default is Yes, which means low volume calls are handled as
                                                      							 voice and they are connected to an IVR port or an agent. |
| Answering Machine Treatment | If
                                                      							 the outbound call detects an answering machine, you can choose to end the call
                                                      							 or transfer it to IVR by selecting the desired radio button in this field. For agent-based campaigns, if you choose to transfer the call to IVR, a trigger
                                                      							 field and an application name field appears for selection. The trigger field is a drop down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. |
| The following fields in
                                                         								Dialing Options are common if you have selected Predictive dialer type for
                                                         								IVR-based and Agent-based campaigns |
| Predictive Correction Pace (10-1000) | The number of calls that were answered by live voice that the
                                                      							 predictive algorithm should consider for each iteration. This is directly
                                                      							 proportional with the correction frequency made in the Lines Per Port or Lines
                                                      							 Per Agent parameter. This is a mandatory field. Default value = 100, Range = 10
                                                      							 to 1000. Note It is advisable not to change this value. | Note | It is advisable not to change this value. |
| Note | It is advisable not to change this value. |
| Predictive Gain | The Gain parameter controls the size of the lines per port or
                                                      							 lines per agent corrections. This is directly proportional to the size of the
                                                      							 lines per port or lines per agent correction. This is a mandatory field. Default value = 1.0, Range = Greater
                                                      							 than 0 to 1.0. Note It is advisable not to change this value. | Note | It is advisable not to change this value. |
| Note | It is advisable not to change this value. |
| Call Abandon Limit (0-100) | Call abandon percentage, which should be within the limit
                                                      							 specified by Federal Trade Commission (FTC). This is a mandatory field. Default value - 3%, Range 0-100%. This means that no more than
                                                      							 three percent of calls that are answered by a person are abandoned, measured
                                                      							 per day per calling campaign. |
| The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an IVR-based campaign |
| Maximum Lines Per Port (1-3) | Maximum number of lines to be dialed for each port. You can
                                                      							 configure the maximum number of lines that can be dialed per port and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. |
| The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an Agent-based campaign |
| Maximum Lines Per Agent (1-3) | Maximum number of lines to be dialed for each agent. You can
                                                      							 configure the maximum number of lines that can be dialed per agent and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. |
| Dial Settings (displayed
                                                         								if you have selected IVR-based or Agent-based campaign types) |
| No
                                                      							 Answer Ring Limit | The duration for which the progressive/predictive dialer should
                                                      							 allow the customer phone to ring before disconnecting an unanswered call. The duration is calculated from the time the dialer receives the
                                                      							 ringing message from the gateway. If the dialer does not receive any ringing
                                                      							 message from the gateway within the time duration entered for this field, then
                                                      							 the dialer waits for the same time duration one more time before disconnecting
                                                      							 the call. For example, if you have configured the value for No Answer Ring
                                                      							 Limit as 30 seconds, then the dialer will wait for 60 seconds before
                                                      							 disconnecting the call. Default = 15 seconds, Range = 1 to 60 seconds. Note This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. | Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. |
| Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. |
| Abandoned Call Wait Time | For IVR-based progressive and predictive outbound campaigns, if
                                                      							 the customer disconnects the call within the time set here, then the call is
                                                      							 classified as customer abandoned. For agent-based progressive and predictive outbound campaigns,
                                                      							 if the customer or the agent disconnects the call within the time set here,
                                                      							 then the call is classified as customer abandoned. This is a mandatory field. Default value = 2 seconds, Range = 1 to 10 seconds. |
| Retries (displayed if you
                                                         								have selected IVR-based or Agent-based campaign types): Set the value for
                                                      							 the following four fields as “0” if you want to disable retry option for an
                                                      							 existing IVR or agent based outbound campaign. Note The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. | Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. |
| Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. |
| No
                                                      							 Answer Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a no-answer call. Default value = 60 minutes. Though the default value is 60 minutes, the retry attempt will
                                                      							 not be made after 60 minutes. This is based on the value set for the Callback
                                                      							 Time Limit configured in the subsystem. For example, if a callback was
                                                      							 scheduled for 9:30 am and if the Callback Time Limit is set to 15 minutes, then
                                                      							 the Outbound subsystem calls the customer anytime between 9:15 am to 9:45 am. Note The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. | Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. |
| Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. |
| Busy Signal Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a busy telephone number. Default value = 60 minutes. This parameter is also based on the value set for the
                                                      							 Callback Time Limit as described above in the No Answer Delay. |
| Customer Abandoned Delay | For IVR-based progressive and predictive outbound campaigns, if a customer abandons a call, the time duration (in minutes)
                                                            after which the dialer should call the customer back. For agent-based progressive and predictive outbound campaigns, if a customer or an agent abandons a call, the time duration
                                                            (in minutes) after which the dialer should call the customer back. Default value = 0 |
| Dialer Abandoned Delay | If
                                                      							 the dialer abandons a call, the time duration (in minutes) after which the
                                                      							 dialer should call back the customer. Default value = 0 |
| Step 3 | Click Add or Save to save the configuration changes. While saving
                                       			 a new or updated campaign, the Outbound subsystem validates the Session values
                                       			 in the application and trigger pages based on following criteria, and it might
                                       			 display an alert message to increase Session value in application and trigger
                                       			 pages: In case
                                                					 of a Progressive campaign, the outbound subsystem checks whether the Lines Per
                                                					 Port * Dedicated Port for IVR-based campaigns and Lines Per Agent * Dedicated
                                                					 Agent for agent-based campaigns is greater than the minimum of the Session
                                                					 value in application and trigger. In case
                                                					 of a Predictive campaign, the outbound subsystem checks whether the maximum
                                                					 Lines Per Port * Dedicated Port for IVR-based campaigns and maximum Lines Per
                                                					 Agent * Dedicated Agent for agent-based campaigns is greater than minimum of
                                                					 the Session value in application and trigger. You should
                                          				increase the Session values in the application and trigger to the suggested
                                          				value in the alert message to reduce the number of abandoned calls in an
                                          				Outbound campaign. Once you
                                          				create a campaign, you need to import contacts for the campaign. |

| Note | You need to
                                                      				  upload an Outbound license on top of the Premium license for Unified CCX to
                                                      				  create a campaign for Outbound. |
|---|---|

| Field | Description |
|---|---|
| Select the type of the
                                                         								campaign |
| Campaign Type | Type
                                                      							 of the campaign to be used for outbound calls. You can specify any one of the
                                                      							 following two campaign types: Agent-based—If you select this, all the outbound calls in a campaign will be handled by the available agents. IVR-based—If you select the IVR-based option, the outbound calls in a campaign will be handled by the IVR scripts. |
| Select the type of dialer
                                                         								for the campaign |
| Description | The dialer type options available for a campaign will vary depending on the selected Campaign Type. If you select Agent-based campaign type, then you can select any one of the following dialer types: Direct Preview (default) Progressive Predictive If you select IVR-based campaign type, then you can select any one of the following dialer types: Progressive (default) Predictive |

| Note | Once the campaign is created, you cannot change the Campaign Type and Dialer Type. |
|---|---|

| Field | Description |
|---|---|
| Campaign Name | Name
                                                      							 of the campaign (must be a unique identifier). This is a mandatory field. |
| Enabled | Indicates the current state of the campaign to the Outbound
                                                      							 subsystem. Yes
                                                      							 = The campaign is currently active. No =
                                                      							 The campaign is currently inactive (default). |
| Description | Description of the campaign. |
| Start Time/End Time (hh:mm) AM PM Time Zone | Indicate the time range during which the campaign runs. These
                                                      							 are mandatory fields. The name of the primary time zone is also displayed
                                                      							 adjacent to these two field values. Default = 8:00 AM - 9:00 PM Pacific Standard Time (USA FCC
                                                      							 regulations). |
| Campaign Calling Number | The campaign calling number is the number that will be displayed to the contact. This number is used by the dialer. This is
                                                      a mandatory field. Note This field is not available if you have selected the direct preview dialer type for an agent based campaign. | Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. |
| Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. |
| Maximum Attempts to Dial Contact | The maximum number of times the Outbound subsystem attempts to
                                                      							 dial a contact beyond which the call status will be marked as closed. You can
                                                      							 choose this value from the drop-down list box. Default = 3, Range = 1 to 3. |
| Callback Time Limit | The time period before and after the scheduled callback time
                                                      							 during which the Outbound subsystem attempts to dial out a callback. For
                                                      							 example, if a callback was scheduled for 9:30 am and if the Callback Time Limit
                                                      							 is set to 15 minutes, then the Outbound subsystem calls the customer anytime
                                                      							 between 9:15 am to 9:45 am. This field is also used to determine the dialing time range for
                                                      							 the Retries settings in the Add New Campaign web page. Default = 15 minutes, Range = 1 to 60 minutes. |
| Fields displayed only if
                                                         								you have selected IVR-based campaign type |
| Application Trigger | This is the JTAPI trigger associated with this campaign. There
                                                      							 will one-to-one mapping between a campaign and an application trigger. Only
                                                      							 those triggers that are not associated with any other campaigns are displayed
                                                      							 in the trigger list. |
| Application Name | The name of the application associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. |
| Fields displayed only if
                                                         								you have selected Agent-based campaign type |
| Abandoned Call Treatment | If the agent is not available to handle the call, you can choose to abandon the
                                                      							 call or transfer it to IVR by selecting the desired radio button in this field.
                                                      							 If you choose to transfer the call to IVR, a trigger field and an application
                                                      							 name field appears for selection. The trigger field is a drop-down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. Note This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. | Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. |
| Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. |
| Assigned CSQs | The CSQs from which agents are selected for Outbound calls for
                                                      							 this campaign. This is a mandatory field. Note For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. | Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. |
| Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. |
| Available CSQs | For direct preview campaigns—CSQs that are allocated for
                                                      							 outbound but not assigned to any progressive or predictive agent-based
                                                      							 campaign. For progressive and predictive agent-based campaigns—CSQs that
                                                      							 are allocated for outbound and not assigned to any other campaign. |
| Fields displayed only if
                                                         								you have selected Direct Preview dialer type for an Agent-based campaign |
| Contact Records Cache Size | The number of contact records the Outbound subsystem retrieves
                                                      							 from the database in bulk for dialing. The allowed values are 1–100. This is a
                                                      							 mandatory field. For example, if 50 records are retrieved in bulk for campaign1
                                                      							 and 10 for campaign2 and they are running at the same time, the Outbound
                                                      							 subsystem attempts to place 50 Outbound calls for campaign1 and 10 Outbound
                                                      							 calls for campaign2. The number of Outbound calls actually placed for each
                                                      							 campaign depends upon the number of agents available for the respective
                                                      							 campaigns. Once all the records retrieved for a campaign have been dialed,
                                                      							 the Outbound subsystem retrieves another batch of records for that campaign.
                                                      							 Over a period of time, it is likely that more contacts would have been called
                                                      							 from campaign1 than from campaign2. If
                                                      							 two campaigns run simultaneously and share CSQs or agents, the records in both
                                                      							 campaigns may not be processed at the same rate even if their contact cache
                                                      							 sizes are identical. It is possible that more records from one of these two
                                                      							 campaigns is processed before the other. Default = 20, Range = 1 to 100 |
| Answering Machine Retry | If
                                                      							 you select Yes, then the Outbound subsystem retries the contact after all the
                                                      							 callbacks and pending contacts for the campaign are dialed out. Default = No |
| The following fields in
                                                         								Dialing Options are displayed if you have selected IVR-based campaign type |
| Number of Dedicated Ports | Number of dedicated IVR ports that you want to reserve for this
                                                      							 campaign based on the number of CTI ports available in the outbound call
                                                      							 control group for the campaign duration. That is, the total number of dedicated
                                                      							 IVR ports for the selected campaign cannot exceed the maximum licensed ports
                                                      							 for outbound IVR minus the sum total of IVR ports dedicated to other campaigns
                                                      							 running at the same time. You can enter or update this value for a campaign only after
                                                      							 associating a trigger with the campaign. Default value = 0, Range = 0 to number
                                                      							 of available ports for the campaign duration. For example, if you have a medium or large profile VM, which
                                                      							 supports maximum of 300 IVR ports with 50 licensed ports for outbound IVR and
                                                      							 you have already dedicated: 20 ports for Campaign1, which runs between 10–12 pm 10 ports for Campaign2, which runs between 2–4 pm, then the
                                                            								  number of dedicated IVR ports that you can enter in this field for a new
                                                            								  campaign cannot exceed: 30 ports if the new campaign runs between 10–12 pm and 40 ports if the new campaign runs between 2–4 pm and 50 ports if the new campaign runs during any time other than
                                                                  										10–12 pm and 2–4 pm If
                                                      							 the number of configured ports for a campaign is greater than the available
                                                      							 number of licensed ports at the specified campaign time, then an alert message
                                                      							 stating the same will be shown while saving the campaign. Note Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. See Unified CCX Requirements to know how the licensed IVR ports are distributed between the inbound and
                                                      							 outbound IVR calls in different scenarios. | Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. |
| Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. |
| Lines Per Port (1-3) | Number of lines to be dialed for each port. The dialer will try
                                                      							 to connect as many live voices to the available port(s) where IVR script is
                                                      							 playing and it will disconnect the remaining calls. The probability of
                                                      							 abandoned calls increases geometrically as the lines per port increases. In
                                                      							 an IVR based progressive campaign, you can configure the number of lines to
                                                      							 dial per port at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per port * Available number of
                                                      							 ports. In
                                                      							 an IVR based predictive campaign, this is the seed value that is passed to the
                                                      							 predictive algorithm. Initially the dialer starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| The following fields in
                                                         								Dialing Options are displayed if you have selected Agent-based campaign
                                                         								type |
| Lines Per Agent (1-3) | Number of lines to be dialed for each agent. The dialer will try
                                                      							 to connect as many live voices to the available agent(s) and it will disconnect
                                                      							 the remaining calls. The probability of abandoned calls increases geometrically
                                                      							 as the lines per agent increases. In
                                                      							 an agent-based progressive campaign, you can configure the number of lines to
                                                      							 dial per agent at a time. The dialer will determine the number of calls to dial
                                                      							 based on the following calculation - Lines per agent * Available number of
                                                      							 agents. In an agent-based predictive campaign, this is the seed value that is passed to the predictive algorithm. Initially the dialer
                                                      starts dialing with this value. Note Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. This is a mandatory field. Default value = 1.5; Range = 1 to 3. Note This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. | Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. | Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. |
| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
| Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. |
| Callback Missed | Determines the action that should be taken on the contacts that
                                                      							 were not called back. The three options for this field are: Reschedule for same time next business day (default) Mark it for a retry Close the record. |
| The following fields in
                                                         								Dialing Options are common if you have selected Progressive or Predictive
                                                         								dialer type for IVR-based and Agent-based campaigns |
| Handle Low Volume as Voice | Determines whether a low volume call should be treated as voice
                                                      							 or disconnected. Select Yes or No radio button accordingly. Default is Yes, which means low volume calls are handled as
                                                      							 voice and they are connected to an IVR port or an agent. |
| Answering Machine Treatment | If
                                                      							 the outbound call detects an answering machine, you can choose to end the call
                                                      							 or transfer it to IVR by selecting the desired radio button in this field. For agent-based campaigns, if you choose to transfer the call to IVR, a trigger
                                                      							 field and an application name field appears for selection. The trigger field is a drop down list of JTAPI triggers
                                                      							 associated with this campaign. There is one-to-one mapping between a campaign
                                                      							 and a trigger. Only those triggers that are not associated with any other
                                                      							 campaigns are displayed in the trigger list. The application name is associated with the above-mentioned
                                                      							 JTAPI trigger. This field is auto-populated. Transfer to IVR radio button is enabled by default. |
| The following fields in
                                                         								Dialing Options are common if you have selected Predictive dialer type for
                                                         								IVR-based and Agent-based campaigns |
| Predictive Correction Pace (10-1000) | The number of calls that were answered by live voice that the
                                                      							 predictive algorithm should consider for each iteration. This is directly
                                                      							 proportional with the correction frequency made in the Lines Per Port or Lines
                                                      							 Per Agent parameter. This is a mandatory field. Default value = 100, Range = 10
                                                      							 to 1000. Note It is advisable not to change this value. | Note | It is advisable not to change this value. |
| Note | It is advisable not to change this value. |
| Predictive Gain | The Gain parameter controls the size of the lines per port or
                                                      							 lines per agent corrections. This is directly proportional to the size of the
                                                      							 lines per port or lines per agent correction. This is a mandatory field. Default value = 1.0, Range = Greater
                                                      							 than 0 to 1.0. Note It is advisable not to change this value. | Note | It is advisable not to change this value. |
| Note | It is advisable not to change this value. |
| Call Abandon Limit (0-100) | Call abandon percentage, which should be within the limit
                                                      							 specified by Federal Trade Commission (FTC). This is a mandatory field. Default value - 3%, Range 0-100%. This means that no more than
                                                      							 three percent of calls that are answered by a person are abandoned, measured
                                                      							 per day per calling campaign. |
| The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an IVR-based campaign |
| Maximum Lines Per Port (1-3) | Maximum number of lines to be dialed for each port. You can
                                                      							 configure the maximum number of lines that can be dialed per port and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. |
| The following field in
                                                         								Dialing Options is displayed only if you have selected Predictive dialer type
                                                         								for an Agent-based campaign |
| Maximum Lines Per Agent (1-3) | Maximum number of lines to be dialed for each agent. You can
                                                      							 configure the maximum number of lines that can be dialed per agent and the
                                                      							 predictive algorithm ensures that it does not exceed this number. This is a mandatory field. Default value = 3.0, Range = 1 to 3. |
| Dial Settings (displayed
                                                         								if you have selected IVR-based or Agent-based campaign types) |
| No
                                                      							 Answer Ring Limit | The duration for which the progressive/predictive dialer should
                                                      							 allow the customer phone to ring before disconnecting an unanswered call. The duration is calculated from the time the dialer receives the
                                                      							 ringing message from the gateway. If the dialer does not receive any ringing
                                                      							 message from the gateway within the time duration entered for this field, then
                                                      							 the dialer waits for the same time duration one more time before disconnecting
                                                      							 the call. For example, if you have configured the value for No Answer Ring
                                                      							 Limit as 30 seconds, then the dialer will wait for 60 seconds before
                                                      							 disconnecting the call. Default = 15 seconds, Range = 1 to 60 seconds. Note This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. | Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. |
| Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. |
| Abandoned Call Wait Time | For IVR-based progressive and predictive outbound campaigns, if
                                                      							 the customer disconnects the call within the time set here, then the call is
                                                      							 classified as customer abandoned. For agent-based progressive and predictive outbound campaigns,
                                                      							 if the customer or the agent disconnects the call within the time set here,
                                                      							 then the call is classified as customer abandoned. This is a mandatory field. Default value = 2 seconds, Range = 1 to 10 seconds. |
| Retries (displayed if you
                                                         								have selected IVR-based or Agent-based campaign types): Set the value for
                                                      							 the following four fields as “0” if you want to disable retry option for an
                                                      							 existing IVR or agent based outbound campaign. Note The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. | Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. |
| Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. |
| No
                                                      							 Answer Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a no-answer call. Default value = 60 minutes. Though the default value is 60 minutes, the retry attempt will
                                                      							 not be made after 60 minutes. This is based on the value set for the Callback
                                                      							 Time Limit configured in the subsystem. For example, if a callback was
                                                      							 scheduled for 9:30 am and if the Callback Time Limit is set to 15 minutes, then
                                                      							 the Outbound subsystem calls the customer anytime between 9:15 am to 9:45 am. Note The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. | Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. |
| Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. |
| Busy Signal Delay | The time duration (in minutes) for which the dialer waits before
                                                      							 calling back a busy telephone number. Default value = 60 minutes. This parameter is also based on the value set for the
                                                      							 Callback Time Limit as described above in the No Answer Delay. |
| Customer Abandoned Delay | For IVR-based progressive and predictive outbound campaigns, if a customer abandons a call, the time duration (in minutes)
                                                            after which the dialer should call the customer back. For agent-based progressive and predictive outbound campaigns, if a customer or an agent abandons a call, the time duration
                                                            (in minutes) after which the dialer should call the customer back. Default value = 0 |
| Dialer Abandoned Delay | If
                                                      							 the dialer abandons a call, the time duration (in minutes) after which the
                                                      							 dialer should call back the customer. Default value = 0 |

| Note | This field is not available if you have selected the direct preview dialer type for an agent based campaign. |
|---|---|

| Note | This field is not applicable if you have selected the Direct
                                                                        									 Preview dialer type for an agent-based campaign. If the agent is available to handle the call and if Unified CCX
                                                                        									 fails to transfer the call to the agent, then the call is dropped and will not
                                                                        									 be transferred to the IVR port. |
|---|---|

| Note | For agent selection, the CSQs are used in the order in which
                                                                        									 they are assigned to the campaign. CSQs that are associated with agent-based progressive or
                                                                        									 predictive campaigns cannot be shared across any other campaigns. CSQs that are associated with direct preview campaigns can be
                                                                        									 shared only across other direct preview campaigns and not with agent-based
                                                                        									 progressive and predictive campaigns. |
|---|---|

| Note | Ensure that few IVR ports from the total number of licensed IVR ports are left free if you want to use the "Transfer to IVR"
                                                                  option available in the answering machine treatment and abandoned call treatment fields for agent-based progressive and predictive
                                                                  outbound campaigns. |
|---|---|

| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
|---|---|

| Note | Predictive algorithm will pick up the LPP value, when the value is updated only while the campaign is running. The updated
                                                               value will be picked when the next set of contacts are fetched for dialing. |
|---|---|

| Note | This field is not applicable if you have selected the Direct
                                                               							 Preview dialer type for an agent-based campaign. |
|---|---|

| Note | It is advisable not to change this value. |
|---|---|

| Note | It is advisable not to change this value. |
|---|---|

| Note | This field is also used to determine the reservation timeout for agent-based
                                                                  								progressive or predictive campaigns. If the agent does not receive any outbound
                                                                  								calls, then the agent continues to remains in the reserved state up to maximum
                                                                  								time duration of twice the value configured in the No Answer Ring Limit field. For example, if you have configured the value for No Answer Ring
                                                                  								Limit as 30 seconds, then the range for reservation timeout is calculated as 30
                                                                  								to 60 (30 * 2) seconds. |
|---|---|

| Note | The time duration for the below fields is calculated as the
                                                               							 value entered for each field, plus or minus the value entered for the Callback
                                                               							 Time Limit field in the Add New Campaign web page. |
|---|---|

| Note | The value set for the No Answer Delay should always be more that
                                                                  								the value set for the Callback Time Limit. |
|---|---|

| Caution | You must verify
                                       		  all the contacts against the national do_not_call list before importing them. |
|---|---|

| Note | When you import contacts that have agent extension numbers, ensure that the agents are not logged in when the campaigns are
                                             running. When you import contacts for campaign, the order of field names is as per the last selected order for that campaign. When Allow Duplicate Contacts option is not selected in both Manual and Automatic import, there could be a difference between the number of contacts imported
                                             and the number of remaining contacts. This is because many of the contacts imported could be duplicates in the database and
                                             are overwritten. When Phone 1 of a contact is dialed and the CPA marks it as Busy or Unanswered the same number is retried based on the retry
                                             count and delay configured in the campaign. When the retry count reaches the maximum value, the contact is marked as closed.
                                             The other phone number for a given contact is dialed only when the called number is classified as Modem, Fax or Invalid. Each time contacts are imported, they are appended to the existing list of contacts for the selected campaign. If the new
                                             list contains a contact with the same Phone 1 value as the Phone 1, Phone 2, or Phone 3 value, or the same Phone 2 value as
                                             the Phone 1, Phone 2, or Phone 3 value, or the same Phone 3 value as the Phone 1, Phone 2, or Phone 3 value, of an existing
                                             contact, the existing contact is overwritten with the new contact information. The call history for the contact (if any) is
                                             retained. For supervisors to Schedule Import of contacts for a campaign, you must configure the campaign to use SFTP or HTTPS. |
|---|---|

| Attention | The contacts file should be ASCII-encoded or UTF-8 encoded if it contains special characters (for example, if the contact
                                             names are in Chinese, Russian, Japanese, and so on). When you want to import multiple dialing lists, ensure that you select one dialing list at a time. The maximum limit of contacts in the contacts file is 100 thousand. The maximum limit of contacts that can be imported per campaign is determined by: Number of contacts that are already imported and yet to be dialed out. The number of contacts present in the contacts file being imported. You must not initiate the manual import of contacts and automatic import of contacts using SFTP or HTTPS at the same time.
                                             If a manual import is attempted when an automatic import is in progress, it would fail. |
|---|---|

| Attention | The contacts file should be ASCII-encoded or UTF-8 encoded if it contains special characters (for example, if the contact
                                             names are in Chinese, Russian, Japanese, and so on). The maximum limit of contacts in the contacts file is 100 thousand. The automatic import process would stop importing contacts for a campaign after the campaign has 20,000 contacts remaining
                                             (yet to be dialed out). After the contacts are dialed out, then the next scheduled import would import additional contacts. The maximum limit of contacts that can be imported per campaign is determined by: Number of contacts that are already imported and yet to be dialed out. The number of contacts present in the contacts file being imported. For example: Assume a new campaign and a contacts file has 100 thousand contacts that are scheduled for import. When the import
                                                   is attempted for the first time, the first 20,000 (from 1 to 20,000 contact) contacts are fetched and imported for the campaign. Before the next scheduled import, assume system has successfully dialed out 5000 contacts and 15000 contacts are remaining.
                                                   In this, case, when next import is attempted as per the schedule, the system would import 5000 contacts for the remaining
                                                   capacity of the campaign (20000-15000=5000 contacts). Thus, assuming that the contacts file has not changed across the imports,
                                                   the system would import the contacts from 20001 to 25000 in the contacts file. You must not initiate the manual import of contacts and automatic import of contacts using SFTP or HTTPS at the same time.
                                             If a manual import is attempted when an automatic import is in progress, it would fail. If there are multiple imports scheduled at the same time, the import of contacts happen one at a time. When an automatic import of contacts is in progress and if there is a Unified CCX Engine fail over, the import will be terminated
                                             and its status is not available on the Automatic Import Contacts page. |
|---|---|

| Step 1 | From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns . The Campaigns
                                             				web page opens, displaying the details of existing campaigns. |
|---|---|
| Step 2 | Click the
                                          			 hyperlink below the Name column for the campaign for which you want to import
                                          			 the contacts. The Campaign
                                             				Configuration web page opens for the selected campaign. |
| Step 3 | Click Import
                                             				Contacts . The Import Contacts web page opens. |
| Step 4 | To import
                                          			 contacts from a CSV or a TXT file, click the Manual
                                             				Import Contacts tab. |
| Step 5 | Navigate to
                                          			 the directory that contains the imported fields in the same
                                             				order as they appear in the text file. Specify a filename to import the
                                          			 contacts from the fields being imported. A contact list can contain up to 7 fields: Account Number - The account number of a contact. The account number can be a maximum length of 25 characters. First Name - The first name of a contact. The first name can be a maximum length of 50 characters. Last Name - The last name of a contact. The last name can be a maximum length of 50 characters. Phone1 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone1 is
                                                   mandatory and must be specified. Phone2 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone3 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Dial Time - The time to dial a number for individual contacts on the current date. The format to be used for this field is
                                                   HH:MM. For example, to specify the dialing time as 08:25 am, the dial time field value should be 08:25 and for 03:45 pm, the
                                                   dial time field value should be 15:45. This field is applicable only for Direct Preview Outbound campaigns. |
| Step 6 | Check the Allow Duplicate Contacts option, if required. Allow Duplicate Contacts A record is considered duplicate when the phone number in any of the three phone fields (Phone 1, Phone 2, and Phone 3) of
                                             the records being imported: Exists in any of the three phone fields of the other contacts being imported. Exists in any of the three phone fields of the contacts previously imported for the campaign that are dialed out since last
                                                   midnight or yet to be dialed out. If this option is not selected: The contacts identified as duplicates are not imported for the campaign. If this option is selected: The check for duplicate contacts is not performed and all contacts are imported as is. Note By
                                                         				  default this option is not selected. | Note | By
                                                         				  default this option is not selected. |
| Note | By
                                                         				  default this option is not selected. |
| Step 7 | Click Import . |

| Note | By
                                                         				  default this option is not selected. |
|---|---|

| Step 1 | From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns . The Campaigns
                                             				web page opens, displaying the details of existing campaigns. |
|---|---|
| Step 2 | Click the
                                          			 hyperlink below the Name column for the campaign for which you want to import
                                          			 the contacts. The Campaign
                                             				Configuration web page opens for the selected campaign. |
| Step 3 | Click Import
                                             				Contacts . The Import Contacts web page opens. |
| Step 4 | To
                                          			 automatically import contacts from a remote server using SFTP or HTTPS, click
                                          			 the Automatic Import Contacts tab. SFTP is the default
                                          			 option. |
| Step 5 | Select the
                                          			 server type as SFTP or HTTPS . Enter the SFTP or the HTTPS remote server
                                          			 details to import contacts from a remote server using SFTP or HTTPS
                                          			 respectively. If you select SFTP, enter the following details for the Remote SFTP Server: IP Address /FQDN—The IP address or the Fully Qualified Domain Name of the remote SFTP server. RSA Key—The RSA public key of the remote SFTP server. This is optional and is used for trust verification of the SFTP server
                                                   by the Unified CCX server. User Name—The username that is required to log in to the remote SFTP server. Password—The password that is required to log in to the remote SFTP server. CSV File Path—The CSV file path (.csv or .txt file path) to import contacts from the remote SFTP server. This is the fully
                                                   qualified file name. For example: If you select HTTPS, enter the following details for the Remote HTTPS Server: URL—The URL to access the contacts over the remote HTTPS Server. User Name—The username that is required to log in to the remote HTTPS server. Password—The password that is required to log in to the remote HTTPS server. HTTPS Certificate—The check box to confirm that: You have uploaded the HTTPS Certificate in the Unified OS Administration web interface at, Security > Certificate Management . Note This is required for trust verification of the HTTPS server by the Unified CCX server. Restarted the Cisco Tomcat and Cisco Unified CCX Engine on both the node. | Note | This is required for trust verification of the HTTPS server by the Unified CCX server. |
| Note | This is required for trust verification of the HTTPS server by the Unified CCX server. |
| Step 6 | Check the Allow Duplicate Contacts option, if required. Allow Duplicate Contacts A record is considered duplicate when the phone number in any of the three phone fields (Phone 1, Phone 2, and Phone 3) of
                                             the records being imported: Exists in any of the three phone fields of the other contacts being imported. Exists in any of the three phone fields of the contacts previously imported for the campaign that are dialed out since last
                                                   midnight or yet to be dialed out. If this option is not selected: The contacts identified as duplicates are not imported for the campaign. If this option is selected: The check for duplicate contacts is not performed and all contacts are imported as is. Note By
                                                         				  default this option is not selected. | Note | By
                                                         				  default this option is not selected. |
| Note | By
                                                         				  default this option is not selected. |
| Step 7 | Click Test
                                             				Connection to check the connectivity with the remote SFTP or HTTPS
                                          			 server. |
| Step 8 | Set the order
                                          			 of field names and a schedule to automatically import contacts in regular
                                          			 intervals. A contact list can contain up to 7 fields: Account Number - The account number of a contact. The account number can be a maximum length of 25 characters. First Name - The first name of a contact. The first name can be a maximum length of 50 characters. Last Name - The last name of a contact. The last name can be a maximum length of 50 characters. Phone1 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone1 is
                                                   mandatory and must be specified. Phone2 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Phone3 - The phone number for the contact. This field can be 28 characters long and must be a valid phone number. Dial Time - The time to dial a number for individual contacts on the current date. The format to be used for this field is
                                                   HH: MM. For example, to specify the dialing time as 08:25 am, the dial time field value should be 08:25 and for 03:45 pm,
                                                   the dial time field value should be 15:45. This field is applicable only for Direct Preview Outbound campaigns. |
| Step 9 | Set the
                                          			 Schedule for the automatic import of contacts. Select
                                                				  the date. Set the Start Time . Check
                                                				  the Repeat Every checkbox and set the reoccurrence of
                                                				  the automatic schedule. Note The
                                                               						Outbound schedule time is based on the Unified CCX server time zone. Avoid
                                                               						scheduling the import of contacts during peak hours. | Note | The
                                                               						Outbound schedule time is based on the Unified CCX server time zone. Avoid
                                                               						scheduling the import of contacts during peak hours. |
| Note | The
                                                               						Outbound schedule time is based on the Unified CCX server time zone. Avoid
                                                               						scheduling the import of contacts during peak hours. |
| Step 10 | Select Enable or Disable option for automatic schedule of import of
                                          			 contacts. |
| Step 11 | Click Save to save the configurations done for Automatic Import Contacts . |

| Note | This is required for trust verification of the HTTPS server by the Unified CCX server. |
|---|---|

| Note | By
                                                         				  default this option is not selected. |
|---|---|

| Note | The
                                                               						Outbound schedule time is based on the Unified CCX server time zone. Avoid
                                                               						scheduling the import of contacts during peak hours. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Outbound > Campaigns . The Campaigns web page opens, displaying following information for
                                          				the existing campaigns: Field Description Name Name of the campaign. Start Time/End Time (hh:mm) AM PM Start Time and End Time fields indicate the time range
                                                      							 during which the campaign runs. Remaining Contacts The Remaining Contacts field indicates the number of
                                                      							 contacts that are yet to be dialed for each campaign. In addition to the
                                                      							 contacts that have not been dialed, this number also includes contacts that
                                                      							 have requested a callback and contacts that will be tried again because of
                                                      							 unsuccessful prior attempt(s) (for example, the contact was busy or unavailable). A
                                                      							 detailed breakdown of the pending contacts is provided in the Printable Reports
                                                      							 page for each campaign. Enabled The Enabled field indicates to the Outbound subsystem
                                                      							 whether this campaign is currently active. Campaign Type Denotes whether a specific campaign is IVR-based or
                                                      							 Agent-based. The existing campaigns will be marked as Agent-based after an
                                                      							 upgrade. Delete Click Delete icon next to the name of
                                                      							 the campaign that you want to delete. | Field | Description | Name | Name of the campaign. | Start Time/End Time (hh:mm) AM PM | Start Time and End Time fields indicate the time range
                                                      							 during which the campaign runs. | Remaining Contacts | The Remaining Contacts field indicates the number of
                                                      							 contacts that are yet to be dialed for each campaign. In addition to the
                                                      							 contacts that have not been dialed, this number also includes contacts that
                                                      							 have requested a callback and contacts that will be tried again because of
                                                      							 unsuccessful prior attempt(s) (for example, the contact was busy or unavailable). A
                                                      							 detailed breakdown of the pending contacts is provided in the Printable Reports
                                                      							 page for each campaign. | Enabled | The Enabled field indicates to the Outbound subsystem
                                                      							 whether this campaign is currently active. | Campaign Type | Denotes whether a specific campaign is IVR-based or
                                                      							 Agent-based. The existing campaigns will be marked as Agent-based after an
                                                      							 upgrade. | Delete | Click Delete icon next to the name of
                                                      							 the campaign that you want to delete. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Name | Name of the campaign. |
| Start Time/End Time (hh:mm) AM PM | Start Time and End Time fields indicate the time range
                                                      							 during which the campaign runs. |
| Remaining Contacts | The Remaining Contacts field indicates the number of
                                                      							 contacts that are yet to be dialed for each campaign. In addition to the
                                                      							 contacts that have not been dialed, this number also includes contacts that
                                                      							 have requested a callback and contacts that will be tried again because of
                                                      							 unsuccessful prior attempt(s) (for example, the contact was busy or unavailable). A
                                                      							 detailed breakdown of the pending contacts is provided in the Printable Reports
                                                      							 page for each campaign. |
| Enabled | The Enabled field indicates to the Outbound subsystem
                                                      							 whether this campaign is currently active. |
| Campaign Type | Denotes whether a specific campaign is IVR-based or
                                                      							 Agent-based. The existing campaigns will be marked as Agent-based after an
                                                      							 upgrade. |
| Delete | Click Delete icon next to the name of
                                                      							 the campaign that you want to delete. |
| Step 2 | Verify that the Enabled field is set to TRUE and that the start and end times are specified as
                                       			 required. |

| Field | Description |
|---|---|
| Name | Name of the campaign. |
| Start Time/End Time (hh:mm) AM PM | Start Time and End Time fields indicate the time range
                                                      							 during which the campaign runs. |
| Remaining Contacts | The Remaining Contacts field indicates the number of
                                                      							 contacts that are yet to be dialed for each campaign. In addition to the
                                                      							 contacts that have not been dialed, this number also includes contacts that
                                                      							 have requested a callback and contacts that will be tried again because of
                                                      							 unsuccessful prior attempt(s) (for example, the contact was busy or unavailable). A
                                                      							 detailed breakdown of the pending contacts is provided in the Printable Reports
                                                      							 page for each campaign. |
| Enabled | The Enabled field indicates to the Outbound subsystem
                                                      							 whether this campaign is currently active. |
| Campaign Type | Denotes whether a specific campaign is IVR-based or
                                                      							 Agent-based. The existing campaigns will be marked as Agent-based after an
                                                      							 upgrade. |
| Delete | Click Delete icon next to the name of
                                                      							 the campaign that you want to delete. |

| Caution | Area code and long
                                          			 distance prefix configuration changes made to the Outbound subsystem do not
                                          			 take effect for calls/contacts currently in the Outbound subsystem's memory.
                                          			 For example, if you change the long distance prefix or local area code, the
                                          			 contacts already in the Outbound subsystem's memory will continue to use the
                                          			 old long distance prefix and local area code. |
|---|---|

| Step 1 | From the Unified
                                       			 CCX Administration menu bar, choose Subsystems > Outbound > Area
                                             				  Codes . The Area Codes
                                          				Management web page opens. |
|---|---|
| Step 2 | In the Area Code
                                       			 field, specify a unique identifier for the area code. This field can have any
                                       			 numeric value, including 0 or leading zeros. This is a mandatory field. |
| Step 3 | Click the Add
                                          				New icon that is displayed in the tool bar in the upper, left
                                       			 corner of the window or the Add
                                          				New button that is displayed at the bottom of the window. The new Area
                                          				Code information is updated. |

| Call Status | Value (stored in database) | Description |
|---|---|---|
| Pending | 1 | The call is pending. This is the initial state for all
                                          						records. |
| Active | 2 | The record was retrieved by the Outbound subsystem for
                                          						dialing. |
| Closed | 3 | The record is closed (not dialed). |
| Callback | 4 | The record is marked for a callback. |
| Max Calls | 5 | Maximum attempts have been reached for this record
                                          						(considered closed). |
| Retry | 6 | The record is redialed immediately whenever there is any
                                          						miss in the callbacks for Retries with Delay. |
| Unknown | 7 | If the Outbound subsystem was restarted with records in the
                                          						Active (2) state, they are moved to this state. |
| Retries with Delay | 8 | The record is redialed as it was either busy, no answer,
                                          						customer abandoned or system abandoned. Retry time is set as per the
                                          						corresponding configuration in Unified CCX Application Administration web
                                          						interface. |

| Note | Outbound contacts with a call status of Unknown indicate that the these contacts were retrieved from the database but the
                                                   system went down before they could be dialed out. |
|---|---|

| Note | The
                                                         						records marked as closed today will be moved the next day at midnight. For
                                                         						example, the records closed on 4th June will be moved on 5th June at midnight. |
|---|---|

| Call
                                          						Result | Value
                                          						(stored in database) | Description |
|---|---|---|
| Voice | 1 | Customer
                                          						answered and was connected to agent. |
| Fax | 2 | Fax
                                          						machine or modem detected. |
| Answering machine | 3 | Answering machine detected. |
| Invalid | 4 | Number
                                          						reported as invalid by the network. |
| Callback | 8 | Customer
                                          						requested callback. |
| Agent
                                          						Rejected | 9 | Agent rejected the preview call. |
| Agent
                                          						Closed | 10 | Agent rejected the preview call with the close option (not dialed). |
| Busy | 11 | Busy
                                          						tone detected. |
| Ring No
                                          						Answer | 12 | Agent
                                          						did not respond to the preview call within the time out duration. Note You
                                                      						  can configure the time out duration using the Preview Call Timeout field
                                                      						  detailed in the Configure General Outbound Properties . | Note | You
                                                      						  can configure the time out duration using the Preview Call Timeout field
                                                      						  detailed in the Configure General Outbound Properties . |
| Note | You
                                                      						  can configure the time out duration using the Preview Call Timeout field
                                                      						  detailed in the Configure General Outbound Properties . |
| Callback Failed | 13 | This
                                          						value should not be written to the database; this is for internal use only. |
| Callback Missed | 14 | Callback missed and marked for Retry. |
| Timeout | 15 | Customer phone timed out either due to Ring No Answer (RNA) or
                                          						Gateway failure. |
| Call
                                          						Abandoned | 16 | Call
                                          						was abandoned because IVR port was unavailable or Unified CCX failed due to
                                          						transfer the call to the IVR port. |
| Call
                                          						Failed | 17 | Call
                                          						failed due any one of the following reasons: Dialer asked the Gateway to cancel a call that has not yet been placed Gateway has declined the call Gateway is down or Gateway has timed out while placing the call Gateway failure or configuration issues at the Gateway . |
| Customer Abandoned | 18 | Customer abandoned as customer disconnected the call within the
                                          						time limit as configured in "Abandoned Call Wait Time" in Unified CCX Application
                                          						Administration web interface. |

| Note | You
                                                      						  can configure the time out duration using the Preview Call Timeout field
                                                      						  detailed in the Configure General Outbound Properties . |
|---|---|

| Call Result | Call Status | Behavior |
|---|---|---|
| Voice (1) | Closed (3) | This contact is not dialed again. |
| Fax (2) | Retry (6) | This contact is retried, using a different phone number provided for this contact. If alternate phone numbers are not available,
                                          the call status is closed. |
| Answering machine (3) | Retry (6) | This contact is retried, with the same phone number as before. |
| Invalid Number (4) | Retry (6) | This contact is retried, using a different phone number provided for this contact. If alternate phone numbers are not available,
                                          the call status is closed. |
| Busy | Retry (6) | This contact is retried, with the same phone number as before. |

| Note | The Call Retrieval Priority is on a per campaign basis. If an agent is part of multiple CSQs that are part of different campaigns,
                                          priority of callbacks may be overridden by different queues. For example, Priority 4 in a particular queue may take precedence
                                          over Priority 1 of another queue. |
|---|---|