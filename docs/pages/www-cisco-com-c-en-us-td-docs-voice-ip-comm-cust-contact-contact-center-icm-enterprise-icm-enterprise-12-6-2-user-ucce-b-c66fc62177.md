---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-ucce-b-c66fc62177
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/ucce_b_1262_outbound_options_guide/ucce_m_1262_administrative-and-supervisory-tasks.html
retrieved_at: 2026-08-16T20:32:53.546039+00:00
---

Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

# Outbound Option Guide for Unified Contact Center Enterprise, Release 12.6(2)

Updated: August 19, 2025

Chapter: Administrative and Supervisory Tasks

## Chapter: Administrative and Supervisory Tasks

# Administrative and Supervisory Tasks

## Agent
                        	 Management

In addition to
                              		  reviewing the following sections, note that the following table lists agent
                              		  tasks and their documentation references.

Task

Where
                                          						Discussed/Notes

Adding agents

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide

Dedicating agent to Outbound Option campaigns

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide ; assign the agent only to campaign skill groups

Re-skilling agents

CCE Web
                                          						Administration Application Online Help

### Agent Addition

You assign agents to skill groups to map them to campaigns and to skill the agents for
                              multiple active campaigns.

An agent can be assigned to multiple campaigns.

### Agents Dedicated to Only Outbound Option Campaigns

There is no setting to restrict a particular agent to only Outbound Option campaigns. If you want to dedicate a particular
                              agent, associate the agent only with Outbound Option campaign skill groups.

### Agent
                           	 Re-skilling

The Unified CCE Web
                                 		  Administration application allows supervisors to sign-in and change the skill
                                 		  groups for agents they manage. CCE Web Administration is a browser-based
                                 		  application for use by call-center supervisors. You can change the skill group
                                 		  designations of agents on your team and quickly view skill group members and
                                 		  details about individual agents. Changes you make to an agent’s skill group
                                 		  membership take place immediately without the need for the agent to exit and
                                 		  re-enter the system.

See the CCE Web
                                 		  Administration Application online help for information about using the agent
                                 		  re-skilling feature.

See the Administration Guide for Cisco Unified Contact Center Enterprise for detailed instructions on how to re-skill agents.

## Campaign
                        	 Management

To manage your campaigns most efficiently, use multiple query rules instead of using multiple campaigns.

### Single Campaign
                           	 Versus Multiple Campaigns

You might choose to
                                 		  run multiple campaigns because of different calling policies (for example, time
                                 		  rules) or to run different outbound modes simultaneously.

From the perspective
                                 		  of dialer port allocation, running fewer campaigns with a larger agent pool is
                                 		  more efficient. Dialer ports are allocated based on the number of agents
                                 		  assigned and the current number of lines per agent to dial. The more campaigns
                                 		  you have that are active, the more the ports are distributed across the
                                 		  campaigns, which affects overall efficiency.

Use query rules to break down a campaign into smaller requirements. These rules can be enabled based on penetration or scheduled
                                 times. Campaign reports are available on a query rule level.

In multiple campaigns, the skill groups of agents handling the calls must be the same as those of a single campaign.

### Results from
                           	 Individual Customers

After running a
                                 		  campaign, you can generate a list of customers who were reached, not reached,
                                 		  or have invalid phone numbers.

The following are options for how to receive this information from the Outbound Option solution.

#### Interpret
                              	 Information from Dialer_Detail Table

The Dialer_Detail
                                    		  table is a single table that contains the customer call results for all
                                    		  campaigns. When you view the Dialer_Detail table, note that each attempted
                                    		  Outbound Option call is recorded as an entry in the table. Each entry lists the
                                    		  number called and which numbers are invalid.

For more information, see the appendix on the Dialer Detail Table.

#### Dialing List

You can also review the Dialing List in the Campaign Manager’s
                                    private database on the Logger Side A for customer call information. However, using this source has several drawbacks
                                    when compared to the Dialer_Detail table:

You must avoid querying this table while campaigns are in progress. Excessive activity on this table slows the  performance
                                          of the real-time processes running on  Logger Side A, particularly the Campaign Manager. This can lead to interruptions in
                                          dialing and long idle
                                          times for agents.

There is a different dialing list
                                          table for every campaign query rule. You must look in multiple locations as opposed to
                                          looking in the one Dialer_Detail table.

Use the Dialer_Detail table for customer call information whenever possible.

### Management of
                           	 Campaign Manager Database Tables

The Campaign Manager tables, Dialing_List and Personal_Callback_List can grow to be large. If the database size grows too
                                 large, Campaign Manager performance can significantly slow down. To limit the size of the Outbound Option database, a stored
                                 procedure is run daily at midnight to purge records that are no longer needed.

