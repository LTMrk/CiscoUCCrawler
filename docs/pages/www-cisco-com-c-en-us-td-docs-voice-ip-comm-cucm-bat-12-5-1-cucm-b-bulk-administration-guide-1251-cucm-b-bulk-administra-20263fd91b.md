---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-20263fd91b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_010.html
retrieved_at: 2026-08-21T17:55:26.625511+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Upload and Download Files

## Chapter: Upload and Download Files

# Upload and Download Files

This chapter provides information to upload files to the Cisco Unified Communications Manager first node and download files to a local
                        		machine.

## Find Downloadable File on Server

Use the following procedure to find files that you can download from the Unified Communications Manager server.

Step 1

Choose Bulk Administration > Upload/Download Files .

Step 2

From the first Find File where drop-down list box, choose one
                                       			 of the following options:

- Name

- Type

Step 3

In the second Find Job where drop-down list, do one of the following:

If you chose Name in Step 2 , choose one of the following options and continue with Step 4 :

begins with

contains

is exactly

ends with

is empty

is not empty

If you chose Type in Step 2 , continue with Step 4 .

Step 4

Specify the appropriate search text, if applicable.

Tip

To find all files that are registered in the database, click Find without entering any search text.

Step 5

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 through Step 4 .

Step 6

If you chose Type in Step 2 ,
                                       			 from the Select item or enter search text drop-down
                                       			 list box, choose one of the following options:

- Insert
                                             				  Files

- Export
                                             				  Files

- Report
                                             				  Files

- Custom
                                             				  Files

- Log
                                             				  Files

- BAT
                                             				  Excel Template

Step 7

Click Find .

A list of discovered files displays by the following:

File Name

Function Type

If you chose Type in Step 2 ,
                                          				the list of discovered files displays by the following:

File Name

Launch Date and Time

### What to do next

You can download a file(s) that you chose.

## Download File Off Server

Use the following procedure to download a file from the Unified Communications Manager server.

Step 1

Find the files that you want to download.

Tip

Step 2

Check the check boxes corresponding to the files that you want to
                                       			 download and click Download Selected .

If you select more than one file to download at a time, the files
                                          				will be downloaded to a common zip file.

Tip

You can download all the files by clicking Select All and then clicking Download Selected .

Step 3

The File Download pop-up window displays. Click Save .

Step 4

In the Save As pop-up window, choose the location where
                                       			 you want to save the file and click Save .

Step 5

The Download Complete pop-up window displays. To
                                       			 open the downloaded file, click Open , or click Close to open it at a later time.

## Upload File to Server

Use the following procedure to upload a file to the Unified Communications Manager server.

The upload file format must always be using alphanumeric (a-z, A-Z and 0-9) characters. Valid characters include hyphens (-),
                                          dot (.), and underscore (_). Also, the file name should not begin with a dot nor contain double dots.

Step 1

Choose Bulk Administration > Upload/Download Files .

Step 2

Click Add New .

Step 3

In the File text box, enter the full path of the file that you want to upload or click Browse , and locate the file.

Step 4

From the Select the Target drop-down list, choose the target for which you want to use the file.

Step 5

From the Transaction Type drop-down list, choose the transaction type that the file defines.

Step 6

If you want to overwrite an existing file with the same name,
                                       			 check the Overwrite File if it Exists check box.

Step 7

Click Save . The status displays that the upload is
                                       			 successful.

## Delete File From Server

Use the following procedure to delete files from the Unified Communications Manager server. If you choose files to delete that are actively being used to execute jobs, those files will not get deleted.

Attention

Do not delete the BAT.xlt file.

Step 1

Find the files that you want to delete.

Step 2

In the Search Results area, check the check box that
                                       			 corresponds to the files that you want to delete.

Step 3

Click Delete Selected .

To delete all files that display in the Search Results area, click Select All and Delete Selected .

Step 4

To continue, click OK .

