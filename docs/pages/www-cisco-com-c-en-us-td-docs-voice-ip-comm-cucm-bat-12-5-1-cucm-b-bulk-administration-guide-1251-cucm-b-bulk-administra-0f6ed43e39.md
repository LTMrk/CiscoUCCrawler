---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-0f6ed43e39
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0111101.html
retrieved_at: 2026-08-21T18:01:52.314959+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Region Matrix Updates

## Chapter: Region Matrix Updates

- Region Matrix Updates

- Populate and Depopulate Region Matrix

# Region Matrix Updates

This chapter provides information to use the Region Matrix menu
                        		in BAT to populate or depopulate the region matrix. The region tables define
                        		physical locations, whereas the region matrix tables define available bandwidth
                        		within (intra) and between (inter) regions.

## Populate and Depopulate Region Matrix

Use BAT to populate or depopulate the region matrix.

Step 1

Choose Bulk
                                             				  Administration > Region
                                             				  Matrix > Populate/Depopulate Region
                                             				  Matrix . The Region Matrix Configuration window
                                       			 displays.

Step 2

In the Region Matrix Options section, choose Populate Region Matrix or Depopulate Region Matrix based on what you want to
                                       			 do.

Step 3

In the Job Information section, enter a name for the
                                       			 job. This helps you to identify your job.

Step 4

Select Run now or Run later , depending upon when you want to run the job.

Step 5

Click the Submit button.

Step 6

View the Job Scheduler window to check the status of the
                                       			 job that you submitted.

Unlike other BAT processes, the progress of a job to populate or
                                                      				  depopulate the region matrix cannot be measured in terms of records passed,
                                                      				  failed, or processed. The results can be viewed only after the entire process
                                                      				  is complete.

The number of records criterion is not applicable to this
                                                      				  transaction.

An administrator can change the region bandwidth defaults,
                                          				however, this cannot be done through the BAT menu.

Choose System > Service
                                                            						Parameters in Cisco Unified Communications Manager to access the region bandwidth defaults. The
                                                      				  parameter type specifies Cisco Unified Communications Manager and the four parameters of interest comprise
                                                      				  part of the Clusterwide Parameters (System - Location and Region) section.

| Step 1 | Choose Bulk
                                             				  Administration > Region
                                             				  Matrix > Populate/Depopulate Region
                                             				  Matrix . The Region Matrix Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the Region Matrix Options section, choose Populate Region Matrix or Depopulate Region Matrix based on what you want to
                                       			 do. |
| Step 3 | In the Job Information section, enter a name for the
                                       			 job. This helps you to identify your job. |
| Step 4 | Select Run now or Run later , depending upon when you want to run the job. |
| Step 5 | Click the Submit button. |
| Step 6 | View the Job Scheduler window to check the status of the
                                       			 job that you submitted. You can use this window to reschedule the job if required. Note Unlike other BAT processes, the progress of a job to populate or
                                                      				  depopulate the region matrix cannot be measured in terms of records passed,
                                                      				  failed, or processed. The results can be viewed only after the entire process
                                                      				  is complete. Note The number of records criterion is not applicable to this
                                                      				  transaction. An administrator can change the region bandwidth defaults,
                                          				however, this cannot be done through the BAT menu. Note Choose System > Service
                                                            						Parameters in Cisco Unified Communications Manager to access the region bandwidth defaults. The
                                                      				  parameter type specifies Cisco Unified Communications Manager and the four parameters of interest comprise
                                                      				  part of the Clusterwide Parameters (System - Location and Region) section. | Note | Unlike other BAT processes, the progress of a job to populate or
                                                      				  depopulate the region matrix cannot be measured in terms of records passed,
                                                      				  failed, or processed. The results can be viewed only after the entire process
                                                      				  is complete. | Note | The number of records criterion is not applicable to this
                                                      				  transaction. | Note | Choose System > Service
                                                            						Parameters in Cisco Unified Communications Manager to access the region bandwidth defaults. The
                                                      				  parameter type specifies Cisco Unified Communications Manager and the four parameters of interest comprise
                                                      				  part of the Clusterwide Parameters (System - Location and Region) section. |
| Note | Unlike other BAT processes, the progress of a job to populate or
                                                      				  depopulate the region matrix cannot be measured in terms of records passed,
                                                      				  failed, or processed. The results can be viewed only after the entire process
                                                      				  is complete. |
| Note | The number of records criterion is not applicable to this
                                                      				  transaction. |
| Note | Choose System > Service
                                                            						Parameters in Cisco Unified Communications Manager to access the region bandwidth defaults. The
                                                      				  parameter type specifies Cisco Unified Communications Manager and the four parameters of interest comprise
                                                      				  part of the Clusterwide Parameters (System - Location and Region) section. |

| Note | Unlike other BAT processes, the progress of a job to populate or
                                                      				  depopulate the region matrix cannot be measured in terms of records passed,
                                                      				  failed, or processed. The results can be viewed only after the entire process
                                                      				  is complete. |
|---|---|

| Note | The number of records criterion is not applicable to this
                                                      				  transaction. |
|---|---|

| Note | Choose System > Service
                                                            						Parameters in Cisco Unified Communications Manager to access the region bandwidth defaults. The
                                                      				  parameter type specifies Cisco Unified Communications Manager and the four parameters of interest comprise
                                                      				  part of the Clusterwide Parameters (System - Location and Region) section. |
|---|---|