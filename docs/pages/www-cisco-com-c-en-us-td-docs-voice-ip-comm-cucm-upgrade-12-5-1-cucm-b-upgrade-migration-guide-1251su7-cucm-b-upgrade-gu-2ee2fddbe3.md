---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-12-5-1-cucm-b-upgrade-migration-guide-1251su7-cucm-b-upgrade-gu-2ee2fddbe3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-1251su7/cucm_b_upgrade-guide-1251su2_chapter_01011.html
retrieved_at: 2026-08-17T00:08:37.395217+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU7

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)SU7

Updated: July 13, 2023

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

This section contains the following information:

## Dump a Log File After an Upgrade Failure

Use this procedure in the event of a failure when you are upgrading Unified Communications Manager or the IM and Presence Service .

### Before you begin

You need the 7-Zip utility to open the log files. Go to http://www.7-zip.org/download.html

Step 1

Attach a new, empty file to the serial port.  Edit the settings on the VM and attach the file name where you want the logs
                                       dumped.

If the system stops running
                                                      due to an upgrade failure and prompts you to dump the logs, you must attach the empty file before you
                                                      answer Yes and proceed.

Step 2

Return to the VM console, and dump the logs into the serial port.

Step 3

When the process is complete, click Inventory > Datastores and Datastore Clusters .

Step 4

Select the datastore where you created the file.

Step 5

Right-click and choose Browse Datastore and browse to the file that you created.

Step 6

Right-click the file, select Download , and select a location on your
                                       PC to save the file.

Step 7

Open the file using 7-Zip and check the file size:

- If the size of the file is larger than 0, extract the files to your PC and then edit the settings on the virtual machine to
                                          remove the serial port.

- If the file size is 0, proceed to the next step.

Step 8

If the file size is zero, complete the following steps:

Power off the virtual machine.

Create a new file for log output.

Unmap the installation disk.

On the Options tab, select Boot Options and enable Force BIOS Setup .

Power on the virtual machine and wait for it to boot to the BIOS.

In the BIOS, select the hard drive as the first boot device and save and
                                             exit.

Input yes to dump the contents of the
                                             log to a file.

Navigate to the file and open it using 7-Zip.

Step 9

If the size of the file is larger than 0, extract the files to your PC and then edit the settings on the virtual machine to
                                       remove the serial port.

## Troubleshooting Unified Communications Manager Upgrades

This section provides information about troubleshooting Unified Communications Manager upgrades.

### Upgrade
                           	 Failure

Problem The upgrade of a subscriber node fails after you upgrade the Unified Communications Manager publisher node and switch it to the new version, or the upgrade of one of the subscriber nodes in your cluster failed during
                                 the upgrade cycle.

Solution Do one of the following:

Correct the
                                       				errors that caused the upgrade failure on the subscriber node. You may want to
                                       				check the network connectivity of the nodes in your cluster, reboot the
                                       				subscriber node, and ensure that the server memory and CPU usage on the
                                       				subscriber node is not too high. Upgrade the subscriber node again.

Make sure that the active partition of the Unified Communications Manager publisher node runs the newest version of software installed on the server. Perform a fresh installation on the subscriber
                                       node using the same software version as that running on the active partition of the publisher node. If you are reinstalling
                                       the subscriber node, you should delete the server from Cisco Unified CM Administration and add the server again as described
                                       in the Administration Guide for Cisco Unified Communications Manager .

#### Retrying a Cluster or Single-node Upgrade

If you are retrying an upgrade without performing a Switch Version or Reboot in the previous upgrade, then, reboot the nodes
                                 before retrying.

### Reboot include on upgrade Success/Failed/Cancel case

Problem: Upgrades might fail or disturb if we didn’t reboot in below stages.

Solution: Reboot is required in the following scenarios:

Any upgrade (Legacy upgrade/Simple upgrade or Upgrade via PCD) get success or failure:

