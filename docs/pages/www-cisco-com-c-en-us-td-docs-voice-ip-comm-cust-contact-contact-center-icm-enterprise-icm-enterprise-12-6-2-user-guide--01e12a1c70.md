---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-user-guide--01e12a1c70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1262/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_010001.html
retrieved_at: 2026-08-21T12:00:38.986893+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 12.6(2)

Updated: May 4, 2023

Chapter: Contact Sharing Reports

## Chapter: Contact Sharing Reports

# Contact Sharing Reports

## Contact Sharing Reporting

You can use Contact Sharing to distribute calls to agents across multiple Unified Contact Center Enterprise (Unified CCE) systems. With Contact Sharing, you can efficiently route calls to a much larger number of agents than a standard Unified CCE system can support.

You configure Contact Sharing to make routing decisions based on the current state of the target Unified CCE systems, such as the number of calls in queue, agent availability, average handle time, and custom calculations. Using rules
                           you specify and Live Data information on the current state of the target systems, Contact Sharing decides which Unified CCE system to route the calls to.

You can use the Contact Sharing reports to understand the current configuration and  behavior of the Contact Sharing system.
                           You can view data on the active configuration of the Contact Sharing routing, the number of calls routed to each target system
                           for each group, and the calls that have errors during the routing process. In addition, you can use the Contact Sharing Results
                           Calculations report to see the change in the actual result calculated by the current Contact Sharing expression formula as
                           routing is processed.

## Contact Sharing All Fields

Use this report to view selected fields that provide Route Call Detail information for Contact Sharing calls.

Views: This report has one grid view, Contact Sharing All Fields.

Query: This report data is built from an Anonymous Block query.

Grouping: This report is grouped by Contact Share Group and Rule.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

Call_Type

Routing_Client

Script

Master_Script

### Current Fields in the Contact Sharing All Fields Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns (Fields)

Description

Group

The unique name of this Contact Share Group.

Derived from: Contact_Share_Group.EnterpriseName

Rule

The name assigned to the rule when it was created.

Derived from: Contact_Share_Rule.EnterpriseName

Rule Expression

The rule expression that the Contact Share server uses to select the skill group or precision queue from a group for a routing
                                          request.

Derived from: Contact_Share_Rule.RuleExpression

Queue

Name

The name of the queue.

Derived from: Contact_Share_Queue.QueueName

Type

Identifies the target queue as PQ (Precision Queue,) or SG (Skill Group.)

Derived from: Contact_Share_Queue.QueueType

Target

Name

The unique enterprise name for the target application gateway.

Derived from: Application_Gateway.EnterpriseName

Label

The label associated with the ultimate target at the switch.

Derived from: Route_Call_Detail.TargetLabel

Accept Queue If

The logical expression used to determine whether to include the individual skill groups and precision queues in the group
                                          for the routing decision. The contact share queue will be accepted IF the expression evaluates to true.

Derived from: Contact_Share_Group.AcceptQueueIf

DateTime

The date and time when the call was routed.

Derived from: Route_Call_Detail.DateTime

ANI

Automatic Number Identification, identifies the calling party.

Derived from: Route_Call_Detail.ANI

Dialed Number

The dialed number for the call. If the dialed number for the call is configured, this will be the same as the DialedNumberString
                                          of the dialed number specified by DialedNumberID. If the dialed number for the call is not configured, this is the dialed
                                          number string and DialedNumberID will be NULL.

Derived from: Route_Call_Detail.DialedNumberString

Call Type

The unique enterprise name for this call. If a script changes the call type, this is the final call type for the call.

Derived from: Call_Type.EnterpriseName

Routing Client

The unique enterprise name for this routing client.

Derived from: Routing_Client.EnterpriseName

Master Script

The unique enterprise name for the primary script.

Master_Script.EnterpriseName

CED

Caller-Entered Digits.

Route_Call_Detail.CED

Variables

Variable1 to Variable10

10 fields are provided for user-defined variables.

Derived from Route_Call_Detail.Variable1 to Route_Call_Detail.Variable10

