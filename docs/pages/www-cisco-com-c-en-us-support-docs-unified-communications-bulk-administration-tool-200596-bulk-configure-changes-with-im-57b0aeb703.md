---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-bulk-administration-tool-200596-bulk-configure-changes-with-im-57b0aeb703
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/bulk-administration-tool/200596-Bulk-Configure-Changes-with-Import-Expor.html
retrieved_at: 2026-08-21T00:00:09.844077+00:00
---

Bulk Configure Changes with Import/Export Feature

# Bulk Configure Changes with Import/Export Feature

### Download Options

Updated: March 12, 2018

Document ID: 200596

Contents

## Contents

## Introduction

This document describes how to use the Import/Export menu in Cisco Unified Communications Manager (CUCM) Bulk Administration Tool (BAT) in  to export or import parts of the CUCM database to another server, or to the same server with modifications.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM.

### Components Used

The information in this document is based on CUCM 10.5.2.12900-14.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Sometimes it is not possible to make changes to the phone and device profile or other components configuration in single job task with BAT update/validate menu if changes are meant to be for multiple phones and device profiles with different device pools or partitions. With this menu you can make changes to any random phones, device profiles and route patterns etc. in a single job task. This reduces the configuration time that is required by importing a preconfigured database to the installed CUCM server. These topics provide procedures to carry out these tasks:

- Exporting Configuration

- Editing the .tar Fil e

- Importing Configuration

## Configure

### Export Configuration

In order to export configuration data from CUCM, use this procedure.

Step 1. Select Bulk Administration > Import/Export> Export .

The Export Data window displays this:

S tep 2. In the Job Information section, enter the .tar file name, without the extension, in the Tar File Name field. BPS uses this filename to export the configuration details.

All files that are exported at the same time get bundled together ( .tar ) and can be downloaded from the server.

Step 3. In the Select items to Export section, check the appropriate check boxes under System Data from these options:

Phone and device profiles are used as an example in this document. You can choose any option based on the requirement.

Step 4. You can use the Select All button to check all the check boxes at once and the Clear All button to clear all the check boxes.

Step 5. In the Job Description field, enter the description that you want to provide for the job. Export Configuration is the default description.

Step 6. You can choose to run the job immediately or later and select the corresponding radio button.

Step 7. In order to check for interdependency of tables to ensure that the related records are also exported, click Check Dependency .

Note : You can de-select any of the check boxes after you check the dependency. You also have the option to skip Checking Dependency .

Check Dependency selects dependent items up to one level of dependency. For example, if an item depends on CSS, then only CSS is selected and the items that CSS depends on are not selected.

Step 8. In order to create a job in order to create the selected data, click Submit .

A message in the Status section lets you know that the job was submitted successfully.

Step 9. Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or activate this job.

Choose Bulk Administration > Job Scheduler > Click on Find and search for the last Job Id.

Since you select the option run immediately, the job gets completed automatically. If you check option run later , then you need to select the Job Id and activate it manually to process it.

### Edit the .tar File

The tar file comprises a list of CSV files and a header file. Header file can be used to refer to the details of the server from where the export was carried out and the time when it was carried out. The header file also has details of the files in the package. If you want to make any changes to the configuration after you have exported the required data, you can do so by editing the exported .tar file with this procedure:

Step 10. Now select Bulk Administration > Upload/Download files

From the Upload/Download window select the tar file and click on Download Selected.

Step11. Un-tar the .tar file to some location on your machine with the tar -xvf command.

The .csv file gets extracted to the location that you specified.

Note : The tar -xvf command might not work on a Windows server, TAR and UNTAR operations are possible in Windows with 7-Zip, which is a freeware available on the World Wide Web (WWW).

The name of the .csv file is always the same as the item name. Use MS Excel to edit the .csv file and save your changes. You can edit the .csv file with Notepad/WordPad also, but Cisco recommends to make use of MS Excel to edit the .csv file.

If you decide to use notepad or WordPad for the edit, ensure that you add a comma for every new entry in the file format.

Always maintain the same filename and file format for the .csv file. If you add a new file to the tar package, ensure that the file has the same name and file format as it would have if it is exported from CUCM. Also, ensure that the new filename is added to the Header file.

This is the original configuration of all the phones in my lab call manager. Changes have been made to the phone description field of 2 phones.

The description field has been changed here:

Note : Import/Export tool does not support update the password and pin attributes. They are exported in encrypted form in the exported file and hence it cannot be changed to plain text. Entities which have credentials are - Common Phone Profile, SIP Realm, Application User, LDAP Authentication, LDAP Directory, Cisco Attendant Console, and Enduser. Know that you must not modify the User ID, User Pkid, Password, and Pin fields in the enduser.csv in the exported file.

Step 12. Once you are done with the changes; Re-tar the files with the tar -cvf command while you ensure that the new .tar file is saved in the default common location.

Note : The tar -cvf command might not work on a Windows server, TAR and UNTAR operations are possible in Windows with 7-Zip, which is a freeware available on the WWW.

The .tar files must maintain the original directory structure when you re-tar the files, because BPS looks for .tar files at the default location only (club the header file, phone.csv and deviceprofile.csv file into .tar file).

### Import Configuration

Use this procedure to upload a file to the CUCM server:

Step 13. Select Bulk Administration > Upload/Download Files . The Find and List Files window displays.

Click Add New . The File Upload Configuration window displays. In the File text box, enter the full path of the file that you want to upload or click Browse and locate the file.

From the Select the Target drop-down list box, select the target for which you want to use the file.

From the Transaction Type drop-down list box, seletc the transaction type that the file defines.

If you want to overwrite a file that already exists with the same name, check the Overwrite File if it exists check box.

Click Save . The status displays that the upload is successful.

### Import File Validation Item

The Validate Import File page in BAT validates these items in the import .tar file:

The .tar file includes a header file.

All files listed in the header file are actually present in the .tar file.

All files in the .tar file are listed in header file.

File names are correct (as per the Import/Export convention).

File format for the CSV files in the .tar file is correct.

Now select Bulk Administration > Import/Export > Validate Import File .

Note : This feature does not include field level validation for valid characters, string length, etc.

In this example, changes are made to the configuration that already existed, therefore Validate Import file option was chosen.

Select Tar File name and hit Submit .

In order to see whether the Job completed successfully or not, navigate to Bulk Administration > Job Scheduler > Click on the latest job scheduler with Job description as Validate Configuration Items.

Ensure that Job result status is displayed as success, if not, then it means the job wasn't completed successfully (in failure scenario you will see Job result status as error).

If there are any problems encountered at the time of validation, these are listed in the log files.

### Import Configuration to the Server

In case you want to use import option, follow this procedure:

Select Bulk Administration > Import/Export > Import

Note : You can only update the existing enterprise or service parameters with the use of import / export. If some of the parameters are missing in the database, when you import the parameter, it fails.

You can use the Override the existing configuration option to make BPS update an item if it already exists on the server or insert the item if it does not. When you import phones or User Device Profiles with the use of the override option, the IP phone services do not get updated but only get appended to the existing set of entities.

Select the File name:

Select the Device Data accordingly and click on Run Immediately radio button and submit the Job.

In order to see whether the Job completed successfully or not, navigate to Bulk Administration > Job Scheduler > Click on the latest job scheduler with Job description as Import Configuration .

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

This section provides information you can use in order  to troubleshoot your configuration.

Navigate to Job Scheduler and click on the respective Job Id and check the log files in the Job results section and see the error description and make modifications accordingly. Also, you can collect bulk provisioning service logs from RTMT and check for the errors.