When an L2 upgrade fails, a reboot is required only in case when an upgrade is required again.

After a successful L2 upgrade, if you do not wish to switch to the new version and would like to upgrade again, you need to
                                             reboot the node first before starting the upgrade.

When an RU upgrade fails, it automatically switches to old partition and an automatic reboot is performed (if upgrade status
                                             is failed, cancel the upgrade and reboot the node).

If the Switch version fails, you should reboot the server before you attempt any further action, as it may stop/ halt the
                                       Service Manager and other services that could impact functionalities.

If you cancel any upgrade at any stage, you should reboot the IM&P/ UCM servers before you attempt any other upgrade.

### Troubleshooting Simplified Upgrade Issues

#### Download Failure in Some Nodes of the Cluster

Problem : Download failed in some nodes of the cluster while performing simplified upgrade.

Solution : Verify the Software location configuration for the nodes that failed to download. Invalid location or wrong credentials
                                 may cause the failure. If you are using the 'Use download credentials from publisher' option, then, ensure that the configuration
                                 of the failed node is correct.

To verify, perform one of the following:

User Interface: Open the Install/Upgrade page of the node and see if the check box is checked. If it is checked, it indicates that the configuration is correct. If
                                       the check box is not checked, check it and click Next to save the configuration and then click Cancel to exit from the Install/Upgrade page.

CLI: Use the utils system upgrade initiate command, and ensure that ‘Use download credentials from Publisher (yes/no)’ is set to ‘yes’. If it is set to ‘yes’, it indicates
                                       that the configuration is correct. If not, set it to ‘yes’ and come out by selecting ‘q’ and execute the utils system upgrade cancel command for a clean exit.

Use download credentials from Publisher is unselected and the Unified Communications Manager cluster upgrade may fail because the subscriber will not use the same
                                             download credentials of publisher. Need to go to each Subscriber and select the option " Use download credential from Publisher ", for the subscriber to use the publisher download credentials.

#### Download or Installation Failure in Some Nodes of the cluster

Problem : Download or Installation failed in some nodes of the cluster while performing simplified upgrade.

Solution : Open the Install/Upgrade Cluster page using User Interface or the utils system upgrade cluster status command using the CLI and identify the failed nodes. Verify that the upgrade or install operation is not already in progress
                                 on those failed nodes by executing the utils system upgrade status command from the CLI. Follow the single node upgrade troubleshooting steps given in the 'Upgrade Failure' subsection in the
                                 'Troubleshooting Unified Communications Manager Upgrades' section to continue the upgrade.

When simplified upgrade fails in Download or Install phase:

User Interface: Install/Upgrade Cluster page displays the status of each node to identify the failed nodes until cancel is clicked.

CLI: utils system upgrade cluster initiate or utils system upgrade cluster status displays the status of each node to identify the failed nodes until the utils system upgrade cluster cancel command is executed.

#### Switch Version or Reboot Failure in Some Nodes of the Cluster

Problem : Switch version or reboot failed in some nodes of the cluster while performing simplified upgrade.

Solution : Open the Restart/Switch-Version Cluster page using User Interface and identify the failed nodes. Fix the issues (network/certificate issue etc.) and retry the switch
                                 version or reboot on the failed nodes by skipping the completed nodes in the Restart/Switch-Version Cluster page.

#### Unified Communications Manager Publisher was rebooted/power-cycled During Cluster Upgrade and the Cluster Upgrade Status is
                                 not Visible

Problem : The Unified Communications Manager Publisher was rebooted/power cycled during cluster upgrade and the cluster upgrade status was not visible.

Solution : The Unified Communications Manager Publisher controls the cluster upgrade operations. You must not reboot or power cycle it during an upgrade. If you do that,
                                 the processes are killed and you cannot get status from other nodes. Also, the Unified Communications Manager Publisher will not be able to provide instructions to other nodes and results in upgrade failures. Login to each node and
                                 cancel the upgrade.

