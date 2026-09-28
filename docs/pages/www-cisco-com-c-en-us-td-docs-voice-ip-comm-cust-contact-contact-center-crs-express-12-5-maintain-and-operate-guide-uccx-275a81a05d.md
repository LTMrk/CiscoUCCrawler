---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-275a81a05d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_unified-ccx-operating-system-1251su3/uccx_m_1251su3_system-restart.html
retrieved_at: 2026-08-16T21:30:35.543022+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

Updated: July 10, 2023

Chapter: System Restart

## Chapter: System Restart

# System Restart

## Switch Versions and Restart

You can use this option both when you are upgrading to a newer
                              		  software version, and when you need to fall back to an earlier software version.
                              		  To shut down the system that is running on the active disk partition and then
                              		  automatically restart the system by using the software version on the inactive
                              		  partition, follow this procedure:

Caution

This procedure causes the system to restart and become temporarily
                                          			 out of service.

Step 1

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

The Version Settings window appears, showing the software version on both the active and inactive partitions.

Step 2

Click Switch Versions to switch versions and
                                       			 restart. Click Cancel to stop the operation.

## Restart Current Version

To restart the system on the current partition without
                              		  switching versions, follow this procedure:

Caution

This procedure causes the system to restart and become temporarily
                                          			 out of service.

Step 1

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

Step 2

Click Restart to restart the system, or click Cancel to stop the operation.

## Shut Down
                        	 System

Caution

Do not press the
                                          			 power button on the server to shut down the server or to reboot the server. If
                                          			 you do, you may accidentally corrupt the file system, which may prevent you
                                          			 from future server reboots.

Caution

This procedure
                                          			 causes the system to shut down.

Step 1

If you are
                                       			 shutting down the system from the command line interface, go to step 4.
                                       			 Otherwise, go to Step 2.

Step 2

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

Step 3

Click Shutdown to shut down the system, or click Cancel to stop the operation.

If you click Shutdown , the system halts all processes and shuts
                                          				down.

Step 4

Enter the
                                       			 command utils
                                          				system shutdown or the command utils
                                          				system restart .

For more information about CLI commands, see the Cisco Unified Contact
                                                   				  Center Express Command Line Interface Reference Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html .

For more information, see the Cisco Unified Contact Center Express Administration and Operations Guide , located at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

### What to do next

When the user
                              		  initiates a switch version, system restart, or system shutdown from the Cisco
                              		  Unified OS Administration web interface, the operation fails in the following
                              		  scenarios:

If the system detects that a switch version is in progress.

If the system detects that a previous switch version was abruptly terminated.

A switch
                                          			 version operation is abruptly terminated if a power reset or hard reboot is
                                          			 done on the Unified CCX system when
                                          			 it is in progress.

| Caution | This procedure causes the system to restart and become temporarily
                                          			 out of service. |
|---|---|

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Settings > Version . The Version Settings window appears, showing the software version on both the active and inactive partitions. |
|---|---|
| Step 2 | Click Switch Versions to switch versions and
                                       			 restart. Click Cancel to stop the operation. If you click Switch Versions , 
                                       			 the system restarts, and the partition that is
                                       			 inactive becomes active. |

| Caution | This procedure causes the system to restart and become temporarily
                                          			 out of service. |
|---|---|

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Settings > Version . The Version Settings window appears, showing the software version on both the active and inactive partitions. |
|---|---|
| Step 2 | Click Restart to restart the system, or click Cancel to stop the operation. If you click Restart , the system restarts on the current
                                       			 partition without switching versions. |

| Caution | Do not press the
                                          			 power button on the server to shut down the server or to reboot the server. If
                                          			 you do, you may accidentally corrupt the file system, which may prevent you
                                          			 from future server reboots. |
|---|---|

| Caution | This procedure
                                          			 causes the system to shut down. |
|---|---|

| Step 1 | If you are
                                       			 shutting down the system from the command line interface, go to step 4.
                                       			 Otherwise, go to Step 2. |
|---|---|
| Step 2 | From the Cisco Unified Operating System Administration window, navigate to Settings > Version . The Version Settings window appears, showing the software version on both the active and inactive partitions. |
| Step 3 | Click Shutdown to shut down the system, or click Cancel to stop the operation. If you click Shutdown , the system halts all processes and shuts
                                          				down. Note The hardware
                                                   				may require several minutes to power down. | Note | The hardware
                                                   				may require several minutes to power down. |
| Note | The hardware
                                                   				may require several minutes to power down. |
| Step 4 | Enter the
                                       			 command utils
                                          				system shutdown or the command utils
                                          				system restart . For more information about CLI commands, see the Cisco Unified Contact
                                                   				  Center Express Command Line Interface Reference Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html . For more information, see the Cisco Unified Contact Center Express Administration and Operations Guide , located at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |

| Note | The hardware
                                                   				may require several minutes to power down. |
|---|---|

| Note | A switch
                                          			 version operation is abruptly terminated if a power reset or hard reboot is
                                          			 done on the Unified CCX system when
                                          			 it is in progress. |
|---|---|