## Contact Sharing Calls Routed

Use this report to view the number of calls routed to each   Gateway from the  Groups selected for the report between the
                              start time and end time specified in the report Filter.

Views: This report has a default chart view (Calls routed) and a grid view.

Query: This report data is built from an Anonymous Block query.

Grouping: This report is grouped by Contact Share Group.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

### Current Fields in the Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Fields

Description

Gateway

The unique enterprise name for the target application gateway.

Derived from: Application_Gateway.EnterpriseName

Calls

The number of calls routed to each Gateway between the start time and end time specified in the report Filter.

A count of the call completion rows in the Route_Call_Detail routed to each Gateway.

## Contact Sharing Calls Routed Realtime

Use this report to view the number of calls routed to each   Gateway in the last 60 minutes from the  Groups selected for
                              the report.

This report re-queries the database every 15 seconds and updates summary values for the last 60 minutes.

Views: This report has a default chart view (Calls Routed) and a grid view.

Query: This report data is built from an Anonymous Block query.

Grouping: This report is grouped by Gateway.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

### Current Fields in the Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Fields

Description

Target

The unique enterprise name for the target application gateway.

If any calls cannot be routed, they are displayed in the report as a separate Errors target.

Derived from: Application_Gateway.EnterpriseName

Calls

The number of calls routed to each Gateway during the last 60 minutes, updated every 15 seconds.

A count of the call completion rows in the Route_Call_Detail routed to each Gateway.

## Contact Sharing Calls Routed Over Time

Use this report to view the number of calls routed to each   target Gateway from the  Groups selected for the report during
                              the 12 hours following the StartDate specified in the report filter.

The number of calls routed to each Gateway are graphed against time in minute intervals over the 12-hour period. The number
                              of calls that could not be routed during the 12 hours are displayed as a separate Errors target.

Views: This report has the following chart views and a gird view (Grid View Routed Over Time):

Line View Routed Over Time (the default)

Column View Routed Over Time

Select the view you want to see from the report drop-down list located to the far right in the menu bar.

Query: This report data is built from an Anonymous Block query.

Grouping: This report is grouped by Gateway.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

### Current Fields in the Routed Overtime Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Fields

Description

Target

The unique enterprise name for the target application gateway.

If any calls cannot be routed, they are displayed in the report as a separate Errors target.

Derived from: Application_Gateway.EnterpriseName

DateTime

The minute interval for which the calls are being reported.

Calls

The number of calls routed to each Gateway during that minute interval.

A count of the call completion rows in the Route_Call_Detail routed to each Gateway.

## Contact Sharing Configuration

Use this report to view the Groups, Rules, Queues, and Targets associated with the Contact Share Groups selected for the report.

Views: This report has a grid view, Contact Sharing Configuration.

Query: This report data is built from a Database Query.

Grouping: This report is grouped by Contact Share Group.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Application_Gateway

### Current Fields in the Contact Sharing Configuration Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Group

The GroupIDs of the groups selected for the report.  Click '+' next to a GroupID  to see detailed infromation for that group.

Rule

The name assigned to   the rule when it was created.

Derived
                                          						from:  
                                          					 Contact_Share_Rule.EnterpriseName

Group

Description

The description of the group entered when it was configured.

Derived
                                          						from: Contact_Share_Group.Description

Rule

Description

The description of the rule entered when it was configured.

Derived
                                          						from: Contact_Share_Rule.Description

Expression

The rule expression that the Contact Share server uses to select the skill group or precision queue from a group for a routing
                                          request.

Derived
                                          						from: Contact_Share_Rule.RuleExpression

Queue

Queue

The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group.

Derived
                                          						from: Contact_Share_Queue.QueueName

Type

Identifies the target queue as P -Precision Queue, or S - Skill Group.

Derived
                                          						from: Contact_Share_Queue.QueueType

Description

The description of this queue.

Derived from: Contact_Share_Queue.Description

Target

Target

The unique enterprise name for the target application gateway.

Derived
                                          						from: Application_Gateway.EnterpriseName

Description

The
                                          						description of this target