#### High CPU Alerts During Cluster Upgrade

Problem : High CPU alerts were received during Cluster upgrade

Solution : You need to schedule cluster upgrades during the least server usage. The upgrade processes are CPU and Disc-intensive and
                                 can cause CPU Alerts.

#### Retrying a Cluster Upgrade after a Failed Cluster Upgrade

Problem : How to retry a cluster upgrade after a failed cluster upgrade?

Solution : First, cancel the cluster upgrade. We recommend that you reboot the nodes after a failed upgrade before retrying an upgrade.

#### Download Failure due to SSL Error

Problem : Download failed in a few nodes nodes due to SSL error.

Solution : Ensure that the cluster has SSL trust set up between the nodes.

#### The Switch Version or Reboot of Cluster Nodes did not Occur as per the Modified Batch

Problem : The switch version or reboot of cluster nodes did not occur as per the modified batch.

Solution : Before starting a cluster reboot or switch version, ensure that the modified batch orders are saved.

#### Changes to 'Skip' Checkbox are not Saved

Problem : Skip check box selections are not saved.

Solution : The 'skip' option is used to exclude a node during reboot or switch version and this selection is not saved. You need to
                                 select the option every time.

#### Unable to Retry Cluster Upgrade or Single-node Upgrade

Problem : Unable to retry cluster upgrade or single-node upgrade.

Solution : Perform a cluster upgrade cancel by executing the utils system upgrade cluster cancel command using the CLI. Also, perform a single-node cancel on the Unified Communications Manager Publisher by executing the utils system upgrade cancel command using the CLI

### Upgrade Fails with Insufficient Disk Space

Problem The upgrade of Unified Communications Manager fails with an error stating that the common partition is full.

Solution Typically, you need at least 25G of common partition space; however, your deployment may require more space if you have a
                                 lot of TFTP data (device firmware loads), music-on-hold (MOH) files, or if you have many locale files installed. Perform one
                                 or more of the following actions to create additional disk space:

Use the Cisco Log Partition Monitoring Tool to adjust the low and high watermarks to reduce the traces and remove unnecessary
                                       log files. Cisco recommends that you adjust the low watermark value to 30, and the high watermark value to 40. After the upgrade,
                                       you must restore the high and low watermarks to their original values in order to avoid premature purging of traces. The default
                                       value for the high watermark is 85. The default value for the low watermark is 80. For more information about using the Cisco
                                       Log Partition Monitoring Tool, see the Cisco Unified Real-Time Monitoring Tool Administration Guide .

Use the Disk Expansion COP file (ciscocm.vmware-disk-size-reallocation-<latest_version>.cop.sgn) to expand the vDisk size
                                       if your virtual environment has additional available disk space. Ensure that you review the Readme file that supports this
                                       COP file before you proceed.

Use the Free Common Space COP file (ciscocm.free_common_space_v<latest_version>.cop.sgn). This COP file removes the inactive
                                       side in the common partition to increase available disk space without requiring a system rebuild. Ensure that you review the
                                       Readme file that supports this COP file before you proceed.

Manually remove outdated or unused firmware files from the TFTP directory. You can remove these files using the TFTP File
                                       Management page in the OS Administration interface, or you can use the file list tftp and file delete tftp commands from the command line interface.

You can download COP files and their Readme files from Cisco.com. Navigate to Support > Downloads > Cisco Unified Communications Manager Version 10.0 >   Unified Communications Manager/CallManager/Cisco
                                       Unity Connection Utilities .

### Resuming a Failed Upgrade

If you find any errors in your system and you have to fix it before resuming an upgrade, follow this process:

You need to restart the node and reinitiate the upgrade process if there is a failure.

Step 1

Cancel the upgrade.

The ISO file download is retained if fully downloaded, even if you cancel the upgrade.

Step 2

Fix your system issue.

Step 3

