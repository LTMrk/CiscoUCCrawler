---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-install-upgrade-guide-hcs-cc-b-ins-2211472cb4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Install_Upgrade_Guide/hcs-cc_b_installing-and-upgrading-guide_12_5/hcs-cc_b_installing-and-upgrading-guide-for_chapter_0110.html
retrieved_at: 2026-08-22T00:12:32.725802+00:00
---

Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

# Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

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