Derived
                                          						from: Application_Gateway.Description

Preferred Side

Indicates which side of the target gateway the software should use when both are available: A or B. This applies only when
                                          Application GatewayType is 0 (custom gateway).

Derived
                                          						from: Application_Gateway.PreferredSide

Accept Queue If

The logical expression used to determine whether to include the individual skill groups and precision queues in the group
                                          for the routing decision.  The contact share queue will be accepted IF the expression evaluates to true.

Derived
                                          						from: Contact_Share_Group.AcceptQueueIf

## Contact Sharing
                        	 Errors

Use this report to
                              		  view information on calls which had errors   during the routing process. If there
                              		  are no errors, the report is empty.

Calls that end with RouterErrorCode 448, Dialog aborted and was deleted, are not included in the report. 
                                          This is not a routing error. This error means the customer leg disconnected for the
                                          call at the routing client, usually because the customer ended the call.

Views: This report has one grid view, Contact Sharing Errors.

Query: This report data
                              		  is built from an Anonymous Block query.

Grouping: This report
                              		  is grouped by Contact Share Group and Target.

Value List: Contact
                              		  Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

### Current Fields in the Contact Sharing Errors Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Group

The
                                          						unique name of this Contact Share Group.

Derived
                                          						from: Contact_Share_Group.EnterpriseName

Target

The
                                          						unique enterprise name for the target application gateway.

Derived
                                          						from: Application_Gateway.EnterpriseName

Rule

The name
                                          						assigned to the rule when it was created.

Derived
                                          						from: Contact_Share_Rule.EnterpriseName

Queue

The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group.

Derived
                                          						from: Contact_Share_Queue.QueueName

Dialed
                                          						Number String

The
                                          						dialed number for the call. If the dialed number for the call is configured,
                                          						this will be the same as the DialedNumberString of the dialed number specified
                                          						by DialedNumberID. If the dialed number for the call is not configured, this is
                                          						the dialed number string and DialedNumberID will be NULL.

Derived
                                          						from: Route_Call_Detail.DialedNumberString

Router
                                          						Error Code

Error code for this call from the CallRouter process.

Calls with RouterErrorCode 448 are not included in the report.

Derived
                                          						from: Route_Call_Detail.RouterErrorCode

Contact
                                          						Sharing Error Code

Contact
                                          						Share Error code returned by the contact share node.

0 -
                                                							 No error

2 -
                                                							 CS_NOT_CONNECTED

No
                                                							 connection to the Contact Share process.

3 -
                                                							 CS_TIMED_OUT

Request to the Contact Share process failed.

4 -
                                                							 CS_CONFIG_ERROR

Contact Share process encountered a configuration related error.

5 -
                                                							 CS_EXECUTION_ERROR

Contact Share process encountered an error related to running of an expression.

8 -
                                                							 CS_APPGTW_ERROR

Unable to lookup application gateway with the code that the
                                                							 Contact Share process returned.

9 -
                                                							 CS_UNKNOWN_ERROR

Contact Sharing encountered an unknown error.

Derived
                                          						from: Route_Call_Detail.ContactShareErrorCode

Interval

The starting date and time for the current count.

Calls

The
                                          						number of calls routed to this queue between the start time and end time
                                          						specified in the report Filter that have errors.

A count
                                          						of call completion records in Route_Call_Detail that have an error.

## Contact Sharing Expression Results

Use this report to
                              		  view a graph of CalculationResults against DateTime for each Contact Sharing
                              		  Group selected for the report.

This report
                              		  graphs the result calculated by the current Contact Sharing expression formula
                              		  for all calls routed to a given Contact Sharing group over the specified time
                              		  period. For example, the default Contact Sharing algorithm, combines a Minimum
                              		  Expected Delay (MED) calculation with an Agent Occupancy calculation to
                              		  determine which target system receives the call for routing. Positive results
                              		  represent an expected delay, and negative results indicate the percentage of
                              		  agent idle time, that is, the percentage of time the agents in the group were
                              		  available but not working.

