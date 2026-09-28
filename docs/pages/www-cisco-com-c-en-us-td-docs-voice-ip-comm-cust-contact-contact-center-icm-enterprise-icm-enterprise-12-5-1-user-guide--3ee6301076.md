---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-user-guide--3ee6301076
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/user/guide/ucce_b_reporting-concepts-for-cisco-unified12_5/ucce_b_reporting-concepts-for-cisco-unified12_5_chapter_010100.html
retrieved_at: 2026-08-22T00:03:45.535851+00:00
---

Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Reporting Concepts for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Reporting in Contact Center Gateway Deployment

## Chapter: Reporting in Contact Center Gateway Deployment

# Reporting in Contact Center Gateway Deployment

## Parent/Child Reporting

This section provides information to help you
                              understand the differences between reporting on the parent and reporting on the
                              child.

Whenever possible, report at
                                 the source ; that is, at the call site where the activity is
                              happening and where the data is generated. Use site (child) reporting for ACD
                              activities such as agent-level reporting. Use parent reporting for cross-site,
                              enterprise level reporting.

Things to keep in mind:

Agent Level
                                       Reporting . To scale the parent optimally across the enterprise,
                                    disable agent-level reporting at the parent. Agent-level reporting is always
                                    enabled at the child.

Agent level reporting can be enabled at the parent but increases the load on the PG and the Central Controller and limits
                                    the total number of agents in Unified CCE to around 8,000 for all PGs.

Call Types . Call Types at the child
                                    are mapped to Services at the parent. Do not have call types that span
                                    peripherals at a child site that has more than a single System PG. Doing so causes
                                    service counts on the parent to be different than Call Type reports on the
                                    child. Use unique call types per system PG where possible.

Configuration is simplified by
                                    autoconfiguration.

Enterprise Queue Time . The EnterpriseQueueTime field in the child Termination_Call_Detail table reflects the duration for which a call was queued
                                    at the parent. This field is not available to child scripts and is not used in any other calculation at the child or in any
                                    of the standard reports. However, users who look at this field in the database have a improved idea for the Customer Experience
                                    as to queue time.

Multichannel . The reporting data collected is voice only
                                    (no enterprise-wide multichannel). Both the parent and the child can use
                                    multichannel independently. The parent and child cannot use each other's
                                    resources.

Network consultative transfer is not possible in a parent/child deployment.

Outbound . There is no enterprise-wide Outbound Option
                                    reporting in a parent/child environment. Both the parent and the child can use
                                    Outbound Option independently. The parent and child cannot use each other's
                                    resources.

Scripting is consistent with traditional PGs, not Unified CCE . Scripts use Longest Available Agent (LAA) and Minimum Expected Delay (MED) and target services and skill groups, not agents.

RONA and RNA . Redirect on No
                                    Answer (RONA) is defined and Ring No Answer (RNA) is handled at the ACD level
                                    (at the child).

RNA is defined as Ring No Answer handled by Unified CVP,
                                          generally at the parent or enterprise level and allows enterprise-wide
                                          consideration when a ring no answer event occurs. RNA is possible only when
                                          queuing is done with Unified CVP at the parent.

RONA allows consideration of resources only at the site (unless the call
                                          is post-routed to the parent, in which case the parent is unaware of the ring
                                          no answer condition).

Do not use both child RONA and parent RNA. Pick one or the other and be consistent. RNA is required when Unified CVP is the
                                          enterprise routing platform.

RNA handling
                                       when a call is redirected . If a call is queued at the parent Unified
                                    CVP and translation-routed to the child and is later pulled back by the parent
                                    CVP and sent to another child or to the same child, when the original child requeries the call, then the parent sends RNA
                                    information to the original
                                    child as a TCD record that shows the  appropriate disposition (Redirected)
                                    and not the disposition of Abandoned.

Routing

Avoid sending calls from one child to another without parent
                                          involvement. Cradle-to-grave tracking is lost if you do
                                          this.

Do not bounce calls. That is, do not
                                          queue the call locally at the child and periodically post-route the call to the
                                          parent to check if another resource is available. Leave the call queued at the
                                          parent or at the child.

Use translation
                                          routes to all children. This allows parent-to-child call data exchange and
                                          cradle-to-grave reporting.

All general ACD functionality is supported: pre-routing, re-routing with translation routing, and post-routing. Third-party
                                          call control on the parent is the exception.

