---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--c6c320490f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_0100000.html
retrieved_at: 2026-08-21T01:37:33.130974+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR System Event Log

## Chapter: CAR System Event Log

# CAR System Event Log

CAR provides logs that you can use to track the status of the
                        		various activities. The event log tracks events that the CAR Scheduler
                        		triggers, such as automatically generated reports, loading of CDRs, report
                        		deletions, and database purging.

The event log provides a report on the status of the activities
                        		that the CAR Scheduler controls. The event log report shows whether the tasks
                        		started, completed successfully, or are in progress.

## Generate Event
                        	 Log

This section describes how to generate the event log report. The event log includes a list of tasks/reports that are scheduled
                              on a daily, weekly, or monthly basis.

This release of Unified Communications Manager introduces the Task Monitor and Database Maintenance as new features.

TaskMonitor monitors the status of other jobs and cleans up Informix Dynamic Server (IDS) memory when necessary by using the
                              IDS command "onmode -F." DatabaseMaintenance runs the IDS-recommended optimized database maintenance "update statistics" procedures.

Task Monitor begins about 1 minute after the Scheduler starts, and 1 minute after the Scheduler repopulates the schedules
                              every day at midnight (00.00). The Task Monitor periodically (every 5 minutes) monitors the status of all jobs for the day
                              from the tbl_event_log with the exception of the following jobs: PopulateSchedules, TaskMonitor, DatabaseMaintenance, and
                              DailyCdrLoad.

When a task does not start on schedule because a previous task is still running, you may see something like the following
                              trace message:

```
2008-02-14 08:00:04, 602 WARN [main] services. Scheduler - runTasks(): Job [DailyCdrLoad] thread is busy, hence it will be removed from today’s schedule and not be started!”
```

The Scheduler gives a grace period to periodically sleep for 10 seconds and then check whether the task thread is complete.
                              The Scheduler sleeps up to 2 minutes total. If the task thread is not complete after the 2 minutes of wait, the next task
                              gets removed from the current schedule, and does not run until its next scheduled time.

The following table displays the list of tasks/reports and how often they are scheduled.

Task

Scheduled

CDR Load

Daily

Task Monitor 1

Daily

Database Maintenance 2

Daily

QoS Notification

Daily

Charge Limit Notification

Daily

Database Alert

Daily

Delete Reports

Daily

Database Purge

Daily

Traffic Summary - Hour of Day

Daily

Top N Charge

Daily

Top N Duration

Daily

Top N Calls

Daily

Conference - Detail

Daily

Traffic Summary - Day of week

Weekly

Conference Bridge Utilization - Day of week

Weekly

Voice Messaging Utilization - Day of week

Weekly

Route Pattern/Hunt Pilot Utilization - Day of week

Weekly

Route/Hunt List Utilization - Day of week

Weekly

Route Group Utilization - Day of week

Weekly

Gateway Utilization - Day of week

Weekly

Line Group Utilization - Day of week

Weekly

QoS Summary

Monthly

Gateway Summary

Monthly

Traffic Summary - Day of month

Monthly

System Overview

Monthly

Department Bill Summary

Monthly

Individual Bill Summary

Monthly

Top N Charge

Monthly

Top N Duration

Monthly

Top N Calls

Monthly

Conference - Summary

Monthly

Choose System > Log Screens > Event
                                             				  Log .

The Event Log
                                          				window displays.

Click the Daily radio button to choose daily jobs, the Weekly radio button to choose weekly jobs, or the Monthly radio button to choose monthly jobs.

In the List of
                                       			 Jobs area, choose the tasks for which you want information.

To add the
                                       			 chosen task to the Selected Jobs area, click the right arrow icon.

To remove
                                       			 tasks from the Selected Jobs area, choose the task that you want removed and
                                       			 click the left arrow icon.

To add tasks
                                       			 with a different frequency, repeat the previous steps. For example, you can
                                       			 have daily reports and reports that include monthly or weekly tasks.

Choose the
                                       			 status to include in the report. You must choose at least one status as
                                       			 described in the following table.

The system
                                                      				  chooses the status of each event log report by default.

Status

Description

Complete

If this check box is checked, the event log report includes
                                                      						  tasks that are complete.

