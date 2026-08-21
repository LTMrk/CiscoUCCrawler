---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-admingd-cucm-b-administration-guide-1251su1-cucm-b-test-87c743c569
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/adminGd/cucm_b_administration-guide-1251SU1/cucm_b_test-adminguide_chapter_01.html
retrieved_at: 2026-08-21T08:30:13.291309+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: April 8, 2025

Chapter: Getting Started

## Chapter: Getting Started

# Getting Started

## Sign In to Adminstrative Interfaces

Use this procedure to sign in to any of the administrative interfaces in your system.

Step 1

Open the Unified Communications Manager interface in your web browser.

Step 2

Choose the administration interface from the Navigation drop-down list.

Step 3

Click Go .

Step 4

Enter your username and password.

Step 5

Click Login .

## Reset the Administrator or Security Password

If you lose the administrator password and cannot access your system, use this procedure to reset the password.

For password changes on IM and Presence nodes, stop the Cisco Presence Engine service in all IM and Presence nodes before
                                          resetting the administrator password. After the password reset, restart the Cisco Presence Engine service in all the nodes.
                                          Make sure that you perform this task during maintenance because you may face presence issues when the PE is stopped.

### Before you begin

You require physical access to the node on which you perform this procedure.

At any point, when you are requested to insert CD or DVD media, you must mount the ISO file through the vSphere client for
                                    the VMWare server. See "Adding DVD or CD Drives to a Virtual Machine" https://www.vmware.com/support/ws5/doc/ws_disk_add_cd_dvd.html for guidance.

The security password on all nodes in a cluster must match. Change the security password on all machines, or the cluster nodes
                                    will not communicate.

Step 1

Sign in to the CLI on the publisher node with the following username and password:

Username: pwrecovery

Password: pwreset

Step 2

Press any key to continue.

Step 3

If you have a valid CD/DVD in the disk drive or you mounted an ISO file, remove it from the VMWare client.

Step 4

Press any key to continue.

Step 5

Insert a valid
                                       			 CD or DVD into the drive or mount the ISO file.

For this
                                                      				  test, you must use a disk or ISO file that is data only.

Step 6

After the
                                       			 system verifies the last step, you are prompted to enter one
                                       			 of the following options to continue:

- Enter a to reset the administrator password.

You must reset each node in a cluster after you change its security password. Failure to reboot the nodes causes system service
                                                            problems and problems with the administration windows on the subscriber nodes.

Step 7

Enter the new password, and then reenter it to confirm.

The administrator credentials must start with an alphabetic character, be at least six characters long, and
                                          			 can contain alphanumeric characters, hyphens, and underscores.

Step 8

After the system verifies the strength of the new password, the
                                       			 password is reset, and you are prompted to press any key to exit the password
                                       			 reset utility.

If you want to set up a different administrator password, use
                                          					 the CLI command set password . 
                                          				  For more information, see the Command Line Interface Reference Guide for CiscoUnified
                                             				  Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Shut Down or
                        	 Restart the System

Use this procedure if you need to shut down or restart your system, for example, after you make a configuration change.

### Before you begin

If the server is forced to shutdown and restart from your virtual machine, the file system may become corrupted. Avoid a
                              forced shutdown; instead, wait for the server to shutdown properly after this procedure or after you run utils system shutdown from the CLI.

You are recommended to shutdown or restart through a virtual machine by a utils system shutdown CLI command. The system-history.log
                                          displays the command entry and is considered as a graceful shutdown. If the shutdown or restart is done from the vSphere client,
                                          then it is considered as an ungraceful shutdown and the entry is not available in the system-history.log. Shutdown/reboot
                                          from vSphere client is not supported from version 10.x onwards.

If you force shutdown or restart the virtual machine from VMware administration tools (vCenter or Embedded Host Client):

Step 1

From Cisco Unified OS Administration, choose Settings > Version .

Step 2

Perform one of
                                       			 the following actions:

- Click Shutdown to stop all processes and shut down the
                                          				system.

- Click Restart to stop all processes and restart the
                                          				system.

| Step 1 | Open the Unified Communications Manager interface in your web browser. |
|---|---|
| Step 2 | Choose the administration interface from the Navigation drop-down list. |
| Step 3 | Click Go . |
| Step 4 | Enter your username and password. |
| Step 5 | Click Login . |

| Note | For password changes on IM and Presence nodes, stop the Cisco Presence Engine service in all IM and Presence nodes before
                                          resetting the administrator password. After the password reset, restart the Cisco Presence Engine service in all the nodes.
                                          Make sure that you perform this task during maintenance because you may face presence issues when the PE is stopped. |
|---|---|

| Step 1 | Sign in to the CLI on the publisher node with the following username and password: Username: pwrecovery Password: pwreset |
|---|---|
| Step 2 | Press any key to continue. |
| Step 3 | If you have a valid CD/DVD in the disk drive or you mounted an ISO file, remove it from the VMWare client. |
| Step 4 | Press any key to continue. |
| Step 5 | Insert a valid
                                       			 CD or DVD into the drive or mount the ISO file. Note For this
                                                      				  test, you must use a disk or ISO file that is data only. | Note | For this
                                                      				  test, you must use a disk or ISO file that is data only. |
| Note | For this
                                                      				  test, you must use a disk or ISO file that is data only. |
| Step 6 | After the
                                       			 system verifies the last step, you are prompted to enter one
                                       			 of the following options to continue: Enter a to reset the administrator password. Enter s to reset the security password. Note You must reset each node in a cluster after you change its security password. Failure to reboot the nodes causes system service
                                                            problems and problems with the administration windows on the subscriber nodes. | Note | You must reset each node in a cluster after you change its security password. Failure to reboot the nodes causes system service
                                                            problems and problems with the administration windows on the subscriber nodes. |
| Note | You must reset each node in a cluster after you change its security password. Failure to reboot the nodes causes system service
                                                            problems and problems with the administration windows on the subscriber nodes. |
| Step 7 | Enter the new password, and then reenter it to confirm. The administrator credentials must start with an alphabetic character, be at least six characters long, and
                                          			 can contain alphanumeric characters, hyphens, and underscores. |
| Step 8 | After the system verifies the strength of the new password, the
                                       			 password is reset, and you are prompted to press any key to exit the password
                                       			 reset utility. If you want to set up a different administrator password, use
                                          					 the CLI command set password . 
                                          				  For more information, see the Command Line Interface Reference Guide for CiscoUnified
                                             				  Solutions at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |

| Note | For this
                                                      				  test, you must use a disk or ISO file that is data only. |
|---|---|

| Note | You must reset each node in a cluster after you change its security password. Failure to reboot the nodes causes system service
                                                            problems and problems with the administration windows on the subscriber nodes. |
|---|---|

| Note | You are recommended to shutdown or restart through a virtual machine by a utils system shutdown CLI command. The system-history.log
                                          displays the command entry and is considered as a graceful shutdown. If the shutdown or restart is done from the vSphere client,
                                          then it is considered as an ungraceful shutdown and the entry is not available in the system-history.log. Shutdown/reboot
                                          from vSphere client is not supported from version 10.x onwards. |
|---|---|

| Note | If you force shutdown or restart the virtual machine from VMware administration tools (vCenter or Embedded Host Client): |
|---|---|

| Step 1 | From Cisco Unified OS Administration, choose Settings > Version . |
|---|---|
| Step 2 | Perform one of
                                       			 the following actions: Click Shutdown to stop all processes and shut down the
                                          				system. Click Restart to stop all processes and restart the
                                          				system. |