When you are ready to resume your upgrade, run the utils system upgrade initiate CLI command and select the Local Image option.

Step 4

Complete your system upgrade.

### Reduced Permissions for Access Control Groups

Problem When you add a new access control group to existing users, the level of privileges for some pre-existing access control
                                 groups is unexpectedly reduced.

Solution Users can belong to multiple access control groups. When you add a new access control group to existing users, the current
                                 level of privileges for some pre-existing access control groups may be reduced if the new access control group has the "Effective Access Privileges for Overlapping User Groups and Roles" Enterprise parameter set to minimum.

Access privilege reduction can occur inadvertently, for example, during an upgrade of Cisco Unified CM Administration. If
                                 the upgrade version supports the Standard RealTimeAndTrace Collection user group, which has the "Effective Access Privileges for Overlapping User Groups and Roles" Enterprise parameter set to minimum, all users are automatically added to that user group during the upgrade. To resolve
                                 the permissions issue in this example, you can remove users from the Standard RealTimeAndTrace Collection user group.

### Loss of Phone Settings

For a short period of time after you install Unified Communications Manager or switch over after upgrading to a different product version, settings that were configured by phone users may be reset.
                                 Examples of settings configured by phone users include call forwarding and message waiting indication settings. This situation
                                 can occur if there have been configuration changes during the upgrade window. When Unified Communications Manager synchronizes the database after an installation or upgrade, it can overwrite setting changes made by phone users. Cisco recommends
                                 that you do not make configuration changes during an upgrade.

### Post-Upgrade Failure of Unified Communications Manager Publisher Node

Problem The upgrade is successful and the cluster is running the new release, but the Unified Communications Manager publisher node subsequently fails.

Solution Do one of the following:

restore the Unified Communications Manager publisher node use a DRS backup file

if you do not have a DRS backup file, you must reinstall the entire cluster, including any IM and Presence Service nodes

### Post-Upgrade Failure of Unified Communications Manager Subscriber Nodes

Problem The upgrade is successful and the cluster is running the new release, but a Unified Communications Manager subscriber node subsequently fails.

Solution Do one of the following:

Restore the Unified Communications Manager subscriber node use a DRS backup file.

If you do not have a DRS backup file, you must perform the upgrade on the subscriber node again. You do not need to remove
                                       the subscriber node from the Unified Communications Manager publisher node's server page before you reinstall it.

## Troubleshooting IM and Presence Upgrades

This section provides information about troubleshooting IM and Presence Service Service upgrades.

### Upgrade Failure of IM and Presence Database Publisher Node

Problem You are upgrading a multinode cluster that includes both Unified Communications Manager and IM and Presence Service nodes, and the upgrade of the IM and Presence Service database publisher node fails.

Solution The action that you take depends on the point at which the failure occurred:

if the upgrade on the IM and Presence Service database publisher node fails before the refresh upgrade causes the node to reboot (that is, if the node failed before switching
                                       to the new partition), perform the upgrade again on the IM and Presence Service database publisher node

If the failure occurred after the IM and Presence Service database publisher node switched to the new software version, you must switch back all the nodes and perform the upgrade
                                       again. Complete the following tasks in the order listed:

switch back the Unified Communications Manager publisher node

switch back the Unified Communications Manager subscriber nodes

switch back the IM and Presence Service database publisher node

upgrade the Unified Communications Manager publisher node again

switch the Unified Communications Manager publisher node forward to the new software version

upgrade the Unified Communications Manager subscriber nodes again

switch the Unified Communications Manager subscriber nodes forward to the new software version

upgrade the IM and Presence Service database publisher node again

### Upgrade Failure of IM and Presence Subscriber Node

Problem You are upgrading a multinode cluster that includes both Unified Communications Manager and IM and Presence Service nodes, and the upgrade of the IM and Presence Service subscriber node fails.

Solution The action that you take depends on the point at which the failure occurred:

