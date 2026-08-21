---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b06usexp-html-e002a4a9ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b06usexp.html
retrieved_at: 2026-08-21T16:13:33.586369+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Export UPS Users

## Chapter: Export UPS Users

- Exporting User Records

- Related Topic

## Export UPS Users

When you use Cisco Unified Presence Server Bulk Administration to export user records, the export utility sorts users according to the organizational hierarchy in the database.

## Exporting User Records

Use this procedure to export User records from Cisco Unified Presence Server.

Step 1 Choose Bulk Administration > UPS > Export UPS Users .

The Export Users Query window displays.

Step 2 In the first Find User where drop-down list box, choose a field to query from the following options:

• User ID

• First Name

• Middle Name

• Last Name

• Manager

• Department

Step 3 In the second drop-down list box, choose from the following options:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 4 In the search field/list box, enter the value that you want to locate, such as a specific name or User ID.

Note To choose users from more than one department, enter multiple departments in this field. For example, to choose users from departments 12 and 34, enter 12, 34 in the third box instead of performing two operations.

Step 5 You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query.

Step 6 Click Find . The search results display.

Note To find all users that are registered in the database, click Find without entering any search text.

Step 7 Click Next .

Step 8 Enter the export users file name in the File Name text box.

Step 9 Choose file format from the File Format drop-down list box.

Step 10 In the Job Information area, enter the Job description.

Step 11 To export user records immediately, click the Run Immediately radio button, or click Run Later to export at a later time.

Step 12 To create a job for exporting user records, click Submit .

Step 13 Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or activate this job.

You can search and download the exported file by using the Upload/Download Files option in the Bulk Administration menu.

## Related Topic

• Exporting User Records