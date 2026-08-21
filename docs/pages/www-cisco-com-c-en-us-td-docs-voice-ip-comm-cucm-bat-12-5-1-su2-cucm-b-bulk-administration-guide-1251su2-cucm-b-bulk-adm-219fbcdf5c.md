---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-219fbcdf5c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_0111111.html
retrieved_at: 2026-08-21T08:50:02.749717+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Import Configuration Data

## Chapter: Import Configuration Data

# Import Configuration Data

This chapter provides information to import configuration data to Cisco Unified Communications Manager using the Bulk Administration Menu.

You can only update the existing enterprise or service parameters using import/export. If your import .csv file has templates
                        specific to IPMA, make sure that you run the IPMA wizard on the target server before you proceed with the import transaction.

## Import Configuration to Server

You can import configuration data to Unified Communications Manager using the Bulk Administration Menu.

The LDAP password configured under the User Management > User Settings > Service Profile > Directory Profile Unified CM Administration interface will be exported in the encrypted format when you export the Service Profiles data using
                                          BAT. To import Service Profiles data from a Unified Communications Manager server to another, you must manually re-enter the
                                          password in plain text form in the exported .csv file. This is because you cannot import the same password as the decryption
                                          key is different for different servers.

If you are using the LDAP credentials for authentication, you should disable the Cisco Jabber Diagnostic Tool using the DiagnosticsToolEnabled parameter configured in the Jabber Client Configuration (jabber-config.xml) file.

To successfully import enterprise or service parameters, you must update the parameter from the Enterprise Parameter or Service Parameter window in Cisco Unified Communications Manager Administration from where it is being imported. In this case, when you are
                              in the Enterprise Parameter or Service Parameter window in Cisco Unified Communications Manager Administration, click Save without making any changes before you run import.

You can use the "Override the existing configuration" option to make BPS update an item if it exists on the server or insert the item if it does not. When you import phones or
                              User Device Profiles using the override option, the IP Phone services do not get updated but only get appended to the existing
                              set of entities.

### Before you begin

If your import .csv file has templates specific to IPMA, make sure
                              		  that you run the IPMA wizard on the target server before you carry out the
                              		  import transaction.

Choose Bulk
                                             				  Administration > Import/Export > Import .

Select the .tar file name in the File Name field and click Next .

The Import Configuration section lists all the
                                       			 components of the .tar file. Check the corresponding check boxes for the
                                       			 options that you want to import.

To make BPS update the item if it exists and insert if it does
                                       			 not, check the Override the existing configuration check box.

Overriding the existing configuration is optional.

You can click Select All to select all the options at once,
                                       			 and click Clear All to clear all selections.

Choose to run the job immediately or later by selecting the
                                       			 corresponding radio button.

To create a job for importing the selected data, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

### What to do next

You can use Override when you are running the same tar file with
                              		  corrections, after a failed job-run.

When a Unified Communications Manager server is created, there are database triggers on the background which create entities
                                          such as Conference Bridge (CFB), Media Termination point (MTP), and so on, automatically. These entities have names like CFB_1,
                                          and MTP_1.

When a user exports this information into a TAR file and imports it to a different Unified Communications Manager server,
                                          then the system creates items such as CFB and MTP. The names on the new Unified Communications Manager server may be consistent
                                          with the names before import, or can be different.

## Cyclic Dependency

Some entities in Cisco Unified Communications Manager depend upon each other in such a way that one
                              		  cannot be imported without importing the other. Import/Export carries out the
                              		  import process for such entities in two stages:

The entity with the higher priority is imported first, with a
                                    				blank value for the supporting entity.

This occurs because the value of the supporting entity is not
                                                				  available at the time.

After importing all the entities in the .tar, Import/Export
                                    				updates the higher priority entity with the value of the supporting entity to
                                    				complete the import process.

The value of the supporting entity becomes available in the next
                                                				  cycle.

### Example

Consider the following example to understand how cyclic
                              		  dependency works:

Device Pool and Media Resource Group List (MRGL)—Device Pool
                              		  (entity with the higher priority) gets imported first, with a blank value for
                              		  MRGL (supporting entity), because the value of MRGL is not available at the
                              		  time. After importing all the entities in the .tar file, Import/Export updates
                              		  Device Pool, replacing the blank value with the true value of MRGL to complete
                              		  the import process.

Consider the following entities as bound by cyclic
                              		  dependency:

Device Pool and MRGL

Device Pool and Route Group

Partition and Time Schedule

Application User and User group

Licensing

### Sample Record

devicepool.csv

```
DEVICE POOL NAME,CISCO UNIFIED CALLMANAGER GROUP,DATE/TIME GROUP,REGION,SRST REFERENCE,CALLING SEARCH SPACE FOR AUTO-REGISTRATION,AAR CALLING SEARCH SPACE,DEVICE MOBILITY CALLING SEARCH SPACE,MEDIA RESOURCE GROUP LIST,LOCATION,NETWORK LOCALE,CONNECTION MONITOR DURATION,DEVICE MOBILITY GROUP,AAR GROUP,REVERTED CALL FOCUS PRIORITY,LOCAL ROUTE GROUP,CALLING PARTY TRANSFORMATION CSS,CALLED PARTY TRANSFORMATION CSS,INCOMING CALLING PARTY NATIONAL NUMBER PREFIX,INCOMING CALLING PARTY INTERNATIONAL NUMBER PREFIX,INCOMING CALLING PARTY UNKNOWN NUMBER PREFIX,INCOMING CALLING PARTY SUBSCRIBER NUMBER PREFIX,PHYSICAL LOCATION
```