Routing to the child is to
                                          peripheral targets (skill groups, service), as for all legacy PGs.

The child can send remote route requests to
                                          the parent for post routes and translation routes, provided that Permit
                                          Application Routing is checked on the Dialed Number. Remote routing takes
                                          priority over local routing if the parent exists, is connected, and the PG
                                          registers for control. This prioritizing allows backup local scripts to take over if the
                                          parent is unavailable.

Queuing

If queuing is done at the parent, the child call center does
                                          not have access to the queue time for some calculations such as Average Handle Time (AHT).

CTI clients connect to the child's CTI and
                                          do not see calls queued by the parent; for example, with Unified
                                          CVP.

Supervisors and
                                       supervisory activity and statistics are not reported at the parent.
                                    The parent is aware of the activities but does not know the reason for them;
                                    for example, an intercept is seen as a transfer.

Third-party call control . There is no third-party call
                                    control through CTI. Agent desktops are connected to the child
                                    only.

Unified CVP at the child is
                                    supported but is discouraged, as no queuing statistics are reported, since
                                    Unified CVP is on a peripheral other than the System PG.

Variables . Full variable passing is done between parent
                                    and child. You can send/receive call variables 1–10 and ECC variables.
                                    Filtering is available to control data passing in each direction if
                                    necessary.

VRU call events are not
                                    reported at the parent and do not appear in parent reports.

### Differences Between Unified ICM Parent and Unified CCE Child Reporting

If
                                 you compare data at the parent with data at the child over intervals, you are
                                 likely to find differences. This section lists some reasons why data collected
                                 and presented in reports run at the parent can differ from data collected and
                                 presented in reports run at the child:

Differences due to transmission delays can cause
                                       variations between reporting data seen on reports run at the parent and at the
                                       child. All times computed on the parent, such as various state transitions, are
                                       based upon event arrival time in the parent, not on their actual event
                                       occurrence on the child.

Differences based on
                                          Central Controller Time or ACD Time . Prior to this
                                       release, call type data was written to Call Type tables on Central Controller
                                       time. Other data (service, skill group, agent) was written to the respective
                                       tables based on Peripheral time.

You can
                                       configure reporting intervals on either Central Controller time or on ACD
                                       (Peripheral) Time.

To continue with existing parent/child
                                       behavior, select ACD (Peripheral) Time. With this selection, Call Type/Skill
                                       Group data at the parent might not be consistent with itself. However, Skill
                                       Group counts at the parent and the child should match.

If your
                                       selection is Central Controller time, then the Call_Type/Skill_Group data at
                                       the parent should match. However, Skill Group counts at the parent and at the
                                       child might not match as they might no longer be synchronized.

Differences in supported concepts at the parent and
                                          child can cause variations. Certain concepts are supported only at the
                                       parent or only at the child. Therefore, certain agent performance and customer
                                       experience statistics might only be available at the parent or at the child.
                                       For example, Skill Group Service Levels are supported on the child but not the
                                       parent.

Differences in implementation of similar
                                          concepts in the parent and child . For example, to measure the Service
                                       Level experienced by incoming callers, reporting users at the parent would use
                                       Service Level statistics on Service Reports, while reporting users at
                                       the child would use Service Level statistics on Call Type Reports.

Differences in configuration of parent and child
                                          systems . Although autoconfiguration minimizes this issue,
                                       discrepancies between child and parent configurations can lead to reporting
                                       differences.

The
                                       following are some examples:

Short
                                                Calls :

Abandoned Short Calls : For
                                             call types and services, you configure only abandoned short calls. Answered
                                             short calls are not reported for call types and services. On the parent, if the "Abandon Wait Time threshold" for services is not configured to be the same as
                                             the Aban Wait Time threshold in the global settings for Call Types on the child
                                             system, discrepancies can arise between abandon counts on the two systems. A
                                             call might be considered as abandoned on the parent and as a Short Call on the
                                             child and vice versa.

Answered Short Calls : Answered short calls can also cause a difference in reporting. Answered short calls apply to the skill group and the agent
                                             skill group database tables. The short call timer starts when the agent answers the call. CallsAnswered is updated for these
                                             calls. However, the ShortCalls fields within the skill group and agent skill group tables are also incremented. Ensure that
                                             the "Answered Short Call threshold" configured on the Contact Center Gateway Peripheral on the parent matches the "Answered Short Call threshold" configured on the System peripheral configured on the child.

Agent Reporting :
                                             If you decide to use the parent system to report on agents, consider the
                                             following configurations.

Ensure that you enable the Agent reporting on the Contact Center Gateway peripheral on the parent and identify the Administration
                                             & Data Server on the Agent Distribution list when configuring the Unified CCE Enterprise Gateway peripheral. If these configurations are not done, then reporting on the parent system does not show any
                                             agent data.

If you plan to use Agent Team reports, configure
                                             Agent Teams and the Agent Team Members on the parent to match those on the
                                             child systems.

If you plan to report on Not Ready reason
                                                codes on the parent system, configure the following on parent:

Configure the Not Ready reason codes by entering numeric and
                                                   text values for each reason code. For example, if you want Not Ready reason code
                                                   1 to equal "Break" , enter "1" for the Reason Code and "Break" for Reason Code Text.
                                                   These codes need to match and must be identical as configured on the child
                                                   system.

Ensure that agent event detail is enabled on the Unified CCE Enterprise Gateway PG that is configured to talk to the Unified CCE System PG on the child.

Mapping of Call Types and
                                                Services : The Call Types on the child are autoconfigured as Services
                                             on the parent. However Call Types are not specific to peripherals, whereas,
                                             Services are.

If you have a child that has two or more Unified CCE System PGs, ensure that you have not configured call types that span these two peripherals. If you configure a Call Type
                                             that spans peripherals on the child, these are configured as two services on the parent system, one for each peripheral. Hence,
                                             a single call type on the child maps to two different Services (on two different peripherals) on the parent, resulting in
                                             reporting differences.

### Reporting Applications in a Parent/Child Environment

Unified Intelligence Center provides real-time and historical reports for agents, skill groups, services, and call types.
                                 These reports can be used to manage agents, measure customer experience, and monitor call center operations.

To run enterprise-wide reports at the parent , always select the ICM Templates check box in each report category. Leave the Unified CCE Templates check box unchecked.

To run reports at the parent to measure customer experience, use "ICM Templates" in the Services category.

To run reports at the child to measure customer experience, use " Unified CCE Templates" in the Call Type category.

Unified IC does not distinguish between ICM Templates and Unified CCE Templates.

### Parent/Child Deployment Models

The following table provides a brief outline of reporting on the
                                 		  parent and child systems for two common parent/child deployment models.

Deployment Model

Parent Reporting

Child Reporting

Caveats

One parent with one or more children, each with a System PG

The parent has its own reporting components: an Historical Data Server, an Administrative & Data Server, and a Unified Intelligence
                                             Center reporting application

Unified Intelligence Center does not distinguish between ICM and Unified CCE templates.

Each child system has its own individual reporting components: an Historical Data Server, an Administrative & Data Server,
                                             and a Unified Intelligence Center reporting application.

Unified Intelligence Center does not distinguish between ICM and Unified CCE templates.

Reports do not reflect Outbound Dialer Campaign or Dialer
                                             					 statistics that are reported on the child.

The Agent and Skill Group reports on the parent do not reflect
                                             					 reporting statistics for the Outbound Option dialer and Multimedia (email, and chat) tasks that are handled by agents
                                             in the child.

Multiple parents connected to a single child system through individual System PGs; for example, multiple Outsourcers sending
                                             calls from their parent to a single child (Provider).

Each parent has its own reporting components. For example,
                                             					 each Outsourcer has its own individual parent with its own Unified IC reporting
                                             					 application.

Each parent can see only reporting information that is associated with its own Unified CCE Enterprise Gateway PG.

The receiving child ( Unified CCE ) system has an Historical Data Server, an Administrative & Data Server, and a Unified IC reporting application and provides
                                             reporting on agent performance and customer experience on calls routed to the Unified CCE child from multiple Unified CCE parents.

In this deployment the child Unified CCE System has two peripherals (System PGs) each talking to different Unified CCE parents.

### Autoconfiguration from Child to Parent

The PG
                                 supports autoconfiguration of basic configuration data from the child to
                                 populate tables on the parent. Autoconfiguration is enabled by default in the
                                 Peripheral tab of the PG Explorer and takes effect when the PG is
                                 started.

