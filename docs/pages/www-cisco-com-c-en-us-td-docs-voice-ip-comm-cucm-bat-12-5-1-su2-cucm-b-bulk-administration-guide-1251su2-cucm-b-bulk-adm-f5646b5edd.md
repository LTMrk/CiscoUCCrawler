---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-f5646b5edd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01001111.html
retrieved_at: 2026-08-21T08:51:09.756210+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Manage
	 Infrastructure Devices

## Chapter: Manage
	 Infrastructure Devices

# Manage
                     	 Infrastructure Devices

## Infrastructure
                        	 Device Setup Using BAT

You can create the CSV file for Infrastructure Device using
                              		  the BAT spreadsheet BAT.xlt.

The BAT.xlt file exists on the first node of the Cisco Unified
                                             				Communications Manager server; however, you normally do not have
                                          			 Microsoft Excel installed on the server. In that case, copy the file from the
                                          			 first node and move it to a local machine that has Microsoft Excel installed.

Choose Bulk Administration > Upload/Download Files .

Click Find and download the BAT.xlt file.

## Create
                        	 Infrastructure Device CSV Data File using BAT.xlt

Open a BAT.xlt
                                       			 spreadsheet that allows you to export or create a text-based CSV file.

Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns:

- Device Name

- IPv4 Address

- IPv6 Address

- BSSID

- Description

Click Export
                                          				to BAT Format.

Click OK to create a .txt file, which will be stored in
                                       			 your local workstation.

### Example:

### What to do next

Upload the created
                              		  file using Bulk
                                    				administration > Upload/Download Files .

## CSV Data File
                        	 Creation for Infrastructure Devices Using Text Editor

You can
                              		  create a CSV text file for Infrastructure Devices using a text editor, such as
                              		  Microsoft Notepad.

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

The first line
                                       			 of the CSV file must be "ACCESSPOINT OR SWITCH NAME,IPV4 ADDRESS,IPV6
                                       			 ADDRESS,BSSID,DESCRIPTION".

Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns:

- Device Name

- IPv4 Address

- IPv6 Address

- BSSID

- Description

To View sample csv data file, Click Bulk
                                             				  administration > Infrastructure
                                             				  Device > Insert Infrastructure
                                             				  Device .

Click View Sample File .

## Infrastructure
                        	 Device Insert Examples

### Infrastructure
                              		  Device Insert Examples

The
                              		  following are examples of a properly formatted Infrastructure device entry:

SFO12-32-AP2,10.77.29.28,FE80::0202:B3FF:FE1E:8330,EC:E1:A9:DA:85:30,SF->Bldg12->3rdFloor

SFO12-42-AP1,10.77.29.52,,3C:CE:73:56:2A:10,SF->Bldg12->4rdFloor

NYC01-3560SW1,10.177.34.50,,,NYC->Blgd1->-IDF1

CHI-3650,10.190.23.33,,,Chicago->1060AddisonSt

## Insert Infrastructure Devices

Use this procedure to complete a bulk import of your  wireless access point infrastructure from a CSV file into the Cisco
                              Unified Communications Manager database. You can use this procedure to import a CSV file that was exported from  Cisco Prime
                              Infrastructure or if you want to import access points from a third-party wireless access point controller.

### Before you begin

You must have a data file
                              			 in comma separated value (CSV) format with the following delineated columns:

AccessPoint or Switch Name

IPv4 Address

IPv6 Address

BSSID—Required for Wireless Access Protocol (WAP) infrastructure devices

Description—A location identifier, a combination of switch type and location, or another meaningful identifier

You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address.

For the BSSID value, enter the BSSID mask, ending in 0, that uniquely identifies the access point as opposed to the BSSIDs
                                          for the individual channels on the access point.

Choose Bulk
                                             				  Administration > Infrastructure Device > Insert Infrastructure
                                             				  Device .

In the File
                                          				Name field, choose the CSV data file that you created for this
                                       			 transaction.

In the Job
                                          			 Information area, enter the Job description.

The default
                                          				description is Insert Infrastructure Device .

Select when you want to run the job:

- Select the Run Immediately radio button, if you want to run the job immediately.

- Select the Run Later radio button, if you want to schedule the job for later.

Click Submit .

If you chose to run the job later, schedule when the job runs:

Choose Bulk Administration > Job Scheduler .

Click Find and select the job that you just created.

In the Job Scheduler window, schedule when you want to run the job.

Click Save .

| Note | The BAT.xlt file exists on the first node of the Cisco Unified
                                             				Communications Manager server; however, you normally do not have
                                          			 Microsoft Excel installed on the server. In that case, copy the file from the
                                          			 first node and move it to a local machine that has Microsoft Excel installed. |
|---|---|

| Step 1 | Choose Bulk Administration > Upload/Download Files . The Find and List Files window opens. |
|---|---|
| Step 2 | Click Find and download the BAT.xlt file. |

| Step 1 | Open a BAT.xlt
                                       			 spreadsheet that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns: Device Name IPv4 Address IPv6 Address BSSID Description |
| Step 3 | Click Export
                                          				to BAT Format. This
                                       			 displays Cisco
                                          				CallManager Bulk Administration Tool pop-up window. |
| Step 4 | Click OK to create a .txt file, which will be stored in
                                       			 your local workstation. Example: C:\XlsDataFiles\Infrastructuredevice-04222015144259. |

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | The first line
                                       			 of the CSV file must be "ACCESSPOINT OR SWITCH NAME,IPV4 ADDRESS,IPV6
                                       			 ADDRESS,BSSID,DESCRIPTION". |
| Step 3 | Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns: Device Name IPv4 Address IPv6 Address BSSID Description |
| Step 4 | To View sample csv data file, Click Bulk
                                             				  administration > Infrastructure
                                             				  Device > Insert Infrastructure
                                             				  Device . The Insert Infrastructure Device Configuration window opens. |
| Step 5 | Click View Sample File . |

| Note | BSSID is a
                                       		  mask and must end with a zero. The BSSID should not be that of an individual
                                       		  wireless network. |
|---|---|

| Note | You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address. |
|---|---|

| Note | For the BSSID value, enter the BSSID mask, ending in 0, that uniquely identifies the access point as opposed to the BSSIDs
                                          for the individual channels on the access point. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Infrastructure Device > Insert Infrastructure
                                             				  Device . The Insert
                                          				Infrastructure Device Configuration window displays. |
|---|---|
| Step 2 | In the File
                                          				Name field, choose the CSV data file that you created for this
                                       			 transaction. |
| Step 3 | In the Job
                                          			 Information area, enter the Job description. The default
                                          				description is Insert Infrastructure Device . |
| Step 4 | Select when you want to run the job: Select the Run Immediately radio button, if you want to run the job immediately. Select the Run Later radio button, if you want to schedule the job for later. |
| Step 5 | Click Submit . If you chose to run the job immediately, the job runs. |
| Step 6 | If you chose to run the job later, schedule when the job runs: Choose Bulk Administration > Job Scheduler . Click Find and select the job that you just created. In the Job Scheduler window, schedule when you want to run the job. Click Save . At the scheduled time, the job runs. |