if the upgrade on the IM and Presence Service subscriber node before the refresh upgrade causes the node to reboot (that is, if the node failed before switching to the
                                       new partition), perform the upgrade again on the IM and Presence Service subscriber node

if the upgrade on the IM and Presence Service subscriber node fails after the node switched to the new version, you must complete the following tasks in the order listed:

switch the Unified Communications Manager publisher node back to the earlier software version

switch the Unified Communications Manager subscriber node back to the earlier software version

switch the IM and Presence Service database publisher node back to the earlier software version

switch the IM and Presence Service subscriber nodes back to the earlier software version

switch the Unified Communications Manager publisher node pub forward to the new software version

switch the IM and Presence Service database publisher node forward to the new software version

perform the upgrade again on the IM and Presence Service subscriber node

### Upgrade From Pre
                           	 Release 8.6(4) Fails

Problem You are upgrading from a
                                 		  release earlier than Cisco Unified Presence 8.6(4) and the upgrade fails on
                                 		  both the publisher and subscriber nodes.

Solution The Unified Communications Manager hostname is case-sensitive. You must ensure that the entry for the Unified Communications Manager publisher node on the Cisco Unified Presence Administration interface matches exactly the Unified Communications Manager hostname. Complete the following procedure:

Log into Cisco Unified Presence Administration interface and choose System > CUCM Publisher .

If the CUCM Publisher Hostname value does not match the hostname, modify it and click Save .

Restart the Cluster Manager service with the following CLI command: utils service restart Cluster Manager

Open the platformConfig.xml file at the following location: /usr/local/platform/conf/

Verify that the values for IPSecMasterHost and NTPServerHost match exactly the Cisco Unified Communications Manager hostname.

If necessary, modify the value for IPSecMasterHost and NTPServerHost , save the platformConfig.xml file and restart the Cluster Manager service again.

### IM and Presence user phone presence problems

Problem After an IM and Presence server upgrade, when all activated feature services and
                                 		  network services are started, IM and Presence phone presence from users is delayed or slow to update.

Solution You must restart the Cisco SIP Proxy service. In Cisco Unified
                                    		  IM and Presence Serviceability , select Tools > Control Center - Features Services .

### Presence User Experiences Issues Obtaining Availability

Problem After an IM and Presence Service server upgrade, when all activated feature services and network services are started, a user experiences inconsistent presence
                                 availability. The user can log in to IM and Presence Service but experiences issues obtaining availability information mainly from SIP-based clients.

Solution This issue is caused when users are provisioned while IM and Presence Service is being upgraded. You must unassign and then reassign the user.

### Real-Time Monitoring Tool alert for Cisco SIP proxy service

Problem After an IM and Presence Service server upgrade, when all activated feature services and network services are started, a Real-Time Monitoring Tool CoreDumpFileFound
                                 alert was generated for the Cisco SIP Proxy service.

Solution You must restart the Cisco SIP Proxy service. In Cisco Unified
                                    		  IM and Presence Serviceability , select Tools > Control Center - Features Services .

### Cannot find upgrade file on remote server

Problem You cannot find the upgrade file on the remote server.

Solution If the upgrade file is located on a Linux or Unix server, you must
                                 		  enter a forward slash at the beginning of the directory path that you want to
                                 		  specify. For example, if the upgrade file is in the patches directory, you must
                                 		  enter /patches . If the upgrade file is located on a
                                 		  Windows server, check with your system administrator for the correct directory
                                 		  path.

### Upgrade file checksum values do not match

Problem The checksum value of the upgrade file does not match the checksum
                                 		  indicated on Cisco.com.

Solution The two checksum values must match to ensure the authenticity and
                                 		  integrity of the upgrade file. If the checksum values do not match, download a
                                 		  fresh version of the file from Cisco.com and try the upgrade again.

### Database replication did not complete

Problem After an upgrade, database replication did not complete and the result
                                 		  of the command utils dbreplication runtimestate was not 2.

