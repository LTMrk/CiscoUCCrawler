---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-6f20451a11
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_12_5_Install_upgrade_guide_ucce/ucce_b_cisco-unified-contact-center-enterprise12_5_chapter_01011.html
retrieved_at: 2026-08-16T19:55:38.461055+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 3, 2020

Chapter: Uninstallation

## Chapter: Uninstallation

- Uninstallation

- Uninstallation of Unified ICM/CCE base version 12.5(1)

- Uninstall Unified CCE Maintenance Release 12.5(2)

# Uninstallation

## Uninstallation of Unified ICM/CCE base version 12.5(1)

Uninstallation of Unified ICM/CCE base of 12.5(1) is not supported for Unified CCE components that are deployed on Windows Server using the ICM-CCE-Installer. However, support
                           for uninstallation and re-installation of client installer packages like Administration Client and Internet Script Editor
                           continues.

## Uninstall Unified CCE Maintenance Release 12.5(2)

Step 1

Log in to your system as a user with administrative privileges.

Step 2

Choose Control Panel > Programs and Features > Cisco ICM Maintenance Release ICM 12.5(2) > Uninstall .

Step 3

On the confirmation window, click Yes .

Step 4

(Optional) On the Installation Messages window, click Next .

Post installation window specifies if any service is set to manual then a pop-up window displays a notification that some
                                          services were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system
                                          operate properly after uninstalling Unified CCE Release 12.5(2). Then, set the ICM services that were changed during the uninstallation
                                          back to their original setting (Automatic).

Step 5

At the prompt, restart the machine.

| Note | The option to roll back to previous versions is only available with minor and maintenance
                                    releases. |
|---|---|

| Step 1 | Log in to your system as a user with administrative privileges. |
|---|---|
| Step 2 | Choose Control Panel > Programs and Features > Cisco ICM Maintenance Release ICM 12.5(2) > Uninstall . The InstallShield Wizard launches. |
| Step 3 | On the confirmation window, click Yes . |
| Step 4 | (Optional) On the Installation Messages window, click Next . Post installation window specifies if any service is set to manual then a pop-up window displays a notification that some
                                          services were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system
                                          operate properly after uninstalling Unified CCE Release 12.5(2). Then, set the ICM services that were changed during the uninstallation
                                          back to their original setting (Automatic). |
| Step 5 | At the prompt, restart the machine. The Unified CCE Maintenance Release 12.5(2) application is uninstalled from your machine. |