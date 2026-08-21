---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b06jobs-html-8f3e3ecc05
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b06jobs.html
retrieved_at: 2026-08-21T16:13:25.848922+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Scheduling Jobs

## Chapter: Scheduling Jobs

## Scheduling Jobs

You can schedule bulk transactions and specify a time when these transactions need to start.

All jobs that are submitted through the Bulk Administration menu queue up on the Bulk Provisioning Service (BPS). Depending on the start time that is specified for a job, the transaction starts running. If no start time is mentioned, the transactions execute in the order in which they are received.

The following topics provide information about activating BPS and scheduling jobs:

• Activating Bulk Provisioning Service

• Starting/Stopping/Restarting BPS

• Deactivating BPS

• Finding a Job

• Scheduling Jobs

## Activating Bulk Provisioning Service

Before submitting a job for execution, ensure that BPS is activated.

Use the following procedure to activate BPS.

Step 1 From Cisco Unified Presence Server Serviceability window, choose Tools > Service Activation .

The Service Activation window displays.

Step 2 From the Service drop-down list box, choose the server that is running Cisco Unified Presence Server.

Step 3 In the Database and Admin Services area, check the check box that corresponds to Cisco Bulk Provisioning Service.

Note If the service is already activated, the Activation Status will display as Activated.

Step 4 Click Update .

Step 5 The window refreshes, and the Activation Status that corresponds to Bulk Provisioning Service displays Activated .

Note BPS starts automatically after it is activated. See the "Starting/Stopping/Restarting BPS" section to stop, start, or restart the service.

Note Every time that the service is started, BPS synchronizes with Cisco Unified Presence Server database.

## Starting/Stopping/Restarting BPS

BPS starts automatically after it is activated by using Cisco Unified Presence Server Serviceability. This section describes the procedures to stop or restart the BPS.

Step 1 In Cisco Unified Presence Server Serviceability, choose Tools > Control Center - Feature Services.

The Control Center-Feature Services window displays.

Step 2 Choose the Cisco Unified Presence Server from the Servers drop-down list box.

Cisco Bulk Provisioning Service displays in list under Service Name column, in the Database and Admin Services area.

Note If BPS was activated by using "Activating Bulk Provisioning Service" section , the Status displays as Activated.

Step 3 Check the check box that corresponds to BPS.

Step 4 If you want to restart BPS, click Restart .

The service restarts, and the message, Service Successfully Restarted, displays.

Step 5 If you want to stop BPS, click Stop .

The service stops, and the message, Service Successfully Stopped, displays.

Step 6 If you want to start the stopped BPS, click Start .

The service starts, and the message, Service Successfully Started, displays.

## Deactivating BPS

You can deactivate BPS when you do not require it. This section describes the procedure to deactivate BPS service and log out of the tool.

Step 1 In Cisco Unified Presence Server Serviceability, choose Tools > Service Activation .

The Service Activation window displays.

Step 2 Choose the Cisco Unified Presence Server from the Servers drop-down list box.

Cisco Bulk Provisioning Service displays in the list under Service Name column, in the Database and Admin Services area.

Step 3 Uncheck the check box that corresponds to the Cisco Bulk Provisioning Service and click Update .

The service deactivates, and the Status column displays the status as Deactivated.

## Finding a Job

Use the following procedure to find jobs that are already submitted to BPS through the Bulk Administration menu.

Step 1 Choose Bulk Administration > Job Scheduler . The Find and List Job window displays.

Step 2 From the first Find Job where drop-down list box, choose one of the following options:

• User

• Status

• Job ID

• Description

• Scheduled Date Time

Step 3 From the second Find Job where drop-down list box, choose one of the following options:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 4 From the third drop-down list box, choose Show to display completed jobs.

Step 5 Specify the appropriate search text, if applicable.

Tip To find all jobs that are registered in the database, click Find without entering any search text.

Step 6 To further define your query, you can choose AND or OR to add multiple filters and repeat Steps 2 through 5 .

Step 7 Click Find .

A list of discovered jobs displays by