Once initial autoconfiguration is complete and
                                 configuration rules are updated, additional changes on the child are sent up
                                 to, and are applied dynamically to, the parent. During subsequent connections,
                                 configuration keys are checked so that only changes are updated.

When records are deleted on the child, they are marked as "deletable" on
                                 the parent but are not actually deleted.

Do
                                 not confuse Cisco Contact
                                 Center Gateway peripheral autoconfiguration with agent
                                 autoconfiguration.

Peripheral autoconfiguration is a
                                       check box on the main Peripheral tab. It is greyed out for all but the gateway
                                       PGs.

Agent autoconfiguration is a check box option
                                       available on the Advanced tab in the PG Explorer.

You must ensure that Agent autoconfiguration is disabled so that the Unified CCE Gateway PG can function properly using Peripheral auto-configuration.

These are the tables on the parent that receive configuration
                                 data from the child:

Agent/Person

Skill Group

Service ( Call Types on the child are configured as Services on the parent.)

Peripheral
                                          Monitor

If any error occurs during autoconfiguration, the keys on the parent are not updated. The Unified CCE PIM continues to upload the entire child configuration to compare it every time it is started until no configuration errors
                                 are encountered.

Autoconfiguration does not provide complete configuration for Unified CCE software. You must configure some elements manually at the parent, such as:

Dialed numbers

Scripts

Peripheral targets

Routes

Agent
                                       desk settings

Agent teams

Supervisors

Service members

To configure service members for any given service, examine the script for a call type on the child and note to what skill
                                       groups the script offers the call. On the Unified CCE parent, make these skill groups service members of that Service.

#### Naming Conventions
                              	 for Mapping on the Parent

Mapping is the method
                                 		that Contact Center Gateway uses to manage data that the child system delivers
                                 		to a parent system during the autoconfiguration process.

Unified CCE uses naming conventions to assist users in tracking data mapping between parent and child systems.

Limit the number of characters in the names of agents, skill groups, and call types on the child system. When these names
                                 are passed to the parent during autoconfiguration, the software configures the name as (Parent)Peripheral.EnterpriseName +"."+ (Child)Skill_Group.PeripheralName . If the configured name exceeds 32 characters, it is automatically truncated, and the name of the skill group, agent, or call type on the child is replaced with a number on the parent. This means that you cannot find the name in reports run on the Unified CCE system.

The following list
                                 		provides the mapping naming convention syntax descriptions for each data entity
                                 		and uses the example of a Peripheral.EnterpriseName value of CCE1:

Skill Group

Default syntax
                                       			 (under 32 characters): (Parent)Peripheral.EnterpriseName+"."
                                       			 +(Child)Skill_Group.PeripheralName

Example:
                                       			 CCE1.Sales

Fallback syntax
                                       			 (over 32 characters): (Parent)Peripheral.EnterpriseName+"."
                                       			 +(Child)Skill_Group.PeripheralNumber

Example: CCE1.5001

Service

Default syntax:
                                       			 (Parent)Peripheral.EnterpriseName+"."+ (Child)Call_Type.Name

Example:
                                       			 CCE1.TECH_SUPPORT_CT

Fallback syntax:
                                       			 (Parent)Peripheral.EnterpriseName+"."+ (Child)Call_Type.CallTypeID

Example: CCE1.5009

Agent

Default syntax:
                                       			 (Parent)Peripheral.EnterpriseName+"."+ (Child)Agent.LastName + "."+
                                       			 (Child)Agent.FirstName

Example:
                                       			 CCE1.Smith.Jane

Fallback syntax:
                                       			 (Parent)Peripheral.EnterpriseName+"."+ (Child)Agent.PeripheralNumber

Example: CCE1.5011

## Call Types on Child Maps to Services on Parent

Most data
                              entities on a child map to corresponding entities on the parent and are mapped
                              by their corresponding peripheral fields. However, there is one important
                              exception: for reporting purposes, Call Types on the child
                              map to Services on the parent. That is, when
                              autoconfiguration occurs, data from the Call Type tables on the child populate the Service tables on the parent.

### Call Type and Service Differences for Parent and Child

On both the parent and the child, Call Type is the
                                 first-level category by which data is determined about the contact and a script
                                 is associated with the Call Type. On the child, when a contact of a certain
                                 Call Type is received, the associated script runs to determine the appropriate
                                 Skill Group to route the call to. However, on the parent, when a contact of a
                                 certain Call Type is received, the associated script runs to determine the
                                 appropriate Service to which to route the call.