Solution After a successful upgrade and switch version to the new software,
                                 		  database replication should take place automatically. During this time core
                                 		  services on the subscriber nodes will not start. Database replication in large
                                 		  deployments can take several hours to complete. If, after several hours, the utils dbreplication runtimestate command shows that database replication did not
                                 		  complete, you need to reset the database replication. Run the following command
                                 		  on the publisher node: utils dbreplication reset all

### Cisco UP Presence Engine database does not restart

Problem After you switch back to Cisco Unified Presence Release 8.6(3) or an earlier software version, the Cisco UP Presence Engine
                                 database does not restart.

Solution Ensure that you installed the required COP file, ciscocm.cup.pe_db_install.cop , on every node in the cluster after you switched back to Cisco Unified Presence Release 8.6(3), or earlier.

### Version Errors

#### Selected Upgrade  Is Disallowed From the Current Version

Problem During a refresh upgrade, the following error is reported: Error encountered: The selected upgrade is disallowed from the current version .

Solution You did not install the required COP file on the node. Download the following COP file from Cisco.com: ciscocm.cup.refresh_upgrade_v<latest_version>.cop . Restart the server. Install the COP file on every node in the cluster before you attempt the refresh upgrade again.

#### Version Does Not Match the Active or Inactive Version

Problem During an upgrade on a IM and Presence Service server, you cannot select the software image from the disk or remote directory. The following error is reported: The version obtained from the name does not match the active or inactive version of the publisher.

Solution The version matching rules have not been met. The software versions must meet the following requirements:

The software version of the IM and Presence Service database publisher node (the first IM and Presence Service node that you upgrade) must match the first two numbers of the software version installed on the Unified Communications Manager publisher node. The software version installed on the Unified Communications Manager publisher node may be active or inactive. For example, IM and Presence Service software version 10.0.1.10000-1 is compatible with Unified Communications Manager software version 10.0.1.30000-2. Make sure to follow sequence rules while upgrading Unified Communications Manager and IM
                                       and Presence Service nodes.

The software version of the IM and Presence Service subscriber nodes that you upgrade must match five numbers of the software version installed on the IM and Presence Service database publisher node.

Ensure that the first node that you upgrade is either the Unified Communications Manager publisher node or the IM and Presence Service database publisher node, or select a different image for the software upgrade.

#### Switch Version on Cisco IM and Presence Node Fails

Problem Switching the version on the Cisco IM and Presence node fails. The following error is reported: Version mismatch. Please switch versions on the publisher and try again.

Solution The version matching rules have not been met. The software versions must meet the following requirements:

The software version of the IM and Presence Service database publisher node (the first IM and Presence Service node that you upgrade) must match the first two numbers of the software version installed on the Unified Communications Manager publisher node. For example, IM and Presence Service Service software version 10.0.1.10000-1 is compatible with Unified Communications Manager software version 10.0.1.30000-2.

The software version of the IM and Presence Service subscriber nodes that you upgrade must match five numbers of the software version installed on the IM and Presence Service database publisher node.

To correct this error, ensure that the first node that you switch is either the Unified Communications Manager publisher node or the IM and Presence Service database publisher node.

### Failed refresh upgrade

Problem A refresh upgrade failed.

Solution Restart the system, it should reboot to the software version that was running before you attempted the refresh upgrade. If
                                 you cannot access the system, you must use the Recovery CD to recover the node.

### Cancelled or failed upgrade

If you cancel an upgrade at any stage, or if an upgrade fails, you must reboot the IM and Presence Service server before you attempt another upgrade.

### Directory Was Located and Searched but No Valid Options or Upgrades Were Available

Problem During an IM and Presence Service upgrade, the IM and Presence Service server generates the following error message, even though the upgrade path and file are valid:

The directory was located and searched but no valid options or upgrades were available. Note, a machine cannot be downgraded
                                    so option and upgrade files for previous releases were ignored .