By default, records are removed from the Personal_Callback_List table when the record's CallStatus is either C, M, or D , and the CallbackDateTime for the record is more than five days old. In the Dialing_List table, records are removed by default when CallStatusZone1 has a value of either C, M, or D , and ImportRuleDate is more than five days old.

You can change the status and age of the records to be removed by modifying the Campaign Manager registry values on the Logger
                                 machine. The registry settings are located in HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<instance name>\LoggerA\BlendedAgent\CurrentVersion
                                 in the Outbound Option registry.

To specify the
                                       				records to remove from the Personal_Callback_List table, set PersonalCallbackCallStatusToPurge and PersonalCallbackDaysToPurgeOldRecords .

PersonalCallbackCallStatusToPurge is not added by default.
                                                   				  To change the call status of the records to remove, create this registry
                                                   				  setting manually.

To specify
                                       				the records to remove from the Dialing_List table, set DialingListCallStatusToPurge and DialingListDaysToPurgeOldRecords .

DialingListCallStatusToPurge is not added by default. To change the call status of the records to remove, create this registry setting manually.

To specify the age of the records to be removed, set PersonalCallbackDaysToPurgeOldRecords or DialingListDaysToPurgeOldRecords to specify the number of days to keep the record before it is removed. For the Personal Callback list, this value is the
                                 number of days after the personal callback is scheduled (CallbackDateTime). For the Dialing List, this value is the number
                                 of days after the record is imported (ImportRuleDate). The default is 5. The valid range is 1 to 30. If the value is not set
                                 or set to 0, the automated purge is disabled.

To set the call
                                 		  status of the records to be removed, set PersonalCallbackCallStatusToPurge or DialingListCallStatusToPurge to a string containing the call status types
                                 		  to apply when purging personal callback or dialing list records. For example,
                                 		  if the string contains “C,M,F,L,I,” all records with these call statuses, that
                                 		  are also older than the number of days specified by PersonalCallbackDaysToPurgeOldRecords or DialingListDaysToPurgeOldRecords , are removed from the database.

You can specify
                                 		  the following call status values:

Value

Description

U

Unknown

F

Fax

I

Invalid
                                             						Number

O

Operator

L

Not
                                             						Allocated

X

Agent
                                             						Not Available

C

Closed

M

Max
                                             						Calls

D

Dialed

### Management of
                           	 Predictive Campaigns

The following sections
                              		provide guidelines to follow when working with predictive campaigns.

#### Initial Values for
                              	 Lines per Agent

Determining the
                                    		  initial value for the number of lines per agent is not as simple as inverting
                                    		  the hit rate. If a campaign has a 20% hit rate, you cannot assume that five
                                    		  lines per agent is the applicable initial value for the campaign if you are
                                    		  targeting a 3% abandon rate. The opportunity for abandoned calls increases
                                    		  geometrically as the lines per agent increases; therefore, set the initial
                                    		  value conservatively in the campaign configuration.

If the reports show
                                    		  that the abandon rate is below target and does not come back in line very
                                    		  quickly, modify the initial value in the campaign configuration to immediately
                                    		  correct the lines per agent being dialed.

#### End-of-Day
                              	 Calculation for Abandon Rate

It is not unusual
                                    		  for a campaign to be over the abandon rate target for any given 30 minute
                                    		  period. The dialer examines the end-of-day rate when managing the abandon rate.
                                    		  If the overall abandon rate is over target for the day, the system targets a
                                    		  lower abandon rate for remaining calls until the average abandon rate falls
                                    		  into line. This end-of-day calculation cannot work until after the campaign has
                                    		  been running for one hour. Small sample sizes due to short campaigns or
                                    		  campaigns with fewer agents might not give the dialer enough time to recover
                                    		  from an initial value that is too high.

Similarly, if the
                                    		  campaign is significantly under the target abandon rate, it might begin dialing
                                    		  more frequently with an abandon rate over target for a while to compensate in
                                    		  the abandon rate.

#### Transfer of
                              	 Answering Machine Detection Calls to Agents

When enabling the
                                    		  Transfer AMD (Answering Machine Detection) to agent option for an agent
                                    		  campaign or enabling the Transfer AMD to IVR option for an IVR campaign,
                                    		  consider the increase in calls to the target resources (agents or IVR) when
                                    		  determining the initial value. If the expectation is that the AMD rate and the
                                    		  live voice rate are over 50%, perhaps start out with an initial value of 1.1 or
                                    		  even one line per agent to stay under a 3% abandon rate.

#### Parameter
                              	 Tuning

The Voice Calls Per
                                    		  Adjustment and Gain parameters are settings in the Advanced Users configuration
                                    		  tab used to control the way the predictive dialing behaves. Do not modify the
                                    		  default values unless you understand the parameters and the possible risks
                                    		  incurred when changing the pacing.