In Progress

If this check box is checked, the event log report includes
                                                      						  tasks that are currently in progress.

Interrupted

If this check box is checked, the event log includes tasks
                                                      						  that have been interrupted, either manually by an administrator, or by an
                                                      						  administrative process such as a DRS backup.

Unsuccessful

If this check box is checked, the event log report includes
                                                      						  tasks that have failed.

Scheduled

If this check box is checked, the event log report includes
                                                      						  tasks that have been scheduled but have not yet started.

When the
                                                      				  Scheduler restarts, all unfinished jobs with a status of Scheduled get deleted.
                                                      				  Current jobs with the status of In Progress or Scheduled get changed to
                                                      				  Interrupted.

Choose a date
                                       			 range by choosing From and To values.

To generate
                                       			 the event log report, click the OK button.

Print the log
                                       			 by right-clicking on the screen and choosing Print .

A grace
                                                      				  period of up to 2 minutes gets provided, so an in-process job can finish before
                                                      				  the next schedule job is scheduled to begin.

## Output of Event Log Report

Parameter

Description

Sl No

Serial number

Jobs

Name of the task

Start Time

Time the task starts

End Time

Time the task ends

Status

Unsuccessful, in progress, completed

Date

Date the task is scheduled

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Task | Scheduled |
|---|---|
| CDR Load | Daily |
| Task Monitor 1 | Daily |
| Database Maintenance 2 | Daily |
| QoS Notification | Daily |
| Charge Limit Notification | Daily |
| Database Alert | Daily |
| Delete Reports | Daily |
| Database Purge | Daily |
| Traffic Summary - Hour of Day | Daily |
| Top N Charge | Daily |
| Top N Duration | Daily |
| Top N Calls | Daily |
| Conference - Detail | Daily |
| Traffic Summary - Day of week | Weekly |
| Conference Bridge Utilization - Day of week | Weekly |
| Voice Messaging Utilization - Day of week | Weekly |
| Route Pattern/Hunt Pilot Utilization - Day of week | Weekly |
| Route/Hunt List Utilization - Day of week | Weekly |
| Route Group Utilization - Day of week | Weekly |
| Gateway Utilization - Day of week | Weekly |
| Line Group Utilization - Day of week | Weekly |
| QoS Summary | Monthly |
| Gateway Summary | Monthly |
| Traffic Summary - Day of month | Monthly |
| System Overview | Monthly |
| Department Bill Summary | Monthly |
| Individual Bill Summary | Monthly |
| Top N Charge | Monthly |
| Top N Duration | Monthly |
| Top N Calls | Monthly |
| Conference - Summary | Monthly |

| Step 1 | Choose System > Log Screens > Event
                                             				  Log . The Event Log
                                          				window displays. |
|---|---|
| Step 2 | Click the Daily radio button to choose daily jobs, the Weekly radio button to choose weekly jobs, or the Monthly radio button to choose monthly jobs. |
| Step 3 | In the List of
                                       			 Jobs area, choose the tasks for which you want information. |
| Step 4 | To add the
                                       			 chosen task to the Selected Jobs area, click the right arrow icon. |
| Step 5 | To remove
                                       			 tasks from the Selected Jobs area, choose the task that you want removed and
                                       			 click the left arrow icon. |
| Step 6 | To add tasks
                                       			 with a different frequency, repeat the previous steps. For example, you can
                                       			 have daily reports and reports that include monthly or weekly tasks. |
