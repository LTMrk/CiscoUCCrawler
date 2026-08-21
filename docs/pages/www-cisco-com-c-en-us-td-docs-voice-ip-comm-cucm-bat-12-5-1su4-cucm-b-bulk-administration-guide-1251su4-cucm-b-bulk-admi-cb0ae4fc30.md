---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-cb0ae4fc30
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_01001101.html
retrieved_at: 2026-08-21T17:54:48.985750+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Manage Scheduled
	 Jobs

## Chapter: Manage Scheduled
	 Jobs

# Manage Scheduled
                     	 Jobs

This chapter
                        		provides information about activating BPS and scheduling jobs.

You can schedule bulk
                        		transactions and specify a time when they need to start these transactions. All
                        		jobs that are submitted through the Bulk Administration menu in the Cisco Unified Communications
                           		  Manager Administration, queue up on the Bulk Provisioning Service
                        		(BPS). Depending on the start time specified for a job, the transaction starts
                        		running. If no start time is mentioned, the transactions execute in the order
                        		that they are received.

## Activate Bulk Provisioning Service

Before submitting a job for execution, the Bulk Provisioning
                              		  Service (BPS) should be activated.

BPS starts automatically after it is activated. Every time that the
                              		  service is started, BPS synchronizes with Cisco Unified Communications Manager database.

From Cisco Unified Communications Manager
                                          				Serviceability window, choose Tools > Service Activation .

From the Server drop-down list box, choose the server
                                       			 that is running Cisco Unified Communications Manager .

In the Database and Admin Services area, check the
                                       			 check box corresponding to Cisco Bulk Provisioning Service .

If the service is already activated, the Activation Status will
                                                      				  display as Activated.

Click Update .

## Start, Stop and Restart BPS

You can manually stop or restart the Bulk Provisioning
                              		  Service (BPS).

The BPS starts automatically after it is activated using Cisco Unified Communications Manager Serviceability.

In Cisco Unified Communications Manager Serviceability, choose Tools > Control Center - Feature
                                             				  Services .

The Control Center–Feature Services window
                                          				displays.

Choose the Cisco Unified Communications Manager server from the Servers drop-down list box.

Cisco Bulk Provisioning Service displays in list under Service Name column, in the Database and Admin Services area.

If BPS is already activated, the Activation Status will display
                                                      				  as Activated.

Check the check box corresponding to BPS and do one of the
                                       			 following:

To restart BPS, click Restart .

To stop BPS, click Stop .

To start the stopped BPS, click Start .

## Deactivate BPS and Log Out

After you deactivate BPS you can log out of the tool when you
                              		  no longer need to use itl.

In Cisco Unified Communications Manager Serviceability, choose Tools Service
                                          				Activation .

Choose the Cisco Unified Communications Manager server from the Servers drop-down list box.

Cisco Bulk Provisioning Service displays in the list under Service Name column in the Database and Admin Services area.

Uncheck the check box corresponding to the Cisco Bulk Provisioning
                                       			 Service and click Update .

## Find Jobs Submitted
                        	 to BPS

You can
                              		  find jobs that are already submitted to BPS through the Bulk Administration
                              		  menu on Cisco Unified Communications
                                 			 Manager Administration.

Choose Bulk
                                             				  Administration > Job Scheduler . The Find and List Job
                                       			 window displays.

From the first Find Job
                                          				where drop-down list box, choose one of the following options.

- User

- Status

- Job ID

- Description

- Scheduled Date Time

When searching for jobs, use epoch time and not human readable
                                                      				  date. For example, search with 1438171 rather than July 2015.

From the second Find Job
                                          				where drop-down list box, choose one of the following options.

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

From the third
                                       			 drop-down list box, choose Show to display completed jobs.

Specify the
                                       			 appropriate search text, if applicable, and click Find.

To further
                                          				define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 .

To find all
                                                      				  jobs that are registered in the database, click Find without entering any search text.

- Job Id

- Scheduled Date Time

- Submit Date Time

- Sequence

- Description

- Status

The Status
                                                               						displays Hold if Run Later radio button was selected while scheduling
                                                               						the job. The Status displays Pending if Run Immediately radio button was selected. The
                                                               						Status displays Completed for completed jobs and it displays Incomplete for
                                                               						jobs that had an error and could not be completed.

Click the Job ID
                                       			 for the job in process or on hold, that you want to schedule and / or activate.

## Schedule Submitted Jobs

You can schedule submitted jobs.

Find the job you want to schedule.

In the Job Configuration window, enter the settings for
                                       			 scheduling and activating the job.

See the following table.

Field

Description

Job Id

Displays the job ID that is created when the job is
                                                      						  submitted.

Job Status

Displays the status of the job from one of the following
                                                      						  options:

Hold

