---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-8bae6688c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01000011.html
retrieved_at: 2026-08-21T08:50:19.508096+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Insert, Update, and Delete EMCC Devices

## Chapter: Insert, Update, and Delete EMCC Devices

# Insert, Update, and Delete EMCC Devices

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert, update, and delete
                        		EMCC devices in the Cisco Unified Communications Manager database.

## Insert EMCC Devices

Use BAT to add EMCC devices to the Cisco Unified Communications Manager database.

Each EMCC device bears a unique name in the format: EMCC1, EMCC2, and
                              		  so on. BAT assigns EMCC device numbers by obtaining the last one used. If any
                              		  other entity like, Phone, UDP, RDP, or EMCC Templates are named in the same
                              		  format (EMCC1, EMCC2), then BAT Insert EMCC generates an error for duplicate
                              		  naming. Therefore, ensure that the above entities with the same name format,
                              		  are renamed before inserting EMCC Devices.

Example

The Admin user wants to insert 27 numbers of EMCC devices.
                              		  First, BAT searches for the last EMCC device serial number used in the UCM say,
                              		  EMCC123. Then it starts inserting devices from the next number onwards: EMCC124
                              		  to EMCC150. If UDP devices have already used the following names: EMCC135,
                              		  EMCC137, and EMCC150, then BAT Insert EMCC will generate a naming error. EMCC
                              		  devices with the above names do not get created unless the UDP devices are
                              		  renamed.

### Before you begin

Before you insert EMCC devices, you must have a valid EMCC template
                              		  set as default. Set the default template following the update EMCC devices procedure.

To determine how many EMCC devices to add, look at the number of registered phones and add
                              5% to account for devices that may not be registered at the moment.  If you have 100 phones, multiply 100
                              by 0.5, which equals 5. You add the result (5) to the total (100). The number of EMCC devices is 105.

To display information about the number of
                              registered phones, gateways, and media resource devices on Cisco
                              Unified Communications Manager, open RTMT and choose Voice/Video
                                 > Device > Device Summary .

Choose Bulk
                                             				  Administration > EMCC > Insert/Update
                                             				  EMCC .

Make sure that the Insert EMCC Devices radio button is selected.

Enter the number of devices in the Number of EMCC Devices to be added field.

In the Job Information area, enter the Job description.

Insert EMCC Devices is the default description.

To insert the EMCC devices immediately, click the Run Immediately radio button. Click Run Later to insert the devices at a later
                                       			 time.

To create a job for inserting the EMCC devices, click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Update EMCC Devices

Use BAT to update EMCC devices in the Cisco Unified Communications Manager database.

Choose Bulk
                                             				  Administration > EMCC > Insert/Update
                                             				  EMCC .

Select the Update EMCC Devices radio button.

To set the default template, choose an EMCC template from the Default EMCC Template drop-down list box.

Select the Reset radio button to reset all devices,
                                       			 select Don't Reset if you do not wish to reset all
                                       			 devices.

In the Job Information area, enter the Job description.

Update EMCC Devices is the default description.

To update the EMCC records immediately, click the Run Immediately radio button. Click Run Later to update the records at a later
                                       			 time.

To create a job for updating the EMCC devices, click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete EMCC Devices

You can use BAT to delete EMCC devices in bulk. Use the
                              		  procedures to delete EMCC devices.

Choose Bulk
                                             				  Administration > EMCC > Delete
                                             				  EMCC .

The Delete EMCC Configuration window displays.

Enter the number of devices to that you wish to delete in the Number of EMCC Devices to be deleted field.

In the Job Information area, enter the Job description.

Delete EMCC is the default description.

To delete the EMCC devices immediately, click the Run Immediately radio button. Click Run Later to delete the devices at a later
                                       			 time.

To create a job for deleting the EMCC devices, click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

| Step 1 | Choose Bulk
                                             				  Administration > EMCC > Insert/Update
                                             				  EMCC . The Insert/Update EMCC Configuration window
                                       			 displays. |
|---|---|
| Step 2 | Make sure that the Insert EMCC Devices radio button is selected. |
| Step 3 | Enter the number of devices in the Number of EMCC Devices to be added field. |
| Step 4 | In the Job Information area, enter the Job description. Insert EMCC Devices is the default description. |
| Step 5 | To insert the EMCC devices immediately, click the Run Immediately radio button. Click Run Later to insert the devices at a later
                                       			 time. |
| Step 6 | To create a job for inserting the EMCC devices, click Submit . |
| Step 7 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Step 1 | Choose Bulk
                                             				  Administration > EMCC > Insert/Update
                                             				  EMCC . The Insert/Update EMCC Configuration window
                                       			 displays. |
|---|---|
| Step 2 | Select the Update EMCC Devices radio button. |
| Step 3 | To set the default template, choose an EMCC template from the Default EMCC Template drop-down list box. |
| Step 4 | Select the Reset radio button to reset all devices,
                                       			 select Don't Reset if you do not wish to reset all
                                       			 devices. |
| Step 5 | In the Job Information area, enter the Job description. Update EMCC Devices is the default description. |
| Step 6 | To update the EMCC records immediately, click the Run Immediately radio button. Click Run Later to update the records at a later
                                       			 time. |
| Step 7 | To create a job for updating the EMCC devices, click Submit . |
| Step 8 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Step 1 | Choose Bulk
                                             				  Administration > EMCC > Delete
                                             				  EMCC . The Delete EMCC Configuration window displays. |
|---|---|
| Step 2 | Enter the number of devices to that you wish to delete in the Number of EMCC Devices to be deleted field. |
| Step 3 | In the Job Information area, enter the Job description. Delete EMCC is the default description. |
| Step 4 | To delete the EMCC devices immediately, click the Run Immediately radio button. Click Run Later to delete the devices at a later
                                       			 time. |
| Step 5 | To create a job for deleting the EMCC devices, click Submit . |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |