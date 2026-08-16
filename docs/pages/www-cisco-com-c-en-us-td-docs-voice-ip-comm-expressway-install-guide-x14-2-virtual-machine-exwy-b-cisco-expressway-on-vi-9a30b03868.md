---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-install-guide-x14-2-virtual-machine-exwy-b-cisco-expressway-on-vi-9a30b03868
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/install_guide/X14-2/virtual-machine/exwy_b_cisco-expressway-on-virtual-machine-installation-guide-x142/exwy_m_creating-a-backup-of-your.html
retrieved_at: 2026-08-16T22:13:10.587086+00:00
---

Cisco Expressway on Virtual Machine Installation Guide (X14.2)

# Cisco Expressway on Virtual Machine Installation Guide (X14.2)

Updated: August 14, 2022

Chapter: Creating a Backup of your System and Deleting Existing Snapshots

## Chapter: Creating a Backup of your System and Deleting Existing Snapshots

- Creating a Backup of your System and Deleting Existing Snapshots

- Creating Backups

- Deleting Existing Snapshots

# Creating a Backup of your System and Deleting Existing Snapshots

## Creating Backups

Do not take VMware snapshots of Cisco Expressway systems. The process interferes
                                          with database timing and negatively impacts performance.

Go to Maintenance > Maintenance Mode and switch Maintenance Mode On.

Go to Maintenance > Backup and Restore .

You can optionally add a password for your backup file.

Click Create system backup file .

Save the backup file.

When you restore your system from a backup, it does not include Active Directory credentials. You will need to add them in
                                                      order to access the Active Directory domain.

## Deleting Existing Snapshots

Make a backup of your configuration.

Shutdown the Expressway:

Go to Maintenance > Restart Options and click Shutdown .

Click OK to shut down the system.

Power off the VM.

Right-click on the VM and select Manage Snapshots .

In the Snapshot Manager , select Delete All Snapshots .

Click Yes in the confirmation dialog box.

Click Close to exit the Snapshot Manager.

| Caution | Do not take VMware snapshots of Cisco Expressway systems. The process interferes
                                          with database timing and negatively impacts performance. |
|---|---|

| Step 1 | Go to Maintenance > Maintenance Mode and switch Maintenance Mode On. |
|---|---|
| Step 2 | Go to Maintenance > Backup and Restore . |
| Step 3 | You can optionally add a password for your backup file. |
| Step 4 | Click Create system backup file . |
| Step 5 | Save the backup file. Note When you restore your system from a backup, it does not include Active Directory credentials. You will need to add them in
                                                      order to access the Active Directory domain. | Note | When you restore your system from a backup, it does not include Active Directory credentials. You will need to add them in
                                                      order to access the Active Directory domain. |
| Note | When you restore your system from a backup, it does not include Active Directory credentials. You will need to add them in
                                                      order to access the Active Directory domain. |

| Note | When you restore your system from a backup, it does not include Active Directory credentials. You will need to add them in
                                                      order to access the Active Directory domain. |
|---|---|

| Step 1 | Make a backup of your configuration. |
|---|---|
| Step 2 | Shutdown the Expressway: Go to Maintenance > Restart Options and click Shutdown . Click OK to shut down the system. |
| Step 3 | Power off the VM. |
| Step 4 | Right-click on the VM and select Manage Snapshots . |
| Step 5 | In the Snapshot Manager , select Delete All Snapshots . |
| Step 6 | Click Yes in the confirmation dialog box. |
| Step 7 | Click Close to exit the Snapshot Manager. |