The Voice Calls
                                          				Per Adjustment parameter is a count of the number of live voice connections
                                          				that are required to trigger a correction. (The default value is 70 voice
                                          				calls.) If the abandon rate exceeds the target by a significant margin, the
                                          				dialer can make corrections before collecting 70 calls.

The Gain
                                          				parameter controls the size of the Lines per agent corrections.

Setting the Voice
                                    		  Calls Per Adjustment parameter to a smaller setting leads to larger
                                    		  fluctuations in the measured Abandon Rate because the sample size is less
                                    		  significant. This results in less change in the Lines per agent value over
                                    		  time.

Caution

Decreasing the
                                                			 Gain while increasing the Voice Calls Per Adjustment can similarly cause too
                                                			 slow of a change to underlying changes in the hit-and-abandon-rates. A campaign
                                                			 that is reaching more than 20 live voice customers every minute (600 per half
                                                			 hour) might benefit from reducing the Gain, but a lower Gain becomes less
                                                			 effective as the number of agents in the campaign dwindles or the hit rate
                                                			 changes rapidly.

### Management of Agent
                           	 Idle Time

One of the key
                                 		  reporting metrics for administrators managing campaigns is the amount of time
                                 		  agents spend idle between calls.

There are many
                                 		  possible reasons for longer idle times, such as a combination of one or more of
                                 		  the following:

A dialing list with a low hit rate. The solution is to create an improved list.

A small agent
                                       				pool results in fewer calls, resulting in slower adjustments. One solution is
                                       				to add more agents to the pool.

Shorter average
                                       				handle times means agents become available more frequently. A shorter handle
                                       				time means that the agent idle time percentage will climb.

Not enough
                                       				dialer ports deployed or too many agents. Deploy more ports or use fewer
                                       				agents.

A large number of retry attempts at the beginning of a day when running with append imports resulting in lower hit rates.
                                       Prioritize pending over retries.

Modifying the
                                       				maximum number of attempts up or down in an active campaign. This activity can
                                       				interrupt the Campaign Manager’s processing of dialer requests for records, as
                                       				mentioned earlier in this chapter. One solution is to perform the activity
                                       				during off hours.

Running out of
                                       				records to dial. Import new records.

EnhancedPredictiveDialing , is a new
                                 				registry setting with the controlled feature. This setting is an attempt to reduce
                                 				the idle time when there is a low hit rate for voice customers, and also when
                                 				there's a long idle agent time. This change adapts to the dialing rate more
                                 				aggressively, and it may not respect the configured abandon limit. This feature is
                                 				disabled by default.

Enabling the reclassifytransferfailures registry setting reduces the agent idle time and will also improve the predictive
                                 				dialing. For more information see, Dialer Registry Settings

#### Sources of Higher
                              	 Idle Times in Reports

The following
                                    		  Outbound Option reports provide information regarding sources of higher idle
                                    		  times:

Campaign
                                          				Consolidated Reports: These reports provide a very useful overview of a
                                          				campaign by combining campaign and agent skill group statistics into a single
                                          				report. They provide average idle time, campaign hit rate, the number of agents
                                          				working on the campaign, as well as their Average Handle Time per call. Low hit
                                          				rates and low average handle times result in more work for the dialer to keep
                                          				those agents busy.

Dialer Capacity
                                          				Reports: These reports show how busy the dialers are and how much time was
                                          				spent at full capacity when the dialer was out of ports. They also provide the
                                          				average reservation call time as well as the average time each dialer port
                                          				spent contacting customers.

#### Dialer
                              	 Saturation

If both Dialers have
                                    		  relatively low idle times and high all ports busy times, then it is likely the
                                    		  Dialers have been oversubscribed. The combination of number of agents, Dialing
                                    		  List hit rate, and average handle time are likely more than the deployed number
                                    		  of ports the Dialer can handle.

To solve this
                                    		  problem, perform one of the following actions:

Reduce the
                                          				number of agents working on the campaign.

Move a campaign to a skill group on another agent PG.

Add more Dialer ports to the solution , possibly on another agent PG .

#### Few Available
                              	 Records

Call Summary Count
                                    		  reports show how many records in the aggregate campaign dialing lists have been
                                    		  closed and how many are still available to dial.

#### Retry Records in
                              	 Append Campaigns

Running campaigns with an append import and maximum number of attempts greater than one can result in a large number of retries
                                    at the beginning of the next day. As a general rule, retries usually have a lower hit rate than pending records. Longer idle
                                    times for agents might result until the first group of retries are called because retry records usually have priority over
                                    pending records by default. The number of records increase as you increase the retry time.

