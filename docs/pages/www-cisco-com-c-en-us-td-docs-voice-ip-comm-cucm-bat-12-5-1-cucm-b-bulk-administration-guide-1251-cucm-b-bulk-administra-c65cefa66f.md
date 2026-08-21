---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-c65cefa66f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_010101.html
retrieved_at: 2026-08-21T17:56:46.650755+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Password and PIN
	 Resets

## Chapter: Password and PIN
	 Resets

# Password and PIN
                     	 Resets

This chapter provides
                        		information about how to reset user passwords used to log on to the
                        		CiscoUnifiedIPPhone User Options window and the extension mobility feature
                        		PINs used to log in to CiscoUnifiedIPPhones.

## Reset Passwords And
                        	 PINs

You can reset the password that
                              		  users use when they log on to the CiscoUnifiedIPPhone User Options window.
                              		  You can also reset the PINs for the extension mobility feature that users use
                              		  when they log in to CiscoUnifiedIPPhones. Use this action when you must
                              		  reset a group of users to a default password or to a default PIN without
                              		  updating any other attributes.

You can
                              		  choose users for resetting passwords and PINs using either a query search or a
                              		  custom file.

Be aware that the
                                          			 credential settings selected on the reset page apply to both the password and
                                          			 the pin.

### Reset User Password
                           	 and PIN Using Query

You can use
                                 		  a query to locate users and reset passwords and PINs to a default value.

Step 1

Choose Bulk
                                                				  Administration > Users > Reset Password/PIN > Query .

Step 2

To locate the
                                          			 users that you want to reset, define the query filter.

Step 3

From the first Find
                                             				User where drop-down list, choose one of the following criteria:

User ID

First Name

Middle Name

Last Name

Manager

Department

From the second Find
                                                				  User where drop-down list box, choose one of the following
                                             				criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

Specify the
                                          			 appropriate search text, if applicable, and click Find .

Tip

Step 5

To further
                                          			 define your query, you can choose AND or OR to add multiple filters and repeat Step 3 and Step 4 .

Step 6

Click Find .

A list of
                                             				discovered users displays by

User ID

First Name

Middle Name

Last Name

Manager

Department Name

LDAP Sync Status

Step 7

Click Next .

Step 8

Enter the values
                                          			 that you want to update for all the records that you defined in your query.

Password—Enter the default password that users use when they log on to the Cisco Unified IP Phone User Options window.

Confirm Password—Reenter the password.

PIN—Enter the default PIN for the extension mobility feature that users should use when they log in to a Cisco Unified IP
                                                   Phone.

Confirm PIN—Reenter the PIN.

Step 9

In the Job
                                             				Information area, enter the Job description.

Step 10

Choose a method
                                          			 to change passwords or PINs. Do one of the following:

Click Run
                                                   					 Immediately to change passwords or PINs immediately.

Click Run
                                                   					 Later to change them at a later time.

Step 11

To create a job
                                          			 for resetting passwords or PINs, click Submit .

Step 12

To schedule and
                                          			 activate this job, use the Job Scheduler option in the Bulk Administration main
                                          			 menu.

Tip

### Reset User Password
                           	 and PIN Using Custom File

To locate
                                 		  users and to reset passwords and PINs to default values, you can create a
                                 		  custom file of user IDs by using a text editor.

#### Before you begin

Create a text file that lists each user ID on a separate line for which you want to reset password or PIN.

Upload the custom file into first node.

Step 1

Choose Bulk
                                                				  Administration > Users > Reset Password/PIN > Custom
                                                				  File .

Step 2

In the Find and
                                             				List Users window, choose the field that you used in the custom file
                                          			 from the following options:

User ID

First Name

Middle Name

Last Name

Department

Step 3

In the In
                                             				Custom File drop-down list box, choose the filename for the custom
                                          			 file.

Step 4

Click Next .

Step 5

In the Reset
                                             				Password/PIN for Users window, enter the values that you want to
                                          			 update for all the records.

Password—Enter the default password that users use when they log on to the Cisco Unified IP Phone Self Care Portal window.

Confirm Password—Reenter the password.

PIN—Enter the default PIN for the extension mobility feature that users should use when they log in to a Cisco Unified IP
                                                   Phone.

Confirm PIN—Reenter the PIN.

Step 6

In the Job
                                             				Information area , enter the Job description.

Step 7

Choose a method
                                          			 to change passwords or PINs. Do one of the following:

Click Run
                                                   					 Immediately to change passwords or PINs immediately.

Click Run
                                                   					 Later to change them at a later time.

Step 8

To create a job
                                          			 for resetting passwords or PINs, click Submit .

Step 9

To schedule and
                                          			 activate this job, use the Job Scheduler option in the Bulk Administration main
                                          			 menu.

Tip

| Note | Be aware that the
                                          			 credential settings selected on the reset page apply to both the password and
                                          			 the pin. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Users > Reset Password/PIN > Query . |
|---|---|
| Step 2 | To locate the
                                          			 users that you want to reset, define the query filter. |
| Step 3 | From the first Find
                                             				User where drop-down list, choose one of the following criteria: User ID First Name Middle Name Last Name Manager Department From the second Find
                                                				  User where drop-down list box, choose one of the following
                                             				criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the
                                          			 appropriate search text, if applicable, and click Find . Note To choose users from more than one department, enter multiple departments separated with a comma in this field. For example,
                                                      to choose users from departments 12 and 14, enter 12, 14 in the third box instead of performing two operations. Tip To find all users that are registered in the database, click Find without entering any search text. | Note | To choose users from more than one department, enter multiple departments separated with a comma in this field. For example,
                                                      to choose users from departments 12 and 14, enter 12, 14 in the third box instead of performing two operations. | Tip | To find all users that are registered in the database, click Find without entering any search text. |
| Note | To choose users from more than one department, enter multiple departments separated with a comma in this field. For example,
                                                      to choose users from departments 12 and 14, enter 12, 14 in the third box instead of performing two operations. |
| Tip | To find all users that are registered in the database, click Find without entering any search text. |
| Step 5 | To further
                                          			 define your query, you can choose AND or OR to add multiple filters and repeat Step 3 and Step 4 . |
| Step 6 | Click Find . A list of
                                             				discovered users displays by User ID First Name Middle Name Last Name Manager Department Name LDAP Sync Status |
| Step 7 | Click Next . |
| Step 8 | Enter the values
                                          			 that you want to update for all the records that you defined in your query. Password—Enter the default password that users use when they log on to the Cisco Unified IP Phone User Options window. Confirm Password—Reenter the password. PIN—Enter the default PIN for the extension mobility feature that users should use when they log in to a Cisco Unified IP
                                                   Phone. Confirm PIN—Reenter the PIN. |
| Step 9 | In the Job
                                             				Information area, enter the Job description. |
| Step 10 | Choose a method
                                          			 to change passwords or PINs. Do one of the following: Click Run
                                                   					 Immediately to change passwords or PINs immediately. Click Run
                                                   					 Later to change them at a later time. |
| Step 11 | To create a job
                                          			 for resetting passwords or PINs, click Submit . |
| Step 12 | To schedule and
                                          			 activate this job, use the Job Scheduler option in the Bulk Administration main
                                          			 menu. To schedule and / or activate this job, use the Job Scheduler option in the Bulk Administration main menu. Tip The log file displays the number of users that were updated and the number of records that failed, including an error code. | Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |
| Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |

| Note | To choose users from more than one department, enter multiple departments separated with a comma in this field. For example,
                                                      to choose users from departments 12 and 14, enter 12, 14 in the third box instead of performing two operations. |
|---|---|

| Tip | To find all users that are registered in the database, click Find without entering any search text. |
|---|---|

| Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |
|---|---|

| Note | Do not use the insert or export transaction files that are created with bat.xlt for the reset transaction. Instead, you must
                                          create a custom file with details of the user records that need to be reset. Use only this file for the reset transaction.
                                          In this custom reset file, you do not need a header, and you can enter values for user ID. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Users > Reset Password/PIN > Custom
                                                				  File . |
|---|---|
| Step 2 | In the Find and
                                             				List Users window, choose the field that you used in the custom file
                                          			 from the following options: User ID First Name Middle Name Last Name Department |
| Step 3 | In the In
                                             				Custom File drop-down list box, choose the filename for the custom
                                          			 file. |
| Step 4 | Click Next . |
| Step 5 | In the Reset
                                             				Password/PIN for Users window, enter the values that you want to
                                          			 update for all the records. Password—Enter the default password that users use when they log on to the Cisco Unified IP Phone Self Care Portal window. Confirm Password—Reenter the password. PIN—Enter the default PIN for the extension mobility feature that users should use when they log in to a Cisco Unified IP
                                                   Phone. Confirm PIN—Reenter the PIN. |
| Step 6 | In the Job
                                             				Information area , enter the Job description. |
| Step 7 | Choose a method
                                          			 to change passwords or PINs. Do one of the following: Click Run
                                                   					 Immediately to change passwords or PINs immediately. Click Run
                                                   					 Later to change them at a later time. |
| Step 8 | To create a job
                                          			 for resetting passwords or PINs, click Submit . |
| Step 9 | To schedule and
                                          			 activate this job, use the Job Scheduler option in the Bulk Administration main
                                          			 menu. To schedule and / or activate this job, use the Job Scheduler option in the Bulk Administration main menu. Tip The log file displays the number of users that were updated and the number of records that failed, including an error code. | Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |
| Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |

| Tip | The log file displays the number of users that were updated and the number of records that failed, including an error code. |
|---|---|