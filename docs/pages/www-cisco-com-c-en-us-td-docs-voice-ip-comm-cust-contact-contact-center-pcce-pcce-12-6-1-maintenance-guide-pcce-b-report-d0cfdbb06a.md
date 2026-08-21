---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-d0cfdbb06a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01001.html
retrieved_at: 2026-08-21T16:53:59.804658+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Report Data Collection

## Chapter: Report Data Collection

# Report Data Collection

## Real Time Data
                        	 Collection

Real time data is stored on the AW-HDS-DDS. Old real time data is constantly overwritten by new real time data. No history is kept. Real time data is stored in data
                              fields that reflect four time increments, as described in the following table:

Real time
                                          					 data time increments

Description

Half

"Half" values contain a
                                          					 value for the current half-hour. Real time half-hour values are not affected by
                                          					 Interval configuration. That is, if you set the historical reporting interval
                                          					 to 15 minutes, the Half values in real time tables represent the current
                                          					 half-hour time period falling between xx:00:00 and xx:29:59, or xx:30:00 and
                                          					 xx:59:59.

For example,
                                          					 if it is currently 09:18:33, the CallsOfferedHalf column in the
                                          					 Call_Type_Real_Time table contains a value that reflects the first 18 minutes
                                          					 and 33 seconds of the specific half-hour. When a new half-hour begins, at time
                                          					 09:00:00 or 09:30:00, the database element is reset to zero.

Now

"Now" contains a snapshot
                                          					 of the activity at a particular instant (the last check).

For example,
                                          					 
                                          					 CCE software
                                          					 tracks CallsQNow, which is the number of calls currently in queue for a route.
                                          					 When a call is answered, the CallsQNow count is reduced immediately by one (-1)
                                          					 because the call has left the queue. This change is seen at the next real time
                                          					 update for reports that query for that value.

To5

The "To5" values track data on a rolling five-minute basis. The rolling five-minute data employs a "sliding" five-minute window.

Today

Contains
                                          					 the counts since midnight for each value

## Live Data
                        	 Collection

In contrast to Real
                           		Time data collection, in which reporting data is written to the database and
                           		queried periodically by the Unified Intelligence Center, Live Data continuously
                           		processes agent and call events from the peripheral gateway and the router, and
                           		publishes data directly to Unified Intelligence Center. Live Data continuously
                           		pushes only changed data to the reporting clients without the delay of writing
                           		to, and reading from the database. Individual state values, such as agent
                           		states, refresh as they happen, while other values, such as calls in queue,
                           		refresh approximately every 3 seconds.

The Live Data
                           		report templates take advantage of the Live Data service.

The Real Time data
                           		flow is still used to support other stock and custom reports.

Live Data is a
                           		stream processing system which aggregates and processes the events in-stream
                           		and publishes the information. Unified Intelligence Center subscribes to the
                           		message stream to receive the events in real-time and continuously update the
                           		Live Data reports. The Live Data Reporting
                              		  Services co-reside on the CUIC Reporting Server as VOS services.

## Historical
                        	 Data

Historical data
                              		  is stored in Interval tables, and Outbound Option data is stored in Half-Hour tables. For both Half-Hour and Interval tables, historical data is written to
                              		  database at the end of the completed interval. Interval tables contain 15 or 30
                              		  minute summaries, depending on which interval is set.

For half-hour
                              		  intervals, the completed interval is the time period falling between xx:00:00
                              		  and xx:29:59, or xx:30:00 and xx:59:59. For 15 minute intervals, the completed
                              		  interval is the time period falling between xx:00:00 and xx:14:59, xx:15:00 and
                              		  xx:29:59, xx:30:00 and xx:44:59, or xx:45:00 and xx:59:59.

Consider this
                              		  example for half-hour intervals. It is now 15:50:00. An error occurred at
                              		  15:47:00. The half-hour interval reported on right now is for the 15:00:00 to
                              		  15:29:59 interval. The error that occurred at 15:47:00 will be written to the
                              		  database at 16:00:00, when the 15:30:00 to 15:59:59 half-hour interval is
                              		  complete.

For data retention information, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .
                              		  If you need additional detailed reporting retention, add an optional external
                              		  HDS.

Historical
                                          					 data

Description

Interval
                                          					 tables are:

Agent_Interval

Agent_Skill_Group_Interval

Skill_Group_Interval

Call_Type_Interval

Call_Type_Skill_Group_Interval

Campaign_Query_Rule_Interval (30-minute data only)

