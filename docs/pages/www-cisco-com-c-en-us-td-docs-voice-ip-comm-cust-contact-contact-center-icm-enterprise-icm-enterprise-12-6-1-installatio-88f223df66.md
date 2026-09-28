---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-88f223df66
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_12_6_1-install_upgrade_guide/ucce_b_12_6_1-install_upgrade_guide_chapter_01011.html
retrieved_at: 2026-08-16T20:01:35.372455+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Uninstallation

## Chapter: Uninstallation

# Uninstallation

## Uninstallation of Unified ICM/CCE base version 12.5(1)

Uninstallation of Unified ICM/CCE base of 12.5(1) is not supported for Unified CCE components that are deployed on Windows Server using the ICM-CCE-Installer. However, support
                           for uninstallation and re-installation of client installer packages like Administration Client and Internet Script Editor
                           continues.

## Prerequisite for Uninstallation of CCE 12.6(1) Minor Release

If you have enabled the optional feature Outbound Option High Availability, you must disable it before you uninstall Unified ICM 12.6(1) . From Unified CCE Web Setup, choose Component Management > Loggers . Select a logger that is enabled for High Availability, and click Next until the Additional Options page appears. Uncheck the Enable High Availability check box. Perform this action for each logger enabled for Outbound Option High Availability.

If you are planning to roll back to previous version of CCE Release 12.6(1) , do the following:

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

### Uninstall Methods

When you uninstall Unified CCE Release 12.6(1) , you must choose one of
                              			two methods of uninstallation:

Temporary - leaves the schema unmodified

Permanent - reverts the database schema to the previous schema version

The option to temporarily or permanently uninstall Unified CCE Release 12.6(1) appears only when you
                              			try to perform this task on a machine that is running the following components:

Logger

AW only

HDS

AW-HDS

### Temporary Uninstallation

In a temporary uninstallation, the schema that was updated during the upgrade process does not
                              revert to previous version of Unified CCE Release 12.6(1) . Use this method of
                              uninstallation when you want to rerun the Unified CCE Release 12.6(1) installer to fix initial
                              installation issues. This method is also useful when you want to upgrade to a future
                              maintenance or minor release.

The Logger, AW, and HDS components check the version table in the ICM database schema for their corresponding schema version.
                                          If the versions of the schema and the executable do not match, the system generates an error message and the services are
                                          shut down. This error is captured in the component logs.

### Permanent
                           	 Uninstallation

In permanent uninstallation, both the application and the database schema change. Uninstallation
                              			will revert the system and the database to previous version of Unified CCE Release 12.6(1) .

A permanent uninstallation is necessary if you wish to revert to previous version of Unified CCE
                              			Release 12.6(1) .

Configuration data may change when you revert to previous version of Unified CCE Release 12.6(1) :

Use the data from the previous version of Unified CCE Release configuration database
                                          				or the virtual machine which you backed up before starting the upgrade process.

If you have used the ICMDBA tool to create an
                              			Outbound Option database on Logger Side B, you can manually delete the database after
                              			the uninstall by using SQL Server Management Studio (SSMS).

Important

If there are any database schema rollback errors encountered during permanent uninstall, the
                                          				database schema may be in a corrupted state. The state prevents CCE Logger /
                                          				Distributor services to start correctly due to schema mismatch. To recover from the
                                          				state, the ICMDBA tool can be used to recreate the Logger or HDS database that may
                                          				have failed.

Routing Scripts which has dynamic queues configured for skill group node will not be accessible
                                          				after permanent rollback to previous version of Unified CCE Release 12.6(1) .

### Uninstall Unified CCE 12.6(1)

Step 1

Log in to your system as a user with administrative privileges.

Step 2

Choose Control Panel > Programs and Features > Cisco ICM Minor Release ICM 12.6(1) > Uninstall .

Step 3

Select either permanent or temporary uninstallation.

If you choose temporary uninstallation, follow the on-screen instructions to temporarily uninstall the application.

If you choose permanent uninstallation and you have enabled Outbound Option High Availability, a message appears informing
                                                you that you disable High Availability before you can proceed with the uninstallation. Disable High Availability, and then
                                                restart the upgrade uninstallation process.

Step 4

On the Database Schema Rollback window, specify if you want to proceed with the uninstallation.

Go to step 5

The uninstallation process cancels

Step 5

On the confirmation window, click Yes .

Step 6

(Optional) On the Installation Messages window, click Next .

Post Installation Window specifies if any service is set to manual. A pop-up window displays a notification that some services
                                             were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system operate
                                             properly after uninstalling Unified CCE 12.6(1) . Then, set the Unified ICM services that were changed during the uninstallation back to their original setting (Automatic).

Step 7

At the prompt, restart the machine.

Before you uninstall, ensure to set ECDSA enabled registry to false, and re-boot the box. Once the re-boot is complete, check the registry and set it to "false".

The ECDSA registry path is HKLM\SOFTWARE\WOW6432Node\Cisco Systems, Inc.\ICM\Cisco SSL Configuration

| Note | The option to roll back to previous versions is only available with minor and maintenance
                                    releases. |
|---|---|

| Note | Uninstallation of CCE 12.6(1) patch will not uninstall OpenJDK. |
|---|---|

| Note | You don't need to reimport the certificates if you are rolling back to CCE 12.5(1a) or 12.6(1). Also, if you have already
                                    installed ES55 (mandatory OpenJDK ES), you don't need to reimport the certificate when you roll back to CCE 12.5(1). |
|---|---|

| Note | The Logger, AW, and HDS components check the version table in the ICM database schema for their corresponding schema version.
                                          If the versions of the schema and the executable do not match, the system generates an error message and the services are
                                          shut down. This error is captured in the component logs. |
|---|---|

| Note | Configuration data may change when you revert to previous version of Unified CCE Release 12.6(1) : Use the data from the previous version of Unified CCE Release configuration database
                                          				or the virtual machine which you backed up before starting the upgrade process. |
|---|---|

| Important | If there are any database schema rollback errors encountered during permanent uninstall, the
                                          				database schema may be in a corrupted state. The state prevents CCE Logger /
                                          				Distributor services to start correctly due to schema mismatch. To recover from the
                                          				state, the ICMDBA tool can be used to recreate the Logger or HDS database that may
                                          				have failed. |
|---|---|

| Note | Routing Scripts which has dynamic queues configured for skill group node will not be accessible
                                          				after permanent rollback to previous version of Unified CCE Release 12.6(1) . |
|---|---|

| Step 1 | Log in to your system as a user with administrative privileges. |
|---|---|
| Step 2 | Choose Control Panel > Programs and Features > Cisco ICM Minor Release ICM 12.6(1) > Uninstall . The InstallShield Wizard launches. |
| Step 3 | Select either permanent or temporary uninstallation. If you choose temporary uninstallation, follow the on-screen instructions to temporarily uninstall the application. If you choose permanent uninstallation and you have enabled Outbound Option High Availability, a message appears informing
                                                you that you disable High Availability before you can proceed with the uninstallation. Disable High Availability, and then
                                                restart the upgrade uninstallation process. |
| Step 4 | On the Database Schema Rollback window, specify if you want to proceed with the uninstallation. Option Action Yes Go to step 5 No The uninstallation process cancels | Option | Action | Yes | Go to step 5 | No | The uninstallation process cancels |
| Option | Action |
| Yes | Go to step 5 |
| No | The uninstallation process cancels |
| Step 5 | On the confirmation window, click Yes . |
| Step 6 | (Optional) On the Installation Messages window, click Next . Post Installation Window specifies if any service is set to manual. A pop-up window displays a notification that some services
                                             were automatically changed to manual as part of the uninstallation. Make sure that both A and B sides of your system operate
                                             properly after uninstalling Unified CCE 12.6(1) . Then, set the Unified ICM services that were changed during the uninstallation back to their original setting (Automatic). |
| Step 7 | At the prompt, restart the machine. |

| Option | Action |
|---|---|
| Yes | Go to step 5 |
| No | The uninstallation process cancels |

| Note | Before you uninstall, ensure to set ECDSA enabled registry to false, and re-boot the box. Once the re-boot is complete, check the registry and set it to "false". The ECDSA registry path is HKLM\SOFTWARE\WOW6432Node\Cisco Systems, Inc.\ICM\Cisco SSL Configuration |
|---|---|