For more
                              		  information on the Contact Sharing expression formula, see "Contact Sharing" in
                              		  the Cisco Unified
                                 			 Contact Center Enterprise Features Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

Views: This report has a default chart view (Contact Sharing Expression Results) and a grid view.

Query: This report data
                              		  is built from a Database Query.

Grouping: This report
                              		  is grouped by Contact Sharing Group.

Value List: Contact
                              		  Sharing Group

Database Schema Tables:

Contact_Share_Group

Route_Call_Detail

### Current Fields in the Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

The following
                              		  table lists the fields used to create the Contact Sharing Results Calculations
                              		  report generated from the stock template.

Field

Description

Group

The
                                          						unique name of this Contact Share Group.

Derived
                                          						from: Contact_Share_Group.EnterpriseName

DateTime

The date
                                          						and time when the call was routed, rounded to the nearest minute.

Derived
                                          						from: Route_Call_Detail.DateTime

Result

The
                                          						result of the Contact Share Calculation as defined by the Rule Expression
                                          						averaged over that minute.

The
                                          						Route_Call_Detail record, ContactShareResult, shows the calculation result for
                                          						the optimal queue in the Contact Sharing group.

Derived
                                          						from: Route_Call_Detail.ContactShareResult

## Contact Sharing Interval

Use this report to see a count of the calls routed for each Contact Share Group selected for the report during the interval.

Views: This report has one grid view, Contact Sharing Report Interval.

Query: This report data is built from an Anonymous Block query.

Grouping: This report is grouped by Dialed Number String, Call Type, Target.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Application_Gateway

### Current Fields in the Contact Sharing Interval Report View

Current fields are those fields that appear by default in a report generated from the stock template.

Columns
                                          						(Fields)

Description

Dialed Number String

The dialed number for the call. If the dialed number for the call is configured, this is the same as the DialedNumberString
                                          of the dialed number specified by DialedNumberID. If the dialed number for the call is not configured, this is the dialed
                                          number string and DialedNumberID is NULL.

Derived from: Route_Call_Detail.DialedNumberString

Call Type

The unique enterprise name for this call. If a script changes the call type, this is the final call type for the call.

Derived from: Call_Type.EnterpriseName

Target

The unique enterprise name for the target application gateway.

Derived
                                          						from: Application_Gateway.EnterpriseName

Group

The unique  name
                                          						of this Contact Share Group.

Derived
                                          						from: Contact_Share_Group.EnterpriseName

Rule

The name assigned to   the rule when it was created.

Derived
                                          						from:  
                                          					 Contact_Share_Rule.EnterpriseName

Queue

The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group.

Derived
                                          						from: Contact_Share_Queue.QueueName

Router Error Code

Error code from the CallRouter process.

Derived
                                          						from: Route_Call_Detail.RouterErrorCode

Contact
                                          						Sharing Error Code

Contact
                                          						Share Error code returned by the contact share node.

0 -
                                                							 No error

2 -
                                                							 CS_NOT_CONNECTED

No
                                                							 connection to the Contact Share process.

3 -
                                                							 CS_TIMED_OUT

Request to the Contact Share process failed.

4 -
                                                							 CS_CONFIG_ERROR

Contact Share process encountered a configuration-related error.

5 -
                                                							 CS_EXECUTION_ERROR

Contact Share process encountered an error related to running of an expression.

8 -
                                                							 CS_APPGTW_ERROR

Unable to lookup application gateway with the code that the
                                                							 Contact Share process returned.

9 -
                                                							 CS_UNKNOWN_ERROR

Contact Sharing encountered an unknown error.

Derived
                                          						from: Route_Call_Detail.ContactShareErrorCode

Interval

The starting date and time for the current count.

Count

The number of calls routed to this queue between the start time and end time specified in the report Filter. This is a count
                                          of the call completion rows from the Routing_Call_Detail table.

## Contact Sharing Queue Over Time

Use this report to view the number of calls routed to each    Queue (precision queue or skill group) configured in the Contact
                              Sharing system for the  Groups selected in the report filter.