| Step 1 | Choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | From the first Find File where drop-down list box, choose one
                                       			 of the following options: Name Type |
| Step 3 | In the second Find Job where drop-down list, do one of the following: If you chose Name in Step 2 , choose one of the following options and continue with Step 4 : begins with contains is exactly ends with is empty is not empty If you chose Type in Step 2 , continue with Step 4 . |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all files that are registered in the database, click Find without entering any search text. | Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Step 5 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 through Step 4 . |
| Step 6 | If you chose Type in Step 2 ,
                                       			 from the Select item or enter search text drop-down
                                       			 list box, choose one of the following options: Insert
                                             				  Files Export
                                             				  Files Report
                                             				  Files Custom
                                             				  Files Log
                                             				  Files BAT
                                             				  Excel Template |
| Step 7 | Click Find . A list of discovered files displays by the following: File Name Function Type If you chose Type in Step 2 ,
                                          				the list of discovered files displays by the following: File Name Launch Date and Time |

| Tip | To find all files that are registered in the database, click Find without entering any search text. |
|---|---|

| Step 1 | Find the files that you want to download. Tip To find files on the server, see Find Downloadable File on Server . | Tip | To find files on the server, see Find Downloadable File on Server . |
|---|---|---|---|
| Tip | To find files on the server, see Find Downloadable File on Server . |
| Step 2 | Check the check boxes corresponding to the files that you want to
                                       			 download and click Download Selected . If you select more than one file to download at a time, the files
                                          				will be downloaded to a common zip file. Tip You can download all the files by clicking Select All and then clicking Download Selected . | Tip | You can download all the files by clicking Select All and then clicking Download Selected . |
| Tip | You can download all the files by clicking Select All and then clicking Download Selected . |
| Step 3 | The File Download pop-up window displays. Click Save . |
| Step 4 | In the Save As pop-up window, choose the location where
                                       			 you want to save the file and click Save . |
| Step 5 | The Download Complete pop-up window displays. To
                                       			 open the downloaded file, click Open , or click Close to open it at a later time. Note When using Windows, use the 7-Zip tool to extract zip files. | Note | When using Windows, use the 7-Zip tool to extract zip files. |
| Note | When using Windows, use the 7-Zip tool to extract zip files. |

| Tip | To find files on the server, see Find Downloadable File on Server . |
|---|---|

| Tip | You can download all the files by clicking Select All and then clicking Download Selected . |
|---|---|

| Note | When using Windows, use the 7-Zip tool to extract zip files. |
|---|---|

| Note | The upload file format must always be using alphanumeric (a-z, A-Z and 0-9) characters. Valid characters include hyphens (-),
                                          dot (.), and underscore (_). Also, the file name should not begin with a dot nor contain double dots. |
|---|---|

| Step 1 | Choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the File text box, enter the full path of the file that you want to upload or click Browse , and locate the file. |
| Step 4 | From the Select the Target drop-down list, choose the target for which you want to use the file. |
| Step 5 | From the Transaction Type drop-down list, choose the transaction type that the file defines. |
| Step 6 | If you want to overwrite an existing file with the same name,
                                       			 check the Overwrite File if it Exists check box. |
| Step 7 | Click Save . The status displays that the upload is
                                       			 successful. |

| Attention | Do not delete the BAT.xlt file. |
|---|---|

| Step 1 | Find the files that you want to delete. |
|---|---|
| Step 2 | In the Search Results area, check the check box that
                                       			 corresponds to the files that you want to delete. |
| Step 3 | Click Delete Selected . Note To delete all files that display in the Search Results area, click Select All and Delete Selected . | Note | To delete all files that display in the Search Results area, click Select All and Delete Selected . |
| Note | To delete all files that display in the Search Results area, click Select All and Delete Selected . |
| Step 4 | To continue, click OK . The files are now deleted from the server. |

| Note | To delete all files that display in the Search Results area, click Select All and Delete Selected . |
|---|---|