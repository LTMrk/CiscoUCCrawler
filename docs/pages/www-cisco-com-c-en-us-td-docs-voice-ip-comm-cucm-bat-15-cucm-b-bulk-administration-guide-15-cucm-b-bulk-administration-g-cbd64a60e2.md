---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-cbd64a60e2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_0100001.html
retrieved_at: 2026-08-21T09:18:24.690747+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Assistant Deletions

## Chapter: Assistant Deletions

# Assistant Deletions

This chapter provides information to delete assistants from the Unified Communications Manager database and LDAP Directory. You can use either a query search or a custom file to locate existing records to delete.

## Assistant Deletions From Cisco Unified Communications Manager

When you delete Unified CM Assistant assistants from the Cisco Unified Communications Manager database and LDAP Directory, Cisco Unified Communications Manager maintains information on the assistant as a user in the directory. For example, Assistant thudson is assigned to two managers,
                              hart and dstewart. You can disassociate thudson from both managers by deleting thudson as an assistant in the Cisco Unified Communications Manager database. The directory still shows thudson as a user.

You can use either a query search or a custom file to locate existing
                              		  records to delete.

### Delete Assistants Associations Using Query

You can delete assistants from their associations with managers from the Cisco Unified Communications Manager directory.

Step 1

Choose BATAdministration > Managers/Assistants > Delete
                                                				  Assistants > Query .

Step 2

From the first Find Assistants where drop-down list, choose one of the following criteria:

User ID

First Name

Middle Name

Last Name

Department

From the second Find Assistants where drop-down list box, choose one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 3

Specify the appropriate search text, if applicable, then click Find .

Tip

To find all assistants that are registered in the database,
                                                         				  click Find without entering any search text.

To choose assistants from more than one department, enter
                                                				  multiple departments in this field. For example, to choose managers from
                                                				  departments 12 and 24, enter 12, 24 in the third box instead of performing two
                                                				  operations.

To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, and repeat Step 2 and Step 3 .

A list of discovered assistants displays by:

User ID

First Name

Middle Name

Last Name

Department

Step 4

In the Job Information area, enter the Job
                                          			 description.

Step 5

Choose a delete method. Do one of the following:

Click Run Immediately to delete assistants
                                                				  immediately.

Click Run Later to delete assistants at a later
                                                				  time.

Step 6

Click Submit to create a job for deleting the chosen
                                          			 assistants.

### Delete Assistant Associations Using Custom File

You can delete assistants associations from the Cisco Unified Communications Manager database using a custom file that you create using a text-editor. Use the custom file to locate assistant associations that
                                 you want to delete.

Attention

#### Before you begin

Create a custom text-based CSV data file that lists user IDs for assistants that you want to delete. Make sure you put each
                                       user ID on a separate line.

Upload the custom file to the first node of Cisco Unified Communications Manager server.

Step 1

Choose BATAdministration > Managers/Assistants > Delete
                                                				  Assistants > Custom File .

Step 2

In Select Assistants where field, keep the
                                          			 identifier, User ID.

Step 3

In the second field, in Custom File drop-down list, choose the name of the custom file that you created for this transaction.

Step 4

Click Find .

Step 5

In the Job Information area, enter the Job
                                          			 description.

Step 6

Choose a delete method. Do one of the following:

Click Run Immediately to delete assistants
                                                				  immediately.

Click Run Later to delete assistants at a later
                                                				  time.

Step 7

Click Submit to create a job for deleting chosen
                                          			 assistants.

| Step 1 | Choose BATAdministration > Managers/Assistants > Delete
                                                				  Assistants > Query . |
|---|---|
| Step 2 | From the first Find Assistants where drop-down list, choose one of the following criteria: User ID First Name Middle Name Last Name Department From the second Find Assistants where drop-down list box, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, then click Find . Tip To find all assistants that are registered in the database,
                                                         				  click Find without entering any search text. To choose assistants from more than one department, enter
                                                				  multiple departments in this field. For example, to choose managers from
                                                				  departments 12 and 24, enter 12, 24 in the third box instead of performing two
                                                				  operations. To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, and repeat Step 2 and Step 3 . A list of discovered assistants displays by: User ID First Name Middle Name Last Name Department | Tip | To find all assistants that are registered in the database,
                                                         				  click Find without entering any search text. |
| Tip | To find all assistants that are registered in the database,
                                                         				  click Find without entering any search text. |
| Step 4 | In the Job Information area, enter the Job
                                          			 description. |
| Step 5 | Choose a delete method. Do one of the following: Click Run Immediately to delete assistants
                                                				  immediately. Click Run Later to delete assistants at a later
                                                				  time. |
| Step 6 | Click Submit to create a job for deleting the chosen
                                          			 assistants. Use the Job Configuration window to schedule
                                          			 and / or activate this job. |

| Tip | To find all assistants that are registered in the database,
                                                         				  click Find without entering any search text. |
|---|---|

| Attention | Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                          create a custom file with details of the assistant association records that need to be deleted. Use only this file for the
                                          delete transaction. |
|---|---|

| Note | The custom delete CSV data file does not need a header and you can enter values for assistants association IDs. |
|---|---|

| Step 1 | Choose BATAdministration > Managers/Assistants > Delete
                                                				  Assistants > Custom File . |
|---|---|
| Step 2 | In Select Assistants where field, keep the
                                          			 identifier, User ID. |
| Step 3 | In the second field, in Custom File drop-down list, choose the name of the custom file that you created for this transaction. |
| Step 4 | Click Find . |
| Step 5 | In the Job Information area, enter the Job
                                          			 description. |
| Step 6 | Choose a delete method. Do one of the following: Click Run Immediately to delete assistants
                                                				  immediately. Click Run Later to delete assistants at a later
                                                				  time. |
| Step 7 | Click Submit to create a job for deleting chosen
                                          			 assistants. Use the Job Configuration window to schedule
                                          			 and / or activate this job. |