```
Branch_0000,CMG 1 Phones,Central,region_0001,Disable,NULL,NULL,NULL,Intrn_MRGL-1_Volkswagen Intn.,,NULL,-1,NULL,NULL,Default,NULL,NULL,NULL,Default,Default,Default,Default,NULL
```

mediaresourcegrouplist.csv

```
NAME,MEDIA RESOURCE GROUP 1,SORT ORDER 1
```

Intrn_MRGL-1_Volkswagen Intn.,,

Import/Export generates two logs files for every import of dependent
                                          			 entities. The first log file indicates the status of insert of the first
                                          			 entity; the other indicates whether the first entity was successfully updated
                                          			 with the value of the supporting entity.

### Items Not Supported on Import or Export

The following items are not supported on import or export:

Dial Plan Installer

Route Plan Report

MOH Audio Source

Fixed MOH Audio Source

MOH Audio File Management

Cisco Voice Mail Port wizard

Firmware load information

Licensing

Announcement

## Override Only

Import/Export does not support insert functionality for the following entities in the Cisco Unified Communications Manager database. You can only update/override these entities.

Cisco Unified CM

LDAP System

Enterprise Parameters

Service Parameter

Mobility Configuration

Annunciator/MOH Server—When a Cisco Unified Communications Manager server is created, database triggers create entities such as MOH server, annunciator, and so on. When you export this information
                                    into a TAR file and import it to a different Cisco Unified Communications Manager server, the system trigger creates items such as MOH server, annunciator, and so on. Import/Export supports only update of
                                    existing MOH server—server association/annunciator—server association. You can edit the TAR file to make sure that the csv
                                    file has the valid association before importing. Cisco recommends that you import the server first; then, based on the association
                                    created, you can edit the csv file and do an Import with Override.

Device Defaults

Credential Policy Default

Certificate—Import/Export supports only update of existing certificates as new certificates cannot be created/uploaded from Cisco Unified Communications Manager Administration . Only the Duration in Cache parameter from the certificate can be updated.

Self-Provisioning

## Upgrade From Cisco Unified CallManager 4.x Releases

Keep the following points in mind when you import entities
                              		  after an upgrade from Cisco Unified CallManager 4.x releases:

BAT supports Import/Export between the same versions of Cisco Unified Communications Manager only. After the upgrade from a 4.x release of
                                    				Cisco Unified CallManager, make sure that you have the same Cisco Unified Communications Manager version on both the source and target servers.

Some user groups associated to application users that are relevant
                                    				to the erstwhile Cisco Unified CallManager 4.x version that was running on the
                                    				source server before the upgrade, may not be relevant to the Cisco Unified Communications Manager version running on the target server. Import
                                    				transaction for such user groups will fail.

## Topics Related to Import/Export Menu

| Note | The LDAP password configured under the User Management > User Settings > Service Profile > Directory Profile Unified CM Administration interface will be exported in the encrypted format when you export the Service Profiles data using
                                          BAT. To import Service Profiles data from a Unified Communications Manager server to another, you must manually re-enter the
                                          password in plain text form in the exported .csv file. This is because you cannot import the same password as the decryption
                                          key is different for different servers. If you are using the LDAP credentials for authentication, you should disable the Cisco Jabber Diagnostic Tool using the DiagnosticsToolEnabled parameter configured in the Jabber Client Configuration (jabber-config.xml) file. |
|---|---|

| Attention | You can only update the existing enterprise or service parameters using Import/Export . If some of the parameters are missing in the database, importing the parameter fails. |
|---|---|

| Note | Because there can be multiple IP Phone services with the same name and there is no unique key to distinguish these services,
                                       Import or Export cannot determine which service to update and appends the service instead. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Import/Export > Import . The Import Configuration window displays. |
|---|---|
| Step 2 | Select the .tar file name in the File Name field and click Next . Note The File Name drop-down list displays all uploaded .tar files. | Note | The File Name drop-down list displays all uploaded .tar files. |
| Note | The File Name drop-down list displays all uploaded .tar files. |
| Step 3 | The Import Configuration section lists all the
                                       			 components of the .tar file. Check the corresponding check boxes for the
                                       			 options that you want to import. |
| Step 4 | To make BPS update the item if it exists and insert if it does
                                       			 not, check the Override the existing configuration check box. Overriding the existing configuration is optional. Note In case the files are modified, then the filename and the file format must not be changed during the update. | Note | In case the files are modified, then the filename and the file format must not be changed during the update. |
| Note | In case the files are modified, then the filename and the file format must not be changed during the update. |
| Step 5 | You can click Select All to select all the options at once,
                                       			 and click Clear All to clear all selections. |
| Step 6 | Choose to run the job immediately or later by selecting the
                                       			 corresponding radio button. |
| Step 7 | To create a job for importing the selected data, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 8 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | The File Name drop-down list displays all uploaded .tar files. |
|---|---|

| Note | In case the files are modified, then the filename and the file format must not be changed during the update. |
|---|---|

| Note | When a Unified Communications Manager server is created, there are database triggers on the background which create entities
                                          such as Conference Bridge (CFB), Media Termination point (MTP), and so on, automatically. These entities have names like CFB_1,
                                          and MTP_1. When a user exports this information into a TAR file and imports it to a different Unified Communications Manager server,
                                          then the system creates items such as CFB and MTP. The names on the new Unified Communications Manager server may be consistent
                                          with the names before import, or can be different. |
|---|---|

| Note | This occurs because the value of the supporting entity is not
                                                				  available at the time. |
|---|---|

| Note | The value of the supporting entity becomes available in the next
                                                				  cycle. |
|---|---|

| Note | Import/Export generates two logs files for every import of dependent
                                          			 entities. The first log file indicates the status of insert of the first
                                          			 entity; the other indicates whether the first entity was successfully updated
                                          			 with the value of the supporting entity. |
|---|---|