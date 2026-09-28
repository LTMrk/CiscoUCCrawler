---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b06updn-html-6c3b405444
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b06updn.html
retrieved_at: 2026-08-21T16:13:21.636094+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Uploading and Downloading Files

## Chapter: Uploading and Downloading Files

## Uploading and Downloading Files

This chapter describes the procedures to upload files to the Cisco Unified Presence Server first node and download files these files to a local machine.

Use the following procedures:

• Finding a File

• Downloading a File

• Uploading a File

• Deleting a File

## Finding a File

Use the following procedure to find files that you can download from the server for the Cisco Unified Presence Server.

Step 1 Choose Bulk Administration > Upload/Download Files . The Find and List Files window displays.

Step 2 From the first Find File where drop-down list box, choose one of the following options:

• Name

• Type

Step 3 From the second Find Job where drop-down list box, choose one of the following options:

• If you chose Name in Step 2 , chose one of the following options and continue with Step 4 :

– begins with

– contains

– is exactly

– ends with

– is empty

– is not empty

• If you chose Type in Step 2 , continue with Step 4 .

Step 4 Specify the appropriate search text, if applicable.

Tip To find all files that are registered in the database, click Find without entering any search text.

Step 5 To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Steps 2 through 4 .

Step 6 If you chose Type in Step 2 , from the Select item or enter search text drop-down list box, choose one of the following options:

• Insert Files

• Export Files

• Report Files

• Custom Files

• Log Files

• BAT Excel Template

Step 7 Click Find .

A list of discovered files displays by

• File Name

• Function Type

If you chose Type in Step 2 and Log Files in Step 6 , the list of discovered files displays by:

• File Name

• Launch Date and Time

To download a file(s) that you chose, see "Downloading a File" section .

Additional Topics

See the "Related Topics" section .

## Downloading a File

Use the following procedure to download a file from the Cisco Unified Presence Server.

Step 1 Find the files that you want to download by using the "Finding a File" section .

Step 2 Check the check boxes that correspond to the files that you want to download and click Download Selected .

Note You can download all the files by clicking Select All and then clicking Download Selecte d.

Note If you select more than one file at a time to download, the files will get downloaded to a common zip file.

Step 3 The File Download pop-up window displays. Click Save .

Step 4 In the Save As pop-up window, choose the location where you want to save the file to and click Save.

Step 5 The Download Complete pop-up window displays. Click Open to open the downloaded file or click Close to open it at a later time.

Additional Topics

See the "Related Topics" section .

## Uploading a File

Use the following procedure to upload a file to the Cisco Unified Presence Server.

Step 1 Choose Bulk Administration > Upload/Download Files . The Find and List Files window displays.

Step 2 Click Add New . The File Upload Configuration window displays.

Step 3 In the File text box, enter the full path of the file that you want to upload or click Browse and locate the file.

Step 4 From the Select the Target drop-down list box, choose the target for which you want to use the file.

Step 5 From the Transaction Type drop-down list box, choose the transaction type that the file defines.

Step 6 If you want to overwrite an existing file with the same name, check the Overwrite File if it Exists check box.

Step 7 Click Save . The status displays that the upload is successful.

Additional Topics

See the "Related Topics" section .

## Deleting a File

Use the following procedure to delete files.

Step 1 Find the files that you want to delete by using the "Finding a File" section .

Step 2 In the Search Results area, check the check box that corresponds to the files that you want to delete.

Step 3 Click Delete Selected .

Note To delete all files that display in the Search Results area, click Select All and Delete Selected .

Step 4 To continue, click OK .

Step 5 The files are now deleted from the server.

Note If any files that you chose for deletion are being used to execute any jobs, these file will not get deleted.

Additional Topics

See the "Related Topics" section .

## Related Topics

• Finding a File

• Downloading a File

• Uploading a File

• Deleting a File