The default graph view displays a line graph of the number of calls routed to each Queue against time in minute intervals
                              over a  12-hour period  following the StartDate you specify.

Views: This report has a chart view (Queue Over Time) and a grid view.

Select the view you want to see from the report drop-down list located to the far right in the menu bar.

Query: This report data is built from an Anonymous Block query.

Value List: Contact Share Group

Database Schema Tables:

Contact_Share_Group

Contact_Share_Group_Member

Contact_Share_Queue

Contact_Share_Rule

Route_Call_Detail

Application_Gateway

### Current Fields in the Grid View

Current fields are those fields that appear by default in a report generated from the stock template.

Fields

Description

Queue

The name of the Queue configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group.

If any calls cannot be routed, they are displayed in the report as a separate Errors queue.

Derived from: Contact_Share_Group.QueueName

Interval

The interval for which the calls are being reported.

Calls

The number of calls routed to each Queue during the interval.

A count of the call completion rows in the Route_Call_Detail routed to each Queue.

| Columns (Fields) | Description |
|---|---|
| Group | The unique name of this Contact Share Group. Derived from: Contact_Share_Group.EnterpriseName |
| Rule | The name assigned to the rule when it was created. Derived from: Contact_Share_Rule.EnterpriseName |
| Rule Expression | The rule expression that the Contact Share server uses to select the skill group or precision queue from a group for a routing
                                          request. Derived from: Contact_Share_Rule.RuleExpression |
| Queue |
| Name | The name of the queue. Derived from: Contact_Share_Queue.QueueName |
| Type | Identifies the target queue as PQ (Precision Queue,) or SG (Skill Group.) Derived from: Contact_Share_Queue.QueueType |
| Target |
| Name | The unique enterprise name for the target application gateway. Derived from: Application_Gateway.EnterpriseName |
| Label | The label associated with the ultimate target at the switch. Derived from: Route_Call_Detail.TargetLabel |
| Accept Queue If | The logical expression used to determine whether to include the individual skill groups and precision queues in the group
                                          for the routing decision. The contact share queue will be accepted IF the expression evaluates to true. Derived from: Contact_Share_Group.AcceptQueueIf |
| DateTime | The date and time when the call was routed. Derived from: Route_Call_Detail.DateTime |
| ANI | Automatic Number Identification, identifies the calling party. Derived from: Route_Call_Detail.ANI |
| Dialed Number | The dialed number for the call. If the dialed number for the call is configured, this will be the same as the DialedNumberString
                                          of the dialed number specified by DialedNumberID. If the dialed number for the call is not configured, this is the dialed
                                          number string and DialedNumberID will be NULL. Derived from: Route_Call_Detail.DialedNumberString |
| Call Type | The unique enterprise name for this call. If a script changes the call type, this is the final call type for the call. Derived from: Call_Type.EnterpriseName |
| Routing Client | The unique enterprise name for this routing client. Derived from: Routing_Client.EnterpriseName |
| Master Script | The unique enterprise name for the primary script. Master_Script.EnterpriseName |
| CED | Caller-Entered Digits. Route_Call_Detail.CED |
| Variables |
| Variable1 to Variable10 | 10 fields are provided for user-defined variables. Derived from Route_Call_Detail.Variable1 to Route_Call_Detail.Variable10 |

| Fields | Description |
|---|---|
| Gateway | The unique enterprise name for the target application gateway. Derived from: Application_Gateway.EnterpriseName |
| Calls | The number of calls routed to each Gateway between the start time and end time specified in the report Filter. A count of the call completion rows in the Route_Call_Detail routed to each Gateway. |

| Fields | Description |
|---|---|
| Target | The unique enterprise name for the target application gateway. If any calls cannot be routed, they are displayed in the report as a separate Errors target. Derived from: Application_Gateway.EnterpriseName |
| Calls | The number of calls routed to each Gateway during the last 60 minutes, updated every 15 seconds. A count of the call completion rows in the Route_Call_Detail routed to each Gateway. |