### Similar Data Concepts in Child Call Type and Parent Service Database Tables

This section
                                 describes the relationship between customer experience data available at the
                                 parent and at the child.

At the child, service level data is
                                 collected and presented in Call Type and Skill Group database tables and
                                 reports.

At the parent, service level data is collected and
                                 reported only in Service database tables and reports.

In addition to these differences, in a Unified CCE child , you can also use scripting to change call types in order to capture certain statistics. In such scripts, when a call changes
                                 call types, the old call type Service Level timer stops and the Service Level timer associated with the new call type starts.
                                 However, the Service Level timer for Services on the Unified CCE parent is not stopped and reset.

Due to this
                                                   timing issue, do not compare ServiceLevel field values in
                                                   Call_Type_Interval/Real_Time tables on the child with the ServiceLevel field
                                                   values in Service_Interval/Real_Time tables at the parent.

"Similar
                                                      concept" in this discussion means "closest in meaning" ; it does
                                                   not imply an absolute match.

The
                                 data collected and presented in Service database tables and Services reports at
                                 the parent is expected to vary from data collected and presented on Call Type
                                 database tables and Call Type reports on the child. Although the two data sets
                                 are not expected to be an exact match, in some cases, the customer can look at
                                 a specific data field in the Services table at the parent and see a
                                 corresponding data field in Call Type table in the child that is similar in
                                 meaning.

Data fields that are not listed in these tables either cannot be mapped (that is, although they might be populated on a parent
                                                   system, they have no corresponding value on the child system) or are not available (that is, they are null or zero on the
                                                   parent.)

There are no corresponding fields or tables in the child for the parent Service_Five_Minute table.

Parent: Service_Interval

Child:
                                             Call_Type_Interval

Comments

AnswerWaitTime

AnswerWaitTime

AvgDelayQ

AvgRouterDelayQ

Network queuing data is not available at the child
                                             level.

CallsAnswered

CallsAnswered

CallsHandled

CallsHandled

CallsOffered

CallsOffered

DelayQAbandTime

DelayQAbandTimeHalf

See Note 1.

HandleTime

HandleTimeHalf

HoldTime

HoldTimeToHalf

OverflowOut

OverflowOutHalf

SkillTargetID

No direct
                                             map

The PeripheralNumber of this service in the
                                             Service table maps to the CallTypeID in the child table.

TalkTime

TalkTimeHalf

TimeZone

TimeZone

Note
                                    1: Any condition on the child causing the call to terminate while in
                                 queue is documented in this field in the database schema. (The child Call Type
                                 reports have more granularity with regard to "error" calls.)

Parent: Service_Real_Time

Child:
                                             Call_Type_Real_Time

Comments

AnswerWaitTimeHalf

AnswerWaitTimeHalf

AnswerWaitTimeTo5

AnswerWaitTimeTo5

AnswerWaitTimeToday

AnswerWaitTimeToday

AvgDelayQATo5

AvgRouterDelayQTo5

See Note 1.

AvgDelayQNow

AvgRouterDelayQNow

CallsAbandQHalf

RouterCallsAbandQToHalf

See Note 1.

CallsAbandQTo5

RouterCallsAbandQTo5

See Note 1.

CallsAbandQToday

RouterCallsAbandQToday

See Note 1.

CallsAnsweredHalf

CallsAnsweredHalf

CallsAnsweredTo5

CallsAnsweredTo5

CallsAnsweredToday

CallsAnsweredToday

CallsHandledHalf

CallsHandledHalf

CallsHandledTo5

CallshandledTo5

CallsHandledToday

CallsHandledToday

CallsOfferedHalf

CallsOfferedHalf

CallsOfferedTo5

CallsOfferedTo5

CallsOfferedToday

CallsOfferedToday

DelayQAbandTimeTo5

DelayQAbandTimeTo5

See Note 1.

HandleTimeHalf

HandleTimeHalf

HandleTimeTo5

HandleTimeTo5

HandleTimeToday

HandleTimeToday

HoldTimeHalf

HoldTimeHalf

HoldTimeTo5

HoldTimeTo5

HoldTimeToday

HoldTimeToday

RedirectNoAnsCallsHalf

