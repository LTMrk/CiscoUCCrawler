---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-c1b31e73b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_0100010.html
retrieved_at: 2026-08-21T17:51:47.997395+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Manager and Assistant Report Generation

## Chapter: Manager and Assistant Report Generation

# Manager and Assistant Report Generation

This chapter provides information about generating reports for
                        		Cisco Unified CM Assistant managers and assistants. The reports follow a fixed
                        		format. You can generate a report by specifying a set of query options for
                        		either managers or assistants.

## Generate Reports for Cisco Unified Communications Manager Assistant Managers and Assistants

You can generate reports for managers or assistants.

Choose one of these options:

To generate a manager report, choose Bulk
                                                   						Administration > Managers/Assistants > Generate
                                                   						Manager Reports .

To generate an assistant report, choose Bulk
                                                   						Administration > Managers/Assistants > Generate
                                                   						Assistant Reports .

You can generate a report for all managers or assistants by not
                                       			 specifying a query, or you can generate a report for specific managers or
                                       			 assistants by using following steps:

In Find Managers (or Assistants) where
                                             				  drop-down list box, choose from these query options:

- User ID

- First Name

- Middle Name

- Last Name

- Department

In the second drop-down list box, choose from the following
                                             				  options:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

In the search field box, enter the value that you want to
                                             				  locate, such as the exact user ID or the last name of a user, and click Find .

You can add multiple values to the search field box by
                                                					 separating them with a comma as shown in this example: JohnJ, PaulP, SueS, JoeJ

To further define your query, you can choose AND or OR to add multiple filters and repeat steps 2.a through 2.c .

To choose details for your type of report, click Next .

In the File Name field, enter your name for this
                                       			 report (required).

In the File Format field, select a file format from
                                       			 the drop-down list box.

In the Job Information area, enter the Job description.

Choose a method to generate reports. Do one of the following:

Click Run Immediately to generate reports
                                             				  immediately.

Click Run Later to generate reports at a later
                                             				  time.

To create a job for generating reports, click Submit .

### What to do next

You can search and download the report file using the
                              		  Upload / Download Files option in the Bulk Administration menu.

## Report Log Files

BAT generates log files for each report transaction and
                              		  stores them on the first node of Cisco Unified Communications Manager server. You can find a link to log files from
                              		  the Job Configuration window for any job that
                              		  generated a report. Click the link in the Log File Name column that corresponds to the job
                              		  with the log file you want to view.

## Topics Related to Manager Assistant Report Generation

Generate Reports for Cisco Unified Communications Manager Assistant Managers and Assistants

BAT Log Files

Manage Scheduled Jobs

| Step 1 | Choose one of these options: To generate a manager report, choose Bulk
                                                   						Administration > Managers/Assistants > Generate
                                                   						Manager Reports . The Manager Reports window displays. To generate an assistant report, choose Bulk
                                                   						Administration > Managers/Assistants > Generate
                                                   						Assistant Reports . The Assistant Reports window displays. |
|---|---|
| Step 2 | You can generate a report for all managers or assistants by not
                                       			 specifying a query, or you can generate a report for specific managers or
                                       			 assistants by using following steps: In Find Managers (or Assistants) where
                                             				  drop-down list box, choose from these query options: User ID First Name Middle Name Last Name Department In the second drop-down list box, choose from the following
                                             				  options: begins with contains is exactly ends with is empty is not empty In the search field box, enter the value that you want to
                                             				  locate, such as the exact user ID or the last name of a user, and click Find . You can add multiple values to the search field box by
                                                					 separating them with a comma as shown in this example: JohnJ, PaulP, SueS, JoeJ Note To further define your query, you can choose AND or OR to add multiple filters and repeat steps 2.a through 2.c . | Note | To further define your query, you can choose AND or OR to add multiple filters and repeat steps 2.a through 2.c . |
| Note | To further define your query, you can choose AND or OR to add multiple filters and repeat steps 2.a through 2.c . |
| Step 3 | To choose details for your type of report, click Next . Tip If you want to change the type of query,
                                                   				click Back . | Tip | If you want to change the type of query,
                                                   				click Back . |
| Tip | If you want to change the type of query,
                                                   				click Back . |
| Step 4 | In the File Name field, enter your name for this
                                       			 report (required). |
| Step 5 | In the File Format field, select a file format from
                                       			 the drop-down list box. |
| Step 6 | In the Job Information area, enter the Job description. |
| Step 7 | Choose a method to generate reports. Do one of the following: Click Run Immediately to generate reports
                                             				  immediately. Click Run Later to generate reports at a later
                                             				  time. |
| Step 8 | To create a job for generating reports, click Submit . Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. Cisco Unified Communications Manager Bulk Administration (BAT) saves the
                                       			 report file on the first node of the Cisco Unified Communications Manager server. |

| Note | To further define your query, you can choose AND or OR to add multiple filters and repeat steps 2.a through 2.c . |
|---|---|

| Tip | If you want to change the type of query,
                                                   				click Back . |
|---|---|