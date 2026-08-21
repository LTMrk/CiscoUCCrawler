---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-a53a7d8807
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01001111.html
retrieved_at: 2026-08-21T09:15:41.405205+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

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

Step 1

Choose Bulk Administration > Upload/Download Files .

Step 2

Click Find and download the BAT.xlt file.

## Create
                        	 Infrastructure Device CSV Data File using BAT.xlt

Step 1

Open a BAT.xlt
                                       			 spreadsheet that allows you to export or create a text-based CSV file.

Step 2

Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns:

- Device Name

- IPv4 Address

- IPv6 Address

- BSSID

- Description

Step 3

Click Export
                                          				to BAT Format.

Step 4

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

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

The first line
                                       			 of the CSV file must be "ACCESSPOINT OR SWITCH NAME,IPV4 ADDRESS,IPV6
                                       			 ADDRESS,BSSID,DESCRIPTION".

Step 3

Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns:

- Device Name

- IPv4 Address

- IPv6 Address

- BSSID

- Description

Step 4

To View sample csv data file, Click Bulk
                                             				  administration > Infrastructure
                                             				  Device > Insert Infrastructure
                                             				  Device .

Step 5

Click View Sample File .

## Insert Infrastructure Devices

Use this procedure to complete a bulk import of your wireless Access Point infrastructure from a CSV file into the database. You can use this procedure to import a CSV file that was exported from Cisco Prime Infrastructure or if you want
                              to import access points from a third-party wireless Access Point controller.

### Before you begin

You must have a data file
                              			 in comma separated value (CSV) format with the following delineated columns:

AccessPoint or Switch Name

IPv4 Address

IPv6 Address

BSSID—Required for Wireless Access Protocol (WAP) infrastructure devices

Description—A location identifier, a combination of switch type and location, or another meaningful identifier

You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address.

For Meraki Access Points, the updates the Basic Service Set Identifiers (BSSID) in the Database after normalizing it to its base BSSID. For more information
                                          about BSSID masking calculation for Meraki Access Points, see Calculating Cisco Meraki BSSID MAC Addresses .

For Non- Meraki Access Points, the Unified CM updates the BSSID in the database by masking the last byte with 0.

This masking logic helps Unified CM to uniquely identify the Access Point as opposed to the BSSIDs for the individual channels
                                          on the Access Point.

Step 1

Choose Bulk
                                             				  Administration > Infrastructure Device > Insert Infrastructure
                                             				  Device .

Step 2

In the File
                                          				Name field, choose the CSV data file that you created for this
                                       			 transaction.

Step 3

In the Job
                                          			 Information area, enter the Job description.

The default
                                          				description is Insert Infrastructure Device .

Step 4

Select when you want to run the job:

- Select the Run Immediately radio button, if you want to run the job immediately.

- Select the Run Later radio button, if you want to schedule the job for later.

Step 5

Click Submit .

Step 6

If you chose to run the job later, schedule when the job runs:

Choose Bulk Administration > Job Scheduler .

Click Find and select the job that you just created.

In the Job Scheduler window, schedule when you want to run the job.

Click Save .

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

RCDN-AP2,,,AA:17:D8:07:CF:4D,Bldg0-F1

For Non-Meraki Access Points, the updates the Basic Service Set Identifiers (BSSID) in the Database by masking the last byte with 0. The BSSID should not be
                                          that of an individual wireless network.

The example “RCDN-AP2,,,AA:17:D8:07:CF:4D,Bldg0-F1” is for non-Meraki Access Points. For more information about BSSID masking
                                          calculation for Meraki Access Points, see Calculating Cisco Meraki BSSID MAC Addresses .

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

| Note | You can define both an IPv4 and IPv6 address, or you can define an IPv4 or an IPv6 address. For Meraki Access Points, the updates the Basic Service Set Identifiers (BSSID) in the Database after normalizing it to its base BSSID. For more information
                                          about BSSID masking calculation for Meraki Access Points, see Calculating Cisco Meraki BSSID MAC Addresses . For Non- Meraki Access Points, the Unified CM updates the BSSID in the database by masking the last byte with 0. This masking logic helps Unified CM to uniquely identify the Access Point as opposed to the BSSIDs for the individual channels
                                          on the Access Point. |
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

| Note | For Non-Meraki Access Points, the updates the Basic Service Set Identifiers (BSSID) in the Database by masking the last byte with 0. The BSSID should not be
                                          that of an individual wireless network. The example “RCDN-AP2,,,AA:17:D8:07:CF:4D,Bldg0-F1” is for non-Meraki Access Points. For more information about BSSID masking
                                          calculation for Meraki Access Points, see Calculating Cisco Meraki BSSID MAC Addresses . |
|---|---|