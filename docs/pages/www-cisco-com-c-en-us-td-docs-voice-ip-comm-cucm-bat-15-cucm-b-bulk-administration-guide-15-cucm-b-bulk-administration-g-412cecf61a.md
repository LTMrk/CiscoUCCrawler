---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-412cecf61a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_011111.html
retrieved_at: 2026-08-21T09:18:15.774105+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Manager and Assistant Deletions

## Chapter: Manager and Assistant Deletions

- Manager and Assistant Deletions

- Delete Specific Manager-Assistant Associations From Cisco Unified Communications Manager

# Manager and Assistant Deletions

This chapter provides information to use Unified Communications Manager Bulk Administration (BAT) to delete a specific manager-assistant association from the Unified Communications Manager database.

## Delete Specific Manager-Assistant Associations From Cisco Unified Communications Manager

You can delete specific manager-assistant associations from Cisco Unified Communications Manager .

### Before you begin

You must have a CSV data file that contains the user IDs for
                              		  the specific managers and assistants associations that you want to delete.

For example, the assistant with the user ID, jmorgan, is assigned to
                              		  two managers with user IDs, rcraig and dbaker. If you want to change the
                              		  manager-assistant association, so the assistant, jmorgan is only assigned to
                              		  rcraig, you can delete the jmorgan-dbaker association by creating a CSV data
                              		  file with the following entry:

Step 1

Choose Bulk
                                             				  Administration > Managers/Assistants > Delete
                                             				  Managers/Assistants .

Step 2

In the File Name field, choose the CSV file that you
                                       			 created for this type of bulk transaction.

Step 3

Choose the type of deletion:

- Delete
                                          				associated assistants for one manager

- Delete
                                          				associated managers for one assistant

Step 4

In the Job Information area, enter the Job description.

Step 5

Choose a delete method. Do one of the following:

Click Run Immediately to delete the
                                             				  manager-assistant associations immediately.

Click Run Later to delete the manager-assistant
                                             				  associations at a later time.

Step 6

Click Submit to create a job for deleting the
                                       			 required manager-assistant associations.

| Step 1 | Choose Bulk
                                             				  Administration > Managers/Assistants > Delete
                                             				  Managers/Assistants . The Delete Managers/Assistants Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV file that you
                                       			 created for this type of bulk transaction. |
| Step 3 | Choose the type of deletion: Delete
                                          				associated assistants for one manager Delete
                                          				associated managers for one assistant |
| Step 4 | In the Job Information area, enter the Job description. |
| Step 5 | Choose a delete method. Do one of the following: Click Run Immediately to delete the
                                             				  manager-assistant associations immediately. Click Run Later to delete the manager-assistant
                                             				  associations at a later time. |
| Step 6 | Click Submit to create a job for deleting the
                                       			 required manager-assistant associations. Use the Job Configuration window to schedule
                                       			 and / or activate this job. |