| Fields | Description |
|---|---|
| Target | The unique enterprise name for the target application gateway. If any calls cannot be routed, they are displayed in the report as a separate Errors target. Derived from: Application_Gateway.EnterpriseName |
| DateTime | The minute interval for which the calls are being reported. |
| Calls | The number of calls routed to each Gateway during that minute interval. A count of the call completion rows in the Route_Call_Detail routed to each Gateway. |

| Columns
                                          						(Fields) | Description |
|---|---|
| Group | The GroupIDs of the groups selected for the report.  Click '+' next to a GroupID  to see detailed infromation for that group. |
| Rule | The name assigned to   the rule when it was created. Derived
                                          						from:  
                                          					 Contact_Share_Rule.EnterpriseName |
| Group |
| Description | The description of the group entered when it was configured. Derived
                                          						from: Contact_Share_Group.Description |
| Rule |
| Description | The description of the rule entered when it was configured. Derived
                                          						from: Contact_Share_Rule.Description |
| Expression | The rule expression that the Contact Share server uses to select the skill group or precision queue from a group for a routing
                                          request. Derived
                                          						from: Contact_Share_Rule.RuleExpression |
| Queue |
| Queue | The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group. Derived
                                          						from: Contact_Share_Queue.QueueName |
| Type | Identifies the target queue as P -Precision Queue, or S - Skill Group. Derived
                                          						from: Contact_Share_Queue.QueueType |
| Description | The description of this queue. Derived from: Contact_Share_Queue.Description |
| Target |
| Target | The unique enterprise name for the target application gateway. Derived
                                          						from: Application_Gateway.EnterpriseName |
| Description | The
                                          						description of this target Derived
                                          						from: Application_Gateway.Description |
| Preferred Side | Indicates which side of the target gateway the software should use when both are available: A or B. This applies only when
                                          Application GatewayType is 0 (custom gateway). Derived
                                          						from: Application_Gateway.PreferredSide |
| Accept Queue If | The logical expression used to determine whether to include the individual skill groups and precision queues in the group
                                          for the routing decision.  The contact share queue will be accepted IF the expression evaluates to true. Derived
                                          						from: Contact_Share_Group.AcceptQueueIf |

| Note | Calls that end with RouterErrorCode 448, Dialog aborted and was deleted, are not included in the report. 
                                          This is not a routing error. This error means the customer leg disconnected for the
                                          call at the routing client, usually because the customer ended the call. |
|---|---|

| Columns
                                          						(Fields) | Description |
|---|---|
| Group | The
                                          						unique name of this Contact Share Group. Derived
                                          						from: Contact_Share_Group.EnterpriseName |
| Target | The
                                          						unique enterprise name for the target application gateway. Derived
                                          						from: Application_Gateway.EnterpriseName |
| Rule | The name
                                          						assigned to the rule when it was created. Derived
                                          						from: Contact_Share_Rule.EnterpriseName |
| Queue | The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group. Derived
                                          						from: Contact_Share_Queue.QueueName |
| Dialed
                                          						Number String | The
                                          						dialed number for the call. If the dialed number for the call is configured,
                                          						this will be the same as the DialedNumberString of the dialed number specified
                                          						by DialedNumberID. If the dialed number for the call is not configured, this is
                                          						the dialed number string and DialedNumberID will be NULL. Derived
                                          						from: Route_Call_Detail.DialedNumberString |
| Router
                                          						Error Code | Error code for this call from the CallRouter process. Note Calls with RouterErrorCode 448 are not included in the report. Derived
                                          						from: Route_Call_Detail.RouterErrorCode | Note | Calls with RouterErrorCode 448 are not included in the report. |
| Note | Calls with RouterErrorCode 448 are not included in the report. |
| Contact
                                          						Sharing Error Code | Contact
                                          						Share Error code returned by the contact share node. 0 -
                                                							 No error 2 -
                                                							 CS_NOT_CONNECTED No
                                                							 connection to the Contact Share process. 3 -
                                                							 CS_TIMED_OUT Request to the Contact Share process failed. 4 -
                                                							 CS_CONFIG_ERROR Contact Share process encountered a configuration related error. 5 -
                                                							 CS_EXECUTION_ERROR Contact Share process encountered an error related to running of an expression. 8 -
                                                							 CS_APPGTW_ERROR Unable to lookup application gateway with the code that the
                                                							 Contact Share process returned. 9 -
                                                							 CS_UNKNOWN_ERROR Contact Sharing encountered an unknown error. Derived
                                          						from: Route_Call_Detail.ContactShareErrorCode |