There are a few ways
                                    		  to manage this situation:

Shorten the
                                          				retry times to reduce the number of retries that are scheduled at the end of
                                          				the day.

Change the
                                          				Campaign Manager priority scheme so all numbers and records are tried once
                                          				before any retries are attempted. Set the PendingOverRetryEnabled registry key
                                          				to 1 in the
                                          				Campaign Manager.

Modify the
                                          				campaign import to use the Overwrite option instead of the Append option and import new records daily.

## SIP Dialer Voice
                        	 Gateway Over-capacity Errors

If your network monitoring tool receives an alarm in the SIP dialer about being over capacity, you can ignore the alarm unless
                              it becomes an ongoing issue. This section describes the source of the alarm and remedial actions associated.

If the Voice Gateway in a SIP dialer implementation is over dialed or over capacity, the SIP Dialer receives one of the following message s :

SIP 503 messages if the SIP Dialer is deployed with Voice Gateway only

SIP 502 messages if the SIP Dialer is deployed with SIP Proxy

If the percentage of SIP 502 or SIP 503 messages reaches 1% of all messages, the SIP dialer raises an alarm.

Use one of the following measures to attempt to remedy the problem if Voice Gateway capacity becomes an ongoing issue:

Check the Voice Gateway configuration. If there are errors, fix them and reset Port Throttle to its original value. Port Throttle
                                    (the calls-per-second rate at which the dialer dials outbound calls) is set on the Dialer General tab in the Configuration
                                    Manager.

Check the sizing information. Adjust the value of Port Throttle according to the documented guidelines.

Enable the auto-throttle mechanism by setting the Dialer registry setting EnableThrottleDown to 1.

To set EnableThrottleDown , open the Registry Editor (regedit.exe) on the PG machine and navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\<customerinstance>\Dialer .

The SIP dialer performs an automatic throttle down when the percentage of SIP 502 or SIP 503 messages reaches 2% of all messages, if the auto-throttle mechanism is enabled. This throttle down means that the
                              SIP dialer decreases the configured value of Port Throttle by approximately 10%.

If one throttle down does not correct the problem, the SIP dialer performs more throttle downs until either the problem is
                              corrected or the value of Port Throttle is throttled down to 50% of the originally configured value.

For each automatic throttle down, alarm and trace messages clearly provide detailed information about the adjusted port throttle
                              value, configured port throttle value, and time duration.

Even after the problem is corrected, the dialer does not automatically throttle back to the configured value. To increase
                              the throttle back to the configured value, run the updateportthrottle /portthrottle <configured value> command using the process monitoring tool Procmon.

When routing outbound calls, the Dialer will stop communicating with the SIP Gateway or Proxy for next Retry-After time, if it receives Service Unavailable SIP message (503) with a Retry-After header multiple times.

## Update the North American Numbering Plan Data

The Regional Prefix Update Tool (RPUT) is used to update the Unified CCE database to the latest North American Local Exchange NPA NXX Database (NALENND).

If Unified CCE ICM is using the North American Numbering Plan.

On an Administration & Data Server that includes Real-time Data Server as part of its role.

The RPUT is composed of the following two files (installed in the ICM\bin directory on the Unified CCE AW-HDS-DDS server):

region_prefix_data.txt (or the <DatafileName>)

Contains the data this tool uses to update the region prefix table in the Unified CCE database. Note that you should change paths to the ICM\bin directory.

regionfix.exe

This executable reads the region_prefix_data.txt data file and updates the region prefix table.

The RPUT is run from the command line as described in the following procedure.

Step 1

Open a command prompt (Select Start > Run , and enter cmd , then click OK ).

Step 2

Change the path to ICM\bin .

Step 3

Enter the following at the prompt: regionfix.exe < DatafileName > (where < DatafileName > is the name of the data file).

The Regional Prefix Update Tool then shows the version of the input data file and asks if you want to proceed. If you proceed,
                                          the tool connects to the Unified CCE database. The number of records that are to be updated, deleted, and inserted appear. These records are put into three different
                                          files:

region_prefix_update.txt (which includes preserved Custom Region Prefixes)

region_prefix_new.txt

region_prefix_delete.txt

Step 4

You can either delete or retain the entries present in the region_prefix_delete.txt file while performing the insertions and
                                       updates. To retain the entries, type No when the tool prompts you to delete the entries. Type Yes to delete the entries.

Step 5

Check the contents of the files before proceeding.

Step 6

Answer Yes to proceed with the update.

When the update is complete, the tool displays the following message:

Your region prefix table has been successfully updated.

## Reports

This section provides an overview of the Outbound Option reports available in the Cisco Unified Intelligence Center.