CallsRONAHalf

RedirectNoAnsCallsTo5

CallsRONATo5

RedirectNoAnsCallsToday

CallsRONAToday

TalkTimeHalf

TalkTimeHalf

TalkTimeTo5

TalkTimeTo5

TalkTimeToday

TalkTimeToday

Note
                                    1: Any condition on the child causing the call to terminate while in
                                 queue is documented in this field in the database schema. (The child Call Type
                                 reports have more granularity with regard to "error" calls.)

#### Mapping Data Between Child and Parent

When the child maps a Call Type to a parent Service, the following
                                 		attributes are passed from the Call_Type table to the Service table:

The CallTypeID in the Call_Type table on the child system maps to
                                       			 the PeripheralNumber in the Service table on the parent.

The EnterpriseName in the Call_Type table on the child maps to the
                                       			 PeripheralName in the Service table on the parent.

You can use this mapping process to locate the corresponding Service
                                 		records on the parent for a call type record on the child.

In the figure:

On the child, the record in the Call_Type_Interval table you are
                                       			 interested in has a CallTypeID value of 5000.

On the parent, you would search the Service table for a Service with
                                       			 a PeripheralNumber field that matches the CallTypeID on the child (5000).

The SkillTargetID for that Service is 6000.

Using the SkillTargetID value (6000), look up the corresponding
                                       			 record in any of the Service Tables (for example, Service_Interval,
                                       			 Service_Real_Time).

| Note | Both Parent
                                             and Child must be at the same Release. |
|---|---|

| Note | Both Parent and Child must be
                                             at the same Release. |
|---|---|

| Note | Both
                                                parent and child must be at the same Release. |
|---|---|

| Deployment Model | Parent Reporting | Child Reporting | Caveats |
|---|---|---|---|
| One parent with one or more children, each with a System PG Note The parent treats each child as a separate ACD. | Note | The parent treats each child as a separate ACD. | The parent has its own reporting components: an Historical Data Server, an Administrative & Data Server, and a Unified Intelligence
                                             Center reporting application Unified Intelligence Center does not distinguish between ICM and Unified CCE templates. | Each child system has its own individual reporting components: an Historical Data Server, an Administrative & Data Server,
                                             and a Unified Intelligence Center reporting application. Unified Intelligence Center does not distinguish between ICM and Unified CCE templates. | Reports do not reflect Outbound Dialer Campaign or Dialer
                                             					 statistics that are reported on the child. The Agent and Skill Group reports on the parent do not reflect
                                             					 reporting statistics for the Outbound Option dialer and Multimedia (email, and chat) tasks that are handled by agents
                                             in the child. |
| Note | The parent treats each child as a separate ACD. |
| Multiple parents connected to a single child system through individual System PGs; for example, multiple Outsourcers sending
                                             calls from their parent to a single child (Provider). | Each parent has its own reporting components. For example,
                                             					 each Outsourcer has its own individual parent with its own Unified IC reporting
                                             					 application. Each parent can see only reporting information that is associated with its own Unified CCE Enterprise Gateway PG. | The receiving child ( Unified CCE ) system has an Historical Data Server, an Administrative & Data Server, and a Unified IC reporting application and provides
                                             reporting on agent performance and customer experience on calls routed to the Unified CCE child from multiple Unified CCE parents. | In this deployment the child Unified CCE System has two peripherals (System PGs) each talking to different Unified CCE parents. Note The child must not set up call types that span the two
                                                      					 peripherals. | Note | The child must not set up call types that span the two
                                                      					 peripherals. |
| Note | The child must not set up call types that span the two
                                                      					 peripherals. |

| Note | The parent treats each child as a separate ACD. |
|---|---|

| Note | The child must not set up call types that span the two
                                                      					 peripherals. |
|---|---|

| Note | With autoconfiguration on, you
                                          cannot alter any of the active configuration on the parent. |
|---|---|

| Note | Default skill groups on the
                                                child, which are non-viewable, are created as real skill groups on the parent.
                                                Activity done in the default skill group on the child shows up in these real
                                                skill groups on the parent. |
|---|---|

| Note | Duplicates are
                                                			 avoided by a suffixed numeral. If a child has two agents with identical names,
                                                			 differentiated enterprise names are generated. (Example: CCE1.Jones.John and
                                                			 CCE1.Jones.John.1) |