| Step 7 | Choose the
                                       			 status to include in the report. You must choose at least one status as
                                       			 described in the following table. Note The system
                                                      				  chooses the status of each event log report by default. Table 2. Event Log
                                                				Report Status Status Description Complete If this check box is checked, the event log report includes
                                                      						  tasks that are complete. In Progress If this check box is checked, the event log report includes
                                                      						  tasks that are currently in progress. Interrupted If this check box is checked, the event log includes tasks
                                                      						  that have been interrupted, either manually by an administrator, or by an
                                                      						  administrative process such as a DRS backup. Unsuccessful If this check box is checked, the event log report includes
                                                      						  tasks that have failed. Scheduled If this check box is checked, the event log report includes
                                                      						  tasks that have been scheduled but have not yet started. Note When the
                                                      				  Scheduler restarts, all unfinished jobs with a status of Scheduled get deleted.
                                                      				  Current jobs with the status of In Progress or Scheduled get changed to
                                                      				  Interrupted. | Note | The system
                                                      				  chooses the status of each event log report by default. | Status | Description | Complete | If this check box is checked, the event log report includes
                                                      						  tasks that are complete. | In Progress | If this check box is checked, the event log report includes
                                                      						  tasks that are currently in progress. | Interrupted | If this check box is checked, the event log includes tasks
                                                      						  that have been interrupted, either manually by an administrator, or by an
                                                      						  administrative process such as a DRS backup. | Unsuccessful | If this check box is checked, the event log report includes
                                                      						  tasks that have failed. | Scheduled | If this check box is checked, the event log report includes
                                                      						  tasks that have been scheduled but have not yet started. | Note | When the
                                                      				  Scheduler restarts, all unfinished jobs with a status of Scheduled get deleted.
                                                      				  Current jobs with the status of In Progress or Scheduled get changed to
                                                      				  Interrupted. |
| Note | The system
                                                      				  chooses the status of each event log report by default. |
| Status | Description |
| Complete | If this check box is checked, the event log report includes
                                                      						  tasks that are complete. |
| In Progress | If this check box is checked, the event log report includes
                                                      						  tasks that are currently in progress. |
| Interrupted | If this check box is checked, the event log includes tasks
                                                      						  that have been interrupted, either manually by an administrator, or by an
                                                      						  administrative process such as a DRS backup. |
| Unsuccessful | If this check box is checked, the event log report includes
                                                      						  tasks that have failed. |
| Scheduled | If this check box is checked, the event log report includes
                                                      						  tasks that have been scheduled but have not yet started. |
| Note | When the
                                                      				  Scheduler restarts, all unfinished jobs with a status of Scheduled get deleted.
                                                      				  Current jobs with the status of In Progress or Scheduled get changed to
                                                      				  Interrupted. |
| Step 8 | Choose a date
                                       			 range by choosing From and To values. |
| Step 9 | To generate
                                       			 the event log report, click the OK button. The
                                       			 event log displays information about the chosen tasks. |
| Step 10 | Print the log
                                       			 by right-clicking on the screen and choosing Print . Note A grace
                                                      				  period of up to 2 minutes gets provided, so an in-process job can finish before
                                                      				  the next schedule job is scheduled to begin. | Note | A grace
                                                      				  period of up to 2 minutes gets provided, so an in-process job can finish before
                                                      				  the next schedule job is scheduled to begin. |
| Note | A grace
                                                      				  period of up to 2 minutes gets provided, so an in-process job can finish before
                                                      				  the next schedule job is scheduled to begin. |

| Note | The system
                                                      				  chooses the status of each event log report by default. |
|---|---|

| Status | Description |
|---|---|
| Complete | If this check box is checked, the event log report includes
                                                      						  tasks that are complete. |
| In Progress | If this check box is checked, the event log report includes
                                                      						  tasks that are currently in progress. |
| Interrupted | If this check box is checked, the event log includes tasks
                                                      						  that have been interrupted, either manually by an administrator, or by an
                                                      						  administrative process such as a DRS backup. |
| Unsuccessful | If this check box is checked, the event log report includes
                                                      						  tasks that have failed. |
| Scheduled | If this check box is checked, the event log report includes
                                                      						  tasks that have been scheduled but have not yet started. |

| Note | When the
                                                      				  Scheduler restarts, all unfinished jobs with a status of Scheduled get deleted.
                                                      				  Current jobs with the status of In Progress or Scheduled get changed to
                                                      				  Interrupted. |
|---|---|

| Note | A grace
                                                      				  period of up to 2 minutes gets provided, so an in-process job can finish before
                                                      				  the next schedule job is scheduled to begin. |
|---|---|

| Parameter | Description |
|---|---|
| Sl No | Serial number |
| Jobs | Name of the task |
| Start Time | Time the task starts |
| End Time | Time the task ends |
| Status | Unsuccessful, in progress, completed |
| Date | Date the task is scheduled |