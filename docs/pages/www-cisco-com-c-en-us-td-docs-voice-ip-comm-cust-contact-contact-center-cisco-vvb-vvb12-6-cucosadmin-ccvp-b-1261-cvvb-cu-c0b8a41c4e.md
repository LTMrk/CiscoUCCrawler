---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-6-cucosadmin-ccvp-b-1261-cvvb-cu-c0b8a41c4e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_6/cucosadmin/ccvp_b_1261-cvvb-cuc-os-administration-guide/ccvp_b_1251-cvvb-cuc-os-administration-guide_chapter_0100.html
retrieved_at: 2026-08-21T16:31:27.453029+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

# Cisco Unified Communications Operating System Administration Guide for Cisco Virtualized Voice Browser, Release 12.6(1)

Updated: May 21, 2021

Chapter: System Restart

## Chapter: System Restart

# System Restart

## Switch Versions and Restart

You can use this option both when you are upgrading to a newer
                              		  software version, and when you need to fall back to an earlier software version.
                              		  To shut down the system that is running on the active disk partition and then
                              		  automatically restart the system by using the software version on the inactive
                              		  partition, follow this procedure:

This procedure causes the system to restart and become temporarily
                                          			 out of service.

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

The Version Settings window appears, showing the software version on both the active and inactive partitions.

Click Switch Versions to switch versions and
                                       			 restart. Click Cancel to stop the operation.

## Restart Current Version

To restart the system on the current partition without
                              		  switching versions, follow this procedure:

This procedure causes the system to restart and become temporarily
                                          			 out of service.

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

Click Restart to restart the system, or click Cancel to stop the operation.

## Shut Down
                        	 System

Do not press the
                                          			 power button on the server to shut down the server or to reboot the server. If
                                          			 you do, you may accidentally corrupt the file system, which may prevent you
                                          			 from future server reboots.

This procedure
                                          			 causes the system to shut down.

If you are
                                       			 shutting down the system from the command line interface, go to step 4.
                                       			 Otherwise, go to Step 2.

From the Cisco Unified Operating System Administration window, navigate to Settings > Version .

Click Shutdown to shut down the system, or click Cancel to stop the operation.

If you click Shutdown , the system halts all processes and shuts
                                          				down.

Enter the
                                       			 command utils
                                          				system shutdown or the command utils
                                          				system restart .

For more information about CLI commands, see the Cisco Unified Contact
                                                   				  Center Express Command Line Interface Reference Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html .

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
                                                   				  Center Express Command Line Interface Reference Guide , located at https://www.cisco.com/en/US/products/sw/custcosw/ps1846/prod_installation_guides_list.html . |

| Note | The hardware
                                                   				may require several minutes to power down. |
|---|---|

| Note | A switch
                                          			 version operation is abruptly terminated if a power reset or hard reboot is
                                          			 done on the Unified CCX system when
                                          			 it is in progress. |
|---|---|