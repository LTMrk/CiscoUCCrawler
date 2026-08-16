---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-15-cucm-b-upgrade-and-migration-guide-15-cucm-m-upgrading-from--b491051e2f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/15/cucm_b_upgrade-and-migration-guide_15/cucm_m_upgrading-from-legacy-releases.html
retrieved_at: 2026-08-16T23:33:05.614494+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 and SUs

Updated: August 14, 2026

Chapter: Upgrading from Legacy Releases

## Chapter: Upgrading from Legacy Releases

- Upgrading from Legacy Releases

- Upgrading and Migrating from Legacy Releases

# Upgrading from Legacy Releases

## Upgrading and Migrating from Legacy Releases

If a direct upgrade or migration from your current release is not supported, you can use the following process:

perform a direct upgrade to an intermediate release using either the Unified CM OS Admin interface or the Cisco Prime Collaboration
                                    Deployment (PCD) Upgrade task

perform a migration from the intermediate release to the current release using the PCD Migration task

Find your starting release in the table below and use it to identify the intermediate releases that you can use as steps in
                              the upgrade and migration process. After you have identified the intermediate release, use the links in the steps below to
                              find the documentation for that release.

If your starting release is not listed, it may require an upgrade to more than one intermediate release. See the "Supported
                              Upgrade and Migration Paths with COP Files" table at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/15_x/cucm_b_compatibility-matrix-cucm-imp-15x.html .

Installed Version

Migrate to this Version on a Virtual Machine

7.0(1) and older

Migration is not possible. You are recommended to rebuild to the latest release from scratch.

8.0(1) and 9.1

Using PCD 12.6 (not PCD 14 or PCD 15), direct migrate to version 12.5. See the initial chapters in this guide to go through
                                          the various migration options possible.

Step 1

Refer to the upgrade documentation for the intermediate release and follow the instructions to upgrade your system.

- For Unified Communications Manager upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

- For IM and Presence Service (formerly Cisco Unified Presence) upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-guides-list.html .

Step 2

Refer to the Cisco Prime Collaboration Deployment Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html and follow the instructions to perform a PCD migration to the current release.

| Installed Version | Migrate to this Version on a Virtual Machine |
|---|---|
| 7.0(1) and older | Migration is not possible. You are recommended to rebuild to the latest release from scratch. |
| 8.0(1) and 9.1 | Using PCD 12.6 (not PCD 14 or PCD 15), direct migrate to version 12.5. See the initial chapters in this guide to go through
                                          the various migration options possible. |

| Step 1 | Refer to the upgrade documentation for the intermediate release and follow the instructions to upgrade your system. For Unified Communications Manager upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . For IM and Presence Service (formerly Cisco Unified Presence) upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-guides-list.html . |
|---|---|
| Step 2 | Refer to the Cisco Prime Collaboration Deployment Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html and follow the instructions to perform a PCD migration to the current release. |