Pending

Completed

Incomplete

Scheduled Date Time

Choose the month, date, year from the drop-down list
                                                      						  boxes. Enter the time when you want the job to be scheduled.

Submit Date Time

Displays the date and time when the job was submitted.

Sequence

Choose from the drop-down list box, the sequence in which
                                                      						  the job should be run. You can choose a number between 1 and 20.

If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time.

Job Description

Displays the description you entered when the job was
                                                      						  created. This description can be edited to include up to 50 characters in any
                                                      						  language, but it cannot include double-quotes ( " ), percentage
                                                      						  sign ( % ), ampersand (&), back-slash ( \ ),
                                                      						  or angle brackets (<>).

Frequency

Choose from the following options, the frequency of the
                                                      						  transaction:

Once

Monthly

Weekly

Daily

Hourly

For example, if you choose Daily, the transaction will be
                                                      						  repeated daily at the time entered in the Schedule Time and Date field.

Job End Time

Displays the end time for recurring (frequency) job.

Last Modified By

Displays the user ID of the administrator who last
                                                      						  modified this job.

Click Activate job to activate the job at the
                                       			 scheduled time or click Save to save the configuration settings to
                                       			 activate the job at a later time.

The Find and List Jobs window displays.

If a Job is saved, but not activated then status of the job will
                                                      				  be displayed as Hold. These jobs will not be processed by BPS unless they are
                                                      				  activated.

Click the job ID for the job you have activated. In the Job Configuration window, the following
                                       			 information displays in the Job Results area, for all jobs that are
                                       			 complete, incomplete, stop requested, or processing.

- Job Launched Date Time

- Job Result Status

- Number of records
                                             				  Processed

- Number of Records
                                             				  Failed

- Total Number of
                                             				  Records

Click on the link in the Log File Name column to view the log
                                                            						file for this transaction.

### What to do next

To go back to the list of jobs, choose Back to Find/List from the Related Links drop-down list box and click Go.

| Step 1 | From Cisco Unified Communications Manager
                                          				Serviceability window, choose Tools > Service Activation . The Service Activation window displays. |
|---|---|
| Step 2 | From the Server drop-down list box, choose the server
                                       			 that is running Cisco Unified Communications Manager . |
| Step 3 | In the Database and Admin Services area, check the
                                       			 check box corresponding to Cisco Bulk Provisioning Service . Note If the service is already activated, the Activation Status will
                                                      				  display as Activated. | Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |
| Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |
| Step 4 | Click Update . The window refreshes and the Activation Status
                                       			 corresponding to Bulk Provisioning Service displays Activated. |

| Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |
|---|---|

| Note | The BPS starts automatically after it is activated using Cisco Unified Communications Manager Serviceability. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Serviceability, choose Tools > Control Center - Feature
                                             				  Services . The Control Center–Feature Services window
                                          				displays. |
|---|---|
| Step 2 | Choose the Cisco Unified Communications Manager server from the Servers drop-down list box. Cisco Bulk Provisioning Service displays in list under Service Name column, in the Database and Admin Services area. Note If BPS is already activated, the Activation Status will display
                                                      				  as Activated. | Note | If BPS is already activated, the Activation Status will display
                                                      				  as Activated. |
| Note | If BPS is already activated, the Activation Status will display
                                                      				  as Activated. |
| Step 3 | Check the check box corresponding to BPS and do one of the
                                       			 following: To restart BPS, click Restart . The service restarts, and the message, Service Successfully
                                             				  Restarted, displays. To stop BPS, click Stop . The service stops, and the message, Service Successfully
                                             				  Stopped, displays. To start the stopped BPS, click Start . The service starts, and the message, Service Successfully
                                             				  Started, displays. |

| Note | If BPS is already activated, the Activation Status will display
                                                      				  as Activated. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Serviceability, choose Tools Service
                                          				Activation . The Service Activation window displays. |
|---|---|
| Step 2 | Choose the Cisco Unified Communications Manager server from the Servers drop-down list box. Cisco Bulk Provisioning Service displays in the list under Service Name column in the Database and Admin Services area. |
| Step 3 | Uncheck the check box corresponding to the Cisco Bulk Provisioning
                                       			 Service and click Update . The service deactivates and the Status column displays the
                                       			 status as Deactivated. |

| Step 1 | Choose Bulk
                                             				  Administration > Job Scheduler . The Find and List Job
                                       			 window displays. |
|---|---|
| Step 2 | From the first Find Job
                                          				where drop-down list box, choose one of the following options. User Status Job ID Description Scheduled Date Time Note When searching for jobs, use epoch time and not human readable
                                                      				  date. For example, search with 1438171 rather than July 2015. | Note | When searching for jobs, use epoch time and not human readable
                                                      				  date. For example, search with 1438171 rather than July 2015. |
| Note | When searching for jobs, use epoch time and not human readable
                                                      				  date. For example, search with 1438171 rather than July 2015. |
| Step 3 | From the second Find Job
                                          				where drop-down list box, choose one of the following options. begins with contains is exactly ends with is empty is not empty |
| Step 4 | From the third
                                       			 drop-down list box, choose Show to display completed jobs. |
| Step 5 | Specify the
                                       			 appropriate search text, if applicable, and click Find. To further
                                          				define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 . Tip To find all
                                                      				  jobs that are registered in the database, click Find without entering any search text. A list of
                                          				discovered jobs displays by: Job Id Scheduled Date Time Submit Date Time Sequence Description Status Last User Note The Status
                                                               						displays Hold if Run Later radio button was selected while scheduling
                                                               						the job. The Status displays Pending if Run Immediately radio button was selected. The
                                                               						Status displays Completed for completed jobs and it displays Incomplete for
                                                               						jobs that had an error and could not be completed. | Tip | To find all
                                                      				  jobs that are registered in the database, click Find without entering any search text. | Note | The Status
                                                               						displays Hold if Run Later radio button was selected while scheduling
                                                               						the job. The Status displays Pending if Run Immediately radio button was selected. The
                                                               						Status displays Completed for completed jobs and it displays Incomplete for
                                                               						jobs that had an error and could not be completed. |
| Tip | To find all
                                                      				  jobs that are registered in the database, click Find without entering any search text. |
| Note | The Status
                                                               						displays Hold if Run Later radio button was selected while scheduling
                                                               						the job. The Status displays Pending if Run Immediately radio button was selected. The
                                                               						Status displays Completed for completed jobs and it displays Incomplete for
                                                               						jobs that had an error and could not be completed. |
| Step 6 | Click the Job ID
                                       			 for the job in process or on hold, that you want to schedule and / or activate. The Job
                                          				Configuration window displays. |

| Note | When searching for jobs, use epoch time and not human readable
                                                      				  date. For example, search with 1438171 rather than July 2015. |
|---|---|

| Tip | To find all
                                                      				  jobs that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | The Status
                                                               						displays Hold if Run Later radio button was selected while scheduling
                                                               						the job. The Status displays Pending if Run Immediately radio button was selected. The
                                                               						Status displays Completed for completed jobs and it displays Incomplete for
                                                               						jobs that had an error and could not be completed. |
|---|---|

| Step 1 | Find the job you want to schedule. |
|---|---|
| Step 2 | In the Job Configuration window, enter the settings for
                                       			 scheduling and activating the job. See the following table. Table 1. Job Configuration Settings Field Description Job Id Displays the job ID that is created when the job is
                                                      						  submitted. Job Status Displays the status of the job from one of the following
                                                      						  options: Hold Pending Completed Incomplete Scheduled Date Time Choose the month, date, year from the drop-down list
                                                      						  boxes. Enter the time when you want the job to be scheduled. Submit Date Time Displays the date and time when the job was submitted. Sequence Choose from the drop-down list box, the sequence in which
                                                      						  the job should be run. You can choose a number between 1 and 20. Note If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. Job Description Displays the description you entered when the job was
                                                      						  created. This description can be edited to include up to 50 characters in any
                                                      						  language, but it cannot include double-quotes ( " ), percentage
                                                      						  sign ( % ), ampersand (&), back-slash ( \ ),
                                                      						  or angle brackets (<>). Frequency Choose from the following options, the frequency of the
                                                      						  transaction: Once Monthly Weekly Daily Hourly For example, if you choose Daily, the transaction will be
                                                      						  repeated daily at the time entered in the Schedule Time and Date field. Job End Time Displays the end time for recurring (frequency) job. Last Modified By Displays the user ID of the administrator who last
                                                      						  modified this job. | Field | Description | Job Id | Displays the job ID that is created when the job is
                                                      						  submitted. | Job Status | Displays the status of the job from one of the following
                                                      						  options: Hold Pending Completed Incomplete | Scheduled Date Time | Choose the month, date, year from the drop-down list
                                                      						  boxes. Enter the time when you want the job to be scheduled. | Submit Date Time | Displays the date and time when the job was submitted. | Sequence | Choose from the drop-down list box, the sequence in which
                                                      						  the job should be run. You can choose a number between 1 and 20. Note If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. | Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. | Job Description | Displays the description you entered when the job was
                                                      						  created. This description can be edited to include up to 50 characters in any
                                                      						  language, but it cannot include double-quotes ( " ), percentage
                                                      						  sign ( % ), ampersand (&), back-slash ( \ ),
                                                      						  or angle brackets (<>). | Frequency | Choose from the following options, the frequency of the
                                                      						  transaction: Once Monthly Weekly Daily Hourly For example, if you choose Daily, the transaction will be
                                                      						  repeated daily at the time entered in the Schedule Time and Date field. | Job End Time | Displays the end time for recurring (frequency) job. | Last Modified By | Displays the user ID of the administrator who last
                                                      						  modified this job. |
| Field | Description |
| Job Id | Displays the job ID that is created when the job is
                                                      						  submitted. |
| Job Status | Displays the status of the job from one of the following
                                                      						  options: Hold Pending Completed Incomplete |
| Scheduled Date Time | Choose the month, date, year from the drop-down list
                                                      						  boxes. Enter the time when you want the job to be scheduled. |
| Submit Date Time | Displays the date and time when the job was submitted. |
| Sequence | Choose from the drop-down list box, the sequence in which
                                                      						  the job should be run. You can choose a number between 1 and 20. Note If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. | Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. |
| Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. |
| Job Description | Displays the description you entered when the job was
                                                      						  created. This description can be edited to include up to 50 characters in any
                                                      						  language, but it cannot include double-quotes ( " ), percentage
                                                      						  sign ( % ), ampersand (&), back-slash ( \ ),
                                                      						  or angle brackets (<>). |
| Frequency | Choose from the following options, the frequency of the
                                                      						  transaction: Once Monthly Weekly Daily Hourly For example, if you choose Daily, the transaction will be
                                                      						  repeated daily at the time entered in the Schedule Time and Date field. |
| Job End Time | Displays the end time for recurring (frequency) job. |
| Last Modified By | Displays the user ID of the administrator who last
                                                      						  modified this job. |
| Step 3 | Click Activate job to activate the job at the
                                       			 scheduled time or click Save to save the configuration settings to
                                       			 activate the job at a later time. The Find and List Jobs window displays. Note If a Job is saved, but not activated then status of the job will
                                                      				  be displayed as Hold. These jobs will not be processed by BPS unless they are
                                                      				  activated. | Note | If a Job is saved, but not activated then status of the job will
                                                      				  be displayed as Hold. These jobs will not be processed by BPS unless they are
                                                      				  activated. |
| Note | If a Job is saved, but not activated then status of the job will
                                                      				  be displayed as Hold. These jobs will not be processed by BPS unless they are
                                                      				  activated. |
| Step 4 | Click the job ID for the job you have activated. In the Job Configuration window, the following
                                       			 information displays in the Job Results area, for all jobs that are
                                       			 complete, incomplete, stop requested, or processing. Job Launched Date Time Job Result Status Number of records
                                             				  Processed Number of Records
                                             				  Failed Total Number of
                                             				  Records Log File Name Note Click on the link in the Log File Name column to view the log
                                                            						file for this transaction. | Note | Click on the link in the Log File Name column to view the log
                                                            						file for this transaction. |
| Note | Click on the link in the Log File Name column to view the log
                                                            						file for this transaction. |

| Field | Description |
|---|---|
| Job Id | Displays the job ID that is created when the job is
                                                      						  submitted. |
| Job Status | Displays the status of the job from one of the following
                                                      						  options: Hold Pending Completed Incomplete |
| Scheduled Date Time | Choose the month, date, year from the drop-down list
                                                      						  boxes. Enter the time when you want the job to be scheduled. |
| Submit Date Time | Displays the date and time when the job was submitted. |
| Sequence | Choose from the drop-down list box, the sequence in which
                                                      						  the job should be run. You can choose a number between 1 and 20. Note If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. | Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. |
| Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. |
| Job Description | Displays the description you entered when the job was
                                                      						  created. This description can be edited to include up to 50 characters in any
                                                      						  language, but it cannot include double-quotes ( " ), percentage
                                                      						  sign ( % ), ampersand (&), back-slash ( \ ),
                                                      						  or angle brackets (<>). |
| Frequency | Choose from the following options, the frequency of the
                                                      						  transaction: Once Monthly Weekly Daily Hourly For example, if you choose Daily, the transaction will be
                                                      						  repeated daily at the time entered in the Schedule Time and Date field. |
| Job End Time | Displays the end time for recurring (frequency) job. |
| Last Modified By | Displays the user ID of the administrator who last
                                                      						  modified this job. |

| Note | If the scheduled date and time is same for two or more
                                                                  							 jobs, then the jobs are queued in BPS according the sequence number. If the
                                                                  							 scheduled date and time, and Sequence is same, then the jobs are queued
                                                                  							 depending on the submitted date and time. |
|---|---|

| Note | If a Job is saved, but not activated then status of the job will
                                                      				  be displayed as Hold. These jobs will not be processed by BPS unless they are
                                                      				  activated. |
|---|---|

| Note | Click on the link in the Log File Name column to view the log
                                                            						file for this transaction. |
|---|---|