Dialer_Interval (30-minute data only)

Router_Queue_Interval

Half-Hour
                                          					 (Outbound Option only)

Half-Hour
                                          					 tables are:

Campaign_Half_Hour

Campaign_Query_Rule_Half_Hour

Dialer_Half_Hour

Dialer_Skill_Group_Half_Hour

## Reasons for Data Discrepancies

You may notice discrepancies in report data if you are comparing counts between real time and historical reports or comparing
                           counts across interval boundaries.

Counts in real time data (for example CallsHandledTo5) do not
                           match counts in the historical interval records (for example,
                           CallsHandled) because the real time data is moved to the historical database at
                           the end of each interval.

Consider this
                           example: at 8:55 a call comes into the contact center and is answered by an
                           agent.

The real time count for CallsAnswered
                                 increases by one (+1).

Between 8:55 and 9:00, the
                                 real time data shows the answered call.

The answered call
                                 does not populate the interval data until 9:00, when the 8:00 to 8:59:59
                                 interval ends.

Counts that would typically match for a day, such as
                           CallsOffered and CallsHandled, might not always match over specific intervals. This discrepancy occurs because the counts
                           for some data
                           elements might be increased across boundaries.

Consider this example: at 8:55, a call comes in to the contact
                           center and is answered by an agent. The agent completes the call at
                           9:05.

In the historical database, the call is counted
                                 as offered in the 8:30:00 to 8:59:59 interval.

The call
                                 is counted as handled in the 9:00:00 to 9:29:59 interval.

If you run a report for the 9:00:00 to 9:29:59 interval, it appears that
                                 tasks handled does not equal tasks offered for the interval.

You also might notice that tasks offered does not equal task abandoned +
                           tasks handled for an interval. Tasks offered reflects the number of
                           calls and tasks that were offered to agents in this interval, while tasks
                           handled and tasks abandoned might include calls that were offered in the last
                           interval and completed in this interval. Some historical report templates group
                           statistics into "Completed Tasks" to indicate that the statistics represent all
                           calls and tasks that completed in this interval.

In
                           general, interval boundary issues are reduced if you run daily reports.
                           However, if your contact center runs 24 hours a day, you might still notice
                           discrepancies for intervals such as  the 11:30:00 to 11:59:59 and 12:00:00 to 12:29:59
                           intervals.

| Real time
                                          					 data time increments | Description |
|---|---|
| Half | "Half" values contain a
                                          					 value for the current half-hour. Real time half-hour values are not affected by
                                          					 Interval configuration. That is, if you set the historical reporting interval
                                          					 to 15 minutes, the Half values in real time tables represent the current
                                          					 half-hour time period falling between xx:00:00 and xx:29:59, or xx:30:00 and
                                          					 xx:59:59. For example,
                                          					 if it is currently 09:18:33, the CallsOfferedHalf column in the
                                          					 Call_Type_Real_Time table contains a value that reflects the first 18 minutes
                                          					 and 33 seconds of the specific half-hour. When a new half-hour begins, at time
                                          					 09:00:00 or 09:30:00, the database element is reset to zero. |
| Now | "Now" contains a snapshot
                                          					 of the activity at a particular instant (the last check). For example,
                                          					 
                                          					 CCE software
                                          					 tracks CallsQNow, which is the number of calls currently in queue for a route.
                                          					 When a call is answered, the CallsQNow count is reduced immediately by one (-1)
                                          					 because the call has left the queue. This change is seen at the next real time
                                          					 update for reports that query for that value. |
| To5 | The "To5" values track data on a rolling five-minute basis. The rolling five-minute data employs a "sliding" five-minute window. |
| Today | Contains
                                          					 the counts since midnight for each value |

| Note | The Half Hour
                                          			 database tables available in the database are not populated because these
                                          			 tables are not supported. These tables are replaced by the Interval database
                                          			 tables. |
|---|---|

| Historical
                                          					 data | Description |
|---|---|
| Interval | Interval
                                          					 tables are: Agent_Interval Agent_Skill_Group_Interval Skill_Group_Interval Call_Type_Interval Call_Type_Skill_Group_Interval Campaign_Query_Rule_Interval (30-minute data only) Dialer_Interval (30-minute data only) Router_Queue_Interval |
| Half-Hour
                                          					 (Outbound Option only) | Half-Hour
                                          					 tables are: Campaign_Half_Hour Campaign_Query_Rule_Half_Hour Dialer_Half_Hour Dialer_Skill_Group_Half_Hour |