| Interval | The starting date and time for the current count. |
| Calls | The
                                          						number of calls routed to this queue between the start time and end time
                                          						specified in the report Filter that have errors. A count
                                          						of call completion records in Route_Call_Detail that have an error. |

| Note | Calls with RouterErrorCode 448 are not included in the report. |
|---|---|

| Field | Description |
|---|---|
| Group | The
                                          						unique name of this Contact Share Group. Derived
                                          						from: Contact_Share_Group.EnterpriseName |
| DateTime | The date
                                          						and time when the call was routed, rounded to the nearest minute. Derived
                                          						from: Route_Call_Detail.DateTime |
| Result | The
                                          						result of the Contact Share Calculation as defined by the Rule Expression
                                          						averaged over that minute. The
                                          						Route_Call_Detail record, ContactShareResult, shows the calculation result for
                                          						the optimal queue in the Contact Sharing group. Derived
                                          						from: Route_Call_Detail.ContactShareResult |

| Columns
                                          						(Fields) | Description |
|---|---|
| Dialed Number String | The dialed number for the call. If the dialed number for the call is configured, this is the same as the DialedNumberString
                                          of the dialed number specified by DialedNumberID. If the dialed number for the call is not configured, this is the dialed
                                          number string and DialedNumberID is NULL. Derived from: Route_Call_Detail.DialedNumberString |
| Call Type | The unique enterprise name for this call. If a script changes the call type, this is the final call type for the call. Derived from: Call_Type.EnterpriseName |
| Target | The unique enterprise name for the target application gateway. Derived
                                          						from: Application_Gateway.EnterpriseName |
| Group | The unique  name
                                          						of this Contact Share Group. Derived
                                          						from: Contact_Share_Group.EnterpriseName |
| Rule | The name assigned to   the rule when it was created. Derived
                                          						from:  
                                          					 Contact_Share_Rule.EnterpriseName |
| Queue | The name of the Queue that is configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group. Derived
                                          						from: Contact_Share_Queue.QueueName |
| Router Error Code | Error code from the CallRouter process. Derived
                                          						from: Route_Call_Detail.RouterErrorCode |
| Contact
                                          						Sharing Error Code | Contact
                                          						Share Error code returned by the contact share node. 0 -
                                                							 No error 2 -
                                                							 CS_NOT_CONNECTED No
                                                							 connection to the Contact Share process. 3 -
                                                							 CS_TIMED_OUT Request to the Contact Share process failed. 4 -
                                                							 CS_CONFIG_ERROR Contact Share process encountered a configuration-related error. 5 -
                                                							 CS_EXECUTION_ERROR Contact Share process encountered an error related to running of an expression. 8 -
                                                							 CS_APPGTW_ERROR Unable to lookup application gateway with the code that the
                                                							 Contact Share process returned. 9 -
                                                							 CS_UNKNOWN_ERROR Contact Sharing encountered an unknown error. Derived
                                          						from: Route_Call_Detail.ContactShareErrorCode |
| Interval | The starting date and time for the current count. |
| Count | The number of calls routed to this queue between the start time and end time specified in the report Filter. This is a count
                                          of the call completion rows from the Routing_Call_Detail table. |

| Fields | Description |
|---|---|
| Queue | The name of the Queue configured on the target Unified CCE systems. It is the same as the EnterpriseName of the precision queue or skill group. If any calls cannot be routed, they are displayed in the report as a separate Errors queue. Derived from: Contact_Share_Group.QueueName |
| Interval | The interval for which the calls are being reported. |
| Calls | The number of calls routed to each Queue during the interval. A count of the call completion rows in the Route_Call_Detail routed to each Queue. |