|---|---|

| Note | In Parent/Child deployment type, the agent name is automatically configured for the customer. Spaces are not allowed in agent
                                          IDs. In a specific scenario, if a child agent is created with a space or a "-", in either the First Name or Last Name field,
                                          the name are not created on the parents. |
|---|---|

| Note | The parent continues to process the Call Type data it owns using
                                       the "traditional" method, that is, by populating the Call Type tables with Call
                                       Types configured on the parent. |
|---|---|

| Note | This diagram does not show
                                          translation routing. |
|---|---|

| Note | Due to this
                                                   timing issue, do not compare ServiceLevel field values in
                                                   Call_Type_Interval/Real_Time tables on the child with the ServiceLevel field
                                                   values in Service_Interval/Real_Time tables at the parent. "Similar
                                                      concept" in this discussion means "closest in meaning" ; it does
                                                   not imply an absolute match. |
|---|---|

| Note | Data fields that are not listed in these tables either cannot be mapped (that is, although they might be populated on a parent
                                                   system, they have no corresponding value on the child system) or are not available (that is, they are null or zero on the
                                                   parent.) There are no corresponding fields or tables in the child for the parent Service_Five_Minute table. |
|---|---|

| Parent: Service_Interval | Child:
                                             Call_Type_Interval | Comments |
|---|---|---|
| AnswerWaitTime | AnswerWaitTime |  |
| AvgDelayQ | AvgRouterDelayQ | Network queuing data is not available at the child
                                             level. |
| CallsAnswered | CallsAnswered |  |
| CallsHandled | CallsHandled |  |
| CallsOffered | CallsOffered |  |
| DelayQAbandTime | DelayQAbandTimeHalf | See Note 1. |
| HandleTime | HandleTimeHalf |  |
| HoldTime | HoldTimeToHalf |  |
| OverflowOut | OverflowOutHalf |  |
| SkillTargetID | No direct
                                             map | The PeripheralNumber of this service in the
                                             Service table maps to the CallTypeID in the child table. |
| TalkTime | TalkTimeHalf |  |
| TimeZone | TimeZone |  |

| Parent: Service_Real_Time | Child:
                                             Call_Type_Real_Time | Comments |
|---|---|---|
| AnswerWaitTimeHalf | AnswerWaitTimeHalf |  |
| AnswerWaitTimeTo5 | AnswerWaitTimeTo5 |  |
| AnswerWaitTimeToday | AnswerWaitTimeToday |  |
| AvgDelayQATo5 | AvgRouterDelayQTo5 | See Note 1. |
| AvgDelayQNow | AvgRouterDelayQNow |  |
| CallsAbandQHalf | RouterCallsAbandQToHalf | See Note 1. |
| CallsAbandQTo5 | RouterCallsAbandQTo5 | See Note 1. |
| CallsAbandQToday | RouterCallsAbandQToday | See Note 1. |
| CallsAnsweredHalf | CallsAnsweredHalf |  |
| CallsAnsweredTo5 | CallsAnsweredTo5 |  |
| CallsAnsweredToday | CallsAnsweredToday |  |
| CallsHandledHalf | CallsHandledHalf |  |
| CallsHandledTo5 | CallshandledTo5 |  |
| CallsHandledToday | CallsHandledToday |  |
| CallsOfferedHalf | CallsOfferedHalf |  |
| CallsOfferedTo5 | CallsOfferedTo5 |  |
| CallsOfferedToday | CallsOfferedToday |  |
| DelayQAbandTimeTo5 | DelayQAbandTimeTo5 | See Note 1. |
| HandleTimeHalf | HandleTimeHalf |  |
| HandleTimeTo5 | HandleTimeTo5 |  |
| HandleTimeToday | HandleTimeToday |  |
| HoldTimeHalf | HoldTimeHalf |  |
| HoldTimeTo5 | HoldTimeTo5 |  |
| HoldTimeToday | HoldTimeToday |  |
| RedirectNoAnsCallsHalf | CallsRONAHalf |  |
| RedirectNoAnsCallsTo5 | CallsRONATo5 |  |
| RedirectNoAnsCallsToday | CallsRONAToday |  |
| TalkTimeHalf | TalkTimeHalf |  |
| TalkTimeTo5 | TalkTimeTo5 |  |
| TalkTimeToday | TalkTimeToday |  |