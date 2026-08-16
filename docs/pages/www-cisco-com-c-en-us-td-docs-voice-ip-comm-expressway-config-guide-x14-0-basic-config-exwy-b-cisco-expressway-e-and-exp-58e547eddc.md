---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-58e547eddc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_maintenance-routine.html
retrieved_at: 2026-08-16T15:27:53.520192+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Maintenance Routine

## Chapter: Maintenance Routine

# Maintenance Routine

## Creating a System Backup

### Before You Begin

From X8.11, backup files are always encrypted. In particular because they include the bootstrap key, and authentication data
                                    and other sensitive information.

Backups can only be restored to a system that is running the same version of software from which the backup was made .

You can create a backup on one Expressway and restore it to a different Expressway. For example if the original system has
                                    failed. Before the restore, you must install the same option keys on the new system that were present on the old one.

If you try to restore a backup made on a different Expressway, you receive a warning message, but you will be allowed to continue.

(If you use FIPS140-2 cryptographic mode) You can't restore a backup made on a non-FIPS system, onto a system that's running
                                    in FIPS mode. You can restore a backup from a FIPS-enabled system onto a non-FIPS system.

Do not use backups to copy data between Expressways. If you do so, system-specific information will be duplicated (like IP
                                    addresses).

Because backup files contain sensitive information, you should not send them to Cisco in relation to technical support cases.
                                    Use snapshot and diagnostic files instead.

### Passwords

From X8.11, all backups must be password protected.

If you restore to a previous backup, and the administrator account password has changed since the backup was done, you must
                                    also provide the old account password when you first log in after the restore.

Active Directory credentials are not included in system backup files. If you use NTLM device authentication, you must provide the Active Directory password to
                                    rejoin the Active Directory domain after any restore.

For backup and restore purposes, emergency account passwords are handled the same as standard administrator account passwords.

## Process

Go to Maintenance > Backup and restore .

Enter an Encryption password to encrypt the backup file.

The password will be required in future if you ever want to restore the backup file.

Click Create system backup file .

Wait for the backup file to be created. This may take several minutes. Do not navigate away from this page while the file
                                       is being prepared.

When the backup is ready, you are prompted to save it. The default filename uses format:

<software version>_<hardware serial number>_<date>_<time>_backup.tar.gz.enc.

Or

If you use Internet Explorer, the default extension is .tar.gz.gz .

(These different filename extensions have no operational impact, and you can create and restore backups using any supported
                                          browser.)

Save the backup file to a secure location.

| Step 1 | Go to Maintenance > Backup and restore . |
|---|---|
| Step 2 | Enter an Encryption password to encrypt the backup file. Caution The password will be required in future if you ever want to restore the backup file. | Caution | The password will be required in future if you ever want to restore the backup file. |
| Caution | The password will be required in future if you ever want to restore the backup file. |
| Step 3 | Click Create system backup file . |
| Step 4 | Wait for the backup file to be created. This may take several minutes. Do not navigate away from this page while the file
                                       is being prepared. |
| Step 5 | When the backup is ready, you are prompted to save it. The default filename uses format: <software version>_<hardware serial number>_<date>_<time>_backup.tar.gz.enc. Or If you use Internet Explorer, the default extension is .tar.gz.gz . (These different filename extensions have no operational impact, and you can create and restore backups using any supported
                                          browser.) |
| Step 6 | Save the backup file to a secure location. |

| Caution | The password will be required in future if you ever want to restore the backup file. |
|---|---|