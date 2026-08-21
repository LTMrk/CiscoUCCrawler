---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-back-rest-html-153a10e30c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/back_rest.html
retrieved_at: 2026-08-21T23:39:42.317949+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Backing Up and Restoring Data

## Chapter: Backing Up and Restoring Data

- Restrictions for Backing Up and Restoring Data

## Backing Up and Restoring Data

Cisco Unified SRST Manager backup and restore functions use an FTP server to store and retrieve data. The backup function copies the files from Cisco Unified SRST Manager to the FTP server and the restore function copies the files from the FTP server to Cisco Unified SRST Manager. The FTP server can reside anywhere in the network as long as the backup and restore functions can access it with an IP address or hostname.

Tip It is recommended that you back up your configuration files whenever you make changes to the system or application files. Do backups regularly to preserve configuration data.

The system supports two types of backup: data and configuration. You can select one or both.

- Configuration—Backs up the system configuration, including registration credentials, configuration templates, central call agent, and so on.

- Data—Backs up system data.

Note It is strongly discouraged to back up only the data because of the potential of introducing inconsistency between configuration and data files.

Backups are performed only in offline mode. The system displays a message before performing the backup alerting you that the system will be taken offline.

Cisco Unified SRST Manager automatically numbers and dates the backup files. Performing different backup types at various times causes different backup IDs for data backups and configuration backups. For example, the last data backup ID might be 3, and the last configuration backup might be 4. Performing an “all” backup might result in a backup ID of 5 for both data and configuration.

When restoring the files, refer to the backup ID for the backup file that you want to use.

Note It is recommended that you back up your configuration files whenever changes are made to the system or application files. Back up data files, which contain voice messages, regularly, to minimize data loss, such as from a hardware failure.

### Restrictions for Backing Up and Restoring Data

- Both the backing up and restoring functions require that the system be in offline mode, so we recommend performing this task when call traffic is least impacted.

- Cisco Unified SRST Manager supports only full backup and restore. This feature does not support backing up or restoring select details of a configuration.

- If you change a configuration, then perform a system restore, the restore process will overwrite the changes to the configuration.