• Job Id

• Scheduled Date Time

• Submit Date Time

• Sequence

• Description

• Status

• Last User

Note The Status displays Hold if the Run Later radio button was selected while you were scheduling the job. The Status displays Pending if the Run Immediately radio button was selected. The Status displays Completed for completed jobs, and it displays Incomplete for jobs that had an error and could not complete.

Step 8 Click the Job ID for the job that is in process or on hold that you want to schedule and/or activate.

The job Configuration window displays.

You can view the status and the summary result of the job you selected.

Additional Topics

See the "Related Topics" section

## Scheduling Jobs

Use the following procedure to schedule submitted jobs.

Step 1 Find the job that you want to schedule by using the "Finding a Job" section .

Step 2 In the Job Configuration window, enter the settings for scheduling and activating the job as described in Table 40-1 .

Table 40-1 Job Configuration Settings

Job Id

This field displays the job ID that is created when the job is submitted.

Job Status

This field displays the status of the job from one of the following options:

• Hold

• Pending

• Completed

• Incomplete

Scheduled Date Time

Choose the month, date, year from the drop-down list boxes. Enter the time when you want the job to be scheduled.

Submit Date Time

This field displays the date and time when the job was submitted.

Sequence

From the drop-down list box, choose the sequence in which the job should be run. You can choose a number between 1 and 20.

Note If the scheduled date and time are the same for two or more jobs, this indicates that the jobs are queued in BPS according the sequence number. If the scheduled date and time, and Sequence are the same, the jobs are queued depending on the submitted date and time.

Job Description

This field displays the description that you entered when the job was created.

Frequency

From the following options, choose the frequency of the transaction:

• Once

• Monthly

• Weekly

• Daily

• Hourly

For example, if you choose Daily, the transaction will repeat daily at the time that is entered in the Schedule Time and Date field.

Job End Time

This field displays the end time for recurring (frequency) job.

Last Modified By

This field displays the user ID of the administrator who last modified this job.

Step 3 To activate the job at the scheduled time, click Activate Job, or, to save the configuration settings and activate the job at a later time, click Save .

The Find and List Jobs window displays.

Note If a job is saved, but not activated, the status of the job will display as Hold. These jobs do not get processed by BPS unless they are activated.

Step 4 Click the job ID for the job that you have activated. In the Job Configuration window, the following information displays in the Job Results area for all jobs that are complete, incomplete, stop requested, or processing:

• Job Launched Date

• Job Result Status

• Number of records Processed

• Number of Records Failed

• Total Number of Records

• Log File Name

Note To view the log file for this transaction, click on the link in the Log File Name column.

Step 5 To go back to the list of jobs, choose Back to Find/List from the Related Links drop-down list box and click Go .

## Related Topics

• Activating Bulk Provisioning Service

• Starting/Stopping/Restarting BPS

• Deactivating BPS

• Finding a Job

• Scheduling Jobs

| Field | Description |
|---|---|
| Job Id | This field displays the job ID that is created when the job is submitted. |
| Job Status | This field displays the status of the job from one of the following options: • Hold • Pending • Completed • Incomplete |
| Scheduled Date Time | Choose the month, date, year from the drop-down list boxes. Enter the time when you want the job to be scheduled. |
| Submit Date Time | This field displays the date and time when the job was submitted. |
| Sequence | From the drop-down list box, choose the sequence in which the job should be run. You can choose a number between 1 and 20. Note If the scheduled date and time are the same for two or more jobs, this indicates that the jobs are queued in BPS according the sequence number. If the scheduled date and time, and Sequence are the same, the jobs are queued depending on the submitted date and time. |
| Job Description | This field displays the description that you entered when the job was created. |
| Frequency | From the following options, choose the frequency of the transaction: • Once • Monthly • Weekly • Daily • Hourly For example, if you choose Daily, the transaction will repeat daily at the time that is entered in the Schedule Time and Date field. |
| Job End Time | This field displays the end time for recurring (frequency) job. |
| Last Modified By | This field displays the user ID of the administrator who last modified this job. |