Solution The upgrade manager checks for connectivity between IM and Presence Service and Unified Communications Manager to validate the version during the upgrade. If this fails, the IM and Presence Service server generates the error message even though the upgrade path and file are valid. Use a tool, such as the Cisco Unified
                                 CM IM and Presence Administration System Troubleshooter, to check that there is connectivity between IM and Presence Service and Unified Communications Manager before proceeding with the upgrade.

### Common Partition Full Upgrade Failure

Problem The upgrade of IM and Presence Service fails with an error stating that the common partition is full.

Solution Download and apply the COP file ciscocm.free_common_cup_space_v<latest_version>.cop.sgn . This COP file cleans up the common partition and allows subsequent upgrades to proceed as normal.

| Step 1 | Attach a new, empty file to the serial port.  Edit the settings on the VM and attach the file name where you want the logs
                                       dumped. Note If the system stops running
                                                      due to an upgrade failure and prompts you to dump the logs, you must attach the empty file before you
                                                      answer Yes and proceed. | Note | If the system stops running
                                                      due to an upgrade failure and prompts you to dump the logs, you must attach the empty file before you
                                                      answer Yes and proceed. |
|---|---|---|---|
| Note | If the system stops running
                                                      due to an upgrade failure and prompts you to dump the logs, you must attach the empty file before you
                                                      answer Yes and proceed. |
| Step 2 | Return to the VM console, and dump the logs into the serial port. |
| Step 3 | When the process is complete, click Inventory > Datastores and Datastore Clusters . |
| Step 4 | Select the datastore where you created the file. |
| Step 5 | Right-click and choose Browse Datastore and browse to the file that you created. |
| Step 6 | Right-click the file, select Download , and select a location on your
                                       PC to save the file. |
| Step 7 | Open the file using 7-Zip and check the file size: If the size of the file is larger than 0, extract the files to your PC and then edit the settings on the virtual machine to
                                          remove the serial port. If the file size is 0, proceed to the next step. |
| Step 8 | If the file size is zero, complete the following steps: Power off the virtual machine. Create a new file for log output. Unmap the installation disk. On the Options tab, select Boot Options and enable Force BIOS Setup . Power on the virtual machine and wait for it to boot to the BIOS. In the BIOS, select the hard drive as the first boot device and save and
                                             exit. The system will boot to the hard drive and go back to the point where the
                                             upgrade failed. A failure notification displays. Input yes to dump the contents of the
                                             log to a file. Navigate to the file and open it using 7-Zip. |
| Step 9 | If the size of the file is larger than 0, extract the files to your PC and then edit the settings on the virtual machine to
                                       remove the serial port. |

| Note | If the system stops running
                                                      due to an upgrade failure and prompts you to dump the logs, you must attach the empty file before you
                                                      answer Yes and proceed. |
|---|---|

| Note | Use download credentials from Publisher is unselected and the Unified Communications Manager cluster upgrade may fail because the subscriber will not use the same
                                             download credentials of publisher. Need to go to each Subscriber and select the option " Use download credential from Publisher ", for the subscriber to use the publisher download credentials. |
|---|---|

| Note | When simplified upgrade fails in Download or Install phase: User Interface: Install/Upgrade Cluster page displays the status of each node to identify the failed nodes until cancel is clicked. CLI: utils system upgrade cluster initiate or utils system upgrade cluster status displays the status of each node to identify the failed nodes until the utils system upgrade cluster cancel command is executed. |
|---|---|

| Note | You need to restart the node and reinitiate the upgrade process if there is a failure. |
|---|---|

| Step 1 | Cancel the upgrade. The ISO file download is retained if fully downloaded, even if you cancel the upgrade. |
|---|---|
| Step 2 | Fix your system issue. |
| Step 3 | When you are ready to resume your upgrade, run the utils system upgrade initiate CLI command and select the Local Image option. |
| Step 4 | Complete your system upgrade. |