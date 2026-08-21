---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-c8779db39e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_0110110.html
retrieved_at: 2026-08-21T17:53:12.135330+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Forced Authorization Codes and Client Matter Code Deletions

## Chapter: Forced Authorization Codes and Client Matter Code Deletions

# Forced Authorization Codes and Client Matter Code Deletions

This chapter provides information to delete CMC and FAC codes
                        		from the system using a custom file that contains the codes that you want to
                        		delete. You can edit a custom file where you previously inserted or updated
                        		authorization codes, or you can create a new CSV file where you manually enter
                        		the codes that you want to delete.

## Code Setting Deletion Examples

If you plan to edit an existing CSV file, you must update the
                              		  file, so only the lines that contain the codes that you want to delete remain
                              		  in the file.

### Example for CMC (Existing CSV File)

You obtain a file that contains the following information,
                              		  and you decide to delete the client matter codes, 5550, 5551, and 5555:

5550,Phil Jones DDS

5551,Southwest Shades

5552,Happy Pharmaceuticals

5553,Weddings by Joyce

5554,Peterson Plumbing

5555,Acme Toys

5556,Chicago Paralegals

Before you delete the entries, the file must contain only the
                              		  following entries:

5550,Phil Jones DDS

5551,Southwest Shades

5555,Acme Toys

### Example for CMC (New CSV File)

If you create a new file to delete the codes, list only the
                              		  codes, separated by lines, as shown in the following example:

5550

5551

5555

### Example for FAC (Existing CSV File)

You obtain a file that contains the following information,
                              		  and you decide to delete the authorization codes that are assigned to John,
                              		  Dave, and Bill:

1233,Sandy Brown,30

1234,John Smith,20

1235,Dave Green,30

1236,John David,20

1237,Alex Anderson,30

1238,Bill Jones,20

1239,Jennifer Summers,20

Before you can delete the entries for John, Dave, and Bill,
                              		  the file must contain only the following entries:

1234,John Smith,20

1235,Dave Green,30

1238,Bill Jones,20

### Example for FAC (New File)

If you create a new file to delete the codes, list only the
                              		  codes, separated by lines, as shown in the following example:

1234

1235

1238

## Delete Forced Authorization Codes and Client Matter Codes

You can delete CMC and FAC records using a custom CSV file.

Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the CMC or FAC records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for codes.

### Before you begin

- For CMC, see Example for CMC (New CSV File) .

- For FAC, see Example for FAC (Existing CSV File) .

- On the Cisco Unified Communications Manager server download the appropriate CSV files from
                                 			 the first node of the Cisco Unified Communications Manager server. For more information, see Download File Off Server .

- In a text editor, open and
                                 			 edit the existing CSV file to delete the entries.

- Upload the modified CSV
                                 			 files to the first node of the Cisco Unified Communications Manager server. For more information, see Upload File to Server :

In Cisco Unified Communications Manager Administration, choose one of the following
                                       			 options, depending on whether you plan to delete client matter codes or forced
                                       			 authorization codes:

For CMC, choose Bulk
                                                   						Administration > Client Matter
                                                   						Codes > Delete Client Matter
                                                   						Codes

For FAC, choose Bulk
                                                   						Administration > Forced Authorization
                                                   						Codes > Delete Forced Authorization
                                                   						Codes

Choose a custom file from the drop-down list box and click Find .

In the Job Information area, enter the Job
                                       			 description.

Choose a delete method. Do one of the following:

Click Run Immediately to delete CMC or FAC
                                             				  immediately.

Click Run Later to delete CMC or FAC at a later
                                             				  time.

Click Submit to create a job for deleting FAC and
                                       			 CMC.

Make sure that you browse the entire list of the displayed
                                                      				  results before submitting the job for deletion.

## Topics Related to Forced Authorization Codes and Client Matter Codes

| Note | Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the CMC or FAC records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for codes. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, choose one of the following
                                       			 options, depending on whether you plan to delete client matter codes or forced
                                       			 authorization codes: For CMC, choose Bulk
                                                   						Administration > Client Matter
                                                   						Codes > Delete Client Matter
                                                   						Codes For FAC, choose Bulk
                                                   						Administration > Forced Authorization
                                                   						Codes > Delete Forced Authorization
                                                   						Codes |
|---|---|
| Step 2 | Choose a custom file from the drop-down list box and click Find . The Find and List Client Matter Codes window or Find and List Forced Authorization window
                                       			 displays. |
| Step 3 | In the Job Information area, enter the Job
                                       			 description. |
| Step 4 | Choose a delete method. Do one of the following: Click Run Immediately to delete CMC or FAC
                                             				  immediately. Click Run Later to delete CMC or FAC at a later
                                             				  time. |
| Step 5 | Click Submit to create a job for deleting FAC and
                                       			 CMC. Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. Caution Make sure that you browse the entire list of the displayed
                                                      				  results before submitting the job for deletion. | Caution | Make sure that you browse the entire list of the displayed
                                                      				  results before submitting the job for deletion. |
| Caution | Make sure that you browse the entire list of the displayed
                                                      				  results before submitting the job for deletion. |

| Caution | Make sure that you browse the entire list of the displayed
                                                      				  results before submitting the job for deletion. |
|---|---|