---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-3fff9d3618
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01001010.html
retrieved_at: 2026-08-21T08:50:48.938034+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: License Updates and Exports Using CUP Menu

## Chapter: License Updates and Exports Using CUP Menu

# License Updates and Exports Using CUP Menu

This chapter provides information to use the CUPS menu in BAT to update
                        		and export licenses of all Unified Presence and Cisco Unified Personal
                        		Communicator users.

Cisco Unified Presence, a critical component for delivering the
                        		full value of a Cisco Unified Communications environment, collects information
                        		about user availability. Using this information, applications such as Cisco
                        		Unified Personal Communicator and Cisco Unified Communications Manager can improve productivity by determining the
                        		most effective way for collaborative communication.

## Update and Export CUP and CUPC User Licenses

You can use the CUPS menu in BAT to update and export CUPS and
                              		  CUPC user licenses.

Choose from the following options:

To update CUPS/CUPC Users, choose Bulk
                                                   						Administration > CUPS > Update
                                                   						CUPS/CUPC Users

To export CUPS/CUPC Users, choose Bulk
                                                   						Administration > CUPS > Export
                                                   						CUPS/CUPC Users

### Add or Update CUPS and CUPC User Licenses

You can use BAT to add or change the license.

Use the Upload/Download Files window to upload the csv
                                          			 file.

You must ensure that you select the correct BAT target and
                                                         				  transaction type while you are uploading the csv file.

Navigate to the Update CUPS window, select the csv file that is
                                          			 uploaded, and submit the job.

You can choose to run the job immediately or later by clicking
                                                         				  the respective radio button. If you choose Run Later , you need to use the Job
                                                         				  Scheduler window to schedule and activate this job.

Use the Job Scheduler window to monitor the progress
                                          			 of the BAT job that is submitted.

### Export All CUPS/CUPC User License Information

You can use the Export Users Query window can be used to obtain the current license information about all users
                                 		  for Unified Presence and Cisco Unified Personal Communicator.

No option currently exists to select a subset of Unified Presence
                                             			 users; all Unified Presence users in the system get exported to file.

Navigate to the Export Users Query window.

To view the basic user information and their license status, click Find .

To view the Export window for CUPS/CUPC, click Next .

Specify the file name to be exported and click Submit to start the BAT job.

Go to the Job Scheduler window to view the status of the
                                          			 BAT job that is submitted.

After the job completes, you can go to the Upload/Download Files window to download the
                                                         				  exported .csv file.

| Choose from the following options: To update CUPS/CUPC Users, choose Bulk
                                                   						Administration > CUPS > Update
                                                   						CUPS/CUPC Users To export CUPS/CUPC Users, choose Bulk
                                                   						Administration > CUPS > Export
                                                   						CUPS/CUPC Users |
|---|

| Step 1 | Use the Upload/Download Files window to upload the csv
                                          			 file. Note You must ensure that you select the correct BAT target and
                                                         				  transaction type while you are uploading the csv file. | Note | You must ensure that you select the correct BAT target and
                                                         				  transaction type while you are uploading the csv file. |
|---|---|---|---|
| Note | You must ensure that you select the correct BAT target and
                                                         				  transaction type while you are uploading the csv file. |
| Step 2 | Navigate to the Update CUPS window, select the csv file that is
                                          			 uploaded, and submit the job. Note You can choose to run the job immediately or later by clicking
                                                         				  the respective radio button. If you choose Run Later , you need to use the Job
                                                         				  Scheduler window to schedule and activate this job. | Note | You can choose to run the job immediately or later by clicking
                                                         				  the respective radio button. If you choose Run Later , you need to use the Job
                                                         				  Scheduler window to schedule and activate this job. |
| Note | You can choose to run the job immediately or later by clicking
                                                         				  the respective radio button. If you choose Run Later , you need to use the Job
                                                         				  Scheduler window to schedule and activate this job. |
| Step 3 | Use the Job Scheduler window to monitor the progress
                                          			 of the BAT job that is submitted. |

| Note | You must ensure that you select the correct BAT target and
                                                         				  transaction type while you are uploading the csv file. |
|---|---|

| Note | You can choose to run the job immediately or later by clicking
                                                         				  the respective radio button. If you choose Run Later , you need to use the Job
                                                         				  Scheduler window to schedule and activate this job. |
|---|---|

| Note | No option currently exists to select a subset of Unified Presence
                                             			 users; all Unified Presence users in the system get exported to file. |
|---|---|

| Step 1 | Navigate to the Export Users Query window. |
|---|---|
| Step 2 | To view the basic user information and their license status, click Find . |
| Step 3 | To view the Export window for CUPS/CUPC, click Next . |
| Step 4 | Specify the file name to be exported and click Submit to start the BAT job. |
| Step 5 | Go to the Job Scheduler window to view the status of the
                                          			 BAT job that is submitted. Note After the job completes, you can go to the Upload/Download Files window to download the
                                                         				  exported .csv file. | Note | After the job completes, you can go to the Upload/Download Files window to download the
                                                         				  exported .csv file. |
| Note | After the job completes, you can go to the Upload/Download Files window to download the
                                                         				  exported .csv file. |

| Note | After the job completes, you can go to the Upload/Download Files window to download the
                                                         				  exported .csv file. |
|---|---|