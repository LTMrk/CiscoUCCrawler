---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b06usupd-html-c41b4e6c7f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b06usupd.html
retrieved_at: 2026-08-21T16:13:29.554763+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: UPS User Update

## Chapter: UPS User Update

- Updating Users in Cisco Unified Presence Server

- Related Topic

## UPS User Update

You can use Cisco Unified Presence Server Bulk Administration (BAT) to update a group of users in the Cisco Unified Presence Server directory.

## Updating Users in Cisco Unified Presence Server

To update a group of users in the Cisco Unified Presence Server directory, use the following procedure.

Before You Begin

You must have a CSV data file that contains the user names, controlled device names, and directory numbers. You can create the CSV data file by using one of these methods:

• BAT spreadsheet that is converted to CSV format

• Export utility that produces an export file of user data

If you are updating files that are generated with the export utility, insert the files in descending order based on the _MgrLevel# suffix, where # is 1 through 20. Insert the file with the _user suffix last to ensure that the user record for a manager exists prior to use of the User ID for a manager in the Manager User ID field.

Step 1 Choose Bulk Administration > PS > UPS User Update .

The CUPS User Update Configuration window displays.

Step 2 In the File Name field, choose the CSV data file that you created for this bulk transaction.

Step 3 In the Job Information area, enter the job description.

Step 4 To insert the user records immediately, click the Run Immediately radio button, or click Run Later to insert the user records at a later time.

Step 5 To create a job for inserting the user records, click Submit .

Step 6 Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job.

## Related Topic

• Updating Users in Cisco Unified Presence Server