---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-14-0-1-cucm-b-upgrade-and-migration-guide-14su3-cucm-b-upgrade--ac296c6abd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/14_0_1/cucm_b_upgrade-and-migration-guide_14su3/cucm_b_upgrade-guide-1251su2_chapter_0111.html
retrieved_at: 2026-08-17T00:05:22.599556+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14SU3 and SU4

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14SU3 and SU4

Updated: July 15, 2026

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
                              Upgrade Paths To/From Table" at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/ccmcompmatr1.html#pgfId-391518 .

Installed Version

Upgrade to this Version on MCS hardware

Migrate to this Version on  a Virtual Machine

Uinified Communications Manager Releases

4.x

Migrate to 6.1(5), 7.1(3), or 7.1(5) using Uinified Communications Manager Data Migration Assistant (DMA)

Check the Software Compatibility Matrix for the intermediate release to find the supported upgrade path from your current release, or see the "Supported Upgrade
                                          Paths To/From Table" at the link above.

PCD Migration to 12.x

5.1(2)

5.1(3)

6.0(x)

6.1(1)

6.1(2)

6.1(3)

6.1(4)

Direct Upgrade to 6.1(5) or 7.1(3)

PCD Migration to 12.x

7.0(1)

7.1(2)

7.1(3), 7.1(5), 8.0(x), 8.5(1), or 8.6(2)

PCD Migration to 12.x

Cisco Unified Presence Releases

8.0(x)

Direct Upgrade to 8.5(4)

PCD Migration to 12.0(1)

Uinified Communications Manager Business Edition Releases

Business Edition 3000 (BE3000)

Upgrades and migrations to Unified Communications Manager Release 12.x are not supported for these deployments. We recommend that you perform a fresh installation for upgrades from
                                          these products to the current Unified Communications Manager release.

Business Edition 5000 (BE5000)

Step 1

Refer to the upgrade documentation for the intermediate release and follow the instructions to upgrade your system.

- For Unified Communications Manager upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

- For IM and Presence Service (formerly Cisco Unified Presence) upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-guides-list.html .

Step 2

Refer to the Cisco Prime Collaboration Deployment Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html and follow the instructions to perform a PCD migration to the current release.

| Installed Version | Upgrade to this Version on MCS hardware | Migrate to this Version on  a Virtual Machine |
|---|---|---|
| Uinified Communications Manager Releases |
| 4.x | Migrate to 6.1(5), 7.1(3), or 7.1(5) using Uinified Communications Manager Data Migration Assistant (DMA) Check the Software Compatibility Matrix for the intermediate release to find the supported upgrade path from your current release, or see the "Supported Upgrade
                                          Paths To/From Table" at the link above. | PCD Migration to 12.x |
| 5.1(2) 5.1(3) 6.0(x) 6.1(1) 6.1(2) 6.1(3) 6.1(4) | Direct Upgrade to 6.1(5) or 7.1(3) | PCD Migration to 12.x |
| 7.0(1) 7.1(2) | 7.1(3), 7.1(5), 8.0(x), 8.5(1), or 8.6(2) | PCD Migration to 12.x |
| Cisco Unified Presence Releases |
| 8.0(x) | Direct Upgrade to 8.5(4) | PCD Migration to 12.0(1) |
| Uinified Communications Manager Business Edition Releases |
| Business Edition 3000 (BE3000) | Upgrades and migrations to Unified Communications Manager Release 12.x are not supported for these deployments. We recommend that you perform a fresh installation for upgrades from
                                          these products to the current Unified Communications Manager release. |
| Business Edition 5000 (BE5000) |

| Step 1 | Refer to the upgrade documentation for the intermediate release and follow the instructions to upgrade your system. For Unified Communications Manager upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . For IM and Presence Service (formerly Cisco Unified Presence) upgrade documentation, see http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-guides-list.html . |
|---|---|
| Step 2 | Refer to the Cisco Prime Collaboration Deployment Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html and follow the instructions to perform a PCD migration to the current release. |