For complete information about using Unified Intelligence Center, how to download and import report bundles, and detailed
                           descriptions of the templates for the reports mentioned here, see Cisco Unified Contact Center Enterprise Reporting User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

### Outbound Option
                           	 Reports

This section
                                 		  describes the Outbound Option reports, created using the Unified Intelligence
                                 		  Center.

All Outbound
                                             			 Option reports are voice-only reports and can be used in Unified CCE
                                             			 environments.

The Outbound Option reports are distributed in two report bundles: Realtime Outbound and Historical Outbound. The report bundles
                                 are available as downloads from Cisco.com https://software.cisco.com/download/type.html?mdfid=282163829&catid=null . Click the Intelligence Center Reports link to view the available report bundles. Depending on how it was deployed, your
                                 installation of Unified Intelligence Center may include all or a subset of these reports.

Additionally,
                                 		  sample custom report templates are available from the Cisco Developer Network
                                 		  ( https://developer.cisco.com/web/ccr/documentation .)

For information on importing report bundles or custom reports to
                                 		  the Cisco Unified Intelligence Center, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

#### Outbound Historical Reports Bundle

The Outbound Options Historical reports receive data from the historical data source. Reports are populated with interval
                                    data that has a default refresh rate of 15 minutes.

Half-hour/Daily:
                                    				Provides statistics for each half-hour period. Many of the half-hour reports
                                    				are also available in a daily report format.

The Outbound Historical bundle contains the following reports:

Attempts per Campaign Daily

Shows the status (summary and percentage) of each campaign for the selected time period and the breakdown of attempts (in
                                             percentage) of each campaign for the selected time period.

Campaign Consolidated Daily

Shows the daily activity and performance of the selected campaigns and their skill groups for the selected time period and
                                             provides analysis of the actual customer calls (outbound calls which reached live voice, inbound calls, or calls transferred
                                             to the campaign's skill group) for the selected campaigns and their skill groups for the selected time period.

Campaign Consolidated Half Hour

Shows the list of Consolidated Calls and Agent Statistics per Campaign by Half Hour and Breakdown of completed calls.

Campaign Half Hour Summary

Shows the status for all campaigns for the selected time period, the status (summary and percentage) of each campaign for
                                             the selected time period and the breakdown of attempts (in percentage) of each campaign for the selected time period.

Dialer Call Result Summary Half Hour

Dialer Capacity Daily

Dialer Capacity Half Hour

Shows the status of each dialer for the selected time period.

Import Rule

Query Rule Within Campaign Daily

Query Rule Within Campaign Half Hour

#### Outbound Realtime Reports Bundle

The Outbound Option Real Time reports display current information about a system entity; for example, the number of tasks
                                    an agent is currently working on or the number of agents currently logged in to a skill group. By default, the reports automatically
                                    query the Admin Workstation database on the distributor every 15 seconds. The data is written to the database by the Router
                                    almost every 10 seconds.

The Outbound Real Time Reports Bundle contains the following reports:

Call Summary Count per Campaign Real Time

Shows the status of each query rule within a campaign, status of all campaign records, and the currently valid campaign dialing times.

Dialer Real Time

Shows the status of each dialer, including the number of contacts dialed today and the result of each attempt.

Import Status Real Time

Shows the status of Outbound Option import records.

Query Rule Within Campaign Real Time

Shows the status of all campaign records, dialing times, and query rule within a campaign.

#### Agent
                              	 Reports

In addition to the reports contained in the Outbound Reports bundles, other Agent reports also provide information about Outbound
                                    activities:

Agent Queue Real-Time

Agent Real-Time

Agent Skill Group Real-Time

Agent Team Real-Time

The Direction field indicates the direction of the call that the agent is currently working on including Other Out/Outbound Direct Preview,
                                                Outbound Reserve, Outbound Preview, or Outbound Predictive/Progressive.

The Destination field indicates  the type of outbound task on which the agent is
                                                currently
                                                working.

Agent Team State Counts

Agent State Real Time Graph

For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call. The Outbound Dialer puts the agent on hold while connecting
                                                the call.

Interpreting agent data for Outbound Option tasks, requires understanding how Outbound Option reserves agents, reports calls
                                    that are connected to agents, and handles calls that are dropped by customers before the calls are connected.

Outbound Option is automatically enabled at setup. It provides automatic outbound dialing capability.

The Outbound Option Dialer assigns and connects calls differently than regular contact center enterprise routing. Report data
                                    for agents handling Outbound Option calls therefore differs from data for agents handling typical voice calls and multichannel
                                    tasks.

When the Outbound Dialer calls a customer, it reserves the agent to handle the call. The Dialer places a reservation call
                                    to the agent and changes the agent's state to Hold. This reservation call is reported as a Direct In call to the agent.

For typical calls, the agent is placed into Reserved state when the contact center reserves the agent to handle a call. For
                                    Outbound Option calls, reports show the agent in Hold state when reserved for a call and the time that agent spends reserved
                                    is reported as Hold Time.

When the customer answers the call, the Outbound Option Dialer transfers the call to an agent. The call is now reported as
                                    a Transfer In call to the agent. When the customer call is transferred to the agent, the Dialer drops the reservation call
                                    and classifies it as Abandon on Hold.

The abandoned call wait time, set in the Campaign Configuration screen, determines how calls are reported if the caller ends
                                    the call. Calls are counted in the Customer Abandon field in both Real Time and Historical campaign query templates only if
                                    the customer ends the call before the abandoned call wait time is reached.

For agent reporting per campaign, Outbound Option provides reports that accurately represent the Outbound Option agent activity
                                    for a contact center, including information grouped by skill group.

The following list describes the data that are presented in the agent reports.

A real-time table that shows Outbound Option agent activity that is related to Outbound Option calls.

A historical
                                          				table that shows agent daily performance for Outbound Option predictive calls,
                                          				by skill group.

A historical
                                          				table that shows agent daily performance for Outbound Option preview calls, by
                                          				skill group.

A historical
                                          				table that shows agent daily performance for Outbound Option reservation calls,
                                          				by skill group.

#### Campaign and Dialer Reports

Outbound Option provides a campaign report template that describes the effectiveness of a campaign and the dialer. This list
                                    can be used for Agent and VRU campaigns.

Observe the
                                    		  following guidelines when using the campaign reports:

Campaign Real
                                          				Time reports describe how many records are left in the campaign dialing list.

Both Campaign and Dialer Half Hour reports provide the call result counts.

Dialer utilization fields in the Dialer Half Hour report are unaffected, although the Half Hour record might be missing if
                                          the Campaign Manager was inactive during the half-hour boundary. When the Dialer restarts, only the Dialer Utilization fields
                                          are affected; therefore, the Dialer Utilization only captures port status since the Dialer restarted during that half hour.
                                          Some records might be left in an active state for a short period of time after the Dialer or Campaign Manager restarts, but
                                          the Campaign Manager has a mechanism to reclaim those records.

When the active Campaign Manager fails over, partial campaign interval reports are generated for the relevant interval based
                                                on the data that was available after failover. Some of the campaign statistics collected prior to failover will be missing.

The campaign interval tables used in Reporting are impacted due to this scenario.

The following list
                                    		  describes the data that is presented in the campaign reports.

A summary of
                                          				call results for query rules within a campaign since the beginning of the day.

A summary of
                                          				call results for a campaign since the beginning of the day. It includes a
                                          				summary of all query rules within the campaign.

A view of what
                                          				is configured for valid campaign calling times for zone1 and zone2 for selected
                                          				campaigns. The times are relative to the customer’s time zone.

A view of what
                                          				is configured for valid campaign calling times for zone1 and zone2 for selected
                                          				campaign query rules. The zone times are relative to the customer’s time zone.
                                          				The query rule start and stop times are relative to the Central Controller
                                          				time.

How many records
                                          				for selected query rules have been dialed to completion, and how many records
                                          				remain.

How many records
                                          				for selected campaigns have been dialed to completion, and how many records
                                          				remain.

A summary of
                                          				call results for selected campaign query rules for selected half-hour
                                          				intervals.

A summary of
                                          				call results for all query rules for selected campaigns for selected half-hour
                                          				intervals.

A historical
                                          				table by half-hour/daily report that shows the status (summary and percentage)
                                          				of each campaign for the selected time period.

A historical
                                          				table by breakdown of attempts (in percentage) of each campaign for the
                                          				selected time period.

A historical
                                          				table by half-hour/daily report that shows the status (summary and percentage)
                                          				per query rule of each campaign for the selected time period.

A historical
                                          				table by breakdown of attempts (in percentage) per query rule of each campaign
                                          				for the selected time period.

A summary
                                          				half-hour/daily report that shows activity and performance of the selected
                                          				campaigns and their skill group for the selected time period, including abandon
                                          				rate, hit rate, and agent idle times.

A historical
                                          				table by breakdown of actual customer calls (outbound calls which reached live
                                          				voice, inbound calls, or calls transferred to the campaign skill group) for the
                                          				selected campaigns and their skill groups for the selected time period.

##### Dialer Reports

The Outbound Option Dialer reports provide
                                       information about the dialer. These reports include information about performance
                                       andresource usage. The templates also enable you to determine whether you need more dialer ports to support more outbound
                                       calls.

The following list describes the data presented in the Outbound Option Dialer
                                       reports:

A real-time table that shows contact, busy, voice, answering
                                             machine, and  special
                                             				information tone (SIT) detection for each dialer. A SIT consists of three rising tones indicating a call has failed.

An historical table that records
                                             contact, busy, voice, answering machine, and SIT Tone detection for each dialer by half-hour intervals.

Displays information about the amount of time the dialer was idle or had all ports busy.

Displays Dialer status on a port-by-port basis used for
                                             troubleshooting. If this report does not display any records, then the data feed
                                             is disabled by default. It is only enabled  for troubleshooting purposes.

#### Skill Group
                              	 Reports

For skill group
                                    		  reporting per campaign, Outbound Option provides reports that represent the
                                    		  skill group activity for a contact center.

The following list
                                    		  describes the data presented in the skill group reports:

A real-time
                                          				table that shows all skill groups and their associated Outbound Option status.

A historical
                                          				table that records Outbound Option counts for the agent states signed on , handle , talk , and hold by half-hour intervals.

#### Import Rule
                              	 Reports

Outbound Option
                                    		  reports also enable you to view the success of record imports. Using the
                                    		  Import Rule templates, you can monitor whether records are being added
                                    		  successfully (good records) or are failing (bad records), and how long it takes to import the records.

The same import rule
                                    		  reports are used for Do Not Call and Contact List imports. The reports display
                                    		  a historical view of when the imports were done, the number of records imported,
                                    		  and the number of records that were considered invalid because of length
                                    		  constraints or improper formatting.

For contact list
                                    		  imports, the reports also provide insight into the number of contacts that were
                                    		  assigned with the default time zone information for the campaign, as well as
                                    		  the number of contacts that were imported into the dialing list after
                                    		  the query rule and format validation was performed.

The following
                                    		  information is available in the Import Rule reports:

Number of
                                          				successful, unsuccessful, and total records imported by time range

Current import
                                          				status

A real-time
                                          				table that shows the number of successful, unsuccessful, and total records
                                          				imported or to be imported.

A historical
                                          				table that shows the number of successful, unsuccessful, and total records
                                          				imported by time range. The Total Records column indicates the total number of
                                          				records available in the import file.

Import Rule reporting data is not populated for Outbound API-based imports. However, you can get this data directly from the
                                                API.

| Task | Where
                                          						Discussed/Notes |
|---|---|
| Adding agents | Cisco Unified Contact Center Enterprise Installation and Upgrade Guide |
| Dedicating agent to Outbound Option campaigns | Cisco Unified Contact Center Enterprise Installation and Upgrade Guide ; assign the agent only to campaign skill groups |
| Re-skilling agents | CCE Web
                                          						Administration Application Online Help |

| Note | An agent can be assigned to multiple campaigns. |
|---|---|

| Note | In multiple campaigns, the skill groups of agents handling the calls must be the same as those of a single campaign. |
|---|---|

| Note | PersonalCallbackCallStatusToPurge is not added by default.
                                                   				  To change the call status of the records to remove, create this registry
                                                   				  setting manually. |
|---|---|

| Note | DialingListCallStatusToPurge is not added by default. To change the call status of the records to remove, create this registry setting manually. |
|---|---|

| Value | Description |
|---|---|
| U | Unknown |
| F | Fax |
| I | Invalid
                                             						Number |
| O | Operator |
| L | Not
                                             						Allocated |
| X | Agent
                                             						Not Available |
| C | Closed |
| M | Max
                                             						Calls |
| D | Dialed |

| Caution | Be
                                             		  careful when modifying both parameters (Gain and Voice Calls Per Adjustment) at
                                             		  the same time. For example, increasing the Gain while decreasing the Voice
                                             		  Calls Per Adjustment results in larger changes in the "Lines per agent
                                                			 correction rate," which might overcorrect changes in measured values. Decreasing the
                                                			 Gain while increasing the Voice Calls Per Adjustment can similarly cause too
                                                			 slow of a change to underlying changes in the hit-and-abandon-rates. A campaign
                                                			 that is reaching more than 20 live voice customers every minute (600 per half
                                                			 hour) might benefit from reducing the Gain, but a lower Gain becomes less
                                                			 effective as the number of agents in the campaign dwindles or the hit rate
                                                			 changes rapidly. |
|---|---|

| Note | See the appendix on Registry settings for detailed information about the PendingOverRetryEnabled registry setting. |
|---|---|

| Note | When routing outbound calls, the Dialer will stop communicating with the SIP Gateway or Proxy for next Retry-After time, if it receives Service Unavailable SIP message (503) with a Retry-After header multiple times. |
|---|---|

| Step 1 | Open a command prompt (Select Start > Run , and enter cmd , then click OK ). |
|---|---|
| Step 2 | Change the path to ICM\bin . |
| Step 3 | Enter the following at the prompt: regionfix.exe < DatafileName > (where < DatafileName > is the name of the data file). The Regional Prefix Update Tool then shows the version of the input data file and asks if you want to proceed. If you proceed,
                                          the tool connects to the Unified CCE database. The number of records that are to be updated, deleted, and inserted appear. These records are put into three different
                                          files: region_prefix_update.txt (which includes preserved Custom Region Prefixes) region_prefix_new.txt region_prefix_delete.txt |
| Step 4 | You can either delete or retain the entries present in the region_prefix_delete.txt file while performing the insertions and
                                       updates. To retain the entries, type No when the tool prompts you to delete the entries. Type Yes to delete the entries. |
| Step 5 | Check the contents of the files before proceeding. |
| Step 6 | Answer Yes to proceed with the update. When the update is complete, the tool displays the following message: Your region prefix table has been successfully updated. |

| Note | All Outbound
                                             			 Option reports are voice-only reports and can be used in Unified CCE
                                             			 environments. |
|---|---|

| Note | Call Type
                                          		  reporting can be used on Outbound Option reservation calls and transfer to VRU
                                          		  calls. Call Type reporting is not applicable for outbound customer calls
                                          		  because a routing script is not used. |
|---|---|

| Report | Description |
|---|---|
| Attempts per Campaign Daily | Shows the status (summary and percentage) of each campaign for the selected time period and the breakdown of attempts (in
                                             percentage) of each campaign for the selected time period. |
| Campaign Consolidated Daily | Shows the daily activity and performance of the selected campaigns and their skill groups for the selected time period and
                                             provides analysis of the actual customer calls (outbound calls which reached live voice, inbound calls, or calls transferred
                                             to the campaign's skill group) for the selected campaigns and their skill groups for the selected time period. |
| Campaign Consolidated Half Hour | Shows the list of Consolidated Calls and Agent Statistics per Campaign by Half Hour and Breakdown of completed calls. |
| Campaign Half Hour Summary | Shows the status for all campaigns for the selected time period, the status (summary and percentage) of each campaign for
                                             the selected time period and the breakdown of attempts (in percentage) of each campaign for the selected time period. |
| Dialer Call Result Summary Half Hour Dialer Capacity Daily Dialer Capacity Half Hour | Shows the status of each dialer for the selected time period. |
| Import Rule | Shows the status of imported records for the selected time period. |
| Query Rule Within Campaign Daily | Shows the breakdown of attempts (in percentage) of each campaign for the selected time period and the status (summary and
                                          percentage) of each campaign for the selected time period. |
| Query Rule Within Campaign Half Hour | Shows the breakdown of attempts (in percentage) of each campaign for the selected time period, the status (summary and percentage)
                                          of each campaign for the selected time period and the status for each Query rule within a campaign for the selected time interval. |

| Report | Description |
|---|---|
| Call Summary Count per Campaign Real Time | Shows the status of each query rule within a campaign, status of all campaign records, and the currently valid campaign dialing times. |
| Dialer Real Time | Shows the status of each dialer, including the number of contacts dialed today and the result of each attempt. |
| Import Status Real Time | Shows the status of Outbound Option import records. |
| Query Rule Within Campaign Real Time | Shows the status of all campaign records, dialing times, and query rule within a campaign. |

| Report | Outbound Option Fields |
|---|---|
| Agent Queue Real-Time Agent Real-Time Agent Skill Group Real-Time Agent Team Real-Time | The Direction field indicates the direction of the call that the agent is currently working on including Other Out/Outbound Direct Preview,
                                                Outbound Reserve, Outbound Preview, or Outbound Predictive/Progressive. The Destination field indicates  the type of outbound task on which the agent is
                                                currently
                                                working. |
| Agent Team State Counts | The Active Out field  
                                             shows the number of agents currently working on outbound tasks. |
| Agent State Real Time Graph | For agents handling Outbound Option calls, the Hold state indicates that the agent has been reserved for a call. The Outbound Dialer puts the agent on hold while connecting
                                                the call. |

| Note | Campaign Real
                                             		  Time reports capture call results since the last Campaign Manager restart only.
                                             		  If the Campaign Manager restarts, data collected before the restart is lost. |
|---|---|

| Note | When the active Campaign Manager fails over, partial campaign interval reports are generated for the relevant interval based
                                                on the data that was available after failover. Some of the campaign statistics collected prior to failover will be missing. The campaign interval tables used in Reporting are impacted due to this scenario. |
|---|---|

| Note | Import Rule reporting data is not populated for Outbound API-based imports. However, you can get this data directly from the
                                                API. |
|---|---|