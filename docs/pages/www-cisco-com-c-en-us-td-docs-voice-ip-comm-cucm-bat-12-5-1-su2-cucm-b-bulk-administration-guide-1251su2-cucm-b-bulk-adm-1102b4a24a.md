---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-1102b4a24a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_0100000.html
retrieved_at: 2026-08-21T08:47:51.635866+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Manager Deletions

## Chapter: Manager Deletions

# Manager Deletions

This chapter provides information to delete managers with all their manager-assistant associations from the Unified Communications Manager database and LDAP Directory. You can use either a query search or a custom file to locate existing records to delete.

## Manager Deletions From Cisco Unified Communications Manager

When you delete Unified CM Assistant managers with all their manager-assistant associations from the Unified Communications Manager database and LDAP Directory, Cisco Unified Communications Manager maintains information on the manager as a user in the directory. For example, if a manager with the user ID, rmartinez, has
                              two assistants with user IDs, dbell and jkent, you can disassociate rmartinez from both assistants by deleting rmartinez as
                              a manager in the Cisco Unified Communications Manager database. The directory still shows rmartinez as a user.

You can use either a query search or a custom file to locate existing
                              		  records to delete.

### Delete Manager Associations Using Query

You can delete managers from their associations with assistants from Cisco Unified Communications Manager directory, use this procedure.

Choose BAT Administration > Managers/Assistants > Delete
                                                				  Managers > Query .

From the first Find Managers where drop-down list box, choose
                                          			 one of the following criteria:

- User ID

- First Name

- Middle Name

- Last Name

- Department

From the second Find Managers where drop-down list box,
                                             				choose one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Specify the appropriate search text, if applicable, then click Find .

To find all managers that are registered in the database, click Find without entering any search text.

To choose managers from more than one department, enter
                                                				  multiple departments in this field. For example, to choose managers from
                                                				  departments 12 and 24, enter 12, 24 in the third box instead of performing two
                                                				  operations.

To further define your query and to add multiple filters,
                                                				  check the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 .

A list of discovered managers displays by

- User ID

- First Name

- Middle Name

- Last Name

- Department

In the Job Information area, enter the Job
                                          			 description.

Choose a delete method. Do one of the following:

Click Run Immediately to delete managers
                                                				  immediately.

Click Run Later to delete managers at a later
                                                				  time.

Click Submit to create a job for deleting the chosen
                                          			 managers.

### Delete Manager Associations Using Custom File

You can delete managers associations from the Cisco Unified Communications Manager database using a custom file that you create using a text-editor. Use the custom file to locate manager associations that
                                 you want to delete.

Do not use the insert or export transaction files that are created
                                             			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                             			 with details of the manager association records that need to be deleted. Use
                                             			 only this file for the delete transaction.

#### Before you begin

The custom delete CSV data file does not need a header and you
                                                   				  can enter values for manager association IDs.

- Upload the custom file to the first node of Cisco Unified Communications Manager server.

Choose BAT Administration > Managers/Assistants > Delete Managers > Custom File .

In Select managers where field, keep the
                                          			 identifier, User ID.

In the second field, in Custom File drop-down list box, choose the
                                          			 name of the custom file that you created for this transaction.

Click Find .

In the Job Information area, enter the Job description.

Choose a delete method. Do one of the following:

Click Run Immediately to delete managers
                                                				  immediately.

Click Run Later to delete manages at a later
                                                				  time.

Click Submit to create a job for deleting chosen
                                          			 managers.

## Topics Related to Manager Deletions

| Step 1 | Choose BAT Administration > Managers/Assistants > Delete
                                                				  Managers > Query . The Delete Managers Configuration window displays. |
|---|---|
| Step 2 | From the first Find Managers where drop-down list box, choose
                                          			 one of the following criteria: User ID First Name Middle Name Last Name Department From the second Find Managers where drop-down list box,
                                             				choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, then click Find . Tip To find all managers that are registered in the database, click Find without entering any search text. To choose managers from more than one department, enter
                                                				  multiple departments in this field. For example, to choose managers from
                                                				  departments 12 and 24, enter 12, 24 in the third box instead of performing two
                                                				  operations. To further define your query and to add multiple filters,
                                                				  check the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 . A list of discovered managers displays by User ID First Name Middle Name Last Name Department | Tip | To find all managers that are registered in the database, click Find without entering any search text. |
| Tip | To find all managers that are registered in the database, click Find without entering any search text. |
| Step 4 | In the Job Information area, enter the Job
                                          			 description. |
| Step 5 | Choose a delete method. Do one of the following: Click Run Immediately to delete managers
                                                				  immediately. Click Run Later to delete managers at a later
                                                				  time. |
| Step 6 | Click Submit to create a job for deleting the chosen
                                          			 managers. Use the Job Configuration window to schedule
                                          			 and / or activate this job. |

| Tip | To find all managers that are registered in the database, click Find without entering any search text. |
|---|---|

| Attention | Do not use the insert or export transaction files that are created
                                             			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                             			 with details of the manager association records that need to be deleted. Use
                                             			 only this file for the delete transaction. |
|---|---|

| Note | The custom delete CSV data file does not need a header and you
                                                   				  can enter values for manager association IDs. |
|---|---|

| Step 1 | Choose BAT Administration > Managers/Assistants > Delete Managers > Custom File . The Delete Managers Configuration window displays. |
|---|---|
| Step 2 | In Select managers where field, keep the
                                          			 identifier, User ID. |
| Step 3 | In the second field, in Custom File drop-down list box, choose the
                                          			 name of the custom file that you created for this transaction. |
| Step 4 | Click Find . The list of discovered managers displays. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose a delete method. Do one of the following: Click Run Immediately to delete managers
                                                				  immediately. Click Run Later to delete manages at a later
                                                				  time. |
| Step 7 | Click Submit to create a job for deleting chosen
                                          			 managers. Use the Job Configuration window to schedule
                                          			 and / or activate this job. |