---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-installatio-1e852f5676
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/installation/guide/ucce_b_install_upgrade_guide_1262/ucce_b_12_6_1-install_upgrade_guide_chapter_01011.html
retrieved_at: 2026-08-16T20:00:09.461120+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Uninstallation

## Chapter: Uninstallation

# Uninstallation

## Uninstallation of Unified ICM/CCE base version 12.5(1)

Uninstallation of Unified ICM/CCE base of 12.5(1) is not supported for Unified CCE components that are deployed on Windows Server using the ICM-CCE-Installer. However, support
                           for uninstallation and re-installation of client installer packages like Administration Client and Internet Script Editor
                           continues.

## Prerequisite for Uninstallation of CCE 12.6(2) Maintenance Release

If you have enabled the optional feature Outbound Option High Availability, you must disable it before you uninstall Unified ICM 12.6(2) . From Unified CCE Web Setup, choose Component Management > Loggers . Select a logger that is enabled for High Availability, and click Next until the Additional Options page appears. Uncheck the Enable High Availability check box. Perform this action for each logger enabled for Outbound Option High Availability.

If you are planning to roll back to previous version of CCE Release 12.6(2) , do the following:

```
keytool -export -keystore <ICM install Dir>\ssl\cacerts -alias <alias of the component> -file <filepath>.cer
```

Enter the truststore password when prompted.

After the roll back, do the following:

```
keytool -import -keystore <Oracle/OpenJDK JRE path>\lib\security\cacerts -file <filepath>.cer -alias <alias>
```

Enter the keystore password when prompted.

Enter yes when prompted to trust the certificate.

### Uninstall Unified CCE 12.6(2)

Step 1

Log in to your system as a user with administrative privileges.

Step 2

Choose Control Panel > Programs and Features > Cisco ICM Maintenance Release ICM 12.6(2) > Uninstall .

Step 3

On the confirmation window, click Yes .

Step 4

(Optional) On the Installation Messages window, click Next .

Post Installation Window specifies if any service is set to manual. A pop-up window displays a notification that some services
                                             were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system operate
                                             properly after uninstalling Unified CCE 12.6(2) . Then, set the Unified ICM services that were changed during the uninstallation back to their original setting (Automatic).

Step 5

At the prompt, restart the machine.

Before you uninstall, ensure to set ECDSA enabled registry to false, and re-boot the box. Once the re-boot is complete, check the registry and set it to "false".

The ECDSA registry path is HKLM\SOFTWARE\WOW6432Node\Cisco Systems, Inc.\ICM\Cisco SSL Configuration

| Note | The option to roll back to previous versions is only available with minor and maintenance
                                    releases. |
|---|---|

| Note | You don't need to reimport the certificates if you are rolling back to CCE 12.5(1a) or 12.6(1). Also, if you have already
                                    installed ES55 (mandatory OpenJDK ES), you don't need to reimport the certificate when you roll back to CCE 12.5(1). |
|---|---|

| Step 1 | Log in to your system as a user with administrative privileges. |
|---|---|
| Step 2 | Choose Control Panel > Programs and Features > Cisco ICM Maintenance Release ICM 12.6(2) > Uninstall . The InstallShield Wizard launches. |
| Step 3 | On the confirmation window, click Yes . |
| Step 4 | (Optional) On the Installation Messages window, click Next . Post Installation Window specifies if any service is set to manual. A pop-up window displays a notification that some services
                                             were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system operate
                                             properly after uninstalling Unified CCE 12.6(2) . Then, set the Unified ICM services that were changed during the uninstallation back to their original setting (Automatic). |
| Step 5 | At the prompt, restart the machine. |

| Note | Before you uninstall, ensure to set ECDSA enabled registry to false, and re-boot the box. Once the re-boot is complete, check the registry and set it to "false". The ECDSA registry path is HKLM\SOFTWARE\WOW6432Node\Cisco Systems, Inc.\ICM\Cisco SSL Configuration |
|---|---|