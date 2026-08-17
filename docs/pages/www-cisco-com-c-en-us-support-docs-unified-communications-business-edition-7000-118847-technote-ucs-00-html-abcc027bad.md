---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-business-edition-7000-118847-technote-ucs-00-html-abcc027bad
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/business-edition-7000/118847-technote-ucs-00.html
retrieved_at: 2026-08-17T01:47:53.945485+00:00
---

BE7000 Migration from Single RAID5 Volume to Dual RAID5 Arrays without VM Rebuild

# BE7000 Migration from Single RAID5 Volume to Dual RAID5 Arrays without VM Rebuild

### Download Options

Updated: March 19, 2015

Document ID: 118847

Contents

## Contents

## Introduction

This document describes the process for how to convert a Business Edition 7000 server that is configured with a single, 12-disk Redundant Array of Independent Disks (RAID) 5 volume to two, 6-disk RAID 5 volumes.

## Problem

Some Cisco Business Edition 7000 (BE7K) servers manufacturered prior to August of 2014 shipped from the factory with a single, 12-disk RAID 5 virtual drive. The Unified Communications (UC) on Unified Computing System (UCS) documentation specifies that this server and its equivalent Tested Reference Configuration (TRC) (C240 M3 SFF TRC2) use two RAID 5 virtual drives of 6 disks each.

If you change the array configuration on the UCS C240M3, it erases all data on the disks that are reconfigured. This means that ESXi must be re-installed and that you must re-apply ESXi licenses, reconfigure ESXi, and restore the Virtual Machines (VMs) in order to complete this migration.

It is easy to identify when the BE7K has an incorrect virtual disk configuration. In the vSphere client, navigate to Home > Inventory > Inventory . Select the BE7K server on the left, and then the Configuration tab . Finally, select Storage and ensure Datastores is selected.

This is what the datstore looks like for a BE7K with a single, 12-disk RAID5 virtual disk from the vSphere client.

Note : The local disk datastore has a capacity of 2.99TB.

This is what a BE7K should look like when correctly configured with two 6-disk RAID 5 virtual disks.

Note : The two local disk datastores each have 1.35TB of space.

## Solution

In order to make this process as easy as possible, complete these steps:

- Take application-level backups of all VMs that run on the BE7K.

- Back up the ESXi configuration and license(s). (Refer to the Backing up and restoring ESXi configuration using the vSphere Command-Line Interface and vSphere PowerCLI (2042141) article for more information.)

- vMotion the VMs to another host and datastore.

- Gracefully shutdown the VMs and copy everything on the local datastore to an external storage location.

- Reboot the BE7K and reconfigure the RAID array with two 6-disk RAID 5 logical disks.

- Apply ESXi Licenses.

- Restore ESXi configuration. (Refer to the Backing up and restoring ESXi configuration using the vSphere Command-Line Interface and vSphere PowerCLI (2042141) article for more information.)

- Move all VMs back onto the BE7K and start them back up.

## Detailed Instructions

### Take Application-Level Backups of VMs

Follow the instructions in the Cisco.com documentation for the UC application in order to take a backup and save it to a safe location. For applications that use Disaster Recovery System (DRS), the Secure Shell FTP (SFTP) server should not be hosted on the BE7K for obvious reasons.

### Back Up ESXi Configuration and License

Reference these two VMware KB articles in order to gain access to the vSphere CLI and perform a backup.

- Using ESXi Shell in ESXi 5.x (2004746)

- Backing up and restoring ESXi configuration using the vSphere Command-Line Interface and vSphere PowerCLI (2042141)

Here is an example of how to use the ESXi shell in order to back up the configuration.

```
~ # vim-cmd hostsvc/firmware/sync_config ~ # vim-cmd hostsvc/firmware/backup_config Bundle can be downloaded at : http://*/downloads/ configBundle-RTP-CUCM-BE7K-1.cisco.com.tgz
```

For this example, you can download the backup archive from https://rtp-cucm-be7k-1.cisco.com/downloads/configBundle-RTP-CUCM-BE7K-1.cisco.com.tgz .

The contents of this bundle include the license.cfg file. This confirms that the ESXi backup and restore operation includes licenses.

### Move VMs Off the Local Datastore

If the BE7K is part of a VCenter deployment, then the VMs should be migrated to shared storage so they can be run on an alternate host while the BE7K is under maintenance. If there is no shared storage available, then the process is as described here:

- Gracefully shut down and power off all VMs on the BE7K.

- Use the vSphere client in order to copy all files on the BE7K datastore to an alternate location.

If no alternate storage location is available to store the VMs and other content on the BE7K datastore, then open a Cisco Technical Assistance Center (TAC) Service Request (SR) so that other options can be explored. Be sure to cite this docuement when you open a TAC SR for this issue.

### Reconfigure the Array

Follow the steps in Cisco Collaboration on Virtual Servers in order to reconfigure the array for two 6-disk RAID5 logical disks. If you use extra Hard Disk Drives (HDDs) in the BE7K for backup purposes, be careful to not to delete the RAID 0 drive group or select New Configuration in the preboot GUI's configuration wizard.

### Re-install and Reconfigure ESXi

- Follow the steps in About vSphere Installation and Setup if you are not familiar with how to install ESXi.

- If you backed up the ESXi configuration, follow the instructions in Backing up and restoring ESXi configuration using the vSphere Command-Line Interface and vSphere PowerCLI (2042141) in order to restore the backup.

- Select Disk/Lun for the Storage Type.

- If multiple options are available, select the disk with a capacity of 1.36TB.

- Select the defaults for the rest of the wizard until you are prompted to provide a name for the datastore.

### Move VMs Back Onto the Local Datastore

This step is simply the reverse of whatever method you used to copy the VMs off of the old datastore.

If you use vCenter in order to migrate the VMs from shared storage back to the BE7K, then the VMs can be powered on immediately after they are migrated. If you manually copy the files back to the datastore, then you must use the vSphere client in order to import the VMs back into ESXi before they can be powered on.

If you used the vSphere datastore browser in order to move files, then it is likely you will see a message like the one here when you import the VMs back into ESXi. Select whether the VM was moved or copied (as appropriate) and click OK in order to proceed.

Note : Because this process reduced the size of the previous datastore from 2.99TB to two separate 1.39TB volumes, it is possible the files that were copied off of the BE7K will not fit onto a single datastore. If this is the case, you should distribute the VMs among the two datastores, and make sure to leave plenty of free space on both.

### Revision History

1.0

19-Mar-2015

Initial Release

### Contributed by Cisco Engineers

Ryan Ratliff

Cisco TAC Engineer.

### This Document Applies to These Products

- Business Edition 7000

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Mar-2015 | Initial Release |